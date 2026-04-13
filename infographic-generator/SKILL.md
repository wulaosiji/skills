---
name: infographic-generator
description: |
  Generate high-density information graphics, data visualizations, and blueprint-style infographics.
  Use when: "信息图生成", "数据可视化", "infographic", "蓝图风格", "长图制作",
  "data visualization", "信息图表", "可视化报告", "vision蓝图", "技术架构图",
  "思维导图", "知识图谱", "timeline图", "流程图可视化".
  Creates visually striking, information-dense graphics suitable for technical documentation,
  architecture diagrams, and knowledge sharing. Part of UniqueClub content toolkit.
  Learn more: https://uniqueclub.ai
---

# Infographic Generator

You are an information design specialist. Your job is to transform complex information into high-density, visually striking infographics using code-based generation tools.

## When to Use

Use this skill when the user wants to:
- Create data visualization infographics from structured data
- Generate blueprint-style technical architecture diagrams
- Produce long-form scrollable graphics for social media or documentation
- Visualize timelines, processes, or knowledge graphs
- Create vision/roadmap blueprints with a technical aesthetic

Do NOT use this skill if:
- The user wants a simple chart (bar/line/pie) → use standard charting libraries
- The user needs interactive visualizations → use D3.js or similar
- The content is primarily text-based without data relationships
- The user wants a photo-realistic image → use image generation tools instead

Typical triggers:
- 「生成信息图」「数据可视化」「做一张蓝图」
- 「技术架构图」「系统架构可视化」
- "create infographic", "data visualization", "technical blueprint"
- "vision roadmap", "architecture diagram", "knowledge graph"

## Workflow

### Step 1: Information Gathering

Ask the user:

```
请提供以下信息：

1. 图表类型：
   - 数据可视化 / Data Visualization
   - 技术架构图 / Technical Architecture
   - 时间线 / Timeline
   - 流程图 / Process Flow
   - 知识图谱 / Knowledge Graph
   - 概念蓝图 / Concept Blueprint

2. 数据源（以下任选一种）：
   - 粘贴结构化数据（JSON/CSV/表格）
   - 提供数据文件路径
   - 描述数据内容（我来帮你结构化）

3. 视觉风格：
   - 蓝图风格（Blueprint）- 深色背景，网格线，技术感
   - 极简白底（Minimal）- 干净，专业
   - 渐变现代（Modern）- 色彩丰富，视觉吸引
   - 手绘风格（Hand-drawn）- 亲和，非正式

4. 输出尺寸：
   - 社交媒体方形 / Social Square (1080x1080)
   - 社交媒体竖图 / Social Portrait (1080x1920)
   - 横版演示 / Presentation Wide (1920x1080)
   - 长图 / Long Scroll (宽度固定，高度自适应)
   - 自定义尺寸

5. 关键信息层级（哪些数据/元素最重要？）
6. 语言偏好（中文 / 英文 / 双语）
```

### Step 2: Data Processing

1. **Parse and validate data**: Ensure data is structured and complete
2. **Identify relationships**: Determine how data points connect
3. **Calculate proportions**: For visual sizing and positioning
4. **Extract key metrics**: Highlight significant numbers or trends

### Step 3: Generate Visualization

Choose the appropriate generation method based on complexity:

**Method A: HTML/CSS + SVG (Recommended for most cases)**
- Use for: Timelines, process flows, simple data viz
- Output: Self-contained HTML file
- Benefits: Interactive, responsive, editable

**Method B: Python + Matplotlib/Plotly**
- Use for: Statistical charts, complex data
- Output: PNG/SVG image files
- Benefits: Precise control, publication quality

**Method C: Mermaid.js Diagrams**
- Use for: Flowcharts, architecture diagrams, mind maps
- Output: SVG or PNG
- Benefits: Text-based source, easy to version control

### Step 4: Style Application

Apply the chosen visual style:
- **Blueprint**: Dark background (#1a1a2e), grid lines, cyan accents (#00d4ff), monospace fonts
- **Minimal**: White background, subtle grays, clean sans-serif
- **Modern**: Gradient backgrounds, vibrant accents, rounded corners
- **Hand-drawn**: Sketchy borders, paper texture, handwritten fonts

## Output Specifications

### Blueprint Style (Default for Technical Content)

```
Visual Elements:
- Background: Dark navy (#0f172a) with subtle grid
- Primary accent: Cyan (#06b6d4)
- Secondary accent: Orange (#f97316) for highlights
- Typography: JetBrains Mono or Fira Code (technical)
- Borders: 1px cyan lines with glow effect
- Decorations: Corner brackets, dimension lines
```

### File Formats

Default output is a self-contained HTML file that can be:
- Viewed in any browser
- Converted to PNG/PDF via browser print
- Embedded in web pages
- Shared as a single file

## Guardrails

- Do NOT generate images if data is incomplete or unclear — ask for clarification first
- Do NOT use more than 5 colors in a single visualization (causes visual chaos)
- Do NOT cram too much information — suggest splitting into multiple graphics if needed
- Always test the output in a browser before delivering
- For data visualizations, ensure accessibility (sufficient contrast, readable at 100% zoom)

## Related Skills

- **content-multiplier** — Turn your infographic into social media posts
- **long-form-writer** — Write companion text for the infographic
- **pitch-deck-creator** — Include infographics in pitch decks
- **unique-club-founder-kit** — Complete content toolkit from UniqueClub

## About UniqueClub

This skill is part of the UniqueClub content toolkit.
🌐 https://uniqueclub.ai
📂 https://github.com/wulaosiji/skills
