# Retrieval and RAG Engineer Capstone

Build a source-grounded policy search feature for a synthetic organization. Include revised, future-dated, and role-restricted documents. Work from the [Retrieval System Engineering workbook](../../courses/retrieval-system-engineering/index.md).

## Milestones

1. Build an ingestion manifest with source IDs, revisions, and access fields. Label at least 15 queries, including at least one unanswerable and one restricted case.
2. Evaluate lexical, dense, and hybrid or reranked configurations on identical queries. Record recall at K and reciprocal rank, plus query latency with sample size and measurement conditions.
3. Demonstrate one freshness change, one denied result, and one invalid citation. Explain a concrete retrieval change using the stage metrics.

## Rubric

| Evidence | Complete when |
|---|---|
| Ingestion and access | Revisions are deterministic and restricted sources are excluded before retrieval. |
| Retrieval comparison | Each method uses the same labels and the report locates both missing and low-ranked evidence. |
| Answer verification | Citations point to eligible retrieved evidence and unresolved cases abstain. |

[Back to the learning path](retrieval-rag-engineer.md)
