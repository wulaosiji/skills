# Document Hub ↔ Media Hub 协作指南

## 架构关系

```
┌─────────────────────────────────────────────────────────────┐
│                    内容处理工作流                            │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  输入源      │   │  输入源      │   │  输入源      │
│  视频文件    │   │  音频文件    │   │  文档文件    │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │
       ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Media Hub   │   │  Media Hub   │   │  Doc Hub     │
│  提取音频    │   │  转录文字    │   │  读取/编辑   │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
                   ┌──────────────┐
                   │  文本内容    │
                   └──────┬───────┘
                          ▼
                   ┌──────────────┐
                   │  Doc Hub     │
                   │  生成文档    │
                   └──────┬───────┘
                          ▼
                   ┌──────────────┐
                   │  Word/Excel  │
                   │  PDF/Markdown│
                   └──────────────┘
```

## 职责划分

| 功能 | Media Hub | Doc Hub |
|------|-----------|---------|
| **视频处理** | ✅ 提取音频、转码、裁剪 | ❌ |
| **音频处理** | ✅ 转录、转换、信息提取 | ❌ |
| **图片处理** | ✅ 格式转换、缩放 | ❌ |
| **文档读取** | ❌ | ✅ Word/Excel/PDF |
| **文档生成** | ❌ | ✅ Word/Excel/PDF/MD |
| **文档转换** | ❌ | ✅ MD ↔ Word ↔ PDF |
| **文本处理** | ✅ 语音→文字 | ✅ 文字→结构化文档 |

## 协作接口

### Media Hub → Doc Hub

```python
from skills.media_hub import get_hub as get_media_hub
from skills.document_hub import get_hub as get_doc_hub

# 1. Media Hub 处理媒体
media = get_media_hub()
doc_path = media.convert_to_doc_format("video.mp4", output_format="txt")
# 输出: video.txt (纯文本转录)

# 2. Doc Hub 生成文档
doc = get_doc_hub()
content = doc.read(doc_path)  # 读取转录文本

# 3. 生成Word
doc.write("output.docx", {
    "title": "会议纪要",
    "paragraphs": [content]
})
```

### 标准协作流程

#### 流程1：视频 → 结构化文档

```python
# Step 1: Media Hub 转录
from skills.media_hub import transcribe_video
result = transcribe_video("meeting.mp4")

# Step 2: 结构化处理（可以在这里添加AI分析）
structured_content = {
    "title": "会议纪要",
    "sections": [
        {"heading": "会议内容", "text": result['text']},
        {"heading": "关键决策", "text": extract_decisions(result['text'])}
    ]
}

# Step 3: Doc Hub 生成
from skills.document_hub import write
write("meeting.docx", structured_content)
```

#### 流程2：播客 → 飞书文档

```python
# Step 1: Media Hub 处理
from skills.media_hub import get_hub
hub = get_hub()
audio = hub.extract_audio("podcast.m4a")
text = hub.transcribe(audio)

# Step 2: 生成Markdown
with open("podcast.md", "w") as f:
    f.write(f"# 播客纪要\n\n{text}")

# Step 3: Doc Hub 转飞书
# 使用 feishu-doc-orchestrator
```

#### 流程3：批量视频处理

```python
import os
from skills.media_hub import get_hub as get_media
from skills.document_hub import get_hub as get_doc

media = get_media()
doc = get_doc()

for video in os.listdir("videos/"):
    # Media Hub: 视频 → 文本
    text = media.transcribe_video(f"videos/{video}")
    
    # Doc Hub: 文本 → Word
    doc.write(f"output/{video}.docx", {
        "title": video,
        "paragraphs": [text]
    })
```

## 数据流转格式

### Media Hub 输出 → Doc Hub 输入

| Media Hub 输出 | Doc Hub 输入 | 说明 |
|----------------|--------------|------|
| `transcribe()` 返回的 `text` | `write()` 的 `paragraphs` | 纯文本段落 |
| `convert_to_doc_format()` 生成的 `.txt` | `read()` 读取 | 文本文件 |
| `convert_to_doc_format()` 生成的 `.json` | 解析后使用 | 结构化数据 |

### 格式转换建议

```python
# Media Hub 转录结果
result = {
    'text': '完整转录文本...',
    'segments': [...],  # 时间分段
    'language': 'zh'
}

# 转为 Doc Hub 格式
content = {
    'title': '标题',
    'paragraphs': result['text'].split('\n'),  # 分段
    'metadata': {
        'language': result['language'],
        'duration': '40分钟'
    }
}
```

## 共享工作流

### 工作流1：会议自动化

```
会议录音 (Media Hub)
    ↓
提取音频 + 转录
    ↓
生成结构化文本
    ↓
Doc Hub 生成Word文档
    ↓
飞书文档上传
```

### 工作流2：内容创作

```
视频素材 (Media Hub)
    ↓
提取关键片段 + 转录
    ↓
整理为文章结构
    ↓
Doc Hub 生成Markdown
    ↓
发布到各平台
```

### 工作流3：知识归档

```
播客/讲座 (Media Hub)
    ↓
完整转录
    ↓
提取知识点 + 打标签
    ↓
Doc Hub 生成PDF文档
    ↓
存档到知识库
```

## 依赖关系

```bash
# 单独使用 Doc Hub
pip install python-docx pandas openpyxl pdfplumber

# 单独使用 Media Hub
pip install openai-whisper pydub moviepy Pillow
brew install ffmpeg

# 两者都用（完整功能）
pip install python-docx pandas openpyxl pdfplumber \
            openai-whisper pydub moviepy Pillow
brew install ffmpeg
```

## 导入方式

```python
# 方式1：分别导入（推荐）
from skills.media_hub import get_hub as get_media_hub
from skills.document_hub import get_hub as get_doc_hub

media = get_media_hub()
doc = get_doc_hub()

# 方式2：快捷函数
from skills.media_hub import transcribe, extract_audio
from skills.document_hub import read, write, convert
```

## 错误处理

```python
try:
    # Media Hub 处理
    text = media.transcribe("audio.mp3")
    
    # Doc Hub 处理
    doc.write("output.docx", {"paragraphs": [text]})
    
except MediaError as e:
    print(f"媒体处理错误: {e}")
except DocumentError as e:
    print(f"文档处理错误: {e}")
```

---

**Document Hub**: `skills/document-hub/`  
**Media Hub**: `skills/media-hub/`  
**协作示例**: `skills/workflows/` (待创建)
