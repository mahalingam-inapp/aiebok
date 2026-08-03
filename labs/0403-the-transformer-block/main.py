"""Lab 4.3: The Transformer Block"""

seq, dim, heads = 4, 8, 2
assert dim % heads == 0
head_dim = dim // heads
x = [[0.1 * (i+j) for j in range(dim)] for i in range(seq)]
def layer_norm(row):
    mu = sum(row) / len(row)
    var = sum((v-mu)**2 for v in row) / len(row)
    return [(v-mu)/(var+1e-5)**0.5 for v in row]
out = [layer_norm(row) for row in x]
print({"seq": seq, "dim": dim, "head_dim": head_dim, "row0_norm_mean": round(sum(out[0])/len(out[0]), 3)})
