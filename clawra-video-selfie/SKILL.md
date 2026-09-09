---
name: clawra-video-selfie
description: |
  Clawra AI selfie video generation skill using WaveSpeed AI Seedance model.
  Creates contextual dynamic selfie videos with natural micro-movements.
  Ideal for bringing character photos to life with subtle breathing and motion.
  Use when: "AI视频生成", "自拍视频", "动态自拍", "视频自拍", "角色视频", "clawra video", "AI video generation", "selfie video", "dynamic selfie", "character video".
  Cross-references: clawra-selfie, zhuoran-video-selfie, video-generation.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Clawra 自拍视频生成器 (Clawra Selfie Video Generator)

> 基于垫图使用 WaveSpeed AI 生成场景化动态自拍视频，支持自然微动作（呼吸、眨眼等），呈现"活人感"。

## When to Use

Use this skill when:
- 需要生成角色的动态自拍视频
- 用户索要视频或动态展示
- 为静态照片添加生命力
- 展示角色在场景中的自然状态
- 需要微动作增强真实感

Do NOT use this skill if:
- 只需要静态照片 → use `clawra-selfie` 更高效
- 需要大幅度动作场景（如跳舞、走路）
- 视频时长需要超过10秒
- 需要多人同框视频
- 需要复杂的镜头运动

Typical triggers:
- 「AI视频生成」「自拍视频」「动态自拍」「视频自拍」「角色视频」「录段视频」
- "clawra video", "AI video generation", "selfie video", "dynamic selfie", "video selfie", "character video"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的场景，确认目标场景代码、视频时长和垫图路径。检查垫图文件是否存在。

2. **约束 (Constrain)**: 验证输入完整性，设定边界：最长8秒、仅使用预定义安全场景、微动作优先。推荐先使用 `clawra-selfie` 生成基础照片作为垫图，确保场景一致性。

3. **证据 (Evidence)**: 每个场景的描述来自预定义场景模板。"活人感"提示词系统（自然微动、避免完美、场景真实）是生成质量的核心证据。

4. **执行 (Execute)**: 调用脚本或 API 生成视频，先给影响与结论，再给行动和必要证据。

**命令行使用**

```bash
python3 skills/clawra-video-selfie/scripts/clawra_video_selfie.py <场景> [--duration 秒数] [--output 路径] [--ref 垫图路径]
```

**Python API 调用**

```python
from skills.clawra-video-selfie.scripts.clawra_video_selfie import generate_video

# 使用默认垫图
video_path = generate_video(scene='office', duration=5, output_path=None)

# 使用自定义垫图（如生成的照片）
video_path = generate_video(scene='office', duration=5, output_path=None, ref_image='/path/to/photo.png')
```

**推荐工作流：照片+视频组合**

1. 生成基础照片 - 先用 `clawra-selfie` 生成场景照片
2. 照片转视频 - 使用该照片作为垫图生成视频
3. 场景一致性 - 确保视频和照片场景更连贯

```bash
python3 skills/clawra-selfie/scripts/clawra_selfie.py office --output /tmp/photo.png
python3 skills/clawra-video-selfie/scripts/clawra_video_selfie.py office --ref /tmp/photo.png
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——使用 FFmpeg 检查视频时长、分辨率和编码格式，确认微动作自然。

6. **交付 (Deliver)**: 返回视频文件路径，清理临时文件。

## Available Scenes

| 场景 | 名称 | 描述 |
|------|------|------|
| `office` | 办公室 | 旧金山初创公司办公室 |
| `cafe` | 咖啡厅 | 舒适咖啡厅环境 |
| `gym` | 健身房 | 运动后场景 |
| `home` | 家里 | 温馨公寓环境 |
| `street` | 街头 | 旧金山街头 |

## Output

- 格式: MP4 (H.264)
- 分辨率: 480p
- 比例: 竖屏
- 时长: 5 或 8 秒
- 默认保存: `/tmp/clawra_{场景}_video.mp4`

## Guardrails

**Anti-patterns:**
- NEVER 使用镜子自拍场景（`mirror_selfie`），逻辑破绽明显
- NEVER 生成大幅度动作场景（`dancing`、`walking`），肢体一致性难保证
- NEVER 生成多人入镜视频（`group`），复杂度太高
- NEVER 生成水下场景（`swimming`），物理逻辑复杂
- Do NOT 视频时长超过8秒，避免暴露不自然动作

**风险控制原则**
- 时长限制: 最长8秒，避免暴露不自然动作
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
occasional natural blink and eye movement, authentic selfie perspective
```

**Environment Requirements**

- `WAVESPEED_KEY`: WaveSpeed API 密钥
- Python 3.8+
- 依赖: requests

## Related Skills

- **clawra-selfie** — 同一角色的静态照片生成（照片版）
- **zhuoran-video-selfie** — 卓然角色的视频生成（相似功能）
- **video-generation** — 更通用的视频生成和超分功能

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for dynamic video generation.
🌐 https://uniqueclub.ai
