# Group-aware splits and dataset lineage

[Model Selection and Adaptation Lab](index.md) · Prepare data and learn a baseline · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Split records by group and document lineage before training.

## How it works

Allocate related examples to the same split. Grouping by source, customer, or template prevents paraphrases of one event appearing in both the train and holdout sets. Keep a version and record counts for each slice. A tiny fixture demonstrates the mechanics while leaving uncertainty visible.

## Worked example

Two requests copied from one campus support template share a group. Putting one copy in validation would make scores artificially optimistic.

## Try it yourself

Compute the group intersections across train, validation and test. Change one fixture so a group leaks across the split.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The leakage assertion should fail and identify the crossing group before fitting begins.

## Continue

[Course outline](index.md) · [Next lecture →](02-fit-and-compare-a-supervised-baseline.md)
