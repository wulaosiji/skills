---
name: wechat-article-fetcher
description: |
  微信公众号文章抓取工具，基于Playwright绕过微信反爬机制，获取完整文章内容，支持批量抓取和Markdown导出。
  Use when: "抓取公众号文章", "获取微信文章内容", "微信文章转Markdown", "fetch WeChat article", "scrape WeChat content", "批量抓取微信文章", "WeChat to Markdown", "公众号内容归档".
  基于Playwright模拟真实浏览器，稳定绕过微信反爬。Cross-references: content-extractor, rss-feed, document-hub, pdf.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能已迁移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) 的 `china-content-research`，推荐使用新版。本版本保留用于向后兼容。

# WeChat Article Fetcher

> 微信公众号文章抓取工具，基于 Playwright，可绕过微信的反爬机制获取完整文章内容。

## When to Use

Use this skill when:
- 需要抓取微信公众号完整文章内容
- 批量获取多个公众号文章
- 将微信文章保存为Markdown格式
- 收集公众号文章作为研究素材
- 微信文章需要离线存档
- 其他方法（如web_fetch）无法获取内容

Do NOT use this skill if:
- 链接已过期或失效 → 使用原始永久链接
- 文章需要登录才能查看 → 不抓取私密内容
- 需要抓取大量文章（建议控制频率）→ 分批执行
- 目标文章是临时分享链接（含tempkey参数）→ 链接会过期
- 网络环境不稳定 → 重试或等待网络恢复

Typical triggers:
- 「抓取公众号文章」「获取微信文章内容」「下载公众号文章」
- "Fetch WeChat article", "Scrape WeChat content", "Download WeChat article"
- 「微信文章转Markdown」「批量抓取微信文章」「保存公众号文章」
- "WeChat to Markdown", "Batch fetch WeChat", "Archive WeChat article"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户提供的URL，确认目标和约束：
- 确保URL有效（非临时链接）
- 检查链接是否过期
- 确认文章是公开访问

2. **约束 (Constrain)**
验证输入完整性，设定抓取频率和边界。临时链接（含tempkey）会过期，必须使用原始永久链接。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
每个抓取结果必须来自微信服务器实际响应，不编造文章内容。记录抓取时间和原始URL作为可追溯证据。

4. **执行 (Execute)**
调用抓取脚本，先给影响与结论，再给行动和必要证据。
```python
from skills.wechat_article_fetcher.wechat_fetcher import fetch_wechat_article

result = fetch_wechat_article(url="https://mp.weixin.qq.com/s/xxxxx")
```

处理结果：
```python
if result['success']:
    print(f"标题: {result['title']}")
    print(f"内容: {result['content'][:500]}")
```

保存文件（可选）：
- Markdown格式
- 纯文本格式
- 导入其他系统

5. **验证 (Verify)**
用不同于生成路径的方式回读输出——检查返回的success字段为True，标题非空，内容长度合理（>100字符）。批量抓取时抽查每个结果。

6. **交付 (Deliver)**
返回结构化结果，清理临时浏览器进程。

## Output

返回字典格式：
```python
{
    'title': '文章标题',
    'content': '完整正文内容（纯文本）',
    'url': '原始链接',
    'fetch_time': '2026-02-12 11:00:00',
    'success': True
}
```

如指定 `output_path`，同时将内容写入Markdown文件。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 频繁抓取触发反爬，建议控制抓取频率
- NEVER 抓取付费或私密内容
- Do NOT 不处理抓取失败的情况，始终检查 `result['success']`
- Do NOT 使用过期临时链接（含tempkey参数）

**Constraints**
- 需要安装Chromium（约100MB），首次运行需下载浏览器
- 不处理图片/视频，仅提取文本
- 临时分享链接会过期
- 依赖Playwright和Chromium环境

**Technical Constraints**
1. **浏览器依赖**: 需要Playwright和Chromium
2. **链接时效**: 临时链接（含tempkey）会过期
3. **内容限制**: 仅提取文本，不下载媒体
4. **频率限制**: 建议控制抓取频率

## Installation

```bash
pip install playwright
playwright install chromium
```

## Usage

**Command Line**
```bash
# 基本用法
python3 skills/wechat-article-fetcher/wechat_fetcher.py \
  "https://mp.weixin.qq.com/s/xxxxx"

# 保存到文件
python3 skills/wechat-article-fetcher/wechat_fetcher.py \
  "https://mp.weixin.qq.com/s/xxxxx" \
  -o "output/article.md"
```

**Python API**
```python
from skills.wechat_article_fetcher.wechat_fetcher import fetch_wechat_article

result = fetch_wechat_article(
    url="https://mp.weixin.qq.com/s/xxxxx",
    output_path="output/article.md"
)

if result['success']:
    print(f"标题: {result['title']}")
    print(f"内容: {result['content'][:500]}")
```

## Why Playwright?

| Method | Feasibility | Notes |
|--------|-------------|-------|
| `web_fetch` | ❌ | 微信反爬，只能获取标题 |
| `browser` (Chrome) | ⚠️ | 需要连接已授权的Chrome实例 |
| `Playwright` | ✅ | 模拟真实浏览器，稳定可靠 |

**Scraping Strategy**
1. 启动 headless Chromium
2. 访问目标URL，等待网络空闲
3. 执行JS提取正文（`#js_content`选择器）
4. 返回纯文本内容

## Use Cases

**Use Case 1: 写书项目素材收集**
```python
import os
from datetime import datetime

url = "https://mp.weixin.qq.com/s/xxxxx"
filename = f"article-{datetime.now().strftime('%Y%m%d')}.md"
output_path = f"01-Projects/book-openclaw/01-raw-materials/community-cases/{filename}"

os.makedirs(os.path.dirname(output_path), exist_ok=True)
result = fetch_wechat_article(url, output_path)
```

**Use Case 2: 批量抓取**
```python
urls = [
    "https://mp.weixin.qq.com/s/xxx1",
    "https://mp.weixin.qq.com/s/xxx2",
    "https://mp.weixin.qq.com/s/xxx3",
]

for url in urls:
    result = fetch_wechat_article(url)
    print(f"✅ {result['title']}" if result['success'] else f"❌ 失败: {url}")
```

**Use Case 3: 子Agent任务**
```
使用 wechat-article-fetcher skill 抓取链接 https://mp.weixin.qq.com/s/xxxxx
保存到 01-Projects/book-openclaw/01-raw-materials/community-cases/
```

## Troubleshooting

**Issue: Chromium Not Found**
```bash
playwright install chromium
```

**Issue: Empty Content**
- 检查链接是否有效（非临时链接）
- 临时分享链接（含`tempkey`参数）会过期
- 尝试使用原始永久链接

**Issue: Timeout Error**
- 网络问题，重试即可
- 微信服务器偶尔响应慢

## Related Skills

- **content-extractor** — 通用替代：多平台内容提取，支持微信在内的多个平台
- **rss-feed** — 数据来源补充：通过RSS订阅获取公众号更新
- **document-hub** — 下游处理：将文章生成Word/PDF文档
- **pdf** — 格式转换：文章转PDF存档

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
