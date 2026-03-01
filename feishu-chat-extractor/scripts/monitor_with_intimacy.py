#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
群聊监控与亲密度更新整合脚本

功能：
1. 抓取AGI智库群最近24小时消息
2. 更新群聊记忆（group-chats）
3. 分析用户活跃度并更新亲密度档案
4. 生成综合报告（涉及吴老师的内容+亲密度变化）

定时任务：每天早9:00、晚21:00执行
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
CHAT_IDS = {
    "oc_f682e4cb4d3eab9bc4e284f7650f4796": "AGI智库-话题群",
    "oc_60c795e2e04eefc3d09eb49da4df15a5": "AGI智库-对话群"
}

KEYWORDS = ["吴畏", "吴老师", "非凡产研"]
SOCIAL_RELATIONS_FILE = "/Users/delta/.openclaw/workspace/memory/social_relations.json"

class GroupMonitorWithIntimacy:
    """群聊监控与亲密度更新整合类"""
    
    def __init__(self):
        self.results = {}
        self.intimacy_updates = []
        
    def fetch_messages(self, chat_id, hours=24):
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
        
        # 飞书API配置
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
        max_pages = 10  # 限制页数
        
        while page < max_pages:
            page += 1
            params = {
                "container_id_type": "chat",
                "container_id": chat_id,
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
                            # 只保留指定时间范围内的消息
                            if datetime.now() - create_time > timedelta(hours=hours):
                                continue
                        except (ValueError, TypeError):
                            create_time = None
                    else:
                        create_time = None
                    
                    msg = Message(
                        message_id=item.get("message_id"),
                        chat_id=chat_id,
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
    
    def update_group_memory(self, chat_id, messages):
        """更新群聊记忆"""
        memory = GroupChatMemory()
        memory.load_chat(chat_id)
        
        # 增量添加消息
        added, skipped = memory.add_messages(messages)
        memory.save_chat(chat_id)
        
        result = {
            'added': added,
            'skipped': skipped,
            'total': len(memory.messages)
        }
        
        print(f"   群聊记忆更新: 新增{result['added']}条, 跳过{result['skipped']}条")
        return result
    
    def analyze_user_activity(self, messages):
        """分析用户活跃度"""
        user_stats = {}
        
        for msg in messages:
            user_id = msg.sender_id
            if not user_id:
                continue
            
            if user_id not in user_stats:
                user_stats[user_id] = {
                    "name": msg.sender_name or f"User_{user_id[:8]}",
                    "count": 0,
                    "messages": []
                }
            
            user_stats[user_id]["count"] += 1
            user_stats[user_id]["messages"].append(msg.content)
        
        return user_stats
    
    def update_intimacy(self, chat_id, user_stats):
        """更新亲密度档案"""
        # 读取现有亲密度档案
        if os.path.exists(SOCIAL_RELATIONS_FILE):
            with open(SOCIAL_RELATIONS_FILE, "r", encoding="utf-8") as f:
                relations = json.load(f)
        else:
            relations = {"version": "1.1", "users": {}, "groups": {}}
        
        updates = []
        
        for user_id, stats in user_stats.items():
            # 跳过吴老师自己
            if user_id == "ou_5f3a4a920dc39a8d1835fd0085afef50":
                continue
            
            # 获取或创建用户档案
            if user_id not in relations["users"]:
                relations["users"][user_id] = {
                    "nickname": stats["name"],
                    "relations": {"familiarity": 0, "trust": 0, "intimacy": 0},
                    "interaction_stats": {"total_interactions": 0}
                }
            
            user = relations["users"][user_id]
            old_familiarity = user["relations"]["familiarity"]
            
            # 根据消息数计算亲密度增量
            msg_count = stats["count"]
            if msg_count >= 20:
                increment = 5
            elif msg_count >= 10:
                increment = 3
            elif msg_count >= 5:
                increment = 2
            elif msg_count >= 1:
                increment = 1
            else:
                increment = 0
            
            # 更新熟悉度
            new_familiarity = min(100, old_familiarity + increment)
            user["relations"]["familiarity"] = new_familiarity
            user["interaction_stats"]["total_interactions"] += msg_count
            
            # 更新群聊来源标记
            if "source" not in user:
                user["source"] = "group"
                user["source_note"] = f"AGI智库群聊互动"
            
            # 记录更新
            if new_familiarity > old_familiarity:
                updates.append({
                    "user_id": user_id,
                    "name": stats["name"],
                    "old": old_familiarity,
                    "new": new_familiarity,
                    "increment": increment,
                    "messages": msg_count
                })
        
        # 保存更新后的档案
        with open(SOCIAL_RELATIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(relations, f, ensure_ascii=False, indent=2)
        
        return updates
    
    def find_mentions_of_wulao(self, messages):
        """查找涉及吴老师的消息"""
        mentions = []
        
        for msg in messages:
            content = msg.content
            for keyword in KEYWORDS:
                if keyword in content:
                    mentions.append({
                        "sender": msg.sender_name or msg.sender_id[:8],
                        "content": content[:200] + "..." if len(content) > 200 else content,
                        "time": msg.create_time
                    })
                    break
        
        return mentions
    
    def generate_report(self, chat_name, memory_result, intimacy_updates, mentions):
        """生成综合报告"""
        report = f"""# 群聊监控与亲密度更新报告 | {chat_name}

## 📊 群聊记忆更新
- 新增消息: {memory_result['added']}条
- 跳过重复: {memory_result['skipped']}条
- 总消息数: {memory_result['total']}条

## 👤 亲密度更新
"""
        
        if intimacy_updates:
            report += "| 用户 | 原熟悉度 | 新熟悉度 | 增量 | 消息数 |\n"
            report += "|------|----------|----------|------|--------|\n"
            for u in intimacy_updates:
                report += f"| {u['name']} | {u['old']} | {u['new']} | +{u['increment']} | {u['messages']} |\n"
        else:
            report += "无亲密度变化\n"
        
        report += "\n## 📢 涉及吴老师的消息\n"
        if mentions:
            for i, m in enumerate(mentions[:10], 1):  # 最多显示10条
                report += f"\n**{i}. [{m['sender']}]** {m['content'][:150]}...\n"
                # 处理时间戳格式
                time_str = "N/A"
                if m['time']:
                    from datetime import datetime
                    try:
                        dt = datetime.fromtimestamp(int(m['time']) / 1000)
                        time_str = dt.strftime('%Y-%m-%d %H:%M')
                    except:
                        time_str = str(m['time'])[:16]
                report += f"   时间: {time_str}\n"
        else:
            report += "过去24小时无涉及吴老师的消息\n"
        
        return report
    
    def run(self):
        """执行完整流程"""
        print("=" * 60)
        print("🔄 群聊监控与亲密度更新整合任务")
        print("=" * 60)
        print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        all_reports = []
        
        for chat_id, chat_name in CHAT_IDS.items():
            print(f"\n📍 处理群: {chat_name}")
            print("-" * 40)
            
            # 1. 抓取消息
            print("1️⃣ 抓取最近24小时消息...")
            messages = self.fetch_messages(chat_id, hours=24)
            print(f"   获取到 {len(messages)} 条消息")
            
            if not messages:
                continue
            
            # 2. 更新群聊记忆
            print("2️⃣ 更新群聊记忆...")
            memory_result = self.update_group_memory(chat_id, messages)
            
            # 3. 分析用户活跃度
            print("3️⃣ 分析用户活跃度...")
            user_stats = self.analyze_user_activity(messages)
            print(f"   活跃用户: {len(user_stats)} 人")
            
            # 4. 更新亲密度
            print("4️⃣ 更新亲密度档案...")
            intimacy_updates = self.update_intimacy(chat_id, user_stats)
            print(f"   更新 {len(intimacy_updates)} 位用户亲密度")
            
            # 5. 查找涉及吴老师的消息
            print("5️⃣ 筛选涉及吴老师的消息...")
            mentions = self.find_mentions_of_wulao(messages)
            print(f"   找到 {len(mentions)} 条相关消息")
            
            # 6. 生成报告
            report = self.generate_report(chat_name, memory_result, intimacy_updates, mentions)
            all_reports.append(report)
        
        # 合并报告
        final_report = "\n\n".join(all_reports)
        
        # 保存报告
        report_file = f"/tmp/group_monitor_report_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(final_report)
        
        print(f"\n✅ 报告已保存: {report_file}")
        print("\n" + "=" * 60)
        
        return final_report

if __name__ == "__main__":
    monitor = GroupMonitorWithIntimacy()
    report = monitor.run()
    print(report)
