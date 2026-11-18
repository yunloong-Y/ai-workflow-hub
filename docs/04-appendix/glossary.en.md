# Bilingual Glossary

[Home](../../README.en.md) · [简体中文](./glossary.md)

| English | 中文 | Description |
|---|---|---|
| AI Workflow | AI 工作流 | Structured development process with AI participation |
| Spec-Driven Development (SDD) | 规范驱动开发 | Write spec before code (Spec Kit) |
| AI-Driven Development (AiDD) | AI 驱动开发 | Full-lifecycle AI-involved development (BMAD) |
| Life Cycle (SDLC / AI-DLC) | 生命周期 | Full process from requirements to operations |
| Workflow Profile | 工作流画像 | Preset flow by task type (11 in AI-DLC) |
| Stage / Phase | 阶段 | Major step in the flow |
| Gate | 门禁 | No-pass-without-standard checkpoint |
| Quality Gate | 质量门禁 | Quality-dimension gate (e.g. coverage) |
| Human Approval Gate | 人工审批门 | Gate requiring human approval to proceed |
| Release Criteria | 放行标准 | Criteria to pass a gate |
| Deliverable / Artifact | 产出物 | Document or code produced by a stage |
| Agent Role | 角色 Agent | AI role with a specific function |
| Orchestration | 编排 | Mechanism coordinating agents/stages |
| Single Source of Truth | 单一事实源 | Single authoritative data/doc source |
| Constitution | 项目宪法 | Project-level principles (Spec Kit) |
| Architecture Decision Record (ADR) | 架构决策记录 | Record of architecture decision and rationale |
| User Story | 用户故事 | Requirement from user perspective |
| Acceptance Criteria | 验收标准 | Standard to judge requirement completion |
| Traceability | 溯源 / 可追溯 | Requirement→code→test chain is auditable |
| ID Flow Arrows | ID 流向箭头 | Visualize full-chain ID binding |
| Convergence | 收敛 | Implementation approaches spec (Spec Kit `/converge`) |
| Coverage | 覆盖率 | Ratio of code covered by tests |
| Credential Scan | 凭证扫描 | Detect leaked secrets in code |
| Audit Trail | 审计轨迹 | Full-flow event record (134 events in AI-DLC) |
| Source-Bound Review | 源代码绑定审查 | Review tied to specific sources |
| Machine-Enforced | 机器强制 | Enforced by git hooks/CI, unbypassable by agent |
| Work Trail | 工作轨迹 | Agent's log of phases & evidence |
| Closed Loop | 闭环 | Loop where feedback drives next iteration |
| Feedback Routing | 反馈路由 | Auto-classify & route feedback |
| Exception Escalation | 异常升级 | Auto-escalate if unresolved (48 hours) |
| Health Dashboard | 健康度仪表板 | Board showing real-time process metrics |
| Skill Versioning | 技能版本管理 | Skill iteration (7-day minor / 30-day major) |
| Change Management | 变更管理 | Change entry/analysis/approval process |
| Alert Rules | 告警规则 | Alert trigger & escalation rules |
| Rollback | 回滚 | Revert to previous version on failed release |
| Scale-Adaptive / Right-Sized | 规模自适应 | Process scales with change size (BMAD) |
| Harness | 宿主 / 工具链 | AI coding tool runtime (Claude Code, Cursor, etc.) |
| Model-Agnostic | 模型无关 | Methodology not bound to a specific model/harness |
| Skill | 技能 / 提示词 | Reusable AI instruction unit |
| Template | 模板 | Reusable document skeleton |
| Extension | 扩展 | Add commands/gates to a flow (Spec Kit) |
| Preset | 预设 | Customize flow standards (Spec Kit) |

---

## Core Command Quick Reference (from frameworks)

| Framework | Command | Purpose |
|---|---|---|
| Spec Kit | `/speckit-constitution` | Establish project principles |
| Spec Kit | `/speckit-specify` | Write specification |
| Spec Kit | `/speckit-plan` | Make technical plan |
| Spec Kit | `/speckit-tasks` | Break down tasks |
| Spec Kit | `/speckit-implement` | Implement code |
| Spec Kit | `/speckit-converge` | Convergence verification |
| Spec Kit | `/speckit-bug-assess/fix/test` | Bug-fix loop |
| Spec Kit | `/speckit-assess-*` | Idea assessment |
| AI-DLC | `/aidlc` | Start AI-DLC workflow |
| Agentic OS | `/plan /build /review /test /ship` | Five-step governance workflow |
| BMAD | `bmad-build / bmad-help / bmad status` | Build/help/status |
