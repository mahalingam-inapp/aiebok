# Decision Transformer

**Purpose:** Reference card for **decision transformer** used across AIEBOK books and knowledge areas.

## Core explanation

Decision Transformer formulates offline reinforcement learning as sequence prediction over returns-to-go, states and actions. An action is conditioned on observed history and a desired return, with no guarantee for desired behavior outside the data distribution.

## Example

A trajectory model trained on cautious scheduling data receives a desired return rarely reached in that data.

## When to use

Use to study return-conditioned policies when trajectory data cover relevant states and actions.

## When not to use

Avoid relying on unreachable target returns or unsupported actions.

## Engineering checklist

- Compare with behavior cloning and a simple planner on the same evaluation environments.

## Evidence of understanding

Evaluate against simple policies on held-out trajectories or a validated simulator, and measure failures under changes in state and action support.

## Common failure modes

- Target returns outside the training range produce unreliable actions.

## Trade-offs

No mechanism is universal. Compare decision transformer against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/decision-models-and-policies/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
