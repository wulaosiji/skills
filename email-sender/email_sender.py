#!/usr/bin/env python3
"""
邮件发送工具 - 使用飞书SMTP
支持HTML模板和纯文本邮件
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from pathlib import Path
from typing import List, Dict, Optional, Union


def load_env_file():
    """加载 .env 文件"""
    env_paths = [
        Path.home() / ".openclaw" / ".env",
        Path.home() / ".openclaw" / "config" / "main.env",
        Path("/Users/delta/.openclaw/.env"),
    ]
    
    for env_path in env_paths:
        if env_path.exists():
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip().strip('"\'')
                        if key not in os.environ:
                            os.environ[key] = value
            return True
    return False


# 加载环境变量
load_env_file()

# SMTP 配置（优先从环境变量读取）
SMTP_SERVER = os.getenv('FEISHU_SMTP_SERVER', 'smtp.feishu.cn')
SMTP_PORT = int(os.getenv('FEISHU_SMTP_PORT', '465'))
SENDER_EMAIL = os.getenv('FEISHU_SMTP_USER', 'zhuoran@100aiapps.cn')


# 大会活动广告HTML模板
EVENT_AD_TEMPLATE = """
<div style="
    background: linear-gradient(135deg, #ff6b35 0%, #ff8c42 50%, #ffa94d 100%);
    border-radius: 12px;
    padding: 25px;
    margin: 25px 0;
    text-align: center;
    box-shadow: 0 8px 30px rgba(255, 107, 53, 0.3);
">
    <div style="font-size: 32px; margin-bottom: 10px;">🎉</div>
    <h3 style="
        color: #ffffff;
        font-size: 20px;
        margin: 0 0 12px 0;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    ">{title}</h3>
    <p style="
        color: rgba(255,255,255,0.95);
        font-size: 15px;
        margin: 0 0 18px 0;
        line-height: 1.6;
    ">{description}</p>
    <div style="
        background: rgba(255,255,255,0.2);
        border-radius: 8px;
        padding: 12px;
        margin: 15px 0;
    ">
        <p style="
            color: #ffffff;
            font-size: 14px;
            margin: 0;
            font-weight: 600;
        ">📅 {date} | 📍 {location}</p>
    </div>
    <a href="{link}" style="
        display: inline-block;
        background: #ffffff;
        color: #ff6b35;
        text-decoration: none;
        padding: 14px 32px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s;
    ">立即报名 →</a>
</div>
"""

# 杭州大会默认广告
HANGZHOU_EVENT_AD = {
    "title": "2026非凡大赏·杭州AI周",
    "description": "3月24-29日，与1000+AI决策者共聚杭州！Minimax、智谱、Kimi等头部企业高管亲临，探讨AI产业前沿趋势。",
    "date": "2026年3月24-29日",
    "location": "杭州",
    "link": "https://uniquecapital.feishu.cn/share/base/form/shrcnO3fS0Se6ThIvbcYhLgM7Dd?from=navigation"
}


def send_email(
    to_email: str,
    subject: str,
    body: str,
    from_email: Optional[str] = None,
    password: Optional[str] = None,
    smtp_server: Optional[str] = None,
    smtp_port: Optional[int] = None
) -> dict:
    """
    发送邮件（强制使用模板+广告+教程）
    
    注意：此函数不再支持纯文本，自动转为模板邮件
    根据当前时间自动选择浅色/深色主题
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        body: 邮件正文（会自动包装为模板格式）
        from_email: 发件人邮箱（可选）
        password: 邮箱密码（可选）
        smtp_server: SMTP服务器（可选）
        smtp_port: SMTP端口（可选）
    
    Returns:
        dict: {'success': bool, 'message': str}
    """
    # 将纯文本转为HTML格式
    html_content = f"<p>{body.replace(chr(10), '</p><p>')}</p>"
    
    # 使用智能发送（自动选主题+广告+教程）
    return send_smart_email(
        to_email=to_email,
        subject=subject,
        title=subject,  # 使用主题作为标题
        content=html_content,
        from_email=from_email,
        password=password
    )


def send_html_email(
    to_email: str,
    subject: str,
    html_body: str,
    from_email: Optional[str] = None,
    password: Optional[str] = None,
    smtp_server: Optional[str] = None,
    smtp_port: Optional[int] = None
) -> dict:
    """
    发送HTML邮件
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        html_body: HTML格式的邮件正文
        from_email: 发件人邮箱（可选）
        password: 邮箱密码（可选）
        smtp_server: SMTP服务器（可选）
        smtp_port: SMTP端口（可选）
    
    Returns:
        dict: {'success': bool, 'message': str}
    """
    sender = from_email or SENDER_EMAIL
    pwd = password or os.getenv('FEISHU_SMTP_PASSWORD')
    server = smtp_server or SMTP_SERVER
    port = smtp_port or SMTP_PORT
    
    if not pwd:
        return {'success': False, 'message': '未配置邮箱密码，请设置 FEISHU_SMTP_PASSWORD'}
    
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = sender
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(server, port, context=context) as s:
            s.login(sender, pwd)
            s.send_message(msg)
        
        return {'success': True, 'message': f'HTML邮件已发送至 {to_email}'}
    except Exception as e:
        error_msg = str(e)
        if 'UNEXPECTED_EOF' in error_msg or 'violation of protocol' in error_msg:
            return {
                'success': False, 
                'message': 'SSL连接失败。请检查网络环境：关闭VPN，使用国内直连网络。'
            }
        return {'success': False, 'message': f'发送失败: {error_msg}'}


# 科技感邮件模板 - 深色主题
TECH_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{title}</title>
    <style>
        body, table, td, p, h1, h2, h3, h4, h5, h6 {{
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}
        
        .email-wrapper {{
            background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        
        .email-container {{
            max-width: 600px;
            margin: 0 auto;
            background: rgba(18, 18, 26, 0.95);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 
                        0 0 0 1px rgba(0, 212, 255, 0.1);
        }}
        
        .header {{
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 212, 255, 0.05) 100%);
            padding: 40px 30px;
            text-align: center;
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
            position: relative;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #ff6b35, #00d4ff);
            background-size: 200% 100%;
            animation: shimmer 3s infinite;
        }}
        
        @keyframes shimmer {{
            0% {{ background-position: -200% 0; }}
            100% {{ background-position: 200% 0; }}
        }}
        
        .header h1 {{
            color: #ffffff;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        }}
        
        .subtitle {{
            color: #00d4ff;
            font-size: 14px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        
        .logo {{
            font-size: 48px;
            margin-bottom: 15px;
        }}
        
        .content {{
            padding: 30px;
            color: #e6e6e6;
            line-height: 1.8;
            font-size: 15px;
        }}
        
        .content h2 {{
            color: #ffffff;
            font-size: 20px;
            margin: 25px 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
        }}
        
        .content h3 {{
            color: #00d4ff;
            font-size: 16px;
            margin: 20px 0 10px 0;
        }}
        
        .content p {{
            margin-bottom: 15px;
        }}
        
        .content ul, .content ol {{
            margin: 15px 0;
            padding-left: 25px;
        }}
        
        .content li {{
            margin-bottom: 8px;
        }}
        
        .info-box {{
            background: rgba(0, 212, 255, 0.05);
            border-left: 4px solid #00d4ff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }}
        
        .highlights {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            padding: 0 30px 30px 30px;
            justify-content: center;
        }}
        
        .highlight-card {{
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 212, 255, 0.05) 100%);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 12px;
            padding: 20px;
            min-width: 150px;
            text-align: center;
            flex: 1;
        }}
        
        .highlight-label {{
            color: #888888;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}
        
        .highlight-value {{
            color: #00d4ff;
            font-size: 18px;
            font-weight: 700;
        }}
        
        .footer {{
            background: rgba(10, 10, 15, 0.8);
            padding: 25px 30px;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .footer-text {{
            color: #666666;
            font-size: 13px;
            margin-bottom: 10px;
        }}
        
        .footer-brand {{
            color: #00d4ff;
            font-weight: 600;
            font-size: 14px;
        }}
        
        .social-links {{
            margin-top: 15px;
        }}
        
        .social-links a {{
            color: #888888;
            text-decoration: none;
            margin: 0 10px;
            font-size: 12px;
        }}
        
        @media (max-width: 600px) {{
            .email-wrapper {{ padding: 20px 10px; }}
            .header {{ padding: 30px 20px; }}
            .header h1 {{ font-size: 24px; }}
            .content {{ padding: 20px; }}
            .highlights {{ flex-direction: column; padding: 0 20px 20px 20px; }}
        }}
    </style>
</head>
<body>
    <div class="email-wrapper">
        <div class="email-container">
            <div class="header">
                <div class="logo">🦞</div>
                <h1>{title}</h1>
                <p class="subtitle">{subtitle}</p>
            </div>
            <div class="content">
                {content}
            </div>
            {highlights_section}
            <div class="footer">
                <p class="footer-text">{footer}</p>
                <p class="footer-brand">非凡产研 🦞 OpenClaw</p>
                <div class="social-links">
                    <a href="https://ffcap.cn">官网</a> |
                    <a href="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=177le97c-ca50-4b90-b660-cd05a994849d">飞书群</a> |
                    <a href="https://github.com/wulaosiji/skills">GitHub</a>
                </div>
                <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
                    <p style="color: #888888; font-size: 12px; margin-bottom: 10px;">📚 想了解更多？查看我们的开源教程：</p>
                    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px;">
                        <a href="https://uniquecapital.feishu.cn/wiki/Uqsqwoug5iYca3koiAQcUaEqnOf" style="color: #00d4ff; text-decoration: none; font-size: 12px;">01-入门教程</a>
                        <a href="https://uniquecapital.feishu.cn/wiki/HJm5wmIl7iDS2Hkp5CXcvbHnntg" style="color: #00d4ff; text-decoration: none; font-size: 12px;">02-技能教程</a>
                        <a href="https://uniquecapital.feishu.cn/wiki/RDgdweb14i1IcOkHHqlc42HQnKe" style="color: #00d4ff; text-decoration: none; font-size: 12px;">03-人设教程</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""


def send_tech_email(
    to_email: str,
    subject: str,
    title: str,
    content: str,
    subtitle: str = "",
    highlights: Optional[List[Dict[str, str]]] = None,
    footer: str = "非凡产研 | 让AI更有价值",
    include_ad: bool = True,
    ad_config: Optional[Dict[str, str]] = None,
    from_email: Optional[str] = None,
    password: Optional[str] = None
) -> dict:
    """
    使用科技感模板发送邮件（深色主题）
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        title: 邮件标题
        content: HTML内容
        subtitle: 副标题
        highlights: 高亮数据
        footer: 页脚文字
        include_ad: 是否包含广告（默认True）
        ad_config: 自定义广告配置（默认使用杭州大会）
        from_email: 发件人邮箱
        password: 密码
    """
    # 添加广告
    if include_ad:
        if ad_config is None:
            ad_config = HANGZHOU_EVENT_AD
        ad_html = EVENT_AD_TEMPLATE.format(**ad_config)
        full_content = content + ad_html
    else:
        full_content = content
    
    highlights_html = ""
    if highlights:
        cards = []
        for item in highlights:
            label = item.get('label', '')
            value = item.get('value', '')
            cards.append(f'''
            <div class="highlight-card">
                <div class="highlight-label">{label}</div>
                <div class="highlight-value">{value}</div>
            </div>
            ''')
        highlights_html = '<div class="highlights">' + ''.join(cards) + '</div>'
    
    html_body = TECH_EMAIL_TEMPLATE.format(
        title=title,
        subtitle=subtitle,
        content=full_content,
        highlights_section=highlights_html,
        footer=footer
    )
    
    return send_html_email(to_email, subject, html_body, from_email, password)


def send_email_with_attachments(
    to_email: str,
    subject: str,
    body: str,
    attachments: List[tuple],
    is_html: bool = False,
    from_email: Optional[str] = None,
    password: Optional[str] = None
) -> dict:
    """发送带附件的邮件"""
    sender = from_email or SENDER_EMAIL
    pwd = password or os.getenv('FEISHU_SMTP_PASSWORD')
    
    if not pwd:
        return {'success': False, 'message': '未配置邮箱密码，请设置 FEISHU_SMTP_PASSWORD'}
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to_email
        msg['Subject'] = subject
        
        content_type = 'html' if is_html else 'plain'
        msg.attach(MIMEText(body, content_type, 'utf-8'))
        
        for filename, filepath in attachments:
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'rb') as f:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(f.read())
            
            encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="{filename}"'
            )
            msg.attach(attachment)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as s:
            s.login(sender, pwd)
            s.send_message(msg)
        
        return {'success': True, 'message': f'邮件（含{len(attachments)}个附件）已发送至 {to_email}'}
    except Exception as e:
        error_msg = str(e)
        if 'UNEXPECTED_EOF' in error_msg or 'violation of protocol' in error_msg:
            return {
                'success': False, 
                'message': 'SSL连接失败。请检查网络环境：关闭VPN，使用国内直连网络。'
            }
        return {'success': False, 'message': f'发送失败: {error_msg}'}


# 浅色主题邮件模板
LIGHT_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; }}
        .wrapper {{ background: linear-gradient(135deg, #f0f4f8 0%, #e6eef7 100%); min-height: 100vh; padding: 40px 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(135deg, #0066cc 0%, #0099ff 100%); padding: 40px 30px; text-align: center; }}
        .header h1 {{ color: #ffffff; font-size: 28px; margin: 0 0 10px 0; }}
        .subtitle {{ color: rgba(255,255,255,0.9); font-size: 14px; letter-spacing: 2px; }}
        .logo {{ font-size: 48px; margin-bottom: 15px; }}
        .content {{ padding: 30px; color: #333333; line-height: 1.8; font-size: 15px; }}
        .content h2 {{ color: #0066cc; font-size: 20px; margin: 25px 0 15px 0; padding-bottom: 10px; border-bottom: 2px solid #e0e7ff; }}
        .content h3 {{ color: #0099ff; font-size: 16px; margin: 20px 0 10px 0; }}
        .content p {{ margin-bottom: 15px; color: #555555; }}
        .content ul {{ margin: 15px 0; padding-left: 25px; }}
        .content li {{ margin-bottom: 8px; color: #555555; }}
        .info-box {{ background: #f0f7ff; border-left: 4px solid #0066cc; padding: 20px; margin: 20px 0; border-radius: 0 8px 8px 0; }}
        .highlights {{ display: flex; flex-wrap: wrap; gap: 15px; padding: 0 30px 30px 30px; justify-content: center; }}
        .highlight-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; min-width: 150px; text-align: center; flex: 1; }}
        .highlight-label {{ color: #666666; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }}
        .highlight-value {{ color: #0066cc; font-size: 18px; font-weight: 700; }}
        .footer {{ background: #f8fafc; padding: 25px 30px; text-align: center; border-top: 1px solid #e2e8f0; }}
        .footer-text {{ color: #666666; font-size: 13px; margin-bottom: 10px; }}
        .footer-brand {{ color: #0066cc; font-weight: 600; font-size: 14px; }}
        .social-links {{ margin-top: 15px; }}
        .social-links a {{ color: #0066cc; text-decoration: none; margin: 0 10px; font-size: 12px; }}
        @media (max-width: 600px) {{ .wrapper {{ padding: 20px 10px; }} .header {{ padding: 30px 20px; }} .content {{ padding: 20px; }} .highlights {{ flex-direction: column; }} }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container">
            <div class="header">
                <div class="logo">🦞</div>
                <h1>{title}</h1>
                <p class="subtitle">{subtitle}</p>
            </div>
            <div class="content">{content}</div>
            {highlights_section}
            <div class="footer">
                <p class="footer-text">{footer}</p>
                <p class="footer-brand">非凡产研 🦞 OpenClaw</p>
                <div class="social-links">
                    <a href="https://ffcap.cn">官网</a> | <a href="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=177le97c-ca50-4b90-b660-cd05a994849d">飞书群</a> | <a href="https://github.com/wulaosiji/skills">GitHub</a>
                </div>
                <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #e2e8f0;">
                    <p style="color: #666666; font-size: 12px; margin-bottom: 10px;">📚 想了解更多？查看我们的开源教程：</p>
                    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px;">
                        <a href="https://uniquecapital.feishu.cn/wiki/Uqsqwoug5iYca3koiAQcUaEqnOf" style="color: #0066cc; text-decoration: none; font-size: 12px;">01-入门教程</a>
                        <a href="https://uniquecapital.feishu.cn/wiki/HJm5wmIl7iDS2Hkp5CXcvbHnntg" style="color: #0066cc; text-decoration: none; font-size: 12px;">02-技能教程</a>
                        <a href="https://uniquecapital.feishu.cn/wiki/RDgdweb14i1IcOkHHqlc42HQnKe" style="color: #0066cc; text-decoration: none; font-size: 12px;">03-人设教程</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""


def send_light_email(
    to_email: str,
    subject: str,
    title: str,
    content: str,
    subtitle: str = "",
    highlights: Optional[List[Dict[str, str]]] = None,
    footer: str = "非凡产研 | 让AI更有价值",
    include_ad: bool = True,
    ad_config: Optional[Dict[str, str]] = None,
    from_email: Optional[str] = None,
    password: Optional[str] = None
) -> dict:
    """
    使用浅色主题发送邮件
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        title: 邮件标题
        content: HTML内容
        subtitle: 副标题
        highlights: 高亮数据
        footer: 页脚文字
        include_ad: 是否包含广告（默认True）
        ad_config: 自定义广告配置（默认使用杭州大会）
        from_email: 发件人邮箱
        password: 密码
    """
    # 添加广告
    if include_ad:
        if ad_config is None:
            ad_config = HANGZHOU_EVENT_AD
        ad_html = EVENT_AD_TEMPLATE.format(**ad_config)
        full_content = content + ad_html
    else:
        full_content = content
    
    highlights_html = ""
    if highlights:
        cards = []
        for item in highlights:
            label = item.get('label', '')
            value = item.get('value', '')
            cards.append(f'<div class="highlight-card"><div class="highlight-label">{label}</div><div class="highlight-value">{value}</div></div>')
        highlights_html = '<div class="highlights">' + ''.join(cards) + '</div>'
    
    html_body = LIGHT_EMAIL_TEMPLATE.format(
        title=title,
        subtitle=subtitle,
        content=full_content,
        highlights_section=highlights_html,
        footer=footer
    )
    
    return send_html_email(to_email, subject, html_body, from_email, password)


def send_daily_email(
    to_email: str,
    subject: str,
    title: str,
    content: str,
    use_light_theme: bool = False,
    include_ad: bool = True,
    ad_config: Optional[Dict[str, str]] = None,
    subtitle: str = "",
    highlights: Optional[List[Dict[str, str]]] = None,
    footer: str = "非凡产研 | 让AI更有价值",
    from_email: Optional[str] = None,
    password: Optional[str] = None
) -> dict:
    """
    发送日报邮件（默认使用模板+广告）
    
    这是最简单的调用方式，一行代码发送带模板和广告的邮件。
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        title: 邮件标题
        content: HTML内容
        use_light_theme: 是否使用浅色主题（默认False=深色）
        include_ad: 是否包含广告（默认True）
        ad_config: 自定义广告配置（默认使用杭州大会）
        subtitle: 副标题
        highlights: 高亮数据
        footer: 页脚文字
        from_email: 发件人邮箱
        password: 密码
    
    Returns:
        dict: {'success': bool, 'message': str}
    
    示例:
        # 最简单用法：深色模板+默认广告
        send_daily_email(
            to_email='user@example.com',
            subject='🦞 AI日报',
            title='今日AI热点',
            content='<p>新闻内容...</p>'
        )
        
        # 浅色主题+广告
        send_daily_email(
            to_email='user@example.com',
            subject='🦞 AI日报',
            title='今日AI热点',
            content='<p>新闻内容...</p>',
            use_light_theme=True
        )
        
        # 无广告
        send_daily_email(
            to_email='user@example.com',
            subject='🦞 AI日报',
            title='今日AI热点',
            content='<p>新闻内容...</p>',
            include_ad=False
        )
    """
    # 添加广告
    if include_ad:
        if ad_config is None:
            ad_config = HANGZHOU_EVENT_AD
        ad_html = EVENT_AD_TEMPLATE.format(**ad_config)
        full_content = content + ad_html
    else:
        full_content = content
    
    # 选择主题
    if use_light_theme:
        return send_light_email(
            to_email=to_email,
            subject=subject,
            title=title,
            content=full_content,
            subtitle=subtitle,
            highlights=highlights,
            footer=footer,
            from_email=from_email,
            password=password
        )
    else:
        return send_tech_email(
            to_email=to_email,
            subject=subject,
            title=title,
            content=full_content,
            subtitle=subtitle,
            highlights=highlights,
            footer=footer,
            from_email=from_email,
            password=password
        )


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='邮件发送工具')
    parser.add_argument('to', help='收件人邮箱')
    parser.add_argument('subject', help='邮件主题')
    parser.add_argument('body', help='邮件正文')
    parser.add_argument('-p', '--password', help='邮箱密码', default=None)
    parser.add_argument('--html', action='store_true', help='发送HTML邮件')
    parser.add_argument('-a', '--attachments', nargs='+', help='附件路径', default=[])
    
    args = parser.parse_args()
    
    if args.attachments:
        attachments = [(os.path.basename(p), p) for p in args.attachments]
        result = send_email_with_attachments(
            args.to, args.subject, args.body, attachments, args.html, password=args.password
        )
    elif args.html:
        result = send_html_email(args.to, args.subject, args.body, password=args.password)
    else:
        result = send_email(args.to, args.subject, args.body, password=args.password)
    
    print(result['message'])
    exit(0 if result['success'] else 1)


def send_smart_email(
    to_email: str,
    subject: str,
    title: str,
    content: str,
    subtitle: str = "",
    highlights: Optional[List[Dict[str, str]]] = None,
    footer: str = "非凡产研 | 让AI更有价值",
    from_email: Optional[str] = None,
    password: Optional[str] = None
) -> dict:
    """
    智能发送邮件 - 根据时间自动选择主题（白天浅色/晚上深色）+ 默认广告
    
    这是推荐的默认发送方式，会自动：
    1. 判断当前时间（6:00-18:00为白天，其他为晚上）
    2. 白天使用浅色主题，晚上使用深色主题
    3. 自动添加杭州大会广告
    """
    from datetime import datetime
    
    # 获取当前小时
    current_hour = datetime.now().hour
    
    # 6:00-18:00 为白天，使用浅色主题
    is_daytime = 6 <= current_hour < 18
    
    if is_daytime:
        return send_light_email(
            to_email=to_email,
            subject=subject,
            title=title,
            content=content,
            subtitle=subtitle,
            highlights=highlights,
            footer=footer,
            include_ad=True,
            from_email=from_email,
            password=password
        )
    else:
        return send_tech_email(
            to_email=to_email,
            subject=subject,
            title=title,
            content=content,
            subtitle=subtitle,
            highlights=highlights,
            footer=footer,
            include_ad=True,
            from_email=from_email,
            password=password
        )
