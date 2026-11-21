from statistics import median

baseline_minutes = (10, 11, 12, 13, 15)
median_target = median(baseline_minutes) * 0.75
assert median_target == 9
print("Median baseline and acceptance target", median(baseline_minutes), median_target)

# %%
from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    source_id: str
    topic: str
    restricted: bool


def normalize(payload):
    if payload.get("schema") != "facilities-v1":
        raise ValueError("unsupported schema")
    source = payload.get("ticket")
    topic = payload.get("queue")
    restricted = payload.get("restricted")
    if not isinstance(source, str) or not source.strip() or not isinstance(topic, str) or type(restricted) is not bool:
        raise ValueError("invalid ticket fields")
    return Ticket(source.strip(), topic.strip().lower(), restricted)


inputs = [
    {"schema": "facilities-v1", "ticket": "F1", "queue": " Heating ", "restricted": False},
    {"schema": "facilities-v1", "ticket": "F2", "queue": "heating", "restricted": True},
    {"schema": "facilities-v1", "ticket": "F3", "queue": "other", "restricted": False},
]
tickets = [normalize(row) for row in inputs]
assert tickets[0] == Ticket("F1", "heating", False)
try:
    normalize(inputs[0] | {"restricted": "false"})
except ValueError as error:
    print("Rejected malformed request", error)
else:
    raise AssertionError("wrong field type was accepted")

# %%
class Intake:
    def __init__(self):
        self.records = {}

    def shadow(self, ticket, lookup):
        saved = self.records.get(ticket.source_id)
        if saved:
            if saved[0] != ticket:
                raise ValueError("source ID reused with different inputs")
            return saved[1]
        try:
            route = lookup(ticket.topic) if not ticket.restricted else None
        except TimeoutError:
            return "retry_manual"
        result = route or "review"
        self.records[ticket.source_id] = (ticket, result)
        return result


def lookup(topic):
    return {"heating": "building-services"}.get(topic)


def unavailable(topic):
    raise TimeoutError("directory did not respond")


intake = Intake()
assert intake.shadow(tickets[0], unavailable) == "retry_manual"
assert "F1" not in intake.records
assert [intake.shadow(ticket, lookup) for ticket in tickets] == ["building-services", "review", "review"]
assert intake.shadow(tickets[0], unavailable) == "building-services"
assert len(intake.records) == 3

# %%
def decide(observed_times, restricted_case_ok, completed_smoke_test):
    return (
        len(observed_times) >= len(baseline_minutes)
        and median(observed_times) <= median_target
        and restricted_case_ok
        and completed_smoke_test
    )


pilot_minutes = (6, 7, 8, 9, 11)
assert decide(pilot_minutes, True, True)
assert not decide(pilot_minutes, False, True)
assert not decide(pilot_minutes[:2], True, True)
print({
    "pilot_cohort": "simulated facilities intake",
    "cases": len(pilot_minutes),
    "median_minutes": median(pilot_minutes),
    "recommendation": "bounded pilot",
    "operator_owner": "facilities shift lead",
    "stop_rule": "route any restricted case manually and pause automation",
    "smoke_case": {"input_id": "F2", "expected": "review"},
})
