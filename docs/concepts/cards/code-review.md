# Code Review

**Purpose:** Reference card for **code review** used across AIEBOK books and knowledge areas.

## Core explanation

Code review evaluates correctness, security, and maintainability of changes—including agent-written code. It remains accountability gate before merge.

## Example

Reviewer checks agent did not skip auth on new endpoint despite passing happy-path tests.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure post-merge incident rate for agent-authored versus human-authored merges.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare code review against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ai Coding Agents](../../concepts/cards/ai-coding-agents.md)
- [Context Files](../../concepts/cards/context-files.md)
- [Repo Instructions](../../concepts/cards/repo-instructions.md)
- [Skills](../../concepts/cards/skills.md)

## Related chapters

- [03 Ai Native Development Workflow](../../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
