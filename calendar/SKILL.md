---
name: calendar
description: |
  Google Calendar集成工具，通过Google Apps Script Web API查询日程、查看今日/本周会议、查询即将到来的事件、创建新日历事件并添加参会人邀请。
  Use when: "查看日历", "今天有什么安排", "我的日程", "check my calendar", "what's on my schedule", "添加日程", "create event", "本周会议".
  支持今日、本周、未来N小时、自定义日期范围查询和事件创建，需一次性配置Apps Script Web App。Cross-references: email-sender, document-hub, daily-report.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Google Calendar Integration

> Integration with Google Calendar via Apps Script Web API for checking schedules and managing events.

## When to Use

Use this skill when:
- Check their schedule or calendar
- View today's events and meetings
- See weekly calendar overview
- Find upcoming events in the next few hours
- Create new calendar events
- Add meeting invites with guests

Do NOT use this skill if:
- The user wants to modify existing events → use Google Calendar directly instead
- The user needs calendar setup → follow `./SETUP.md` first
- The user needs other calendar providers (Outlook, etc.)

Typical triggers:
- 「查看日历」「今天有什么安排」「我的日程」
- "check my calendar", "what's on my schedule", "upcoming events"
- 「这周有什么会议」「添加会议」「创建日程」
- "add meeting", "create event", "schedule a call"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认日历操作类型和时间范围。验证用户已完成配置：
- Google Apps Script deployed as web app
- API URL and token configured
- Calendar access permissions granted

If not set up, guide them through `./SETUP.md` first.

2. **约束 (Constrain)**
确定用户需要的查询类型和参数，设定不可降级的标准——创建事件前必须确认详情。受阻时换通道，不降级交付物。

| Action | Description | Parameters |
|--------|-------------|------------|
| `today` | Today's events | - |
| `week` | This week's events | - |
| `upcoming` | Next N hours | `hours` (default: 4) |
| `range` | Custom date range | `start`, `end` (ISO dates) |
| `create` | Create new event | `title`, `start`, `end`, `guests`, `description`, `location` |

3. **证据 (Evidence)**
每个日程数据必须来自Google Calendar API实际响应，不编造事件。记录查询时间和API响应状态作为可追溯证据。

4. **执行 (Execute)**
调用对应API端点，先给影响与结论，再给行动和必要证据。创建事件时先与用户确认详情再执行。

5. **验证 (Verify)**
用不同于生成路径的方式回读——检查返回的事件列表非空（或明确说明无事件），每个事件有title和start/end字段，创建事件后确认返回成功状态。

6. **交付 (Deliver)**
以清晰可读的格式返回事件列表（标题、时间、地点、全天标识），创建事件返回事件详情。不存储用户日历数据。

## Output

返回JSON格式：
```json
{
  "count": 1,
  "events": [
    {
      "title": "Meeting Name",
      "start": "2026-01-04T09:00:00.000Z",
      "end": "2026-01-04T10:00:00.000Z",
      "location": "Zoom link or address",
      "isAllDay": false
    }
  ]
}
```

创建事件返回创建的事件详情。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 在未确认详情的情况下创建日历事件
- NEVER 与未授权方共享用户日历数据
- Do NOT 忽略过期/无效token的情况，需优雅处理并引导重新配置
- Do NOT 使用无效的参会人邮箱（会静默失败）

**Constraints**
- 必须先配置Google Apps Script Web App才能使用
- 仅支持Google Calendar，不支持Outlook等其他提供商
- 不支持修改现有事件（需直接使用Google Calendar）
- 参会人邮箱必须有效，否则会静默失败

**Privacy Rules**
- Always verify API token is configured before making requests
- Handle expired/invalid tokens gracefully
- Respect user privacy - don't share calendar data with unauthorized parties
- When creating events, confirm details with user before execution

## References

- `SETUP.md` — Setup instructions for Google Apps Script
- `references/calendar-api.gs` — The Apps Script implementation
- `references/clasp-setup.md` — Detailed clasp CLI guide

## Related Skills

- **email-sender** — 发送会议邀请邮件和日程提醒
- **daily-report** — 将日程整合到每日简报中
- **document-hub** — 导出日程为文档格式

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
