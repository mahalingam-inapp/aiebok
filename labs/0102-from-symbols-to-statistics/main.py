"""Lab 1.2: From Symbols to Statistics"""

RULES = [("urgent", "P1"), ("question", "P3")]
tickets = [
    "URGENT: payment gateway offline",
    "urgent feature request for dashboard",
    "question about invoice format",
]
def rule_route(text):
    lower = text.lower()
    for kw, sev in RULES:
        if kw in lower:
            return sev
    return "P2"
for t in tickets:
    print({"ticket": t[:40], "route": rule_route(t)})
