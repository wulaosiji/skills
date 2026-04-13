---
name: feishu-doc-converter
description: |
  飞书文档格式转换技能 / Feishu document converter.
  支持飞书云文档与 Markdown 互转，以及外部链接（微信公众号等）转 Markdown。

  Use when: 飞书文档转Markdown, feishu doc to markdown, markdown转飞书, markdown to feishu,
  链接转Markdown, url to markdown, 微信公众号抓取, wechat article fetch,
  批量文档转换, batch document conversion, 知识库导出, wiki export,
  文档迁移, document migration, 飞书内容提取, feishu content extraction.

  Related: feishu-doc-orchestrator, feishu-wiki-orchestrator, feishu-doc, feishu-pdf-downloader.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Document Converter

飞书文档格式转换技能 — 支持文档与 Markdown 互转，以及外部链接转 Markdown。

## When to Use

- 需要将飞书云文档导出为 Markdown 时
- 需要将微信公众号文章等外部链接转为 Markdown 时
- 需要批量转换多个文档或链接时
- 需要将知识库内容导出以便迁移或备份时

### Do NOT use this skill if

- 需要创建新的飞书文档 → 使用 `feishu-doc-orchestrator`
- 只需要读取文档内容而不转换格式 → 使用 `feishu-doc`
- 需要下载原始 PDF 文件 → 使用 `feishu-pdf-downloader`

### Typical Trigger Phrases

- "把这个飞书文档转成 Markdown"
- "导出知识库文档为 MD"
- "Convert this Feishu doc to markdown"
- "抓取微信文章并转成 Markdown"

## Workflow

1. **Ask for inputs**: 确认源内容类型（飞书文档 URL / 外部链接 / 本地文件）和输出路径
2. **Choose method**:
   - 飞书云盘文档 → `doc_to_md()` 或命令行 `convert.py doc`
   - 知识库文档 → `url_to_md()`（Browser 方式）
   - 外部链接（微信公众号等） → `url_to_md()`
3. **Run conversion**:
   ```bash
   # 文档转 MD
   python3 skills/feishu-doc-converter/scripts/convert.py doc "https://feishu.cn/docx/xxx" output.md

   # 链接转 MD
   python3 skills/feishu-doc-converter/scripts/convert.py url "https://mp.weixin.qq.com/s/xxx" output.md
   ```
4. **Validate output**: 检查生成的 Markdown 格式和内容完整性
5. **Return result**: 返回输出文件路径

## Guardrails

- 飞书云盘文档推荐使用 API 方式（`doc_to_md`），速度快且无需登录
- 知识库文档统一使用 `url_to_md`（Browser 方式），因为知识库权限模型与云盘不同
- 微信文章抓取复用 `wechat-article-fetcher` 逻辑
- 批量转换时建议逐个处理，避免并发导致封号或限流

## Supported Sources

| 平台 | 状态 | 说明 |
|------|------|------|
| 飞书云盘文档 | ✅ 支持 | API 方式（`doc_to_md`）或 Browser 方式（`url_to_md`） |
| 飞书知识库文档 | ✅ 支持 | Browser 方式（`url_to_md`，推荐） |
| 外部知识库 | ✅ 支持 | Browser 方式（`url_to_md`） |
| 微信公众号 | ✅ 支持 | API 方式（`url_to_md`） |
| 知乎 | 🚧 待实现 | - |
| 普通网页 | 🚧 待实现 | - |

## Python API

```python
from skills.feishu_doc_converter import doc_to_md, url_to_md

# 云盘文档转 Markdown
md_content = doc_to_md("docx/UD18dxyZfoo4uRx4cTNchIc8nBe")
md_content = doc_to_md("https://feishu.cn/docx/xxx")

# 知识库文档
md_content = doc_to_md("https://uniquecapital.feishu.cn/wiki/xxx")

# 链接转 Markdown
md_content = url_to_md("https://mp.weixin.qq.com/s/xxx")
```

## Related Skills

- [feishu-doc-orchestrator](../feishu-doc-orchestrator/) - 创建飞书文档
- [feishu-wiki-orchestrator](../feishu-wiki-orchestrator/) - 知识库文档创建
- [feishu-doc](../feishu-doc/) - 只读读取飞书文档
- [feishu-pdf-downloader](../feishu-pdf-downloader/) - 下载飞书文件

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
