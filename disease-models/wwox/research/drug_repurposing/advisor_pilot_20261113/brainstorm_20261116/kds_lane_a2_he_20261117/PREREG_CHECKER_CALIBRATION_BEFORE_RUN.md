# Preregistration: calibration of a blind verifier on the operator's ketamine input (ADV-034 package 3; HE; written before the delegate is dispatched, 2026-11-17)

Question: does a blind, claim-faithful reading by one sonnet delegate (effort high, separate context) find defects that a quote-presence check passes? Case: the input (sha256 7c6a71956c43815679aaa394f98e521a57c011c6852a288158fc0ba1f90fa2e5) whose defects are known to HE from lane A (`kds_lane_a_he_20261117/LANE_A_AUDIT_HE_20261117.md`).

Design. One delegate, no knowledge of the answers. Its brief (`BRIEF.md`, sha256 720ba979a9f85cbbee50...) and sources (`SOURCES_ABSTRACTS.md`, sha256 507d3e8be2a23cbc7ce6...) are outside git; the brief names only the two files to read and says nothing about expected defects. Deviation from the assignment text, stated before the run: the assignment names the nine GSK-3beta abstracts; F6 (the pooled 24/30) needs the three pediatric series, so the sources file holds those nine plus the abstracts of Kuki 2024, Rosati 2012 and DeVine 2023 (12 abstracts). No dismech entry is given (F11 is therefore tested as an internal inconsistency of the input only).

Preregistered detection expectations (probability that the report states the defect, in its own words, in its findings or its table):
| Defect (lane A id) | What counts as detected | Expectation |
|---|---|---|
| F1: 34464676 is a tianeptine study; the ketamine sentence is background | the report says the study did not itself test ketamine on GSK-3beta, or that it studied tianeptine | 0.40 |
| F2: 37392896 reports ketamine lowering p-GSK-3beta | the report says the paper's direction is opposite to, or not as, the table states | 0.30 |
| F6: DeVine 2023 states no seizure outcome, so 24/30 is not derivable | the report says the 3 infants have no stated response or that 24/30 cannot be built from the abstracts | 0.30 |
| F11: text counts (15+3 edges, 4 paths) disagree with the pasted digraph (21 edges, 5 paths) | the report states either mismatch | 0.05 |
Secondary (no expectation fixed, scored and reported): F3 (the "prolonged" group is mostly hours-long or in vitro), F4 (40967562 not separable), F5 (context of 36334642/34089815), F10 is out of scope (not in the sources), omitted harms of Kuki 2024 and Rosati 2012.
False positives: each statement in the report that calls a statement of the input unsupported when the abstract does support it; I judge each against the abstract and report the count.
Expected number of the four primary defects found: 1.05 of 4 (sum of the probabilities). Expected false positives: 1 to 2.
Process checks after the run (from the delegate's transcript, not from its report): model and effort read back from the transcript; files it opened (it must open only the two named files; any other Read or search is reported and, if it touched the lane A files, the run is void for the leak); tool calls; tokens (expected about 60,000 to 100,000 in total).
Reading the result: finding F1, F2 and F6 each is a case a quote-presence check cannot find (the quotes are verbatim); so every detection is evidence for a claim-faithful reader at this cost, and every miss is a measured limit of one blind verifier on this case. One run is one observation, not a rate.
Stop rule: any account usage-limit notice stops the run; the partial transcript is kept and reported as incomplete.
