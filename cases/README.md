# 端到端实战案例集（End-to-End Case Studies）

> 用两个真实感案例，把[统一 10 阶段工作流](../docs/02-unified-framework/unified-workflow.md)从"方法论"变成"看得见的产出物"。
> 每个案例都带真实的 ID、日期、门禁结论、代码、覆盖率数字与 Mermaid 图，可直接对照仓库里的门禁与角色定义来审阅。

[返回首页](../README.md) · [English](./README.en.md) · [统一工作流](../docs/02-unified-framework/unified-workflow.md) · [质量门禁](../docs/02-unified-framework/quality-gates.md) · [闭环体系](../docs/03-user-system/closed-loop-system.md)

---

## 为什么要读案例

方法论文档回答"该怎么干"，案例回答"真实干出来长什么样"。本案例集刻意保留三种"不完美但真实"的细节：

- **门禁失败与返工**：覆盖率第一次 76% 未过 Gate 8，补测后 87% 才放行。
- **审查拦截**：Gate 7 真实发现 3 个问题（1 个 Blocker、2 个 Major），修复后才放行。
- **事后补审批**：线上紧急修复走绿色通道，但 24 小时内补齐变更单与风险评估。

> 核心信念：**能被审计的流程才是好流程**。每个结论都附证据（证据文件、命令输出、指纹、审批记录），而不是一句"已完成"。

---

## 案例一览与对照

| 维度 | 案例一 · OrderHub 电商订单系统 | 案例二 · 登录崩溃紧急修复 |
|---|---|---|
| 文件 | [case-01-ecommerce.md](./case-01-ecommerce.md) | [case-02-hotfix.md](./case-02-hotfix.md) |
| 一句话 | 从想法到上线的完整闭环 | 生产事故下的轻量快速通道 |
| 变更类型 | 新项目 / 功能开发 | 小改动 / 线上 bugfix |
| 起点 | G0（企业级系统，全 10 阶段） | G6（小改动直达构建） |
| 路径 | G0→G1→G2→G3→G4→G5→G6→G7→G8→G9→G10→回到 G3 | G6→G7→G8→G9（事后补审批） |
| 角色参与 | 8 大角色全部登场 | 开发 + 安全 + 测试 + 运维 + 发布经理 |
| 时间跨度 | 2026-09-02 → 2026-11-20（含上线后反馈） | 2026-11-16 02:14 → 05:47（约 3.5 小时） |
| 需求/缺陷 ID | REQ-001 ~ REQ-006，TASK-001 ~ TASK-014 | BUG-2026-1116-001，HF-001 ~ HF-004 |
| 覆盖率 | 87%（首轮 76% 未过，补测后达标） | 仅跑受影响模块，目标 80%，实测 83% |
| 门禁特点 | 全部 11 个 Gate 留痕 | 轻量门禁 + 紧急通道事后补审批 |
| Mermaid 图 | 端到端时序图、ID 溯源流向图、架构图 | 修复时序图 |
| 核心看点 | ID 全链路溯源、ADR、Converged、健康度仪表板、反馈驱动规格修订 | 规模自适应、48h 超时升级、事后补审批 |

两案例对照的目的是说明：**同一套工作流可以按变更规模裁剪**——不要让一个 typo 修复走完 10 阶段，也不要让企业系统跳过审计门禁。这正是[规模自适应原则](../docs/02-unified-framework/unified-workflow.md#规模自适应借鉴-bmad--spec-kit-的三条入口)的落地示范。

---

## 如何使用本案例集

1. **通读主线**：先读 [统一工作流框架](../docs/02-unified-framework/unified-workflow.md)，记住 G0–G10 与对应 Gate。
2. **对照案例一**：按阶段读 [case-01](./case-01-ecommerce.md)，每读一个 Gate，回看[质量门禁表](../docs/02-unified-framework/quality-gates.md#门禁总表)的判据，核对案例里的证据是否满足。
3. **对照案例二**：读 [case-02](./case-02-hotfix.md)，体会"哪些门禁可以裁剪、哪些绝对不能省"（凭证扫描、测试证据、变更审批一个都不能少）。
4. **复用产出物模板**：案例中的 `decision.md`、`ADR-001`、`审查报告`、`converge 报告`、`变更请求单` 均可直接作为团队模板起点。
5. **沿 ID 溯源箭头走一遍**：从 `REQ-003` 出发，看它如何贯穿 `TASK-007` → `OrderService.pay()` → `UT-Order-014` → `v1.0.0-orderhub-release-2026-11-14` —— 这是理解闭环体系的最佳练习。

---

## 案例里的关键术语（与全文一致）

| 术语 | 英文 | 含义 |
|---|---|---|
| 门禁 | Gate | "不达标不放行"的质量检查点（Gate 0–10） |
| 项目宪法 | Constitution | G0 建立、贯穿全程的质量原则与治理基线 |
| 架构决策记录 | ADR (Architecture Decision Record) | 记录"背景-决策-后果"的技术决策文档 |
| 需求 ID 溯源 | ID traceability | 需求 → 任务 → 代码 → 测试 → 发布的全链路绑定 |
| 收敛 | Converged | `/converge` 报告证明实现与规格一致的状态 |
| 健康度仪表板 | Health Dashboard | 展示门禁通过率、覆盖率趋势等指标的流程监控面板 |
| 48h 超时升级 | 48h escalation | 门禁 48 小时未处理自动升级到上一级负责人 |
| 变更流程 | Change process | 在线表单 + AI 评估 + 人工审批的发布管控 |
| 规模自适应 | Scale-adaptive | 按变更大小选择起点与门禁深度 |

---

## 目录

- [案例一：电商订单管理系统 OrderHub（中）](./case-01-ecommerce.md) · [English](./case-01-ecommerce.en.md)
- [案例二：生产环境登录崩溃紧急修复（中）](./case-02-hotfix.md) · [English](./case-02-hotfix.en.md)

---

*所有案例数据为教学演示而构造，但结构、门禁判据与产出物格式完全对齐本仓库的方法论。*
