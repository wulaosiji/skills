---
name: feishu-doc-orchestrator
description: |
  知识库文档创建主编排子技能 / Feishu wiki document creation orchestrator sub-skill. 将 Markdown 文件转换为飞书知识库文档，编排多个子技能协作完成，使用文件传递数据以节省 Token。
  Use when: "编排知识库文档创建", "orchestrate wiki doc creation", "Markdown转知识库文档", "markdown to wiki doc", "知识库五步编排", "wiki five-step orchestration", "文件传递数据", "file-based data passing".
  内部嵌套编排组件，协调 md-parser → creator-with-permission → block-adder → verifier → logger 流程。Cross-references: feishu-wiki-orchestrator, feishu-md-parser, feishu-block-adder.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Wiki Document Orchestrator (Nested Sub-skill)

> 飞书知识库文档创建主编排子技能——将 Markdown 转换为知识库文档，编排 5 个子技能协作，使用文件传递数据节省 Token。内部嵌套组件。

## When to Use

Use this skill when:
- 需要在嵌套层级中编排知识库文档创建流程时
- 需要协调多个子技能按顺序执行时
- 需要通过文件传递中间结果以节省 Token 时

Do NOT use this skill if:
- 需要顶层编排入口 → use `feishu-wiki-orchestrator` (parent) instead
- 需要创建云盘文档 → use `feishu-doc-orchestrator` instead
- 只需要单个子技能功能 → 直接调用对应子技能

Typical triggers:
- 「编排知识库文档创建流程」「协调知识库子技能」
- "orchestrate wiki doc creation pipeline", "coordinate wiki sub-skills"

## Workflow

1. **探查 (Probe)**
确认 Markdown 文件路径、文档标题、知识库空间 ID 和父节点 ID。

2. **约束 (Constrain)**
子技能之间只传递文件路径，不传递实际内容（节省 60-80% Token）。每步结果保存到 `workflow/` 目录，支持断点续传。知识库创建需要 Wiki 权限。

3. **执行 (Execute)**
五步编排：
1. **Markdown 解析**：`feishu-md-parser` → `workflow/step1_parse/blocks.json`
2. **文档创建+权限管理**：`feishu-doc-creator-with-permission` → `workflow/step2_create_with_permission/doc_with_permission.json`
3. **块添加**：`feishu-block-adder` → `workflow/step3_add_blocks/add_result.json`
4. **文档验证**：`feishu-doc-verifier` → `workflow/step4_verify/verify_result.json`
5. **日志记录**：`feishu-logger` → `CREATED_DOCS.md` + `created_docs.json`

```bash
python scripts/orchestrator.py input.md "文档标题"
```

4. **验证 (Verify)**
检查每步输出文件是否存在且包含有效数据，确认最终知识库文档可访问且位置正确。

5. **交付 (Deliver)**
返回知识库文档 URL 和创建日志，清理临时文件。

## Output

成功完成后返回知识库文档 URL、节点 Token、`CREATED_DOCS.md`、`created_docs.json` 和完整的 `workflow/` 中间结果。

数据流：
```
input.md → [feishu-md-parser] → blocks.json
→ [feishu-doc-creator-with-permission] → doc_with_permission.json
→ [feishu-block-adder] → add_result.json
→ [feishu-doc-verifier] → verify_result.json
→ [feishu-logger] → CREATED_DOCS.md + created_docs.json
```

## Guardrails

**Anti-patterns**
- NEVER 在子技能之间传递实际内容（只传文件路径）
- Do NOT 跳过任何编排步骤（尤其是权限管理）
- Do NOT 独立使用本子技能——应由父技能调用

**Constraints**
- 单一职责：每个子技能只做一件事
- 中间结果保存为文件，可追溯、可断点续传
- 知识库文档创建后移动位置需手动操作
- Callout 块颜色字段必须直接放在 `callout` 对象下

## Related Skills

- **feishu-wiki-orchestrator** (parent) — 顶层主编排技能
- **feishu-md-parser** — 子技能：解析 Markdown
- **feishu-block-adder** — 子技能：添加块

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
