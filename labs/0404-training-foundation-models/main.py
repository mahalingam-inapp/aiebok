"""Lab 4.4: Training Foundation Models"""

CHAPTER = "4.4"
print("chapter hook:", CHAPTER)
tokens, params, epochs, batch = 10_000_000, 50_000_000, 1, 32
steps = tokens // (batch * 512)
ratio = tokens / params
print({"train_steps_approx": steps, "tokens_per_param": round(ratio, 2)})
print("note: pretrain learns distributions, not a queryable policy DB")
print("---")
print("change one input above, predict output, re-run")
