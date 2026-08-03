# Breadth First Search

**Purpose:** Reference card for **breadth first search** used across AIEBOK books and knowledge areas.

## Core explanation

Breadth-first search expands nodes level by level, guaranteeing shortest path in unweighted graphs. It is the baseline for optimal reachability before adding heuristics.

## Example

In a grid maze, BFS finds the minimum-step route from start to exit by exploring all distance-1 cells before distance-2.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run BFS on a fixed maze and verify path length equals the known shortest distance.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare breadth first search against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A](../../concepts/cards/a.md)
- [Heuristics](../../concepts/cards/heuristics.md)
- [Planning](../../concepts/cards/planning.md)
- [State Spaces](../../concepts/cards/state-spaces.md)

## Related chapters

- [03 Search Planning And Decisions](../../books/01-foundations-of-intelligence/03-search-planning-and-decisions.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
