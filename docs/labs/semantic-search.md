# Lab — Semantic Search

## Objective

Build intuition for vector representation and ranking without an embedding API.

## Run

```bash
python labs/02-semantic-search/main.py
```

The toy embedder hashes words into a fixed vector. It is not semantically learned, but it exposes the pipeline: normalize → embed → compare → rank.

## Exercises

1. Add domain synonyms during normalization.
2. Change vector dimensions and observe collisions.
3. Add an exact keyword bonus to create hybrid scoring.
4. Create five queries with expected top results and calculate recall@1.
5. Replace the toy embedder with a real embedding model in an optional notebook.

## Reflection

Which failures are caused by representation, corpus quality, query ambiguity, or ranking? What metadata filters would be mandatory in a multi-tenant system?
