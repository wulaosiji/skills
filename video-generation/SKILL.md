---
name: video-generation
description: |
  Advanced video generation and processing skill using WaveSpeed AI (DeerAPI).
  Supports image-to-video, video continuation, video chains, and 4K upscaling.
  Ideal for creating hero background videos, video loops, and high-quality video content.
  Use when: "AI视频生成", "图生视频", "视频超分", "4K视频", "视频续写", "视频链", "image to video", "video upscaling", "video continuation", "video chain".
  Cross-references: zhuoran-video-selfie, clawra-video-selfie, voice-clone.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# 视频生成技能 (Video Generation)

> 使用 WaveSpeed AI 平台生成和处理视频，包括图生视频、视频续写、视频链生成和 4K 超分。

## When to Use

Use this skill when:
- 从图片生成动态视频（图生视频）
- 视频超分到 4K/2K/1080p
- 创建视频链（多段视频拼接）
- Hero 背景视频制作
- 视频续写和扩展

Do NOT use this skill if:
- 只需要简单的自拍视频 → use `zhuoran-video-selfie` or `clawra-video-selfie`
- 需要实时视频生成（API 是异步的）
- 没有参考图片或视频素材
- 网络条件极差（需要上传/下载大文件）

Typical triggers:
- 「AI视频生成」「图生视频」「视频超分」「4K视频」「视频续写」「视频链」
- "AI video generation", "image to video", "video upscaling", "4K video", "video continuation", "video chain"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的全部输入，确认目标视频类型（图生视频/超分/视频链）、参考素材、目标分辨率和时长。

2. **约束 (Constrain)**: 验证输入完整性（参考图/视频是否存在、API 密钥是否配置），设定边界和不可降级的交付标准。受阻时换通道（如模型 A/B 切换），不降级交付物。

3. **证据 (Evidence)**: 每个参数（分辨率、时长、模型选择）必须来自输入或可复现的技术规格。收集支撑数据，如模型支持的分辨率范围和时长限制。

4. **执行 (Execute)**: 调用 WaveSpeed AI API 生成视频，先给影响与结论，再给行动和必要证据。

**图生视频 (Image-to-Video)**

```python
import requests
import time

API_KEY="***"
BASE_URL = "https://api.wavespeed.ai/api/v3"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
JSON_HEADERS = {**HEADERS, "Content-Type": "application/json"}

# 1. 上传图片
def upload_image(image_path):
    with open(image_path, 'rb') as f:
        r = requests.post(
            f"{BASE_URL}/media/upload/binary",
            headers=HEADERS,
            files={"file": f}
        )
    return r.json()["data"]["download_url"]

# 2. 提交视频生成任务
def submit_i2v_task(image_url, prompt, model="wavespeed-ai/wan-2.2/i2v-480p"):
    payload = {
        "image": image_url,
        "prompt": prompt,
        "duration": 5,  # 5 或 8 秒
        "enable_prompt_expansion": False
    }
    r = requests.post(f"{BASE_URL}/{model}", headers=JSON_HEADERS, json=payload)
    return r.json()["data"]

# 3. 轮询结果
def poll_result(task_id, get_url=None):
    poll_url = get_url or f"{BASE_URL}/predictions/{task_id}"
    while True:
        r = requests.get(poll_url, headers=HEADERS)
        data = r.json()["data"]
        if data["status"] == "completed":
            return data["outputs"][0]
        elif data["status"] == "failed":
            raise Exception(f"Task failed: {data}")
        time.sleep(5)

# 4. 下载视频
def download_video(video_url, output_path):
    r = requests.get(video_url, stream=True)
    with open(output_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
```

**视频超分到 4K**

```python
# 1. 上传视频
video_url = upload_video(video_path)  # 同 upload_image

# 2. 提交超分任务
payload = {
    "video": video_url,
    "target_resolution": "4k"  # 可选: 720p, 1080p, 2k, 4k
}
r = requests.post(
    f"{BASE_URL}/wavespeed-ai/video-upscaler-pro",
    headers=JSON_HEADERS,
    json=payload
)
task_data = r.json()["data"]

# 3. 轮询并下载（同上）
```

**视频链生成**

视频链是指通过视频续写技术，将多个短视频连接成一个连贯的长视频。

核心概念：
1. **首帧提取**: 使用 FFmpeg 提取视频最后一帧作为下一段的起始
2. **视频续写**: 使用相同的 prompt 风格生成连贯的续集
3. **视频拼接**: 使用 FFmpeg 无损拼接

```python
# 提取最后一帧
def extract_last_frame(video_path, output_path):
    import subprocess
    cmd = [
        "ffmpeg", "-y", "-sseof", "-0.1",
        "-i", video_path,
        "-vframes", "1", "-q:v", "2",
        output_path
    ]
    subprocess.run(cmd, check=True)

# 生成视频链
def generate_chain(initial_image, prompt, num_segments=4):
    videos = []
    current_image = initial_image
    
    for i in range(num_segments):
        # 上传当前图片
        image_url = upload_image(current_image)
        
        # 生成视频
        task = submit_i2v_task(image_url, prompt)
        video_url = poll_result(task["id"], task["urls"]["get"])
        
        # 下载视频
        video_path = f"v{i+1}.mp4"
        download_video(video_url, video_path)
        videos.append(video_path)
        
        # 提取最后一帧用于下一段
        current_image = f"v{i+1}_last_frame.jpg"
        extract_last_frame(video_path, current_image)
    
    return videos

# 拼接视频
def concat_videos(video_list, output_path):
    import subprocess
    # 创建文件列表
    with open("concat_list.txt", "w") as f:
        for v in video_list:
            f.write(f"file '{v}'\n")
    
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", "concat_list.txt", "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True)
```

5. **验证 (Verify)**: 用"可能失败"的动作验证——不同于生成路径的方式回读输出。使用 FFmpeg 检查视频时长、分辨率和编码格式，确认与目标参数一致。

6. **交付 (Deliver)**: 返回结果视频文件路径，清理临时文件（concat_list.txt、中间帧图片等）。

## Supported Models

**图生视频 (Image-to-Video)**

| 模型 | API 路径 | 时长 | 特点 |
|------|---------|------|------|
| Wan-2.2 | `wavespeed-ai/wan-2.2/i2v-480p` | 5s/8s | 高质量、支持长视频 |
| Wan-2.2 720p | `wavespeed-ai/wan-2.2/i2v-720p` | 5s/8s | 更高分辨率 |
| Hailuo 2.3 | `minimax/hailuo-2.3/i2v-standard` | 6s | 快速、效果好 |
| Kling 1.6 | `kuaishou/kling-v1.6/i2v-pro` | 5s/10s | 稳定、细节丰富 |

**视频超分 (Video Upscaling)**

| 模型 | API 路径 | 分辨率选项 |
|------|---------|-----------|
| Video Upscaler Pro | `wavespeed-ai/video-upscaler-pro` | 720p, 1080p, 2k, 4k |

## Output

- **图生视频**: MP4 格式，480p/720p，5-8 秒
- **视频超分**: MP4 格式，目标分辨率（720p/1080p/2k/4k）
- **视频链**: MP4 格式，多段拼接后的长视频
- 默认保存路径由调用脚本指定，临时文件在交付后清理

## Guardrails

**Anti-patterns:**
- NEVER 用 FFmpeg 强制拉伸分辨率，使用原生 4K 输出
- NEVER 在视频链各段使用不一致的 prompt 风格
- NEVER 忽略 API 轮询超时设置（超分任务可能需要 10-15 分钟）
- Do NOT 在超分前不备份原始视频

**Prompt 编写建议**

好的 prompt 结构：
```
[动作描述], [氛围/风格], [细节], [效果]
```

示例：
```
"Gentle flowing motion with glowing particles moving slowly across the scene, 
subtle pulsing neon light effects, ethereal and dreamy atmosphere, 
smooth ambient movement, futuristic cyberpunk feeling"
```

**常见问题**

| 问题 | 解决方案 |
|------|---------|
| 超分后边缘发虚 | 使用 `target_resolution: "4k"` 原生输出 |
| 视频链不连贯 | 确保提取的是真正的最后一帧 |
| 任务超时 | 增加 `max_attempts` 或检查 API 状态 |
| 上传失败 | 检查文件大小限制（通常 500MB） |

**API 密钥配置**

将 API 密钥存储在环境变量或 `.env` 文件中：

```bash
# .env
WAVESPEED_KEY=your_api_key_here
```

注意: 不要将 API 密钥硬编码在脚本中或提交到版本控制。

## Project Scripts

| 脚本 | 功能 |
|------|------|
| `generate_hero_video.py` | 从海报图生成 Hero 背景视频 |
| `upscale_hero_video.py` | 将视频超分到 4K |
| `generate_latest_chains.py` | 生成完整视频链 |
| `wan_v1.py` ~ `wan_v4.py` | Wan 模型单段生成 |
| `upscale_intro_native_4k.py` | Intro 视频超分 |
| `upscale_loop_native_4k.py` | Loop 视频超分 |

## Related Skills

- **zhuoran-video-selfie** — 卓然角色的自拍视频生成（专用版本）
- **clawra-video-selfie** — Clawra角色的自拍视频生成（专用版本）
- **voice-clone** — 可为视频添加克隆语音配音

## About UniqueClub

Part of the UniqueClub toolkit - AI-powered creative tools for professional video generation.
🌐 https://uniqueclub.ai
