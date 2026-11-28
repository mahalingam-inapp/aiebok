# Reasoning budgets and model cascades

<p class="study-position" data-course="reasoning-efficient-inference" data-lecture="01-reasoning-budgets-and-model-cascades.md">Allocate compute at inference time · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Bounded search and independent verification →](02-bounded-search-and-independent-verification.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Allocate compute at inference time**

    - **Reasoning budgets and model cascades** (current)
    - [Bounded search and independent verification](02-bounded-search-and-independent-verification.md)

    **Improve throughput and measure honestly**

    - [Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md)
    - [Serving workload and release gates](04-serving-workload-and-release-gates.md)

## What you will learn

Design a request-level escalation policy and compare it against always using one model configuration.

## Pick an observable escalation signal

A cheap candidate returns a confident answer about a closed station. Its source date is older than the date supplied in the request.

Use verifiable source age as an escalation signal. Benchmark the whole escalation path, including both attempts and the capacity needed for a manual handoff.

## How it works

Some hosted models expose a reasoning-effort setting. A service can also route between smaller and larger models or vary a search budget. Extra compute has diminishing returns and can increase tail latency. Use a pre-specified escalation signal, such as failure to produce a verifiable answer or a difficult input slice. An internally reported confidence score needs calibration before it can drive a cascade.

### Spend the budget where you can measure it
Choose a quality gate that can be checked against the request and its authoritative evidence. Pin the prompt, endpoint version, and settings for the first and second attempts. Report verified successes divided by eligible requests and spend divided by verified successes. A cheaper average request can still produce a more expensive usable result. Use a fallback path when the remaining latency budget cannot fit another attempt.

An inference budget chooses how much compute to use for a deployed checkpoint. Post-training methods change the checkpoint itself. For example, reinforcement learning from verifiable rewards can use an outcome checker to score training responses. If you compare checkpoints as well as budgets, change one axis at a time. Include checks for whether the outputs satisfy the intended task beyond the reward signal.

## Worked example

A transit analyst uses a cheap extraction pass for routine tickets. Tickets with conflicting documents reach a more expensive evidence check. If both fail the answer contract, the workflow hands off.

### Follow the example

**Given:** A cheap attempt succeeds twice in four requests. Expensive attempts recover one of the two failures. Each cheap attempt costs 1 and each expensive attempt costs 4.

**Walkthrough:** The cascade spends 4 + 8 = 12 for three verified successes. Always-expensive uses 16 on the same fixture. Check each request separately before treating a similar aggregate score as equivalent.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
# These fixtures describe verification results, not sampled model responses.
requests = [(True, True), (True, True), (False, True), (False, False)]


def trial(rows, mode):
    verified = spend = escalations = 0
    for cheap, expensive in rows:
        if mode == "expensive":
            spend += 4
            verified += expensive
            continue
        spend += 1
        if mode == "cascade" and not cheap:
            escalations += 1
            spend += 4
            verified += expensive
        else:
            verified += cheap
    return verified, spend, escalations


for mode in ("cheap", "expensive", "cascade"):
    print(mode, trial(requests, mode))
assert trial(requests, "cascade") == (3, 12, 2)
```

## Try it yourself

Compare always-cheap, always-expensive, and cascade strategies on the same workload. Count both attempts for escalated requests.

[Download the workbook](../../assets/notebooks/reasoning-efficient-inference.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Escalation cost is the sum of both attempts. Report hard-slice quality and the handoff rate alongside the overall score.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Bounded search and independent verification →](02-bounded-search-and-independent-verification.md)
{: .study-directions .study-directions--footer }
