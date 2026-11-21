# Autoregressive evaluation and retrieval baseline

[LLM Adaptation and Inference Lab](index.md) · Establish and adapt baselines · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Establish frozen and retrieval-augmented baselines on a held-out task.

## How it works

An autoregressive model assigns probabilities to next tokens. Compare task behavior and log loss on the same cases. A retrieval baseline can supply new facts without changing model parameters, which is useful when facts change frequently.

## Worked example

A policy task needs unfamiliar contact names. A retrieval hint gives the correct evidence without modifying the base model.

## Try it yourself

Run the bundled base and retrieval baseline on the held-out cases. Inspect where retrieval has the relevant evidence.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report both baselines and preserve the held-out examples while deciding what to adapt.

## Continue

[Course outline](index.md) · [Next lecture →](02-train-and-evaluate-a-low-rank-adapter.md)
