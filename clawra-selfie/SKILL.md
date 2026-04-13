---
name: clawra-selfie
description: |
  Clawra AI selfie photo generation skill using WaveSpeed AI with reference image.
  Creates contextual self-portrait photos for office, cafe, gym, and street scenes.
  Ideal for generating character photos with consistent identity.

  Use when: AI照片生成, 自拍生成, 角色照片, 场景照片, 垫图生成, 
  AI photo generation, selfie generation, character photo, scene photo, 
  reference image generation

  Related: clawra-video-selfie, zhuoran-selfie, qizhuo-selfie

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Clawra 自拍照片生成器 (Clawra Selfie Photo Generator)

基于垫图使用 WaveSpeed AI 生成场景化自拍照片。支持自定义提示词和多种预设场景，适用于为 Clawra 生成个人照片内容。

## When to Use

**适用于以下场景：**
- 需要生成角色自拍照片
- 用户索要个人照片或头像
- 根据场景生成上下文匹配的照片
- 创意照片生成和角色展示
- 需要保持角色一致性（使用垫图）

**Do NOT use this skill if:**
- 需要生成动态视频（使用 clawra-video-selfie 替代）
- 场景涉及镜子自拍或反射场景（存在逻辑破绽）
- 需要全身镜自拍照（使用直接肖像模式代替）
- 涉及不合适的服装或场景

**触发关键词 / Trigger Phrases:**
- AI照片生成 / AI photo generation
- 自拍生成 / selfie generation  
- 角色照片 / character photo
- 场景照片 / scene photo
- 垫图生成 / reference image generation
- 办公室照片 / office photo
- 咖啡厅自拍 / cafe selfie
- 来张照片 / send a photo

## Workflow

### 方式1：使用自定义提示词（推荐）

```bash
python3 skills/clawra-selfie/scripts/clawra_selfie.py --prompt "自定义提示词" [--output 路径]
```

### 方式2：使用预设场景

```bash
python3 skills/clawra-selfie/scripts/clawra_selfie.py <场景> [--output 路径]
```

### Python API 调用

```python
from skills.clawra-selfie.scripts.clawra_selfie import generate_with_prompt, generate_image

# 使用自定义提示词（推荐）
image_url = generate_with_prompt(
    prompt="young woman in bathroom, towel wrapped around body, steamy atmosphere, soft lighting"
)

# 使用预设场景
image_url = generate_image(
    scene='office'
)
```

### 完整工作流步骤

1. **准备垫图** - 确保参考图已上传到技能目录
2. **选择生成方式** - 自定义提示词或预设场景
3. **执行生成** - 调用脚本或 API
4. **获取结果** - 下载生成的照片
5. **验证质量** - 检查人物一致性和场景匹配度

## Available Scenes

| 场景 | 名称 | 描述 |
|------|------|------|
| `office` | 办公室 | 旧金山初创公司办公室 |
| `cafe` | 咖啡厅 | 舒适咖啡厅环境 |
| `gym` | 健身房 | 运动后场景 |
| `home` | 家里 | 温馨公寓环境 |
| `street` | 旧金山街头 | 城市街头 |
| `selfie` | 通用自拍 | 通用自拍场景 |

## Guardrails

### 禁用场景

以下场景已被禁用（高风险）：
- `mirror_selfie` - 全身镜自拍，存在逻辑破绽
- `mirror_reflection_selfie` - 镜子反射自拍，破绽明显
- `beach_selfie` - 涉及比基尼，可能不合适

### 安全控制原则
- **人物一致性**：使用垫图确保角色外观一致
- **场景真实性**：避免不可能的场景组合
- **隐私保护**：不生成敏感或不适当内容
- **提示词审查**：自定义提示词需符合使用规范

### 提示词建议

**好的提示词要素**：
- 场景描述（bathroom, bedroom, office...）
- 服装状态（towel wrapped, oversized t-shirt...）
- 表情/情绪（seductive, emotional, relaxed...）
- 光线氛围（soft lighting, steamy atmosphere...）
- 动作细节（towel slipping, looking at mirror...）

**示例模板**：
```
young woman [场景], [服装/状态], [表情], [光线], [氛围]
```

## Environment Requirements

- `WAVESPEED_KEY`: WaveSpeed API 密钥
- Python 3.8+
- 依赖: requests

## Output

- 格式: PNG
- 自定义提示词默认保存: `/tmp/clawra_custom_selfie.png`

## Related Skills

| 技能 | 关系 | 说明 |
|------|------|------|
| [clawra-video-selfie](./clawra-video-selfie) | 视频版 | 同一角色的动态视频生成 |
| [zhuoran-selfie](./zhuoran-selfie) | 相似功能 | 卓然角色的照片生成 |
| [qizhuo-selfie](./qizhuo-selfie) | 相似功能 | 奇卓角色的照片生成（守护型风格） |
| [zhuoran-video-selfie](./zhuoran-video-selfie) | 视频版 | 卓然角色的视频生成 |
| [voice-clone](./voice-clone) | 配套 | 可配合声音克隆增加沉浸感 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for digital content generation.
Learn more: https://uniqueclub.ai
