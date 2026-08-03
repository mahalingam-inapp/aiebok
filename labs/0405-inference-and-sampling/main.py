"""Lab 4.5: Inference and Sampling"""

import random
logits = [2.0, 1.0, 0.5, 0.1]
def sample_temp(logits, temp=1.0):
    scaled = [l/temp for l in logits]
    m = max(scaled)
    ex = [math.exp(l-m) for l in scaled]
    s = sum(ex)
    probs = [e/s for e in ex]
    r = random.random()
    c = 0
    for i, p in enumerate(probs):
        c += p
        if r <= c:
            return i, probs
    return len(probs)-1, probs
import math
idx, probs = sample_temp(logits, temp=0.8)
print({"sampled_index": idx, "probs": [round(p, 3) for p in probs]})
