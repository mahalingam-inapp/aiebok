# Embeddings

**Purpose:** Represent objects as vectors so useful relationships can be computed.

**Prerequisites:** Vectors, dot product, model inference, tokens.

## Why embeddings exist

Exact matching cannot reliably connect “application unavailable” with “service is down.” An embedding model maps content into a dense numeric space where proximity can correspond to learned similarity.

## Core intuition

An embedding is a coordinate, not a definition. Meaning arises from relationships in the learned space and the task used to train the model.

## Mechanics

1. Normalize and tokenize the input.
2. Run it through an embedding model.
3. Obtain a fixed-length vector.
4. Compare vectors using a compatible metric.
5. Retrieve, cluster, classify, or recommend using those relationships.

Cosine similarity is:

\[
\operatorname{cos}(a,b)=\frac{a\cdot b}{\lVert a\rVert\lVert b\rVert}
\]

## Engineering checklist

- Choose models using domain and language evals, not leaderboards alone.
- Use the same compatible model/version for indexed documents and queries.
- Preserve model version and preprocessing metadata.
- Benchmark retrieval on realistic queries and hard negatives.
- Plan re-indexing, access control, deletion, and drift monitoring.

## Code practice

Run `python labs/01-cosine-similarity/main.py`, then `python labs/02-semantic-search/main.py` from the repository root.

## Trade-offs

Embeddings enable fuzzy semantic matching but can blur important distinctions, encode bias, cost storage/compute, and require re-indexing after a model change. Keyword search often remains stronger for identifiers and exact phrases; hybrid retrieval uses both.

## Common misconceptions

- Vector closeness is not universal truth.
- A vector database does not create good embeddings.
- Higher dimensionality is not automatically better.
- Embeddings alone do not make a grounded answer.

## Evolution lens

Yesterday: keywords, TF–IDF, and BM25. Today: task-tuned dense and hybrid retrieval. Tomorrow: more multimodal, contextual, and late-interaction representations. The durable principle is representing items so useful relationships become computable.
