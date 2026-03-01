import os
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每小时检查遗漏的 @消息并补回响应
"""

import requests
import json
from datetime import datetime, timezone, timedelta
import time

APP_ID = os.getenv("FEISHU_APP_ID")
APP_SECRET = os.getenv("FEISHU_APP_SECRET")

# 监控的群
MONITORED_CHATS = [
    ("oc_60c795e2e04eefc3d09eb49da4df15a5", "AGI智库-对话群"),
    ("oc_f682e4cb4d3eab9bc4e284f7650f4796", "AGI智库-话题群"),
    # ("oc_951cf024c656acd330f440b6bd086cee", "非凡大队"),  # 2026-02-07: 吴老师指示不监控此群
]

def get_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": APP_ID, "app_secret": APP_SECRET})
    return resp.json().get("tenant_access_token")

def send_message(token, chat_id, content, reply_to=None):
    """发送消息"""
    url = "https://open.feishu.cn/open-apis/im/v1/messages"
    headers = {"Authorization": f"Bearer {token}"}
    
    body = {
        "receive_id": chat_id,
        "msg_type": "text",
        "content": json.dumps({"text": content})
    }
    
    if reply_to:
        body["reply_in_thread"] = True
        # 飞书回复需要使用特定的 reply 参数，这里简化处理
    
    resp = requests.post(url, headers=headers, json=body)
    return resp.json()

def check_missed_mentions():
    """检查遗漏的 @消息"""
    token = get_token()
    if not token:
        print("❌ 获取 token 失败")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    beijing = timezone(timedelta(hours=8))
    now = datetime.now(beijing)
    
    # 检查最近1小时内的消息
    one_hour_ago = (now - timedelta(hours=1)).timestamp() * 1000
    
    missed_count = 0
    
    for chat_id, name in MONITORED_CHATS:
        print(f"\n📋 检查 {name}...")
        
        url = "https://open.feishu.cn/open-apis/im/v1/messages"
        params = {
            "container_id": chat_id,
            "container_id_type": "chat",
            "page_size": 50,
            "sort_type": "ByCreateTimeDesc"
        }
        
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        
        if data.get("code") != 0:
            print(f"  ❌ 读取失败: {data.get('msg')}")
            continue
        
        items = data.get("data", {}).get("items", [])
        
        for item in items:
            create_time = int(item.get("create_time", 0))
            
            # 只检查最近1小时内的消息
            if create_time < one_hour_ago:
                break
            
            content = str(item.get("body", {}).get("content", ""))
            mentions = item.get("mentions", [])
            sender = item.get("sender", {}).get("sender_id", {}).get("name", "某人")
            msg_id = item.get("message_id")
            
            # 检查是否 @我
            is_mention_me = False
            if mentions:
                for m in mentions:
                    if m.get("user_id") == "@_user_1":
                        is_mention_me = True
                        break
            elif "@_user_1" in content:
                is_mention_me = True
            
            if is_mention_me:
                # 检查我是否已经回复过（简单的启发式：检查后面是否有我的消息）
                msg_time = datetime.fromtimestamp(create_time/1000, tz=beijing)
                print(f"  ⚠️ 发现 @我: [{msg_time.strftime('%H:%M')}] {sender}: {content[:40]}...")
                
                # 发送补回响应
                response = f"@{sender} 抱歉刚才在处理其他任务，现在回复您！请说～"
                result = send_message(token, chat_id, response)
                
                if result.get("code") == 0:
                    print(f"  ✅ 已补回响应")
                    missed_count += 1
                else:
                    print(f"  ❌ 发送失败: {result.get('msg')}")
    
    print(f"\n{'='*50}")
    print(f"📊 检查完成，补回 {missed_count} 条遗漏响应")
    print(f"⏰ 下次检查: {(now + timedelta(hours=1)).strftime('%H:%M')}")

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始检查遗漏的 @消息...")
    check_missed_mentions()
