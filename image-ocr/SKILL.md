---
name: image-ocr
description: |
  图片OCR识别工具，提取图片中的文字内容，支持中英文混合识别、代码截图优化、表格数据提取，让纯文本模型也能理解图片。
  
  Use when:
  - 提取图片中的文字 extract text from images
  - 代码截图识别 recognize code screenshots
  - 表格图片转结构化数据 convert table images to structured data
  - 让文本模型理解图片内容 make text models understand images
  - 批量图片文字提取 batch image text extraction
  - 文档扫描件OCR OCR scanned documents
  
  Cross-references: content-extractor, document-hub, pdf, long-form-writer, md-to-wechat
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Image OCR Skill

将图片中的文字提取出来，让不支持视觉的模型（如 Qwen-Coder）也能"看懂"图片内容。

## When to Use

### Use This Skill When
- 需要提取图片中的文字内容
- 识别代码截图并格式化
- 将表格图片转换为结构化数据
- 让纯文本模型处理图片内容
- 批量处理图片文字提取
- OCR识别扫描文档

### Do NOT Use This Skill If
- 图片清晰度太低（建议300dpi以上）
- 需要识别手写体（准确率较低）
- 图片包含敏感或私人信息
- 需要实时OCR大量图片

### Typical Trigger Phrases
**Chinese:**
- "识别图片文字"
- "OCR提取"
- "代码截图识别"
- "图片转文字"
- "提取图中文字"
- "批量OCR"

**English:**
- "Extract text from image"
- "OCR recognition"
- "Recognize code screenshot"
- "Image to text"
- "Batch OCR processing"
- "Scan document OCR"

## Workflow

### Step 1: 选择OCR引擎
| 引擎 | 特点 | 适用场景 |
|------|------|----------|
| **PaddleOCR** | 离线、免费、中英支持好 | 日常使用、代码识别 |
| **Baidu OCR** | API、更准确、支持手写 | 手写体、高要求场景 |
| **Tencent OCR** | API、多语言 | 多语言需求 |

### Step 2: 配置引擎
```python
# config.json
{
  "ocr_engine": "paddle",
  "language": "ch_sim",
  "save_temp": false
}
```

### Step 3: 执行OCR
```python
from skills.image_ocr.scripts.ocr import recognize

result = recognize("/path/to/image.png")
print(result.text)
```

### Step 4: 后处理
- 代码格式化
- 表格结构化
- 语言检测

## Guardrails

### Anti-Patterns
- ❌ 处理低分辨率图片
- ❌ 不验证识别结果准确性
- ❌ 频繁调用云端API（有费用）
- ❌ 不处理识别错误的情况

### Limitations
- 手写体识别准确率较低
- 复杂排版可能丢失格式
- 艺术字体识别困难
- 需要适当的图片预处理

### Best Practices
1. **图片质量**: 确保300dpi以上分辨率
2. **光线充足**: 避免阴影和反光
3. **文字清晰**: 确保文字与背景对比度高
4. **结果验证**: 关键内容人工复核

## Installation

```bash
# PaddleOCR（推荐）
pip3 install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或完整版
pip3 install paddlepaddle paddleocr
```

## Core Capabilities

- 🖼️ 支持多种图片格式（PNG、JPG、WEBP、GIF）
- 🔤 中英文混合识别
- 💻 代码截图专用优化
- 📊 表格/结构化数据提取

## Usage

### Command Line
```bash
# 基本用法
python3 skills/image-ocr/scripts/ocr.py /path/to/image.png

# 带选项
python3 skills/image-ocr/scripts/ocr.py /path/to/image.png --format markdown --save
```

### Python API
```python
from skills.image_ocr.ocr_engine import OCREngine

ocr = OCREngine(engine="paddle")
result = ocr.recognize("image.png")

print(result.text)           # 完整文字
print(result.blocks)         # 文字块详情
print(result.confidence)     # 置信度
```

## Output Formats

### Default (Plain Text)
```
这是图片中的文字内容：
第一行文字
第二行文字
```

### Markdown Format
```markdown
## 图片内容识别结果

```python
def hello():
    print("Hello World")
```

表格数据：
| 列1 | 列2 |
|-----|-----|
| A   | B   |
```

### JSON Format
```json
{
  "text": "完整文字",
  "blocks": [
    {"text": "第一块", "confidence": 0.98, "position": [x1,y1,x2,y2]},
    {"text": "第二块", "confidence": 0.95, "position": [x1,y1,x2,y2]}
  ],
  "language": "ch_sim"
}
```

## Code Screenshot Optimization

针对代码截图的特殊处理：
```python
# 自动检测代码并格式化
ocr_result = ocr.recognize(image_path)
if is_code_screenshot(ocr_result):
    formatted = format_as_code(ocr_result)
```

Features:
- 自动检测缩进
- 修复OCR常见符号错误（`0`→`O`，`1`→`l`）
- 识别代码语言（Python、JS、Java等）

## Configuration

```json
{
  "ocr_engine": "paddle",
  "baidu_api_key": "your_key",
  "baidu_secret_key": "your_secret",
  "language": "ch_sim",
  "save_temp": false
}
```

| 参数 | 选项 | 说明 |
|------|------|------|
| `ocr_engine` | paddle/baidu/tencent | OCR引擎选择 |
| `language` | ch_sim/en/ch_tra | 语言：简体中文/英文/繁体中文 |
| `save_temp` | true/false | 是否保存临时文件 |

## Integration with OpenClaw

### Option A: Auto Image-to-Text (Recommended)
```python
if message.type == "image":
    image_path = download_image(message.file_key)
    ocr_result = run_skill("image-ocr", image_path)
    text_prompt = f"用户发了一张图片，内容是：\n{ocr_result}\n请根据以上内容回答..."
    response = query_model("qwen-coder", text_prompt)
```

### Option B: Explicit Call
```
用户：帮我识别这张图里的代码
[图片]
Agent：我来识别一下...
[调用 ocr skill]
Agent：图片里的代码是：...
```

## Troubleshooting

**Q: PaddleOCR安装失败？**
```bash
# 使用 Conda 安装
conda install paddlepaddle -c conda-forge
pip install paddleocr
```

**Q: 识别准确率不高？**
- 检查图片清晰度（300dpi以上）
- 尝试不同的 `language` 配置
- 对于手写体，建议使用百度/腾讯OCR API

**Q: 支持多语言吗？**
- PaddleOCR默认支持中英，可扩展日韩等
- 百度/腾讯API支持更多语言

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 内容提取 | 提取图片内容到文本 |
| **document-hub** | 文档处理 | 将OCR结果生成文档 |
| **pdf** | 格式处理 | PDF扫描件OCR |
| **long-form-writer** | 内容加工 | 基于OCR内容写作 |
| **md-to-wechat** | 输出转换 | 转换为公众号格式 |

## File Structure

```
skills/image-ocr/
├── SKILL.md
├── config.json           # 配置文件
├── ocr_engine.py         # OCR引擎封装
├── post_processor.py     # 后处理（代码格式化等）
└── scripts/
    └── ocr.py           # CLI入口
```

## Changelog

- **v1.0** (2026-02-11): 初始版本，支持 PaddleOCR 和百度OCR

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
