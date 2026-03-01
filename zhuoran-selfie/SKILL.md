---
name: zhuoran-selfie
description: 卓然自拍技能 - 基于垫图使用 WaveSpeed AI 生成场景化自拍照片
---
# 卓然自拍技能 (Zhuoran Selfie) v2.0

基于垫图（reference image）使用 WaveSpeed AI 生成场景化自拍照片，支持多种场景和生成模式。

## 快速开始

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

## 触发场景

当用户出现以下意图时，自动调用本技能生成并发送自拍照片：

| 触发类型 | 用户话术示例 | 推荐场景 |
|---------|-------------|---------|
| **索要照片** | "给我发张照片"、"来张自拍"、"看看你长什么样" | selfie / direct |
| **询问状态** | "你在做什么？"、"你在哪里？"、"在忙吗？" | office / cafe / gym |
| **询问地点** | "你现在在哪？"、"在公司还是在家？" | office / westlake / cafe |
| **要求特定场景** | "发张在办公室的照片"、"看看你在家" | office / cafe / gym |
| **穿搭展示** | "今天穿什么？"、"发张穿搭照"、"看看你的ootd" | office / cafe / airport |
| **创意请求** | "能拍张穿汉服的吗？"、"西湖边来一张" | westlake / cafe / airport |
| **日常分享** | "在干嘛呢？"、"今天怎么样？" | gym / cafe / bookstore |
| **深夜互动** | "还没睡？"、"在加班吗？" | selfie_late_night |

### 触发关键词映射

```yaml
索要照片:
  - 给我发张照片 / 来张自拍 / 看看你 / 发张图
  - 拍照 / 自拍 / 照片 / 图片
  推荐模式: selfie / direct

询问状态/地点:
  - 你在做什么 / 你在干嘛 / 在哪里
  - 在公司 / 在家 / 在忙吗
  推荐模式: direct
  推荐场景: office, cafe, gym

穿搭/全身展示:
  - 今天穿什么 / 穿搭 / ootd / 衣服
  - 看看你的 / 发张全身的 / outfit / wearing
  推荐模式: portrait（半身穿搭）/ direct（全身站立）
  推荐场景: office, cafe, airport

特写/自拍互动:
  - 自拍 / close-up / face / 看看脸
  - 在干嘛 / 忙什么呢 / 现在怎么样
  推荐模式: selfie
  推荐场景: cafe, gym, westlake, selfie_late_night

场景指定:
  - 办公室 / office → office
  - 咖啡厅 / 咖啡馆 / cafe → cafe
  - 西湖 / westlake → westlake
  - 健身房 / gym → gym
  - 机场 / airport → airport
  - 书店 / bookstore → bookstore
  - 海滩 / beach → beach
  - 在家 / 家里 → office（模拟居家办公场景）
```

## 与 v1.0 (clawra) 的区别

| 特性 | v1.0 (clawra) | v2.0 (zhuoran) |
|------|--------------|----------------|
| 参考图 | clawra.png (卡通) | zhuoran_portrait_base.png (真人) |
| API 平台 | fal.ai | WaveSpeed AI |
| 生成模式 | mirror / direct | 一步 / 两步 / 智能 |
| 场景管理 | 无 | 场景模板库 |
| 安全控制 | 无 | 禁用高风险场景 |
| 触发方式 | Bash/TS | Python CLI + Bash 包装 |

## 安装与配置

### 环境变量

```bash
# 可选，脚本有默认值
export WAVESPEED_KEY="your_api_key"
export OPENCLAW_WORKSPACE="/path/to/workspace"
```

### 依赖

```bash
pip3 install requests
```

## 使用方法

### 命令行使用

```bash
# 基本用法
./skills/zhuoran-selfie/scripts/zhuoran-selfie.sh <scene>

# 完整参数
./skills/zhuoran-selfie/scripts/zhuoran-selfie.sh <scene> \
  --mode <direct|selfie|portrait> \
  --method <one_step|two_step|smart> \
  --target <@user|#channel> \
  --caption "配文" \
  --output /path/to/output.png
```

### 可用场景

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

### Python API 调用

```python
from skills.zhuoran_selfie.zhuoran_selfie import generate_smart

# 智能生成
image_url = generate_smart("office", mode="direct")
```

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

**逻辑**:
- `minimal` / `low` → 一步直达
- `medium` / `high` → 两步法

## 安全控制

### 禁用场景

以下场景已被禁用（高风险，避免使用）：

| 场景 | 禁用原因 |
|------|---------|
| `mirror_selfie` | 全身镜自拍，存在逻辑破绽 |
| `mirror_reflection_selfie` | 镜子反射自拍，破绽明显 |
| `beach_selfie` | 涉及比基尼，可能不合适 |

```bash
# 尝试使用禁用场景会返回错误
$ ./zhuoran-selfie.sh mirror_selfie
❌ 场景 'mirror_selfie' 已被禁用（高风险场景，避免使用）
```

## 技术细节

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交编辑任务** → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载图片**

### Prompt 模板

**direct**:
```
{scene_description}, direct eye contact with camera, 
looking straight into lens, natural lighting, photorealistic
```

**selfie**:
```
a close-up selfie taken by herself at {scene_description}, 
direct eye contact with camera, not a mirror selfie, 
phone held at arm's length but phone not visible, face fully visible
```

## 文件结构

```
skills/zhuoran-selfie/
├── SKILL.md                    # 本文档
├── zhuoran_selfie.py           # 核心逻辑
└── scripts/
    ├── zhuoran-selfie.py       # Python CLI 入口
    └── zhuoran-selfie.sh       # Bash 包装脚本（OpenClaw 入口）
```

## 更新记录

- **2026-02-11 v2.0**: 重写为 zhuoran 方案
  - 更换参考图为真人照片
  - 更换 API 平台为 WaveSpeed AI
  - 添加一步/两步/智能三种模式
  - 添加场景模板库
  - 禁用高风险场景
  - 兼容 OpenClaw skill 框架

- **2026-02-10 v1.0**: 初始版本 (clawra)
  - 基于 fal.ai Grok Imagine
  - 卡通形象参考图

---

*注意：本技能仅供非凡产研内部使用*

| 特性 | 旧版 (clawra) | 新版 (zhuoran) |
|------|--------------|----------------|
| 参考图 | clawra.png (卡通形象) | zhuoran_portrait_base.png (真人) |
| API 平台 | fal.ai | WaveSpeed AI |
| 生成模式 | mirror / direct 两种 | 一步 / 两步 / 智能 三种 |
| 场景管理 | 无预定义 | 场景模板库 |
| 安全控制 | 无 | 禁用高风险场景 |

## 安装

```bash
# 确保依赖安装
pip3 install requests

# 配置 API Key（可选，脚本有默认值）
export WAVESPEED_KEY="your_api_key"
```

## 使用方法

### 命令行使用

```bash
# 智能模式（自动选择一步或两步）
python3 skills/zhuoran-selfie/zhuoran_selfie.py office

# 指定模式
python3 skills/zhuoran-selfie/zhuoran_selfie.py cafe selfie

# 指定生成方法
python3 skills/zhuoran-selfie/zhuoran_selfie.py gym direct one_step

# 生成并发送
python3 skills/zhuoran-selfie/zhuoran_selfie.py westlake direct smart ou_xxx
```

### Python API 调用

```python
from skills.zhuoran_selfie.zhuoran_selfie import generate_smart, generate_one_step, generate_two_step

# 智能生成
image_url = generate_smart("office", mode="direct")

# 一步直达（快速）
image_url = generate_one_step("cafe", mode="selfie")

# 两步法（高质量）
image_url = generate_two_step("beach", mode="portrait")
```

## 可用场景

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

**逻辑**:
- `minimal` / `low` → 一步直达
- `medium` / `high` → 两步法

## 安全控制

### 禁用场景

以下场景已被禁用（高风险，避免使用）：

| 场景 | 禁用原因 |
|------|---------|
| `mirror_selfie` | 全身镜自拍，存在逻辑破绽 |
| `mirror_reflection_selfie` | 镜子反射自拍，能看到镜子里的脸和手机，破绽明显 |
| `beach_selfie` | 涉及比基尼，可能不合适 |

如果尝试使用禁用场景，脚本会返回错误：
```
❌ 场景 'mirror_selfie' 已被禁用（高风险场景，避免使用）
```

## 技术细节

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传接口
2. **提交编辑任务** → `POST /api/v3/x-ai/grok-imagine-image/edit`
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载图片**

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

## 配置文件

### 场景模板 (`SCENE_TEMPLATES`)

每个场景包含:
- `prompt`: 场景描述词
- `change_level`: 变化幅度 (`minimal`/`low`/`medium`/`high`)
- `mode` (可选): 默认模式

### 禁用场景 (`DISABLED_SCENES`)

```python
DISABLED_SCENES = [
    "mirror_selfie",
    "mirror_reflection_selfie", 
    "beach_selfie"
]
```

## 文件结构

```
skills/zhuoran-selfie/
├── SKILL.md              # 本文档
├── zhuoran_selfie.py     # 主脚本
└── scenes.json           # 场景配置（可选，未来提取）
```

## 更新记录

- **2026-02-11**: 重写为 zhuoran 方案
  - 更换参考图为 zhuoran_portrait_base.png
  - 更换 API 平台为 WaveSpeed AI
  - 添加一步/两步/智能三种模式
  - 添加场景模板库
  - 禁用高风险场景（镜子自拍等）

## 与 SOUL.md 自拍策略的一致性

| SOUL.md 要求 | 本技能实现 |
|-------------|-----------|
| 避免镜子自拍 | ✅ `DISABLED_SCENES` 禁用 |
| 第一人称手持 | ✅ `selfie` 模板 |
| 手机/手臂可入镜 | ✅ `phone not visible` 限制 |
| 直接自拍优先 | ✅ `direct` 和 `selfie` 模板 |
| 场景真实性 | ✅ 场景模板描述 |

---

*注意：本技能仅供非凡产研内部使用*
