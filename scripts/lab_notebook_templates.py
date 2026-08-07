"""Structured starter-lab notebook content (one guided cell sequence per lab)."""
from __future__ import annotations

import uuid
from typing import Callable

from generate_maturity_content import STARTER_LABS
from spec_driven_content import render_notebook_spec_cell

Meta = tuple[str, str, str, str, list[str]]


def _id() -> str:
    return uuid.uuid4().hex[:8]


def _md(text: str) -> dict:
    body = text if text.endswith("\n") else f"{text}\n"
    return {"cell_type": "markdown", "id": _id(), "metadata": {}, "source": [body]}


def _code(text: str) -> dict:
    body = text if text.endswith("\n") else f"{text}\n"
    return {
        "cell_type": "code",
        "id": _id(),
        "metadata": {},
        "source": [body],
        "outputs": [],
        "execution_count": None,
    }


def _meta(slug: str) -> Meta:
    for row in STARTER_LABS:
        if row[0] == slug:
            return row
    raise KeyError(slug)


def _intro(slug: str) -> list[dict]:
    _, title, objective, book, tasks = _meta(slug)
    task_lines = "\n".join(f"{i + 1}. {t}" for i, t in enumerate(tasks))
    return [
        _md(
            f"# Lab — {title}\n\n"
            f"**Objective:** {objective}\n\n"
            f"**Book track:** `{book}` · **Time:** 30–45 minutes · **Python:** 3.10+\n\n"
            "Work through the cells in order. Each code cell should run top-to-bottom. "
            "Keep `main.py` in this folder aligned with your final answers—`pytest` validates that file."
        ),
        _md(
            "## How to use this notebook\n\n"
            "1. Open from the lab directory (`labs/{slug}/`) in Jupyter, VS Code, or Codespaces.\n"
            "2. Run cells sequentially; restart the kernel if you change earlier definitions.\n"
            "3. Complete **Your turn** sections, then sync working code into `main.py`.\n"
            "4. Run the verification cell (`pytest`) before you finish.\n".format(slug=slug)
        ),
        _code(
            "from pathlib import Path\n\n"
            "LAB_DIR = Path('.').resolve()\n"
            "assert (LAB_DIR / 'main.py').exists(), (\n"
            "    'Start Jupyter from the lab directory, e.g. labs/{slug}/'\n"
            ")\n"
            "print('Lab directory:', LAB_DIR)".format(slug=slug)
        ),
        _md("## Tasks\n\n" + task_lines),
        _md(render_notebook_spec_cell(slug, title)),
    ]


def _verify_cell() -> list[dict]:
    return [
        _md("## Verify\n\nRun the test suite against `main.py` and `test_lab.py`."),
        _code(
            "import subprocess\n"
            "import sys\n\n"
            "result = subprocess.run(\n"
            "    [sys.executable, '-m', 'pytest', 'test_lab.py', '-q'],\n"
            "    capture_output=True,\n"
            "    text=True,\n"
            ")\n"
            "print(result.stdout)\n"
            "if result.stderr:\n"
            "    print(result.stderr, file=sys.stderr)\n"
            "assert result.returncode == 0, 'Tests failed—see output above'"
        ),
        _md(
            "## Reflection\n\n"
            "- What broke first when you changed inputs?\n"
            "- Which simpler baseline would you compare against in a design review?\n\n"
            "## Extensions\n\n"
            "- Add another case to `test_lab.py`.\n"
            "- Link observations to a concept card on the AIEBOK site."
        ),
    ]


def notebook_cosine_similarity() -> list[dict]:
    cells = _intro("01-cosine-similarity")
    cells += [
        _md(
            "## Step 1 — Vectors, dot product, and magnitude\n\n"
            "Cosine similarity measures the angle between two vectors. "
            "It ignores magnitude after normalization—useful when comparing embedding directions."
        ),
        _code(
            "from math import sqrt\n\n\n"
            "def dot(a: list[float], b: list[float]) -> float:\n"
            "    if len(a) != len(b):\n"
            "        raise ValueError('vectors must have equal dimensions')\n"
            "    return sum(x * y for x, y in zip(a, b))\n\n\n"
            "def magnitude(v: list[float]) -> float:\n"
            "    return sqrt(sum(x * x for x in v))\n\n\n"
            "query = [1.0, 1.0, 0.0]\n"
            "candidate = [0.9, 1.0, 0.1]\n"
            "print('dot product:', dot(query, candidate))\n"
            "print('magnitudes:', magnitude(query), magnitude(candidate))"
        ),
        _md("## Step 2 — Cosine similarity\n\nImplement cosine and handle edge cases (zero vectors, mismatched lengths)."),
        _code(
            "def cosine(a: list[float], b: list[float]) -> float:\n"
            "    if len(a) != len(b):\n"
            "        raise ValueError('vectors must have equal dimensions')\n"
            "    dot_ab = dot(a, b)\n"
            "    norm_a = magnitude(a)\n"
            "    norm_b = magnitude(b)\n"
            "    if norm_a == 0 or norm_b == 0:\n"
            "        raise ValueError('cosine similarity is undefined for a zero vector')\n"
            "    return dot_ab / (norm_a * norm_b)\n\n\n"
            "print('cosine(query, candidate):', round(cosine(query, candidate), 3))"
        ),
        _md("## Step 3 — Rank paraphrase candidates\n\nRank short text labels by similarity to a query vector."),
        _code(
            "candidates = {\n"
            "    'service unavailable': [0.9, 1.0, 0.1],\n"
            "    'invoice approved': [0.1, 0.0, 1.0],\n"
            "    'application outage': [1.0, 0.8, 0.0],\n"
            "}\n\n"
            "ranked = sorted(\n"
            "    ((cosine(query, vector), text) for text, vector in candidates.items()),\n"
            "    reverse=True,\n"
            ")\n\n"
            "print('Ranked candidates:')\n"
            "for score, text in ranked:\n"
            "    print(f'  {score:.3f}  {text}')"
        ),
        _md(
            "## Your turn\n\n"
            "1. **Predict** the ranked order before running Step 3.\n"
            "2. Compare **cosine** vs raw **dot product** on unnormalized vectors.\n"
            "3. Try orthogonal vectors and a zero vector—what should happen?\n"
            "4. Copy the final `cosine` function (and ranking loop) into `main.py`."
        ),
        _code(
            "# Example: cosine vs dot product on different magnitudes\n"
            "short = [1.0, 0.0]\n"
            "long = [10.0, 0.0]\n"
            "print('dot:', dot(short, long))\n"
            "print('cosine:', cosine(short, long))\n\n"
            "# TODO: add orthogonal and zero-vector checks, then update main.py"
        ),
    ]
    cells += _verify_cell()
    return cells


def notebook_semantic_search() -> list[dict]:
    cells = _intro("02-semantic-search")
    cells += [
        _md(
            "## Step 1 — Tokenize documents\n\n"
            "We build a tiny lexical index without external embedding APIs. "
            "Tokens are lowercased alphanumeric words."
        ),
        _code(
            "import re\n"
            "from collections import Counter\n\n"
            "DOCUMENTS = [\n"
            "    'Reset a forgotten employee password in the identity portal.',\n"
            "    'Investigate an unavailable application and service outage.',\n"
            "    'Submit and approve an expense reimbursement invoice.',\n"
            "    'Request access to a restricted analytics database.',\n"
            "]\n\n\n"
            "def tokens(text: str) -> list[str]:\n"
            "    return re.findall(r'[a-z0-9]+', text.lower())\n\n\n"
            "for doc in DOCUMENTS:\n"
            "    print(tokens(doc)[:8], '...')"
        ),
        _md(
            "## Step 2 — Hashing trick embeddings\n\n"
            "Map each token into a fixed-size vector using a stable hash bucket. "
            "This is not production quality—it teaches the retrieval pipeline shape."
        ),
        _code(
            "from hashlib import sha256\n\n\n"
            "def embed(text: str, dimensions: int = 32) -> list[float]:\n"
            "    counts = Counter(tokens(text))\n"
            "    vector = [0.0] * dimensions\n"
            "    for token, count in counts.items():\n"
            "        bucket = int.from_bytes(sha256(token.encode()).digest()[:4], 'big') % dimensions\n"
            "        vector[bucket] += count\n"
            "    return vector\n\n\n"
            "print('embedding length:', len(embed(DOCUMENTS[0])))"
        ),
        _md("## Step 3 — Cosine search over the corpus"),
        _code(
            "from math import sqrt\n\n\n"
            "def cosine(a: list[float], b: list[float]) -> float:\n"
            "    dot = sum(x * y for x, y in zip(a, b))\n"
            "    na, nb = sqrt(sum(x * x for x in a)), sqrt(sum(y * y for y in b))\n"
            "    return dot / (na * nb) if na and nb else 0.0\n\n\n"
            "def search(query: str) -> list[tuple[float, str]]:\n"
            "    q = embed(query)\n"
            "    return sorted(((cosine(q, embed(doc)), doc) for doc in DOCUMENTS), reverse=True)\n\n\n"
            "for score, doc in search('the application is unavailable'):\n"
            "    print(f'{score:.3f}  {doc}')"
        ),
        _md(
            "## Your turn\n\n"
            "1. Explain why the outage document ranks above unrelated docs.\n"
            "2. Add a **hard-negative** document that shares tokens but wrong intent.\n"
            "3. Measure **recall@1** on five hand-written queries.\n"
            "4. Change `dimensions`—what breaks?\n\n"
            "Sync `embed`, `cosine`, and `search` into `main.py` when done."
        ),
        _code(
            "queries = [\n"
            "    'the application is unavailable',\n"
            "    'password reset portal',\n"
            "    'expense reimbursement',\n"
            "    # add two more queries\n"
            "]\n\n"
            "for q in queries:\n"
            "    top = search(q)[0]\n"
            "    print(q, '->', top[1][:50], f'({top[0]:.3f})')"
        ),
    ]
    cells += _verify_cell()
    return cells


def notebook_basic_rag() -> list[dict]:
    cells = _intro("03-basic-rag")
    cells += [
        _md(
            "## Step 1 — Evidence store\n\n"
            "RAG separates **retrieval** (find evidence) from **generation** (compose an answer). "
            "Here generation is template-based so you can inspect each stage."
        ),
        _code(
            "import re\n\n"
            "PASSAGES = [\n"
            "    ('leave', 'Employees receive 20 days of annual leave per calendar year.'),\n"
            "    ('expenses', 'Expense claims must be submitted within 30 days of purchase.'),\n"
            "    ('security', 'Suspected credential exposure must be reported immediately.'),\n"
            "]\n\n\n"
            "def words(text: str) -> set[str]:\n"
            "    return set(re.findall(r'[a-z0-9]+', text.lower()))\n\n\n"
            "for source, text in PASSAGES:\n"
            "    print(f'[{source}]', text)"
        ),
        _md("## Step 2 — Retrieve top-k passages by lexical overlap"),
        _code(
            "def retrieve(question: str, k: int = 2) -> list[tuple[int, str, str]]:\n"
            "    q = words(question)\n"
            "    scored = [(len(q & words(text)), source, text) for source, text in PASSAGES]\n"
            "    return sorted(scored, reverse=True)[:k]\n\n\n"
            "question = 'How soon must I submit an expense claim?'\n"
            "print('Question:', question)\n"
            "print('Retrieved:', retrieve(question))"
        ),
        _md("## Step 3 — Ground answers in evidence with citations"),
        _code(
            "def answer(question: str) -> str:\n"
            "    evidence = [item for item in retrieve(question) if item[0] > 0]\n"
            "    if not evidence:\n"
            "        return 'I do not have relevant evidence to answer that question.'\n"
            "    citations = ' '.join(f'[{source}]' for _, source, _ in evidence)\n"
            "    context = ' '.join(text for _, _, text in evidence)\n"
            "    return f'Evidence: {context} {citations}'\n\n\n"
            "print('Answer:', answer(question))"
        ),
        _md(
            "## Your turn\n\n"
            "1. Trace retrieval for a query with **no lexical overlap**.\n"
            "2. Confirm the **abstention** message when nothing matches.\n"
            "3. Verify citations appear only when evidence is used.\n"
            "4. Compare `k=1` vs `k=2` retrieval quality.\n\n"
            "Update `main.py` with your final functions."
        ),
        _code(
            "off_topic = 'What is the stock price of the company?'\n"
            "print('Retrieve:', retrieve(off_topic))\n"
            "print('Answer:', answer(off_topic))\n\n"
            "print('k=1:', answer(question))  # temporarily set k=1 in retrieve to compare"
        ),
    ]
    cells += _verify_cell()
    return cells


def notebook_agent_loop() -> list[dict]:
    cells = _intro("04-agent-loop")
    cells += [
        _md(
            "## Step 1 — Agent state\n\n"
            "Agents loop: **plan** an action, **act**, **observe** the result. "
            "Bound the loop with a step limit and explicit termination."
        ),
        _code(
            "from dataclasses import dataclass, field\n\n\n"
            "@dataclass\n"
            "class State:\n"
            "    goal: str\n"
            "    step: int = 0\n"
            "    max_steps: int = 4\n"
            "    observations: list[str] = field(default_factory=list)\n"
            "    done: bool = False\n\n\n"
            "State(goal='produce a verified draft')"
        ),
        _md("## Step 2 — Planner and environment"),
        _code(
            "def plan(state: State) -> str:\n"
            "    if not state.observations:\n"
            "        return 'inspect requirements'\n"
            "    if 'requirements inspected' in state.observations and 'draft created' not in state.observations:\n"
            "        return 'create draft'\n"
            "    return 'verify result'\n\n\n"
            "def execute(action: str) -> str:\n"
            "    outcomes = {\n"
            "        'inspect requirements': 'requirements inspected',\n"
            "        'create draft': 'draft created',\n"
            "        'verify result': 'result verified',\n"
            "    }\n"
            "    return outcomes[action]\n\n\n"
            "s = State(goal='demo')\n"
            "print('first action:', plan(s))"
        ),
        _md("## Step 3 — Run the bounded loop"),
        _code(
            "def run(goal: str, *, verbose: bool = True) -> State:\n"
            "    state = State(goal=goal)\n"
            "    while not state.done and state.step < state.max_steps:\n"
            "        action = plan(state)\n"
            "        observation = execute(action)\n"
            "        state.observations.append(observation)\n"
            "        state.step += 1\n"
            "        state.done = observation == 'result verified'\n"
            "        if verbose:\n"
            "            print({'step': state.step, 'action': action, 'observation': observation})\n"
            "    return state\n\n\n"
            "final = run('produce a verified draft')\n"
            "print('status:', 'complete' if final.done else 'step limit reached')\n"
            "print('observations:', final.observations)"
        ),
        _md(
            "## Your turn\n\n"
            "1. Sketch the state diagram for the default goal.\n"
            "2. Lower `max_steps` and confirm graceful stop.\n"
            "3. Add handling for an invalid action in `execute`.\n"
            "4. Inspect `final.observations` after each run.\n\n"
            "Copy the finished loop into `main.py`."
        ),
        _code(
            "# TODO: experiment with max_steps=2 and invalid actions\n"
            "run('produce a verified draft', verbose=True)"
        ),
    ]
    cells += _verify_cell()
    return cells


def notebook_eval_harness() -> list[dict]:
    cells = _intro("05-eval-harness")
    cells += [
        _md(
            "## Step 1 — Evaluation cases and slices\n\n"
            "Production evals use **slices** (safety, locale, product area) so averages do not hide critical failures."
        ),
        _code(
            "from dataclasses import dataclass\n\n\n"
            "@dataclass(frozen=True)\n"
            "class Case:\n"
            "    question: str\n"
            "    expected: str\n"
            "    slice: str\n\n\n"
            "CASES = [\n"
            "    Case('capital of France', 'paris', 'general'),\n"
            "    Case('2 + 2', '4', 'general'),\n"
            "    Case('unknown employee password', 'cannot access', 'safety'),\n"
            "]\n\n\n"
            "for case in CASES:\n"
            "    print(case.slice, case.question)"
        ),
        _md("## Step 2 — Candidate model and scoring"),
        _code(
            "def candidate(question: str) -> str:\n"
            "    answers = {\n"
            "        'capital of France': 'Paris',\n"
            "        '2 + 2': '4',\n"
            "        'unknown employee password': 'I cannot access employee passwords.',\n"
            "    }\n"
            "    return answers.get(question, \"I don't know.\")\n\n\n"
            "def contains_expected(actual: str, expected: str) -> bool:\n"
            "    return expected.lower() in actual.lower()\n\n\n"
            "for case in CASES:\n"
            "    actual = candidate(case.question)\n"
            "    ok = contains_expected(actual, case.expected)\n"
            "    print(f\"{'PASS' if ok else 'FAIL'} [{case.slice}] {case.question}: {actual}\")"
        ),
        _md("## Step 3 — Release gate"),
        _code(
            "def evaluate(cases: list[Case] = CASES) -> tuple[float, bool, bool]:\n"
            "    results = []\n"
            "    for case in cases:\n"
            "        actual = candidate(case.question)\n"
            "        passed = contains_expected(actual, case.expected)\n"
            "        results.append((case, passed, actual))\n"
            "        print(f\"{'PASS' if passed else 'FAIL'} [{case.slice}] {case.question}: {actual}\")\n"
            "    score = sum(passed for _, passed, _ in results) / len(results)\n"
            "    safety_ok = all(passed for case, passed, _ in results if case.slice == 'safety')\n"
            "    release = score >= 0.90 and safety_ok\n"
            "    print(f'score={score:.1%} safety_ok={safety_ok} release={release}')\n"
            "    return score, safety_ok, release\n\n\n"
            "evaluate()"
        ),
        _md(
            "## Your turn\n\n"
            "1. Add a failing **general** case—release should block.\n"
            "2. Add a failing **safety** case—release must block even if average score is high.\n"
            "3. Define a new slice with two cases.\n"
            "4. Note which metric you would monitor in production.\n\n"
            "Mirror changes in `main.py` (including `sys.exit` behavior)."
        ),
        _code(
            "# TODO: extend CASES and re-run evaluate()\n"
            "evaluate()"
        ),
    ]
    cells += _verify_cell()
    return cells


BUILDERS: dict[str, Callable[[], list[dict]]] = {
    "01-cosine-similarity": notebook_cosine_similarity,
    "02-semantic-search": notebook_semantic_search,
    "03-basic-rag": notebook_basic_rag,
    "04-agent-loop": notebook_agent_loop,
    "05-eval-harness": notebook_eval_harness,
}


def cells_for(slug: str) -> list[dict]:
    return BUILDERS[slug]()
