---
name: secure-key-manager
description: |
  Enterprise-grade secure key management for AI agents. Encrypts API keys using AES-256-GCM with
  PBKDF2HMAC key derivation (480k rounds). Features runtime decryption, automatic output sanitization,
  and strict file permissions (0600). Replaces plaintext key storage in TOOLS.md.
  Use when: "密钥管理", "secure key storage", "API key encryption", "密钥加密", "password vault",
  "密钥保护", "secret management", "key rotation", "敏感信息存储", "API密钥安全".
  Cross-references: security-hardening, skill-security-audit.
  Built by UniqueClub 🌐 https://uniqueclub.ai
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
- "API密钥加密", "secret storage", "key rotation"

## Workflow

### Step 1: Initialize Vault
```bash
cd skills/secure-key-manager
python3 key_manager.py init
# Enter a strong password when prompted
```

### Step 2: Store Keys
```bash
python3 key_manager.py set \
  -p "your-password" \
  -n "brave-search-api-key" \
  -v "BSAxxxxx..." \
  -d "Brave Search API Key"
```

### Step 3: Retrieve Keys (Runtime)
```python
from key_manager import SecureKeyManager

manager = SecureKeyManager()
manager.unlock("your-password")
api_key = manager.get_key("brave-search-api-key")
# Use api_key for API call, then clear from memory
```

### Step 4: Enable Output Sanitization
```python
from key_manager import sanitize_output
safe_output = sanitize_output(raw_output)  # Auto-redacts patterns
```

### Step 5: List & Rotate
```bash
python3 key_manager.py list -p "your-password"
# To rotate: delete old key, set new key with same name
```

## Guardrails

### Anti-patterns
- NEVER store the vault password in code or environment variables on shared systems
- NEVER commit `.secrets.enc` or `.salt` files to public repositories
- NEVER disable output sanitization in production

### Security Layers
- File permissions: `0600` (owner read/write only)
- Encryption: AES-256-GCM with authenticated encryption
- Key derivation: PBKDF2HMAC with 480,000 iterations + random salt
- Runtime behavior: decrypt on-demand, no persistent cleartext in memory

### Incident Response
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
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
