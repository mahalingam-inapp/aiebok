# Lexical retrieval and dense similarity

[Retrieval System Engineering](index.md) · Ingest and index evidence · Lecture 2 of 4 · 45–60 min · Project practicum

## What you will learn

Compare keyword ranking with a small dense semantic representation.

## How it works

Lexical matching rewards shared terms and can miss synonyms. Dense vectors represent related meanings as nearby points. The lab uses manually constructed low-dimensional concept vectors so the rankings can be diagnosed by inspection.

## Worked example

The query “holidays” should retrieve a policy titled “vacation leave” even though it shares no exact terms.

## Try it yourself

Score the same labeled cases with both ranking methods and inspect the first result.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Recall can improve on vocabulary shifts. Examine a query where the semantic representation is too broad or incomplete.

## Continue

[← Previous lecture](01-versioned-ingestion-and-chunk-provenance.md) · [Course outline](index.md) · [Next lecture →](03-hybrid-fusion-and-relevance-diagnostics.md)
