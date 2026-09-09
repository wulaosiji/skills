---
name: skill-security-audit
description: |
  AI技能自动化安全审计与合规检查工具，扫描SKILL.md文件、脚本和配置，发现漏洞、错误配置、弱Guardrails和缺失安全控制，输出分级报告和修复建议。
  Use when: "安全审计", "检查skill漏洞", "合规检查", "security audit", "vulnerability scan", "技能安全检查", "security review", "代码审计".
  覆盖命名元数据、Guardrails、权限边界、密钥处理、输出安全和交叉引用六大审计维度。Cross-references: security-hardening, secure-key-manager, security-drill.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Skill Security Audit

> Automated security auditing for AI skills.

## When to Use

Use this skill when:
- Auditing a skill for **security vulnerabilities** or **compliance issues**
- Reviewing SKILL.md guardrails, permissions, and safety controls
- Performing a **pre-release security review**
- A skill is behaving suspiciously and needs inspection

Do NOT use this skill if:
- You need to fix the environment itself → use **security-hardening**
- The problem is a runtime bug, not a security flaw → use debugging tools
- You want to simulate attacks → use **security-drill** instead

Typical triggers:
- 「审计skill安全」「检查漏洞」「安全合规审查」
- "security audit skill", "check for vulnerabilities", "compliance scan"
- 「审查技能安全性」「pen test my skill」「security review」
- "代码审计", "vulnerability scan", "发现安全风险"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取目标技能的所有文件，确认审计范围：
- Identify the skill path and read its `SKILL.md` and scripts
- 列出所有需要审计的文件（SKILL.md、scripts/、配置文件）

2. **约束 (Constrain)**
设定审计边界和不可降级的标准——不修改被审计文件，不泄露发现的真实密钥。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
每个审计发现必须有具体的file:line引用，不凭印象判断。收集原始代码片段作为证据。

4. **执行 (Execute)**
运行六大维度审计，先给影响与结论，再给行动和必要证据：

1. **Naming & Metadata** — kebab-case, clear description, no leaked secrets
2. **Guardrails** — explicit When to Use / Not Use, anti-patterns listed
3. **Permission Boundaries** — no overly broad file system or network access
4. **Secret Handling** — no hardcoded API keys or tokens in code/docs
5. **Output Safety** — no instructions to reveal system paths or internal configs
6. **Cross-References** — related security skills referenced

5. **验证 (Verify)**
用不同于生成路径的方式回读——交叉验证每个发现的严重性评级，确认修复建议可操作。关键发现至少两个独立检查确认。

6. **交付 (Deliver)**
输出结构化审计报告，包含严重性分级、具体file:line引用和可操作的修复步骤。建议使用 security-hardening / secure-key-manager 进行修复。不修改被审计文件，除非用户明确确认。

## Output

输出结构化报告：
- Severity ratings (Critical / High / Medium / Low)
- Specific file:line references
- Actionable remediation steps
- 发现的密钥以 `[REDACTED]` 脱敏显示

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER modify audited skill files without user confirmation
- NEVER expose actual secrets found during the audit in your response
- NEVER provide exploit code that could harm live systems

**Output Constraints**
- Report findings in user's preferred language
- Redact any discovered secrets with `[REDACTED]`
- Provide severity-ranked, actionable recommendations only

## Related Skills

- **security-hardening** — Deploy hardened security controls to the agent environment
- **secure-key-manager** — Securely store and retrieve API keys with encryption
- **security-drill** — Run automated attack simulations to validate defenses

## About UniqueClub

This skill is part of the **UniqueClub** security toolkit.
🌐 https://uniqueclub.ai
