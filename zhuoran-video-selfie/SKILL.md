---
name: zhuoran-video-selfie
description: |
  Zhuoran AI selfie video generation skill using WaveSpeed AI Seedance model.
  Creates living selfie videos with natural micro-movements like breathing and blinking.
  Supports office, cafe, westlake, and gym scenes with authentic selfie perspective.
  Use when: "卓然视频", "AI视频生成", "动态自拍", "活人感视频", "视频自拍", "zhuoran video", "dynamic selfie", "living video", "video selfie", "character video".
  Cross-references: zhuoran-selfie, clawra-video-selfie, video-generation.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# 卓然视频自拍技能 (Zhuoran Video Selfie)

> 基于垫图使用 WaveSpeed AI 生成"活人感"自拍视频，支持自然微动作（呼吸、眨眼等）。

## When to Use

Use this skill when:
- 需要生成卓然角色的动态自拍视频
- 为照片添加生命力和动态感
- 展示角色在场景中的自然状态
- 需要微动作增强真实感
- 用户索要视频或动态展示

Do NOT use this skill if:
- 只需要静态照片 → use `zhuoran-selfie` 更高效
- 需要大幅度动作场景（如跳舞、走路）
- 需要多人同框视频
- 需要复杂的镜头运动
- 网络条件极差（视频文件较大）

Typical triggers:
- 「卓然视频」「AI视频生成」「动态自拍」「活人感视频」「视频自拍」「角色视频」
- "zhuoran video", "AI video generation", "dynamic selfie", "living video", "video selfie", "character video"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的场景，确认目标场景代码、视频时长和输出要求。检查垫图文件 `assets/zhuoran_portrait_base.png` 是否存在。

2. **约束 (Constrain)**: 验证输入完整性，设定边界：最长5秒、仅使用预定义安全场景、微动作优先。受阻时切换备用模型（VidU Q3 Turbo），不降级交付物。

3. **证据 (Evidence)**: 每个场景的推荐时长和提示词重点来自预定义场景模板。模型选择基于 A/B 机制（Seedance v1 pro 首选，VidU Q3 Turbo 备用）。

4. **执行 (Execute)**: 调用 WaveSpeed AI API 生成视频，先给影响与结论，再给行动和必要证据。

**快速开始**

```bash
# 生成办公室自拍视频
openclaw skill run zhuoran-video-selfie office

# 指定场景并发送
openclaw skill run zhuoran-video-selfie cafe --target ou_xxx

# 直接调用脚本
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh westlake
```

**命令行参数**

```bash
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh <scene> \
  --duration 5 \
  --target <user_id> \
  --caption "配文" \
  --output /path/to/output.mp4
```

**垫图配置**

重要: 本 skill 需要垫图文件 `assets/zhuoran_portrait_base.png`。

首次使用前请复制垫图:
```bash
cp ~/.openclaw/workspace/assets/avatars/zhuoran_portrait_base.png \
   ~/.openclaw/workspace/skills/zhuoran-video-selfie/assets/
```

垫图要求: PNG格式、真人照片（非卡通形象）、建议512x512或更高、背景简洁。

**API 调用流程**

1. 上传参考图 → WaveSpeed AI 媒体上传
2. 提交视频生成任务 → `POST /api/v3/x-ai/video/generate`（模型: `bytedance/seedance-v1-pro-i2v-720p`，参数: duration=5, aspect_ratio="1:1"）
3. 轮询结果 → `GET /api/v3/predictions/{task_id}/result`
4. 下载视频 → 保存到临时目录
5. 飞书发送（如指定 target）→ 上传获取 file_key → 发送消息

**Python API**

```python
from skills.zhuoran_video_selfie.zhuoran_video_selfie import generate_video

# 生成视频
video_path = generate_video("office", duration=5)

# 生成并发送
video_path = generate_video("cafe", duration=5, target="ou_xxx")
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——使用 FFmpeg 检查视频时长、分辨率和编码格式，确认微动作自然不僵硬。

6. **交付 (Deliver)**: 返回视频文件路径，如指定 target 则通过飞书发送（使用 `msg_type: "media"`），清理临时文件。

## Available Scenes

| 场景 | 代码 | 推荐时长 | 提示词重点 |
|------|------|---------|-----------|
| 办公室 | `office` | 5秒 | 自然工作姿态、微动作 |
| 咖啡厅 | `cafe` | 5秒 | 轻松氛围、微笑 |
| 西湖 | `westlake` | 5秒 | 风景互动、微风 |
| 健身房 | `gym` | 3秒 | 运动姿态、呼吸感 |

## Output

- 格式: MP4 (H.264)
- 分辨率: 720p
- 比例: 1:1 (正方形，适合自拍)
- 时长: 3-5 秒
- 默认保存: `/tmp/zhuoran_{场景}_video.mp4`

## Guardrails

**Anti-patterns:**
- NEVER 使用镜子自拍场景（`mirror_selfie`），逻辑破绽明显
- NEVER 生成大幅度动作场景（`dancing`、`walking`），肢体一致性难保证
- NEVER 生成多人入镜视频（`group`），复杂度太高
- NEVER 生成水下场景（`swimming`），物理逻辑复杂
- Do NOT 视频时长超过5秒，避免暴露不自然动作

**风险控制原则**
- 时长限制: 最长5秒，避免暴露不自然动作
- 场景限制: 仅使用预定义的安全场景
- 动作限制: 微动作优先（呼吸、眨眼），避免大幅度运动
- 频率限制: 视频比照片使用频率更低
- 垫图质量: 确保垫图清晰，面部特征明确

**"活人感"提示词系统**

核心原则：自然微动（呼吸、眨眼、头发飘动）、避免完美（保留皮肤纹理、自然瑕疵）、场景真实（自拍角度、环境互动）。

基础模板：
```
{scene_description}, subtle breathing motion and natural posture shift, 
gentle hair swaying in {environment} breeze, soft smile with micro-expressions, 
occasional natural blink and eye movement, {interaction}, 
authentic selfie perspective with slight arm visible, 
natural skin texture with realistic details, 4k cinematic quality, 
shallow depth of field, lifelike atmosphere
```

**备用模型方案（A/B 机制）**

| 优先级 | 模型 | 端点 | 状态 | 说明 |
|-------|------|------|------|------|
| A方案 | Seedance v1 pro 720p | `/bytedance/seedance-v1-pro-i2v-720p` | ✅ 可用 | 首选，质量好 |
| B方案 | VidU Q3 Turbo | `/vidu/q3-turbo/image-to-video` | ✅ 可用 | 备用，稳定 |

**飞书视频发送**

重要: 视频不能直接通过 OpenClaw `message` 工具的 `filePath` 发送，否则会显示为文件附件无法播放。必须使用 `msg_type: "media"` 而非 `"file"`，必须同时提供 `file_key`（视频）和 `image_key`（封面）。

```bash
python3 skills/feishu-video-sender/feishu_video_sender.py \
  /tmp/zhuoran_office_video.mp4 \
  ou_5f3a4a920dc39a8d1835fd0085afef50
```

**Environment Requirements**

- `WAVESPEED_KEY`: WaveSpeed AI API 密钥
- `FEISHU_APP_ID`: 飞书 App ID（用于发送）
- `FEISHU_APP_SECRET`: 飞书 App Secret
- Python 3.8+
- 依赖: requests

## File Structure

```
skills/zhuoran-video-selfie/
├── SKILL.md                    # 本文档
├── zhuoran_video_selfie.py     # 核心逻辑
└── scripts/
    ├── zhuoran-video-selfie.py # Python CLI 入口
    └── zhuoran-video-selfie.sh # Bash 包装脚本（OpenClaw 入口）
```

## Related Skills

- **zhuoran-selfie** — 同一角色的静态照片生成（照片版）
- **clawra-video-selfie** — Clawra角色的视频生成（对应角色）
- **video-generation** — 更通用的视频生成和超分功能

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for dynamic video generation.
🌐 https://uniqueclub.ai
