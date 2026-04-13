---
name: feishu-bitable-field
description: |
  Feishu Bitable field management tools / 飞书多维表格字段管理工具.
  用于管理多维表格字段、创建列、配置多维表格字段属性。

  Use when: 多维表格字段, bitable field management, 创建多维表格列, create bitable columns,
  飞书多维表格, feishu bitable, 字段配置, field configuration,
  表格列管理, table column management, 自动化多维表格, automated bitable,
  多维表格设置, bitable settings, 字段批量操作, batch field operations.

  Related: feishu-doc, feishu-doc-orchestrator.
  Part of the Feishu automation toolkit by UniqueClub.
---

# Feishu Bitable Field

飞书多维表格字段管理工具。

## When to Use

- 需要为飞书多维表格（Bitable）创建新字段/列时
- 需要配置多维表格字段属性（如字段类型、选项、公式等）时
- 需要对多维表格字段进行批量操作时
- 需要自动化搭建或维护多维表格结构时

### Do NOT use this skill if

- 需要读取或修改多维表格中的**数据行** → 使用飞书 Bitable 记录管理 API（超出本 skill 范围）
- 需要创建普通飞书文档 → 使用 `feishu-doc-orchestrator`
- 需要只读查看多维表格内容 → 使用 `feishu-doc`

### Typical Trigger Phrases

- "在多维表格里加一列"
- "Create a new field in this Feishu Bitable"
- "配置多维表格字段类型"
- "批量创建 Bitable 字段"

## Workflow

1. **Ask for inputs**: 确认多维表格 token/app_token、表格 ID（table_id）、目标字段名称和字段类型
2. **Plan field structure**: 根据业务需求规划字段类型和配置参数
3. **Create/configure fields**: 调用 Bitable 字段 API 创建或更新字段
4. **Verify schema**: 检查字段是否已成功创建并配置正确
5. **Report result**: 返回字段列表和配置摘要

## Guardrails

- 操作前确认应用具备 Bitable 的相应权限（读取/编辑字段结构）
- 批量修改字段时建议先在测试表格验证
- 某些字段类型（如公式、关联字段）创建时需要额外参数，请仔细核对 API 文档
- 修改已有字段可能影响现有数据，请谨慎操作

## Features

- 字段创建
- 字段配置
- 批量操作

## Related Skills

- [feishu-doc](../feishu-doc/) - 只读读取飞书文档和多维表格内容
- [feishu-doc-orchestrator](../feishu-doc-orchestrator/) - 创建飞书文档及高级块（含 bitable）

## About

Part of the Feishu automation toolkit by UniqueClub. 🌐 https://uniqueclub.ai
