# 中英术语对照表（Glossary）

[返回首页](../../README.md) · [English](./glossary.en.md)

| 中文 | English | 说明 |
|---|---|---|
| AI 工作流 | AI Workflow | AI 参与的结构化开发流程 |
| 规范驱动开发 | Spec-Driven Development (SDD) | 先写规格再写代码（Spec Kit） |
| AI 驱动开发 | AI-Driven Development (AiDD) | AI 全流程参与的软件开发（BMAD） |
| 生命周期 | Life Cycle (SDLC / AI-DLC) | 从需求到运维的全过程 |
| 工作流画像 | Workflow Profile | 按任务类型预设的流程（AI-DLC 11 种） |
| 阶段 | Stage / Phase | 流程中的大步骤 |
| 门禁 | Gate | 不达标不放行的质量检查点 |
| 质量门禁 | Quality Gate | 质量维度的门禁（如覆盖率） |
| 人工审批门 | Human Approval Gate | 需要人批准才能继续的门禁 |
| 放行标准 | Release Criteria | 通过门禁的判据 |
| 产出物 | Deliverable / Artifact | 阶段产出的文档或代码 |
| 角色 Agent | Agent Role | 承担特定职能的 AI 角色 |
| 编排 | Orchestration | 协调多个 Agent/阶段的机制 |
| 单一事实源 | Single Source of Truth | 唯一权威的数据/文档来源 |
| 项目宪法 | Constitution | 项目级原则与约束（Spec Kit） |
| 架构决策记录 | Architecture Decision Record (ADR) | 记录架构决策及其依据 |
| 用户故事 | User Story | 从用户视角描述的需求 |
| 验收标准 | Acceptance Criteria | 判定需求完成的標準 |
| 溯源 / 可追溯 | Traceability | 需求到代码到测试的链路可查 |
| ID 流向箭头 | ID Flow Arrows | 可视化 ID 全链路绑定 |
| 收敛 | Convergence | 实现与规格趋于一致（Spec Kit `/converge`） |
| 覆盖率 | Coverage | 测试覆盖代码的比例 |
| 凭证扫描 | Credential Scan | 检测代码中的密钥泄露 |
| 审计轨迹 | Audit Trail | 记录全流程事件（AI-DLC 134 事件） |
| 源代码绑定审查 | Source-Bound Review | 审查意见绑定具体来源 |
| 机器强制 | Machine-Enforced | 由 git hook/CI 强制执行，Agent 无法绕过 |
| 工作轨迹 | Work Trail | Agent 留下的阶段与证据记录 |
| 闭环 | Closed Loop | 反馈驱动下一轮迭代的循环 |
| 反馈路由 | Feedback Routing | 按类别自动分流反馈 |
| 异常升级 | Exception Escalation | 超时未处理自动上报（48 小时） |
| 健康度仪表板 | Health Dashboard | 展示流程实时指标的看板 |
| 技能版本管理 | Skill Versioning | 技能的版本迭代（7 天小版/30 天大版） |
| 变更管理 | Change Management | 变更的入口/分析/审批流程 |
| 告警规则 | Alert Rules | 监控告警的触发与升级规则 |
| 回滚 | Rollback | 发布失败时回退到上一版本 |
| 规模自适应 | Scale-Adaptive / Right-Sized | 流程按变更规模伸缩（BMAD） |
| 宿主 / 工具链 | Harness | AI 编码工具运行环境（Claude Code、Cursor 等） |
| 模型无关 | Model-Agnostic | 方法论不绑定特定模型/宿主 |
| 提示词 / 技能 | Skill | 可复用的 AI 指令单元 |
| 模板 | Template | 可复用的文档骨架 |
| 扩展 | Extension | 给流程增加命令/门禁（Spec Kit） |
| 预设 | Preset | 定制流程规范（Spec Kit） |

---

## 核心命令速查（源自各框架）

| 框架 | 命令 | 作用 |
|---|---|---|
| Spec Kit | `/speckit-constitution` | 建立项目原则 |
| Spec Kit | `/speckit-specify` | 编写规格 |
| Spec Kit | `/speckit-plan` | 制定技术计划 |
| Spec Kit | `/speckit-tasks` | 拆解任务 |
| Spec Kit | `/speckit-implement` | 实现代码 |
| Spec Kit | `/speckit-converge` | 收敛验证 |
| Spec Kit | `/speckit-bug-assess/fix/test` | Bug 修复闭环 |
| Spec Kit | `/speckit-assess-*` | 想法评估 |
| AI-DLC | `/aidlc` | 启动 AI-DLC 工作流 |
| Agentic OS | `/plan /build /review /test /ship` | 五步治理工作流 |
| BMAD | `bmad-build / bmad-help / bmad status` | 构建/帮助/状态 |
