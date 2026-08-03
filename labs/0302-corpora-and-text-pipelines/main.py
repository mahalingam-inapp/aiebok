"""Lab 3.2: Corpora and Text Pipelines"""

CHAPTER = "3.2"
print("chapter hook:", CHAPTER)
import unicodedata
samples = ["café", "caf\u0301", "PT\u200bO policy"]
for s in samples:
    nfc = unicodedata.normalize("NFC", s)
    print({"raw": repr(s), "nfc": repr(nfc), "len": len(s), "nfc_len": len(nfc)})
print("---")
print("change one input above, predict output, re-run")
