"""Lab 2.3: Unsupervised and Representation Learning"""

import math
docs = {"payroll": "salary direct deposit batch", "retail": "card swipe retail purchase"}
words = sorted(set(w for d in docs.values() for w in d.split()))
def vec(doc):
    counts = {w: doc.split().count(w) for w in words}
    df = {w: sum(w in d.split() for d in docs.values()) for w in words}
    n = len(docs)
    return {w: counts[w] * math.log(n / df[w]) for w in words}
va, vb = vec(docs["payroll"]), vec(docs["retail"])
dot = sum(va[w]*vb[w] for w in words)
print("payroll vs retail dot:", round(dot, 3))
