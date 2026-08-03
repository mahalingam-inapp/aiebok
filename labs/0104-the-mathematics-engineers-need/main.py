"""Lab 1.4: The Mathematics Engineers Need"""

import math
a = [3.0, 0.0, 1.0]
b = [2.0, 0.0, 2.0]
def cosine(u, v):
    dot = sum(x*y for x, y in zip(u, v))
    nu = math.sqrt(sum(x*x for x in u))
    nv = math.sqrt(sum(y*y for y in v))
    return dot / (nu * nv)
def softmax(xs):
    m = max(xs)
    ex = [math.exp(x - m) for x in xs]
    s = sum(ex)
    return [e/s for e in ex]
sims = [cosine(a, b), cosine(a, a), cosine(b, b)]
print("cosines:", [round(c, 3) for c in sims])
print("softmax:", [round(p, 3) for p in softmax(sims)])
