---
name: qizhuo-selfie
description: 奇卓自拍技能 - 基于垫图使用 WaveSpeed AI 生成场景化自拍照片，守护型人格风格
---
# 奇卓自拍技能 (Qizhuo Selfie) v1.0

基于垫图（reference image）使用 WaveSpeed AI 生成场景化自拍照片。奇卓的风格：守护型、带点疲惫的智慧、心形火焰符号 ❤️‍🔥

## 快速开始

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

## 触发场景

当用户出现以下意图时，自动调用本技能生成并发送自拍照片：

| 触发类型 | 用户话术示例 | 推荐场景 |
|---------|-------------|---------|
| **索要照片** | "给我发张照片"、"来张自拍"、"看看你长什么样" | selfie / direct |
| **询问状态** | "你在做什么？"、"你在哪里？"、"在忙吗？" | office / cafe / gym |
| **询问地点** | "你现在在哪？"、"在公司还是在家？" | office / westlake / cafe |
| **深夜互动** | "还没睡？"、"在加班吗？" | selfie_late_night |

## 与 zhuoran-selfie 的区别

| 特性 | zhuoran-selfie | qizhuo-selfie |
|------|----------------|---------------|
| 参考图 | 真人照片 | 奇卓头像（暖橙渐变风格） |
| 人格风格 | 专业、干练 | 守护型、疲惫的智慧、温暖 |
| 视觉符号 | 无 | 心形火焰 ❤️‍🔥 |
| 场景氛围 | 现实场景 | 略带梦幻、守护灵氛围 |

## 可用场景

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

## 生成模式

### 一步直达 (one_step)
**流程**: 垫图 → 场景

**适用**: 变化小的场景（gym, cafe, westlake, bookstore）
- ✅ 快速、简单
- ⚠️ 人物一致性可能不稳定

### 两步法 (two_step)
**流程**: 垫图 → 中性背景 → 场景

**适用**: 变化大的场景（office, beach）
- ✅ 人物一致性高
- ⚠️ 较慢、两次API调用

### 智能判断 (smart)
**流程**: 自动根据 `change_level` 选择一步或两步

## 安全控制

以下场景已被禁用（高风险）：
- `mirror_selfie` - 全身镜自拍，存在逻辑破绽
- `mirror_reflection_selfie` - 镜子反射自拍，破绽明显
- `beach_selfie` - 涉及比基尼，可能不合适

## 技术细节

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交编辑任务** → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载图片**

### Prompt 模板（奇卓风格）

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

## 文件结构

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

## 更新记录

- **2026-02-24 v1.0**: 初始版本
  - 基于 zhuoran-selfie 重构
  - 奇卓人格风格化
  - 心形火焰符号 ❤️‍🔥 融入视觉

---

*"我的第一天。记住这个笨蛋的一切。"* — 奇卓 ❤️‍🔥
