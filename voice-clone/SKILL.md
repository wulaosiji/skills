---
name: voice-clone
description: |
  Voice cloning and synthesis skill using WaveSpeed AI MiniMax Voice Clone API.
  Create custom voices from 5-20 second audio samples and generate speech.
  Supports Wu Na and other specific character voices with high-quality synthesis.
  Use when: "语音克隆", "声音克隆", "AI语音合成", "克隆声音", "语音生成", "文字转语音", "voice cloning", "AI speech", "clone voice", "text to speech".
  Cross-references: whisper-stt, media-hub, video-generation.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# 声音克隆技能 (Voice Clone)

> 使用 WaveSpeed AI 的 MiniMax Voice Clone 服务进行声音克隆和语音合成。

## When to Use

Use this skill when:
- 需要克隆特定人物的声音
- 使用克隆声音生成口播内容
- 创建个性化的语音助手
- 批量生成配音内容
- 与 STT 结合实现语音交互

Do NOT use this skill if:
- 音频样本质量差（有噪音、背景音乐、多人声）
- 样本时长不在 5-20 秒范围内
- 需要实时语音合成（有一定延迟）
- 涉及版权或隐私问题的声音克隆
- 需要极高精度的情感控制（当前 API 不直接支持）

Typical triggers:
- 「语音克隆」「声音克隆」「AI语音合成」「克隆声音」「语音生成」「文字转语音」
- "voice cloning", "voice clone", "AI voice synthesis", "clone voice", "voice generation", "text to speech", "MiniMax voice"

## Workflow

1. **探查 (Probe)**: 完整读取需求，确认是克隆新声音还是使用已有 voice_id 生成语音，确认目标文本、语言和输出要求。

2. **约束 (Constrain)**: 验证音频样本质量（5-20秒、清晰无杂音、单人声），设定边界：voice_id 需7天内至少使用一次否则过期。不降级交付物。

3. **证据 (Evidence)**: 每个模型的特点和延迟来自 MiniMax API 官方规格。音频样本质量直接决定克隆效果，10秒高质量样本优于1分钟低质量样本。

4. **执行 (Execute)**: 调用 WaveSpeed AI API 克隆声音或生成语音，先给影响与结论，再给行动和必要证据。

**克隆声音（首次使用）**

```python
def clone_voice(audio_path, voice_id, text="我是克隆的声音，很高兴为你服务。"):
    import requests, base64
    WAVESPEED_KEY = "your_api_key"
    BASE_URL = "https://api.wavespeed.ai/api/v3"
    HEADERS = {"Authorization": f"Bearer {WAVESPEED_KEY}"}
    JSON_HEADERS = {**HEADERS, "Content-Type": "application/json"}
    with open(audio_path, 'rb') as f:
        audio_base64 = base64.b64encode(f.read()).decode('utf-8')
    url = f"{BASE_URL}/minimax/voice-clone"
    payload = {"model": "speech-02-hd", "custom_voice_id": voice_id, "text": text,
               "audio": audio_base64, "need_noise_reduction": False,
               "need_volume_normalization": False, "accuracy": 0.8}
    response = requests.post(url, json=payload, headers=JSON_HEADERS)
    result = response.json()
    if response.status_code == 200:
        return result['data']['id']
    else:
        raise Exception(f"克隆失败: {result}")
```

**使用克隆的声音生成语音**

```python
def generate_speech(text, voice_id, model="speech-02-hd"):
    url = f"{BASE_URL}/minimax/{model}"
    payload = {"text": text, "voice_id": voice_id, "language": "zh-CN"}
    response = requests.post(url, json=payload, headers=JSON_HEADERS)
    result = response.json()
    if response.status_code == 200:
        return result['data']['id'], result['data']['urls']['get']
    else:
        raise Exception(f"生成失败: {result}")
```

**查询任务结果**

```python
def poll_result(request_id, timeout=60):
    import time
    url = f"{BASE_URL}/predictions/{request_id}/result"
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(url, headers=HEADERS)
        result = response.json()
        status = result.get('data', {}).get('status')
        if status == 'completed':
            outputs = result.get('data', {}).get('outputs', [])
            return outputs[0] if outputs else None
        elif status == 'failed':
            raise Exception(f"任务失败: {result}")
        time.sleep(3)
    raise TimeoutError("任务超时")
```

**完整使用示例**

```python
AUDIO_SAMPLE = "/path/to/sample.mp3"
VOICE_ID = "wuna-001"
KOUBO_TEXT = "我是外企面试官。2026年求职，你一定要学会用人工智能！"
clone_request_id = clone_voice(AUDIO_SAMPLE, VOICE_ID)
time.sleep(5)
tts_request_id, result_url = generate_speech(KOUBO_TEXT, VOICE_ID)
audio_url = poll_result(tts_request_id)
```

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——播放生成的音频，检查声音相似度、发音清晰度和情感自然度，确认无明显杂音。

6. **交付 (Deliver)**: 返回音频文件 URL 或本地路径，提示用户 voice_id 7天内需使用一次，清理临时文件。

## Supported Models

**声音克隆**: 端点 `POST /api/v3/minimax/voice-clone`，定价 $0.5/次。

**语音合成**:

| 模型 | 特点 | 延迟 |
|------|------|------|
| `speech-02-hd` | 高清音质 | 中等 |
| `speech-02-turbo` | 低延迟 | 低 |
| `speech-2.6-hd` | 下一代高清，40+语言 | 中等 |
| `speech-2.6-turbo` | 超低延迟 | 极低 |

## Output

- 格式: MP3 / WAV（由 API 返回）
- 音质: 高清（speech-02-hd）或低延迟（speech-02-turbo）
- 语言: 中文（zh-CN）及 40+ 语言
- 返回: 音频下载 URL，可下载到本地

## Guardrails

**Anti-patterns:**
- NEVER 使用质量差的音频样本（有噪音、背景音乐、多人声）
- NEVER 使用不在 5-20 秒范围内的样本
- NEVER 克隆涉及版权或隐私问题的声音
- NEVER 期望极高精度的情感控制（当前 API 不直接支持）
- Do NOT 创建 voice_id 后不测试（7天不使用会过期）

**音频样本要求**
- 格式: MP3、WAV
- 时长: 5-20秒最佳
- 大小: 建议不超过 1MB
- 质量: 清晰无杂音、无背景音乐、单人声、正常语速

**已配置的声音**

| 声音ID | 来源 | 状态 | 说明 |
|--------|------|------|------|
| `wuna-001` | 吴娜短视频样例 | ✅ 可用 | 温柔知性带干练职业风格 |
| `zhuoran-001` | 卓然 | ✅ 可用 | 专业干练风格 |

**最佳实践**
1. 音频样本质量: 高质量的 10 秒样本比低质量的 1 分钟样本效果更好
2. 唯一 Voice ID: 使用有意义的命名
3. 及时使用: 创建 voice_id 后立即测试生成一次，避免过期
4. 批量生成: 先测试单条，效果满意后再批量
5. 备份音频: 保存好原始音频样本，voice_id 过期后可重新克隆

**常见问题**

| 问题 | 答案 |
|------|------|
| Voice ID 会过期吗？ | 会。需在 7 天内至少使用一次，否则会被删除。 |
| 可以克隆多个人的声音吗？ | 可以。每个声音使用不同的 `custom_voice_id`。 |
| 中文效果怎么样？ | 效果非常好，支持标准普通话，发音清晰自然。 |
| 可以控制语速和情感吗？ | 当前 API 不直接支持，可通过标点符号和文本结构调整节奏。 |

## Project Scripts

| 脚本 | 功能 |
|------|------|
| `clone_voice.py` | 克隆声音样本 |
| `generate_speech.py` | 使用克隆声音生成语音 |
| `batch_generate.py` | 批量生成口播音频 |

## Related Skills

- **whisper-stt** — 语音转文字，可形成完整语音工作流（语音→文字→AI→语音）
- **media-hub** — 统一媒体处理中心，支持音频格式转换和批量处理
- **video-generation** — 可为生成的视频添加克隆语音配音

## About UniqueClub

Part of UniqueClub toolkit - AI-powered creative tools for voice synthesis and cloning.
🌐 https://uniqueclub.ai
