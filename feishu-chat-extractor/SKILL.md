---
name: feishu-chat-extractor
description: |
  提取并分析飞书群聊历史消息 / Extract and analyze historical chat messages from Feishu/Lark groups. 支持分页、时间范围过滤和内容提取，可生成用户反馈报告和话题分类。
  Use when: "提取聊天记录", "extract chat history", "分析群消息", "analyze group messages", "飞书聊天导出", "feishu chat export", "消息历史检索", "message history retrieval", "用户反馈收集", "user feedback collection".
  支持按时间范围过滤、关键词分析、话题分类，自动处理分页确保完整检索。Cross-references: feishu-chat-monitor, feishu-card-parser, feishu-message-recall.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Chat Extractor

> 提取并分析飞书群聊历史消息——支持分页、时间范围过滤和内容提取。

## When to Use

Use this skill when:
- 需要提取飞书群的完整聊天记录时
- 需要按时间范围过滤和分析群消息时
- 需要从聊天中提取 OpenClaw/Clawdbot 相关讨论时
- 需要基于聊天数据生成用户反馈报告时
- 需要对聊天内容进行关键词分析和话题分类时

Do NOT use this skill if:
- 只需要检查最近是否有遗漏的 @提及 → use `feishu-chat-monitor` instead
- 需要发送消息或语音到群聊 → use `feishu-voice-sender` or `feishu-video-sender` instead
- 需要撤回已发送消息 → use `feishu-message-recall` instead

Typical triggers:
- 「导出这个群的聊天记录」「分析最近一周的群消息」
- "Extract chat history from this Feishu group", "帮我整理群里的用户反馈"

## Workflow

1. **探查 (Probe)**
确认目标群聊 ID、时间范围、是否需要关键词过滤。

2. **约束 (Constrain)**
务必使用 `start_time` 和 `end_time` 参数以确保完整提取，避免因保留策略导致分页遗漏。提取完成后检查 `has_more` 字段，确保所有分页已处理。不降级——数据不完整时报告错误。

3. **证据 (Evidence)**
确定提取范围（全部消息还是按关键词过滤），收集所有必要参数。

4. **执行 (Execute)**
运行提取和分析脚本：
```bash
# 提取聊天记录
python3 scripts/extract_chat.py --chat-id <CHAT_ID> --output chat_data.json

# 分析内容（如需要）
python3 scripts/analyze_content.py --input chat_data.json --keywords openclaw,clawdbot,cron,mcp
```
自动处理分页，确保完整消息检索跨所有时间范围。

5. **验证 (Verify)**
检查消息数量、时间覆盖范围和数据完整性。确认 `has_more` 为 false，所有分页已处理。

6. **交付 (Deliver)**
输出结构化报告并保存到工作区，返回提取摘要和分析结果。

## Output

返回 JSON 格式的聊天数据和结构化分析报告，包含消息列表、时间范围、关键词统计和话题分类。

## Guardrails

**Anti-patterns**
- NEVER 不使用时间范围参数提取（可能导致分页遗漏）
- Do NOT 忽略 `has_more` 字段（可能遗漏后续分页）
- Do NOT 在未验证数据完整性的情况下生成分析报告

**Constraints**
- 保存中间结果以避免重复提取
- 分析前验证数据完整性
- 文档化提取参数以便结果可复现
- 时间范围使用 Unix 时间戳（秒）

## Key Techniques

### Time Range Extraction
```python
params = {
    "container_id": chat_id,
    "container_id_type": "chat",
    "start_time": 1700000000,
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

- **feishu-chat-monitor** — 检查遗漏的 @提及消息
- **feishu-card-parser** — 解析飞书卡片消息为可读文本
- **feishu-message-recall** — 撤回已发送的消息

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
