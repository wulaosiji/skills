---
name: zhuoran-video-selfie
description: |
  Zhuoran AI selfie video generation skill using WaveSpeed AI Seedance model.
  Creates "living" selfie videos with natural micro-movements like breathing and blinking.
  Supports office, cafe, westlake, and gym scenes with authentic selfie perspective.

  Use when: 卓然视频, AI视频生成, 动态自拍, 活人感视频, 视频自拍, 
  zhuoran video, AI video generation, dynamic selfie, living video, 
  video selfie, character video

  Related: zhuoran-selfie, clawra-video-selfie, video-generation

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# 卓然视频自拍技能 (Zhuoran Video Selfie)

基于垫图使用 WaveSpeed AI 生成"活人感"自拍视频，支持自然微动作（呼吸、眨眼等）。

## When to Use

**适用于以下场景：**
- 需要生成卓然角色的动态自拍视频
- 为照片添加生命力和动态感
- 展示角色在场景中的自然状态
- 需要微动作增强真实感
- 用户索要视频或动态展示

**Do NOT use this skill if：**
- 只需要静态照片（使用 zhuoran-selfie 更高效）
- 需要大幅度动作场景（如跳舞、走路）
- 需要多人同框视频
- 需要复杂的镜头运动
- 网络条件极差（视频文件较大）

**触发关键词 / Trigger Phrases：**
- 卓然视频 / zhuoran video
- AI视频生成 / AI video generation
- 动态自拍 / dynamic selfie
- 活人感视频 / living video
- 视频自拍 / video selfie
- 角色视频 / character video
- 生成视频 / generate video
- 自拍视频 / selfie video

## Workflow

### 快速开始

```bash
# 生成办公室自拍视频
openclaw skill run zhuoran-video-selfie office

# 指定场景并发送
openclaw skill run zhuoran-video-selfie cafe --target ou_xxx

# 直接调用脚本
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh westlake
```

### 命令行参数

```bash
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh <scene> \
  --duration 5 \
  --target <user_id> \
  --caption "配文" \
  --output /path/to/output.mp4
```

### 垫图配置

**重要**: 本 skill 需要垫图文件 `assets/zhuoran_portrait_base.png`。

**首次使用前请复制垫图**:
```bash
# 从中央 assets 目录复制
cp ~/.openclaw/workspace/assets/avatars/zhuoran_portrait_base.png \
   ~/.openclaw/workspace/skills/zhuoran-video-selfie/assets/
```

**或者创建软链接**:
```bash
ln -s ~/.openclaw/workspace/assets/avatars/zhuoran_portrait_base.png \
      ~/.openclaw/workspace/skills/zhuoran-video-selfie/assets/zhuoran_portrait_base.png
```

**垫图要求**:
- 格式: PNG
- 内容: 真人照片（非卡通形象）
- 尺寸: 建议 512x512 或更高
- 背景: 简洁，便于场景融合

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交视频生成任务** → `POST /api/v3/x-ai/video/generate`
   - 模型: `bytedance/seedance-v1-pro-i2v-720p`
   - 输入: 垫图 URL + 提示词
   - 参数: duration=5, aspect_ratio="1:1"
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载视频** → 保存到临时目录
5. **飞书发送**（如指定 target）→ 上传获取 file_key → 发送消息

### Python API

```python
from skills.zhuoran_video_selfie.zhuoran_video_selfie import generate_video

# 生成视频
video_path = generate_video("office", duration=5)

# 生成并发送
video_path = generate_video("cafe", duration=5, target="ou_xxx")
```

## Available Scenes

| 场景 | 代码 | 推荐时长 | 提示词重点 |
|------|------|---------|-----------|
| 办公室 | `office` | 5秒 | 自然工作姿态、微动作 |
| 咖啡厅 | `cafe` | 5秒 | 轻松氛围、微笑 |
| 西湖 | `westlake` | 5秒 | 风景互动、微风 |
| 健身房 | `gym` | 3秒 | 运动姿态、呼吸感 |

## Guardrails

### 禁用场景

以下场景已被禁用（高风险）：
- `mirror_selfie` - 镜子反射，逻辑破绽明显
- `dancing` - 大幅度动作，肢体一致性难保证
- `walking` - 移动场景，背景与人物同步难
- `group` - 多人入镜，复杂度太高
- `swimming` - 水下场景，物理逻辑复杂

### 风险控制原则
- **时长限制**: 最长5秒，避免暴露不自然动作
- **场景限制**: 仅使用预定义的安全场景
- **动作限制**: 微动作优先（呼吸、眨眼），避免大幅度运动
- **频率限制**: 视频比照片使用频率更低
- **垫图质量**: 确保垫图清晰，面部特征明确

### "活人感"提示词系统

**核心原则：**
1. **自然微动** - 呼吸、眨眼、头发飘动
2. **避免完美** - 保留皮肤纹理、自然瑕疵
3. **场景真实** - 自拍角度、环境互动

**基础模板**：
```
{scene_description}, subtle breathing motion and natural posture shift, 
gentle hair swaying in {environment} breeze, soft smile with micro-expressions, 
occasional natural blink and eye movement, {interaction}, 
authentic selfie perspective with slight arm visible, 
natural skin texture with realistic details, 4k cinematic quality, 
shallow depth of field, lifelike atmosphere
```

**场景变体：**

**office**:
```
young professional woman at modern office desk, subtle breathing motion...
working on laptop, occasional glance up from screen, natural office lighting...
```

**cafe**:
```
young woman at cozy cafe, subtle breathing motion...
holding coffee cup, gentle steam rising, warm ambient lighting...
```

### 备用模型方案（A/B 机制）

| 优先级 | 模型 | 端点 | 状态 | 说明 |
|-------|------|------|------|------|
| **A方案** | Seedance v1 pro 720p | `/bytedance/seedance-v1-pro-i2v-720p` | ✅ 可用 | 首选，质量好 |
| **B方案** | VidU Q3 Turbo | `/vidu/q3-turbo/image-to-video` | ✅ 可用 | 备用，稳定 |

## 飞书视频发送

**⚠️ 重要**: 视频不能直接通过 OpenClaw `message` 工具的 `filePath` 发送，否则会显示为文件附件无法播放。

**正确方式**：

```bash
python3 skills/feishu-video-sender/feishu_video_sender.py \
  /tmp/zhuoran_office_video.mp4 \
  ou_5f3a4a920dc39a8d1835fd0085afef50
```

**技术要点**：
- 必须使用 `msg_type: "media"` 而非 `"file"`
- 必须同时提供 `file_key`（视频）和 `image_key`（封面）

## Environment Requirements

- `WAVESPEED_KEY`: WaveSpeed AI API 密钥
- `FEISHU_APP_ID`: 飞书 App ID（用于发送）
- `FEISHU_APP_SECRET`: 飞书 App Secret
- Python 3.8+
- 依赖: requests

## Output

- 格式: MP4 (H.264)
- 分辨率: 720p
- 比例: 1:1 (正方形，适合自拍)
- 时长: 3-5 秒
- 默认保存: `/tmp/zhuoran_{场景}_video.mp4`

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

| 技能 | 关系 | 说明 |
|------|------|------|
| [zhuoran-selfie](./zhuoran-selfie) | 照片版 | 同一角色的静态照片生成 |
| [clawra-video-selfie](./clawra-video-selfie) | 对应角色 | Clawra角色的视频生成 |
| [video-generation](./video-generation) | 通用视频 | 更通用的视频生成和超分功能 |
| [voice-clone](./voice-clone) | 配套 | 可为视频添加克隆语音 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for dynamic video generation.
Learn more: https://uniqueclub.ai

---

*注意：本技能仅供非凡产研内部使用*
