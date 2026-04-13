---
name: whisper-stt
description: |
  Local speech-to-text transcription skill based on OpenAI Whisper.
  Completely free, no API key required, supports Chinese and multiple languages.
  Ideal for private, offline voice transcription with high accuracy.

  Use when: 语音转文字, 语音转录, 本地STT, 语音识别, 音频转文字, 
  speech to text, voice transcription, local STT, speech recognition, 
  audio transcription, whisper transcription

  Related: voice-clone

  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Whisper STT 技能 (Whisper Speech-to-Text)

本地语音转文字，隐私安全，完全免费，无需 API Key。

## When to Use

**适用于以下场景：**
- 需要将语音/音频转换为文字
- 隐私要求高的场景（本地处理，不上传云端）
- 无需网络连接的场景
- 中文语音转录
- 多语言语音转录
- 与语音克隆结合使用（语音→文字→AI处理→语音）

**Do NOT use this skill if:**
- 需要实时流式转录（Whisper 适合离线批量处理）
- 对转录速度要求极高且设备性能有限
- 需要云端协作或共享转录结果
- 音频质量极差（背景噪音过大）

**触发关键词 / Trigger Phrases:**
- 语音转文字 / speech to text
- 语音转录 / voice transcription
- 本地STT / local STT
- 语音识别 / speech recognition
- 音频转文字 / audio transcription
- 转录音频 / transcribe audio
- whisper转录 / whisper transcription

## Workflow

### 1. 安装依赖

```bash
pip3 install openai-whisper
```

### 2. 使用封装脚本

```python
from tools.whisper_stt import transcribe

# 转录音频
result = transcribe("audio.mp3", model="base", language="zh")

if result.get("success"):
    print(f"转录内容: {result['text']}")
else:
    print(f"错误: {result['error']}")
```

### 3. 命令行使用

```bash
# 基本用法
whisper audio.mp3

# 指定中文和模型
whisper audio.mp3 --model base --language zh

# 指定输出格式
whisper audio.mp3 --model base --language zh --output_format txt
```

### 4. 与语音克隆结合

```python
from tools.whisper_stt import transcribe
from tools.voice_clone_api import generate_speech

# 语音转文字
stt_result = transcribe("user_voice.mp3")
text = stt_result["text"]

# AI处理...
response = f"收到: {text}"

# 文字转语音（克隆声音）
generate_speech(response, voice_id="wuna-001")
```

## Model Selection

| 模型 | 大小 | 速度 | 准确率 | 推荐场景 |
|------|------|------|--------|---------|
| tiny | 39MB | 最快 | 一般 | 测试 |
| base | 74MB | 快 | 良好 | **日常使用** ✅ |
| small | 244MB | 中等 | 好 | 平衡 |
| medium | 769MB | 较慢 | 很好 | 高质量 |
| large | 1550MB | 最慢 | 最佳 | 精确转录 |

## Guardrails

### 音频质量要求

- **格式**: MP3, WAV, M4A 等常见格式
- **清晰度**: 语音清晰，避免背景噪音
- **音量**: 正常音量，避免过小或失真
- **语言**: 支持中文、英文及 90+ 语言

### 限制说明

- **实时性**: 不适合实时流式转录
- **资源占用**: 大型模型需要较多内存
- **准确性**: 口音、方言可能影响准确率
- **时长**: 长音频可能需要分批处理

### 故障排除

| 问题 | 解决方案 |
|------|---------|
| 安装失败 | 先装PyTorch CPU: `pip3 install torch --index-url https://download.pytorch.org/whl/cpu` |
| 速度慢 | 换用tiny/base模型 |
| 中文不准 | 确认指定 `--language zh` |
| 内存不足 | 使用base/tiny模型 |

## Related Skills

| 技能 | 关系 | 说明 |
|------|------|------|
| [voice-clone](./voice-clone) | 配套 | 语音克隆技能，可与STT形成完整语音工作流 |

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for speech processing.
Learn more: https://uniqueclub.ai

---

*基于OpenAI Whisper开源项目*
