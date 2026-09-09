---
name: infographic-generator
description: |
  Generate high-density information graphics, data visualizations, and blueprint-style infographics.
  Creates visually striking, information-dense graphics suitable for technical documentation,
  architecture diagrams, and knowledge sharing.
  Use when: "信息图生成", "数据可视化", "蓝图风格", "长图制作", "技术架构图", "infographic", "data visualization", "technical blueprint", "architecture diagram", "knowledge graph".
  Cross-references: long-form-writer, md-to-wechat, image-ocr.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能的优化版本已移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) 作为 `infographic-generator`，推荐使用新版。本版本保留用于向后兼容。

# Infographic Generator

> You are an information design specialist. Transform complex information into high-density, visually striking infographics using code-based generation tools.

## When to Use

Use this skill when:
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
- 「生成信息图」「数据可视化」「做一张蓝图」「技术架构图」「系统架构可视化」「长图制作」
- "create infographic", "data visualization", "technical blueprint", "vision roadmap", "architecture diagram", "knowledge graph"

## Workflow

1. **探查 (Probe)**: 完整读取需求，确认图表类型、数据源、视觉风格、输出尺寸和关键信息层级。

2. **约束 (Constrain)**: 验证数据完整性，设定边界：单图不超过5种颜色、信息密度合理、可访问性达标。数据不完整时先请求澄清，不降级交付物。

3. **证据 (Evidence)**: 每个数据点必须来自输入、具体信源或可复现计算。解析并验证数据结构，识别数据关系，计算比例，提取关键指标。

4. **执行 (Execute)**: 选择合适的生成方法，先给影响与结论，再给行动和必要证据。

**信息收集清单**

1. 图表类型：数据可视化 / 技术架构图 / 时间线 / 流程图 / 知识图谱 / 概念蓝图
2. 数据源：粘贴结构化数据（JSON/CSV/表格）/ 提供数据文件路径 / 描述数据内容
3. 视觉风格：蓝图风格 / 极简白底 / 渐变现代 / 手绘风格
4. 输出尺寸：社交媒体方形(1080x1080) / 竖图(1080x1920) / 横版(1920x1080) / 长图 / 自定义
5. 关键信息层级
6. 语言偏好（中文 / 英文 / 双语）

**数据处理**
1. Parse and validate data: Ensure data is structured and complete
2. Identify relationships: Determine how data points connect
3. Calculate proportions: For visual sizing and positioning
4. Extract key metrics: Highlight significant numbers or trends

**生成方法选择**

Method A: HTML/CSS + SVG (Recommended) — 用于时间线、流程图、简单数据可视化，输出自包含HTML文件，可交互、响应式、可编辑。

Method B: Python + Matplotlib/Plotly — 用于统计图表、复杂数据，输出PNG/SVG，精确控制、出版质量。

Method C: Mermaid.js Diagrams — 用于流程图、架构图、思维导图，输出SVG/PNG，文本源易版本控制。

**视觉风格应用**
- Blueprint: Dark background (#1a1a2e), grid lines, cyan accents (#00d4ff), monospace fonts
- Minimal: White background, subtle grays, clean sans-serif
- Modern: Gradient backgrounds, vibrant accents, rounded corners
- Hand-drawn: Sketchy borders, paper texture, handwritten fonts

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——在浏览器中测试 HTML 输出，检查颜色对比度（可访问性）、文字可读性（100%缩放下）、数据准确性。

6. **交付 (Deliver)**: 返回自包含 HTML 文件或图片，可通过浏览器打印转换为 PNG/PDF，清理临时文件。

## Output Specifications

**Blueprint Style (Default for Technical Content)**

- Background: Dark navy (#0f172a) with subtle grid
- Primary accent: Cyan (#06b6d4)
- Secondary accent: Orange (#f97316) for highlights
- Typography: JetBrains Mono or Fira Code (technical)
- Borders: 1px cyan lines with glow effect
- Decorations: Corner brackets, dimension lines

**File Formats**

Default output is a self-contained HTML file that can be viewed in any browser, converted to PNG/PDF via browser print, embedded in web pages, or shared as a single file.

## Output

- **HTML** (default): Self-contained, interactive, editable
- **PNG/SVG**: Via browser print or Python generation
- **PDF**: Professional delivery via browser print
- 尺寸: 按需求指定（社交媒体方形/竖图、横版演示、长图）

## Guardrails

**Anti-patterns:**
- NEVER 数据不完整或不清晰时生成图片——先请求澄清
- NEVER 单图使用超过5种颜色（造成视觉混乱）
- NEVER 塞入过多信息——建议拆分为多张图
- Do NOT 不测试输出就交付
- Do NOT 忽略可访问性（对比度不足、文字过小）

**Constraints**
- Always test the output in a browser before delivering
- For data visualizations, ensure accessibility (sufficient contrast, readable at 100% zoom)
- Original data sources remain untouched
- Color palette limited to 5 colors per visualization

## Related Skills

- **long-form-writer** — Write companion text for the infographic（配套长文）
- **md-to-wechat** — Convert infographic content for WeChat publishing（公众号适配）
- **image-ocr** — Extract text from existing infographics for reuse（素材提取）

## About UniqueClub

This skill is part of the UniqueClub content toolkit.
🌐 https://uniqueclub.ai
