"""Original workplace scenarios and their lecture-by-lecture case notes."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Moment:
    title: str
    scene: str
    reasoning: str


@dataclass(frozen=True)
class CourseCase:
    title: str
    opening: str
    moments: tuple[Moment, ...]
    field_note: str = ""


# Keys are book numbers or course slugs. Each scenario is fictional.
CASES = {
    1: CourseCase(
        "The alarms at 2 a.m.",
        "Priya is the overnight dispatcher for a regional transit agency. Last Friday, two reports about an elevator outage went into a low-priority queue. A separate report sounded urgent because it was written in all caps. The operations lead wants a smarter dispatcher. Priya wants disabled riders to reach a working station and wants the on-call engineer to receive fewer false alarms.",
        (
            Moment("Two queues, two kinds of success",
                   "Priya receives ‘Lift failed again, at North Gate.’ The same wording can mean a functioning lift has a recurring fault or that a passenger is currently stuck. Which decision is the system supposed to help her make?",
                   "Split the task into identifying the asset, estimating the situation, and deciding who owns the response. A summary can be accurate while the dispatch outcome is wrong. Measure time to the right responder and count missed urgent cases before judging the system by how well it writes."),
            Moment("Keep the rule the dispatcher can defend",
                   "A sensor reports that a passenger is trapped. A second report mentions a lift that has been ‘temperamental’. Priya can explain an immediate dispatch for the first case. The second case has many historical variations.",
                   "A hard rule is appropriate for the verified emergency because the consequence is clear. A learned classifier can rank ambiguous language for review. Keeping those decisions in separate layers also makes it possible to tell whether a bad outcome came from the policy or the estimate."),
            Moment("Draw the station before choosing a route",
                   "The shortest walking route to a working lift uses a gate locked after midnight. A noticeably longer route stays accessible. Priya must update the rider before asking maintenance for a repair estimate.",
                   "Represent gates and locks as constraints in the state graph. If a route search receives only distance, it can return an unusable route with a perfect distance score. Test the route on a changed lock state before comparing the search algorithms."),
            Moment("An average that hides thirty minutes",
                   "Five dispatches take 3, 4, 4, 5, and 30 minutes. The manager asks whether the new routing rule is faster. Priya remembers the passenger attached to the last number.",
                   "The median is 4 minutes and the mean is 9.2. They answer different questions. Compare typical speed with the fraction over a service deadline so a system can improve its average while still exposing an unacceptable tail."),
            Moment("A new station breaks the naming shortcut",
                   "The training set calls every lift near the old North Gate ‘NG’. A new station uses the same abbreviation for a bus stand. Early pilot accuracy looked excellent on a random sample of old tickets.",
                   "Hold out whole stations or newer periods. A random split can put near-duplicate messages in training and evaluation. Comparing results on an unseen station tests whether the routing behavior depends on a general signal or on a remembered abbreviation."),
            Moment("When an uncertain alert still needs action",
                   "The estimator assigns a 0.4 probability that a lift report is urgent. Manual review costs about two minutes. Leaving a rider stranded much longer would be far more costly than a review.",
                   "A probability estimate can inform two policies with different action costs. Route midrange scores to a reviewer and choose the thresholds using measured errors and staffing capacity. Check that 0.4 means something similar across the stations before carrying it into a new policy."),
        ),
        "support-assistants",
    ),
    2: CourseCase(
        "The repairs that arrive after moving day",
        "Daniel coordinates maintenance for a housing cooperative. Residents sometimes wait several days for a repair because the mobile form sends sparse descriptions into the same queue as rich phone reports. The board funds one pilot. Daniel can promise faster triage only if mobile requests and uncommon repair types see the same benefit.",
        (
            Moment("Define urgency before opening a notebook",
                   "The historical priority field reflects which jobs a supervisor eventually expedited. It also reflects who called repeatedly. Training directly on that field could teach the system to give quieter residents slower service.",
                   "Choose an operational label such as whether verified conditions demand a same-day visit. Establish a rules baseline using information available at intake. Inspect a small sample with the maintenance team before deciding whether older labels can be reused."),
            Moment("What gets more expensive when a threshold moves?",
                   "The model sees 100 urgent and 900 ordinary requests. Moving the priority threshold catches 8 more urgent cases and adds 35 ordinary cases to the priority queue.",
                   "The policy trade-off is measurable. Estimate effects on urgent misses and technician capacity separately, then ask who can absorb the additional reviews. A change that increases recall can still fail if it creates a queue long enough to delay all urgent work."),
            Moment("A cluster is a clue",
                   "An unsupervised analysis finds a tight cluster of short requests submitted in the evening. The model labels it ‘low detail’. The tenant liaison suspects these are residents using an accessibility setting on the form.",
                   "Read sampled requests before turning cluster labels into operational categories. Compare source and task variables and check stability after removing time of day. A useful cluster can describe a form problem that no repair model should learn from."),
            Moment("Watch the model learn who wrote the ticket",
                   "The neural model reads both description and channel. It quickly learns that phone reports are often urgent because a front-desk worker already screened them. A new contractor will begin transcribing all calls.",
                   "Retraining can reduce loss by learning an unstable shortcut. Compare a model with and without the channel feature and test it during a shift in intake practice. Preserve the option to use channel for monitoring even if the predictor should ignore it."),
            Moment("Ninety per cent overall is a poor handoff",
                   "The pilot routes 90 of 100 tickets correctly. The mobile slice contributes 8 of the 10 failures even though it contributes only 20 tickets. Daniel cannot tell whether the issue is short text or an old adapter.",
                   "Report per-slice denominators and inspect the serialized request reaching the model. Fix a contract if the text was lost. If it arrived intact, compare error types and availability of supporting fields before adding model complexity."),
            Moment("Assign the person who can roll back",
                   "A form release changes how the unit number is encoded. The model keeps scoring requests, but the technician tool cannot use half the routes.",
                   "Monitor the output contract and the completed handoff, not just model uptime. Tie training data, model, and form versions together. Give a named operator a reversible route to the queue staff already know."),
        ),
        "face-matching",
    ),
    3: CourseCase(
        "The library card that goes by three names",
        "Marisol runs a library’s multilingual help desk. Patrons call the same borrowing card a reader card, a library pass, or the local-language equivalent. A policy search that works for staff using official terms returns an unrelated event pass for visitors. The librarian asks the engineering team to preserve regional variation while giving patrons a source they can verify.",
        (
            Moment("What did the patron mean by ‘renew’?",
                   "A patron asks to ‘renew my pass’. Staff know that pass can mean a library card or an event ticket. The system has both documents in the catalog.",
                   "Treat ambiguity as a task condition rather than a vocabulary defect. A narrow follow-up distinguishes the objects with less risk than confidently retrieving one. Evaluate whether the system asks when necessary and whether the question moves the patron forward."),
            Moment("Preserve the distinction the source author made",
                   "A cleanup job strips accents and punctuation from each policy title. Deduplication now collapses two distinct records, and one community group loses its language edition.",
                   "Keep original source text and use normalized copies for lookup. Record language, revision, and transformations as provenance. Compare cases before and after normalization so a gain in matching does not hide a loss of access."),
            Moment("One character is not always one token",
                   "Two translated help requests have similar character counts. One consistently uses many more tokens in a model. The longer token sequence is truncated when the chatbot adds instructions and retrieved evidence.",
                   "Inspect tokenization with actual examples for each locale, then budget outputs and context accordingly. Monitoring characters alone will miss a token-boundary effect that people experience as shorter or less grounded answers."),
            Moment("When exact words are an asset",
                   "A permit guide mentions form R14. Similar language appears in three other forms. A dense result is semantically close but points to R40 rather than R14.",
                   "Use exact term and identifier evidence alongside dense retrieval. Favor semantic similarity for wording variation and preserve lexical signals for named entities and codes. Label both query types so the team can see where each approach helps."),
            Moment("Neighbors need a relevance test",
                   "‘Borrow a tablet’ and ‘borrow a laptop’ are close in an embedding model. The tablet policy has an age restriction the laptop policy does not.",
                   "Similarity proposes candidates. It does not establish which record is legally or operationally applicable. Compare nearest neighbors against metadata-filtered results using actual patron tasks."),
            Moment("An embedding upgrade has a migration window",
                   "Marisol switches a new model on for query encoding while overnight indexing still uses the old version. Individual requests complete, but useful results disappear for half the languages.",
                   "Version query and document vectors together. Build and test a second index before moving traffic. Keep a small per-language query set so the rollback decision does not depend on broad engagement changes."),
        ),
        "speech-recognition",
    ),
    4: CourseCase(
        "The meeting notes with the wrong owner",
        "Asha reviews action items extracted from messy project transcripts. A teammate named twice is incorrectly assigned ownership for a different task. She needs a way to explain the failure to the project lead and compare a small local model with a hosted candidate without asking the team to trust the larger model by default.",
        (
            Moment("The person named at the end",
                   "A decision begins on page one and ownership is assigned near the end. A sequence model that compresses history into a small state has little room for intervening discussion and the original thread.",
                   "Test short and long versions of the same transcript. If attribution worsens with distance, compare with a mechanism that can directly access earlier token representations. Hold the action item and speaker constant while changing the gap."),
            Moment("Attention can favor the wrong mention",
                   "The transcript mentions Jules twice in a budget discussion and once in the final ownership sentence. The extractor attaches the budget owner to the deliverable.",
                   "Attention creates input-dependent mixtures of representations. It does not guarantee the weighting reflects the role required by the task. Test with a transcript that repeats a distractor and check the observable owner assignment before using attention weights as an explanation."),
            Moment("Follow one representation through the block",
                   "Asha wants to know why replacing a name also changes the task category. The model passes contextualized representations from attention through other transformations before predicting.",
                   "Track tensor shapes and isolate one change in the input. Compare the resulting owner and category outputs. This connects the block-level mechanism to behavioral evidence without assuming any individual head is assigned a stable human-readable role."),
            Moment("Learn the task without seeing the answer key",
                   "The transcript collection contains meeting minutes and near-duplicate action-item exports. An evaluation set built from the same exports looks much cleaner than the actual meeting traffic.",
                   "Split by meeting series before creating windows, then deduplicate across splits. Keep evaluation examples from unseen teams and newer recordings. Otherwise a pretraining or fine-tuning comparison can reward memorization of workflow artifacts."),
            Moment("The selector needs repeatability",
                   "The team reruns the same transcript three times and sees two owners inferred. Asha can accept variation in notes phrasing, but an ownership field must stay grounded.",
                   "Tune output behavior by field and enforce constraints downstream. Measure owner consistency and correctness across repeated runs, rather than assuming a single low-temperature run establishes determinism or quality."),
            Moment("Choose a model with the reviewers",
                   "A hosted model wins on long transcripts. The local model matches it on ordinary meetings and can keep sensitive transcripts on the approved machine.",
                   "Route by evaluated needs and permission, then include review time and escalation rates in the model decision. A larger model has a defensible role if measured benefit exceeds latency and access costs for the actual workload."),
        ),
        "model-behavior-rollback",
    ),
    5: CourseCase(
        "The shift handoff that changed a date",
        "Noah runs scheduling for a community center. A writing assistant helps staff hand off room changes between shifts. When it turns ‘date pending’ into ‘next Thursday’, volunteers receive an incorrect message. Noah wants brief drafts while giving the next shift enough evidence to verify and approve them.",
        (
            Moment("Make the missing value part of the request",
                   "A prompt asks for a polished handoff. The notes establish which room closed but leave the reopening date pending.",
                   "Instructions should name the output, authoritative facts, and what to do when a value is missing. Compare drafts for the same notes with and without the missing-value rule. Look for grounded facts and time saved at review."),
            Moment("A valid field can still be a false commitment",
                   "An output includes a valid date format and the right room number. The date came from the assistant’s guess.",
                   "Use schema validation for required fields and format. Separately verify assertions against the source. An explicit unknown value lets the reviewer distinguish a pending date from one that the schedule confirms."),
            Moment("Which sentence deserves the last token?",
                   "The room-closure notice and a three-month-old maintenance summary compete for context. The old note is longer and includes convenient dates.",
                   "Budget for the current policy and evidence before adding conversation history. The next shift needs facts they can verify. Test a tight context window with the older source present to see what was dropped and why."),
            Moment("Memory needs a way to forget",
                   "A coordinator cancels a closure mentioned in a previous turn. The assistant repeats the old closure the next day as though it were a live decision.",
                   "Store confirmed, tentative, and superseded items differently. Retrieve by effective date and preserve who made a change. Provide correction and expiry paths instead of treating every prior statement as persistent truth."),
            Moment("A document can inform the model and still have no authority",
                   "An imported room note contains instructions aimed at the assistant alongside a legitimate closure update. Noah expects the room data to be usable and any instruction to remain untrusted.",
                   "Keep source content on the data side of the trust boundary. The approval or publishing action must check user permissions independently. Verify that the system can extract the update without acquiring authority from a document."),
            Moment("Save the evidence for the next revision",
                   "A prompt edit shortens drafts. The operator notices that follow-up messages now omit the uncertainty marker on pending dates.",
                   "Version the prompt, input fixture, output validation, and reviewer decision together. Put pending-date cases in a release suite and restore the previous configuration if a critical field regresses."),
        ),
        "bereavement-fares",
    ),
    6: CourseCase(
        "The policy that changed on Monday",
        "Imani answers employee reimbursement questions. On Friday the limit is $80. A policy update makes it $60 on Monday and adds an exception for approved field work. Old copies are still in email attachments. Imani wants one answer that shows its evidence and explains which rule applied when a purchase was made.",
        (
            Moment("A policy is state that can change",
                   "An employee made a purchase on Sunday and asks on Tuesday. The latest policy alone gives the wrong number for one of those dates.",
                   "Persist effective dates outside the model and resolve which revision applies to the requested event. Hold the question fixed and change the event date. The evidence selection should change even if the model and prompt stay identical."),
            Moment("A chunk starts halfway through an exception",
                   "The parser separates ‘except for approved field work’ from the limit it qualifies. Staff get a clean passage that omits the condition.",
                   "Retain document hierarchy and provenance while chunking. Test retrieval of a paragraph containing both the limit and its exception, then confirm that the assembly step keeps them together."),
            Moment("The right amount for the wrong expense",
                   "Searching for ‘field allowance’ returns a travel note because it contains both words. The reimbursement policy uses ‘approved field work’.",
                   "Compare lexical, dense, and filtered retrieval for this labeled query. Look at top-K recall before changing generation. If the necessary policy never arrives, a more fluent model can only conceal the upstream failure."),
            Moment("Reranking must keep the date attached",
                   "The current policy ranks first for relevance, but the employee’s purchase predates it. The reranker rewards text similarity and ignores effective dates.",
                   "Enforce eligibility before comparing relevance. Keep temporal and access checks as auditable filters, then compare rank quality only among eligible passages. This makes it easier to distinguish a missing candidate from a scoring error."),
            Moment("A citation can point to the wrong paragraph",
                   "The answer quotes $80 and cites the correct document title. The linked paragraph is from the new revision and says $60.",
                   "Verify the claim against the exact passage and revision. If the retrieved evidence does not establish what applied on Sunday, make that uncertainty visible and hand the case to Imani."),
            Moment("One index, two audiences",
                   "A finance-only reviewer note explains an exception. A regular employee should see the approved policy, while a finance reviewer can see both sources.",
                   "Apply access controls before retrieval or context assembly and maintain separate verification cases per role. Review caches, indexing refresh, and logs because an answer can be correct while evidence crosses an audience boundary."),
        ),
        "bereavement-fares",
    ),
    7: CourseCase(
        "A permit desk with three sources of truth",
        "Ravi wants to help permit clerks answer requests that span an address register, planning rules, and human approval. Some checks are deterministic. Some require evidence from more than one source. The clerk remains responsible for sending the final decision.",
        (
            Moment("Search only where choices change the outcome",
                   "One address has two parcel candidates. Another has exactly one registered parcel. Treating both as a large search slows the common case.",
                   "Use deterministic lookup for unique matches. Reserve a bounded candidate search for ambiguous inputs and score candidates using evidence the clerk can independently inspect."),
            Moment("The order of checks protects the counter staff",
                   "A plan starts by drafting approval and then checks whether the parcel is even in the jurisdiction. A polished draft can bias the subsequent review.",
                   "Make eligibility a dependency before drafting. Represent missing evidence as a reason to stop and test the plan with a parcel outside the jurisdiction so the workflow never creates a misleading approval draft."),
            Moment("A second pass needs independent evidence",
                   "A model proposes that a permit requirement has been met. Asking the same model if it agrees produces agreement even when the official record is missing.",
                   "Verify against a rule or a separate evidence source. Keep proposal and verification outcomes separate, and make one test where fluent wording accompanies missing proof."),
            Moment("Read access and write authority are different grants",
                   "The clerk’s assistant should be able to retrieve a parcel record but only a human reviewer can file the completed decision.",
                   "Make read and write separate tools with independent authorizations. Confirm the caller and target record at the service boundary. Verify the behavior with clerks who can read but lack filing authority."),
            Moment("A discovered tool is still a dependency",
                   "A connector’s lookup contract changes and starts returning a nullable address. The workflow used to assume the field was always populated.",
                   "Keep a compatibility check at the tool boundary and treat missing data explicitly. A protocol simplifies discovering capabilities, while the application still owns compatibility, permitted usage, and the fallback."),
            Moment("A second attempt should buy evidence",
                   "The first plan cannot disambiguate two parcel candidates. Ravi can pay for another reasoning pass or ask the clerk for one missing field.",
                   "Compare expected resolution time and review cost. A second call is justified if it can use new evidence or recover from a transient failure. If the address register lacks a field, a human clarification is more useful."),
        ),
        "paused-jobs",
    ),
    8: CourseCase(
        "Tuesday's volunteer calendar",
        "Lena coordinates a volunteer program. Choosing a candidate schedule can be flexible, but publishing repeated or unapproved calendar changes wastes other people’s time. She needs the workflow to survive overnight outages with a comprehensible activity history.",
        (
            Moment("Decide which step needs discretion",
                   "The notice period and shift duration are fixed. Finding candidates is ambiguous because volunteers describe availability in natural language.",
                   "Use a fixed workflow for constraints and approval. Bound a model-assisted step to interpreting availability and suggesting candidates. Test each transition without requiring a model call."),
            Moment("A loop that stops early is often the right result",
                   "The scheduler has exhausted its candidate slots and considers asking a calendar tool again despite unchanged inputs.",
                   "Make progress observable and set a stopping condition tied to budget and evidence. A stop with an explanation and a next action gives Lena something to work with. Repetition without new state gives her a delay."),
            Moment("The service is back after midnight",
                   "An approval arrived before the worker restarted. The schedule proposal and its approval must stay paired after recovery.",
                   "Persist the reviewed proposal, the decision, and the next valid transition. Exercise restart separately from replay so the team can check both continuity and duplicate prevention."),
            Moment("A review step protects the moment a draft becomes a commitment",
                   "A general-purpose planner suggests a shift swap. It is plausible but violates a commitment to a volunteer made off-platform.",
                   "Use a draft–review–publish workflow and make the evidence available at the approval step. The person reviewing the proposal needs to see affected shifts and who will be notified."),
            Moment("Two specialists disagree",
                   "One agent optimizes staffing and another minimizes changes to volunteers’ schedules. Both proposals pass their own tests.",
                   "Define a shared outcome and an explicit conflict-resolution rule. Let a reviewer see the trade-off instead of adding more agents. Track who made the final decision and which constraints they accepted."),
            Moment("Late results are still real results",
                   "A calendar operation times out and returns success after the worker is ready to retry. Volunteers are already seeing a new shift.",
                   "Use a stable operation identifier and inspect the external result before retrying an uncertain effect. Record whether it was completed, pending, or requires reconciliation so the operator knows what to do after restart."),
        ),
        "paused-jobs",
    ),
    9: CourseCase(
        "The pull request nobody has time to review",
        "Nadia’s scheduling team is asked to use a coding assistant to clear its backlog. The first demonstration creates a large change quickly. Reviewers now spend longer understanding the diffs and correcting edge cases. Nadia needs evidence that the entire workflow is getting better.",
        (
            Moment("Follow the wait through the whole workflow",
                   "A developer can draft a change in ten minutes, yet code sits three days awaiting a domain reviewer. More drafts make the queue worse.",
                   "Observe elapsed time from request to accepted change. If the constraint is review capacity, reduce diff size or automate evidence collection before paying to increase code output."),
            Moment("Define what should happen before touching the code",
                   "A roster change should let users trade shifts, but managers ask who may confirm a swap. The example decision in the ticket leaves that open.",
                   "Write observable acceptance cases for both allowed and denied actions. Clarify which person owns the rule before implementation. Then use the tests to hold the assistant and human implementation to the same standard."),
            Moment("Make the reviewer’s job concrete",
                   "The assistant proposes rewriting a scheduler and several unrelated files. The change is hard to validate, and nobody can tell which edit solved the original issue.",
                   "Use small proposals with a scoped diff, tests, and assumptions. Read the diff before expansion and ask for a separate change when behavior outside the agreed task would move."),
            Moment("A passing example can leave a critical gap",
                   "The output shape is correct and happy-path tests pass. The assistant silently approves a duplicate shift swap on a retry.",
                   "Add a replay case and assert the business effect count. Keep fixture inputs and workflow versions fixed when comparing changes. Test that the race or retry does not simply disappear from logs."),
            Moment("A person needs an escape route",
                   "The new screen suggests a confident schedule but hides the reason a shift cannot be filled. A coordinator has to start over to make a manual correction.",
                   "Expose uncertain or rejected suggestions with their reason and permit editing in place. Measure recovery time and successful corrections in the pilot, not only whether people turned the feature on."),
            Moment("Publish the denominator",
                   "The team reports 30 assistant-generated changes. Twenty were abandoned or rewritten after review. Nadia wants to know whether total effort changed.",
                   "Include failed attempts and rework in the comparison. Use realistic tasks that cover experience levels and task sizes, then measure accepted changes per reviewer hour and defects discovered after merge."),
        ),
        "coding-productivity",
    ),
    10: CourseCase(
        "The pilot that passed on average",
        "Simone, a support operations lead, is asked to sign off an assistant that scores 96% on a broad test. Its mistakes concentrate on requests that change a customer’s eligibility. The launch sponsor sees a headline number. Simone sees a high-consequence decision being delegated without enough evidence.",
        (
            Moment("A critical failure needs its own criterion",
                   "Routine requests dominate the report. A wrong eligibility answer can commit money while a wrong greeting is easy to repair.",
                   "Define severe failures and release gates before the overall average is calculated. Require adequate examples and clear review ownership for the high-consequence slice. A strong routine score alone cannot establish that slice is safe."),
            Moment("Two reviewers read the same answer differently",
                   "One reviewer grades the policy conclusion, another grades clarity. Their mean scores agree and their individual ratings do not.",
                   "Write an observable rubric for each dimension and ask both reviewers to rate a small shared sample. Inspect disagreements and label cases independently before averaging."),
            Moment("Locate the failure before editing the prompt",
                   "An eligibility exception is correctly fetched but discarded during context assembly. The answer is then wrong despite a successful retrieval hit.",
                   "Measure retrieval, assembly, and final output separately. A trace that names the selected evidence can identify the broken stage. Freeze the failing example so a later prompt change cannot conceal the regression."),
            Moment("Treat the action boundary as part of the test",
                   "A support transcript contains untrusted text and the assistant can also retrieve restricted information. The workflow owner wants useful summaries without giving transcript text authority.",
                   "Keep read permissions and action approvals independent of generated content. A test should prove that the resulting action stays within the caller’s rights and that policy-relevant transcript text still reaches the summary."),
            Moment("Measure who has to fix the misses",
                   "Two customer groups see the same response rate, but one group must contact support more often to resolve wrong answers. The extra work does not appear in the model score.",
                   "Track errors and correction burden per slice. Include an escalation route, collect representative cases, and assign ownership for decisions that a person can appeal."),
            Moment("What would the reviewer need six months later?",
                   "The launch meeting authorizes a limited trial. A new manager cannot find which version was approved or which failures would require a pause.",
                   "Store the version, evidence, decision owner, allowed scope, and rollback conditions together. This is the record people need to investigate an outcome after the original reviewers have moved on."),
        ),
        "model-behavior-rollback",
    ),
    11: CourseCase(
        "The supplier assistant that learned last year’s policy",
        "Wei operates an assistant for a purchasing team. The team wants a consistent approval format and accurate current pricing guidance, but contract terms can change weekly. A pilot must also survive peak workload on order day with an identifiable release and rollback decision.",
        (
            Moment("Separate changing facts from persistent behavior",
                   "The assistant skips a required approval field and also gives an outdated contract amount.",
                   "A structured constraint or adaptation can improve the recurring format. The current amount belongs in versioned retrieval. Test the two behaviors separately to avoid paying to retrain the model whenever a contract changes."),
            Moment("Adapting the model can improve the wrong thing",
                   "A tuned version matches the training examples more closely. Reviewers notice it now sounds certain when an approval is missing.",
                   "Hold out realistic new requests and include abstentions in the behavioral criteria. Compare the base and adapted versions on formatting and uncertainty independently before interpreting a loss improvement."),
            Moment("Remove the answer from the training window",
                   "The submitted record contains both a draft and the later reviewer correction. Splitting by row puts variants of one supplier request into both training and evaluation.",
                   "Group by supplier and workflow before splitting. Version the transformation that decides which fields would have existed at inference time. Track excluded examples so the next run can reproduce the data decision."),
            Moment("Latency belongs to the workload, not the badge",
                   "The model serves short requests quickly but slows when 30 long contract excerpts arrive together. The queue grows during peak order entry.",
                   "Separate arrival rates, input length, generation work, and wait time. Compare a small candidate with batching or input limits on a representative mix before assuming a single hardware change solves the bottleneck."),
            Moment("Make fallback independent enough to help",
                   "The primary candidate times out during payroll. Its fallback uses the same overloaded service and fails during the same window.",
                   "Test a degraded mode that can run under different constraints, even if it only creates a review task. Verify that the user sees the status and knows who owns the next action."),
            Moment("Ask where the regression entered the pipeline",
                   "Operations sees fewer correct citations after a release. The checkpoints, quantization, and document index were all updated together.",
                   "Record all relevant versions and change them separately where possible. Compare slices and retrieve-stage evidence before restoring the right artifact or rerouting to the prior configuration."),
        ),
        "model-behavior-rollback",
    ),
    12: CourseCase(
        "Recovery day at a public utility",
        "Fatima designs a policy assistant for a utility. Field staff sometimes work with a poor connection. The legal team needs auditable access and the operations team needs a safe recovery path if a managed service or deployment is wrong. Her architecture review starts with those needs and then considers cloud capabilities.",
        (
            Moment("Start with the capabilities the crew needs",
                   "A field worker must view current procedures on a weak connection and know which revision they have. The design review starts by comparing three vendor product names.",
                   "Draw data, identity, retrieval, and recovery boundaries first. Then map capabilities to products. The weak-connection case may call for a timestamped local view, regardless of which platform serves the assistant."),
            Moment("Permissions need to travel with the data",
                   "A shared policy index serves managers and contractors. A contractor’s result should never depend on a policy document they cannot read.",
                   "Propagate caller, role, and source access into retrieval and testing. Check the same question for distinct roles and verify logs and caches keep the boundary too."),
            Moment("Plan a dependency failure before choosing a managed stack",
                   "One embedding service falls behind during a reindex. Field staff could still use approved keyword search to locate procedures.",
                   "Tie each managed dependency to a service boundary and test a reduced-capability path. Compare recovery and observability as part of platform selection, alongside cost and ease of provisioning."),
            Moment("Review the person behind each role assignment",
                   "An identity integration grants broad access to an operations group that includes short-term vendors. The demo accounts all belonged to permanent staff.",
                   "Test real role categories and lifecycle transitions, such as an expiring assignment. Ensure emergency access is auditable and revocable before trusting any platform’s default group mapping."),
            Moment("Portability includes export and restore",
                   "The organization can export prompts and documents, but its indexes, evaluations, and permission maps live in provider-specific formats.",
                   "Decide which artifacts must be portable and test their restore path. Migration risk is visible only when a second deployment reproduces the relevant behavior and access boundaries."),
            Moment("Write the runbook for the person on duty",
                   "An upstream service goes down during a weekend. Both teams think the other team owns approval to roll back.",
                   "Name who detects, who decides, and who verifies recovery for each dependency. Practice the handoff so a real outage does not become the first test of team ownership."),
        ),
        "unisuper-recovery",
    ),
    13: CourseCase(
        "The records that weren’t written for a model",
        "A public archive lets researchers search handwritten forms, meeting recordings, and plain-text transcripts. Elise, the archivist, notices that one exhibit is overrepresented because its pages scan cleanly and its speakers use standard studio audio. The team wants useful discovery while letting users see where evidence is uncertain or incomplete.",
        (
            Moment("Two lines can become one wrong record",
                   "A faded form places a name above its address. The vision system reads the lines correctly but attaches the address to the neighboring record.",
                   "Evaluate field extraction and record association separately. Preserve page and region references so reviewers can inspect low-confidence mappings rather than only correcting text."),
            Moment("A transcript can hide where the audio failed",
                   "The system transcribes the chair well but breaks down on remote participants who have noisy connections. A smooth transcript misattributes one decision.",
                   "Slice by speaker and recording condition, and check whether meaning survived rather than only counting word errors. Keep a link to the source time range for a reviewer."),
            Moment("Generated visuals need provenance and editorial choice",
                   "The team creates a period-style reconstruction for a public exhibit. A reader mistakes it for an archival photograph.",
                   "Record and disclose provenance at publication. Evaluate whether the reconstruction supports the intended explanation and whether labeling remains visible when the image is shared or cropped."),
            Moment("A visible button can still change a real record",
                   "An experimental tool proposes editing an archive entry after spotting an apparent typo. The field may contain the historical spelling that curators need to keep.",
                   "Make inspection read-only by default. Put the proposed change and supporting evidence in front of an authorized reviewer. Check recoverability and expected state before applying an approved edit."),
            Moment("A longer context window can hide missing retrieval",
                   "A model receives a long transcript but overlooks a brief correction two-thirds of the way through. Flipping to a bigger context window raises cost without fixing the omission.",
                   "Place a known correction at different positions and measure whether the answer uses it. Compare targeted retrieval with the longer window using the same corrections and authority decisions."),
            Moment("A frontier benchmark can miss the archive",
                   "A new model wins a public image benchmark and fails on faded handwritten entries from one exhibit. Elise needs a decision for that collection.",
                   "Add a small labeled set from the actual archive with a process for checking errors and coverage. Record format, model version, and what reviewers had to correct before deciding which workflow to deploy."),
        ),
        "speech-recognition",
    ),
}


CASES.update({
    "ai-literacy": CourseCase(
        "A message from the school office",
        "Amal helps at a school office. A water outage closes a building with little notice. Parents need a short message explaining what has changed. The head teacher has confirmed today's closure and promised a further update, so Amal needs to decide what an AI writing tool can safely help with and what must still come from the school.",
        (
            Moment("A draft and a decision are different jobs",
                   "Amal can ask a tool to simplify the closure notice or ask it what the district will decide tomorrow. Only one of those requests takes a confirmed decision as an input.",
                   "Rewriting confirmed information can save time because Amal can compare the draft with the original. A model's prediction about reopening cannot substitute for a decision by the school. Look for who has access to the relevant facts and who has authority to act."),
            Moment("Check the detail a parent would act on",
                   "The draft says the building reopens tomorrow morning. It reads naturally and has the right school name. The head teacher's message says the next announcement will be tomorrow morning.",
                   "Read the two sentences side by side. An update time became a reopening time. Restore the distinction and give families the official update channel. One uncertain detail can matter more than the quality of the rest of the message."),
            Moment("The safest first use still saves time",
                   "Amal considers using the same service to translate a short public message and to decide which students should receive an accommodation.",
                   "Begin with a reversible drafting task and arrange a competent review of names, dates, meaning, and accessibility. Eligibility decisions need the school's policy and a responsible person with authority. The convenience of a tool does not extend its authority."),
            Moment("Remove a detail if it does no work",
                   "Amal wants to paste the parent mailing sheet to tailor the draft. The public announcement can be written without children's names or contact details.",
                   "Provide the public facts and an audience description instead. Before sharing a file, check whether each field changes the task outcome and what your organization allows. Replacing names alone can leave combinations of details that still identify someone."),
        ),
        "bereavement-fares",
    ),
    "using-ai-at-work": CourseCase(
        "The neighborhood workshop moves indoors",
        "Maya coordinates a free weekend workshop. She needs to move it indoors and notify participants in simple language. The new room is confirmed, the accessible entrance is still being checked, and a colleague will review the announcement before publication.",
        (
            Moment("Give the assistant the job you would give a colleague",
                   "Maya has confirmed the address, room number, and start time. An earlier message lists a side entrance, but the facilities team has not confirmed it.",
                   "Separate verified facts from pending details in the brief. Say who will read it, what the reader needs to do, and which uncertainty must stay visible. For the entrance, ask the draft to say accessibility directions will follow."),
            Moment("An attractive draft can still fail one line",
                   "The draft adds ‘plenty of parking’ and changes the start from 10:30 to 10:00. The colleague says the tone sounds perfect.",
                   "Mark claims that could change what a participant does. Trace each one to a source and remove unsupported additions. Review usefulness and factual support separately so a pleasant tone does not hide the wrong start time."),
            Moment("Hand off the problem with context",
                   "Facilities confirms the entrance but asks Maya to verify a portable ramp. The publication deadline is in 15 minutes.",
                   "Send the reviewer the draft, the confirmed entrance, the unanswered ramp question, and the time the notice must go out. Give the reviewer a safe interim option such as publishing confirmed details with a contact for accessibility questions."),
            Moment("Count the time your colleague spent",
                   "A manual announcement takes 14 minutes to write and 4 to review. The tool drafts it in 3 minutes but the reviewer needs 11 minutes to check it.",
                   "The draft workflow totals 14 minutes rather than 18, a saving of four minutes in this example. Compare material corrections too. Time saved in drafting alone would make the change look much larger and miss the shift in who did the work."),
        ),
        "support-assistants",
    ),
    "ai-product-decisions": CourseCase(
        "The clinic’s front desk is drowning in repeats",
        "Kavita manages a clinic front desk. The team spends part of each shift answering questions about location, hours, and appointment preparation. A sponsor suggests an assistant for every inquiry. Kavita needs a narrower pilot that relieves staff without steering people toward the wrong appointment process.",
        (
            Moment("Name the wait before naming the technology",
                   "Callers asking for hours wait in the same queue as callers who need staff attention. A new app would be visible to sponsors, but it is unclear which part of the queue it would improve.",
                   "Observe one shift and count repeat questions, time to answer, and which requests staff redirect. Pick a bottleneck such as routine lookup, then compare ways to reduce it before allocating scope to AI."),
            Moment("Choose the least complicated useful option",
                   "Hours and location change on a known schedule, while some preparation questions depend on a document and need a staff check.",
                   "Use a maintained lookup for fixed facts and compare a search answer for document-based questions. Allow generated summaries only where they can cite the same material and where a responsible reviewer can handle ambiguity."),
            Moment("Measure the cases people would regret getting wrong",
                   "A pilot deflects more calls, but one caller reaches the wrong appointment queue because a preparation question was treated as a general one.",
                   "Keep deflection as a benefit metric. Add a separate gate for wrong routing on consequential cases and measure successful handoffs. Decide before launch which errors pause the trial."),
            Moment("Sign the limited decision you can defend",
                   "The pilot saves time on hours and directions. The preparation slice has too few cases and a missed handoff. The sponsor wants to expand to all inquiries.",
                   "Approve only the range supported by the evidence, if the appropriate owner agrees. Keep preparation questions with staff and collect a separate review set. Write the stop rule and who can invoke it."),
        ),
        "support-assistants",
    ),
    "managing-ai-delivery": CourseCase(
        "Friday's municipal service launch",
        "Sofia owns a pilot that routes resident reports to city departments. The trial includes routine reports about streetlights, alongside accessibility and urgent road hazards. She has one staff reviewer on Friday and needs to decide which parts can launch, who will watch them, and how to stop safely.",
        (
            Moment("The same average hides two experiences",
                   "The trial gets 90 of 100 reports right. It misses 4 of 10 urgent reports and 6 of 90 routine reports.",
                   "Compare the urgent miss rate of 40% with roughly 7% for routine reports. The overall score does not describe either group. Require a separately justified decision for urgent routing."),
            Moment("Three owners, three different decisions",
                   "The supplier knows the tool, the routing team owns the guidance, and residents need someone in the city to resolve mistakes. Each assumes another group signs off.",
                   "Name who can approve a policy change, who watches the rollout, and who can switch routing back to manual. Give residents a named point of contact or clearly staffed queue. A vendor escalation alone does not resolve today’s report."),
            Moment("Simulate the stop before expanding",
                   "A limited rollout can be paused by switching a queue configuration. The reviewer has never checked whether reports already in flight return to the manual queue.",
                   "Practice rollback with a test report submitted immediately before the switch. Confirm it is visible to staff and stays associated with its original identifier. Write down who owns the in-flight work."),
            Moment("Resume only after checking the original failure",
                   "A pilot route is paused after several urgent reports land in general intake. The supplier ships a configuration change and reports that its health check is green.",
                   "Ask for evidence that the original urgent cases now route correctly and that staff can handle a manual fallback. Record the decision and resume within a small cohort until operational evidence is available."),
        ),
        "model-behavior-rollback",
    ),
    "evaluating-ai-in-practice": CourseCase(
        "Six notices and one deadline that matters",
        "Ben coordinates notices for a volunteer group. He compares his current writing process with an assisted workflow that drafts messages from source notes. He wants a small scorecard that distinguishes easy notices from cases where a wrong claim could send people to the wrong place.",
        (
            Moment("Choose a case that can reveal a weakness",
                   "Ben’s first three examples are routine meeting reminders. None contains a canceled plan or an unresolved detail.",
                   "Sample typical work and add cases a polished draft could get wrong. For example, include a notice with no confirmed date, one with a late change, and one with private detail that should stay out."),
            Moment("An omission can be an error even when every sentence is true",
                   "A rescheduling notice states the correct new room. It leaves out the closed entrance, so someone using that entrance cannot act on it.",
                   "Score required information as well as accuracy of stated claims. Use the same requirement list for manual and assisted drafts. Record why a reviewer rejected the output and whether the source itself was incomplete."),
            Moment("Where did the saving go?",
                   "The tool saves eight minutes drafting a notice. Ben then spends five minutes verifying details and four minutes making corrections.",
                   "This draft took one minute more than the baseline once the extra review work is included. Keep a time column for each stage and count which corrections were consequential. Do not remove aborted drafts from the comparison."),
            Moment("Make every recommendation conditional on what you saw",
                   "Routine notices pass and save time. The tool gets one time-sensitive notice wrong. Ben has too few cases to estimate how often that will happen.",
                   "Record a limited use decision for routine work and keep time-sensitive notices on the manual path. Say what extra evidence or workflow change would make you reconsider."),
        ),
        "support-assistants",
    ),
    "model-selection-for-leaders": CourseCase(
        "Three model demos, one procurement memo",
        "Luis is buying support for a small policy help desk. The fastest vendor demonstration is persuasive, the careful candidate is expensive, and the team still needs a person to approve sensitive answers. Luis must turn the demos into a fair trial and recommendation.",
        (
            Moment("All candidates need the same questions",
                   "One vendor showed routine policy lookups. Another was asked about an unclear exception. Their demo outcomes are hard to compare.",
                   "Write the task and sources once and use the same held-out cases for every candidate. Include an exception where the expected behavior is to hand off. Agree which mistakes are unacceptable before looking at scores."),
            Moment("A perfect tiny sample is provisional",
                   "Two testers agree that one candidate passed both critical checks. Its sales lead claims a perfect critical accuracy rate for future traffic.",
                   "Record the denominator and scope. Two pass cases are evidence about those two inputs. Ask for more cases from the actual workload and for examples where graders initially disagreed."),
            Moment("Count the cost of an answer that still needs fixing",
                   "A candidate costs 12 units for a run and gives 9 acceptable answers. A second costs 20 units and also gives 9, but its reviewers spend less time correcting outputs.",
                   "The measured service costs are about 1.33 and 2.22 per acceptable answer. Compare them after adding reviewer time at a consistent rate. Keep costs and critical failure gates separate."),
            Moment("A trial approval needs a way back",
                   "The preferred candidate meets the speed budget for routine cases. Its results for another language are still unknown.",
                   "Record the approved audience, who verifies outputs, the failure that pauses use, and what evidence permits a broader rollout. A defensible recommendation can include a manual path for untested work."),
        ),
        "coding-productivity",
    ),
    "model-backed-applications": CourseCase(
        "The answer the help desk can stand behind",
        "Mei builds an assistant for policy questions. Users expect a short decision and a source. Her manager wants a pilot, but a false answer can force an employee to repeat a claim. She sets out to test the model path, the fallback, and the evidence people receive.",
        (
            Moment("Read a reply as a contract",
                   "One provider returns prose where the app expects a structured reply. Another returns the right format with an unsupported decision.",
                   "Validate shape before consuming the response. Then validate what the response claims separately. A timeout and a malformed reply can both fall back safely while retaining different diagnostic reasons."),
            Moment("Retrieve only evidence the requester can see",
                   "A reviewer can see a private payroll policy. A normal employee asks the same question and deserves a public answer or a clear handoff.",
                   "Filter evidence by role before ranking and validate each citation against material actually available to the response. Test both roles using the same question so a retrieval success never excuses a permission failure."),
            Moment("Track the point where the answer went wrong",
                   "The right paragraph is in the retrieved set, but the assistant cites a source it never saw. Overall accuracy does not tell Mei which fix is needed.",
                   "Separate candidate recall, citation validity, and final behavior. Keep the same cases for each model and record a distinct abstention reason. That makes it possible to improve a prompt without masking a retrieval regression."),
            Moment("Compare live results without changing the experiment",
                   "The local fixture responds instantly. A working model gives richer phrasing and slower answers, while some outputs fail the exact quote check.",
                   "Keep corpus, cases, and validator fixed. Record runtime and measurement conditions separately from answer quality. If you want to accept paraphrases, add a rubric and test that change rather than silently relaxing it for one model."),
        ),
        "bereavement-fares",
    ),
    "supervised-coding-harness": CourseCase(
        "Someone has to approve the formatter change",
        "Tomas maintains a help-desk formatter that other teams depend on. He wants to accept small assistant-suggested changes while showing reviewers what changed, what was tested, and why a repeated request cannot apply twice.",
        (
            Moment("Protect an old behavior on purpose",
                   "Whitespace should collapse in tickets. Empty inputs must still go to review. The first suggested change disregards the legacy behavior.",
                   "Write acceptance cases before implementation. Include a failing case that demonstrates the new requirement and a passing case for what people already expect."),
            Moment("A known proposal can still be wrong",
                   "A candidate uses a permitted operation but changes a part of the workflow outside the requested format. It passes a general style check.",
                   "Validate scope and run focused regression cases separately. Do not give an assistant arbitrary execution authority for a narrow formatting task. Give the reviewer the failing case and a small diff."),
            Moment("Approval expires when the reviewed payload changes",
                   "A reviewer approves a proposed revision in the morning. A later edit changes the payload before the worker applies it.",
                   "Bind approval to the exact reviewed revision and record a stable request identifier. A stale approval should cause a new review. A retry of an already applied version should return its recorded outcome."),
            Moment("Make the result make sense in the morning",
                   "The on-call engineer finds that three proposals were blocked. A log with only ‘false’ leaves the team guessing why.",
                   "Record the proposed revision, check result, owner, and next action. Distinguish an invalid proposal from pending approval and an applied replay so another colleague can safely continue."),
        ),
        "coding-productivity",
    ),
    "model-selection-and-adaptation": CourseCase(
        "A campus queue nobody wants to call twice",
        "Hassan is piloting a routing classifier for campus support. Some students submit one short sentence from a phone. The help desk wants to resolve requests faster and wants difficult cases to reach a person instead of being routed confidently to the wrong queue.",
        (
            Moment("Put related incidents in the same split",
                   "Several students use the same residence template for a network issue. Randomly splitting individual tickets leaves near copies in training and test.",
                   "Group by site and incident pattern where possible. Keep related records together and report those grouping decisions with the split. A realistic holdout includes unfamiliar phrasing."),
            Moment("Make the baseline live through the same workload",
                   "The trained classifier beats the majority rule on examples written by staff. Its lead is uncertain on short student messages.",
                   "Fit both choices on the same training scope and compare on the same validation cases. Look at errors by source and length. A gain on polished examples may be irrelevant to workload routing."),
            Moment("A better accepted score may cost more",
                   "A stricter threshold improves accuracy among answered cases and doubles the cases sent to the help desk.",
                   "Report accepted error, coverage, and review workload together. Choose the threshold on validation using an explicit error and handoff cost, then report results on held-out cases once."),
            Moment("Save what the operator will actually run",
                   "The model artifact reloads correctly. Another team loads it with a different threshold because that setting was stored in a notebook cell.",
                   "Version parameters, preprocessing, threshold, and split evidence together. Run an artifact round trip and a gate check so the deployed decision matches the one that reviewers evaluated."),
        ),
        "face-matching",
    ),
    "operating-ai-services": CourseCase(
        "When a successful response is really a fallback",
        "Helena operates a review assistant for a utility. A canary route starts timing out. Callers still get responses from a fallback, so the dashboard looks healthy until staff report that manual review queues are growing.",
        (
            Moment("Probe the route the caller will actually use",
                   "The service reports ready. A smoke request through the public interface gets the wrong version because routing wasn’t updated.",
                   "Probe readiness and the actual versioned response separately. Record caller-visible status and active version. It is possible for every component to be up and for the customer-facing route to be wrong."),
            Moment("Tell the operator what the fallback did",
                   "The fallback returns a result, but Helena sees only a successful transport status. The primary is still failing and work handed to staff is piling up.",
                   "Record requested and served versions, elapsed time, and fallback reason without storing sensitive input. Query failures by requested version so a successful fallback doesn’t hide a broken candidate."),
            Moment("Hold the canary even if the aggregate is green",
                   "Stable requests dominate traffic. The candidate exceeds its fallback rate for one cohort, but overall success still looks good.",
                   "Apply the gate to the candidate cohort with a predeclared denominator. Require enough observations and a tolerable operational burden. Record why you held rollout and the evidence needed to retry."),
            Moment("Recovery is a new observation",
                   "The on-call operator moves the active pointer back to the last stable revision. Staff still need confirmation that new requests use the intended version.",
                   "Reopen the state if relevant and send a smoke request through the serving interface. Compare requested and served versions and log the decision. A successful configuration write is not itself evidence of recovery."),
        ),
        "feature-file-outage",
    ),
    "customer-pilot-engineering": CourseCase(
        "Meet the people who fix the building",
        "Inez is embedded with a facilities contractor. Earlier demos suggested AI could route almost every maintenance issue. The shift lead shows her unclassified tickets, a legacy form, and a queue that must keep working during a network failure. They agree on a limited trial with manual ownership intact.",
        (
            Moment("Translate vague enthusiasm into a measured goal",
                   "The sponsor asks for smart intake. The shift lead says reporters will still call if they cannot tell who owns a request.",
                   "Observe actual handoffs and name which delay the pilot must reduce. Establish manual median time, escalation behavior, and a safety gate. Ask the shift lead to confirm the expected human follow-up."),
            Moment("Keep source identity when you normalize fields",
                   "The upstream form sends an old category value and the same ticket can arrive twice. A malformed record should not silently enter a general queue.",
                   "Validate schema version and expected types at intake. Preserve source identity so staff can resolve errors. Route unknown categories to an explicit review state instead of assuming a default."),
            Moment("Shadow decisions while the old process still runs",
                   "During a rehearsal, the directory fails for a routine ticket and an unusual ticket arrives twice. The existing staff queue keeps moving.",
                   "Record candidate decisions without applying them. Compare against the staff route, retry recoverable failures, and test duplicate handling. This gives the customer useful acceptance evidence before changing the live process."),
            Moment("Hand over a decision someone can operate",
                   "The pilot reaches its time target on routine tickets. The shift lead worries about what happens when someone submits a restricted request tomorrow.",
                   "Show the restricted-case result and a working stop rule. Name the owner of manual fallback, provide a reproducible smoke case, and document how the customer can pause the pilot without the engineering team."),
        ),
        "support-assistants",
    ),
    "llm-evaluation-benchmarks": CourseCase(
        "The reviewer who disagreed with the leaderboard",
        "Ren runs a model comparison for an employee policy assistant. A vendor has the best aggregate score, yet the reviewer rejects several responses that involve exceptions. The decision memo will be used by a procurement lead who needs to know why a seemingly strong model might be held.",
        (
            Moment("Freeze the workload before asking who wins",
                   "Teams keep adding examples after seeing candidate mistakes. The more examples they add, the harder it becomes to interpret relative improvements.",
                   "Separate exploratory cases from a frozen comparison set with versioned provenance and critical slices. Evaluate the same inputs for all models. New discoveries can inform the next round without changing the meaning of this one."),
            Moment("An agreement figure needs disagreement examples",
                   "Two evaluators score one response differently because the evidence supports only half its claims. One judged the primary claim and the other judged every material claim.",
                   "Double-rate a shared sample and inspect the disagreement. Revise the rubric and report both raw and chance-adjusted agreement where meaningful. Then rerate a fresh subset to see whether the clarification worked."),
            Moment("Compare successes and the cost of failures",
                   "The fast candidate is cheap per request but produces more outputs requiring review. A careful candidate is slow and handles some difficult cases better.",
                   "Use paired quality differences on the same workload and include the uncertainty associated with a small sample. Compare latency and cost per correct task, including paid failures and clearly identified review assumptions."),
            Moment("Let the gate make ineligibility visible",
                   "The cheapest candidate fails a critical case and a better-scoring candidate misses the latency bound. The sponsor expects one winner.",
                   "Show each candidate’s blocked conditions and recommend only eligible options. If none qualify, record a hold and the test or mitigation that could change the decision."),
        ),
        "model-behavior-rollback",
    ),
    "retrieval-system-engineering": CourseCase(
        "The archive remembers every version",
        "Sana maintains a policy library where approved versions are added without deleting history. A reviewer has access to extra attachments. An answer is useful only if it cites material that was both effective at the requested date and appropriate for the requester.",
        (
            Moment("Ingest a policy so you can explain what happened later",
                   "An amended policy states a new effective date. The indexed copy includes the source text but loses which version it came from.",
                   "Retain source identity, revision, and effective and access metadata at chunk creation. Test when the old and new versions should enter retrieval. A reviewer needs to be able to reopen exactly the cited evidence."),
            Moment("When synonyms help and identifiers hurt",
                   "A user alternates between ‘holiday’ and ‘annual leave’ while another asks for a form identified only by a code.",
                   "Use the same query labels for lexical and dense methods. Semantic closeness can help synonyms and still fail exact references. Report those slices separately before choosing a hybrid."),
            Moment("Find the lost document or the buried document",
                   "Two rankings contain the right record, but after combining them the passage appears below the cutoff. The metric reports a miss either way.",
                   "Inspect candidate recall and rank at each stage. Reranking can improve ordering when a passage is present, but it cannot recover a passage removed before scoring. Keep a labeled example of each failure."),
            Moment("Check eligibility again when the citation is shown",
                   "A cached answer correctly quotes a passage that is now expired. The current index excludes it, but the answer still displays an old source ID.",
                   "Bind cached responses to relevant policy, audience, and revision state or revalidate before reuse. Test stale and denied citations along with a supported quote. An honest abstention is preferable when authoritative evidence is missing."),
        ),
        "bereavement-fares",
    ),
    "durable-agent-tool-runtime": CourseCase(
        "The reviewer approves after the worker goes home",
        "Jo coordinates public meeting agendas. A local tool can retrieve the outline, and a separate step records an approved note. Review can take hours. Jo needs the draft to survive a restart and wants a replay to be visible without creating another copy.",
        (
            Moment("Read the tool declaration before treating it as a promise",
                   "The tool advertises an agenda lookup and a declared identifier field. It does not promise that the requester can see every agenda.",
                   "Inspect the declared input and validate the result against a known case. Discovery tells the client what exists. Application policy still determines which calls are permitted."),
            Moment("The same valid payload can be unauthorized",
                   "A reviewer and a guest supply the same meeting identifier. Both requests satisfy the input schema.",
                   "Check caller and resource policy in addition to argument shape. Record a denied request without sending it to the tool. This keeps a correctness check from being mistaken for authorization."),
            Moment("Persist what the reviewer actually saw",
                   "Jo approves a draft after the workflow restarts. A corrected draft exists with a different payload.",
                   "Persist the proposed payload and its fingerprint before pause. Bind the human decision to exactly that version. A changed payload should be reviewed anew."),
            Moment("A replay is neither a new note nor a new approval",
                   "A write completes and the worker is interrupted before the caller sees success. On restart, the same command arrives.",
                   "Commit the local note and its completion record atomically. Use the command identity to return the existing result on replay. For external effects, rely on the external idempotency contract or reconcile before trying again."),
        ),
        "paused-jobs",
    ),
    "llm-adaptation-inference": CourseCase(
        "A smaller model for ticket routing",
        "Attiya supports a routing feature with a tight compute budget. The model must learn a stable output convention and must use current guidance when a team moves. She compares a frozen model, a small adaptation, and a retrieval baseline, then checks how precision choices affect the service.",
        (
            Moment("Recognize a retrieval problem before you train",
                   "A model chooses the wrong team for a newly reorganized unit. On older cases its label format is already correct.",
                   "Use a retrieval-assisted baseline for the current directory. Measure it alongside the frozen model on the same held-out requests. Reserve adaptation for a recurring behavior where updating facts alone cannot solve the problem."),
            Moment("Inspect held-out behavior after adapting",
                   "A low-rank correction learns the labels in training. The evaluation set also contains unfamiliar phrasing that still needs human follow-up.",
                   "Compare loss and routing accuracy on data held out before training. Verify that base parameters stayed fixed. Compare against retrieval because a change in adaptation accuracy alone cannot tell you which system to ship."),
            Moment("Memory savings and latency savings are different observations",
                   "A lower-precision correction is smaller to store, but unpacking it for each request takes extra work in a local implementation.",
                   "Measure payload size including scale metadata and compare repeated timings on the same hardware. Report quality drift separately from memory and speed. Name the parts of inference the timing actually includes."),
            Moment("Transfer the experiment without transferring the claim",
                   "The small fixture improves, while a transformer checkpoint uses another tokenizer and may split a routing label differently.",
                   "Confirm the output label representation and compare frozen and adapted versions on the same checkpoint and cases. A lab fixture teaches the measurement method. Production quality still needs representative traffic, a tested fallback, and proportionate rollout."),
        ),
        "model-behavior-rollback",
    ),
    "ai-reliability-release": CourseCase(
        "Four timeouts in a small rollout",
        "Olivia is on call for an assistant that summarizes support tickets. A candidate version is handling a small cohort while the stable version serves everyone else. Several pilot requests are late and some need the manual queue. The rest of the system looks healthy.",
        (
            Moment("A user can receive a response and still lose time",
                   "A late summary eventually arrives, after an agent already opened a second ticket to work around the delay. Transport success stays green.",
                   "Define a good outcome in terms of valid and timely work. Use the cohort denominator and the agreed objective to estimate burn. Keep the observation window and sample size attached to the number."),
            Moment("Start at the earliest stage that differs",
                   "Retrieval and validation look similar across versions. Generation in the pilot shows a long wait and failed calls.",
                   "Compare stage traces for stable and pilot requests with similar inputs. Separate observed divergence from the proposed cause. The operator needs a bounded reason to disable the candidate while deeper diagnosis continues."),
            Moment("Predeclare the stop rule for the small cohort",
                   "The whole-service error rate appears stable because most requests go to the baseline. The pilot has four failures among twenty requests.",
                   "Apply quality, latency, and cost gates to the pilot version with only its own denominator. Keep an explicit minimum sample and critical stop conditions. The aggregate cannot replace cohort evidence."),
            Moment("Write the timeline while decisions are still clear",
                   "The candidate is disabled and the next test request succeeds. Olivia needs to prove that affected users are now served by the stable model and that the queue is recovering.",
                   "Check both cohorts, note the observed version and outcome, then record detection, decision, mitigation, and validation in order. Attach one owned follow-up with a concrete verification condition."),
        ),
        "feature-file-outage",
    ),
})


FIELD_NOTES = {
    "bereavement-fares": "A chatbot answer that changed a travel decision",
    "support-assistants": "What changed for customer support workers",
    "face-matching": "The errors a face-matching average hides",
    "speech-recognition": "Who gets left out of a transcript?",
    "model-behavior-rollback": "When a better-liked model got harder to trust",
    "coding-productivity": "Two studies measured two different coding jobs",
    "unisuper-recovery": "Two zones and one deletion boundary",
    "feature-file-outage": "A feature file takes down a healthy service",
    "paused-jobs": "Why GitHub paused queued work",
}


def course_case_intro(case: CourseCase) -> str:
    field_note = ""
    if case.field_note:
        title = FIELD_NOTES[case.field_note]
        field_note = f"\n\nFor a documented comparison, read [{title}](../../casebook/{case.field_note}.md)."
    return f"## Practice case · {case.title}\n\n{case.opening}\n\nThis fictional case continues through the lectures.{field_note}"


def lecture_case(course: int | str, number: int, *, level: int = 2) -> str:
    moment = CASES[course].moments[number - 1]
    heading = "#" * level
    text = f"{heading} {moment.title}\n\n{moment.scene}\n\n{moment.reasoning}"
    walkthrough = WALKTHROUGHS.get((course, number))
    if walkthrough:
        return f"{text}\n\n{heading}#{walkthrough.removeprefix('###')}"
    return text


WALKTHROUGHS = {
    ("ai-literacy", 2): """### Read the notice as a parent

| Draft | What a reader could conclude |
|---|---|
| The school will reopen at 9 a.m. tomorrow. | It is safe to send my child to school at 9. |
| The building is closed today. The school will post another update tomorrow at 9 a.m. | Check the official channel at 9 before making a plan. |

The revisions may look small on a screen. They create different plans for a parent arranging childcare or travel. When you review an assisted draft, mark the sentences that tell someone what will happen or what they should do. Trace those sentences back to the source before editing for tone.

Try another version of the exercise. The school moves only one class online. Which words prevent a parent of a different class from mistakenly staying home?""",
    ("using-ai-at-work", 4): """### Compare a week of work

Suppose Maya and her colleague try two drafts using each workflow. Assume the draft and review times below cover every attempt, including the one that needs a correction.

| Method | Drafting minutes | Review minutes | Material corrections |
|---|---:|---:|---:|
| Manual | 28 | 8 | 1 |
| Assisted | 6 | 22 | 2 |

Across this tiny sample, drafting time dropped by 22 minutes, but review time grew by 14. The observed saving is eight minutes in total. The assisted version also required one more material correction. A single overall score would hide the trade: Maya saves time while her colleague takes on more review work.

Before extending the trial, Maya asks whether that reviewer is available near the publication deadline. If not, the four-minute saving per notice may make little difference to whether announcements go out on time. Write one observable condition that would make the workflow worthwhile for both people.""",
    ("ai-product-decisions", 4): """### What Kavita takes to the sponsor

A sponsor might reasonably ask why the whole queue cannot use the tool if hours and directions went well. The answer is that the two types of work have different failure costs. One inconveniences a caller. The other may send them to the wrong place or leave them without a clear next step.

A short release memo could make that distinction concrete.

- **Approve** routine hours and directions for the trial audience, using the maintained directory.
- **Keep with staff** appointment preparation and ambiguous requests. The assistant gives callers the current contact route.
- **Pause if** any preparation question is presented as a confirmed answer during an audit. The front-desk lead owns the pause and the manual route.
- **Revisit after** a separate preparation trial shows correct referrals across the expected cases, and staff confirm the handoff is manageable.

The last line matters. A hold can be reviewed when someone knows what evidence would change the decision. A vague promise to revisit it leaves both the sponsor and staff guessing.""",
    ("evaluating-ai-in-practice", 2): """### Score the notice before revising it

The required facts are the new room, the time, and the only usable entrance. The draft says “Room 12, 6 p.m.” The organizer’s update says “Room 12, 6 p.m., enter through the south door.”

| Check | Result | Why |
|---|---|---|
| Correct location | Pass | The draft and source both say Room 12. |
| Correct time | Pass | Both say 6 p.m. |
| Entrance usable | Fail | The instruction a participant needs is missing. |

Two of three checks pass. A person who cannot reach the room will still experience the notice as a failure. Revise the notice, then record the failure in the trial so a later comparison includes how often it happens.

Apply the same check to the manual draft. It is easy to compare a tool's mistakes with an ideal version of manual work. Use evidence from the actual baseline.""",
    (1, 4): """### Turn the numbers into a decision

| Routing plan | Observed minutes | Median | Cases taking over 10 minutes |
|---|---|---:|---:|
| Current | 3, 4, 4, 5, 30 | 4 | 1 of 5 |
| Review-first trial | 4, 5, 5, 6, 8 | 5 | 0 of 5 |

The current plan serves a typical case a minute faster. The review-first trial avoids the observed 30-minute wait and has a lower mean, 5.6 minutes versus 9.2. Which matters more depends on the dispatch policy. If a rider must be contacted within 10 minutes, the deadline is directly relevant. If there is only one dispatcher, the extra minute on everyday work can still matter.

Five cases are enough to see the trade-off, and far too few to estimate the worst week. Priya would want to record more overnight cases and compare repeat incidents at the same station before endorsing a threshold. The numbers should make her decision more accountable rather than replacing her judgment.""",
    (6, 5): """### Debug the answer in three passes

The purchase happened on Sunday. Imani opens the trace and finds that retrieval returned only the Monday revision. Adding stricter wording to the prompt will not restore evidence the model never received. She writes three checks.

1. **Temporal retrieval** · The same query returns the Friday revision for Sunday and the Monday revision for Tuesday. Record the sources before generation.
2. **Claim support** · Both amounts appear in the corpus. Before showing an answer, verify that the exact quoted passage supports the amount and the effective date together.
3. **Handoff** · In a broken index with only the Monday document, the assistant says it cannot confirm the Sunday limit and gives the employee a route to staff review.

These checks isolate a missing source, a wrong conclusion, and a poor fallback. The learner can now test each change separately. Change the case so that the purchase includes approved field work. Which additional evidence must the answer include before it can cite the exception?""",
    ("customer-pilot-engineering", 3): """### Follow one work order through the rehearsal

In the existing workflow, the desk retains ownership until the shift lead sees a filed ticket. In the rehearsal, the adapter records a proposed route without changing that ownership.

| Event | Candidate record | What the shift lead should see |
|---|---|---|
| Routine ticket, directory available | Propose the expected queue | A candidate destination beside the desk’s route |
| Directory unavailable | Request needs manual handling or retry | The original ticket remains visible to the desk |
| Same ticket arrives again | Return the prior result for that ticket ID | No second work order |

Ask an operator to perform these steps using the workbook output as evidence. They should be able to tell whether the pilot acted, whether staff still own the ticket, and when they need to do something. A green automated assertion can confirm a route; the rehearsal checks whether the customer can safely run the process.""",
    ("ai-reliability-release", 3): """### Make the call while the stable version is available

Assume the release owner established a 95% threshold for on-time, valid responses and requires at least 20 candidate requests before deciding on expansion. The pilot records 16 good results in 20 attempts. That's 80% for the pilot. The baseline records 99 good results in 100 attempts. Combining both produces 115 good results in 120 attempts, or about 96%.

The combined number clears the threshold while the candidate fails it. Hold the candidate. Compare the earliest failed stage with comparable baseline requests and verify that the stable version can still serve the pilot users. A small cohort limits exposure. It does not make its missing or late work less important.

Now change the pilot to one failure in 20. The observed rate equals the threshold. Would you expand immediately? Check whether the minimum sample addresses the workload you are about to expose, including any consequential slice missing from the pilot.""",
}


CASES.update({
    "sparse-model-architectures": CourseCase(
        "A Monday morning at HarborLink",
        "HarborLink's engineering team wants to process rider questions and long equipment logs on the same fleet. Arun has a dense baseline, a candidate with sparse experts, and a limited device budget. The support desk only cares which choice still works during a noisy Monday queue.",
        (
            Moment("Follow one token across the layer",
                   "A maintenance request goes to the long-document endpoint. A diagram on the team wall labels that endpoint an expert, which makes it hard to discuss what the model actually computes.",
                   "Draw one box around the endpoint decision and another around the token-level operation. A request can take one endpoint and still use many experts inside it across tokens and layers."),
            Moment("A burst hits the same expert",
                   "A station closure causes many near-identical equipment questions to arrive together. Last week's averaged routing histogram looked balanced.",
                   "Inspect assignments at the batch boundary. Count overflow per expert, then rerun the behavior check when assignments are rerouted. A healthier histogram can still hide changed answers."),
            Moment("Follow the activation across devices",
                   "The sparsest candidate reduces expert FLOPs in a spreadsheet. Its busiest expert lives across a slow link from the device handling most inputs.",
                   "Estimate the outgoing and return payload. Mark the synchronization cost and collective startup as unknown. Watch the busiest rank before attributing a latency miss to the model math."),
            Moment("The workload has two kinds of long prompt",
                   "Support wants exact citations in a long policy. Maintenance wants a summary of recurring events across a log. Those requests can have the same number of input tokens.",
                   "Measure memory against input length and run each task separately. A lower cache estimate can be a useful reason to benchmark and says little about quality on an exact lookup."),
        ),
    ),
    "reasoning-efficient-inference": CourseCase(
        "Fast answers without a guess",
        "Meera owns HarborLink's response-time budget. Some requests only need one current policy excerpt. Others require choosing a route across stations with exclusions. She can afford added model time when it changes what the desk can verify.",
        (
            Moment("Pick an observable escalation signal",
                   "A cheap candidate returns a confident answer about a closed station. Its source date is older than the date supplied in the request.",
                   "Use verifiable source age as an escalation signal. Benchmark the whole escalation path, including both attempts and the capacity needed for a manual handoff."),
            Moment("Test the answer before reading the explanation",
                   "Two routes look reasonable in the planner's prose. One uses a closed lift and the other has a bad total.",
                   "Run an independent feasibility check over the structured routes. Track when a valid route is never proposed separately from when the verifier accepts a bad route."),
            Moment("Reject the suffix when the prefix changes",
                   "The draft system expects a policy sentence to end with 'business days'. The target chooses a token that begins a different phrase.",
                   "Keep the matching prefix and continue from the target's chosen token. Any later draft token was proposed in an obsolete context."),
            Moment("A warm benchmark misses the expensive cohort",
                   "A performance report looks good on repeated policy prompts. A contractor batch uses fresh logs, increasing the queue time for first tokens.",
                   "Fix separate gates for warm and cold cohorts. Record prompt lengths and concurrency so a follow-up can reproduce the failure."),
        ),
    ),
    "decision-models-and-policies": CourseCase(
        "Who gets the next maintenance slot?",
        "HarborLink has a queue and a finite number of technician slots. Leena owns the decision policy. She needs to translate delay-risk estimates into a plan and explain why some tickets are deferred for review.",
        (
            Moment("Give the uncertainty somewhere to go",
                   "A maintenance alert is neither clearly routine nor obviously urgent. The model is moderately confident and a short review is available.",
                   "Write the action and review costs before choosing a threshold. Track how often the policy defers and whether the team can handle that load."),
            Moment("Several good jobs compete for one crew",
                   "The highest-value job needs both available time blocks. Two smaller jobs fit together and can be finished today.",
                   "Solve for the set of jobs rather than the rank of an individual ticket. If a compulsory job cannot fit, escalate the schedule instead of dropping it silently."),
            Moment("History contains the actions somebody chose",
                   "The log has thousands of observations, but a rarely selected region has very little evidence for the new policy's proposed action.",
                   "Record the logging policy's action probabilities and measure overlap. Examine effective sample size and stop the comparison if the target action has no historical support."),
            Moment("Saving minutes now can cost a visit later",
                   "A policy defers tricky jobs to improve today's completed jobs per hour. Repeat visits rise over the next reporting period.",
                   "Include future workload and unresolved work in the objective. Evaluate a candidate with a shadow workload and connect delayed outcomes to the original policy decision."),
        ),
    ),
})
