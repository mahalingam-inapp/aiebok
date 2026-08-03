# Ablations

**Purpose:** Reference card for **ablations** used across AIEBOK books and knowledge areas.

## Core explanation

Ablations remove components to measure contribution—essential for judging which mechanism drives reported gains.

## Example

Paper claims graph RAG helps; ablation removing graph should show drop if claim holds.

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

Require ablation table or run own component removal on reproduction attempt.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare ablations against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Benchmarks](../../concepts/cards/benchmarks.md)
- [Primary Sources](../../concepts/cards/primary-sources.md)
- [Reproduction](../../concepts/cards/reproduction.md)
- [Technology Forecasting](../../concepts/cards/technology-forecasting.md)

## Related chapters

- [06 How To Track The Frontier](../../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
