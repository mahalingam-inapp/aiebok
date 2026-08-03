"""Lab 13.6: How to Track the Frontier"""

assessment = {
    "claim": "new agent framework 2x faster",
    "evidence": "vendor blog",
    "reproduced": False,
    "confidence": "low",
}
action = "monitor" if assessment["confidence"] == "low" else "pilot"
print({"action": action, **assessment})
