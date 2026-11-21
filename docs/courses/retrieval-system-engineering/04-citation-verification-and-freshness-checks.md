# Citation verification and freshness checks

<p class="study-position" data-course="retrieval-system-engineering" data-lecture="04-citation-verification-and-freshness-checks.md">Fuse, rank and verify · Lecture 4 of 4</p>

[← Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Ingest and index evidence**

    - [Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md)
    - [Lexical retrieval and dense similarity](02-lexical-retrieval-and-dense-similarity.md)

    **Fuse, rank and verify**

    - [Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md)
    - **Citation verification and freshness checks** (current)

## What you will learn

Allow citations only to eligible retrieved evidence and abstain when evidence is incomplete.

## Check eligibility again when the citation is shown

A cached answer correctly quotes a passage that is now expired. The current index excludes it, but the answer still displays an old source ID.

Bind cached responses to relevant policy, audience, and revision state or revalidate before reuse. Test stale and denied citations along with a supported quote. An honest abstention is preferable when authoritative evidence is missing.

## How it works

Validate source IDs against the passages the response received and verify the supporting text. Treat a stale revision as unavailable even if it was present in a prior cached result. Reevaluate after indexes or access policies change.

### Verify the citation at the boundary where it is used

A citation should point to an eligible source version and support the exact claim. Check that the identifier belongs to the passages made available to the model. Then inspect whether the relevant passage supports the stated amount, date, and exception. The same document title can refer to different content over time.

Update tests when evidence changes. If a result was cached while a source was current, it can outlast the source's permissions or effective date. Bind the cache to scope and revision, or revalidate before returning the answer. Give missing and contradictory evidence distinct outcomes callers can understand.

Try one answer with a correct amount and an incorrect source. Try another with a correct source but an unsupported exception. A useful validator catches both. When evidence remains incomplete, return an explicit handoff. That fallback preserves trust better than presenting a citation that a reviewer cannot reproduce.

## Worked example

A candidate quotes an old leave policy accurately. The citation is still invalid when that revision is no longer eligible.

## Try it yourself

Run the freshness and citation fixtures. Add a case where a restricted source has the best lexical match.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    The restricted source is filtered before both rankings, and the grounded-answer stage uses only retrieved, currently eligible evidence.

## Continue

[← Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
