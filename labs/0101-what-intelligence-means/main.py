"""Lab 1.1: What Intelligence Means"""

GOAL = "route P1 incidents to on-call"
CAPABILITIES = ["perceive", "represent", "decide", "act"]
ticket = "All regions down — writes failing"
features = set(ticket.lower().split())
severity = "P1" if {"down", "failing"} & features else "P2"
trace = {cap: cap for cap in CAPABILITIES}
trace["represent"] = sorted(features)
trace["decide"] = severity
print({"goal": GOAL, "trace": trace})
