# Five AI Development Workflows — Landscape & Project-by-Project Analysis

> An in-depth dissection of 5 leading AI development workflow frameworks + 1 reference project, compared across positioning, methodology, stages, roles, deliverables, and unique mechanisms.

[Home](../../README.en.md) · [简体中文](./overview.md)

---

## 0. Landscape at a Glance

| Dimension | Spec Kit | BMAD Method | AI-DLC | gstack | Agentic OS |
|---|---|---|---|---|---|
| Positioning | Spec-driven development | Agile AI-driven development | Development lifecycle framework | Role-based toolset | Governance framework |
| Core idea | Spec before code | Explicit decisions, scale-adaptive process | One core, many harnesses, fully auditable | Opinionated role-based collaboration | Machine-enforced stages & evidence |
| Process granularity | 6-step main flow | Adaptive (Quick/Full) | 5 phases, 33 stages | Organized by role | 5-step loop |
| Role system | Via Extension/Bundle | Product/arch/UX/dev/test experts | 14 agents (11 experts + 2 reviewers + 1 composer) | 23 role tools | Skills auto-attached by task type |
| Harness compat. | Multi-agent integrations | Multi coding tools | 7 native harnesses | Claude Code-centric | Model-agnostic Markdown |
| Quality mechanism | converge check + checklists | Review + test architecture module | Human approval gates + audit trail | Cross-role review | git hook + validator + CI |
| Best for | "Think requirements through first" | Process that scales with project | Enterprise, audit & governance | Quickly assemble a "virtual team" | Preventing skipped steps / missing tests |

---

## 1. github/spec-kit — Spec-Driven Development (SDD)

- **Stars**: ~150k ｜ **License**: MIT ｜ **Default branch**: main
- **One-liner**: A structured process, reusable templates, and documented outcomes for AI coding agents — "build with a spec".

### Core Flow (Six Steps)

```
/constitution  →  /specify  →  /plan  →  /tasks  →  /implement  →  /converge
  project principles   what to build    how (tech)    breakdown     code      convergence
```

- `/constitution`: created once per project — principles for code quality, testing, maintainability.
- `/specify`: describe what to build and why, without touching the tech stack.
- `/plan`: add technical constraints (e.g. Vite + vanilla JS, local images, SQLite metadata).
- `/tasks`: break the spec and plan into executable tasks.
- `/implement`: let the agent implement step by step.
- `/converge`: repeat until it reports `Converged`, ensuring implementation matches the spec.

### Three Independent Entry Points (not mandatory phases)

1. **Spec-Driven Development**: build a feature — spec carried through plan, implementation, convergence.
2. **Bug fixing** (`/bug-assess → bug-fix → bug-test`): assess cause → scoped fix → recorded verification; verdict `verified / partial / failed`.
3. **Idea assessment** (`/assess-intake → research → define → shape → decide`): evidence-based `go / needs-clarification / kill`.

### Unique Mechanisms

- **Composable capabilities**: Integration (switch agents), Extension (add commands/gates), Preset (customize standards), Workflow (automation), Bundle (role-based setups), Catalog (community/private component catalogs), Hook (lifecycle events).
- **Project-local overrides**: one-off template changes without global modification.
- **Offline/air-gapped**: local sources and self-hosted catalogs.
- Prereqs: Python 3.11+, `uv`, a supported AI coding agent.

**Takeaway**: Make the spec a first-class citizen throughout; the `converge` idea prevents AI drift from requirements; three entry points show "choose flow by task type" rather than one-size-fits-all.

---

## 2. bmad-code-org/BMAD-METHOD — Agile AI-Driven Development

- **Stars**: ~55k ｜ **License**: MIT ｜ **Current**: v6.12 stable / v7 preview
- **One-liner**: Turn an idea or change request into working software "without giving up the thinking".

### Core Idea: Right-Sized Process

BMad's delivery loop: **Clarify → Plan → Build → Learn & Adjust**, with learning looping back to Plan.

- Vague notion → start at Clarify
- Big clear idea → start at Plan
- Small change → go straight to Build + verify

### Key Features

- **Durable context**: carry product & technical decisions forward — no re-explaining each chat.
- **Specialized perspectives**: product, architecture, UX, development, testing experts on demand.
- **Guided collaboration**: structured workflows + multi-agent discussions without surrendering judgment.
- **New or existing code**: start from scratch or establish verified context on an inherited codebase.

### Ecosystem Modules

BMad Method (core), BMad Builder (skill/workflow/agent builder), Creative Intelligence Suite, Test Architect (enterprise testing), BMad Loop (unattended full-epic runs), Game Dev Studio.

### Takeaway

"**Right-sized process**" is the most valuable idea — use a planning-path selector to decide how much planning a change needs, avoiding heavy process for small changes and under-planning for big ones.

---

## 3. awslabs/aidlc-workflows — AI-Driven Development Life Cycle

- **Stars**: ~6.1k ｜ **License**: MIT-0 ｜ **Version**: 2.11.4
- **One-liner**: Turn AI coding assistants into structured, verifiable delivery workflows — "one core, many harnesses".

### Hard Numbers

- **5 phases, 33 stages** (initialization through operations)
- **14 agents**: 11 domain experts + 2 reviewers + 1 adaptive composer
- **11 workflow profiles**: features, bug fixes, infrastructure, security, PoCs, enterprise delivery, etc.
- **134-event audit trail** + persistent state + team knowledge + learned rules
- **7 native harnesses**: Claude Code, Kiro CLI/IDE, Codex CLI, Cursor, opencode, GitHub Copilot

### Core Mechanisms

- **Human approval gates**: stop for approval before advancing.
- **Source-bound review evidence**: reviews are traceable.
- **Deterministic engine**: same engine across all harnesses; methodology independent of model provider.
- **Workflow profiles**: Classic / Express and focused workflows, selected by task.

### Takeaway

The fine-grained **5-phase 33-stage breakdown**, **11 workflow profiles**, and **134-event audit trail** set the enterprise-grade auditability benchmark.

---

## 4. garrytan/gstack — Role-Based Claude Code Toolset

- **Stars**: ~142k ｜ **License**: MIT
- **One-liner**: Garry Tan's exact Claude Code setup — 23 opinionated tools serving as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, etc.

### Core Idea: A Role-Based "Virtual Team"

Unlike process-type frameworks, gstack enters through **roles**: it crystallizes the functions of a senior founder/manager team into opinionated agent tools, so AI collaborates in distinct professional identities.

### Unique Value

- **Role-as-tool**: each role has clear responsibility boundaries and judgment criteria.
- **Opinionated**: no fence-sitting — roles give strong judgments from their standpoint.
- **Composable**: 23 tools cover the full chain from strategy and design to release and docs.

### Takeaway

Role-based design is an effective way to make AI output "professional and consistent" — echoing BMAD's multi-role and AI-DLC's 14 agents. **The quality of role definitions directly determines output quality.**

---

## 5. KbWen/agentic-os — Governance Framework for AI Coding Agents

- **Stars**: ~240 ｜ **License**: MIT
- **One-liner**: A rules file (Cursor Rules / AGENTS.md) is just a prompt the agent can ignore; Agentic OS adds a layer the agent doesn't control.

### Five-Step Workflow

```
plan  →  build  →  review  →  test  →  ship
```

### Core: Machine-Enforced Backstops

| Failure mode | What catches it | On after install? |
|---|---|---|
| Secret committed to history | `scan_credentials.py` credential scan | No — enable pre-commit hook or CI |
| Phase skipped with no evidence | `validate.sh` reads work trail, fails on missing phase/evidence | No — run it or put in a hook |
| "Tests pass" with no tests | Your CI running the real suite | Only where CI runs |
| Test recorded passing, then code changed | `record_test_run.py` records exit code + code fingerprint; `/ship` verifies | No — run tests through it |

### Other Mechanisms

- **Skills auto-attached by phase**: push the right checklist by task type (TDD for features, security pass for login code).
- **Cross-session memory**: decisions & evidence in a single source-of-truth state file.
- **Model-agnostic**: native entries for Claude Code (`CLAUDE.md`), Codex (`AGENTS.md`), Gemini (`GEMINI.md`); works with Cursor, Copilot, etc.
- **Token-efficient**: risk-scaled governance; tiny fixes skip heavy guardrails (~5,000 tokens).
- `⚡ ACX` runtime marker + `gate:` block (`gate / classification / verdict / missing`).

### Takeaway

**"Rules get ignored; gates must be enforced"** is the most important delivery warning. For a workflow to truly work, it needs physical constraints an agent can't bypass — git hooks, validators, CI.

---

## 6. Reference Baseline: cilangzzz/software-dev-ai-workflow

- **Stars**: ~48 ｜ **License**: MIT ｜ **Language**: Python
- **Positioning**: AI Agent-driven Claude Code software development workflow framework — "description as delivery".

### Framework Features

- 🔄 **Dual flow**: Waterfall / Agile full process, with quality gates Gate 1-5
- 🏭 **Industry system models**: ERP (12 modules), MES (10+ modules), voice community
- 🔧 **27+ general skills**: SSH, Word, Draw.io, Notion, Jira, ZenTao, etc.
- 🤖 **8-stage end-to-end workflow**: `.claude/` orchestration from requirements to front/back-end dev
- 🧬 **Self-extensible**: `author-skill` meta-skill lets AI create new skills
- 🗂️ **Single source of truth**: auto-generated `catalog.json`, skill index, deliverables by stage/department

### 8 Role Agents

Product, R&D, Testing, Operations, Security, Design, Data, Project Management.

### Takeaway

The three-dimensional **role × stage × deliverable** structure, quality gates Gate 1-5, and auto-generated single-source-of-truth catalog are important prototypes for this hub's unified framework.

---

## 7. Cross-Cutting Insights: 8 Things the Five Frameworks Teach Us

1. **Spec is first-class** (Spec Kit) — clarify what/why before how.
2. **Process adapts to scale/task** (BMAD / Spec Kit) — small changes straight to build, big ones get deep planning.
3. **Role definitions determine output quality** (gstack / BMAD / AI-DLC) — constrain AI judgment with professional identities.
4. **Audit & traceability are enterprise necessities** (AI-DLC) — 134-event trail, approval gates, source-bound evidence.
5. **Rules get ignored; gates must be enforced** (Agentic OS) — git hooks + validators + CI are real constraints.
6. **Context must persist across sessions** (BMAD / Agentic OS) — decisions survive conversation end.
7. **Convergence/verification loops are indispensable** (Spec Kit converge / Agentic OS ship) — done only when proven consistent.
8. **Toolchains should be model-agnostic** (AI-DLC / Agentic OS) — decouple methodology from specific harness/model.

> These 8 insights + our proprietary closed-loop system form the design basis of the [Unified Workflow Framework](../02-unified-framework/unified-workflow.en.md).
