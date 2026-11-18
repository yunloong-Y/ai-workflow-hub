# 图 2 · 10 阶段工作流架构

> 回答：从想法到上线，流程如何流转？闭环如何形成？不同规模的变更如何裁剪？

[图集导航](./README.md) · [English](./02-workflow-stages.en.md) · [统一工作流正文](../docs/02-unified-framework/unified-workflow.md)

---

## 2.1 主流程图（完整 10 阶段 + 闭环）

<!-- IMG-EMBED -->
**图 1 · flowchart**

![图 1 · flowchart](../assets/architecture-02-workflow-stages--1.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart TD
    START([想法 / 变更请求]) --> G0["G0 治理基线<br/>宪法·角色·门禁·工具链"]
    G0 --> G1{"G1 想法评估"}
    G1 -->|"kill / 待澄清"| STOP([带理由停止<br/>也是有效产出])
    G1 -->|"go"| G2["G2 澄清启动<br/>消歧·上下文·风险"]
    G2 --> G3["G3 规格需求<br/>PRD·用户故事·验收标准·ID"]
    G3 --> G4["G4 计划架构<br/>选型·架构·ADR"]
    G4 --> G5["G5 任务拆解<br/>Epic→Story→Task·依赖图"]
    G5 --> G6["G6 构建实现<br/>编码·TDD·凭证扫描"]
    G6 --> G7["G7 代码审查<br/>代码·安全·一致性审查"]
    G7 --> G8{"G8 测试验证<br/>覆盖率≥80%·Converged?"}
    G8 -->|"未通过"| FIX["回到对应阶段修正"]
    FIX --> G6
    G8 -->|"通过"| G9["G9 发布交付<br/>审批·部署·告警·回滚"]
    G9 --> G10["G10 反馈迭代<br/>反馈分类·健康度·知识库"]
    G10 -->|"需求落地反馈迭代"| G3
    G10 --> DONE([闭环完成 → 下一轮])
    START -.->|"小改动走轻量路径"| LIGHT["G6→G7→G8→G9"]
    LIGHT --> G9

    style G0 fill:#FAEEDA,stroke:#BA7517
    style G1 fill:#E6F1FB,stroke:#185FA5
    style G3 fill:#E6F1FB,stroke:#185FA5
    style G8 fill:#FCEBEB,stroke:#A32D2D
    style G10 fill:#E1F5EE,stroke:#0F6E56
    style LIGHT fill:#F1EFE8,stroke:#888780
```

</details>

**读图要点：**
- **三个出口**：`kill`（想法评估阶段带理由停止）、`DONE`（闭环完成）、修正回环。
- **门禁卡点**：G1（`go` 决策）、G8（覆盖率+Converged）是关键判定门，未通过会回退修正。
- **闭环**：G10 的反馈不是终点，而是通过"需求落地反馈迭代"回到 G3 修订规格。
- **规模裁剪**：小改动通过虚线走轻量路径 `G6→G7→G8→G9`（借鉴 BMAD/Agentic OS）。

---

## 2.2 三阶段视图（规划域 / 交付域 / 反馈域）

<!-- IMG-EMBED -->
**图 2 · flowchart**

![图 2 · flowchart](../assets/architecture-02-workflow-stages--2.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart LR
    subgraph PLAN["规划域 · Think"]
        P1["G0 治理"] --> P2["G1 评估"] --> P3["G2 澄清"] --> P4["G3 规格"] --> P5["G4 架构"] --> P6["G5 任务"]
    end
    subgraph BUILD["交付域 · Build & Ship"]
        B1["G6 构建"] --> B2["G7 审查"] --> B3["G8 测试"] --> B4["G9 发布"]
    end
    subgraph FEED["反馈域 · Learn"]
        F1["G10 反馈迭代"] --> F2["知识库更新"]
    end
    P6 --> B1
    B4 --> F1
    F2 -.->|"驱动规格修订"| P4

    style PLAN fill:#EEEDFE,stroke:#534AB7
    style BUILD fill:#E6F1FB,stroke:#185FA5
    style FEED fill:#E1F5EE,stroke:#0F6E56
```

</details>

> 对应 BMAD 的 `Clarify → Plan → Build → Learn` 交付循环，本体系把它细化为可落地的 10 个带门禁的阶段。

---

## 2.3 规模自适应路径对照

| 变更类型 | 起点 | 路径 | 门禁强度 |
|---|---|---|---|
| 小改动（typo / 小 bug） | G6 | G6→G7→G8→G9 | 轻量（~5k tokens，借鉴 Agentic OS） |
| 功能开发 | G2/G3 | G2→…→G9→G10 | 标准 |
| 想法 / 新项目 | G1 | G1→(go)→G3→… | 含评估门 |
| 企业 / 受监管系统 | G0 | 全 10 阶段 | 全量 + 审计轨迹（借鉴 AI-DLC） |
