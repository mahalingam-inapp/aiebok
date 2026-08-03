# Syntax

**Purpose:** Reference card for **syntax** used across AIEBOK books and knowledge areas.

## Core explanation

Syntax governs how words combine into grammatical structures—phrases, clauses, dependencies. Parsers and models exploit syntactic patterns but fluent text can violate syntax without humans noticing.

## Example

Dependency parsing links verbs to subjects, helping extract who did what in contract clauses.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare parser accuracy on ten hand-annotated sentences including passive voice and coordination.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare syntax against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ambiguity](../../concepts/cards/ambiguity.md)
- [Discourse](../../concepts/cards/discourse.md)
- [Pragmatics](../../concepts/cards/pragmatics.md)
- [Semantics](../../concepts/cards/semantics.md)

## Related chapters

- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
