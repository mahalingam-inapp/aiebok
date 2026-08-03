# KA 06 — Knowledge Systems

## Purpose

Ground answers with retrievable evidence.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Knowledge Outside the Model** — read [chapter](../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md), run [lab](../labs/0601-knowledge-outside-the-model.md), lesson page [L-06-knowledge-systems-01](../lessons/06-knowledge-systems-01.md)
2. **Document Ingestion** — read [chapter](../books/06-knowledge-and-retrieval-systems/02-document-ingestion.md), run [lab](../labs/0602-document-ingestion.md), lesson page [L-06-knowledge-systems-02](../lessons/06-knowledge-systems-02.md)
3. **Retrieval** — read [chapter](../books/06-knowledge-and-retrieval-systems/03-retrieval.md), run [lab](../labs/0603-retrieval.md), lesson page [L-06-knowledge-systems-03](../lessons/06-knowledge-systems-03.md)
4. **Ranking and Context Selection** — read [chapter](../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md), run [lab](../labs/0604-ranking-and-context-selection.md), lesson page [L-06-knowledge-systems-04](../lessons/06-knowledge-systems-04.md)
5. **RAG Generation and Citations** — read [chapter](../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md), run [lab](../labs/0605-rag-generation-and-citations.md), lesson page [L-06-knowledge-systems-05](../lessons/06-knowledge-systems-05.md)
6. **Advanced and Enterprise RAG** — read [chapter](../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md), run [lab](../labs/0606-advanced-and-enterprise-rag.md), lesson page [L-06-knowledge-systems-06](../lessons/06-knowledge-systems-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Knowledge Outside the Model | Put knowledge in the component best suited to update, govern, query, and verify it. | Apply without baseline or slice eval |
| Document Ingestion | Retrieval cannot recover content or permissions lost during ingestion. | Apply without baseline or slice eval |
| Retrieval | Retrieval is candidate selection under relevance and policy constraints. | Apply without baseline or slice eval |
| Ranking and Context Selection | Every selected passage competes for limited attention; more context can reduce quality. | Apply without baseline or slice eval |

## Core topics

- [RAG](../concepts/cards/rag.md)
- [hybrid search](../concepts/cards/hybrid-search.md)
- [rerankers](../concepts/cards/rerankers.md)

## Guided resources

- Primary book: [Knowledge and Retrieval Systems](../books/06-knowledge-and-retrieval-systems/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Deliver hybrid RAG with citations and stage evals.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
