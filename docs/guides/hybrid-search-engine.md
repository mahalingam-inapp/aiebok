# Hybrid Search Engine

## Goal

Lexical + dense retrieval with fusion and offline eval.

## Overview

Implement lexical plus dense search with score fusion and offline recall measurement. The result is a search service you can tune with evidence instead of intuition.

## Architecture

Indexing and query paths are separate binaries sharing a chunk schema. BM25 and vector indexes update from the same corpus snapshot. The query API accepts filters, runs both retrievers, fuses with RRF, and returns ranked hits with scores and source metadata. Offline eval computes recall@k on labeled queries.

## Prerequisites

Complete the matching [guided book](../books/06-knowledge-and-retrieval-systems/index.md) and related labs.

## Build phases

### 1. BM25 index

**Goal:** Build a lexical index with metadata filters.

**Steps:**
   - Tokenize and index chunk text with Pyserini or a lightweight BM25 implementation.
   - Store doc_id, chunk_id, and filter fields alongside postings.
   - Support incremental rebuild from corpus JSONL snapshots.
   - Expose search CLI with query, k, and filter flags.

**Acceptance:**
   - BM25 search returns deterministic ranks for fixed corpus and query.
   - Metadata filters reduce candidate set before scoring.
   - Index build completes on sample corpus in under 60 seconds.

   **Commands:**

   ```bash
   python search/build_bm25.py --corpus data/chunks.jsonl --out indexes/bm25
   python search/query_bm25.py --index indexes/bm25 --query "hybrid fusion" -k 10
   ```
### 2. Vector index

**Goal:** Embed chunks and serve approximate nearest neighbor search.

**Steps:**
   - Embed chunks with a local sentence-transformer model.
   - Build FAISS or hnswlib index with normalized vectors.
   - Persist embedding model version alongside index artifacts.
   - Implement batch embedding for rebuild throughput.

**Acceptance:**
   - Vector search returns top-k with cosine similarity scores.
   - Query embedding uses same model version as index metadata.
   - ANN index recall within 2% of brute-force on validation sample.

   **Commands:**

   ```bash
   python search/build_vectors.py --corpus data/chunks.jsonl --out indexes/faiss
   python search/query_vectors.py --index indexes/faiss --query "hybrid fusion" -k 10
   ```
### 3. RRF fusion

**Goal:** Merge ranked lists without calibrating incompatible scores.

**Steps:**
   - Retrieve top-k from BM25 and vector indexes independently.
   - Apply reciprocal rank fusion with configurable k constant (default 60).
   - Deduplicate by chunk_id, keeping best fused rank.
   - Return fused list with component ranks for debugging.

**Acceptance:**
   - Fusion improves recall@10 vs either single retriever on labeled set.
   - Duplicate chunks appear once in fused output.
   - Fusion weights tunable via config without code change.

   **Commands:**

   ```bash
   python search/hybrid_query.py --query "token budget" -k 10
   python eval/fusion_grid.py --queries data/labeled_queries.jsonl
   ```
### 4. recall@k eval

**Goal:** Measure retrieval quality offline before shipping ranking changes.

**Steps:**
   - Prepare labeled qrels: query_id, relevant chunk_ids.
   - Run batch retrieval for k in {1, 5, 10, 20}.
   - Compute recall@k and MRR; breakdown by query category.
   - Store eval results with index version and fusion config hash.

**Acceptance:**
   - Eval script outputs recall@5 and recall@10 with confidence over query count.
   - Regression vs baseline flagged when recall@10 drops >1 point.
   - Results reproducible from pinned corpus and index artifacts.

   **Commands:**

   ```bash
   python eval/recall_at_k.py --queries data/labeled_queries.jsonl --k 5,10,20
   python eval/recall_at_k.py --index-version sha256:abc123 --out reports/recall.json
   ```

## Troubleshooting

- Dense recall weak on rare tokens: increase k before fusion or add synonym expansion on BM25 path.
- RRF hurts precision: reduce k or apply reranker after fusion on top-20 only.
- Filter excludes all hits: validate filter schema at index time vs query time.
- Slow rebuilds: embed in batches and parallelize BM25 and vector builds from same snapshot.

## Related patterns

- [Hybrid Retrieval](../patterns/hybrid-retrieval.md)
- [Retrieval Fusion](../patterns/retrieval-fusion.md)
- [Metadata Filter First](../patterns/metadata-filter-first.md)
- [Retrieve Then Rerank](../patterns/retrieve-then-rerank.md)

## Related labs

- [0603 Retrieval](../labs/0603-retrieval.md)
- [0305 Similarity And Vector Search](../labs/0305-similarity-and-vector-search.md)
- [0306 Embedding Systems In Production](../labs/0306-embedding-systems-in-production.md)
- [0604 Ranking And Context Selection](../labs/0604-ranking-and-context-selection.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
