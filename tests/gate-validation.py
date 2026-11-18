#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gate-validation.py · Agentic OS 风格「机器强制」门禁校验器
=====================================================================

用途
----
在统一工作流的 G8 测试门禁 / G9 发布门禁处，用机器可重复执行的方式校验：

  1. 工作轨迹 (work trail) 的每个必需阶段是否有证据记录 (evidence)
  2. 测试覆盖率 (coverage) 是否达标（默认 >= 80%）
  3. 代码是否存在凭证泄露 (credential leak)
  4. 测试运行指纹 (test-run fingerprint) 是否与当前代码匹配

退出码语义（与 docs/02-unified-framework/quality-gates.md 对齐）
---------------------------------------------------------------
  0 = 通过 (PASS)      —— 门禁放行
  1 = 错误 (FAIL)      —— 阻断放行，必须修复
  2 = 警告 (WARN)      —— 放行但需关注（覆盖率贴线、证据时间戳缺失等）

设计原则
--------
  * 纯标准库：argparse / json / re / pathlib / sys / hashlib，无第三方依赖
  * 可机器强制：退出码可被 git pre-commit hook 与 CI 直接消费
  * 证据留痕：每次校验输出可粘贴进审计轨迹 (audit trail)

用法示例
--------
  python3 gate-validation.py --demo
  python3 gate-validation.py trail     --file work-trail.json
  python3 gate-validation.py coverage  --file coverage.json --threshold 80
  python3 gate-validation.py credentials --path ./src
  python3 gate-validation.py fingerprint --code app.py --expected <sha256>
  python3 gate-validation.py all --trail work-trail.json --coverage coverage.json \
                                 --path ./src --code app.py --expected <sha256>
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 常量区（Constants）
# ---------------------------------------------------------------------------

EXIT_PASS = 0    # 通过
EXIT_ERROR = 1   # 错误 / 失败
EXIT_WARN = 2    # 警告

DEFAULT_THRESHOLD = 80.0          # 覆盖率门禁门槛：>= 80%
WARN_BAND = 5.0                   # 贴线区间：[80, 85) 记为警告

# Agentic OS 五步工作流必需阶段（plan → build → review → test → ship）
REQUIRED_STAGES = ("plan", "build", "review", "test", "ship")

# 凭证泄露正则（简化版，演示用；生产环境应接入专用扫描器）
CREDENTIAL_PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private Key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Generic API Key": re.compile(
        r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"
    ),
    "Slack Token": re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}"),
    "Hardcoded Password": re.compile(
        r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}

# 凭证扫描涉及的文件类型 / 排除目录
SCAN_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".env",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".sh",
}
SCAN_EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}


# ---------------------------------------------------------------------------
# 打印辅助（Reporting helpers）
# ---------------------------------------------------------------------------

def badge(status):
    """把退出码映射成文本徽章（不用 emoji，便于粘贴进 Markdown / CI 日志）。"""
    return {EXIT_PASS: "[PASS]", EXIT_WARN: "[WARN]", EXIT_ERROR: "[FAIL]"}[status]


def rule(char="─", width=72):
    return char * width


def print_banner(title, subtitle=""):
    print(rule("═"))
    print("  " + title)
    if subtitle:
        print("  " + subtitle)
    print(rule("═"))


def print_result(status, label="判定结果"):
    print(rule("─"))
    print(f"  {label}: {badge(status)}  (退出码 {status})")
    print(rule("─"))


def worst_status(statuses):
    """取最严重的状态：ERROR > WARN > PASS。"""
    if EXIT_ERROR in statuses:
        return EXIT_ERROR
    if EXIT_WARN in statuses:
        return EXIT_WARN
    return EXIT_PASS


def load_json(path):
    """读取 JSON 文件；失败时返回 None 并打印错误。"""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"  [ERROR] 无法读取 JSON 文件 {path}: {exc}")
        return None


# ---------------------------------------------------------------------------
# 检查项 1：工作轨迹证据（Work trail evidence）
# ---------------------------------------------------------------------------

def check_trail(trail_data):
    """
    校验每个必需阶段是否有非空证据记录。
    返回 (status, findings, errors, warnings)。
      findings: [(stage, evidence, timestamp)]
    """
    stages = trail_data.get("stages", []) if isinstance(trail_data, dict) else trail_data
    by_name = {}
    for record in stages:
        name = record.get("stage") or record.get("name")
        if name:
            by_name[name] = record

    findings, errors, warnings = [], [], []
    for stage in REQUIRED_STAGES:
        record = by_name.get(stage)
        if record is None:
            errors.append(f"阶段 '{stage}' 无任何轨迹记录 (missing trail)")
            continue
        evidence = record.get("evidence") or record.get("artifact") or ""
        if not str(evidence).strip():
            errors.append(f"阶段 '{stage}' 缺少证据记录 (empty evidence)")
            continue
        timestamp = record.get("timestamp", "")
        if not timestamp:
            warnings.append(f"阶段 '{stage}' 证据存在但缺少 timestamp")
        findings.append((stage, str(evidence), timestamp or "—"))

    status = EXIT_ERROR if errors else (EXIT_WARN if warnings else EXIT_PASS)
    return status, findings, errors, warnings


# ---------------------------------------------------------------------------
# 检查项 2：测试覆盖率（Coverage）
# ---------------------------------------------------------------------------

def compute_coverage(coverage_data):
    """
    按 lines.total 加权计算整体覆盖率。
    返回 (line_pct, branch_pct, func_pct, rows)。
      rows: [(module, line_pct, branch_pct, func_pct, covered, total)]
    """
    modules = coverage_data.get("modules", []) if isinstance(coverage_data, dict) else coverage_data
    sum_lc = sum_lt = sum_bc = sum_bt = sum_fc = sum_ft = 0
    rows = []
    for module in modules:
        lines = module.get("lines", {})
        branches = module.get("branches", {})
        functions = module.get("functions", {})
        lc, lt = lines.get("covered", 0), lines.get("total", 0)
        bc, bt = branches.get("covered", 0), branches.get("total", 0)
        fc, ft = functions.get("covered", 0), functions.get("total", 0)
        sum_lc += lc; sum_lt += lt
        sum_bc += bc; sum_bt += bt
        sum_fc += fc; sum_ft += ft
        rows.append((
            module.get("name", "<unnamed>"),
            100.0 * lc / lt if lt else 0.0,
            100.0 * bc / bt if bt else 0.0,
            100.0 * fc / ft if ft else 0.0,
            lc, lt,
        ))
    line_pct = 100.0 * sum_lc / sum_lt if sum_lt else 0.0
    branch_pct = 100.0 * sum_bc / sum_bt if sum_bt else 0.0
    func_pct = 100.0 * sum_fc / sum_ft if sum_ft else 0.0
    return line_pct, branch_pct, func_pct, rows


def check_coverage(coverage_data, threshold=DEFAULT_THRESHOLD):
    """判定覆盖率门禁：<threshold 为 FAIL，贴线 [threshold, threshold+5) 为 WARN。"""
    line_pct, branch_pct, func_pct, rows = compute_coverage(coverage_data)
    if line_pct < threshold:
        status = EXIT_ERROR
    elif line_pct < threshold + WARN_BAND:
        status = EXIT_WARN
    else:
        status = EXIT_PASS
    return status, line_pct, branch_pct, func_pct, rows, threshold


# ---------------------------------------------------------------------------
# 检查项 3：凭证泄露扫描（Credential scan）
# ---------------------------------------------------------------------------

def scan_text(text, source="<text>"):
    """扫描一段文本中的凭证泄露，返回命中列表 [(source, lineno, label, snippet)]。"""
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for label, pattern in CREDENTIAL_PATTERNS.items():
            if pattern.search(line):
                hits.append((source, lineno, label, line.strip()[:72]))
                break  # 同一行只记一条，避免重复刷屏
    return hits


def scan_path(path):
    """扫描目录或文件，返回 (hits, scanned_file_count)。"""
    target = Path(path)
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = [
            f for f in target.rglob("*")
            if f.is_file()
            and f.suffix in SCAN_EXTENSIONS
            and not (set(f.parts) & SCAN_EXCLUDE_DIRS)
        ]
    else:
        files = []
    hits = []
    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        hits.extend(scan_text(text, str(file_path)))
    return hits, len(files)


def check_credentials(path):
    hits, file_count = scan_path(path)
    status = EXIT_ERROR if hits else EXIT_PASS
    return status, hits, file_count


# ---------------------------------------------------------------------------
# 检查项 4：测试运行指纹（Test-run fingerprint）
# ---------------------------------------------------------------------------

def file_fingerprint(path):
    """计算文件的 SHA256 指纹（用于「测试后代码是否被改动」校验）。"""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def text_fingerprint(text):
    """计算字符串的 SHA256 指纹（demo 用）。"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compare_fingerprint(expected, actual):
    """比对期望指纹与实际指纹；不匹配意味着测试后代码被改动。"""
    matched = expected.strip().lower() == actual.strip().lower()
    status = EXIT_PASS if matched else EXIT_ERROR
    return status, expected, actual, matched


# ---------------------------------------------------------------------------
# 打印各个检查报告（Report renderers）
# ---------------------------------------------------------------------------

def report_trail(status, findings, errors, warnings):
    print("  [1/4] 工作轨迹证据 (Work Trail) " + badge(status))
    print(f"  {'STAGE':<10}{'EVIDENCE':<48}{'TIMESTAMP'}")
    for stage, evidence, timestamp in findings:
        print(f"  {stage:<10}{evidence[:46]:<48}{timestamp}")
    for warning in warnings:
        print("  [WARN] " + warning)
    for error in errors:
        print("  [FAIL] " + error)


def report_coverage(status, line_pct, branch_pct, func_pct, rows, threshold):
    print(f"  [2/4] 测试覆盖率 (Coverage, threshold {threshold:.1f}%) " + badge(status))
    print(f"  {'MODULE':<32}{'LINES':>9}{'BRANCH':>9}{'FUNC':>9}")
    for module, lp, bp, fp, _covered, _total in rows:
        print(f"  {module:<32}{lp:>8.1f}%{bp:>8.1f}%{fp:>8.1f}%")
    print(f"  {'OVERALL (weighted)':<32}{line_pct:>8.1f}%{branch_pct:>8.1f}%{func_pct:>8.1f}%")
    if line_pct < threshold:
        print(f"  [FAIL] 整体覆盖率 {line_pct:.1f}% < 门槛 {threshold:.1f}%")
    elif line_pct < threshold + WARN_BAND:
        print(f"  [WARN] 覆盖率 {line_pct:.1f}% 贴线通过（低于 {threshold + WARN_BAND:.1f}% 舒适区）")
    else:
        print(f"  [PASS] 覆盖率 {line_pct:.1f}% >= 门槛 {threshold:.1f}%")


def report_credentials(status, hits, file_count):
    print("  [3/4] 凭证泄露扫描 (Credential Scan) " + badge(status))
    print(f"  已扫描 {file_count} 个文件，命中 {len(hits)} 处")
    for source, lineno, label, snippet in hits:
        print(f"  [HIT]  {source}:{lineno}  {label}  | {snippet}")
    if not hits:
        print("  [PASS] 未发现凭证泄露")


def report_fingerprint(status, expected, actual, matched):
    print("  [4/4] 测试运行指纹 (Test-run Fingerprint) " + badge(status))
    print(f"  expected: {expected}")
    print(f"  actual  : {actual}")
    if matched:
        print("  [PASS] 指纹一致：测试后代码未变更")
    else:
        print("  [FAIL] 指纹不一致：测试后代码被改动 (code changed after test run)")


# ---------------------------------------------------------------------------
# 子命令实现（Subcommand handlers）
# ---------------------------------------------------------------------------

def cmd_trail(args):
    data = load_json(args.file)
    if data is None:
        return EXIT_ERROR
    print_banner("GATE VALIDATOR · 工作轨迹校验", f"文件: {args.file}")
    status, findings, errors, warnings = check_trail(data)
    report_trail(status, findings, errors, warnings)
    print_result(status, "轨迹门禁判定")
    return status


def cmd_coverage(args):
    data = load_json(args.file)
    if data is None:
        return EXIT_ERROR
    print_banner("GATE VALIDATOR · 覆盖率校验", f"文件: {args.file}  门槛: {args.threshold}%")
    status, line_pct, branch_pct, func_pct, rows, threshold = check_coverage(data, args.threshold)
    report_coverage(status, line_pct, branch_pct, func_pct, rows, threshold)
    print_result(status, "覆盖率门禁判定")
    return status


def cmd_credentials(args):
    print_banner("GATE VALIDATOR · 凭证泄露扫描", f"路径: {args.path}")
    status, hits, file_count = check_credentials(args.path)
    report_credentials(status, hits, file_count)
    print_result(status, "凭证扫描判定")
    return status


def cmd_fingerprint(args):
    print_banner("GATE VALIDATOR · 测试运行指纹校验", f"代码: {args.code}")
    try:
        actual = file_fingerprint(args.code)
    except OSError as exc:
        print(f"  [ERROR] 无法读取代码文件 {args.code}: {exc}")
        return EXIT_ERROR
    status, expected, actual, matched = compare_fingerprint(args.expected, actual)
    report_fingerprint(status, expected, actual, matched)
    print_result(status, "指纹门禁判定")
    return status


def cmd_all(args):
    """组合全部四项校验，给出综合判定。缺哪份输入就跳过哪项并记为警告。"""
    print_banner("GATE VALIDATOR · 全门禁综合校验", "G8 测试验证 + G9 发布前检查")
    statuses = []

    if args.trail:
        data = load_json(args.trail)
        if data is None:
            statuses.append(EXIT_ERROR)
        else:
            s, findings, errors, warnings = check_trail(data)
            statuses.append(s)
            report_trail(s, findings, errors, warnings)
    else:
        print("  [1/4] 工作轨迹证据 ... [SKIP] 未提供 --trail")
        statuses.append(EXIT_WARN)

    print()

    if args.coverage:
        data = load_json(args.coverage)
        if data is None:
            statuses.append(EXIT_ERROR)
        else:
            s, lp, bp, fp, rows, t = check_coverage(data, args.threshold)
            statuses.append(s)
            report_coverage(s, lp, bp, fp, rows, t)
    else:
        print("  [2/4] 测试覆盖率 ... [SKIP] 未提供 --coverage")
        statuses.append(EXIT_WARN)

    print()

    if args.path:
        s, hits, count = check_credentials(args.path)
        statuses.append(s)
        report_credentials(s, hits, count)
    else:
        print("  [3/4] 凭证泄露扫描 ... [SKIP] 未提供 --path")
        statuses.append(EXIT_WARN)

    print()

    if args.code and args.expected:
        try:
            actual = file_fingerprint(args.code)
            s, exp, act, matched = compare_fingerprint(args.expected, actual)
            statuses.append(s)
            report_fingerprint(s, exp, act, matched)
        except OSError as exc:
            print(f"  [ERROR] 无法读取代码文件 {args.code}: {exc}")
            statuses.append(EXIT_ERROR)
    else:
        print("  [4/4] 测试运行指纹 ... [SKIP] 未提供 --code / --expected")
        statuses.append(EXIT_WARN)

    final_status = worst_status(statuses)
    print_result(final_status, "综合门禁判定")
    return final_status


# ---------------------------------------------------------------------------
# Demo 模式（内置数据，讲一个「76% 未通过 → 补测 → 89% 通过」的故事）
# ---------------------------------------------------------------------------

DEMO_TRAIL_BEFORE = {
    "project": "OrderHub",
    "gate": "G8",
    "stages": [
        {"stage": "plan", "evidence": "plan.md (RewritePlan) @v1.4.0", "timestamp": "2026-11-18T09:12:00Z"},
        {"stage": "build", "evidence": "PR #218 / commit 9f3c1ab", "timestamp": "2026-11-18T10:40:00Z"},
        {"stage": "review", "evidence": "review-report.md (2 findings resolved)", "timestamp": "2026-11-18T11:05:00Z"},
        {"stage": "test", "evidence": "test-run.json (pytest exit=0, 214 passed)", "timestamp": "2026-11-18T11:30:00Z"},
        # ship 阶段缺证据 —— 故意留空，演示门禁拦截
    ],
}

DEMO_TRAIL_AFTER = {
    "project": "OrderHub",
    "gate": "G8",
    "stages": DEMO_TRAIL_BEFORE["stages"] + [
        {"stage": "ship", "evidence": "release-record.md (dry-run ok) @4e8d2f1", "timestamp": "2026-11-18T13:48:00Z"},
    ],
}

# 补测前：加权覆盖率 611/800 = 76.4% (< 80% 门槛)
DEMO_COVERAGE_BEFORE = {
    "project": "OrderHub",
    "commit": "9f3c1ab",
    "modules": [
        {"name": "order/domain.py", "lines": {"covered": 184, "total": 220}, "branches": {"covered": 44, "total": 58}, "functions": {"covered": 28, "total": 32}},
        {"name": "payment/gateway.py", "lines": {"covered": 108, "total": 180}, "branches": {"covered": 21, "total": 48}, "functions": {"covered": 15, "total": 26}},
        {"name": "inventory/stock.py", "lines": {"covered": 105, "total": 120}, "branches": {"covered": 26, "total": 30}, "functions": {"covered": 18, "total": 20}},
        {"name": "api/order_routes.py", "lines": {"covered": 154, "total": 180}, "branches": {"covered": 33, "total": 40}, "functions": {"covered": 22, "total": 25}},
        {"name": "notification/notify.py", "lines": {"covered": 60, "total": 100}, "branches": {"covered": 12, "total": 24}, "functions": {"covered": 9, "total": 18}},
    ],
}

# 补测后：加权覆盖率 712/800 = 89.0% (>= 80% 门槛)
DEMO_COVERAGE_AFTER = {
    "project": "OrderHub",
    "commit": "4e8d2f1",
    "modules": [
        {"name": "order/domain.py", "lines": {"covered": 190, "total": 220}, "branches": {"covered": 48, "total": 58}, "functions": {"covered": 30, "total": 32}},
        {"name": "payment/gateway.py", "lines": {"covered": 156, "total": 180}, "branches": {"covered": 40, "total": 48}, "functions": {"covered": 23, "total": 26}},
        {"name": "inventory/stock.py", "lines": {"covered": 110, "total": 120}, "branches": {"covered": 28, "total": 30}, "functions": {"covered": 19, "total": 20}},
        {"name": "api/order_routes.py", "lines": {"covered": 166, "total": 180}, "branches": {"covered": 37, "total": 40}, "functions": {"covered": 24, "total": 25}},
        {"name": "notification/notify.py", "lines": {"covered": 90, "total": 100}, "branches": {"covered": 21, "total": 24}, "functions": {"covered": 17, "total": 18}},
    ],
}

# 补测前的源码片段：含 3 处凭证泄露
DEMO_SOURCE_BEFORE = """\
# payment/gateway.py  (commit 9f3c1ab)
API_KEY = "AKIA1234567890ABCDEF"
def connect():
    api_key = "sk_live_51H8xY2eZvKYlo2C9qW3rTn"
    password = "sup3rS3cretPwd!"
    return api_key
"""

# 补测后的源码片段：改为环境变量 + 密钥管理，泄露清零
DEMO_SOURCE_AFTER = """\
# payment/gateway.py  (commit 4e8d2f1)
import os
API_KEY = os.environ["ORDERHUB_API_KEY"]
def connect():
    api_key = os.environ["ORDERHUB_API_KEY"]
    password = secret_manager.get("orderhub/payment")
    return api_key
"""

DEMO_CODE_TESTED = "orderhub-v1.4.0-source-at-test-time"
DEMO_CODE_EDITED = "orderhub-v1.4.0-source-edited-after-test"


def _demo_scenario(title, subtitle, trail, coverage, source, expected_fp, actual_fp, threshold):
    """运行一遍完整的四项校验，打印报告，返回综合状态。"""
    print()
    print(rule("▶", 1))
    print(f"  {title}")
    print(f"  {subtitle}")
    print(rule("─"))

    s_trail, findings, errors, warnings = check_trail(trail)
    report_trail(s_trail, findings, errors, warnings)
    print()

    s_cov, lp, bp, fp, rows, t = check_coverage(coverage, threshold)
    report_coverage(s_cov, lp, bp, fp, rows, t)
    print()

    hits = scan_text(source, "payment/gateway.py")
    s_cred = EXIT_ERROR if hits else EXIT_PASS
    report_credentials(s_cred, hits, 1)  # demo 中视为单个源码文件
    print()

    s_fp, exp, act, matched = compare_fingerprint(expected_fp, actual_fp)
    report_fingerprint(s_fp, exp, act, matched)
    print()

    final = worst_status([s_trail, s_cov, s_cred, s_fp])
    gate_text = {EXIT_PASS: "GATE PASSED", EXIT_WARN: "GATE PASSED (WITH WARNINGS)", EXIT_ERROR: "GATE FAILED"}[final]
    print(rule("─"))
    print(f"  场景判定: {gate_text}  (退出码 {final})")
    print(rule("─"))
    return final


def run_demo():
    """演示一个完整的门禁故事：首次校验失败 → 补测修复 → 重新校验通过。"""
    print_banner(
        "GATE VALIDATOR · DEMO · Agentic OS 机器强制门禁",
        "项目: OrderHub  |  门禁: G8 测试验证  |  门槛: 覆盖率 >= 80.0%",
    )
    print("  本演示内置样例数据，依次展示「补测前失败」与「补测后通过」两段校验。")

    before = _demo_scenario(
        "场景 A · 首次校验（补测前，commit 9f3c1ab）",
        "覆盖率 76.4% 未达标 + 缺 ship 证据 + 3 处凭证泄露 + 指纹不一致",
        DEMO_TRAIL_BEFORE,
        DEMO_COVERAGE_BEFORE,
        DEMO_SOURCE_BEFORE,
        text_fingerprint(DEMO_CODE_TESTED),
        text_fingerprint(DEMO_CODE_EDITED),
        DEFAULT_THRESHOLD,
    )

    after = _demo_scenario(
        "场景 B · 补测修复后重新校验（commit 4e8d2f1）",
        "覆盖率 89.0% 达标 + 证据齐全 + 凭证清零 + 指纹一致",
        DEMO_TRAIL_AFTER,
        DEMO_COVERAGE_AFTER,
        DEMO_SOURCE_AFTER,
        text_fingerprint(DEMO_CODE_TESTED),
        text_fingerprint(DEMO_CODE_TESTED),
        DEFAULT_THRESHOLD,
    )

    print()
    print_banner(
        "DEMO 完成",
        f"场景 A 退出码 = {before} (FAIL)  →  场景 B 退出码 = {after} (PASS)",
    )
    print("  门禁规则: 0=通过 / 1=错误 / 2=警告  —— 与 quality-gates.md 一致")
    print(rule("═"))
    return EXIT_PASS  # 演示流程本身成功完成


# ---------------------------------------------------------------------------
# CLI 入口（Argument parser）
# ---------------------------------------------------------------------------

EXAMPLES = """示例:
  python3 gate-validation.py --demo
  python3 gate-validation.py trail --file work-trail.json
  python3 gate-validation.py coverage --file coverage.json --threshold 80
  python3 gate-validation.py credentials --path ./src
  python3 gate-validation.py fingerprint --code app.py --expected <sha256>
  python3 gate-validation.py all --trail work-trail.json --coverage coverage.json \\
                                 --path ./src --code app.py --expected <sha256>

退出码: 0=通过  1=错误(阻断)  2=警告(放行但关注)
"""


def build_parser():
    parser = argparse.ArgumentParser(
        prog="gate-validation.py",
        description="Agentic OS 风格机器强制门禁校验器（覆盖率/证据/凭证/指纹）",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--demo", action="store_true", help="运行内置示例数据（76%%, fail → 89%%, pass）")
    subparsers = parser.add_subparsers(dest="command")

    p_trail = subparsers.add_parser("trail", help="校验工作轨迹每个阶段是否有证据")
    p_trail.add_argument("--file", "-f", required=True, help="work-trail.json 路径")
    p_trail.set_defaults(handler=cmd_trail)

    p_cov = subparsers.add_parser("coverage", help="校验测试覆盖率是否达标")
    p_cov.add_argument("--file", "-f", required=True, help="coverage.json 路径")
    p_cov.add_argument("--threshold", "-t", type=float, default=DEFAULT_THRESHOLD, help="覆盖率门槛（默认 80）")
    p_cov.set_defaults(handler=cmd_coverage)

    p_cred = subparsers.add_parser("credentials", help="扫描代码中的凭证泄露")
    p_cred.add_argument("--path", "-p", required=True, help="待扫描的文件或目录")
    p_cred.set_defaults(handler=cmd_credentials)

    p_fp = subparsers.add_parser("fingerprint", help="校验测试运行指纹是否匹配")
    p_fp.add_argument("--code", "-c", required=True, help="被测代码文件")
    p_fp.add_argument("--expected", "-e", required=True, help="测试运行时记录的期望 SHA256")
    p_fp.set_defaults(handler=cmd_fingerprint)

    p_all = subparsers.add_parser("all", help="运行全部四项校验并给出综合判定")
    p_all.add_argument("--trail", help="work-trail.json 路径")
    p_all.add_argument("--coverage", help="coverage.json 路径")
    p_all.add_argument("--path", help="凭证扫描路径")
    p_all.add_argument("--code", help="被测代码文件（配合 --expected）")
    p_all.add_argument("--expected", help="期望的测试运行指纹 SHA256")
    p_all.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help="覆盖率门槛（默认 80）")
    p_all.set_defaults(handler=cmd_all)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.demo:
        return run_demo()
    if getattr(args, "handler", None) is None:
        parser.print_help()
        return EXIT_WARN
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
