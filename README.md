# AI Workflow Hub · 最全 AI 软件开发工作流全景与落地体系

> 一套**集大成、可落地、中英双语**的 AI 驱动软件开发工作流知识体系。
> 横向对标业界 5 大主流框架，纵向沉淀「需求 → 上线 → 反馈迭代」全流程闭环，
> 并融入一套经过优化升级的**全流程闭环落地体系**（ID 溯源 / 异常处理 / 质量门禁 / 监控告警 / 版本管理 / 知识库 / 变更流程）。

[English](./README.en.md) · [统一工作流框架](./docs/02-unified-framework/unified-workflow.md) · [闭环落地体系](./docs/03-user-system/closed-loop-system.md) · [全景对比](./docs/01-landscape/overview.md)

> 🆕 **有图有真相**：[架构设计图集](./architecture/README.md)（5 张 Mermaid 架构图）· [端到端实战案例](./cases/README.md)（OrderHub 全流程 + Hotfix）· [测试体系与可运行门禁校验器](./tests/README.md)

---

## 这是什么

这不是一个代码库，而是一套**方法论 + 工作流 + 角色 + 门禁 + 治理**的知识体系，回答一个核心问题：

> **当 AI Agent 参与软件开发的全生命周期时，人该是什么角色？每个阶段该怎么干、产出什么、何时放行？**

我们把业界最优秀的 5 个 AI 开发工作流框架逐一拆解、横向对比，取其精华，融合成一套**统一的 10 阶段工作流**；再叠加一套完整的**闭环落地保障体系**，让流程不仅"能对标"，更能"真落地"。

**三个设计目标：**

| 目标 | 说明 |
|---|---|
| 🎯 最全（Comprehensive） | 覆盖 5 大主流框架 + 1 套自有闭环体系，纵向全流程、横向全角色 |
| 🔗 可融合（Composable） | 统一框架按阶段可插拔，取用任一框架的 Skill / Agent / 模板均可 |
| 🛡️ 可落地（Enforceable） | 质量门禁 + 异常升级 + 监控告警 + 变更审批，让 AI 输出可验证、可审计 |

---

## 一、五大主流框架全景（对标）

| # | 项目 | Star | 一句话定位 | 核心贡献 | 许可证 |
|---|---|---:|---|---|---|
| 1 | [github/spec-kit](https://github.com/github/spec-kit) | ~150k | 规范驱动开发（SDD）工具包 | `/constitution → specify → plan → tasks → implement → converge` 六步法 + 可扩展的 Extension/Preset/Workflow | MIT |
| 2 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | ~55k | 敏捷 AI 驱动开发（AiDD） | 规模自适应流程（小改动直达构建，大项目深度规划）+ 产品/架构/UX/开发/测试多角色 | MIT |
| 3 | [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | ~6.1k | AI 驱动开发生命周期 | **5 阶段 33 步 + 14 Agent + 11 工作流画像 + 134 事件审计** | MIT-0 |
| 4 | [garrytan/gstack](https://github.com/garrytan/gstack) | ~142k | 角色化 Claude Code 工具集 | 23 个"意见鲜明"的角色工具（CEO / Designer / Eng Manager / Release Manager / Doc Engineer…） | MIT |
| 5 | [KbWen/agentic-os](https://github.com/KbWen/agentic-os) | ~240 | AI 编码 Agent 治理框架 | `plan → build → review → test → ship` 五步 + **机器强制的门禁/证据/审计轨迹** | MIT |

> 另含**灵感来源与参考基准**：[cilangzzz/software-dev-ai-workflow](https://github.com/cilangzzz/software-dev-ai-workflow)（~48★，8 阶段 + 8 大角色 + 27 通用 Skill + 质量门控 Gate 1-5），本项目在其"角色 Agent + 阶段编排"思路上做了体系化扩展。

> ⚠️ Star 数为 2026-11-18 抓取快照，会随时间变化。

📖 详细拆解见 [全景对比与逐项目解析](./docs/01-landscape/overview.md)

---

## 二、统一工作流框架（10 阶段）

融合五大框架后沉淀的主流程，纵向贯穿需求到运维：

```
G0 治理基线  →  G1 想法评估  →  G2 澄清启动  →  G3 规格需求  →  G4 计划架构
     ↓
G5 任务拆解  →  G6 构建实现  →  G7 代码审查  →  G8 测试验证  →  G9 发布交付
     ↓
G10 反馈迭代  ──────────────→ 回到 G3（需求落地反馈闭环）
```

每个阶段都定义了：**输入 → 活动 → 产出物 → 放行门禁 → 对应框架做法 → 角色**。

📖 完整定义见 [统一工作流框架](./docs/02-unified-framework/unified-workflow.md)

---

## 三、闭环落地保障体系（自有体系升级版）

源自《AI 产品全流程闭环落地体系设计（优化版）》，在七阶段标准化 SOP 之上，新增 **10 项优化点**，覆盖 15 项新旧流程对比：

| 模块 | 优化要点 | 状态 |
|---|---|---|
| ID 溯源可视化 | 新增 ID 流向箭头，展示全链路绑定 | ✅ |
| 异常处理机制 | 超时升级：48 小时未处理自动升级 | ✅ |
| 质量门禁 | 覆盖率 < 80% 不通过等标准 | ✅ |
| 流程监控体系 | 健康度仪表板展示实时指标 | ✅ |
| 版本管理规范 | `v[版本][功能]-[类型]-[日期]` 命名规则 | ✅ |
| 运营模式 | 智能反馈路由：三类自动分类 | ✅ |
| 技能版本管理 | 7 天小版 + 30 天大版 | ✅ |
| 知识库强化 | 用户驱动的动态更新 | ✅ |
| 变更流程 | 在线表单 + AI 评估 | ✅ |
| 监控告警 | 告警规则配置 + 升级路径 | ✅ |

📖 完整体系见 [闭环落地体系](./docs/03-user-system/closed-loop-system.md)

---

## 四、仓库结构

```
ai-workflow-hub/
├── README.md                       # 中文主入口（本文件）
├── README.en.md                    # 英文主入口
├── LICENSE                         # MIT
├── .gitignore
├── architecture/                   # 🆕 架构设计图集（Mermaid，GitHub 原生渲染）
│   ├── 01-system-context           # 系统上下文架构
│   ├── 02-workflow-stages          # 10 阶段工作流 + 闭环
│   ├── 03-agent-orchestration      # Agent 编排时序与上下文传递
│   ├── 04-traceability             # ID 溯源数据流
│   └── 05-gate-pipeline            # 质量门禁流水线（每图 .md / .en.md）
├── cases/                          # 🆕 端到端实战案例
│   ├── case-01-ecommerce           # OrderHub：想法→上线→反馈闭环（贯穿 G0-G10）
│   └── case-02-hotfix              # 轻量案例：登录崩溃 Bug 紧急修复（G6-G9）
├── tests/                          # 🆕 测试体系与可运行门禁校验器
│   ├── test-strategy               # 测试策略与金字塔
│   ├── test-cases                  # 测试用例与追踪矩阵
│   ├── coverage-report             # 覆盖率报告样例（76%→89% 故事）
│   ├── gate-validation.py          # 真实可运行的门禁校验脚本（--demo）
│   └── gate-validation             # 脚本说明与 CI/hook 集成（每文档 .md / .en.md）
└── docs/
    ├── 01-landscape/
    │   └── overview.md / overview.en.md          # 5 大框架 + 参考项目全景对比与逐项解析
    ├── 02-unified-framework/
    │   ├── unified-workflow.md / .en.md          # 统一 10 阶段工作流（核心）
    │   ├── agent-roles.md / .en.md               # 8 大角色 Agent 定义
    │   └── quality-gates.md / .en.md             # 质量门禁 Gate 0-10 + 检查清单
    ├── 03-user-system/
    │   └── closed-loop-system.md / .en.md        # 闭环落地体系（10 项优化 + 15 项对比）
    └── 04-appendix/
        ├── glossary.md / .en.md                  # 中英术语对照表
        └── quick-start.md / .en.md               # 快速上手与选型指南
```

---

## 五、如何使用

1. **想快速了解全景** → 读本页 + [全景对比](./docs/01-landscape/overview.md)
2. **想看图理解架构** → 读 [架构设计图集](./architecture/README.md)（5 张 Mermaid 图，含系统上下文、10 阶段流程、Agent 编排、ID 溯源、门禁流水线）
3. **想看真实案例** → 读 [OrderHub 全流程案例](./cases/case-01-ecommerce.md) + [Hotfix 轻量案例](./cases/case-02-hotfix.md)
4. **想看测试与门禁** → 读 [测试体系](./tests/README.md)，运行 `python3 tests/gate-validation.py --demo` 看门禁校验效果
5. **想落地一套流程** → 读 [统一工作流框架](./docs/02-unified-framework/unified-workflow.md) 与 [质量门禁](./docs/02-unified-framework/quality-gates.md)
6. **想定义团队角色** → 读 [角色 Agent](./docs/02-unified-framework/agent-roles.md)
7. **想补齐落地保障** → 读 [闭环落地体系](./docs/03-user-system/closed-loop-system.md)
8. **想知道选哪个框架** → 读 [快速上手与选型](./docs/04-appendix/quick-start.md)

---

## 六、许可证与致谢

本项目内容以 [MIT License](./LICENSE) 开源。所有引用的第三方项目版权归各自作者所有，本文仅作方法论整理与学习研究之用。

如果这套体系对你有帮助，欢迎 Star ⭐ 与贡献。

---

*Made with ❤️ by yunloong-Y · 中英双语 · 持续更新*
