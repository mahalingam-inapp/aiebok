# Book 6 — Knowledge and Retrieval Systems

## Purpose

Build grounded knowledge systems whose ingestion, retrieval, generation, and citations can be evaluated separately.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Knowledge Outside the Model__

    Decide among direct context, search, databases, knowledge graphs, RAG, fine-tuning, and deterministic rules.

    [Open chapter →](01-knowledge-outside-the-model.md)

-   :material-numeric-2-circle:{ .lg .middle } __Document Ingestion__

    Preserve provenance while parsing documents, OCR, tables, images, metadata, permissions, versions, and deleti…

    [Open chapter →](02-document-ingestion.md)

-   :material-numeric-3-circle:{ .lg .middle } __Retrieval__

    Compare lexical, dense, sparse, hybrid, filtered, multi-query, parent-child, and late-interaction retrieval.

    [Open chapter →](03-retrieval.md)

-   :material-numeric-4-circle:{ .lg .middle } __Ranking and Context Selection__

    Use fusion, reranking, diversity, deduplication, compression, and token-aware packing.

    [Open chapter →](04-ranking-and-context-selection.md)

-   :material-numeric-5-circle:{ .lg .middle } __RAG Generation and Citations__

    Construct grounded prompts, handle missing evidence, attribute claims, validate citations, and avoid unsuppor…

    [Open chapter →](05-rag-generation-and-citations.md)

-   :material-numeric-6-circle:{ .lg .middle } __Advanced and Enterprise RAG__

    Study graph, multi-hop, adaptive, and agentic retrieval together with tenancy, freshness, security, resilienc…

    [Open chapter →](06-advanced-and-enterprise-rag.md)

</div>

## Entry prerequisites

- Books 3–5
- Embeddings and search
- Structured model output

## Book project

Deliver an enterprise RAG system with authorization, hybrid retrieval, reranking, citations, and stage-specific evaluation.

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Lewis et al. — Retrieval-Augmented Generation
- Karpukhin et al. — Dense Passage Retrieval

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
