# 图 3 · Agent 编排架构

> 回答：8 大角色 Agent 如何协作？上下文与决策如何跨阶段、跨会话传递？

[图集导航](./README.md) · [English](./03-agent-orchestration.en.md) · [角色定义](../docs/02-unified-framework/agent-roles.md)

---

## 3.1 角色协作时序图

> 以"一个新功能从需求到上线"为例，展示各角色 Agent 在编排下的调用顺序与上下文流转。

```mermaid
sequenceDiagram
    autonumber
    participant H as 人（审批者）
    participant O as 编排器 Agent
    participant PM as 产品经理 Agent
    participant AR as 架构师 Agent
    participant DV as 开发工程师 Agent
    participant QA as 测试工程师 Agent
    participant SE as 安全工程师 Agent
    participant OP as 运维工程师 Agent
    participant KB as 知识库（单一事实源）

    H->>O: 提出想法
    O->>PM: G1 想法评估
    PM->>KB: 读取历史经验
    PM-->>O: decision.md (go)
    O->>H: 请求审批
    H-->>O: 批准

    O->>PM: G2-G3 澄清与规格
    PM->>KB: 写入 PRD / 验收标准 / 需求ID
    PM-->>O: PRD + 用户故事

    O->>AR: G4 计划架构
    AR->>KB: 读取 PRD
    AR->>KB: 写入 ADR-001/002
    AR-->>O: 架构 + ADR

    O->>DV: G5-G6 任务与构建
    DV->>KB: 读取架构 + ADR + 任务
    DV->>DV: TDD 编码
    DV-->>O: 代码 + 单测

    O->>SE: G6 凭证扫描 / G7 安全审查
    SE-->>O: 扫描通过 + 审查报告

    O->>QA: G8 测试验证
    QA->>QA: 跑测试 + 覆盖率 + converge
    QA->>KB: 写入测试证据 + 指纹
    QA-->>O: 覆盖率 87% + Converged

    O->>OP: G9 发布交付
    OP->>H: 变更审批
    H-->>OP: 批准
    OP->>OP: 部署 + 告警配置
    OP-->>O: 发布记录

    O->>PM: G10 反馈迭代
    PM->>KB: 写入反馈分类 + 健康度
    KB-->>O: 驱动下一轮规格修订
    O-->>H: 闭环完成报告
```

**读图要点：**
- **编排器**（借鉴 AI-DLC 的 adaptive composer）是中枢，负责按阶段调度角色、在审批点暂停。
- **知识库是单一事实源**：每个角色的产出都写入 KB，下个角色从 KB 读取，避免"每次对话重新解释"（BMAD 的 durable context）。
- **人在关键节点审批**：G1 决策、G9 变更发布等需要人类把关。
- **证据留痕**：QA 把测试证据与指纹写入 KB，让"机器强制门禁"可校验（Agentic OS）。

---

## 3.2 上下文传递机制

```mermaid
flowchart LR
    CTX["项目宪法<br/>Constitution"] --> KB[("知识库<br/>单一事实源")]
    DEC["架构决策<br/>ADR"] --> KB
    REQ["需求 / 验收标准"] --> KB
    EVI["测试证据 / 指纹"] --> KB
    KB -->|"按需注入上下文"| A1["产品 Agent"]
    KB -->|"按需注入上下文"| A2["架构 Agent"]
    KB -->|"按需注入上下文"| A3["开发 Agent"]
    KB -->|"按需注入上下文"| A4["测试 Agent"]
    KB -->|"按需注入上下文"| A5["运维 Agent"]

    style KB fill:#EEEDFE,stroke:#534AB7
```

> **核心思想**：决策与证据写入一个单一事实源，各角色按需读取——这正是 BMAD "durable context" 与 Agentic OS "memory that survives handoffs" 的落地点。
