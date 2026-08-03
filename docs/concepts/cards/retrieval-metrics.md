# Retrieval Metrics

**Purpose:** Reference card for **retrieval metrics** used across AIEBOK books and knowledge areas.

## Core explanation

Retrieval metrics—recall@k, MRR, nDCG—measure candidate set quality before generation sees it.

## Example

High recall@20 with poor faithfulness suggests generation issue, not retrieval.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Report recall@5, @10, @20 on fixed query set each index version.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare retrieval metrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Component Evals](../../concepts/cards/component-evals.md)
- [End To End Evals](../../concepts/cards/end-to-end-evals.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)
- [Tool Success](../../concepts/cards/tool-success.md)

## Related chapters

- [03 Evaluation By System Stage](../../books/10-evaluation-safety-and-governance/03-evaluation-by-system-stage.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
