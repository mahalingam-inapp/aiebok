# Lexical retrieval and dense similarity

<p class="study-position" data-course="retrieval-system-engineering" data-lecture="02-lexical-retrieval-and-dense-similarity.md">Ingest and index evidence · Lecture 2 of 4</p>

[← Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md) · [Course outline](index.md#course-outline){ .study-overview } · [Hybrid fusion and relevance diagnostics →](03-hybrid-fusion-and-relevance-diagnostics.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Ingest and index evidence**

    - [Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md)
    - **Lexical retrieval and dense similarity** (current)

    **Fuse, rank and verify**

    - [Hybrid fusion and relevance diagnostics](03-hybrid-fusion-and-relevance-diagnostics.md)
    - [Citation verification and freshness checks](04-citation-verification-and-freshness-checks.md)

## What you will learn

Compare keyword ranking with a small dense semantic representation.

## When synonyms help and identifiers hurt

A user alternates between ‘holiday’ and ‘annual leave’ while another asks for a form identified only by a code.

Use the same query labels for lexical and dense methods. Semantic closeness can help synonyms and still fail exact references. Report those slices separately before choosing a hybrid.

## How it works

Lexical matching rewards shared terms and can miss synonyms. Dense vectors represent related meanings as nearby points. The lab uses manually constructed low-dimensional concept vectors so the rankings can be diagnosed by inspection.

### Learn why each retrieval signal works

Lexical ranking uses visible terms. Exact matches are particularly important for names, dates, codes, and form numbers. A dense representation can place differently worded descriptions near one another. That helps with synonyms and concepts while sometimes weakening the distinction between related but different identifiers.

Evaluate both signals on the same labeled questions. Inspect one exact reference and one paraphrase before averaging. Make sure candidates are eligible for the user and query date before scoring relevance. A perfect semantic match from a restricted source should never become an ordinary candidate.

The demo uses a small corpus so you can inspect what each representation includes. Note which fields are encoded and whether a title or body changes the result. Transfer those questions to a real corpus before choosing an index or model. Better retrieval comes from a clearer definition of relevance as well as better ranking.

## Worked example

The query “holidays” should retrieve a policy titled “vacation leave” even though it shares no exact terms.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from math import sqrt
import re


def tokens(text):
    return set(re.findall(r"[a-z]+", text.lower()))


concepts = (
    {"vacation", "leave", "holidays"},
    {"travel", "boarding", "rail", "journey", "board"},
    {"board", "equipment", "circuit"},
    {"payroll", "tax", "adjustments"},
)


def vector(text):
    terms = tokens(text)
    return tuple(len(terms & concept) for concept in concepts)


def similarity(left, right):
    norm = sqrt(sum(v * v for v in left) * sum(v * v for v in right))
    return sum(a * b for a, b in zip(left, right)) / norm if norm else 0


def ranked(query, rows, score):
    scores = [(score(query, row.text), row.source) for row in rows]
    return [source for value, source in sorted(scores, key=lambda pair: (-pair[0], pair[1])) if value > 0]


def lexical(query, rows):
    return ranked(query, rows, lambda a, b: len(tokens(a) & tokens(b)))


def dense(query, rows):
    return ranked(query, rows, lambda a, b: similarity(vector(a), vector(b)))


assert lexical("holidays", eligible) == []
assert dense("holidays", eligible)[0] == "leave@2"
```

## Try it yourself

Score the same labeled cases with both ranking methods and inspect the first result.

[Download the workbook](../../assets/notebooks/retrieval-system-engineering.ipynb){ download } and run through **Lecture 02** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Recall can improve on vocabulary shifts. Examine a query where the semantic representation is too broad or incomplete.

## Continue

[← Versioned ingestion and chunk provenance](01-versioned-ingestion-and-chunk-provenance.md) · [Course outline](index.md#course-outline){ .study-overview } · [Hybrid fusion and relevance diagnostics →](03-hybrid-fusion-and-relevance-diagnostics.md)
{: .study-directions .study-directions--footer }
