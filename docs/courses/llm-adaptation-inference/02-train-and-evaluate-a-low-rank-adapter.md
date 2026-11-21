# Train and evaluate a low-rank adapter

[LLM Adaptation and Inference Lab](index.md) · Establish and adapt baselines · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Train a small adapter over frozen parameters and evaluate held-out next-token predictions.

## How it works

A low-rank adapter writes a correction as the product of two small matrices. The base weights stay frozen. Optimize on training loss and compare held-out metrics using the same tokenizer, cases, and scoring approach.

## Worked example

A repeated output convention can be learned from examples. A recently changed phone number is better supplied by current evidence.

## Try it yourself

Train the bundled adapter and compare held-out results. Change the rank or training budget and record the quality change.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The frozen base stays unchanged. Report when adaptation improves behavior and identify any regression relative to retrieval.

## Continue

[← Previous lecture](01-autoregressive-evaluation-and-retrieval-baseline.md) · [Course outline](index.md) · [Next lecture →](03-quantization-and-inference-measurement.md)
