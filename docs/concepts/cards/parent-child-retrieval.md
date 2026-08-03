# Parent Child Retrieval

**Purpose:** Reference card for **parent child retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Parent–child retrieval indexes small child chunks for precision but returns parent sections for generation context.

## Example

A child bullet may lack the section title needed for a correct answer unless parent is joined.

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

Demonstrate failure with child-only context and fix by returning parent at generation time.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare parent child retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [Dense Retrieval](../../concepts/cards/dense-retrieval.md)
- [Hybrid Search](../../concepts/cards/hybrid-search.md)
- [Query Rewriting](../../concepts/cards/query-rewriting.md)

## Related chapters

- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
