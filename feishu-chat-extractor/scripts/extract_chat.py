#!/usr/bin/env python3
"""
Extract chat history from Feishu group
Usage: python3 extract_chat.py --chat-id <CHAT_ID> [--start-time <TS>] [--end-time <TS>] --output <FILE>
"""

import argparse
import json
import requests
from datetime import datetime
import sys
import os

# Feishu API credentials - read from environment or config file
def get_credentials():
    """Get Feishu API credentials"""
    # Try to read from config file
    config_path = os.path.expanduser("~/.openclaw/agents/main/agent/feishu-app-token.txt")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            token = f.read().strip()
            return {"token": token}
    
    # Fallback to hardcoded (for development)
    return {
        "app_id": os.getenv("FEISHU_APP_ID"),
        "app_secret": os.getenv("FEISHU_APP_SECRET")
    }

def get_token(creds):
    """Get tenant access token"""
    if "token" in creds:
        return creds["token"]
    
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={
        "app_id": creds["app_id"],
        "app_secret": creds["app_secret"]
    })
    return resp.json().get("tenant_access_token")

def extract_messages(chat_id, start_time=None, end_time=None, page_size=50):
    """Extract all messages from chat"""
    creds = get_credentials()
    token = get_token(creds)
    
    all_messages = []
    page_token = None
    page_count = 0
    
    print(f"🔍 Extracting messages from chat: {chat_id}")
    if start_time:
        print(f"   Start time: {datetime.fromtimestamp(start_time)}")
    if end_time:
        print(f"   End time: {datetime.fromtimestamp(end_time)}")
    
    while True:
        url = "https://open.feishu.cn/open-apis/im/v1/messages"
        headers = {"Authorization": f"Bearer {token}"}
        params = {
            "container_id": chat_id,
            "container_id_type": "chat",
            "page_size": page_size
        }
        
        if start_time:
            params["start_time"] = start_time
        if end_time:
            params["end_time"] = end_time
        if page_token:
            params["page_token"] = page_token
        
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            result = resp.json()
            
            if result.get("code") != 0:
                print(f"❌ API Error: {result.get('msg')}")
                break
            
            items = result.get("data", {}).get("items", [])
            all_messages.extend(items)
            page_count += 1
            
            print(f"   Page {page_count}: Got {len(items)} messages (Total: {len(all_messages)})")
            
            if not result.get("data", {}).get("has_more"):
                break
            
            page_token = result.get("data", {}).get("page_token")
            if not page_token:
                break
                
        except Exception as e:
            print(f"❌ Request error: {e}")
            break
    
    return all_messages

def save_results(messages, chat_id, output_file):
    """Save extraction results"""
    result = {
        "chat_id": chat_id,
        "extraction_time": datetime.now().isoformat(),
        "total_messages": len(messages),
        "messages": messages
    }
    
    # Extract time range if messages exist
    if messages:
        timestamps = [int(m.get("create_time", 0)) for m in messages if m.get("create_time")]
        if timestamps:
            result["time_range"] = {
                "start": datetime.fromtimestamp(min(timestamps) / 1000).isoformat(),
                "end": datetime.fromtimestamp(max(timestamps) / 1000).isoformat()
            }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Saved {len(messages)} messages to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Extract Feishu chat history')
    parser.add_argument('--chat-id', required=True, help='Chat ID (oc_xxx)')
    parser.add_argument('--start-time', type=int, help='Start timestamp (seconds)')
    parser.add_argument('--end-time', type=int, help='End timestamp (seconds)')
    parser.add_argument('--output', default='chat_extracted.json', help='Output file')
    parser.add_argument('--page-size', type=int, default=50, help='Page size (1-50)')
    
    args = parser.parse_args()
    
    # Extract messages
    messages = extract_messages(
        args.chat_id,
        args.start_time,
        args.end_time,
        args.page_size
    )
    
    # Save results
    save_results(messages, args.chat_id, args.output)
    
    print(f"\n📊 Extraction Summary:")
    print(f"   Total messages: {len(messages)}")
    if messages:
        timestamps = [int(m.get("create_time", 0)) for m in messages if m.get("create_time")]
        if timestamps:
            print(f"   Time range: {datetime.fromtimestamp(min(timestamps)/1000)} ~ {datetime.fromtimestamp(max(timestamps)/1000)}")

if __name__ == "__main__":
    main()