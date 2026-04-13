---
name: feishu-doc-perm
description: |
  飞书文档权限管理最佳实践 / Feishu document permission manager.
  创建、配置、批量管理文档权限，支持用户和群聊级别权限控制。

  Use when: 飞书文档权限, feishu document permissions, 添加协作者, add collaborators,
  文档共享设置, document sharing settings, 批量权限管理, batch permission management,
  移除文档权限, remove document access, 群聊只读授权, group read-only authorization,
  无法转发问题, cannot forward issue, 安全权限配置, security permission config.

  Related: feishu-doc-orchestrator, feishu-wiki-orchestrator, feishu-doc, feishu-group-welcome.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Document Permission Manager

飞书文档权限管理最佳实践 — 创建、配置、批量管理文档权限。

## When to Use

- 需要为飞书文档添加或移除协作者权限时
- 需要给群聊批量授予文档查看或编辑权限时
- 需要查询文档当前的权限配置状态时
- 用户反馈"无法转发"文档需要调整权限设置时
- 需要对敏感文档实施最小权限原则时

### Do NOT use this skill if

- 需要创建新文档 → 使用 `feishu-doc-orchestrator`
- 需要读取文档内容 → 使用 `feishu-doc`
- 目标文档在知识库中且需要 Wiki 特有权限 → 结合 `feishu-wiki-orchestrator` 处理

### Typical Trigger Phrases

- "给这个文档加权限"
- "Add edit permission for this user to the Feishu doc"
- "群成员看不到文档"
- "解决无法转发的问题"
- "查询文档当前权限"

## Workflow

1. **Ask for inputs**: 确认文档 token、文档类型（docx/sheet等）、目标用户/群聊 ID、期望权限级别
2. **List current permissions**: 查询现有权限
   ```
   feishu_perm action=list token=xxx type=docx
   ```
3. **Add or remove permissions**: 根据需求添加或移除权限
   ```
   feishu_perm action=add token=xxx type=docx member_id=ou_xxx member_type=openid perm=edit
   feishu_perm action=add token=xxx type=docx member_id=oc_xxx member_type=openchat perm=view
   feishu_perm action=remove token=xxx type=docx member_id=ou_xxx member_type=openid
   ```
4. **Verify changes**: 再次查询权限列表确认变更已生效
5. **Report result**: 返回权限变更摘要

## Guardrails

### ✅ 推荐做法

1. **最小权限原则**
   - 默认给 `view` 权限
   - 需要编辑才给 `edit`
   - 仅管理员给 `full_access`

2. **群聊权限 vs 个人权限**
   - 群聊给 `view`（只读）
   - 特定协作者给 `edit`（可编辑）
   - 创建者保留 `full_access`

3. **敏感文档保护**
   - 核心配置文件（如 SOUL.md）仅限创建者可编辑
   - 群聊中不展示敏感配置
   - 定期审查文档权限

### ❌ 避免做法

1. 给群聊 `full_access`（所有人可删除）
2. 给陌生人编辑权限而不审核
3. 在群聊中分享包含敏感信息的文档

## Permission Levels

| 权限 | 说明 |
|------|------|
| `view` | 仅查看，不可编辑 |
| `edit` | 可编辑内容，不可管理权限 |
| `full_access` | 完全权限，包括删除 |

## Related Skills

- [feishu-doc-orchestrator](../feishu-doc-orchestrator/) - 创建文档并自动分配权限
- [feishu-wiki-orchestrator](../feishu-wiki-orchestrator/) - 知识库文档创建
- [feishu-doc](../feishu-doc/) - 只读读取文档
- [feishu-group-welcome](../feishu-group-welcome/) - 群聊管理相关工具

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
