---
name: image-ocr
description: |
  图片OCR识别工具，提取图片中的文字内容，支持中英文混合识别、代码截图优化、表格数据提取，让纯文本模型也能理解图片。
  Use when: "识别图片文字", "OCR提取", "代码截图识别", "图片转文字", "提取图中文字", "批量OCR", "extract text from image", "recognize code screenshot", "batch OCR", "scan document OCR".
  Cross-references: long-form-writer, md-to-wechat, infographic-generator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Image OCR Skill

> 将图片中的文字提取出来，让不支持视觉的模型（如 Qwen-Coder）也能"看懂"图片内容。

## When to Use

Use this skill when:
- 需要提取图片中的文字内容
- 识别代码截图并格式化
- 将表格图片转换为结构化数据
- 让纯文本模型处理图片内容
- 批量处理图片文字提取
- OCR识别扫描文档

Do NOT use this skill if:
- 图片清晰度太低（建议300dpi以上）
- 需要识别手写体（准确率较低）
- 图片包含敏感或私人信息
- 需要实时OCR大量图片

Typical triggers:
- 「识别图片文字」「OCR提取」「代码截图识别」「图片转文字」「提取图中文字」「批量OCR」
- "Extract text from image", "OCR recognition", "Recognize code screenshot", "Image to text", "Batch OCR processing", "Scan document OCR"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的图片输入，确认图片格式、内容类型（普通文字/代码/表格）、目标输出格式和语言设置。

2. **约束 (Constrain)**: 验证图片质量（建议300dpi以上），设定边界：不处理敏感或私人信息、手写体准确率较低需提示。选择合适的OCR引擎，不降级交付物。

3. **证据 (Evidence)**: 每个识别结果附带置信度。OCR引擎的选择基于场景需求（PaddleOCR离线免费、百度OCR更准确支持手写、腾讯OCR多语言）。

4. **执行 (Execute)**: 调用OCR引擎识别图片，先给影响与结论，再给行动和必要证据。

**选择OCR引擎**

| 引擎 | 特点 | 适用场景 |
|------|------|----------|
| PaddleOCR | 离线、免费、中英支持好 | 日常使用、代码识别 |
| Baidu OCR | API、更准确、支持手写 | 手写体、高要求场景 |
| Tencent OCR | API、多语言 | 多语言需求 |

**配置引擎**
```python
# config.json
{"ocr_engine": "paddle", "language": "ch_sim", "save_temp": false}
```

**执行OCR**
```python
from skills.image_ocr.scripts.ocr import recognize
result = recognize("/path/to/image.png")
print(result.text)
```

**命令行使用**
```bash
python3 skills/image-ocr/scripts/ocr.py /path/to/image.png
python3 skills/image-ocr/scripts/ocr.py /path/to/image.png --format markdown --save
```

**Python API**
```python
from skills.image_ocr.ocr_engine import OCREngine
ocr = OCREngine(engine="paddle")
result = ocr.recognize("image.png")
print(result.text)       # 完整文字
print(result.blocks)     # 文字块详情
print(result.confidence) # 置信度
```

**后处理**: 代码格式化、表格结构化、语言检测。

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——关键内容人工复核，检查识别准确率，特别是代码符号（`0`→`O`，`1`→`l`等常见OCR错误）。

6. **交付 (Deliver)**: 返回识别结果（纯文本/Markdown/JSON），清理临时文件。

## Core Capabilities

- 支持多种图片格式（PNG、JPG、WEBP、GIF）
- 中英文混合识别
- 代码截图专用优化
- 表格/结构化数据提取

## Code Screenshot Optimization

针对代码截图的特殊处理：自动检测缩进、修复OCR常见符号错误（`0`→`O`，`1`→`l`）、识别代码语言（Python、JS、Java等）。

## Output Formats

**Plain Text (default)**: 纯文本识别结果。

**Markdown**: 带格式的识别结果（代码块、表格）。

**JSON**: 结构化数据（文字块、置信度、位置）。
```json
{"text": "完整文字", "blocks": [{"text": "第一块", "confidence": 0.98, "position": [x1,y1,x2,y2]}], "language": "ch_sim"}
```

## Output

- **Plain Text** (default): 纯文本识别结果
- **Markdown**: 带格式的识别结果（代码块、表格）
- **JSON**: 结构化数据（文字块、置信度、位置）
- 支持批量处理多张图片

## Guardrails

**Anti-patterns:**
- NEVER 处理低分辨率图片（建议300dpi以上）
- NEVER 不验证识别结果准确性
- NEVER 频繁调用云端API（有费用）
- NEVER 不处理识别错误的情况
- Do NOT 处理包含敏感或私人信息的图片

**Limitations**
- 手写体识别准确率较低
- 复杂排版可能丢失格式
- 艺术字体识别困难
- 需要适当的图片预处理

**Best Practices**
1. 图片质量: 确保300dpi以上分辨率
2. 光线充足: 避免阴影和反光
3. 文字清晰: 确保文字与背景对比度高
4. 结果验证: 关键内容人工复核

## Installation

```bash
pip3 install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Configuration

| 参数 | 选项 | 说明 |
|------|------|------|
| `ocr_engine` | paddle/baidu/tencent | OCR引擎选择 |
| `language` | ch_sim/en/ch_tra | 语言：简体中文/英文/繁体中文 |
| `save_temp` | true/false | 是否保存临时文件 |

## Integration with OpenClaw

**Auto Image-to-Text (Recommended)**: 当用户发送图片时，自动调用OCR提取文字，再将文字传给文本模型处理。

**Explicit Call**: 用户明确要求识别图片内容时调用。

## Troubleshooting

- PaddleOCR安装失败: 使用 Conda 安装 `conda install paddlepaddle -c conda-forge`
- 识别准确率不高: 检查图片清晰度（300dpi以上），尝试不同的 language 配置
- 支持多语言: PaddleOCR默认支持中英，可扩展日韩等

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

## Related Skills

- **long-form-writer** — 基于OCR内容写作（内容加工下游）
- **md-to-wechat** — 将OCR结果转换为公众号格式（输出转换）
- **infographic-generator** — 将OCR提取的数据可视化为信息图（数据可视化）

## About UniqueClub

Part of the UniqueClub toolkit - a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
