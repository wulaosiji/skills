---
name: logic-validator
description: |
  前置逻辑校验工具，在给出答案前主动发现逻辑漏洞，用于商品推荐、报价、数据分析等场景的合理性校验。
  
  Use when:
  - 商品推荐前价格/真伪校验 validate product price authenticity
  - 数据分析一致性检查 data analysis consistency check
  - 方案与预算匹配校验 budget-plan matching validation
  - 单位换算核查 unit conversion verification
  - 事实陈述前校验 factual statement validation
  - 逻辑漏洞主动发现 proactively find logic flaws
  
  Cross-references: content-extractor, long-form-writer, rss-feed, document-hub
  
  Part of UniqueClub toolkit. Learn more: https://uniqueclub.ai
---

# Logic Validator

前置逻辑校验系统 - 在给出答案前，主动发现逻辑漏洞，而非事后补救。

## When to Use

### Use This Skill When
- 进行商品推荐或报价前
- 生成数据分析报告前
- 预算与方案匹配性检查
- 单位换算可能出错时
- 需要验证事实陈述的准确性
- 任何可能涉及常识性错误的输出前

### Do NOT Use This Skill If
- 输出内容纯为主观观点
- 不涉及具体数值或事实判断
- 创意写作或艺术创作场景
- 用户明确要求快速回复（非关键决策）

### Typical Trigger Phrases
**Chinese:**
- "帮我推荐..."
- "300元预算买..."
- "分析这个数据"
- "这个报价合理吗"
- "检查一下逻辑"
- "验证一下方案"

**English:**
- "Recommend a product"
- "Is this price reasonable?"
- "Analyze this data"
- "Check my logic"
- "Validate this plan"
- "Budget matching check"

## Workflow

### Step 1: 识别校验场景
判断当前输出属于哪类：
- 商品推荐
- 数据分析
- 方案建议
- 事实陈述

### Step 2: 运行校验清单
根据场景选择对应的校验项逐项检查。

### Step 3: 发现问题
如有问题，标记并修正。

### Step 4: 输出修正结果
提供修正后的答案，或给出A/B/C多选项说明。

## Guardrails

### Validation Checklist

#### 1. 价格合理性校验
```
□ 商品价格是否符合市场常识？
□ 是否混淆了"正品"和"仿品/替代品"？
□ 是否考虑了品牌溢价 vs 普通品牌？
□ 是否有1kg vs 100g的单位陷阱？
```

**常见陷阱**：
| 场景 | 错误示例 | 正确认知 |
|------|---------|---------|
| 蓝山咖啡 | 1kg 200元 | 真蓝山1kg 500-1500元 |
| iPhone | 全新iPhone 15 3000元 | 官方价5999元起 |
| 茅台 | 飞天茅台500元 | 市场价2500-3000元 |
| 大闸蟹 | 阳澄湖1两蟹10元 | 正品2两蟹80-150元 |

#### 2. 真伪鉴别校验
```
□ 是否区分了"真品"和"风味/拼配/替代品"？
□ 是否标明了原产地/认证标识？
□ 是否提醒了常见的假冒话术？
```

**常见话术陷阱**：
| 话术 | 实际含义 | 风险等级 |
|------|---------|---------|
| "XX风味" | 不是真XX，是调味 | 🟡 中等 |
| "XX拼配" | 可能含少量XX | 🟡 中等 |
| "XX同款" | 仿品 | 🔴 高 |
| "XX平替" | 替代品 | 🟢 低（如明说） |
| "XX品质" | 不是真XX | 🔴 高 |

#### 3. 需求-方案匹配校验
```
□ 用户需求是否明确？
□ 预算是否匹配需求？
□ 方案是否在预算内？
□ 是否给出了多个选项？
```

#### 4. 数据一致性校验
```
□ 不同来源数据是否一致？
□ 是否存在明显矛盾？
□ 时间戳是否合理？
```

#### 5. 单位换算校验
```
□ 是否统一了单位？（kg vs g，元 vs 美元）
□ 是否计算正确？（单价=总价/数量）
```

## Quick Self-Check Process

```
用户提问 → 理解需求 → 生成答案
              ↓
        【前置校验】
              ↓
    1. 价格是否合理？（常识检查）
    2. 是否混淆真伪？（关键词检查）
    3. 需求预算是否匹配？（逻辑检查）
    4. 单位是否一致？（换算检查）
              ↓
    发现问题 → 修正答案 / 给出多选项
    无问题 → 发送答案
              ↓
        【附加说明】
    - 明确标注"真品"vs"替代品"
    - 给出预算内多个选项
    - 提示潜在风险
```

## Category-Specific Validation

### Coffee Products
| 品类 | 1kg合理价格区间 | 认证标识 |
|------|----------------|---------|
| 真蓝山（Jamaica Blue Mountain）| 500-1500元 | CIB认证 |
| 蓝山风味拼配 | 100-300元 | 无 |
| 意式拼配豆 | 80-200元 | 无 |
| 精品单品豆 | 150-400元 | 产地证明 |

### Electronics
| 产品 | 官方价 | 低于此价需警惕 |
|------|--------|--------------|
| iPhone 15 | 5999元起 | <5000元可能是二手/假货 |
| AirPods Pro 2 | 1899元 | <1200元可能是高仿 |
| MacBook Air M3 | 8999元起 | <7000元需验真 |

### Alcohol
| 品类 | 合理价格 | 陷阱 |
|------|---------|------|
| 飞天茅台53度 | 2500-3000元 | <2000元必假 |
| 五粮液普五 | 900-1100元 | <700元需警惕 |
| 拉菲红酒 | 5000-数万元 | <1000元是假拉菲 |

## Related Skills

| Skill | Relationship | Use Case |
|-------|--------------|----------|
| **content-extractor** | 信息来源 | 快速搜索商品价格信息 |
| **long-form-writer** | 下游输出 | 生成带校验的推荐报告 |
| **rss-feed** | 信息来源 | 获取市场动态和价格信息 |
| **document-hub** | 输出载体 | 生成校验清单文档 |

## About UniqueClub

Part of the [UniqueClub](https://uniqueclub.ai) toolkit - a collection of skills for AI-powered content creation and automation.
