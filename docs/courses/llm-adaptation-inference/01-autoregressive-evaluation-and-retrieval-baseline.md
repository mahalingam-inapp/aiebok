# Autoregressive evaluation and retrieval baseline

<p class="study-position" data-course="llm-adaptation-inference" data-lecture="01-autoregressive-evaluation-and-retrieval-baseline.md">Establish and adapt baselines · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Train and evaluate a low-rank adapter →](02-train-and-evaluate-a-low-rank-adapter.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Establish and adapt baselines**

    - **Autoregressive evaluation and retrieval baseline** (current)
    - [Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md)

    **Compress and transfer**

    - [Quantization and inference measurement](03-quantization-and-inference-measurement.md)
    - [Transfer to an open-weight checkpoint](04-transfer-to-an-open-weight-checkpoint.md)

## What you will learn

Establish frozen and retrieval-augmented baselines on a held-out task.

## Recognize a retrieval problem before you train

A model chooses the wrong team for a newly reorganized unit. On older cases its label format is already correct.

Use a retrieval-assisted baseline for the current directory. Measure it alongside the frozen model on the same held-out requests. Reserve adaptation for a recurring behavior where updating facts alone cannot solve the problem.

## How it works

An autoregressive model assigns probabilities to next tokens. Compare task behavior and log loss on the same cases. A retrieval baseline can supply new facts without changing model parameters, which is useful when facts change frequently.

### Separate knowledge from behavior before changing weights

A frozen model is a baseline for the task as initially specified. A retrieval-assisted version can add current evidence without modifying that model. An adapted version changes behavior learned from examples. Compare all three on identical held-out inputs so a routing convention improvement is not confused with adding the latest directory.

An autoregressive model predicts a distribution for the next token given earlier tokens. For a routing task, inspect whether the expected label is a single token for the local tokenizer. If tokenization differs, score complete labels consistently. Measure both task outcomes and how confidently the model assigns probability to the expected label.

Include an unfamiliar category and a case that should go to staff. A model that labels routine requests more consistently may still fail when outside its evidence. Keep the simpler retrieval or rule baseline and identify what the extra training is meant to improve before spending compute.

## Worked example

A policy task needs unfamiliar contact names. A retrieval hint gives the correct evidence without modifying the base model.

## Try it yourself

Run the bundled base and retrieval baseline on the held-out cases. Inspect where retrieval has the relevant evidence.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report both baselines and preserve the held-out examples while deciding what to adapt.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Train and evaluate a low-rank adapter →](02-train-and-evaluate-a-low-rank-adapter.md)
{: .study-directions .study-directions--footer }
