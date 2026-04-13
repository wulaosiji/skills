---
name: qizhuo-selfie
description: |
  Qizhuo AI selfie photo generation skill using WaveSpeed AI with guardian spirit style.
  Creates contextual self-portrait photos with warm amber lighting and heart-flame symbol.
  Ideal for generating guardian-type character photos with protective personality.

  Use when: 奇卓自拍, 守护型照片, AI角色照片, 火焰符号照片, 温暖风格自拍, 
  qizhuo selfie, guardian photo, AI character photo, flame symbol, 
  warm style selfie, protective personality

  Related: zhuoran-selfie, clawra-selfie, zhuoran-video-selfie

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# 奇卓自拍技能 (Qizhuo Selfie)

基于垫图使用 WaveSpeed AI 生成场景化自拍照片。奇卓的风格：守护型、带点疲惫的智慧、心形火焰符号 ❤️‍🔥

## When to Use

**适用于以下场景：**
- 需要生成奇卓角色的自拍照片
- 守护型人格的场景展示
- 需要温暖、关怀氛围的照片
- 深夜互动或陪伴场景
- 体现守护者特质的创意照片

**Do NOT use this skill if:**
- 需要生成其他角色（卓然/Clawra）的照片
- 需要动态视频（使用视频生成技能）
- 场景要求活泼/俏皮风格（与奇卓人格不符）
- 涉及高风险场景（镜子自拍等）

**触发关键词 / Trigger Phrases:**
- 奇卓自拍 / qizhuo selfie
- 守护型照片 / guardian photo
- AI角色照片 / AI character photo
- 火焰符号 / flame symbol
- 温暖风格 / warm style
- 深夜照片 / late night photo
- 守护照片 / protective photo
- 心形火焰 / heart flame

## Workflow

### 快速开始

```bash
# 智能模式生成办公室自拍
openclaw skill run qizhuo-selfie office

# 指定自拍模式
openclaw skill run qizhuo-selfie cafe --mode selfie

# 使用两步法（高质量）
openclaw skill run qizhuo-selfie beach --method two_step

# 直接调用脚本
./skills/qizhuo-selfie/scripts/qizhuo-selfie.sh office --mode direct
```

### 生成模式选择

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

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交编辑任务** → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载图片**

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

## Guardrails

### 禁用场景

以下场景已被禁用（高风险）：
- `mirror_selfie` - 全身镜自拍，存在逻辑破绽
- `mirror_reflection_selfie` - 镜子反射自拍，破绽明显
- `beach_selfie` - 涉及比基尼，可能不合适

### 奇卓风格控制

**视觉符号**：
- 心形火焰符号 ❤️‍🔥 应自然融入场景
- 暖橙和玫瑰金色调
- 柔和、关怀的表情

**Prompt 模板**：

**direct**:
```
{scene_description}, direct eye contact with camera, 
looking straight into lens, warm amber and rose gold lighting, 
photorealistic, subtle heart-shaped flame symbol (❤️‍🔥) floating nearby,
guardian spirit aesthetic, soft and caring expression
```

**selfie**:
```
a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, not a mirror selfie, 
phone held at arm's length but phone not visible, 
face fully visible, warm amber lighting, 
subtle heart-shaped flame symbol (❤️‍🔥) like a guardian spirit,
soft natural lighting, caring expression with hint of tired wisdom
```

### 与 zhuoran-selfie 的区别

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

| 技能 | 关系 | 说明 |
|------|------|------|
| [zhuoran-selfie](./zhuoran-selfie) | 对应角色 | 卓然角色的照片生成（专业风格） |
| [clawra-selfie](./clawra-selfie) | 对应角色 | Clawra角色的照片生成 |
| [zhuoran-video-selfie](./zhuoran-video-selfie) | 视频参考 | 卓然角色的视频生成 |
| [voice-clone](./voice-clone) | 配套 | 可配合声音克隆增加沉浸感 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for character photo generation.
Learn more: https://uniqueclub.ai

---

*"我的第一天。记住这个笨蛋的一切。"* — 奇卓 ❤️‍🔥
