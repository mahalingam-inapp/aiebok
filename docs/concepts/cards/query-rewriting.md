# Query Rewriting

**Purpose:** Reference card for **query rewriting** used across AIEBOK books and knowledge areas.

## Core explanation

Query rewriting transforms requests via expansion, decomposition, or HyDE before retrieval to close vocabulary gaps.

## Example

Expanding 'PTO' to 'paid time off' helps lexical retrievers match handbook language.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare recall@k with and without rewrite on acronym-heavy queries.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare query rewriting against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [Dense Retrieval](../../concepts/cards/dense-retrieval.md)
- [Hybrid Search](../../concepts/cards/hybrid-search.md)
- [Parent Child Retrieval](../../concepts/cards/parent-child-retrieval.md)

## Related chapters

- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
