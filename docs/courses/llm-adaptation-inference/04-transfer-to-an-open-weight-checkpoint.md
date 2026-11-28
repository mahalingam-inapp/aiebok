# Transfer to an open-weight checkpoint

<p class="study-position" data-course="llm-adaptation-inference" data-lecture="04-transfer-to-an-open-weight-checkpoint.md">Compress and transfer · Lecture 4 of 4</p>

[← Quantization and inference measurement](03-quantization-and-inference-measurement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Establish and adapt baselines**

    - [Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md)
    - [Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md)

    **Compress and transfer**

    - [Quantization and inference measurement](03-quantization-and-inference-measurement.md)
    - **Transfer to an open-weight checkpoint** (current)

## What you will learn

Run the same train and holdout comparison against a compatible local transformer checkpoint.

## Transfer the experiment without transferring the claim

The small fixture improves, while a transformer checkpoint uses another tokenizer and may split a routing label differently.

Confirm the output label representation and compare frozen and adapted versions on the same checkpoint and cases. A lab fixture teaches the measurement method. Production quality still needs representative traffic, a tested fallback, and proportionate rollout.

## How it works

An open-weight model adds tokenization, pretrained weights, and hardware-dependent serving. Freeze the checkpoint and train a low-rank output correction using synthetic labels. Use isolated train and test cases, and compare whether the change improves the intended task enough to justify deployment.

### Transfer the protocol as you change the model

A checkpoint experiment should record its model identity, tokenizer, local precision, label format, and hardware. Freeze the task and held-out cases first. Once the checkpoint is loaded, measure the frozen baseline before training the correction so the comparison remains interpretable.

Inspect one input and its label encoding. If an expected label spans several tokens, the score you get from looking at one token does not describe that label. Match the score to the task, and ensure the fallback remains in the evaluation. Report both result quality and the cost of reaching it.

If the optional transformer checkpoint does not improve, preserve that result. Compare it with the simple fixture and identify which assumption stopped transferring. The exercise is about producing evidence for a deployment decision, including a choice to keep the simpler baseline or restore the known-good configuration.

## Worked example

A small local causal LM can be adapted to choose two response labels. Changes in label tokenization affect what the classifier can reliably measure.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
import os


def checkpoint_experiment(path):
    # Install torch and transformers in the same Python environment before opting in.
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    torch.manual_seed(4)
    tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(path, local_files_only=True).eval()
    model.requires_grad_(False)
    token_ids = [tokenizer.encode(" " + label, add_special_tokens=False) for label in labels[:2]]
    if any(len(ids) != 1 for ids in token_ids) or token_ids[0] == token_ids[1]:
        raise ValueError("Choose a checkpoint with distinct single tokens for ' open' and ' review'.")

    def collect(rows):
        outputs = []
        with torch.no_grad():
            for row in rows:
                prompt = f"Ticket: {row.text}\nRoute:"
                result = model(**tokenizer(prompt, return_tensors="pt"), output_hidden_states=True)
                hidden = result.hidden_states[-1][0, -1]
                logits = result.logits[0, -1, [ids[0] for ids in token_ids]]
                outputs.append((hidden.float(), logits.float()))
        x, base = zip(*outputs)
        return torch.stack(x), torch.stack(base), torch.tensor([row.label for row in rows])

    x_train, base_train, y_train = collect(train)
    x_test, base_test, y_test = collect(test)
    left = torch.nn.Linear(x_train.shape[1], 2, bias=False)
    right = torch.nn.Linear(2, 2, bias=False)
    torch.nn.init.zeros_(right.weight)
    optimizer = torch.optim.AdamW([*left.parameters(), *right.parameters()], lr=0.02)
    for _ in range(40):
        optimizer.zero_grad()
        loss = torch.nn.functional.cross_entropy(base_train + right(left(x_train)), y_train)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        after = base_test + right(left(x_test))
        comparison = {}
        for name, logits in (("frozen", base_test), ("adapted", after)):
            comparison[name] = {
                "log_loss": torch.nn.functional.cross_entropy(logits, y_test).item(),
                "accuracy": (logits.argmax(dim=-1) == y_test).float().mean().item(),
            }
        assert torch.isfinite(after).all() and torch.count_nonzero(right.weight) > 0
        assert not any(parameter.grad is not None for parameter in model.parameters())
        print("Checkpoint", path, "held-out two-label comparison", comparison)


checkpoint = os.getenv("AIEBOK_LOCAL_CHECKPOINT")
if checkpoint:
    checkpoint_experiment(checkpoint)
else:
    print("Offline exercise passed. Install torch and transformers and set AIEBOK_LOCAL_CHECKPOINT to a local causal LM directory to run the optional comparison.")
```

## Try it yourself

Run the default offline comparison. For the optional transfer, configure a compatible local checkpoint as described in the workbook and compare held-out label probabilities.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Record the checkpoint and tokenizer versions. Keep the default runnable result separate from the checkpoint experiment and compare held-out evidence before considering release.

## Continue

[← Quantization and inference measurement](03-quantization-and-inference-measurement.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
