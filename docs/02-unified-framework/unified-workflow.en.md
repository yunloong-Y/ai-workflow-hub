# Unified Workflow Framework · 10-Stage End-to-End AI Software Development

> Fusing the five frameworks (Spec Kit, BMAD, AI-DLC, gstack, Agentic OS) plus our proprietary closed-loop assurance system — the "most comprehensive" main flow.
> Each stage specifies: **Input → Activities → Deliverables → Release Gate → Corresponding Framework Practice → Lead Role**.

[Home](../../README.en.md) · [简体中文](./unified-workflow.md) · [Quality Gates](./quality-gates.en.md) · [Agent Roles](./agent-roles.en.md)

---

## Overall Flow Diagram

```
                          ┌──────────────────────────────────────────┐
                          │  G0 Governance Baseline (once/project)    │
                          │  constitution + roles + gates + toolchain │
                          └────────────────────┬─────────────────────┘
                                               ▼
   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
   │ G1 Idea   │→ │ G2 Clarify│→ │ G3 Specify│→ │ G4 Plan   │→ │ G5 Tasks  │
   │ Assessment│   │ & Incept  │   │ & Reqs   │   │ & Arch    │   │ Breakdown │
   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                                     ▼
   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
   │ G10 Learn│← │ G9 Ship   │← │ G8 Test   │← │ G7 Review │← │ G6 Build  │
   │ & Iterate│   │ & Deploy  │   │ & Verify  │   │          │   │ & Impl    │
   └────┬─────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
        │
        └──────────────────→ back to G3 (requirements feedback loop, driving next spec revision)
```

**Scale-adaptive** (borrowing BMAD / Spec Kit entry points): not every change runs all 10 stages:

| Change type | Suggested start | Path |
|---|---|---|
| Small change (typo, minor bug) | G6 | G6 → G7 → G8 → G9 (light gates, ~5k tokens) |
| Feature development | G2/G3 | G2 → G3 → … → G9 → G10 |
| Idea / new project assessment | G1 | G1 → (go) → G3 or G0 → … |
| Enterprise / regulated system | G0 | All 10 stages + full audit gates |

---

## G0 · Governance Baseline

> Created once per project — the "constitution" for all later stages. Borrowing Spec Kit `/constitution` + Agentic OS governance layer.

| Item | Content |
|---|---|
| **Input** | Project goals, team size, compliance needs, tech preferences |
| **Activities** | Define quality principles; assign roles; configure gates; select toolchain/harness; establish audit & memory |
| **Deliverables** | Project constitution, role matrix, gate config, toolchain list, single-source-of-truth catalog |
| **Release Gate** | Gate 0: principles clear, roles assigned, gates machine-verifiable |
| **Framework practice** | Spec Kit `/constitution`; Agentic OS governance files (CLAUDE.md / AGENTS.md / GEMINI.md) + git hooks |
| **Lead role** | Project manager / Tech lead / Governance officer |

**Constitution template essentials**: code quality standards, test coverage threshold (e.g. ≥80%), maintainability requirements, security baseline, naming conventions, change approval rules.

---

## G1 · Idea Assessment

> Use evidence to decide if an idea is worth investing in. Borrowing Spec Kit `/assess-*`.

| Item | Content |
|---|---|
| **Input** | Idea description, existing codebase (optional) |
| **Activities** | Gather evidence → define value → assess shape/feasibility → decide |
| **Deliverables** | Assessment report, `decision.md` (`go` / `needs-clarification` / `kill`) |
| **Release Gate** | Gate 1: verdict is `go` with sufficient evidence, then G2/G3 |
| **Framework practice** | Spec Kit `/assess-intake → research → define → shape → decide` |
| **Lead role** | Product manager / Founder advisor |

> Key: **stopping with a well-documented reason (kill) is a valid outcome** — not every idea needs development.

---

## G2 · Clarify & Inception

> Turn a vague idea into clarity, establish verified context. Borrowing BMAD Clarify + AI-DLC Inception.

| Item | Content |
|---|---|
| **Input** | Approved idea (go), existing codebase context |
| **Activities** | Resolve ambiguities; establish context; identify constraints & risks; decide planning path |
| **Deliverables** | Clarification record, context doc, risk list, planning-path decision |
| **Release Gate** | Gate 2: key ambiguities resolved, context sufficient for spec writing |
| **Framework practice** | BMAD Clarify; AI-DLC Inception phase |
| **Lead role** | Product manager / Business analyst / Architect |

---

## G3 · Specify / PRD

> Write clearly "what to build and why" — no tech implementation yet. Borrowing Spec Kit `/specify` + BMAD PRD.

| Item | Content |
|---|---|
| **Input** | Clarified requirements, context doc |
| **Activities** | Write spec / PRD; user stories + acceptance criteria (Gherkin); design system constraints |
| **Deliverables** | Spec / PRD, user stories, acceptance criteria, ID traceability map |
| **Release Gate** | Gate 3: spec complete, testable, IDs fully traceable end-to-end (see closed-loop system) |
| **Framework practice** | Spec Kit `/specify`; BMAD PRD / Gherkin acceptance |
| **Lead role** | Product manager / Requirements analyst |

**ID traceability requirement** (our system): assign a unique ID to each requirement, threading down through tasks, code, tests, and release; show flow with arrows for full-chain binding.

---

## G4 · Plan & Architecture

> Turn the spec into a technical solution and architecture decisions. Borrowing Spec Kit `/plan` + BMAD Architect/ADR + AI-DLC expert agents.

| Item | Content |
|---|---|
| **Input** | Spec / PRD, acceptance criteria |
| **Activities** | Tech selection; architecture design; API/data model design; write ADRs |
| **Deliverables** | Tech selection report, architecture doc, ADR, architecture diagrams, data model |
| **Release Gate** | Gate 4: architecture aligns with spec, decisions documented (ADR), security & maintainability reviewed |
| **Framework practice** | Spec Kit `/plan`; BMAD Architect + ADR; AI-DLC 11 domain experts |
| **Lead role** | Architect / Tech lead |

---

## G5 · Task Breakdown

> Break spec and plan into executable, assignable tasks. Borrowing Spec Kit `/tasks` + BMAD Epics/Stories.

| Item | Content |
|---|---|
| **Input** | Spec, architecture, ADR |
| **Activities** | Break Epic → Story → Task; annotate dependencies & priority; bind requirement IDs |
| **Deliverables** | Task list, dependency graph, priority queue, requirement→task ID map |
| **Release Gate** | Gate 5: tasks cover all acceptance criteria, dependencies clear, IDs traceable |
| **Framework practice** | Spec Kit `/tasks`; BMAD Epics/Stories |
| **Lead role** | Project manager / Tech lead |

---

## G6 · Build / Implement

> AI agents code by task, humans steer direction. Borrowing Spec Kit `/implement` + gstack role tools + AI-DLC build stage.

| Item | Content |
|---|---|
| **Input** | Task list, architecture, codebase |
| **Activities** | Implement task by task; TDD for features; auto-attach skill checklists by phase; preserve context |
| **Deliverables** | Runnable code, data models, API implementation, unit tests |
| **Release Gate** | Gate 6: tasks complete, code compiles, unit tests pass, no credential leaks |
| **Framework practice** | Spec Kit `/implement`; gstack 23 role tools; AI-DLC build stage; Agentic OS credential scan |
| **Lead role** | Developer / AI coding agent |

> Discipline (Agentic OS): plan before editing, no unasked-for refactors, credential scan must intercept at the gate.

---

## G7 · Review

> Multi-role review ensuring implementation matches spec and quality standards. Borrowing BMAD code-review + AI-DLC reviewers + gstack cross-role review.

| Item | Content |
|---|---|
| **Input** | Code changes, spec, architecture |
| **Activities** | Code review; security review (login/auth code); spec consistency check; review evidence logging |
| **Deliverables** | Review report, issue list, source-bound review evidence |
| **Release Gate** | Gate 7: no blocking issues, review evidenced, source-bound |
| **Framework practice** | BMAD `code-review` / `bug-analyzer`; AI-DLC 2 reviewer agents; gstack cross-role review |
| **Lead role** | Reviewer / Security engineer / Tech lead |

---

## G8 · Test & Verify

> Prove quality with real tests — reject "tests pass but no tests". Borrowing Spec Kit `/converge` + Agentic OS test gate + BMAD Test Architect.

| Item | Content |
|---|---|
| **Input** | Code, acceptance criteria |
| **Activities** | Unit/integration/E2E tests; coverage check; convergence verification (impl vs spec); record test evidence |
| **Deliverables** | Test report, coverage report (≥80%), convergence report (`Converged`), test-run fingerprint |
| **Release Gate** | Gate 8: coverage met, tests actually run, `converge` reports Converged, code unchanged after tests |
| **Framework practice** | Spec Kit `/converge`; Agentic OS `record_test_run.py`; BMAD Test Architect |
| **Lead role** | Test engineer / QA |

> Machine-enforced (Agentic OS): test exit code + code fingerprint recorded; if tests fail or code changed after tests, `/ship` verification fails.

---

## G9 · Ship / Deploy

> Produce deployment & ops artifacts under approval gates and change management. Borrowing AI-DLC Operations + Agentic OS `/ship` + our change process.

| Item | Content |
|---|---|
| **Input** | Code passing Gate 8, change request |
| **Activities** | CI/CD pipeline; deploy; generate ops manual/monitoring config; change approval; alert rule config |
| **Deliverables** | Deployment package, CI/CD config, ops manual, monitoring/alert config, change record |
| **Release Gate** | Gate 9: change AI-assessed + approved, test evidence valid, alerting & rollback ready |
| **Framework practice** | AI-DLC Operations; Agentic OS `/ship` + `validate.sh`; our change process (form + AI assessment) |
| **Lead role** | Operations engineer / Release manager |

---

## G10 · Learn & Iterate

> Collect post-launch feedback, drive next spec revision, forming a closed loop. Borrowing BMAD Learn + our closed-loop system.

| Item | Content |
|---|---|
| **Input** | Launch feedback, monitoring metrics, user behavior |
| **Activities** | Smart feedback routing (3-category auto-classification); health dashboard analysis; distill learnings into knowledge base; version iteration |
| **Deliverables** | Feedback classification report, health report, knowledge base update, next-round requirements/spec revision |
| **Release Gate** | Gate 10: feedback classified into backlog, knowledge base updated, experience issues tracked |
| **Framework practice** | BMAD Learn & Adjust; our smart feedback routing + dynamic knowledge base |
| **Lead role** | Product manager / Operations / Project manager |

**Closed-loop key**: G10 is not the end — it returns to G3 via "requirements delivery feedback iteration", forming a true loop — the core of this project's "full-flow closed loop".

---

## Stage → Framework Practice Quick Reference

| Stage | Spec Kit | BMAD | AI-DLC | gstack | Agentic OS | Ours |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| G0 Governance | constitution | — | engine/rules | role tools | governance files | version/change spec |
| G1 Assessment | assess-* | — | workflow profile | CEO view | gate classification | — |
| G2 Clarify | — | Clarify | Inception | — | — | — |
| G3 Specify | specify | PRD | requirements | Designer | plan | ID traceability |
| G4 Architecture | plan | Architect/ADR | design | Eng Manager | plan | — |
| G5 Tasks | tasks | Epics/Stories | planning | Eng Manager | plan | ID binding |
| G6 Build | implement | Dev | build | role tools | build | credential scan |
| G7 Review | — | code-review | reviewer agents | cross-review | review | exception handling |
| G8 Test | converge | Test Architect | testing | — | test | quality gates |
| G9 Ship | — | — | Operations | Release Manager | ship | change/alerting |
| G10 Learn | — | Learn | ops feedback | — | — | feedback routing/KB |

---

## Delivery Recommendations

1. **Start at G0** — solidify constitution, roles, gates, toolchain first; it's the foundation for everything after.
2. **Tailor by change scale** — don't make a typo fix run 10 stages, and don't let an enterprise system skip audit.
3. **Gates must be machine-enforced** — borrowing Agentic OS, wire automatable gates (credential scan, coverage, phase evidence) into git hooks and CI.
4. **The loop must return to G3** — if G10 feedback doesn't drive spec revision, the loop is broken.
