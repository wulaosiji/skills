---
name: feishu-block-adder
description: |
  块添加子技能 / Feishu block adder sub-skill. 将解析后的块数据添加到飞书文档，分批处理以避免 API 限制，支持表格和普通块。
  Use when: "添加飞书块", "add feishu blocks", "批量添加块", "batch add blocks", "飞书表格创建", "feishu table creation", "块写入文档", "block write to doc".
  内部组件，由 feishu-doc-orchestrator 编排调用，每批最多 20 个块，表格单独处理。Cross-references: feishu-doc-orchestrator, feishu-md-parser, feishu-doc-verifier.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Block Adder (Sub-skill)

> 将解析后的块数据分批添加到飞书文档，支持表格和普通块。内部组件，由父技能编排调用。

## When to Use

Use this skill when:
- 需要将 `feishu-md-parser` 生成的块数据写入飞书文档时
- 需要分批添加大量块以避免 API 限制时
- 需要在文档中创建表格块时

Do NOT use this skill if:
- 需要独立创建文档 → use `feishu-doc-orchestrator` (parent) instead
- 需要解析 Markdown → use `feishu-md-parser` instead
- 需要验证文档 → use `feishu-doc-verifier` instead

Typical triggers:
- 「添加块到飞书文档」「批量写入飞书块」
- "add blocks to feishu doc", "batch block insertion"

## Workflow

1. **探查 (Probe)**
从 `blocks.json` 加载解析后的块数据，从 `doc_info.json` 加载文档 ID。

2. **约束 (Constrain)**
每批最多 20 个块，表格单独处理，普通块批量添加。不支持的块类型跳过并记录。

3. **执行 (Execute)**
分批调用飞书 API 添加块：
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
- Do NOT 独立使用本子技能——应由父技能 `feishu-doc-orchestrator` 编排

**Constraints**
- 当前支持 13 种块类型：text, heading1-6, bullet, ordered, code, quote, divider, table
- Callout 块（block_type: 19）颜色字段必须直接放在 `callout` 对象下，不能嵌套在 `style` 中
- 添加新块类型需同时修改 `feishu-md-parser` 解析逻辑和本技能的有效块类型检查

## Related Skills

- **feishu-doc-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-md-parser** — 上游：解析 Markdown 为块数据
- **feishu-doc-verifier** — 下游：验证文档内容

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
