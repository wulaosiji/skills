---
name: media-hub
description: |
  Unified media processing center for audio and video transcription, format conversion,
  frame extraction, and content understanding. Handles batch processing, subtitle generation,
  and speech-to-text with multi-language support.
  Use when: "媒体处理", "音视频转录", "格式转换", "视频转文字", "生成字幕", "media processing", "video transcription", "audio to text", "subtitle generation", "extract frames".
  Cross-references: whisper-stt, voice-clone, video-generation.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Media Hub

> Unified audio and video processing, transcription, and understanding.

## When to Use

Use this skill when:
- Processing **audio or video files** for transcription or conversion
- Generating **subtitles** or **speech-to-text** output
- Extracting **frames** or **clips** from video content
- Performing **batch media operations** or format conversions
- Generating **content summaries** or topic extraction from media

Do NOT use this skill if:
- The task is creating presentation slides → use **pitch-deck-creator**
- The task requires map or location data → use **amap-navigator**
- You only need simple file copying without media analysis
- You need real-time streaming transcription → use specialized streaming tools

Typical triggers:
- 「视频转文字」「音频转录」「生成字幕」「格式转换」「媒体转换」「提取视频帧」
- "transcribe video", "convert media format", "audio to text", "extract video frames", "batch process audio", "media processing"

## Workflow

1. **探查 (Probe)**: 完整读取需求，确认媒体输入类型（本地文件路径/URL/批量目录）、目标操作（转录/格式转换/帧提取/字幕生成/内容理解）和输出要求。

2. **约束 (Constrain)**: 验证输入文件完整性和格式支持，设定边界：不覆盖原始源文件、大文件需分块、低质量音频需标注准确率警告。受阻时换通道（如格式不支持先转码），不降级交付物。

3. **证据 (Evidence)**: 每个处理操作的参数来自媒体文件元数据（时长、分辨率、编码格式）和用户指定要求。转录结果附带时间戳和置信度。

4. **执行 (Execute)**: 运行相关处理管道，先给影响与结论，再给行动和必要证据。

**接收媒体输入**
- File path to local audio/video
- URL to downloadable media
- Existing media directory for batch processing

**选择处理模式**
- Transcription — speech-to-text with speaker diarization (optional)
- Format Conversion — re-encode to mp3, mp4, wav, webm, etc.
- Frame Extraction — capture keyframes at intervals or timestamps
- Subtitle Generation — produce SRT/VTT from transcribed audio
- Content Understanding — generate summaries or topic extraction from media

**配置参数**
- Source language for transcription (auto-detect if not specified)
- Output format and quality settings
- Target directory for processed files
- Batch size (for bulk operations)

**执行处理**
```
Processing: filename.ext
- Transcoding: 45%
- Transcribing: 20%
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——检查转录文本与音频对应关系、验证转换后文件可正常播放、确认提取帧的时间戳准确、检查字幕同步。

6. **交付 (Deliver)**: 输出文件到结构化目录，返回处理结果摘要，清理临时文件。

## Output

输出文件结构化目录：
```
media-output/
├── transcript.txt / .srt / .vtt
├── converted/
├── frames/
└── summary.md
```

- **转录**: TXT / SRT / VTT 格式，含时间戳（字幕格式）
- **格式转换**: 目标格式文件（mp3/mp4/wav/webm等）
- **帧提取**: PNG/JPG 帧图片，含元数据（时间戳、分辨率）
- **内容理解**: Markdown 格式摘要和主题提取
- **原始文件**: 保持不变，不覆盖

## Guardrails

**Anti-patterns:**
- NEVER 处理受版权保护的内容而未经用户确认
- NEVER 覆盖原始源文件，始终输出到单独目录
- NEVER 返回极长的原始转录文本而不提供摘要或目录
- Do NOT 对不支持的格式不提示用户就跳过
- Do NOT 对大文件不分块处理

**Output Constraints**
- Original files remain untouched
- Transcripts include timestamps when subtitles are requested
- Frame extractions include metadata (timestamp, resolution)
- Summaries are concise and structured

**Error Handling**
- Unsupported format: inform user and suggest conversion options
- Large files: split into chunks or request shorter segments
- Low-quality audio: flag accuracy warnings in transcription output

## Related Skills

- **whisper-stt** — 本地语音转文字，可作为媒体转录的底层引擎
- **voice-clone** — 语音克隆和合成，可与媒体处理结合生成配音
- **video-generation** — 视频生成和超分，可作为媒体处理的上游或下游

## About UniqueClub

This skill is part of the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai
