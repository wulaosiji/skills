#!/usr/bin/env python3
"""
群聊监控脚本 - 检测AGI智库群中涉及吴老师的信息
每日早9:00、晚21:00执行
"""

import json
import subprocess
import os
from datetime import datetime, timedelta

# 配置
CHAT_IDS = [
    "oc_f682e4cb4d3eab9bc4e284f7650f4796",  # AGI智库-话题群
    "oc_60c795e2e04eefc3d09eb49da4df15a5"   # AGI智库-对话群
]
KEYWORDS = ["吴畏", "吴老师", "非凡产研"]
OUTPUT_DIR = "/tmp/monitor_reports"
SKILL_DIR = "/Users/delta/.openclaw/workspace/skills/feishu-chat-extractor"

def run_extraction(chat_id, output_file, hours=24):
    """提取群聊消息"""
    import time
    start_time = int(time.time()) - hours * 3600
    
    cmd = [
        "python3", f"{SKILL_DIR}/scripts/extract_chat.py",
        "--chat-id", chat_id,
        "--start-time", str(start_time),
        "--output", output_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.returncode == 0
    except Exception as e:
        print(f"提取失败: {e}")
        return False

def analyze_content(input_file, output_file):
    """分析内容"""
    keywords_str = ",".join(KEYWORDS)
    cmd = [
        "python3", f"{SKILL_DIR}/scripts/analyze_content.py",
        "--input", input_file,
        "--keywords", keywords_str,
        "--output", output_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0
    except Exception as e:
        print(f"分析失败: {e}")
        return False

def generate_report():
    """生成监控报告"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    report_lines = [f"🦞 **群聊监控日报** | {report_time}\n"]
    report_lines.append("**监控范围**：AGI智库-话题群 + AGI智库-对话群\n")
    report_lines.append("**监控关键词**：吴畏、吴老师、非凡产研\n")
    report_lines.append("---\n\n")
    
    total_related = 0
    
    for i, chat_id in enumerate(CHAT_IDS):
        chat_name = "话题群" if i == 0 else "对话群"
        raw_file = f"{OUTPUT_DIR}/chat_{chat_name}_{datetime.now().strftime('%Y%m%d')}.json"
        analysis_file = f"{OUTPUT_DIR}/analysis_{chat_name}_{datetime.now().strftime('%Y%m%d')}.json"
        
        if run_extraction(chat_id, raw_file, hours=24):
            if analyze_content(raw_file, analysis_file):
                # 读取分析结果
                try:
                    with open(analysis_file, 'r') as f:
                        data = json.load(f)
                    
                    total = data.get('total_messages', 0)
                    related = data.get('related_messages', 0)
                    total_related += related
                    
                    report_lines.append(f"**{chat_name}**：{total}条消息 → **{related}条涉及您**\n")
                    
                    # 列出相关消息摘要
                    if related > 0:
                        report_lines.append("\n**涉及内容摘要**：\n")
                        messages = data.get('messages', [])[:5]  # 只显示前5条
                        for msg in messages:
                            content = msg.get('content', '')[:100]
                            sender = msg.get('sender_name', '未知')
                            report_lines.append(f"- {sender}: {content}...\n")
                        if related > 5:
                            report_lines.append(f"- ... 等共{related}条\n")
                        report_lines.append("\n")
                        
                except Exception as e:
                    report_lines.append(f"**{chat_name}**：分析出错 - {e}\n")
            else:
                report_lines.append(f"**{chat_name}**：分析失败\n")
        else:
            report_lines.append(f"**{chat_name}**：提取失败\n")
    
    report_lines.append("---\n")
    if total_related == 0:
        report_lines.append("\n✅ 过去24小时内未检测到涉及您的讨论。\n")
    else:
        report_lines.append(f"\n⚠️ 共检测到 **{total_related}** 条涉及您的消息，详细内容已记录。\n")
    
    return "".join(report_lines)

if __name__ == "__main__":
    report = generate_report()
    print(report)
    # 将报告写入文件供OpenClaw读取发送
    report_file = f"{OUTPUT_DIR}/daily_report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\n报告已保存: {report_file}")
