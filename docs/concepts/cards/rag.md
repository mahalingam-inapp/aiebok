# Rag

**Purpose:** Reference card for **rag** used across AIEBOK books and knowledge areas.

## Core explanation

Retrieval-augmented generation retrieves external evidence at query time and conditions generation on it.

## Example

HR assistant retrieves current travel policy and refuses when no supporting document exists.

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

Evaluate retrieval recall and answer faithfulness separately before end-to-end judgment.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare rag against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Behavior Versus Knowledge](../../concepts/cards/behavior-versus-knowledge.md)
- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Model Selection](../../concepts/cards/model-selection.md)
- [Prompting](../../concepts/cards/prompting.md)

## Related chapters

- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
