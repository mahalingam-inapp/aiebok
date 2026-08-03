# Benchmarks

**Purpose:** Reference card for **benchmarks** used across AIEBOK books and knowledge areas.

## Core explanation

Benchmarks standardize task comparisons—MMLU, HumanEval, BEIR—but may not reflect your production distribution.

## Example

High MMLU does not guarantee payroll policy QA performance.

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

Reproduce one benchmark subset plus in-domain eval before vendor selection.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare benchmarks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ablations](../../concepts/cards/ablations.md)
- [Primary Sources](../../concepts/cards/primary-sources.md)
- [Reproduction](../../concepts/cards/reproduction.md)
- [Technology Forecasting](../../concepts/cards/technology-forecasting.md)

## Related chapters

- [06 How To Track The Frontier](../../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
