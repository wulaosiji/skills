---
name: remotion-best-practices
description: |
  Best practices and domain-specific knowledge for Remotion — programmatic video creation in React.
  Covers animations, audio, captions, 3D, charts, compositions, transitions, text effects, FFmpeg operations, and 30+ specialized rule files with code examples.
  Use when: "remotion", "React视频", "programmatic video", "remotion动画", "视频生成", "remotion best practices", "React video creation", "remotion音频", "视频渲染", "remotion composition".
  Loads on-demand rule files for captions, FFmpeg, audio visualization, 3D, animations, assets, and more.
  Cross-references: gh-cli, find-skills.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Remotion Best Practices

Domain-specific knowledge and best practices for creating videos programmatically with Remotion (React-based video framework).

## When to Use

Use this skill whenever you are dealing with Remotion code to obtain the domain-specific knowledge, including:
- Writing or editing Remotion compositions, animations, or transitions
- Working with audio, video, images, or fonts in Remotion
- Creating captions, subtitles, charts, 3D content, or text animations
- Using FFmpeg for video operations (trimming, silence detection) within a Remotion workflow
- Troubleshooting Remotion rendering, timing, or asset issues

Do NOT use this skill if:
- You need general React/Next.js best practices (not video-specific) → use general React knowledge
- You need to discover/install agent skills → use `find-skills` instead
- You need GitHub operations → use `gh-cli` instead
- You need non-Remotion video editing (Premiere, Final Cut, DaVinci) → this skill is Remotion-specific

Typical triggers:
- 「remotion」「React视频」「视频生成」「remotion动画」
- "programmatic video" "remotion best practices" "React video creation"
- 「remotion音频」「视频渲染」「remotion composition」

## Workflow

1. **探查 (Probe)**
确认用户正在处理的 Remotion 具体领域（动画 / 音频 / 字幕 / 3D / 图表 / 转场 / 资源管理 / FFmpeg），确认项目使用的 Remotion 版本和相关依赖。

2. **约束 (Constrain)**
设定 Remotion 项目约束：使用官方推荐的组件和 API，不绕过 Remotion 的渲染管线。对于 FFmpeg 操作，确认系统已安装 ffmpeg。不降级交付——若缺少依赖，先指导安装。

3. **证据 (Evidence)**
所有最佳实践和代码示例来自本技能的 `rules/` 目录下的规则文件。根据具体领域加载对应的规则文件获取详细说明和代码示例，不凭记忆编造 API 用法。

4. **执行 (Execute)**
根据领域加载对应的规则文件（见下方 "How to use" 和规则文件列表），应用其中的最佳实践和代码模式到用户的 Remotion 项目中。对于常见操作：
- **Captions/subtitles**: load `rules/subtitles.md`
- **FFmpeg operations** (trimming, silence detection): load `rules/ffmpeg.md`
- **Audio visualization** (spectrum, waveform, bass-reactive): load `rules/audio-visualization.md`

5. **验证 (Verify)**
验证 Remotion 代码：确认组件导入正确、props 类型匹配、时间计算（frame/fps）准确、资源路径有效。对于渲染问题，建议用户运行 `npx remotion render` 或 `npx remotion studio` 验证输出。

6. **交付 (Deliver)**
返回应用了最佳实践的 Remotion 代码或修改建议，引用对应的规则文件来源。对于多文件修改，总结每个文件的变更点。不保留临时文件。

## Output

Remotion code snippets, component implementations, or modification guidance based on the relevant rule files. Output includes: correct component usage, prop configurations, animation timing patterns, asset import statements, and references to the specific `rules/*.md` file that supports each recommendation. For FFmpeg operations, returns command-line instructions.

## Captions

When dealing with captions or subtitles, load the [./rules/subtitles.md](./rules/subtitles.md) file for more information.

## Using FFmpeg

For some video operations, such as trimming videos or detecting silence, FFmpeg should be used. Load the [./rules/ffmpeg.md](./rules/ffmpeg.md) file for more information.

## Audio visualization

When needing to visualize audio (spectrum bars, waveforms, bass-reactive effects), load the [./rules/audio-visualization.md](./rules/audio-visualization.md) file for more information.

## How to use

Read individual rule files for detailed explanations and code examples:

- [rules/3d.md](rules/3d.md) - 3D content in Remotion using Three.js and React Three Fiber
- [rules/animations.md](rules/animations.md) - Fundamental animation skills for Remotion
- [rules/assets.md](rules/assets.md) - Importing images, videos, audio, and fonts into Remotion
- [rules/audio.md](rules/audio.md) - Using audio and sound in Remotion - importing, trimming, volume, speed, pitch
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Dynamically set composition duration, dimensions, and props
- [rules/can-decode.md](rules/can-decode.md) - Check if a video can be decoded by the browser using Mediabunny
- [rules/charts.md](rules/charts.md) - Chart and data visualization patterns for Remotion (bar, pie, line, stock charts)
- [rules/compositions.md](rules/compositions.md) - Defining compositions, stills, folders, default props and dynamic metadata
- [rules/extract-frames.md](rules/extract-frames.md) - Extract frames from videos at specific timestamps using Mediabunny
- [rules/fonts.md](rules/fonts.md) - Loading Google Fonts and local fonts in Remotion
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Getting the duration of an audio file in seconds with Mediabunny
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Getting the width and height of a video file with Mediabunny
- [rules/get-video-duration.md](rules/get-video-duration.md) - Getting the duration of a video file in seconds with Mediabunny
- [rules/gifs.md](rules/gifs.md) - Displaying GIFs synchronized with Remotion's timeline
- [rules/images.md](rules/images.md) - Embedding images in Remotion using the Img component
- [rules/light-leaks.md](rules/light-leaks.md) - Light leak overlay effects using @remotion/light-leaks
- [rules/lottie.md](rules/lottie.md) - Embedding Lottie animations in Remotion
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Measuring DOM element dimensions in Remotion
- [rules/measuring-text.md](rules/measuring-text.md) - Measuring text dimensions, fitting text to containers, and checking overflow
- [rules/sequencing.md](rules/sequencing.md) - Sequencing patterns for Remotion - delay, trim, limit duration of items
- [rules/tailwind.md](rules/tailwind.md) - Using TailwindCSS in Remotion
- [rules/text-animations.md](rules/text-animations.md) - Typography and text animation patterns for Remotion
- [rules/timing.md](rules/timing.md) - Interpolation curves in Remotion - linear, easing, spring animations
- [rules/transitions.md](rules/transitions.md) - Scene transition patterns for Remotion
- [rules/transparent-videos.md](rules/transparent-videos.md) - Rendering out a video with transparency
- [rules/trimming.md](rules/trimming.md) - Trimming patterns for Remotion - cut the beginning or end of animations
- [rules/videos.md](rules/videos.md) - Embedding videos in Remotion - trimming, volume, speed, looping, pitch
- [rules/parameters.md](rules/parameters.md) - Make a video parametrizable by adding a Zod schema
- [rules/maps.md](rules/maps.md) - Add a map using Mapbox and animate it
- [rules/voiceover.md](rules/voiceover.md) - Adding AI-generated voiceover to Remotion compositions using ElevenLabs TTS

## Guardrails

**Source & Attribution**
- This skill contains best practices for **Remotion** (https://www.remotion.dev/), a React-based framework for programmatic video creation, developed by Remotion GmbH.
- Rule files in `rules/` are derived from Remotion official documentation and community best practices.
- Some rule files reference **Mediabunny** (https://mediabunny.com/) for media processing operations.
- FFmpeg operations require the FFmpeg open-source tool (https://ffmpeg.org/) installed on the system.
- Users must have Remotion installed in their project (`npm i remotion @remotion/cli`).

**Anti-patterns**
- NEVER bypass Remotion's rendering pipeline with direct DOM manipulation outside of components.
- Do NOT use `setTimeout` or `setInterval` for animations — use Remotion's `useCurrentFrame()` and `interpolate()`.
- NEVER hardcode frame numbers without considering FPS — always calculate based on `fps` prop.
- Do NOT load rule files that are not relevant to the user's task — only load on demand.

**Constraints**
- Always load the specific `rules/*.md` file relevant to the user's task before providing code examples.
- Verify Remotion version compatibility — some APIs may differ between major versions.
- For FFmpeg operations, confirm ffmpeg is installed (`ffmpeg -version`) before providing commands.
- For Mediabunny operations, confirm the user has access to the Mediabunny API.
- Never modify or delete rule files in the `rules/` directory.

## Related Skills

- **gh-cli** — GitHub CLI reference for managing Remotion project repositories, releases, and CI/CD workflows.
- **find-skills** — Discover additional agent skills for video creation, animation, and media processing.
- **bright-data** — Web data extraction, useful for gathering data to visualize in Remotion charts.

## About UniqueClub

Part of the UniqueClub toolkit. This skill curates third-party Remotion best practices within the UniqueClub skill ecosystem.
🌐 https://uniqueclub.ai
