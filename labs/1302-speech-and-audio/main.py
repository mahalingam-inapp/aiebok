"""Lab 13.2: Speech and Audio"""

CHAPTER = "13.2"
print("chapter hook:", CHAPTER)
segments = [
    {"start": 0.0, "end": 2.5, "speaker": "HR", "text": "welcome", "conf": 0.95},
    {"start": 2.5, "end": 4.0, "speaker": "?", "text": "mumbled", "conf": 0.55},
]
for s in segments:
    flag = s["conf"] < 0.75
    print(s, "review:", flag)
print("---")
print("change one input above, predict output, re-run")
