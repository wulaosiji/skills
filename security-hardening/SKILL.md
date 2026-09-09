---
name: security-hardening
description: |
  AI Agent一键安全加固系统，部署输入过滤器、命令拦截器、模型锁、持久防护和审计日志，防御prompt注入、社会工程学、危险命令执行和信息泄露。
  Use when: "安全加固", "agent安全防护", "prompt注入防御", "security hardening", "protect my agent", "部署安全过滤器", "防止信息泄露", "secure my agent".
  默认拒绝安全姿态，所有敏感操作需管理员验证，审计日志记录每次安全相关动作。Cross-references: skill-security-audit, secure-key-manager, security-drill.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
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
- 「部署安全过滤器」「设置命令拦截」「model lock配置」
- "secure my agent", "security controls", "防止信息泄露"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取环境状态，确认加固前的检查项：
- **Admin ID** (e.g., `ou_xxxxxxxx...`)
- **Allowed models** (e.g., `kimi-coding/k2p5`)
- **Workspace path** (typically `~/.openclaw/workspace`)

2. **约束 (Constrain)**
验证管理员ID所有权，设定默认拒绝（default-deny）安全姿态和不可降级的防护标准。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
记录加固前的环境状态作为基线证据，包括当前权限配置、已安装组件和开放端口。每个配置变更必须有明确的安全理由。

4. **执行 (Execute)**
运行加固脚本，先给影响与结论，再给行动和必要证据。
```bash
# Auto (recommended)
node skills/security-hardening/install.js \
  --admin=ou_xxx \
  --workspace=~/.openclaw/workspace \
  --models=kimi-coding/k2p5

# Interactive
node skills/security-hardening/install.js --interactive
```

5. **验证 (Verify)**
用不同于生成路径的方式回读——运行验证脚本确认所有组件已部署，防护等级为High。
```bash
node skills/security-hardening/verify.js
```
Expected: all components ✅ and protection level 🟢 High.

手动测试注入/危险命令场景，确认防护生效。

6. **交付 (Deliver)**
返回加固结果和验证报告，设置定期维护：
- Review weekly drill reports: `logs/security/drill-*.json`
- Update via: `node skills/security-hardening/install.js --update`

## Output

返回加固结果，包含：
- 各组件部署状态（输入过滤器、命令拦截器、模型锁、持久防护、审计日志）
- 防护等级（High/Medium/Low）
- 验证报告路径
- 管理员ID和允许的模型列表

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER run hardening without verifying admin ID ownership
- NEVER skip the verification step after installation
- NEVER disclose `security/` directory paths or config contents to users

**Output Constraints**
- Default-deny: block when uncertain
- All sensitive operations require admin validation
- Audit logs record every security-relevant action

**Safety Rules**
- `/new`, `/model`, `/reset` commands are blocked for non-admins
- System paths, tokens, and `SOUL.md` contents are redacted in responses
- Persistent guard auto-restores rules after session resets

## Related Skills

- **skill-security-audit** — Audit existing skills for security vulnerabilities and compliance gaps
- **secure-key-manager** — Encrypt and manage API keys with runtime decryption and output sanitization
- **security-drill** — Conduct automated attack simulations and validate incident response

## About UniqueClub

This skill is part of the **UniqueClub** security toolkit.
🌐 https://uniqueclub.ai
