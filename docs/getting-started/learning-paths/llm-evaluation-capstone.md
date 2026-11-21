# LLM Evaluation and Model Selection Capstone

Compare three candidates for one bounded task using a workload other than the provided ten-case example. Candidates may be model configurations, deterministic baselines, or local providers. Report which outputs you measured and which quantities came from fixtures. Start from [LLM Evaluation and Model Selection](../../courses/llm-evaluation-benchmarks/index.md).

## Milestones

1. Freeze at least 24 labeled cases across routine, ambiguous, unanswerable, and critical slices. Record provenance and separate the cases that guide iteration.
2. Grade the paired results using a documented rubric. Double-rate a subset, inspect disagreements, and report paired uncertainty, quality by slice, latency, and cost per correct task.
3. Apply predeclared gates and write a decision memo. Identify one result that would reverse your decision and one metric that the benchmark did not measure.

## Rubric

| Evidence | Complete when |
|---|---|
| Reproducibility | A manifest, candidate configurations, and scoring instructions are sufficient to re-run the comparison. |
| Valid comparison | The report preserves pairing, denominators, failures, and critical slices, and explains uncertainty. |
| Decision | The recommendation follows the gates and states conditions for reconsideration. |

[Back to the learning path](llm-evaluation-model-selection.md)
