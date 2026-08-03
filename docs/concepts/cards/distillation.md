# Distillation

**Purpose:** Reference card for **distillation** used across AIEBOK books and knowledge areas.

## Core explanation

Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed.

## Example

Student classifier matches teacher on 95% of eval at 5× lower latency.

## Evidence of understanding

Measure student versus teacher gap on full eval and acceptable degradation threshold.

## Trade-offs

No mechanism is universal. Compare distillation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
