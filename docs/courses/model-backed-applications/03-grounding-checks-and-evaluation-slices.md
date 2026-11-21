# Grounding checks and evaluation slices

[Build and Evaluate a Model-Backed Application](index.md) · Measure and integrate · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Run fixed cases through a baseline and candidate and attribute errors by stage.

## How it works

Keep a frozen set of inputs with expected outcomes and evidence. Evaluate retrieval, citation support, and final decisions separately. Report per-slice counts so a class of failure cannot disappear in aggregate accuracy. Exact-match excerpts are a conservative support check for this exercise. Evaluate paraphrases with a human rubric before accepting them.

## Worked example

A candidate may retrieve the right policy yet cite an unavailable ID. That case passes retrieval but fails answer validation. A fallback preserves safety while still costing task completion.

## Try it yourself

Run both providers on the same cases and identify one case where retrieval succeeds but the provider reply fails its contract.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Keep the retrieval denominator restricted to answerable cases. Keep abstentions and invalid responses in the decision and fallback reports with their own counts.

## Continue

[← Previous lecture](02-retrieval-evidence-and-citations.md) · [Course outline](index.md) · [Next lecture →](04-compare-a-live-provider-with-a-local-baseline.md)
