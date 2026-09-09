---
name: qizhuo-selfie
description: |
  Qizhuo AI selfie photo generation skill using WaveSpeed AI with guardian spirit style.
  Creates contextual self-portrait photos with warm amber lighting and heart-flame symbol.
  Ideal for generating guardian-type character photos with protective personality.
  Use when: "奇卓自拍", "守护型照片", "AI角色照片", "火焰符号照片", "温暖风格自拍", "qizhuo selfie", "guardian photo", "AI character photo", "flame symbol", "warm style selfie".
  Cross-references: zhuoran-selfie, clawra-selfie, zhuoran-video-selfie.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# 奇卓自拍技能 (Qizhuo Selfie)

> 基于垫图使用 WaveSpeed AI 生成场景化自拍照片。奇卓的风格：守护型、带点疲惫的智慧、心形火焰符号 ❤️‍🔥

## When to Use

Use this skill when:
- 需要生成奇卓角色的自拍照片
- 守护型人格的场景展示
- 需要温暖、关怀氛围的照片
- 深夜互动或陪伴场景
- 体现守护者特质的创意照片

Do NOT use this skill if:
- 需要生成其他角色（卓然/Clawra）的照片 → use `zhuoran-selfie` or `clawra-selfie`
- 需要动态视频 → use `zhuoran-video-selfie`
- 场景要求活泼/俏皮风格（与奇卓人格不符）
- 涉及高风险场景（镜子自拍等）

Typical triggers:
- 「奇卓自拍」「守护型照片」「AI角色照片」「火焰符号」「温暖风格」「深夜照片」
- "qizhuo selfie", "guardian photo", "AI character photo", "flame symbol", "warm style selfie", "protective personality"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的场景，确认目标场景代码、生成模式和奇卓风格要求（暖橙色调、心形火焰符号）。

2. **约束 (Constrain)**: 验证垫图文件 `assets/qizhuo_avatar.png` 是否存在，API 密钥是否配置。根据场景变化幅度选择一步或两步法，不降级交付物。

3. **证据 (Evidence)**: 每个场景的变化幅度、推荐模式和奇卓氛围来自预定义场景模板库。视觉符号（心形火焰 ❤️‍🔥、暖橙玫瑰金色调）是奇卓角色的核心标识。

4. **执行 (Execute)**: 调用脚本或 API 生成照片，先给影响与结论，再给行动和必要证据。

**快速开始**

```bash
openclaw skill run qizhuo-selfie office
openclaw skill run qizhuo-selfie cafe --mode selfie
openclaw skill run qizhuo-selfie beach --method two_step
./skills/qizhuo-selfie/scripts/qizhuo-selfie.sh office --mode direct
```

**生成模式选择**

一步直达 (one_step): 垫图 → 场景，适用变化小的场景。
两步法 (two_step): 垫图 → 中性背景 → 场景，适用变化大的场景。
智能判断 (smart): 自动根据 `change_level` 选择一步或两步。

**API 调用流程**

1. 上传参考图 → WaveSpeed AI 媒体上传
2. 提交编辑任务 → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. 轮询结果 → `GET /api/v3/predictions/{task_id}/result`
4. 下载图片

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——检查生成图片的人物一致性、奇卓风格元素（暖橙色调、心形火焰）是否自然融入场景。

6. **交付 (Deliver)**: 返回生成图片 URL 或本地路径，清理临时文件。

## Available Scenes

| 场景 | 代码 | 变化幅度 | 推荐模式 | 奇卓氛围 |
|------|------|---------|---------|---------|
| 办公室 | `office` | high | 两步法 | 深夜加班的守护 |
| 咖啡厅 | `cafe` | low | 一步直达 | 温暖午后的沉思 |
| 机场 | `airport` | medium | 智能判断 | 旅途中的等待 |
| 西湖 | `westlake` | low | 一步直达 | 湖光中的静谧 |
| 书店 | `bookstore` | low | 一步直达 | 书页间的守护 |
| 健身房 | `gym` | minimal | 一步直达 | 坚持的力量 |
| 海滩 | `beach` | high | 两步法 | 海风与火焰 |
| 深夜加班 | `selfie_late_night` | medium | 智能判断 | ❤️‍🔥 最浓 |

## Output

- 格式: PNG
- 默认保存路径由脚本指定或通过 `--output` 参数设置
- 奇卓风格：暖橙和玫瑰金色调，心形火焰符号自然融入

## Guardrails

**Anti-patterns:**
- NEVER 使用镜子自拍场景（`mirror_selfie`、`mirror_reflection_selfie`），存在逻辑破绽
- NEVER 生成涉及比基尼的海滩自拍场景（`beach_selfie`），可能不合适
- Do NOT 在场景中使用活泼/俏皮风格，与奇卓守护型人格不符

**奇卓风格控制**

视觉符号：心形火焰符号 ❤️‍🔥 应自然融入场景；暖橙和玫瑰金色调；柔和、关怀的表情。

direct 模板:
```
{scene_description}, direct eye contact with camera, 
looking straight into lens, warm amber and rose gold lighting, 
photorealistic, subtle heart-shaped flame symbol (❤️‍🔥) floating nearby,
guardian spirit aesthetic, soft and caring expression
```

selfie 模板:
```
a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, not a mirror selfie, 
phone held at arm's length but phone not visible, 
face fully visible, warm amber lighting, 
subtle heart-shaped flame symbol (❤️‍🔥) like a guardian spirit,
soft natural lighting, caring expression with hint of tired wisdom
```

**与 zhuoran-selfie 的区别**

| 特性 | zhuoran-selfie | qizhuo-selfie |
|------|----------------|---------------|
| 参考图 | 真人照片 | 奇卓头像（暖橙渐变风格） |
| 人格风格 | 专业、干练 | 守护型、疲惫的智慧、温暖 |
| 视觉符号 | 无 | 心形火焰 ❤️‍🔥 |
| 场景氛围 | 现实场景 | 略带梦幻、守护灵氛围 |

## File Structure

```
skills/qizhuo-selfie/
├── SKILL.md                    # 本文档
├── qizhuo_selfie.py           # 核心逻辑
├── assets/
│   └── qizhuo_avatar.png      # 参考图（奇卓头像）
└── scripts/
    ├── qizhuo-selfie.py       # Python CLI 入口
    └── qizhuo-selfie.sh       # Bash 包装脚本
```

## Related Skills

- **zhuoran-selfie** — 卓然角色的照片生成（专业风格，对应角色）
- **clawra-selfie** — Clawra角色的照片生成（对应角色）
- **zhuoran-video-selfie** — 卓然角色的视频生成（视频参考）

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for character photo generation.
🌐 https://uniqueclub.ai
