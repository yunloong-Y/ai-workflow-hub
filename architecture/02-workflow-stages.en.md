# Diagram 2 · 10-Stage Workflow Architecture

> Question answered: How does the flow run from idea to launch? How is the loop closed? How are changes tailored by scale?

[Diagram Index](./README.en.md) · [简体中文](./02-workflow-stages.md) · [Unified Workflow](../docs/02-unified-framework/unified-workflow.en.md)

---

## 2.1 Main Flow Diagram (Full 10 Stages + Loop)

```mermaid
flowchart TD
    START([Idea / Change request]) --> G0["G0 Governance<br/>Constitution·Roles·Gates·Toolchain"]
    G0 --> G1{"G1 Idea Assessment"}
    G1 -->|"kill / needs clarity"| STOP([Stop with reason<br/>also a valid outcome])
    G1 -->|"go"| G2["G2 Clarify & Inception<br/>Resolve ambiguity·Context·Risks"]
    G2 --> G3["G3 Specify<br/>PRD·User stories·Acceptance·IDs"]
    G3 --> G4["G4 Plan & Architecture<br/>Selection·Architecture·ADR"]
    G4 --> G5["G5 Task Breakdown<br/>Epic→Story→Task·Dependency graph"]
    G5 --> G6["G6 Build<br/>Code·TDD·Credential scan"]
    G6 --> G7["G7 Review<br/>Code·Security·Consistency"]
    G7 --> G8{"G8 Test & Verify<br/>Coverage≥80%·Converged?"}
    G8 -->|"Fail"| FIX["Return to stage for fix"]
    FIX --> G6
    G8 -->|"Pass"| G9["G9 Ship<br/>Approval·Deploy·Alert·Rollback"]
    G9 --> G10["G10 Learn & Iterate<br/>Feedback class·Health·KB"]
    G10 -->|"delivery feedback iteration"| G3
    G10 --> DONE([Loop complete → next round])
    START -.->|"small change: light path"| LIGHT["G6→G7→G8→G9"]
    LIGHT --> G9

    style G0 fill:#FAEEDA,stroke:#BA7517
    style G1 fill:#E6F1FB,stroke:#185FA5
    style G3 fill:#E6F1FB,stroke:#185FA5
    style G8 fill:#FCEBEB,stroke:#A32D2D
    style G10 fill:#E1F5EE,stroke:#0F6E56
    style LIGHT fill:#F1EFE8,stroke:#888780
```

**How to read:**
- **Three exits**: `kill` (stop with reason at assessment), `DONE` (loop complete), and fix loop.
- **Gate checkpoints**: G1 (`go` decision) and G8 (coverage + Converged) are key decision gates; failure triggers rollback to a prior stage.
- **The loop**: G10 feedback is not the end — it returns to G3 via "requirements delivery feedback iteration" to revise the spec.
- **Scale tailoring**: small changes take the dashed light path `G6→G7→G8→G9` (borrowing BMAD/Agentic OS).

---

## 2.2 Three-Domain View (Planning / Delivery / Feedback)

```mermaid
flowchart LR
    subgraph PLAN["Planning Domain · Think"]
        P1["G0 Govern"] --> P2["G1 Assess"] --> P3["G2 Clarify"] --> P4["G3 Specify"] --> P5["G4 Architect"] --> P6["G5 Tasks"]
    end
    subgraph BUILD["Delivery Domain · Build & Ship"]
        B1["G6 Build"] --> B2["G7 Review"] --> B3["G8 Test"] --> B4["G9 Ship"]
    end
    subgraph FEED["Feedback Domain · Learn"]
        F1["G10 Learn & Iterate"] --> F2["Knowledge Base Update"]
    end
    P6 --> B1
    B4 --> F1
    F2 -.->|"drives spec revision"| P4

    style PLAN fill:#EEEDFE,stroke:#534AB7
    style BUILD fill:#E6F1FB,stroke:#185FA5
    style FEED fill:#E1F5EE,stroke:#0F6E56
```

> Corresponding to BMAD's `Clarify → Plan → Build → Learn` delivery loop, this system refines it into 10 landable stages with gates.

---

## 2.3 Scale-Adaptive Path Comparison

| Change type | Start | Path | Gate intensity |
|---|---|---|---|
| Small change (typo / minor bug) | G6 | G6→G7→G8→G9 | Light (~5k tokens, borrowing Agentic OS) |
| Feature development | G2/G3 | G2→…→G9→G10 | Standard |
| Idea / new project | G1 | G1→(go)→G3→… | Includes assessment gate |
| Enterprise / regulated system | G0 | All 10 stages | Full + audit trail (borrowing AI-DLC) |
