---
name: smart-shopping
description: |
  Smart shopping assistant for JD (京东) and Taobao (淘宝) with cookie-based authentication.
  Use when the user wants to search products, compare prices, check inventory, monitor price drops, or find deals on Chinese e-commerce platforms.
  Use when: "帮我查京东价格", "淘宝比价", "price check", "shopping assistant", "查商品库存", "降价提醒", "智能购物".
  Requires one-time cookie setup, then enables persistent automated searches.
---

# Smart Shopping Assistant

Cookie-based intelligent shopping assistant for JD and Taobao. One-time setup enables long-term automated price checks, inventory queries, and deal recommendations.

## When to Use

Use this skill when the user wants to:
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
- "check price on JD", "Taobao price comparison"
- "price monitor", "shopping assistant", "find deals"
- 「查商品库存」「降价提醒」「自动领券凑单"

## Workflow

### Step 1: Verify Authentication

Check if the user has saved cookies for the requested platform (`jd` or `taobao`).

If not authenticated, provide the cookie extraction guide and ask them to:
1. Log in to the platform (JD or Taobao)
2. Open browser dev tools (F12)
3. Copy the cookie data via the provided script
4. Send the cookie data to save securely

### Step 2: Gather Search Requirements

Ask the user for:
- Target platform (`jd` or `taobao`)
- Search keyword or product URL
- Optional filters (price range, brand, rating, etc.)

### Step 3: Execute Search

Use the saved cookie to perform an authenticated search on the platform and return structured results including:
- Product names and prices
- Stock/inventory status
- Ratings and reviews
- Promotions and coupons

### Step 4: Provide Recommendations

Based on the search results, help the user with:
- Best value picks
- Price trend insights
- Similar product comparisons
- Optimal purchase timing

## Guardrails

- Cookies are stored locally and encrypted; never share them externally
- Cookies expire after 30 days and must be refreshed
- Do NOT complete actual purchases — only research and recommendations
- Respect platform terms of service and rate limits
- If cookie authentication fails, guide the user to re-authenticate

## Cookie Extraction Guides

### JD (京东)

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

### Taobao (淘宝)

1. Visit https://www.taobao.com and log in
2. Press F12 → Application → Cookies
3. Copy all cookie values
4. Paste them here to save securely

## Related Skills

- **travel-booking** — For flight and hotel price comparisons
- **coupon-aggregator** — For finding platform-wide promotions and discounts

## References

- `smart_shopping.py` — Main assistant implementation

## About UniqueClub

Part of the UniqueClub toolkit.
🌐 https://uniqueclub.ai
📂 https://github.com/wulaosiji/skills
