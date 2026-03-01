#!/usr/bin/env python3
"""
使用合成垫图生成特定场景照片
"""

import os
import sys
import requests
from typing import Optional

# 配置
WAVESPEED_KEY = os.getenv("WAVESPEED_KEY")

def upload_image_to_wavespeed(image_path: str) -> Optional[str]:
    """上传图片到 WaveSpeed AI，返回 URL"""
    url = "https://api.wavespeed.ai/api/v3/media/upload/binary"
    headers = {"Authorization": f"Bearer {WAVESPEED_KEY}"}
    
    with open(image_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(url, headers=headers, files=files)
    
    result = resp.json()
    if result.get("code") in [0, 200]:
        return result["data"]["download_url"]
    print(f"Upload failed: {result}")
    return None

def call_grok_edit(image_url: str, prompt: str) -> Optional[str]:
    """调用 WaveSpeed AI Grok Imagine Edit API"""
    url = "https://api.wavespeed.ai/api/v3/x-ai/grok-imagine-image/edit"
    headers = {
        "Authorization": f"Bearer {WAVESPEED_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "image": image_url,
        "prompt": prompt,
        "num_images": 1,
        "output_format": "jpeg"
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

def poll_result(task_id: str, max_wait: int = 180) -> Optional[str]:
    """轮询获取结果"""
    url = f"https://api.wavespeed.ai/api/v3/predictions/{task_id}/result"
    headers = {"Authorization": f"Bearer {WAVESPEED_KEY}"}
    
    import time
    for _ in range(max_wait // 5):
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            data = resp.json()
            status = data.get('data', {}).get('status')
            
            if status == 'completed':
                return data['data']['outputs'][0] if data['data']['outputs'] else None
            elif status == 'failed':
                print(f"Task failed: {data.get('data', {}).get('error')}")
                return None
            
            time.sleep(5)
        except Exception as e:
            print(f"Poll error: {e}")
            time.sleep(5)
    
    return None

def download_image(url: str, output_path: str) -> bool:
    """下载图片"""
    try:
        resp = requests.get(url, timeout=30)
        with open(output_path, 'wb') as f:
            f.write(resp.content)
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False

def generate_mirror_room_scene(
    combined_base_path: str,
    output_path: str
) -> Optional[str]:
    """
    生成镜面房间场景
    
    Args:
        combined_base_path: 合成垫图路径（两个人并排）
        output_path: 输出路径
    
    Returns:
        生成的图片 URL
    """
    print(f"🎨 正在生成镜面房间场景...")
    print(f"📸 使用合成垫图: {combined_base_path}")
    
    # 上传合成垫图
    image_url = upload_image_to_wavespeed(combined_base_path)
    if not image_url:
        print("❌ 上传垫图失败")
        return None
    
    print("✅ 垫图上传成功")
    
    # 构建镜面房间提示词
    prompt = """two beautiful young women standing together in an infinity mirror room, 
contemporary art installation with endless reflections, surrounded by mirrors on all sides, 
creating infinite reflections, artistic lighting, dreamy atmosphere, 
both women clearly visible, photorealistic, high quality"""
    
    print("🚀 提交生成任务...")
    task_id = call_grok_edit(image_url, prompt)
    if not task_id:
        print("❌ 提交任务失败")
        return None
    
    print(f"⏳ 任务ID: {task_id}，等待生成...")
    result_url = poll_result(task_id, max_wait=180)
    
    if result_url:
        print(f"✅ 生成成功!")
        
        # 下载保存
        if download_image(result_url, output_path):
            print(f"💾 已保存到: {output_path}")
            return result_url
        else:
            print(f"⚠️ 下载失败，但获取到URL: {result_url}")
            return result_url
    else:
        print("❌ 生成失败")
        return None

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("Usage: python generate_mirror_room.py <combined_base_image> <output_path>")
        print("Example: python generate_mirror_room.py combined.png output.png")
        sys.exit(1)
    
    combined_base = sys.argv[1]
    output_path = sys.argv[2]
    
    if not os.path.exists(combined_base):
        print(f"❌ 合成垫图不存在: {combined_base}")
        sys.exit(1)
    
    result = generate_mirror_room_scene(combined_base, output_path)
    
    if result:
        print(f"\n✅ 完成! 镜面房间照片已生成: {output_path}")
        print(f"🌐 URL: {result}")
        sys.exit(0)
    else:
        print("\n❌ 生成失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
