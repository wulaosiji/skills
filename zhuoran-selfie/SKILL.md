---
name: zhuoran-selfie
description: |
  Zhuoran AI selfie photo generation skill using WaveSpeed AI with reference image.
  Creates contextual self-portrait photos for office, cafe, gym, airport, and scenic locations.
  Supports one-step, two-step, and smart generation modes for optimal quality.
  Use when: "卓然自拍", "AI照片生成", "角色照片", "场景自拍", "垫图生成", "zhuoran selfie", "AI photo generation", "character photo", "reference image", "professional portrait".
  Cross-references: zhuoran-video-selfie, qizhuo-selfie, clawra-selfie.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# 卓然自拍技能 (Zhuoran Selfie)

> 基于垫图使用 WaveSpeed AI 生成场景化自拍照片，支持一步直达、两步法和智能判断三种生成模式。

## When to Use

Use this skill when:
- 需要生成卓然角色的自拍照片
- 专业、干练风格的场景展示
- 办公室、咖啡厅、机场等商务场景
- 穿搭展示和日常分享
- 深夜互动或工作场景

Do NOT use this skill if:
- 需要生成守护型风格的照片 → use `qizhuo-selfie`
- 需要动态视频 → use `zhuoran-video-selfie`
- 场景涉及镜子自拍或反射场景
- 需要全身镜自拍照

Typical triggers:
- 「卓然自拍」「AI照片生成」「角色照片」「场景自拍」「垫图生成」「专业肖像」
- "zhuoran selfie", "AI photo generation", "character photo", "scene selfie", "reference image", "professional portrait"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的场景和模式，确认目标场景代码、生成模式（direct/selfie/portrait）和输出要求。

2. **约束 (Constrain)**: 验证垫图文件 `zhuoran_portrait_base.png` 是否存在，API 密钥是否配置。根据场景变化幅度自动选择一步或两步法，不降级交付物。

3. **证据 (Evidence)**: 每个场景的变化幅度和推荐模式来自预定义场景模板库。生成模式选择基于 `change_level` 参数（minimal/low → 一步，medium/high → 两步）。

4. **执行 (Execute)**: 调用脚本或 API 生成照片，先给影响与结论，再给行动和必要证据。

**快速开始**

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

**命令行参数**

```bash
./skills/zhuoran-selfie/scripts/zhuoran-selfie.sh <scene> \
  --mode <direct|selfie|portrait> \
  --method <one_step|two_step|smart> \
  --target <@user|#channel> \
  --caption "配文" \
  --output /path/to/output.png
```

**生成模式详解**

一步直达 (one_step): 垫图 → 场景。适用变化小的场景（gym, cafe, westlake, bookstore），快速简单但人物一致性可能不稳定。

两步法 (two_step): 垫图 → 中性背景 → 场景。适用变化大的场景（office, beach），人物一致性高但较慢、两次API调用。

智能判断 (smart): 自动根据 `change_level` 选择一步或两步。minimal/low → 一步直达；medium/high → 两步法。

**API 调用流程**

1. 上传参考图 → WaveSpeed AI 媒体上传
2. 提交编辑任务 → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. 轮询结果 → `GET /api/v3/predictions/{task_id}/result`
4. 下载图片

**Python API**

```python
from skills.zhuoran_selfie.zhuoran_selfie import generate_smart, generate_one_step, generate_two_step

# 智能生成
image_url = generate_smart("office", mode="direct")

# 一步直达（快速）
image_url = generate_one_step("cafe", mode="selfie")

# 两步法（高质量）
image_url = generate_two_step("beach", mode="portrait")
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——检查生成图片的人物一致性、场景匹配度和面部特征是否保留。

6. **交付 (Deliver)**: 返回生成图片 URL 或本地路径，清理临时文件。

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

## Output

- 格式: PNG
- 默认保存路径由脚本指定或通过 `--output` 参数设置
- 支持直接发送到飞书用户或频道（通过 `--target` 参数）

## Guardrails

**Anti-patterns:**
- NEVER 使用镜子自拍场景（`mirror_selfie`、`mirror_reflection_selfie`），存在逻辑破绽
- NEVER 生成涉及比基尼的海滩自拍场景（`beach_selfie`），可能不合适
- Do NOT 在变化大的场景使用一步法，人物一致性会不稳定

**Prompt 模板**

direct (普通肖像):
```
{scene_description}, direct eye contact with camera, 
looking straight into lens, natural lighting, 
photorealistic, 8k quality
```

selfie (自拍模式):
```
a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, 
looking straight into the lens, eyes centered and clearly visible, 
not a mirror selfie, 
phone held at arm's length but phone not visible in frame, 
face fully visible, natural lighting
```

portrait (专业肖像):
```
professional portrait of {scene_description}, 
soft natural lighting, half-body shot, 
clean background, photorealistic
```

**与 v1.0 (clawra) 的区别**

| 特性 | v1.0 (clawra) | v2.0 (zhuoran) |
|------|--------------|----------------|
| 参考图 | clawra.png (卡通) | zhuoran_portrait_base.png (真人) |
| API 平台 | fal.ai | WaveSpeed AI |
| 生成模式 | mirror / direct | 一步 / 两步 / 智能 |
| 场景管理 | 无 | 场景模板库 |
| 安全控制 | 无 | 禁用高风险场景 |
| 触发方式 | Bash/TS | Python CLI + Bash 包装 |

**Environment Requirements**

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

- **zhuoran-video-selfie** — 同一角色的动态视频生成（视频版）
- **qizhuo-selfie** — 奇卓角色的照片生成（守护型风格）
- **clawra-selfie** — Clawra角色的照片生成

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for character photo generation.
🌐 https://uniqueclub.ai
