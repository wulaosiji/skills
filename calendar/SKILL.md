---
name: calendar
description: |
  Google Calendar integration via Google Apps Script Web API.
  Use when checking schedule, viewing today's events, weekly calendar, upcoming meetings, or adding new calendar events.
  Use when: "check my calendar", "what's on my schedule today", "do I have meetings this week", "add event to calendar", "我的日历", "今天有什么安排", "查看日程".
  Supports querying events (today, week, upcoming, date range) and creating new events with guest invites.
---

# Google Calendar Integration

Integration with Google Calendar via Apps Script Web API for checking schedules and managing events.

## When to Use

Use this skill when the user wants to:
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
- 「check my calendar」「what's on my schedule"
- 「add meeting」「create event」「schedule a call"
- 「这周有什么会议」「upcoming events"

## Workflow

### Step 1: Verify Setup

Ensure the user has completed the setup:
- Google Apps Script deployed as web app
- API URL and token configured
- Calendar access permissions granted

If not set up, guide them through `./SETUP.md` first.

### Step 2: Gather Query Requirements

Determine what the user needs:
- **Today's events**: Quick daily overview
- **This week**: Weekly calendar view
- **Upcoming**: Next N hours (default: 4 hours)
- **Date range**: Specific start/end dates
- **Create event**: New meeting with title, time, guests

### Step 3: Execute Calendar Action

Use the appropriate API endpoint:

| Action | Description | Parameters |
|--------|-------------|------------|
| `today` | Today's events | - |
| `week` | This week's events | - |
| `upcoming` | Next N hours | `hours` (default: 4) |
| `range` | Custom date range | `start`, `end` (ISO dates) |
| `create` | Create new event | `title`, `start`, `end`, `guests`, `description`, `location` |

### Step 4: Present Results

Return events in a clear, readable format:
- Event title and time
- Location (if any)
- All-day event indicator

## Guardrails

- Always verify API token is configured before making requests
- Handle expired/invalid tokens gracefully
- Respect user privacy - don't share calendar data with unauthorized parties
- When creating events, confirm details with user before execution
- Guest emails must be valid - invalid emails will fail silently

## API Response Format

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

## Related Skills

- **meeting-scheduler** — For complex scheduling with multiple participants
- **zoom-meeting** — For generating meeting links to include in calendar events

## References

- `SETUP.md` — Setup instructions for Google Apps Script
- `references/calendar-api.gs` — The Apps Script implementation
- `references/clasp-setup.md` — Detailed clasp CLI guide

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
📂 https://github.com/wulaosiji/skills
