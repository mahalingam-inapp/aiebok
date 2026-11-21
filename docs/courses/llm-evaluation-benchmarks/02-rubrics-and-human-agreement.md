# Rubrics and human agreement

[LLM Evaluation and Model Selection](index.md) · Design trustworthy evidence · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Calibrate a binary rubric on paired reviewer labels before relying on an automated grader.

## How it works

Write observable criteria. Report the confusion counts and both raw and chance-adjusted agreement for a binary grading task. Inspect disagreement cases and document adjudication. Perfect agreement with one label used everywhere may make chance adjustment undefined.

## Worked example

Two reviewers agree on five of six assistant answers. The one disagreement involves a valid citation supporting only part of the claim.

## Try it yourself

Run the agreement calculation and inspect the disagreement. Rewrite one rubric criterion to resolve it.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A useful rewrite states that all material claims must be supported by the cited evidence and keeps abstention separate.

## Continue

[← Previous lecture](01-workload-design-and-versioned-cases.md) · [Course outline](index.md) · [Next lecture →](03-paired-comparison-across-quality-cost-and-latency.md)
