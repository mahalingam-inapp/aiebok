# Lab 9.3 — AI-Native Development Workflow

## Objective

Run a bounded repository task with two assistants and compare review burden.

## Prerequisites

Book [AI Software and Product Engineering](../books/09-ai-software-and-product-engineering/index.md), chapter 3.

## Run

```bash
python labs/0903-ai-native-development-workflow/main.py
python -m pytest labs/0903-ai-native-development-workflow/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
