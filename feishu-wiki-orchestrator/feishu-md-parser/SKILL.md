---
name: feishu-md-parser
description: |
  知识库Markdown解析子技能 / Feishu wiki markdown parser sub-skill. 将 Markdown 文件解析为飞书知识库文档块格式，输出 JSON 文件，支持25种块类型映射。
  Use when: "解析Markdown为知识库块", "parse markdown to wiki blocks", "Markdown转知识库块格式", "markdown to wiki block format", "知识库块类型映射", "wiki block type mapping", "知识库文档块解析", "wiki document block parsing".
  内部组件，由 feishu-wiki-orchestrator 编排调用，输出 blocks.json 供 feishu-block-adder 使用。Cross-references: feishu-wiki-orchestrator, feishu-block-adder, feishu-doc-converter.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Wiki Markdown Parser (Sub-skill)

> 将 Markdown 文件解析为飞书知识库文档块格式，输出 JSON 文件。支持25种块类型映射。内部组件。

## When to Use

Use this skill when:
- 需要将 Markdown 文件解析为飞书知识库文档块格式时
- 需要将标题、列表、表格、代码块等转换为知识库块时
- 需要清理 Markdown 中的零宽字符和特殊格式时

Do NOT use this skill if:
- 需要添加块到知识库文档 → use `feishu-block-adder` instead
- 需要创建知识库文档 → use `feishu-wiki-orchestrator` (parent) instead
- 需要将知识库文档转为 Markdown → use `feishu-doc-converter` instead

Typical triggers:
- 「解析 Markdown 为知识库块」「转换 Markdown 为知识库块格式」
- "parse markdown to wiki blocks", "convert markdown to wiki format"

## Workflow

1. **探查 (Probe)**
从指定路径读取 Markdown 文件内容。

2. **约束 (Constrain)**
支持的块类型：标题（# - ######）、无序/有序列表、表格、代码块、引用块、粗体/斜体、分割线。不支持的元素跳过并记录。清理零宽字符（\u200b, \u200c, \u200d, \ufeff）。知识库文档与云盘文档使用相同的块格式。

3. **执行 (Execute)**
1. 解析 Markdown 内容为飞书块格式
2. 清理内容（移除零宽字符、清理表格单元格、处理粗体标记）
3. 输出 JSON 文件

```bash
python scripts/md_parser.py input.md output/blocks.json
```

4. **验证 (Verify)**
检查 `blocks.json` 中的块数量、表格数量、标题数量等元数据，确认解析完整。

5. **交付 (Deliver)**
输出 `output/blocks.json`（块数据）和 `output/metadata.json`（解析元数据）。

## Output

```json
{
  "blocks": [
    {
      "block_type": 2,
      "text": {
        "elements": [{"text_run": {"content": "文本内容"}}],
        "style": {}
      }
    },
    {
      "block_type": 31,
      "table": {
        "property": {"row_size": 3, "column_size": 2, "header_row": true},
        "data": [["标题1", "标题2"], ["数据1", "数据2"], ["数据3", "数据4"]]
      }
    }
  ],
  "metadata": {"total_blocks": 50, "table_count": 5, "heading_count": 10}
}
```

## Guardrails

**Anti-patterns**
- NEVER 将 Callout 块的颜色字段嵌套在 `style` 中（必须直接放在 `callout` 对象下）
- Do NOT 保留零宽字符（会导致飞书显示异常）
- Do NOT 独立使用本子技能——应由父技能编排

**Constraints**
- 只传递文件路径，不传递内容
- 输出给 `feishu-doc-creator` 和 `feishu-block-adder`
- 知识库文档与云盘文档共享相同的块格式和解析逻辑
- Callout 块（block_type: 19）使用 Python 展开操作符将样式字段直接展开到 `callout` 下

## Related Skills

- **feishu-wiki-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-block-adder** — 下游：将解析后的块添加到知识库文档
- **feishu-doc-converter** — 反向转换：知识库文档转 Markdown

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
