# Model Selection and Adaptation Lab

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Train and compare a small text classifier using governed splits, task slices, cost estimates, and a release decision.

[Start the first lecture](01-group-aware-splits-and-dataset-lineage.md){ .md-button .md-button--primary }

## Entry prerequisites

Python, basic probability, and familiarity with held-out evaluation. See Machine Learning Systems and Training, Serving, and AI Operations.

## Course outline

### Prepare data and learn a baseline

- [01 · Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md) — Split records by group and document lineage before training.
- [02 · Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md) — Train a Naive Bayes text classifier and compare its decisions with a majority-class baseline.

### Choose a threshold and package evidence

- [03 · Measure selective risk and cost](03-measure-selective-risk-and-cost.md) — Pick an abstention threshold on validation and report coverage and accuracy on test.
- [04 · Version a model artifact and regression gate](04-version-a-model-artifact-and-regression-gate.md) — Serialize a fitted model, reload it, and gate release using both quality and coverage.

## Workbook

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver an experiment report and a saved classifier artifact for routing synthetic service requests. Compare a majority baseline with a trained model, inspect missed cases by slice, and justify an operating threshold.

**How to check your project**

Demonstrate group-disjoint splits, fit the model only on train, pick the threshold on validation, and report the untouched test results. Include false positives, abstentions, an artifact round trip, and a regression gate.

## Further study

- [Machine Learning Systems](../../books/02-machine-learning-systems/index.md)
- [Training, Serving, and AI Operations](../../books/11-training-serving-and-ai-operations/index.md)
- [Fine-tune and Serve build guide](../../guides/fine-tune-and-serve.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
