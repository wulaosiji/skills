---
name: email-sender
description: |
  邮件发送工具，支持HTML模板邮件发送。用于发送格式化的邮件通知、报告等。
  
  特性：
  - 支持纯文本和HTML邮件
  - 内置科技感邮件模板
  - 支持附件发送
  - 自动处理VPN网络环境警告
---

# Email Sender Skill

邮件发送统一封装，支持HTML模板和纯文本。

## 邮件发送规则（2026-03-04 更新）

### 强制规范

**所有邮件必须遵循以下规则：**

1. **必须使用模板** - 不允许纯文本邮件
   - 白天 (6:00-18:00) → 使用浅色主题 `send_light_email()`
   - 晚上 (18:00-6:00) → 使用深色主题 `send_tech_email()`

2. **必须包含广告** - 默认添加杭州大会广告
   - 除非明确指定 `include_ad=False`
   - 广告位置：邮件内容底部

### 智能时间判断函数

```python
from email_sender import send_smart_email

# 自动根据当前时间选择主题（白天浅色/晚上深色）+ 默认广告
send_smart_email(
    to_email='user@example.com',
    subject='AI日报',
    title='今日热点',
    content='<p>内容...</p>'
)
```

### 手动指定主题

```python
# 强制使用深色（晚上）
send_tech_email(
    to_email='user@example.com',
    subject='晚间报告',
    title='今日回顾',
    content='...',
    # 自动包含广告
)

# 强制使用浅色（白天）
send_light_email(
    to_email='user@example.com',
    subject='早报',
    title='今日热点',
    content='...',
    # 自动包含广告
)
```

### 例外情况

如需无广告或纯文本，必须显式声明：

```python
# 无广告
send_tech_email(
    ...,
    include_ad=False  # 明确去掉广告
)

# 纯文本（不推荐）
send_email(
    to_email='user@example.com',
    subject='纯文本',
    body='内容...'
)
```

---

```python
from skills.email_sender.email_sender import send_email, send_html_email, send_tech_email

# 发送纯文本邮件
send_email(
    to_email="recipient@example.com",
    subject="测试邮件",
    body="这是一封测试邮件"
)

# 发送HTML邮件
send_html_email(
    to_email="recipient@example.com",
    subject="HTML邮件",
    html_body="<h1>标题</h1><p>内容</p>"
)

# 使用科技感模板发送
send_tech_email(
    to_email="recipient@example.com",
    subject="AI日报",
    title="今日AI热点",
    content="邮件正文内容...",
    highlights=["亮点1", "亮点2", "亮点3"]
)
```

## 功能特性

### 1. 纯文本邮件
```python
from skills.email_sender.email_sender import send_email

send_email(
    to_email="recipient@example.com",
    subject="主题",
    body="正文内容",
    from_email="zhuoran@100aiapps.cn",  # 可选，默认从.env读取
    password="your_password"  # 可选，默认从.env读取
)
```

### 2. HTML邮件
```python
from skills.email_sender.email_sender import send_html_email

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
    </style>
</head>
<body>
    <h1>标题</h1>
    <p>内容</p>
</body>
</html>
"""

send_html_email(
    to_email="recipient@example.com",
    subject="HTML邮件",
    html_body=html_content
)
```

### 3. 科技感模板邮件
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

### 4. 带附件邮件
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

## 配置信息

**SMTP配置**（自动从`~/.openclaw/.env`读取）：
- 服务器: `smtp.feishu.cn:465`
- 用户名: `zhuoran@100aiapps.cn`
- 密码: `FEISHU_SMTP_PASSWORD`

## 网络环境注意事项

⚠️ **重要**：使用邮件功能时请保持**国内网络环境**

- ✅ 国内直连：SMTP连接正常
- ❌ VPN/代理：SSL握手会被飞书服务器拒绝

**错误特征**：
```
SSL: UNEXPECTED_EOF_WHILE_READING
EOF occurred in violation of protocol
```

**解决方案**：关闭VPN，切换国内网络后重试。

## 科技感邮件模板

内置模板特点：
- 深色科技感背景
- 渐变色彩设计
- 响应式布局
- 支持高亮数据卡片
- 移动端适配

### 模板颜色方案
| 元素 | 颜色 |
|------|------|
| 主背景 | `#0a0a0f` (深空黑) |
| 卡片背景 | `#12121a` |
| 主色调 | `#00d4ff` (科技蓝) |
| 强调色 | `#ff6b35` (活力橙) |
| 文字 | `#e6e6e6` |
| 次要文字 | `#888888` |

### 模板结构
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <style>
        /* 科技感样式 */
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{title}}</h1>
            <p class="subtitle">{{subtitle}}</p>
        </div>
        <div class="content">
            {{content}}
        </div>
        <div class="highlights">
            {{highlights}}
        </div>
        <div class="footer">
            {{footer}}
        </div>
    </div>
</body>
</html>
```

## 完整示例

### 发送AI日报
```python
from skills.email_sender.email_sender import send_tech_email

send_tech_email(
    to_email="team@100aiapps.cn",
    subject="🦞 卓然AI早报 | 2026-03-04",
    title="今日AI热点",
    subtitle="2026年3月4日 周三",
    content="""
    <h2>🔥 头条新闻</h2>
    <p>Claude登顶美区App Store榜首，用户发起"ChatGPT解约运动"...</p>
    
    <h2>💡 关键洞察</h2>
    <p>美国AI军事化正在撕裂硅谷...</p>
    """,
    highlights=[
        {"label": "政策", "value": "AI军事化加速"},
        {"label": "市场", "value": "Claude登顶榜首"},
        {"label": "数据", "value": "卸载量+295%"}
    ],
    footer="非凡产研 | 让AI更有价值"
)
```

### 发送会议邀请
```python
from skills.email_sender.email_sender import send_tech_email

send_tech_email(
    to_email="guest@example.com",
    subject="会议邀请：AI产品策略讨论",
    title="📅 会议邀请",
    subtitle="非凡产研 · 战略会议",
    content="""
    <p>您好，诚邀您参加AI产品策略讨论会。</p>
    
    <div class="info-box">
        <p><strong>时间：</strong>2026年3月5日 14:00</p>
        <p><strong>地点：</strong>飞书会议</p>
        <p><strong>议题：</strong>Q2产品规划</p>
    </div>
    """,
    highlights=[
        {"label": "会议ID", "value": "123-456-789"},
        {"label": "密码", "value": "8888"}
    ],
    footer="非凡产研 | 战略部"
)
```

## 依赖

- Python 3.7+
- 无需额外依赖（使用标准库）

## 更新日志

- **2026-03-04**: 初始版本，封装邮件发送功能，添加科技感HTML模板

---

*邮件配置存储于 `~/.openclaw/.env`*
*网络环境要求：国内直连（VPN会导致连接失败）*
