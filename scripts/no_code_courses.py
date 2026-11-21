"""Original lectures and practice for nontechnical and leadership learners."""
from course_types import Course, Lecture
from specialist_courses import LEADER_SELECTION


NO_CODE_COURSES = (
    Course(
        "ai-literacy", "AI Literacy",
        "Recognize where AI can help, where it can fail, and how to verify an output before using it.",
        "No AI account or technical background needed.",
        "Make a one-page AI-use checklist for a task you encounter at work or at home.",
        "Include the task, a simpler alternative, one fact to verify, and a reason to stop or ask a person.",
        (
            ("Recognize the capabilities", (
                Lecture(
                    "What AI can do", "Distinguish prediction, generation, and rules in a familiar workflow.",
                    "A rule applies a condition someone specified. A predictive model estimates a label or value from patterns. A generative model produces content, such as text or an image, from a request and the information it receives. Several of these can coexist in one workflow.",
                    "A help desk uses a rule to acknowledge every ticket, predicts which team should own it, and drafts a response with a generative model. The support employee still checks that the response answers the right question.",
                    "Classify three tasks as rules, predictions, or generation. Warn when a field is empty, estimate when a parcel will arrive, and draft an update to the customer.",
                    "The missing-field warning is a rule, the arrival estimate is prediction, and the draft update is generation.",
                ),
                Lecture(
                    "Why confident answers can be wrong", "Identify a claim that needs independent verification.",
                    "Language models generate plausible continuations based on learned patterns and supplied context. A fluent answer can include unsupported facts, outdated details, or an invented source. A link or citation is useful only when it actually supports the claim.",
                    "A tool says expenses must be filed within 45 days. The current dated policy says 30 days. Reading the policy resolves the discrepancy.",
                    "A generated meeting summary says a decision was unanimous. What would you check before reporting that detail?",
                    "Check the notes or recording for the actual votes. If the record is incomplete, report that the decision was recorded and omit the claim about unanimity.",
                ),
            )),
            ("Decide when to trust the output", (
                Lecture(
                    "Choose an appropriate use", "Choose a task where errors are easy to detect and reverse.",
                    "Consider the consequences of a wrong answer, how quickly someone can catch it, and whether it can be reversed. Low-stakes drafting can be a good trial when a reviewer understands the source material. Decisions affecting people, money, or safety call for tighter controls and a clear owner.",
                    "Rewriting an internal agenda is easy to review and reverse. Automatically approving an employee reimbursement affects money and calls for authoritative rules and accountable review.",
                    "Choose a first pilot among drafting a public FAQ, approving a refund, and deciding who qualifies for benefits. Describe what review is still needed.",
                    "Draft the FAQ from current approved material and have its owner verify every answer before publication.",
                ),
                Lecture(
                    "Handle sensitive information", "Decide whether information can be shared with an AI tool.",
                    "Check the organization's policy, the tool's approval for the data, and whether the task needs the information. Sensitive details can appear in text, attachments, transcripts, and metadata. Removing names may leave other details that identify a person.",
                    "To improve the tone of a customer email, you can use a synthetic example that preserves the writing problem while removing the real account, contact, and order details.",
                    "A teammate wants to paste a spreadsheet containing real customer complaints into a public assistant for rewriting. Propose a safer way to practice.",
                    "Use invented examples or an approved internal tool with suitable access controls. Share only fields needed for the exercise.",
                ),
            )),
        ),
    ),
    Course(
        "using-ai-at-work", "Using AI at Work",
        "Write clear requests, review generated work, and design a simple human handoff.",
        "AI Literacy or equivalent. All activities can be done on paper or in a document.",
        "Improve a low-risk draft and retain a short record of the brief, checks, and edits.",
        "Your final draft meets the brief, uses verified facts, and identifies who owns approval.",
        (
            ("Request and review a draft", (
                Lecture(
                    "Turn a request into a clear brief", "Write a brief with context, constraints, and a checkable output.",
                    "A useful brief specifies who will read the output, the intended decision or action, which facts to use, and the shape of the response. Explicit unknowns give the reviewer a way to distinguish missing information from invented detail.",
                    "Instead of asking for a good office notice, specify its audience, the known closure date, a 100-word limit, and ask for a placeholder if the reopening date is unknown.",
                    "Write a three-sentence brief for an email about a rescheduled training session when the replacement date is unknown.",
                    "Ask for a short email to enrolled staff. State the original date and the fact of postponement. Ask for a placeholder for the new date and omit speculation.",
                ),
                Lecture(
                    "Review output against the source", "Use a short checklist to catch factual and format errors.",
                    "Review a draft against its request and original evidence. Check names, dates, numbers, claims, and audience. A polished rewrite can silently change a requirement or remove a caveat.",
                    "The source says office access resumes Monday at 10 a.m. A draft says Monday morning. The missing time matters to early arrivals, so restore it.",
                    "The source says registration closes Friday at noon and places are limited. A draft says to sign up by Friday and guarantees a seat. List both corrections.",
                    "Restore the noon deadline and remove the seat guarantee. Include the actual allocation rule if it is available.",
                ),
            )),
            ("Build a repeatable workflow", (
                Lecture(
                    "Design a human handoff", "Write a fallback for incomplete or conflicting information.",
                    "A handoff names who reviews the issue, what evidence they receive, and what action waits for their decision. Define the trigger before using the workflow so the same situation gets the same treatment.",
                    "When two handbooks give different leave rules, the assistant can flag the discrepancy and send both dated references to HR. Publication pauses until HR confirms the applicable rule.",
                    "Design a handoff for a customer notice when two internal documents disagree on the launch date.",
                    "Send both dated records and the draft notice to the launch owner. Hold distribution pending a confirmed date.",
                ),
                Lecture(
                    "Measure whether the workflow helped", "Compare the new workflow with the current workflow using a fair baseline.",
                    "A baseline records what happens today for comparable work. Count time spent prompting, checking, and reworking alongside drafting time. Track outcome quality and time separately so a faster draft does not hide larger review costs.",
                    "If the old workflow takes 15 minutes and the new one takes 5 minutes to draft plus 12 to check, the new process takes 17 minutes for that example.",
                    "Plan a comparison for drafting five routine notices. What will you record for each method?",
                    "Use comparable notices. Record total time including review and the number of material errors corrected. Compare both outcomes before expanding use.",
                ),
            )),
        ),
    ),
    Course(
        "ai-product-decisions", "AI Product Decisions",
        "Turn an AI proposal into a measurable decision about a bounded pilot.",
        "AI Literacy or equivalent. No coding required.",
        "Write a proposal for a two-week pilot of an AI feature or workflow.",
        "State the problem and baseline, compare alternatives, define a success metric and guardrail, and name the reviewer.",
        (
            ("Find the right problem", (
                Lecture(
                    "Frame the decision before selecting a model", "Describe a business workflow in terms of its user, friction, and outcome.",
                    "Start with who does the work, which decision they make, how often it occurs, and where the current process fails. Quantifying the baseline makes proposals comparable. A narrow problem gives a pilot a result you can attribute to the change.",
                    "Instead of proposing an AI help desk, target the time to route incoming requests to the correct team. Measure routing time and how often requests are reassigned.",
                    "Reframe ‘We need a chatbot for onboarding’ into a user, a repeated problem, and a measurable outcome.",
                    "New hires have trouble finding the correct benefits form. Measure how many find it without contacting HR and how long it takes.",
                ),
                Lecture(
                    "Compare rules, search, and generation", "Choose the simplest design that can meet the requirement.",
                    "Rules suit clear, stable conditions. Search can surface authoritative sources for a person to read. Generation helps when users need a tailored explanation or draft and the team can check it for fidelity. A single product can combine all three.",
                    "An eligibility checker can use approved rules. A policy library can use search. Drafting a personalized summary from verified policy may justify generation with review.",
                    "For finding the current travel policy, compare keyword search and a generated answer. What would justify adding generation?",
                    "Begin with search and source links. Add generation if users repeatedly need to combine multiple passages and evidence shows that summaries retain the correct policy details.",
                ),
            )),
            ("Set evidence and limits", (
                Lecture(
                    "Define success and guardrails", "Write a primary metric and a separate quality threshold for a pilot.",
                    "The primary metric describes the intended gain. A guardrail limits a downside that could make the gain unacceptable. Both need a population, a measurement method, and a decision threshold before the pilot begins.",
                    "A routing pilot aims to cut median routing time by 20% while keeping the wrong-team rate at or below the current 5%. Measure on the same ticket categories under both methods.",
                    "A draft assistant is supposed to save review time. Write one success criterion and one guardrail for customer notices.",
                    "For example, reduce median total drafting and review time by 20% while allowing zero incorrect deadlines in the reviewed notices.",
                ),
                Lecture(
                    "Make a ship, revise, or stop decision", "State a decision based on pilot evidence and remaining uncertainty.",
                    "Use the agreed thresholds. Report what was measured, which cases were underrepresented, and the next decision. A small pilot can justify a larger trial when uncertainty remains. It rarely establishes that a result will carry over to every team or workload.",
                    "A pilot meets its time target and misses its accuracy guardrail. Hold rollout, inspect which cases failed, and rerun a targeted pilot after correcting those failures.",
                    "Your pilot meets both thresholds on 20 routine cases. It includes no urgent cases. What is the next decision?",
                    "Consider a bounded expansion for routine cases. Keep urgent cases in the established process until they are evaluated separately.",
                ),
            )),
        ),
    ),
    Course(
        "managing-ai-delivery", "Managing AI Delivery",
        "Assign ownership, review launch evidence, and decide when to pause or roll back an AI feature.",
        "AI Product Decisions or equivalent. No coding required.",
        "Prepare a launch decision for a pilot and practice responding to one simulated incident.",
        "Name an owner, affected groups, approval evidence, pause criteria, and rollback or fallback procedure.",
        (
            ("Own quality and risk", (
                Lecture(
                    "Find the failure hidden in the average", "Identify a critical user group or circumstance that needs its own evidence.",
                    "A slice is a meaningful subset of cases, such as a language or request type. Aggregate accuracy can be high while a small group experiences frequent errors. Review slices with distinct consequences and report how many examples were checked.",
                    "A tool is correct on 95 of 100 tickets. If all five mistakes are urgent tickets, the overall score obscures the urgent-case failure.",
                    "A feature is correct on 99 of 100 outputs. The one wrong answer gives an incorrect emergency contact. What evidence would you ask for before expansion?",
                    "Ask for a dedicated emergency-contact check, including current authorized source records and representative variations. Require that slice to pass its own criterion.",
                ),
                Lecture(
                    "Assign decision and data ownership", "Name who owns release, data access, ongoing quality, and escalation.",
                    "A release has several distinct decisions. The product owner weighs benefit, the data owner approves use, the reviewer judges evidence, and an operator can pause service. A named person or accountable role for each decision helps prevent gaps.",
                    "For a staff assistant, HR can own policy data, a product manager can own pilot scope, and support operations can own monitoring and rollback.",
                    "An employee reports that a document appeared outside its intended audience. Name two roles that should act immediately and what each decides.",
                    "The operator pauses access or switches to the fallback. The data owner assesses which documents and audiences were affected and decides how access should be restored.",
                ),
            )),
            ("Launch and respond", (
                Lecture(
                    "Plan a limited launch and rollback", "Define the trial audience, stop condition, and fallback.",
                    "A limited launch exposes a feature to a controlled audience first. Decide which signals pause it, who monitors those signals, and what users experience after rollback. Validate the fallback before opening access.",
                    "A pilot covers one department. If a restricted document is shown to an unauthorized person, the operator immediately turns off the feature and returns users to the approved document portal.",
                    "Draft a launch scope and stop rule for the first week of a meeting-summary assistant.",
                    "Limit the pilot to opted-in internal meetings. Pause if private content is distributed outside the participant list. Return to the established manual notes workflow.",
                ),
                Lecture(
                    "Review an incident and decide when to resume", "Separate containment, learning, and the relaunch decision.",
                    "Contain the failure first and preserve records needed to understand its impact. Identify the cause, add a test that would catch it, and verify the correction before resuming. Record who approves the relaunch and which limits still apply.",
                    "An assistant sent an outdated notice. The team stopped the output, corrected the source selection, verified a case with conflicting versions, and asked the content owner to approve resumption.",
                    "A pilot generated summaries using superseded procedure documents. Give one containment action, one corrective test, and one condition for resuming.",
                    "Pause affected summaries, test retrieval against a current and superseded document, and resume only after the current document is reliably selected and the responsible owner approves.",
                ),
            )),
        ),
    ),
)


NO_CODE_COURSES += (
    Course(
        "evaluating-ai-in-practice", "Evaluating AI in Practice",
        "Compare AI-assisted workflows with an evidence scorecard and a recorded keep, revise, or stop decision.",
        "AI Literacy or equivalent. Use the examples on each lecture page with paper or a document.",
        "Submit a one-page evidence scorecard for an AI-assisted workflow. Use three representative cases and record the existing method, review time, quality failures, and your next decision.",
        """Include one case with incomplete evidence, one potentially harmful error, the review burden, and a condition that would reverse your decision.

Copy this scorecard into a document and fill it in before writing your recommendation.

| Case | Expected result and source | Current result and time | Assisted result and total review time | Material error or omission |
|---|---|---|---|---|
| Typical | | | | |
| Incomplete evidence | | | | |
| High consequence | | | | |

Finish with your decision, the allowed scope, the reviewer, and the evidence that would change the decision.""",
        (
            ("Build the comparison", (
                Lecture(
                    "Pick cases that represent the real task",
                    "Build a small case set with typical, ambiguous, and out-of-scope requests.",
                    "A useful comparison begins with real work patterns. Choose cases that expose different demands rather than multiple versions of the easiest example. Define the intended answer or decision from a trusted source before testing. Replace personal information with invented equivalents.",
                    "For meeting summaries, a routine agenda, an unresolved decision, and a confidential item exercise three different expectations. Your examples should preserve uncertainty and omit the confidential item from public notes.",
                    "Create three cases for an assistant that drafts facilities notices. Give each case an expected result.",
                    "Use a confirmed closure date, an unknown reopening time, and a private contact detail. Expect the confirmed date, an explicit unknown, and no private detail.",
                ),
                Lecture(
                    "Score evidence and omissions",
                    "Use a small rubric consistently and record why an output passed or failed.",
                    "Define the evidence before reading results. Use observable checks such as correct date, source supports the central claim, and unresolved details remain visible. One serious failure can outweigh several correct cosmetic details.",
                    "A draft preserves the event date and claims a replacement venue without a source. Record a pass on the date and a fail on the unsupported venue.",
                    "A summary correctly reports the deadline and leaves out a required approval. Score the two details separately and decide whether to send it.",
                    "The deadline passes. The omission fails the approval check. Revise before sending because the omitted step changes what the audience may do.",
                ),
            )),
            ("Make a decision with evidence", (
                Lecture(
                    "Measure time and review burden",
                    "Calculate the total effort and compare it with the existing workflow.",
                    "Measure drafting, verification, rework, and handoff separately. Track how many outputs required major edits. A faster initial answer can increase total effort if checking and correction are expensive.",
                    "Manual work takes 18 minutes. An assisted version takes 5 minutes to draft, 7 to verify, and 8 to correct. The assisted workflow takes 20 minutes and adds review work.",
                    "Manual drafting takes 22 minutes. Assisted drafting takes 6 minutes, verification takes 8, and corrections take 3. Compare the time and write one remaining quality check.",
                    "The assisted path takes 17 minutes and saves 5. Check a material fact such as the deadline and record whether the result still meets the original standard.",
                ),
                Lecture(
                    "Record a keep, revise, or stop decision",
                    "Make a bounded recommendation with a named reviewer and a test for revisiting the decision.",
                    "Use the fixed criteria and record which cases support the decision. Keep a short note of what you tested, what failed, the allowed scope, and what evidence would change the decision. A three-case scorecard supports a small experiment and leaves uncertainty explicit.",
                    "An assistant saves time on routine notices and gives a misleading answer on an emergency closure. Keep emergency notices on the manual workflow and test routine notices with an assigned reviewer before any expansion.",
                    "Write a decision for a workflow that saves time but has one sensitive-data failure. State what could make it safe to retry.",
                    "Pause that workflow. Remove or protect the sensitive input, assign an accountable reviewer, and recheck the relevant failure cases before a bounded restart.",
                ),
            )),
        ),
    ),
)


NO_CODE_COURSES += (LEADER_SELECTION,)
