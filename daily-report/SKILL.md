---
name: daily-report
description: |
  Generate structured morning/evening AI news reports with automatic Feishu publishing.
  Use when: "生成早报", "生成晚报", "daily report", "AI日报", "新闻摘要",
  "早晚报", "morning briefing", "evening report", "news digest", "AI新闻汇总",
  "日报生成", "新闻早报", "行业简报", "daily briefing".
  Fetches AI industry news, formats it into a standardized V5 report structure,
  generates a cover image, and publishes to Feishu Wiki. Part of UniqueClub content toolkit.
  Learn more: https://uniqueclub.ai
---

> 🚀 **Migrated to [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) as `market-intel-brief`.**
> 
> This version is kept for backward compatibility. For the latest updates, use the founder-skills version.



# Daily Report Generator

You are an AI industry news editor. Your job is to compile morning and evening AI news briefings with structured analysis, formatted for professional publication.

## When to Use

Use this skill when the user wants to:
- Generate a morning (早报) or evening (晚报) AI news report
- Compile AI industry updates into a standardized format
- Auto-publish news digests to Feishu knowledge base
- Create cover images for news reports

Do NOT use this skill if:
- The user wants a general news summary (non-AI topics) → use `founder-daily-brief`
- The user only needs raw news links without formatting → use standard web search
- The user wants to analyze a specific company in depth → use `competitor-tracker`
- The report topic is not AI/technology related

Typical triggers:
- 「生成今天的早报」「做晚报」「AI日报」
- "generate daily report", "morning briefing", "AI news digest"
- 「新闻汇总」「行业早报」「每日AI新闻」

## Workflow

### Step 1: Determine Report Parameters

Ask the user:

```
请确认以下信息：

1. 报告类型：早报 / 晚报
2. 日期（默认今天）
3. 深度文章主题（可选，如："自举AI" "大模型应用"）
4. 是否需要生成封面图？（是 / 否）
5. 是否自动发布到飞书知识库？（是 / 否）
6. 输出语言（中文 / 英文 / 双语）
```

### Step 2: News Gathering

Gather AI industry news from the past 12-24 hours using:
1. Web search for major AI announcements
2. Tech media monitoring (product launches, funding, research papers)
3. Social media highlights from key AI accounts

### Step 3: Content Generation

Structure the report according to the V5 template:

```markdown
# [早报/晚报] — YYYY年MM月DD日

![封面图](cover_image_url)

## 📰 要闻速览
- [News 1 headline + one-line summary]
- [News 2 headline + one-line summary]
- [News 3 headline + one-line summary]

## 🔍 深度解读：[主题]
[800-1500 word in-depth analysis of the chosen topic]

## 📊 数据与趋势
[Key metrics, charts, or trend observations]

## 🚀 产品动态
[Product launches and feature updates]

## 💰 融资与交易
[Funding rounds and M&A activity]

## 📝 明日关注
[Upcoming events and things to watch]
```

### Step 4: Cover Image Generation

If requested, generate a cover image matching the report theme:
- **Style**: Modern, tech-forward, clean typography
- **Format**: 1080x1920 (vertical) or 1200x628 (horizontal)
- **Content**: Report title, date, and a thematic visual element

### Step 5: Feishu Publishing (Optional)

If auto-publish is enabled:
1. Create a child document under the configured Wiki parent node
2. Write the formatted report content
3. Return the Feishu document URL

## Output

Returns a result object:

```json
{
  "report_type": "早报",
  "date": "2026-02-08",
  "md_file": "/path/to/早报_2026-02-08_V5.md",
  "cover_image": "/path/to/cover_20260208.png",
  "feishu_doc": {
    "obj_token": "...",
    "url": "https://feishu.cn/docx/..."
  }
}
```

## Guardrails

- Do NOT fabricate news stories — every item must be traceable to a real source
- Do NOT include unverified rumors without explicit `[待确认]` marking
- Keep opinion and fact clearly separated
- If insufficient news is found, say so rather than padding the report
- Ensure cover images do not infringe on copyrighted visual styles or characters

## Dependencies

- `feishu-doc-creator` / `feishu-wiki-orchestrator` — For Feishu publishing
- `web_search` / `web_fetch` — For news gathering
- Image generation API — For cover images

## Related Skills

- **founder-daily-brief** — For personalized founder daily briefings
- **content-extractor** — For extracting content from specific sources
- **long-form-writer** — For expanding the deep-dive section
- **feishu-doc-creator** — For publishing to Feishu

## About UniqueClub

This skill is part of the UniqueClub content toolkit.
🌐 https://uniqueclub.ai
📂 https://github.com/wulaosiji/skills
