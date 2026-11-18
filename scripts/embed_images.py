#!/usr/bin/env python3
"""
embed_images.py — 把渲染好的 PNG 嵌入到对应 Markdown 文档中。

策略：每个 Mermaid 代码块 -> 真实 PNG 图片直接展示 + 折叠的 Mermaid 源码（<details>）。
这样任何 Markdown 阅读器（VSCode / 本地预览 / GitHub）打开即见图，同时保留可编辑源码。

幂等：已嵌入的块（含 <!-- IMG-EMBED --> 标记）会跳过，重复运行安全。
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
MARKER = "<!-- IMG-EMBED -->"


def main():
    manifest = json.load(open(os.path.join(ASSETS, "manifest.json"), encoding="utf-8"))
    by_file = {}
    for item in manifest:
        by_file.setdefault(item["file"], []).append(item)

    changed = 0
    for rel, items in by_file.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print("跳过(文件不存在):", rel)
            continue
        txt = open(path, encoding="utf-8").read()
        if MARKER in txt:
            print("跳过(已嵌入):", rel)
            continue

        md_dir = os.path.dirname(path)
        assets_rel = os.path.relpath(ASSETS, md_dir).replace("\\", "/")

        # 定位所有 mermaid 块
        matches = list(re.finditer(r"```mermaid\s*\n(.*?)```", txt, re.S))
        if len(matches) != len(items):
            print(f"警告: {rel} 块数 {len(matches)} != manifest {len(items)}")

        # 按 index 降序替换，避免位置偏移
        items_sorted = sorted(items, key=lambda x: x["index"], reverse=True)
        for item in items_sorted:
            idx = item["index"]
            m = matches[idx - 1]
            code = m.group(1).rstrip("\n")
            img_name = os.path.basename(item["image"])
            img_path = f"{assets_rel}/{img_name}"
            dtype = item["type"]
            # 尝试从源码里找一句图标题（subgraph 标题或首行注释）
            caption = f"图 {idx} · {dtype}"
            replacement = (
                f"{MARKER}\n"
                f"**{caption}**\n\n"
                f"![{caption}]({img_path})\n\n"
                f"<details>\n"
                f"<summary>查看 Mermaid 源码（可编辑）</summary>\n\n"
                f"```mermaid\n{code}\n```\n\n"
                f"</details>"
            )
            txt = txt[:m.start()] + replacement + txt[m.end():]

        open(path, "w", encoding="utf-8").write(txt)
        changed += 1
        print(f"嵌入 {rel}: {len(items)} 张图")

    print(f"\n完成: {changed} 个文件已嵌入图片")


if __name__ == "__main__":
    main()
