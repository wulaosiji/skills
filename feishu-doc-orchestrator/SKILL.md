---
name: feishu-doc-orchestrator
description: |
  飞书文档创建主编排技能 / Feishu document creation orchestrator.
  将 Markdown 文件转换为飞书文档，编排多个子技能协作完成，支持25种飞书文档块类型。

  Use when: 创建飞书文档, create feishu doc, markdown转飞书, markdown to feishu, 
  飞书文档排版, feishu document formatting, 批量导入文档, batch import documents,
  飞书块类型, feishu block types, 文档权限管理, document permission management.

  Related: feishu-doc, feishu-wiki-orchestrator, feishu-doc-perm, feishu-doc-converter.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Document Orchestrator

将 Markdown 文件转换为飞书文档，支持25种块类型，完整权限管理。

## When to Use

- 需要将 Markdown 文件发布为飞书文档时
- 需要创建包含多种块类型（表格、代码块、图片等）的飞书文档时
- 需要自动分配文档权限给群聊或指定用户时
- 需要批量导入多个 Markdown 文档到飞书时

### Do NOT use this skill if

- 只需要**读取**现有飞书文档 → 使用 `feishu-doc`
- 需要创建到**知识库（Wiki）** → 使用 `feishu-wiki-orchestrator`
- 只需要下载已有文档或 PDF → 使用 `feishu-pdf-downloader`

### Typical Trigger Phrases

- "帮我把这个 Markdown 转成飞书文档"
- "Create a Feishu doc from this markdown"
- "批量导入这些文档到飞书"
- "生成飞书文档并设置权限"

## Workflow

1. **Ask for inputs**: 确认 Markdown 文件路径、目标文档标题、是否需要设置权限
2. **Check configuration**: 运行 `python .claude/skills/feishu-doc-orchestrator/scripts/check_config.py` 验证飞书应用配置
3. **Parse Markdown**: 调用 feishu-md-parser 将 Markdown 解析为飞书块格式
4. **Create document**: 调用 feishu-doc-creator-with-permission 创建文档并分配权限
5. **Add blocks**: 调用 feishu-block-adder 批量添加25种支持的块类型
6. **Verify**: 调用 feishu-doc-verifier 验证文档可访问性和内容完整性
7. **Log result**: 调用 feishu-logger 记录创建结果并返回文档 URL

## Guardrails

- 配置文件 `.claude/feishu-config.env` 包含敏感信息，**请勿提交到 Git**
- `.claude/feishu-config.env` 和 `.claude/feishu-token.json` 已在 `.gitignore` 中
- 首次使用前必须通过 `scripts/setup_config.py` 完成飞书应用配置
- 发布前确保不包含个人隐私数据

## Supported Blocks

**基础文本（11种）**：text, heading1-9, quote_container  
**列表（4种）**：bullet, ordered, todo, task  
**特殊块（5种）**：code, quote, callout, divider, image  
**AI块（1种）**：ai_template  
**高级块（5种）**：bitable, grid, sheet, table, board

## Related Skills

- [feishu-doc](../feishu-doc/) - 只读读取飞书文档
- [feishu-wiki-orchestrator](../feishu-wiki-orchestrator/) - 在知识库中创建文档
- [feishu-doc-perm](../feishu-doc-perm/) - 文档权限管理
- [feishu-doc-converter](../feishu-doc-converter/) - 文档格式转换

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
