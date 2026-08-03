# Lab 13.5 — Long Context, World Models, and Continual Learning

## Objective

Compare a frontier method with retrieval, explicit state, or fine-tuning baselines.

## Prerequisites

Book [Multimodal and Frontier Systems](../books/13-multimodal-and-frontier-systems/index.md), chapter 5.

## Run

```bash
python labs/1305-long-context-world-models-and-continual-lea/main.py
python -m pytest labs/1305-long-context-world-models-and-continual-lea/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
