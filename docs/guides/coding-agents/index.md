# Implement AIeBOK projects with coding agents

Use the same change brief, tests, and review across four tools. Start with HarborLink, a local help desk, or apply the workflow to the lead-screening harness in the [Undercover case study](../undercover-harness.md).

| Tool | Start here | Project customization |
| --- | --- | --- |
| [Codex](codex.md) | `codex` or `codex exec` | `AGENTS.md`, `.agents/skills/`, `.codex/agents/` |
| [Cursor](cursor.md) | Agent panel or `agent -p` | `.cursor/rules/`, `.cursor/commands/`, `.cursor/skills/`, `.cursor/agents/` |
| [OpenCode](opencode.md) | `opencode` or `opencode run` | `AGENTS.md`, `.opencode/commands/`, `.opencode/skills/`, `.opencode/agents/` |
| [Claude Code](claude-code.md) | `claude` or `claude -p` | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/` |

## First change

From the AIeBOK repository root, establish the baseline. Python 3 and Node.js are enough for HarborLink.

```sh
python scripts/generate_interactive_workbook.py
node scripts/check_interactive_workbook.js
git diff --check
```

Give your agent this brief. Pick the same brief when evaluating multiple tools.

> Add one fixed case for a public query about ledger reconciliation before the first policy effective date. The response must be a handoff with no citations with every optional HarborLink module closed or open. Own only the workbook check unless the test exposes a defect. Run the baseline and changed checks. Report the diff and test output for review.

The code lives in `scripts/interactive_workbook/`, and the regression suite is `scripts/check_interactive_workbook.js`. Edit source and regenerate the bundled HTML when the runtime changes. For a site change, install the repository dependencies and run `python scripts/validate_content.py` and `mkdocs build --strict`.

## Give each instruction a home

Use repository instructions for persistent boundaries, a short command for a frequently repeated prompt, and a skill for a named procedure with inputs, steps, and expected outputs. Save this as `SKILL.md` in the project folder listed on the tool page.

```markdown
---
name: verify-harborlink
description: Verify HarborLink after changes to workbook code, policy evidence, or module selection.
---

1. Run `python scripts/generate_interactive_workbook.py`.
2. Run `node scripts/check_interactive_workbook.js` and `git diff --check`.
3. Report the command, outcome, first failure, and whether baseline behavior changed.
4. Keep the source diff and regenerated output available for human review.
```

## Turn a design into a reviewable change

| Change | Implementation assignment | Review evidence |
| --- | --- | --- |
| Retrieval, context, or multimodal evidence | Add a dated source fixture with origin and audience. Keep the context and citation contracts stable. | Test no evidence, stale evidence, restricted evidence, and a synonym. |
| Model adaptation, inference, or serving | Keep the baseline runnable. Put model changes behind an adapter with fixed cases and revise the cache key when artifacts change. | Report quality and resource measurements separately. Use paired cases and record the artifact version. |
| Agent workflow, skills, or tools | Specify tool input, write scope, step budget, and a proposal/approval boundary. Use a local fixture adapter first. | Test malformed input, a repeated request, a timeout, and missing approval. |
| Evals, release, or governance | Freeze examples before tuning. Record who owns a hold decision and how to restore the previous version. | Report slice counts, critical failures, and rollback evidence. |
| Product, operations, or rollout | Define the baseline and what changes for the person waiting for an answer. Name a manual intake owner. | Let a reviewer reproduce the answer, fallback, and decision from a small packet. |

## Coordinate agents without overlapping writes

Start with two read-only assignments in parallel. Ask one reviewer to trace date and audience checks and the other to trace module selection and fallback. Each returns `file:line`, observed behavior, a regression case, and an open question. The coordinator resolves disagreements against the fixture contract. Give one implementer the agreed scope, then run the checks in the main checkout and review before committing.

For genuinely independent implementations, assign disjoint files on separate Git worktrees. Give both workers the same commit and contract. Integrate one diff at a time and rerun checks after integration. Keep hosted tools and writable MCP servers outside the local verification task unless the change has an explicit dependency on them.

[Spec-driven workflow](../../getting-started/spec-driven-workflow.md) · [HarborLink workbook](../../labs/interactive-workbook.md)
