# Pragmatics

**Purpose:** Reference card for **pragmatics** used across AIEBOK books and knowledge areas.

## Core explanation

Pragmatics interprets meaning in context—speaker intent, implicature, and shared knowledge. Models lack shared world state unless you supply it explicitly.

## Example

'Can you shut the door?' is a request, not a capability question—intent classification must capture this.

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

Evaluate intent classification on indirect requests versus literal questions in the same domain.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare pragmatics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ambiguity](../../concepts/cards/ambiguity.md)
- [Discourse](../../concepts/cards/discourse.md)
- [Semantics](../../concepts/cards/semantics.md)
- [Syntax](../../concepts/cards/syntax.md)

## Related chapters

- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
