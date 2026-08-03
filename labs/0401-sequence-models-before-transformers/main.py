"""Lab 4.1: Sequence Models Before Transformers"""

CHAPTER = "4.1"
print("chapter hook:", CHAPTER)
from collections import Counter
text = "region east failover region west failover"
n = 3
grams = Counter(tuple(text.split()[i:i+n]) for i in range(len(text.split())-n+1))
context = ("region", "east")
candidates = [g[-1] for g in grams if g[:2] == context]
print({"context": context, "next_token_candidates": candidates})
print("---")
print("change one input above, predict output, re-run")
