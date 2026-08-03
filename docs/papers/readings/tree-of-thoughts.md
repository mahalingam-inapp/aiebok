# Tree of Thoughts: Deliberate Problem Solving with LLMs

## Citation

Yao et al.. *Tree of Thoughts: Deliberate Problem Solving with LLMs.* 2023. [https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)

## One-sentence contribution

Search over intermediate reasoning states improves hard tasks.

## Problem

Chain-of-thought follows a single reasoning path—no backtracking, exploration, or comparison of alternatives. Hard problems (puzzles, planning, creative writing) require deliberate search over multiple intermediate states.

## Prior art

CoT elicited single-path reasoning. Beam search operated over tokens, not semantic states. Classical search (BFS, DFS, A*) required formal state representations incompatible with free-form LM generation.

## Core idea

Yao et al. treat each intermediate reasoning step as a 'thought' node in a search tree. At each node, the LM generates candidate next thoughts. A evaluation function (LM self-evaluation or heuristic) scores each candidate. Search algorithms (BFS or DFS) explore the tree, pruning low-scoring branches. Backtracking occurs when all children of a node score poorly. This generalizes CoT from a single chain to a deliberate search process with LM-generated states and LM-generated evaluations.

## Evidence

- Game of 24: ToT solved 74% vs. CoT 4% (GPT-4)—dramatic improvement on search-heavy task.
- Creative writing (coherent paragraph planning): ToT improved coherence scores in human eval.
- Mini crosswords: ToT with BFS outperformed greedy CoT on word fill rate.
- Self-evaluation as heuristic correlated with actual success on Game of 24.

## Limitations

- Token cost 5–20× higher than single CoT—each node requires generation + evaluation.
- Self-evaluation is unreliable for many tasks—external verifiers needed when available.
- Search hyperparameters (breadth, depth, branching factor) are task-specific.
- No general framework—each task requires designing thought decomposition and evaluation.

## Lasting impact

ToT established test-time compute scaling via search as a research direction, influencing o1-style reasoning models and best-of-N sampling strategies. It formalized the idea that inference-time search can substitute for model scale.

## Reproduction exercise

Implement BFS-ToT on Game of 24 with 10 puzzles using GPT-4o-mini. Use 3-step thoughts (partial equations) with LM self-evaluation. Compare solve rate against standard CoT. Log total tokens used per puzzle.

## Related chapters

- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)
- [02 Planning](../../books/07-reasoning-and-tool-use/02-planning.md)
- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related concepts

- [Backtracking](../../concepts/cards/backtracking.md)
- [Test Time Compute](../../concepts/cards/test-time-compute.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
