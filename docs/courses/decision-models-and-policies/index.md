# Decision Models, Optimization, and Feedback

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Turn predictions into constrained decisions, evaluate a contextual policy offline, and measure consequences before rollout.

[Start the first lecture](01-calibrated-predictions-and-decisions-under-cost.md){ .md-button .md-button--primary .study-start data-course="decision-models-and-policies" }

## Practice case · Who gets the next maintenance slot?

HarborLink has a queue and a finite number of technician slots. Leena owns the decision policy. She needs to translate delay-risk estimates into a plan and explain why some tickets are deferred for review.

This fictional case continues through the lectures.

## Entry prerequisites

Basic probability and statistics, Python, and a working understanding of supervised evaluation.

## Course outline

### Design the decision layer

- [01 · Calibrated predictions and decisions under cost](01-calibrated-predictions-and-decisions-under-cost.md){ .study-lecture data-lecture="01-calibrated-predictions-and-decisions-under-cost.md" } — Derive an action threshold from costs and measure the option to defer.
- [02 · Constrained optimization and planning](02-constrained-optimization-and-planning.md){ .study-lecture data-lecture="02-constrained-optimization-and-planning.md" } — Choose a feasible assignment under shared resources and compare it with greedy ranking.

### Learn and evaluate from feedback

- [03 · Contextual bandits and off-policy evaluation](03-contextual-bandits-and-off-policy-evaluation.md){ .study-lecture data-lecture="03-contextual-bandits-and-off-policy-evaluation.md" } — Estimate a target policy from logged actions, rewards and propensities while checking support.
- [04 · Sequential decisions and safe policy rollout](04-sequential-decisions-and-safe-policy-rollout.md){ .study-lecture data-lecture="04-sequential-decisions-and-safe-policy-rollout.md" } — Compare myopic choices with finite-horizon planning and set a release contract for feedback-driven policies.

## Workbook

[Download the workbook](../../assets/notebooks/decision-models-and-policies.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver a decision policy for a synthetic service queue, comparing thresholding, constrained assignment and a feedback policy.

**How to check your project**

Name the objective and action costs. Provide a defer route, enforce capacity, and report support and effective sample size for offline comparisons.

## Further study

- [OR-Tools CP-SAT guide](https://developers.google.com/optimization/cp/cp_solver)
- [Doubly robust policy evaluation](https://arxiv.org/abs/1103.4601)
- [Decision Transformer paper](https://arxiv.org/abs/2106.01345)
- [Off-policy evaluation](../../concepts/cards/off-policy-evaluation.md)
- [Constrained assignment](../../concepts/cards/constrained-assignment.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
