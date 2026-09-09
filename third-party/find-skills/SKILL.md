---
name: find-skills
description: |
  Discover and install agent skills from the open agent skills ecosystem using the Skills CLI (`npx skills`).
  Helps users find functionality that might exist as an installable skill for specialized domains, workflows, and tools.
  Use when: "找个skill", "find a skill", "有没有技能", "install skill", "搜索技能", "npx skills", "skill discovery", "扩展agent能力", "找工具", "skill marketplace".
  Searches skills.sh ecosystem, presents options, and can install skills globally with confirmation.
  Cross-references: gh-cli, skill-optimizer.
  Built by UniqueClub 🌐 https://uniqueclub.ai
version: "1.0.0"
---

# Find Skills

This skill helps you discover and install skills from the open agent skills ecosystem.

## When to Use

Use this skill when:
- The user asks "how do I do X" where X might be a common task with an existing skill
- The user says "find a skill for X" or "is there a skill for X"
- The user asks "can you do X" where X is a specialized capability
- The user expresses interest in extending agent capabilities
- The user wants to search for tools, templates, or workflows
- The user mentions they wish they had help with a specific domain (design, testing, deployment, etc.)

Do NOT use this skill if:
- The user wants to optimize an existing skill's description → use `skill-optimizer` instead
- The user wants GitHub operations → use `gh-cli` instead
- The capability is already available as a built-in tool or installed skill
- The user is asking for general knowledge that doesn't require a specialized skill

Typical triggers:
- 「找个skill」「有没有技能能做X」「搜索技能」
- "find a skill for X" "install skill" "npx skills"
- 「扩展agent能力」「skill marketplace」「找工具」

## Workflow

1. **探查 (Probe)**
理解用户需求，识别领域（如 React、testing、design、deployment）和具体任务，判断是否可能存在对应技能。

2. **约束 (Constrain)**
设定搜索边界：使用具体关键词而非泛词；若首次搜索无果，尝试替代术语。安装技能前必须获得用户确认，不自动安装。

3. **证据 (Evidence)**
搜索结果来自 `npx skills find` 命令的实时返回和 skills.sh 目录。每个推荐的技能必须有名称、功能描述、安装命令和来源链接，不编造不存在的技能。

4. **执行 (Execute)**
Run the find command with a relevant query:

```bash
npx skills find [query]
```

For example:
- User asks "how do I make my React app faster?" → `npx skills find react performance`
- User asks "can you help me with PR reviews?" → `npx skills find pr review`
- User asks "I need to create a changelog" → `npx skills find changelog`

The command will return results like:

```
Install with npx skills add <owner/repo@skill>

vercel-labs/agent-skills@vercel-react-best-practices
└ https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices
```

Present options to the user with: skill name, what it does, install command, and a link to learn more at skills.sh.

5. **验证 (Verify)**
验证推荐的技能确实存在于 skills.sh 目录，安装命令格式正确（`owner/repo@skill`）。若用户选择安装，验证安装成功且技能可被发现。

6. **交付 (Deliver)**
If the user wants to proceed, install the skill:

```bash
npx skills add <owner/repo@skill> -g -y
```

The `-g` flag installs globally (user-level) and `-y` skips confirmation prompts.

If no relevant skills exist: acknowledge that no existing skill was found, offer to help with the task directly using general capabilities, and suggest the user could create their own skill with `npx skills init`.

## Output

A list of recommended skills with: skill name (`owner/repo@skill` format), one-line description, install command (`npx skills add ...`), and skills.sh link. If the user proceeds, the skill is installed globally and confirmation is returned. If no skills are found, a clear message is returned with alternative suggestions.

## What is the Skills CLI?

The Skills CLI (`npx skills`) is the package manager for the open agent skills ecosystem. Skills are modular packages that extend agent capabilities with specialized knowledge, workflows, and tools.

**Key commands:**

- `npx skills find [query]` - Search for skills interactively or by keyword
- `npx skills add <package>` - Install a skill from GitHub or other sources
- `npx skills check` - Check for skill updates
- `npx skills update` - Update all installed skills

**Browse skills at:** https://skills.sh/

## Common Skill Categories

When searching, consider these common categories:

| Category        | Example Queries                          |
| --------------- | ---------------------------------------- |
| Web Development | react, nextjs, typescript, css, tailwind |
| Testing         | testing, jest, playwright, e2e           |
| DevOps          | deploy, docker, kubernetes, ci-cd        |
| Documentation   | docs, readme, changelog, api-docs        |
| Code Quality    | review, lint, refactor, best-practices   |
| Design          | ui, ux, design-system, accessibility     |
| Productivity    | workflow, automation, git                |

## Tips for Effective Searches

1. **Use specific keywords**: "react testing" is better than just "testing"
2. **Try alternative terms**: If "deploy" doesn't work, try "deployment" or "ci-cd"
3. **Check popular sources**: Many skills come from `vercel-labs/agent-skills` or `ComposioHQ/awesome-claude-skills`

## Guardrails

**Source & Attribution**
- This skill uses the **Skills CLI** (`npx skills`) and the **skills.sh** directory (https://skills.sh/), an open ecosystem for agent skills.
- Skills are installed from GitHub repositories and other sources specified by the Skills CLI.
- No skills are bundled or endorsed by UniqueClub — users install third-party skills at their own discretion.

**Anti-patterns**
- NEVER install a skill without explicit user confirmation — always present options first.
- Do NOT fabricate or recommend skills that don't exist in the skills.sh directory.
- NEVER run `npx skills add` with untrusted sources without warning the user about third-party code.
- Do NOT use this skill to optimize or audit existing skills — use `skill-optimizer` instead.

**Constraints**
- Always use specific search keywords; avoid overly broad queries.
- If no skills are found, offer to help directly rather than forcing a skill installation.
- Verify install commands are in `owner/repo@skill` format before executing.
- Clean up any temporary files created during the search/install process.

## Related Skills

- **skill-optimizer** — Audit and optimize installed SKILL.md files for discoverability and routing accuracy.
- **gh-cli** — GitHub CLI reference for repository operations, useful when skills are hosted on GitHub.
- **bright-data** — Web data extraction skill, an example of a specialized capability that might be found via this skill.

## About UniqueClub

Part of the UniqueClub toolkit. This skill helps users discover third-party skills within the open agent skills ecosystem.
🌐 https://uniqueclub.ai
