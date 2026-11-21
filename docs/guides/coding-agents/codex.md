# Codex implementation guide

Run Codex from the repository root. Use interactive mode to agree on a plan and implement the [shared change brief](index.md#first-change). Use `exec` to capture a repeatable review.

```sh
codex --help
codex
codex exec --sandbox read-only 'Review HarborLink policy guards and module selection. Return file:line evidence and proposed regression cases.'
```

## Instructions and short commands

Keep scope, build commands, and the review contract in `AGENTS.md`. Save the shared skill as `.agents/skills/verify-harborlink/SKILL.md` and enter `$verify-harborlink` in the session. Use `/plan` to discuss a larger change before asking for edits. New reusable procedures fit in skills. [Repository instructions](https://developers.openai.com/codex/guides/agents-md) · [Skills](https://developers.openai.com/codex/skills) · [CLI slash commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

## Parallel reviewers

Save this as `.codex/agents/fixture-reviewer.toml`. Set a narrow task each time the orchestrator delegates it.

```toml
name = "fixture_reviewer"
description = "Read-only review of policy fixtures and workbook behavior"
sandbox_mode = "read-only"
developer_instructions = "Return file:line evidence, one concrete regression case, and any uncertainty."
```

> Spawn two fixture reviewers. Have one trace effective dates and source scopes. Have the other trace disabled modules, missing evidence, and outage handoff. Wait for both reports and reconcile them against the fixed cases. Present the patch plan for review.

After the plan is accepted, use a workspace-write session for a scoped implementation and run the skill. Use `git diff` and the deterministic check for the final review. [Codex subagents](https://developers.openai.com/codex/subagents)
