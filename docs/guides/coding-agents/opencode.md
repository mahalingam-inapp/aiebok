# OpenCode implementation guide

Open the repository with `opencode`. Use the Plan agent to inspect the [shared change brief](index.md#first-change), then switch to Build for the agreed edits. For a scripted review, call the Plan agent directly.

```sh
opencode --help
opencode run --agent plan 'Review HarborLink policy guards and module selection. Return file:line evidence and proposed regression cases.'
```

## Instructions, commands, and skills

Put repository boundaries in `AGENTS.md`. Save the shared verification skill in `.opencode/skills/verify-harborlink/SKILL.md`. Ask OpenCode to load `verify-harborlink` for implementation verification. For a short review prompt, save `.opencode/commands/review-harborlink.md`.

```markdown
---
description: Review HarborLink against a narrow acceptance case
agent: plan
---

Review the HarborLink workbook. Focus on $ARGUMENTS.
Return file:line evidence and one regression case.
```

Run `/review-harborlink collapsed retrieval` in the interactive session. [CLI](https://opencode.ai/docs/cli/) · [Commands](https://opencode.ai/docs/commands/) · [Skills](https://opencode.ai/docs/skills/)

## Parallel reviewers

Add `.opencode/agents/fixture-reviewer.md`.

```markdown
---
description: Read-only policy and fallback reviewer
mode: subagent
permission:
  edit: deny
  bash: deny
---

Trace the requested behavior and report file:line, one regression case, and any uncertainty.
```

Ask Build to delegate two separate tasks to `@fixture-reviewer`, one about policy scope and one about disabled modules. Keep the reviewer’s permissions narrow and give the parent agent authority to integrate after you review its proposal. If project configuration restricts delegation, allow this named agent in the parent’s `task` permissions. [Agents](https://opencode.ai/docs/agents/) · [Permissions](https://opencode.ai/docs/permissions/)
