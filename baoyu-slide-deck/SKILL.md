---
name: baoyu-slide-deck
description: |
  Generates professional slide deck images and exports to PPTX/PDF from any content.
  Creates structured outlines, style-guided image prompts, and individual slide images.
  Supports 16+ visual presets, custom dimensions, audience adaptation, and multi-language output.
  Use when: "生成PPT", "create slides", "做演示文稿", "make a presentation", "生成幻灯片",
  "slide deck", "pitch deck", "融资PPT", "生成路演材料", "generate deck".
  Cross-references: amap-navigator, media_hub.
  Built by UniqueClub 🌐 https://uniqueclub.ai
---

# Baoyu Slide Deck

> Transform content into professional slide deck images, PPTX, and PDF.

## When to Use

Use this skill when:
- The user asks to **create slides**, **make a presentation**, or **generate a deck**
- Converting articles, outlines, or raw content into **PPTX/PDF** or **slide images**
- Producing **pitch decks**, **tutorials**, **keynotes**, or **infographics**
- Needing **styled visual slides** with custom dimensions and audience targeting

Do NOT use this skill if:
- The user only wants a text outline without any visual output
- The task is video editing or audio processing → use **media_hub** instead
- You need map-based location slides → use **amap-navigator** for geolocation data first

Typical triggers:
- 「帮我做PPT」「生成幻灯片」「做路演 deck」
- "create slides", "make a presentation", "generate deck", "slide deck"
- "融资PPT", "pitch deck", "生成演示文稿", "PPT制作"

## Workflow

### Step 1: Setup & Analyze
1. **Load Preferences** — Check for `.baoyu-skills/baoyu-slide-deck/EXTEND.md` (project) or `$HOME/.baoyu-skills/baoyu-slide-deck/EXTEND.md` (user).
2. **Analyze Content** — Save source content, detect language, determine topic slug, and recommend slide count.
3. **Check Existing** — If `slide-deck/{topic-slug}/` exists, prompt the user: regenerate outline, regenerate images, backup & regenerate, or exit.

### Step 2: Confirm Options (Required)
Ask the user via interactive questions:
- **Style** — Choose from 16 presets or custom dimensions (texture, mood, typography, density)
- **Audience** — general, beginners, experts, executives
- **Slide count** — recommended, fewer, or more
- **Review outline** — yes/no
- **Review prompts** — yes/no

### Step 3: Generate Outline
- Read the selected style preset or combine dimension files
- Build `outline.md` following `references/outline-template.md`
- If `--outline-only`, stop here

### Step 4: Review Outline (Conditional)
- Display slide-by-slide summary: `# | Title | Type | Layout`
- Ask user to proceed, edit, or regenerate

### Step 5: Generate Prompts
- Read `references/base-prompt.md`
- For each slide, create a prompt file in `prompts/NN-slide-{slug}.md`
- If `--prompts-only`, stop here

### Step 6: Review Prompts (Conditional)
- Display prompt list
- Ask user to proceed, edit, or regenerate

### Step 7: Generate Images
- Generate slide images sequentially using a shared session ID
- Backup existing images before overwriting
- Auto-retry once on failure

### Step 8: Merge to PPTX & PDF
```bash
npx -y bun ${SKILL_DIR}/scripts/merge-to-pptx.ts <slide-deck-dir>
npx -y bun ${SKILL_DIR}/scripts/merge-to-pdf.ts <slide-deck-dir>
```

### Step 9: Output Summary
```
Slide Deck Complete!
Topic: [topic]
Style: [preset name or custom]
Location: [directory path]
Slides: N total
Files: outline.md, prompts/, *.png, *.pptx, *.pdf
```

## Guardrails

### Anti-patterns
- NEVER skip Step 2 (confirmation) — style, audience, and counts must be confirmed
- NEVER generate images without checking existing content first
- NEVER discard existing slides without backing them up

### Output Constraints
- Slide count: 5-30 slides depending on content length (default recommendations: <1k words = 5-10, 1k-3k = 10-18, 3k-5k = 15-25, >5k = 20-30)
- All user-facing text uses the user's preferred language; technical terms remain in English
- Image generation maintains style consistency via shared session ID

### Partial Workflow Options
- `--outline-only` → Steps 1-3 only
- `--prompts-only` → Steps 1-5 only
- `--images-only` → Skip to Step 7 (requires existing prompts/)
- `--regenerate N` → Regenerate specific slide(s) only

## Related Skills

- **amap-navigator** — Add location data, routes, or map visualizations to slides
- **media_hub** — Include transcribed or processed audio/video content in presentations

## About UniqueClub

This skill is part of the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
