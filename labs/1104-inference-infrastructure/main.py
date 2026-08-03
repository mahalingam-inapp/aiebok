"""Lab 11.4: Inference Infrastructure"""

CHAPTER = "11.4"
print("chapter hook:", CHAPTER)
batch_sizes = [1, 4, 8]
for b in batch_sizes:
    throughput = b / (1 + 0.1 * (b - 1))
    print(f"batch={b} relative_throughput={throughput:.2f}")
print("---")
print("change one input above, predict output, re-run")
