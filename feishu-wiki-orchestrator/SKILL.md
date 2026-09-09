---
name: feishu-wiki-orchestrator
description: |
  飞书知识库文档创建编排技能 / Feishu wiki document orchestrator. 直接在知识库（Wiki）中创建文档，无需先创建到云盘再手动移动，支持完整块类型和权限管理。
  Use when: "创建知识库文档", "create wiki document", "wiki转飞书", "wiki to feishu", "飞书知识库", "feishu wiki", "知识库排版", "wiki formatting", "导入知识库", "import to wiki".
  直接在知识库创建文档，编排 md-parser → creator-with-permission → block-adder → verifier → logger 流程。Cross-references: feishu-doc-orchestrator, feishu-doc, feishu-doc-perm, feishu-doc-converter.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Wiki Orchestrator

> 飞书知识库文档创建编排技能——直接在知识库创建文档，无需先创建到云盘再手动移动。

## When to Use

Use this skill when:
- 需要在飞书知识库（Wiki）中直接创建文档时
- 希望将 Markdown 内容发布为知识库正式文档时
- 需要避免"先创建到云盘再移动到知识库"的繁琐流程时
- 团队知识库内容需要批量更新或归档时

Do NOT use this skill if:
- 只需要创建临时文档或不确定最终归属位置 → use `feishu-doc-orchestrator` instead
- 只需要读取现有文档 → use `feishu-doc` instead
- 目标不是知识库而是普通云盘文件夹 → use `feishu-doc-orchestrator` instead

Typical triggers:
- 「把这个 Markdown 发到知识库」「在 Wiki 里创建一篇文档」
- "Create a Feishu wiki page from this markdown", "帮我归档到飞书知识库"

## Workflow

1. **探查 (Probe)**
确认 Markdown 文件路径、目标知识库空间 ID、父节点 ID、文档标题。

2. **约束 (Constrain)**
确认 `feishu-config.env` 中已配置 `FEISHU_WIKI_SPACE_ID` 和 `FEISHU_WIKI_PARENT_NODE`。知识库创建需要应用具备相应的 Wiki 权限。与云盘不同，Wiki 创建后移动位置需手动在飞书中操作。

3. **证据 (Evidence)**
调用 `feishu-md-parser` 将 Markdown 解析为飞书块格式，确认块数据完整。

4. **执行 (Execute)**
按顺序编排子技能：
1. **Markdown 解析**：`feishu-md-parser` → 块数据
2. **文档创建+权限管理**：`feishu-doc-creator-with-permission` → 在知识库创建文档节点并分配权限
3. **块添加**：`feishu-block-adder` → 批量添加内容块
4. **文档验证**：`feishu-doc-verifier` → 验证知识库文档可访问
5. **日志记录**：`feishu-logger` → 汇总记录

5. **验证 (Verify)**
使用 Playwright 访问知识库文档 URL，确认页面加载成功、标题正确、内容完整。检查文档在知识库节点树中的位置是否正确。

6. **交付 (Deliver)**
返回知识库文档 URL 和节点 Token，汇总创建日志，清理临时文件。

## Output

返回知识库文档 URL、节点 Token 和创建日志。文档直接创建在知识库中，无需手动移动。

## Guardrails

**Anti-patterns**
- NEVER 在未配置 `FEISHU_WIKI_SPACE_ID` 的情况下创建知识库文档
- Do NOT 尝试通过 API 移动知识库文档位置（需手动在飞书中操作）
- Do NOT 混淆云盘文档和知识库文档的创建流程

**Constraints**
- 必须在 `feishu-config.env` 中预先配置知识库 `SPACE_ID` 和 `PARENT_NODE`
- 知识库创建需要应用具备相应的 Wiki 权限
- 与 `feishu-doc-orchestrator` 共享解析逻辑，但创建目标不同

## Differences from feishu-doc-orchestrator

| 特性 | feishu-doc-orchestrator | feishu-wiki-orchestrator |
|------|------------------------|-------------------------|
| 创建位置 | 云盘文件夹 | 知识库（Wiki） |
| 后续操作 | 需要手动移动到知识库 | 直接创建在知识库 |
| 使用场景 | 临时文档、不确定归属 | 正式文档、知识库内容 |

## Related Skills

- **feishu-doc-orchestrator** — 在云盘中创建飞书文档
- **feishu-doc** — 只读读取飞书文档
- **feishu-doc-perm** — 管理文档和知识库权限

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
