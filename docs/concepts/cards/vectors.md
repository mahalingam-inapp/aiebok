# Vectors

**Purpose:** Reference card for **vectors** used across AIEBOK books and knowledge areas.

## Core explanation

Vectors represent objects as numeric arrays so similarity, direction, and composition become computable. They underpin embeddings, attention, and most modern ML pipelines.

## Example

Representing users and items as vectors lets recommendation score candidates with a dot product in milliseconds.

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

Compute dot products for three pairs and verify ordering matches your semantic expectations.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare vectors against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Entropy](../../concepts/cards/entropy.md)
- [Gradient Descent](../../concepts/cards/gradient-descent.md)
- [Matrix Transformations](../../concepts/cards/matrix-transformations.md)
- [Probability](../../concepts/cards/probability.md)

## Related chapters

- [04 The Mathematics Engineers Need](../../books/01-foundations-of-intelligence/04-the-mathematics-engineers-need.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
