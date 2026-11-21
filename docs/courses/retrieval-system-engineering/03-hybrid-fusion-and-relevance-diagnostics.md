# Hybrid fusion and relevance diagnostics

[Retrieval System Engineering](index.md) · Fuse, rank and verify · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Fuse two rankings, rerank the candidates, and measure retrieval by stage.

## How it works

Rank fusion combines evidence from different scorers. A second pass can use higher-cost features to reorder a short list. Measure recall at K and reciprocal rank on open, restricted, and no-answer queries, distinguishing answerable queries from safe abstention.

## Worked example

An exact term match for ‘board’ can favor an equipment policy over a travel policy. An additional concept match can reorder the fused candidates.

## Try it yourself

Run the retrieval report. Change the fusion parameters and compare results for the synonym and exact-term cases.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Use stage metrics to see whether the relevant document is missing from the candidates or ranked too low.

## Continue

[← Previous lecture](02-lexical-retrieval-and-dense-similarity.md) · [Course outline](index.md) · [Next lecture →](04-citation-verification-and-freshness-checks.md)
