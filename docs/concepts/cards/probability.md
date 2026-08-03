# Probability

**Purpose:** Reference card for **probability** used across AIEBOK books and knowledge areas.

## Core explanation

Probability quantifies uncertainty over outcomes, enabling expectations, risk calculations, and principled decisions under incomplete information. ML outputs are almost always distributions, not certainties.

## Example

A fraud scorer outputs P(fraud); finance uses that probability with loss asymmetries, not a raw boolean.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Convert three model scores to expected cost given asymmetric false-positive and false-negative penalties.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare probability against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Entropy](../../concepts/cards/entropy.md)
- [Gradient Descent](../../concepts/cards/gradient-descent.md)
- [Matrix Transformations](../../concepts/cards/matrix-transformations.md)
- [Vectors](../../concepts/cards/vectors.md)

## Related chapters

- [04 The Mathematics Engineers Need](../../books/01-foundations-of-intelligence/04-the-mathematics-engineers-need.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
