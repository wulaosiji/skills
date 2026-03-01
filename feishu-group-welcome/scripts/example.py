#!/usr/bin/env python3
"""
使用示例：批量欢迎新成员
"""

import sys
sys.path.insert(0, '/Users/delta/.openclaw/workspace/skills/feishu-group-welcome/scripts')

from welcome_bot import GroupWelcomeBot

# 初始化
bot = GroupWelcomeBot()

# 示例1：自动检测并欢迎新成员
print("=== 示例1：自动检测新成员 ===")
bot.check_and_welcome("oc_60c795e2e04eefc3d09eb49da4df15a5", "AGI智库-对话群")

# 示例2：手动欢迎指定用户
print("\n=== 示例2：手动欢迎指定用户 ===")
members = [
    ("ou_xxx1", "用户1"),
    ("ou_xxx2", "用户2"),
    ("ou_xxx3", "用户3"),
]
bot.send_welcome("oc_60c795e2e04eefc3d09eb49da4df15a5", "AGI智库-对话群", members)
