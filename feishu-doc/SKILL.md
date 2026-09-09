---
name: feishu-doc
description: |
  飞书文档只读工具 / Feishu document read-only tool. 仅用于读取、解析现有飞书文档内容，禁止写入操作。支持快速预览和结构化块提取。
  Use when: "读取飞书文档", "read feishu document", "提取文档内容", "extract document content", "飞书文档预览", "feishu doc preview", "获取表格数据", "get table data", "文档块解析", "document block parsing".
  支持 read / list_blocks / get_block 三种只读操作，严格不支持写入。Cross-references: feishu-doc-orchestrator, feishu-wiki-orchestrator, feishu-doc-converter, feishu-pdf-downloader.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Document Tool (Read-Only)

> 飞书文档**只读**工具——读取、解析文档内容，严格不支持写入。

## When to Use

Use this skill when:
- 需要快速预览飞书文档的纯文本内容时
- 需要提取文档中的表格、图片等结构化数据时
- 需要获取文档中的特定块内容时
- 需要验证文档是否存在且可访问时

Do NOT use this skill if:
- 需要**创建**新文档 → use `feishu-doc-orchestrator` instead
- 需要**修改**现有文档 → use `feishu-doc-orchestrator` instead
- 需要创建到**知识库** → use `feishu-wiki-orchestrator` instead
- 需要下载原始文件 → use `feishu-pdf-downloader` instead

Typical triggers:
- 「帮我读一下这个飞书文档」「提取文档里的表格数据」
- "Read this Feishu document for me", "Get the content from this docx link"

## Workflow

1. **探查 (Probe)**
确认飞书文档 URL 或 doc_token，从 URL `https://xxx.feishu.cn/docx/ABC123def` 提取 `doc_token`。

2. **约束 (Constrain)**
确认本技能为只读操作，不执行任何写入。如需写入，切换到 `feishu-doc-orchestrator`。

3. **证据 (Evidence)**
执行 `read` 操作获取标题、纯文本内容、块统计：
```json
{ "action": "read", "doc_token": "ABC123def" }
```
检查响应中的 `hint` 字段和 `block_types`，判断是否需要进一步提取结构化内容。

4. **执行 (Execute)**
根据需要执行以下操作：
- `list_blocks`：获取完整结构化数据
  ```json
  { "action": "list_blocks", "doc_token": "ABC123def" }
  ```
- `get_block`：精准获取特定部分
  ```json
  { "action": "get_block", "doc_token": "ABC123def", "block_id": "doxcnXXX" }
  ```

5. **验证 (Verify)**
回读返回的块数据，确认内容完整性和表格/图片等结构化元素已正确提取。

6. **交付 (Deliver)**
返回文档内容摘要或结构化数据，清理临时文件。

## Output

返回 JSON 格式的文档内容，包含标题、纯文本、块统计和结构化块数据。示例：
```json
{
  "title": "文档标题",
  "content": "纯文本内容...",
  "block_count": 50,
  "block_types": ["text", "heading", "table"]
}
```

## Guardrails

**Anti-patterns**
- NEVER 执行 `create`、`write`、`append`、`update_block`、`delete_block` 等写入操作
- Do NOT 在本技能中尝试修改文档内容
- 原 `feishu-doc` 的写入操作存在以下问题，因此已禁用：create 和 write 分离容易创建空文档、表格格式不支持、位置控制弱、无原子性保证

**Constraints**
- 本技能**严格只读**，如需写入操作必须使用 `feishu-doc-orchestrator`
- 所有操作通过飞书 Open API 完成，需要有效的应用凭证

## Use Cases

| 需求 | 推荐操作 | 说明 |
|------|----------|------|
| 快速了解文档内容 | `read` | 纯文本，速度快 |
| 需要表格数据 | `list_blocks` | 包含完整结构化数据 |
| 只需要特定部分 | `get_block` | 精准获取，节省 Token |
| 检查文档是否存在 | `read` | 轻量级验证 |

## Related Skills

- **feishu-doc-orchestrator** — 创建和修改飞书文档（写入操作入口）
- **feishu-wiki-orchestrator** — 知识库文档操作
- **feishu-doc-converter** — 文档格式转换（Markdown 互转）
- **feishu-pdf-downloader** — 下载飞书文件为 PDF

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
