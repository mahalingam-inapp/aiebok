# Autoscaling

**Purpose:** Reference card for **autoscaling** used across AIEBOK books and knowledge areas.

## Core explanation

Autoscaling adjusts inference replica count based on CPU, GPU utilization, or queue depth.

## Example

Scale GPU pods from 2 to 10 when p95 queue wait exceeds 500ms.

## Evidence of understanding

Load spike test verifies scale-up within target minutes without error burst.

## Trade-offs

No mechanism is universal. Compare autoscaling against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
