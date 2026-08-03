# A

**Purpose:** Reference card for **a** used across AIEBOK books and knowledge areas.

## Core explanation

A* expands the lowest estimated total-cost node first, combining path cost g(n) with heuristic h(n) toward the goal. With an admissible heuristic it finds optimal paths while often expanding fewer nodes than BFS.

## Example

In a grid maze, A* with Manhattan distance typically expands fewer cells than BFS while returning the same shortest path.

## Evidence of understanding

Compare expanded node counts for BFS and A* on identical inputs and verify equal path cost.

## Trade-offs

No mechanism is universal. Compare a against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
