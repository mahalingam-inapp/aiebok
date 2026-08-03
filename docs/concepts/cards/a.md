# A

**Purpose:** Reference card for **a** used across AIEBOK books and knowledge areas.

## Core explanation

A* expands the lowest estimated total-cost node first, combining path cost g(n) with heuristic h(n) toward the goal. With an admissible heuristic it finds optimal paths while often expanding fewer nodes than BFS.

## Example

In a grid maze, A* with Manhattan distance typically expands fewer cells than BFS while returning the same shortest path.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare expanded node counts for BFS and A* on identical inputs and verify equal path cost.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare a against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Breadth First Search](../../concepts/cards/breadth-first-search.md)
- [Heuristics](../../concepts/cards/heuristics.md)
- [Planning](../../concepts/cards/planning.md)
- [State Spaces](../../concepts/cards/state-spaces.md)

## Related chapters

- [03 Search Planning And Decisions](../../books/01-foundations-of-intelligence/03-search-planning-and-decisions.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
