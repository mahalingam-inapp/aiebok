# Ambiguity

**Purpose:** Reference card for **ambiguity** used across AIEBOK books and knowledge areas.

## Core explanation

Ambiguity arises when the same text supports multiple interpretations without disambiguating context. Production systems need clarification, abstention, or retrieval—not forced guesses.

## Example

'Reset my password' versus 'reset the server password' differ by scope; missing context causes wrong runbooks.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Collect ten ambiguous user queries and measure how often the system asks clarifying questions.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare ambiguity against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Discourse](../../concepts/cards/discourse.md)
- [Pragmatics](../../concepts/cards/pragmatics.md)
- [Semantics](../../concepts/cards/semantics.md)
- [Syntax](../../concepts/cards/syntax.md)

## Related chapters

- [01 Why Language Is Hard](../../books/03-language-and-representation/01-why-language-is-hard.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
