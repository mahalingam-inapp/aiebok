# Grounding checks and evaluation slices

<p class="study-position" data-course="model-backed-applications" data-lecture="03-grounding-checks-and-evaluation-slices.md">Measure and integrate · Lecture 3 of 4</p>

[← Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md) · [Course outline](index.md#course-outline){ .study-overview } · [Compare a live provider with a local baseline →](04-compare-a-live-provider-with-a-local-baseline.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Implement the contract and baseline**

    - [Model interfaces and structured output](01-model-interfaces-and-structured-output.md)
    - [Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md)

    **Measure and integrate**

    - **Grounding checks and evaluation slices** (current)
    - [Compare a live provider with a local baseline](04-compare-a-live-provider-with-a-local-baseline.md)

## What you will learn

Run fixed cases through a baseline and candidate and attribute errors by stage.

## Track the point where the answer went wrong

The right paragraph is in the retrieved set, but the assistant cites a source it never saw. Overall accuracy does not tell Mei which fix is needed.

Separate candidate recall, citation validity, and final behavior. Keep the same cases for each model and record a distinct abstention reason. That makes it possible to improve a prompt without masking a retrieval regression.

## How it works

Keep a frozen set of inputs with expected outcomes and evidence. Evaluate retrieval, citation support, and final decisions separately. Report per-slice counts so a class of failure cannot disappear in aggregate accuracy. Exact-match excerpts are a conservative support check for this exercise. Evaluate paraphrases with a human rubric before accepting them.

### Preserve failure categories in the score

For each evaluation case, record the expected behavior before running the candidate. Use separate indicators for retrieval recall, citation validity, and whether the response met the request. You may also need an explicit category for a correct abstention, where the expected answer is to request more information or route to staff.

Consider 20 cases. The right evidence was retrieved in 18, but only 15 answers met their criteria. Two cases could not support a response. Five final failures should not automatically send you to the retrieval layer. Join the failed cases to their retrieval records and inspect whether evidence was lost in assembly or never used by the answer.

Keep the same fixtures when comparing configuration changes. Report the counts for critical slices with the aggregate. Include cost and latency for attempted cases, as failed calls still consume resources. This turns the score into an explanation of where work should go next.

## Worked example

A candidate may retrieve the right policy yet cite an unavailable ID. That case passes retrieval but fails answer validation. A fallback preserves safety while still costing task completion.

## Try it yourself

Run both providers on the same cases and identify one case where retrieval succeeds but the provider reply fails its contract.

[Download the workbook](../../assets/notebooks/model-backed-applications.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Keep the retrieval denominator restricted to answerable cases. Keep abstentions and invalid responses in the decision and fallback reports with their own counts.

## Continue

[← Retrieval, evidence and citations](02-retrieval-evidence-and-citations.md) · [Course outline](index.md#course-outline){ .study-overview } · [Compare a live provider with a local baseline →](04-compare-a-live-provider-with-a-local-baseline.md)
{: .study-directions .study-directions--footer }
