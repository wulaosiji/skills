---
name: twitter-scraper
description: |
  Twitter/X推文抓取工具，基于xcancel.com获取公开推文数据，支持单个用户抓取、批量账号抓取、JSON/CSV输出。
  
  Use when:
  - 抓取Twitter/X用户推文 scrape Twitter/X tweets
  - 批量监控多个账号 batch monitor multiple accounts
  - 社交媒体数据分析 social media data analysis
  - 获取公开推文数据 fetch public tweet data
  - 推特内容归档 archive Twitter content
  - 竞品/舆情监控 competitive monitoring
  
  Cross-references: content-extractor, rss-feed, document-hub, email-sender, long-form-writer
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

> 🚀 **Migrated to [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) as `social-intelligence`.**
> 
> This version is kept for backward compatibility. For the latest updates, use the founder-skills version.



# Twitter/X Scraper Skill

基于 xcancel.com 的 Twitter/X 推文抓取工具，使用浏览器自动化获取公开推文数据。

## When to Use

### Use This Skill When
- 需要抓取特定Twitter/X用户的公开推文
- 批量监控多个账号的最新动态
- 进行社交媒体数据分析
- 收集Twitter内容作为研究素材
- 需要推文数据导出为JSON/CSV
- 竞品监测和舆情追踪

### Do NOT Use This Skill If
- 目标用户设为私密账户
- xcancel.com 服务不可用
- 需要抓取大量推文（建议单次不超过20条）
- 需要登录态才能查看的内容
- 目标账号已不存在或被封禁

### Typical Trigger Phrases
**Chinese:**
- "抓取Twitter内容"
- "获取X平台推文"
- "推特数据抓取"
- "监控Twitter账号"
- "批量抓取推文"
- "Twitter舆情分析"

**English:**
- "Scrape Twitter tweets"
- "Fetch X posts"
- "Twitter data scraping"
- "Monitor Twitter accounts"
- "Batch tweet collection"
- "Twitter sentiment analysis"

## Workflow

### Step 1: 确认目标账号
- 检查账号是否为公开状态
- 确认用户名正确（不含@）
- 评估所需推文数量

### Step 2: 选择抓取模式
| 模式 | 函数 | 适用场景 |
|------|------|----------|
| 单用户 | `scrape_user()` | 抓取单个账号 |
| 批量 | `scrape_multiple_users()` | 多个账号同时监控 |
| 命令行 | `scrape.py` | 脚本自动化 |

### Step 3: 执行抓取
```python
from skills.twitter_scraper.scripts.scrape import scrape_user

tweets = scrape_user("sama", max_tweets=5)
```

### Step 4: 处理输出
- JSON格式：程序化分析
- CSV格式：表格查看
- 直接打印：快速预览

## Guardrails

### Anti-Patterns
- ❌ 单次抓取过多推文（建议≤20条）
- ❌ 高频连续抓取（可能导致超时）
- ❌ 抓取私密用户内容
- ❌ 将数据用于违规用途

### Limitations
- 依赖 xcancel.com 服务可用性
- 需要浏览器环境（启动约3-5秒）
- 每次抓取需等待JS验证（约2-3秒）
- 不支持登录态内容
- 数据字段可能不完整

### Best Practices
1. **控制数量**: 单次抓取建议不超过20条
2. **错误处理**: 捕获网络超时和空结果
3. **服务依赖**: 关注xcancel.com可用性
4. **合法合规**: 仅抓取公开数据

## Installation

无需额外依赖，直接使用 OpenClaw 内置 browser 工具。

## Usage

### 1. 抓取单个用户
```python
from skills.twitter_scraper.scripts.scrape import scrape_user

# 抓取 @sama 的最新5条推文
tweets = scrape_user("sama", max_tweets=5)

for tweet in tweets:
    print(f"{tweet['date']}: {tweet['text'][:100]}...")
```

### 2. 批量抓取多个用户
```python
from skills.twitter_scraper.scripts.scrape import scrape_multiple_users

users = ["sama", "gdb", "deepseek_ai", "elonmusk"]
results = scrape_multiple_users(users, max_tweets=5)

for username, tweets in results.items():
    print(f"@{username}: {len(tweets)} 条推文")
```

### 3. 命令行使用
```bash
# 抓取单个用户
python3 skills/twitter_scraper/scripts/scrape.py --user sama --max 10

# 批量抓取
python3 skills/twitter_scraper/scripts/scrape.py --users sama,gdb,elonmusk --max 5

# 保存到文件
python3 skills/twitter_scraper/scripts/scrape.py --user sama --output tweets.json
```

## Output Format

```json
[
  {
    "id": "2019814741129195576",
    "username": "sama",
    "text": "How would you prefer us to charge for Codex?...",
    "date": "22h",
    "likes": 2341,
    "retweets": 82,
    "replies": 1941,
    "url": "https://xcancel.com/sama/status/2019814741129195576"
  }
]
```

## Verified Accounts

已测试可用的账号：
- @sama (Sam Altman)
- @gdb (Greg Brockman)
- @elonmusk (Elon Musk)
- @deepseek_ai (DeepSeek)

## Data Source

- 数据来源：xcancel.com (Nitter 替代品)
- 数据类型：公开推文（无需登录）
- 更新频率：实时

## Troubleshooting

### Issue: Empty Results
- 检查用户名是否正确
- 确认 xcancel.com 可访问
- 检查用户是否设为私密

### Issue: Timeout Error
- 减少 max_tweets 数量
- 检查网络连接
- 稍后重试

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 通用替代 | 多平台内容提取 |
| **rss-feed** | 数据来源 | RSS订阅作为补充 |
| **document-hub** | 下游处理 | 导出为Excel/Word |
| **email-sender** | 分发渠道 | 发送监控报告 |
| **long-form-writer** | 内容加工 | 基于推文数据分析写作 |

## Changelog

- 2026-02-07: 初始版本，支持基本抓取功能

## Author

卓然 (Zhuoran) for 非凡产研

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
