# Build and Evaluate a Model-Backed Application

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build a source-grounded service desk assistant, measure its performance, and run a provider comparison.

[Start the first lecture](01-model-interfaces-and-structured-output.md){ .md-button .md-button--primary .study-start data-course="model-backed-applications" }

## Practice case · The answer the help desk can stand behind

Mei builds an assistant for policy questions. Users expect a short decision and a source. Her manager wants a pilot, but a false answer can force an employee to repeat a claim. She sets out to test the model path, the fallback, and the evidence people receive.

This fictional case continues through the lectures.

For a documented comparison, read [A chatbot answer that changed a travel decision](../../casebook/bereavement-fares.md).

## Entry prerequisites

Python functions, JSON, and basic retrieval. See Prompt and Context Engineering and Knowledge and Retrieval Systems for background.

## Course outline

### Implement the contract and baseline

- [01 · Model interfaces and structured output](01-model-interfaces-and-structured-output.md){ .study-lecture data-lecture="01-model-interfaces-and-structured-output.md" } — Validate a model response and distinguish response-format errors from provider failures.
- [02 · Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md){ .study-lecture data-lecture="02-retrieval-evidence-and-citations.md" } — Build a retrieval baseline, measure top-k recall, and enforce evidence scope before ranking.

### Measure and integrate

- [03 · Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md){ .study-lecture data-lecture="03-grounding-checks-and-evaluation-slices.md" } — Run fixed cases through a baseline and candidate and attribute errors by stage.
- [04 · Compare a live provider with a local baseline](04-compare-a-live-provider-with-a-local-baseline.md){ .study-lecture data-lecture="04-compare-a-live-provider-with-a-local-baseline.md" } — Use the same contract and cases with a model endpoint and record latency and workload conditions.

## Workbook

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver a runnable assistant for a small public or synthetic knowledge base. Include representative questions, a deterministic baseline, and a decision memo comparing model or retrieval choices.

**How to check your project**

Show a valid answer, insufficient evidence, restricted evidence, and a response that fails validation. Report retrieval recall, grounded answer accuracy, and fallback rates separately. Record model version and measurement conditions if you use a live model.

## Further study

- [Prompt and Context Engineering](../../books/05-prompt-and-context-engineering/index.md)
- [Knowledge and Retrieval Systems](../../books/06-knowledge-and-retrieval-systems/index.md)
- [Ollama generate API and local endpoint](https://docs.ollama.com/api/generate)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
