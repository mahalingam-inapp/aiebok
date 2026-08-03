# Context Files

**Purpose:** Reference card for **context files** used across AIEBOK books and knowledge areas.

## Core explanation

Context files—.cursorrules, architecture docs—supply persistent project knowledge to coding agents. Stale context misleads worse than no context.

## Example

Architecture.md describes service boundaries so agent edits correct package.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Update context file when ADR changes and note version in agent traces.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare context files against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Coding Agents](../../concepts/cards/ai-coding-agents.md)
- [Code Review](../../concepts/cards/code-review.md)
- [Repo Instructions](../../concepts/cards/repo-instructions.md)
- [Skills](../../concepts/cards/skills.md)

## Related chapters

- [03 Ai Native Development Workflow](../../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
