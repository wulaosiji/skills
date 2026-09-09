---
name: twitter-scraper
description: |
  Twitter/X推文抓取工具，基于xcancel.com获取公开推文数据，支持单个用户抓取、批量账号监控、JSON/CSV输出和舆情分析。
  Use when: "抓取Twitter内容", "获取X平台推文", "监控Twitter账号", "scrape Twitter tweets", "fetch X posts", "批量抓取推文", "Twitter data scraping", "推特舆情分析".
  使用浏览器自动化获取公开推文，无需登录态。Cross-references: content-extractor, rss-feed, wechat-article-fetcher, document-hub, email-sender.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能已迁移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) 的 `social-intelligence`，推荐使用新版。本版本保留用于向后兼容。

# Twitter/X Scraper Skill

> 基于 xcancel.com 的 Twitter/X 推文抓取工具，使用浏览器自动化获取公开推文数据。

## When to Use

Use this skill when:
- 需要抓取特定Twitter/X用户的公开推文
- 批量监控多个账号的最新动态
- 进行社交媒体数据分析
- 收集Twitter内容作为研究素材
- 需要推文数据导出为JSON/CSV
- 竞品监测和舆情追踪

Do NOT use this skill if:
- 目标用户设为私密账户 → 不抓取私密内容
- xcancel.com 服务不可用 → 等待服务恢复或换通道
- 需要抓取大量推文（建议单次不超过20条）→ 分批执行
- 需要登录态才能查看的内容 → 不支持
- 目标账号已不存在或被封禁

Typical triggers:
- 「抓取Twitter内容」「获取X平台推文」「推特数据抓取」
- "Scrape Twitter tweets", "Fetch X posts", "Twitter data scraping"
- 「监控Twitter账号」「批量抓取推文」「Twitter舆情分析」
- "Monitor Twitter accounts", "Batch tweet collection", "Twitter sentiment analysis"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认目标账号和抓取数量：
- 检查账号是否为公开状态
- 确认用户名正确（不含@）
- 评估所需推文数量

2. **约束 (Constrain)**
验证输入完整性，设定抓取边界。单次抓取建议不超过20条，受阻时换通道，不降级交付物。

| 模式 | 函数 | 适用场景 |
|------|------|----------|
| 单用户 | `scrape_user()` | 抓取单个账号 |
| 批量 | `scrape_multiple_users()` | 多个账号同时监控 |
| 命令行 | `scrape.py` | 脚本自动化 |

3. **证据 (Evidence)**
每个推文数据必须来自xcancel.com实际响应，不编造推文内容。记录抓取时间和原始URL作为可追溯证据。

4. **执行 (Execute)**
调用抓取脚本，先给影响与结论，再给行动和必要证据。
```python
from skills.twitter_scraper.scripts.scrape import scrape_user

tweets = scrape_user("sama", max_tweets=5)
```

处理输出：
- JSON格式：程序化分析
- CSV格式：表格查看
- 直接打印：快速预览

5. **验证 (Verify)**
用不同于生成路径的方式回读输出——检查返回的推文列表非空，每条推文有text和date字段，URL格式正确。批量抓取时抽查每个账号的结果。

6. **交付 (Deliver)**
返回结构化推文数据，清理临时浏览器进程。

## Output

返回JSON数组格式：
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

批量抓取返回 `Dict[username, List[tweet]]`。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 单次抓取过多推文（建议≤20条）
- NEVER 高频连续抓取（可能导致超时）
- NEVER 抓取私密用户内容
- Do NOT 将数据用于违规用途

**Constraints**
- 依赖 xcancel.com 服务可用性
- 需要浏览器环境（启动约3-5秒）
- 每次抓取需等待JS验证（约2-3秒）
- 不支持登录态内容
- 数据字段可能不完整

**Best Practices**
1. **控制数量**: 单次抓取建议不超过20条
2. **错误处理**: 捕获网络超时和空结果
3. **服务依赖**: 关注xcancel.com可用性
4. **合法合规**: 仅抓取公开数据

## Installation

无需额外依赖，直接使用 OpenClaw 内置 browser 工具。

## Usage

**1. 抓取单个用户**
```python
from skills.twitter_scraper.scripts.scrape import scrape_user

# 抓取 @sama 的最新5条推文
tweets = scrape_user("sama", max_tweets=5)

for tweet in tweets:
    print(f"{tweet['date']}: {tweet['text'][:100]}...")
```

**2. 批量抓取多个用户**
```python
from skills.twitter_scraper.scripts.scrape import scrape_multiple_users

users = ["sama", "gdb", "deepseek_ai", "elonmusk"]
results = scrape_multiple_users(users, max_tweets=5)

for username, tweets in results.items():
    print(f"@{username}: {len(tweets)} 条推文")
```

**3. 命令行使用**
```bash
# 抓取单个用户
python3 skills/twitter_scraper/scripts/scrape.py --user sama --max 10

# 批量抓取
python3 skills/twitter_scraper/scripts/scrape.py --users sama,gdb,elonmusk --max 5

# 保存到文件
python3 skills/twitter_scraper/scripts/scrape.py --user sama --output tweets.json
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

**Issue: Empty Results**
- 检查用户名是否正确
- 确认 xcancel.com 可访问
- 检查用户是否设为私密

**Issue: Timeout Error**
- 减少 max_tweets 数量
- 检查网络连接
- 稍后重试

## Related Skills

- **content-extractor** — 通用替代：多平台内容提取
- **rss-feed** — 数据来源：RSS订阅作为社交媒体内容补充
- **wechat-article-fetcher** — 平台扩展：中文社交媒体内容抓取
- **document-hub** — 下游处理：导出为Excel/Word
- **email-sender** — 分发渠道：发送监控报告

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
