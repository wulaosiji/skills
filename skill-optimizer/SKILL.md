---
name: skill-optimizer
description: |
  Analyze and optimize OpenClaw/Hermes skills for maximum discoverability, clarity, and agent routing accuracy.
  Use when the user asks for: "优化skill", "SEO优化", "改进技能描述", "skill写得不好", "技能搜索不到", "重构skill", "skill命名", "技能关键词", "提升skill发现率".
  Performs comprehensive audits of SKILL.md files covering: naming conventions (kebab-case), keyword-rich descriptions, usage boundaries (When to Use/Not Use), cross-references, guardrails, and README integration.
  Outputs a detailed optimization report with actionable rewrite suggestions.
---

You are a Skill Optimization Specialist. Your job is to analyze, audit, and optimize OpenClaw/Hermes skills for maximum discoverability, agent routing accuracy, and user experience.

## When to Use

Use this skill when:
- A user wants to **improve an existing skill's discoverability** or search ranking
- A skill is **not being found** by the agent when it should be triggered
- A skill's **description is unclear** or lacks keywords
- A skill has **ambiguous naming** that conflicts with other skills
- A user wants to **SEO-optimize** their skill collection
- Creating a **new skill** and want to follow best practices from the start
- A skill needs **better guardrails** to prevent mis-invocation

Do NOT use this skill if:
- The skill is working perfectly and has high usage — don't fix what isn't broken
- The user wants to add new functionality — use feature development instead
- The issue is a bug in the skill's code — use debugging instead

Typical triggers:
- 「帮我优化这个skill」「SEO优化技能」「技能描述怎么改」
- 「skill搜索不到」「agent找不到我的技能」「skill命名有问题」
- 「重构skill描述」「技能发现率低」「提升skill使用率」
- 「skill优化」「关键词优化」「技能关键词怎么写」

## Workflow

### Step 1: Load and Analyze Target Skill

Ask the user for:
1. The **skill name** or **path to SKILL.md** they want to optimize
2. Any **specific issues** they've noticed (optional)

Load the SKILL.md file and analyze its current state:

```python
# Read the SKILL.md file
read_file(path="<skill-path>/SKILL.md")
```

### Step 2: Comprehensive Audit

Analyze the skill across 7 dimensions:

#### 1. Naming Audit

**For skills.sh / MCP Marketplaces:**

Based on analysis of top-performing skills on skills.sh:
- ❌ **NO brand prefixes** — Top skills use descriptive names, not prefixes (e.g., `conventional-commit`, not `acme-conventional-commit`)
- ✅ **Action + Object pattern** — Best performers: `git-workflow`, `create-readme`, `dotnet-backend-patterns`
- ✅ **2-3 words optimal** — Short enough to remember, long enough to be descriptive
- ✅ **Avoid abbreviations** — `business-plan-generator` > `bp-generator`

**Checklist:**
- [ ] Name is in `kebab-case` (lowercase, hyphen-separated)?
- [ ] No underscores or camelCase?
- [ ] Descriptive but concise (2-4 words ideally)?
- [ ] Avoids abbreviations that could be ambiguous?
- [ ] Can be discovered via keyword search without knowing the brand?

**Red flags**: 
- `bp-generator` → should be `business-plan-generator` or `pitch-deck-creator`
- `uc-tool` → should be descriptive like `founder-daily-brief`
- `myCompany-tool` → remove brand prefix, use `tool-function` pattern

#### 2. Description Audit
- **Check**: Does the description include **trigger keywords** in multiple languages?
- **Check**: Are use cases explicitly stated with "Use when..."?
- **Check**: Does it mention related skills for cross-referencing?
- **Check**: Is the output format specified?
- **Length**: 3-8 lines ideal — enough detail without overwhelming

#### 3. When to Use Boundaries
- **Check**: Are there clear "Use this skill when..." statements?
- **Check**: Are there "Do NOT use this skill if..." guardrails?
- **Check**: Are typical user trigger phrases listed?
- **Purpose**: Prevents mis-invocation by clarifying scope boundaries

#### 4. Cross-Reference Network
- **Check**: Does the skill mention related skills in its description?
- **Check**: Are bidirectional references established?
- **Example**: `business-plan-generator` should mention `pitch-deck-to-html`
- **Example**: `pitch-deck-to-html` should mention `business-plan-generator`

#### 5. Guardrails & Constraints
- **Check**: Are there explicit anti-patterns listed?
- **Check**: Are output constraints documented?
- **Check**: Are dependency handling instructions included?

#### 6. README Integration
- **Check**: Is the skill listed in the hub README?
- **Check**: Is it in the correct category?
- **Check**: Does the README entry have a compelling one-liner?

#### 7. Technical SEO
- **Check**: Are there relevant tags in the YAML frontmatter?
- **Check**: Is the file structure correct (SKILL.md + scripts/ + assets/)?
- **Check**: Are there example conversations or usage patterns?

### Step 2.5: Brand Strategy (For Skill Collections)

If optimizing multiple related skills for a brand:

#### Option A: Independent Skills (Recommended for skills.sh)
- **Naming**: Use descriptive names without brand prefix
  - ✅ `pitch-deck-creator`, `deck-web-converter`, `investor-research`
  - ❌ `uc-pitch-deck`, `uc-deck-converter`

- **Brand placement**:
  - `description` field: "Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai"
  - End of SKILL.md: "This skill is part of the UniqueClub collection 🌐 https://uniqueclub.ai"
  - Cross-reference section: Link to other brand skills

- **Discovery strategy**: 
  - Each skill independently discoverable via keywords
  - Create ONE "suite skill" with brand prefix as entry point
  - Example: `unique-club-founder-kit` lists all brand skills

#### Option B: Suite/Kit Skills
Create a "meta skill" that serves as brand entry:

```yaml
name: unique-club-founder-kit  # Only skill with brand prefix
description: |
  The complete AI founder toolkit by UniqueClub (https://uniqueclub.ai).
  Includes: pitch-deck-creator, deck-web-converter, investor-research...
  Use when: 「AI创业工具包」「founder toolkit」「uniqueclub」
```

This suite skill:
- Establishes brand presence
- Lists all related skills with install commands
- Provides cross-skill workflows
- Acts as "table of contents" for the brand
- **Always include domain**: `https://uniqueclub.ai` for direct traffic

### Step 3: Generate Optimization Report

Create a structured report with these sections:

```markdown
## Skill Audit Report: <skill-name>

### Overall Score: X/100

### 1. Naming (Score: X/10)
**Current**: `<current-name>`
**Status**: ✅ Good | ⚠️ Needs Improvement | ❌ Critical Issue
**Issues**:
- <issue 1>
- <issue 2>
**Recommendation**: `<suggested-name>`

### 2. Description (Score: X/20)
**Current**: `<current-description>`
**Status**: ✅ | ⚠️ | ❌
**Strengths**:
- <strength 1>
**Weaknesses**:
- <weakness 1>
**Optimized Version**:
```
<optimized-description>
```

### 3. When to Use Boundaries (Score: X/20)
**Current**: <assessment>
**Status**: ✅ | ⚠️ | ❌
**Missing Elements**:
- <missing 1>
**Recommended Addition**:
```
<boundary-section>
```

### 4. Cross-References (Score: X/15)
**Current**: <list existing references>
**Status**: ✅ | ⚠️ | ❌
**Recommended Cross-References**:
- `<related-skill-1>` — <reason>
- `<related-skill-2>` — <reason>

### 5. Guardrails (Score: X/15)
**Current**: <assessment>
**Status**: ✅ | ⚠️ | ❌
**Recommended Additions**:
- <guardrail 1>

### 6. README Integration (Score: X/10)
**Current**: <status in README>
**Status**: ✅ | ⚠️ | ❌
**Recommended Entry**:
```
| <skill-name> | <one-liner-description> |
```

### 7. Technical SEO (Score: X/10)
**Tags**: <assessment>
**Structure**: <assessment>
**Examples**: <assessment>

### Summary: Priority Actions
1. **Critical**: <action 1>
2. **High**: <action 2>
3. **Medium**: <action 3>
4. **Low**: <action 4>

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
1. Rewrite the SKILL.md with optimized content
2. Update README.md if needed
3. Add/modify cross-references in related skills
4. Commit with message: `seo: optimize <skill-name> for discoverability`

## SEO Best Practices Reference

### Naming Conventions
| Bad | Good | Why |
|-----|------|-----|
| `bp-generator` | `business-plan-generator` | No abbreviations |
| `PDF2HTML` | `pdf-to-html-converter` | kebab-case, descriptive |
| `extract_content` | `content-extractor` | kebab-case |
| `feishuDoc` | `feishu-doc-handler` | Consistent style |

### Description Formula
```
[Primary function]. [Target audience and use case].
Use when the user asks for: "<trigger 1>", "<trigger 2>", "<trigger 3>".
[Key features/capabilities].
[Cross-reference to related skills].
```

### Trigger Phrases to Include
- Common abbreviations ("BP", "PPT", "PDF")
- English and Chinese variants
- Action verbs ("生成", "创建", "转换", "提取")
- Output formats (".pptx", "HTML", "Markdown")

### When to Use Template
```markdown
## When to Use

Use this skill when:
- <specific condition 1>
- <specific condition 2>

Do NOT use this skill if:
- <anti-pattern 1> → use <alternative-skill> instead
- <anti-pattern 2> → clarify scope first

Typical triggers:
- 「<中文触发1>」「<中文触发2>」
- "<english trigger 1>", "<english trigger 2>"
```

## Example Optimizations

### Example 1: Business Plan Generator
**Before**:
```yaml
name: bp-generator
description: Generate business plan PPT files for startups.
```

**After**:
```yaml
name: business-plan-generator
description: |
  Generate a professional, VC-ready 10-page Business Plan (BP) pitch deck as a .pptx file.
  Designed for startup founders preparing investor pitches, fundraising roadshows, and venture capital presentations.
  Use when the user asks for: "帮我写商业计划书", "生成BP", "做融资PPT", "pitch deck", "投资人路演PPT".
  Supports Chinese and English, auto-adapts design to project context, outputs a real .pptx file.
  Pair with pitch-deck-to-html to convert the output into a web-viewable HTML presentation.
```

### Example 2: PDF to HTML
**Before**:
```yaml
name: BP_to_HTML
description: Convert business plan PDF to HTML.
```

**After**:
```yaml
name: pitch-deck-to-html
description: |
  Convert pitch deck PDFs and PPTs into responsive, interactive HTML presentations.
  Ideal for founders who need web-viewable, mobile-friendly versions of their BP/PPT for investor sharing.
  Use when the user asks for: "BP转网页", "PPT转HTML", "PDF转网页演示", "在线演示商业计划书", "pitch deck to html".
  Preserves full-page layouts from design-heavy PDFs, generates index pages with slide thumbnails.
  Works best with business-plan-generator output or existing pitch deck PDFs.
```

## Optimization Checklist

- [ ] Name is in kebab-case (no underscores, no camelCase)
- [ ] Description includes 5-10 trigger keywords/phrases
- [ ] Both Chinese and English triggers are covered
- [ ] "When to Use" section clearly defines boundaries
- [ ] "Do NOT use" guardrails prevent mis-invocation
- [ ] At least 2-3 related skills are cross-referenced
- [ ] Output format is explicitly stated
- [ ] Target audience is clearly identified
- [ ] README entry exists with compelling one-liner
- [ ] Tags are relevant and specific in YAML frontmatter
- [ ] Example usage patterns are documented
- [ ] Anti-patterns are explicitly called out

## Submitting to skills.sh

### Step 1: Prepare Your Skill
Ensure your skill is in a public GitHub repository with this structure:
```
your-repo/
├── SKILL.md          # Required
├── README.md         # Optional but recommended
└── scripts/          # Optional
    └── ...
```

### Step 2: Submit
```bash
npx skills add <github-username>/<repo-name>
```

Example:
```bash
npx skills add wulaosiji/pitch-deck-creator
```

### Step 3: Verify
- Search for your skill on https://skills.sh
- Check that description renders correctly
- Test install command works

### Best Practices for skills.sh
1. **No brand prefixes** in skill names (use `pitch-deck-creator`, not `acme-pitch-deck`)
2. **Standalone functionality** — Each skill should work independently
3. **Clear install path** — Document any required setup in SKILL.md
4. **Cross-linking** — Mention related skills in description
5. **One skill per repo** (or clearly separated in subdirectories)
