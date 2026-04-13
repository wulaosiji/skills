---
name: feishu-chat-extractor
description: |
  Extract and analyze historical chat messages from Feishu/Lark groups.
  提取并分析飞书群聊历史消息，支持分页、时间范围过滤和内容提取。

  Use when: 提取聊天记录, extract chat history, 分析群消息, analyze group messages,
  飞书聊天导出, feishu chat export, 消息历史检索, message history retrieval,
  OpenClaw讨论分析, openclaw discussion analysis, 用户反馈收集, user feedback collection,
  聊天数据报告, chat data report, 话题分类, topic categorization.

  Related: feishu-chat-monitor, feishu-card-parser.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Chat Extractor

Extract and analyze historical messages from Feishu group chats.

## When to Use

- 需要提取飞书群的完整聊天记录时
- 需要按时间范围过滤和分析群消息时
- 需要从聊天中提取 OpenClaw/Clawdbot 相关讨论时
- 需要基于聊天数据生成用户反馈报告时
- 需要对聊天内容进行关键词分析和话题分类时

### Do NOT use this skill if

- 只需要检查最近是否有遗漏的 @提及 → 使用 `feishu-chat-monitor`
- 需要发送消息或语音到群聊 → 使用 `feishu-voice-sender` 或 `feishu-video-sender`
- 需要撤回已发送消息 → 使用 `feishu-message-recall`

### Typical Trigger Phrases

- "导出这个群的聊天记录"
- "分析最近一周的群消息"
- "Extract chat history from this Feishu group"
- "帮我整理群里的用户反馈"

## Workflow

1. **Ask for inputs**: 确认目标群聊 ID、时间范围、是否需要关键词过滤
2. **Plan scope**: 确定提取范围（全部消息还是按关键词过滤）
3. **Extract messages**: 运行提取脚本
   ```bash
   python3 scripts/extract_chat.py --chat-id <CHAT_ID> --output chat_data.json
   ```
4. **Handle pagination**: 自动处理分页，确保完整消息检索跨所有时间范围
5. **Analyze content**: 运行分析脚本（如需要）
   ```bash
   python3 scripts/analyze_content.py --input chat_data.json --keywords openclaw,clawdbot,cron,mcp
   ```
6. **Validate data**: 检查消息数量、时间覆盖范围和数据完整性
7. **Generate report**: 输出结构化报告并保存到工作区

## Guardrails

- **务必使用 `start_time` 和 `end_time` 参数**以确保完整提取，避免因保留策略导致分页遗漏
- 提取完成后检查 `has_more` 字段，确保所有分页已处理
- 保存中间结果以避免重复提取
- 分析前验证数据完整性
- 文档化提取参数以便结果可复现

## Key Techniques

### Time Range Extraction

```python
params = {
    "container_id": chat_id,
    "container_id_type": "chat",
    "start_time": 1700000000,  # Unix timestamp (seconds)
    "end_time": 1700100000,
    "page_size": 50
}
```

### Pagination Handling

```python
all_messages = []
page_token = None
while True:
    params["page_token"] = page_token
    result = fetch_messages(params)
    all_messages.extend(result["items"])
    if not result["has_more"]:
        break
    page_token = result["page_token"]
```

## Related Skills

- [feishu-chat-monitor](../feishu-chat-monitor/) - 检查遗漏的 @提及消息
- [feishu-card-parser](../feishu-card-parser/) - 解析飞书卡片消息为可读文本

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
