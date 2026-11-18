# Image Rendering & Embedding Tools

All figures in this repo are **real PNG files** visible directly in Markdown, while the editable Mermaid source is preserved (folded inside `<details>`). These two scripts generate and embed the images from scratch.

## Why

- **Proof with diagrams**: any Markdown reader (VSCode, Typora, GitHub) shows the figures inline — no Mermaid renderer required.
- **Diagrams as code**: Mermaid source stays in the docs; to change a figure, edit the source and re-render.
- **Zero local deps**: renders online via public [Kroki](https://kroki.io) — no Mermaid CLI / Chromium install.

## Pipeline

```
```mermaid blocks in Markdown
        │
        ▼  render_images.py (Kroki online render)
assets/<doc>-<index>.png  +  manifest.json
        │
        ▼  embed_images.py (embed PNG + fold source)
Markdown (PNG inline + expandable Mermaid source)
```

## Usage

### 1. Render images

```bash
python3 scripts/render_images.py
```

- Scans all `*.md` for `mermaid` blocks (50 total).
- Renders each to PNG via Kroki into `assets/`.
- Generates `assets/manifest.json` mapping each block to its image.
- Requires network; a full render takes ~3 minutes.

### 2. Embed images

```bash
python3 scripts/embed_images.py
```

- Reads `manifest.json`, replaces each Mermaid block with: image reference + `<details>`-folded source.
- **Idempotent**: docs already embedded (marked with `<!-- IMG-EMBED -->`) are skipped — safe to re-run.
- Computes relative paths automatically, so `architecture/`, `tests/`, etc. correctly reference `../assets/`.

## Notes

- **Kroki is stricter than GitHub**: e.g. a semicolon `;` inside a Mermaid `Note` line is treated as a statement separator — use a comma. If rendering returns HTTP 400, check the error line Kroki returns.
- **Keep CN/EN sources in sync**: a past mismatch (comma in Chinese, semicolon in English) broke the English render; already fixed. After editing one language's figure, re-render both.
- **Re-render a single image**: either re-run `render_images.py` (full but safe), or use the `render_block()` helper in the script to render one block.

## Image inventory

52 PNGs total:

| Category | Count | Notes |
|---|---:|---|
| Overview figures | 2 | `overview-zh.png` / `overview-en.png`, atop READMEs |
| Architecture | 12 | `architecture-*` |
| Cases | 10 | `cases-*` |
| Testing | 28 | `tests-*` |

See `assets/manifest.json` for the full mapping.
