# Lab 6.4 — Ranking and Context Selection

## Objective

Add reranking and measure quality versus latency.

## Prerequisites

Book [Knowledge and Retrieval Systems](../books/06-knowledge-and-retrieval-systems/index.md), chapter 4.

## Run

```bash
python labs/0604-ranking-and-context-selection/main.py
python -m pytest labs/0604-ranking-and-context-selection/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
