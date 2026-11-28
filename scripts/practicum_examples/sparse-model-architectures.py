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
# %%
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
# %%
def remote_bytes(assignments, placements, width, element_bytes):
    remote = sum(source_rank != placements[expert] for source_rank, expert in assignments)
    return remote * width * element_bytes * 2


traffic = [(0, 0)] * 64 + [(1, 1)] * 8
for placement in ((0, 1), (1, 0)):
    print("payload bytes", remote_bytes(traffic, placement, 4096, 2))
assert remote_bytes([(0, 0)] * 64, (1,), 4096, 2) == 1024 ** 2
# %%
def estimate_state(tokens, layers, attention_layers, kv_heads=4, head_dim=128, scalar_bytes=2,
                   recurrent_state_bytes=65536):
    kv = tokens * attention_layers * 2 * kv_heads * head_dim * scalar_bytes
    return kv + (layers - attention_layers) * recurrent_state_bytes


for tokens in (128, 4096, 32768):
    print(tokens, {count: estimate_state(tokens, 32, count) for count in (32, 8)})
assert estimate_state(0, 32, 8) == 24 * 65536
assert estimate_state(4096, 32, 8) < estimate_state(4096, 32, 32)
