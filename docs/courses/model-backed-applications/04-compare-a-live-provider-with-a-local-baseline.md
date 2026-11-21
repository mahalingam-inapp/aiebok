# Compare a live provider with a local baseline

[Build and Evaluate a Model-Backed Application](index.md) · Measure and integrate · Lecture 4 of 4 · 45–60 min · Project practicum

## What you will learn

Use the same contract and cases with a model endpoint and record latency and workload conditions.

## How it works

An endpoint adapter is useful only if it preserves request and result semantics. Use a timeout, record the endpoint and model version, and separate infrastructure failures from model-quality failures. Capture median latency with the number of runs and distinguish a cold first request from warmed requests.

## Worked example

A fast local baseline can quote retrieved evidence verbatim. A live model might respond naturally, yet a stricter validator might reject its phrasing. That difference belongs in the decision memo before selecting a backend.

## Try it yourself

Run the standard-library baseline. For the optional live run, start Ollama with an installed model and set AIEBOK_OLLAMA_MODEL to its local model name before launching Jupyter. The adapter calls the loopback generate endpoint and records any token counts returned.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The live path runs only when you configure a model. Keep the same cases and validation rules, and record the model, hardware, errors, and fallback count for interpretation.

## Continue

[← Previous lecture](03-grounding-checks-and-evaluation-slices.md) · [Course outline](index.md) · [Course project →](index.md#course-project)
