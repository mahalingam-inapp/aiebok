# Enterprise RAG End to End

## Goal

Ship authorized hybrid RAG with citations and stage evals.

## Overview

Build a production-shaped RAG pipeline from document ingestion through grounded answers with verifiable citations. You will wire hybrid retrieval, reranking, and stage-specific evals so every release is backed by measurable evidence.

## Architecture

Separate ingestion, retrieval, generation, and validation into distinct services with typed contracts. The ingestion worker writes normalized chunks and metadata to object storage and registers them in a manifest table. The query path runs authorization filters first, then hybrid retrieval, reranking, context assembly, and finally generation behind a gateway that logs traces and enforces token budgets.

## Prerequisites

Complete the matching [guided book](../books/06-knowledge-and-retrieval-systems/index.md) and related labs.

## Build phases

### 1. Ingestion manifest

**Goal:** Produce a reproducible, auditable corpus with chunk lineage.

**Steps:**
   - Define a source manifest schema: source_id, uri, checksum, acl_tags, ingested_at.
   - Implement a chunker that emits parent/child chunks with stable chunk_id hashes.
   - Write ingestion jobs that idempotently upsert manifest rows and chunk artifacts.
   - Add a dry-run mode that validates ACL tags and rejects documents missing required metadata.

**Acceptance:**
   - Re-running ingestion on unchanged sources produces zero duplicate chunks.
   - Every chunk traceable to source_id, page/section, and ingestion job version.
   - Manifest query returns only documents authorized for a test principal.

   **Commands:**

   ```bash
   python -m scripts.ingest --manifest data/sources.yaml --dry-run
   python -c "from ingest.manifest import load; print(len(load('data/sources.yaml')))"
   pytest tests/test_ingestion_manifest.py -q
   ```
### 2. Hybrid retrieval

**Goal:** Combine lexical and dense recall with metadata filters.

**Steps:**
   - Build a BM25 index over chunk text with stored metadata fields.
   - Embed chunks with a local sentence-transformer and load vectors into an ANN index.
   - Implement metadata-filter-first query routing (tenant, acl_tags, doc_type).
   - Fuse BM25 and dense hits with reciprocal rank fusion (RRF).

**Acceptance:**
   - Recall@20 on a held-out query set exceeds BM25-only baseline.
   - Queries with acl_tags never return chunks from unauthorized sources.
   - P95 retrieval latency under 200 ms on the local benchmark corpus.

   **Commands:**

   ```bash
   python retrieval/build_bm25.py --corpus data/chunks.jsonl --out indexes/bm25
   python retrieval/build_vectors.py --corpus data/chunks.jsonl --out indexes/faiss
   python retrieval/search.py --query "refund policy" --k 20 --hybrid
   ```
### 3. Reranker

**Goal:** Improve precision of top-k context with a cross-encoder or lightweight reranker.

**Steps:**
   - Collect 50–100 query–passage relevance labels from your eval set.
   - Wire a cross-encoder reranker that scores fused candidates.
   - Truncate to top-N passages after rerank while respecting token budget headroom.
   - Log rerank scores and rank deltas for offline analysis.

**Acceptance:**
   - MRR@5 improves over RRF-only fusion on the labeled set.
   - Top-8 passages fit within 70% of the context token budget.
   - Reranker failures fall back to RRF ordering without empty context.

   **Commands:**

   ```bash
   python retrieval/rerank.py --query "SLA breach" --candidates tmp/hits.json
   python eval/rerank_ablation.py --baseline rrf --candidate cross-encoder
   ```
### 4. Grounded generation

**Goal:** Generate answers constrained to retrieved evidence.

**Steps:**
   - Assemble a context block with numbered passage citations [1]..[N].
   - Use a system prompt that forbids claims without citation markers.
   - Route generation through a gateway that records prompt hash and model version.
   - Return structured output: answer text, cited chunk_ids, abstention flag.

**Acceptance:**
   - Every factual sentence in the answer maps to at least one citation marker.
   - Abstention triggers when retrieval confidence score is below threshold.
   - Generation trace includes prompt version, model id, and token counts.

   **Commands:**

   ```bash
   python rag/generate.py --query "data retention" --context ctx.json --out answer.json
   python -m pytest tests/test_grounded_generation.py -k citation_required -q
   ```
### 5. Citation validator

**Goal:** Verify that cited passages support the claims in the answer.

**Steps:**
   - Parse citation markers and resolve them to chunk text.
   - Run an entailment or overlap check between each claim span and its cited passage.
   - Flag unsupported claims and optionally trigger a repair pass with stricter prompt.
   - Emit a validation report attached to the response metadata.

**Acceptance:**
   - Validator catches deliberately hallucinated citations in adversarial test cases.
   - Supported-claim ratio reported per request in structured metadata.
   - Failed validation downgrades to abstention rather than ungrounded output.

   **Commands:**

   ```bash
   python rag/validate_citations.py --answer answer.json --chunks data/chunks.jsonl
   python eval/citation_suite.py --cases tests/adversarial_citations.jsonl
   ```
### 6. Release gate

**Goal:** Block deploys that regress retrieval, grounding, or latency SLOs.

**Steps:**
   - Define gold cases with expected citations and slice tags (domain, difficulty).
   - Run stage evals: retrieval recall, citation precision, end-to-end answer quality.
   - Set threshold gates per slice; fail CI if any critical slice regresses.
   - Archive eval artifacts (metrics JSON, sample traces) with the release tag.

**Acceptance:**
   - CI fails when citation precision drops more than 2 points on any slice.
   - Release artifact bundle includes eval report and rollback instructions.
   - Canary config ready before merge to main.

   **Commands:**

   ```bash
   python eval/run_stage_evals.py --suite gold --out reports/stage_eval.json
   python eval/release_gate.py --report reports/stage_eval.json --thresholds config/thresholds.yaml
   ```

## Troubleshooting

- Retrieval returns irrelevant passages: inspect chunk size, metadata filters, and embedding model mismatch between index and query time.
- Answers cite wrong chunks: verify citation numbering in context assembly and that chunk_ids survive reranking.
- High latency: profile ANN index size, reranker batch size, and generation token limits separately.
- Eval flakiness: pin model and index versions; ensure gold cases use frozen corpus snapshots.

## Related patterns

- [Hybrid Retrieval](../patterns/hybrid-retrieval.md)
- [Retrieve Then Rerank](../patterns/retrieve-then-rerank.md)
- [Citation Validator](../patterns/citation-validator.md)
- [Citation Grounded Answer](../patterns/citation-grounded-answer.md)
- [Eval Gated Release](../patterns/eval-gated-release.md)

## Related labs

- [0602 Document Ingestion](../labs/0602-document-ingestion.md)
- [0603 Retrieval](../labs/0603-retrieval.md)
- [0604 Ranking And Context Selection](../labs/0604-ranking-and-context-selection.md)
- [0605 Rag Generation And Citations](../labs/0605-rag-generation-and-citations.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
