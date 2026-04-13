---
name: media-hub
description: |
  Unified media processing center for audio and video transcription, format conversion,
  frame extraction, and content understanding. Handles batch processing, subtitle generation,
  and speech-to-text with multi-language support.
  Use when: "媒体处理", "media processing", "音视频转录", "video transcription", "格式转换",
  "audio to text", "视频转文字", "subtitle generation", "extract frames", "内容理解".
  Cross-references: baoyu-slide-deck, amap-navigator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
---

# Media Hub

> Unified audio and video processing, transcription, and understanding.

## When to Use

Use this skill when:
- Processing **audio or video files** for transcription or conversion
- Generating **subtitles** or **speech-to-text** output
- Extracting **frames** or **clips** from video content
- Performing **batch media operations** or format conversions

Do NOT use this skill if:
- The task is creating presentation slides → use **baoyu-slide-deck**
- The task requires map or location data → use **amap-navigator**
- You only need simple file copying without media analysis

Typical triggers:
- 「视频转文字」「音频转录」「生成字幕」
- "transcribe video", "convert media format", "audio to text"
- "extract video frames", "batch process audio", "媒体转换"

## Workflow

### Step 1: Ingest Media
Accept input via:
- File path to local audio/video
- URL to downloadable media
- Existing media directory for batch processing

### Step 2: Select Operation
Choose the appropriate processing mode:
- **Transcription** — speech-to-text with speaker diarization (optional)
- **Format Conversion** — re-encode to mp3, mp4, wav, webm, etc.
- **Frame Extraction** — capture keyframes at intervals or timestamps
- **Subtitle Generation** — produce SRT/VTT from transcribed audio
- **Content Understanding** — generate summaries or topic extraction from media

### Step 3: Configure Parameters
- Source language for transcription (auto-detect if not specified)
- Output format and quality settings
- Target directory for processed files
- Batch size (for bulk operations)

### Step 4: Execute Processing
Run the relevant pipeline and report progress:
```
Processing: filename.ext
- Transcoding: 45%
- Transcribing: 20%
```

### Step 5: Deliver Results
Output files to a structured directory:
```
media-output/
├── transcript.txt / .srt / .vtt
├── converted/
├── frames/
└── summary.md
```

## Guardrails

### Anti-patterns
- NEVER process copyrighted content without user confirmation
- NEVER overwrite original source files; always output to a separate directory
- NEVER return extremely long raw transcripts without a summary or table of contents

### Output Constraints
- Original files remain untouched
- Transcripts include timestamps when subtitles are requested
- Frame extractions include metadata (timestamp, resolution)
- Summaries are concise and structured

### Error Handling
- Unsupported format: inform user and suggest conversion options
- Large files: split into chunks or request shorter segments
- Low-quality audio: flag accuracy warnings in transcription output

## Related Skills

- **baoyu-slide-deck** — Convert processed media insights into presentation slides
- **amap-navigator** — Geotag or route media content when location context is needed

## About UniqueClub

This skill is part of the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
