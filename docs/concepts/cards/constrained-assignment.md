# Constrained Assignment

**Purpose:** Reference card for **constrained assignment** used across AIEBOK books and knowledge areas.

## Core explanation

Constrained assignment optimizes a set of choices together under resource, eligibility or precedence rules. Feasibility and objective value are separate results.

## Example

Two short maintenance jobs can fit together and beat the highest-value single task.

## When to use

Use when individually promising actions compete for shared capacity or violate combination rules.

## When not to use

Use simple ranking when actions are independent and share no relevant constraints.

## Engineering checklist

- Check feasibility and objective value against a tiny exact reference.

## Evidence of understanding

Compare feasibility, regret against a small exact solver, and solve time. Report infeasibility as its own outcome.

## Common failure modes

- A greedy choice consumes capacity needed by a higher-value combination.

## Trade-offs

No mechanism is universal. Compare constrained assignment against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/decision-models-and-policies/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
