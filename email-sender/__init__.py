"""
Email Sender Skill
邮件发送工具封装
"""

from .email_sender import (
    send_email,
    send_html_email,
    send_tech_email,
    send_light_email,
    send_email_with_attachments,
    send_email_with_ad,
    TECH_EMAIL_TEMPLATE,
    LIGHT_EMAIL_TEMPLATE,
    EVENT_AD_TEMPLATE,
    HANGZHOU_EVENT_AD
)

__all__ = [
    'send_email',
    'send_html_email',
    'send_tech_email',
    'send_light_email',
    'send_email_with_attachments',
    'send_email_with_ad',
    'TECH_EMAIL_TEMPLATE',
    'LIGHT_EMAIL_TEMPLATE',
    'EVENT_AD_TEMPLATE',
    'HANGZHOU_EVENT_AD'
]

__version__ = '1.2.0'
