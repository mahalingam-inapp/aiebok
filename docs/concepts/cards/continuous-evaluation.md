# Continuous Evaluation

**Purpose:** Reference card for **continuous evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Continuous evaluation runs production or shadow traffic against eval suites to detect drift post-release.

## Example

Nightly job scores 500 sampled prod queries with LLM judge against rubric.

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

Alert when rolling 7-day faithfulness drops below threshold versus launch baseline.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare continuous evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Canaries](../../concepts/cards/canaries.md)
- [Finops](../../concepts/cards/finops.md)
- [Tracing](../../concepts/cards/tracing.md)
- [Versioning](../../concepts/cards/versioning.md)

## Related chapters

- [06 Llmops](../../books/11-training-serving-and-ai-operations/06-llmops.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
