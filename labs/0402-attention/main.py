"""Lab 4.2: Attention"""

import math
q = [1.0, 0.0]
keys = [[0.9, 0.1], [0.0, 1.0], [0.9, 0.1]]
def scaled_dot(q, k, scale):
    return sum(a*b for a, b in zip(q, k)) / scale
scale = math.sqrt(len(q))
scores = [scaled_dot(q, k, scale) for k in keys]
m = max(scores)
weights = [math.exp(s-m) for s in scores]
Z = sum(weights)
weights = [w/Z for w in weights]
print("weights:", [round(w, 3) for w in weights])
