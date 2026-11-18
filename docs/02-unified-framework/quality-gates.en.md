# Quality Gates Gate 0–10 & Checklists

> Gates are "no-pass-without-standard" quality checkpoints in the workflow. Borrowing AI-DLC human approval gates, Spec Kit checklists, cilangzzz Gate 1-5, and our "coverage < 80% = fail" standard.

[Home](../../README.en.md) · [简体中文](./quality-gates.md) · [Unified Workflow](./unified-workflow.en.md)

---

## Gate Design Principles

1. **Quantifiable**: every gate has explicit criteria (coverage ≥80%, report = Converged, etc.).
2. **Traceable**: gate verdicts and evidence are logged, source-bound.
3. **Enforce when possible**: anything automatable via git hook / CI should not rely on agent discipline (Agentic OS lesson).
4. **Tailor by scale**: light paths pass only core gates (G6/G8/G9); full paths pass all.

---

## Gate Master Table

| Gate | Stage | Criteria (pass standard) | Enforcement | On-failure |
|---|---|---|---|---|
| **G0** | Governance | Constitution/roles/gates/toolchain complete & verifiable | Manual + config check | Fill governance elements |
| **G1** | Idea Assessment | Verdict = `go` with sufficient evidence | Human approval | `kill` or `needs-clarification` backfill |
| **G2** | Clarify | Key ambiguities resolved, context sufficient | Human approval | Return to clarification |
| **G3** | Specify | Spec complete, testable, IDs fully traceable | Checklist + ID check | Complete spec/ID map |
| **G4** | Architecture | Architecture aligns spec, ADR documented, security reviewed | Manual + ADR check | Revise architecture |
| **G5** | Tasks | Tasks cover all acceptance criteria, dependencies clear | Coverage check | Add tasks |
| **G6** | Build | Compiles, unit tests pass, no credential leaks | `scan_credentials.py` + build | Fix/rollback |
| **G7** | Review | No blocking issues, review evidenced | Manual + review log | Fix then re-review |
| **G8** | Test | Coverage ≥80%, tests actually run, Converged | CI + fingerprint check | Add tests/fix |
| **G9** | Ship | Change approved, monitoring/alerting/rollback ready | `validate.sh` + approval | Block release |
| **G10** | Learn | Feedback classified into backlog, KB updated | Manual + status check | Log feedback |

---

## Key Gates Detailed

### Gate 3 · Spec Gate

- [ ] Every requirement has a unique ID
- [ ] Every requirement has testable acceptance criteria (Gherkin preferred)
- [ ] Complete ID flow arrows: requirement → task → code → test → release
- [ ] Spec conflicts with project constitution resolved

### Gate 6 · Build Gate (machine-enforced)

- [ ] `scan_credentials.py` credential scan passes (can wire to pre-commit hook)
- [ ] Code compiles/builds
- [ ] Unit tests pass
- [ ] No unasked-for refactors

### Gate 8 · Test Gate (machine-enforced)

- [ ] Test coverage ≥80%
- [ ] Tests actually run via `record_test_run.py` with exit code recorded
- [ ] Code fingerprint matches test run (code unchanged after tests)
- [ ] `converge` report is `Converged`
- [ ] CI runs the real test suite

### Gate 9 · Ship Gate (machine-enforced)

- [ ] Change assessed via online form + AI
- [ ] Change approved (human)
- [ ] `validate.sh` passes (phases & evidence complete)
- [ ] Alert rules configured
- [ ] Rollback plan ready

---

## Exception Handling & Escalation (Our System)

| Exception type | Trigger | Handling path |
|---|---|---|
| Gate timeout | Unresolved for 48 hours | Auto-escalate to next-level owner |
| Human intervention | Gate requires human judgment | Route to human queue and log |
| Gate failure | Coverage/evidence below standard | Block release, return to stage for fix |
| Urgent change | Production hotfix | Emergency channel, retroactive approval & logging |

> **Timeout escalation: auto-escalate if unresolved for 48 hours** is the core rule of our "exception handling mechanism".

---

## Alert Levels (Our System)

| Level | Scenario | Response |
|---|---|---|
| P0 Critical | Release failure, gate bypassed, credential leak | Immediate response, block + notify owner |
| P1 High | Gate timeout, test failure | Respond within 4 hours |
| P2 Medium | Coverage drop, feedback backlog | Respond within 24 hours |
| P3 Low | Docs not updated, KB pending | Regular iteration |

---

## Monitoring Health Metrics (Our System)

The health dashboard should show: gate pass rate, average gate processing time, timeout escalation count, test coverage trend, defect escape rate, feedback closure rate, knowledge base update frequency.
