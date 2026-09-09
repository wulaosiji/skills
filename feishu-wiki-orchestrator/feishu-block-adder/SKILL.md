---
name: feishu-block-adder
description: |
  知识库块添加子技能 / Feishu wiki block adder sub-skill. 将解析后的块数据添加到飞书知识库文档，分批处理以避免 API 限制，支持表格和普通块。
  Use when: "添加知识库块", "add wiki blocks", "批量添加知识库块", "batch add wiki blocks", "知识库表格创建", "wiki table creation", "块写入知识库", "block write to wiki".
  内部组件，由 feishu-wiki-orchestrator 编排调用，每批最多 20 个块，表格单独处理。Cross-references: feishu-wiki-orchestrator, feishu-md-parser, feishu-doc-verifier.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Wiki Block Adder (Sub-skill)

> 将解析后的块数据分批添加到飞书知识库文档，支持表格和普通块。内部组件，由父技能编排调用。

## When to Use

Use this skill when:
- 需要将 `feishu-md-parser` 生成的块数据写入知识库文档时
- 需要分批添加大量块以避免 API 限制时
- 需要在知识库文档中创建表格块时

Do NOT use this skill if:
- 需要独立创建知识库文档 → use `feishu-wiki-orchestrator` (parent) instead
- 需要解析 Markdown → use `feishu-md-parser` instead
- 需要向云盘文档添加块 → use `feishu-doc-orchestrator/feishu-block-adder` instead

Typical triggers:
- 「添加块到知识库文档」「批量写入知识库块」
- "add blocks to wiki doc", "batch wiki block insertion"

## Workflow

1. **探查 (Probe)**
从 `blocks.json` 加载解析后的块数据，从 `doc_info.json` 加载知识库文档 ID。

2. **约束 (Constrain)**
每批最多 20 个块，表格单独处理，普通块批量添加。不支持的块类型跳过并记录。

3. **执行 (Execute)**
分批调用飞书 API 添加块到知识库文档：
```bash
python scripts/block_adder.py workflow/step1_parse/blocks.json workflow/step2_create/doc_info.json output
```

4. **验证 (Verify)**
检查 API 返回结果，确认所有块添加成功，统计成功/失败数量。

5. **交付 (Deliver)**
保存添加结果到 `output/add_result.json`。

## Output

```json
{
  "success": true,
  "document_id": "U2wNd2rMkot6fzxr67ScN7hJn7c",
  "total_blocks": 290,
  "tables_created": 10,
  "regular_blocks": 280,
  "batches": 15,
  "duration_seconds": 5.2
}
```

## Guardrails

**Anti-patterns**
- NEVER 一次性添加超过 20 个块（API 限制）
- Do NOT 将表格块与普通块混合在同一批中
- Do NOT 独立使用本子技能——应由父技能 `feishu-wiki-orchestrator` 编排

**Constraints**
- 当前支持 13 种块类型：text, heading1-6, bullet, ordered, code, quote, divider, table
- Callout 块（block_type: 19）颜色字段必须直接放在 `callout` 对象下，不能嵌套在 `style` 中
- 知识库文档的块添加 API 与云盘文档相同，但文档 token 类型不同

## Related Skills

- **feishu-wiki-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-md-parser** — 上游：解析 Markdown 为块数据
- **feishu-doc-verifier** — 下游：验证知识库文档内容

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
