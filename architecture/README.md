# 架构设计图集（Architecture Diagrams）

> "一图胜千言"——本文用 Mermaid 图（GitHub 原生渲染）把这套 AI 工作流体系的架构講清楚。
> 所有图均为源码级文本，可版本控制、可随时修改，改完即渲染。

[返回首页](../README.md) · [English](./README.en.md) · [统一工作流](../docs/02-unified-framework/unified-workflow.md)

---

## 图集导航

| # | 架构图 | 回答的问题 | Mermaid 类型 |
|---|---|---|---|
| 1 | [系统上下文架构](./01-system-context.md) | 这套体系与外部角色/工具如何交互？ | `C4Context` / `flowchart` |
| 2 | [10 阶段工作流架构](./02-workflow-stages.md) | 从想法到上线，流程如何流转？闭环怎么形成？ | `flowchart` |
| 3 | [Agent 编排架构](./03-agent-orchestration.md) | 8 大角色 Agent 如何协作？上下文如何传递？ | `sequenceDiagram` |
| 4 | [ID 溯源数据流](./04-traceability.md) | 一条需求如何贯穿到代码、测试、发布？ | `flowchart` / `graph` |
| 5 | [质量门禁流水线](./05-gate-pipeline.md) | Gate 0-10 如何卡点？哪些是机器强制？ | `flowchart` / `stateDiagram` |

---

## 视图分层（类 C4 模型）

```
┌─────────────────────────────────────────────────────────┐
│ Level 1 · 系统上下文  体系作为一个整体，与谁交互          │  ← 图 1
├─────────────────────────────────────────────────────────┤
│ Level 2 · 工作流/容器  10 阶段主流程与闭环                │  ← 图 2
├─────────────────────────────────────────────────────────┤
│ Level 3 · 组件/编排    Agent 角色、门禁、ID 溯源等内部机制 │  ← 图 3/4/5
└─────────────────────────────────────────────────────────┘
```

---

## 关于 Mermaid

本仓库所有架构图使用 [Mermaid](https://mermaid.js.org/) 语法，写在 Markdown 的 mermaid 代码块（以三个反引号 + mermaid 开头的代码围栏）中。GitHub、GitLab、大部分 Markdown 阅读器都原生支持渲染。

- **可维护**：图即代码，改文字即改图，无需外部绘图工具。
- **可审查**：图的变更可以像代码一样 diff 和 review。
- **零依赖**：不需要上传图片文件或维护图床。

如果在本地阅读器里图没有渲染，请在 GitHub 网页端查看，或安装支持 Mermaid 的 Markdown 插件。
