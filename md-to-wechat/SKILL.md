---
name: md-to-wechat
description: |
  Markdown转微信公众号HTML工具，支持全内联样式、系统字体栈、丰富组件、自定义主题色和元数据，生成微信公众号编辑器兼容的HTML。
  
  Use when:
  - Markdown转公众号HTML Markdown to WeChat HTML
  - 公众号文章排版 WeChat article formatting
  - 自定义主题色文章 custom theme colors
  - 批量生成公众号内容 batch WeChat content generation
  - 技术文章发公众号 publish tech articles to WeChat
  - 公众号样式组件 WeChat style components
  
  Cross-references: content-extractor, long-form-writer, document-hub, wechat-article-fetcher, image-ocr
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Markdown to WeChat HTML

将Markdown格式的文章转换为微信公众号编辑器兼容的HTML格式。

## When to Use

### Use This Skill When
- 需要将Markdown文章发布到微信公众号
- 需要自定义公众号文章的主题色
- 生成带样式的公众号HTML内容
- 批量将Markdown文档转为公众号格式
- 需要场景卡片、结论框等特殊组件
- 确保公众号文章在各平台显示一致

### Do NOT Use This Skill If
- 需要复杂的交互式排版
- 图片需要直接嵌入（微信不支持外部图片URL）
- 需要动态内容或脚本
- 文章超过2万字（微信建议限制）

### Typical Trigger Phrases
**Chinese:**
- "Markdown转公众号"
- "生成公众号HTML"
- "公众号排版工具"
- "发微信公众号"
- "微信文章转换"
- "公众号样式"

**English:**
- "Markdown to WeChat"
- "Generate WeChat HTML"
- "WeChat article formatter"
- "Convert to WeChat format"
- "WeChat publishing tool"
- "WeChat style conversion"

## Workflow

### Step 1: 准备Markdown内容
编写标准Markdown格式文章：
```markdown
# 文章主标题
## 章节标题
### 小节标题
> 引用内容
- 列表项
| 表格 | 数据 |
```

### Step 2: 配置元数据
```python
converter = MarkdownToWechatConverter(
    title="文章标题",
    subtitle="副标题",
    author="作者名称",
    tags=["标签1", "标签2"]
)
```

### Step 3: 执行转换
```bash
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md -o output.html
```

### Step 4: 验证与发布
- 复制HTML到公众号编辑器
- 上传图片到微信素材库
- iOS/Android真机预览

## Guardrails

### Anti-Patterns
- ❌ 使用外部图片URL（微信不支持）
- ❌ 文章超过2万字
- ❌ 不测试移动端显示效果
- ❌ 忽略微信的样式限制

### Limitations
- 不支持CSS变量和伪元素
- 外部图片URL需上传素材库
- 复杂表格可能显示异常
- 部分特殊字符需转义

### Important Notes
1. **图片处理**: 微信编辑器不支持外部图片URL，需上传到微信素材库
2. **预览测试**: 务必在iOS和Android真机预览
3. **字数限制**: 单篇文章建议不超过2万字
4. **样式兼容性**: 使用全内联样式确保兼容

## Supported Markdown Syntax

| Markdown | 公众号样式 |
|----------|-----------|
| `# 标题` | 文章主标题（封面区域） |
| `## 标题` | 章节标题（带金色装饰线） |
| `### 标题` | 小节标题（带左边框） |
| `> 引用` | 引用块（带大引号装饰） |
| `**加粗**` | 黑色加粗文字 |
| `` `代码` `` | 行内代码（珊瑚色） |
| `\`\`\`代码块\`\`\`` | 深色背景代码块 |
| `\| 表格 \|` | 精美表格（深色表头） |
| `- 列表` | 无序列表 |
| `【场景重现】` | 场景卡片（珊瑚色边框） |
| `【结论】` | 结论黑框（深色背景） |

## Usage

### Command Line
```bash
# 基本用法
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md

# 指定输出文件
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md -o output.html

# 完整参数
./skills/md-to-wechat/scripts/md-to-wechat.sh input.md \
  -o output.html \
  -t "文章标题" \
  -s "副标题描述" \
  -a "作者名称" \
  --tags "标签1,标签2,标签3"
```

### Python API
```python
from skills.md_to_wechat.md_to_wechat import MarkdownToWechatConverter

# 创建转换器
converter = MarkdownToWechatConverter(
    title="文章标题",
    subtitle="副标题",
    author="作者",
    tags=["标签1", "标签2"]
)

# 转换Markdown
with open('input.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()

html = converter.convert(markdown_text)

# 保存
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)
```

## Style Components

### Chapter Heading (##)
带金色装饰线的章节标题：
```html
<div style="display:flex;align-items:center;gap:12px;">
  <div style="width:6px;height:28px;background:#d4a574;border-radius:3px;"></div>
  <h2>章节标题</h2>
</div>
```

### Quote Block (>)
带大引号装饰的引用块，支持作者署名：
```markdown
> 引用内容
> —— 作者名称
```

### Scene Card（【场景重现】）
特殊标记生成珊瑚色边框的场景卡片：
```markdown
【场景重现】
这里是场景描述内容...
```

### Conclusion Box（【结论】）
深色背景的结论框：
```markdown
【结论】
这里是结论内容...
```

### Table
标准Markdown表格转换为精美样式表格：
```markdown
| 项目 | 费用 | 频率 |
|------|------|------|
| Token | $0.003 | 持续 |
| 服务器 | $20 | 月付 |
```

### Code Block
深色背景的代码块，支持语法高亮：
```markdown
```json
{
  "key": "value"
}
```
```

## Theme Colors

默认使用金色+珊瑚色主题，可自定义：

```python
colors = {
    'primary': '#d4a574',      # 金色 - 主色调
    'accent': '#e07a5f',       # 珊瑚色 - 强调色
    'dark': '#2d3436',         # 深色 - 表格头部
    'text': '#1a1a1a',         # 主文字
    'text_secondary': '#666',  # 次要文字
    'bg_light': '#f5f5f5',     # 浅灰背景
    'bg_card': '#f8f9fa',      # 卡片背景
}

converter = MarkdownToWechatConverter(colors=colors)
```

## Compatibility

- ✅ 微信公众号编辑器
- ✅ 企业微信
- ✅ 微信内置浏览器
- ✅ 支持iOS/Android/Windows

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 内容来源 | 提取内容后发公众号 |
| **long-form-writer** | 内容生成 | 生成Markdown长文 |
| **document-hub** | 格式补充 | 生成Word/PDF版本 |
| **wechat-article-fetcher** | 反向操作 | 抓取公众号文章 |
| **image-ocr** | 辅助识别 | 识别图片文字入文章 |

## Workflow Integration

### Workflow: 长文 → 公众号
```python
from skills.long_form_writer import expand_outline
from skills.md_to_wechat.md_to_wechat import MarkdownToWechatConverter

# 生成长文
markdown_text = expand_outline(outline_path="outline.md")

# 转换为公众号HTML
converter = MarkdownToWechatConverter(
    title="文章标题",
    subtitle="副标题",
    author="作者"
)
html = converter.convert(markdown_text)

# 保存
with open("wechat.html", "w", encoding="utf-8") as f:
    f.write(html)
```

## Changelog

- **v1.0.0** (2026-02-14)
  - 初始版本
  - 支持基础Markdown语法转换
  - 支持场景卡片、结论框等特殊组件
  - 支持自定义主题色

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
