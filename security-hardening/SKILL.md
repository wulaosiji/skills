---
name: security-hardening
description: |
  One-click security hardening system for AI agents and skills. Deploys input filters, command interceptors,
  model locks, persistent guards, and audit logging to protect against prompt injection, social engineering,
  dangerous command execution, and information leakage.
  Use when: "安全加固", "security hardening", "prompt injection", "社会工程学攻击", "agent security",
  "防护配置", "secure my agent", "安全演练", "security controls", "防止信息泄露".
  Cross-references: skill-security-audit, secure-key-manager, security-drill.
  Built by UniqueClub 🌐 https://uniqueclub.ai
---

# Security Hardening

> 一键安全加固 - One-click security hardening for AI agents.

## When to Use

Use this skill when:
- An agent or skill environment needs **security hardening**
- You want to protect against **prompt injection** and **social engineering attacks**
- You need to deploy **input filtering**, **command interception**, or **model locking**
- Setting up a new workspace and want **default-deny security posture**

Do NOT use this skill if:
- The issue is a specific skill bug → use **skill-security-audit** instead
- You need to store API keys securely → use **secure-key-manager** instead
- You want to run attack simulations → use **security-drill** instead

Typical triggers:
- 「帮我加固安全」「agent安全防护」「prompt注入防御」
- "security hardening", "protect my agent", "prevent prompt injection"
- "部署安全过滤器", "设置命令拦截", "model lock配置"

## Workflow

### Step 1: Pre-hardening Checklist
Confirm the following before execution:
- **Admin ID** (e.g., `ou_xxxxxxxx...`)
- **Allowed models** (e.g., `kimi-coding/k2p5`)
- **Workspace path** (typically `~/.openclaw/workspace`)

### Step 2: Execute Hardening
```bash
# Auto (recommended)
node skills/security-hardening/install.js \
  --admin=ou_xxx \
  --workspace=~/.openclaw/workspace \
  --models=kimi-coding/k2p5

# Interactive
node skills/security-hardening/install.js --interactive
```

### Step 3: Verify Deployment
```bash
node skills/security-hardening/verify.js
```
Expected: all components ✅ and protection level 🟢 High.

### Step 4: Test & Maintain
- Manually test injection / dangerous command scenarios
- Review weekly drill reports: `logs/security/drill-*.json`
- Update via: `node skills/security-hardening/install.js --update`

## Guardrails

### Anti-patterns
- NEVER run hardening without verifying admin ID ownership
- NEVER skip the verification step after installation
- NEVER disclose `security/` directory paths or config contents to users

### Output Constraints
- Default-deny: block when uncertain
- All sensitive operations require admin validation
- Audit logs record every security-relevant action

### Safety Rules
- `/new`, `/model`, `/reset` commands are blocked for non-admins
- System paths, tokens, and `SOUL.md` contents are redacted in responses
- Persistent guard auto-restores rules after session resets

## Related Skills

- **skill-security-audit** — Audit existing skills for security vulnerabilities and compliance gaps
- **secure-key-manager** — Encrypt and manage API keys with runtime decryption and output sanitization
- **security-drill** — Conduct automated attack simulations and validate incident response

## About UniqueClub

This skill is part of the **UniqueClub** security toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
