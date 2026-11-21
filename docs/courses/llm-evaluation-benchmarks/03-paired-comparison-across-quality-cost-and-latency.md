# Paired comparison across quality, cost and latency

[LLM Evaluation and Model Selection](index.md) · Measure and decide · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Report per-slice quality, a paired uncertainty interval, latency, and cost per correct task.

## How it works

Evaluate candidates on identical cases and resample paired score differences to preserve that comparison. Keep sample size visible and explain why a tiny set has wide uncertainty. Cost per correct task includes spend on failures. Report unavailable metrics explicitly.

## Worked example

A cheap model can cost more per correct result when its mistakes are frequent. A higher median score can coexist with a critical-slice regression.

## Try it yourself

Run the three fixture candidates and compare the paired delta. Recompute after changing the seed or sample mix.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Interpret the interval as uncertainty for this workload and investigate any weak critical slice before recommending a candidate.

## Continue

[← Previous lecture](02-rubrics-and-human-agreement.md) · [Course outline](index.md) · [Next lecture →](04-release-gates-and-selection-memo.md)
