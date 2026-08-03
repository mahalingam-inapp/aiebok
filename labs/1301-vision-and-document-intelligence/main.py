"""Lab 13.1: Vision and Document Intelligence"""

CHAPTER = "13.1"
print("chapter hook:", CHAPTER)
blocks = [
    {"type": "table", "text": "PTO cap 240", "page": 3, "confidence": 0.96},
    {"type": "chart", "text": "headcount trend", "page": 4, "confidence": 0.71},
]
THRESH = 0.85
for b in blocks:
    print(b["type"], "auto_extract:", b["confidence"] >= THRESH)
print("---")
print("change one input above, predict output, re-run")
