# Retrieval

**Purpose:** Reference card for **retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Retrieval selects candidate evidence from a corpus given a query before ranking and generation. It is candidate generation under relevance and policy constraints—not the final answer.

## Example

Hybrid retrieval returns 20 chunks for reranking; generation never sees the full million-document index.

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

Report recall@20 on a labeled query set before tuning downstream prompts.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Grounding](../../concepts/cards/grounding.md)
- [Knowledge Freshness](../../concepts/cards/knowledge-freshness.md)
- [Structured Data](../../concepts/cards/structured-data.md)

## Related chapters

- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
