---
name: zhuoran-selfie
description: |
  Zhuoran AI selfie photo generation skill using WaveSpeed AI with reference image.
  Creates contextual self-portrait photos for office, cafe, gym, airport, and scenic locations.
  Supports one-step, two-step, and smart generation modes for optimal quality.

  Use when: 卓然自拍, AI照片生成, 角色照片, 场景自拍, 垫图生成, 
  zhuoran selfie, AI photo generation, character photo, scene selfie, 
  reference image, professional portrait

  Related: zhuoran-video-selfie, qizhuo-selfie, clawra-selfie

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# 卓然自拍技能 (Zhuoran Selfie)

基于垫图使用 WaveSpeed AI 生成场景化自拍照片，支持一步直达、两步法和智能判断三种生成模式。

## When to Use

**适用于以下场景：**
- 需要生成卓然角色的自拍照片
- 专业、干练风格的场景展示
- 办公室、咖啡厅、机场等商务场景
- 穿搭展示和日常分享
- 深夜互动或工作场景

**Do NOT use this skill if:**
- 需要生成守护型风格的照片（使用 qizhuo-selfie）
- 需要动态视频（使用 zhuoran-video-selfie）
- 场景涉及镜子自拍或反射场景
- 需要全身镜自拍照

**触发关键词 / Trigger Phrases:**
- 卓然自拍 / zhuoran selfie
- AI照片生成 / AI photo generation
- 角色照片 / character photo
- 场景自拍 / scene selfie
- 垫图生成 / reference image
- 专业肖像 / professional portrait
- 办公室照片 / office photo
- 穿搭展示 / outfit showcase

## Workflow

### 快速开始

```bash
# 智能模式生成办公室自拍
openclaw skill run zhuoran-selfie office

# 指定自拍模式
openclaw skill run zhuoran-selfie cafe --mode selfie

# 使用两步法（高质量）
openclaw skill run zhuoran-selfie beach --method two_step

# 直接调用脚本
./skills/zhuoran-selfie/scripts/zhuoran-selfie.sh office --mode direct
```

### 命令行参数

```bash
./skills/zhuoran-selfie/scripts/zhuoran-selfie.sh <scene> \
  --mode <direct|selfie|portrait> \
  --method <one_step|two_step|smart> \
  --target <@user|#channel> \
  --caption "配文" \
  --output /path/to/output.png
```

### 生成模式详解

#### 一步直达 (one_step)
**流程**: 垫图 → 场景

**适用**: 变化小的场景（gym, cafe, westlake, bookstore）
- ✅ 快速、简单
- ⚠️ 人物一致性可能不稳定

#### 两步法 (two_step)
**流程**: 垫图 → 中性背景 → 场景

**适用**: 变化大的场景（office, beach）
- ✅ 人物一致性高
- ⚠️ 较慢、两次API调用

#### 智能判断 (smart)
**流程**: 自动根据 `change_level` 选择一步或两步

**逻辑**:
- `minimal` / `low` → 一步直达
- `medium` / `high` → 两步法

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交编辑任务** → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载图片**

### Python API

```python
from skills.zhuoran_selfie.zhuoran_selfie import generate_smart, generate_one_step, generate_two_step

# 智能生成
image_url = generate_smart("office", mode="direct")

# 一步直达（快速）
image_url = generate_one_step("cafe", mode="selfie")

# 两步法（高质量）
image_url = generate_two_step("beach", mode="portrait")
```

## Available Scenes

| 场景 | 代码 | 变化幅度 | 推荐模式 |
|------|------|---------|---------|
| 办公室 | `office` | high | 两步法 |
| 咖啡厅 | `cafe` | low | 一步直达 |
| 机场 | `airport` | medium | 智能判断 |
| 西湖 | `westlake` | low | 一步直达 |
| 书店 | `bookstore` | low | 一步直达 |
| 健身房 | `gym` | minimal | 一步直达 |
| 海滩 | `beach` | high | 两步法 |
| 深夜加班 | `selfie_late_night` | medium | 智能判断 |

## Guardrails

### 禁用场景

以下场景已被禁用（高风险）：
- `mirror_selfie` - 全身镜自拍，存在逻辑破绽
- `mirror_reflection_selfie` - 镜子反射自拍，破绽明显
- `beach_selfie` - 涉及比基尼，可能不合适

### Prompt 模板

**direct** (普通肖像):
```
{scene_description}, direct eye contact with camera, 
looking straight into lens, natural lighting, 
photorealistic, 8k quality
```

**selfie** (自拍模式):
```
a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, 
looking straight into the lens, eyes centered and clearly visible, 
not a mirror selfie, 
phone held at arm's length but phone not visible in frame, 
face fully visible, natural lighting
```

**portrait** (专业肖像):
```
professional portrait of {scene_description}, 
soft natural lighting, half-body shot, 
clean background, photorealistic
```

### 与 v1.0 (clawra) 的区别

| 特性 | v1.0 (clawra) | v2.0 (zhuoran) |
|------|--------------|----------------|
| 参考图 | clawra.png (卡通) | zhuoran_portrait_base.png (真人) |
| API 平台 | fal.ai | WaveSpeed AI |
| 生成模式 | mirror / direct | 一步 / 两步 / 智能 |
| 场景管理 | 无 | 场景模板库 |
| 安全控制 | 无 | 禁用高风险场景 |
| 触发方式 | Bash/TS | Python CLI + Bash 包装 |

## Environment Requirements

- `WAVESPEED_KEY`: WaveSpeed API 密钥
- Python 3.8+
- 依赖: requests

## File Structure

```
skills/zhuoran-selfie/
├── SKILL.md                    # 本文档
├── zhuoran_selfie.py           # 核心逻辑
└── scripts/
    ├── zhuoran-selfie.py       # Python CLI 入口
    └── zhuoran-selfie.sh       # Bash 包装脚本（OpenClaw 入口）
```

## Related Skills

| 技能 | 关系 | 说明 |
|------|------|------|
| [zhuoran-video-selfie](./zhuoran-video-selfie) | 视频版 | 同一角色的动态视频生成 |
| [qizhuo-selfie](./qizhuo-selfie) | 对应角色 | 奇卓角色的照片生成（守护型风格） |
| [clawra-selfie](./clawra-selfie) | 参考 | Clawra角色的照片生成 |
| [voice-clone](./voice-clone) | 配套 | 可配合声音克隆增加沉浸感 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for character photo generation.
Learn more: https://uniqueclub.ai

---

*注意：本技能仅供非凡产研内部使用*
