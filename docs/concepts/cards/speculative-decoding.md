# Speculative Decoding

**Purpose:** Reference card for **speculative decoding** used across AIEBOK books and knowledge areas.

## Core explanation

Speculative decoding proposes continuation tokens and verifies them in a block with a target model. A greedy implementation can commit a matching prefix and correct the first mismatch, while stochastic equivalence requires the appropriate acceptance and correction distributions.

## Example

If the third of four draft tokens differs, a greedy check commits two matching tokens and the target token at the third position.

## When to use

Use when a cheap draft tends to predict several tokens the target can accept.

## When not to use

Skip when low acceptance or saturated target batches erase gains.

## Engineering checklist

- Compare with target-only decoding on the same prompts and settings.

## Evidence of understanding

Measure accepted tokens per check, end-to-end latency, throughput and target decode equivalence on a fixed workload.

## Common failure modes

- An incorrect sampling correction changes the target distribution.

## Trade-offs

No mechanism is universal. Compare speculative decoding against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/reasoning-efficient-inference/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
