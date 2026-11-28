# Model interfaces and structured output

<p class="study-position" data-course="model-backed-applications" data-lecture="01-model-interfaces-and-structured-output.md">Implement the contract and baseline · Lecture 1 of 4</p>

[Course outline](index.md#course-outline){ .study-overview } · [Retrieval, evidence and citations →](02-retrieval-evidence-and-citations.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Implement the contract and baseline**

    - **Model interfaces and structured output** (current)
    - [Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md)

    **Measure and integrate**

    - [Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md)
    - [Compare a live provider with a local baseline](04-compare-a-live-provider-with-a-local-baseline.md)

## What you will learn

Validate a model response and distinguish response-format errors from provider failures.

## Read a reply as a contract

One provider returns prose where the app expects a structured reply. Another returns the right format with an unsupported decision.

Validate shape before consuming the response. Then validate what the response claims separately. A timeout and a malformed reply can both fall back safely while retaining different diagnostic reasons.

## How it works

Define a small typed contract before choosing a model. Treat a response as untrusted input and validate each required field, value, and relationship. A malformed JSON reply and a provider timeout should both activate the fallback while remaining distinguishable in logs. Keep provider-specific code behind one callable.

### Classify failures at the application boundary

Wrap the provider behind a contract that names the inputs, allowed outputs, and failure behavior. A timeout means the call did not finish in time. Invalid JSON means its response could not be parsed. A valid response with a source outside the supplied evidence means it violated a separate grounding condition. If all three are logged as “model error,” the person on call cannot tell which layer to fix.

Validate locally before using an output. A typed schema can require an allowed status and a list of citations. Then check that the status makes sense for the presence of evidence. An answer can pass both checks and still make an unsupported statement, so verify claims separately.

All three failures can give the user a safe fallback while retaining distinct operational reasons. Use the notebook to induce each failure independently. The same user-facing message can be correct in more than one case, as long as the report preserves which check fired.

## Worked example

A service desk assistant returns a status, a short answer, and source IDs. A reply with source_ids set to a string cannot satisfy the contract. A valid abstention has an empty answer and no sources.

## Follow the code

Run this cell in Python 3.10 or later. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Reply:
    status: str
    answer: str
    sources: tuple[str, ...]


ABSTAIN = Reply("abstain", "", ())


def parse_reply(raw):
    value = json.loads(raw)
    if not isinstance(value, dict) or set(value) != {"status", "answer", "sources"}:
        raise ValueError("unexpected fields")
    status, answer, sources = value["status"], value["answer"], value["sources"]
    if not isinstance(answer, str) or not isinstance(sources, list):
        raise ValueError("invalid field types")
    if any(not isinstance(source, str) or not source for source in sources):
        raise ValueError("invalid source ID")
    reply = Reply(status, answer, tuple(sources))
    if reply != ABSTAIN and not (status == "answer" and answer.strip() and sources):
        raise ValueError("inconsistent response")
    return reply


assert parse_reply('{"status":"abstain","answer":"","sources":[]}') == ABSTAIN
for invalid in ('{"status":"answer","answer":"x","sources":"p1"}', '[]', 'not JSON'):
    try:
        parse_reply(invalid)
    except ValueError:
        continue
    raise AssertionError(f"Accepted invalid reply {invalid}")
```

## Try it yourself

Run the contract cases. Add a syntactically valid response with an unknown status and explain why JSON parsing alone accepts it.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 01** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Reject the status during semantic validation and test that the handler returns the same public fallback without losing the failure category internally.

## Continue

[Course outline](index.md#course-outline){ .study-overview } · [Retrieval, evidence and citations →](02-retrieval-evidence-and-citations.md)
{: .study-directions .study-directions--footer }
