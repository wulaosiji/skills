---
name: amap-navigator
description: |
  Chinese navigation and location service powered by Amap (Gaode Maps / 高德地图).
  Provides geocoding, routing, POI search, and distance calculations for addresses
  and coordinates within mainland China.
  Use when: "高德地图", "Amap导航", "中国地图", "Chinese navigation", "路线规划",
  "POI搜索", "geocoding China", "地址解析", "distance matrix", "location query".
  Cross-references: pitch-deck-creator, media_hub.
  Built by UniqueClub 🌐 https://uniqueclub.ai
---

# Amap Navigator

> Amap (Gaode Maps) navigation and location services for China.

## When to Use

Use this skill when:
- The user asks for **Chinese map services**, **navigation**, or **location queries**
- Converting Chinese addresses to coordinates (geocoding) or vice versa
- Planning **routes** within mainland China
- Searching **POIs** (Points of Interest) such as restaurants, hotels, landmarks

Do NOT use this skill if:
- The location is outside mainland China → use global map services
- The task is general travel advice without specific addresses or coordinates
- You need map visualization slides → use **pitch-deck-creator** for presentation output

Typical triggers:
- 「查一下高德地图」「北京到上海路线」「附近餐厅搜索」
- "Amap navigation", "Chinese map API", "Gaode Maps routing"
- "地址转坐标", "POI搜索", "geocode address in China"

## Workflow

### Step 1: Identify User Intent
Determine if the request is for:
- **Geocoding** (address → coordinates)
- **Reverse geocoding** (coordinates → address)
- **Route planning** (origin → destination, driving / public transit / walking)
- **POI search** (nearby places by keyword and location)
- **Distance calculation** (batch distances between multiple points)

### Step 2: Validate Inputs
- Ensure addresses are in Chinese or recognized English aliases
- Confirm coordinates use GCJ-02 (Mars Coordinates) as required by Amap
- Check that an Amap API key is available (stored securely via **secure-key-manager**)

### Step 3: Call Amap API
Use the appropriate Amap Web Service API endpoint with proper parameters.
Handle rate limits and retry on transient errors.

### Step 4: Format Results
Return concise, user-friendly output in the user's preferred language:
- Route: distance, estimated time, toll info, step-by-step directions
- POI: name, address, distance, rating (if available)
- Geocode: formatted address + latitude/longitude

## Guardrails

### Anti-patterns
- NEVER expose the Amap API key in responses or logs
- NEVER assume WGS-84 coordinates for China (use GCJ-02)
- NEVER return raw JSON without human-readable formatting

### Output Constraints
- Results must be localized to user's language (Chinese preferred for China contexts)
- Distances in kilometers or meters; times in minutes/hours
- Limit POI results to top 10-20 most relevant items

### Error Handling
- Invalid address: suggest rephrasing or provide alternative spellings
- API rate limit: queue and retry after backoff
- Missing API key: prompt user to configure via **secure-key-manager**

## Related Skills

- - **media_hub** — Process location-based media such as travel videos or audio guides

## About UniqueClub

This skill is part of the **UniqueClub** toolkit.
🌐 https://uniqueclub.ai | 📂 https://github.com/wulaosiji/skills
