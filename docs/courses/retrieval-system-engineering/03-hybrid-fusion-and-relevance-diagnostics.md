# Hybrid fusion and relevance diagnostics

<p class="study-position" data-course="retrieval-system-engineering" data-lecture="03-hybrid-fusion-and-relevance-diagnostics.md">Fuse, rank and verify · Lecture 3 of 4</p>

[← Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md) · [Course outline](index.md#course-outline){ .study-overview } · [Citation verification and freshness checks →](04-citation-verification-and-freshness-checks.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Ingest and index evidence**

    - [Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md)
    - [Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md)

    **Fuse, rank and verify**

    - **Hybrid fusion and relevance diagnostics** (current)
    - [Citation verification and freshness checks](04-citation-verification-and-freshness-checks.md)

## What you will learn

Fuse two rankings, rerank the candidates, and measure retrieval by stage.

## Find the lost document or the buried document

Two rankings contain the right record, but after combining them the passage appears below the cutoff. The metric reports a miss either way.

Inspect candidate recall and rank at each stage. Reranking can improve ordering when a passage is present, but it cannot recover a passage removed before scoring. Keep a labeled example of each failure.

## How it works

Rank fusion combines evidence from different scorers. A second pass can use higher-cost features to reorder a short list. Measure recall at K and reciprocal rank on open, restricted, and no-answer queries, distinguishing answerable queries from safe abstention.

### Diagnose candidates before tuning the final order

Combine lexical and dense rankings when their strengths complement each other. Rank-based fusion can favor candidates that appear high in either list without requiring compatible score scales. A later reranker can use more context to order the smaller set, at the cost of another processing step.

For a labeled query, inspect the candidate pool before reranking. If the correct passage never arrived, changing the final scoring cannot recover it. If it appears but falls after the cutoff, ranking is a plausible fix. Track recall at each candidate limit and the rank of the first relevant result to separate the two questions.

A practical evaluation includes exact codes, synonyms, restricted sources, and queries with no answer. Compare latency along with relevance. A marginal improvement in order might not justify an additional stage for the routine workload. Keep a few cases that visibly improve and regress so the choice can be explained.

## Worked example

An exact term match for ‘board’ can favor an equipment policy over a travel policy. An additional concept match can reorder the fused candidates.

## Try it yourself

Run the retrieval report. Change the fusion parameters and compare results for the synonym and exact-term cases.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Use stage metrics to see whether the relevant document is missing from the candidates or ranked too low.

## Continue

[← Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md) · [Course outline](index.md#course-outline){ .study-overview } · [Citation verification and freshness checks →](04-citation-verification-and-freshness-checks.md)
{: .study-directions .study-directions--footer }
