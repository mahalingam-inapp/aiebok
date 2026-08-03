"""Lab 9.2: Specification-Driven Development"""

acceptance = [
    {"input": "grant admin access", "expect": "require approval"},
    {"input": "unknown policy", "expect": "abstain"},
]
def check(outcome, expected):
    return expected in outcome
for case in acceptance:
    simulated = "abstain: no policy found" if "unknown" in case["input"] else "require approval"
    print(case["input"], check(simulated, case["expect"]))
