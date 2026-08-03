"""Lab 5.2: Structured Generation"""

schema = {"type": "object", "required": ["total"], "properties": {"total": {"type": "number"}}}
payloads = [{"total": 12.5}, {"total": "12.50"}, {"total": 12.5, "note": "'; DROP TABLE--"}]
def validate(p):
    if not isinstance(p.get("total"), (int, float)):
        return False, "total must be numeric"
    return True, "ok"
for p in payloads:
    ok, msg = validate(p)
    print({"payload": p, "valid": ok, "msg": msg})
