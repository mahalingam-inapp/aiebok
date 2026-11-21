# Measure selective risk and cost

[Model Selection and Adaptation Lab](index.md) · Choose a threshold and package evidence · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Pick an abstention threshold on validation and report coverage and accuracy on test.

## How it works

A selective classifier can hand uncertain cases to a person. Accuracy among answered cases can look high if the system answers very little, so report coverage alongside it. Use independently estimated costs for mistakes and reviews. Choose the threshold with validation data and freeze it before evaluating test.

## Worked example

If one mistaken route costs four minutes and a review costs one, a threshold may be valuable even when accuracy changes little. A small sample can only illustrate the trade-off.

## Try it yourself

Compare the tested thresholds. Increase review cost and see which threshold you would choose on validation.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report accepted count, wrong accepted count, and handoffs on each slice. Explain any change through its expected operating cost.

## Continue

[← Previous lecture](02-fit-and-compare-a-supervised-baseline.md) · [Course outline](index.md) · [Next lecture →](04-version-a-model-artifact-and-regression-gate.md)
