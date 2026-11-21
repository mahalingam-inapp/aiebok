# Fit and compare a supervised baseline

<p class="study-position" data-course="model-selection-and-adaptation" data-lecture="02-fit-and-compare-a-supervised-baseline.md">Prepare data and learn a baseline · Lecture 2 of 4</p>

[← Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md) · [Course outline](index.md#course-outline){ .study-overview } · [Measure selective risk and cost →](03-measure-selective-risk-and-cost.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Prepare data and learn a baseline**

    - [Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md)
    - **Fit and compare a supervised baseline** (current)

    **Choose a threshold and package evidence**

    - [Measure selective risk and cost](03-measure-selective-risk-and-cost.md)
    - [Version a model artifact and regression gate](04-version-a-model-artifact-and-regression-gate.md)

## What you will learn

Train a Naive Bayes text classifier and compare its decisions with a majority-class baseline.

## Make the baseline live through the same workload

The trained classifier beats the majority rule on examples written by staff. Its lead is uncertain on short student messages.

Fit both choices on the same training scope and compare on the same validation cases. Look at errors by source and length. A gain on polished examples may be irrelevant to workload routing.

## How it works

Naive Bayes combines empirical class priors with smoothed token likelihoods. Use Laplace smoothing to avoid assigning zero probability to unseen terms. Compare with a majority baseline trained on the same partition. Its score puts any gain from text features into context.

### Establish what the features add

Start with a majority classifier or a rule the existing workflow can explain. Fit it on the same training examples as the learned candidate and use the same test cases. A baseline should be cheap enough to maintain and realistic enough that beating it would matter.

A token-frequency model treats counts as evidence for a category. If the word “billing” occurs frequently in labeled payment tickets, it may raise that class's score for a new input. Smoothing prevents a word absent in one class from making the whole class impossible. A result may still depend too heavily on names or templates seen during training.

Compare errors on short and long requests. If the learned model improves only on long, well-formed examples, review whether that covers the actual intake. Check one false positive and one false negative with the desk team. Ask which available feature would correct the case and whether it would still exist at prediction time.

## Worked example

A model trained on Wi-Fi and image-projector reports may learn the word projector. Spelling changes and overlapping words can still move its estimate unexpectedly.

## Try it yourself

Fit the two approaches on train. Print out predictions for validation and explain which words contribute to one mistake.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Keep priors and token counts tied to train. Explain the error rather than tuning directly on the test split.

## Continue

[← Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md) · [Course outline](index.md#course-outline){ .study-overview } · [Measure selective risk and cost →](03-measure-selective-risk-and-cost.md)
{: .study-directions .study-directions--footer }
