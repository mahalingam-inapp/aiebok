# Heuristics

**Purpose:** Reference card for **heuristics** used across AIEBOK books and knowledge areas.

## Core explanation

Heuristics estimate remaining cost or promise of partial solutions to guide search toward promising branches. Good heuristics cut compute; bad ones waste it or break optimality guarantees.

## Example

Manhattan distance guides grid navigation; an overestimated heuristic can make A* suboptimal or incomplete.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure nodes expanded with and without the heuristic on ten random maps and report the speedup ratio.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare heuristics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A](../../concepts/cards/a.md)
- [Backtracking](../../concepts/cards/backtracking.md)
- [Breadth First Search](../../concepts/cards/breadth-first-search.md)
- [Decomposition](../../concepts/cards/decomposition.md)

## Related chapters

- [03 Search Planning And Decisions](../../books/01-foundations-of-intelligence/03-search-planning-and-decisions.md)
- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
