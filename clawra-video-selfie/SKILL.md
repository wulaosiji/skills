---
name: clawra-video-selfie
description: |
  Clawra AI selfie video generation skill using WaveSpeed AI Seedance model.
  Creates contextual dynamic selfie videos with natural micro-movements.
  Ideal for bringing character photos to life with subtle breathing and motion.

  Use when: AI视频生成, 自拍视频, 动态自拍, 视频自拍, 角色视频, 
  AI video generation, selfie video, dynamic selfie, video selfie, 
  character video, motion generation

  Related: clawra-selfie, zhuoran-video-selfie, video-generation

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Clawra 自拍视频生成器 (Clawra Selfie Video Generator)

基于垫图使用 WaveSpeed AI 生成场景化动态自拍视频，支持自然微动作（呼吸、眨眼等），呈现"活人感"。

## When to Use

**适用于以下场景：**
- 需要生成角色的动态自拍视频
- 用户索要视频或动态展示
- 为静态照片添加生命力
- 展示角色在场景中的自然状态
- 需要微动作增强真实感

**Do NOT use this skill if:**
- 只需要静态照片（使用 clawra-selfie 更高效）
- 需要大幅度动作场景（如跳舞、走路）
- 视频时长需要超过10秒
- 需要多人同框视频
- 需要复杂的镜头运动

**触发关键词 / Trigger Phrases:**
- AI视频生成 / AI video generation
- 自拍视频 / selfie video
- 动态自拍 / dynamic selfie
- 视频自拍 / video selfie
- 角色视频 / character video
- 生成视频 / generate video
- 录段视频 / record a video
- 动一下看看 / show some movement

## Workflow

### 命令行使用

```bash
python3 skills/clawra-video-selfie/scripts/clawra_video_selfie.py <场景> [--duration 秒数] [--output 路径] [--ref 垫图路径]
```

### Python API 调用

```python
from skills.clawra-video-selfie.scripts.clawra_video_selfie import generate_video

# 使用默认垫图
video_path = generate_video(
    scene='office',      # 场景
    duration=5,          # 时长(秒)
    output_path=None     # 输出路径(可选)
)

# 使用自定义垫图（如生成的照片）
video_path = generate_video(
    scene='office',
    duration=5,
    output_path=None,
    ref_image='/path/to/photo.png'  # 自定义垫图路径
)
```

### 推荐工作流：照片+视频组合

1. **生成基础照片** - 先用 `clawra-selfie` 生成场景照片
2. **照片转视频** - 使用该照片作为垫图生成视频
3. **场景一致性** - 确保视频和照片场景更连贯

```bash
# 完整流程示例
python3 skills/clawra-selfie/scripts/clawra_selfie.py office --output /tmp/photo.png
python3 skills/clawra-video-selfie/scripts/clawra_video_selfie.py office --ref /tmp/photo.png
```

## Available Scenes

| 场景 | 名称 | 描述 |
|------|------|------|
| `office` | 办公室 | 旧金山初创公司办公室 |
| `cafe` | 咖啡厅 | 舒适咖啡厅环境 |
| `gym` | 健身房 | 运动后场景 |
| `home` | 家里 | 温馨公寓环境 |
| `street` | 街头 | 旧金山街头 |

## Guardrails

### 禁用场景

以下场景已被禁用（高风险）：
- `mirror_selfie` - 镜子反射，逻辑破绽明显
- `dancing` - 大幅度动作，肢体一致性难保证
- `walking` - 移动场景，背景与人物同步难
- `group` - 多人入镜，复杂度太高
- `swimming` - 水下场景，物理逻辑复杂

### 风险控制原则
- **时长限制**: 最长8秒，避免暴露不自然动作
- **场景限制**: 仅使用预定义的安全场景
- **动作限制**: 微动作优先（呼吸、眨眼），避免大幅度运动
- **频率限制**: 视频比照片使用频率更低
- **垫图质量**: 确保垫图清晰，面部特征明确

### "活人感"提示词系统

**核心原则：**
1. **自然微动** - 呼吸、眨眼、头发飘动
2. **避免完美** - 保留皮肤纹理、自然瑕疵
3. **场景真实** - 自拍角度、环境互动

**基础模板：**
```
{scene_description}, subtle breathing motion and natural posture shift, 
gentle hair swaying in {environment} breeze, soft smile with micro-expressions, 
occasional natural blink and eye movement, authentic selfie perspective
```

## Environment Requirements

- `WAVESPEED_KEY`: WaveSpeed API 密钥
- Python 3.8+
- 依赖: requests

## Output

- 格式: MP4 (H.264)
- 分辨率: 480p
- 比例: 竖屏
- 时长: 5 或 8 秒
- 默认保存: `/tmp/clawra_{场景}_video.mp4`

## Related Skills

| 技能 | 关系 | 说明 |
|------|------|------|
| [clawra-selfie](./clawra-selfie) | 照片版 | 同一角色的静态照片生成 |
| [zhuoran-video-selfie](./zhuoran-video-selfie) | 相似功能 | 卓然角色的视频生成 |
| [video-generation](./video-generation) | 通用视频 | 更通用的视频生成和超分功能 |
| [zhuoran-selfie](./zhuoran-selfie) | 参考 | 卓然角色照片版 |
| [qizhuo-selfie](./qizhuo-selfie) | 参考 | 奇卓角色照片版 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for dynamic video generation.
Learn more: https://uniqueclub.ai
