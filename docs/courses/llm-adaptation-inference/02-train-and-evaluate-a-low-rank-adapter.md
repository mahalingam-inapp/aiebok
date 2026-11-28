# Train and evaluate a low-rank adapter

<p class="study-position" data-course="llm-adaptation-inference" data-lecture="02-train-and-evaluate-a-low-rank-adapter.md">Establish and adapt baselines · Lecture 2 of 4</p>

[← Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md) · [Course outline](index.md#course-outline){ .study-overview } · [Quantization and inference measurement →](03-quantization-and-inference-measurement.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Establish and adapt baselines**

    - [Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md)
    - **Train and evaluate a low-rank adapter** (current)

    **Compress and transfer**

    - [Quantization and inference measurement](03-quantization-and-inference-measurement.md)
    - [Transfer to an open-weight checkpoint](04-transfer-to-an-open-weight-checkpoint.md)

## What you will learn

Train a small adapter over frozen parameters and evaluate held-out next-token predictions.

## Inspect held-out behavior after adapting

A low-rank correction learns the labels in training. The evaluation set also contains unfamiliar phrasing that still needs human follow-up.

Compare loss and routing accuracy on data held out before training. Verify that base parameters stayed fixed. Compare against retrieval because a change in adaptation accuracy alone cannot tell you which system to ship.

## How it works

A low-rank adapter writes a correction as the product of two small matrices. The base weights stay frozen. Optimize on training loss and compare held-out metrics using the same tokenizer, cases, and scoring approach.

### Tune a small correction and inspect what transfers

A low-rank adapter represents a weight adjustment as two smaller factors. During training, keep the base fixed and optimize the factors on the training split. This reduces the parameters you need to update, while the base model still determines much of the representation available to the correction.

Compare training loss with a held-out task score. Fitting familiar labels can improve likelihood without improving what users receive. Inspect whether the model learned a stable convention or simply memorized the examples. Include valid evidence, contradictory evidence, and a realistic request that should be handed off.

Record adapter shape, base revision, data split, and optimizer settings. If the adapted configuration improves only easy requests or regresses critical slices, test a narrower route or retrieval baseline. The small workbook illustrates the mechanics of adaptation. Its result does not establish the expected gain for another model or workload.

## Worked example

A repeated output convention can be learned from examples. A recently changed phone number is better supplied by current evidence.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
# Rank one correction: A maps two input features to one number; B maps that to three logits.
a = [0.15, -0.15]
b = [0.0, 0.0, 0.0]


def forward(text, left, right):
    hidden = sum(weight * feature for weight, feature in zip(left, features(text)))
    return [value + hidden * weight for value, weight in zip(frozen(text), right)]


def adapted(text):
    return forward(text, a, b)


base_before = [frozen(row.text) for row in test]
for _ in range(100):
    for row in train:
        x = features(row.text)
        hidden = sum(weight * feature for weight, feature in zip(a, x))
        residual = [p - int(i == row.label) for i, p in enumerate(probabilities(adapted(row.text)))]
        grad_hidden = sum(error * weight for error, weight in zip(residual, b))
        a = [weight - 0.08 * grad_hidden * feature for weight, feature in zip(a, x)]
        b = [weight - 0.08 * error * hidden for weight, error in zip(b, residual)]

assert [frozen(row.text) for row in test] == base_before
assert metrics(adapted, test)["log_loss"] < metrics(frozen, test)["log_loss"]
assert metrics(adapted, test)["accuracy"] == 1
print("Adapted", metrics(adapted, test))
```

## Try it yourself

Train the bundled adapter and compare held-out results. Change the rank or training budget and record the quality change.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The frozen base stays unchanged. Report when adaptation improves behavior and identify any regression relative to retrieval.

## Continue

[← Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md) · [Course outline](index.md#course-outline){ .study-overview } · [Quantization and inference measurement →](03-quantization-and-inference-measurement.md)
{: .study-directions .study-directions--footer }
