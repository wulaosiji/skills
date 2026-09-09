---
name: feishu-doc-converter
description: |
  飞书文档格式转换技能 / Feishu document converter. 支持飞书云文档与 Markdown 互转，以及外部链接（微信公众号等）转 Markdown。
  Use when: "飞书文档转Markdown", "feishu doc to markdown", "markdown转飞书", "markdown to feishu", "链接转Markdown", "url to markdown", "微信公众号抓取", "wechat article fetch", "批量文档转换", "batch document conversion".
  支持 doc_to_md() 和 url_to_md() 两种转换方式，覆盖飞书云盘、知识库和外部链接。Cross-references: feishu-doc-orchestrator, feishu-wiki-orchestrator, feishu-doc, feishu-pdf-downloader.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Document Converter

> 飞书文档格式转换技能——文档与 Markdown 互转，外部链接转 Markdown。

## When to Use

Use this skill when:
- 需要将飞书云文档导出为 Markdown 时
- 需要将微信公众号文章等外部链接转为 Markdown 时
- 需要批量转换多个文档或链接时
- 需要将知识库内容导出以便迁移或备份时

Do NOT use this skill if:
- 需要创建新的飞书文档 → use `feishu-doc-orchestrator` instead
- 只需要读取文档内容而不转换格式 → use `feishu-doc` instead
- 需要下载原始 PDF 文件 → use `feishu-pdf-downloader` instead

Typical triggers:
- 「把这个飞书文档转成 Markdown」「导出知识库文档为 MD」
- "Convert this Feishu doc to markdown", "抓取微信文章并转成 Markdown"

## Workflow

1. **探查 (Probe)**
确认源内容类型（飞书文档 URL / 外部链接 / 本地文件）和输出路径。

2. **约束 (Constrain)**
根据源类型选择转换方式，不混用：飞书云盘文档用 API 方式，知识库文档用 Browser 方式，外部链接用 url_to_md。批量转换时逐个处理，避免并发导致封号或限流。

3. **证据 (Evidence)**
确认源 URL 有效且可访问。对于飞书文档，提取 doc_token；对于外部链接，确认页面可抓取。

4. **执行 (Execute)**
运行转换脚本：
```bash
# 文档转 MD
python3 skills/feishu-doc-converter/scripts/convert.py doc "https://feishu.cn/docx/xxx" output.md

# 链接转 MD
python3 skills/feishu-doc-converter/scripts/convert.py url "https://mp.weixin.qq.com/s/xxx" output.md
```

5. **验证 (Verify)**
检查生成的 Markdown 格式和内容完整性，确认标题、表格、代码块等元素正确转换。

6. **交付 (Deliver)**
返回输出文件路径，清理临时文件。

## Output

生成 Markdown 文件，包含转换后的文档内容。Python API 示例：
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

## Guardrails

**Anti-patterns**
- NEVER 对知识库文档使用 API 方式（`doc_to_md`），因为知识库权限模型与云盘不同
- Do NOT 并发批量转换，避免触发飞书限流或封号
- Do NOT 尝试转换需要登录才能访问的私有外部链接

**Constraints**
- 飞书云盘文档推荐使用 API 方式（`doc_to_md`），速度快且无需登录
- 知识库文档统一使用 `url_to_md`（Browser 方式）
- 微信文章抓取复用 `wechat-article-fetcher` 逻辑

## Supported Sources

| 平台 | 状态 | 说明 |
|------|------|------|
| 飞书云盘文档 | ✅ 支持 | API 方式（`doc_to_md`）或 Browser 方式（`url_to_md`） |
| 飞书知识库文档 | ✅ 支持 | Browser 方式（`url_to_md`，推荐） |
| 外部知识库 | ✅ 支持 | Browser 方式（`url_to_md`） |
| 微信公众号 | ✅ 支持 | API 方式（`url_to_md`） |
| 知乎 | 🚧 待实现 | - |
| 普通网页 | 🚧 待实现 | - |

## Related Skills

- **feishu-doc-orchestrator** — 创建飞书文档（Markdown 转飞书文档的写入端）
- **feishu-wiki-orchestrator** — 知识库文档创建
- **feishu-doc** — 只读读取飞书文档
- **feishu-pdf-downloader** — 下载飞书文件

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
