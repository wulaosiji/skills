---
name: feishu-card-parser
description: |
  飞书卡片消息解析器 / Feishu interactive card parser. 解析飞书 Interactive Card 消息为可读 Markdown 或纯文本格式，支持提取图片、链接、@用户等元素。
  Use when: "解析飞书卡片", "parse feishu card", "卡片消息提取", "card message extraction", "富文本转Markdown", "rich text to markdown", "飞书卡片内容", "feishu card content", "提取图片链接", "extract image links".
  支持 text / lark_md / img / link / at / code_block / url 等元素解析，输出 Markdown 或结构化 JSON。Cross-references: feishu-chat-extractor, feishu-chat-monitor, feishu-message-recall.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Card Parser

> 飞书卡片消息解析器——将飞书的富文本卡片解析为 Markdown 或纯文本格式。

## When to Use

Use this skill when:
- 收到飞书卡片消息需要提取其中文本内容时
- 需要将卡片中的 `lark_md` 格式转换为标准 Markdown 时
- 需要提取卡片中的图片 key、链接、@用户等信息时
- 需要对飞书消息进行结构化处理或归档时

Do NOT use this skill if:
- 需要提取普通文本聊天记录 → use `feishu-chat-extractor` instead
- 需要处理视频或语音消息 → use `feishu-video-sender` or `feishu-voice-sender` instead
- 需要发送卡片消息 → 使用飞书消息发送 API（非本 skill 范畴）

Typical triggers:
- 「解析这个飞书卡片消息」「把卡片内容转成 Markdown」
- "Extract text from this Feishu card", "提取卡片里的图片和链接"

## Workflow

1. **探查 (Probe)**
确认卡片消息 JSON 内容或 JSON 文件路径。

2. **约束 (Constrain)**
输入必须是有效的飞书卡片 JSON 格式。`lark_md` 格式会尽量转换为标准 Markdown，但部分飞书特有语法可能无法完全对应。图片提取后返回的是 `image_key`，如需实际图片文件需配合飞书图片下载 API。不降级——无效 JSON 时报告错误。

3. **证据 (Evidence)**
确认卡片 JSON 结构有效，识别卡片中的元素类型。

4. **执行 (Execute)**
调用解析器处理卡片 JSON：
```bash
python3 skills/feishu-card-parser/card_parser.py --input card.json --format markdown
```
提取文本、图片、链接、@用户、代码块等元素，根据需求输出为 Markdown 或结构化 JSON。

5. **验证 (Verify)**
检查解析结果，确认所有元素已正确提取，Markdown 格式正确。

6. **交付 (Deliver)**
返回解析后的内容和元数据，清理临时文件。

## Output

返回解析后的 Markdown 文本或结构化 JSON，包含提取的文本、图片 key、链接 URL、@用户信息和代码块内容。

## Guardrails

**Anti-patterns**
- NEVER 尝试解析无效的飞书卡片 JSON
- Do NOT 假设 `lark_md` 能完全转换为标准 Markdown（部分飞书特有语法可能丢失）
- Do NOT 将 `image_key` 当作图片 URL（需配合飞书图片下载 API 获取实际图片）

**Constraints**
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

- **feishu-chat-extractor** — 提取和分析聊天记录
- **feishu-chat-monitor** — 监控遗漏的 @提及消息
- **feishu-message-recall** — 撤回已发送的消息

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
