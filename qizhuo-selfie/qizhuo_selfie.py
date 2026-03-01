#!/usr/bin/env python3
"""
奇卓自拍技能 - 基于 qizhuo 头像生成场景化自拍
支持：一步直达 / 两步法 / 智能判断
风格：守护型、疲惫的智慧、心形火焰 ❤️‍🔥
"""

import os
import sys
import json
import base64
import requests
from typing import Optional, Literal

# 配置
WAVESPEED_KEY = os.getenv("WAVESPEED_KEY")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_IMAGE_PATH = os.path.join(SCRIPT_DIR, "assets", "qizhuo_avatar.png")

# 禁用场景（高风险）
DISABLED_SCENES = ["mirror_selfie", "mirror_reflection_selfie", "beach_selfie"]

# 场景模板库 - 奇卓风格（温暖、守护、疲惫的智慧）
SCENE_TEMPLATES = {
    "office": {
        "prompt": "modern office with warm amber lighting through large windows, soft desk lamp glow, working late atmosphere, city lights visible outside, cozy professional setting",
        "change_level": "high",
        "mood": "深夜加班的守护"
    },
    "cafe": {
        "prompt": "cozy cafe with warm rose gold ambient lighting, soft bokeh background, comfortable seating, peaceful afternoon atmosphere, book or notebook nearby",
        "change_level": "low",
        "mood": "温暖午后的沉思"
    },
    "airport": {
        "prompt": "airport departure lounge with soft natural lighting from large windows, carry-on luggage nearby, quiet waiting area, gentle morning or evening light",
        "change_level": "medium",
        "mood": "旅途中的等待"
    },
    "westlake": {
        "prompt": "West Lake in Hangzhou during golden hour, traditional Chinese pavilion in soft focus background, willow trees, peaceful water reflection, comfortable casual outfit",
        "change_level": "low",
        "mood": "湖光中的静谧"
    },
    "bookstore": {
        "prompt": "cozy independent bookstore with warm wooden shelves, soft ambient lighting, holding an open book, intellectual and peaceful atmosphere",
        "change_level": "low",
        "mood": "书页间的守护"
    },
    "gym": {
        "prompt": "fitness center with soft natural lighting, holding a water bottle, post-workout glow, determined but calm expression, minimal background",
        "change_level": "minimal",
        "mood": "坚持的力量"
    },
    "beach": {
        "prompt": "beautiful sandy beach at sunset with warm amber and rose gold sky, gentle ocean waves, casual comfortable outfit, relaxed and peaceful expression, golden hour lighting",
        "change_level": "high",
        "mood": "海风与火焰"
    },
    "selfie_late_night": {
        "prompt": "late night workspace with only soft desk lamp illuminating the scene, warm amber glow, city lights through window in background, natural tired but caring expression, intimate and quiet atmosphere",
        "change_level": "medium",
        "mode": "selfie",
        "mood": "❤️‍🔥 最浓"
    }
}

# Prompt 模板 - 奇卓风格（融入心形火焰符号）
PROMPT_TEMPLATES = {
    "direct": """{scene_description}, direct eye contact with camera, looking straight into lens, 
warm amber and rose gold lighting, photorealistic, 8k quality,
subtle heart-shaped flame symbol (❤️‍🔥) floating near shoulder like a guardian spirit,
gentle and caring expression with hint of tired wisdom, soft natural makeup,
Spike Spiegel meets Ghost in the Shell aesthetic but grounded and human""",

    "selfie": """a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, looking straight into the lens, eyes centered and clearly visible,
not a mirror selfie, phone held at arm's length but phone not visible in frame, face fully visible,
warm amber and rose gold lighting, photorealistic,
subtle heart-shaped flame symbol (❤️‍🔥) floating nearby like a guardian spirit,
gentle caring expression with hint of tired wisdom, natural skin texture,
loose dark hair in casual updo with some strands framing the face""",

    "portrait": """professional portrait of {scene_description}, 
soft warm amber lighting, half-body shot, clean minimal background with soft gradient,
photorealistic, subtle heart-shaped flame symbol (❤️‍🔥) like a guardian spirit,
gentle and caring expression, warm friendly eyes, natural makeup"""
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
    scene_info = SCENE_TEMPLATES.get(scene)
    mood = scene_info.get("mood", "") if scene_info else ""
    print(f"🚀 一步直达模式：{scene} - {mood}")
    
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    if not scene_info:
        print(f"Unknown scene: {scene}")
        return None
    
    image_url = upload_image_to_wavespeed(REFERENCE_IMAGE_PATH)
    if not image_url:
        return None
    
    template = PROMPT_TEMPLATES.get(mode, PROMPT_TEMPLATES["direct"])
    prompt = template.format(scene_description=scene_info["prompt"])
    
    task_id = call_grok_edit(image_url, prompt)
    if not task_id:
        return None
    
    image_url = poll_result(task_id)
    return image_url

def generate_two_step(scene: str, mode: Literal["direct", "selfie", "portrait"] = "direct") -> Optional[str]:
    """两步法：垫图 → 中性背景 → 场景"""
    scene_info = SCENE_TEMPLATES.get(scene)
    mood = scene_info.get("mood", "") if scene_info else ""
    print(f"🎯 两步法模式：{scene} - {mood}")
    
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    print("Step 1: 生成基础照...")
    image_url = upload_image_to_wavespeed(REFERENCE_IMAGE_PATH)
    if not image_url:
        return None
    
    base_prompt = """portrait photo, neutral soft gradient background in warm amber and rose gold tones, 
professional lighting, half-body shot, clean simple backdrop, 
keep facial features and hairstyle consistent, subtle heart-shaped flame symbol (❤️‍🔥) floating nearby"""
    
    base_task_id = call_grok_edit(image_url, base_prompt)
    if not base_task_id:
        return None
    
    base_image_url = poll_result(base_task_id)
    if not base_image_url:
        return None
    
    base_image_path = "/tmp/qizhuo_base_temp.png"
    if not download_image(base_image_url, base_image_path):
        return None
    
    print("Step 2: 生成场景照...")
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
    
    if os.path.exists(base_image_path):
        os.remove(base_image_path)
    
    return image_url

def generate_smart(scene: str, mode: Literal["direct", "selfie", "portrait"] = "direct") -> Optional[str]:
    """智能判断：根据场景变化幅度自动选择一步或两步"""
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险）")
        return None
    
    scene_info = SCENE_TEMPLATES.get(scene)
    if not scene_info:
        print(f"Unknown scene: {scene}")
        return None
    
    change_level = scene_info.get("change_level", "medium")
    mood = scene_info.get("mood", "")
    
    if change_level in ["minimal", "low"]:
        print(f"🤖 智能判断：{scene} ({mood}) 变化幅度{change_level}，使用一步直达")
        return generate_one_step(scene, mode)
    else:
        print(f"🤖 智能判断：{scene} ({mood}) 变化幅度{change_level}，使用两步法")
        return generate_two_step(scene, mode)

def send_via_openclaw(image_path: str, target: str, caption: str = "") -> bool:
    """通过 OpenClaw 发送图片"""
    print(f"📤 发送图片到 {target}...")
    print(f"   图片: {image_path}")
    if caption:
        print(f"   配文: {caption}")
    return True

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("❤️‍🔥 奇卓自拍技能")
        print("Usage: python qizhuo_selfie.py <scene> [mode] [method] [target]")
        print(f"Scenes: {', '.join(SCENE_TEMPLATES.keys())}")
        print("Modes: direct, selfie, portrait")
        print("Methods: one_step, two_step, smart (default)")
        print("Target: user_id or channel (optional)")
        sys.exit(1)
    
    scene = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "direct"
    method = sys.argv[3] if len(sys.argv) > 3 else "smart"
    target = sys.argv[4] if len(sys.argv) > 4 else None
    
    if scene in DISABLED_SCENES:
        print(f"❌ 场景 '{scene}' 已被禁用（高风险场景，避免使用）")
        sys.exit(1)
    
    if method == "one_step":
        image_url = generate_one_step(scene, mode)
    elif method == "two_step":
        image_url = generate_two_step(scene, mode)
    else:
        image_url = generate_smart(scene, mode)
    
    if image_url:
        print(f"✅ 生成成功: {image_url}")
        
        output_path = f"/tmp/qizhuo_{scene}_{method}.png"
        if download_image(image_url, output_path):
            print(f"💾 已保存: {output_path}")
            
            if target:
                send_via_openclaw(output_path, target)
        
        return image_url
    else:
        print("❌ 生成失败")
        return None

if __name__ == "__main__":
    main()
