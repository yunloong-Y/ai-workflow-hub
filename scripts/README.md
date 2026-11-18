# 图片渲染与嵌入工具

本仓库所有配图都是**真实 PNG 文件**，打开 Markdown 即可见；同时保留可编辑的 Mermaid 源码（折叠在 `<details>` 中）。本目录的两个脚本负责从零生成并嵌入这些图片。

## 为什么这么做

- **有图有真相**：本地 VSCode、Typora、GitHub 任何阅读器打开 md 都能直接看到图，不再依赖 Mermaid 渲染器。
- **图即代码**：Mermaid 源码仍嵌在文档里，改图只需改源码后重新渲染。
- **零本地依赖**：用公共 [Kroki](https://kroki.io) 服务在线渲染，无需安装 Mermaid CLI / Chromium。

## 工作流

```
Markdown 里的 ```mermaid 块
        │
        ▼  render_images.py（Kroki 在线渲染）
assets/<文档>-<序号>.png  +  manifest.json
        │
        ▼  embed_images.py（图片嵌入 + 源码折叠）
Markdown（PNG 直接展示 + Mermaid 源码可展开）
```

## 使用方法

### 1. 渲染图片

```bash
python3 scripts/render_images.py
```

- 扫描全仓库 `*.md` 中的 `mermaid` 代码块（共 50 个）。
- 逐个调用 Kroki 渲染成 PNG，写入 `assets/`。
- 生成 `assets/manifest.json`，记录每个块与图片的映射。
- 需要联网；单次渲染约 3 分钟。

### 2. 嵌入图片

```bash
python3 scripts/embed_images.py
```

- 读取 `manifest.json`，把每个 Mermaid 块替换为：图片引用 + `<details>` 折叠的源码。
- **幂等**：已嵌入（含 `<!-- IMG-EMBED -->` 标记）的文档会跳过，可安全重复运行。
- 自动计算相对路径，`architecture/`、`tests/` 等子目录均正确引用 `../assets/`。

## 注意事项

- **Kroki 语法比 GitHub 严格**：例如 Mermaid `Note` 文本中不能用分号 `;`（会被当作语句分隔符），要用逗号。若渲染返回 HTTP 400，先看 Kroki 返回的错误行。
- **中英文源码要一致**：曾出现中文版用逗号、英文版用分号导致英文图渲染失败，已修复。改动任一语言版本的图后，建议两边都重新渲染。
- **重新渲染单张图**：改动某个块后，可只重跑 `render_images.py`（全量较慢但稳妥），或参考脚本里的 `render_block()` 函数单独渲染。

## 图片清单

共 52 张 PNG：

| 类别 | 数量 | 说明 |
|---|---:|---|
| 门面总览图 | 2 | `overview-zh.png` / `overview-en.png`，放在 README 顶部 |
| 架构图 | 12 | `architecture-*` |
| 实战案例图 | 10 | `cases-*` |
| 测试体系图 | 28 | `tests-*` |

映射明细见 `assets/manifest.json`。
