# Prefill, decode and speculative decoding

<p class="study-position" data-course="reasoning-efficient-inference" data-lecture="03-prefill-decode-and-speculative-decoding.md">Improve throughput and measure honestly · Lecture 3 of 4</p>

[← Bounded search and independent verification](02-bounded-search-and-independent-verification.md) · [Course outline](index.md#course-outline){ .study-overview } · [Serving workload and release gates →](04-serving-workload-and-release-gates.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Allocate compute at inference time**

    - [Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md)
    - [Bounded search and independent verification](02-bounded-search-and-independent-verification.md)

    **Improve throughput and measure honestly**

    - **Prefill, decode and speculative decoding** (current)
    - [Serving workload and release gates](04-serving-workload-and-release-gates.md)

## What you will learn

Model draft-token acceptance and explain when speculation can lower decode time.

## Reject the suffix when the prefix changes

The draft system expects a policy sentence to end with 'business days'. The target chooses a token that begins a different phrase.

Keep the matching prefix and continue from the target's chosen token. Any later draft token was proposed in an obsolete context.

## How it works

Prefill processes the prompt. Decode produces incremental continuations and accesses cached state. A speculative system proposes several draft tokens and asks the target to check them together. In greedy decoding, accept matching tokens through the first mismatch and emit the target token at that position. Exact stochastic sampling requires acceptance and correction using the draft and target distributions.

### Keep comparison conditions fixed
Draft and target can have different compute costs and batching behavior. Log how many proposed tokens are accepted per check and compare against a non-speculative baseline on the same output lengths. Greedy verification is a useful teaching limit. For sampling, equality to one sampled target continuation is not the acceptance rule, and dropping the correction step can change the output distribution.

## Worked example

A four-token draft with a mismatch at position three commits the first two draft tokens and the target's third token. The last draft token is discarded because it depends on a different prefix.

### Follow the example

**Given:** A draft proposes a, b, x, d. The greedy target agrees on a and b and selects c next.

**Walkthrough:** Commit a, b, c. Verify the continuation from that prefix. This trace assumes greedy verification and does not cover stochastic acceptance.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def greedy_speculation(draft, target):
    """One check. Target must supply a token for each position verified."""
    if len(target) < len(draft):
        raise ValueError("Missing target tokens")
    for index, token in enumerate(draft):
        if token != target[index]:
            return tuple(draft[:index]) + (target[index],), index
    return tuple(draft), len(draft)


assert greedy_speculation(("a", "b", "x", "d"), ("a", "b", "c", "z")) == (("a", "b", "c"), 2)
assert greedy_speculation(("a", "b"), ("a", "b")) == (("a", "b"), 2)
print(greedy_speculation(("a", "b", "x", "d"), ("a", "b", "c", "z")))
```

## Try it yourself

Compare identical and mismatched drafts with the same greedy target fixtures. Explain why committed tokens per check is only a proxy for speed.

[Download the workbook](../../assets/notebooks/reasoning-efficient-inference.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Draft work, verifier cost, batching and workload shape can overturn the speedup. Preserve the target's decoding contract when measuring latency.

## Continue

[← Bounded search and independent verification](02-bounded-search-and-independent-verification.md) · [Course outline](index.md#course-outline){ .study-overview } · [Serving workload and release gates →](04-serving-workload-and-release-gates.md)
{: .study-directions .study-directions--footer }
