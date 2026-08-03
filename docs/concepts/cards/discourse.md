# Discourse

**Purpose:** Reference card for **discourse** used across AIEBOK books and knowledge areas.

## Core explanation

Discourse connects sentences across turns and documents—coreference, topic continuity, rhetorical structure. Long interactions fail when each turn is processed in isolation.

## Example

'It' in turn three refers to the outage mentioned in turn one only if discourse state is preserved.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run a coreference test set and report F1 on pronouns spanning three or more turns.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare discourse against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Ambiguity](../../concepts/cards/ambiguity.md)
- [Pragmatics](../../concepts/cards/pragmatics.md)
- [Semantics](../../concepts/cards/semantics.md)
- [Syntax](../../concepts/cards/syntax.md)

## Related chapters

- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
