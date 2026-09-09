---
name: feishu-chat-monitor
description: |
  检查飞书群聊中遗漏的 @提及 消息并发送补回复 / Check for missed @mentions in Feishu groups and send catch-up responses. 手动按需运行，监控预设群组最近 1 小时内的 @提及消息。
  Use when: "检查遗漏消息", "check missed mentions", "补回复飞书", "catch-up feishu replies", "监控@消息", "monitor @mentions", "群聊消息检查", "group chat monitoring", "手动查漏", "manual message review".
  手动按需运行（非定时自动），默认监控 AGI智库 相关群组，检查最近 1 小时内的 @提及并自动发送补回复。Cross-references: feishu-chat-extractor, feishu-message-recall, feishu-group-welcome.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Chat Monitor

> 手动检查飞书群聊中遗漏的 @提及消息并发送补回复。手动按需运行，非定时自动执行。

## When to Use

Use this skill when:
- 离开一段时间后需要检查是否有遗漏的 @提及消息时
- 需要手动触发检查监控群的 @提及消息时
- 需要在 AGI智库 相关群组中补回复时
- 需要批量发送"抱歉刚才在处理其他任务"类补回复时

Do NOT use this skill if:
- 需要提取完整聊天记录进行深度分析 → use `feishu-chat-extractor` instead
- 需要撤回误发消息 → use `feishu-message-recall` instead
- 需要主动发送新消息（非补回复）→ use `feishu-group-welcome` or `feishu-voice-sender` instead

Typical triggers:
- 「帮我看看有没有漏回的 @」「补回复一下刚才的 @消息」
- "Check missed mentions in my Feishu groups", "检查一下 AGI智库 的 @提及"

## Workflow

1. **探查 (Probe)**
确认需要检查的群聊（默认监控预设群组：AGI智库-对话群 和 AGI智库-话题群）。

2. **约束 (Constrain)**
本技能为手动按需运行，非定时自动执行。只能回复监控列表中的群聊。检查时间窗口默认为最近 1 小时。已发送的补回复无法撤回，发送前确认。不降级——不在非监控群聊中发送补回复。

3. **证据 (Evidence)**
执行检查脚本，扫描监控群最近 1 小时内的消息，找出所有 `@_user_1`（即 @我）的消息。

4. **执行 (Execute)**
```bash
python3 scripts/check_missed_mentions.py
```
自动发送补回复："@[发送者] 抱歉刚才在处理其他任务，现在回复您！请说～"

5. **验证 (Verify)**
确认补回复已发送，统计发现多少条遗漏、已回复多少条。

6. **交付 (Deliver)**
返回检查结果摘要，清理临时文件。

## Output

返回检查结果摘要，包含发现的遗漏 @提及数量、已回复数量和涉及的群聊列表。

## Guardrails

**Anti-patterns**
- NEVER 在非监控群聊中发送补回复
- Do NOT 自动定时运行（必须手动按需触发）
- Do NOT 超过默认 1 小时时间窗口（如需更长时间范围，使用 `feishu-chat-extractor`）

**Constraints**
- 本技能为手动按需运行，非定时自动执行
- 只能回复监控列表中的群聊
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

- **feishu-chat-extractor** — 提取和分析完整聊天记录
- **feishu-message-recall** — 撤回已发送的消息
- **feishu-group-welcome** — 群聊欢迎消息管理

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
