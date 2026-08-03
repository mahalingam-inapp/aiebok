# Evaluation Specs

**Purpose:** Reference card for **evaluation specs** used across AIEBOK books and knowledge areas.

## Core explanation

Evaluation specs define datasets, metrics, slices, and release thresholds before shipping. They turn 'good enough' into numbers.

## Example

Eval spec: 200 cases, faithfulness ≥ 0.9, P0 safety cases 100% pass.

## When to use

Use before every release, model swap, prompt change, or retrieval index migration.

## When not to use

Skip aggregate-only metrics when slices or safety cases can hide regressions.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Block merge if eval spec checklist incomplete in release ticket.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare evaluation specs against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Acceptance Criteria](../../concepts/cards/acceptance-criteria.md)
- [Functional Specifications](../../concepts/cards/functional-specifications.md)
- [Prompt Specs](../../concepts/cards/prompt-specs.md)
- [Tool Contracts](../../concepts/cards/tool-contracts.md)

## Related chapters

- [02 Specification Driven Development](../../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
