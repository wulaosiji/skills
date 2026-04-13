---
name: feishu-voice-sender
description: |
  飞书语音消息发送工具 / Feishu voice message sender.
  将 MP3 音频文件以语音条形式发送到飞书私聊或群聊（非文件附件）。

  Use when: 发送语音消息, send voice message, 飞书语音条, feishu voice clip,
  MP3转飞书语音, mp3 to feishu voice, 群发语音, broadcast voice message,
  语音通知, voice notification, 私聊语音, private voice message,
  自动化语音推送, automated voice push.

  Related: feishu-video-sender, feishu-group-welcome.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Voice Sender

飞书语音消息发送工具 — 将 MP3 音频以语音条形式发送到飞书聊天。

## When to Use

- 需要将 MP3 音频以语音条（非文件附件）形式发送到飞书时
- 需要向群聊或私聊发送语音通知时
- 希望用户体验类似微信语音（点击直接播放）时
- 需要配合自动化流程发送语音消息时

### Do NOT use this skill if

- 需要发送视频消息 → 使用 `feishu-video-sender`
- 需要发送普通文本或富文本消息 → 使用 `feishu-group-welcome` 或标准 message 工具
- 需要发送音频文件（让用户下载后播放）→ 直接使用 file 消息类型

### Typical Trigger Phrases

- "发送一条语音到群里"
- "Send this MP3 as a voice message in Feishu"
- "把这段音频转成飞书语音条"
- "群发语音通知"

## Workflow

1. **Ask for inputs**: 确认音频文件路径（MP3）、目标 ID（群 ID `oc_xxx` 或用户 ID `ou_xxx`）、发送类型（chat/user）
2. **Verify environment**: 确认系统已安装 `ffmpeg`，Python 已安装 `requests`
3. **Convert format**: MP3 → AMR（飞书语音格式）
4. **Upload audio**: 上传到飞书获取 `file_key`
5. **Send voice message**: 使用 `msg_type: "voice"` 发送
   ```bash
   # 发送到群聊
   python3 skills/feishu-voice-sender/feishu_voice_sender.py /tmp/voice.mp3 oc_xxx --chat

   # 发送到私聊
   python3 skills/feishu-voice-sender/feishu_voice_sender.py /tmp/voice.mp3 ou_xxx --user
   ```
6. **Confirm delivery**: 返回消息发送结果

## Guardrails

- 必须安装 `ffmpeg` 用于格式转换
- 语音消息与音频文件的区别在于 `msg_type`：`voice` 直接播放，`file` 需要下载
- 确保飞书应用具备发送消息的权限

## Python API

```python
from skills.feishu_voice_sender import send_voice_message

# 发送到群聊
result = send_voice_message(
    audio_path="/tmp/voice.mp3",
    target_id="oc_xxx",
    target_type="chat"
)

# 发送到私聊
result = send_voice_message(
    audio_path="/tmp/voice.mp3",
    target_id="ou_xxx",
    target_type="user"
)
```

## Voice vs File

| 方式 | 消息类型 | 用户体验 |
|------|----------|----------|
| 语音条 | `msg_type: "voice"` | ✅ 点击播放，类似微信语音 |
| 音频文件 | `msg_type: "file"` | ❌ 下载后播放 |

## Related Skills

- [feishu-video-sender](../feishu-video-sender/) - 发送飞书视频消息（带播放器）
- [feishu-group-welcome](../feishu-group-welcome/) - 群聊欢迎消息管理

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
