"""Concrete input-to-result walkthroughs for decision-focused lectures."""

TRACE_PAIRS = {
    "ai-literacy": (
        ("The office receives ‘North Wing closed. No reopening date yet.’",
         "A rule can flag the missing reopening date. A prediction can estimate call volume using past closures. A generator can draft an update from the confirmed note. Only the last step produces text for families, and a person checks it before sending."),
        ("A draft reads ‘The district voted unanimously to reopen.’ The minutes contain a reopening motion but no vote tally.",
         "Retain only what the minutes support. Mark the tally unknown and check the recording or the clerk's report before describing the vote."),
        ("The FAQ draft and a reimbursement approval each take five minutes to review.",
         "Publishing a reversible, checked FAQ is a smaller pilot. Approval affects a real payment, so preserve the existing reviewer and authorized rules."),
        ("A draft request includes a student roster, parent phone numbers, and a confirmed event time.",
         "Extract the time, place, and audience category into a new brief. Keep the roster with the school. Verify the resulting notice against the confirmed event information."),
    ),
    "using-ai-at-work": (
        ("Someone writes ‘Tell everyone the workshop changed.’ The destination room is confirmed, the accessible entrance is still being checked.",
         "Brief the tool to write to registered attendees, retain the confirmed location, and identify the entrance as pending. Check those three requirements before judging the tone."),
        ("Source notes say ‘Room 204, Friday at noon, seats assigned by a lottery.’ The draft promises a seat to anyone registering Friday.",
         "Restore noon and the allocation rule. Have the event owner check the room separately. These are distinct factual and audience checks."),
        ("A shared calendar says Friday. The owner’s signed update, dated later, says the event has been postponed without a new date.",
         "Send the owner both records and the paused draft. Ask for the decision needed to publish. Log who owns the next update."),
        ("An assisted draft takes 5 minutes to create, 8 to review, and 4 to fix. The previous verified draft took 15 minutes.",
         "Compare 17 minutes with 15. Record corrections separately. Prefer the method that meets the deadline and quality requirement on comparable cases."),
    ),
    "ai-product-decisions": (
        ("A support lead wants a chatbot. A sample of 40 incoming requests contains 12 that bounced between teams.",
         "Start with a routing pilot. Measure first-team accuracy and time to a responsible owner on the same 40-case design before proposing a broader customer assistant."),
        ("One caller wants a policy link. Another needs to compare conditions for two different routes.",
         "Return the current source directly for the first task. For the second, test whether a source-grounded explanation preserves both sets of conditions. Keep the simpler approach as the baseline."),
        ("The candidate routes 18 of 20 requests correctly. Its two failures are both urgent access requests.",
         "Keep urgent access requests on manual intake. Publish the urgent-case denominator alongside overall performance and set a separate gate for that group."),
        ("The pilot saves six minutes per routine call. The owner of the manual fallback will be on leave during rollout.",
         "Keep the pilot bounded until the fallback has an owner and a verified response time. Write the pause rule into the release decision."),
    ),
    "managing-ai-delivery": (
        ("A team reports ‘pilot complete’ and shares an encouraging screenshot without the case set.",
         "Request the versioned inputs, current workflow, comparison results, and approval record. Tie the milestone to evidence the next reviewer can reproduce."),
        ("A supplier renews a model endpoint and the application changes its review behavior on the same day.",
         "Assign separate owners to endpoint verification and the release gate. Replay the frozen checks and restore the stable route if the gate fails."),
        ("Most routine requests succeed, but a sample uncovers a single missing critical escalation.",
         "Pause the affected cohort, retain the record, and verify manual intake. Ask the named owner to approve reopening against the critical cases."),
        ("Operations receives an issue report but cannot tell which deployment version produced it.",
         "Attach the versions, reproduction case, workaround, and owner. Verify the fallback with the person who will use it before transferring responsibility."),
    ),
    "evaluating-ai-in-practice": (
        ("Six trials contain five routine reminders and one ambiguous closure notice.",
         "Record the planned workload and include cases with missing or conflicting instructions. Keep the difficult cases visible in a separate row so success on reminders cannot hide failures."),
        ("A notice gives the right room but omits that the accessible entrance has moved.",
         "Score the room and the entrance separately. Record the omitted access instruction as material because it changes whether an attendee can use the notice."),
        ("A candidate saves 20 minutes of drafting and adds 16 minutes of review over five notices.",
         "Report four minutes of total savings and the count of material corrections. Check who absorbs the review time and whether it moves past a deadline."),
        ("Both workflows handle routine reminders. The assisted one turns an unconfirmed location into a published fact.",
         "Keep assisted drafting for confirmed reminders. Route unconfirmed locations to the organizer and specify a repeat test before revising the decision."),
    ),
    "model-selection-for-leaders": (
        ("A vendor demo answers familiar questions quickly. The intended workload includes archived policies and restricted cases.",
         "Refuse to infer coverage from the demo. Write one acceptance case for dated material and another for access. Test both vendors against the same conditions."),
        ("Two vendors both score 90%. Their errors occur on different requests.",
         "Put outcomes side by side for each request ID. Let reviewers resolve disagreements and state which failure would reverse the choice."),
        ("A low-cost endpoint needs twice as many manual checks as its competitor.",
         "Combine price, verified successes, and reviewer minutes. Include escalation staffing and the cost of retreating to the current process."),
        ("A candidate passes the bounded pilot, but performance after a version change is unknown.",
         "Approve only the tested scope and version. Name the supervisor who can stop rollout and specify which evidence is required to approve a replacement."),
    ),
    "sparse-model-architectures": (
        ("Two selected experts emit 2 and 6. Their normalized weights are 0.75 and 0.25.",
         "Multiply and sum to get 3. Top-1 gives 2 with the first expert alone. Changing k changes the forward computation, while the full bank still needs to fit across the serving devices."),
        ("The preferred loads are [6, 2] and capacity is [4, 4].",
         "Plain routing serves six assignments. Rerouting moves two assignments to the quieter expert and serves all eight. Test the changed outputs before deciding whether better utilization is useful."),
        ("Rank 0 sends 64 tokens to an expert on rank 1. Each token has 4,096 two-byte elements.",
         "The send is 512 KiB and the return is another 512 KiB. Time the transfer and the slowest rank separately. Payload alone leaves the collective and queueing costs unknown."),
        ("One 32-layer model uses full attention in every layer. The hybrid has eight full-attention layers and 24 fixed-state layers.",
         "Multiply token-dependent bytes by 32 and 8 respectively, then add the fixed hybrid state. Before selecting the hybrid, check exact recall on a long policy and compare with summarized logs."),
    ),
    "reasoning-efficient-inference": (
        ("A cheap attempt succeeds twice in four requests. Expensive attempts recover one of the two failures. Each cheap attempt costs 1 and each expensive attempt costs 4.",
         "The cascade spends 4 + 8 = 12 for three verified successes. Always-expensive uses 16 on the same fixture. Check each request separately before treating a similar aggregate score as equivalent."),
        ("Three candidates report [West, Lift, East] at cost 4, [West, East] at cost 6, and [West, East] at cost 7. The lift is closed, and the direct segment costs 7.",
         "The first is infeasible, the second misstates cost, and the third passes. A one-attempt budget abstains. Feasibility only certifies this route against the supplied contract."),
        ("A draft proposes a, b, x, d. The greedy target agrees on a and b and selects c next.",
         "Commit a, b, c. Verify the continuation from that prefix. This trace assumes greedy verification and does not cover stochastic acceptance."),
        ("One hundred warm requests have time to first token of 85 ms. Three cold requests take 140, 210, and 310 ms.",
         "The pooled p95 is 85 ms, and the cold p95 is 310 ms under the nearest-rank definition. A 200 ms cold gate fails despite the reassuring aggregate."),
    ),
    "decision-models-and-policies": (
        ("The urgency estimate is 0.19. Unnecessary action costs 2, a missed issue costs 8, and review costs 0.50.",
         "Expected action cost is 1.62, waiting costs 1.52, and review costs 0.50. Choose review while a reviewer has capacity. This calculation assumes review resolves the uncertainty at the stated cost."),
        ("Two technician slots are free. Job A takes both slots for benefit 9. Jobs B and C each take one slot and yield 6.",
         "Enumerate feasible sets. B and C yield 12 together. If A is mandatory, it becomes the feasible optimum. Record infeasibility explicitly when mandatory jobs exceed capacity."),
        ("A four-row log chooses the target action once with logging probability 0.25, and that row has reward 1.",
         "The inverse propensity estimate is (4 × 1) ÷ 4 = 1, with an effective sample size of 1. Withhold a confident policy comparison. If any target action has zero support, the estimator cannot cover that context."),
        ("Deferring gives 3 units now and creates a repeat visit costing 5. Inspecting gives 1 now and leaves the job resolved.",
         "A one-period policy defers. A two-period policy with no discount compares −2 and 1 and inspects. Include repeat visits in the eval before changing the schedule."),
    ),
}


WORKED_TRACES = {
    slug: tuple(f"### Follow the example\n\n**Given:** {given}\n\n**Walkthrough:** {decision}"
                for given, decision in traces)
    for slug, traces in TRACE_PAIRS.items()
}
