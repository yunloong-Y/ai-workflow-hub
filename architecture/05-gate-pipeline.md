# 图 5 · 质量门禁流水线

> 回答：Gate 0-10 如何卡点？哪些是机器强制（Agent 绕不过去）？哪些靠人工审批？

[图集导航](./README.md) · [English](./05-gate-pipeline.en.md) · [质量门禁正文](../docs/02-unified-framework/quality-gates.md)

---

## 5.1 门禁流水线图（含强制方式标注）

<!-- IMG-EMBED -->
**图 1 · flowchart**

![图 1 · flowchart](../assets/architecture-05-gate-pipeline--1.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart LR
    G0["G0<br/>治理基线"]:::manual --> G1["G1<br/>想法评估"]:::manual
    G1 --> G2["G2<br/>澄清启动"]:::manual
    G2 --> G3["G3<br/>规格需求"]:::check
    G3 --> G4["G4<br/>计划架构"]:::manual
    G4 --> G5["G5<br/>任务拆解"]:::check
    G5 --> G6["G6<br/>构建实现"]:::machine
    G6 --> G7["G7<br/>代码审查"]:::manual
    G7 --> G8["G8<br/>测试验证"]:::machine
    G8 --> G9["G9<br/>发布交付"]:::machine
    G9 --> G10["G10<br/>反馈迭代"]:::manual

    classDef manual fill:#E6F1FB,stroke:#185FA5
    classDef check fill:#FAEEDA,stroke:#BA7517
    classDef machine fill:#FCEBEB,stroke:#A32D2D

    HOOK["Git Hooks / CI"]:::infra --> G6
    HOOK --> G8
    HOOK --> G9
    classDef infra fill:#F1EFE8,stroke:#888780
```

</details>

**强制方式图例：**
- 🔵 **人工审批**（manual）：需要人判断和签字（G0/G1/G2/G4/G7/G10）。
- 🟡 **清单/校验**（check）：清单检查 + ID 校验（G3/G5）。
- 🔴 **机器强制**（machine）：git hook / CI 强制执行，Agent 绕不过去（G6/G8/G9）——借鉴 Agentic OS 的核心思想。

---

## 5.2 机器强制门禁内部流程（以 Gate 8 为例）

<!-- IMG-EMBED -->
**图 2 · flowchart**

![图 2 · flowchart](../assets/architecture-05-gate-pipeline--2.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart TD
    START["代码提交 / 请求发布"] --> SCAN["凭证扫描<br/>scan_credentials.py"]
    SCAN -->|"发现密钥"| BLOCK1[("🚫 阻断 + 告警 P0")]
    SCAN -->|"通过"| BUILD["构建 + 单元测试"]
    BUILD -->|"失败"| BLOCK2[("🚫 阻断")]
    BUILD -->|"通过"| COV["覆盖率检查<br/>≥80%?"]
    COV -->|"76% < 80%"| BLOCK3[("🚫 门禁失败<br/>补测后重试")]
    COV -->|"88% ≥ 80%"| FP["测试指纹校验<br/>代码在测试后未变更?"]
    FP -->|"已变更"| BLOCK4[("🚫 阻断：重跑测试")]
    FP -->|"未变更"| CONV["收敛检查<br/>Converged?"]
    CONV -->|"否"| BLOCK5[("🚫 回到 G6 修正")]
    CONV -->|"是"| PASS[("✅ Gate 8 通过 → G9")]

    style BLOCK1 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK2 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK3 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK4 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK5 fill:#FCEBEB,stroke:#A32D2D
    style PASS fill:#E1F5EE,stroke:#0F6E56
```

</details>

> **核心警示（来自 Agentic OS）**：rules 文件只是 Agent 可以忽略的提示；真正生效的门禁必须是机器强制的——凭证扫描、覆盖率、测试指纹、阶段证据都要接进 git hook 与 CI。

---

## 5.3 门禁状态机

<!-- IMG-EMBED -->
**图 3 · stateDiagram-v2**

![图 3 · stateDiagram-v2](../assets/architecture-05-gate-pipeline--3.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
stateDiagram-v2
    [*] --> Pending: 进入阶段
    Pending --> Checking: 提交证据
    Checking --> Passed: 判据达标
    Checking --> Failed: 判据未达标
    Checking --> Timeout: 48h 未处理
    Failed --> Pending: 修正后重试
    Timeout --> Escalated: 自动升级上一级
    Escalated --> Pending: 上级介入处理
    Passed --> [*]: 放行到下一阶段
    Passed --> Pending: G10 反馈回环（下一轮）
```

</details>

> 状态机体现了自有体系的"异常处理机制"：**超时 48 小时自动升级**，失败回退修正，通过后放行或进入下一轮闭环。
