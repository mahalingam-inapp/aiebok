# Release gates and selection memo

[LLM Evaluation and Model Selection](index.md) · Measure and decide · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Apply hard quality thresholds before optimizing for cost or speed.

## How it works

Set the gates before looking at results. Require enough evidence for critical slices, then compare eligible candidates by cost and latency. Save the reason, unresolved uncertainties, and what would reverse the decision.

## Worked example

The lowest-cost candidate misses one access-boundary case. It is ineligible even if it wins aggregate cost.

## Try it yourself

Run the gated selection. Tighten the latency budget and see whether any candidate still qualifies.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    A report can recommend holding all candidates. State the failed condition and choose what to investigate next.

## Continue

[← Previous lecture](03-paired-comparison-across-quality-cost-and-latency.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
