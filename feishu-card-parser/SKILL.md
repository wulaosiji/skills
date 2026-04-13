---
name: feishu-card-parser
description: |
  飞书卡片消息解析器 / Feishu interactive card parser.
  解析飞书 Interactive Card 消息为可读 Markdown 或纯文本格式。

  Use when: 解析飞书卡片, parse feishu card, 卡片消息提取, card message extraction,
  富文本转Markdown, rich text to markdown, 飞书卡片内容, feishu card content,
  提取图片链接, extract image links, @用户识别, mention recognition,
  消息结构化, message structuring, 卡片转文本, card to text conversion.

  Related: feishu-chat-extractor, feishu-chat-monitor.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Card Parser

飞书卡片消息解析器 — 将飞书的富文本卡片解析为 Markdown 或纯文本格式。

## When to Use

- 收到飞书卡片消息需要提取其中文本内容时
- 需要将卡片中的 `lark_md` 格式转换为标准 Markdown 时
- 需要提取卡片中的图片 key、链接、@用户等信息时
- 需要对飞书消息进行结构化处理或归档时

### Do NOT use this skill if

- 需要提取普通文本聊天记录 → 使用 `feishu-chat-extractor`
- 需要处理视频或语音消息 → 使用 `feishu-video-sender` 或 `feishu-voice-sender`
- 需要发送卡片消息 → 使用飞书消息发送 API（非本 skill 范畴）

### Typical Trigger Phrases

- "解析这个飞书卡片消息"
- "把卡片内容转成 Markdown"
- "Extract text from this Feishu card"
- "提取卡片里的图片和链接"

## Workflow

1. **Ask for inputs**: 确认卡片消息 JSON 内容或 JSON 文件路径
2. **Parse card structure**: 调用解析器处理卡片 JSON
   ```bash
   python3 skills/feishu-card-parser/card_parser.py --input card.json --format markdown
   ```
3. **Extract elements**: 提取文本、图片、链接、@用户、代码块等元素
4. **Convert format**: 根据需求输出为 Markdown 或结构化 JSON
5. **Return result**: 返回解析后的内容和元数据

## Guardrails

- 输入必须是有效的飞书卡片 JSON 格式
- `lark_md` 格式会尽量转换为标准 Markdown，但部分飞书特有语法可能无法完全对应
- 图片提取后返回的是 `image_key`，如需实际图片文件需配合飞书图片下载 API

## Supported Elements

| 标签 | 说明 | 解析方式 |
|------|------|---------|
| `text` | 普通文本 | ✅ 直接提取 |
| `lark_md` | Lark Markdown | ✅ 转换为标准 Markdown |
| `img` | 图片 | ✅ 提取 image_key |
| `link` | 链接 | ✅ 提取 URL |
| `at` | @用户 | ✅ 提取用户ID和名称 |
| `code_block` | 代码块 | ✅ 提取代码内容 |
| `url` | 预览卡片 | ✅ 提取链接和标题 |

## Python API

```python
from skills.feishu_card_parser import parse_card_message, card_to_markdown

# 解析卡片消息
card_json = '{"title":"","content":[[{"tag":"text","text":"内容"}]]}'
result = parse_card_message(card_json)

# 转换为 Markdown
markdown = card_to_markdown(card_json)
```

## Related Skills

- [feishu-chat-extractor](../feishu-chat-extractor/) - 提取和分析聊天记录
- [feishu-chat-monitor](../feishu-chat-monitor/) - 监控遗漏的 @提及消息

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
