---
name: rss-feed
description: |
  RSS订阅源处理与管理工具，支持RSS内容解析、订阅管理、内容聚合、关键词筛选和自动化分发（邮件/报告）。
  Use when: "解析RSS源", "RSS订阅管理", "内容自动采集", "parse RSS feed", "manage RSS subscriptions", "RSS转邮件", "news feed monitoring", "博客播客追踪".
  支持批量解析、关键词过滤和去重，适用于新闻聚合和内容监控。Cross-references: content-extractor, wechat-article-fetcher, twitter-scraper, email-sender, document-hub.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# RSS Feed Skill

> Process and manage RSS feeds for content aggregation and automated distribution.

## When to Use

Use this skill when:
- 需要解析RSS订阅源内容
- 管理和跟踪多个RSS订阅
- 自动化采集新闻和博客内容
- 基于RSS生成日报/周报
- 监控特定主题的内容更新
- 追踪播客、博客的更新动态

Do NOT use this skill if:
- RSS源不可用或已废弃 → 更换有效源
- 需要实时推送（RSS有延迟）→ 使用实时API
- 源内容需要付费订阅 → 不抓取付费内容
- 需要抓取没有RSS源的网站 → 使用 content-extractor
- 网络环境无法访问目标RSS源

Typical triggers:
- 「解析RSS源」「RSS订阅管理」「内容自动采集」
- "Parse RSS feed", "Manage RSS subscriptions", "Content aggregation"
- 「RSS转邮件」「新闻聚合」「订阅源监控」
- "RSS to email", "News feed monitoring", "Track blog updates"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户提供的RSS源列表，确认目标和约束。收集需要监控的RSS订阅地址：
```python
feeds = [
    "https://example.com/feed.xml",
    "https://news.example.com/rss"
]
```

2. **约束 (Constrain)**
验证RSS源可访问性，设定轮询间隔（建议≥15分钟）和最大条目数。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
每个条目必须来自RSS源实际响应，不编造内容。使用GUID或链接去重，记录发布时间作为可追溯证据。

4. **执行 (Execute)**
调用解析脚本，先给影响与结论，再给行动和必要证据。
```python
from skills.rss_feed.rss_feed import parse_feed

for feed_url in feeds:
    items = parse_feed(feed_url, max_items=10)
    for item in items:
        print(f"{item.title}: {item.link}")
```

内容处理：
- 去重过滤
- 关键词筛选
- 分类归档

自动化分发：
- 生成日报邮件
- 保存到文档
- 转发到其他平台

5. **验证 (Verify)**
用不同于生成路径的方式回读输出——检查解析结果的条目数，每条有title和link字段，发布时间格式合理。批量解析时抽查每个源的结果。

6. **交付 (Deliver)**
返回结构化条目列表，清理临时缓存文件。

## Output

返回RSS条目字典列表：
```python
{
    "title": "文章标题",
    "link": "https://example.com/article",
    "description": "文章摘要",
    "published": "2026-02-07T10:00:00Z",
    "author": "作者名",
    "guid": "唯一标识"
}
```

批量解析返回 `Dict[feed_url, List[item]]`。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 高频轮询RSS源（建议间隔≥15分钟）
- Do NOT 不处理RSS源失效的情况，单个源失败不影响其他
- Do NOT 抓取全文时不遵守robots.txt
- Do NOT 不过滤重复内容，使用GUID或链接去重

**Constraints**
- RSS源更新有延迟
- 部分RSS仅提供摘要
- 源地址可能变更
- 某些源有访问频率限制

**Best Practices**
1. **缓存机制**: 避免重复解析相同内容
2. **错误处理**: 单个RSS源失败不影响其他
3. **频率控制**: 合理设置轮询间隔
4. **内容去重**: 使用GUID或链接去重

## Core Functions

**Parse RSS Feed**
```python
from skills.rss_feed.rss_feed import parse_feed

items = parse_feed("https://example.com/feed.xml", max_items=20)
for item in items:
    print(item.title, item.link, item.published)
```

**Batch Processing**
```python
from skills.rss_feed.rss_feed import batch_parse

results = batch_parse(feed_urls, max_items=10)
for feed_url, items in results.items():
    print(f"{feed_url}: {len(items)} items")
```

**Filter by Keywords**
```python
from skills.rss_feed.rss_feed import filter_items

filtered = filter_items(items, keywords=["AI", "人工智能", "机器学习"])
```

## Workflow Integration

**Workflow 1: RSS → Daily Report Email**
```python
from skills.rss_feed.rss_feed import parse_feed
from skills.email_sender.email_sender import send_tech_email

items = parse_feed("https://tech-news.com/rss", max_items=10)
content = "<ul>" + "".join([f"<li>{i.title}</li>" for i in items]) + "</ul>"

send_tech_email(
    to_email="user@example.com",
    subject="每日科技资讯",
    title="今日热点",
    content=content
)
```

**Workflow 2: RSS → Document Archive**
```python
from skills.rss_feed.rss_feed import parse_feed
from skills.document_hub.document_hub import write

items = parse_feed("https://blog.example.com/feed.xml")
data = [{"标题": i.title, "链接": i.link, "时间": i.published} for i in items]
write("rss-archive.xlsx", {"sheets": {"订阅内容": {"data": data}}})
```

## Related Skills

- **content-extractor** — 内容补充：抓取RSS摘要对应的全文
- **wechat-article-fetcher** — 平台扩展：中文公众号内容抓取
- **twitter-scraper** — 数据来源：社交媒体内容补充
- **email-sender** — 分发渠道：发送RSS汇总邮件
- **document-hub** — 归档存储：保存RSS内容到文档

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
