---
name: clawra-selfie
description: |
  Clawra AI selfie photo generation skill using WaveSpeed AI with reference image.
  Creates contextual self-portrait photos for office, cafe, gym, and street scenes.
  Ideal for generating character photos with consistent identity.
  Use when: "AI照片生成", "自拍生成", "角色照片", "场景照片", "垫图生成", "clawra selfie", "AI photo generation", "selfie generation", "character photo", "reference image".
  Cross-references: clawra-video-selfie, zhuoran-selfie, qizhuo-selfie.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Clawra 自拍照片生成器 (Clawra Selfie Photo Generator)

> 基于垫图使用 WaveSpeed AI 生成场景化自拍照片。支持自定义提示词和多种预设场景，适用于为 Clawra 生成个人照片内容。

## When to Use

Use this skill when:
- 需要生成角色自拍照片
- 用户索要个人照片或头像
- 根据场景生成上下文匹配的照片
- 创意照片生成和角色展示
- 需要保持角色一致性（使用垫图）

Do NOT use this skill if:
- 需要生成动态视频 → use `clawra-video-selfie`
- 场景涉及镜子自拍或反射场景（存在逻辑破绽）
- 需要全身镜自拍照（使用直接肖像模式代替）
- 涉及不合适的服装或场景

Typical triggers:
- 「AI照片生成」「自拍生成」「角色照片」「场景照片」「垫图生成」「来张照片」
- "clawra selfie", "AI photo generation", "selfie generation", "character photo", "scene photo", "reference image"

## Workflow

1. **探查 (Probe)**: 完整读取需求，确认生成方式（自定义提示词或预设场景）、目标场景代码和输出要求。检查垫图文件是否存在。

2. **约束 (Constrain)**: 验证输入完整性，设定边界：仅使用预定义安全场景，自定义提示词需符合使用规范。不降级交付物。

3. **证据 (Evidence)**: 每个预设场景的描述来自场景模板库。提示词要素（场景、服装、表情、光线、氛围）是生成质量的关键证据。

4. **执行 (Execute)**: 调用脚本或 API 生成照片，先给影响与结论，再给行动和必要证据。

**方式1：使用自定义提示词（推荐）**

```bash
python3 skills/clawra-selfie/scripts/clawra_selfie.py --prompt "自定义提示词" [--output 路径]
```

**方式2：使用预设场景**

```bash
python3 skills/clawra-selfie/scripts/clawra_selfie.py <场景> [--output 路径]
```

**Python API 调用**

```python
from skills.clawra-selfie.scripts.clawra_selfie import generate_with_prompt, generate_image

# 使用自定义提示词（推荐）
image_url = generate_with_prompt(
    prompt="young woman in bathroom, towel wrapped around body, steamy atmosphere, soft lighting"
)

# 使用预设场景
image_url = generate_image(scene='office')
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——检查人物一致性、场景匹配度和提示词审查结果。

6. **交付 (Deliver)**: 返回生成图片 URL 或本地路径，清理临时文件。

## Available Scenes

| 场景 | 名称 | 描述 |
|------|------|------|
| `office` | 办公室 | 旧金山初创公司办公室 |
| `cafe` | 咖啡厅 | 舒适咖啡厅环境 |
| `gym` | 健身房 | 运动后场景 |
| `home` | 家里 | 温馨公寓环境 |
| `street` | 旧金山街头 | 城市街头 |
| `selfie` | 通用自拍 | 通用自拍场景 |

## Output

- 格式: PNG
- 自定义提示词默认保存: `/tmp/clawra_custom_selfie.png`
- 预设场景保存路径由脚本指定

## Guardrails

**Anti-patterns:**
- NEVER 使用镜子自拍场景（`mirror_selfie`、`mirror_reflection_selfie`），存在逻辑破绽
- NEVER 生成涉及比基尼的海滩自拍场景（`beach_selfie`），可能不合适
- Do NOT 生成不可能的场景组合
- Do NOT 生成敏感或不适当内容

**安全控制原则**
- 人物一致性：使用垫图确保角色外观一致
- 场景真实性：避免不可能的场景组合
- 隐私保护：不生成敏感或不适当内容
- 提示词审查：自定义提示词需符合使用规范

**提示词建议**

好的提示词要素：场景描述、服装状态、表情/情绪、光线氛围、动作细节。

示例模板：
```
young woman [场景], [服装/状态], [表情], [光线], [氛围]
```

**Environment Requirements**

- `WAVESPEED_KEY`: WaveSpeed API 密钥
- Python 3.8+
- 依赖: requests

## Related Skills

- **clawra-video-selfie** — 同一角色的动态视频生成（视频版）
- **zhuoran-selfie** — 卓然角色的照片生成（相似功能）
- **qizhuo-selfie** — 奇卓角色的照片生成（守护型风格，相似功能）

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for digital content generation.
🌐 https://uniqueclub.ai
