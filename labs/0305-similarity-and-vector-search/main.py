"""Lab 3.5: Similarity and Vector Search"""

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = sum(x*x for x in a) ** 0.5
    nb = sum(y*y for y in b) ** 0.5
    return dot / (na * nb + 1e-9)
q = [0.2, 0.9, 0.1]
docs = {"leave": [0.3, 0.8, 0.0], "expense": [0.9, 0.1, 0.2]}
ranked = sorted(((k, cosine(q, v)) for k, v in docs.items()), key=lambda x: -x[1])
print("dense ranking:", ranked)
