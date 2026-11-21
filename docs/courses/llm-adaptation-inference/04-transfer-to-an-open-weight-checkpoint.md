# Transfer to an open-weight checkpoint

<p class="study-position" data-course="llm-adaptation-inference" data-lecture="04-transfer-to-an-open-weight-checkpoint.md">Compress and transfer · Lecture 4 of 4</p>

[← Quantization and inference measurement](03-quantization-and-inference-measurement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Establish and adapt baselines**

    - [Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md)
    - [Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md)

    **Compress and transfer**

    - [Quantization and inference measurement](03-quantization-and-inference-measurement.md)
    - **Transfer to an open-weight checkpoint** (current)

## What you will learn

Run the same train and holdout comparison against a compatible local transformer checkpoint.

## Transfer the experiment without transferring the claim

The small fixture improves, while a transformer checkpoint uses another tokenizer and may split a routing label differently.

Confirm the output label representation and compare frozen and adapted versions on the same checkpoint and cases. A lab fixture teaches the measurement method. Production quality still needs representative traffic, a tested fallback, and proportionate rollout.

## How it works

An open-weight model adds tokenization, pretrained weights, and hardware-dependent serving. Freeze the checkpoint and train a low-rank output correction using synthetic labels. Use isolated train and test cases, and compare whether the change improves the intended task enough to justify deployment.

### Transfer the protocol as you change the model

A checkpoint experiment should record its model identity, tokenizer, local precision, label format, and hardware. Freeze the task and held-out cases first. Once the checkpoint is loaded, measure the frozen baseline before training the correction so the comparison remains interpretable.

Inspect one input and its label encoding. If an expected label spans several tokens, the score you get from looking at one token does not describe that label. Match the score to the task, and ensure the fallback remains in the evaluation. Report both result quality and the cost of reaching it.

If the optional transformer checkpoint does not improve, preserve that result. Compare it with the simple fixture and identify which assumption stopped transferring. The exercise is about producing evidence for a deployment decision, including a choice to keep the simpler baseline or restore the known-good configuration.

## Worked example

A small local causal LM can be adapted to choose two response labels. Changes in label tokenization affect what the classifier can reliably measure.

## Try it yourself

Run the default offline comparison. For the optional transfer, configure a compatible local checkpoint as described in the workbook and compare held-out label probabilities.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Record the checkpoint and tokenizer versions. Keep the default runnable result separate from the checkpoint experiment and compare held-out evidence before considering release.

## Continue

[← Quantization and inference measurement](03-quantization-and-inference-measurement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
