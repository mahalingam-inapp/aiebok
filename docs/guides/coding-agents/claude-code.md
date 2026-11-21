# Claude Code implementation guide

Open the repository with `claude`. Use Plan mode for the [shared change brief](index.md#first-change) and approve the scope before implementation. For a non-interactive review, request Plan mode explicitly.

```sh
claude --help
claude -p --permission-mode plan 'Review HarborLink policy guards and module selection. Return file:line evidence and proposed regression cases.'
```

## Instructions and short commands

Put persistent guidance in `CLAUDE.md`. Save the shared skill as `.claude/skills/verify-harborlink/SKILL.md` and invoke `/verify-harborlink`. A skill can include `disable-model-invocation: true` when you want to initiate the procedure explicitly. [CLI](https://code.claude.com/docs/en/cli-reference) · [Skills](https://code.claude.com/docs/en/skills)

## Parallel reviewers and agent teams

Save `.claude/agents/fixture-reviewer.md`.

```markdown
---
name: fixture-reviewer
description: Read-only review of evidence, permissions, and fallback behavior.
tools: Read, Glob, Grep
permissionMode: plan
---

Return file:line evidence, one regression case, and any uncertainty.
```

Ask Claude to run two independent fixture-reviewer tasks and wait for both results. Have the parent summarize disagreements and propose the smallest patch. Re-run the fixed check after the implementation and inspect the diff.

For workstreams that need to communicate during parallel work, Claude Code also offers experimental agent teams. Enable them with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`, assign each teammate an independent scope, and let the lead integrate. Keep the shared test and final review with the lead. [Subagents](https://code.claude.com/docs/en/sub-agents) · [Agent teams](https://code.claude.com/docs/en/agent-teams)
