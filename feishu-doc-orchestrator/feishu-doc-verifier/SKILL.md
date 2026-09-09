---
name: feishu-doc-verifier
description: |
  文档验证子技能 / Feishu document verifier sub-skill. 使用 Playwright 验证飞书文档是否创建成功并可正常访问，截图留证。
  Use when: "验证飞书文档", "verify feishu document", "文档可访问性检查", "doc accessibility check", "Playwright验证", "playwright verification", "文档截图", "document screenshot".
  内部组件，由 feishu-doc-orchestrator 编排调用，使用不同于生成路径的方式回读验证。Cross-references: feishu-doc-orchestrator, feishu-doc, feishu-logger.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Feishu Document Verifier (Sub-skill)

> 使用 Playwright 访问飞书文档，验证文档是否创建成功并可正常访问，截图留证。内部组件。

## When to Use

Use this skill when:
- 需要验证新创建的飞书文档是否可正常访问时
- 需要通过浏览器截图确认文档内容时
- 需要在文档创建流程末尾做最终验证时

Do NOT use this skill if:
- 需要读取文档内容（API 方式）→ use `feishu-doc` instead
- 需要创建文档 → use `feishu-doc-orchestrator` (parent) instead
- 需要记录日志 → use `feishu-logger` instead

Typical triggers:
- 「验证文档是否创建成功」「检查文档可访问性」
- "verify feishu doc", "check document accessibility"

## Workflow

1. **探查 (Probe)**
从 `doc_info.json` 加载文档 ID 和 URL。

2. **约束 (Constrain)**
使用 Playwright 持久化上下文启动浏览器，确保登录态有效。验证方式必须不同于生成路径（API 创建 → 浏览器验证）。

3. **执行 (Execute)**
1. 启动 Playwright 浏览器
2. 导航到文档 URL，等待页面加载
3. 检查页面标题和内容
4. 截图保存

```bash
python scripts/doc_verifier.py workflow/step2_create/doc_info.json output
```

4. **验证 (Verify)**
确认 `page_loaded` 为 true，`page_title` 与预期标题匹配，截图文件已生成。

5. **交付 (Deliver)**
保存验证结果到 `output/verify_result.json`。

## Output

```json
{
  "success": true,
  "document_id": "U2wNd2rMkot6fzxr67ScN7hJn7c",
  "document_url": "https://feishu.cn/docx/U2wNd2rMkot6fzxr67ScN7hJn7c",
  "page_loaded": true,
  "page_title": "文档标题",
  "screenshot": "output/screenshot.png",
  "verified_at": "2026-01-22T10:40:00"
}
```

## Guardrails

**Anti-patterns**
- NEVER 使用 API 方式验证（与生成路径相同，无法发现浏览器端问题）
- Do NOT 跳过截图步骤（截图是验证的重要证据）
- Do NOT 独立使用本子技能——应由父技能编排

**Constraints**
- 需要 Playwright 和浏览器驱动已安装
- 使用持久化上下文以保持飞书登录态
- 输出给 `feishu-logger` 汇总记录

## Related Skills

- **feishu-doc-orchestrator** (parent) — 主编排技能，调用本子技能
- **feishu-doc** — API 方式读取文档内容
- **feishu-logger** — 下游：汇总验证结果到日志

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
