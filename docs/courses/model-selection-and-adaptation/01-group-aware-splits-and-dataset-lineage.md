# Group-aware splits and dataset lineage

<p class="study-position" data-course="model-selection-and-adaptation" data-lecture="01-group-aware-splits-and-dataset-lineage.md">Prepare data and learn a baseline · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Fit and compare a supervised baseline →](02-fit-and-compare-a-supervised-baseline.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Prepare data and learn a baseline**

    - **Group-aware splits and dataset lineage** (current)
    - [Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md)

    **Choose a threshold and package evidence**

    - [Measure selective risk and cost](03-measure-selective-risk-and-cost.md)
    - [Version a model artifact and regression gate](04-version-a-model-artifact-and-regression-gate.md)

## What you will learn

Split records by group and document lineage before training.

## Put related incidents in the same split

Several students use the same residence template for a network issue. Randomly splitting individual tickets leaves near copies in training and test.

Group by site and incident pattern where possible. Keep related records together and report those grouping decisions with the split. A realistic holdout includes unfamiliar phrasing.

## How it works

Allocate related examples to the same split. Grouping by source, customer, or template prevents paraphrases of one event appearing in both the train and holdout sets. Keep a version and record counts for each slice. A tiny fixture demonstrates the mechanics while leaving uncertainty visible.

### Split independent work before fitting

Repeated templates and near-duplicate incidents can make random row splits misleading. If similar tickets appear in both training and evaluation, a model can learn a wording shortcut and still look as if it generalized. Choose a group such as site, original incident, or source document so related rows stay together.

Record fields as they existed at the moment the prediction is made. A status added by the support team after resolution is part of the outcome, even if it is present in a table you can train on. Excluding it may lower measured accuracy and make that evidence more representative of the deployed task.

Use training data to fit, validation data to choose settings, and a held-out test to report the final comparison. Record group membership and preprocessing versions. Review a few examples from each split to check that the separation is meaningful, not merely an artifact of the grouping key.

## Worked example

Two requests copied from one campus support template share a group. Putting one copy in validation would make scores artificially optimistic.

## Try it yourself

Compute the group intersections across train, validation and test. Change one fixture so a group leaks across the split.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The leakage assertion should fail and identify the crossing group before fitting begins.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Fit and compare a supervised baseline →](02-fit-and-compare-a-supervised-baseline.md)
{: .study-directions .study-directions--footer }
