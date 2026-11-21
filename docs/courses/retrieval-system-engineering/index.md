# Retrieval System Engineering

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build and diagnose a versioned, access-aware retrieval pipeline with lexical and dense rankings.

[Start the first lecture](01-versioned-ingestion-and-chunk-provenance.md){ .md-button .md-button--primary .study-start data-course="retrieval-system-engineering" }

## Practice case · The archive remembers every version

Sana maintains a policy library where approved versions are added without deleting history. A reviewer has access to extra attachments. An answer is useful only if it cites material that was both effective at the requested date and appropriate for the requester.

This fictional case continues through the lectures.

For a documented comparison, read [A chatbot answer that changed a travel decision](../../casebook/bereavement-fares.md).

## Entry prerequisites

Python, embedding similarity, and basic information retrieval and RAG.

## Course outline

### Ingest and index evidence

- [01 · Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md){ .study-lecture data-lecture="01-versioned-ingestion-and-chunk-provenance.md" } — Track source identity, revision, role, and freshness through chunk creation.
- [02 · Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md){ .study-lecture data-lecture="02-lexical-retrieval-and-dense-similarity.md" } — Compare keyword ranking with a small dense semantic representation.

### Fuse, rank and verify

- [03 · Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md){ .study-lecture data-lecture="03-hybrid-fusion-and-relevance-diagnostics.md" } — Fuse two rankings, rerank the candidates, and measure retrieval by stage.
- [04 · Citation verification and freshness checks](04-citation-verification-and-freshness-checks.md){ .study-lecture data-lecture="04-citation-verification-and-freshness-checks.md" } — Allow citations only to eligible retrieved evidence and abstain when evidence is incomplete.

## Workbook

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver a policy-search pipeline with versioned ingestion, separate lexical and dense retrieval, reranking, and a cited response or abstention.

**How to check your project**

On labeled queries, report recall and first-relevant-rank results for three configurations. Detect a stale revision, a restricted passage, and a proposed citation outside the retrieved set.

## Further study

- [Donner’s LLM Engineering project](https://github.com/ed-donner/llm_engineering)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
