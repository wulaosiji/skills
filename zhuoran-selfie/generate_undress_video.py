#!/usr/bin/env python3
"""
生成脱衣视频 - 基于垫图
"""

import os
import sys
import requests
import time
from typing import Optional

WAVESPEED_KEY = os.getenv("WAVESPEED_KEY")
BASE_URL = "https://api.wavespeed.ai/api/v3"

def upload_image_to_wavespeed(image_path: str) -> Optional[str]:
    """上传图片到 WaveSpeed AI，返回 URL"""
    url = f"{BASE_URL}/media/upload/binary"
    headers = {"Authorization": f"Bearer {WAVESPEED_KEY}"}
    
    with open(image_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(url, headers=headers, files=files)
    
    result = resp.json()
    if result.get("code") in [0, 200]:
        return result["data"]["download_url"]
    print(f"Upload failed: {result}")
    return None

def generate_video_task(image_url: str, prompt: str, duration: int = 5) -> Optional[str]:
    """提交视频生成任务"""
    # 使用 Seedance 模型
    url = f"{BASE_URL}/bytedance/seedance-v1-pro-i2v-720p"
    headers = {
        "Authorization": f"Bearer {WAVESPEED_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "image": image_url,
        "prompt": prompt,
        "duration": duration,
        "resolution": "720p"
    }
    
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        result = resp.json()
        if result.get("code") in [0, 200] and result.get("data"):
            return result["data"]["id"]
        print(f"Error: {result}")
        return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def poll_task_result(task_id: str, max_wait: int = 300) -> Optional[str]:
    """轮询获取视频结果"""
    url = f"{BASE_URL}/predictions/{task_id}/result"
    headers = {"Authorization": f"Bearer {WAVESPEED_KEY}"}
    
    print("⏳ 等待视频生成...")
    for i in range(max_wait // 10):
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            data = resp.json()
            status = data.get('data', {}).get('status')
            
            if status == 'completed':
                outputs = data.get('data', {}).get('outputs', [])
                if outputs:
                    return outputs[0]
                return None
            elif status == 'failed':
                print(f"❌ 任务失败: {data.get('data', {}).get('error')}")
                return None
            
            # 每30秒打印一次进度
            if i % 3 == 0:
                print(f"   已等待 {i*10} 秒...")
            time.sleep(10)
        except Exception as e:
            print(f"Poll error: {e}")
            time.sleep(10)
    
    print("⏰ 等待超时")
    return None

def download_video(url: str, output_path: str) -> bool:
    """下载视频"""
    try:
        print(f"📥 下载视频...")
        resp = requests.get(url, timeout=60)
        with open(output_path, 'wb') as f:
            f.write(resp.content)
        print(f"✅ 已保存: {output_path}")
        return True
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return False

def main():
    # 使用刚才生成的噜噜全身水淋湿照片作为垫图
    base_image = "/tmp/lulu_wet_fullbody_v2.png"
    output_path = "/tmp/lulu_undress_video.mp4"
    
    print("🎬 开始生成视频...")
    print(f"📸 垫图: {base_image}")
    
    # 上传垫图
    print("📤 上传垫图...")
    image_url = upload_image_to_wavespeed(base_image)
    if not image_url:
        print("❌ 上传失败")
        sys.exit(1)
    print("✅ 上传成功")
    
    # 构建脱衣动作提示词
    prompt = """beautiful young woman slowly removing her wet camisole top, 
subtle movements, elegant and graceful, 
water droplets on skin glistening, 
soft dramatic lighting, cinematic quality"""
    
    print("🚀 提交视频生成任务...")
    task_id = generate_video_task(image_url, prompt, duration=5)
    if not task_id:
        print("❌ 提交失败")
        sys.exit(1)
    
    print(f"🆔 任务ID: {task_id}")
    
    # 轮询获取结果
    video_url = poll_task_result(task_id)
    
    if video_url:
        print(f"✅ 视频生成成功!")
        print(f"🌐 URL: {video_url}")
        
        # 下载视频
        if download_video(video_url, output_path):
            print(f"\n🎉 完成! 视频已保存: {output_path}")
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        print("❌ 视频生成失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
