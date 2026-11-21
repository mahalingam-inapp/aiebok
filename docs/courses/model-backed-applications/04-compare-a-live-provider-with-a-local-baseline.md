# Compare a live provider with a local baseline

<p class="study-position" data-course="model-backed-applications" data-lecture="04-compare-a-live-provider-with-a-local-baseline.md">Measure and integrate · Lecture 4 of 4</p>

[← Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Implement the contract and baseline**

    - [Model interfaces and structured output](01-model-interfaces-and-structured-output.md)
    - [Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md)

    **Measure and integrate**

    - [Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md)
    - **Compare a live provider with a local baseline** (current)

## What you will learn

Use the same contract and cases with a model endpoint and record latency and workload conditions.

## Compare live results without changing the experiment

The local fixture responds instantly. A working model gives richer phrasing and slower answers, while some outputs fail the exact quote check.

Keep corpus, cases, and validator fixed. Record runtime and measurement conditions separately from answer quality. If you want to accept paraphrases, add a rubric and test that change rather than silently relaxing it for one model.

## How it works

An endpoint adapter is useful only if it preserves request and result semantics. Use a timeout, record the endpoint and model version, and separate infrastructure failures from model-quality failures. Capture median latency with the number of runs and distinguish a cold first request from warmed requests.

### Make the live comparison a controlled change

A deterministic baseline makes it easier to test your own application contract. A live provider introduces sampling, network delays, rate limits, and model versions. Keep the same corpus, input cases, validators, and scoring rules when changing the provider. Record anything that still differs, including timeouts and inference settings.

Run each configuration over the same cases, measuring first successful results and the spread of latency over repeated trials. Report the number of attempts and failures. Compare output quality per slice rather than assuming a provider with more natural phrasing belongs on every route.

If you change an exact-match validator to allow a paraphrase, treat it as another experiment. Decide what support means, review a small sample, and rerun both candidates with the same requirement. The workbook can run with a fixture when a local model is unavailable. Fixture timings are useful for understanding the harness and do not estimate a live workload.

## Worked example

A fast local baseline can quote retrieved evidence verbatim. A live model might respond naturally, yet a stricter validator might reject its phrasing. That difference belongs in the decision memo before selecting a backend.

## Try it yourself

Run the standard-library baseline. For the optional live run, start Ollama with an installed model and set AIEBOK_OLLAMA_MODEL to its local model name before launching Jupyter. The adapter calls the loopback generate endpoint and records any token counts returned.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The live path runs only when you configure a model. Keep the same cases and validation rules, and record the model, hardware, errors, and fallback count for interpretation.

## Continue

[← Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
