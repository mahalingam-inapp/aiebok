"""Worked explanations and executable experiments for the five starter labs."""

STARTER_READINGS = {
    "01-cosine-similarity": (
        """## When scale changes the ranking

Two reports can use the same vocabulary proportions and have different lengths. A raw dot product rewards both agreement in direction and magnitude. Cosine normalizes by both vector norms, so multiplying either nonzero vector by a positive scalar leaves the score unchanged. This is useful when the proportions matter more than the volume of text.

Take query `[1, 1]` and candidates `[1, 1]` and `[10, 0]`. The raw dot products are 2 and 10, while the cosine scores are 1 and about 0.707. The ranking reverses because the long candidate has a larger magnitude even though it matches only one coordinate. An orthogonal vector scores zero. A zero vector has no direction, so the notebook explicitly rejects it.

This synthetic example does not certify relevance. It checks what the scoring function measures. In a retrieved support queue, record cases where magnitude indicates useful evidence and cases where long documents win for the wrong reason. Choose a measure on labeled requests before using it to rank work.""",
        """short, long, probe = [1.0, 1.0], [10.0, 0.0], [1.0, 1.0]
assert dot(probe, short) < dot(probe, long)
assert cosine(probe, short) > cosine(probe, long)
assert abs(cosine(probe, short) - cosine(probe, [5.0, 5.0])) < 1e-12
assert cosine([1.0, 0.0], [0.0, 1.0]) == 0
try:
    cosine(probe, [0.0, 0.0])
except ValueError as exc:
    print("Zero-vector guard:", exc)
else:
    raise AssertionError("A zero vector should be rejected")
print("Dot-product and cosine rankings disagree as predicted.")""",
    ),
    "02-semantic-search": (
        """## Test the representation before attributing meaning

The hash buckets in this lab encode term counts. Two different words can share a bucket and appear similar, while synonyms with different buckets can appear unrelated. The hash is stable across runs, but stability supplies reproducibility rather than semantic understanding. Reducing the dimensionality increases the chance of collisions.

Build a lexical baseline using the intersection of unique query and document terms. On a query that repeats exact wording, the baseline should surface the right document. When a query uses different wording, inspect its individual tokens and then its occupied buckets. A surprising hit can come from a genuine overlap, a hash collision, or a tie broken by the ordering rule.

Evaluate with labeled queries and distinguish the fraction of answerable queries where the correct item arrived from behavior on unsupported queries. An always-return-a-document policy cannot abstain. The experiment below deliberately collapses nonempty input to one feature to show how stable but uninformative scores can still produce a top-ranked result.""",
        """query = "password reset portal"
lexical = max(DOCUMENTS, key=lambda doc: len(set(tokens(query)) & set(tokens(doc))))
assert lexical == DOCUMENTS[0]
assert search(query)[0][1] == lexical
one_bucket = [cosine(embed(query, 1), embed(doc, 1)) for doc in DOCUMENTS]
assert all(abs(score - 1) < 1e-12 for score in one_bucket)
print("Exact-word baseline:", lexical)
print("Every nonempty document ties with one bucket:", one_bucket)""",
    ),
    "03-basic-rag": (
        """## Locate the boundary that failed

Retrieval proposes passages, context assembly decides what to supply, and the answer stage uses only what survives. Measure them separately. If an expense deadline never arrives in the top candidates, changing the answer wording cannot fix the upstream miss. If the passage arrives but its qualifier is removed, the fault belongs to context assembly.

A citation is not a proof by itself. Its identifier should refer to a passage that was actually supplied, and that passage should support the exact statement. This teaching answer concatenates source text, making the link easy to check. A production generator can introduce unsupported content even when it cites a relevant source.

Include a question with no evidence in evaluation. If zero-overlap candidates accidentally enter context, a system may sound helpful while giving irrelevant advice. Increasing the number of returned results can help a multi-topic query, while also increasing the amount of irrelevant text a later stage must reject. Measure both using the same cases.""",
        r"""scope = "Compare expense claims and annual leave"
for k in (1, 2):
    supplied = {source for score, source, _ in retrieve(scope, k=k) if score > 0}
    cited = set(re.findall(r"\[([^\]]+)\]", answer(scope, k=k)))
    assert cited == supplied
    print(f"k={k}: sources:", sorted(supplied))
assert len({source for score, source, _ in retrieve(scope, k=2) if score > 0}) == 2
assert not re.findall(r"\[([^\]]+)\]", answer("What is the stock price of the company?"))
print("Unsupported questions abstain without fabricated source IDs.")""",
    ),
    "04-agent-loop": (
        """## A terminated run can still be unfinished

A stateful workflow reads a goal and previous observations, proposes an operation, and advances only after observing its result. The loop here has a fixed vocabulary and an explicit maximum number of steps. Reaching the step limit is a stop condition. Reaching the verification observation is a success condition.

For this fixture, inspecting, drafting, and verifying consume three transitions. A budget of two allows a draft to exist, but it cannot declare success. Keeping the result unfinished makes it possible to hand the draft to a reviewer, request more time, or resume after recording a durable checkpoint. A real retry needs to distinguish work that has already taken effect from work that was merely proposed.

Run both budgets and read their observation lists. Ask which information a second worker needs to resume without drafting twice, then name one operation worth leaving behind human approval. No external tools are called by this exercise.""",
        """short_run = run("produce a verified draft", max_steps=2, verbose=False)
complete_run = run("produce a verified draft", max_steps=3, verbose=False)
assert short_run.step == 2 and not short_run.done
assert complete_run.done and complete_run.step == 3
assert complete_run.observations[:2] == short_run.observations
print("Paused:", short_run.observations)
print("Verified:", complete_run.observations)""",
    ),
    "05-eval-harness": (
        """## Aggregate and critical results answer different questions

An overall score describes the average for this mixture of evaluation cases. A critical slice tests behavior where failure is unacceptable or must be reviewed separately. A slice needs evidence to pass. An empty slice is missing coverage, even though Python's all function returns true for an empty iterable.

Suppose 19 routine test cases pass and one access-related case fails. The aggregate is 95%, which meets a 90% threshold, but a gate requiring every critical case to pass should block release. If the 19 routine cases all repeat the same input, this is only an illustration of the arithmetic. It offers little evidence about covered behaviors in the real workload.

Keep counts, expected results, and the consequence of failure with your decision. The fixture uses a substring scorer to isolate the gate. In a real application, a negated statement can contain the expected words and still fail the intended check. Use a rubric, a precise response contract, or review where a simple substring is insufficient.""",
        """illustration = [Case("2 + 2", "4", "general")] * 19
critical_failure = Case("unknown employee password", "requires staff review", "safety")
score, safety_ok, release = evaluate(illustration + [critical_failure])
assert score == 0.95 and not safety_ok and not release
assert evaluate(illustration) == (1.0, False, False)
print("A high average does not override a failed or missing critical slice.")""",
    ),
}
