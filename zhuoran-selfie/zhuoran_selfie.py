#!/usr/bin/env python3
"""
卓然自拍技能 - 基于 zhuoran_photo_generator 方案
支持：一步直达 / 两步法 / 智能判断
"""

import os
import sys
import json
import base64
import requests
from typing import Optional, Literal

# 配置
WAVESPEED_KEY = os.getenv("WAVESPEED_KEY")
# 获取脚本所在目录，构建相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_IMAGE_PATH = os.path.join(SCRIPT_DIR, "assets", "zhuoran_portrait_base.png")

# 禁用场景（高风险）
DISABLED_SCENES = ["mirror_selfie", "mirror_reflection_selfie", "beach_selfie"]

# 场景模板库
SCENE_TEMPLATES = {
    "office": {
        "prompt": "professional headshot at modern office with large windows, navy blue blazer, light blue shirt, red lobster brooch, natural soft lighting, warm friendly smile",
        "change_level": "high"
    },
    "cafe": {
        "prompt": "casual portrait at cozy cafe with warm ambient lighting, reading a book, relaxed atmosphere",
        "change_level": "low"
    },
    "airport": {
        "prompt": "at airport departure lounge with carry-on luggage, smart casual travel outfit, business trip vibes",
        "change_level": "medium"
    },
    "westlake": {
        "prompt": "walking at West Lake in Hangzhou, beautiful scenic lake view with traditional Chinese pavilion, comfortable casual spring outfit, peaceful expression",
        "change_level": "low"
    },
    "bookstore": {
        "prompt": "in a cozy bookstore, browsing bookshelves, holding an open book, warm ambient lighting, intellectual atmosphere",
        "change_level": "low"
    },
    "gym": {
        "prompt": "fitness center, holding water bottle with lobster logo, sporty outfit, confident smile",
        "change_level": "minimal"
    },
    "beach": {
        "prompt": "beautiful sandy beach with blue ocean and palm trees, summer vacation vibe, casual beachwear, full-body shot, relaxed and happy expression, golden sunlight, ocean waves in background",
        "change_level": "high"
    },
    "selfie_late_night": {
        "prompt": "late night office, soft desk lamp lighting, casual work clothes, natural tired but focused expression, city lights through window",
        "change_level": "medium",
        "mode": "selfie"
    }
}

# Prompt 模板
PROMPT_TEMPLATES = {
    "direct": "{scene_description}, direct eye contact with camera, looking straight into lens, natural lighting, photorealistic, 8k quality",
    "selfie": "a close-up selfie taken by herself at {scene_description}, direct eye contact with camera, looking straight into the lens, eyes centered and clearly visible, not a mirror selfie, phone held at arm's length but phone not visible in frame, face fully visible, natural lighting",
    "portrait": "professional portrait of {scene_description}, soft natural lighting, half-body shot, clean background, photorealistic"
}

def get_image_base64(image_path: str) -> str:
    """读取图片并转为base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

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
    # 注意：这个端点可能需要更新，目前用的是 wavespeed 的统一接口
    # 实际调用时可能需要根据最新 API 文档调整
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

def generate_one_step(scene: str, mode: Literal["direct", "selfie", "portrait"] = "direct") -> Optional[str]:
    """一步直达：直接从垫图生成场景"""
    print(f"🚀 一步直达模式：{scene}")
    
    # 检查禁用场景
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    scene_info = SCENE_TEMPLATES.get(scene)
    if not scene_info:
        print(f"Unknown scene: {scene}")
        return None
    
    # 上传参考图
    image_url = upload_image_to_wavespeed(REFERENCE_IMAGE_PATH)
    if not image_url:
        return None
    
    # 构建 prompt
    template = PROMPT_TEMPLATES.get(mode, PROMPT_TEMPLATES["direct"])
    prompt = template.format(scene_description=scene_info["prompt"])
    
    # 调用 API
    task_id = call_grok_edit(image_url, prompt)
    if not task_id:
        return None
    
    # 获取结果
    image_url = poll_result(task_id)
    return image_url

def generate_two_step(scene: str, mode: Literal["direct", "selfie", "portrait"] = "direct") -> Optional[str]:
    """两步法：垫图 → 中性背景 → 场景"""
    print(f"🎯 两步法模式：{scene}")
    
    # 检查禁用场景
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    # Step 1: 上传并生成中性背景基础照
    print("Step 1: 生成基础照...")
    image_url = upload_image_to_wavespeed(REFERENCE_IMAGE_PATH)
    if not image_url:
        return None
    
    base_prompt = "portrait photo, neutral soft gradient background, professional lighting, half-body shot, clean simple backdrop, keep facial features and hairstyle consistent"
    base_task_id = call_grok_edit(image_url, base_prompt)
    if not base_task_id:
        return None
    
    base_image_url = poll_result(base_task_id)
    if not base_image_url:
        return None
    
    # 下载基础照作为第二步的输入
    base_image_path = "/tmp/zhuoran_base_temp.png"
    if not download_image(base_image_url, base_image_path):
        return None
    
    # Step 2: 上传基础照并生成场景
    print("Step 2: 生成场景照...")
    scene_info = SCENE_TEMPLATES.get(scene)
    if not scene_info:
        print(f"Unknown scene: {scene}")
        return None
    
    step2_image_url = upload_image_to_wavespeed(base_image_path)
    if not step2_image_url:
        return None
    
    template = PROMPT_TEMPLATES.get(mode, PROMPT_TEMPLATES["direct"])
    prompt = template.format(scene_description=scene_info["prompt"])
    
    task_id = call_grok_edit(step2_image_url, prompt)
    if not task_id:
        return None
    
    image_url = poll_result(task_id)
    
    # 清理临时文件
    if os.path.exists(base_image_path):
        os.remove(base_image_path)
    
    return image_url

def generate_smart(scene: str, mode: Literal["direct", "selfie", "portrait"] = "direct") -> Optional[str]:
    """智能判断：根据场景变化幅度自动选择一步或两步"""
    # 检查禁用场景
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    scene_info = SCENE_TEMPLATES.get(scene)
    if not scene_info:
        print(f"Unknown scene: {scene}")
        return None
    
    change_level = scene_info.get("change_level", "medium")
    
    if change_level in ["minimal", "low"]:
        print(f"🤖 智能判断：{scene} 变化幅度{change_level}，使用一步直达")
        return generate_one_step(scene, mode)
    else:
        print(f"🤖 智能判断：{scene} 变化幅度{change_level}，使用两步法")
        return generate_two_step(scene, mode)

def send_via_openclaw(image_path: str, target: str, caption: str = "") -> bool:
    """通过飞书 API 发送图片"""
    import requests
    import json
    from pathlib import Path
    
    print(f"📤 发送图片到 {target}...")
    print(f"   图片: {image_path}")
    if caption:
        print(f"   配文: {caption}")
    
    try:
        # 从 .env 读取配置
        env_path = Path.home() / '.openclaw' / '.env'
        config = {}
        if env_path.exists():
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip().strip('"\'')
        
        APP_ID = config.get('FEISHU_APP_ID')
        APP_SECRET = config.get('FEISHU_APP_SECRET')
        
        # 获取 token
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        resp = requests.post(url, json={"app_id": APP_ID, "app_secret": APP_SECRET})
        token = resp.json()["tenant_access_token"]
        
        # 上传图片
        url = "https://open.feishu.cn/open-apis/im/v1/images"
        headers = {"Authorization": f"Bearer {token}"}
        
        with open(image_path, "rb") as f:
            files = {"image": (Path(image_path).name, f, "image/png")}
            data = {"image_type": "message"}
            resp = requests.post(url, headers=headers, files=files, data=data)
        
        result = resp.json()
        if result.get("code") == 0:
            image_key = result["data"]["image_key"]
            
            # 发送图片消息
            url = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            
            content = json.dumps({"image_key": image_key})
            data = {
                "receive_id": target,
                "msg_type": "image",
                "content": content
            }
            
            resp = requests.post(url, headers=headers, json=data)
            result = resp.json()
            if result.get("code") == 0:
                print(f"✅ 图片发送成功: {result['data']['message_id']}")
                return True
            else:
                print(f"❌ 发送失败: {result}")
                return False
        else:
            print(f"❌ 上传失败: {result}")
            return False
    except Exception as e:
        print(f"❌ 发送异常: {e}")
        return False

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("Usage: python zhuoran_selfie.py <scene> [mode] [method] [target]")
        print(f"Scenes: {', '.join(SCENE_TEMPLATES.keys())}")
        print("Modes: direct, selfie, portrait")
        print("Methods: one_step, two_step, smart (default)")
        print("Target: user_id or channel (optional)")
        sys.exit(1)
    
    scene = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "direct"
    method = sys.argv[3] if len(sys.argv) > 3 else "smart"
    target = sys.argv[4] if len(sys.argv) > 4 else None
    
    # 检查禁用场景
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险场景，避免使用）")
        sys.exit(1)
    
    # 选择生成方法
    if method == "one_step":
        image_url = generate_one_step(scene, mode)
    elif method == "two_step":
        image_url = generate_two_step(scene, mode)
    else:  # smart
        image_url = generate_smart(scene, mode)
    
    if image_url:
        print(f"✅ 生成成功: {image_url}")
        
        # 下载保存
        output_path = f"/tmp/zhuoran_{scene}_{method}.png"
        if download_image(image_url, output_path):
            print(f"💾 已保存: {output_path}")
            
            # 如果指定了目标，发送
            if target:
                send_via_openclaw(output_path, target)
        
        return image_url
    else:
        print("❌ 生成失败")
        return None

if __name__ == "__main__":
    main()
