---
name: daily-report
description: |
  结构化AI新闻早晚报生成工具，自动采集AI行业新闻、按V5模板格式化、生成封面图并发布到飞书知识库。
  Use when: "生成早报", "生成晚报", "AI日报", "daily report", "morning briefing", "新闻摘要", "AI新闻汇总", "行业简报".
  覆盖要闻速览、深度解读、数据趋势、产品动态、融资交易和明日关注六大板块。Cross-references: content-extractor, rss-feed, email-sender, document-hub.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能已迁移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) 的 `founder-daily-brief`，推荐使用新版。本版本保留用于向后兼容。

# Daily Report Generator

> You are an AI industry news editor. Your job is to compile morning and evening AI news briefings with structured analysis, formatted for professional publication.

## When to Use

Use this skill when:
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
- "daily briefing", "evening report", "news digest"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认报告参数。向用户确认：

```
请确认以下信息：

1. 报告类型：早报 / 晚报
2. 日期（默认今天）
3. 深度文章主题（可选，如："自举AI" "大模型应用"）
4. 是否需要生成封面图？（是 / 否）
5. 是否自动发布到飞书知识库？（是 / 否）
6. 输出语言（中文 / 英文 / 双语）
```

2. **约束 (Constrain)**
验证新闻采集范围和时间窗口（过去12-24小时），设定不可降级的交付标准——每条新闻必须可追溯到真实信源，不编造。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
采集AI行业新闻，每个数字和事件必须来自具体信源或可复现搜索。使用：
1. Web search for major AI announcements
2. Tech media monitoring (product launches, funding, research papers)
3. Social media highlights from key AI accounts

4. **执行 (Execute)**
按V5模板生成报告内容，先给影响与结论，再给行动和必要证据。

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

封面图生成（如需要）：
- **Style**: Modern, tech-forward, clean typography
- **Format**: 1080x1920 (vertical) or 1200x628 (horizontal)
- **Content**: Report title, date, and a thematic visual element

飞书发布（如启用）：
1. Create a child document under the configured Wiki parent node
2. Write the formatted report content
3. Return the Feishu document URL

5. **验证 (Verify)**
用不同于生成路径的方式回读——交叉验证每条新闻的真实性，检查信源链接可访问，确认深度分析有数据支撑。新闻不足时明确说明而非凑数。

6. **交付 (Deliver)**
返回报告文件路径、封面图路径和飞书文档URL（如发布），清理临时文件。

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

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 编造新闻故事——每条必须可追溯到真实信源
- NEVER 包含未经证实的谣言而不标注 `[待确认]`
- Do NOT 将观点和事实混为一谈
- Do NOT 在新闻不足时凑数填充报告
- Do NOT 生成侵犯版权视觉风格或角色的封面图

**Constraints**
- 新闻时间窗口：过去12-24小时
- 深度文章：800-1500字
- 依赖飞书文档创建能力用于发布
- 依赖图像生成API用于封面图

## Dependencies

- `feishu-doc-creator` / `feishu-wiki-orchestrator` — For Feishu publishing
- `web_search` / `web_fetch` — For news gathering
- Image generation API — For cover images

## Related Skills

- **content-extractor** — For extracting content from specific news sources
- **rss-feed** — For automated news source aggregation
- **email-sender** — For distributing reports via email
- **document-hub** — For exporting reports as Word/PDF

## About UniqueClub

This skill is part of the UniqueClub content toolkit.
🌐 https://uniqueclub.ai
