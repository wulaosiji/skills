---
name: feishu-doc
description: |
  Feishu 文档只读工具 / Feishu document read-only tool.
  仅用于读取、解析现有飞书文档内容，禁止写入操作。支持快速预览和结构化块提取。

  Use when: 读取飞书文档, read feishu document, 提取文档内容, extract document content,
  飞书文档预览, feishu doc preview, 获取表格数据, get table data,
  文档块解析, document block parsing, 只读文档, read-only document,
  检查文档存在性, check document existence, 文档内容分析, document content analysis.

  Related: feishu-doc-orchestrator, feishu-wiki-orchestrator, feishu-doc-converter, feishu-pdf-downloader.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Document Tool (Read-Only)

飞书文档**只读**工具。支持读取、解析文档内容。

## When to Use

- 需要快速预览飞书文档的纯文本内容时
- 需要提取文档中的表格、图片等结构化数据时
- 需要获取文档中的特定块内容时
- 需要验证文档是否存在且可访问时

### Do NOT use this skill if

- 需要**创建**新文档 → 使用 `feishu-doc-orchestrator`
- 需要**修改**现有文档 → 使用 `feishu-doc-orchestrator`
- 需要创建到**知识库** → 使用 `feishu-wiki-orchestrator`
- 需要下载原始文件 → 使用 `feishu-pdf-downloader`

### Typical Trigger Phrases

- "帮我读一下这个飞书文档"
- "Read this Feishu document for me"
- "提取文档里的表格数据"
- "Get the content from this docx link"

## Workflow

1. **Ask for inputs**: 确认飞书文档 URL 或 doc_token
2. **Extract token**: 从 URL `https://xxx.feishu.cn/docx/ABC123def` 提取 `doc_token`
3. **Quick read**: 执行 `read` 操作获取标题、纯文本内容、块统计
   ```json
   { "action": "read", "doc_token": "ABC123def" }
   ```
4. **Check hints**: 如果响应中的 `hint` 字段存在，或 `block_types` 包含 `Table` / `Image`，说明需要进一步提取结构化内容
5. **List blocks**（如需要）: 执行 `list_blocks` 获取完整结构化数据
   ```json
   { "action": "list_blocks", "doc_token": "ABC123def" }
   ```
6. **Get specific block**（如需要）: 执行 `get_block` 精准获取特定部分
   ```json
   { "action": "get_block", "doc_token": "ABC123def", "block_id": "doxcnXXX" }
   ```
7. **Return summary**: 返回文档内容摘要或结构化数据

## Guardrails

- 本技能**严格只读**，不支持 `create`、`write`、`append`、`update_block`、`delete_block`
- 如需写入操作，必须使用 `feishu-doc-orchestrator`
- 原 `feishu-doc` 的写入操作存在以下问题，因此已禁用：
  - `create` 和 `write` 分离，容易创建空文档
  - 表格格式不支持
  - 位置控制弱（容易创建到错误位置）
  - 无原子性保证

## Use Cases

| 需求 | 推荐操作 | 说明 |
|------|----------|------|
| 快速了解文档内容 | `read` | 纯文本，速度快 |
| 需要表格数据 | `list_blocks` | 包含完整结构化数据 |
| 只需要特定部分 | `get_block` | 精准获取，节省 Token |
| 检查文档是否存在 | `read` | 轻量级验证 |

## Related Skills

- [feishu-doc-orchestrator](../feishu-doc-orchestrator/) - 创建和修改飞书文档
- [feishu-wiki-orchestrator](../feishu-wiki-orchestrator/) - 知识库文档操作
- [feishu-doc-converter](../feishu-doc-converter/) - 文档格式转换
- [feishu-pdf-downloader](../feishu-pdf-downloader/) - 下载飞书文件

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
