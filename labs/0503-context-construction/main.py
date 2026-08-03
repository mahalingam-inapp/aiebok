"""Lab 5.3: Context Construction"""

BUDGET = 100
sections = [("system", 30, 1), ("auth", 20, 1), ("evidence", 80, 2), ("user", 40, 3)]
sections.sort(key=lambda x: x[2])
used = 0
packed = []
for name, tokens, _prio in sections:
    allow = min(tokens, BUDGET - used)
    if allow <= 0:
        packed.append((name, "TRUNCATED"))
    else:
        packed.append((name, allow))
        used += allow
print({"budget": BUDGET, "packed": packed, "used": used})
