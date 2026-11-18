# Diagram 1 · System Context Architecture

> Question answered: How does this AI workflow system interact with external roles, tools, and systems as a whole?

[Diagram Index](./README.en.md) · [简体中文](./01-system-context.md)

---

## 1.1 System Context Diagram

<!-- IMG-EMBED -->
**图 1 · flowchart**

![图 1 · flowchart](../assets/architecture-01-system-context.en--1.png)

<details>
<summary>查看 Mermaid 源码（可编辑）</summary>

```mermaid
flowchart TB
    subgraph ACTORS["External Actors"]
        DEV["Developer / PM / Architect<br/>Raise requirements, review decisions, final approval"]
        USER["End User<br/>Use the product, provide feedback"]
    end

    subgraph SYSTEM["AI Workflow System (this repo's methodology)"]
        CORE["Workflow Engine<br/>10-stage orchestration + scale-adaptive"]
        ROLES["8 Agent Roles<br/>Product/Arch/Dev/QA/Ops..."]
        GATES["Quality Gates + Assurance<br/>Gate 0-10 + ID traceability + monitoring"]
        KB[("Knowledge Base<br/>Decisions / context / learnings")]
    end

    subgraph TOOLS["External Tools & Harnesses"]
        HARNESS["AI Coding Harness<br/>Claude Code / Cursor / Codex / Copilot"]
        SCM["Source Control<br/>GitHub / GitLab + Git Hooks"]
        CI["CI/CD Pipeline<br/>Build / Test / Deploy"]
        MON["Monitoring & Alerting<br/>Dashboard / Alert rules"]
    end

    DEV -->|"ideas / PRD / approval"| CORE
    CORE <-->|"orchestrate / context"| ROLES
    ROLES -->|"deliverables"| GATES
    GATES <-->|"read/write decisions & evidence"| KB
    ROLES <-->|"generate / execute"| HARNESS
    HARNESS -->|"commit code"| SCM
    GATES -->|"trigger validation"| SCM
    SCM -->|"push / hook"| CI
    CI -->|"coverage / test results"| GATES
    CI -->|"deploy"| MON
    MON -->|"health / feedback"| KB
    USER -->|"usage feedback"| MON
    KB -->|"feedback drives spec revision"| CORE

    style SYSTEM fill:#EEEDFE,stroke:#534AB7
    style ACTORS fill:#E6F1FB,stroke:#185FA5
    style TOOLS fill:#E1F5EE,stroke:#0F6E56
```

</details>

**How to read:**
- The system core has three parts: **workflow engine** (orchestration) + **agent roles** (execution) + **gate assurance** (verification).
- The **knowledge base** is the "memory" across the entire flow, making decisions persist across sessions and roles.
- External tools fall into three categories: AI coding harness (where work happens), source control/CI (how it's validated), monitoring (how it's observed).
- The key loop: `MON → KB → CORE`, i.e. "usage feedback → knowledge distillation → driving the next spec revision".

---

## 1.2 System Boundaries & Responsibilities

| Layer | Inside this system | Outside (external) |
|---|---|---|
| Process | 10-stage definition, scale-adaptive, gate rules | Specific Jira/TAPD project management systems |
| Execution | 8 role definitions, Skill/Agent orchestration | Specific LLM models (Claude/GPT) |
| Assurance | ID traceability rules, coverage standards, alert levels | Specific CI platforms (GitHub Actions/Jenkins) |
| Memory | Knowledge base structure, decision record spec | Specific vector DB / document systems |

> This system is **model-agnostic and tool-agnostic** (borrowing AI-DLC and Agentic OS), and can be grafted onto any coding harness and toolchain.
