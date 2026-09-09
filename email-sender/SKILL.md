---
name: email-sender
description: |
  邮件发送统一封装工具，支持HTML模板邮件（科技感深色/浅色主题自动切换）、纯文本邮件、附件发送、营销邮件和系统通知，内置飞书SMTP配置。
  Use when: "发送邮件", "发封报告邮件", "HTML邮件", "send email", "email report", "带附件的邮件", "HTML email template", "日报邮件".
  强制使用模板（白天浅色/晚上深色），默认包含广告，支持高亮数据卡片和自定义页脚。Cross-references: document-hub, pdf, rss-feed, daily-report.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Email Sender Skill

> 邮件发送统一封装，支持HTML模板和纯文本，内置科技感深色/浅色主题。

## When to Use

Use this skill when:
- 需要发送格式化的HTML邮件
- 发送带有品牌样式的营销邮件
- 附件发送（报告、数据文件等）
- 根据时间自动切换邮件主题（白天浅色/晚上深色）
- 发送系统通知或日报/周报
- 需要科技感设计风格的邮件

Do NOT use this skill if:
- 需要发送大量邮件（可能触发SMTP限制）→ 分批发送或使用专业邮件服务
- 收件人邮箱服务器有严格过滤 → 确认收件地址有效性
- 网络环境使用VPN/代理（会导致SSL错误）→ 切换国内网络
- 需要复杂的邮件模板定制（超出内置模板）

Typical triggers:
- 「发送邮件」「发封报告邮件」「HTML邮件」
- "Send email", "Email report", "HTML email template"
- 「科技感邮件模板」「带附件的邮件」「日报邮件」
- "Send with attachment", "Daily report email", "Tech-style email"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认邮件类型、收件人、主题和内容。检查网络环境（必须国内直连，VPN会导致SSL错误）。

2. **约束 (Constrain)**
根据当前时间选择邮件主题，设定不可降级的标准——必须使用模板（不允许纯文本邮件）。受阻时换通道，不降级交付物。

| 函数 | 场景 | 特点 |
|------|------|------|
| `send_smart_email()` | 通用 | 自动根据时间选主题 |
| `send_tech_email()` | 晚上/深色 | 科技感深色主题 |
| `send_light_email()` | 白天/浅色 | 清爽浅色主题 |
| `send_email()` | 简单 | 纯文本（不推荐） |
| `send_email_with_attachments()` | 附件 | 带文件 |

配置邮件参数：
```python
required_params = {
    "to_email": "recipient@example.com",
    "subject": "邮件主题",
    "title": "邮件标题",        # HTML模板用
    "content": "邮件正文",       # HTML模板用
}
```

3. **证据 (Evidence)**
邮件内容必须来自用户输入或可追溯数据源，不编造报告内容。每个数据点必须有明确来源。

4. **执行 (Execute)**
调用邮件发送函数，先给影响与结论，再给行动和必要证据。
```python
from skills.email_sender.email_sender import send_smart_email

send_smart_email(
    to_email='user@example.com',
    subject='AI日报',
    title='今日热点',
    content='<p>内容...</p>'
)
```

处理异常：
- 捕获网络错误
- 处理SMTP认证失败
- 记录发送日志

5. **验证 (Verify)**
用不同于生成路径的方式回读——检查发送返回状态为成功，确认收件人地址格式正确，验证附件文件存在且可读。如遇SSL错误，确认已关闭VPN。

6. **交付 (Deliver)**
返回邮件发送成功/失败状态，清理临时附件文件（如需要）。记录发送日志。

## Output

返回邮件发送结果：
- 成功：返回收件人、主题和发送时间
- 失败：返回错误类型和建议解决方案（如SSL错误→关闭VPN，认证失败→检查SMTP密码）

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 使用纯文本邮件——必须使用HTML模板
- NEVER 在VPN/代理环境下发送（会导致SSL握手被飞书服务器拒绝）
- Do NOT 发送大量邮件（可能触发SMTP频率限制）
- Do NOT 不处理发送失败的情况

**Email Sending Rules (Updated 2026-03-04)**

**强制规范:**

1. **必须使用模板** - 不允许纯文本邮件
   - 白天 (6:00-18:00) → 使用浅色主题 `send_light_email()`
   - 晚上 (18:00-6:00) → 使用深色主题 `send_tech_email()`

2. **默认包含广告** - 默认添加杭州大会广告
   - 除非明确指定 `include_ad=False`
   - 广告位置：邮件内容底部

**Network Environment**
⚠️ **重要**: 使用邮件功能时请保持**国内网络环境**

- ✅ 国内直连: SMTP连接正常
- ❌ VPN/代理: SSL握手会被飞书服务器拒绝

**错误特征**:
```
SSL: UNEXPECTED_EOF_WHILE_READING
EOF occurred in violation of protocol
```

**解决方案**: 关闭VPN，切换国内网络后重试。

**Constraints**
- 依赖飞书SMTP服务器（smtp.feishu.cn:465）
- 单账户有发送频率限制
- 附件大小限制（通常25MB）
- 不支持邮件追踪功能

## Core Features

**1. 智能主题选择**
```python
from skills.email_sender.email_sender import send_smart_email

# 自动根据当前时间选择主题（白天浅色/晚上深色）+ 默认广告
send_smart_email(
    to_email='user@example.com',
    subject='AI日报',
    title='今日热点',
    content='<p>内容...</p>'
)
```

**2. 深色科技感模板**
```python
from skills.email_sender.email_sender import send_tech_email

send_tech_email(
    to_email="recipient@example.com",
    subject="非凡产研 - AI日报",
    title="🦞 今日AI热点",
    subtitle="2026年3月4日",
    content="""
    <p>今日AI领域发生重大事件...</p>
    <h3>关键洞察</h3>
    <ul>
        <li>Anthropic事件持续发酵</li>
        <li>Claude登顶App Store</li>
    </ul>
    """,
    highlights=[
        {"label": "政策风向", "value": "AI军事化加速"},
        {"label": "资本流向", "value": "基础设施增长"},
        {"label": "用户态度", "value": "卸载量激增295%"}
    ],
    footer="非凡产研 | 连接技术与商业"
)
```

**3. 浅色主题模板**
```python
from skills.email_sender.email_sender import send_light_email

send_light_email(
    to_email="recipient@example.com",
    subject='早报',
    title='今日热点',
    content='...',
    # 自动包含广告
)
```

**4. 带附件邮件**
```python
from skills.email_sender.email_sender import send_email_with_attachments

send_email_with_attachments(
    to_email="recipient@example.com",
    subject="带附件的邮件",
    body="请查收附件",
    attachments=[
        ("report.pdf", "/path/to/report.pdf"),
        ("data.xlsx", "/path/to/data.xlsx")
    ]
)
```

**5. 纯文本邮件（不推荐）**
```python
from skills.email_sender.email_sender import send_email

send_email(
    to_email="recipient@example.com",
    subject="测试邮件",
    body="这是一封测试邮件"
)
```

## Template Color Scheme

| 元素 | 深色主题 | 浅色主题 |
|------|----------|----------|
| 主背景 | `#0a0a0f` | `#ffffff` |
| 卡片背景 | `#12121a` | `#f5f5f5` |
| 主色调 | `#00d4ff` | `#0066cc` |
| 强调色 | `#ff6b35` | `#ff6b35` |
| 文字 | `#e6e6e6` | `#1a1a1a` |
| 次要文字 | `#888888` | `#666666` |

## Configuration

**SMTP配置**（自动从`~/.openclaw/.env`读取）：
- 服务器: `smtp.feishu.cn:465`
- 用户名: `zhuoran@100aiapps.cn`
- 密码: `FEISHU_SMTP_PASSWORD`

## Workflow Integration

**Workflow: 生成报告 → 发送邮件**
```python
from skills.long_form_writer import generate_report
from skills.email_sender.email_sender import send_tech_email

# 生成长文报告
report = generate_report(data, template="daily")

# 发送邮件
send_tech_email(
    to_email="team@example.com",
    subject="🦞 卓然AI日报",
    title="今日AI热点",
    content=report.html_content,
    highlights=report.key_insights
)
```

**Workflow: 生成PDF → 邮件附件**
```python
from skills.document_hub.document_hub import write
from skills.email_sender.email_sender import send_email_with_attachments

# 生成报告文档
write("report.docx", content)

# 发送带附件邮件
send_email_with_attachments(
    to_email="client@example.com",
    subject="月度报告",
    body="请查收附件中的月度报告",
    attachments=[("月度报告.docx", "./report.docx")]
)
```

## Dependencies

- Python 3.7+
- 无需额外依赖（使用标准库 smtplib）

## Changelog

- **2026-03-04**: 初始版本，封装邮件发送功能，添加科技感HTML模板

## Related Skills

- **document-hub** — 附件来源：生成Word/Excel附件
- **pdf** — 附件来源：生成PDF报告附件
- **rss-feed** — 数据来源：RSS内容作为邮件素材
- **daily-report** — 内容生成：日报内容直接作为邮件正文

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
