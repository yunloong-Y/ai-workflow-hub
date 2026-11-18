# Architecture Diagrams

> "A picture is worth a thousand words" — this section explains the architecture of this AI workflow system using Mermaid diagrams (natively rendered on GitHub).
> All diagrams are source-level text, version-controllable and editable — change the text, the diagram updates.

[Home](../README.en.md) · [简体中文](./README.md) · [Unified Workflow](../docs/02-unified-framework/unified-workflow.en.md)

---

## Diagram Index

| # | Diagram | Question it answers | Mermaid type |
|---|---|---|---|
| 1 | [System Context](./01-system-context.en.md) | How does the system interact with external roles/tools? | `C4Context` / `flowchart` |
| 2 | [10-Stage Workflow](./02-workflow-stages.en.md) | How does the flow run from idea to launch? How is the loop closed? | `flowchart` |
| 3 | [Agent Orchestration](./03-agent-orchestration.en.md) | How do 8 agent roles collaborate? How is context passed? | `sequenceDiagram` |
| 4 | [ID Traceability](./04-traceability.en.md) | How does a requirement thread through code, tests, and release? | `flowchart` / `graph` |
| 5 | [Quality Gate Pipeline](./05-gate-pipeline.en.md) | How do Gates 0-10 gate? Which are machine-enforced? | `flowchart` / `stateDiagram` |

---

## View Layers (C4-like model)

```
┌─────────────────────────────────────────────────────────┐
│ Level 1 · System Context  The system as a whole & its interactions │ ← Diagram 1
├─────────────────────────────────────────────────────────┤
│ Level 2 · Workflow/Container  10-stage main flow & loop           │ ← Diagram 2
├─────────────────────────────────────────────────────────┤
│ Level 3 · Component/Orchestration  Agents, gates, ID traceability │ ← Diagrams 3/4/5
└─────────────────────────────────────────────────────────┘
```

---

## About Mermaid

All diagrams in this repo use [Mermaid](https://mermaid.js.org/) syntax inside mermaid code blocks (fences starting with three backticks + mermaid) in Markdown. GitHub, GitLab, and most Markdown readers render it natively.

- **Maintainable**: diagram-as-code — change the text, update the diagram, no external drawing tool.
- **Reviewable**: diagram changes can be diffed and reviewed like code.
- **Zero dependency**: no image files or image hosting to maintain.

If a diagram doesn't render in your local reader, view it on GitHub, or install a Mermaid-enabled Markdown plugin.
