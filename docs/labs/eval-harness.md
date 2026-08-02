# Lab — Evaluation Harness

## Objective

Create a versioned dataset, deterministic metrics, slice results, and a release gate.

## Run

```bash
python labs/05-eval-harness/main.py
```

## Exercises

1. Add a high-risk slice whose threshold is stricter than the global threshold.
2. Capture latency and estimate per-case cost.
3. Compare two candidate functions and output a regression report.
4. Add a rubric-based score with explicit reasons.
5. Store run metadata: model, prompt, code revision, dataset version, and timestamp.

## Exit criteria

The harness must fail its process exit code when the release gate fails, making it usable in continuous integration.
