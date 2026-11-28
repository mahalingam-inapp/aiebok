# Contextual Bandits

**Purpose:** Reference card for **contextual bandits** used across AIEBOK books and knowledge areas.

## Core explanation

A contextual bandit chooses an action given observed context and receives feedback for the chosen action. The action can affect which outcome is observed, so the same log lacks counterfactual rewards for the other actions.

## Example

A synthetic queue chooses one of two reminder policies per ticket and records the eligible options, action, probability and outcome.

## When to use

Use for repeated one-step choices with observable feedback.

## When not to use

Use a sequential model when choices materially change future states and rewards.

## Engineering checklist

- Log the eligible actions, selected action, propensity and outcome.

## Evidence of understanding

Check action support, selection probabilities, feedback delay and evaluation uncertainty before comparing policies.

## Common failure modes

- Selection probabilities are missing or detached from the policy version.

## Trade-offs

No mechanism is universal. Compare contextual bandits against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/decision-models-and-policies/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
