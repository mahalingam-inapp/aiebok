"""Extended readings for no-code and applied courses, in lecture order."""

READINGS = {
    "ai-literacy": (
        """### Start with the operation the tool performs

Imagine three buttons in a school office. One sends a closure notice to every parent on a list. Another estimates how many calls the office might receive. A third drafts an answer to a parent’s question. The first follows a rule, the second estimates an unknown quantity, and the third generates text. All three can be useful in one workflow, but each can fail in a different way.

A rule works only as well as the condition and data it receives. A prediction needs examples or measurements that have some relation to the future. A generated draft may sound right even when the tool had no access to the fact it describes. Classify the job before choosing the tool so you know what to check.

When a school worker uses a model to simplify a confirmed notice, the original notice remains the evidence. Compare the dates and instructions in both versions. If the job changes to estimating when a repair will finish, a draft about the repair cannot stand in for a prediction from the facilities team. In your own workflow, name the source, the operation, and the person who ultimately makes the decision.""",
        """### Separate a claim from the wording around it

A model can produce a likely continuation of a sentence without checking the world. If its input says there will be an update tomorrow, it may fill in the more familiar idea that the school reopens tomorrow. The same behavior helps it write smoothly in routine cases. Fluency therefore provides little evidence that a particular detail is true.

Underline what a reader might act on. Dates, locations, amounts, rules, and commitments are often more important than a stylistic problem. Compare each claim with the source and ask whether the source is both current and authoritative for that decision. A link should support the exact claim in the draft. A link to a general school page does not establish a reopening time.

When a source is incomplete, keep that gap visible. “We will share another update at 9 a.m.” tells families what to do without implying that classes resume at 9. Try looking for uncertainty that changed form: pending became confirmed, estimate became promise, or possibility became instruction. Those transformations often matter more than grammar.""",
        """### Decide how expensive a mistake would be

One way to choose a first use is to ask how quickly you would notice a mistake, whether you could undo it, and who would bear the cost. An internal draft is usually easy to inspect before sending. An eligibility decision sent directly to a student can be hard to reverse and can affect what help they receive.

Match the review to the effect. A volunteer may ask a tool for three alternate phrasings of a known announcement and then select the clearest. A school employee deciding an accommodation needs access to the applicable policy, any case-specific evidence, and someone with authority. A likely-sounding suggestion does not change any of those requirements.

A useful test is to pretend the tool is wrong once. Describe how the person affected would find out, correct the record, and reach the right owner. If the answer is unclear or the action is hard to undo, first narrow the task to preparation or drafting. Revisit automation only when the process can handle the consequences of failure.""",
        """### Minimize the data before you think about the prompt

Start with a copy of the task description, then list the facts the tool actually needs. For a closure announcement, the date, building, and audience category are enough. A spreadsheet with family names, email addresses, accessibility needs, and pickup arrangements adds exposure without improving the public draft.

Removing names is only one step. A unique combination of class, date, and event can still point to a specific child. A substitute example is often easier to verify: write a fictitious situation with the same form and no real personal details, then adapt the output privately. Follow your organization’s rules for which tools can handle which classes of information.

Checking the input and checking the output are separate jobs. An approved input might still produce a draft with inappropriate inferred details. Before sharing it, read it as the intended audience would and ask whether it reveals anything they do not need to know. Assign that check to a person, rather than relying on a line in the prompt.""",
    ),
    "using-ai-at-work": (
        """### A brief has a purpose and an acceptance test

Handing a task to a writing tool resembles briefing a colleague who has never seen the project. Describe the reader, the action they should take, the facts they may rely on, and the shape of the result. Distinguish required facts from tone preferences. A paragraph may be flexible in style while the date and address are fixed.

Try two briefs for the workshop notice. “Announce that we moved indoors” leaves the tool to infer the address and what attendees should do. “Write a short notice for attendees. Keep the confirmed room and start time unchanged. State that accessible entrance directions will follow” gives the draft a concrete acceptance test. Compare the results one requirement at a time.

Include contradictions when you expect them. If an old flyer and a newer update disagree, identify which supersedes the other. If you cannot establish that, instruct the draft to surface the disagreement for review. This is especially useful when several people hand off work and nobody remembers which version supplied a detail.""",
        """### Review the result in two passes

First inspect the facts and obligations. Read dates, numbers, places, required steps, and promises against the notes. Check for omissions as well as invented statements. A draft with the right room can still be unusable if it leaves out the only accessible entrance.

In the second pass, read as the recipient. Could someone tell whether a change is confirmed? Do they know where to go or whom to contact? This is a different test from whether the sentences are factually accurate. Keep the two judgments separate so a friendly tone does not raise your confidence in an unsupported instruction.

When the draft says “plenty of parking,” ask which source confirms it. You can delete the claim, soften it only if a reliable source justifies the revision, or ask the responsible person to verify it. Rewriting a guess in more careful language does not solve the evidence problem. Mark unresolved items in the draft until someone owns them.""",
        """### Make a handoff actionable

A handoff should include the state of the work, the open decision, the evidence, the new owner, and the time by which it matters. Simply forwarding a draft forces the next person to reconstruct what has already been checked. They may assume that a polished sentence is approved when it was only proposed.

For the moved workshop, the reviewer needs the confirmed room, the facilities message about the ramp, the publication deadline, and permission to publish a version with the access detail pending. State what has not been sent. This prevents both colleagues from sending separate versions to the same participants.

Choose a useful fallback before a deadline creates pressure. If no reviewer is available, publish only the confirmed details or hold the announcement if the missing information would stop people attending safely. State who will post the update and where. The best handoff lets a person restore the workflow even if the drafting tool is unavailable.""",
        """### Compare total work rather than draft speed

Time a request from a usable brief through an accepted final result. Include source collection, review, corrections, and any abandoned attempts. Use the same quality checks for manual and assisted work. Otherwise the result can reflect how strict the reviewer was rather than any difference in the tools.

One short note might take four minutes to write and two to check manually. An assisted version takes one minute to generate and six to verify. Although the draft arrives faster, the final result takes a minute longer. Another task with a more repetitive format might show the opposite result. Compare work by task type before aggregating.

A pilot should also identify who does the work. A writer may save time while a specialist review queue grows. Track whether that queue causes missed deadlines or interruptions. Use a small trial to decide which tasks are worth keeping, and make it easy for staff to switch back when a case falls outside the tested scope.""",
    ),
    "ai-product-decisions": (
        """### Trace the job from the user's point of view

A product request such as “add a chatbot” names an interface rather than the burden it removes. Follow a caller from the moment they need an answer to the moment their task is resolved. Note where they wait, where they repeat information, and where a staff member exercises judgment.

Suppose a caller waits six minutes to ask for opening hours. The staff answer takes 20 seconds. A clear, maintained schedule page may reduce the wait without requiring people to explain their question to a model. If many callers need to understand how two written policies interact, search and a staff handoff may address a different gap. The two cases need different tests.

Turn an observation into a narrow decision. State the audience, workflow step, measured baseline, and change you can verify. Ask which other paths users take when the new feature fails. A pilot focused on a real bottleneck is easier to stop, improve, or expand than one that promises to automate the entire service.""",
        """### Choose the simplest mechanism that meets the need

Rules suit cases where inputs and decisions are known and the organization can keep them current. Search helps people find an authoritative document when the decision remains theirs. Generation is useful when language needs to be reorganized, summarized, or adapted for an audience. Each mechanism still depends on a source and an owner.

Consider clinic hours, directions, and appointment preparation. The hours can come from a directory. Directions might be assembled from a maintained template. Explaining preparation across several documents may call for a draft with citations and a staff handoff for ambiguous questions. One interface can offer all three behaviors deliberately.

Use the current workflow as the comparison. Ask whether a person can resolve the task with a lookup page plus a staff queue. If the generated candidate adds value, identify the tasks where it does, then check that its claims remain grounded. Consider maintenance and escalation, since a more expressive interface can add review work.""",
        """### Pair benefits with a guardrail

A benefit measures the improvement you want, such as fewer repeat calls or less waiting. A guardrail measures a failure you cannot accept as the price of that improvement. Making them separate keeps good routine results from canceling out a consequential mistake.

Imagine the front desk redirects 60 of 100 routine callers to a useful source. The same pilot gives one incorrect instruction to a caller with a preparation question. Count the successful redirects, but report the consequential mistake in its own slice. A single combined number would hide which outcome the pilot is allowed to optimize.

Before release, name the denominator, acceptable limit, and person who reviews a breach. Give rejected or uncertain cases an explicit fallback. A stop rule should say what to pause and what continues. The front desk may keep serving the routine directory workload while preparation questions return to staff.""",
        """### Write the decision while the evidence is fresh

A pilot decision should record scope, outcome, remaining uncertainty, and an owner. “The pilot worked” leaves the next operator unable to tell which tasks passed. “Continue with published hours and directions for this cohort” gives them a bounded action they can verify.

Read a sparse result carefully. Five correct answers about preparation are encouraging, but they say little about rare exceptions. If a mistake could leave a caller in the wrong queue, keep that slice with staff until you have better evidence. Record which cases are missing, who can supply them, and what result would justify revisiting the hold.

When you choose to pause, preserve the benefit evidence as well as the failure. The organization may still have a valuable directory or a better handoff even if one proposed form of automation is unsuitable. A clear decision memo helps separate a failed experiment from a judgment about all uses of the technology.""",
    ),
    "managing-ai-delivery": (
        """### Ask whose experience the average represents

An overall rate weights groups by how often they occur in the sample. Routine reports in a large queue can conceal repeated errors on a smaller group. Start by listing the cases for which failure carries a different consequence or requires a different recovery process.

If a trial routes 86 of 90 routine reports and 6 of 10 urgent reports correctly, the total is 92 of 100. An urgent reporter sees a 60% observed success rate. The small urgent sample makes that estimate uncertain, and it is already a reason to collect better evidence before delegation. Write counts alongside percentages.

Avoid slicing only after noticing a surprising number. Predeclare the groups you must protect, the expected result, and who reviews the case. Continue to inspect new clusters of errors during operation. A reviewer looking at the actual misroutes can often distinguish a missing intake field from a poor decision rule faster than a dashboard can.""",
        """### Separate the authority to recommend, approve, and restore

Several teams can contribute to a service without having authority over the same decision. Policy owners define what is allowed. Operators handle queues and recovery. A product owner sets the scope of the pilot. Reviewers decide whether the evidence is sufficient to proceed, and users need a visible way to dispute or correct an outcome.

Build an ownership map around events, not an organization chart. Who approves a change to routing? Who can pause it at 5 p.m. on Friday? Who contacts a resident after a misroute? Assign names or staffed roles and offer a substitute when the primary person is unavailable.

Check that authority matches access. A named rollback owner with no ability to change the route cannot recover the service. A vendor engineer with broad configuration access cannot take responsibility for a city's service decision. Test the required action and the escalation route in a rehearsal so an incident is not the first time people discover either constraint.""",
        """### Roll back the effect, then verify recovery

A reversible launch gives one group the new behavior while the original process remains usable. Decide on the trigger, who can act, and how to verify recovery before admitting the first real case. Simply restoring a configuration does not establish that the work has returned to staff.

Use three probes in a rehearsal: a request that was already in flight, a new request after rollback, and a duplicate of one that has already completed. Confirm where each appears and what staff are expected to do next. The service may need to preserve identifiers and outcomes even while routing changes.

During a rollout, distinguish a correct result from one that was rescued by a human fallback. A dashboard that counts both as success can hide a growing manual queue. Keep fallback volume visible and agree on how much work the staffed team can handle before you expand the pilot.""",
        """### A green health check answers a narrow question

After a failure, record what users saw, which work is in an uncertain state, and which stage first diverged from normal behavior. System availability and correct user outcomes are different questions. A healthy service may still be applying the wrong rule or using stale evidence.

Before resuming, reproduce the original failing cases using the proposed fix. Check the accepted outcome and the handoff for any open work. If a failure is consequential or poorly understood, restart with a smaller group and observe it under the actual release conditions. A staged recovery makes the result easier to interpret.

Write down what would cause the incident team to halt again. Assign one person to communicate affected cases and another, if needed, to verify that the recovery worked. Keeping those duties explicit prevents a technical fix from being mistaken for a complete resolution for the people who were affected.""",
    ),
    "evaluating-ai-in-practice": (
        """### Build a comparison set from the work people actually do

Start by observing a few real tasks. Describe both frequent patterns and failures that matter, then create safe examples that preserve those conditions. Use the same cases with your existing process and with the tool. Give both access to the same authoritative facts and time to arrive at an accepted result.

For announcements, a reasonable small set might include a routine notice, a late correction, a notice that must omit private information, and one with a still-unknown location. Assign each case an expected behavior. The expected output can be a question or handoff if the source does not establish an answer.

Keep these cases aside once you start changing the workflow. If you fix the draft after seeing all the cases and then report the same cases as proof, you are measuring how well you handled familiar examples. Exercise the revision on a fresh sample before making a broader recommendation.""",
        """### Make the scoring rule something two people can use

A clear rubric describes observable behavior. “Good notice” is too broad. “Correct room and date, current entrance instructions, no unconfirmed reopening promise” lets reviewers compare a draft against the same expectations. Mark both false statements and missing requirements.

Test the rubric on two outputs with another reviewer. If one reviewer counts a missing entrance as minor and the other calls it a failure, ask who needs that instruction and what happens without it. Revise the criterion so someone new can apply it consistently. Keep the original disagreement as useful evidence about where judgment varies.

Preserve the denominator and which requirements were applicable. A draft cannot be credited for avoiding a particular error if the task never tested that condition. Use a separate record for cases that were reviewed but could not be resolved from the source. Those cases may teach more about the workflow than a score alone.""",
        """### Time the whole task and record correction effort

An assisted draft may arrive quickly while the person who signs it takes longer to check it. Record the start and finish of briefing, drafting, reviewing, fixing, and sending. Include time spent asking someone else for confirmation. A quick failed attempt still consumed time and should stay in the comparison.

Measure quality alongside time. Track how often a material fact had to be corrected and how much work fell on the reviewer. If a tool shifts specialist work into a queue with a fixed capacity, the average time on any one notice may not describe what happens at busy times.

Compare similar requests and keep task types visible. Separate routine reminders from late cancellations. A favorable time result for the first group can support a limited change even if the second group needs the existing workflow. Explain the difference with cases, rather than calling the whole trial a success or failure.""",
        """### Make the result useful to the next decision maker

Put the actual evidence beside the recommendation: the tested tasks, denominators, rework, benefits, and harms. State whether you recommend continuing, revising, or stopping for each relevant task type. A responsible decision may keep the same tool for one purpose and pause it for another.

Name what would change your decision. A narrower prompt could reduce unconfirmed claims on late updates. A staffed review channel could make occasional handoffs acceptable. Ask for a rerun with previously unseen requests and a threshold that can be judged without inventing a new rule after seeing results.

Give a person ownership of the next run and keep the old workflow available. Good evaluation does not need a large deck of scores. It needs a clear statement of what was observed, who experienced the effect, and what action the evidence now permits.""",
    ),
    "model-selection-for-leaders": (
        """### Make candidates earn the same outcome

A vendor demonstration can illustrate a capability. A purchasing decision needs comparison on equivalent work. Specify the inputs, approved sources, expected output, review process, and conditions that make a result unacceptable before giving cases to candidates.

For a policy help desk, a successful result is a source-supported answer or an appropriate handoff, delivered in time for a staff member to use it. Define which requests call for durable evidence. Use representative user wording, including ambiguous and unsupported questions, and reserve cases for a blind comparison.

Give each candidate a fair setup within the same scope. Record different configurations and any human effort needed to get a result. A candidate that needs a carefully hand-prepared document for every request might be a poor fit for a team that makes frequent policy updates, even if the demonstration looks strong.""",
        """### Read denominators before reading rankings

Nine successes in ten attempts and 90 in 100 share a percentage. They do not offer the same confidence about what happens next. Keep the count, type of cases, and any exclusions attached to the score. Look at errors that matter separately from errors a staff member can quickly correct.

Several reviewers can also disagree about what counts as support. Ask them to rate a common subset and record where they differ. Inspect cases where a major claim relied on a weak source or where an apparently incomplete response was actually a correct handoff. Agree on the rule before using it to compare candidates.

For a purchase, ask for the workload that the trial did not cover. A model may have passed all tested examples and still have no evidence on the regional languages or exception types that your users need. Keep untested work out of approved scope or plan how to get the missing evidence.""",
        """### Price useful work

A cost per call can look low while a cost per completed task is high. Include retries, reviews, corrections, and any paid requests that failed. If a service costs 12 units to attempt 10 tasks and 9 meet the agreed checks, its observed cost per correct result is about 1.33 units before review.

Time is another part of the cost. Two candidates with the same total bill may differ in reviewer effort and the delay they impose on staff. If one needs five extra minutes per case or more rounds of clarification, an inexpensive inference bill can be misleading.

Use a consistent workload and report the limits of the comparison. Price estimates at modest volume may miss peaks, implementation effort, or support. Separate known costs from assumptions. This makes it easier to recalculate the recommendation if the volume, reviewer rate, or vendor terms change.""",
        """### Make a recommendation someone can act on

Agree on the rules for eligibility before ranking acceptable candidates. Require evidence on the critical cases and a workable operational response when the system cannot answer. Only then compare speed, cost, and usability among the candidates that passed those gates.

Your recommendation should specify a trial audience and what stays under the existing process. Record the owner, pause condition, and what evidence would justify expanding scope. If two candidates are close, choose an experiment that would separate them on the factor that matters, such as review burden or the worst language slice.

Keep the option to defer a choice. A scorecard can show that a simpler method already meets the need, or that no candidate has demonstrated an acceptable result. State what would reverse the decision rather than choosing the least weak option just to complete the procurement process.""",
    ),
}


READINGS.update({
    "model-backed-applications": (
        """### Classify failures at the application boundary

Wrap the provider behind a contract that names the inputs, allowed outputs, and failure behavior. A timeout means the call did not finish in time. Invalid JSON means its response could not be parsed. A valid response with a source outside the supplied evidence means it violated a separate grounding condition. If all three are logged as “model error,” the person on call cannot tell which layer to fix.

Validate locally before using an output. A typed schema can require an allowed status and a list of citations. Then check that the status makes sense for the presence of evidence. An answer can pass both checks and still make an unsupported statement, so verify claims separately.

All three failures can give the user a safe fallback while retaining distinct operational reasons. Use the notebook to induce each failure independently. The same user-facing message can be correct in more than one case, as long as the report preserves which check fired.""",
        """### Trace an evidence item end to end

A retrieval pipeline starts with authorized documents, splits and indexes them, ranks candidates, and passes selected passages to the model. Preserve a stable source identifier from the index to the answer. A title alone is not enough when a policy has multiple revisions or sections that make different promises.

For a given question, evaluate whether an authorized relevant passage reached the candidate set before inspecting the final output. A missing passage is a retrieval problem. A passage that arrived but lost its exception during assembly is a context problem. A contradiction of the supplied passage is an answer problem. The same final symptom can have three different fixes.

Test the same input for two roles. Remove any restricted passages before ranking and verify that returned citation identifiers refer to the evidence actually supplied. If the ordinary user has insufficient evidence, an explicit handoff is a successful application outcome.""",
        """### Preserve failure categories in the score

For each evaluation case, record the expected behavior before running the candidate. Use separate indicators for retrieval recall, citation validity, and whether the response met the request. You may also need an explicit category for a correct abstention, where the expected answer is to request more information or route to staff.

Consider 20 cases. The right evidence was retrieved in 18, but only 15 answers met their criteria. Two cases could not support a response. Five final failures should not automatically send you to the retrieval layer. Join the failed cases to their retrieval records and inspect whether evidence was lost in assembly or never used by the answer.

Keep the same fixtures when comparing configuration changes. Report the counts for critical slices with the aggregate. Include cost and latency for attempted cases, as failed calls still consume resources. This turns the score into an explanation of where work should go next.""",
        """### Make the live comparison a controlled change

A deterministic baseline makes it easier to test your own application contract. A live provider introduces sampling, network delays, rate limits, and model versions. Keep the same corpus, input cases, validators, and scoring rules when changing the provider. Record anything that still differs, including timeouts and inference settings.

Run each configuration over the same cases, measuring first successful results and the spread of latency over repeated trials. Report the number of attempts and failures. Compare output quality per slice rather than assuming a provider with more natural phrasing belongs on every route.

If you change an exact-match validator to allow a paraphrase, treat it as another experiment. Decide what support means, review a small sample, and rerun both candidates with the same requirement. The workbook can run with a fixture when a local model is unavailable. Fixture timings are useful for understanding the harness and do not estimate a live workload.""",
    ),
    "supervised-coding-harness": (
        """### Write behavior before inviting implementation

An acceptance contract describes observable results for the proposed change, side effects, and old behavior the user still relies on. Build a small set that distinguishes the current implementation from the proposed one. A good starting set includes a normal input, a boundary case, and a preserved behavior.

For a formatter, “trim whitespace” leaves open whether internal spaces collapse and what happens when the result is empty. Use an input with both surrounding and internal spaces. An empty input can still go to the existing review mechanism. Test both so the proposed improvement cannot accidentally turn an unparseable ticket into an accepted one.

First run the tests against the current implementation. You expect the new case to fail for the reason you intend to fix, while existing cases pass. A test that already passes both implementations provides little evidence about the change. Keep the input and expected output in the review packet.""",
        """### Check the proposal before granting effects

A harness can accept a small, typed proposal and run independent checks. Separate the declared operation and scope from the mechanism that applies it. An allowed field can still carry a change that violates the request, so validation of format and regression tests both matter.

A formatter proposal may name a recognized transformation and a known file. It can still change output for a legacy category outside the requested task. Evaluate the proposed behavior against the precise fixtures, and show the reviewer a diff small enough to inspect. A general lint pass adds evidence about style, which is weaker evidence about behavior.

Use a bounded sandbox or simulated effect for student exercises. Preserve the current state until a person has reviewed whatever needs approval. Record failures as evidence for the next attempt, such as a malformed proposal, an out-of-scope change, or a failing example. That makes review work measurable and prevents a retry from becoming blind expansion.""",
        """### Bind authorization to a specific revision

An approval for one revision is not general permission to apply later changes. Preserve the exact input, proposed effect, approval, and an operation identifier. Before applying, compare the current proposal with the approved revision. If it changed, ask for a new review.

Now suppose the worker applies a change but the acknowledgment is lost. A retry should return the recorded outcome when the system already completed that operation. Store completion alongside the relevant state change when the storage boundary permits it. An external action needs its own stable request identity and a way to reconcile uncertain outcomes.

Exercise two cases independently. Submitting a changed proposal after approval should wait. Resubmitting the completed operation should produce no second effect. Both cases can look like a duplicate request on arrival, but they need different handling. A trace should retain which revision and completion record the harness used.""",
        """### Tell the next operator what actually happened

A compact trace can show the request, proposal, checks, decision owner, applied revision, and outcome. It gives the reviewer a way to understand a blocked effect without replaying every intermediate generation. Organize traces by stable request identity so retries can be followed across process restarts.

Compare traces from two workflows at the decision points. One may spend less time generating changes but produce more rejected proposals. Another may wait longer for review but lower the rate of surprises after execution. Include total completion time, reviewer effort, and unresolved work when judging the workflow.

A handoff should distinguish “check failed and needs a revised proposal,” “passed and waiting for a human,” and “already applied.” Those states imply different next steps. Test that a new operator can pick up the right action using the evidence in the trace, without needing access to hidden model reasoning.""",
    ),
    "model-selection-and-adaptation": (
        """### Split independent work before fitting

Repeated templates and near-duplicate incidents can make random row splits misleading. If similar tickets appear in both training and evaluation, a model can learn a wording shortcut and still look as if it generalized. Choose a group such as site, original incident, or source document so related rows stay together.

Record fields as they existed at the moment the prediction is made. A status added by the support team after resolution is part of the outcome, even if it is present in a table you can train on. Excluding it may lower measured accuracy and make that evidence more representative of the deployed task.

Use training data to fit, validation data to choose settings, and a held-out test to report the final comparison. Record group membership and preprocessing versions. Review a few examples from each split to check that the separation is meaningful, not merely an artifact of the grouping key.""",
        """### Establish what the features add

Start with a majority classifier or a rule the existing workflow can explain. Fit it on the same training examples as the learned candidate and use the same test cases. A baseline should be cheap enough to maintain and realistic enough that beating it would matter.

A token-frequency model treats counts as evidence for a category. If the word “billing” occurs frequently in labeled payment tickets, it may raise that class's score for a new input. Smoothing prevents a word absent in one class from making the whole class impossible. A result may still depend too heavily on names or templates seen during training.

Compare errors on short and long requests. If the learned model improves only on long, well-formed examples, review whether that covers the actual intake. Check one false positive and one false negative with the desk team. Ask which available feature would correct the case and whether it would still exist at prediction time.""",
        """### A decision threshold changes who does the work

A system can route high-confidence requests and send the rest to staff. Define **coverage** as the fraction of requests handled automatically and **selective risk** as the error rate on those accepted requests. Moving the threshold trades speed and queue volume against the number of incorrect automatic routes.

Imagine one setting accepts 80 of 100 requests and misroutes 8. Another accepts 60 and misroutes 3. Selective risk drops from 10% to 5%, while review volume doubles from 20 to 40. A recommendation needs operational costs as well as acceptance accuracy. Some wrong routes may be more costly than a manual review.

Select the threshold using validation data and a cost assumption appropriate to the workload. Report the final result on the held-out test, including uncertainty and per-group counts. Recheck that confidence estimates are usable on new traffic before assuming a threshold chosen from one set transfers to another.""",
        """### A release includes the decision rule

Saving only model weights is insufficient if another environment uses different tokenization, a different threshold, or a different label order. Package the estimator with input normalization, output mapping, version identifiers, and the operating point that was evaluated.

Make a known-case round trip. Save the artifact, reload it through the same interface as serving, and compare predictions and fallback outcomes on a narrow fixture. Include a request at or close to the threshold. That case can reveal small version differences that a simple serialization check will miss.

Tie each release to a replayable evaluation record. Declare which failing slice would block deployment, and which previously approved artifact can be restored. After switching versions, verify the result through the serving route. An unchanged file hash confirms you loaded an object, while the round trip checks that people still receive the intended decision.""",
    ),
    "operating-ai-services": (
        """### Probe the interface the caller uses

A deployable endpoint has a defined request shape, response shape, and behavior when an input is missing or a provider is unavailable. Include served version or another traceable revision, particularly when traffic is split. A health check answers whether a service can receive traffic. An end-to-end smoke request checks which behavior a real caller receives.

Separate process liveness from readiness. A process may be alive while the dependency needed to handle requests has not loaded. Conversely, a fallback could serve a reduced response even though the preferred route is temporarily unavailable. Choose a contract that makes this visible where it matters.

Use a known request in the workbook to verify both the route and its answer or handoff. Test invalid input as well. Capture the active version and actual result so later operators can tell whether traffic returned to the stable implementation.""",
        """### Give fallback behavior its own operational record

When a primary route fails, fallback can maintain a useful outcome. It can also hide reliability problems if the dashboard counts every response the same way. A successful handoff might still consume staff time. Record what was requested, what actually served, and why those choices differed.

A structured trace can include a request identifier, attempted version, served version, status, elapsed time, and fallback reason. Avoid storing personal request text where counts and identifiers suffice. Choose retention and access deliberately so support can investigate an incident without making routine observability a new source of exposure.

Persist the events needed for release evaluation. A worker restart should not erase the recent evidence for a failing canary. Run one forced timeout and query the resulting record. If the public response was correct and the events still show a primary failure, the telemetry is describing the system that operators need to run.""",
        """### Evaluate the candidate cohort on its own merits

A canary limits the group receiving a proposed version. The gate must still examine the candidate group separately. Stable traffic can dominate the aggregate and obscure a regression in a small trial. Record how cases are assigned and which version the request attempted to use.

Choose a minimum useful observation count and high-priority criteria before looking at results. Check latency, fallback reason, and valid user outcome. An aggregate availability signal is useful for alerting, but insufficient for deciding whether a version should receive additional traffic. Compare like workloads so a batch of unusually easy requests does not accidentally justify expansion.

If the candidate fails, preserve both the decision and evidence. Decide whether to hold at the current scope, disable it, or investigate a confounding factor. A good release tool distinguishes “failed the gate” from “insufficient evidence” so operators know whether to change the system or gather more observations.""",
        """### Verify the service after restoring the pointer

Rollback is a new deployment decision. Use the prior known-good version, record who authorized it and why, then verify the observed route. A successful configuration write can coexist with stale workers, cached policy, or new requests still being routed to the candidate.

Run a smoke check from the perspective of both a stable caller and a caller affected by the candidate. Check the served version, result, and health of any manual queue that received fallback work. If the candidate caused inconsistent or pending effects, decide how operators will reconcile those separately.

Persist the pointer and event history if service continuity depends on surviving restart. Reopen the store in the workbook and repeat the request. The handoff should tell a colleague what failed, which version is safe to use, what remains pending, and which evidence would permit the next release.""",
    ),
    "customer-pilot-engineering": (
        """### Learn from the person doing the work

A pilot starts with a workflow and a customer decision. Watch how a real request moves through the current process, including the unofficial work people do to correct mistakes. Write the acceptance criterion in terms the shift lead can verify. Faster proposed routes are useful only if staff can recognize who owns the resulting ticket.

Use historical and synthetic cases to agree on what the pilot may touch. Establish the manual baseline, which work is sensitive, and when to ask a person. Decide which faults would pause the feature even if the average time improves. Protect an existing route for uncertain and restricted items.

Ask the customer to verify what an accepted result looks like using the evidence they normally work with. A successful demonstration is one repeatable observation, while acceptance also needs coverage and explicit ownership. Frame the smallest scope that can answer the customer’s real question.""",
        """### Keep a record recognizable after normalization

An adapter maps between the customer's data and the application's contract. Validate the upstream schema version and required fields, then preserve identifiers and timestamps. People need these details to find the original ticket when a candidate route looks wrong or a record is delivered twice.

Handle three inputs separately. A known category maps to an allowed internal value. An unknown category becomes an explicit review item. An invalid value is rejected with a reason and, where permitted, a reference to the original record. Using a broad default for all three loses evidence about what happened.

Version the mapping and exercise a boundary case before deploying it. Ask the upstream owner how a schema or category changes are advertised. A customer can make a sensible update in their system and still break your assumptions. Give the operator a way to detect, pause, and recover from that mismatch.""",
        """### Compare decisions without changing operational ownership

In a shadow trial, the candidate produces proposed outputs while the original workflow retains control. Run both against the same ticket inputs and compare the observable result. A difference is a reason to inspect the case, not automatic proof that the candidate is wrong. The existing route can contain errors too.

Include a temporary directory failure, an uncertain category, and a repeated ticket. On failure, staff should still be able to find the original work. On replay, the candidate should refer to the existing record. When routing is uncertain, the system should describe the review state rather than claiming automatic success.

Ask the shift lead to walk through the evidence in order. Can they see who owns the ticket right now? Would the proposal improve triage? What would happen after disconnecting the service? These operational checks complement accuracy and help the customer decide when it is safe to introduce a live effect.""",
        """### The pilot is only as reversible as the handoff

A customer-facing release needs a named owner, a defined scope, a known smoke case, and an accessible fallback. Report which tasks passed and which still go to staff. Include the threshold that triggers pause and explain how to identify requests handled during the pilot.

Give the shift lead a small rehearsal. Have them recognize a failure, pause the feature, find an in-flight item, and confirm it remains in the manual queue. The ability to follow a runbook becomes part of acceptance evidence. A handoff is incomplete if preserving the workflow still requires the developer to be present.

Keep a log of responsibilities and a checkpoint for reassessment. A bounded approval can be extended later when the customer has enough evidence on new categories. A limited release that the operators can understand and reverse is often more valuable than a broader demonstration with uncertain ownership.""",
    ),
    "llm-evaluation-benchmarks": (
        """### Preserve comparability as the workload grows

A benchmark is a specified workload and scoring procedure. Freeze inputs, allowed evidence, expected behaviors, and the environment before measuring alternatives. Record an identifier for the set so another reviewer can tell whether a change in results came from the model or from different cases.

Separate exploratory inputs from a comparison set. Exploratory cases reveal failures and guide fixes. If you tune repeatedly on the reporting set, it becomes part of training by another route. Add a new, representative set before using the result to justify a wider release.

Include standard cases and critical slices such as missing evidence or a required handoff. Report the denominator per slice. Combining all cases can answer how a candidate performed on this mixture, but it cannot establish competence in a rare behavior for which the data offers little evidence.""",
        """### Inspect what disagreement is telling you

A rubric should translate impressions into observable criteria. Review exact source support, completeness, and appropriate handoff separately. Two reviewers can agree on fluency while disagreeing on whether a major claim needs evidence. Make the consequential distinction explicit before collecting the final ratings.

Double-rate a subset and retain disagreement examples. Raw agreement is the fraction of matching ratings. A chance-adjusted measure asks how much agreement remains after accounting for the raters' overall use of each category. An imbalanced rubric can yield high raw agreement even when raters rarely agree on the rare failure.

Use the workbook to compare the measures, then read the underlying examples. If the wording caused different interpretations, update the rubric and rerate a fresh subset. If qualified reviewers still disagree, describe the uncertainty or escalate to a domain owner rather than creating a single spurious label.""",
        """### Pair cases before comparing candidates

When candidates see the same tasks, compare the results case by case. An improvement on one case and a regression on another can cancel in the mean. The paired record lets a reviewer find that trade. Repeatedly sampling paired observations can provide an interval for the observed difference, within the assumptions of the sample.

Report latency with attempts and timeouts. Include all paid requests in cost per correct task. A candidate charging a small amount per call can be expensive per accepted result if it often requires retries or human correction. State what your cost estimate includes and what it leaves out.

Inspect critical slices before ranking the full sample. Report counts and assess how representative they are. A lower-cost candidate with one additional consequential failure may be ineligible even when its average quality estimate is comparable. The decision depends on the separate gate agreed before evaluation.""",
        """### Keep a hold decision available

State the eligibility gates before comparing scores. A candidate may need to pass critical behaviors, have enough cases to support the estimate, and meet latency or cost limits. Rank only those that are eligible. This prevents a very large benefit on routine tasks from purchasing a smaller but unacceptable risk.

Describe the proposed release, conditions, and evidence together. An apparently strong candidate may need more samples on a language slice. Another may be acceptable for a read-only job but lack evidence for a more consequential action. Scope is part of the decision.

A decision memo should explain why a rejected option was held and what would change that result. Maintain the evaluation set and recorded version so a later rerun reflects a known change. If no option passes, retaining the current service is a legitimate outcome of the benchmark.""",
    ),
})


READINGS.update({
    "retrieval-system-engineering": (
        """### Keep the meaning of a document attached to every chunk

Ingestion turns sources into fragments, but each fragment still belongs to a document, a revision, and an eligibility rule. Use stable identifiers with a clear relationship between the source and its chunks. Record when a revision takes effect and what audience can see it. A document that is present is not necessarily relevant to the requested time.

Segment on structure where possible. A table cell can depend on its row and column headers, and an exception can depend on the paragraph before it. Inspect the stored fragments before training or tuning retrieval. An index cannot restore context discarded at ingestion.

Test revision changes and permissions together. Demonstrate that a new version takes over on the effective date and that a historical lookup can still find earlier eligible evidence. Keep deletion and replacement behavior explicit. A stale fragment left in a secondary index can affect results even after the primary record was updated.""",
        """### Learn why each retrieval signal works

Lexical ranking uses visible terms. Exact matches are particularly important for names, dates, codes, and form numbers. A dense representation can place differently worded descriptions near one another. That helps with synonyms and concepts while sometimes weakening the distinction between related but different identifiers.

Evaluate both signals on the same labeled questions. Inspect one exact reference and one paraphrase before averaging. Make sure candidates are eligible for the user and query date before scoring relevance. A perfect semantic match from a restricted source should never become an ordinary candidate.

The demo uses a small corpus so you can inspect what each representation includes. Note which fields are encoded and whether a title or body changes the result. Transfer those questions to a real corpus before choosing an index or model. Better retrieval comes from a clearer definition of relevance as well as better ranking.""",
        """### Diagnose candidates before tuning the final order

Combine lexical and dense rankings when their strengths complement each other. Rank-based fusion can favor candidates that appear high in either list without requiring compatible score scales. A later reranker can use more context to order the smaller set, at the cost of another processing step.

For a labeled query, inspect the candidate pool before reranking. If the correct passage never arrived, changing the final scoring cannot recover it. If it appears but falls after the cutoff, ranking is a plausible fix. Track recall at each candidate limit and the rank of the first relevant result to separate the two questions.

A practical evaluation includes exact codes, synonyms, restricted sources, and queries with no answer. Compare latency along with relevance. A marginal improvement in order might not justify an additional stage for the routine workload. Keep a few cases that visibly improve and regress so the choice can be explained.""",
        """### Verify the citation at the boundary where it is used

A citation should point to an eligible source version and support the exact claim. Check that the identifier belongs to the passages made available to the model. Then inspect whether the relevant passage supports the stated amount, date, and exception. The same document title can refer to different content over time.

Update tests when evidence changes. If a result was cached while a source was current, it can outlast the source's permissions or effective date. Bind the cache to scope and revision, or revalidate before returning the answer. Give missing and contradictory evidence distinct outcomes callers can understand.

Try one answer with a correct amount and an incorrect source. Try another with a correct source but an unsupported exception. A useful validator catches both. When evidence remains incomplete, return an explicit handoff. That fallback preserves trust better than presenting a citation that a reviewer cannot reproduce.""",
    ),
    "durable-agent-tool-runtime": (
        """### Discover a contract, then inspect it

An MCP client establishes a session with a compatible server and requests its tool definitions. A definition can describe the shape of inputs and the tool's purpose. It is useful evidence about how to form a request. The application must still decide whether a tool is appropriate and verify that its behavior meets that contract.

In the local exercise, use the agenda lookup in read-only mode and compare the listed schema with the actual result. Record the server version and one known output. When debugging, distinguish a transport error, an unknown operation, an invalid argument, and a successful call that returned no useful evidence.

Treat external tool descriptions as data from another boundary. A readable description does not give the server authority to change the caller’s task. Keep the allowed operations narrow, test permission separately, and make the failure state legible to the reviewer.""",
        """### Check both the argument and the actor

Validation asks whether a request has a well-formed resource identifier and expected fields. Authorization asks whether this caller can perform that operation for that resource. A guest and an approved reviewer can send identical valid payloads and should receive different outcomes.

Perform the authorization check in the trusted application or service boundary before dispatch. Use the caller identity provided by that boundary rather than a role asserted by generated text. Give read-only operations and persistent writes separate decisions. On a denial, return a controlled outcome with enough context for an operator to investigate.

Write paired tests for the same resource and different roles, plus a malformed request from an allowed role. The malformed case proves shape is checked. The paired case proves shape does not substitute for authority. Record the rejected reason without logging more request data than necessary.""",
        """### Persist the state a person saw when they approved

A waiting workflow needs data that can survive restart: the proposed effect, its exact revision, who can approve it, the recorded approval state, and the next legal transition. If the worker only holds that state in memory, a restart can transform an approved or pending effect into an ambiguous one.

Bind approval to the reviewed version. In the agenda exercise, change the note after storing a pending request and verify that approval for the old note cannot apply to the revision. Restore a checkpoint in a fresh process and confirm it reports whether the workflow is still waiting.

Approval and completion are distinct facts. An approval authorizes an effect under specified conditions. A completion record reports that the effect happened. If an operation can succeed while a response is lost, retain a stable identifier and a reconciliation route. Resume only after you can tell which facts are already durable.""",
        """### Define what a replay is allowed to do

An idempotent operation can accept repeated requests for the same intended effect without producing a second effect. Use a stable identity tied to the logical operation, not a new identifier for each delivery attempt. With a local database, committing a note and its completion record together gives the next worker one place to inspect.

A remote service may complete a write before the caller times out. Local memory alone cannot tell whether it happened. Use the service's idempotency contract where possible, otherwise reconcile before retrying. When evidence still cannot establish what happened, stop and ask an operator instead of sending a second notification blindly.

Log the operation identity, reviewed revision, effect state, and retry disposition. Verify a successful repeat returns the prior result and a genuinely changed request needs a new decision. The trace should explain why the system resumed, waited, or declined to repeat the action.""",
    ),
    "llm-adaptation-inference": (
        """### Separate knowledge from behavior before changing weights

A frozen model is a baseline for the task as initially specified. A retrieval-assisted version can add current evidence without modifying that model. An adapted version changes behavior learned from examples. Compare all three on identical held-out inputs so a routing convention improvement is not confused with adding the latest directory.

An autoregressive model predicts a distribution for the next token given earlier tokens. For a routing task, inspect whether the expected label is a single token for the local tokenizer. If tokenization differs, score complete labels consistently. Measure both task outcomes and how confidently the model assigns probability to the expected label.

Include an unfamiliar category and a case that should go to staff. A model that labels routine requests more consistently may still fail when outside its evidence. Keep the simpler retrieval or rule baseline and identify what the extra training is meant to improve before spending compute.""",
        """### Tune a small correction and inspect what transfers

A low-rank adapter represents a weight adjustment as two smaller factors. During training, keep the base fixed and optimize the factors on the training split. This reduces the parameters you need to update, while the base model still determines much of the representation available to the correction.

Compare training loss with a held-out task score. Fitting familiar labels can improve likelihood without improving what users receive. Inspect whether the model learned a stable convention or simply memorized the examples. Include valid evidence, contradictory evidence, and a realistic request that should be handed off.

Record adapter shape, base revision, data split, and optimizer settings. If the adapted configuration improves only easy requests or regresses critical slices, test a narrower route or retrieval baseline. The small workbook illustrates the mechanics of adaptation. Its result does not establish the expected gain for another model or workload.""",
        """### Measure precision trade-offs on the path that runs

Quantization stores values with lower precision. A typical integer scheme pairs compact values with scales that approximate the original values when used. Payload bytes include those scales and any metadata. Also report whether the measurement covers the adapter, the base model, or the whole deployment.

Lower storage cost is independent of faster inference. Unpacking or converting values can cost more time in a local implementation. A production runtime with suitable kernels might behave differently. Repeat the same workload on the same machine, record warm-up and measurement conditions, and report latency separately from quality.

Check both task behavior and numerical drift. Small changes in scores can flip a decision near a threshold even when average performance barely moves. Use cases near the edge and actual routing outcomes to decide whether a compression setting is acceptable.""",
        """### Transfer the protocol as you change the model

A checkpoint experiment should record its model identity, tokenizer, local precision, label format, and hardware. Freeze the task and held-out cases first. Once the checkpoint is loaded, measure the frozen baseline before training the correction so the comparison remains interpretable.

Inspect one input and its label encoding. If an expected label spans several tokens, the score you get from looking at one token does not describe that label. Match the score to the task, and ensure the fallback remains in the evaluation. Report both result quality and the cost of reaching it.

If the optional transformer checkpoint does not improve, preserve that result. Compare it with the simple fixture and identify which assumption stopped transferring. The exercise is about producing evidence for a deployment decision, including a choice to keep the simpler baseline or restore the known-good configuration.""",
    ),
    "ai-reliability-release": (
        """### Count a good request as the caller experiences it

A service-level indicator should define a usable result. For an assistant, that could require a valid answer or useful handoff within a deadline. A transport success with a late, malformed, or unsupported result might fail this definition. State the eligible population and observation window.

An objective of 99% good results allows 1% bad results in the chosen window. If the measured bad rate is 5%, the budget is being consumed at five times the allowed rate for that window. Burn expresses the pace of failure relative to the target, rather than the total incident impact on its own.

Check the cohort denominator and sample size. A small sample can be enough to reveal a severe problem, even though it gives a noisy estimate of the true rate. Decide when to alert, when to gather more evidence, and when a critical failure independently requires pausing.""",
        """### Follow a trace from user outcome to the earliest divergence

A stage trace connects the user's result with what happened in routing, retrieval, generation, and validation. Record timings, versions, outcomes, and a request identity. Keep sensitive content out of telemetry when a category or identifier is enough. A low-level exception alone rarely tells an operator what the user experienced.

Compare an affected request with a similar stable one. Start at the earliest point where their behavior differs. Slow generation might be the visible issue, while the deeper cause could be an overly long context, a dependency delay, or a new route. Distinguish those observations from hypotheses.

Exercise the distinction in the lab by injecting a delay at a known stage. A report that attributes the failure correctly gives the next responder a bounded place to investigate. Include fallback behavior so served results do not hide a failed primary or an unexpected burden on staff.""",
        """### Protect the canary from misleading averages

Assign a small cohort to the candidate and measure that cohort alongside comparable stable traffic. Record both the attempted and served versions, especially when fallback is enabled. If most requests use the baseline, a healthy aggregate can coexist with a candidate that fails much more often.

Predeclare a primary outcome, minimum observation requirement, and blocking conditions. Consider valid results, latency, fallback burden, and cost per usable task. Confirm that the canary contains the cases the release will serve. Missing evidence may justify holding the current exposure while collecting more data.

Keep the rollback route live and define who can invoke it. In the workbook, compare one passing and one failing cohort. An operator should be able to explain which criterion blocked expansion and what observation would justify resuming, without reverse-engineering the decision from a headline score.""",
        """### Close the loop from rollback to user recovery

Restore the prior serving version and verify the effect through a request representative of the affected cohort. Confirm version, result, latency, and whether any manual work remains queued. The rollback can restore new traffic while leaving older work that still needs reconciliation.

Build a timeline while evidence is available. Separate detection, decision, mitigation, verification, and follow-up. Preserve the observed impact and the source of each observation. If the cause is uncertain, label it and assign a way to investigate rather than treating a plausible story as a confirmed explanation.

A useful follow-up has an owner and a verification condition. “Add monitoring” is vague. “Alert when generation wait breaches the candidate gate on the replayed fixture” tells reviewers how to know the change works. Verify that people can still resolve delayed requests, not only that the graph returned to normal.""",
    ),
})
