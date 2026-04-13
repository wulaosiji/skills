---
name: skill-optimizer
description: |
  The premier skill optimization specialist for OpenClaw/Hermes. Analyzes, audits, and rewrites
  SKILL.md files for maximum discoverability, agent routing accuracy, SEO, and clarity.
  Performs comprehensive audits covering naming conventions (kebab-case), keyword-rich descriptions,
  usage boundaries, cross-references, guardrails, and README integration. Outputs detailed reports
  with actionable rewrite suggestions and can apply changes directly.
  Use when: "优化skill", "SEO优化", "改进技能描述", "skill写得不好", "技能搜索不到",
  "重构skill", "skill命名", "技能关键词", "提升skill发现率", "skill optimization".
  Cross-references: skill-security-audit, security-hardening, pitch-deck-creator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
---

# Skill Optimizer

> Analyze, audit, and optimize skills for maximum discoverability and agent routing accuracy.

## When to Use

Use this skill when:
- A user wants to **improve an existing skill's discoverability** or search ranking
- A skill is **not being found** by the agent when it should be triggered
- A skill's **description is unclear**, lacks keywords, or has poor boundaries
- A skill has **ambiguous naming** that conflicts with other skills
- A user wants to **SEO-optimize** their skill collection
- Creating a **new skill** and want to follow best practices from the start
- A skill needs **better guardrails** to prevent mis-invocation

Do NOT use this skill if:
- The skill is working perfectly and has high usage — don't fix what isn't broken
- The user wants to add new functionality — use feature development instead
- The issue is a security vulnerability or bug in the skill's code — use **skill-security-audit** instead

Typical triggers:
- 「帮我优化这个skill」「SEO优化技能」「技能描述怎么改」
- "skill search不到", "agent找不到我的技能", "skill命名有问题"
- "重构skill描述", "技能发现率低", "提升skill使用率"
- "optimize my skill", "SEO for skills", "improve skill discoverability"

## Workflow

### Step 1: Load and Analyze Target Skill
Ask the user for:
1. The **skill name** or **path to SKILL.md** they want to optimize
2. Any **specific issues** they've noticed (optional)

Load the `SKILL.md` file and analyze its current state.

### Step 2: Comprehensive Audit
Analyze the skill across 7 dimensions:

1. **Naming Audit** — kebab-case? No underscores/camelCase? Descriptive and discoverable?
2. **Description Audit** — Trigger keywords in multiple languages? "Use when..." explicit? Cross-references included? Output format stated?
3. **When to Use Boundaries** — Clear conditions? Anti-patterns listed? Typical trigger phrases documented?
4. **Cross-Reference Network** — Bidirectional references to related skills? Suite/kit skills linked?
5. **Guardrails & Constraints** — Explicit anti-patterns? Output constraints? Dependencies handled?
6. **README Integration** — Listed in hub README? Correct category? Compelling one-liner?
7. **Technical SEO** — Relevant YAML frontmatter? Correct file structure? Example usage patterns?

### Step 3: Generate Optimization Report
Create a structured report with these sections:

```markdown
## Skill Audit Report: <skill-name>

### Overall Score: X/100

### 1. Naming (Score: X/10)
**Current**: `<current-name>`
**Status**: ✅ Good | ⚠️ Needs Improvement | ❌ Critical Issue
**Recommendation**: `<suggested-name>`

### 2. Description (Score: X/20)
**Current**: `<current-description>`
**Optimized Version**:
```
<optimized-description>
```

### 3. When to Use Boundaries (Score: X/20)
**Missing Elements**: <list>
**Recommended Addition**: <snippet>

### 4. Cross-References (Score: X/15)
**Recommended Cross-References**:
- `<related-skill>` — <reason>

### 5. Guardrails (Score: X/15)
**Recommended Additions**: <list>

### 6. README Integration (Score: X/10)
**Status**: ✅ | ⚠️ | ❌

### 7. Technical SEO (Score: X/10)
**Tags/Structure/Examples**: <assessment>

### Summary: Priority Actions
1. **Critical**: <action>
2. **High**: <action>
3. **Medium**: <action>
4. **Low**: <action>

### Optimized SKILL.md
```yaml
---
name: <optimized-name>
description: |
  <optimized-description>
---

<optimized-body>
```
```

### Step 4: Apply Changes (Optional)
If the user approves:
1. Rewrite the `SKILL.md` with optimized content
2. Update `README.md` if needed
3. Add/modify cross-references in related skills
4. Commit with message: `seo: optimize <skill-name> for discoverability`

## Guardrails

### Anti-patterns
- NEVER rename a skill without checking for existing references in other skills
- NEVER remove functional code or scripts during optimization
- NEVER optimize blindly without understanding the skill's actual purpose

### Output Constraints
- Optimized descriptions must include **5-10 trigger keywords** in **both Chinese and English**
- All names must be **kebab-case** (no underscores, no camelCase)
- Each optimized skill must have clear **When to Use / Do NOT use** boundaries
- Every skill should reference **2-3 related skills** where applicable

### Best Practices Reference
| Bad | Good | Why |
|-----|------|-----|
| `bp-generator` | `business-plan-generator` | No abbreviations |
| `PDF2HTML` | `pdf-to-html-converter` | kebab-case, descriptive |
| `extract_content` | `content-extractor` | kebab-case |
| `feishuDoc` | `feishu-doc-handler` | Consistent style |

**Description Formula:**
```
[Primary function]. [Target audience and use case].
Use when: "<trigger 1>", "<trigger 2>", "<trigger 3>".
[Key features/capabilities].
[Cross-reference to related skills].
```

## Related Skills

- **skill-security-audit** — Audit skills for security vulnerabilities before optimizing
- **security-hardening** — Harden the agent environment for safely testing optimized skills
- 
## About UniqueClub

This skill is the **showcase example** of optimization excellence in the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
