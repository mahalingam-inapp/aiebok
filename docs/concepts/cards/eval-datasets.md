# Eval Datasets

**Purpose:** Reference card for **eval datasets** used across AIEBOK books and knowledge areas.

## Core explanation

Eval datasets are labeled or rubric-scored cases representing production risks and happy paths. They must refresh as products and policies evolve.

## Example

200 support queries with gold answers updated quarterly after product launches.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Version eval dataset with changelog and rerun full suite monthly.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare eval datasets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Adversarial Tests](../../concepts/cards/adversarial-tests.md)
- [Contract Tests](../../concepts/cards/contract-tests.md)
- [Release Gates](../../concepts/cards/release-gates.md)
- [Unit Tests](../../concepts/cards/unit-tests.md)

## Related chapters

- [04 Testing Ai Systems](../../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
