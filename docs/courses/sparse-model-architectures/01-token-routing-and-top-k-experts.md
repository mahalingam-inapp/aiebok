# Token routing and top-k experts

<p class="study-position" data-course="sparse-model-architectures" data-lecture="01-token-routing-and-top-k-experts.md">Route tokens through experts · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Expert capacity and load balancing →](02-expert-capacity-and-load-balancing.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Route tokens through experts**

    - **Token routing and top-k experts** (current)
    - [Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md)

    **Size the system and workload**

    - [Expert parallelism and communication](03-expert-parallelism-and-communication.md)
    - [Hybrid backbones and architecture selection](04-hybrid-backbones-and-architecture-selection.md)

## What you will learn

Implement top-k expert routing and distinguish it from routing entire requests to different models.

## Follow one token across the layer

A maintenance request goes to the long-document endpoint. A diagram on the team wall labels that endpoint an expert, which makes it hard to discuss what the model actually computes.

Draw one box around the endpoint decision and another around the token-level operation. A request can take one endpoint and still use many experts inside it across tokens and layers.

## How it works

A sparse transformer can replace its feed-forward block with a bank of feed-forward experts. A learned router scores experts from each token's hidden state. The layer combines the chosen expert outputs, then returns the result to the transformer. The routing weights can be normalized over the selected experts. A request router operates outside the network and selects a model or workflow for a whole request.

### What crosses the boundary
Apply the router to a token's hidden state and inspect the scores before interpreting the chosen experts. The scores determine expert identity and can also influence the mixture weights. The residual stream and attention use separate computation. In a model with one shared expert, add that expert's compute for every token before comparing with a dense feed-forward block. Always state which parameters your active-count comparison includes.

A request-level cascade may choose a sparse model as an endpoint. That service decision happens at a different layer from the token router, and you can change it without altering the checkpoint.

## Worked example

If two experts return 2 and 6 with normalized weights 0.75 and 0.25, the mixed output is 3. With eight equally sized experts and top-2, 25% of the expert-bank parameters are active per token in this toy layer. The attention block and shared parameters still execute.

### Follow the example

**Given:** Two selected experts emit 2 and 6. Their normalized weights are 0.75 and 0.25.

**Walkthrough:** Multiply and sum to get 3. Top-1 gives 2 with the first expert alone. Changing k changes the forward computation, while the full bank still needs to fit across the serving devices.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from math import exp, isclose


def mix_experts(logits, outputs, k):
    if not 1 <= k <= len(logits) or len(logits) != len(outputs):
        raise ValueError("Choose k from the available experts")
    selected = sorted(range(len(logits)), key=lambda expert: -logits[expert])[:k]
    maximum = logits[selected[0]]
    weights = [exp(logits[expert] - maximum) for expert in selected]
    total = sum(weights)
    return sum(weight * outputs[expert] for expert, weight in zip(selected, weights)) / total


assert isclose(mix_experts((1.0, 0.0), (2.0, 6.0), 1), 2.0)
for k in (1, 2):
    print("output", mix_experts((1.0, 0.0), (2.0, 6.0), k),
          "active", 100 + k * 400, "resident", 100 + 2 * 400)
```

## Try it yourself

Change the top-k value and inspect both the output and the two parameter counts.

[Download the workbook](../../assets/notebooks/sparse-model-architectures.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Top-1 selects a single expert's output. Resident expert weights do not shrink when k changes. Add shared weights to both totals when estimating the full model.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Expert capacity and load balancing →](02-expert-capacity-and-load-balancing.md)
{: .study-directions .study-directions--footer }
