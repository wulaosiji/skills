---
name: pdf
description: |
  PDF文件处理全能工具，支持PDF创建、合并、拆分、文本提取、表格提取、OCR识别、加密解密、添加水印等操作。
  
  Use when:
  - 读取或提取PDF文本/表格 read extract PDF text tables
  - 合并多个PDF为一个 merge multiple PDFs
  - 拆分PDF页面 split PDF pages
  - 旋转PDF页面 rotate PDF pages
  - 添加水印 add watermarks
  - 创建新PDF create new PDFs
  - 填写PDF表单 fill PDF forms
  - 加密/解密PDF encrypt decrypt PDFs
  - OCR扫描PDF OCR scanned PDFs
  - 提取PDF图片 extract images from PDF
  
  Cross-references: document-hub, image-ocr, content-extractor, email-sender
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# PDF Processing Guide

Comprehensive PDF processing operations using Python libraries and command-line tools.

## When to Use

### Use This Skill When
- 需要提取PDF中的文本或表格数据
- 合并多个PDF文件为一个
- 将PDF拆分为单页文件
- 旋转PDF页面方向
- 为PDF添加水印
- 创建新的PDF文档
- 处理PDF表单填写
- 对PDF进行加密或解密
- OCR识别扫描版PDF
- 从PDF中提取图片

### Do NOT Use This Skill If
- PDF文件被密码保护且无密码
- 需要复杂的PDF编辑（如修改现有内容）
- PDF文件损坏无法读取
- 需要保留原始PDF的复杂排版

### Typical Trigger Phrases
**Chinese:**
- "提取PDF文字"
- "合并PDF文件"
- "拆分PDF"
- "PDF加水印"
- "PDF转Word"
- "扫描PDF识别"

**English:**
- "Extract PDF text"
- "Merge PDF files"
- "Split PDF"
- "Add watermark to PDF"
- "Convert PDF to Word"
- "OCR scanned PDF"

## Workflow

### Step 1: 确定PDF操作类型
| 操作类型 | 推荐工具 | 复杂度 |
|----------|----------|--------|
| 文本提取 | pdfplumber | 简单 |
| 表格提取 | pdfplumber | 中等 |
| 合并/拆分 | pypdf / qpdf | 简单 |
| 创建PDF | reportlab | 中等 |
| OCR识别 | pytesseract | 复杂 |

### Step 2: 选择合适工具
- **pypdf**: 基础操作（合并、拆分、元数据）
- **pdfplumber**: 文本和表格提取
- **reportlab**: 创建PDF
- **qpdf**: 命令行高级操作

### Step 3: 执行操作
```python
from pypdf import PdfReader, PdfWriter
# 或
import pdfplumber
```

### Step 4: 验证结果
- 检查输出文件完整性
- 验证提取的文本/数据准确性
- 确认格式保持正确

## Guardrails

### Anti-Patterns
- ❌ 使用Unicode上下标字符（会导致黑框）
- ❌ 不验证提取的表格数据
- ❌ 忽略PDF版本兼容性问题
- ❌ 处理大型PDF时不分页处理

### Limitations
- 扫描版PDF需要OCR才能提取文本
- 复杂排版可能丢失格式
- 某些PDF字体嵌入问题
- 加密PDF需要密码

### Important Notes
1. **Subscripts/Superscripts**: 使用 `<sub>` 和 `<super>` 标签，不要用Unicode字符
2. **Table Extraction**: 复杂表格可能需要手动调整
3. **OCR Quality**: 依赖图片清晰度

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

# Read a PDF
reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Extract text
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Python Libraries

### pypdf - Basic Operations

#### Merge PDFs
```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Split PDF
```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

#### Extract Metadata
```python
reader = PdfReader("document.pdf")
meta = reader.metadata
print(f"Title: {meta.title}")
print(f"Author: {meta.author}")
```

#### Rotate Pages
```python
reader = PdfReader("input.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)  # Rotate 90 degrees clockwise
writer.add_page(page)

with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

### pdfplumber - Text and Table Extraction

#### Extract Text with Layout
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

#### Extract Tables
```python
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"Table {j+1} on page {i+1}:")
            for row in table:
                print(row)
```

#### Advanced Table Extraction
```python
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_excel("extracted_tables.xlsx", index=False)
```

### reportlab - Create PDFs

#### Basic PDF Creation
```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter

c.drawString(100, height - 100, "Hello World!")
c.line(100, height - 140, 400, height - 140)

c.save()
```

#### Multi-Page PDF
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Report Title", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Body content", styles['Normal']))
story.append(PageBreak())
story.append(Paragraph("Page 2", styles['Heading1']))

doc.build(story)
```

#### Subscripts and Superscripts
**IMPORTANT**: Never use Unicode subscript/superscript characters. Use ReportLab's XML markup:
```python
from reportlab.platypus import Paragraph

# Subscripts: use <sub> tag
chemical = Paragraph("H<sub>2</sub>O", styles['Normal'])

# Superscripts: use <super> tag  
squared = Paragraph("x<super>2</super>", styles['Normal'])
```

## Command-Line Tools

### pdftotext (poppler-utils)
```bash
# Extract text
pdftotext input.pdf output.txt

# Preserve layout
pdftotext -layout input.pdf output.txt

# Specific pages
pdftotext -f 1 -l 5 input.pdf output.txt  # Pages 1-5
```

### qpdf
```bash
# Merge PDFs
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Split pages
qpdf input.pdf --pages . 1-5 -- pages1-5.pdf

# Rotate pages
qpdf input.pdf output.pdf --rotate=+90:1

# Remove password
qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
```

## Common Tasks

### OCR on Scanned PDFs
```python
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path('scanned.pdf')
text = ""
for i, image in enumerate(images):
    text += f"Page {i+1}:\n"
    text += pytesseract.image_to_string(image)
    text += "\n\n"
```

### Add Watermark
```python
from pypdf import PdfReader, PdfWriter

watermark = PdfReader("watermark.pdf").pages[0]
reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output:
    writer.write(output)
```

### Extract Images
```bash
pdfimages -j input.pdf output_prefix
```

### Password Protection
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("userpassword", "ownerpassword")

with open("encrypted.pdf", "wb") as output:
    writer.write(output)
```

## Quick Reference

| Task | Best Tool | Command/Code |
|------|-----------|--------------|
| Merge PDFs | pypdf | `writer.add_page(page)` |
| Split PDFs | pypdf | One page per file |
| Extract text | pdfplumber | `page.extract_text()` |
| Extract tables | pdfplumber | `page.extract_tables()` |
| Create PDFs | reportlab | Canvas or Platypus |
| Command line merge | qpdf | `qpdf --empty --pages ...` |
| OCR scanned PDFs | pytesseract | Convert to image first |

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **document-hub** | 上级封装 | Word/Excel与PDF互转 |
| **image-ocr** | 辅助工具 | 扫描PDF的OCR识别 |
| **content-extractor** | 内容来源 | 提取内容生成PDF |
| **email-sender** | 下游分发 | 发送PDF附件 |

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
