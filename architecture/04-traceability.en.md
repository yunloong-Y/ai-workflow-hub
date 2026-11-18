# Diagram 4 · ID Traceability Data Flow

> Question answered: How does a requirement (e.g. REQ-042) thread down to tasks, code, tests, and release? How is full-chain binding and visualization achieved?

[Diagram Index](./README.en.md) · [简体中文](./04-traceability.md) · [Closed-Loop System](../docs/03-user-system/closed-loop-system.en.md)

---

## 4.1 Full-Chain ID Flow Diagram

> This is the core of our "ID traceability visualization enhancement": ID flow arrows showing full-chain binding.

```mermaid
flowchart LR
    REQ["REQ-042<br/>Requirement: batch cancel orders"] --> STORY["US-042<br/>User story"]
    STORY --> TASK1["TASK-042A<br/>API implementation"]
    STORY --> TASK2["TASK-042B<br/>Frontend interaction"]
    TASK1 --> CODE1["Code: OrderService<br/>.cancelBatch()"]
    TASK2 --> CODE2["Code: OrderPanel<br/>.vue"]
    CODE1 --> UT["Unit test<br/>test_cancel_batch.py<br/>TC-042-01~05"]
    CODE2 --> E2E["E2E test<br/>TC-042-E2E"]
    UT --> REPORT["Test report<br/>coverage 88%"]
    E2E --> REPORT
    REPORT --> REL["Release<br/>v2.3.0-feature-20261118"]
    REL --> FB["Feedback<br/>FB-042 3-category class"]
    FB -.->|"feedback drives revision"| REQ

    style REQ fill:#E6F1FB,stroke:#185FA5
    style CODE1 fill:#EEEDFE,stroke:#534AB7
    style CODE2 fill:#EEEDFE,stroke:#534AB7
    style REPORT fill:#E1F5EE,stroke:#0F6E56
    style REL fill:#FAEEDA,stroke:#BA7517
    style FB fill:#FBEAF0,stroke:#993556
```

**How to read:**
- Each requirement gets a unique ID (`REQ-042`), threading down through stories, tasks, code, tests, release, and feedback.
- One requirement can fork into multiple tasks/code/tests, forming a **traceable graph**.
- Feedback `FB-042` returns to the requirement via dashed line, closing the loop — exactly "requirements delivery feedback iteration".
- Any node can be reverse-traced: from a production bug you can locate the exact requirement, task, code, and test.

---

## 4.2 Bidirectional Traceability Matrix

```mermaid
flowchart TB
    subgraph FORWARD["Forward traceability (requirement → delivery)"]
        direction TB
        R1["REQ-042"] --> T1["TASK-042A/B"]
        T1 --> C1["Commit a1b2c3d"]
        C1 --> TC1["TC-042-01~05"]
        TC1 --> D1["Deploy v2.3.0"]
    end
    subgraph BACKWARD["Backward traceability (issue → root cause)"]
        direction TB
        BUG["Production BUG-118"] --> D2["Locate deploy v2.3.0"]
        D2 --> TC2["Related test TC-042-03"]
        TC2 --> C2["Related code cancelBatch()"]
        C2 --> R2["Root requirement REQ-042"]
    end
    D1 -.->|"production observation"| BUG

    style FORWARD fill:#E6F1FB,stroke:#185FA5
    style BACKWARD fill:#FBEAF0,stroke:#993556
```

---

## 4.3 ID Naming Convention (Our System)

| Prefix | Meaning | Example | Produced at |
|---|---|---|---|
| `REQ-` | Requirement ID | REQ-042 | G3 Specify |
| `US-` | User story | US-042 | G3 Specify |
| `TASK-` | Task ID | TASK-042A | G5 Breakdown |
| `ADR-` | Architecture decision record | ADR-001 | G4 Architecture |
| `TC-` | Test case | TC-042-01 | G8 Test |
| `BUG-` | Defect ID | BUG-118 | G7/G10 |
| `FB-` | Feedback ID | FB-042 | G10 Feedback |
| `CR-` | Change request | CR-20261118-01 | G9 Change |

> Version naming convention (our system): `v[version][feature]-[type]-[date]`, e.g. `v2.3.0-feature-20261118`.
