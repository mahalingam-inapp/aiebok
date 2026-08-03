"""Lab 11.2: Post-Training Methods"""

CHAPTER = "11.2"
print("chapter hook:", CHAPTER)
methods = {"prompt": 0.82, "SFT": 0.91, "DPO": 0.93}
cost = {"prompt": 1, "SFT": 4, "DPO": 6}
target = 0.90
choice = min((m for m, s in methods.items() if s >= target), key=lambda m: cost[m])
print({"method": choice, "score": methods[choice]})
print("---")
print("change one input above, predict output, re-run")
