# Expert capacity and load balancing

<p class="study-position" data-course="sparse-model-architectures" data-lecture="02-expert-capacity-and-load-balancing.md">Route tokens through experts · Lecture 2 of 4</p>

[← Token routing and top-k experts](01-token-routing-and-top-k-experts.md) · [Course outline](index.md#course-outline){ .study-overview } · [Expert parallelism and communication →](03-expert-parallelism-and-communication.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Route tokens through experts**

    - [Token routing and top-k experts](01-token-routing-and-top-k-experts.md)
    - **Expert capacity and load balancing** (current)

    **Size the system and workload**

    - [Expert parallelism and communication](03-expert-parallelism-and-communication.md)
    - [Hybrid backbones and architecture selection](04-hybrid-backbones-and-architecture-selection.md)

## What you will learn

Measure routing skew, simulate a capacity limit, and compare overflow against a balancing policy.

## A burst hits the same expert

A station closure causes many near-identical equipment questions to arrive together. Last week's averaged routing histogram looked balanced.

Inspect assignments at the batch boundary. Count overflow per expert, then rerun the behavior check when assignments are rerouted. A healthier histogram can still hide changed answers.

## How it works

A batch can favor one expert even when the router looks balanced across a long evaluation. A fixed bucket can overflow. Dropping, delaying, and rerouting assignments have different effects on quality and latency. Training-time balancing losses or bias updates influence routing decisions. Serving-time expert replication and placement change where already-chosen expert work runs.

### Count assignments per batch
Top-2 over 100 tokens produces 200 assignments if every token reaches two experts. Divide assignment counts by the available capacity and inspect the highest-loaded expert. Weighting the result by the total number of original tokens answers a different question. A capacity limit may be a training design choice, and some serving implementations use dropless kernels. A simulator with overflow demonstrates the consequence of a fixed-capacity policy. It does not imply every implementation drops tokens.

## Worked example

Six tokens choose expert 0 and two choose expert 1. With a capacity of four per expert, two assignments overflow even though total capacity is eight. Rerouting them fills the second expert but changes which expert processes their tokens.

### Follow the example

**Given:** The preferred loads are [6, 2] and capacity is [4, 4].

**Walkthrough:** Plain routing serves six assignments. Rerouting moves two assignments to the quieter expert and serves all eight. Test the changed outputs before deciding whether better utilization is useful.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def dispatch(preferences, expert_count, capacity, reroute=False):
    load = [0] * expert_count
    overflow = changed = 0
    for order in preferences:
        choices = order if reroute else order[:1]
        for expert in choices:
            if load[expert] < capacity:
                load[expert] += 1
                changed += expert != order[0]
                break
        else:
            overflow += 1
    return load, overflow, changed


skewed = [(0, 1)] * 6 + [(1, 0)] * 2
balanced = [(0, 1), (1, 0)] * 4
assert dispatch(skewed, 2, 4) == ([4, 2], 2, 0)
assert dispatch(balanced, 2, 4, reroute=True) == ([4, 4], 0, 0)
assert dispatch(skewed, 2, 4, reroute=True)[1] == 0
for cap in (4, 3):
    print("capacity", cap, dispatch(skewed, 2, cap, reroute=True))
```

## Try it yourself

Compare the balanced and overloaded batches. Try capacity three with the same two experts.

[Download the workbook](../../assets/notebooks/sparse-model-architectures.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    At most six assignments fit. Report the remaining overflow and the fallback assignments separately.

## Continue

[← Token routing and top-k experts](01-token-routing-and-top-k-experts.md) · [Course outline](index.md#course-outline){ .study-overview } · [Expert parallelism and communication →](03-expert-parallelism-and-communication.md)
{: .study-directions .study-directions--footer }
