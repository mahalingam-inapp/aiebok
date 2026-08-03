"""Lab 9.3: AI-Native Development Workflow"""

CHAPTER = "9.3"
print("chapter hook:", CHAPTER)
REPO_RULES = ["run tests before commit", "use internal SDK docs", "no new deps without ADR"]
task = "add checkpoint resume"
checklist = [rule for rule in REPO_RULES]
print({"task": task, "agent_checklist": checklist})
print("---")
print("change one input above, predict output, re-run")
