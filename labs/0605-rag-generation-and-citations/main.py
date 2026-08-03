"""Lab 6.5: RAG Generation and Citations"""

CHAPTER = "6.5"
print("chapter hook:", CHAPTER)
claim = "PTO cap is 300 hours"
source = "PTO accrual cap is 240 hours"
claim_tokens = set(claim.lower().split())
source_tokens = set(source.lower().split())
overlap = len(claim_tokens & source_tokens) / len(claim_tokens)
print({"overlap": round(overlap, 2), "supported": "240" in source and "240" in claim})
print("---")
print("change one input above, predict output, re-run")
