# Semantics

**Purpose:** Reference card for **semantics** used across AIEBOK books and knowledge areas.

## Core explanation

Semantics concerns meaning—entities, relations, entailment—not just form. Systems must map language to intended referents and propositions, especially under ambiguity.

## Example

'Bank' as financial institution versus river edge changes retrieval targets entirely.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Build ten minimal pairs differing by one word and verify the system assigns different meanings.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare semantics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ambiguity](../../concepts/cards/ambiguity.md)
- [Discourse](../../concepts/cards/discourse.md)
- [Pragmatics](../../concepts/cards/pragmatics.md)
- [Syntax](../../concepts/cards/syntax.md)

## Related chapters

- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
