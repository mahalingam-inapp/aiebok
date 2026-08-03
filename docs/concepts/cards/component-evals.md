# Component Evals

**Purpose:** Reference card for **component evals** used across AIEBOK books and knowledge areas.

## Core explanation

Component evals test retrieval, generation, tools, and UX stages independently before end-to-end runs. They localize failures.

## Example

Retrieval recall@10 evaluated separately from answer faithfulness on same queries.

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

Build failure attribution matrix mapping end-to-end misses to component scores.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare component evals against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [End To End Evals](../../concepts/cards/end-to-end-evals.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)
- [Retrieval Metrics](../../concepts/cards/retrieval-metrics.md)
- [Tool Success](../../concepts/cards/tool-success.md)

## Related chapters

- [03 Evaluation By System Stage](../../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
