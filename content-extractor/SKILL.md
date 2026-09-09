---
name: content-extractor
description: |
  多平台内容抓取与提取的统一中心，支持小宇宙播客、抖音、微信公众号、B站、小红书等平台的内容提取、批量下载和归档。
  Use when: "提取播客内容", "下载抖音视频", "抓取公众号文章", "content extraction", "batch download media", "多平台内容聚合", "social media scraping", "内容归档备份".
  支持快速模式和完整模式，返回标题、媒体URL、文本内容和元数据。Cross-references: wechat-article-fetcher, twitter-scraper, rss-feed, document-hub, pdf.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Content Extractor — 统一内容提取中心

> 多平台内容抓取与提取：小宇宙播客、抖音、微信公众号、B站、小红书。

## When to Use

Use this skill when:
- 需要从小宇宙、抖音、微信公众号、B站、小红书等平台提取内容
- 批量下载音频、视频或文章进行归档
- 将社交媒体内容转换为可编辑的文档格式
- 收集多平台素材用于报告或研究
- 需要提取媒体文件的直接下载链接
- 监控和抓取公开的社交媒体内容

Do NOT use this skill if:
- 需要访问私密/受保护的内容（需要登录态）→ 确认登录态后再使用
- 抓取频率过高可能触发平台反爬机制 → 控制批量速率
- 内容涉及版权限制或付费墙 → 不抓取付费内容
- 需要实时抓取大量数据（有速率限制）
- 目标平台需要特殊认证（如企业账号）

Typical triggers:
- 「帮我提取小宇宙播客内容」「下载这个抖音视频」「抓取公众号文章」
- "Extract podcast content", "Download video from URL", "Scrape WeChat article"
- 「批量获取B站视频信息」「提取小红书笔记」「多平台内容汇总」
- "Batch extract social media", "Get media download links", "Aggregate content"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户提供的URL列表，确认目标平台和提取需求。检测平台类型：
```python
from skills.content_extractor.content_extractor import detect_platform

platform = detect_platform("https://www.xiaoyuzhoufm.com/episode/xxx")
# Returns: Platform.XIAOYUZHOU, Platform.DOUYIN, etc.
```

2. **约束 (Constrain)**
验证URL有效性，设定提取模式和边界。受阻时换通道，不降级交付物。

| 模式 | 速度 | 完整度 | 适用场景 |
|------|------|--------|----------|
| **快速模式** (extract/extract_fast) | 3-5秒 | ⭐⭐⭐ | 仅需要标题+媒体URL |
| **完整模式** (extract_full) | 10-30秒 | ⭐⭐⭐⭐⭐ | 需要详细描述和元数据 |

3. **证据 (Evidence)**
每个提取结果必须来自实际平台响应，不编造内容。收集平台返回的原始数据作为证据。

4. **执行 (Execute)**
调用提取脚本，先给影响与结论，再给行动和必要证据。
```python
from skills.content_extractor.content_extractor import extract, extract_full

# 快速模式 - 推荐用于音频下载
result = extract("https://www.xiaoyuzhoufm.com/episode/xxx")

# 完整模式 - 推荐用于内容分析
result = extract_full("https://mp.weixin.qq.com/s/xxx")
```

结果处理：
```python
print(result.title)           # 标题
print(result.media_urls)      # 媒体下载链接
print(result.content)         # 文本内容
print(result.author)          # 作者
print(result.metadata)        # 完整元数据
```

批量处理（可选）：
```python
from skills.content_extractor.content_extractor import batch_extract

urls = [url1, url2, url3]
results = batch_extract(urls, download_media=False)
```

5. **验证 (Verify)**
用不同于生成路径的方式回读输出——检查提取结果的标题非空、媒体URL可访问、内容长度合理。批量提取时抽查至少20%的结果。

6. **交付 (Deliver)**
返回结构化结果，清理临时下载文件（如设置了download_media=True且不需要保留）。

## Output

返回 `ExtractResult` 数据结构：
```python
@dataclass
class ExtractResult:
    platform: Platform          # 平台类型
    title: str                  # 标题
    content: str                # 内容/描述
    author: Optional[str]       # 作者
    publish_time: Optional[str] # 发布时间
    media_urls: List[str]       # 音频/视频URL列表
    images: List[str]           # 图片URL列表
    metadata: Dict[str, Any]    # 元数据（包含原始URL等）
```

批量提取返回 `List[ExtractResult]`。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 频繁抓取同一平台（可能触发反爬），批量提取时添加适当延迟
- NEVER 抓取付费或版权保护内容
- Do NOT 将下载内容用于商业用途
- Do NOT 不处理提取失败的情况，始终捕获 `ExtractError` 异常

**Constraints**
- 部分平台链接有时效性，过期后无法提取
- 需要 Playwright 环境支持完整模式
- 不处理图片/视频下载（仅返回URL，除非显式设置download_media）
- 首次使用需要安装浏览器依赖：`pip install playwright requests && playwright install chromium`

**Safety Rules**
1. **版权合规**: 下载内容仅供个人学习使用
2. **反爬友好**: 批量提取时添加适当延迟
3. **错误处理**: 始终捕获 ExtractError 异常
4. **隐私保护**: 不抓取用户私密内容

## Core Features

**1. 单链接提取**

#### 快速模式（推荐）
```python
from skills.content_extractor.content_extractor import extract, extract_fast

# 快速提取（默认）- 使用curl直接获取音频URL，速度最快
result = extract("https://www.xiaoyuzhoufm.com/episode/xxx")
print(result.title)           # 播客标题
print(result.media_urls)      # 音频下载链接
print(result.author)          # 播客名称

# 快速提取 + 下载音频
result = extract_fast(
    "https://www.xiaoyuzhoufm.com/episode/xxx",
    download=True,
    save_path="./downloads"
)
```

#### 完整模式（需要Playwright）
```python
from skills.content_extractor.content_extractor import extract_full

# 完整提取 - 使用浏览器渲染，获取更完整的信息
result = extract_full("https://www.xiaoyuzhoufm.com/episode/xxx")
print(result.content)         # 详细描述
print(result.metadata)        # 完整元数据
```

**2. 批量提取**
```python
from skills.content_extractor.content_extractor import batch_extract

urls = [
    "https://www.xiaoyuzhoufm.com/episode/xxx",
    "https://mp.weixin.qq.com/s/xxx",
    "https://www.bilibili.com/video/xxx",
]

results = batch_extract(urls, download_media=False)
for result in results:
    print(f"{result.platform.value}: {result.title}")
```

**3. 平台检测**
```python
from skills.content_extractor.content_extractor import detect_platform

platform = detect_platform("https://www.xiaoyuzhoufm.com/episode/xxx")
print(platform)  # Platform.XIAOYUZHOU
```

## 支持的平台

| 平台 | 支持内容 | 音频 | 视频 | 文字 | 图片 |
|------|---------|------|------|------|------|
| 小宇宙 | 播客 | ✅ | - | ✅ | - |
| 抖音 | 短视频 | ✅ | ✅ | - | - |
| 微信公众号 | 文章 | - | ✅ | ✅ | ✅ |
| B站 | 视频 | ✅ | ✅ | ✅ | - |
| 小红书 | 笔记 | - | ✅ | ✅ | ✅ |

## Options Parameters

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `download_media` | bool | False | 是否下载音视频 |
| `save_path` | str | None | 下载保存路径 |
| `extract_text` | bool | True | 是否提取文字内容 |

## Error Handling

```python
from skills.content_extractor.content_extractor import ExtractError

try:
    result = extract("https://invalid-url.com")
except ExtractError as e:
    print(f"提取失败: {e}")
```

## Workflow Integration Examples

**Workflow 1: 播客内容提取 → 生成文档**
```python
from skills.content_extractor.content_extractor import extract
from skills.document_hub.document_hub import write

# 提取播客
result = extract("https://www.xiaoyuzhoufm.com/episode/xxx")

# 生成Word文档
content = {
    "title": result.title,
    "paragraphs": [
        f"来源：小宇宙播客",
        f"作者：{result.author}",
        "",
        "内容描述：",
        result.content
    ]
}
write("播客笔记.docx", content)
```

**Workflow 2: 多平台内容汇总 → Excel**
```python
from skills.content_extractor.content_extractor import batch_extract

urls = [
    "https://www.xiaoyuzhoufm.com/episode/xxx",
    "https://mp.weixin.qq.com/s/xxx",
    "https://www.bilibili.com/video/xxx",
]

results = batch_extract(urls)

# 汇总到Excel
excel_data = []
for result in results:
    excel_data.append({
        "平台": result.platform.value,
        "标题": result.title,
        "作者": result.author,
    })

write("内容汇总.xlsx", {"sheets": {"内容汇总": {"data": excel_data}}})
```

## Extending New Platforms

```python
# 在 ContentExtractor 类中添加新的提取方法
def _extract_new_platform(self, url: str, **options) -> ExtractResult:
    # 实现提取逻辑
    return ExtractResult(
        platform=Platform.NEW_PLATFORM,
        title="...",
        content="...",
        metadata={"url": url}
    )

# 在 __init__ 中注册
self.extractors[Platform.NEW_PLATFORM] = self._extract_new_platform
```

## Related Skills

- **wechat-article-fetcher** — 专门用于微信公众号文章抓取的专用替代
- **twitter-scraper** — 抓取Twitter/X平台内容的平台扩展
- **rss-feed** — RSS订阅源解析，作为无专用提取器平台的补充
- **document-hub** — 下游处理：将提取内容生成Word/Excel文档
- **pdf** — 下游处理：将内容转换为PDF格式

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
