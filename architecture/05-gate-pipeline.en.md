# Diagram 5 · Quality Gate Pipeline

> Question answered: How do Gates 0-10 check? Which are machine-enforced (unbypassable by agents)? Which rely on human approval?

[Diagram Index](./README.en.md) · [简体中文](./05-gate-pipeline.md) · [Quality Gates](../docs/02-unified-framework/quality-gates.en.md)

---

## 5.1 Gate Pipeline Diagram (with enforcement annotations)

```mermaid
flowchart LR
    G0["G0<br/>Governance"]:::manual --> G1["G1<br/>Assessment"]:::manual
    G1 --> G2["G2<br/>Clarify"]:::manual
    G2 --> G3["G3<br/>Specify"]:::check
    G3 --> G4["G4<br/>Architect"]:::manual
    G4 --> G5["G5<br/>Tasks"]:::check
    G5 --> G6["G6<br/>Build"]:::machine
    G6 --> G7["G7<br/>Review"]:::manual
    G7 --> G8["G8<br/>Test"]:::machine
    G8 --> G9["G9<br/>Ship"]:::machine
    G9 --> G10["G10<br/>Learn"]:::manual

    classDef manual fill:#E6F1FB,stroke:#185FA5
    classDef check fill:#FAEEDA,stroke:#BA7517
    classDef machine fill:#FCEBEB,stroke:#A32D2D

    HOOK["Git Hooks / CI"]:::infra --> G6
    HOOK --> G8
    HOOK --> G9
    classDef infra fill:#F1EFE8,stroke:#888780
```

**Enforcement legend:**
- 🔵 **Human approval** (manual): requires human judgment and sign-off (G0/G1/G2/G4/G7/G10).
- 🟡 **Checklist/validation** (check): checklist + ID validation (G3/G5).
- 🔴 **Machine-enforced** (machine): git hooks / CI enforce, unbypassable by agents (G6/G8/G9) — borrowing Agentic OS's core idea.

---

## 5.2 Machine-Enforced Gate Internal Flow (Gate 8 example)

```mermaid
flowchart TD
    START["Commit / release request"] --> SCAN["Credential scan<br/>scan_credentials.py"]
    SCAN -->|"secret found"| BLOCK1[("BLOCK + alert P0")]
    SCAN -->|"passed"| BUILD["Build + unit tests"]
    BUILD -->|"failed"| BLOCK2[("BLOCK")]
    BUILD -->|"passed"| COV["Coverage check<br/>≥80%?"]
    COV -->|"76% < 80%"| BLOCK3[("GATE FAIL<br/>add tests & retry")]
    COV -->|"88% ≥ 80%"| FP["Test fingerprint check<br/>code unchanged after tests?"]
    FP -->|"changed"| BLOCK4[("BLOCK: re-run tests")]
    FP -->|"unchanged"| CONV["Convergence check<br/>Converged?"]
    CONV -->|"No"| BLOCK5[("Return to G6 fix")]
    CONV -->|"Yes"| PASS[("Gate 8 PASSED → G9")]

    style BLOCK1 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK2 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK3 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK4 fill:#FCEBEB,stroke:#A32D2D
    style BLOCK5 fill:#FCEBEB,stroke:#A32D2D
    style PASS fill:#E1F5EE,stroke:#0F6E56
```

> **Core warning (from Agentic OS)**: a rules file is just a prompt the agent can ignore; gates that truly work must be machine-enforced — credential scan, coverage, test fingerprint, phase evidence all wired into git hooks and CI.

---

## 5.3 Gate State Machine

```mermaid
stateDiagram-v2
    [*] --> Pending: enter stage
    Pending --> Checking: submit evidence
    Checking --> Passed: criteria met
    Checking --> Failed: criteria unmet
    Checking --> Timeout: unresolved 48h
    Failed --> Pending: fix & retry
    Timeout --> Escalated: auto-escalate to next level
    Escalated --> Pending: superior intervenes
    Passed --> [*]: release to next stage
    Passed --> Pending: G10 feedback loop (next round)
```

> The state machine embodies our "exception handling mechanism": **auto-escalate after 48 hours**, failure rolls back for fixes, passing releases or enters the next closed loop.
