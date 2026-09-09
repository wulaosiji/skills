---
name: document-hub
description: |
  文档处理统一中心，支持Word、Excel、PDF、Markdown等格式的创建、转换、编辑、批量处理和多媒体文件转换。
  Use when: "生成Word文档", "Excel表格处理", "PDF转换", "create Word document", "process Excel file", "批量处理文档", "document format conversion", "创建报告".
  提供统一API处理多种文档格式，支持模板应用和批量操作。Cross-references: pdf, content-extractor, email-sender, rss-feed.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Document Hub

> 处理、生成、发送、转换、编辑 Word、Excel、PDF、Markdown 等文档的统一中心。

## When to Use

Use this skill when:
- 需要创建Word、Excel、PDF文档
- 进行文档格式转换（Word↔PDF等）
- 批量处理多个文档
- 应用模板生成标准化文档
- 编辑和修改现有文档内容
- 提取文档中的结构化数据
- 多媒体文件格式转换

Do NOT use this skill if:
- 需要复杂的排版设计（建议使用专业设计工具）
- 需要处理大型PDF的精细编辑 → 使用 pdf skill
- 目标格式不支持当前内容类型
- 需要实时协作编辑（建议用在线文档）

Typical triggers:
- 「生成Word文档」「Excel表格处理」「PDF转换」
- "Create Word document", "Process Excel file", "Convert to PDF"
- 「批量处理文档」「文档格式转换」「创建报告」
- "Batch document processing", "Document format conversion", "Generate report"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认文档目标和约束：
- 目标格式（.docx / .xlsx / .pdf / .md）
- 内容结构（标题、段落、表格、图片）
- 是否需要模板

2. **约束 (Constrain)**
验证输入数据完整性，设定格式边界和不可降级的交付标准。受阻时换通道，不降级交付物。

准备内容数据：
```python
content = {
    "title": "文档标题",
    "paragraphs": ["段落1", "段落2"],
    "tables": [...],
}
```

3. **证据 (Evidence)**
文档内容必须来自用户输入或可追溯数据源，不编造数据。每个表格数据必须有明确来源。

4. **执行 (Execute)**
调用文档处理脚本，先给影响与结论，再给行动和必要证据。
```python
from skills.document_hub.document_hub import write, convert

# 创建文档
write("output.docx", content)

# 格式转换
convert("input.docx", "output.pdf")
```

5. **验证 (Verify)**
用不同于生成路径的方式回读输出——检查文档格式是否正确，确认内容完整性，验证特殊元素（表格、图片）。批量处理时抽查关键文档。

6. **交付 (Deliver)**
返回生成的文档路径，清理临时文件。

## Output

- 创建文档：返回文件路径字符串
- 格式转换：返回输出文件路径
- 批量处理：返回成功/失败状态字典
- Excel数据：接受 `{"sheets": {"Sheet名": {"data": [{"列名": "值"}]}}}` 格式

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- Do NOT 将不支持的格式强行转换
- Do NOT 不验证转换后的文档内容
- Do NOT 批量处理时不做异常捕获
- Do NOT 忽视不同格式的特性限制

**Constraints**
- 复杂排版能力有限
- 某些字体可能不兼容
- 大文件处理速度较慢
- 部分高级PDF特性不支持

**Best Practices**
1. **格式适配**: 针对不同格式调整内容结构
2. **异常处理**: 批量操作时捕获单个文件错误
3. **内容验证**: 生成后抽查关键文档
4. **模板复用**: 建立标准化文档模板

## Core Functions

**文档创建**
```python
from skills.document_hub.document_hub import write

# Word文档
write("document.docx", {
    "title": "标题",
    "paragraphs": ["内容段落1", "内容段落2"]
})

# Excel表格
write("spreadsheet.xlsx", {
    "sheets": {
        "Sheet1": {
            "data": [
                {"列A": "值1", "列B": "值2"},
                {"列A": "值3", "列B": "值4"}
            ]
        }
    }
})
```

**格式转换**
```python
from skills.document_hub.document_hub import convert

# Word to PDF
convert("input.docx", "output.pdf")

# PDF to images (via hub)
from skills.document_hub.document_hub import get_hub
hub = get_hub()
```

**批量处理**
```python
from skills.document_hub.document_hub import batch_process

files = ["doc1.docx", "doc2.docx", "doc3.docx"]
batch_process(files, operation="convert", target_format="pdf")
```

**媒体转换**
```python
from skills.document_hub.document_hub import get_hub

hub = get_hub()
# 视频转音频
hub.convert_media("video.mp4", "audio.mp3")
```

## Supported Formats

| 操作 | 支持格式 | 说明 |
|------|----------|------|
| 创建 | .docx, .xlsx | Word, Excel |
| 转换 | .docx ↔ .pdf | Word与PDF互转 |
| 媒体 | .mp4 ↔ .mp3 | 视频音频转换 |
| 读取 | .docx, .xlsx | 提取内容和数据 |

## Integration Examples

**Workflow 1: 内容提取 → 生成Word**
```python
from skills.content_extractor.content_extractor import extract
from skills.document_hub.document_hub import write

result = extract("https://mp.weixin.qq.com/s/xxx")

doc_content = {
    "title": result.title,
    "paragraphs": [
        f"作者：{result.author}",
        f"发布时间：{result.publish_time}",
        "",
        result.content
    ]
}
write("文章.docx", doc_content)
```

**Workflow 2: 数据汇总 → Excel**
```python
from skills.document_hub.document_hub import write

data = {
    "sheets": {
        "汇总": {
            "data": [
                {"平台": "小宇宙", "标题": "播客1"},
                {"平台": "B站", "标题": "视频1"}
            ]
        }
    }
}
write("内容汇总.xlsx", data)
```

**Workflow 3: Word → PDF**
```python
from skills.document_hub.document_hub import convert

convert("报告.docx", "报告.pdf")
```

## Related Skills

- **pdf** — 专业补充：复杂的PDF读取和处理
- **content-extractor** — 上游输入：提取网络内容生成文档
- **email-sender** — 下游分发：将文档作为邮件附件发送
- **rss-feed** — 数据来源：RSS内容归档到文档

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
