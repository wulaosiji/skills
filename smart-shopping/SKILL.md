---
name: smart-shopping
description: |
  京东/淘宝智能购物助手，基于Cookie认证进行商品搜索、价格比较、库存查询、降价监控和优惠推荐，支持跨平台比价和最优凑单建议。
  Use when: "查京东价格", "淘宝比价", "智能购物", "price check", "shopping assistant", "查商品库存", "降价提醒", "find deals".
  一次性Cookie配置后实现长期自动化价格查询、库存监控和优惠推荐，仅做研究和推荐不完成实际购买。Cross-references: logic-validator, content-extractor, document-hub, email-sender.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Smart Shopping Assistant

> Cookie-based intelligent shopping assistant for JD and Taobao. One-time setup enables long-term automated price checks, inventory queries, and deal recommendations.

## When to Use

Use this skill when:
- Search products on JD or Taobao
- Check real-time prices and inventory
- Compare prices across platforms
- Set up price drop monitoring
- Get product recommendations with filters
- Find coupons and optimal bundling deals

Do NOT use this skill if:
- The user wants to complete a purchase transaction → redirect to the official platform
- The user hasn't provided platform cookies yet → guide them through cookie extraction first
- The user needs general shopping advice without platform-specific data

Typical triggers:
- 「帮我查京东价格」「淘宝比价」「智能购物」
- "check price on JD", "Taobao price comparison", "shopping assistant"
- 「查商品库存」「降价提醒」「自动领券凑单」
- "price monitor", "find deals", "coupon aggregation"

## Workflow

遵循六步推进法（探查→约束→证据→执行→验证→交付）完成操作。

1. **探查 (Probe)**
完整读取用户需求，确认目标平台和搜索关键词。检查用户是否已保存对应平台（`jd` 或 `taobao`）的Cookie。

2. **约束 (Constrain)**
如未认证，提供Cookie提取指南并引导用户完成配置。设定不可降级的标准——仅做研究和推荐，不完成实际购买。受阻时换通道，不降级交付物。

Cookie提取步骤：
1. Log in to the platform (JD or Taobao)
2. Open browser dev tools (F12)
3. Copy the cookie data via the provided script
4. Send the cookie data to save securely

3. **证据 (Evidence)**
每个价格和库存数据必须来自平台实际响应，不编造价格。记录查询时间和平台作为可追溯证据。价格波动时注明查询时间。

4. **执行 (Execute)**
使用保存的Cookie执行认证搜索，先给影响与结论，再给行动和必要证据。返回结构化结果包括：
- Product names and prices
- Stock/inventory status
- Ratings and reviews
- Promotions and coupons

基于搜索结果提供推荐：
- Best value picks
- Price trend insights
- Similar product comparisons
- Optimal purchase timing

5. **验证 (Verify)**
用不同于生成路径的方式回读——交叉验证价格是否在合理区间（可结合logic-validator），确认库存状态准确，检查优惠券是否有效。关键推荐至少两个商品对比验证。

6. **交付 (Deliver)**
返回商品搜索结果和推荐建议，不完成实际购买。设置降价监控时返回监控配置状态。

## Output

返回结构化商品列表，每个商品包含：
- 商品名称和价格
- 库存状态
- 评分和评论数
- 促销和优惠券信息
- 平台来源（JD/Taobao）

推荐结果包含最佳性价比选择、价格趋势分析和最优购买时机建议。

## Guardrails

以下约束确保安全、可靠地使用本技能。

**Anti-patterns**
- NEVER 完成实际购买交易——仅做研究和推荐
- NEVER 与外部共享用户Cookie数据
- Do NOT 忽略Cookie过期的情况，需引导用户重新认证
- Do NOT 违反平台服务条款和速率限制

**Constraints**
- Cookies are stored locally and encrypted; never share them externally
- Cookies expire after 30 days and must be refreshed
- Do NOT complete actual purchases — only research and recommendations
- Respect platform terms of service and rate limits
- If cookie authentication fails, guide the user to re-authenticate

## Cookie Extraction Guides

**JD (京东)**

1. Visit https://www.jd.com and log in
2. Press F12 to open Developer Tools
3. Run this script in the Console:

```javascript
(function() {
    const data = {
        cookies: document.cookie,
        time: new Date().toLocaleString()
    };
    navigator.clipboard.writeText(JSON.stringify(data, null, 2));
    alert('已复制！粘贴发给助手即可');
})();
```

4. Paste the copied JSON here to save securely

**Taobao (淘宝)**

1. Visit https://www.taobao.com and log in
2. Press F12 → Application → Cookies
3. Copy all cookie values
4. Paste them here to save securely

## References

- `smart_shopping.py` — Main assistant implementation

## Related Skills

- **logic-validator** — 价格合理性校验和真伪鉴别，避免推荐明显低价假货
- **content-extractor** — 补充商品信息和评测内容提取
- **email-sender** — 降价提醒和优惠信息邮件通知
- **document-hub** — 导出比价结果为Excel文档

## About UniqueClub

Part of the UniqueClub toolkit — a collection of skills for AI-powered content creation and automation.
🌐 https://uniqueclub.ai
