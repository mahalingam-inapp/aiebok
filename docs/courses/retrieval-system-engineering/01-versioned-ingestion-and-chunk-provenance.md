# Versioned ingestion and chunk provenance

<p class="study-position" data-course="retrieval-system-engineering" data-lecture="01-versioned-ingestion-and-chunk-provenance.md">Ingest and index evidence · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Lexical retrieval and dense similarity →](02-lexical-retrieval-and-dense-similarity.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Ingest and index evidence**

    - **Versioned ingestion and chunk provenance** (current)
    - [Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md)

    **Fuse, rank and verify**

    - [Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md)
    - [Citation verification and freshness checks](04-citation-verification-and-freshness-checks.md)

## What you will learn

Track source identity, revision, role, and freshness through chunk creation.

## Ingest a policy so you can explain what happened later

An amended policy states a new effective date. The indexed copy includes the source text but loses which version it came from.

Retain source identity, revision, and effective and access metadata at chunk creation. Test when the old and new versions should enter retrieval. A reviewer needs to be able to reopen exactly the cited evidence.

## How it works

Use stable IDs for documents and distinct IDs for revisions or passages. Replace previous revisions predictably and filter by effective date and role before passing evidence downstream. Keep original IDs for citation and traceability.

### Keep the meaning of a document attached to every chunk

Ingestion turns sources into fragments, but each fragment still belongs to a document, a revision, and an eligibility rule. Use stable identifiers with a clear relationship between the source and its chunks. Record when a revision takes effect and what audience can see it. A document that is present is not necessarily relevant to the requested time.

Segment on structure where possible. A table cell can depend on its row and column headers, and an exception can depend on the paragraph before it. Inspect the stored fragments before training or tuning retrieval. An index cannot restore context discarded at ingestion.

Test revision changes and permissions together. Demonstrate that a new version takes over on the effective date and that a historical lookup can still find earlier eligible evidence. Keep deletion and replacement behavior explicit. A stale fragment left in a secondary index can affect results even after the primary record was updated.

## Worked example

Policy owners publish a new return window. A search result from the old revision is a freshness failure even if its wording matches the query exactly.

## Try it yourself

Inspect the bundled versioned policy records. Add a new revision and verify which one is visible to each role.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Return only the latest effective revision and respect access controls. Preserve the document ID in the result.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Lexical retrieval and dense similarity →](02-lexical-retrieval-and-dense-similarity.md)
{: .study-directions .study-directions--footer }
