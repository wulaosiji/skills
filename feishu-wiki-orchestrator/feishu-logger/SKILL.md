---
name: feishu-logger
description: |
  知识库日志记录子技能 / Feishu wiki logger sub-skill. 收集所有步骤的结果，记录知识库文档创建结果到日志文件，支持 Markdown 和 JSON 格式。
  Use when: "记录知识库文档日志", "log wiki document", "知识库创建日志汇总", "wiki creation log summary", "Markdown日志", "markdown log", "JSON日志", "json log".
  内部组件，由 feishu-wiki-orchestrator 编排调用，汇总所有子技能输出到 CREATED_DOCS.md 和 created_docs.json。Cross-references: feishu-wiki-orchestrator, feishu-doc-verifier, feishu-block-adder.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Wiki Logger (Sub-skill)

> 收集所有步骤的结果，记录知识库文档创建到日志文件（Markdown 和 JSON 格式）。内部组件。

## When to Use

Use this skill when:
- 需要汇总知识库文档创建流程中所有步骤的结果时
- 需要生成 Markdown 格式的知识库创建日志时
- 需要生成 JSON 格式的结构化日志时

Do NOT use this skill if:
- 需要验证知识库文档 → use `feishu-doc-verifier` instead
- 需要创建知识库文档 → use `feishu-wiki-orchestrator` (parent) instead
- 需要添加块 → use `feishu-block-adder` instead

Typical triggers:
- 「记录知识库创建日志」「汇总知识库文档创建结果」
- "log wiki creation result", "summarize wiki doc creation"

## Workflow

1. **探查 (Probe)**
从工作流目录加载所有 JSON 结果文件：`blocks.json`、`doc_info.json`、`add_result.json`、`permission_result.json`、`verify_result.json`。

2. **约束 (Constrain)**
只记录关键信息（文档 ID、URL、知识库空间、权限状态、验证状态），不记录敏感凭证。日志文件追加写入，不覆盖历史记录。

3. **执行 (Execute)**
1. 加载所有结果文件
2. 提取关键信息（含知识库空间 ID 和节点 Token）
3. 追加记录到 `CREATED_DOCS.md` 和 `created_docs.json`
4. 在控制台打印创建摘要

```bash
python scripts/logger.py workflow/ output
```

4. **验证 (Verify)**
检查日志文件已更新，新记录包含完整的知识库文档信息和状态。

5. **交付 (Deliver)**
返回日志文件路径和创建摘要。

## Output

`CREATED_DOCS.md` 格式：
```markdown
## 知识库文档标题

- **时间**: 2026-01-22 10:30:00
- **文档ID**: `U2wNd2rMkot6fzxr67ScN7hJn7c`
- **知识库空间**: `space_xxx`
- **URL**: [https://feishu.cn/wiki/...](...)
- **collaborator_added**: True
- **owner_transferred**: True
- **user_has_full_control**: True
- **document_verified**: True
- **tables_created**: 10
- **blocks_created**: 290
```

## Guardrails

**Anti-patterns**
- NEVER 在日志中记录飞书应用凭证或 token
- Do NOT 覆盖历史日志记录（追加写入）
- Do NOT 独立使用本子技能——应由父技能编排

**Constraints**
- 接收所有子技能的输出结果
- 最终汇总并记录到日志文件
- 支持 Markdown 和 JSON 双格式输出
- 知识库日志额外记录空间 ID 和节点 Token

## Related Skills

- **feishu-wiki-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-doc-verifier** — 上游：提供验证结果
- **feishu-block-adder** — 上游：提供块添加结果

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
