---
name: feishu-video-sender
description: |
  飞书视频发送工具 / Feishu video message sender. 直接调用 API 发送视频消息，在飞书中以视频播放器形式展示（非文件附件），支持自动生成封面。
  Use when: "发送视频消息", "send video message", "飞书视频播放", "feishu video player", "上传视频到飞书", "upload video to feishu", "群视频分享", "group video sharing", "视频封面生成", "video cover generation".
  使用 msg_type: media 发送视频，配合 file_key 和 image_key，在飞书中显示为可播放的视频播放器。Cross-references: feishu-voice-sender, feishu-group-welcome, feishu-message-recall.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Video Sender

> 直接调用飞书 API 发送视频消息，支持私聊和群聊，视频以播放器形式展示（不是文件附件）。

## When to Use

Use this skill when:
- 需要发送可在飞书中直接播放的视频消息时
- 使用标准 `message(filePath="video.mp4")` 导致视频变成不可播放的文件附件时
- 需要自动生成视频封面并发送时
- 需要向群聊或私聊分享视频内容时

Do NOT use this skill if:
- 需要发送语音消息 → use `feishu-voice-sender` instead
- 只需要发送普通文件（不要求播放器形式）→ 使用标准 file 消息 instead
- 视频超过 100MB（可能超出 API 限制）→ 建议先压缩或上传到云盘分享链接 instead

Typical triggers:
- 「发一个视频到飞书群」「视频发出去变成文件了，帮我修复」
- "Send this video to Feishu chat", "上传视频并发送"

## Workflow

1. **探查 (Probe)**
确认视频文件路径、目标 ID（`ou_xxx` 或 `oc_xxx`）、可选封面图路径、可选视频描述。

2. **约束 (Constrain)**
确保已安装 `ffmpeg` 和 Python `requests`。飞书 API 对视频大小通常限制在 100MB 以内。必须使用 `msg_type: "media"` 才能在飞书中显示为可播放的视频。不降级——视频过大时建议压缩而非强行发送。

3. **证据 (Evidence)**
确认视频文件存在且可读，目标 ID 格式正确。获取飞书 `tenant_access_token`。

4. **执行 (Execute)**
1. 上传视频获取 `file_key`：`POST /open-apis/im/v1/files`
2. 自动生成封面（第1秒画面）或上传用户指定的封面图获取 `image_key`
3. 使用 `msg_type: "media"` 发送视频

```bash
python3 skills/feishu-video-sender/feishu_video_sender.py /path/to/video.mp4 ou_xxx
```

5. **验证 (Verify)**
确认消息发送成功，返回消息 ID 和发送状态。检查视频在飞书中是否以播放器形式展示。

6. **交付 (Deliver)**
返回消息 ID 和发送状态，清理临时文件（自动生成的封面图）。

## Output

返回消息 ID 和发送状态，包含 file_key、image_key 和目标 ID。

## Guardrails

**Anti-patterns**
- NEVER 使用 `msg_type: "file"` 发送视频（会变成不可播放的文件附件）
- Do NOT 发送超过 100MB 的视频（可能超出 API 限制）
- Do NOT 跳过封面图（没有封面的视频在飞书中显示效果差）

**Constraints**
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

- **feishu-voice-sender** — 发送飞书语音消息
- **feishu-group-welcome** — 群聊管理与消息发送
- **feishu-message-recall** — 撤回已发送的消息

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
