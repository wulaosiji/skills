---
name: long-form-writer
description: |
  长文生成与深度写作工具，支持结构化长文（2000字以上）的生成，包括教程、研究报告、分析报告等。
  Use when: "写一篇深度教程", "生成研究报告", "扩写大纲", "长文写作", "详细分析报告", "多章节文档", "generate long tutorials", "write research reports", "expand outline", "in-depth analysis".
  Cross-references: md-to-wechat, image-ocr, infographic-generator.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

> ⚠️ **已迁移**: 本技能的优化版本已移至 [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) 作为 `founder-content-writer`，推荐使用新版。本版本保留用于向后兼容。

# Long Form Writer

> Generate comprehensive long-form articles and reports with structured depth.

## When to Use

Use this skill when:
- 需要创建超过2000字的深度教程或指南
- 撰写结构化的研究报告或白皮书
- 将零散素材扩展为完整文章
- 需要多层递进的内容结构
- 生成带有案例分析的专业文档
- 基于数据生成叙事性报告

Do NOT use this skill if:
- 只需要简短回复（少于500字）
- 需要实时生成的快速内容
- 没有明确的内容大纲或方向
- 目标受众和目的不明确
- 不需要案例或数据支撑的观点文

Typical triggers:
- 「写一篇深度教程」「生成研究报告」「扩写大纲」「长文写作」「详细分析报告」「多章节文档」
- "Write a comprehensive tutorial", "Generate research report", "Expand this outline", "Long-form article", "In-depth analysis", "Multi-chapter document"

## Workflow

1. **探查 (Probe)**: 完整读取需求指定的全部输入（大纲、素材、数据文件、聊天记录等），确认文章类型、目标长度、受众和核心论点。

2. **约束 (Constrain)**: 验证输入完整性，设定边界和不可降级的交付标准：每章必有案例、字数达标、逻辑连贯、数据标注来源。受阻时换通道（如补充素材），不降级交付物。

3. **证据 (Evidence)**: 每个数字必须来自输入、具体信源或可复现计算。收集支撑数据：真实用户案例、统计数据、对比趋势、截图建议。

4. **执行 (Execute)**: 按四层架构生成内容，先给影响与结论，再给行动和必要证据。

**Layer 1: Structure (大纲规划)**

```markdown
## Article Blueprint

**Type**: [tutorial | report | analysis | guide]
**Target Length**: [3000 | 5000 | 8000 | 10000] words
**Audience**: [technical | general | executive]

### Chapter Plan
1. [Title] - [Word count] - [Key points]
2. [Title] - [Word count] - [Key points]
```

**Layer 2: Expand (章节展开)**

For each chapter: Write 500-1500 words, include concept + example + application, add subsections if needed, mark [EXPAND] for sections needing more depth.

**Layer 3: Enrich (素材增强)**

- Cases: Real user examples from chat history
- Data: Statistics, comparisons, trends
- Visuals: Screenshot suggestions, diagram descriptions
- FAQ: Common questions and answers

**Layer 4: Polish (润色检查)**

- [ ] Remove AI filler phrases
- [ ] Check for 3-part structures → convert to 2 or 4
- [ ] Vary sentence length
- [ ] Add personal insights
- [ ] Verify logical flow between chapters

5. **验证 (Verify)**: 用"可能失败"的动作验证——不同于生成路径的方式回读输出。检查总字数是否达标、每章是否有具体案例、数据是否标注来源、章节间逻辑是否连贯。

6. **交付 (Deliver)**: 返回完整 Markdown 文档，清理临时文件。可配合 `md-to-wechat` 转换为公众号格式，或 `pdf` 生成专业PDF。

## Usage Patterns

**Pattern 1: From Data to Report**
```bash
long-form-writer generate --input data.json --type report --template structured --output report.md
```

**Pattern 2: From Outline to Article**
```bash
long-form-writer expand --outline outline.md --depth 3 --word-count 5000 --output article.md
```

**Pattern 3: Chat History to Guide**
```bash
long-form-writer guide --chat-history chat.json --topic "OpenClaw Usage" --output guide.md
```

## Output

- **Markdown** (default): Editable, version control friendly
- **PDF**: Professional delivery via pdf skill
- **Word**: Collaborative editing via document-hub
- **HTML**: Web publishing via md-to-wechat
- 目标长度: 2000字以上，按章节分配字数

## Guardrails

**Anti-patterns:**
- NEVER 生成空洞的填充内容
- NEVER 每个章节都用三段式结构
- NEVER 缺乏具体案例的理论堆砌
- NEVER 忽略目标读者的背景水平
- Do NOT 不标注数据来源

**Limitations**
- 需要明确的大纲或输入素材
- 长文生成耗时较长
- 需要人工审核事实准确性
- 不适合需要实时数据的动态内容

**Quality Standards**
1. 每章必有案例: 理论结合实际
2. 字数达标: 总字数符合目标
3. 逻辑连贯: 章节间过渡自然
4. 数据引用: 标注数据来源
5. 首尾呼应: 结论回应引言

## Quality Checklist

Before delivery, verify:
1. [ ] Each chapter has concrete examples
2. [ ] Total word count meets target
3. [ ] No section is purely theoretical
4. [ ] Data/sources are cited
5. [ ] Conclusion ties back to introduction
6. [ ] Formatting is consistent

## Related Skills

- **md-to-wechat** — 转换为公众号文章格式（平台适配）
- **image-ocr** — 识别图片中的文字素材（素材处理）
- **infographic-generator** — 为长文生成配套信息图（视觉增强）

## About UniqueClub

Part of the UniqueClub toolkit - a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
