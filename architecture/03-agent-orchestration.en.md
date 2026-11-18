# Diagram 3 · Agent Orchestration Architecture

> Question answered: How do the 8 agent roles collaborate? How are context and decisions passed across stages and sessions?

[Diagram Index](./README.en.md) · [简体中文](./03-agent-orchestration.md) · [Agent Roles](../docs/02-unified-framework/agent-roles.en.md)

---

## 3.1 Role Collaboration Sequence Diagram

> Using "a new feature from requirements to launch" as an example, showing the call order and context flow across roles under orchestration.

<!-- IMG-EMBED -->
**图 1 · sequenceDiagram**

![图 1 · sequenceDiagram](../assets/architecture-03-agent-orchestration.en--1.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
sequenceDiagram
    autonumber
    participant H as Human (Approver)
    participant O as Orchestrator Agent
    participant PM as Product Manager Agent
    participant AR as Architect Agent
    participant DV as Developer Agent
    participant QA as QA / Test Agent
    participant SE as Security Engineer Agent
    participant OP as Operations Agent
    participant KB as Knowledge Base (SoT)

    H->>O: Raise idea
    O->>PM: G1 Idea assessment
    PM->>KB: Read historical learnings
    PM-->>O: decision.md (go)
    O->>H: Request approval
    H-->>O: Approved

    O->>PM: G2-G3 Clarify & specify
    PM->>KB: Write PRD / acceptance / requirement IDs
    PM-->>O: PRD + user stories

    O->>AR: G4 Plan architecture
    AR->>KB: Read PRD
    AR->>KB: Write ADR-001/002
    AR-->>O: Architecture + ADR

    O->>DV: G5-G6 Tasks & build
    DV->>KB: Read architecture + ADR + tasks
    DV->>DV: TDD coding
    DV-->>O: Code + unit tests

    O->>SE: G6 credential scan / G7 security review
    SE-->>O: Scan passed + review report

    O->>QA: G8 Test & verify
    QA->>QA: Run tests + coverage + converge
    QA->>KB: Write test evidence + fingerprint
    QA-->>O: Coverage 87% + Converged

    O->>OP: G9 Ship
    OP->>H: Change approval
    H-->>OP: Approved
    OP->>OP: Deploy + alert config
    OP-->>O: Release record

    O->>PM: G10 Learn & iterate
    PM->>KB: Write feedback class + health metrics
    KB-->>O: Drive next spec revision
    O-->>H: Loop-complete report
```

</details>

**How to read:**
- The **orchestrator** (borrowing AI-DLC's adaptive composer) is the hub — dispatching roles by stage and pausing at approval points.
- The **knowledge base is the single source of truth**: each role writes its outputs to KB, the next reads from KB — avoiding "re-explaining every chat" (BMAD's durable context).
- **Humans approve at key nodes**: G1 decision, G9 change/release.
- **Evidence is logged**: QA writes test evidence + fingerprint to KB, enabling machine-enforced gates (Agentic OS).

---

## 3.2 Context Passing Mechanism

<!-- IMG-EMBED -->
**图 2 · flowchart**

![图 2 · flowchart](../assets/architecture-03-agent-orchestration.en--2.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart LR
    CTX["Constitution"] --> KB[("Knowledge Base<br/>Single Source of Truth")]
    DEC["ADR decisions"] --> KB
    REQ["Requirements / acceptance"] --> KB
    EVI["Test evidence / fingerprint"] --> KB
    KB -->|"inject context on demand"| A1["Product Agent"]
    KB -->|"inject context on demand"| A2["Architect Agent"]
    KB -->|"inject context on demand"| A3["Developer Agent"]
    KB -->|"inject context on demand"| A4["QA Agent"]
    KB -->|"inject context on demand"| A5["Ops Agent"]

    style KB fill:#EEEDFE,stroke:#534AB7
```

</details>

> **Core idea**: decisions and evidence are written to a single source of truth, read on demand by each role — the landing point of BMAD "durable context" and Agentic OS "memory that survives handoffs".
