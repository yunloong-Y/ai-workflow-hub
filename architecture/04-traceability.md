# 图 4 · ID 溯源数据流

> 回答：一条需求（如 REQ-042）如何向下贯穿到任务、代码、测试、发布？全链路绑定与可视化如何实现？

[图集导航](./README.md) · [English](./04-traceability.en.md) · [闭环体系](../docs/03-user-system/closed-loop-system.md)

---

## 4.1 ID 流向全链路图

> 这是自有闭环体系的"ID 溯源可视化增强"核心：用 ID 流向箭头展示全链路绑定。

```mermaid
flowchart LR
    REQ["REQ-042<br/>需求：支持订单批量取消"] --> STORY["US-042<br/>用户故事"]
    STORY --> TASK1["TASK-042A<br/>API 实现"]
    STORY --> TASK2["TASK-042B<br/>前端交互"]
    TASK1 --> CODE1["代码：OrderService<br/>.cancelBatch()"]
    TASK2 --> CODE2["代码：OrderPanel<br/>.vue"]
    CODE1 --> UT["单元测试<br/>test_cancel_batch.py<br/>TC-042-01~05"]
    CODE2 --> E2E["E2E 测试<br/>TC-042-E2E"]
    UT --> REPORT["测试报告<br/>覆盖率 88%"]
    E2E --> REPORT
    REPORT --> REL["发布<br/>v2.3.0-feature-20261118"]
    REL --> FB["反馈<br/>FB-042 三类分类"]
    FB -.->|"反馈驱动修订"| REQ

    style REQ fill:#E6F1FB,stroke:#185FA5
    style CODE1 fill:#EEEDFE,stroke:#534AB7
    style CODE2 fill:#EEEDFE,stroke:#534AB7
    style REPORT fill:#E1F5EE,stroke:#0F6E56
    style REL fill:#FAEEDA,stroke:#BA7517
    style FB fill:#FBEAF0,stroke:#993556
```

**读图要点：**
- 每个需求分配唯一 ID（`REQ-042`），向下贯穿到故事、任务、代码、测试、发布、反馈。
- 一条需求可能分叉成多个任务/代码/测试，形成一张**可追溯的图**。
- 反馈 `FB-042` 通过虚线回到需求，形成闭环——这正是"需求落地反馈迭代"。
- 任一环节都可反向追溯：从线上 bug 可定位到具体需求、任务、代码、测试。

---

## 4.2 双向追溯矩阵

```mermaid
flowchart TB
    subgraph FORWARD["正向追溯（需求 → 交付）"]
        direction TB
        R1["REQ-042"] --> T1["TASK-042A/B"]
        T1 --> C1["代码提交 a1b2c3d"]
        C1 --> TC1["TC-042-01~05"]
        TC1 --> D1["部署 v2.3.0"]
    end
    subgraph BACKWARD["反向追溯（问题 → 根源）"]
        direction TB
        BUG["线上问题 BUG-118"] --> D2["定位部署 v2.3.0"]
        D2 --> TC2["关联测试 TC-042-03"]
        TC2 --> C2["关联代码 cancelBatch()"]
        C2 --> R2["根源需求 REQ-042"]
    end
    D1 -.->|"线上观测"| BUG

    style FORWARD fill:#E6F1FB,stroke:#185FA5
    style BACKWARD fill:#FBEAF0,stroke:#993556
```

---

## 4.3 ID 命名规范表（自有体系）

| 前缀 | 含义 | 示例 | 产生阶段 |
|---|---|---|---|
| `REQ-` | 需求 ID | REQ-042 | G3 规格 |
| `US-` | 用户故事 | US-042 | G3 规格 |
| `TASK-` | 任务 ID | TASK-042A | G5 任务拆解 |
| `ADR-` | 架构决策记录 | ADR-001 | G4 架构 |
| `TC-` | 测试用例 | TC-042-01 | G8 测试 |
| `BUG-` | 缺陷 ID | BUG-118 | G7/G10 |
| `FB-` | 反馈 ID | FB-042 | G10 反馈 |
| `CR-` | 变更请求 | CR-20261118-01 | G9 变更 |

> 版本命名规范（自有体系）：`v[版本][功能]-[类型]-[日期]`，如 `v2.3.0-feature-20261118`。
