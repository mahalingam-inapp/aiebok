def current_title(value):
    return value.strip().lower() or "untitled"


CASES = (
    (" Study PLAN ", "study plan"),
    ("", "untitled"),
    ("draft\t  release   plan", "draft release plan"),
)


def regressions(formatter):
    failures = []
    for value, expected in CASES:
        actual = formatter(value)
        if actual != expected:
            failures.append({"input": value, "expected": expected, "actual": actual})
    return failures


assert len(regressions(current_title)) == 1

# %%
from dataclasses import dataclass


def proposed_title(value):
    return " ".join(value.lower().split()) or "untitled"


CANDIDATES = {"current": current_title, "collapse-spaces": proposed_title}


@dataclass(frozen=True)
class Review:
    candidate: str
    revision: int
    failures: tuple
    approved: bool = False


def evaluate(proposal, revision):
    if (
        not isinstance(proposal, dict) or set(proposal) != {"action", "candidate"}
        or proposal["action"] != "update-formatter" or not isinstance(proposal["candidate"], str)
        or proposal["candidate"] not in CANDIDATES
    ):
        raise ValueError("proposal outside the allowed contract")
    candidate = proposal["candidate"]
    return Review(candidate, revision, tuple(regressions(CANDIDATES[candidate])))


proposal = {"action": "update-formatter", "candidate": "collapse-spaces"}
assert evaluate(proposal, 1).failures == ()
assert evaluate(proposal | {"candidate": "current"}, 1).failures
try:
    evaluate(proposal | {"action": "unregistered-action"}, 1)
except ValueError:
    pass
else:
    raise AssertionError("unknown action accepted")

# %%
from dataclasses import replace


class FormatterStore:
    def __init__(self):
        self.revision = 1
        self.candidate = "current"
        self.records = {}

    def apply(self, request_id, review):
        if request_id in self.records:
            recorded, revision = self.records[request_id]
            if recorded != review:
                raise ValueError("request ID reused with a different review")
            return "replayed", revision
        if review.revision != self.revision:
            return "stale", self.revision
        if review.failures:
            return "failed_checks", self.revision
        if not review.approved:
            return "awaiting_review", self.revision
        self.candidate = review.candidate
        self.revision += 1
        self.records[request_id] = review, self.revision
        return "applied", self.revision


store = FormatterStore()
review = evaluate(proposal, store.revision)
assert store.apply("change-1", review) == ("awaiting_review", 1)
approved = replace(review, approved=True)
assert store.apply("change-1", approved) == ("applied", 2)
assert store.apply("change-1", approved) == ("replayed", 2)
assert store.apply("change-2", approved) == ("stale", 2)
assert store.candidate == "collapse-spaces"

# %%
trace = []
scenario = FormatterStore()
for request_id, candidate_id, approve in (
    ("invalid-regression", "current", True),
    ("valid-change", "collapse-spaces", False),
    ("valid-change", "collapse-spaces", True),
):
    reviewed = replace(evaluate(proposal | {"candidate": candidate_id}, scenario.revision), approved=approve)
    outcome, revision = scenario.apply(request_id, reviewed)
    trace.append({
        "request": request_id, "candidate": candidate_id, "reviewed_revision": reviewed.revision,
        "test_failures": reviewed.failures, "decision": outcome, "resulting_revision": revision,
    })
assert [entry["decision"] for entry in trace] == ["failed_checks", "awaiting_review", "applied"]
for decision in trace:
    print(decision)
