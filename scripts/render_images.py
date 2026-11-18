#!/usr/bin/env python3
"""
render_images.py — 把仓库所有 Markdown 里的 Mermaid 图块渲染成真实 PNG 图片。

- 使用公共 Kroki 服务 (https://kroki.io) 渲染，无需本地安装 Mermaid CLI。
- 输出目录：assets/，文件名与来源文档一一对应。
- 生成 manifest.json 供文档嵌入时引用。
"""
import re
import glob
import json
import subprocess
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
KROKI = "https://kroki.io/mermaid/png"


def render_block(code: str, out_path: str, retries: int = 3) -> bool:
    """把一个 Mermaid 块渲染成 PNG。成功返回 True。"""
    tmp = out_path + ".mmd"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(code)
    for attempt in range(1, retries + 1):
        try:
            r = subprocess.run(
                ["curl", "-s", "-X", "POST", "-H", "Content-Type: text/plain",
                 "--data-binary", f"@{tmp}", "--max-time", "60",
                 KROKI, "-o", out_path, "-w", "%{http_code}"],
                capture_output=True, text=True, timeout=75,
            )
            code_status = r.stdout.strip()
            if code_status == "200" and os.path.getsize(out_path) > 1000:
                os.unlink(tmp)
                return True
            print(f"    attempt {attempt}: http={code_status} size="
                  f"{os.path.getsize(out_path) if os.path.exists(out_path) else 0}")
        except Exception as e:
            print(f"    attempt {attempt}: exception {e}")
        time.sleep(2)
    if os.path.exists(tmp):
        os.unlink(tmp)
    return False


def main():
    os.makedirs(ASSETS, exist_ok=True)
    manifest = []
    md_files = sorted(
        f for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
        if "assets" not in f
    )
    total_blocks = 0
    ok = 0
    fail = []
    for f in md_files:
        rel = os.path.relpath(f, ROOT)
        txt = open(f, encoding="utf-8").read()
        blocks = list(re.finditer(r"```mermaid\s*\n(.*?)```", txt, re.S))
        if not blocks:
            continue
        # 文件名: docs-01-landscape-overview--1.png
        base = rel.replace("/", "-").replace(".md", "")
        for i, m in enumerate(blocks, 1):
            total_blocks += 1
            code = m.group(1)
            first = next((l.strip() for l in code.strip().split("\n") if l.strip()), "")
            dtype = first.split()[0] if first else "?"
            img_name = f"{base}--{i}.png"
            out = os.path.join(ASSETS, img_name)
            print(f"[{total_blocks:>2}] {dtype:<16} {img_name}")
            success = render_block(code, out)
            if success:
                ok += 1
                manifest.append({
                    "file": rel,
                    "index": i,
                    "type": dtype,
                    "image": f"assets/{img_name}",
                    "size": os.path.getsize(out),
                })
            else:
                fail.append(f"{rel} #{i} ({dtype})")

    with open(os.path.join(ASSETS, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\n完成: {ok}/{total_blocks} 渲染成功")
    if fail:
        print("失败:")
        for x in fail:
            print("  -", x)
    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main())
