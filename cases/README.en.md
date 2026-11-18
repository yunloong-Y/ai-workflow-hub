# End-to-End Case Studies

> Two realistic cases turn the [10-stage unified workflow](../docs/02-unified-framework/unified-workflow.md) from "methodology" into "artifacts you can actually see".
> Each case carries concrete IDs, dates, gate outcomes, code, coverage numbers and Mermaid diagrams, so it can be reviewed directly against the gate and role definitions in this repository.

[Home](../README.en.md) · [简体中文](./README.md) · [Unified Workflow](../docs/02-unified-framework/unified-workflow.md) · [Quality Gates](../docs/02-unified-framework/quality-gates.md) · [Closed-Loop System](../docs/03-user-system/closed-loop-system.md)

---

## Why read these cases

The methodology docs answer "how it should be done"; the cases answer "what it actually looks like when done for real". These cases deliberately preserve details that are *imperfect but authentic*:

- **Gate failures and rework**: coverage first came in at 76% and failed Gate 8; only after adding tests did it reach 87% and pass.
- **Review interceptions**: Gate 7 surfaced 3 real findings (1 blocker, 2 major) before sign-off.
- **Retroactive approval**: an urgent production hotfix used the green channel, but the change ticket and risk assessment were completed within 24 hours.

> Core belief: **only an auditable process is a good process**. Every conclusion is backed by evidence (artifact files, command output, fingerprints, approval records), never a bare "done".

---

## Cases at a glance

| Dimension | Case 1 · OrderHub E-commerce Orders | Case 2 · Login Crash Hotfix |
|---|---|---|
| File | [case-01-ecommerce.en.md](./case-01-ecommerce.en.md) | [case-02-hotfix.en.md](./case-02-hotfix.en.md) |
| One-liner | A full closed loop from idea to production | A fast lane under a production incident |
| Change type | New project / feature development | Small change / production bugfix |
| Entry point | G0 (enterprise system, all 10 stages) | G6 (small change goes straight to build) |
| Path | G0→G1→G2→G3→G4→G5→G6→G7→G8→G9→G10→back to G3 | G6→G7→G8→G9 (retroactive approval) |
| Roles involved | All 8 roles | Developer + Security + QA + Ops + Release Manager |
| Time span | 2026-09-02 → 2026-11-20 (incl. post-release feedback) | 2026-11-16 02:14 → 05:47 (~3.5 hours) |
| Requirement / defect IDs | REQ-001 ~ REQ-006, TASK-001 ~ TASK-014 | BUG-2026-1116-001, HF-001 ~ HF-004 |
| Coverage | 87% (failed at 76% first, passed after more tests) | Affected modules only, target 80%, measured 83% |
| Gate characteristics | All 11 Gates leave an audit trail | Light gates + green channel with retroactive approval |
| Mermaid diagrams | E2E sequence, ID traceability flow, architecture | Hotfix sequence diagram |
| Key takeaway | Full-chain ID traceability, ADRs, Converged, Health Dashboard, feedback-driven spec revision | Scale-adaptivity, 48h escalation, retroactive approval |

The point of comparing the two: **the same workflow can be tailored to change size** — don't drag a typo fix through all 10 stages, and don't let an enterprise system skip audit gates. This is a worked demonstration of the [scale-adaptive principle](../docs/02-unified-framework/unified-workflow.en.md#scale-adaptive-borrowing-bmad--spec-kit-entry-points).

---

## How to use this case set

1. **Read the main line first**: go through the [Unified Workflow Framework](../docs/02-unified-framework/unified-workflow.en.md) and memorize G0–G10 with their Gates.
2. **Work through Case 1**: read [case-01](./case-01-ecommerce.en.md) stage by stage. For each Gate, revisit the [quality gate table](../docs/02-unified-framework/quality-gates.en.md) and check whether the evidence in the case satisfies the criteria.
3. **Work through Case 2**: read [case-02](./case-02-hotfix.en.md) and notice which gates can be trimmed and which must never be skipped (credential scan, test evidence, change approval — none are optional).
4. **Reuse the artifact templates**: `decision.md`, `ADR-001`, the review report, the `converge` report, and the change request form in the cases can all serve as starting templates for your team.
5. **Trace an ID end to end**: start at `REQ-003` and follow it through `TASK-007` → `OrderService.pay()` → `UT-Order-014` → `v1.0.0-orderhub-release-2026-11-14`. This is the best exercise for understanding the closed-loop system.

---

## Key terms used in these cases (consistent across the repo)

| Term | Meaning |
|---|---|
| Gate | A "no pass, no release" quality checkpoint (Gate 0–10) |
| Constitution | The quality principles and governance baseline set in G0, binding throughout |
| ADR (Architecture Decision Record) | A technical decision documented as context → decision → consequences |
| ID traceability | Full-chain binding: requirement → task → code → test → release |
| Converged | The state where the `/converge` report proves implementation matches the spec |
| Health Dashboard | The process-monitoring board showing gate pass rate, coverage trend, etc. |
| 48h escalation | A gate untouched for 48 hours auto-escalates to the next-level owner |
| Change process | Release control via online form + AI assessment + human approval |
| Scale-adaptive | Choosing entry point and gate depth based on change size |

---

## Contents

- [Case 1: E-commerce Order System OrderHub (EN)](./case-01-ecommerce.en.md) · [简体中文](./case-01-ecommerce.md)
- [Case 2: Production Login Crash Hotfix (EN)](./case-02-hotfix.en.md) · [简体中文](./case-02-hotfix.md)

---

*All case data is constructed for teaching purposes, but the structure, gate criteria and artifact formats are fully aligned with this repository's methodology.*
