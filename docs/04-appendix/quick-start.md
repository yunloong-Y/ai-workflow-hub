# 快速上手与选型指南

[返回首页](../../README.md) · [English](./quick-start.en.md) · [全景对比](../01-landscape/overview.md)

---

## 一、我该选哪个框架？

| 你的诉求 | 推荐框架 | 理由 |
|---|---|---|
| 想先把需求想清楚，再让 AI 写代码 | **Spec Kit** | SDD 六步法，`converge` 保证不偏离规格 |
| 项目大小不一，想要流程能伸缩 | **BMAD Method** | 规模自适应，小改动直达构建 |
| 企业级、要审计与合规 | **AI-DLC** | 5 阶段 33 步、134 事件审计、审批门 |
| 想快速组建一支 AI"虚拟团队" | **gstack** | 23 个意见鲜明的角色工具 |
| 担心 AI 跳步骤、漏测试、泄露密钥 | **Agentic OS** | 机器强制门禁 + git hook + CI |
| 想要一套完整、可融合、中英双语的体系 | **本仓库统一框架** | 融合以上全部 + 自有闭环保障 |

> 这些框架并不互斥。本仓库的统一框架按阶段可插拔，你可以混搭：用 Spec Kit 写规格，用 gstack 角色分工，用 Agentic OS 做门禁，用 AI-DLC 做审计。

---

## 二、三条起步路径

### 路径 A：快速体验（30 分钟）

1. 读 [全景对比](../01-landscape/overview.md) 建立整体认知。
2. 选一个框架，按其官方 Quick Start 安装（见各项目 README）。
3. 跑一遍它的最小流程（如 Spec Kit 的 `/specify → /plan → /tasks → /implement`）。

### 路径 B：落地一套团队流程（1–2 周）

1. **G0 治理基线**：用 [质量门禁](./../02-unified-framework/quality-gates.md) 定义门禁，用 [角色定义](../02-unified-framework/agent-roles.md) 明确分工。
2. 按 [统一工作流](../02-unified-framework/unified-workflow.md) 逐阶段配置产出物模板。
3. 把可自动化门禁（凭证扫描、覆盖率、阶段证据）接进 git hook + CI。
4. 接入 [闭环落地体系](../03-user-system/closed-loop-system.md) 的 ID 溯源、异常处理、监控告警。

### 路径 C：企业级治理（持续）

1. 采用 AI-DLC 的 5 阶段 33 步 + 134 事件审计。
2. 叠加 Agentic OS 的机器强制门禁。
3. 用自有体系的"健康度仪表板"持续监控流程健康度。
4. 通过 G10 反馈迭代 + 动态知识库形成组织级闭环。

---

## 三、各框架安装速查

| 框架 | 安装命令（摘要） | 前置 |
|---|---|---|
| Spec Kit | `uv tool install specify-cli && specify init my-project --integration copilot` | Python 3.11+、uv |
| BMAD (v6.12) | `npx bmad-method install` | Node.js 20.12+、Python 3.10+ |
| BMAD (v7 preview) | `npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'` | Node.js、npm、Git |
| AI-DLC | `curl -fsSL .../install.sh \| sh` 然后 `aidlc config --harness claude` | macOS/Linux/WSL 或 Windows |
| gstack | 见项目 README | Claude Code |
| Agentic OS | 见项目 `docs/INSTALL.md`（安装后默认不启用，需手动开启 hook/CI） | Python |

> ⚠️ 具体命令以各项目官方 README 为准，版本可能变化。

---

## 四、常见误区

| 误区 | 正解 |
|---|---|
| 让所有改动都走完整 10 阶段 | 按规模裁剪：小改动走轻量路径（G6→G9） |
| 把 rules 文件当门禁 | rules 会被 AI 忽视，真门禁要靠 git hook + CI |
| 只看"测试通过"字样 | 要验证测试真实运行（退出码 + 代码指纹） |
| 规格写完就扔 | 规格要贯穿到实现与收敛，最后还要被 G10 反馈修订 |
| 闭环止于上线 | 上线只是中点，反馈回到 G3 才是闭环 |

---

## 五、贡献

欢迎补充新的框架解析、模板、术语或最佳实践。提交前请确认：
- 内容中英双语齐全；
- 引用第三方项目注明出处；
- 遵循原文的体系内容不做擅自推断（尤其自有体系部分）。
