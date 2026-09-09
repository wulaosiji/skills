---
name: feishu-pdf-downloader
description: |
  通过文件 token 从飞书云盘下载 PDF 及其他文件 / Download PDF and other files from Feishu/Lark cloud drive using file token. 支持自动凭证加载，可批量下载多个文件。
  Use when: "下载飞书文件", "download feishu files", "飞书PDF下载", "feishu pdf download", "云盘文件导出", "cloud drive export", "提取飞书文档", "extract feishu documents", "文件token下载", "file token download".
  通过飞书 Open API 下载文件，支持自动凭证加载，下载后可配合 PDF 处理工具进行文本提取或 OCR。Cross-references: feishu-doc, feishu-doc-converter, feishu-doc-orchestrator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu PDF Downloader

> 通过文件 token 从飞书云盘下载 PDF 及其他文件，支持自动凭证加载。

## When to Use

Use this skill when:
- 需要从飞书云盘下载 PDF 或其他文件到本地时
- 已知文件 token 需要批量下载多个文件时
- 需要提取飞书存储的文档进行离线处理时
- 需要配合 PDF 处理工具进行后续文本提取或 OCR 时

Do NOT use this skill if:
- 需要读取飞书文档内容而不下载文件 → use `feishu-doc` instead
- 需要将文档转换为 Markdown → use `feishu-doc-converter` instead
- 需要创建新文档 → use `feishu-doc-orchestrator` instead

Typical triggers:
- 「帮我把飞书云盘的文件下载下来」「提取飞书 PDF 到本地」
- "Download this file from Feishu drive", "根据 file_token 下载文档"

## Workflow

1. **探查 (Probe)**
确认文件 token 和期望的本地保存路径。从 Web URL 提取 token：`https://xxx.feishu.cn/file/<file_token>`。

2. **约束 (Constrain)**
确保 `~/.openclaw/.env` 中包含有效的 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`。确保应用具备 `drive:file:read` 权限。文件 token 必须有效且文件存在。不降级——凭证缺失时停止并提示用户。

3. **证据 (Evidence)**
确认文件 token 有效，调用飞书认证 API 获取 tenant_access_token。

4. **执行 (Execute)**
调用下载 API 获取文件二进制内容并保存到本地：
```bash
python3 skills/feishu-pdf-downloader/scripts/download_feishu_pdf.py <file_token> [output_path]
```

5. **验证 (Verify)**
检查文件大小和完整性，确认下载的文件非空且格式正确。

6. **交付 (Deliver)**
返回本地文件路径，清理临时文件。

## Output

返回下载的本地文件路径。下载的 PDF 可配合 `pdf` skill 进行文本提取、OCR 或表格提取。

## Guardrails

**Anti-patterns**
- NEVER 在没有 `drive:file:read` 权限的情况下尝试下载
- Do NOT 使用无效的文件 token（下载会失败）
- Do NOT 跳过文件完整性验证

**Constraints**
- 确保应用具备 `drive:file:read` 权限
- 文件 token 必须有效且文件存在，否则下载会失败
- 下载的 PDF 如需 OCR 或表格提取，建议使用 `pdfplumber`、`pdf2image` 等工具

## How to Get File Token

### From Web URL
- `https://xxx.feishu.cn/file/<file_token>`
- `https://xxx.feishu.cn/drive/folder/<folder_token>`

### From API
Use Feishu drive API to list files and get tokens.

## Processing Downloaded PDFs

After downloading, use the `pdf` skill to:
- Extract text: `pdftotext input.pdf output.txt`
- OCR scanned PDFs: Convert to images → pytesseract
- Extract tables: Use pdfplumber

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "FEISHU_APP_ID not set" | Check `~/.openclaw/.env` file format |
| "Failed to get token" | Verify app_id and app_secret are correct |
| "Download failed" | Check file_token is valid and file exists |
| Permission denied | Ensure app has drive:file:read permission |

## Related Skills

- **feishu-doc** — 只读读取飞书文档内容
- **feishu-doc-converter** — 将飞书文档转换为 Markdown
- **feishu-doc-orchestrator** — 创建飞书文档

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
