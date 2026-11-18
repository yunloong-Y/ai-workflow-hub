# 8 Agent Roles

> Role-based design is key to making AI output "professional and consistent" (shared lesson from gstack / BMAD / AI-DLC).
> This document defines 8 core agent roles, each with: responsibility, stages involved, input, output, judgment criteria.

[Home](../../README.en.md) · [简体中文](./agent-roles.md) · [Unified Workflow](./unified-workflow.en.md)

---

## Roles at a Glance

| # | Agent Role | Stages Involved | Core Deliverable |
|---|---|---|---|
| 1 | Product Manager | G1/G2/G3/G10 | PRD, user stories, feedback classification |
| 2 | Architect | G4 | Architecture design, ADR, tech selection |
| 3 | Developer | G6 | Runnable code, unit tests |
| 4 | QA / Test Engineer | G8 | Test report, coverage report |
| 5 | Operations Engineer | G9 | Deployment plan, monitoring/alert config |
| 6 | Security Engineer | G7 | Security review report |
| 7 | Data Engineer | G4/G10 | Data model, data lineage |
| 8 | Project Manager | G0/G5/G9/G10 | Gate config, task breakdown, milestones |

---

## 1. Product Manager

- **Responsibility**: Turn ideas/requirements into clear specs; make value judgments and feedback routing.
- **Stages**: G1 assessment, G2 clarify, G3 specify, G10 feedback iteration.
- **Input**: Idea description, user feedback, market info.
- **Output**: Assessment report + `decision.md`, PRD, user stories, acceptance criteria, 3-category feedback classification.
- **Judgment criteria**: Is the requirement worth doing (go/kill), is the spec testable, is feedback prioritization sound.
- **Borrowed from**: Spec Kit `/assess-*` `/specify`; BMAD product expert; gstack CEO/PM view.

## 2. Architect

- **Responsibility**: Turn spec into technical solution; make documented architecture decisions.
- **Stages**: G4 plan & architecture (also G2 context building).
- **Input**: PRD, acceptance criteria, constraints.
- **Output**: Architecture doc, ADR, tech selection report, diagrams, data model.
- **Judgment criteria**: Architecture aligns spec, decisions backed by ADR, secure & maintainable.
- **Borrowed from**: BMAD Architect + ADR; Spec Kit `/plan`; AI-DLC architecture expert.

## 3. Developer

- **Responsibility**: Implement code by task, preserve context and code quality.
- **Stages**: G6 build.
- **Input**: Task list, architecture, codebase.
- **Output**: Runnable code, API implementation, unit tests.
- **Judgment criteria**: Compiles, unit tests pass, discipline followed (plan before editing, no out-of-scope refactors).
- **Borrowed from**: Spec Kit `/implement`; gstack role tools; AI-DLC build agent.

## 4. QA / Test Engineer

- **Responsibility**: Prove quality with real tests — reject "tests pass but no tests".
- **Stages**: G8 test & verify.
- **Input**: Code, acceptance criteria.
- **Output**: Test cases, test report, coverage report (≥80%), convergence report.
- **Judgment criteria**: Coverage met, tests actually run, implementation converges with spec.
- **Borrowed from**: BMAD Test Architect; Spec Kit `/converge`; Agentic OS `record_test_run.py`.

## 5. Operations Engineer

- **Responsibility**: Safely deliver code to production, ensure observability and rollback.
- **Stages**: G9 ship, G10 ops feedback.
- **Input**: Code passing Gate 8, change request.
- **Output**: CI/CD config, deployment plan, ops manual, monitoring/alert config.
- **Judgment criteria**: Change approved, alerting configured, rollback ready.
- **Borrowed from**: AI-DLC Operations; cilangzzz CI pipeline assistant; our change process.

## 6. Security Engineer

- **Responsibility**: Review auth/security code, intercept credential leaks and security risks.
- **Stages**: G6 credential scan, G7 security review.
- **Input**: Code changes, login/auth code.
- **Output**: Security review report, credential scan results.
- **Judgment criteria**: No credential leaks, no vulnerabilities, review logged.
- **Borrowed from**: Agentic OS credential scan; AI-DLC security workflow profile; gstack security view.

## 7. Data Engineer

- **Responsibility**: Design data models, trace data lineage, ensure data quality.
- **Stages**: G4 data model design, G10 data feedback analysis.
- **Input**: Requirements, business entities.
- **Output**: Data model, data lineage doc, data quality rules.
- **Judgment criteria**: Model supports requirements, lineage traceable.
- **Borrowed from**: cilangzzz data lineage tracing skill.

## 8. Project Manager

- **Responsibility**: Establish governance baseline, break down tasks, track gates & milestones, control changes.
- **Stages**: G0 governance, G5 tasks, G9 change, G10 closure.
- **Input**: Project goals, spec, architecture.
- **Output**: Constitution/gate config, task list, dependency graph, milestone report, change record.
- **Judgment criteria**: Tasks cover acceptance criteria, gates verifiable, changes approved.
- **Borrowed from**: cilangzzz project management agent; AI-DLC composer agent; our version/change spec.

---

## Role Collaboration Diagram

```
Product Manager ──(PRD)──→ Architect ──(arch/ADR)──→ Project Mgr ──(tasks)──→ Developer
   ↑                                                              │
   │                                                            (code)
   │                                                              ▼
Feedback class ←──(monitoring)── Ops Engineer ←──(deploy)── Security/QA ←──(review/test)
   └──────────────────(loop: feedback drives spec revision)──────────────────┘
```
