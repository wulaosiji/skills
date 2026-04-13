---
name: long-form-writer
description: |
  长文生成与深度写作工具，支持结构化长文（2000字以上）的生成，包括教程、研究报告、分析报告等。
  
  Use when:
  - 生成长篇教程（2000字以上）generate long tutorials 2000+ words
  - 撰写研究报告 write research reports
  - 创建深度分析报告 create in-depth analysis
  - 将原始数据转为叙事结构 transform data to narrative
  - 扩写大纲为完整内容 expand outline to full content
  - 多章节长文档生成 multi-chapter document generation
  
  Cross-references: content-extractor, document-hub, pdf, email-sender, md-to-wechat
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

> 🚀 **Migrated to [wulaosiji/founder-skills](https://github.com/wulaosiji/founder-skills) as `founder-content-writer`.**
> 
> This version is kept for backward compatibility. For the latest updates, use the founder-skills version.



# Long Form Writer

Generate comprehensive long-form articles and reports with structured depth.

## When to Use

### Use This Skill When
- 需要创建超过2000字的深度教程或指南
- 撰写结构化的研究报告或白皮书
- 将零散素材扩展为完整文章
- 需要多层递进的内容结构
- 生成带有案例分析的专业文档
- 基于数据生成叙事性报告

### Do NOT Use This Skill If
- 只需要简短回复（少于500字）
- 需要实时生成的快速内容
- 没有明确的内容大纲或方向
- 目标受众和目的不明确
- 不需要案例或数据支撑的观点文

### Typical Trigger Phrases
**Chinese:**
- "写一篇深度教程"
- "生成研究报告"
- "扩写大纲"
- "长文写作"
- "详细分析报告"
- "多章节文档"
- "2000字以上文章"

**English:**
- "Write a comprehensive tutorial"
- "Generate research report"
- "Expand this outline"
- "Long-form article"
- "In-depth analysis"
- "Multi-chapter document"
- "2000+ words content"

## Workflow

### Layer 1: Structure (大纲规划)
Define the article architecture:

```markdown
## Article Blueprint

**Type**: [tutorial | report | analysis | guide]
**Target Length**: [3000 | 5000 | 8000 | 10000] words
**Audience**: [technical | general | executive]

### Chapter Plan
1. [Title] - [Word count] - [Key points]
2. [Title] - [Word count] - [Key points]
...
```

### Layer 2: Expand (章节展开)
Generate each chapter independently:

```
For each chapter:
1. Write 500-1500 words
2. Include: concept + example + application
3. Add subsections if needed (recursive)
4. Mark [EXPAND] for sections needing more depth
```

### Layer 3: Enrich (素材增强)
Add supporting materials:

- **Cases**: Real user examples from chat history
- **Data**: Statistics, comparisons, trends
- **Visuals**: Screenshot suggestions, diagram descriptions
- **FAQ**: Common questions and answers

### Layer 4: Polish (润色检查)
Apply quality standards:

- [ ] Remove AI filler phrases
- [ ] Check for 3-part structures → convert to 2 or 4
- [ ] Vary sentence length
- [ ] Add personal insights
- [ ] Verify logical flow between chapters

## Guardrails

### Anti-Patterns
- ❌ 生成空洞的填充内容
- ❌ 每个章节都用三段式结构
- ❌ 缺乏具体案例的理论堆砌
- ❌ 忽略目标读者的背景水平

### Limitations
- 需要明确的大纲或输入素材
- 长文生成耗时较长
- 需要人工审核事实准确性
- 不适合需要实时数据的动态内容

### Quality Standards
1. **每章必有案例**: 理论结合实际
2. **字数达标**: 总字数符合目标
3. **逻辑连贯**: 章节间过渡自然
4. **数据引用**: 标注数据来源
5. **首尾呼应**: 结论回应引言

## Usage Patterns

### Pattern 1: From Data to Report
```bash
# Input: analysis.json
# Output: comprehensive report

long-form-writer generate \
  --input data.json \
  --type report \
  --template structured \
  --output report.md
```

### Pattern 2: From Outline to Article
```bash
# Input: outline.md
# Output: full tutorial

long-form-writer expand \
  --outline outline.md \
  --depth 3 \
  --word-count 5000 \
  --output article.md
```

### Pattern 3: Chat History to Guide
```bash
# Extract cases from chat, generate guide

long-form-writer guide \
  --chat-history chat.json \
  --topic "OpenClaw Usage" \
  --output guide.md
```

## Core Workflow (4 Layers)

### L1: Structure
- Define article type and target length
- Create chapter breakdown
- Allocate word count per chapter

### L2: Expand
- Generate content chapter by chapter
- Include concept-explanation-application pattern
- Mark sections needing expansion

### L3: Enrich
- Inject real cases
- Add data and statistics
- Suggest visual elements
- Include Q&A sections

### L4: Polish
- Remove filler phrases
- Vary sentence structure
- Add personal voice
- Verify cross-chapter coherence

## Integration with Other Skills

| Skill | Usage |
|-------|-------|
| content-extractor | 提取外部素材作为写作原料 |
| document-hub | 导出为Word/Excel格式 |
| pdf | 生成最终PDF交付物 |
| email-sender | 发送报告邮件 |
| md-to-wechat | 转换为公众号文章 |

## Output Formats

- **Markdown** (default): Editable, version control friendly
- **PDF**: Professional delivery via pdf skill
- **Word**: Collaborative editing via document-hub
- **HTML**: Web publishing via md-to-wechat

## Quality Checklist

Before delivery, verify:

1. [ ] Each chapter has concrete examples
2. [ ] Total word count meets target
3. [ ] No section is purely theoretical
4. [ ] Data/sources are cited
5. [ ] Conclusion ties back to introduction
6. [ ] Formatting is consistent

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 素材来源 | 提取外部内容作为写作素材 |
| **document-hub** | 格式输出 | 生成Word/Excel版本 |
| **pdf** | 格式输出 | 生成专业PDF文档 |
| **email-sender** | 分发渠道 | 发送报告邮件 |
| **md-to-wechat** | 平台适配 | 转换为公众号文章格式 |
| **image-ocr** | 素材处理 | 识别图片中的文字素材 |

## Examples

See `references/examples.md` for sample outputs.

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
