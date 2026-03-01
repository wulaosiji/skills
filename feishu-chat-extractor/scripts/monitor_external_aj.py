#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外部群-AJ 消息记忆保存脚本

功能：
1. 定期抓取外部群-AJ的消息
2. 更新群聊记忆
3. 筛选OpenClaw/Clawdbot相关讨论
4. 生成简要报告

定时任务：每天执行（可配置频次）
"""

import json
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# 添加路径
sys.path.insert(0, '/Users/delta/.openclaw/workspace/01-Projects/group-management/src')
sys.path.insert(0, '/Users/delta/.openclaw/workspace/skills/feishu-chat-extractor')

from group_memory import GroupChatMemory, Message

# 配置
CHAT_ID = "oc_3cc1c4abbc093b180cb0b75e40bb6e1b"
CHAT_NAME = "外部群-AJ"
KEYWORDS = ["OpenClaw", "Clawdbot", "Clawd", "龙虾", "clawd", "openclaw"]
OUTPUT_DIR = "/Users/delta/.openclaw/workspace/01-Projects/group-management/data/group-chats"

class ExternalGroupMonitor:
    """外部群监控类"""
    
    def __init__(self):
        self.keywords_found = []
        
    def fetch_messages(self, hours=24):
        """抓取群聊消息"""
        import requests
        import os
        from pathlib import Path
        
        # 从 .env 文件读取配置
        env_path = Path.home() / '.openclaw' / '.env'
        env_config = {}
        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        env_config[key.strip()] = value.strip().strip('"\'')
        
        app_id = os.getenv("FEISHU_APP_ID")
        app_secret = os.getenv("FEISHU_APP_SECRET")
        
        # 获取token
        token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        resp = requests.post(token_url, json={"app_id": app_id, "app_secret": app_secret}, timeout=10)
        token = resp.json().get("tenant_access_token")
        
        if not token:
            print(f"❌ 获取Token失败")
            return []
        
        url = "https://open.feishu.cn/open-apis/im/v1/messages"
        headers = {"Authorization": f"Bearer {token}"}
        
        all_messages = []
        page_token = None
        page = 0
        max_pages = 20
        
        while page < max_pages:
            page += 1
            params = {
                "container_id_type": "chat",
                "container_id": CHAT_ID,
                "sort_type": "ByCreateTimeDesc",
                "page_size": 50
            }
            if page_token:
                params["page_token"] = page_token
            
            try:
                resp = requests.get(url, headers=headers, params=params, timeout=30)
                result = resp.json()
                
                if result.get("code") != 0:
                    break
                
                items = result.get("data", {}).get("items", [])
                
                for item in items:
                    if item.get("msg_type") != "text":
                        continue
                    
                    content = item.get("body", {}).get("content", "")
                    try:
                        content_data = json.loads(content)
                        text = content_data.get("text", "")
                    except:
                        text = content
                    
                    create_time_ms = item.get("create_time")
                    if create_time_ms:
                        try:
                            create_time = datetime.fromtimestamp(int(create_time_ms) / 1000)
                            if datetime.now() - create_time > timedelta(hours=hours):
                                continue
                        except:
                            pass
                    
                    msg = Message(
                        message_id=item.get("message_id"),
                        chat_id=CHAT_ID,
                        sender_id=item.get("sender", {}).get("id", ""),
                        sender_name=item.get("sender", {}).get("name", ""),
                        content=text,
                        msg_type="text",
                        create_time=int(create_time_ms) if create_time_ms else 0
                    )
                    all_messages.append(msg)
                
                page_token = result.get("data", {}).get("page_token")
                has_more = result.get("data", {}).get("has_more", False)
                
                if not has_more or not page_token:
                    break
                    
            except Exception as e:
                print(f"❌ 请求失败: {e}")
                break
        
        return all_messages
    
    def update_group_memory(self, messages):
        """更新群聊记忆"""
        memory = GroupChatMemory()
        memory.load_chat(CHAT_ID)
        
        added, skipped = memory.add_messages(messages)
        memory.save_chat(CHAT_ID)
        
        print(f"   群聊记忆更新: 新增{added}条, 跳过{skipped}条")
        return {'added': added, 'skipped': skipped, 'total': len(memory.messages)}
    
    def search_keywords(self, messages):
        """搜索关键词"""
        found = []
        for msg in messages:
            content_lower = msg.content.lower()
            for keyword in KEYWORDS:
                if keyword.lower() in content_lower:
                    found.append({
                        "sender": msg.sender_name or msg.sender_id[:8],
                        "content": msg.content[:200] + "..." if len(msg.content) > 200 else msg.content,
                        "time": msg.create_time,
                        "keyword": keyword
                    })
                    break
        return found
    
    def generate_report(self, memory_result, keyword_matches):
        """生成报告"""
        report = f"""# {CHAT_NAME} 消息监控报告

## 📊 消息统计
- 新增消息: {memory_result['added']}条
- 跳过重复: {memory_result['skipped']}条
- 总消息数: {memory_result['total']}条

## 🔍 OpenClaw相关讨论 ({len(keyword_matches)}条)

"""
        if keyword_matches:
            for i, m in enumerate(keyword_matches[:20], 1):
                report += f"**{i}. [{m['sender']}]** (匹配: {m['keyword']})\n"
                report += f"> {m['content']}\n\n"
        else:
            report += "过去24小时无OpenClaw相关讨论\n"
        
        report += f"\n---\n*报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        return report
    
    def run(self, hours=24, generate_md=True):
        """执行完整流程"""
        print("=" * 60)
        print(f"🔄 {CHAT_NAME} 消息监控任务")
        print("=" * 60)
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # 1. 抓取消息
        print(f"1️⃣ 抓取最近{hours}小时消息...")
        messages = self.fetch_messages(hours=hours)
        print(f"   获取到 {len(messages)} 条消息")
        
        if not messages:
            print("   无新消息，跳过")
            return None
        
        # 2. 更新群聊记忆
        print("2️⃣ 更新群聊记忆...")
        memory_result = self.update_group_memory(messages)
        
        # 3. 搜索关键词
        print("3️⃣ 搜索OpenClaw相关讨论...")
        keyword_matches = self.search_keywords(messages)
        print(f"   找到 {len(keyword_matches)} 条相关消息")
        
        # 4. 生成报告
        if generate_md:
            print("4️⃣ 生成报告...")
            report = self.generate_report(memory_result, keyword_matches)
            
            # 保存报告
            report_file = f"{OUTPUT_DIR}/{CHAT_ID}_report_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"   报告已保存: {report_file}")
        
        print("\n" + "=" * 60)
        print("✅ 任务完成")
        
        return keyword_matches

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description=f'{CHAT_NAME} 消息监控')
    parser.add_argument('--hours', type=int, default=24, help='抓取多少小时内的消息')
    parser.add_argument('--no-report', action='store_true', help='不生成Markdown报告')
    
    args = parser.parse_args()
    
    monitor = ExternalGroupMonitor()
    monitor.run(hours=args.hours, generate_md=not args.no_report)
