# Repo Instructions

**Purpose:** Reference card for **repo instructions** used across AIEBOK books and knowledge areas.

## Core explanation

Repo instructions—AGENTS.md, CONTRIBUTING—orient coding agents to build, test, and review conventions. They reduce wrong-file edits and skipped tests.

## Example

Instructions specify pytest command, lint rules, and forbidden directories.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run agent on sample task and measure review comments tied to instruction violations.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare repo instructions against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Coding Agents](../../concepts/cards/ai-coding-agents.md)
- [Code Review](../../concepts/cards/code-review.md)
- [Context Files](../../concepts/cards/context-files.md)
- [Skills](../../concepts/cards/skills.md)

## Related chapters

- [03 Ai Native Development Workflow](../../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
