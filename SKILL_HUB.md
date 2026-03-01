# Skill Hub - 技能导航中心 🧰

> 统一管理所有技能的入口和导航

## 快速导航

| 技能中心 | 功能 | 路径 |
|----------|------|------|
| 📄 **Document Hub** | Word/Excel/PDF/音视频处理 | `skills/document-hub/` |
| 🎬 **Video Understanding** | 音视频转录与理解 | `skills/media_hub/` |
| 🔍 **Content Extractor** | 外部平台内容抓取 | `skills/content-extractor/` |

## Document Hub（文档中心）

**路径**: `skills/document-hub/`

### 核心功能

```python
from skills.document_hub.document_hub import get_hub

hub = get_hub()

# 文档处理
hub.read("document.docx")           # 读取Word
hub.write("output.docx", content)   # 写入Word
hub.convert("input.md", "output.docx")  # 格式转换

# 音视频处理
hub.media.extract_audio_from_video("video.mp4", "audio.mp3")
hub.media.transcribe_video("meeting.mp4")  # 视频转录
hub.media.convert_audio("input.mp3", "output.wav")

# 获取信息
hub.get_info("file.pdf")
hub.get_media_info("song.mp3")
```

### 支持格式

**文档**: Word (.docx), Excel (.xlsx), PDF (.pdf), Markdown (.md)

**音频**: MP3, WAV, AAC, FLAC, OGG, M4A, WMA

**视频**: MP4, MOV, AVI, MKV, FLV, WMV, WEBM, M4V

### 文档

详见: `skills/document-hub/SKILL.md`

---

## Video Understanding（音视频理解）

**路径**: `skills/media_hub/`

### 核心功能

```python
from skills.media_hub import process_video, process_podcast

# 处理群聊视频
result = process_video(
    message_id="om_xxx",
    file_key="file_v3_xxx",
    model_size="base"
)

# 处理播客
result = process_podcast(
    audio_url="https://media.xyzcdn.net/xxx.m4a",
    title="播客标题",
    model_size="base"
)

# 访问结果
print(result['text'])        # 转录文本
print(result['analysis'])    # 内容分析
print(result['summary'])     # 自动摘要
```

### 模型选择

| 模型 | 大小 | 速度 | 适用场景 |
|------|------|------|----------|
| tiny | 39 MB | 最快 | 快速测试 |
| base | 74 MB | 快 | **日常使用** |
| small | 244 MB | 中等 | 高质量需求 |
| medium | 769 MB | 较慢 | 专业场景 |
| large | 1550 MB | 慢 | 最高质量 |

### 文档

详见: `skills/media_hub/SKILL.md`

---

## Content Extractor（内容提取）

**路径**: `skills/content-extractor/`

### 核心功能

```python
from skills.content_extractor import extract_xiaoyuzhou, extract_wechat

# 提取小宇宙播客
result = extract_xiaoyuzhou("https://www.xiaoyuzhoufm.com/episode/xxx")

# 提取微信公众号文章
result = extract_wechat("https://mp.weixin.qq.com/s/xxx")
```

### 支持平台

- 小宇宙播客
- 微信公众号
- 抖音
- B站
- 小红书

### 文档

详见: `skills/content-extractor/SKILL.md`

---

## 技能关系图

```
输入源
  │
  ├── 飞书群聊 ───┬──► Video Understanding ───► 文本/分析
  │               │
  ├── URL链接 ────┼──► Content Extractor ────► 结构化内容
  │               │
  ├── 本地文件 ───┼──► Document Hub ──────────► 文档处理
  │               │       │
  │               │       ├── 读取/写入/转换
  │               │       └── 音视频转录
  │               │
  └── 外部平台 ───┘

输出
  │
  ├── 飞书文档
  ├── Markdown
  ├── JSON
  └── 本地文件
```

## 典型工作流

### 工作流1：播客转飞书文档

```python
from skills.media_hub import process_podcast
from skills.feishu_doc_orchestrator import create_doc

# 1. 处理播客
result = process_podcast(audio_url, title)

# 2. 生成文档内容
doc_content = generate_podcast_summary(result)

# 3. 创建飞书文档
create_doc(title, doc_content)
```

### 工作流2：群聊视频理解

```python
from skills.media_hub import VideoUnderstandingSkill

skill = VideoUnderstandingSkill()

# 1. 下载视频
video = skill.download_from_feishu(msg_id, file_key)

# 2. 提取音频
audio = skill.extract_audio(video)

# 3. 转录+分析
result = skill.transcribe(audio)
analysis = skill.analyze_content(result['text'])
```

### 工作流3：文档转换链

```python
from skills.document_hub.document_hub import get_hub

hub = get_hub()

# Markdown → Word → PDF
hub.convert("input.md", "temp.docx")
hub.convert("temp.docx", "output.pdf")
```

---

## 更新日志

- **2026-02-12**: 
  - Video Understanding技能沉淀
  - Document Hub集成Whisper转录
  - Skill Hub导航中心创建

---

**维护**: 卓然  
**最后更新**: 2026-02-12
