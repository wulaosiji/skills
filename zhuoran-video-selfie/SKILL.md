---
name: zhuoran-video-selfie
description: 卓然自拍视频技能 - 基于垫图使用 WaveSpeed AI 生成场景化动态自拍视频
---
# 卓然视频自拍技能 (Zhuoran Video Selfie) v1.0

基于垫图（reference image）使用 WaveSpeed AI 生成"活人感"自拍视频，支持多种场景和发送方式。

## 快速开始

```bash
# 生成办公室自拍视频
openclaw skill run zhuoran-video-selfie office

# 指定场景并发送
openclaw skill run zhuoran-video-selfie cafe --target ou_xxx

# 直接调用脚本
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh westlake
```

## 触发场景

当用户出现以下意图时，自动调用本技能生成并发送自拍视频：

| 触发类型 | 用户话术示例 | 推荐场景 |
|---------|-------------|---------|
| **索要视频** | "发段视频看看"、"录个自拍视频"、"拍段小视频" | office / cafe |
| **动态展示** | "在做什么？动一下看看"、"眨个眼" | gym / westlake |
| **场景视频** | "拍段在西湖散步的"、"办公室里来一段" | westlake / office |
| **创意请求** | "能拍段穿汉服的视频吗？" | westlake / cafe |

### 触发关键词映射

```yaml
索要视频:
  - 发段视频 / 录个视频 / 拍段视频 / 小视频
  - 自拍视频 / 视频自拍 / 动态自拍
  推荐场景: office, cafe

动态展示:
  - 动一下 / 眨个眼 / 看看你在干嘛
  - 在做什么 / 在忙什么
  推荐场景: gym, cafe, office

场景指定:
  - 办公室 / office → office
  - 咖啡厅 / 咖啡馆 / cafe → cafe
  - 西湖 / westlake → westlake
  - 健身房 / gym → gym
```

## 与 zhuoran-selfie（照片版）的区别

| 特性 | 照片版 (zhuoran-selfie) | 视频版 (zhuoran-video-selfie) |
|------|------------------------|------------------------------|
| 输出格式 | 静态图片 PNG | 动态视频 MP4 |
| API 端点 | `/grok-imagine-image/edit` | `/video/generate` (Seedance) |
| 生成时长 | 2-10秒 | 2-5分钟 |
| 推荐时长 | 单张 | 5秒 |
| "活人感" | 静态 pose | 微动作（呼吸、眨眼） |
| 使用频率 | 高 | 低（偶尔使用） |
| 风险等级 | 低 | 中（动作不自然易暴露） |

## 安装与配置

### 环境变量

```bash
# WaveSpeed AI API Key
export WAVESPEED_KEY="your_api_key"

# 飞书配置（用于发送）
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

### 依赖

```bash
pip3 install requests
```

### 垫图配置

**重要**: 本 skill 需要垫图文件 `assets/zhuoran_portrait_base.png`，但该文件不被提交到 git（二进制文件）。

**首次使用前请复制垫图**:
```bash
# 从中央 assets 目录复制
cp ~/.openclaw/workspace/assets/avatars/zhuoran_portrait_base.png \
   ~/.openclaw/workspace/skills/zhuoran-video-selfie/assets/
```

**或者创建软链接**:
```bash
ln -s ~/.openclaw/workspace/assets/avatars/zhuoran_portrait_base.png \
      ~/.openclaw/workspace/skills/zhuoran-video-selfie/assets/zhuoran_portrait_base.png
```

**垫图要求**:
- 格式: PNG
- 内容: 真人照片（非卡通形象）
- 尺寸: 建议 512x512 或更高
- 背景: 简洁，便于场景融合

## 使用方法

### 命令行使用

```bash
# 基本用法
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh <scene>

# 生成并发送给指定用户
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh office --target ou_xxx

# 指定时长（默认5秒）
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh cafe --duration 3

# 完整参数
./skills/zhuoran-video-selfie/scripts/zhuoran-video-selfie.sh <scene> \
  --duration 5 \
  --target <user_id> \
  --caption "配文" \
  --output /path/to/output.mp4
```

### 可用场景

| 场景 | 代码 | 推荐时长 | 提示词重点 |
|------|------|---------|-----------|
| 办公室 | `office` | 5秒 | 自然工作姿态、微动作 |
| 咖啡厅 | `cafe` | 5秒 | 轻松氛围、微笑 |
| 西湖 | `westlake` | 5秒 | 风景互动、微风 |
| 健身房 | `gym` | 3秒 | 运动姿态、呼吸感 |

### Python API 调用

```python
from skills.zhuoran_video_selfie.zhuoran_video_selfie import generate_video

# 生成视频
video_path = generate_video("office", duration=5)

# 生成并发送
video_path = generate_video("cafe", duration=5, target="ou_xxx")
```

## "活人感"提示词系统

### 核心原则

1. **自然微动** - 呼吸、眨眼、头发飘动
2. **避免完美** - 保留皮肤纹理、自然瑕疵
3. **场景真实** - 自拍角度、环境互动

### 基础模板

```
{scene_description}, subtle breathing motion and natural posture shift, 
gentle hair swaying in {environment} breeze, soft smile with micro-expressions, 
occasional natural blink and eye movement, {interaction}, 
authentic selfie perspective with slight arm visible, 
natural skin texture with realistic details, 4k cinematic quality, 
shallow depth of field, lifelike atmosphere
```

### 场景变体

**office**:
```
young professional woman at modern office desk, subtle breathing motion...
working on laptop, occasional glance up from screen, natural office lighting...
```

**cafe**:
```
young woman at cozy cafe, subtle breathing motion...
holding coffee cup, gentle steam rising, warm ambient lighting...
```

**westlake**:
```
young woman at West Lake Hangzhou, subtle breathing motion...
enjoying the scenery, golden hour sunlight, water reflection in background...
```

**gym**:
```
young woman at gym, subtle breathing motion and natural posture shift...
light workout movement, natural exertion, gym equipment in background...
```

## 安全控制

### 禁用场景

以下场景已被禁用（高风险，避免使用）：

| 场景 | 禁用原因 |
|------|---------|
| `mirror_selfie` | 镜子反射，逻辑破绽明显 |
| `dancing` | 大幅度动作，肢体一致性难保证 |
| `walking` | 移动场景，背景与人物同步难 |
| `group` | 多人入镜，复杂度太高 |
| `swimming` | 水下场景，物理逻辑复杂 |

### 风险控制原则

- **时长限制**: 最长5秒，避免暴露不自然动作
- **场景限制**: 仅使用预定义的安全场景
- **动作限制**: 微动作优先，避免大幅度运动
- **频率限制**: 视频比照片使用频率更低

## 技术细节

### API 调用流程

1. **上传参考图** → WaveSpeed AI 媒体上传
2. **提交视频生成任务** → `POST /api/v3/x-ai/video/generate`
   - 模型: `bytedance/seedance-v1-pro-i2v-720p`
   - 输入: 垫图 URL + 提示词
   - 参数: duration=5, aspect_ratio="1:1"
3. **轮询结果** → `GET /api/v3/predictions/{task_id}/result`
4. **下载视频** → 保存到临时目录
5. **飞书发送**（如指定 target）→ 上传获取 file_key → 发送消息

### 飞书视频发送

**⚠️ 重要**: 视频不能直接通过 OpenClaw `message` 工具的 `filePath` 发送，否则会显示为文件附件无法播放。

**正确方式**:

**方法1: 使用技能脚本（推荐）**
```bash
python3 skills/feishu-video-sender/feishu_video_sender.py \
  /tmp/zhuoran_office_video.mp4 \
  ou_5f3a4a920dc39a8d1835fd0085afef50
```

**方法2: 直接调用 API**
```python
# 1. 上传视频获取 file_key
file_key = upload_video_to_feishu(video_path)

# 2. 生成/上传封面获取 image_key  
image_key = upload_image_to_feishu(thumbnail_path)

# 3. 发送视频消息（msg_type: media）
send_feishu_message(
    msg_type="media",
    content={"file_key": file_key, "image_key": image_key}
)
```

**技术要点**:
- 必须使用 `msg_type: "media"` 而非 `"file"`
- 必须同时提供 `file_key`（视频）和 `image_key`（封面）
- 技能 `feishu-video-sender` 已封装完整流程

---

### 备用模型方案（A/B 机制）

**问题**: 2026-02-11 发现 `/x-ai/video/generate` 统一端点故障，需使用模型专属端点。

**推荐配置**:

| 优先级 | 模型 | 端点 | 状态 | 说明 |
|-------|------|------|------|------|
| **A方案** | Seedance v1 pro 720p | `/bytedance/seedance-v1-pro-i2v-720p` | ✅ 可用 | 首选，质量好 |
| **B方案** | VidU Q3 Turbo | `/vidu/q3-turbo/image-to-video` | ✅ 可用 | 备用，稳定 |

**自动切换逻辑**:
```python
# 优先尝试 A方案
models = [
    ("bytedance/seedance-v1-pro-i2v-720p", {
        "image": image_url,
        "prompt": prompt,
        "duration": duration,
        "resolution": "720p"
    }),
    ("vidu/q3-turbo/image-to-video", {  # 备用
        "image": image_url,
        "prompt": prompt,
        "duration": duration,
        "resolution": "720p"
    })
]

for model, payload in models:
    try:
        result = call_model_endpoint(model, payload)
        if result.get("code") == 200:
            return result
    except Exception as e:
        continue
```

### 推荐模型配置（更新）

| 参数 | Seedance (A方案) | VidU (B方案) |
|------|-----------------|--------------|
| 端点 | `/bytedance/seedance-v1-pro-i2v-720p` | `/vidu/q3-turbo/image-to-video` |
| 参数格式 | `image`, `prompt`, `duration`, `resolution` | `image`, `prompt`, `duration`, `resolution` |
| 时长范围 | 1-10秒 | 1-16秒 |
| 分辨率 | 480p/720p/1080p | 540p/720p/1080p |

| 参数 | 值 | 说明 |
|------|-----|------|
| model | `bytedance/seedance-v1-pro-i2v-720p` | 推荐：高清720p |
| duration | 5 | 5秒时长 |
| aspect_ratio | "1:1" | 正方形，适合自拍 |
| resolution | "720p" | 720p分辨率 |

## 文件结构

```
skills/zhuoran-video-selfie/
├── SKILL.md                    # 本文档
├── zhuoran_video_selfie.py     # 核心逻辑
└── scripts/
    ├── zhuoran-video-selfie.py # Python CLI 入口
    └── zhuoran-video-selfie.sh # Bash 包装脚本（OpenClaw 入口）
```

## 与 SOUL.md 自拍策略的一致性

| SOUL.md 要求 | 本技能实现 |
|-------------|-----------|
| 避免镜子自拍 | ✅ `DISABLED_SCENES` 禁用 mirror_selfie |
| 第一人称手持 | ✅ 提示词包含 `authentic selfie perspective` |
| 手机/手臂可入镜 | ✅ `slight arm visible` |
| 直接自拍优先 | ✅ 场景模板设计为自拍视角 |
| 亲密度边界 | 由调用方控制（target 参数）|
| "活人感" | ✅ 微动作提示词系统 |
| 时长控制 | ✅ 默认5秒，避免暴露 |

## 更新记录

- **2026-02-11 v1.0**: 初始版本
  - 基于 WaveSpeed AI Seedance 模型
  - 支持 4 个安全场景（office/cafe/westlake/gym）
  - "活人感"提示词系统
  - 禁用高风险场景
  - 飞书视频发送集成

---

*注意：本技能仅供非凡产研内部使用*
