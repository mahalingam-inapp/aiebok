"""Lab 11.3: Dataset Engineering"""

CHAPTER = "11.3"
print("chapter hook:", CHAPTER)
train = {"case-101", "case-102", "case-103"}
eval = {"case-103", "case-200"}
leak = train & eval
print({"leaked_ids": sorted(leak)})
print("---")
print("change one input above, predict output, re-run")
