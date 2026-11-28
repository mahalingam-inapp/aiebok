# Retrieval, evidence and citations

<p class="study-position" data-course="model-backed-applications" data-lecture="02-retrieval-evidence-and-citations.md">Implement the contract and baseline · Lecture 2 of 4</p>

[← Model interfaces and structured output](01-model-interfaces-and-structured-output.md) · [Course outline](index.md#course-outline){ .study-overview } · [Grounding checks and evaluation slices →](03-grounding-checks-and-evaluation-slices.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Implement the contract and baseline**

    - [Model interfaces and structured output](01-model-interfaces-and-structured-output.md)
    - **Retrieval, evidence and citations** (current)

    **Measure and integrate**

    - [Grounding checks and evaluation slices](03-grounding-checks-and-evaluation-slices.md)
    - [Compare a live provider with a local baseline](04-compare-a-live-provider-with-a-local-baseline.md)

## What you will learn

Build a retrieval baseline, measure top-k recall, and enforce evidence scope before ranking.

## Retrieve only evidence the requester can see

A reviewer can see a private payroll policy. A normal employee asks the same question and deserves a public answer or a clear handoff.

Filter evidence by role before ranking and validate each citation against material actually available to the response. Test both roles using the same question so a retrieval success never excuses a permission failure.

## How it works

Start with lexical retrieval over passages with stable IDs and explicit roles. Filter relevance candidates by permission before scoring, then check that model citations refer to the actual retrieved snippets. ID validation catches fabricated citations. Checking the answer against the passage is a separate step.

### Trace an evidence item end to end

A retrieval pipeline starts with authorized documents, splits and indexes them, ranks candidates, and passes selected passages to the model. Preserve a stable source identifier from the index to the answer. A title alone is not enough when a policy has multiple revisions or sections that make different promises.

For a given question, evaluate whether an authorized relevant passage reached the candidate set before inspecting the final output. A missing passage is a retrieval problem. A passage that arrived but lost its exception during assembly is a context problem. A contradiction of the supplied passage is an answer problem. The same final symptom can have three different fixes.

Test the same input for two roles. Remove any restricted passages before ranking and verify that returned citation identifiers refer to the evidence actually supplied. If the ordinary user has insufficient evidence, an explicit handoff is a successful application outcome.

## Worked example

A travel-policy question may retrieve a correct current article and an unrelated reimbursement rule. Source IDs let you compare rankings against labeled expectations and inspect why the current article was missed.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
import re


@dataclass(frozen=True)
class Passage:
    id: str
    text: str
    roles: frozenset[str]


CORPUS = (
    Passage("travel", "File a travel receipt within 15 days.", frozenset({"employee", "reviewer"})),
    Passage("payroll", "Review payroll adjustments on Tuesday.", frozenset({"reviewer"})),
    Passage("room", "Reserve a meeting room through the calendar.", frozenset({"employee", "reviewer"})),
)
STOP = {"a", "an", "do", "i", "how", "the", "should", "when", "where", "what", "on", "for", "through"}


def tokens(text):
    return set(re.findall(r"[a-z]+", text.lower())) - STOP


def retrieve(question, role, limit=2):
    query = tokens(question)
    eligible = (passage for passage in CORPUS if role in passage.roles)
    ranked = sorted(
        ((len(query & tokens(p.text)), p.id, p) for p in eligible),
        key=lambda row: (-row[0], row[1]),
    )
    return [passage for score, _, passage in ranked[:limit] if score > 0]


assert [p.id for p in retrieve("When should I file a travel receipt?", "employee")] == ["travel"]
assert [p.id for p in retrieve("When are payroll adjustments reviewed?", "reviewer")] == ["payroll"]
assert retrieve("When are payroll adjustments reviewed?", "employee") == []
```

## Try it yourself

Compare the results for an employee and a policy reviewer. Add a query with no answer in the allowed documents.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The employee never sees reviewer-only passages. The no-answer case returns no citations, even if the question is phrased fluently.

## Continue

[← Model interfaces and structured output](01-model-interfaces-and-structured-output.md) · [Course outline](index.md#course-outline){ .study-overview } · [Grounding checks and evaluation slices →](03-grounding-checks-and-evaluation-slices.md)
{: .study-directions .study-directions--footer }
