# Serving workload and release gates

<p class="study-position" data-course="reasoning-efficient-inference" data-lecture="04-serving-workload-and-release-gates.md">Improve throughput and measure honestly · Lecture 4 of 4</p>

[← Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Allocate compute at inference time**

    - [Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md)
    - [Bounded search and independent verification](02-bounded-search-and-independent-verification.md)

    **Improve throughput and measure honestly**

    - [Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md)
    - **Serving workload and release gates** (current)

## What you will learn

Report time to first token, inter-token latency, and verified quality under a predeclared serving gate.

## A warm benchmark misses the expensive cohort

A performance report looks good on repeated policy prompts. A contractor batch uses fresh logs, increasing the queue time for first tokens.

Fix separate gates for warm and cold cohorts. Record prompt lengths and concurrency so a follow-up can reproduce the failure.

## How it works

Continuous batching can admit a new request between generation steps. Prefix caching can reuse prefill work for a compatible model and prefix. KV paging manages allocation, while quantization changes storage or arithmetic. Prefill/decode disaggregation adds a transfer path. These mechanisms target different bottlenecks. Benchmark warm and cold requests, concurrency, input length and output length under the same quality contract.

### Report tails with their workloads
Keep warm cache, cold cache, short prompt, long prompt, low concurrency, and saturation visible in the benchmark. Time to first token covers queueing and prefill. Inter-token timing captures cadence during decode. Record total end-to-end latency as its own measure. The output from the faster route must still pass the same frozen functional checks. Bottlenecks can move when a batching or caching change makes another stage busier.

## Worked example

A cache improves repeated short prompts. A cohort with long unique prompts gains little and may experience worse p95 time to first token because it competes for capacity.

### Follow the example

**Given:** One hundred warm requests have time to first token of 85 ms. Three cold requests take 140, 210, and 310 ms.

**Walkthrough:** The pooled p95 is 85 ms, and the cold p95 is 310 ms under the nearest-rank definition. A 200 ms cold gate fails despite the reassuring aggregate.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from math import ceil


def p95(observations):
    return sorted(observations)[ceil(0.95 * len(observations)) - 1]


# Synthetic milliseconds. Pooling makes the smaller cohort's failure disappear.
warm = [85] * 100
cold = [140, 210, 310]
limit = 200
assert p95(warm + cold) <= limit < p95(cold)
print("p95 TTFT by cohort", {"warm": p95(warm), "cold": p95(cold), "pooled": p95(warm + cold)})
```

## Try it yourself

Apply one release gate to the candidate fixtures. Inspect what happens when the warm and cold cohorts are pooled.

[Download the workbook](../../assets/notebooks/reasoning-efficient-inference.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Gate each critical cohort explicitly. Avoid describing fixture timing as measured latency or conflating prefill latency with total time.

## Continue

[← Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
