---
name: feishu-voice-sender
description: |
  飞书语音消息发送工具 / Feishu voice message sender. 将 MP3 音频文件以语音条形式发送到飞书私聊或群聊（非文件附件），用户点击直接播放。
  Use when: "发送语音消息", "send voice message", "飞书语音条", "feishu voice clip", "MP3转飞书语音", "mp3 to feishu voice", "群发语音", "broadcast voice message", "语音通知", "voice notification".
  将 MP3 转换为 AMR 格式后上传，使用 msg_type: voice 发送，支持群聊和私聊。Cross-references: feishu-video-sender, feishu-group-welcome, feishu-message-recall.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Voice Sender

> 飞书语音消息发送工具——将 MP3 音频以语音条形式发送到飞书聊天（非文件附件），用户点击直接播放。

## When to Use

Use this skill when:
- 需要将 MP3 音频以语音条（非文件附件）形式发送到飞书时
- 需要向群聊或私聊发送语音通知时
- 希望用户体验类似微信语音（点击直接播放）时
- 需要配合自动化流程发送语音消息时

Do NOT use this skill if:
- 需要发送视频消息 → use `feishu-video-sender` instead
- 需要发送普通文本或富文本消息 → use `feishu-group-welcome` or standard message tool instead
- 需要发送音频文件（让用户下载后播放）→ 直接使用 file 消息类型 instead

Typical triggers:
- 「发送一条语音到群里」「把这段音频转成飞书语音条」
- "Send this MP3 as a voice message in Feishu", "群发语音通知"

## Workflow

1. **探查 (Probe)**
确认音频文件路径（MP3）、目标 ID（群 ID `oc_xxx` 或用户 ID `ou_xxx`）、发送类型（chat/user）。

2. **约束 (Constrain)**
确认系统已安装 `ffmpeg`，Python 已安装 `requests`。确保飞书应用具备发送消息的权限。语音消息与音频文件的区别在于 `msg_type`：`voice` 直接播放，`file` 需要下载。不降级——ffmpeg 缺失时停止并提示安装。

3. **证据 (Evidence)**
确认 MP3 文件存在且可读，目标 ID 格式正确。

4. **执行 (Execute)**
1. MP3 → AMR（飞书语音格式）转换
2. 上传音频到飞书获取 `file_key`
3. 使用 `msg_type: "voice"` 发送

```bash
# 发送到群聊
python3 skills/feishu-voice-sender/feishu_voice_sender.py /tmp/voice.mp3 oc_xxx --chat

# 发送到私聊
python3 skills/feishu-voice-sender/feishu_voice_sender.py /tmp/voice.mp3 ou_xxx --user
```

5. **验证 (Verify)**
确认消息发送成功，返回消息 ID 和发送状态。

6. **交付 (Deliver)**
返回消息发送结果，清理临时文件（转换后的 AMR 文件）。

## Output

返回消息发送结果，包含消息 ID、目标 ID、发送状态和 file_key。

## Guardrails

**Anti-patterns**
- NEVER 使用 `msg_type: "file"` 发送语音（用户需要下载后播放，体验差）
- Do NOT 在未安装 ffmpeg 的情况下尝试转换格式
- Do NOT 发送超过飞书语音时长限制的音频

**Constraints**
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

- **feishu-video-sender** — 发送飞书视频消息（带播放器）
- **feishu-group-welcome** — 群聊欢迎消息管理
- **feishu-message-recall** — 撤回已发送的消息

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
