---
name: feishu-chat-monitor
description: Check for missed @mentions in Feishu groups and send catch-up responses. Use when needing to review recent group messages for @mentions that may have been missed, or when manually checking for遗漏的@消息 in monitored Feishu groups (AGI智库-对话群, AGI智库-话题群).
---

# Feishu Chat Monitor

## Overview

Manually check Feishu group chats for @mentions that may have been missed and send catch-up responses. This skill runs on-demand (not scheduled) to review recent messages and respond to any @mentions that were not previously handled.

## When to Use

- After being away or busy and want to check if any @mentions were missed
- Manually triggered review of group chat @mentions
- Catch-up on conversations in monitored AGI智库 groups

## Monitored Groups

| Group ID | Group Name |
|----------|------------|
| `oc_60c795e2e04eefc3d09eb49da4df15a5` | AGI智库-对话群 |
| `oc_f682e4cb4d3eab9bc4e284f7650f4796` | AGI智库-话题群 |

## Usage

Run the check script to scan for missed @mentions:

```bash
python3 scripts/check_missed_mentions.py
```

### What It Does

1. Checks recent messages in monitored groups (last 1 hour)
2. Identifies messages that @ me (`@_user_1`)
3. Sends a catch-up response: "@[发送者] 抱歉刚才在处理其他任务，现在回复您！请说～"

### Configuration

Edit `scripts/check_missed_mentions.py` to adjust:
- `MONITORED_CHATS`: List of groups to monitor
- Time window for checking (default: last 1 hour)
- Response message template

## Resources

### scripts/

- `check_missed_mentions.py` - Main script to check and respond to missed @mentions
