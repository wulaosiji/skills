---
name: feishu-doc-creator-with-permission
description: |
  文档创建+权限管理子技能 / Feishu doc creator with permission sub-skill. 在飞书创建文档并自动完成权限分配（添加协作者+转移所有权），两步原子操作。
  Use when: "创建飞书文档带权限", "create feishu doc with permission", "添加协作者", "add collaborator", "转移所有权", "transfer ownership", "文档权限分配", "doc permission assignment".
  内部组件，由 feishu-doc-orchestrator 编排调用，确保每次创建都正确分配权限。Cross-references: feishu-doc-orchestrator, feishu-doc-perm, feishu-block-adder.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Doc Creator with Permission (Sub-skill)

> 在飞书创建新文档，并自动完成完整权限管理流程（添加协作者 + 转移所有权），确保用户获得完全控制权。内部组件。

## When to Use

Use this skill when:
- 需要创建飞书文档并确保用户获得完全控制权时
- 需要在创建文档后自动添加协作者权限时
- 需要将文档所有权转移给用户时

Do NOT use this skill if:
- 需要独立创建文档而不需要权限管理 → use `feishu-doc-creator` instead
- 需要管理已有文档的权限 → use `feishu-doc-perm` instead
- 需要创建到知识库 → use `feishu-wiki-orchestrator` (parent) instead

Typical triggers:
- 「创建文档并分配权限」「转移文档所有权」
- "create doc with permission", "transfer document ownership"

## Workflow

1. **探查 (Probe)**
确认文档标题（必需）和 Markdown 文件路径（可选，用于确定标题）。

2. **约束 (Constrain)**
创建文档和权限管理是强关联操作，必须合并执行。只有 `tenant_token` 可以添加协作者，只有 `user_token` 可以转移所有权。不降级——权限分配失败时报告错误，不创建无权限文档。

3. **执行 (Execute)**
三步原子操作：
1. **创建文档**：使用 `tenant_access_token` 创建新文档，应用成为创建者
2. **添加协作者权限**：使用 `tenant_access_token` 添加协作者，用户获得编辑权限
3. **转移所有权**：使用 `user_access_token` 转移所有权，用户获得完全控制权

```bash
python scripts/doc_creator_with_permission.py "文档标题" output
```

4. **验证 (Verify)**
检查权限状态：`collaborator_added` 和 `owner_transferred` 均为 true，确认 `user_has_full_control`。

5. **交付 (Deliver)**
保存文档信息和权限状态到 `output/doc_with_permission.json`。

## Output

```json
{
  "document_id": "U2wNd2rMkot6fzxr67ScN7hJn7c",
  "document_url": "https://feishu.cn/docx/U2wNd2rMkot6fzxr67ScN7hJn7c",
  "title": "文档标题",
  "created_at": "2026-01-22T10:30:00",
  "permission": {
    "collaborator_added": true,
    "owner_transferred": true,
    "user_has_full_control": true,
    "collaborator_id": "ou_xxx"
  }
}
```

## Guardrails

**Anti-patterns**
- NEVER 只创建文档而不分配权限（用户将看不到文档）
- Do NOT 跳过所有权转移（用户可编辑但无法删除）
- Do NOT 使用错误的 token 类型：添加协作者必须用 `tenant_token`，转移所有权必须用 `user_token`

**Constraints**
- 权限管理的必要性：应用创建的文档用户默认无权限 → 添加协作者后可编辑但无法删除 → 转移所有权后获得完全控制权
- 只传递文件路径，不传递内容
- 输出给 `feishu-block-adder`、`feishu-doc-verifier`、`feishu-logger`

## Related Skills

- **feishu-doc-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-doc-perm** — 管理已有文档的权限
- **feishu-block-adder** — 下游：向创建的文档添加块

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
