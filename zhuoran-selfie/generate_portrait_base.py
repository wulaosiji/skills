#!/usr/bin/env python3
"""
生成标准人像垫图工具
基于参考照片生成中性背景的标准化肖像，用于后续场景化生成
"""

import os
import sys
import requests
from typing import Optional, List
from pathlib import Path

# 优先加载统一配置文件
def load_config():
    """加载 ~/.openclaw/config/main.env"""
    config_path = Path.home() / '.openclaw' / 'config' / 'main.env'
    if config_path.exists():
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    # 环境变量优先
                    if key not in os.environ:
                        os.environ[key] = value

load_config()

# 配置（环境变量 > 配置文件 > 默认值）
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

def poll_result(task_id: str, max_wait: int = 120) -> Optional[str]:
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

def generate_standard_portrait(
    reference_image_path: str,
    output_path: str,
    name: str = "character"
) -> Optional[str]:
    """
    生成标准人像垫图
    
    Args:
        reference_image_path: 参考照片路径
        output_path: 输出路径
        name: 角色名称（用于提示词）
    
    Returns:
        生成的图片 URL
    """
    print(f"🎨 正在为 {name} 生成标准人像垫图...")
    print(f"📸 参考照片: {reference_image_path}")
    
    # 上传参考图
    image_url = upload_image_to_wavespeed(reference_image_path)
    if not image_url:
        print("❌ 上传参考图失败")
        return None
    
    print("✅ 参考图上传成功")
    
    # 构建标准人像提示词
    # 中性背景、正面、清晰的标准肖像
    prompt = """professional headshot portrait, neutral soft gray gradient background, 
soft studio lighting, facing camera directly, front view, shoulders visible, 
natural makeup, photorealistic, high quality, clean simple backdrop,
consistent facial features with reference, same hairstyle, same face shape"""
    
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
        print("Usage: python generate_portrait_base.py <reference_image> <output_path> [name]")
        print("Example: python generate_portrait_base.py /path/to/photo.jpg /path/to/output.png Lulu")
        sys.exit(1)
    
    reference_image = sys.argv[1]
    output_path = sys.argv[2]
    name = sys.argv[3] if len(sys.argv) > 3 else "character"
    
    if not os.path.exists(reference_image):
        print(f"❌ 参考图片不存在: {reference_image}")
        sys.exit(1)
    
    result = generate_standard_portrait(reference_image, output_path, name)
    
    if result:
        print(f"\n✅ 完成! 标准人像垫图已生成: {output_path}")
        print(f"🌐 URL: {result}")
        sys.exit(0)
    else:
        print("\n❌ 生成失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
