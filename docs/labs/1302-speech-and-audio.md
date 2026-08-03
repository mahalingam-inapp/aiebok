# Lab 13.2 — Speech and Audio

## Objective

Build a transcript pipeline with timestamps and confidence handling.

## Prerequisites

Book [Multimodal and Frontier Systems](../books/13-multimodal-and-frontier-systems/index.md), chapter 2.

## Run

```bash
python labs/1302-speech-and-audio/main.py
python -m pytest labs/1302-speech-and-audio/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
