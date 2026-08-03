"""One-off helper to seed concept_library.py with entries for every catalog topic."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_books import BOOKS  # noqa: E402


def normalize(topic: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")


def slug_to_words(slug: str) -> str:
    return slug.replace("-", " ")


SPECIFIC: dict[str, tuple[str, str, str]] = {
    "bm25": (
        "BM25 ranks documents by weighted term frequency with length normalization and term-frequency saturation, so extra keyword repeats help less over time.",
        "Searching 'PTO accrual cap' should rank the handbook section containing that exact phrase above a generic leave-policy overview.",
        "Measure recall@k on identifier-heavy queries and compare against a dense-only baseline.",
    ),
    "dense-retrieval": (
        "Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by cosine similarity or dot product.",
        "A query about 'application unavailable' can retrieve 'service is down' even when the words do not overlap.",
        "Build a 30-query eval set with paraphrases and hard negatives; report recall@5 and MRR.",
    ),
    "hybrid-search": (
        "Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—because neither method alone covers identifiers and paraphrases.",
        "Fusing BM25 and vector rankings surfaces policy IDs in lexical results while keeping semantic matches for informal user phrasing.",
        "Show a query where lexical-only and dense-only each miss the correct document but fusion succeeds.",
    ),
    "goal-directed-behavior": (
        "Goal-directed behavior means the system selects actions to reduce distance to an explicit objective rather than producing unconstrained output.",
        "An incident router should minimize misroutes and escalation time, not maximize fluent ticket summaries.",
        "State the goal, list candidate actions, and show how each action changes measurable progress toward the goal.",
    ),
    "attention": (
        "Attention computes a weighted mix of values where weights come from query–key compatibility, letting each position gather context-dependent information.",
        "In translation, a target word can attend strongly to its aligned source word regardless of distance in the sentence.",
        "Implement scaled dot-product attention and verify that masking prevents illegal positions from receiving weight.",
    ),
    "kv-cache": (
        "The KV cache stores previously computed key and value tensors during autoregressive decoding so each new token does not reprocess the full prefix.",
        "Streaming chat reuses cached states for the system prompt and prior turns, cutting latency after the first token.",
        "Compare tokens-per-second with and without cache enabled on a fixed 2k-token prefix.",
    ),
    "prompt-injection": (
        "Prompt injection embeds hostile instructions in untrusted content that the model may follow instead of trusted system policy.",
        "A retrieved web page containing 'ignore previous instructions' can redirect a summarizer to exfiltrate secrets.",
        "Red-team with malicious retrieved text and verify the system treats external content as data, not authority.",
    ),
    "rag": (
        "Retrieval-augmented generation retrieves external evidence at query time, packs it into context, and conditions generation on that evidence.",
        "An HR assistant retrieves the current travel policy, cites the passage, and refuses when no supporting document exists.",
        "Evaluate retrieval recall and answer faithfulness separately before judging end-to-end quality.",
    ),
    "a-star": (
        "A* expands the lowest estimated total-cost node first, combining path cost g(n) with heuristic h(n) toward the goal.",
        "In a grid maze, A* with a Manhattan-distance heuristic often expands fewer cells than breadth-first search while still finding an optimal path.",
        "Run BFS and A* on the same maze; compare expanded nodes and verify identical shortest-path length.",
    ),
    "gradient-descent": (
        "Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples.",
        "One step on linear regression moves the weight toward the line that minimizes squared error on the batch.",
        "Hand-compute one update for y = 2x + 1 noise data and confirm loss decreases.",
    ),
    "plan-act-observe": (
        "Plan–act–observe separates choosing the next action, executing it in the environment, and recording observations that update state.",
        "An agent plans 'create draft', executes it, observes 'draft created', then plans verification instead of repeating creation.",
        "Log each cycle and show that observations change subsequent plans rather than repeating identical actions.",
    ),
    "reciprocal-rank-fusion": (
        "Reciprocal rank fusion merges ranked lists by summing 1/(k + rank) per document across retrievers, boosting items strong in multiple lists.",
        "A document ranked third lexically and second densely can outscore one that tops only a single retriever.",
        "Fuse two hand-built rankings and verify the dual-high document receives the highest fused score.",
    ),
    "query-rewriting": (
        "Query rewriting transforms the user's request—via expansion, decomposition, or HyDE—before retrieval to close vocabulary and intent gaps.",
        "Expanding 'PTO' to include 'paid time off' and 'leave accrual' helps lexical retrievers match handbook language users did not type.",
        "Compare recall@k with and without rewrite on acronym-heavy and multi-intent queries.",
    ),
    "parent-child-retrieval": (
        "Parent–child retrieval indexes small child chunks for precision but returns parent sections for generation so answers retain headings and surrounding context.",
        "A child chunk may contain one bullet while the parent section carries the policy title and exceptions needed for a correct answer.",
        "Show a failure where child-only retrieval omits the section title and fix it by joining to the parent at generation time.",
    ),
    "rational-agents": (
        "Rational agents choose actions that maximize expected utility toward a goal given what they perceive and know—under explicit constraints.",
        "A router agent should prefer actions with higher expected task success, not actions that merely produce confident language.",
        "Define the utility function and show one action that improves it versus one that sounds better but scores worse.",
    ),
    "bounded-rationality": (
        "Bounded rationality acknowledges limited compute, time, and information—systems must satisfice rather than exhaustively optimize.",
        "An on-call assistant stops after three retrieval attempts within a latency SLO instead of searching until perfect certainty.",
        "Document the budget that stops search and show a case where more compute would help but violates the budget.",
    ),
    "capability-decomposition": (
        "Capability decomposition breaks intelligence into perception, memory, learning, planning, and action so teams can own and test each part separately.",
        "Incident routing can fail in classification while generation still looks fluent—decomposition makes the failing capability visible.",
        "Draw a capability map and mark which box owns each failure from the chapter scenario.",
    ),
    "feedback": (
        "Feedback closes the loop: outcomes from actions update beliefs, models, or policies for subsequent decisions.",
        "Misrouted tickets returned by engineers should update routing features or rules so the same mistake is measurable and reducible.",
        "Identify one feedback signal, where it is stored, and how long until it influences the next decision.",
    ),
    "json-schema": (
        "JSON Schema declares required fields, types, and constraints that validators enforce after model generation.",
        "Rejecting payloads where 'total' is a string prevents silent accounting errors from plausible-looking JSON.",
        "List three invalid payloads and confirm the validator rejects each for distinct reasons.",
    ),
    "context-windows": (
        "The context window caps how many tokens the model can attend to in one forward pass—prompt, evidence, tools, and output compete for this budget.",
        "A 128k window still requires prioritization when ten long documents are retrieved; packing policy matters as much as size.",
        "Measure task quality versus tokens used and identify the knee of the curve for your workload.",
    ),
    "fine-tuning": (
        "Fine-tuning adapts pretrained weights with supervised or preference data when prompts alone cannot stabilize required behavior.",
        "Support tone and escalation policy may need SFT so responses stay consistent across thousands of ticket types.",
        "Compare fine-tuned and prompt-only models on a held-out behavioral eval with cost and rollback plan documented.",
    ),
    "lora": (
        "LoRA fine-tunes low-rank adapter matrices inserted into attention layers, reducing trainable parameters and memory versus full fine-tuning.",
        "A 7B model with LoRA adapters can learn a domain tone on one GPU while base weights stay frozen.",
        "Report eval uplift, training cost, and adapter version used at inference.",
    ),
    "function-calling": (
        "Function calling lets models emit structured invocations with typed arguments that runtime code validates and executes.",
        "Searching internal docs via a read-only tool returns live titles and URLs instead of hallucinated links.",
        "Fuzz tool arguments and confirm unauthorized or mistyped calls fail before side effects.",
    ),
    "checkpoints": (
        "Checkpoints persist durable agent state so interrupted runs resume without repeating side effects or losing progress.",
        "After approval for a payment step, a checkpoint stores pending state until the human approves, then continues from that point.",
        "Kill a run mid-loop, restore from checkpoint, and verify idempotent tools are not duplicated.",
    ),
    "slices": (
        "Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure.",
        "95% overall accuracy can mask 60% accuracy on high-value enterprise accounts.",
        "Define three slices from real traffic and report metrics separately with release thresholds per slice.",
    ),
    "rubrics": (
        "Rubrics score qualitative outputs against explicit criteria with anchored levels, enabling consistent human or model judging.",
        "A support reply rubric scores correctness, completeness, tone, and citation presence on a 1–4 scale with examples.",
        "Calibrate two raters against the rubric and report inter-rater agreement on 20 cases.",
    ),
}


CATEGORY_HINTS: dict[str, str] = {
    "eval": "Define a metric tied to a user decision, collect labeled cases, and set pass thresholds before release.",
    "security": "Threat-model the boundary, log access, default deny, and verify mitigations with adversarial tests.",
    "memory": "Separate working, session, and durable stores; record provenance and expiry for every recalled item.",
    "retrieval": "Measure recall@k on realistic queries with hard negatives before tuning generation.",
    "cloud": "Map the logical capability first, then choose managed services whose constraints match the workload.",
    "agent": "Make state, budgets, and termination explicit; never rely on the model to stop itself.",
    "training": "Track data version, hyperparameters, and eval splits so results are reproducible and comparable.",
    "ux": "Expose uncertainty, citations, and undo paths so users can verify and recover from mistakes.",
}


TOPIC_OPENINGS: dict[str, str] = {
    "eval": "{label} turns desired behavior into measurable pass/fail criteria tied to real decisions.",
    "security": "{label} reduces exploitability when models, users, or retrieved content cannot be fully trusted.",
    "memory": "{label} controls what past information is reconstructed for the next decision—and what is forgotten.",
    "retrieval": "{label} influences which evidence enters the candidate set before ranking and generation.",
    "cloud": "{label} maps a logical AI capability to deployable, governable infrastructure choices.",
    "agent": "{label} affects how autonomous loops choose actions, recover, and stop.",
    "training": "{label} shapes how models learn from data and how those changes are verified before release.",
    "ux": "{label} determines whether users can trust, verify, and recover from probabilistic outputs.",
    "general": "{label} is a design choice whose value must be shown with baselines, not assumed from labels.",
}


ROLE_FRAMING = [
    "defines the initial boundary for what the system can represent or decide",
    "performs the main transformation that turns inputs into comparable candidates",
    "connects this mechanism to neighboring components in the pipeline",
    "governs quality, cost, latency, or safety trade-offs at runtime",
    "surfaces the constraint or failure mode engineers most often miss",
]


def categorize(slug: str) -> str:
    text = slug_to_words(slug)
    if any(w in text for w in ("eval", "metric", "rubric", "benchmark", "threshold", "slice")):
        return "eval"
    if any(w in text for w in ("security", "injection", "sandbox", "threat", "audit", "authorization", "permission")):
        return "security"
    if any(w in text for w in ("memory", "checkpoint", "recovery", "episodic", "session")):
        return "memory"
    if any(w in text for w in ("retriev", "bm25", "rerank", "embedding", "index", "chunk", "rag", "fusion")):
        return "retrieval"
    if any(w in text for w in ("aws", "azure", "cloud", "vertex", "bedrock", "lambda", "kubernetes", "entra")):
        return "cloud"
    if any(w in text for w in ("agent", "workflow", "plan", "tool", "mcp", "delegat", "supervisor")):
        return "agent"
    if any(w in text for w in ("train", "fine-tun", "lora", "dataset", "loss", "gradient", "optim")):
        return "training"
    if any(w in text for w in ("ux", "user", "adoption", "accessibility", "citation", "undo")):
        return "ux"
    return "general"


def craft_entry(topic: str, role_idx: int, summary: str) -> tuple[str, str, str]:
    label = topic.strip()
    key = normalize(label)
    words = slug_to_words(key)
    cat = categorize(key)
    opening = TOPIC_OPENINGS[cat].format(label=f"**{label.title()}**")
    role = ROLE_FRAMING[role_idx % len(ROLE_FRAMING)]
    explanation = f"{opening} Here it {role}."
    example = (
        f"In the book scenario, apply {words} to one normal case and one case where ignoring it produces a fluent but wrong outcome."
    )
    evidence = CATEGORY_HINTS.get(cat, "State inputs, outputs, and one test that would falsify a wrong design.")
    return explanation, example, evidence


def build_entries() -> dict[str, tuple[str, str, str]]:
    entries: dict[str, tuple[str, str, str]] = {}
    seen: set[str] = set()
    for book in BOOKS:
        for chapter in book["chapters"]:
            summary = chapter[1]
            for i, topic in enumerate(chapter[2]):
                key = normalize(topic)
                if key in seen:
                    continue
                seen.add(key)
                entries[key] = SPECIFIC.get(key, craft_entry(topic, i, summary))
    return entries


def main() -> None:
    entries = build_entries()
    out = Path(__file__).resolve().parent / "concept_entries.json"
    out.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} concept entries to {out.name}")


if __name__ == "__main__":
    main()
