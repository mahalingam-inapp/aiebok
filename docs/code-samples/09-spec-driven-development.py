"""Turn acceptance examples into an executable contract.

Spec-driven discipline: write CASES before changing assistant() logic.
Tooling: see docs/getting-started/spec-driven-workflow.md for OpenSpec and Cursor workflows.
Run: python docs/code-samples/09-spec-driven-development.py
"""
SPEC = [
    {"input": "Known answer", "evidence": ["Known answer"], "must_contain": "Known answer"},
    {"input": "Unknown", "evidence": [], "must_contain": "insufficient evidence"},
]


def assistant(case):
    if not case["evidence"]:
        return "insufficient evidence"
    return case["evidence"][0]


failures = []
for case in SPEC:
    actual = assistant(case)
    passed = case["must_contain"].lower() in actual.lower()
    print("PASS" if passed else "FAIL", case["input"], "->", actual)
    if not passed:
        failures.append(case)
raise SystemExit(1 if failures else 0)
