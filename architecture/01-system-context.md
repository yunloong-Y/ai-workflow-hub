# 图 1 · 系统上下文架构

> 回答：这套 AI 工作流体系作为一个整体，与哪些外部角色、工具、系统交互？

[图集导航](./README.md) · [English](./01-system-context.en.md)

---

## 1.1 系统上下文图（System Context）

<!-- IMG-EMBED -->
**图 1 · flowchart**

![图 1 · flowchart](../assets/architecture-01-system-context--1.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart TB
    subgraph ACTORS["外部参与者"]
        DEV["👤 开发者 / 产品 / 架构师<br/>提出需求、审查决策、最终审批"]
        USER["👤 终端用户<br/>使用产品、提供反馈"]
    end

    subgraph SYSTEM["AI 工作流体系（本仓库方法论）"]
        CORE["🧠 统一工作流引擎<br/>10 阶段编排 + 规模自适应"]
        ROLES["🤖 8 大角色 Agent<br/>产品/架构/开发/测试/运维…"]
        GATES["🛡️ 质量门禁 + 闭环保障<br/>Gate 0-10 + ID 溯源 + 监控告警"]
        KB[("📚 知识库<br/>决策 / 上下文 / 经验")]
    end

    subgraph TOOLS["外部工具与宿主"]
        HARNESS["AI 编码宿主<br/>Claude Code / Cursor / Codex / Copilot"]
        SCM["代码托管<br/>GitHub / GitLab + Git Hooks"]
        CI["CI/CD 流水线<br/>构建 / 测试 / 部署"]
        MON["监控告警<br/>仪表板 / 告警规则"]
    end

    DEV -->|"想法 / PRD / 审批"| CORE
    CORE <-->|"编排 / 上下文"| ROLES
    ROLES -->|"产出物"| GATES
    GATES <-->|"读写决策与证据"| KB
    ROLES <-->|"生成 / 执行"| HARNESS
    HARNESS -->|"代码提交"| SCM
    GATES -->|"触发校验"| SCM
    SCM -->|"push / hook"| CI
    CI -->|"覆盖率 / 测试结果"| GATES
    CI -->|"部署"| MON
    MON -->|"健康度 / 反馈"| KB
    USER -->|"使用反馈"| MON
    KB -->|"反馈驱动规格修订"| CORE

    style SYSTEM fill:#EEEDFE,stroke:#534AB7
    style ACTORS fill:#E6F1FB,stroke:#185FA5
    style TOOLS fill:#E1F5EE,stroke:#0F6E56
```

</details>

**读图要点：**
- 体系的核心由三部分组成：**工作流引擎**（编排）+ **角色 Agent**（执行）+ **门禁保障**（验证）。
- **知识库**是贯穿全程的"记忆"，让决策跨会话、跨角色持久。
- 外部工具分三类：AI 编码宿主（在哪干活）、代码托管/CI（怎么落库校验）、监控告警（怎么观测）。
- 关键闭环：`MON → KB → CORE`，即"使用反馈 → 知识沉淀 → 驱动下一轮规格修订"。

---

## 1.2 体系边界与职责

| 层 | 属于本体系 | 不属于本体系（外部） |
|---|---|---|
| 流程 | 10 阶段定义、规模自适应、门禁规则 | 具体的 Jira/TAPD 项目管理系统 |
| 执行 | 8 角色定义、Skill/Agent 编排 | 具体的 LLM 模型（Claude/GPT） |
| 保障 | ID 溯源规则、覆盖率标准、告警分级 | 具体的 CI 平台（GitHub Actions/Jenkins） |
| 记忆 | 知识库结构、决策记录规范 | 具体的向量数据库/文档系统 |

> 这套体系是**模型无关、工具无关**的方法论（借鉴 AI-DLC 与 Agentic OS），可以嫁接到任意编码宿主与工具链上。
