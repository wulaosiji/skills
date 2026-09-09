---
name: feishu-doc-creator
description: |
  Create and write Feishu (Lark) documents via API — supporting both Drive (cloud) docs and Wiki (knowledge base) docs. 飞书文档创建统一入口，支持自动内容写入和权限管理。
  Use when: "创建飞书文档", "飞书写文档", "feishu doc", "lark document", "飞书知识库", "飞书云文档", "创建飞书 wiki", "feishu wiki", "飞书文档写入".
  The unified entry point for Feishu document creation with automatic content writing and permission management. Cross-references: feishu-doc-orchestrator, feishu-doc-converter, feishu-wiki-orchestrator, feishu-pdf-downloader.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Document Creator

> 飞书文档创建统一入口——通过 API 创建云文档或知识库文档，并自动写入内容和管理权限。

## When to Use

Use this skill when:
- 需要在飞书云盘（Drive）或知识库（Wiki）中创建新文档时
- 需要将 Markdown 内容自动写入飞书文档时
- 需要以编程方式设置文档权限或添加协作者时
- 需要从模板或结构化数据批量创建文档时

Do NOT use this skill if:
- 需要读取或搜索现有飞书文档 → use `feishu-doc` or `feishu-chat-extractor` instead
- 需要在文档之间转换格式 → use `feishu-doc-converter` instead
- 只需要在飞书中发送消息 → use `feishu-chat-monitor` instead
- 需要完整的文档编排流程（含块解析、验证、日志）→ use `feishu-doc-orchestrator` instead

Typical triggers:
- 「创建飞书文档」「在飞书里写文档」「飞书 wiki 创建」
- "create feishu doc", "lark document", "飞书文档自动化"
- 「生成飞书知识库页面」「自动写入飞书文档」

## Workflow

1. **探查 (Probe)**
确认以下信息：文档类型（云文档 Drive / 知识库 Wiki）、文档标题、文档内容（直接粘贴 / Markdown 文件路径 / 按主题生成）、目标位置（云盘文件夹 token / 知识库父节点 token）、协作者（可选）。

2. **约束 (Constrain)**
验证飞书凭证环境变量 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 可用。可选默认配置：`FEISHU_DRIVE_FOLDER_TOKEN`、`FEISHU_PARENT_DAILY_REPORT`、`FEISHU_AUTO_COLLABORATOR_ID`。凭证缺失时提示用户配置，不降级执行。

3. **证据 (Evidence)**
确认文档类型和目标位置后，选择对应脚本。收集所有必要参数（标题、内容路径、位置 token）。

4. **执行 (Execute)**
使用对应脚本创建文档：
```bash
# Drive document
python3 skills/feishu-doc-creator/scripts/create_doc.py drive "标题" input.md

# Wiki document
python3 skills/feishu-doc-creator/scripts/create_doc.py wiki "标题" input.md
```
创建后将 Markdown 转换为飞书文档块并写入，验证插入成功。如指定协作者，调用权限 API 授予访问。

5. **验证 (Verify)**
回读创建的文档，确认标题、内容和权限均已正确设置。检查返回的 doc_token 和 URL 有效性。

6. **交付 (Deliver)**
返回文档 URL 和创建结果 JSON，清理临时文件。

## Output

脚本返回 JSON 结果：
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

**Anti-patterns**
- NEVER 在没有有效飞书凭证的情况下创建文档
- Do NOT 覆盖现有文档，除非用户明确确认
- Do NOT 尝试通过本技能读取或修改已有文档内容

**Constraints**
- 内容包含图片时，确保图片为公开可访问的 URL（飞书 API 无法直接上传本地图片）
- API 文档大小有限制，超长内容（>100 页）建议拆分为多个文档
- 始终返回文档 URL 供用户访问

## Legacy Skill Migration

本技能替代以下旧技能：

| Old Skill | Replaced By | Reason |
|-----------|-------------|--------|
| `feishu-drive-doc-creator` | `feishu-doc-creator` | Unified API |
| `feishu-wiki-doc-creator` | `feishu-doc-creator` | Unified API |
| `feishu-wiki-child-creator` | `feishu-doc-creator` | Unified API |

## Related Skills

- **feishu-doc-orchestrator** — 完整文档编排流程（解析→创建→添加块→验证→日志）
- **feishu-doc-converter** — 飞书文档与 Markdown/PDF 格式互转
- **feishu-wiki-orchestrator** — 知识库空间和节点的批量操作
- **feishu-pdf-downloader** — 导出飞书文档为 PDF

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
