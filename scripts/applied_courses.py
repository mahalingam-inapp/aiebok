"""Original project courses and their lecture material."""
from course_types import Course, Lecture
from specialist_courses import SPECIALIST_COURSES


APPLIED_COURSES = (
    Course(
        "model-backed-applications", "Build and Evaluate a Model-Backed Application",
        "Build a source-grounded service desk assistant, measure its performance, and run a provider comparison.",
        "Python functions, JSON, and basic retrieval. See Prompt and Context Engineering and Knowledge and Retrieval Systems for background.",
        "Deliver a runnable assistant for a small public or synthetic knowledge base. Include representative questions, a deterministic baseline, and a decision memo comparing model or retrieval choices.",
        "Show a valid answer, insufficient evidence, restricted evidence, and a response that fails validation. Report retrieval recall, grounded answer accuracy, and fallback rates separately. Record model version and measurement conditions if you use a live model.",
        (
            ("Implement the contract and baseline", (
                Lecture(
                    "Model interfaces and structured output",
                    "Validate a model response and distinguish response-format errors from provider failures.",
                    "Define a small typed contract before choosing a model. Treat a response as untrusted input and validate each required field, value, and relationship. A malformed JSON reply and a provider timeout should both activate the fallback while remaining distinguishable in logs. Keep provider-specific code behind one callable.",
                    "A service desk assistant returns a status, a short answer, and source IDs. A reply with source_ids set to a string cannot satisfy the contract. A valid abstention has an empty answer and no sources.",
                    "Run the contract cases. Add a syntactically valid response with an unknown status and explain why JSON parsing alone accepts it.",
                    "Reject the status during semantic validation and test that the handler returns the same public fallback without losing the failure category internally.",
                ),
                Lecture(
                    "Retrieval, evidence and citations",
                    "Build a retrieval baseline, measure top-k recall, and enforce evidence scope before ranking.",
                    "Start with lexical retrieval over passages with stable IDs and explicit roles. Filter relevance candidates by permission before scoring, then check that model citations refer to the actual retrieved snippets. ID validation catches fabricated citations. Checking the answer against the passage is a separate step.",
                    "A travel-policy question may retrieve a correct current article and an unrelated reimbursement rule. Source IDs let you compare rankings against labeled expectations and inspect why the current article was missed.",
                    "Compare the results for an employee and a policy reviewer. Add a query with no answer in the allowed documents.",
                    "The employee never sees reviewer-only passages. The no-answer case returns no citations, even if the question is phrased fluently.",
                ),
            )),
            ("Measure and integrate", (
                Lecture(
                    "Grounding checks and evaluation slices",
                    "Run fixed cases through a baseline and candidate and attribute errors by stage.",
                    "Keep a frozen set of inputs with expected outcomes and evidence. Evaluate retrieval, citation support, and final decisions separately. Report per-slice counts so a class of failure cannot disappear in aggregate accuracy. Exact-match excerpts are a conservative support check for this exercise. Evaluate paraphrases with a human rubric before accepting them.",
                    "A candidate may retrieve the right policy yet cite an unavailable ID. That case passes retrieval but fails answer validation. A fallback preserves safety while still costing task completion.",
                    "Run both providers on the same cases and identify one case where retrieval succeeds but the provider reply fails its contract.",
                    "Keep the retrieval denominator restricted to answerable cases. Keep abstentions and invalid responses in the decision and fallback reports with their own counts.",
                ),
                Lecture(
                    "Compare a live provider with a local baseline",
                    "Use the same contract and cases with a model endpoint and record latency and workload conditions.",
                    "An endpoint adapter is useful only if it preserves request and result semantics. Use a timeout, record the endpoint and model version, and separate infrastructure failures from model-quality failures. Capture median latency with the number of runs and distinguish a cold first request from warmed requests.",
                    "A fast local baseline can quote retrieved evidence verbatim. A live model might respond naturally, yet a stricter validator might reject its phrasing. That difference belongs in the decision memo before selecting a backend.",
                    "Run the standard-library baseline. For the optional live run, start Ollama with an installed model and set AIEBOK_OLLAMA_MODEL to its local model name before launching Jupyter. The adapter calls the loopback generate endpoint and records any token counts returned.",
                    "The live path runs only when you configure a model. Keep the same cases and validation rules, and record the model, hardware, errors, and fallback count for interpretation.",
                ),
            )),
        ),
        workbook=True,
        resources=(
            ("Prompt and Context Engineering", "../../books/05-prompt-and-context-engineering/index.md"),
            ("Knowledge and Retrieval Systems", "../../books/06-knowledge-and-retrieval-systems/index.md"),
            ("Ollama generate API and local endpoint", "https://docs.ollama.com/api/generate"),
        ),
    ),
    Course(
        "supervised-coding-harness", "Supervised Coding-Agent Harnesses",
        "Build a reviewable harness around a proposed change and measure whether its checks catch regressions.",
        "Python and automated tests. Familiarity with specification-driven development and the agent loop is helpful.",
        "Demonstrate a supervised change to a deterministic formatter. Preserve its spec, structured proposal, regression report, approval decision, and replay record.",
        "Show that a wrong proposal fails before approval, an otherwise valid proposal waits, and a repeated approved request does not apply twice. Explain how your checks and review would transfer to a coding-agent framework.",
        (
            ("Specify and verify a candidate", (
                Lecture(
                    "Write an acceptance contract for a change",
                    "Turn a small change request into regression and acceptance examples.",
                    "An acceptance case states an observable input and expected output. Freeze current behaviors you want to preserve before asking for a change, and keep acceptance cases independent from any particular implementation. A small fixture makes a failing example cheap to inspect.",
                    "A task-title formatter should now remove redundant spaces. Existing lowercasing and empty-title behavior still matter. Add a fixture for tabs and a case that captures the default title.",
                    "Write one legacy case and one case that fails with the baseline.",
                    "The whitespace case should reproduce the new requirement. The legacy case should remain green after the change.",
                ),
                Lecture(
                    "Constrain proposals and run checks",
                    "Validate the shape and scope of a proposed change before running the acceptance suite.",
                    "A model can propose a typed change request without receiving a shell or arbitrary file-writing capability. In the workbook, a proposal selects one registered formatter. The harness rejects unknown actions and runs the same fixtures against each candidate. The review record retains test details.",
                    "A known but incorrect formatter lowercases text while preserving doubled spaces. It passes some existing behaviors and still fails the added requirement.",
                    "Evaluate an unknown proposal and a known incorrect candidate. Compare the failure categories.",
                    "An unknown proposal fails validation. A known candidate should return concrete test failures for the reviewer.",
                ),
            )),
            ("Approve and audit a change", (
                Lecture(
                    "Approval, revisions and replay",
                    "Bind an approval to the reviewed proposal and current revision.",
                    "Approval is a decision about a specific candidate and the state against which it was tested. Compare the reviewed revision with the current revision before applying the change. Store a stable request ID and outcome so retries can return the previous result without repeating the action.",
                    "A reviewer approves the whitespace change at revision 1. Another edit lands before approval is applied. The old approval now needs a fresh review.",
                    "Try applying a good proposal before approval. Replay after applying it and then try the old review against a newer revision.",
                    "Return a waiting result before approval, the recorded result on replay, and a stale result when a different request uses an older review.",
                ),
                Lecture(
                    "Compare workflow traces and handoffs",
                    "Use a fixed suite to compare proposals and design a human handoff with useful evidence.",
                    "Count validated proposals, test passes, approval waits, and applications separately. A trace should be detailed enough to reproduce the decision and compact enough for a reviewer to scan. In a framework, carry the proposal ID and revision through each transition and keep the executor boundary explicit.",
                    "Two candidates may look identical in a summary. A trace showing a failed whitespace case and a review approval against a specific revision distinguishes them.",
                    "Create a small report from the trace. Identify what the reviewer sees at each blocked stage.",
                    "The report should name the failed check or approval state and the next responsible person. Keep the evidence tied to the exact candidate.",
                ),
            )),
        ),
        workbook=True,
        resources=(
            ("Reasoning and Tool Use, including MCP", "../../books/07-reasoning-and-tool-use/index.md"),
            ("Agent Systems", "../../books/08-agent-systems/index.md"),
            ("Framework examples from Donner’s Agents repository", "https://github.com/ed-donner/agents"),
        ),
    ),
    Course(
        "model-selection-and-adaptation", "Model Selection and Adaptation Lab",
        "Train and compare a small text classifier using governed splits, task slices, cost estimates, and a release decision.",
        "Python, basic probability, and familiarity with held-out evaluation. See Machine Learning Systems and Training, Serving, and AI Operations.",
        "Deliver an experiment report and a saved classifier artifact for routing synthetic service requests. Compare a majority baseline with a trained model, inspect missed cases by slice, and justify an operating threshold.",
        "Demonstrate group-disjoint splits, fit the model only on train, pick the threshold on validation, and report the untouched test results. Include false positives, abstentions, an artifact round trip, and a regression gate.",
        (
            ("Prepare data and learn a baseline", (
                Lecture(
                    "Group-aware splits and dataset lineage",
                    "Split records by group and document lineage before training.",
                    "Allocate related examples to the same split. Grouping by source, customer, or template prevents paraphrases of one event appearing in both the train and holdout sets. Keep a version and record counts for each slice. A tiny fixture demonstrates the mechanics while leaving uncertainty visible.",
                    "Two requests copied from one campus support template share a group. Putting one copy in validation would make scores artificially optimistic.",
                    "Compute the group intersections across train, validation and test. Change one fixture so a group leaks across the split.",
                    "The leakage assertion should fail and identify the crossing group before fitting begins.",
                ),
                Lecture(
                    "Fit and compare a supervised baseline",
                    "Train a Naive Bayes text classifier and compare its decisions with a majority-class baseline.",
                    "Naive Bayes combines empirical class priors with smoothed token likelihoods. Use Laplace smoothing to avoid assigning zero probability to unseen terms. Compare with a majority baseline trained on the same partition. Its score puts any gain from text features into context.",
                    "A model trained on Wi-Fi and image-projector reports may learn the word projector. Spelling changes and overlapping words can still move its estimate unexpectedly.",
                    "Fit the two approaches on train. Print out predictions for validation and explain which words contribute to one mistake.",
                    "Keep priors and token counts tied to train. Explain the error rather than tuning directly on the test split.",
                ),
            )),
            ("Choose a threshold and package evidence", (
                Lecture(
                    "Measure selective risk and cost",
                    "Pick an abstention threshold on validation and report coverage and accuracy on test.",
                    "A selective classifier can hand uncertain cases to a person. Accuracy among answered cases can look high if the system answers very little, so report coverage alongside it. Use independently estimated costs for mistakes and reviews. Choose the threshold with validation data and freeze it before evaluating test.",
                    "If one mistaken route costs four minutes and a review costs one, a threshold may be valuable even when accuracy changes little. A small sample can only illustrate the trade-off.",
                    "Compare the tested thresholds. Increase review cost and see which threshold you would choose on validation.",
                    "Report accepted count, wrong accepted count, and handoffs on each slice. Explain any change through its expected operating cost.",
                ),
                Lecture(
                    "Version a model artifact and regression gate",
                    "Serialize a fitted model, reload it, and gate release using both quality and coverage.",
                    "Persist parameters, label order, model configuration, and dataset lineage. Check loaded predictions against the in-memory result. Gate on meaningful evidence and inspect slice sample counts before trusting a pass. Changing parameters or the decision threshold should produce a new artifact and reevaluation.",
                    "A new model achieves better accepted accuracy by deferring half the traffic. A minimum coverage requirement surfaces the extra operational burden.",
                    "Round-trip the model. Tighten the coverage requirement and observe when the gate changes.",
                    "Round-trip results should match exactly. Record a keep, revise, or release decision with the evaluated version and the reason.",
                ),
            )),
        ),
        workbook=True,
        resources=(
            ("Machine Learning Systems", "../../books/02-machine-learning-systems/index.md"),
            ("Training, Serving, and AI Operations", "../../books/11-training-serving-and-ai-operations/index.md"),
            ("Fine-tune and Serve build guide", "../../guides/fine-tune-and-serve.md"),
        ),
    ),
    Course(
        "operating-ai-services", "Deploy and Operate an AI Service",
        "Exercise a versioned service, fallback, canary, telemetry, and rollback in a local deployment.",
        "Python, HTTP, and evaluation basics. Familiarity with model-backed applications is helpful.",
        "Ship a local service and a release packet with an architecture decision, version routing, a smoke test, measured canary evidence, a telemetry schema, and an operator runbook.",
        "Demonstrate repeatable smoke requests, fallback under injected provider failure, a blocked canary, and a saved rollback decision. Describe how health checks, secrets, and telemetry would map to a selected hosting platform.",
        (
            ("Package and observe", (
                Lecture(
                    "Serve a versioned endpoint",
                    "Expose a local HTTP endpoint with explicit version and health behavior.",
                    "A model service has an externally testable contract and versioned implementation. Readiness answers whether the service may receive traffic. A smoke test sends a known request across the same transport the caller uses and checks the response and version.",
                    "A policy helper returns an answer or handoff plus the requested and served versions. A separate health endpoint lets routing detect an unavailable process.",
                    "Run the in-process application smoke check. Use the loopback HTTP smoke client in the final lecture to test the same contract through the network stack.",
                    "The response identifies the active version and health succeeds without invoking a model.",
                ),
                Lecture(
                    "Fallback, trace fields and durable telemetry",
                    "Record provider failures and successful fallback without storing request text.",
                    "A fallback may preserve availability while hiding primary failures from aggregate success. Measure the primary failure rate separately. Capture request ID, requested and served versions, elapsed time, and the fallback outcome. Persist the telemetry so the release gate can query it.",
                    "A candidate fails to answer during a dry run. The baseline serves it and the trace preserves the fact that a fallback occurred.",
                    "Trigger the bundled provider failure. Query the telemetry and check that sensitive request text is absent.",
                    "The stored row should show the candidate as requested and baseline as served with a fallback flag.",
                ),
            )),
            ("Release and recover", (
                Lecture(
                    "Canary evaluation and rollout decisions",
                    "Compare gated evidence and identify a canary that must pause.",
                    "A canary is a limited rollout of a labeled version. Define sample requirements, acceptable fallback or error rates, and a latency bound. Evaluate on traffic attributed to the requested version, so fallbacks do not improve the apparent reliability of the failing version.",
                    "If the candidate has two failures in ten comparable requests and the maximum is one in ten, pause even when all ten callers received some response.",
                    "Run the gate with a limited candidate cohort and compare its decision with normal traffic. The notebook uses a loopback request header to select the fixture cohort. In a deployed service, assign cohorts in trusted routing infrastructure.",
                    "An insufficient sample should fail with a coverage reason. A well-sampled unhealthy candidate should fail with the measured rate.",
                ),
                Lecture(
                    "Rollback and production handoff",
                    "Persist a version-pointer rollback and verify it through a local HTTP smoke test.",
                    "Rollback restores the previous serving version. Keep the decision durable and include it in the operator log. After changing the pointer, send a smoke request through the serving endpoint. In hosted environments, use a managed secret store, readiness checks, and an explicit release owner.",
                    "A blocked canary reassigns the production pointer to v1. After reopening its state store, the next request reports v1 and the decision log still contains the rollback.",
                    "Run rollback, reopen the store, and make a loopback HTTP health and prediction request. Write your runbook with the measurable trigger and post-rollback check.",
                    "The version pointer and decision survive reopen. The deployed service reports its baseline version through HTTP.",
                ),
            )),
        ),
        workbook=True,
        resources=(
            ("Cloud and Enterprise AI Architecture", "../../books/12-cloud-and-enterprise-ai-architecture/index.md"),
            ("Evaluation-gated release guide", "../../guides/eval-gated-release.md"),
            ("Staged cloud deployment from the Alex capstone", "https://github.com/ed-donner/alex/blob/main/gameplan.md"),
        ),
    ),
)


APPLIED_COURSES += SPECIALIST_COURSES
