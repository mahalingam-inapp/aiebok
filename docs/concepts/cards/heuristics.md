# Heuristics

**Purpose:** Reference card for **heuristics** used across AIEBOK books and knowledge areas.

## Core explanation

Heuristics estimate remaining cost or promise of partial solutions to guide search toward promising branches. Good heuristics cut compute; bad ones waste it or break optimality guarantees.

## Example

Manhattan distance guides grid navigation; an overestimated heuristic can make A* suboptimal or incomplete.

## Evidence of understanding

Measure nodes expanded with and without the heuristic on ten random maps and report the speedup ratio.

## Trade-offs

No mechanism is universal. Compare heuristics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
