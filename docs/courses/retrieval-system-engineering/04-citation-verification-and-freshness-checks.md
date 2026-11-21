# Citation verification and freshness checks

[Retrieval System Engineering](index.md) · Fuse, rank and verify · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Allow citations only to eligible retrieved evidence and abstain when evidence is incomplete.

## How it works

Validate source IDs against the passages the response received and verify the supporting text. Treat a stale revision as unavailable even if it was present in a prior cached result. Reevaluate after indexes or access policies change.

## Worked example

A candidate quotes an old leave policy accurately. The citation is still invalid when that revision is no longer eligible.

## Try it yourself

Run the freshness and citation fixtures. Add a case where a restricted source has the best lexical match.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The restricted source is filtered before both rankings, and the grounded-answer stage uses only retrieved, currently eligible evidence.

## Continue

[← Previous lecture](03-hybrid-fusion-and-relevance-diagnostics.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
