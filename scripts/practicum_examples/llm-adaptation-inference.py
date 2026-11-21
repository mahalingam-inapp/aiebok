from dataclasses import dataclass
from math import exp, log


@dataclass(frozen=True)
class Example:
    text: str
    label: int


labels = ("open", "review", "other")
train = (
    Example("routine facilities task", 0), Example("routine supplies request", 0),
    Example("restricted staff question", 1), Example("restricted policy change", 1),
)
test = (
    Example("routine schedule change", 0), Example("restricted legal request", 1),
    Example("routine delivery update", 0), Example("restricted vendor details", 1),
)
assert not {row.text for row in train} & {row.text for row in test}


def features(text):
    first, *_ = text.split()
    return (float(first == "routine"), float(first == "restricted"))


def probabilities(logits):
    maximum = max(logits)
    weights = [exp(value - maximum) for value in logits]
    total = sum(weights)
    return [weight / total for weight in weights]


def frozen(text):
    return (0.1, 0.0, 0.2)


guides = {"routine": 0}  # This small source has no restricted-policy guidance.


def retrieval(text):
    hint = guides.get(text.split()[0])
    return tuple(value + (2 if index == hint else 0) for index, value in enumerate(frozen(text)))


def metrics(model, cases):
    outputs = [probabilities(model(row.text)) for row in cases]
    correct = sum(max(range(len(dist)), key=dist.__getitem__) == row.label for dist, row in zip(outputs, cases))
    loss = -sum(log(dist[row.label]) for dist, row in zip(outputs, cases)) / len(cases)
    return {"accuracy": correct / len(cases), "log_loss": loss}


print("Frozen", metrics(frozen, test), "retrieval", metrics(retrieval, test))

# %%
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

# %%
from array import array
from statistics import median
from time import perf_counter


def quantize(values):
    scale = max(abs(value) for value in values) / 127 or 1
    return array("b", (round(value / scale) for value in values)), array("f", [scale])


# Pack the whole correction with one scale. The scale is included in the byte count.
float_payload = array("f", a + b)
int_payload, scale = quantize(float_payload)


def compressed(text):
    unpacked = [item * scale[0] for item in int_payload]
    return forward(text, unpacked[:len(a)], unpacked[len(a):])


def timed(model, count=300):
    values = []
    for _ in range(count):
        start = perf_counter()
        model(test[0].text)
        values.append((perf_counter() - start) * 1e6)
    return median(values)


compressed_bytes = len(int_payload.tobytes()) + len(scale.tobytes())
assert compressed_bytes < len(float_payload.tobytes())
assert abs(metrics(adapted, test)["log_loss"] - metrics(compressed, test)["log_loss"]) < 0.05
print("float bytes", len(float_payload.tobytes()), "compressed bytes", compressed_bytes,
      "median µs float/int8", timed(adapted), timed(compressed))

# %%
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
