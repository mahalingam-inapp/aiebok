# From Local to Global: A Graph RAG Approach to Query-Focused Summarization

## Citation

Edge et al.. *From Local to Global: A Graph RAG Approach to Query-Focused Summarization.* 2024. [https://arxiv.org/abs/2404.16130](https://arxiv.org/abs/2404.16130)

## One-sentence contribution

Graph structure over corpus supports global summarization queries.

## Problem

Standard vector RAG retrieves local chunks similar to the query—it fails on global questions that require synthesizing information across an entire corpus ('What are the main themes in this dataset?' or 'How does entity X relate to entity Y across all documents?').

## Prior art

Naive chunk-and-embed RAG handled entity-specific queries but not corpus-wide synthesis. Knowledge graphs required manual schema design and entity resolution. Map-reduce summarization was expensive and lost detail.

## Core idea

Edge et al. build a graph index in two phases: (1) extract entities and relationships from each text chunk using an LLM, forming a knowledge graph; (2) apply community detection (Leiden algorithm) to cluster related entities, then generate natural-language summaries for each community. At query time, map-reduce operates over community summaries for global queries, or graph traversal for local entity queries. This hierarchical structure captures both fine-grained entity facts and high-level corpus themes.

## Evidence

- Podcast transcript corpus: Graph RAG produced more comprehensive answers on global sensemaking queries vs. naive RAG (human eval).
- Entity-specific queries: graph traversal retrieved relevant context missed by vector search alone.
- Community summaries captured themes not present in any single chunk.
- Indexing cost is higher than naive RAG but amortized over many queries.

## Limitations

- Graph extraction errors propagate—wrong entities or relations corrupt the index.
- Community detection parameters affect summary granularity; no universal settings.
- Indexing requires LLM calls per chunk for entity extraction—expensive for large corpora.
- Dynamic corpora require re-indexing; incremental updates are non-trivial.

## Lasting impact

Graph RAG became Microsoft's recommended pattern for enterprise RAG on document collections and influenced Neo4j, LangChain, and LlamaIndex graph retrieval modules. It addresses a real failure mode of production RAG systems.

## Reproduction exercise

Index 20 news articles: extract entities/relations with an LLM, build a NetworkX graph, detect communities, summarize each. Ask 5 global questions ('What themes appear across these articles?') and compare Graph RAG answers against naive top-k chunk RAG.

## Related chapters

- [06 Advanced And Enterprise Rag](../../books/06-knowledge-and-retrieval-systems/06-advanced-and-enterprise-rag.md)
- [02 Document Ingestion](../../books/06-knowledge-and-retrieval-systems/02-document-ingestion.md)
- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)

## Related concepts

- [Graph Rag](../../concepts/cards/graph-rag.md)
- [Retrieval](../../concepts/cards/retrieval.md)
- [Summarization](../../concepts/cards/summarization.md)
