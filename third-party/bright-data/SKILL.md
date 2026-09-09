---
name: bright-data
description: |
  Bright Data Web Scraper API via curl for social media scraping, web data extraction, and account management.
  Supports Twitter/X, Reddit, YouTube, Instagram, TikTok, LinkedIn profiles, posts, comments, and engagement metrics.
  Use when: "抓取社交媒体", "scrape twitter", "爬取社媒数据", "bright data", "web scraper API", "抓取Reddit", "scrape Instagram", "社媒数据采集", "YouTube数据抓取", "social media scraping".
  Provides async/sync scraping, progress monitoring, snapshot management, and bandwidth usage tracking.
  Cross-references: x-twitter-scraper, gh-cli.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Bright Data Web Scraper API

Use the Bright Data API via direct `curl` calls for **social media scraping**, **web data extraction**, and **account management**.

> Official docs: `https://docs.brightdata.com/`

## When to Use

Use this skill when:
- You need to scrape social media data from Twitter/X, Reddit, YouTube, Instagram, TikTok, or LinkedIn
- You need to extract posts, profiles, comments, engagement metrics, or media from social platforms
- You need to monitor Bright Data account status, zones, or bandwidth usage
- You need batch/asynchronous data collection from web sources

Do NOT use this skill if:
- You need to post/tweet or perform write actions on X → use `x-twitter-scraper` instead
- You need GitHub repository/issue/PR operations → use `gh-cli` instead
- You need general web search without structured social media extraction → use general search tools
- The user does not have a Bright Data API key or dataset_id → guide them to sign up first

Typical triggers:
- 「抓取社交媒体数据」「爬取Twitter」「社媒数据采集」
- "scrape Instagram profile" "bright data API" "web scraper"
- 「抓取Reddit帖子」「YouTube评论抓取」「TikTok数据」

## Workflow

1. **探查 (Probe)**
确认用户需要抓取的平台和目标（profile/post/comment/search），确认用户是否已有 Bright Data API key 和 dataset_id。

2. **约束 (Constrain)**
验证 API key 已配置（`BRIGHTDATA_API_KEY` 环境变量），dataset_id 已创建。设定速率限制：batch mode 最多100并发请求，单次输入最大1GB。不降级交付——若依赖缺失，先指导用户配置。

3. **证据 (Evidence)**
所有数据来自 Bright Data API 实时返回。构造请求时，目标 URL 必须来自用户输入，不编造目标。抓取结果以 JSON 格式返回，字段以 API 响应为准。

4. **执行 (Execute)**
通过 `curl` 调用 Bright Data API：
- 小请求用同步模式 (`/scrape`) 立即获取结果
- 大批量用异步模式 (`/trigger`) 获取 `snapshot_id`，轮询 `/progress`，状态为 `ready` 后下载结果
- 使用 `bash -c '...'` 包裹含环境变量的管道命令（避免环境变量被清空）

5. **验证 (Verify)**
验证 API 响应：检查 HTTP 状态码、确认返回 JSON 包含预期字段、异步任务确认 status 为 `ready` 而非 `failed`。若返回 429，遵守 `Retry-After` 后退重试。

6. **交付 (Deliver)**
返回抓取的 JSON 数据或文件路径，总结关键指标，清理 `/tmp/` 下的临时请求文件。若结果较大，提示用户可导出为 CSV 格式。

## Output

JSON data from the Bright Data API, returned directly in the response for synchronous calls or as a downloadable snapshot for asynchronous jobs. Output includes platform-specific fields (e.g., `followers`, `likes`, `retweets`, `comments`, `post_id`, `profile_name`). Account management endpoints return status, zone info, and bandwidth usage JSON.

---

## When to Use

Use this skill when you need to:

- **Scrape social media** - Twitter/X, Reddit, YouTube, Instagram, TikTok, LinkedIn
- **Extract web data** - Posts, profiles, comments, engagement metrics
- **Monitor usage** - Track bandwidth and request usage
- **Manage account** - Check status and zones

---

## Prerequisites

1. Sign up at [Bright Data](https://brightdata.com/)
2. Get your API key from [Settings > Users](https://brightdata.com/cp/setting/users)
3. Create a Web Scraper dataset in the [Control Panel](https://brightdata.com/cp/datasets) to get your `dataset_id`

```bash
export BRIGHTDATA_API_KEY="your-api-key"
```

### Base URL

```
https://api.brightdata.com
```

---


> **Important:** When using `$VAR` in a command that pipes to another command, wrap the command containing `$VAR` in `bash -c '...'`. Due to a Claude Code bug, environment variables are silently cleared when pipes are used directly.
> ```bash
> bash -c 'curl -s "https://api.example.com" -H "Authorization: Bearer $API_KEY"'
> ```

---

## Social Media Scraping

Bright Data supports scraping these social media platforms:

| Platform | Profiles | Posts | Comments | Reels/Videos |
|----------|----------|-------|----------|--------------|
| Twitter/X | ✅ | ✅ | - | - |
| Reddit | - | ✅ | ✅ | - |
| YouTube | ✅ | ✅ | ✅ | - |
| Instagram | ✅ | ✅ | ✅ | ✅ |
| TikTok | ✅ | ✅ | ✅ | - |
| LinkedIn | ✅ | ✅ | - | - |

---

## How to Use

### 1. Trigger Scraping (Asynchronous)

Trigger a data collection job and get a `snapshot_id` for later retrieval.

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://twitter.com/username"},
  {"url": "https://twitter.com/username2"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Response:**
```json
{
  "snapshot_id": "s_m4x7enmven8djfqak"
}
```

---

### 2. Trigger Scraping (Synchronous)

Get results immediately in the response (for small requests).

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.reddit.com/r/technology/comments/xxxxx"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

---

### 3. Monitor Progress

Check the status of a scraping job (replace `<snapshot-id>` with your actual snapshot ID):

```bash
bash -c 'curl -s "https://api.brightdata.com/datasets/v3/progress/<snapshot-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"'
```

**Response:**
```json
{
  "snapshot_id": "s_m4x7enmven8djfqak",
  "dataset_id": "gd_xxxxx",
  "status": "running"
}
```

Status values: `running`, `ready`, `failed`

---

### 4. Download Results

Once status is `ready`, download the collected data (replace `<snapshot-id>` with your actual snapshot ID):

```bash
bash -c 'curl -s "https://api.brightdata.com/datasets/v3/snapshot/<snapshot-id>?format=json" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"'
```

---

### 5. List Snapshots

Get all your snapshots:

```bash
bash -c 'curl -s "https://api.brightdata.com/datasets/v3/snapshots" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"' | jq '.[] | {snapshot_id, dataset_id, status}'
```

---

### 6. Cancel Snapshot

Cancel a running job (replace `<snapshot-id>` with your actual snapshot ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/cancel?snapshot_id=<snapshot-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"'
```

---

## Platform-Specific Examples

### Twitter/X - Scrape Profile

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://twitter.com/elonmusk"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `x_id`, `profile_name`, `biography`, `is_verified`, `followers`, `following`, `profile_image_link`

### Twitter/X - Scrape Posts

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://twitter.com/username/status/123456789"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `post_id`, `text`, `replies`, `likes`, `retweets`, `views`, `hashtags`, `media`

---

### Reddit - Scrape Subreddit Posts

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.reddit.com/r/technology", "sort_by": "hot"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Parameters:** `url`, `sort_by` (new/top/hot)

**Returns:** `post_id`, `title`, `description`, `num_comments`, `upvotes`, `date_posted`, `community`

### Reddit - Scrape Comments

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.reddit.com/r/technology/comments/xxxxx/post_title"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `comment_id`, `user_posted`, `comment_text`, `upvotes`, `replies`

---

### YouTube - Scrape Video Info

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `title`, `views`, `likes`, `num_comments`, `video_length`, `transcript`, `channel_name`

### YouTube - Search by Keyword

Write to `/tmp/brightdata_request.json`:

```json
[
  {"keyword": "artificial intelligence", "num_of_posts": 50}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

### YouTube - Scrape Comments

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.youtube.com/watch?v=xxxxx", "load_replies": 3}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `comment_text`, `likes`, `replies`, `username`, `date`

---

### Instagram - Scrape Profile

Write to `/tmp/brightdata_request.json`:

```json
[
  {"url": "https://www.instagram.com/username"}
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/scrape?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

**Returns:** `followers`, `post_count`, `profile_name`, `is_verified`, `biography`

### Instagram - Scrape Posts

Write to `/tmp/brightdata_request.json`:

```json
[
  {
    "url": "https://www.instagram.com/username",
    "num_of_posts": 20,
    "start_date": "01-01-2024",
    "end_date": "12-31-2024"
  }
]
```

Then run (replace `<dataset-id>` with your actual dataset ID):

```bash
bash -c 'curl -s -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=<dataset-id>" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @/tmp/brightdata_request.json'
```

---

## Account Management

### Check Account Status

```bash
bash -c 'curl -s "https://api.brightdata.com/status" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"'
```

**Response:**
```json
{
  "status": "active",
  "customer": "hl_xxxxxxxx",
  "can_make_requests": true,
  "ip": "x.x.x.x"
}
```

### Get Active Zones

```bash
bash -c 'curl -s "https://api.brightdata.com/zone/get_active_zones" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"' | jq '.[] | {name, type}'
```

### Get Bandwidth Usage

```bash
bash -c 'curl -s "https://api.brightdata.com/customer/bw" \
  -H "Authorization: Bearer ${BRIGHTDATA_API_KEY}"'
```

---

## Getting Dataset IDs

To use the scraping features, you need a `dataset_id`:

1. Go to [Bright Data Control Panel](https://brightdata.com/cp/datasets)
2. Create a new Web Scraper dataset or select an existing one
3. Choose the platform (Twitter, Reddit, YouTube, etc.)
4. Copy the `dataset_id` from the dataset settings

Dataset IDs can also be found in the bandwidth usage API response under the `data` field keys (e.g., `v__ds_api_gd_xxxxx` where `gd_xxxxx` is your dataset ID).

---

## Common Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `url` | Target URL to scrape | `https://twitter.com/user` |
| `keyword` | Search keyword | `"artificial intelligence"` |
| `num_of_posts` | Limit number of results | `50` |
| `start_date` | Filter by date (MM-DD-YYYY) | `"01-01-2024"` |
| `end_date` | Filter by date (MM-DD-YYYY) | `"12-31-2024"` |
| `sort_by` | Sort order (Reddit) | `new`, `top`, `hot` |
| `format` | Response format | `json`, `csv` |

---

## Rate Limits

- Batch mode: up to 100 concurrent requests
- Maximum input size: 1GB per batch
- Exceeding limits returns `429` error

---

## Guidelines

1. **Create datasets first**: Use the Control Panel to create scraper datasets
2. **Use async for large jobs**: Use `/trigger` for discovery and batch operations
3. **Use sync for small jobs**: Use `/scrape` for single URL quick lookups
4. **Check status before download**: Poll `/progress` until status is `ready`
5. **Respect rate limits**: Don't exceed 100 concurrent requests
6. **Date format**: Use MM-DD-YYYY for date parameters

## Guardrails

**Source & Attribution**
- This skill integrates the **Bright Data Web Scraper API** (https://brightdata.com/), a third-party commercial data collection service.
- Official documentation: https://docs.brightdata.com/
- All API calls are made to `https://api.brightdata.com` — no data is stored or processed locally beyond what the user requests.
- Users must have a valid Bright Data account and API key. Usage is subject to Bright Data's terms of service and pricing.

**Anti-patterns**
- NEVER hardcode or expose the user's API key in scripts or output — always use the `BRIGHTDATA_API_KEY` environment variable.
- Do NOT exceed 100 concurrent requests in batch mode — respect rate limits (429 errors).
- NEVER use Bright Data for scraping personal data beyond what is publicly available and permitted by applicable laws and platform terms.
- Do NOT fabricate dataset_id or snapshot_id values — these must come from the Bright Data Control Panel or API responses.

**Constraints**
- When using `$VAR` in a piped command, wrap in `bash -c '...'` to prevent environment variable loss.
- Always create a Web Scraper dataset in the Bright Data Control Panel before using scraping endpoints.
- Use async (`/trigger`) for large/batch jobs, sync (`/scrape`) for single-URL quick lookups.
- Poll `/progress` until status is `ready` before downloading results.
- Clean up `/tmp/brightdata_request.json` after use.

## Related Skills

- **x-twitter-scraper** — X (Twitter) API integration for read/write operations, posting tweets, DMs, and real-time monitoring (complementary to Bright Data's X scraping).
- **gh-cli** — GitHub CLI reference for repository, issue, PR, and Actions operations.
- **find-skills** — Discover and install additional agent skills from the open ecosystem.

## About UniqueClub

Part of the UniqueClub toolkit. This skill wraps a third-party API for convenience within the UniqueClub skill ecosystem.
🌐 https://uniqueclub.ai
