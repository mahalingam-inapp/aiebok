# Faithfulness

**Purpose:** Reference card for **faithfulness** used across AIEBOK books and knowledge areas.

## Core explanation

Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions. It is separate from fluency or user satisfaction.

## Example

Correct tone but wrong deductible amount is unfaithful despite readable prose.

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

Use NLI or human rubric on 100 answers; require faithfulness ≥ threshold for release.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare faithfulness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Abstention](../../concepts/cards/abstention.md)
- [Answer Validation](../../concepts/cards/answer-validation.md)
- [Citation Precision](../../concepts/cards/citation-precision.md)
- [Component Evals](../../concepts/cards/component-evals.md)

## Related chapters

- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)
- [03 Evaluation By System Stage](../../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
