---
name: feishu-bitable-field
description: |
  飞书多维表格字段管理工具 / Feishu Bitable field management tools. 用于管理多维表格字段、创建列、配置多维表格字段属性，支持批量操作。
  Use when: "多维表格字段", "bitable field management", "创建多维表格列", "create bitable columns", "飞书多维表格", "feishu bitable", "字段配置", "field configuration", "表格列管理", "table column management".
  支持字段创建、字段配置和批量操作，覆盖文本、数字、单选、多选、日期、公式、关联等字段类型。Cross-references: feishu-doc, feishu-doc-orchestrator, feishu-doc-converter.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Bitable Field

> 飞书多维表格字段管理工具——创建列、配置字段属性、批量操作多维表格字段结构。

## When to Use

Use this skill when:
- 需要为飞书多维表格（Bitable）创建新字段/列时
- 需要配置多维表格字段属性（如字段类型、选项、公式等）时
- 需要对多维表格字段进行批量操作时
- 需要自动化搭建或维护多维表格结构时

Do NOT use this skill if:
- 需要读取或修改多维表格中的**数据行** → 使用飞书 Bitable 记录管理 API（超出本 skill 范围）
- 需要创建普通飞书文档 → use `feishu-doc-orchestrator` instead
- 需要只读查看多维表格内容 → use `feishu-doc` instead

Typical triggers:
- 「在多维表格里加一列」「配置多维表格字段类型」
- "Create a new field in this Feishu Bitable", "批量创建 Bitable 字段"

## Workflow

1. **探查 (Probe)**
确认多维表格 token/app_token、表格 ID（table_id）、目标字段名称和字段类型。

2. **约束 (Constrain)**
操作前确认应用具备 Bitable 的相应权限（读取/编辑字段结构）。批量修改字段时建议先在测试表格验证。某些字段类型（如公式、关联字段）创建时需要额外参数，请仔细核对 API 文档。修改已有字段可能影响现有数据，请谨慎操作。不降级——权限不足时停止并提示。

3. **证据 (Evidence)**
根据业务需求规划字段类型和配置参数，确认字段名称不重复。

4. **执行 (Execute)**
调用 Bitable 字段 API 创建或更新字段，支持字段创建、字段配置和批量操作。

5. **验证 (Verify)**
检查字段是否已成功创建并配置正确，回读多维表格 schema 确认字段列表。

6. **交付 (Deliver)**
返回字段列表和配置摘要，清理临时文件。

## Output

返回字段列表和配置摘要，包含创建的字段 ID、字段名称、字段类型和配置参数。

## Guardrails

**Anti-patterns**
- NEVER 在未确认权限的情况下修改多维表格字段结构
- Do NOT 在生产表格上直接批量修改字段（先在测试表格验证）
- Do NOT 修改已有字段而不评估对现有数据的影响
- 禁止创建公式/关联字段时缺少必要参数（会创建失败）

**Constraints**
- 操作前确认应用具备 Bitable 的相应权限（读取/编辑字段结构）
- 批量修改字段时建议先在测试表格验证
- 某些字段类型（如公式、关联字段）创建时需要额外参数，请仔细核对 API 文档
- 修改已有字段可能影响现有数据，请谨慎操作

## Features

- 字段创建
- 字段配置
- 批量操作

## Related Skills

- **feishu-doc** — 只读读取飞书文档和多维表格内容
- **feishu-doc-orchestrator** — 创建飞书文档及高级块（含 bitable）
- **feishu-doc-converter** — 文档格式转换

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
