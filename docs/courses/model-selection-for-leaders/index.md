# Model Selection Decisions for Leaders

No code · 2 sections · 4 lectures · About 2 hours, plus the project

Use a shared candidate scorecard to make a model purchasing or rollout decision.

[Start the first lecture](01-specify-the-workload-and-critical-failures.md){ .md-button .md-button--primary }

## Entry prerequisites

AI Literacy or equivalent. The examples and scorecard require no coding.

## Course outline

### Frame the decision

- [01 · Specify the workload and critical failures](01-specify-the-workload-and-critical-failures.md) — Turn a model shortlist into an evaluation brief tied to representative work.
- [02 · Interpret quality evidence and uncertainty](02-interpret-quality-evidence-and-uncertainty.md) — Read aggregate and critical-slice scores without hiding the size of the test.

### Compare economics and decide

- [03 · Cost per successful task](03-cost-per-successful-task.md) — Calculate cost per correct result and include review effort in the decision.
- [04 · Make a bounded selection decision](04-make-a-bounded-selection-decision.md) — Specify a model choice, approval owner, and conditions for reconsidering it.

## Course project

Write a one-page recommendation using the same frozen-workload scenario as the technical model-selection course.

**How to check your project**

Use a matrix that records the work done, the number of valid outcomes, cost, operational risk, and who can reconsider the decision.

| Candidate | Correct tasks out of 10 | Critical checks out of 2 | Median latency | Evaluation spend |
|---|---:|---:|---:|---:|
| Fast | 9 | 1 | 420 ms | 0.012 |
| Balanced | 9 | 2 | 680 ms | 0.026 |
| Careful | 10 | 2 | 1,100 ms | 0.051 |

Assume the pilot budget allows a median latency of at most 800 ms and requires both critical checks to pass. Choose a candidate, state the sample limitation, and specify a test that could reverse your recommendation.

## Further study

- [Donner’s Choosing the Right LLM](https://github.com/ed-donner/choose_llm)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
