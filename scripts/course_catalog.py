"""Curriculum structure shared by the book and learning-path generators."""
from dataclasses import dataclass


@dataclass(frozen=True)
class AppliedExercise:
    lecture: int
    title: str
    instructions: str
    code: str


@dataclass(frozen=True)
class TechnicalCourse:
    sections: tuple[str, str, str]
    checks: tuple[str, str, str]
    experiment: str
    verification: str
    applied: AppliedExercise | None = None


TECHNICAL_COURSES = (
    TechnicalCourse(
        ("Goals and representations", "Search and mathematics", "Learning and decisions"),
        ("Write a support-routing goal and identify an example where a fixed keyword rule misroutes a request.",
         "Trace BFS and A* on the same grid. Record both path length and states expanded.",
         "Assign separate costs to a wrong route and a human review. Specify when review becomes cheaper."),
        "Cover the route with a blocked cell and compare the path returned by each search. Record when the heuristic saves work.",
        """
bfs_path, bfs_expanded = bfs()
astar_path, astar_expanded = astar()
assert len(bfs_path) == len(astar_path)
assert astar_expanded <= bfs_expanded
"""),
    TechnicalCourse(
        ("Problem framing and supervised models", "Representations and neural networks", "Evidence and lifecycle"),
        ("Define a prediction cutoff and a naive baseline. Identify a feature available only after the cutoff.",
         "Compare fitting a line with learning an intermediate representation. Name an input for which a line would be inadequate.",
         "Define a holdout slice and a rollback trigger. Explain which metric would detect the failure first."),
        "Add a held-out point and compare the trained line with the mean of the training labels. Keep the held-out point outside DATA.",
        """
held_out = (4, 9)
x, expected = held_out
prediction = w * x + b
mean_label = sum(y for _, y in DATA) / len(DATA)
assert abs(prediction - expected) < abs(mean_label - expected)
"""),
    TechnicalCourse(
        ("Language and corpus preparation", "Tokens and representations", "Search and indexing"),
        ("Write an ambiguous search query. Normalize two spelling variants without discarding their original source text.",
         "Compare the visible tokens for two search queries. Identify a distinct word that should retrieve the same policy.",
         "Record the top document for a token-overlap query and a synonym-only query. Explain the difference."),
        "Compare a direct password query with an alternate wording that shares no indexed terms. Use the scores to motivate a dense retrieval baseline.",
        """
assert cosine(vector("reset password"), vector(DOCS[2])) > 0
assert all(cosine(vector("credentials forgotten"), vector(doc)) == 0 for doc in DOCS)
"""),
    TechnicalCourse(
        ("Sequence models and attention", "Transformer blocks and training", "Decoding and model selection"),
        ("Trace one attention query and identify which key contributes most to the weighted result.",
         "Draw the path through attention and the feed-forward block. Mark where training computes a loss.",
         "Compare decoding distributions at two temperatures. Pick a model selection metric for repeatability."),
        "Keep logits fixed, vary temperature, and compare the probability of the leading token. Explain why selection still needs a task-level evaluation.",
        """
cold = softmax([2.0, 1.0, 0.0], temperature=0.5)
warm = softmax([2.0, 1.0, 0.0], temperature=2.0)
assert abs(sum(cold) - 1.0) < 1e-9
assert cold[0] > warm[0]
"""),
    TechnicalCourse(
        ("Instructions and output contracts", "Context and memory", "Trust and prompt operations"),
        ("Write a prompt requirement and one schema check that can be evaluated independently of the model.",
         "Rebuild the context for a smaller budget. Record which memory or evidence you would summarize first.",
         "Identify which text originated outside the trusted boundary and propose one regression case."),
        "Give a trusted instruction and a retrieved passage competing budgets. Inspect which survives a tight budget and how source trust is represented.",
        """
tight = build(sections, budget=8)
roomy = build(sections, budget=50)
assert len(tight) < len(roomy)
assert "trusted='false'" in roomy
assert "trusted='false'" not in tight
"""),
    TechnicalCourse(
        ("Knowledge strategy and ingestion", "Retrieval and reranking", "Grounded answers and enterprise constraints"),
        ("Sketch source identifiers and chunk lineage for two versions of the same policy.",
         "Compare two ranked lists and trace how reciprocal rank fusion combines them.",
         "Define pass cases for authorized evidence, no relevant evidence, and a citation to the wrong passage."),
        "Build rankings with one shared candidate. Test how agreement affects rank before evaluating citation faithfulness separately.",
        """
ranked = reciprocal_rank_fusion([["shared", "lexical"], ["shared", "dense"]])
assert ranked[0][0] == "shared"
""",
        AppliedExercise(
            5, "Evaluate grounded answers against an access boundary",
            "Read the labeled cases before you run the cell. Predict which sources an employee "
            "should see. Then add a case for a user who has no authorized role. "
            "Check source IDs separately from answer text. The generator here returns a passage extract, "
            "so you can inspect the retrieval and citation behavior directly.",
            """
from dataclasses import dataclass


@dataclass(frozen=True)
class Passage:
    source: str
    tags: set[str]
    text: str
    roles: set[str]


corpus = [
    Passage("travel", {"travel", "receipt"}, "Attach travel receipts to the expense form.", {"employee", "payroll"}),
    Passage("rates", {"payroll", "rate"}, "Use the current internal payroll rate table.", {"payroll"}),
]


def grounded_answer(query_terms, role):
    allowed = [passage for passage in corpus if role in passage.roles]
    ranked = sorted(allowed, key=lambda passage: len(query_terms & passage.tags), reverse=True)
    if not ranked or not query_terms & ranked[0].tags:
        return "No authorized matching evidence.", []
    evidence = ranked[0]
    return evidence.text, [evidence.source]


cases = [
    ({"travel", "receipt"}, "employee", ["travel"]),
    ({"payroll", "rate"}, "employee", []),
    ({"weather"}, "employee", []),
    ({"payroll", "rate"}, "payroll", ["rates"]),
]
for terms, role, expected_sources in cases:
    answer, sources = grounded_answer(terms, role)
    assert sources == expected_sources, (terms, role, sources)
    if not expected_sources:
        assert answer == "No authorized matching evidence."
    print(role, sorted(terms), answer, sources)
""",
        ),
    ),
    TechnicalCourse(
        ("Search and planning", "Verification and tool contracts", "Integrations and reasoning cost"),
        ("Specify the goal, allowed actions, and stop condition for a small research workflow.",
         "Pass a complete plan and then swap two dependent steps. Compare the verifier's decisions.",
         "List the minimum tool fields and estimate the budget for one verification retry."),
        "Construct a plan that contains every step but places the final review too early. Compare it with the valid plan.",
        """
assert verify(PLANS[1])[0]
assert not verify(list(reversed(PLANS[1])))[0]
"""),
    TechnicalCourse(
        ("Workflows and agent loops", "Recovery and patterns", "Coordination and operations"),
        ("Identify where a fixed workflow is sufficient. Write an invariant for a bounded loop.",
         "Record what must survive a restart so an approved action is handled once.",
         "Choose a stopping rule and specify what evidence an operator receives on failure."),
        "Trace the example from planning to its approval pause, then resume after approval and verify that it reaches completion.",
        """
state = State()
state = transition(transition(state))
assert state.step == "approval"
state = transition(state)
assert state.step == "approval"
state.approved = True
state = transition(state)
assert state.step == "complete" and state.done
"""),
    TechnicalCourse(
        ("Discovery and specifications", "Development and testing", "Experience and value"),
        ("Write a baseline workflow and one measurable acceptance case before adding a model.",
         "Turn a rejection behavior into a test that fails for a plausible but incorrect answer.",
         "Name a user-facing fallback and a guardrail metric for a pilot."),
        "Add an out-of-scope case. Decide what an acceptable handoff looks like and check that the demonstration follows it.",
        """
assert all(case["must_contain"].lower() in assistant(case).lower() for case in SPEC)
assert assistant({"input": "Out of scope", "evidence": []}) == "insufficient evidence"
"""),
    TechnicalCourse(
        ("Requirements and judgment", "Stage evaluation and security", "Risk and governance"),
        ("Choose an error whose cost justifies a separate release criterion and define who labels it.",
         "Write separate checks for retrieving evidence and for using it correctly in the final response.",
         "State who may approve release and what evidence or failure blocks it."),
        "Compare aggregate accuracy with accuracy on a critical slice. Add passing general cases and observe why the critical gate should remain closed.",
        """
expanded = CASES + [("high-risk", False)] + [("general", True)] * 100
critical = [row for row in expanded if row[0] == "high-risk"]
assert accuracy(expanded) > 0.95
assert accuracy(critical) < 1.0
"""),
    TechnicalCourse(
        ("Model adaptation and post-training", "Datasets and inference infrastructure", "Deployment and operations"),
        ("Specify a behavior where prompt changes are a reasonable baseline before considering an adapter.",
         "Describe a held-out slice and a serving constraint. Explain which one affects training versus deployment.",
         "Compare routing choices and write a rollback trigger in terms of latency and quality."),
        "Compare the router's decisions for a simple task and a high-risk task. Draft a separate held-out evaluation for any future fine-tune.",
        """
assert route({"complexity": 0.2, "risk": "low"}) != route({"complexity": 0.2, "risk": "high"})
""",
        AppliedExercise(
            2, "Train a rank-one adapter and evaluate held-out inputs",
            "A frozen two-output model returns the input vector. Fit two small vectors so their outer "
            "product adds a rank-one correction. Compare base and adapted error on held-out inputs, "
            "then reduce the training steps and rerun. This exercise uses a tiny linear model to make "
            "the update visible. A transformer has many more weights and training choices.",
            """
training = [(1.0, 0.0), (0.0, 1.0), (-1.0, -1.0), (2.0, 1.0)]
holdout = [(2.0, -1.0), (-2.0, 3.0)]


def target(point):
    x, y = point
    signal = 2 * x - y
    return [x + signal, y - 0.5 * signal]


def base(point):
    return list(point)


a = [0.1, -0.1]
b = [0.0, 0.0]


def adapted(point):
    hidden = sum(weight * value for weight, value in zip(a, point))
    return [value + weight * hidden for value, weight in zip(base(point), b)]


for _ in range(200):
    for point in training:
        residual = [prediction - wanted for prediction, wanted in zip(adapted(point), target(point))]
        hidden = sum(weight * value for weight, value in zip(a, point))
        gradient_hidden = sum(error * weight for error, weight in zip(residual, b))
        a = [weight - 0.04 * gradient_hidden * value for weight, value in zip(a, point)]
        b = [weight - 0.04 * error * hidden for weight, error in zip(b, residual)]


def squared_error(predict):
    return sum(
        (observed - expected) ** 2
        for point in holdout
        for observed, expected in zip(predict(point), target(point))
    )


base_error = squared_error(base)
adapted_error = squared_error(adapted)
print(f"Held-out squared error: base={base_error:.3f}, adapted={adapted_error:.3f}")
assert adapted_error < 0.1 * base_error
""",
        ),
    ),
    TechnicalCourse(
        ("Architecture and trust boundaries", "AWS and Azure implementations", "Portability and operating model"),
        ("Sketch the logical model, search, compute, and identity capabilities before picking services.",
         "Compare the AWS and Azure mapping. Identify which identity and data controls require verification.",
         "Map the same design to Google Cloud and assign an owner for each operational control."),
        "Compare the logical keys in the provider maps. Identify a capability that would need its own abstraction and conformance test.",
        """
maps = [architecture(provider) for provider in ("aws", "azure", "gcp")]
assert set(maps[0]) == set(maps[1]) == set(maps[2])
assert maps[0] != maps[1]
"""),
    TechnicalCourse(
        ("Documents, vision, and audio", "Generative media and bounded action", "Emerging systems and evidence"),
        ("Annotate one extracted document field with a page reference and one speech result with a time range.",
         "Define one review gate for a generated asset and one approval condition for an irreversible action.",
         "Write a falsifiable claim about a new capability and define the baseline and evidence needed."),
        "Inspect provenance and the confidence gate on the bundled evidence. Propose a separate review rule for records where confidence is unavailable.",
        """
assert all(item.source and item.page > 0 for item in items)
assert len(usable) == 1
assert usable[0].source == "report.pdf" and usable[0].modality == "table"
"""),
)


@dataclass(frozen=True)
class LearningPath:
    slug: str
    title: str
    level: str
    audience: str
    entry: str
    courses: tuple[str | int, ...]
    outcome: str
    capstone: str | None = None


PATHS = (
    LearningPath("00-ai-for-everyone", "AI for Everyone", "No code",
                 "People who use or encounter AI at work or in everyday life.",
                 "No programming, AI background, or AI account required.",
                 ("ai-literacy", "using-ai-at-work", "evaluating-ai-in-practice"),
                 "Complete an AI-use checklist, a reviewed draft, and a three-case scorecard with a bounded keep, revise, or stop decision."),
    LearningPath("01-product-technical-leader", "AI for Managers and Product Leaders", "No code · applied",
                 "Managers, product leaders, sponsors, and policy or operations teams.",
                 "Start here with basic AI literacy, or complete AI Literacy first.",
                 ("ai-literacy", "ai-product-decisions", "evaluating-ai-in-practice", "managing-ai-delivery"),
                 "Submit a one-page pilot decision with a baseline scorecard, launch guardrails, an accountable owner, and a pause rule."),
    LearningPath("06-software-engineer", "Software Engineer Building with AI", "Technical foundations",
                 "Developers adding model-backed features to existing applications.",
                 "Comfort with Python and automated tests. Start with Courses 01 and 02 if ML or basic algebra is unfamiliar.",
                 (3, 4, 5, 6, 7, 8, 9, 10, "model-backed-applications"),
                 "Demonstrate a source-grounded feature with a validated response, fallback, access boundaries, and a baseline comparison on frozen cases."),
    LearningPath("02-coding-agent-specialist", "Coding-Agent Specialist", "Intermediate",
                 "Software engineers building supervised coding workflows.",
                 "Python, testing, Git, and familiarity with model inference and retrieval, or finish the Software Engineer path.",
                 (5, 7, 8, 9, 10, "supervised-coding-harness"),
                 "Demonstrate a supervised change with a typed proposal, a failing and passing regression case, an approval record, and a replay check."),
    LearningPath("03-software-architect", "AI Systems Architect", "Advanced",
                 "Architects designing across applications, data, access, and operations.",
                 "System design, cloud identity, APIs, and familiarity with foundation models, search, and context engineering.",
                 (6, 7, 8, 9, 10, 11, 12, 13, "operating-ai-services"),
                 "Defend a design with an architecture decision record, threat model, service objectives, a measured canary, and a demonstrated rollback."),
    LearningPath("04-ml-engineer", "ML Engineer", "Advanced · model lifecycle",
                 "Engineers specializing in training, measurement, serving, and monitoring.",
                 "Working Python, basic statistics and linear algebra, and experience testing a model-backed service and working with APIs or containers. Courses 06–09 can fill gaps in application engineering before Course 10.",
                 (1, 2, 3, 4, 5, 10, 11, "model-selection-and-adaptation", "operating-ai-services"),
                 "Deliver a trained model artifact, held-out slice comparison against a baseline, an operating threshold, and a versioned release and rollback plan."),
    LearningPath("05-ai-engineer", "AI Engineer", "Advanced · full curriculum",
                 "Practitioners building, evaluating, deploying, and operating end-to-end AI systems.",
                 "Python, basic algebra, and time for implementation and a capstone.",
                 (1, 2, 3, 4, 5, 6, "model-backed-applications", 7, 8, 9, 10,
                  "supervised-coding-harness", 11, "model-selection-and-adaptation", 12, 13, "operating-ai-services"),
                 "Complete the AI engineer capstone and defend the system using evaluation and operations evidence."),
)


SPECIALIST_PATHS = (
    LearningPath(
        "model-selection-leaders", "Model Selection for Leaders", "No code · specialist",
        "Product owners, program leads, and sponsors making a model or vendor decision.",
        "Basic AI literacy and familiarity with pilot decisions, or start with AI Literacy.",
        ("ai-product-decisions", "evaluating-ai-in-practice", "model-selection-for-leaders"),
        "Submit a recommendation that ties one candidate to quality, economics, and launch conditions.",
        "model-selection-leaders-capstone.md",
    ),
    LearningPath(
        "forward-deployed-ai-engineer", "Forward-Deployed AI Engineer", "Specialist · customer delivery",
        "Engineers delivering a pilot inside a customer’s existing workflow.",
        "Complete Software Engineer Building with AI or bring equivalent Python, integration, and evaluation experience.",
        ("ai-product-decisions", 9, "model-backed-applications", "customer-pilot-engineering"),
        "Deliver an accepted synthetic customer pilot with a working intake integration and an operator handoff.",
        "forward-deployed-capstone.md",
    ),
    LearningPath(
        "llm-evaluation-model-selection", "LLM Evaluation & Model Selection Engineer", "Specialist · evaluation",
        "Engineers who own model comparisons, grading protocols, or release evidence.",
        "Basic statistics, Python, and experience building or evaluating a model-backed application.",
        (10, "model-backed-applications", "model-selection-and-adaptation", "llm-evaluation-benchmarks"),
        "Publish a paired comparison with agreed rating criteria and a defensible model or release decision.",
        "llm-evaluation-capstone.md",
    ),
    LearningPath(
        "retrieval-rag-engineer", "Retrieval & RAG Engineer", "Specialist · information retrieval",
        "Engineers responsible for enterprise search, knowledge-grounded features, and citation quality.",
        "Know basic embeddings and Python. Take Language and Representation if you need the vector search foundations.",
        (3, 6, 10, "model-backed-applications", "retrieval-system-engineering"),
        "Demonstrate a versioned, permission-aware retrieval pipeline and quantify its quality by stage.",
        "retrieval-rag-capstone.md",
    ),
    LearningPath(
        "agent-runtime-mcp-engineer", "Agent Runtime & MCP Engineer", "Advanced specialist · runtime",
        "Engineers building supervised, resumable workflows with tool interfaces.",
        "Comfort with Python, JSON, testing, and tool-calling basics.",
        (7, 8, "supervised-coding-harness", "durable-agent-tool-runtime"),
        "Build a tool-using workflow that waits for approval, survives restart, and avoids duplicate local effects.",
        "agent-runtime-capstone.md",
    ),
    LearningPath(
        "llm-adaptation-inference-engineer", "LLM Adaptation & Inference Engineer", "Advanced specialist · models",
        "ML engineers selecting and adapting models and measuring serving trade-offs.",
        "Python, basic linear algebra, and held-out evaluation. Start with Machine Learning Systems if these are unfamiliar.",
        (2, 4, 11, "model-selection-and-adaptation", "llm-adaptation-inference"),
        "Compare a frozen and adapted model against a retrieval baseline on the same held-out workload.",
        "llm-adaptation-capstone.md",
    ),
    LearningPath(
        "ai-reliability-release-engineer", "AI Reliability & Release Engineer", "Advanced specialist · operations",
        "Platform, ML operations, and reliability engineers operating model-backed features.",
        "HTTP, service telemetry, and basic evaluation. Complete the service practicum before the reliability lab.",
        (10, 11, 12, "operating-ai-services", "ai-reliability-release"),
        "Diagnose a staged release failure, restore the baseline, and produce an evidence-based incident review.",
        "ai-reliability-capstone.md",
    ),
)

PATHS += SPECIALIST_PATHS
