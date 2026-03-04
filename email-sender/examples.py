#!/usr/bin/env python3
"""
邮件发送示例 - 展示科技感HTML模板的使用
"""

import sys
sys.path.insert(0, '/Users/delta/.openclaw/workspace')

from skills.email_sender.email_sender import send_tech_email, send_email, send_html_email


def example_simple_text():
    """示例1: 发送纯文本邮件"""
    result = send_email(
        to_email="recipient@example.com",
        subject="测试邮件",
        body="这是一封纯文本测试邮件。\n\n祝好，\n卓然"
    )
    print(f"纯文本邮件: {result['message']}")


def example_html():
    """示例2: 发送自定义HTML邮件"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; color: #333; }
            h1 { color: #0066cc; }
        </style>
    </head>
    <body>
        <h1>自定义HTML邮件</h1>
        <p>这是自定义HTML格式的邮件内容。</p>
    </body>
    </html>
    """
    
    result = send_html_email(
        to_email="recipient@example.com",
        subject="HTML邮件示例",
        html_body=html_content
    )
    print(f"HTML邮件: {result['message']}")


def example_ai_daily_report():
    """示例3: 发送AI日报（科技感模板）"""
    result = send_tech_email(
        to_email="recipient@example.com",
        subject="🦞 卓然AI早报 | 2026-03-04",
        title="今日AI热点",
        subtitle="2026年3月4日 周三",
        content="""
        <h2>🔥 头条新闻</h2>
        <p>Claude登顶美区App Store榜首，用户发起"ChatGPT解约运动"，卸载量激增295%。</p>
        
        <h2>💡 关键洞察</h2>
        <p>美国AI军事化正在撕裂硅谷：</p>
        <ul>
            <li>Anthropic坚守伦理底线失去政府合同</li>
            <li>OpenAI妥协合作后遭遇卸载潮</li>
            <li>Claude逆势登顶证明"理想主义"仍有市场</li>
        </ul>
        
        <div class="info-box">
            <p><strong>值得关注：</strong>这场博弈的核心争议是AI安全护栏是否应该适用于军事用途。</p>
        </div>
        """,
        highlights=[
            {"label": "政策风向", "value": "AI军事化加速"},
            {"label": "资本流向", "value": "基础设施增长"},
            {"label": "用户态度", "value": "卸载量+295%"}
        ],
        footer="非凡产研 | 让AI更有价值"
    )
    print(f"AI日报: {result['message']}")


def example_meeting_invitation():
    """示例4: 发送会议邀请"""
    result = send_tech_email(
        to_email="guest@example.com",
        subject="📅 会议邀请：AI产品策略讨论",
        title="会议邀请",
        subtitle="非凡产研 · 战略会议",
        content="""
        <p>您好，诚邀您参加AI产品策略讨论会。</p>
        
        <div class="info-box">
            <p><strong>时间：</strong>2026年3月5日 14:00-16:00</p>
            <p><strong>地点：</strong>飞书会议</p>
            <p><strong>议题：</strong></p>
            <ul>
                <li>Q2产品规划</li>
                <li>技术架构调整</li>
                <li>资源分配方案</li>
            </ul>
        </div>
        
        <p style="text-align: center; margin: 30px 0;">
            <a href="#" class="cta-button">确认参加</a>
        </p>
        """,
        highlights=[
            {"label": "会议ID", "value": "123-456-789"},
            {"label": "密码", "value": "8888"}
        ],
        footer="非凡产研 | 战略部"
    )
    print(f"会议邀请: {result['message']}")


def example_welcome_email():
    """示例5: 发送欢迎邮件"""
    result = send_tech_email(
        to_email="newuser@example.com",
        subject="🎉 欢迎加入非凡产研",
        title="欢迎加入",
        subtitle="开启您的AI之旅",
        content="""
        <p>您好，欢迎加入非凡产研社区！🦞</p>
        
        <h3>您可以：</h3>
        <ul>
            <li>参与每日AI话题讨论</li>
            <li>获取最新AI行业洞察</li>
            <li>连接AI领域专家和创业者</li>
        </ul>
        
        <p>如有任何问题，随时联系我们的团队。</p>
        """,
        highlights=[
            {"label": "社区成员", "value": "10,000+"},
            {"label": "日活话题", "value": "50+"}
        ],
        footer="非凡产研 | 社区团队"
    )
    print(f"欢迎邮件: {result['message']}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='邮件发送示例')
    parser.add_argument('--example', choices=['text', 'html', 'daily', 'meeting', 'welcome'], 
                        default='daily', help='选择示例类型')
    
    args = parser.parse_args()
    
    examples = {
        'text': example_simple_text,
        'html': example_html,
        'daily': example_ai_daily_report,
        'meeting': example_meeting_invitation,
        'welcome': example_welcome_email
    }
    
    print(f"运行示例: {args.example}")
    examples[args.example]()
