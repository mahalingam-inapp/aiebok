# LLM Evaluation and Model Selection

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build a paired benchmark, calibrate a grading rubric, and decide which candidate can ship.

[Start the first lecture](01-workload-design-and-versioned-cases.md){ .md-button .md-button--primary .study-start data-course="llm-evaluation-benchmarks" }

## Practice case · The reviewer who disagreed with the leaderboard

Ren runs a model comparison for an employee policy assistant. A vendor has the best aggregate score, yet the reviewer rejects several responses that involve exceptions. The decision memo will be used by a procurement lead who needs to know why a seemingly strong model might be held.

This fictional case continues through the lectures.

For a documented comparison, read [When a better-liked model got harder to trust](../../casebook/model-behavior-rollback.md).

## Entry prerequisites

Python, model-backed applications, and basic evaluation metrics.

## Course outline

### Design trustworthy evidence

- [01 · Workload design and versioned cases](01-workload-design-and-versioned-cases.md){ .study-lecture data-lecture="01-workload-design-and-versioned-cases.md" } — Freeze a workload containing expected outcomes, critical slices, and realistic negative cases.
- [02 · Rubrics and human agreement](02-rubrics-and-human-agreement.md){ .study-lecture data-lecture="02-rubrics-and-human-agreement.md" } — Calibrate a binary rubric on paired reviewer labels before relying on an automated grader.

### Measure and decide

- [03 · Paired comparison across quality, cost and latency](03-paired-comparison-across-quality-cost-and-latency.md){ .study-lecture data-lecture="03-paired-comparison-across-quality-cost-and-latency.md" } — Report per-slice quality, a paired uncertainty interval, latency, and cost per correct task.
- [04 · Release gates and selection memo](04-release-gates-and-selection-memo.md){ .study-lecture data-lecture="04-release-gates-and-selection-memo.md" } — Apply hard quality thresholds before optimizing for cost or speed.

## Workbook

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Compare three candidates on a frozen workload. Submit a benchmark report, rubric, candidate versions, slice results, and a model decision.

**How to check your project**

Use the same cases for each candidate. Report coverage, grader agreement, latency, and cost per correct task. Block a candidate that fails a critical slice even when its aggregate score is higher.

## Further study

- [Donner’s Choosing the Right LLM](https://github.com/ed-donner/choose_llm)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
