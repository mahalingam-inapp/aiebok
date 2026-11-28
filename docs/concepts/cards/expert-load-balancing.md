# Expert Load Balancing

**Purpose:** Reference card for **expert load balancing** used across AIEBOK books and knowledge areas.

## Core explanation

Expert load balancing controls the concentration of assignments in a sparse layer. Training can influence the router through an auxiliary loss or score adjustments, while serving can change expert placement or replication.

## Example

A burst sends six assignments to an expert whose modeled capacity is four, leaving two unserved despite spare capacity elsewhere.

## When to use

Use when bursts or recurring request shapes concentrate assignments.

## When not to use

Equal assignment counts alone do not establish equal quality or execution cost.

## Engineering checklist

- Record rerouted and overflow assignments alongside the original choices.

## Evidence of understanding

Measure peak assignments, overflow and fallback quality on both balanced inputs and realistic bursts.

## Common failure modes

- Rerouting reduces overflow but sends tokens to experts that perform poorly on the task.

## Trade-offs

No mechanism is universal. Compare expert load balancing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/sparse-model-architectures/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
