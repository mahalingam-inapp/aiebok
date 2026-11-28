# Map a customer data contract

<p class="study-position" data-course="customer-pilot-engineering" data-lecture="02-map-a-customer-data-contract.md">Discover and integrate · Lecture 2 of 4</p>

[← Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md) · [Course outline](index.md#course-outline){ .study-overview } · [Shadow acceptance and integration failures →](03-shadow-acceptance-and-integration-failures.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Discover and integrate**

    - [Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md)
    - **Map a customer data contract** (current)

    **Evaluate and hand off**

    - [Shadow acceptance and integration failures](03-shadow-acceptance-and-integration-failures.md)
    - [Rollout, operator handoff and stop rules](04-rollout-operator-handoff-and-stop-rules.md)

## What you will learn

Normalize a source payload and publish a versioned integration boundary.

## Keep source identity when you normalize fields

The upstream form sends an old category value and the same ticket can arrive twice. A malformed record should not silently enter a general queue.

Validate schema version and expected types at intake. Preserve source identity so staff can resolve errors. Route unknown categories to an explicit review state instead of assuming a default.

## How it works

Map external fields to internal types and preserve provenance. Reject incomplete records before calling a downstream dependency. Agree who owns the upstream schema and define the service behavior if an unexpected version arrives.

### Keep a record recognizable after normalization

An adapter maps between the customer's data and the application's contract. Validate the upstream schema version and required fields, then preserve identifiers and timestamps. People need these details to find the original ticket when a candidate route looks wrong or a record is delivered twice.

Handle three inputs separately. A known category maps to an allowed internal value. An unknown category becomes an explicit review item. An invalid value is rejected with a reason and, where permitted, a reference to the original record. Using a broad default for all three loses evidence about what happened.

Version the mapping and exercise a boundary case before deploying it. Ask the upstream owner how a schema or category changes are advertised. A customer can make a sensible update in their system and still break your assumptions. Give the operator a way to detect, pause, and recover from that mismatch.

## Worked example

A partner sends a customer ticket ID, topic, and audience flag. Normalize known topics and route any unrecognized topic to review.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
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
```

## Try it yourself

Run the adapter for the bundled records. Add a case for a field with the wrong type.

[Download the workbook](../../assets/notebooks/customer-pilot-engineering.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Treat the malformed input as a rejected record. Leave the original source identifier available for support.

## Continue

[← Discovery and pilot acceptance](01-discovery-and-pilot-acceptance.md) · [Course outline](index.md#course-outline){ .study-overview } · [Shadow acceptance and integration failures →](03-shadow-acceptance-and-integration-failures.md)
{: .study-directions .study-directions--footer }
