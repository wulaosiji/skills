---
name: feishu-doc-orchestrator
description: |
  飞书文档创建主编排技能 / Feishu document creation orchestrator. 将 Markdown 文件转换为飞书文档，编排多个子技能协作完成，支持25种飞书文档块类型和完整权限管理。
  Use when: "创建飞书文档", "create feishu doc", "markdown转飞书", "markdown to feishu", "飞书文档排版", "feishu document formatting", "批量导入文档", "batch import documents", "飞书块类型", "feishu block types".
  编排 feishu-md-parser → feishu-doc-creator-with-permission → feishu-block-adder → feishu-doc-verifier → feishu-logger 五步流程。Cross-references: feishu-doc, feishu-wiki-orchestrator, feishu-doc-perm, feishu-doc-converter.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Document Orchestrator

> 将 Markdown 文件转换为飞书文档，支持25种块类型，完整权限管理，五步子技能编排。

## When to Use

Use this skill when:
- 需要将 Markdown 文件发布为飞书文档时
- 需要创建包含多种块类型（表格、代码块、图片等）的飞书文档时
- 需要自动分配文档权限给群聊或指定用户时
- 需要批量导入多个 Markdown 文档到飞书时

Do NOT use this skill if:
- 只需要**读取**现有飞书文档 → use `feishu-doc` instead
- 需要创建到**知识库（Wiki）** → use `feishu-wiki-orchestrator` instead
- 只需要下载已有文档或 PDF → use `feishu-pdf-downloader` instead
- 只需要简单创建文档而不需要完整编排 → use `feishu-doc-creator` instead

Typical triggers:
- 「帮我把这个 Markdown 转成飞书文档」「批量导入这些文档到飞书」
- "Create a Feishu doc from this markdown", "生成飞书文档并设置权限"

## Workflow

1. **探查 (Probe)**
确认 Markdown 文件路径、目标文档标题、是否需要设置权限。运行配置检查脚本验证飞书应用配置：
```bash
python .claude/skills/feishu-doc-orchestrator/scripts/check_config.py
```

2. **约束 (Constrain)**
确认配置文件 `.claude/feishu-config.env` 包含有效凭证，且已在 `.gitignore` 中排除敏感文件。首次使用前必须通过 `scripts/setup_config.py` 完成配置。不降级交付物——配置缺失时停止并提示用户。

3. **证据 (Evidence)**
调用 `feishu-md-parser` 将 Markdown 解析为飞书块格式，输出 `workflow/step1_parse/blocks.json`。确认块数量、表格数量等元数据。

4. **执行 (Execute)**
按顺序编排五个子技能：
1. **Markdown 解析**：`feishu-md-parser` → `workflow/step1_parse/blocks.json`
2. **文档创建+权限管理**（原子操作）：`feishu-doc-creator-with-permission` → `workflow/step2_create_with_permission/doc_with_permission.json`
3. **块添加**：`feishu-block-adder` → `workflow/step3_add_blocks/add_result.json`
4. **文档验证**：`feishu-doc-verifier` → `workflow/step4_verify/verify_result.json`
5. **日志记录**：`feishu-logger` → `CREATED_DOCS.md` + `created_docs.json`

命令行使用：
```bash
python scripts/orchestrator.py input.md "文档标题"
```

5. **验证 (Verify)**
调用 `feishu-doc-verifier` 使用 Playwright 访问文档 URL，确认页面加载成功、标题正确、内容完整。检查 `verify_result.json` 中的 `page_loaded` 和 `page_title` 字段。

6. **交付 (Deliver)**
返回文档 URL，汇总创建日志（`CREATED_DOCS.md` 和 `created_docs.json`），清理临时文件。

## Output

成功完成后返回：
1. **文档 URL**：可直接访问的飞书文档链接
2. **CREATED_DOCS.md**：Markdown 格式的创建日志
3. **created_docs.json**：JSON 格式的创建日志
4. **workflow/**：完整的中间结果，可追溯每一步

数据流（文件传递，节省 Token）：
```
input.md → [feishu-md-parser] → blocks.json
→ [feishu-doc-creator-with-permission] → doc_with_permission.json
→ [feishu-block-adder] → add_result.json
→ [feishu-doc-verifier] → verify_result.json
→ [feishu-logger] → CREATED_DOCS.md + created_docs.json
```

## Guardrails

**Anti-patterns**
- NEVER 将 `.claude/feishu-config.env` 或 `.claude/feishu-token.json` 提交到 Git（已在 `.gitignore` 中）
- Do NOT 在子技能之间传递实际内容，只传递文件路径（节省 60-80% Token）
- Do NOT 跳过权限管理步骤——应用创建的文档用户默认无权限

**Constraints**
- 配置文件包含敏感信息，发布前确保不包含个人隐私数据
- 子技能之间通过 `workflow/` 目录传递文件，支持断点续传
- 每步结果保存为文件，可追溯、可手动修复后继续

## Supported Blocks

**基础文本（11种）**：text, heading1-9, quote_container
**列表（4种）**：bullet, ordered, todo, task
**特殊块（5种）**：code, quote, callout, divider, image
**AI块（1种）**：ai_template
**高级块（5种）**：bitable, grid, sheet, table, board

## Related Skills

- **feishu-doc** — 只读读取飞书文档
- **feishu-wiki-orchestrator** — 在知识库中创建文档
- **feishu-doc-perm** — 文档权限管理
- **feishu-doc-converter** — 文档格式转换

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
