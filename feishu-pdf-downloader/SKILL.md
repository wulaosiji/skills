---
name: feishu-pdf-downloader
description: |
  Download PDF and other files from Feishu/Lark cloud drive using file token.
  通过文件 token 从飞书云盘下载 PDF 及其他文件，支持自动凭证加载。

  Use when: 下载飞书文件, download feishu files, 飞书PDF下载, feishu pdf download,
  云盘文件导出, cloud drive export, 提取飞书文档, extract feishu documents,
  文件token下载, file token download, 批量下载, batch download,
  文档离线处理, offline document processing.

  Related: feishu-doc, feishu-doc-converter.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu PDF Downloader

Download files from Feishu (Lark) cloud drive using the Open API.

## When to Use

- 需要从飞书云盘下载 PDF 或其他文件到本地时
- 已知文件 token 需要批量下载多个文件时
- 需要提取飞书存储的文档进行离线处理时
- 需要配合 PDF 处理工具进行后续文本提取或 OCR 时

### Do NOT use this skill if

- 需要读取飞书文档内容而不下载文件 → 使用 `feishu-doc`
- 需要将文档转换为 Markdown → 使用 `feishu-doc-converter`
- 需要创建新文档 → 使用 `feishu-doc-orchestrator`

### Typical Trigger Phrases

- "帮我把飞书云盘的文件下载下来"
- "Download this file from Feishu drive"
- "提取飞书 PDF 到本地"
- "根据 file_token 下载文档"

## Workflow

1. **Ask for inputs**: 确认文件 token 和期望的本地保存路径
2. **Verify credentials**: 确保 `~/.openclaw/.env` 中包含有效的 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`
3. **Get token**: 调用飞书认证 API 获取 tenant_access_token
4. **Download file**: 调用下载 API 获取文件二进制内容
   ```bash
   python3 skills/feishu-pdf-downloader/scripts/download_feishu_pdf.py <file_token> [output_path]
   ```
5. **Save locally**: 将内容写入本地文件
6. **Validate**: 检查文件大小和完整性
7. **Report result**: 返回本地文件路径

## Guardrails

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

- [feishu-doc](../feishu-doc/) - 只读读取飞书文档内容
- [feishu-doc-converter](../feishu-doc-converter/) - 将飞书文档转换为 Markdown

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
