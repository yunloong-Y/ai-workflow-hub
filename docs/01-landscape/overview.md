# 五大 AI 开发工作流全景对比与逐项解析

> 本文对 5 个主流 AI 开发工作流框架 + 1 个参考项目进行深度拆解，从定位、方法论、阶段、角色、产出物、独特机制等维度横向对比。

[返回首页](../../README.md) · [English](./overview.en.md)

---

## 0. 全景速览

| 维度 | Spec Kit | BMAD Method | AI-DLC | gstack | Agentic OS |
|---|---|---|---|---|---|
| 定位 | 规范驱动开发 | 敏捷 AI 驱动开发 | 生命周期框架 | 角色化工具集 | 治理框架 |
| 核心理念 | 先写规格再写代码 | 决策显式化、流程按规模自适应 | 一个核心、多宿主、全程可审计 | 用"意见鲜明"的角色分工协作 | 机器强制的阶段与证据 |
| 流程粒度 | 6 步主流程 | 自适应（Quick/Full） | 5 阶段 33 步 | 按角色组织 | 5 步闭环 |
| 角色体系 | 靠 Extension/Bundle 扩展 | 产品/架构/UX/开发/测试专家 | 14 Agent（11 专家 + 2 审查 + 1 编排） | 23 个角色工具 | 按任务类型自动挂载 Skill |
| 宿主兼容 | 多 Agent 集成 | 多编码工具 | 7 大宿主原生 | Claude Code 为主 | 模型无关 Markdown |
| 质量机制 | converge 收敛检查 + 清单 | 审查 + 测试架构模块 | 人工审批门 + 审计轨迹 | 角色互审 | git hook + 校验器 + CI |
| 最适合 | 想"先把需求想清楚" | 想让流程随项目规模伸缩 | 企业级、要审计与治理 | 想快速组建"虚拟团队" | 担心 AI 跳步骤/漏测试 |

---

## 1. github/spec-kit — 规范驱动开发（SDD）

- **Star**：~150k ｜ **许可证**：MIT ｜ **默认分支**：main
- **一句话**：给 AI 编码 Agent 一套结构化流程、可复用模板与有据可查的产出物，"用规格构建"。

### 核心流程（六步法）

```
/constitution  →  /specify  →  /plan  →  /tasks  →  /implement  →  /converge
   项目原则         要构建什么     技术怎么实现    任务拆解       写代码         收敛验证
```

- `/constitution`：每个项目建立一次，定义代码质量、测试、可维护性原则。
- `/specify`：描述要构建的功能（做什么、为什么），不碰技术栈。
- `/plan`：加入技术约束（如 Vite + 原生 JS、图片本地化、SQLite 存元数据）。
- `/tasks`：把规格与计划拆成可执行任务。
- `/implement`：让 Agent 逐步实现。
- `/converge`：反复执行直到报告 `Converged`，确保实现与规格收敛一致。

### 三条独立入口（不是强制阶段）

1. **Spec-Driven Development**：建功能 —— 规格贯穿计划、实现、收敛。
2. **Bug fixing**（`/bug-assess → bug-fix → bug-test`）：评估成因 → 限定修复 → 记录验证，结论为 `verified / partial / failed`。
3. **Idea assessment**（`/assess-intake → research → define → shape → decide`）：用证据决定 `go / needs-clarification / kill`。

### 独特机制

- **可组合能力体系**：Integration（切换 Agent）、Extension（加命令/门禁）、Preset（定制规范）、Workflow（自动化）、Bundle（角色化套装）、Catalog（社区/私有组件目录）、Hook（生命周期事件）。
- **项目级覆盖**：单项目可覆盖模板，无需改全局。
- **离线/内网**：支持 Local sources 与自托管 catalog。
- 前置：Python 3.11+、`uv`、一个受支持的 AI 编码 Agent。

**借鉴要点**：把"规格"作为一等公民贯穿全程；`converge` 收敛思想确保 AI 实现不偏离需求；三条独立入口体现"流程按任务类型选择"而非一刀切。

---

## 2. bmad-code-org/BMAD-METHOD — 敏捷 AI 驱动开发

- **Star**：~55k ｜ **许可证**：MIT ｜ **当前**：v6.12 稳定版 / v7 预览
- **一句话**：把一个想法或变更请求变成可运行软件，同时"不丢掉思考"。

### 核心理念：规模自适应（Right-sized process）

BMad 的交付闭环：**Clarify（澄清）→ Plan（规划）→ Build（构建）→ Learn & Adjust（学习与调整）**，学习结果回环到 Plan。

- 模糊想法 → 从 Clarify 开始
- 大而清晰的想法 → 从 Plan 开始
- 小改动 → 直接从 Build + verify 开始

### 关键特性

- **持久上下文（Durable context）**：把产品与技术决策一路传递，不必在每次对话重复解释。
- **多专业视角**：产品、架构、UX、开发、测试专家按需介入。
- **引导式协作**：结构化工作流 + 多 Agent 讨论，但不替人做判断。
- **新旧代码通吃**：既可从零开始，也可在既有代码库上先建立"已验证的上下文"。

### 生态模块

BMad Method（主方法）、BMad Builder（Skill/Workflow/Agent 构建器）、Creative Intelligence Suite（创新/设计思维）、Test Architect（企业测试）、BMad Loop（无人值守跑完整 epic）、Game Dev Studio（游戏开发）。

### 借鉴要点

**"流程按规模自适应"** 是最值得吸收的思想——用一个"规划路径选择器"决定一个变更需要多少规划深度，避免小改动走重流程、大项目缺规划。

---

## 3. awslabs/aidlc-workflows — AI 驱动开发生命周期

- **Star**：~6.1k ｜ **许可证**：MIT-0 ｜ **版本**：2.11.4
- **一句话**：把 AI 编码助手变成结构化、可验证的软件交付工作流，"一个核心、多个宿主"。

### 硬核数字

- **5 个阶段、33 个步骤**（从初始化到运维）
- **14 个 Agent**：11 领域专家 + 2 审查者 + 1 自适应编排者
- **11 种工作流画像**：功能、修 bug、基础设施、安全、概念验证、企业交付等
- **134 事件审计轨迹** + 持久状态 + 团队知识 + 学习到的规则
- **7 大宿主原生运行**：Claude Code、Kiro CLI/IDE、Codex CLI、Cursor、opencode、GitHub Copilot

### 核心机制

- **人工审批门（Human approval gates）**：进入下一步前必须停下等待批准。
- **溯源审查证据（Source-bound review evidence）**：审查有据可查。
- **确定性引擎**：同一套引擎跨所有宿主，方法论与模型提供商无关。
- **工作流画像**：Classic / Express 及聚焦型工作流，按任务选择。

### 借鉴要点

**5 阶段 33 步的细粒度拆解**、**11 种工作流画像** 与 **134 事件审计轨迹** 是"企业级可审计"的标杆。适合把审计与治理作为工作流的一等公民。

---

## 4. garrytan/gstack — 角色化 Claude Code 工具集

- **Star**：~142k ｜ **许可证**：MIT
- **一句话**：使用 Garry Tan 本人那套 Claude Code 配置——23 个"意见鲜明"的工具，分别充当 CEO、设计师、工程经理、发布经理、文档工程师等角色。

### 核心理念：角色分工的"虚拟团队"

与流程型框架不同，gstack 的切入点是**角色**：把一位资深创业者/管理者团队的各种职能，固化成一个个有明确立场（opinionated）的 Agent 工具，让 AI 以不同专业身份协作。

### 独特价值

- **角色即工具**：每个角色有清晰的职责边界与判断标准。
- **意见鲜明**：不做"和稀泥"式回答，角色会基于自身立场给出强判断。
- **可组合**：23 个工具覆盖从战略、设计到发布、文档的全链职能。

### 借鉴要点

角色化是让 AI 输出"专业且一致"的有效手段。与 BMAD 的多角色、AI-DLC 的 14 Agent 呼应——**角色定义的质量，直接决定 AI 输出的质量**。

---

## 5. KbWen/agentic-os — AI 编码 Agent 治理框架

- **Star**：~240 ｜ **许可证**：MIT
- **一句话**：一份 rules 文件（Cursor Rules / AGENTS.md）只是 Agent 可以忽视的提示；Agentic OS 增加一层 Agent 无法控制的强制机制。

### 五步工作流

```
plan  →  build  →  review  →  test  →  ship
规划      构建       审查       测试      发布
```

### 核心：机器强制的兜底（Machine-enforced backstops）

| 失败模式 | 由谁拦截 | 装完就生效？ |
|---|---|---|
| 密钥被提交进历史 | `scan_credentials.py` 凭证扫描 | 否，需启用 pre-commit hook 或 CI |
| 跳过阶段且无证据 | `validate.sh` 读取工作轨迹，缺阶段/缺证据即失败 | 否，需手动运行或放进 hook |
| "测试通过"但根本没测试 | 你的 CI 跑真实测试套件 | 仅在 CI 运行处 |
| 测试记录通过后代码又改了 | `record_test_run.py` 记录退出码与代码指纹，`/ship` 校验 | 否，需通过它跑测试 |

### 其他机制

- **按阶段自动挂载 Skill**：按任务类型把正确清单推到 Agent 面前（功能开发上 TDD、登录代码上安全审查）。
- **跨会话记忆**：决策与证据存于单一事实源状态文件。
- **模型无关**：Claude Code（`CLAUDE.md`）、Codex（`AGENTS.md`）、Gemini（`GEMINI.md`）原生入口，兼容 Cursor、Copilot 等。
- **Token 经济**：按风险分级治理，微小修复跳过重门禁（约 5,000 tokens）。
- `⚡ ACX` 运行时标记 + `gate:` 块（`gate / classification / verdict / missing`）。

### 借鉴要点

**"规则会被忽视，门禁必须机器强制"** 是本报告最重要的落地警示。工作流要真正生效，必须有 git hook、校验器、CI 这类 Agent 绕不过去的物理约束。

---

## 6. 参考基准：cilangzzz/software-dev-ai-workflow

- **Star**：~48 ｜ **许可证**：MIT ｜ **语言**：Python
- **定位**：AI Agent 驱动的 Claude Code 软件开发工作流框架，"描述即交付"。

### 框架特性

- 🔄 **双流程支持**：瀑布 / 敏捷全流程，含质量门控 Gate 1-5
- 🏭 **行业系统模型**：ERP（12 模块）、MES（10+ 模块）、语音社区
- 🔧 **27+ 通用技能**：SSH、Word、Draw.io、Notion、Jira、禅道等
- 🤖 **8 阶段端到端工作流**：`.claude/` 下从需求分析到前后端开发的编排
- 🧬 **可自扩展**：`author-skill` 元技能让 AI 自己创建新技能
- 🗂️ **单一事实源**：自动生成 `catalog.json`、Skill 总目录、按阶段/按部门产出物

### 8 大角色 Agent

产品、研发、测试、运维、安全、设计、数据、项目管理。

### 借鉴要点

"**角色 × 阶段 × 产出物**"的三维结构、质量门控 Gate 1-5、以及"单一事实源自动生成目录"的工程做法，是本仓库统一框架的重要参考原型。

---

## 7. 横向洞察：五大框架教会我们的 8 件事

1. **规格是一等公民**（Spec Kit）—— 先把 what/why 说清楚，再谈 how。
2. **流程按规模/任务自适应**（BMAD / Spec Kit）—— 小改动直达构建，大项目才深度规划。
3. **角色定义决定输出质量**（gstack / BMAD / AI-DLC）—— 用专业身份约束 AI 的判断。
4. **审计与可追溯是企业级刚需**（AI-DLC）—— 134 事件轨迹、审批门、溯源证据。
5. **规则会被忽视，门禁必须强制**（Agentic OS）—— git hook + 校验器 + CI 才是真约束。
6. **上下文要跨会话持久化**（BMAD / Agentic OS）—— 决策不因对话结束而丢失。
7. **收敛/验证闭环不可省**（Spec Kit converge / Agentic OS ship）—— 直到证明一致才算完成。
8. **工具链要模型无关**（AI-DLC / Agentic OS）—— 方法论与具体宿主/模型解耦。

> 这 8 条洞察 + 本项目自有闭环体系，共同构成 [统一工作流框架](../02-unified-framework/unified-workflow.md) 的设计基础。
