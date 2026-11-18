# Quick Start & Framework Selection Guide

[Home](../../README.en.md) · [简体中文](./quick-start.md) · [Landscape](../01-landscape/overview.en.md)

---

## 1. Which Framework Should I Choose?

| Your need | Recommended | Why |
|---|---|---|
| Think requirements through before coding | **Spec Kit** | SDD 6-step flow, `converge` prevents drift |
| Process that scales with project size | **BMAD Method** | Scale-adaptive, small changes straight to build |
| Enterprise, audit & compliance | **AI-DLC** | 5 phases 33 stages, 134-event audit, approval gates |
| Quickly assemble an AI "virtual team" | **gstack** | 23 opinionated role tools |
| Prevent skipped steps, missing tests, secret leaks | **Agentic OS** | Machine-enforced gates + git hooks + CI |
| A complete, composable, bilingual system | **This hub's unified framework** | Fuses all above + our closed-loop assurance |

> These frameworks are not mutually exclusive. The unified framework here is pluggable by stage — mix and match: use Spec Kit for specs, gstack for roles, Agentic OS for gates, AI-DLC for audit.

---

## 2. Three Starting Paths

### Path A: Quick Experience (30 min)

1. Read the [Landscape](../01-landscape/overview.en.md) for overall context.
2. Pick one framework and install via its official Quick Start (see each README).
3. Run its minimal flow (e.g. Spec Kit `/specify → /plan → /tasks → /implement`).

### Path B: Deliver a Team Process (1–2 weeks)

1. **G0 governance**: define gates with [Quality Gates](../02-unified-framework/quality-gates.en.md), assign roles with [Agent Roles](../02-unified-framework/agent-roles.en.md).
2. Configure deliverable templates stage by stage following the [Unified Workflow](../02-unified-framework/unified-workflow.en.md).
3. Wire automatable gates (credential scan, coverage, phase evidence) into git hooks + CI.
4. Integrate our [Closed-Loop System](../03-user-system/closed-loop-system.en.md): ID traceability, exception handling, monitoring & alerting.

### Path C: Enterprise Governance (ongoing)

1. Adopt AI-DLC's 5 phases 33 stages + 134-event audit.
2. Layer Agentic OS machine-enforced gates.
3. Use our "health dashboard" to continuously monitor process health.
4. Form an organization-level closed loop via G10 feedback iteration + dynamic knowledge base.

---

## 3. Installation Quick Reference

| Framework | Install command (summary) | Prereqs |
|---|---|---|
| Spec Kit | `uv tool install specify-cli && specify init my-project --integration copilot` | Python 3.11+, uv |
| BMAD (v6.12) | `npx bmad-method install` | Node.js 20.12+, Python 3.10+ |
| BMAD (v7 preview) | `npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'` | Node.js, npm, Git |
| AI-DLC | `curl -fsSL .../install.sh \| sh` then `aidlc config --harness claude` | macOS/Linux/WSL or Windows |
| gstack | See project README | Claude Code |
| Agentic OS | See `docs/INSTALL.md` (nothing enabled by default — enable hooks/CI manually) | Python |

> ⚠️ Refer to each project's official README for exact commands; versions may change.

---

## 4. Common Pitfalls

| Pitfall | Correction |
|---|---|
| Running all 10 stages for every change | Tailor by scale: small changes use light path (G6→G9) |
| Treating a rules file as a gate | Rules get ignored by AI; real gates need git hooks + CI |
| Trusting "tests pass" at face value | Verify tests actually ran (exit code + code fingerprint) |
| Writing a spec then forgetting it | Spec must carry through to implementation & convergence, then be revised by G10 feedback |
| Ending the loop at launch | Launch is the midpoint; feedback returning to G3 is the real closure |

---

## 5. Contributing

Contributions of new framework analyses, templates, glossary terms, or best practices are welcome. Before submitting:
- Include both Chinese and English versions;
- Cite sources for third-party projects;
- Do not infer or alter system content from original documents (especially our proprietary system section).
