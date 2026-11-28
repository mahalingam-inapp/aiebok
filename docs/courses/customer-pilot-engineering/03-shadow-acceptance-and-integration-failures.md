# Shadow acceptance and integration failures

<p class="study-position" data-course="customer-pilot-engineering" data-lecture="03-shadow-acceptance-and-integration-failures.md">Evaluate and hand off · Lecture 3 of 4</p>

[← Map a customer data contract](02-map-a-customer-data-contract.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollout, operator handoff and stop rules →](04-rollout-operator-handoff-and-stop-rules.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Discover and integrate**

    - [Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md)
    - [Map a customer data contract](02-map-a-customer-data-contract.md)

    **Evaluate and hand off**

    - **Shadow acceptance and integration failures** (current)
    - [Rollout, operator handoff and stop rules](04-rollout-operator-handoff-and-stop-rules.md)

## What you will learn

Exercise normal, ambiguous, restricted, and unavailable-dependency cases before live use.

## Shadow decisions while the old process still runs

During a rehearsal, the directory fails for a routine ticket and an unusual ticket arrives twice. The existing staff queue keeps moving.

Record candidate decisions without applying them. Compare against the staff route, retry recoverable failures, and test duplicate handling. This gives the customer useful acceptance evidence before changing the live process.

### Follow one work order through the rehearsal

In the existing workflow, the desk retains ownership until the shift lead sees a filed ticket. In the rehearsal, the adapter records a proposed route without changing that ownership.

| Event | Candidate record | What the shift lead should see |
|---|---|---|
| Routine ticket, directory available | Propose the expected queue | A candidate destination beside the desk’s route |
| Directory unavailable | Request needs manual handling or retry | The original ticket remains visible to the desk |
| Same ticket arrives again | Return the prior result for that ticket ID | No second work order |

Ask an operator to perform these steps using the workbook output as evidence. They should be able to tell whether the pilot acted, whether staff still own the ticket, and when they need to do something. A green automated assertion can confirm a route; the rehearsal checks whether the customer can safely run the process.

## How it works

A shadow run records proposed actions while the original workflow retains control. Test the same inputs for both workflows and compare decisions and timing. Make failures easy to retry without duplicating the outcome.

### Compare decisions without changing operational ownership

In a shadow trial, the candidate produces proposed outputs while the original workflow retains control. Run both against the same ticket inputs and compare the observable result. A difference is a reason to inspect the case, not automatic proof that the candidate is wrong. The existing route can contain errors too.

Include a temporary directory failure, an uncertain category, and a repeated ticket. On failure, staff should still be able to find the original work. On replay, the candidate should refer to the existing record. When routing is uncertain, the system should describe the review state rather than claiming automatic success.

Ask the shift lead to walk through the evidence in order. Can they see who owns the ticket right now? Would the proposal improve triage? What would happen after disconnecting the service? These operational checks complement accuracy and help the customer decide when it is safe to introduce a live effect.

## Worked example

When the routing dependency is unavailable, leave the ticket in manual triage. If an accepted request is delivered twice, return the existing route.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
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
```

## Try it yourself

Compare the deterministic acceptance results. Add a replay for a successful request and a retry after dependency recovery.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The successful replay returns the same result and creates one record. A transient failure leaves room for a successful retry.

## Continue

[← Map a customer data contract](02-map-a-customer-data-contract.md) · [Course outline](index.md#course-outline){ .study-overview } · [Rollout, operator handoff and stop rules →](04-rollout-operator-handoff-and-stop-rules.md)
{: .study-directions .study-directions--footer }
