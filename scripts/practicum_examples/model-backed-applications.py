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

# %%
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

# %%
from collections import defaultdict
from statistics import median
from time import perf_counter


def baseline(question, evidence):
    if not evidence:
        return json.dumps({"status": "abstain", "answer": "", "sources": []})
    return json.dumps({"status": "answer", "answer": evidence[0].text, "sources": [evidence[0].id]})


def candidate(question, evidence):
    if question == "How do I reserve a meeting room?":
        return json.dumps({"status": "answer", "answer": "Use the calendar.", "sources": ["unknown"]})
    return baseline(question, evidence)


def call(provider, question, evidence):
    if not evidence:
        return ABSTAIN, "no_evidence"
    try:
        reply = parse_reply(provider(question, evidence))
    except OSError:
        return ABSTAIN, "provider_failure"
    except ValueError:
        return ABSTAIN, "invalid_response"
    if reply.status == "answer":
        supplied = {p.id: p.text for p in evidence}
        if len(reply.sources) != 1 or supplied.get(reply.sources[0]) != reply.answer:
            return ABSTAIN, "unsupported"
    return reply, reply.status


CASES = (
    ("When should I file a travel receipt?", "employee", "answerable", "travel"),
    ("How do I reserve a meeting room?", "employee", "answerable", "room"),
    ("When are payroll adjustments reviewed?", "reviewer", "answerable", "payroll"),
    ("When are payroll adjustments reviewed?", "employee", "restricted", None),
    ("Is snow forecast?", "employee", "out_of_scope", None),
)


def score(provider):
    counts = defaultdict(lambda: {"cases": 0, "correct": 0})
    hits = answerable = fallback = 0
    durations = []
    for question, role, slice_name, expected in CASES:
        start = perf_counter()
        evidence = retrieve(question, role)
        reply, reason = call(provider, question, evidence)
        durations.append(1000 * (perf_counter() - start))
        answerable += expected is not None
        hits += expected is not None and any(p.id == expected for p in evidence)
        fallback += reason in {"unsupported", "invalid_response", "provider_failure"}
        counts[slice_name]["cases"] += 1
        counts[slice_name]["correct"] += reply.sources == ((expected,) if expected else ())
    return {
        "retrieval_recall_at_2": hits / answerable, "slices": dict(counts),
        "fallbacks": fallback, "median_ms": round(median(durations), 3),
    }


baseline_report = score(baseline)
candidate_report = score(candidate)
print(baseline_report, candidate_report)
assert baseline_report["retrieval_recall_at_2"] == candidate_report["retrieval_recall_at_2"] == 1
assert baseline_report["fallbacks"] == 0 and candidate_report["fallbacks"] == 1
assert candidate_report["slices"]["restricted"]["correct"] == 1


def busy_provider(question, evidence):
    raise TimeoutError("fixture timeout")


question, role, _, _ = CASES[0]
evidence = retrieve(question, role)
assert call(busy_provider, question, evidence) == (ABSTAIN, "provider_failure")
assert call(lambda question, evidence: "not JSON", question, evidence) == (ABSTAIN, "invalid_response")

# %%
import os
from collections import Counter
from urllib.request import ProxyHandler, Request, build_opener


def ollama_provider(model, usage):
    def generate(question, evidence):
        context = [{"id": p.id, "text": p.text} for p in evidence]
        prompt = (
            "Choose an exact quote that answers the question. "
            "Return a JSON object with status, answer, and sources. "
            "Use status answer, the full quote, and its one source ID. "
            "If insufficient, use status abstain, an empty answer, and an empty sources list. "
            + json.dumps({"question": question, "passages": context})
        )
        body = json.dumps({"model": model, "prompt": prompt, "format": "json", "stream": False})
        request = Request(
            "http://127.0.0.1:11434/api/generate", data=body.encode(),
            headers={"Content-Type": "application/json"},
        )
        with build_opener(ProxyHandler({})).open(request, timeout=15) as response:
            result = json.load(response)
        raw = result.get("response") if isinstance(result, dict) else None
        if not isinstance(raw, str):
            raise ValueError("missing provider response")
        for field in ("prompt_eval_count", "eval_count"):
            count = result.get(field)
            if type(count) is int and count >= 0:
                usage[field] += count
        return raw

    return generate


model = os.getenv("AIEBOK_OLLAMA_MODEL")
if model:
    usage = Counter()
    print(model, score(ollama_provider(model, usage)), "reported token counts", dict(usage))
else:
    print("Local baseline and fixture candidate verified. Set AIEBOK_OLLAMA_MODEL to include a running local Ollama model.")
