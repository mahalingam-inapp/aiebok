# Reranking

**Purpose:** Re-order initial retrieval candidates with a more accurate but expensive scorer before packing context for generation.

**Prerequisites:** Retrieval (lexical and/or dense), latency budgeting, evaluation metrics.

## Why reranking exists

First-stage retrievers optimize for speed and recall@k, not final answer quality. Rerankers—often cross-encoders or dedicated reranking models—score query–passage pairs jointly and improve precision at the top of the list.

## Core intuition

Retrieval proposes; reranking disposes. Reciprocal rank fusion merges multiple first-stage lists without score calibration; learned rerankers refine a shortlist before the generator sees it.

## Mechanics

1. Retrieve top N candidates quickly (lexical, dense, or hybrid).
2. Fuse lists if multiple retrievers ran (e.g., reciprocal rank fusion).
3. Rerank top M ≪ N with a cross-encoder or reranker model.
4. Deduplicate, diversify, and pack selected passages under a token budget.
5. Measure precision@k and end-to-end faithfulness—not reranker accuracy alone.

## Engineering checklist

- Cap N and M from latency budgets; reranking every document in the corpus is infeasible.
- Evaluate on hard negatives and paraphrased queries.
- Log both pre- and post-rerank lists for failure analysis.
- Compare quality/latency against skipping reranking on low-risk query classes.

## Code practice

Run `python docs/code-samples/06-hybrid-rag.py` and extend it with a toy reranker score.

## Trade-offs

Reranking improves top-result quality but adds model calls and milliseconds to seconds of latency. Fusion without reranking may suffice for identifier-heavy query sets.

## Common misconceptions

- Higher reranker benchmark scores do not guarantee downstream answer quality.
- Fusion fixes complementary retrievers; it does not fix bad embeddings or ACL filters.
- More context after reranking can still hurt generation if packing is naive.

## Evolution lens

Yesterday: single retriever score. Today: multi-stage retrieve-then-rerank pipelines. Tomorrow: unified models with late interaction and adaptive depth. The durable principle is spending compute where marginal relevance gain is highest.
