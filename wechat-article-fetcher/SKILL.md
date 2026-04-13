---
name: wechat-article-fetcher
description: |
  微信公众号文章抓取工具，基于Playwright绕过微信反爬机制，获取完整文章内容。
  
  Use when:
  - 抓取微信公众号文章内容 fetch WeChat article content
  - 批量获取公众号文章 batch fetch WeChat articles
  - 公众号内容归档 archive WeChat content
  - 文章素材收集 article material collection
  - 绕过微信反爬 bypass WeChat anti-crawling
  - 微信文章转Markdown convert WeChat to Markdown
  
  Cross-references: content-extractor, document-hub, pdf, md-to-wechat, long-form-writer
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

> 🚀 **Migrated to [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) as `china-content-research`.**
> 
> This version is kept for backward compatibility. For the latest updates, use the founder-skills version.



# WeChat Article Fetcher

微信公众号文章抓取工具，基于 Playwright，可绕过微信的反爬机制获取完整文章内容。

## When to Use

### Use This Skill When
- 需要抓取微信公众号完整文章内容
- 批量获取多个公众号文章
- 将微信文章保存为Markdown格式
- 收集公众号文章作为研究素材
- 微信文章需要离线存档
- 其他方法（如web_fetch）无法获取内容

### Do NOT Use This Skill If
- 链接已过期或失效
- 文章需要登录才能查看
- 需要抓取大量文章（建议控制频率）
- 目标文章是临时分享链接（含tempkey参数）
- 网络环境不稳定

### Typical Trigger Phrases
**Chinese:**
- "抓取公众号文章"
- "获取微信文章内容"
- "下载公众号文章"
- "微信文章转Markdown"
- "批量抓取微信文章"
- "保存公众号文章"

**English:**
- "Fetch WeChat article"
- "Scrape WeChat content"
- "Download WeChat article"
- "WeChat to Markdown"
- "Batch fetch WeChat"
- "Archive WeChat article"

## Workflow

### Step 1: 准备URL
- 确保URL有效（非临时链接）
- 检查链接是否过期
- 确认文章是公开访问

### Step 2: 执行抓取
```python
from skills.wechat_article_fetcher.wechat_fetcher import fetch_wechat_article

result = fetch_wechat_article(url="https://mp.weixin.qq.com/s/xxxxx")
```

### Step 3: 处理结果
```python
if result['success']:
    print(f"标题: {result['title']}")
    print(f"内容: {result['content'][:500]}")
```

### Step 4: 保存文件（可选）
- Markdown格式
- 纯文本格式
- 导入其他系统

## Guardrails

### Anti-Patterns
- ❌ 频繁抓取触发反爬
- ❌ 抓取付费或私密内容
- ❌ 不处理抓取失败的情况
- ❌ 使用过期临时链接

### Limitations
- 需要安装Chromium（约100MB）
- 首次运行需下载浏览器
- 不处理图片/视频，仅提取文本
- 临时分享链接会过期

### Technical Constraints
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

### Command Line
```bash
# 基本用法
python3 skills/wechat-article-fetcher/wechat_fetcher.py \
  "https://mp.weixin.qq.com/s/xxxxx"

# 保存到文件
python3 skills/wechat-article-fetcher/wechat_fetcher.py \
  "https://mp.weixin.qq.com/s/xxxxx" \
  -o "output/article.md"
```

### Python API
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

## Return Format

```python
{
    'title': '文章标题',
    'content': '完整正文内容（纯文本）',
    'url': '原始链接',
    'fetch_time': '2026-02-12 11:00:00',
    'success': True
}
```

## Why Playwright?

| Method | Feasibility | Notes |
|--------|-------------|-------|
| `web_fetch` | ❌ | 微信反爬，只能获取标题 |
| `browser` (Chrome) | ⚠️ | 需要连接已授权的Chrome实例 |
| `Playwright` | ✅ | 模拟真实浏览器，稳定可靠 |

### Scraping Strategy
1. 启动 headless Chromium
2. 访问目标URL，等待网络空闲
3. 执行JS提取正文（`#js_content`选择器）
4. 返回纯文本内容

## Use Cases

### Use Case 1: 写书项目素材收集
```python
import os
from datetime import datetime

url = "https://mp.weixin.qq.com/s/xxxxx"
filename = f"article-{datetime.now().strftime('%Y%m%d')}.md"
output_path = f"01-Projects/book-openclaw/01-raw-materials/community-cases/{filename}"

os.makedirs(os.path.dirname(output_path), exist_ok=True)
result = fetch_wechat_article(url, output_path)
```

### Use Case 2: 批量抓取
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

### Use Case 3: 子Agent任务
```
使用 wechat-article-fetcher skill 抓取链接 https://mp.weixin.qq.com/s/xxxxx
保存到 01-Projects/book-openclaw/01-raw-materials/community-cases/
```

## Troubleshooting

### Issue: Chromium Not Found
```bash
playwright install chromium
```

### Issue: Empty Content
- 检查链接是否有效（非临时链接）
- 临时分享链接（含`tempkey`参数）会过期
- 尝试使用原始永久链接

### Issue: Timeout Error
- 网络问题，重试即可
- 微信服务器偶尔响应慢

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 通用替代 | 多平台内容提取 |
| **document-hub** | 下游处理 | 将文章生成Word/PDF |
| **pdf** | 格式转换 | 文章转PDF存档 |
| **md-to-wechat** | 反向操作 | 将Markdown发公众号 |
| **long-form-writer** | 内容加工 | 基于文章素材写作 |

## Changelog

### v1.0.0 (2026-02-12)
- 初始版本
- 基于Playwright实现微信文章抓取
- 支持命令行和Python API

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
