---
name: secure-key-manager
description: |
  企业级AI Agent密钥管理工具，使用AES-256-GCM加密和PBKDF2HMAC密钥派生（48万轮），支持运行时解密、自动输出脱敏和严格文件权限（0600），替代TOOLS.md中的明文密钥存储。
  Use when: "密钥管理", "API key加密", "密钥加密存储", "secure key storage", "API key encryption", "密钥保护", "secret management", "key rotation".
  按需解密、内存中不持久化明文、输出自动脱敏，支持密钥轮换和审计。Cross-references: security-hardening, skill-security-audit, security-drill.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Secure Key Manager

> AES-256-GCM encrypted key storage for AI agents.

## When to Use

Use this skill when:
- Storing **API keys** or **secrets** that should not be in plaintext
- Migrating from hardcoded keys in `TOOLS.md` to encrypted storage
- Implementing **output sanitization** to prevent accidental key leakage
- Rotating compromised keys in a secure vault

Do NOT use this skill if:
- You are deploying general security controls → use **security-hardening**
- You need to audit existing skills → use **skill-security-audit**
- Keys need to be shared across many team members (use enterprise vaults)

Typical triggers:
- 「加密存储API Key」「密钥管理」「安全存储密码」
- "encrypt my API keys", "secure vault", "key manager"
- 「API密钥加密」「secret storage」「key rotation」
- "敏感信息存储", "API密钥安全", "password vault"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取当前密钥存储状态，确认需要管理的密钥列表和现有存储方式（TOOLS.md明文、环境变量等）。

2. **约束 (Constrain)**
设定加密标准和不可降级的安全边界——AES-256-GCM、PBKDF2HMAC 48万轮、文件权限0600。受阻时换通道，不降级交付物。

3. **证据 (Evidence)**
记录密钥迁移前后的状态，每个密钥条目有名称、描述和创建时间。不记录明文密钥值。

4. **执行 (Execute)**
初始化保险库并存储密钥，先给影响与结论，再给行动和必要证据。

初始化：
```bash
cd skills/secure-key-manager
python3 key_manager.py init
# Enter a strong password when prompted
```

存储密钥：
```bash
python3 key_manager.py set \
  -p "your-password" \
  -n "brave-search-api-key" \
  -v "BSAxxxxx..." \
  -d "Brave Search API Key"
```

运行时获取：
```python
from key_manager import SecureKeyManager

manager = SecureKeyManager()
manager.unlock("your-password")
api_key = manager.get_key("brave-search-api-key")
# Use api_key for API call, then clear from memory
```

输出脱敏：
```python
from key_manager import sanitize_output
safe_output = sanitize_output(raw_output)  # Auto-redacts patterns
```

列出和轮换：
```bash
python3 key_manager.py list -p "your-password"
# To rotate: delete old key, set new key with same name
```

5. **验证 (Verify)**
用不同于生成路径的方式回读——检查加密文件权限为0600，验证解密后密钥与原始值一致，确认输出脱敏能正确识别并遮蔽密钥模式。

6. **交付 (Deliver)**
返回保险库初始化结果和密钥存储状态，设置定期轮换提醒。如怀疑泄露，立即执行事件响应流程。

## Output

- 初始化：返回保险库创建状态和文件路径
- 存储密钥：返回存储成功/失败状态
- 获取密钥：返回解密后的密钥字符串（仅运行时使用）
- 列出密钥：返回密钥名称列表（不含明文值）
- 输出脱敏：返回脱敏后的安全字符串

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER store the vault password in code or environment variables on shared systems
- NEVER commit `.secrets.enc` or `.salt` files to public repositories
- NEVER disable output sanitization in production

**Security Layers**
- File permissions: `0600` (owner read/write only)
- Encryption: AES-256-GCM with authenticated encryption
- Key derivation: PBKDF2HMAC with 480,000 iterations + random salt
- Runtime behavior: decrypt on-demand, no persistent cleartext in memory

**Incident Response**
If leakage suspected:
1. Immediately revoke exposed keys at the provider
2. Rotate keys in the vault: `set` new value for same key name
3. Review audit logs for unauthorized access patterns

## Related Skills

- **security-hardening** — Deploy comprehensive security controls including input filtering
- **skill-security-audit** — Audit skills to detect hardcoded keys before migration
- **security-drill** — Validate that key leakage scenarios are handled correctly

## About UniqueClub

This skill is part of the **UniqueClub** security toolkit.
🌐 https://uniqueclub.ai
