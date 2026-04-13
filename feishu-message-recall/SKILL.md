---
name: feishu-message-recall
description: |
  飞书消息撤回/删除工具 / Feishu message recall tool.
  撤回或删除已发送的普通群消息和话题（Thread）消息，支持批量删除。

  Use when: 撤回飞书消息, recall feishu message, 删除群消息, delete group message,
  批量撤回, batch recall, 话题消息删除, thread message deletion,
  清理误发消息, clean up accidental messages, 消息管理, message management,
  24小时内撤回, recall within 24 hours, 话题清理, thread cleanup.

  Related: feishu-chat-monitor, feishu-group-welcome.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Message Recall

飞书消息撤回/删除工具 — 用于撤回或删除已发送的消息。

## When to Use

- 需要删除自己误发的单条群消息时
- 需要批量删除话题（Thread）中的多条消息时
- 需要清理测试消息或历史垃圾消息时
- 需要查询话题中的消息列表以便选择性删除时

### Do NOT use this skill if

- 需要删除别人发送的消息 → 飞书 API 仅支持删除自己发送的消息
- 消息发送已超过 24 小时 → 可能无法撤回
- 需要撤回系统消息或机器人自动消息 → 权限可能受限

### Typical Trigger Phrases

- "撤回这条消息"
- "删除话题里的消息"
- "批量清理我刚才发的消息"
- "Recall the last Feishu message I sent"

## Workflow

1. **Ask for inputs**: 确认消息 ID（`om_xxx`）或话题 ID（`omt_xxx`），以及是否需要批量删除
2. **Verify permission**: 确认目标消息由当前应用/用户发送
3. **Execute recall**:
   ```bash
   # 删除单条消息
   python3 skills/feishu-message-recall/scripts/recall.py --msg-id om_x100b5741b264fca0c12f636d26d1cdd

   # 删除话题中的所有消息
   python3 skills/feishu-message-recall/scripts/recall.py --thread-id omt_1ae2d7a2164f9ce5
   ```
4. **Validate result**: 确认删除成功，返回成功/失败计数
5. **Report summary**: 返回操作结果摘要

## Guardrails

- **只能删除自己发送的消息**
- 超过 **24 小时**的消息可能无法删除
- 话题消息的删除权限与普通群消息相同
- 批量删除前建议先用 `--list-thread` 查询话题中的消息列表
- 删除操作不可恢复，请谨慎执行

## API Limitations

- `APP_ID` 和 `APP_SECRET` 从环境变量或 `config.py` 读取
- 需要 Python 3.8+ 和 `requests`

## Usage Examples

```bash
# 删除单条消息
python3 skills/feishu-message-recall/scripts/recall.py --msg-id om_xxx

# 删除话题中的所有消息
python3 skills/feishu-message-recall/scripts/recall.py --thread-id omt_xxx

# 查询话题中的消息
python3 skills/feishu-message-recall/scripts/recall.py --list-thread omt_xxx
```

## Related Skills

- [feishu-chat-monitor](../feishu-chat-monitor/) - 检查遗漏的 @提及
- [feishu-group-welcome](../feishu-group-welcome/) - 群聊欢迎消息管理

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
