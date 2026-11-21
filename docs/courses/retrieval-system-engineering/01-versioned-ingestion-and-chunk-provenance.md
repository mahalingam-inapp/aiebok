# Versioned ingestion and chunk provenance

[Retrieval System Engineering](index.md) · Ingest and index evidence · Lecture 1 of 4 · 45–60 min · Project practicum

## What you will learn

Track source identity, revision, role, and freshness through chunk creation.

## How it works

Use stable IDs for documents and distinct IDs for revisions or passages. Replace previous revisions predictably and filter by effective date and role before passing evidence downstream. Keep original IDs for citation and traceability.

## Worked example

Policy owners publish a new return window. A search result from the old revision is a freshness failure even if its wording matches the query exactly.

## Try it yourself

Inspect the bundled versioned policy records. Add a new revision and verify which one is visible to each role.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Return only the latest effective revision and respect access controls. Preserve the document ID in the result.

## Continue

[Course outline](index.md) · [Next lecture →](02-lexical-retrieval-and-dense-similarity.md)
