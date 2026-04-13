---
name: rss-feed
description: |
  RSS订阅源处理与管理工具，支持RSS内容解析、订阅管理、内容聚合和自动化分发。
  
  Use when:
  - 解析RSS订阅源内容 parse RSS feed content
  - 管理RSS订阅 manage RSS subscriptions
  - 内容聚合与监控 content aggregation monitoring
  - RSS转邮件/报告 RSS to email reports
  - 新闻源自动采集 automated news collection
  - 博客/播客内容追踪 blog podcast tracking
  
  Cross-references: content-extractor, email-sender, document-hub, twitter-scraper, long-form-writer
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# RSS Feed Skill

Process and manage RSS feeds for content aggregation and automated distribution.

## When to Use

### Use This Skill When
- 需要解析RSS订阅源内容
- 管理和跟踪多个RSS订阅
- 自动化采集新闻和博客内容
- 基于RSS生成日报/周报
- 监控特定主题的内容更新
- 追踪播客、博客的更新动态

### Do NOT Use This Skill If
- RSS源不可用或已废弃
- 需要实时推送（RSS有延迟）
- 源内容需要付费订阅
- 需要抓取没有RSS源的网站
- 网络环境无法访问目标RSS源

### Typical Trigger Phrases
**Chinese:**
- "解析RSS源"
- "RSS订阅管理"
- "内容自动采集"
- "RSS转邮件"
- "新闻聚合"
- "订阅源监控"

**English:**
- "Parse RSS feed"
- "Manage RSS subscriptions"
- "Content aggregation"
- "RSS to email"
- "News feed monitoring"
- "Track blog updates"

## Workflow

### Step 1: 配置RSS源
收集需要监控的RSS订阅地址：
```python
feeds = [
    "https://example.com/feed.xml",
    "https://news.example.com/rss"
]
```

### Step 2: 解析内容
```python
from skills.rss_feed.rss_feed import parse_feed

for feed_url in feeds:
    items = parse_feed(feed_url, max_items=10)
    for item in items:
        print(f"{item.title}: {item.link}")
```

### Step 3: 内容处理
- 去重过滤
- 关键词筛选
- 分类归档

### Step 4: 自动化分发
- 生成日报邮件
- 保存到文档
- 转发到其他平台

## Guardrails

### Anti-Patterns
- ❌ 高频轮询RSS源（建议间隔≥15分钟）
- ❌ 不处理RSS源失效的情况
- ❌ 抓取全文时不遵守robots.txt
- ❌ 不过滤重复内容

### Limitations
- RSS源更新有延迟
- 部分RSS仅提供摘要
- 源地址可能变更
- 某些源有访问频率限制

### Best Practices
1. **缓存机制**: 避免重复解析相同内容
2. **错误处理**: 单个RSS源失败不影响其他
3. **频率控制**: 合理设置轮询间隔
4. **内容去重**: 使用GUID或链接去重

## Core Functions

### Parse RSS Feed
```python
from skills.rss_feed.rss_feed import parse_feed

items = parse_feed("https://example.com/feed.xml", max_items=20)
for item in items:
    print(item.title, item.link, item.published)
```

### Batch Processing
```python
from skills.rss_feed.rss_feed import batch_parse

results = batch_parse(feed_urls, max_items=10)
for feed_url, items in results.items():
    print(f"{feed_url}: {len(items)} items")
```

### Filter by Keywords
```python
from skills.rss_feed.rss_feed import filter_items

filtered = filter_items(items, keywords=["AI", "人工智能", "机器学习"])
```

## RSS Item Structure

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

## Workflow Integration

### Workflow 1: RSS → Daily Report Email
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

### Workflow 2: RSS → Document Archive
```python
from skills.rss_feed.rss_feed import parse_feed
from skills.document_hub.document_hub import write

items = parse_feed("https://blog.example.com/feed.xml")
data = [{"标题": i.title, "链接": i.link, "时间": i.published} for i in items]
write("rss-archive.xlsx", {"sheets": {"订阅内容": {"data": data}}})
```

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 内容补充 | 抓取RSS摘要对应的全文 |
| **email-sender** | 分发渠道 | 发送RSS汇总邮件 |
| **document-hub** | 归档存储 | 保存RSS内容到文档 |
| **twitter-scraper** | 数据来源 | 社交媒体内容补充 |
| **long-form-writer** | 内容加工 | 基于RSS内容生成报告 |

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
