---
name: feishu-group-welcome
description: |
  飞书群聊新成员欢迎工具 / Feishu group welcome bot.
  自动检测新成员并发送欢迎消息，支持批量 @ 多位新成员，分批发送避免消息过长。

  Use when: 群聊欢迎, group welcome message, 新成员欢迎, welcome new members,
  批量@用户, batch mention users, 飞书群管理, feishu group management,
  自动发欢迎语, automated welcome messages, 群助手配置, group assistant config,
  新人 onboarding, new member onboarding, 欢迎语模板, welcome templates.

  Related: feishu-voice-sender, feishu-video-sender, feishu-doc-perm.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Group Welcome Bot

自动检测并欢迎飞书群聊中的新成员，支持批量 @ 和自定义欢迎语。

## When to Use

- 群聊有新成员加入需要发送欢迎消息时
- 需要一次性批量 @ 多位新成员（39人以上）时
- 需要自定义欢迎语模板时
- 需要将欢迎功能集成到群管理助手时

### Do NOT use this skill if

- 需要发送语音或视频欢迎消息 → 使用 `feishu-voice-sender` 或 `feishu-video-sender`
- 需要撤回误发的欢迎消息 → 使用 `feishu-message-recall`
- 需要管理群聊文档权限 → 使用 `feishu-doc-perm`

### Typical Trigger Phrases

- "设置群欢迎语"
- "批量欢迎新成员"
- "Welcome new members in the Feishu group"
- "配置新人入群自动回复"

## Workflow

1. **Ask for inputs**: 确认目标群聊 ID、是否需要自定义欢迎语模板
2. **Check configuration**: 确认 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 已配置
3. **Run welcome check**: 执行欢迎脚本检测新成员
   ```bash
   cd skills/feishu-group-welcome && python3 scripts/welcome_bot.py
   ```
4. **Batch mention**: 如超过 20 人，自动分批发送（每批最多 20 人）
5. **Send welcome messages**: 使用富文本 `at` 标签发送真正的 @ 通知
6. **Log activity**: 记录已欢迎的成员，避免重复发送

## Guardrails

- 飞书 API 只能获取当前群成员列表，无法获取历史加入记录
- 已发送的欢迎消息无法撤回，发送前请确认
- 单条消息 @ 人数无明确上限，但建议分批避免消息过长
- **夜间模式**：23:00-07:00 自动静默，不发送欢迎消息
- 默认冷却时间为 60 分钟，可在 `scripts/config.py` 中调整

## Batch Strategy

| 批次 | 人数 | 内容 |
|------|------|------|
| 第1批 | 1-20人 | 完整欢迎语 + 表情包 |
| 第2批+ | 21-39人+ | 简化文案 "欢迎 @xxx 加入群聊！（第N批）" |

## Usage Examples

```bash
# 基本用法 - 检查并欢迎所有群的新成员
python3 scripts/welcome_bot.py

# 指定群聊
python3 scripts/welcome_bot.py --chat-id oc_60c795e2e04eefc3d09eb49da4df15a5

# 手动欢迎指定用户（用于补欢迎）
python3 scripts/welcome_bot.py --chat-id oc_xxx --users user1,user2,user3
```

## Related Skills

- [feishu-voice-sender](../feishu-voice-sender/) - 发送语音消息
- [feishu-video-sender](../feishu-video-sender/) - 发送视频消息
- [feishu-doc-perm](../feishu-doc-perm/) - 管理群聊文档权限

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
