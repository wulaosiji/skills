#!/usr/bin/env python3
"""
Analyze chat content and extract relevant information
Usage: python3 analyze_content.py --input <FILE> --keywords <KW1,KW2> --output <FILE>
"""

import argparse
import json
import re
from datetime import datetime
from collections import Counter

def load_messages(input_file):
    """Load messages from extraction file"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get("messages", [])

def extract_text_content(message):
    """Extract text from message body"""
    msg_type = message.get("msg_type", "")
    content = message.get("body", {}).get("content", "")
    
    if not content:
        return ""
    
    try:
        data = json.loads(content)
        if msg_type == "text":
            return data.get("text", "")
        elif msg_type == "post":
            # Extract text from post content
            text_parts = []
            for item in data.get("content", []):
                for part in item:
                    if part.get("tag") == "text":
                        text_parts.append(part.get("text", ""))
            return " ".join(text_parts)
    except:
        return ""
    
    return ""

def filter_by_keywords(messages, keywords):
    """Filter messages containing keywords"""
    filtered = []
    keyword_list = [k.strip().lower() for k in keywords.split(",")]
    
    for msg in messages:
        text = extract_text_content(msg).lower()
        if any(kw in text for kw in keyword_list):
            filtered.append({
                "message": msg,
                "text": extract_text_content(msg),
                "matched_keywords": [kw for kw in keyword_list if kw in text]
            })
    
    return filtered

def categorize_messages(filtered_messages):
    """Categorize messages by topics"""
    categories = {
        "部署环境": ["mac mini", "vps", "服务器", "部署", "安装"],
        "模型选择": ["模型", "claude", "api", "openrouter", "minimax", "token"],
        "功能问题": ["cron", "定时任务", "bug", "问题", "报错", "不行"],
        "使用场景": ["场景", "用法", "怎么用", "使用"],
        "平台支持": ["飞书", "telegram", "whatsapp", "平台"],
        "讨论反馈": ["感觉", "觉得", "建议", "反馈"]
    }
    
    categorized = {cat: [] for cat in categories}
    
    for item in filtered_messages:
        text = item["text"].lower()
        matched = False
        
        for cat, keywords in categories.items():
            if any(kw in text for kw in keywords):
                categorized[cat].append(item)
                matched = True
                break
        
        if not matched:
            categorized.setdefault("其他", []).append(item)
    
    return categorized

def generate_report(messages, filtered, categorized, output_file):
    """Generate structured report"""
    report = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_messages": len(messages),
            "filtered_messages": len(filtered),
            "categories": {cat: len(items) for cat, items in categorized.items()}
        },
        "categories": {}
    }
    
    # Add categorized content
    for cat, items in categorized.items():
        if items:
            report["categories"][cat] = {
                "count": len(items),
                "messages": [
                    {
                        "time": datetime.fromtimestamp(int(item["message"].get("create_time", 0)) / 1000).strftime("%Y-%m-%d %H:%M"),
                        "text": item["text"][:200] + "..." if len(item["text"]) > 200 else item["text"],
                        "keywords": item["matched_keywords"]
                    }
                    for item in items[:10]  # Limit to 10 per category
                ]
            }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return report

def generate_markdown_report(report, output_file):
    """Generate markdown report"""
    md = f"""# OpenClaw 群聊讨论分析报告

生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}

## 数据概览

| 指标 | 数值 |
|------|------|
| 总消息数 | {report['summary']['total_messages']} |
| 相关消息数 | {report['summary']['filtered_messages']} |

## 分类统计

| 类别 | 数量 |
|------|------|
"""
    
    for cat, count in report['summary']['categories'].items():
        if count > 0:
            md += f"| {cat} | {count} |\n"
    
    md += "\n## 详细内容\n\n"
    
    for cat, data in report['categories'].items():
        md += f"### {cat} ({data['count']} 条)\n\n"
        for msg in data['messages'][:5]:  # Show top 5
            md += f"- **{msg['time']}**: {msg['text']}\n"
        md += "\n"
    
    with open(output_file.replace('.json', '.md'), 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"✅ Markdown report saved to {output_file.replace('.json', '.md')}")

def main():
    parser = argparse.ArgumentParser(description='Analyze chat content')
    parser.add_argument('--input', required=True, help='Input JSON file from extract_chat.py')
    parser.add_argument('--keywords', default="openclaw,clawdbot,cron,mcp,claude", help='Comma-separated keywords')
    parser.add_argument('--output', default='analysis_report.json', help='Output report file')
    
    args = parser.parse_args()
    
    print(f"📊 Analyzing {args.input}...")
    
    # Load messages
    messages = load_messages(args.input)
    print(f"   Loaded {len(messages)} messages")
    
    # Filter by keywords
    print(f"   Filtering by keywords: {args.keywords}")
    filtered = filter_by_keywords(messages, args.keywords)
    print(f"   Found {len(filtered)} matching messages")
    
    # Categorize
    print("   Categorizing messages...")
    categorized = categorize_messages(filtered)
    
    # Generate report
    print(f"   Generating report...")
    report = generate_report(messages, filtered, categorized, args.output)
    
    # Generate markdown
    generate_markdown_report(report, args.output)
    
    # Print summary
    print(f"\n📈 Analysis Summary:")
    print(f"   Total messages: {len(messages)}")
    print(f"   Related messages: {len(filtered)}")
    print(f"   Categories:")
    for cat, count in report['summary']['categories'].items():
        if count > 0:
            print(f"      - {cat}: {count}")
    
    print(f"\n✅ Reports saved:")
    print(f"   JSON: {args.output}")
    print(f"   Markdown: {args.output.replace('.json', '.md')}")

if __name__ == "__main__":
    main()