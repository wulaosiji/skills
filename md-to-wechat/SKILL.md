---
name: md-to-wechat
description: |
  Markdown转微信公众号HTML工具，支持全内联样式、系统字体栈、丰富组件、自定义主题色和元数据，生成微信公众号编辑器兼容的HTML。
  Use when: "Markdown转公众号", "生成公众号HTML", "公众号排版工具", "发微信公众号", "公众号样式", "Markdown to WeChat", "WeChat article formatting", "WeChat HTML", "custom theme colors", "WeChat publishing".
  Cross-references: long-form-writer, image-ocr, infographic-generator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Markdown to WeChat HTML

> 将Markdown格式的文章转换为微信公众号编辑器兼容的HTML格式。

## When to Use

Use this skill when:
- 需要将Markdown文章发布到微信公众号
- 需要自定义公众号文章的主题色
- 生成带样式的公众号HTML内容
- 批量将Markdown文档转为公众号格式
- 需要场景卡片、结论框等特殊组件
- 确保公众号文章在各平台显示一致

Do NOT use this skill if:
- 需要复杂的交互式排版
- 图片需要直接嵌入（微信不支持外部图片URL）
- 需要动态内容或脚本
- 文章超过2万字（微信建议限制）

Typical triggers:
- 「Markdown转公众号」「生成公众号HTML」「公众号排版工具」「发微信公众号」「微信文章转换」「公众号样式」
- "Markdown to WeChat", "Generate WeChat HTML", "WeChat article formatter", "Convert to WeChat format", "WeChat publishing tool", "WeChat style conversion"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的 Markdown 输入文件，确认文章标题、副标题、作者、标签等元数据，以及目标主题色和输出路径。

2. **约束 (Constrain)**: 验证输入完整性，设定边界：全内联样式（不支持CSS变量和伪元素）、文章不超过2万字、外部图片URL需上传素材库。不降级交付物。

3. **证据 (Evidence)**: 每个样式组件的转换规则来自微信公众号编辑器兼容规范。Markdown 语法与公众号样式的映射关系是可复现的转换证据。

4. **执行 (Execute)**: 调用转换脚本生成 HTML，先给影响与结论，再给行动和必要证据。

**准备Markdown内容**
```markdown
# 文章主标题
## 章节标题
### 小节标题
> 引用内容
- 列表项
| 表格 | 数据 |
```

**配置元数据**
```python
converter = MarkdownToWechatConverter(
    title="文章标题",
    subtitle="副标题",
    author="作者名称",
    tags=["标签1", "标签2"]
)
```

**执行转换**
```bash
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md -o output.html
```

**命令行完整参数**
```bash
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md \
  -o output.html \
  -t "文章标题" \
  -s "副标题描述" \
  -a "作者名称" \
  --tags "标签1,标签2,标签3"
```

**Python API**
```python
from skills.md_to_wechat.md_to_wechat import MarkdownToWechatConverter

converter = MarkdownToWechatConverter(title="文章标题", subtitle="副标题", author="作者", tags=["标签1", "标签2"])
with open('input.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()
html = converter.convert(markdown_text)
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——复制HTML到公众号编辑器预览，在iOS和Android真机上检查显示效果，确认样式兼容。

6. **交付 (Deliver)**: 返回生成的 HTML 文件，提示用户上传图片到微信素材库，清理临时文件。

## Supported Markdown Syntax

| Markdown | 公众号样式 |
|----------|-----------|
| `# 标题` | 文章主标题（封面区域） |
| `## 标题` | 章节标题（带金色装饰线） |
| `### 标题` | 小节标题（带左边框） |
| `> 引用` | 引用块（带大引号装饰） |
| `**加粗**` | 黑色加粗文字 |
| `` `代码` `` | 行内代码（珊瑚色） |
| 代码块 | 深色背景代码块 |
| `表格` | 精美表格（深色表头） |
| `- 列表` | 无序列表 |
| `【场景重现】` | 场景卡片（珊瑚色边框） |
| `【结论】` | 结论黑框（深色背景） |

## Style Components

**Chapter Heading (##)**: 带金色装饰线的章节标题。

**Quote Block (>)**: 带大引号装饰的引用块，支持作者署名。
```markdown
> 引用内容
> —— 作者名称
```

**Scene Card（【场景重现】）**: 特殊标记生成珊瑚色边框的场景卡片。

**Conclusion Box（【结论】）**: 深色背景的结论框。

**Theme Colors**: 默认使用金色+珊瑚色主题，可自定义。
```python
colors = {
    'primary': '#d4a574', 'accent': '#e07a5f', 'dark': '#2d3436',
    'text': '#1a1a1a', 'text_secondary': '#666', 'bg_light': '#f5f5f5', 'bg_card': '#f8f9fa',
}
converter = MarkdownToWechatConverter(colors=colors)
```

## Output

- 格式: HTML（全内联样式，微信公众号编辑器兼容）
- 编码: UTF-8
- 默认输出: 与输入文件同名的 `.html` 文件，或通过 `-o` 指定
- 兼容性: 微信公众号编辑器、企业微信、微信内置浏览器、iOS/Android/Windows

## Guardrails

**Anti-patterns:**
- NEVER 使用外部图片URL（微信不支持），需上传到微信素材库
- NEVER 文章超过2万字（微信建议限制）
- NEVER 不测试移动端显示效果
- NEVER 忽略微信的样式限制（不支持CSS变量和伪元素）
- Do NOT 使用复杂表格（可能显示异常）

**Limitations**
- 不支持CSS变量和伪元素
- 外部图片URL需上传素材库
- 复杂表格可能显示异常
- 部分特殊字符需转义

**Important Notes**
1. 图片处理: 微信编辑器不支持外部图片URL，需上传到微信素材库
2. 预览测试: 务必在iOS和Android真机预览
3. 字数限制: 单篇文章建议不超过2万字
4. 样式兼容性: 使用全内联样式确保兼容

## Workflow Integration

**长文 → 公众号**
```python
from skills.long_form_writer import expand_outline
from skills.md_to_wechat.md_to_wechat import MarkdownToWechatConverter

markdown_text = expand_outline(outline_path="outline.md")
converter = MarkdownToWechatConverter(title="文章标题", subtitle="副标题", author="作者")
html = converter.convert(markdown_text)
with open("wechat.html", "w", encoding="utf-8") as f:
    f.write(html)
```

## Changelog

- **v1.0.0** (2026-02-14): 初始版本，支持基础Markdown语法转换、场景卡片、结论框等特殊组件、自定义主题色

## Related Skills

- **long-form-writer** — 生成Markdown长文（内容生成上游）
- **image-ocr** — 识别图片文字入文章（素材处理）
- **infographic-generator** — 为公众号文章生成配套信息图（视觉增强）

## About UniqueClub

Part of the UniqueClub toolkit - a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
