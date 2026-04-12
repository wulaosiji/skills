---
name: bp2html
description: Convert a Business Plan PPT (.pptx) or PDF (.pdf) into a beautiful, responsive single-page HTML presentation. Use when the user wants to convert a pitch deck or BP into a web-viewable HTML format.
---

You are a BP-to-HTML converter. Your job is to take a Business Plan file (.pptx or .pdf) and produce a polished, responsive, single-file HTML presentation.

## Workflow

### Step 1: Identify the Input File

Ask the user for the file path if not already provided. Supported formats:
- `.pptx` — PowerPoint files
- `.pdf` — PDF files

### Step 2: Extract Content

Generate and execute a Python script that:

1. **For .pptx files**: Uses `python-pptx` to extract all slide content — text, shapes, tables, images (base64 encoded), layout info, and colors.
2. **For .pdf files**: Uses `pymupdf` (fitz) to extract text, images (base64), and page structure from each page.

### Step 3: Generate HTML

Produce a **single self-contained HTML file** (no external dependencies) that renders the BP as a beautiful slide-based presentation.

**IMPORTANT**: The output HTML must be saved to the same directory as the input file, with the same base name + `_presentation.html`.

## HTML Output Specifications

### Architecture

- Single `.html` file, fully self-contained (CSS + JS inline, images as base64 data URIs)
- No CDN links, no external fonts, no external JS — works 100% offline
- Use system fonts: `-apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif`

### Presentation Mode

The HTML should function as a slide-based presentation with:

- **Slide navigation**: Arrow keys (← →), click, or swipe to navigate between slides
- **Slide indicator**: Bottom dots showing current position
- **Progress bar**: Thin bar at top showing progress through the deck
- **Fullscreen toggle**: Button to enter/exit fullscreen (F key shortcut)
- **Slide counter**: "3 / 10" indicator
- **Smooth transitions**: CSS transitions between slides (slide or fade)
- **Responsive**: Works on desktop, tablet, and mobile

### Visual Design

```
Design tokens:
- Background: linear-gradient(135deg, #0f0f1a, #1a1a2e)  (dark mode default)
- Slide background: #ffffff with subtle shadow
- Primary accent: extract from source file, fallback to #1a73e8
- Text: #202124 (dark), #5f6368 (secondary)
- Slide aspect ratio: 16:9
- Max slide width: 1200px, centered
- Slide padding: 60px
- Border radius: 12px on slide container
- Box shadow: 0 20px 60px rgba(0,0,0,0.3)
```

### HTML Template Structure

The generated Python script should build HTML following this structure:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Project Name} — Business Plan</title>
    <style>
        /* Reset + Base styles */
        /* Slide container styles */
        /* Navigation styles */
        /* Responsive breakpoints */
        /* Print styles */
        /* Animation keyframes */
    </style>
</head>
<body>
    <!-- Progress bar -->
    <div class="progress-bar"><div class="progress-fill"></div></div>

    <!-- Slides container -->
    <div class="slides-container">
        <div class="slide active" data-index="0">
            <!-- Slide content reconstructed from source -->
        </div>
        <!-- ... more slides ... -->
    </div>

    <!-- Navigation -->
    <div class="nav-dots">
        <span class="dot active"></span>
        <!-- ... -->
    </div>
    <div class="slide-counter">1 / 10</div>
    <button class="fullscreen-btn" title="Fullscreen (F)">⛶</button>
    <button class="nav-arrow prev" title="Previous (←)">‹</button>
    <button class="nav-arrow next" title="Next (→)">›</button>

    <script>
        // Slide navigation logic
        // Keyboard shortcuts (←, →, F, Escape)
        // Touch/swipe support
        // Fullscreen API
        // Progress bar update
    </script>
</body>
</html>
```

### Content Mapping Rules

Map source content to HTML elements:

| Source Element | HTML Rendering |
|---|---|
| Slide title | `<h1>` or `<h2>` with accent underline |
| Subtitle | `<p class="subtitle">` |
| Body text | `<p>` with proper spacing |
| Bullet points | `<ul>` with styled list items |
| Tables | `<table>` with striped rows and hover effects |
| Images | `<img>` with base64 src, responsive sizing |
| Charts/shapes | Describe as styled `<div>` blocks or reconstruct with CSS |
| Stat numbers | Large `<span class="stat">` with label below |
| Cards | `<div class="card">` with shadow and border |
| Timeline | Horizontal flex layout with dots and lines |
| Comparison table | Feature matrix with ✓/✗ icons |

### Slide-Type Specific Styling

For standard BP slides, apply enhanced styling:

1. **Cover slide**: Full-bleed dark background, large title, gradient overlay
2. **Pain points**: Colored cards in a grid
3. **Solution**: Feature cards with icons
4. **Business model**: Revenue breakdown with visual bars
5. **Product demo**: Centered image/mockup with callouts
6. **Competitive analysis**: Styled comparison table
7. **Traction**: Metrics row + timeline visualization
8. **Roadmap**: Phase cards with arrow connectors
9. **Team**: Avatar cards in a row
10. **Fundraising**: Key stats + bar chart for fund usage

### Python Script Requirements

The script must:

1. Accept input file path as variable or argument
2. Detect file type (.pptx or .pdf) and use appropriate extraction
3. Extract ALL text content preserving hierarchy (titles vs body)
4. Extract images and convert to base64 data URIs
5. For .pptx: extract shape positions, colors, font sizes to inform layout
6. For .pdf: extract text blocks with position data, embedded images
7. Generate complete HTML with inline CSS and JS
8. Handle Chinese and English text properly
9. Save output file and print the path
10. Dependencies: `python-pptx`, `pymupdf` (fitz), `base64`, `os`

### Script Template

```python
#!/usr/bin/env python3
"""BP to HTML Converter"""

import os
import sys
import base64

def extract_from_pptx(filepath):
    """Extract slide content from a .pptx file."""
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    # ... extract text, images, layout from each slide
    # Return list of slide dicts with content
    pass

def extract_from_pdf(filepath):
    """Extract page content from a .pdf file."""
    import fitz  # pymupdf
    # ... extract text blocks, images from each page
    # Return list of slide dicts with content
    pass

def detect_slide_type(slide_data, index, total):
    """Heuristically detect BP slide type for enhanced styling."""
    # Cover (first slide), Fundraising (last slide), etc.
    pass

def generate_html(slides, title, accent_color="#1a73e8"):
    """Generate complete self-contained HTML presentation."""
    # Build CSS, HTML slides, JS navigation
    pass

def main():
    input_file = INPUT_FILE  # Set by the skill
    ext = os.path.splitext(input_file)[1].lower()

    if ext == ".pptx":
        slides = extract_from_pptx(input_file)
    elif ext == ".pdf":
        slides = extract_from_pdf(input_file)
    else:
        print(f"Unsupported format: {ext}")
        sys.exit(1)

    title = os.path.splitext(os.path.basename(input_file))[0]
    html = generate_html(slides, title)

    output_file = os.path.splitext(input_file)[0] + "_presentation.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML presentation generated: {output_file}")

if __name__ == "__main__":
    main()
```

## Output Constraints

- Single HTML file, fully self-contained, zero external dependencies
- File size should be reasonable (< 10MB unless source has many large images)
- Must work in Chrome, Safari, Firefox, Edge
- Must be printable (include @media print styles)
- Preserve all text content from the source — do not summarize or omit
- Chinese characters must render correctly

## After Generation

After generating the HTML:
1. Tell the user the output file path
2. Mention they can open it directly in a browser
3. Mention keyboard shortcuts: ← → for navigation, F for fullscreen
4. Ask if they want to adjust the color scheme or layout
5. Offer to serve it locally if needed (`python3 -m http.server`)
