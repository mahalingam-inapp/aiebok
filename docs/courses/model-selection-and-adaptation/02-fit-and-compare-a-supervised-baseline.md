# Fit and compare a supervised baseline

[Model Selection and Adaptation Lab](index.md) · Prepare data and learn a baseline · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Train a Naive Bayes text classifier and compare its decisions with a majority-class baseline.

## How it works

Naive Bayes combines empirical class priors with smoothed token likelihoods. Use Laplace smoothing to avoid assigning zero probability to unseen terms. Compare with a majority baseline trained on the same partition. Its score puts any gain from text features into context.

## Worked example

A model trained on Wi-Fi and image-projector reports may learn the word projector. Spelling changes and overlapping words can still move its estimate unexpectedly.

## Try it yourself

Fit the two approaches on train. Print out predictions for validation and explain which words contribute to one mistake.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Keep priors and token counts tied to train. Explain the error rather than tuning directly on the test split.

## Continue

[← Previous lecture](01-group-aware-splits-and-dataset-lineage.md) · [Course outline](index.md) · [Next lecture →](03-measure-selective-risk-and-cost.md)
