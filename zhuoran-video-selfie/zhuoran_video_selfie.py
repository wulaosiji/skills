#!/usr/bin/env python3
"""
卓然视频自拍技能 - 核心逻辑 (已修复)
基于垫图使用 WaveSpeed AI 生成"活人感"自拍视频

修复: 使用正确的 WaveSpeed API 端点 (参考 video_core.py)
"""

import os
import sys
import json
import time
import requests
from pathlib import Path

# 配置
BASE_URL = "https://api.wavespeed.ai/api/v3"
API_KEY = os.environ.get("WAVESPEED_KEY", "b9c67f3def268385bb9734970b11531f12ea24ae0d153859242e48ae46227668")
# 获取脚本所在目录，构建相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_IMAGE = os.environ.get("ZHUORAN_REFERENCE", os.path.join(SCRIPT_DIR, "assets", "zhuoran_portrait_base.png"))

# 场景模板
SCENE_TEMPLATES = {
    "office": {
        "prompt": "young professional woman at modern office desk with city view through window, subtle breathing motion and natural posture shift, gentle hair swaying in air-conditioned breeze, soft smile with micro-expressions, occasional natural blink and eye movement, working on laptop and occasionally glancing up from screen, authentic selfie perspective with slight arm visible, relaxed and genuine mood, natural skin texture with realistic details, natural office lighting, 4k cinematic quality, shallow depth of field, lifelike atmosphere",
        "change_level": "medium"
    },
    "cafe": {
        "prompt": "young woman at cozy urban cafe with warm ambient lighting, subtle breathing motion and natural posture shift, gentle hair swaying, soft smile with micro-expressions, occasional natural blink, holding coffee cup with gentle steam rising, authentic selfie perspective with slight arm visible, relaxed and genuine mood, natural skin texture with realistic details, 4k cinematic quality, shallow depth of field, lifelike atmosphere",
        "change_level": "low"
    },
    "westlake": {
        "prompt": "young woman at West Lake Hangzhou with iconic scenery, subtle breathing motion and natural posture shift, gentle hair swaying in lakeside breeze, soft smile with micro-expressions, occasional natural blink and eye movement, enjoying the scenery with gentle head turn, golden hour sunlight creating warm glow, water reflection in background, willow trees swaying, authentic selfie perspective with slight arm visible, relaxed and genuine mood, natural skin texture with realistic details, 4k cinematic quality, shallow depth of field, lifelike atmosphere",
        "change_level": "low"
    },
    "gym": {
        "prompt": "young athletic woman at modern gym with exercise equipment in background, wearing fitted athletic tank top and sports leggings, subtle breathing motion and natural posture shift, gentle hair movement tied back in ponytail, soft determined expression with micro-expressions, occasional natural blink, light workout posture with natural exertion, holding smartphone for selfie, authentic selfie perspective with slight arm visible, focused and genuine mood, natural skin texture with realistic details including slight sweat glow, gym lighting with fluorescent highlights, 4k cinematic quality, shallow depth of field, lifelike atmosphere",
        "change_level": "medium"
    }
}

# 禁用场景
DISABLED_SCENES = [
    "mirror_selfie",
    "mirror_reflection_selfie",
    "dancing",
    "walking",
    "group",
    "swimming",
    "running"
]

def log(message):
    """打印日志"""
    print(f"[zhuoran-video-selfie] {message}", file=sys.stderr)

def upload_reference_image(image_path):
    """
    上传参考图到 WaveSpeed AI
    修复: 使用正确的 /media/upload/binary 端点
    """
    log(f"正在上传参考图: {image_path}")
    
    # 修复: 使用正确的上传端点
    upload_url = f"{BASE_URL}/media/upload/binary"
    
    with open(image_path, 'rb') as f:
        files = {'file': ('reference.png', f, 'image/png')}
        headers = {'Authorization': f'Bearer {API_KEY}'}
        
        response = requests.post(upload_url, headers=headers, files=files)
        
        if response.status_code != 200:
            log(f"上传失败: {response.status_code} - {response.text[:200]}")
            raise Exception(f"上传失败: {response.status_code}")
        
        result = response.json()
        
        if result.get('code') == 200:
            # 修复: 正确的图片URL路径
            image_url = result['data']['download_url']
            log(f"✅ 参考图上传成功")
            return image_url
        else:
            raise Exception(f"上传失败: {result.get('message')}")

def generate_video_task(image_url, prompt, duration=5):
    """
    提交视频生成任务
    修复: 使用正确的 /wavespeed-ai/wan-2.2/i2v-480p 端点
    """
    log(f"提交视频生成任务...")
    
    # 修复: 使用正确的视频生成端点
    endpoint = f"{BASE_URL}/wavespeed-ai/wan-2.2/i2v-480p"
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "image": image_url,
        "prompt": prompt,
        "duration": duration,
        "enable_prompt_expansion": False
    }
    
    response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
    result = response.json()
    
    if result.get('code') == 200:
        task_id = result['data']['id']
        log(f"✅ 任务提交成功: {task_id}")
        return task_id
    else:
        raise Exception(f"任务提交失败: {result.get('message')}")

def poll_task_result(task_id, timeout=300):
    """
    轮询任务结果
    修复: 使用正确的结果查询端点
    """
    log(f"⏳ 等待视频生成 (最长{timeout}秒)...")
    
    # 修复: 正确的结果查询端点
    result_url = f"{BASE_URL}/predictions/{task_id}/result"
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(result_url, headers=headers)
        result = response.json()
        
        if result.get('code') != 200:
            log(f"查询失败: {result.get('message')}")
            time.sleep(5)
            continue
        
        data = result['data']
        status = data.get('status')
        
        if status == 'completed':
            outputs = data.get('outputs', [])
            if outputs:
                video_url = outputs[0]
                log(f"✅ 视频生成完成")
                return video_url
            else:
                raise Exception("任务完成但无输出")
        
        elif status == 'failed':
            error = data.get('error', 'Unknown error')
            raise Exception(f"视频生成失败: {error}")
        
        log(f"  [{int(time.time() - start_time)}s] 状态: {status}")
        time.sleep(10)
    
    raise TimeoutError(f"轮询超时 ({timeout}秒)")

def download_video(video_url, output_path):
    """下载视频到本地"""
    log(f"⬇️ 下载视频...")
    
    response = requests.get(video_url, stream=True)
    response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    file_size = os.path.getsize(output_path) / 1024
    log(f"✅ 视频下载完成: {file_size:.1f} KB")
    return output_path

def send_to_feishu(video_path, target_id):
    """发送视频到飞书"""
    log(f"📤 发送视频到飞书: {target_id}")
    
    # 调用 feishu-video-sender
    import subprocess
    result = subprocess.run([
        'python3',
        'skills/feishu-video-sender/feishu_video_sender.py',
        video_path,
        target_id
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        log("✅ 发送成功")
    else:
        log(f"❌ 发送失败: {result.stderr}")

def generate_video(scene, duration=5, output_path=None, target=None):
    """
    生成自拍视频
    
    Args:
        scene: 场景名称 (office/cafe/westlake/gym)
        duration: 视频时长 (秒)
        output_path: 输出路径
        target: 飞书目标ID (发送)
    """
    # 检查场景是否可用
    if scene in DISABLED_SCENES:
        raise ValueError(f"场景 '{scene}' 已被禁用")
    
    if scene not in SCENE_TEMPLATES:
        raise ValueError(f"未知场景: {scene}. 可用: {list(SCENE_TEMPLATES.keys())}")
    
    # 获取场景配置
    scene_config = SCENE_TEMPLATES[scene]
    prompt = scene_config['prompt']
    
    log(f"🎬 开始生成场景: {scene}, 时长: {duration}秒")
    
    try:
        # 1. 上传参考图
        image_url = upload_reference_image(REFERENCE_IMAGE)
        
        # 2. 提交视频生成任务
        task_id = generate_video_task(image_url, prompt, duration)
        
        # 3. 轮询结果
        video_url = poll_task_result(task_id)
        
        # 4. 下载视频
        if not output_path:
            output_path = f"/tmp/zhuoran_{scene}_video.mp4"
        
        download_video(video_url, output_path)
        
        # 5. 发送到飞书（如果指定了目标）
        if target:
            send_to_feishu(output_path, target)
        
        log(f"✅ 全部完成: {output_path}")
        return output_path
        
    except Exception as e:
        log(f"❌ 生成失败: {e}")
        raise

def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description='卓然视频自拍生成')
    parser.add_argument('scene', choices=list(SCENE_TEMPLATES.keys()), help='场景')
    parser.add_argument('--duration', type=int, default=5, help='时长(秒)')
    parser.add_argument('--output', help='输出路径')
    parser.add_argument('--target', help='飞书目标ID(发送)')
    
    args = parser.parse_args()
    
    try:
        output = generate_video(args.scene, args.duration, args.output, args.target)
        print(output)  # 输出路径
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
