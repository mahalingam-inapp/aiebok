# Lab 7.5 — MCP and Integration Protocols

## Objective

Implement a small local MCP server and test a hostile client request.

## Prerequisites

Book [Reasoning and Tool Use](../books/07-reasoning-and-tool-use/index.md), chapter 5.

## Run

```bash
python labs/0705-mcp-and-integration-protocols/main.py
python -m pytest labs/0705-mcp-and-integration-protocols/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
