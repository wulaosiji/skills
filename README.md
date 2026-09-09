![bef1edad6138ccfb53759a4158f2b280](https://github.com/user-attachments/assets/33afb497-32f5-4fe6-baa2-4b3af018460e)

# OpenClaw Skills - 技能仓库

> 50 个顶层 AI Agent 技能（含 12 个嵌套子技能、5 个第三方技能，共 67 个 SKILL.md），即拿即用。全部通过 7 维质量审计（100/100）。

---

## 🎯 这是什么

这是 **OpenClaw** 的官方技能仓库，包含 50 个可直接使用的自定义顶层技能，覆盖飞书生态、内容生成、数据抓取、安全加固等场景。

特别推荐：[UniqueClub 创业者工具包](https://github.com/wulaosiji/founder-skills) — 专为 AI 创业者设计的融资、内容、增长一站式技能套件（24 个技能）。https://uniqueclub.ai

每个技能都经过 7 维质量审计（命名、描述、使用边界、工作流、输出、约束、关联技能），配有完整的 SKILL.md 文档和可执行脚本。

---

## 📊 技能统计

| 分类 | 数量 | 说明 |
|------|------|------|
| 🔵 飞书生态 | 15 | feishu-* 系列，含文档编排、群聊管理、消息发送 |
| 🎨 内容生成与媒体 | 13 | 视频/照片生成、长文写作、OCR、语音、媒体处理 |
| 📊 数据处理与抓取 | 7 | 多平台抓取、PDF、文档中心、逻辑校验 |
| 📰 报告与工具 | 6 | 日报、技能优化、日历、购物、邮件、导航 |
| 🛡️ 系统与安全 | 4 | 安全加固、审计、密钥管理、攻防演练 |
| ⚠️ 已迁移商业技能 | 5 | BP/演示类，已迁移至 founder-skills |
| 🔗 第三方技能 | 5 | bright-data、gh-cli、remotion 等 |
| **顶层技能合计** | **50** | 不含嵌套子技能和第三方 |
| 📦 嵌套子技能 | 12 | feishu-doc-orchestrator / feishu-wiki-orchestrator 内部组件 |
| **SKILL.md 总计** | **67** | 含顶层 + 嵌套 + 第三方 |

---

## 📦 技能分类

### 🔵 飞书生态（15个）

| 技能 | 一句话介绍 | 触发关键词 |
|------|-----------|-----------|
| [feishu-doc-orchestrator](feishu-doc-orchestrator/) | 飞书文档创建主编排，含块解析、验证、日志的完整流水线 | "创建飞书文档", "markdown转飞书", "批量导入文档", "飞书文档排版" |
| [feishu-wiki-orchestrator](feishu-wiki-orchestrator/) | 飞书知识库文档创建编排，支持批量导入和权限管理 | "创建知识库文档", "飞书知识库", "wiki转飞书", "导入知识库" |
| [feishu-doc-creator](feishu-doc-creator/) | 飞书文档创建统一入口，支持云文档/Wiki、自动写入和权限 | "创建飞书文档", "飞书写文档", "feishu doc", "飞书云文档" |
| [feishu-doc](feishu-doc/) | 飞书文档只读工具，提取内容和表格数据 | "读取飞书文档", "提取文档内容", "飞书文档预览", "获取表格数据" |
| [feishu-doc-converter](feishu-doc-converter/) | 飞书文档格式转换，支持 Markdown↔飞书双向转换 | "飞书文档转Markdown", "markdown转飞书", "链接转Markdown", "批量文档转换" |
| [feishu-doc-perm](feishu-doc-perm/) | 飞书文档权限管理，批量添加协作者和共享设置 | "飞书文档权限", "添加协作者", "文档共享设置", "批量权限管理" |
| [feishu-pdf-downloader](feishu-pdf-downloader/) | 通过文件 token 从飞书云盘批量下载 PDF 及其他文件 | "下载飞书文件", "飞书PDF下载", "云盘文件导出", "文件token下载" |
| [feishu-chat-extractor](feishu-chat-extractor/) | 提取并分析飞书群聊历史消息，支持导出和检索 | "提取聊天记录", "分析群消息", "飞书聊天导出", "消息历史检索" |
| [feishu-chat-monitor](feishu-chat-monitor/) | 检查群聊遗漏的 @提及 消息并自动发送补回复 | "检查遗漏消息", "补回复飞书", "监控@消息", "群聊消息检查" |
| [feishu-card-parser](feishu-card-parser/) | 飞书卡片消息解析器，提取富文本和图片链接 | "解析飞书卡片", "卡片消息提取", "富文本转Markdown", "提取图片链接" |
| [feishu-group-welcome](feishu-group-welcome/) | 飞书群聊新成员欢迎工具，支持批量 @用户 | "群聊欢迎", "新成员欢迎", "批量@用户", "自动发欢迎语" |
| [feishu-message-recall](feishu-message-recall/) | 飞书消息撤回/删除工具，支持批量撤回和话题清理 | "撤回飞书消息", "删除群消息", "批量撤回", "清理误发消息" |
| [feishu-voice-sender](feishu-voice-sender/) | 飞书语音消息发送，支持 MP3 转语音条和群发 | "发送语音消息", "飞书语音条", "MP3转飞书语音", "语音通知" |
| [feishu-video-sender](feishu-video-sender/) | 飞书视频消息发送，支持上传、封面生成和群分享 | "发送视频消息", "飞书视频播放", "上传视频到飞书", "群视频分享" |
| [feishu-bitable-field](feishu-bitable-field/) | 飞书多维表格字段管理，批量创建和配置表格列 | "多维表格字段", "创建多维表格列", "飞书多维表格", "字段配置" |

### 🎨 内容生成与媒体（13个）

| 技能 | 一句话介绍 | 触发关键词 |
|------|-----------|-----------|
| [video-generation](video-generation/) | AI 视频生成与处理，支持图生视频、视频续写、4K 超分 | "AI视频生成", "图生视频", "视频超分", "4K视频", "视频续写" |
| [zhuoran-selfie](zhuoran-selfie/) | 卓然风格 AI 自拍照片生成，支持垫图和角色照片 | "卓然自拍", "AI照片生成", "角色照片", "垫图生成", "场景自拍" |
| [zhuoran-video-selfie](zhuoran-video-selfie/) | 卓然风格 AI 自拍视频生成，活人感动态视频 | "卓然视频", "AI视频生成", "动态自拍", "活人感视频", "视频自拍" |
| [clawra-selfie](clawra-selfie/) | Clawra 风格 AI 自拍照片生成，支持参考图 | "AI照片生成", "自拍生成", "角色照片", "clawra selfie", "垫图生成" |
| [clawra-video-selfie](clawra-video-selfie/) | Clawra 风格 AI 自拍视频生成 | "AI视频生成", "自拍视频", "动态自拍", "clawra video", "角色视频" |
| [qizhuo-selfie](qizhuo-selfie/) | 奇卓风格 AI 自拍照片，守护型温暖风格 | "奇卓自拍", "守护型照片", "AI角色照片", "火焰符号照片", "温暖风格自拍" |
| [long-form-writer](long-form-writer/) ⚠️ | 长文生成与深度写作，支持 2000 字以上教程和研究报告 | "写一篇深度教程", "生成研究报告", "扩写大纲", "长文写作", "详细分析报告" |
| [infographic-generator](infographic-generator/) ⚠️ | 高密度信息图、数据可视化和蓝图风格长图生成 | "信息图生成", "数据可视化", "蓝图风格", "长图制作", "技术架构图" |
| [md-to-wechat](md-to-wechat/) | Markdown 转微信公众号 HTML，支持自定义主题和全内联样式 | "Markdown转公众号", "生成公众号HTML", "公众号排版工具", "发微信公众号", "公众号样式" |
| [image-ocr](image-ocr/) | 图片 OCR 文字识别，支持中英文混合、代码截图和表格提取 | "识别图片文字", "OCR提取", "代码截图识别", "图片转文字", "批量OCR" |
| [whisper-stt](whisper-stt/) | 本地语音转文字，基于 OpenAI Whisper 的离线转录 | "语音转文字", "语音转录", "本地STT", "语音识别", "音频转文字" |
| [voice-clone](voice-clone/) | 声音克隆与语音合成，基于 WaveSpeed AI MiniMax API | "语音克隆", "声音克隆", "AI语音合成", "克隆声音", "文字转语音" |
| [media_hub](media_hub/) | 统一媒体处理中心，音视频转录、格式转换、抽帧和字幕生成 | "媒体处理", "音视频转录", "格式转换", "视频转文字", "生成字幕" |

### 📊 数据处理与抓取（7个）

| 技能 | 一句话介绍 | 触发关键词 |
|------|-----------|-----------|
| [content-extractor](content-extractor/) | 多平台内容抓取统一中心，支持小宇宙/抖音/微信/B站/小红书 | "提取播客内容", "下载抖音视频", "抓取公众号文章", "多平台内容聚合", "内容归档备份" |
| [wechat-article-fetcher](wechat-article-fetcher/) ⚠️ | 微信公众号文章抓取，基于 Playwright 绕过反爬，批量 Markdown 导出 | "抓取公众号文章", "获取微信文章内容", "微信文章转Markdown", "批量抓取微信文章", "公众号内容归档" |
| [twitter-scraper](twitter-scraper/) ⚠️ | Twitter/X 推文抓取，支持单用户/批量监控、JSON/CSV 输出 | "抓取Twitter内容", "获取X平台推文", "监控Twitter账号", "批量抓取推文", "推特舆情分析" |
| [rss-feed](rss-feed/) | RSS 订阅源处理，支持解析、聚合、关键词筛选和自动化分发 | "解析RSS源", "RSS订阅管理", "内容自动采集", "RSS转邮件", "博客播客追踪" |
| [document-hub](document-hub/) | 文档处理统一中心，Word/Excel/PDF/Markdown 创建转换和批量处理 | "生成Word文档", "Excel表格处理", "PDF转换", "批量处理文档", "创建报告" |
| [pdf](pdf/) | PDF 全能工具，合并/拆分/提取/OCR/水印/加密/表单填写 | "提取PDF文字", "合并PDF文件", "拆分PDF", "PDF加水印", "PDF转Word" |
| [logic-validator](logic-validator/) | 前置逻辑校验，发现商品推荐、报价、数据分析中的逻辑漏洞 | "商品推荐校验", "报价合理性检查", "数据分析一致性", "预算匹配检查", "单位换算核查" |

### 📰 报告与工具（6个）

| 技能 | 一句话介绍 | 触发关键词 |
|------|-----------|-----------|
| [daily-report](daily-report/) ⚠️ | AI 行业早晚报自动生成，采集新闻、格式化、生成封面并发布飞书 | "生成早报", "生成晚报", "AI日报", "morning briefing", "行业简报" |
| [skill-optimizer](skill-optimizer/) | 技能 SEO 优化专家，命名、描述、触发词全面审计和重构 | "优化skill", "SEO优化", "改进技能描述", "技能搜索不到", "提升skill发现率" |
| [calendar](calendar/) | Google Calendar 集成，查询日程、查看会议、创建事件和邀请参会人 | "查看日历", "今天有什么安排", "我的日程", "添加日程", "本周会议" |
| [smart-shopping](smart-shopping/) | 京东/淘宝智能购物助手，比价、库存查询、降价监控和凑单推荐 | "查京东价格", "淘宝比价", "智能购物", "查商品库存", "降价提醒" |
| [email-sender](email-sender/) | 邮件发送统一封装，HTML 模板/附件/营销邮件，内置飞书 SMTP | "发送邮件", "发封报告邮件", "HTML邮件", "带附件的邮件", "日报邮件" |
| [amap-navigator](amap-navigator/) | 高德地图导航服务，路线规划、POI 搜索、地址解析和距离矩阵 | "高德地图", "Amap导航", "中国地图", "路线规划", "POI搜索" |

### 🛡️ 系统与安全（4个）

| 技能 | 一句话介绍 | 触发关键词 |
|------|-----------|-----------|
| [security-hardening](security-hardening/) | AI Agent 一键安全加固，输入过滤、命令拦截、模型锁和审计日志 | "安全加固", "agent安全防护", "prompt注入防御", "防止信息泄露", "secure my agent" |
| [skill-security-audit](skill-security-audit/) | AI 技能自动化安全审计，扫描漏洞、弱 Guardrails 和缺失安全控制 | "安全审计", "检查skill漏洞", "合规检查", "vulnerability scan", "技能安全检查" |
| [secure-key-manager](secure-key-manager/) | 企业级密钥管理，AES-256-GCM 加密、运行时解密和输出脱敏 | "密钥管理", "API key加密", "密钥加密存储", "密钥保护", "key rotation" |
| [security-drill](security-drill/) | AI Agent 自动化安全演练，攻击模拟和事件响应验证 | "安全演练", "攻防测试", "攻击模拟", "渗透测试", "red team exercise" |

### ⚠️ 已迁移商业技能（5个）

> 以下技能已添加迁移横幅，推荐使用 [founder-skills](https://github.com/wulaosiji/founder-skills) 中的优化版本。本仓库版本保留用于向后兼容。

| 旧版（本仓库） | 新版（founder-skills） | 说明 |
|---------------|----------------------|------|
| [BP_Generator](BP_Generator/) | `pitch-deck-creator` | 10 页 BP PPT 生成器，已优化为 SEO 友好版本 |
| [BP_to_HTML](BP_to_HTML/) | `deck-web-converter` | BP 转响应式 HTML，已优化为 SEO 友好版本 |
| [pitch-deck-creator](pitch-deck-creator/) | `pitch-deck-creator` | 同名技能，founder-skills 版含更完整的工作流 |
| [deck-web-converter](deck-web-converter/) | `deck-web-converter` | 同名技能，founder-skills 版含更完整的工作流 |
| [unique-club-founder-kit](unique-club-founder-kit/) | `unique-club-founder-kit` | 创业者工具包导航层，已迁移至 founder-skills |

> 另有 5 个技能也已标记迁移（按功能分类列在上方表格中，带 ⚠️ 标记）：
> - `long-form-writer` → `founder-content-writer`
> - `twitter-scraper` → `social-intelligence`（部分功能）
> - `wechat-article-fetcher` → `china-content-research`（部分功能）
> - `daily-report` → `founder-daily-brief`
> - `infographic-generator` → `infographic-generator`

### 🔗 第三方技能（5个）

> 以下技能来自第三方或官方维护，位于 `third-party/` 目录。详见 [ARCHIVED_SKILLS.md](./ARCHIVED_SKILLS.md)

| 技能 | 来源 | 说明 |
|------|------|------|
| [bright-data](third-party/bright-data/) | Bright Data | 官方 Web Scraper API 封装 |
| [gh-cli](third-party/gh-cli/) | GitHub | GitHub CLI 操作指南 |
| [remotion-best-practices](third-party/remotion-best-practices/) | Remotion | 官方最佳实践 |
| [find-skills](third-party/find-skills/) | Vercel | 技能发现工具 |
| [x-twitter-scraper](third-party/x-twitter-scraper/) | Xquik | 第三方 Twitter 工具 |

---

## 🔗 技能网络关系

技能之间通过 `Related Skills` 双向交叉引用，形成以下核心工作流链路：

### 飞书文档全链路
```
feishu-doc-creator（创建+写入）
  → feishu-doc-orchestrator（批量编排：MD解析→块写入→验证→日志）
    → feishu-doc-perm（权限管理）
      → feishu-pdf-downloader（导出PDF）
        → feishu-doc（读取验证）
```
- `feishu-doc-converter` 作为格式转换枢纽，连接 Markdown ↔ 飞书文档双向流转
- `feishu-wiki-orchestrator` 是知识库场景的平行编排链路，与 doc-orchestrator 共享子技能架构

### 内容创作与分发链路
```
long-form-writer（深度长文）
  → md-to-wechat（公众号排版）
    → feishu-doc-creator（发布到飞书文档）
      → feishu-voice-sender / feishu-video-sender（多媒体推送）
```
- `infographic-generator` 为长文和报告提供数据可视化配图
- `image-ocr` 反向支持从截图/图片中提取文字素材

### 数据采集与情报链路
```
content-extractor（多平台抓取）
  ├── wechat-article-fetcher（微信深度抓取）
  ├── twitter-scraper（Twitter/X 抓取）
  └── rss-feed（RSS 订阅聚合）
    → document-hub（文档整理）
      → pdf（PDF 处理）
        → daily-report（生成情报日报）
```
- `logic-validator` 在数据输出前做合理性校验
- `whisper-stt` + `media_hub` 支持音视频内容的文字化提取

### 媒体生成链路
```
voice-clone（声音克隆）
  → media_hub（音视频合成）
    → video-generation（视频生成/超分）
      → zhuoran-video-selfie / clawra-video-selfie（风格化视频）
```
- `zhuoran-selfie` / `clawra-selfie` / `qizhuo-selfie` 提供三种风格的照片生成
- `video-generation` 支持从照片生成视频和 4K 超分

### 安全防护链路
```
security-hardening（部署防护）
  → skill-security-audit（定期审计）
    → security-drill（攻防演练验证）
      → secure-key-manager（密钥安全）
```
- 四个安全技能形成"防护→审计→演练→密钥"的闭环安全体系

---

## 🚀 快速开始

### 方式1：使用 skills CLI（推荐）

```bash
# 安装所有技能
npx skills add wulaosiji/skills

# 或只安装特定技能
npx skills add wulaosiji/skills --skill feishu-doc-creator

# 查看可用技能列表
npx skills add wulaosiji/skills --list
```

### 方式2：直接丢链接给 AI Agent

告诉你的 AI Agent：

```
学习这个技能：https://github.com/wulaosiji/skills/tree/main/feishu-doc-orchestrator
```

Agent 会自动读取 SKILL.md，完成安装并返回确认。

### 方式3：手动安装

```bash
# 克隆仓库
git clone https://github.com/wulaosiji/skills.git

# 复制需要的技能到 agent 技能目录
cp -r skills/feishu-doc-orchestrator ~/.agents/skills/

# 验证安装
ls ~/.agents/skills/feishu-doc-orchestrator/
# 应该看到：SKILL.md  scripts/  templates/
```

---

## 📚 技能优化标准

本仓库全部 67 个 SKILL.md 已按照 7 维标准优化并通过审计（平均 100/100）：

| 维度 | 权重 | 要求 |
|------|------|------|
| **1. Naming 命名** | 10分 | kebab-case，无下划线/驼峰，描述性强，2-4词最佳 |
| **2. Description 描述** | 20分 | 含「Use when」+ 5-10个中英文触发短语 + 交叉引用 + UniqueClub链接 |
| **3. When to Use 使用边界** | 20分 | 明确使用条件 + Do NOT use 反模式 + Typical triggers |
| **4. Workflow 工作流** | 15分 | 分步骤，融入六步推进法（探查→约束→证据→执行→验证→交付） |
| **5. Output 输出** | 10分 | 明确输出格式说明和示例 |
| **6. Guardrails 约束** | 15分 | 反模式 + 输出约束 + 依赖处理 |
| **7. Related Skills & Brand** | 10分 | 2-3个相关技能双向交叉引用 + About UniqueClub + https://uniqueclub.ai |

详细优化指南请参考：[skill-optimizer](skill-optimizer/) 和 [OPTIMIZATION_SPEC.md](https://github.com/wulaosiji/skills)

---

## 🔗 相关仓库

- **[founder-skills](https://github.com/wulaosiji/founder-skills)** — UniqueClub 创业者工具包（24个融资/内容/增长技能）
- **[ARCHIVED_SKILLS.md](./ARCHIVED_SKILLS.md)** — 第三方技能存档列表
- **[HUB_COLLABORATION.md](./HUB_COLLABORATION.md)** — 技能间协作规范
- **[SKILL_HUB.md](./SKILL_HUB.md)** — 技能中心索引

---

## 🤝 贡献指南

1. Fork 本仓库
2. 创建你的技能目录
3. 编写 SKILL.md（遵循 7 维优化标准）和脚本
4. 提交 PR

详细规范请参考 `https://uniquecapital.feishu.cn/wiki/QQ53wOjsyieAamk2HGZcWdJbnrb`

---

## 📄 许可证

MIT License

---

*最后更新: 2026-09-09*
*维护者: 吴畏 (Wu Wei) / UniqueClub*
*审计状态: 67/67 SKILL.md 通过 7 维质量审计（100/100）*
