"""Lab 10.2: Metrics and Human Judgment"""

CHAPTER = "10.2"
print("chapter hook:", CHAPTER)
human = [1, 0, 1, 1]
judge = [1, 1, 1, 0]
agree = sum(h == j for h, j in zip(human, judge)) / len(human)
print({"agreement": round(agree, 2)})
print("---")
print("change one input above, predict output, re-run")
