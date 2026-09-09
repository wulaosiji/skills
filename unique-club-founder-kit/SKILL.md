---
name: unique-club-founder-kit
description: |
  ⚠️ MIGRATED: This toolkit has moved to wulaosiji/founder-skills.
  The complete AI founder toolkit by UniqueClub for fundraising, content, growth, and automation.
  Includes pitch-deck-creator, deck-web-converter, content-multiplier, investor-research, and more.
  Use when: "AI创业工具包", "founder toolkit", "startup skills", "uniqueclub", "创业者技能",
  "AI founder tools", "创业必备", "pitch deck工具", "融资技能包", "founder automation".
  Cross-references: pitch-deck-creator, deck-web-converter.
  🔄 NEW LOCATION: https://github.com/wulaosiji/founder-skills
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能的优化版本已移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills)，推荐使用新版。本版本保留用于向后兼容。

# UniqueClub Founder Kit

> ⚠️ **MIGRATED** — This skill has moved to a new repository.

## 🚨 Migration Notice

This toolkit has been **migrated** to a dedicated repository for better maintenance and updates.

**New Location:**
📂 **https://github.com/wulaosiji/founder-skills**

Please use the new repository for:
- Latest founder skills
- Updated workflows
- New additions to the toolkit

## When to Use

Use this skill when:
- You're a **startup founder** looking for AI-powered fundraising and growth tools
- You need **pitch decks**, **investor research**, or **content automation**
- You want **pre-built workflows** for fundraising sprints and content engines

**Important:** For the latest version, install from the new repository:
```bash
npx skills add wulaosiji/founder-skills
```

Do NOT use this skill if:
- You need general security skills → use **security-hardening**, **skill-security-audit**
- You need media processing → use **media_hub**
- You need Chinese navigation → use **amap-navigator**

Typical triggers:
- 「AI创业工具包」「founder toolkit」「startup skills」
- "pitch deck creator", "investor research", "content automation"
- "创业者技能", "融资PPT工具", "uniqueclub founder kit"

## Workflow

1. **探查 (Probe)**
确认用户的创业阶段和具体需求（融资、内容、增长、自动化），匹配工具包中对应的技能。

2. **约束 (Constrain)**
从新仓库安装，不降级使用旧版。设定标准：所有技能遵循 UniqueClub 质量规范，输出可交付、可验证。

3. **证据 (Evidence)**
每个技能的输出基于用户输入和可复现计算。融资数据、市场数据不编造，使用占位符或用户提供的真实数据。

4. **执行 (Execute)**
Install from the new repository and access individual skills:

```bash
npx skills add wulaosiji/founder-skills
```

The founder-skills repository includes:
- **pitch-deck-creator** — VC-ready pitch decks (.pptx)
- **deck-web-converter** — PPT/PDF to responsive HTML
- **investor-research** — Research and track investors
- **content-multiplier** — Turn one idea into multiple content pieces
- **social-post-generator** — Engaging social media content
- **video-script-creator** — Product demo and explainer scripts
- **newsletter-autopilot** — Newsletter drafting from updates
- **founder-daily-brief** — Daily summaries of meetings and tasks
- **meeting-minutes-ai** — Action items from transcripts
- **competitor-tracker** — Monitor competitor updates

**7-Day Fundraising Sprint:**
- Day 1-2: Story & Materials (pitch-deck-creator → deck-web-converter)
- Day 3-5: Outreach Preparation (content-multiplier → social-post-generator)
- Day 6-7: Execute & Track (meeting-minutes-ai → founder-daily-brief)

5. **验证 (Verify)**
验证每个技能的输出：检查文件是否生成、内容是否完整、数据是否可追溯。用不同于生成路径的方式回读输出。

6. **交付 (Deliver)**
返回最终结果，清理临时文件。确保用户获得可直接使用的交付物（PPT、HTML、研究报告等）。

## Output

This toolkit produces a range of deliverables depending on the skill used: pitch decks (.pptx), responsive HTML presentations, investor research reports, content pieces, social media posts, video scripts, newsletters, daily briefs, meeting minutes, and competitor tracking reports. All outputs follow UniqueClub quality standards and are ready for immediate use.

## Guardrails

**Anti-patterns**
- NEVER use the old `wulaosiji/skills/unique-club-founder-kit` for new projects — always install from `wulaosiji/founder-skills`.
- Do NOT fabricate financial data, market size, or investor information in any toolkit output.
- NEVER skip verification of generated deliverables before delivering to the user.

**Migration Guidelines**
- Update any existing scripts pointing to `wulaosiji/skills/unique-club-founder-kit`
- Re-install from `wulaosiji/founder-skills` for latest features
- Back up any custom EXTEND.md configurations before migrating

**Repository Status**
- This directory (`unique-club-founder-kit`) is in **maintenance mode**
- New features will only be added to `wulaosiji/founder-skills`
- Bug fixes may be backported for critical issues

## Related Skills

- **security-hardening** — Secure your founder tools and agent environment
- **skill-security-audit** — Audit skills for vulnerabilities before production use
- **secure-key-manager** — Encrypt API keys used by founder skills
- **baoyu-slide-deck** — Alternative slide generation with extensive style options

## About UniqueClub

**UniqueClub** is a curated collection of AI skills for startup founders.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/founder-skills

Built with ❤️ by founders, for founders.
