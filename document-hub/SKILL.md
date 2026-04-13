---
name: document-hub
description: |
  文档处理统一中心，支持Word、Excel、PDF、Markdown等格式的创建、转换、编辑和批量处理。
  
  Use when:
  - 创建Word/Excel/PDF文档 create Word Excel PDF documents
  - 文档格式转换 document format conversion
  - 批量处理文档 batch document processing
  - 应用文档模板 apply document templates
  - 文档内容编辑 document editing
  - 多媒体文件转换 media format conversion
  
  Cross-references: pdf, content-extractor, email-sender, long-form-writer, md-to-wechat, image-ocr
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Document Hub

处理、生成、发送、转换、编辑 Word、Excel、PDF、Markdown 等文档的统一中心。

## When to Use

### Use This Skill When
- 需要创建Word、Excel、PDF文档
- 进行文档格式转换（Word↔PDF等）
- 批量处理多个文档
- 应用模板生成标准化文档
- 编辑和修改现有文档内容
- 提取文档中的结构化数据
- 多媒体文件格式转换

### Do NOT Use This Skill If
- 需要复杂的排版设计（建议使用专业设计工具）
- 需要处理大型PDF的精细编辑
- 目标格式不支持当前内容类型
- 需要实时协作编辑（建议用在线文档）

### Typical Trigger Phrases
**Chinese:**
- "生成Word文档"
- "Excel表格处理"
- "PDF转换"
- "批量处理文档"
- "文档格式转换"
- "创建报告"

**English:**
- "Create Word document"
- "Process Excel file"
- "Convert to PDF"
- "Batch document processing"
- "Document format conversion"
- "Generate report"

## Workflow

### Step 1: 确定文档需求
- 目标格式（.docx / .xlsx / .pdf / .md）
- 内容结构（标题、段落、表格、图片）
- 是否需要模板

### Step 2: 准备内容数据
```python
content = {
    "title": "文档标题",
    "paragraphs": ["段落1", "段落2"],
    "tables": [...],
}
```

### Step 3: 生成/转换文档
```python
from skills.document_hub.document_hub import write, convert

# 创建文档
write("output.docx", content)

# 格式转换
convert("input.docx", "output.pdf")
```

### Step 4: 验证输出
- 检查文档格式是否正确
- 确认内容完整性
- 验证特殊元素（表格、图片）

## Guardrails

### Anti-Patterns
- ❌ 将不支持的格式强行转换
- ❌ 不验证转换后的文档内容
- ❌ 批量处理时不做异常捕获
- ❌ 忽视不同格式的特性限制

### Limitations
- 复杂排版能力有限
- 某些字体可能不兼容
- 大文件处理速度较慢
- 部分高级PDF特性不支持

### Best Practices
1. **格式适配**: 针对不同格式调整内容结构
2. **异常处理**: 批量操作时捕获单个文件错误
3. **内容验证**: 生成后抽查关键文档
4. **模板复用**: 建立标准化文档模板

## Core Functions

### 文档创建
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

### 格式转换
```python
from skills.document_hub.document_hub import convert

# Word to PDF
convert("input.docx", "output.pdf")

# PDF to images (via hub)
from skills.document_hub.document_hub import get_hub
hub = get_hub()
```

### 批量处理
```python
from skills.document_hub.document_hub import batch_process

files = ["doc1.docx", "doc2.docx", "doc3.docx"]
batch_process(files, operation="convert", target_format="pdf")
```

### 媒体转换
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

### Workflow 1: 内容提取 → 生成Word
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

### Workflow 2: 数据汇总 → Excel
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

### Workflow 3: Word → PDF
```python
from skills.document_hub.document_hub import convert

convert("报告.docx", "报告.pdf")
```

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **pdf** | 专业补充 | 复杂的PDF读取和处理 |
| **content-extractor** | 上游输入 | 提取网络内容生成文档 |
| **email-sender** | 下游分发 | 将文档作为邮件附件发送 |
| **long-form-writer** | 内容生成 | 生成长文后导出文档 |
| **md-to-wechat** | 格式转换 | Markdown转公众号HTML |
| **image-ocr** | 辅助识别 | 提取图片文字到文档 |

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
