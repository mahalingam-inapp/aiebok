# Cursor implementation guide

Open the repository in Cursor. Start in Plan mode in the Agent panel. Ask it to trace the [shared change brief](index.md#first-change), then let one agent implement the agreed patch. For a terminal review, use the CLI’s print mode.

```sh
agent --help
agent -p 'Review HarborLink policy guards and module selection. Return file:line evidence and proposed regression cases.'
```

## Rules, commands, and skills

Save persistent workspace guidance in `.cursor/rules/harborlink.mdc` with frontmatter `description: HarborLink implementation and test boundaries` and `alwaysApply: true`. Put this prompt in `.cursor/commands/review-harborlink.md` and select `/review-harborlink` in the editor.

> Review the workbook against the fixed cases. Report the first difference in policy scope, effective date, fallback, or approval. Include a file and line and a proposed regression case.

Save the standard verification procedure separately as `.cursor/skills/verify-harborlink/SKILL.md`. Select the skill in Agent chat when ready to run the checks.

[Rules](https://cursor.com/help/customization/rules) · [Custom commands](https://cursor.com/changelog/1-6) · [Skills](https://cursor.com/docs/skills) · [CLI](https://cursor.com/docs/cli/using)

## Parallel reviewers

Save `.cursor/agents/fixture-reviewer.md`.

```markdown
---
name: fixture-reviewer
description: Reviews policy evidence, access, effective dates, and fallback behavior.
readonly: true
---

Report file and line evidence, one regression case, and any uncertainty.
```

Ask the editor Agent to delegate the policy and execution reviews as separate read-only subagent tasks. Compare the returned findings, review the proposed files, then assign one writer. Review the resulting diff in the editor and run the check from the terminal. Configure actual CLI file and shell access through Cursor’s permissions when automating a review. [Subagents](https://cursor.com/docs/subagents) · [CLI permissions](https://cursor.com/docs/cli/reference/permissions)
