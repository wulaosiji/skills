---
name: whisper-stt
description: |
  Local speech-to-text transcription skill based on OpenAI Whisper.
  Completely free, no API key required, supports Chinese and multiple languages.
  Ideal for private, offline voice transcription with high accuracy.
  Use when: "语音转文字", "语音转录", "本地STT", "语音识别", "音频转文字", "转录音频", "speech to text", "local STT", "speech recognition", "whisper transcription".
  Cross-references: voice-clone, media-hub, video-generation.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Whisper STT 技能 (Whisper Speech-to-Text)

> 本地语音转文字，隐私安全，完全免费，无需 API Key。

## When to Use

Use this skill when:
- 需要将语音/音频转换为文字
- 隐私要求高的场景（本地处理，不上传云端）
- 无需网络连接的场景
- 中文语音转录
- 多语言语音转录
- 与语音克隆结合使用（语音→文字→AI处理→语音）

Do NOT use this skill if:
- 需要实时流式转录（Whisper 适合离线批量处理）
- 对转录速度要求极高且设备性能有限
- 需要云端协作或共享转录结果
- 音频质量极差（背景噪音过大）

Typical triggers:
- 「语音转文字」「语音转录」「本地STT」「语音识别」「音频转文字」「转录音频」
- "speech to text", "voice transcription", "local STT", "speech recognition", "audio transcription", "whisper transcription"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的音频文件，确认音频格式、语言、目标输出格式和模型大小选择。

2. **约束 (Constrain)**: 验证音频质量（语音清晰、避免背景噪音），设定边界：不适合实时流式转录、长音频需分批处理。根据设备性能选择合适模型大小，不降级交付物。

3. **证据 (Evidence)**: 模型选择基于大小/速度/准确率的权衡（tiny/base/small/medium/large）。每个模型的参数量和适用场景来自 OpenAI Whisper 官方规格。

4. **执行 (Execute)**: 调用 Whisper 模型转录音频，先给影响与结论，再给行动和必要证据。

**安装依赖**
```bash
pip3 install openai-whisper
```

**使用封装脚本**
```python
from tools.whisper_stt import transcribe
result = transcribe("audio.mp3", model="base", language="zh")
if result.get("success"):
    print(f"转录内容: {result['text']}")
```

**命令行使用**
```bash
whisper audio.mp3
whisper audio.mp3 --model base --language zh
whisper audio.mp3 --model base --language zh --output_format txt
```

**与语音克隆结合**
```python
from tools.whisper_stt import transcribe
from tools.voice_clone_api import generate_speech
stt_result = transcribe("user_voice.mp3")
text = stt_result["text"]
response = f"收到: {text}"
generate_speech(response, voice_id="wuna-001")
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——抽查转录文本与音频的对应关系，检查专业术语和人名的准确性，确认语言检测正确。

6. **交付 (Deliver)**: 返回转录文本（支持 txt/srt/vtt 等格式），清理临时文件和模型缓存（如需要）。

## Model Selection

| 模型 | 大小 | 速度 | 准确率 | 推荐场景 |
|------|------|------|--------|---------|
| tiny | 39MB | 最快 | 一般 | 测试 |
| base | 74MB | 快 | 良好 | 日常使用 ✅ |
| small | 244MB | 中等 | 好 | 平衡 |
| medium | 769MB | 较慢 | 很好 | 高质量 |
| large | 1550MB | 最慢 | 最佳 | 精确转录 |

## Output

- 格式: TXT (默认) / SRT / VTT / JSON
- 语言: 自动检测或指定（中文、英文及 90+ 语言）
- 输出包含: 转录文本、时间戳（字幕格式）、检测语言
- 默认保存: 与输入文件同目录，同名不同后缀

## Guardrails

**Anti-patterns:**
- NEVER 在音频质量极差时期望高准确率（背景噪音过大）
- NEVER 对长音频不分批处理（可能内存不足）
- NEVER 不指定语言时期望中文最佳效果（自动检测可能偏差）
- Do NOT 用于实时流式转录场景

**音频质量要求**
- 格式: MP3, WAV, M4A 等常见格式
- 清晰度: 语音清晰，避免背景噪音
- 音量: 正常音量，避免过小或失真
- 语言: 支持中文、英文及 90+ 语言

**限制说明**
- 实时性: 不适合实时流式转录
- 资源占用: 大型模型需要较多内存
- 准确性: 口音、方言可能影响准确率
- 时长: 长音频可能需要分批处理

**故障排除**

| 问题 | 解决方案 |
|------|---------|
| 安装失败 | 先装PyTorch CPU: `pip3 install torch --index-url https://download.pytorch.org/whl/cpu` |
| 速度慢 | 换用tiny/base模型 |
| 中文不准 | 确认指定 `--language zh` |
| 内存不足 | 使用base/tiny模型 |

## Related Skills

- **voice-clone** — 语音克隆技能，可与STT形成完整语音工作流（语音→文字→AI→语音）
- **media-hub** — 统一媒体处理中心，支持批量音视频转录和格式转换
- **video-generation** — 可为生成的视频添加语音转录和字幕

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for speech processing.
🌐 https://uniqueclub.ai
