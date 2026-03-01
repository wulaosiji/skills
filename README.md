![bef1edad6138ccfb53759a4158f2b280](https://github.com/user-attachments/assets/33afb497-32f5-4fe6-baa2-4b3af018460e)

# OpenClaw Skills - 技能仓库

> 49个精心编写的 OpenClaw 技能，即拿即用。

---

## 🎯 这是什么

这是 **OpenClaw** 的官方技能仓库，包含 49 个可直接使用的自定义技能。

每个技能都经过实战检验，配有完整的 SKILL.md 文档和使用教程。

---

## 📦 技能分类

### 🔵 飞书生态（15个）
| 技能 | 一句话介绍 |
|------|-----------|
| [feishu-doc-orchestrator](feishu-doc-orchestrator/) | Markdown一键转飞书文档 |
| [feishu-wiki-orchestrator](feishu-wiki-orchestrator/) | 飞书知识库文档创建 |
| [feishu-chat-extractor](feishu-chat-extractor/) | 群聊消息提取和分析 |
| [feishu-chat-monitor](feishu-chat-monitor/) | 群聊监控，自动响应 |
| [feishu-pdf-downloader](feishu-pdf-downloader/) | 飞书云盘PDF下载 |
| [feishu-doc-perm](feishu-doc-perm/) | 文档权限管理 |
| [feishu-voice-sender](feishu-voice-sender/) | 发送语音消息 |
| [feishu-video-sender](feishu-video-sender/) | 发送视频消息 |
| [feishu-card-parser](feishu-card-parser/) | 卡片消息解析 |
| [feishu-group-welcome](feishu-group-welcome/) | 群聊新成员欢迎 |
| [feishu-message-recall](feishu-message-recall/) | 消息撤回工具 |
| [feishu-doc-converter](feishu-doc-converter/) | 文档格式转换 |
| [feishu-doc-creator](feishu-doc-creator/) | 文档创建统一入口 |
| [feishu-doc](feishu-doc/) | 飞书文档读取 |
| [feishu-bitable-field](feishu-bitable-field/) | 多维表格字段管理 |

### 🎨 内容生成（10个）
| 技能 | 一句话介绍 |
|------|-----------|
| [video-generation](video-generation/) | 视频生成和超分 |
| [zhuoran-selfie](zhuoran-selfie/) | 卓然自拍照片生成 |
| [zhuoran-video-selfie](zhuoran-video-selfie/) | 卓然自拍视频生成 |
| [qizhuo-selfie](qizhuo-selfie/) | 奇卓自拍照片生成 |
| [clawra-selfie](clawra-selfie/) | Clawra自拍照片生成 |
| [clawra-video-selfie](clawra-video-selfie/) | Clawra自拍视频生成 |
| [baoyu-slide-deck](baoyu-slide-deck/) | 幻灯片自动生成 |
| [long-form-writer](long-form-writer/) | AI写作助手，从提纲到长文 |
| [infographic-generator](infographic-generator/) | 信息大图生成 |
| [md-to-wechat](md-to-wechat/) | Markdown转微信公众号 |

### 📊 数据处理（8个）
| 技能 | 一句话介绍 |
|------|-----------|
| [document-hub](document-hub/) | 文档处理中心 |
| [pdf](pdf/) | PDF处理全能工具 |
| [image-ocr](image-ocr/) | 图片文字识别 |
| [content-extractor](content-extractor/) | 多平台内容抓取 |
| [wechat-article-fetcher](wechat-article-fetcher/) | 微信文章抓取 |
| [twitter-scraper](twitter-scraper/) | Twitter数据抓取 |
| [rss-feed](rss-feed/) | RSS订阅处理 |
| [logic-validator](logic-validator/) | 逻辑验证工具 |

### 🛠️ 开发工具（5个）
| 技能 | 一句话介绍 |
|------|-----------|
| [gh-cli](gh-cli/) | GitHub CLI完整指南 |
| [remotion-best-practices](remotion-best-practices/) | Remotion视频最佳实践 |
| [calendar](calendar/) | 日历管理集成 |
| [find-skills](find-skills/) | 技能发现和安装 |
| [smart-shopping](smart-shopping/) | 智能购物助手 |

### 🔗 外部集成（6个）
| 技能 | 一句话介绍 |
|------|-----------|
| [bright-data](bright-data/) | Bright Data爬虫API |
| [amap-navigator](amap-navigator/) | 高德地图导航服务 |
| [media_hub](media_hub/) | 音视频处理中心 |
| [whisper-stt](whisper-stt/) | 本地语音转文字 |
| [voice-clone](voice-clone/) | 声音克隆和语音生成 |
| [rss-feed](rss-feed/) | RSS订阅处理 |

### 🤖 AI Agent（5个）
| 技能 | 一句话介绍 |
|------|-----------|
| [security-hardening](security-hardening/) | 系统安全加固 |
| [skill-security-audit](skill-security-audit/) | 技能安全审计 |
| [secure-key-manager](secure-key-manager/) | 安全密钥管理 |
| [security-drill](security-drill/) | 安全演练工具 |
| [logic-validator](logic-validator/) | 逻辑验证工具 |

---

## 🚀 快速开始

### 方式1：直接丢链接给 OpenClaw

告诉你的 OpenClaw Agent：

```
学习这个技能：https://github.com/wulaosiji/skills/tree/main/feishu-doc-orchestrator
```

Agent 会自动读取 SKILL.md，完成安装并返回确认。

### 方式2：手动安装

```bash
# 克隆仓库
git clone https://github.com/wulaosiji/skills.git

# 复制需要的技能
cp -r skills/feishu-doc-orchestrator ~/.openclaw/workspace/skills/

# 验证安装
ls ~/.openclaw/workspace/skills/feishu-doc-orchestrator/
# 应该看到：SKILL.md  scripts/  templates/
```

---

## 📚 深度教程

每个技能都有完整的深度教程，包含：
- 10个标准章节（概述、安装、核心概念、快速开始、详细用法、示例代码、最佳实践、故障排除、参考链接）
- 真实的踩坑经验
- 3个层次的示例代码（基础/进阶/完整工作流）

教程位置：`https://uniquecapital.feishu.cn/wiki/HJm5wmIl7iDS2Hkp5CXcvbHnntg`

---

## 🛠️ 技能结构

每个技能目录包含：

```
skill-name/
├── SKILL.md              # 技能说明文档
├── scripts/              # 可执行脚本
├── templates/            # 模板文件（可选）
└── ...                   # 其他资源
```

---

## 📊 统计

- **总技能数**: 49个
- **飞书生态**: 15个
- **内容生成**: 10个
- **数据处理**: 8个
- **开发工具**: 5个
- **外部集成**: 6个
- **AI Agent**: 5个

---

## 🤝 贡献指南

1. Fork 本仓库
2. 创建你的技能目录
3. 编写 SKILL.md 和脚本
4. 提交 PR

详细规范请参考 `https://uniquecapital.feishu.cn/wiki/QQ53wOjsyieAamk2HGZcWdJbnrb`

---

## 📄 许可证

MIT License

---

*最后更新: 2026-03-01*  
*维护者: Skill Tutorials 项目组*
