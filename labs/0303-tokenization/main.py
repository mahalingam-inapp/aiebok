"""Lab 3.3: Tokenization"""

corpus = "PTO PTO accrual XR-9000 XR-9000 policy"
words = corpus.split()
pairs = {}
for w in words:
    for i in range(len(w)-1):
        p = w[i:i+2]
        pairs[p] = pairs.get(p, 0) + 1
merge = max(pairs, key=pairs.get)
print("most frequent pair:", merge, "count:", pairs[merge])
print("word token count:", len(words))
