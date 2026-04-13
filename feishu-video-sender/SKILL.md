---
name: feishu-video-sender
description: |
  飞书视频发送工具 / Feishu video message sender.
  直接调用 API 发送视频消息，在飞书中以视频播放器形式展示（非文件附件）。

  Use when: 发送视频消息, send video message, 飞书视频播放, feishu video player,
  上传视频到飞书, upload video to feishu, 群视频分享, group video sharing,
  视频封面生成, video cover generation, 私聊发视频, private video message,
  富媒体消息, rich media message, 自动发视频, automated video delivery.

  Related: feishu-voice-sender, feishu-group-welcome.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Video Sender

直接调用飞书 API 发送视频消息，支持私聊和群聊，视频以播放器形式展示（不是文件附件）。

## When to Use

- 需要发送可在飞书中直接播放的视频消息时
- 使用标准 `message(filePath="video.mp4")` 导致视频变成不可播放的文件附件时
- 需要自动生成视频封面并发送时
- 需要向群聊或私聊分享视频内容时

### Do NOT use this skill if

- 需要发送语音消息 → 使用 `feishu-voice-sender`
- 只需要发送普通文件（不要求播放器形式）→ 使用标准 file 消息
- 视频超过 100MB（可能超出 API 限制）→ 建议先压缩或上传到云盘分享链接

### Typical Trigger Phrases

- "发一个视频到飞书群"
- "Send this video to Feishu chat"
- "视频发出去变成文件了，帮我修复"
- "上传视频并发送"

## Workflow

1. **Ask for inputs**: 确认视频文件路径、目标 ID（`ou_xxx` 或 `oc_xxx`）、可选封面图路径、可选视频描述
2. **Verify dependencies**: 确保已安装 `ffmpeg` 和 Python `requests`
3. **Get token**: 获取飞书 `tenant_access_token`
4. **Upload video**: 调用 `POST /open-apis/im/v1/files` 上传视频获取 `file_key`
5. **Generate/upload cover**: 使用 `ffmpeg` 自动生成封面（第1秒画面），或上传用户指定的封面图获取 `image_key`
6. **Send video**: 调用 `POST /open-apis/im/v1/messages`，使用 `msg_type: "media"` 发送
   ```bash
   python3 skills/feishu-video-sender/feishu_video_sender.py /path/to/video.mp4 ou_xxx
   ```
7. **Confirm delivery**: 返回消息 ID 和发送状态

## Guardrails

- 飞书 API 对视频大小通常限制在 100MB 以内
- 自动生成封面取视频第 1 秒画面，如需更好效果建议手动提供封面图
- 必须使用 `msg_type: "media"` 才能在飞书中显示为可播放的视频

## Python API

```python
from skills.feishu_video_sender.feishu_video_sender import (
    get_token, upload_video, upload_image, generate_cover, send_video
)

token = get_token()
file_key = upload_video("/path/to/video.mp4", token)
generate_cover("/path/to/video.mp4", "/tmp/cover.jpg")
image_key = upload_image("/tmp/cover.jpg", token)
message_id = send_video(
    file_key=file_key,
    image_key=image_key,
    target_id="ou_xxx",
    token=token,
    msg_type="open_id"
)
```

## OpenClaw vs Direct API

| 方式 | 代码 | 结果 |
|------|------|------|
| OpenClaw | `message(filePath="video.mp4")` | 文件附件，无法播放 |
| 直接 API | `msg_type="media"` + file_key + image_key | 视频播放器，可播放 |

## Related Skills

- [feishu-voice-sender](../feishu-voice-sender/) - 发送飞书语音消息
- [feishu-group-welcome](../feishu-group-welcome/) - 群聊管理与消息发送

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
