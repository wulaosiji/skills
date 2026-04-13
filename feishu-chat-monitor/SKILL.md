---
name: feishu-chat-monitor
description: |
  Check for missed @mentions in Feishu groups and send catch-up responses.
  检查飞书群聊中遗漏的 @提及 消息并发送补回复。

  Use when: 检查遗漏消息, check missed mentions, 补回复飞书, catch-up feishu replies,
  监控@消息, monitor @mentions, 群聊消息检查, group chat monitoring,
  AGI智库群管理, AGI智库 group management, 手动查漏, manual message review,
  批量回复, batch reply, 消息提醒, message reminders.

  Related: feishu-chat-extractor, feishu-message-recall.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Chat Monitor

Manually check Feishu group chats for @mentions that may have been missed and send catch-up responses.

## When to Use

- 离开一段时间后需要检查是否有遗漏的 @提及消息时
- 需要手动触发检查监控群的 @提及消息时
- 需要在 AGI智库 相关群组中补回复时
- 需要批量发送"抱歉刚才在处理其他任务"类补回复时

### Do NOT use this skill if

- 需要提取完整聊天记录进行深度分析 → 使用 `feishu-chat-extractor`
- 需要撤回误发消息 → 使用 `feishu-message-recall`
- 需要主动发送新消息（非补回复）→ 使用 `feishu-group-welcome` 或 `feishu-voice-sender`

### Typical Trigger Phrases

- "帮我看看有没有漏回的 @"
- "Check missed mentions in my Feishu groups"
- "补回复一下刚才的 @消息"
- "检查一下 AGI智库 的 @提及"

## Workflow

1. **Ask for inputs**: 确认需要检查的群聊（默认监控预设群组）
2. **Run monitor script**: 执行检查脚本
   ```bash
   python3 scripts/check_missed_mentions.py
   ```
3. **Scan recent messages**: 检查监控群最近 1 小时内的消息
4. **Identify @mentions**: 找出所有 `@_user_1`（即 @我）的消息
5. **Send catch-up replies**: 自动发送补回复："@[发送者] 抱歉刚才在处理其他任务，现在回复您！请说～"
6. **Report summary**: 返回检查结果摘要（发现多少条遗漏、已回复多少条）

## Guardrails

- 本技能为**手动按需运行**，非定时自动执行
- 只能回复监控列表中的群聊，默认包含 AGI智库-对话群 和 AGI智库-话题群
- 检查时间窗口默认为最近 1 小时，可在脚本中调整
- 已发送的补回复无法撤回，发送前请确认

## Configuration

编辑 `scripts/check_missed_mentions.py` 调整：
- `MONITORED_CHATS`: 监控的群聊列表
- 检查时间窗口（默认：最近 1 小时）
- 补回复消息模板

## Monitored Groups

| Group ID | Group Name |
|----------|------------|
| `oc_60c795e2e04eefc3d09eb49da4df15a5` | AGI智库-对话群 |
| `oc_f682e4cb4d3eab9bc4e284f7650f4796` | AGI智库-话题群 |

## Related Skills

- [feishu-chat-extractor](../feishu-chat-extractor/) - 提取和分析完整聊天记录
- [feishu-message-recall](../feishu-message-recall/) - 撤回已发送的消息

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
