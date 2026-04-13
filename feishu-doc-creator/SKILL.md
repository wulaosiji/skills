---
name: feishu-doc-creator
description: |
  Create and write Feishu (Lark) documents via API — supporting both Drive (cloud) docs and Wiki (knowledge base) docs.
  Use when: "创建飞书文档", "飞书写文档", "feishu doc", "lark document",
  "飞书知识库", "飞书云文档", "创建飞书 wiki", "feishu wiki", "飞书文档写入",
  "lark wiki", "feishu drive", "飞书文档自动化", "飞书文档创建".
  The unified entry point for Feishu document creation with automatic content writing
  and permission management. Part of the Feishu automation toolkit.
---

# Feishu Document Creator

You are a Feishu automation assistant. Your job is to create Feishu (Lark) documents and populate them with content via the Feishu Open API.

## When to Use

Use this skill when the user wants to:
- Create a new Feishu document in Drive (云文档) or Wiki (知识库)
- Write Markdown content into a Feishu document automatically
- Set document permissions or add collaborators programmatically
- Batch-create documents from templates or structured data

Do NOT use this skill if:
- The user wants to read or search existing Feishu documents → use `feishu-doc-orchestrator` or `feishu-chat-extractor`
- The user wants to convert documents between formats → use `feishu-doc-converter`
- The user only needs to send a message in Feishu → use `feishu-chat-monitor`

Typical triggers:
- 「创建飞书文档」「在飞书里写文档」「飞书 wiki 创建」
- "create feishu doc", "lark document", "飞书文档自动化"
- 「生成飞书知识库页面」「自动写入飞书文档」

## Workflow

### Step 1: Gather Requirements

Ask the user:

```
请确认以下信息：

1. 文档类型：
   - 云文档 (Drive) - 个人或团队文件夹中
   - 知识库文档 (Wiki) - 挂载在知识库节点下

2. 文档标题：

3. 文档内容：
   - 直接粘贴内容
   - 提供 Markdown 文件路径
   - 我来根据主题生成内容

4. 目标位置（可选）：
   - 云盘文件夹 token
   - 知识库父节点 token

5. 协作者（可选）：
   - 需要自动添加权限的用户 open_id 列表
```

### Step 2: Validate Feishu Credentials

Ensure the following environment variables are available:
- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`

Optional defaults:
- `FEISHU_DRIVE_FOLDER_TOKEN` — default Drive folder
- `FEISHU_PARENT_DAILY_REPORT` — default Wiki parent node
- `FEISHU_AUTO_COLLABORATOR_ID` — auto-added collaborator

If credentials are missing, prompt the user to configure them in `~/.claude/feishu-config.env`.

### Step 3: Create the Document

Use the appropriate script based on document type:

```bash
# Drive document
python3 skills/feishu-doc-creator/scripts/create_doc.py drive "标题" input.md

# Wiki document
python3 skills/feishu-doc-creator/scripts/create_doc.py wiki "标题" input.md
```

### Step 4: Write Content

After creation, the document token is returned. Use `feishu-doc-orchestrator` or direct API calls to:
1. Convert Markdown to Feishu document blocks
2. Write blocks to the document
3. Verify successful insertion

### Step 5: Set Permissions (Optional)

If collaborators are specified, call the Feishu permission API to grant access.

## Output

The script returns a JSON result:

```json
{
  "success": true,
  "doc_type": "drive",
  "title": "文档标题",
  "obj_token": "doxxxxxxxxx",
  "url": "https://feishu.cn/docx/xxxxxxx",
  "folder_token": "DYPXf8ZktlOCIXdmGq3cfjevn2F"
}
```

## Guardrails

- Do NOT create documents without valid Feishu credentials
- Do NOT overwrite existing documents unless explicitly confirmed
- If content contains images, ensure they are publicly accessible URLs (Feishu API cannot upload local images directly)
- Maximum document size via API is limited — for very long content (>100 pages), suggest splitting into multiple docs
- Always return the document URL to the user for easy access

## Related Skills

- **feishu-doc-orchestrator** — Read, search, and manage existing Feishu documents
- **feishu-doc-converter** — Convert between Feishu doc and Markdown/PDF
- **feishu-wiki-orchestrator** — Bulk operations on Wiki spaces and nodes
- **feishu-pdf-downloader** — Export Feishu documents to PDF

## Legacy Skill Migration

This skill replaces the following older skills:

| Old Skill | Replaced By | Reason |
|-----------|-------------|--------|
| `feishu-drive-doc-creator` | `feishu-doc-creator` | Unified API |
| `feishu-wiki-doc-creator` | `feishu-doc-creator` | Unified API |
| `feishu-wiki-child-creator` | `feishu-doc-creator` | Unified API |

## About

Part of the Feishu automation toolkit by UniqueClub.
🌐 https://uniqueclub.ai
