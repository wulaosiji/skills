---
name: feishu-wiki-orchestrator
description: |
  飞书知识库文档创建编排技能 / Feishu wiki document orchestrator.
  直接在知识库（Wiki）中创建文档，无需先创建到云盘再手动移动。

  Use when: 创建知识库文档, create wiki document, wiki转飞书, wiki to feishu,
  飞书知识库, feishu wiki, 知识库排版, wiki formatting, 导入知识库, import to wiki,
  飞书文档迁移, feishu document migration, 正式文档归档, formal document archiving.

  Related: feishu-doc-orchestrator, feishu-doc, feishu-doc-perm.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Wiki Orchestrator

飞书知识库文档创建编排技能 — 直接在知识库创建文档。

## When to Use

- 需要在飞书知识库（Wiki）中直接创建文档时
- 希望将 Markdown 内容发布为知识库正式文档时
- 需要避免"先创建到云盘再移动到知识库"的繁琐流程时
- 团队知识库内容需要批量更新或归档时

### Do NOT use this skill if

- 只需要创建临时文档或不确定最终归属位置 → 使用 `feishu-doc-orchestrator`
- 只需要读取现有文档 → 使用 `feishu-doc`
- 目标不是知识库而是普通云盘文件夹 → 使用 `feishu-doc-orchestrator`

### Typical Trigger Phrases

- "把这个 Markdown 发到知识库"
- "在 Wiki 里创建一篇文档"
- "帮我归档到飞书知识库"
- "Create a Feishu wiki page from this markdown"

## Workflow

1. **Ask for inputs**: 确认 Markdown 文件路径、目标知识库空间 ID、父节点 ID、文档标题
2. **Verify wiki config**: 确认 `feishu-config.env` 中已配置 `FEISHU_WIKI_SPACE_ID` 和 `FEISHU_WIKI_PARENT_NODE`
3. **Parse Markdown**: 解析 Markdown 为飞书块格式（与 feishu-doc-orchestrator 共享解析逻辑）
4. **Create wiki node**: 在知识库中创建文档节点
5. **Add blocks**: 将内容块批量添加到 wiki 文档
6. **Verify access**: 验证文档在知识库中可正常访问
7. **Return URL**: 返回知识库文档 URL 和节点 Token

## Guardrails

- 必须在 `feishu-config.env` 中预先配置知识库 `SPACE_ID` 和 `PARENT_NODE`
- 知识库创建需要应用具备相应的 Wiki 权限
- 与 `feishu-doc-orchestrator` 不同，Wiki 创建后移动位置需手动在飞书中操作

## Differences from feishu-doc-orchestrator

| 特性 | feishu-doc-orchestrator | feishu-wiki-orchestrator |
|------|------------------------|-------------------------|
| 创建位置 | 云盘文件夹 | 知识库（Wiki） |
| 后续操作 | 需要手动移动到知识库 | 直接创建在知识库 |
| 使用场景 | 临时文档、不确定归属 | 正式文档、知识库内容 |

## Related Skills

- [feishu-doc-orchestrator](../feishu-doc-orchestrator/) - 在云盘中创建飞书文档
- [feishu-doc](../feishu-doc/) - 只读读取飞书文档
- [feishu-doc-perm](../feishu-doc-perm/) - 管理文档和知识库权限

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
