---
name: amap-navigator
description: |
  Chinese navigation and location service powered by Amap (Gaode Maps / 高德地图).
  Provides geocoding, routing, POI search, and distance calculations for addresses
  and coordinates within mainland China.
  Use when: "高德地图", "Amap导航", "中国地图", "路线规划", "POI搜索", "地址解析", "Chinese navigation", "geocoding China", "Gaode Maps routing", "distance matrix".
  Cross-references: media-hub, infographic-generator, long-form-writer.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Amap Navigator

> Amap (Gaode Maps) navigation and location services for China.

## When to Use

Use this skill when:
- The user asks for **Chinese map services**, **navigation**, or **location queries**
- Converting Chinese addresses to coordinates (geocoding) or vice versa
- Planning **routes** within mainland China
- Searching **POIs** (Points of Interest) such as restaurants, hotels, landmarks
- Calculating **distance matrix** between multiple points

Do NOT use this skill if:
- The location is outside mainland China → use global map services
- The task is general travel advice without specific addresses or coordinates
- You need map visualization slides → use **infographic-generator** for presentation output
- You need real-time traffic camera feeds or live navigation

Typical triggers:
- 「查一下高德地图」「北京到上海路线」「附近餐厅搜索」「地址转坐标」「POI搜索」「路线规划」
- "Amap navigation", "Chinese map API", "Gaode Maps routing", "geocode address in China", "POI search", "distance matrix"

## Workflow

1. **探查 (Probe)**: 完整读取需求，确认用户意图类型（地理编码/逆地理编码/路线规划/POI搜索/距离计算），确认输入地址或坐标、出行方式和语言偏好。

2. **约束 (Constrain)**: 验证输入完整性，设定边界：仅支持中国大陆、坐标使用 GCJ-02（火星坐标系）、POI结果限制 top 10-20。检查 Amap API key 是否可用，不降级交付物。

3. **证据 (Evidence)**: 每个查询结果来自 Amap Web Service API 的实时返回。路线距离和预计时间来自 Amap 路径规划服务，POI 评分和距离来自 Amap 搜索服务。

4. **执行 (Execute)**: 调用 Amap API，先给影响与结论，再给行动和必要证据。

**识别用户意图**
- Geocoding (address → coordinates)
- Reverse geocoding (coordinates → address)
- Route planning (origin → destination, driving / public transit / walking)
- POI search (nearby places by keyword and location)
- Distance calculation (batch distances between multiple points)

**验证输入**
- Ensure addresses are in Chinese or recognized English aliases
- Confirm coordinates use GCJ-02 (Mars Coordinates) as required by Amap
- Check that an Amap API key is available (stored securely via secure-key-manager)

**调用 Amap API**
Use the appropriate Amap Web Service API endpoint with proper parameters. Handle rate limits and retry on transient errors.

**格式化结果**
- Route: distance, estimated time, toll info, step-by-step directions
- POI: name, address, distance, rating (if available)
- Geocode: formatted address + latitude/longitude

5. **验证 (Verify)**: 用不同于生成路径的方式回读输出——交叉验证坐标与地址的对应关系，检查路线距离是否合理，确认 POI 结果与搜索关键词相关。

6. **交付 (Deliver)**: 返回格式化的查询结果（路线/POI列表/坐标），不暴露 API key，清理临时请求数据。

## Output

- **路线规划**: 距离（公里/米）、预计时间（分钟/小时）、收费信息、分步导航
- **POI搜索**: 名称、地址、距离、评分（如有），限制 top 10-20 最相关结果
- **地理编码**: 格式化地址 + 纬度/经度（GCJ-02）
- **逆地理编码**: 坐标对应的详细地址信息
- **距离矩阵**: 多点之间的距离和时间矩阵
- 语言: 用户偏好语言（中国场景优先中文）

## Guardrails

**Anti-patterns:**
- NEVER 在回复或日志中暴露 Amap API key
- NEVER 对中国坐标假设 WGS-84（必须使用 GCJ-02）
- NEVER 返回原始 JSON 而不做人类可读格式化
- Do NOT 对中国大陆以外的地址使用本技能
- Do NOT 对无效地址不提示就返回空结果

**Output Constraints**
- Results must be localized to user's language (Chinese preferred for China contexts)
- Distances in kilometers or meters; times in minutes/hours
- Limit POI results to top 10-20 most relevant items
- API key must never be exposed in output

**Error Handling**
- Invalid address: suggest rephrasing or provide alternative spellings
- API rate limit: queue and retry after backoff
- Missing API key: prompt user to configure via secure-key-manager

## Related Skills

- **media-hub** — Process location-based media such as travel videos or audio guides（地理位置媒体处理）
- **infographic-generator** — Visualize route maps and location data as infographics（地理位置可视化）
- **long-form-writer** — Write travel guides and location-based articles（地理位置内容创作）

## About UniqueClub

This skill is part of the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai
