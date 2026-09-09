---
name: feishu-group-welcome
description: |
  飞书群聊新成员欢迎工具 / Feishu group welcome bot. 自动检测新成员并发送欢迎消息，支持批量 @ 多位新成员，分批发送避免消息过长，含夜间静默模式。
  Use when: "群聊欢迎", "group welcome message", "新成员欢迎", "welcome new members", "批量@用户", "batch mention users", "飞书群管理", "feishu group management", "自动发欢迎语", "automated welcome messages".
  支持批量 @（每批最多 20 人）、自定义欢迎语模板、夜间静默模式（23:00-07:00）和冷却时间控制。Cross-references: feishu-voice-sender, feishu-video-sender, feishu-doc-perm, feishu-message-recall.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Group Welcome Bot

> 自动检测并欢迎飞书群聊中的新成员，支持批量 @ 和自定义欢迎语，含夜间静默模式。

## When to Use

Use this skill when:
- 群聊有新成员加入需要发送欢迎消息时
- 需要一次性批量 @ 多位新成员（39人以上）时
- 需要自定义欢迎语模板时
- 需要将欢迎功能集成到群管理助手时

Do NOT use this skill if:
- 需要发送语音或视频欢迎消息 → use `feishu-voice-sender` or `feishu-video-sender` instead
- 需要撤回误发的欢迎消息 → use `feishu-message-recall` instead
- 需要管理群聊文档权限 → use `feishu-doc-perm` instead

Typical triggers:
- 「设置群欢迎语」「批量欢迎新成员」
- "Welcome new members in the Feishu group", "配置新人入群自动回复"

## Workflow

1. **探查 (Probe)**
确认目标群聊 ID、是否需要自定义欢迎语模板。

2. **约束 (Constrain)**
确认 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 已配置。飞书 API 只能获取当前群成员列表，无法获取历史加入记录。已发送的欢迎消息无法撤回，发送前确认。夜间模式（23:00-07:00）自动静默，不发送欢迎消息。默认冷却时间 60 分钟。不降级——不在夜间发送欢迎消息。

3. **证据 (Evidence)**
获取当前群成员列表，与上次记录对比，识别新加入的成员。

4. **执行 (Execute)**
```bash
cd skills/feishu-group-welcome && python3 scripts/welcome_bot.py
```
如超过 20 人，自动分批发送（每批最多 20 人），使用富文本 `at` 标签发送真正的 @ 通知。

5. **验证 (Verify)**
确认欢迎消息已发送，记录已欢迎的成员，避免重复发送。

6. **交付 (Deliver)**
返回欢迎活动日志，更新已欢迎成员记录，清理临时文件。

## Output

返回欢迎活动日志，包含欢迎的新成员数量、涉及的群聊和发送的消息数量。

## Guardrails

**Anti-patterns**
- NEVER 在夜间（23:00-07:00）发送欢迎消息
- Do NOT 重复欢迎已欢迎过的成员
- Do NOT 在单条消息中 @ 过多用户（建议分批，每批最多 20 人）
- 禁止发送欢迎消息后不记录（会导致重复欢迎）

**Constraints**
- 飞书 API 只能获取当前群成员列表，无法获取历史加入记录
- 已发送的欢迎消息无法撤回，发送前请确认
- 单条消息 @ 人数无明确上限，但建议分批避免消息过长
- 夜间模式：23:00-07:00 自动静默，不发送欢迎消息
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

- **feishu-voice-sender** — 发送语音消息
- **feishu-video-sender** — 发送视频消息
- **feishu-doc-perm** — 管理群聊文档权限
- **feishu-message-recall** — 撤回已发送的消息

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
