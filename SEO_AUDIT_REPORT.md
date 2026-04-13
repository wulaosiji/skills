# Skills SEO 审计报告

**审计时间**: 2026-04-13  
**技能总数**: 63  
**审计工具**: skill-optimizer

---

## 📊 总体评分

| 维度 | 达标数 | 总数 | 覆盖率 | 评级 |
|------|--------|------|--------|------|
| 命名规范 (kebab-case) | 61 | 63 | 97% | 🟢 优秀 |
| When to Use 边界 | 10 | 63 | 16% | 🔴 需改进 |
| Do NOT Use 边界 | 3 | 63 | 5% | 🔴 需改进 |
| 交叉引用 | 3 | 63 | 5% | 🔴 需改进 |
| Guardrails/约束 | 4 | 63 | 6% | 🔴 需改进 |
| Examples | 3 | 63 | 5% | 🔴 需改进 |
| Workflow/步骤 | 7 | 63 | 11% | 🔴 需改进 |

**综合评分**: 21/100 ⚠️

---

## 🏆 优秀技能（完整度 ≥ 80%）

| 技能 | 评分 | 亮点 |
|------|------|------|
| skill-optimizer | 100% | 所有维度完整，自洽性最佳 |
| BP_Generator | 100% | SEO优化标杆，交叉引用完善 |
| BP_to_HTML | 100% | 与BP_Generator形成技能网络 |

---

## ⚠️ 需重点改进技能（完整度 < 30%）

### 🔴 Critical - 核心技能但严重缺失

| 技能 | 问题 | 影响 |
|------|------|------|
| feishu-doc-orchestrator | 缺失所有边界定义 | 飞书生态核心技能，易被误调用 |
| feishu-wiki-orchestrator | 缺失所有边界定义 | 知识库核心技能 |
| long-form-writer | 仅有When to Use | 内容生成类重要技能 |
| gh-cli | 缺失所有边界定义 | 开发工具类重要技能 |
| content-extractor | 缺失所有边界定义 | 数据处理类重要技能 |

### 🟡 High - 功能完整但发现性差

| 技能 | 问题 | 建议 |
|------|------|------|
| baoyu-slide-deck | 699行但无边界定义 | 增加 When to Use/Not Use |
| zhuoran-selfie | 426行但无边界定义 | 明确与 qizhuo/clawra 的区别 |
| zhuoran-video-selfie | 353行但无边界定义 | 明确与 selfie 的区别 |
| x-twitter-scraper | 有 Guardrails 但无边界 | 补充 When to Use |
| voice-clone | 318行但无边界定义 | 增加触发关键词 |

### 🟢 Medium - 短小精悍但可完善

| 技能 | 当前行数 | 建议 |
|------|----------|------|
| amap-navigator | 9行 | 补充完整 SKILL.md |
| document-hub | 16行 | 补充完整 SKILL.md |
| infographic-generator | 15行 | 补充完整 SKILL.md |
| media_hub | 16行 | 补充完整 SKILL.md |
| rss-feed | 9行 | 补充完整 SKILL.md |
| security-drill | 27行 | 补充完整 SKILL.md |
| skill-security-audit | 9行 | 补充完整 SKILL.md |

---

## 📋 具体问题清单

### 1. 命名问题（2个技能）

| 技能目录 | 当前命名 | 问题 | 建议 |
|----------|----------|------|------|
| pdf | `pdf` | 过于简短，无连字符 | 重命名为 `pdf-processor` 或 `pdf-toolkit` |
| security-hardening | `security_hardening` | 使用下划线 | 重命名为 `security-hardening` |

### 2. 飞书技能生态（15个）一致性缺失

所有飞书技能都缺少统一的边界定义，建议建立标准模板：

```markdown
## When to Use
- 飞书文档/表格/群聊相关操作
- 需要与飞书API交互的场景

Do NOT use if:
- 非飞书平台（如钉钉、企业微信）→ 使用对应平台技能
- 纯本地文件处理 → 使用本地工具技能
```

### 3. Selfie 技能群定位模糊

4个 selfie 技能（zhuoran/qizhuo/clawra/clawra-video）缺少差异化描述：
- 用户不清楚该用哪个
- 建议每个技能明确说明：风格差异、使用场景、推荐人群

### 4. 交叉引用网络缺失

当前仅3个技能有交叉引用：
- BP_Generator ↔ BP_to_HTML（优秀案例）
- x-twitter-scraper（有 anti-pattern 指引）

**建议建立以下技能对**：
| 技能A | 技能B | 关联理由 |
|-------|-------|----------|
| feishu-doc-orchestrator | feishu-wiki-orchestrator | 文档vs知识库 |
| content-extractor | wechat-article-fetcher | 通用vs专用 |
| twitter-scraper | x-twitter-scraper | 功能重合需区分 |
| image-ocr | pdf | 图像文字vs文档处理 |
| video-generation | remotion-best-practices | 生成vs最佳实践 |

---

## 🎯 优先级行动建议

### P0 - Critical（立即处理）

1. **修复命名问题**
   - `pdf` → `pdf-processor`
   - `security_hardening` → `security-hardening`

2. **为核心飞书技能添加边界定义**
   - feishu-doc-orchestrator
   - feishu-wiki-orchestrator
   - feishu-chat-extractor

3. **区分 Selfie 技能群**
   - 每个 selfie 技能添加差异化描述
   - 建立互引关系

### P1 - High（本周处理）

4. **补充 When to Use 到高使用量技能**
   - long-form-writer
   - gh-cli
   - content-extractor
   - voice-clone

5. **建立交叉引用网络**
   - 识别功能相关的技能对
   - 在每个技能中提及相关技能

### P2 - Medium（本月处理）

6. **为短小技能补充完整文档**
   - amap-navigator
   - document-hub
   - rss-feed
   - skill-security-audit

7. **添加 Examples 到复杂技能**
   - baoyu-slide-deck
   - zhuoran-selfie
   - video-generation

### P3 - Low（持续优化）

8. **全面添加 Guardrails**
   - anti-patterns
   - output constraints
   - dependency handling

9. **关键词优化**
   - 每个技能添加 5-10 个中英文触发词

---

## 📈 预期效果

完成 P0-P2 后预期提升：

| 指标 | 当前 | 目标 | 提升 |
|------|------|------|------|
| When to Use 覆盖率 | 16% | 80% | +64% |
| 交叉引用覆盖率 | 5% | 40% | +35% |
| Examples 覆盖率 | 5% | 30% | +25% |
| 综合评分 | 21/100 | 70/100 | +49分 |

---

## 🛠️ 使用 skill-optimizer 进行优化

对每个技能执行：

```
帮我优化 <skill-name> 这个 skill
```

skill-optimizer 将输出：
1. 7维度评分
2. 具体问题列表
3. 优化后的 SKILL.md 草稿
4. 优先级建议

---

*报告生成完毕。需要我针对特定技能进行详细优化吗？*
