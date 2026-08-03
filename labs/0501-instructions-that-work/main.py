"""Lab 5.1: Instructions That Work"""

WEAK = "You are a helpful HR assistant."
STRONG = """Role: HR policy assistant.
Task: Answer using provided policy excerpts only.
Constraints: Cite policy_id or reply ABSTAIN.
Example:
User: PTO cap?
Assistant: {"policy_id":"L-12","answer":"240 hours"}"""
for name, prompt in [("weak", WEAK), ("strong", STRONG)]:
    print(name, "chars:", len(prompt), "has_abstain:", "ABSTAIN" in prompt)
