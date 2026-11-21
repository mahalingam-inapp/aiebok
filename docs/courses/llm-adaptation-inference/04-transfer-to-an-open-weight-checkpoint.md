# Transfer to an open-weight checkpoint

[LLM Adaptation and Inference Lab](index.md) · Compress and transfer · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Run the same train and holdout comparison against a compatible local transformer checkpoint.

## How it works

An open-weight model adds tokenization, pretrained weights, and hardware-dependent serving. Freeze the checkpoint and train a low-rank output correction using synthetic labels. Use isolated train and test cases, and compare whether the change improves the intended task enough to justify deployment.

## Worked example

A small local causal LM can be adapted to choose two response labels. Changes in label tokenization affect what the classifier can reliably measure.

## Try it yourself

Run the default offline comparison. For the optional transfer, configure a compatible local checkpoint as described in the workbook and compare held-out label probabilities.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Record the checkpoint and tokenizer versions. Keep the default runnable result separate from the checkpoint experiment and compare held-out evidence before considering release.

## Continue

[← Previous lecture](03-quantization-and-inference-measurement.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
