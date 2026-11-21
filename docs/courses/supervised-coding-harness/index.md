# Supervised Coding-Agent Harnesses

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build a reviewable harness around a proposed change and measure whether its checks catch regressions.

[Start the first lecture](01-write-an-acceptance-contract-for-a-change.md){ .md-button .md-button--primary .study-start data-course="supervised-coding-harness" }

## Practice case · Someone has to approve the formatter change

Tomas maintains a help-desk formatter that other teams depend on. He wants to accept small assistant-suggested changes while showing reviewers what changed, what was tested, and why a repeated request cannot apply twice.

This fictional case continues through the lectures.

For a documented comparison, read [Two studies measured two different coding jobs](../../casebook/coding-productivity.md).

## Entry prerequisites

Python and automated tests. Familiarity with specification-driven development and the agent loop is helpful.

## Course outline

### Specify and verify a candidate

- [01 · Write an acceptance contract for a change](01-write-an-acceptance-contract-for-a-change.md){ .study-lecture data-lecture="01-write-an-acceptance-contract-for-a-change.md" } — Turn a small change request into regression and acceptance examples.
- [02 · Constrain proposals and run checks](02-constrain-proposals-and-run-checks.md){ .study-lecture data-lecture="02-constrain-proposals-and-run-checks.md" } — Validate the shape and scope of a proposed change before running the acceptance suite.

### Approve and audit a change

- [03 · Approval, revisions and replay](03-approval-revisions-and-replay.md){ .study-lecture data-lecture="03-approval-revisions-and-replay.md" } — Bind an approval to the reviewed proposal and current revision.
- [04 · Compare workflow traces and handoffs](04-compare-workflow-traces-and-handoffs.md){ .study-lecture data-lecture="04-compare-workflow-traces-and-handoffs.md" } — Use a fixed suite to compare proposals and design a human handoff with useful evidence.

## Workbook

[Download the workbook](../../assets/notebooks/supervised-coding-harness.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Demonstrate a supervised change to a deterministic formatter. Preserve its spec, structured proposal, regression report, approval decision, and replay record.

**How to check your project**

Show that a wrong proposal fails before approval, an otherwise valid proposal waits, and a repeated approved request does not apply twice. Explain how your checks and review would transfer to a coding-agent framework.

## Further study

- [Reasoning and Tool Use, including MCP](../../books/07-reasoning-and-tool-use/index.md)
- [Agent Systems](../../books/08-agent-systems/index.md)
- [Framework examples from Donner’s Agents repository](https://github.com/ed-donner/agents)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
