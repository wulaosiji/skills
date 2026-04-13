---
name: skill-security-audit
description: |
  Automated security audit and compliance checker for OpenClaw/Hermes skills.
  Scans SKILL.md files, scripts, and configurations for vulnerabilities, misconfigurations,
  weak guardrails, and missing safety controls.
  Use when: "安全审计", "security audit", "检查skill漏洞", "合规检查", "vulnerability scan",
  "技能安全检查", "security review", "发现安全风险", "penetration test", "代码审计".
  Cross-references: security-hardening, secure-key-manager, security-drill.
  Built by UniqueClub 🌐 https://uniqueclub.ai
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
- "审查技能安全性", "pen test my skill", "security review"

## Workflow

### Step 1: Load Target Skill
Identify the skill path and read its `SKILL.md` and scripts.

### Step 2: Run Audit Dimensions
Check across these categories:
1. **Naming & Metadata** — kebab-case, clear description, no leaked secrets
2. **Guardrails** — explicit When to Use / Not Use, anti-patterns listed
3. **Permission Boundaries** — no overly broad file system or network access
4. **Secret Handling** — no hardcoded API keys or tokens in code/docs
5. **Output Safety** — no instructions to reveal system paths or internal configs
6. **Cross-References** — related security skills referenced

### Step 3: Generate Report
Output a structured report with:
- Severity ratings (Critical / High / Medium / Low)
- Specific file:line references
- Actionable remediation steps

### Step 4: Recommend Fixes
Suggest concrete rewrites or use **security-hardening** / **secure-key-manager** where applicable.

## Guardrails

### Anti-patterns
- NEVER modify audited skill files without user confirmation
- NEVER expose actual secrets found during the audit in your response
- NEVER provide exploit code that could harm live systems

### Output Constraints
- Report findings in user's preferred language
- Redact any discovered secrets with `[REDACTED]`
- Provide severity-ranked, actionable recommendations only

## Related Skills

- **security-hardening** — Deploy hardened security controls to the agent environment
- **secure-key-manager** — Securely store and retrieve API keys with encryption
- **security-drill** — Run automated attack simulations to validate defenses

## About UniqueClub

This skill is part of the **UniqueClub** security toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
