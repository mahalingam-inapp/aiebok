# Workload design and versioned cases

[LLM Evaluation and Model Selection](index.md) · Design trustworthy evidence · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Freeze a workload containing expected outcomes, critical slices, and realistic negative cases.

## How it works

A paired benchmark uses the same inputs for every candidate. Store intended behavior, source provenance, slice labels, and versions so results remain comparable. Keep iteration cases separate from the final held-out set.

## Worked example

A support assistant may answer a routine question, decline an unknown one, or withhold restricted information. Use fixtures that make each decision observable.

## Try it yourself

Inspect the case manifest and fingerprint. Add one abstention case and compare the fingerprint.

[Download the workbook](../../assets/notebooks/llm-evaluation-benchmarks.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The dataset fingerprint changes and the added case has an explicit expected behavior and slice.

## Continue

[Course outline](index.md) · [Next lecture →](02-rubrics-and-human-agreement.md)
