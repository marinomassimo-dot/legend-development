# Value trial IT2 - scoring protocol (fixed BEFORE any answer exists)

Scorer rules, items and the cost protocol. Nothing here has been applied to an answer: none exists.

## 1. Who scores, and how
- The scorer must NOT be the producer of this design (scientist-b) and should not be the actor who runs the answers. Preferred: an actor that has seen neither.
- The three answer files are relabelled X / Y / Z by the integrator (a mapping kept in a sealed file opened only after scoring). The scorer sees answer text only, never the condition, never the cost figures.
- Scoring unit = item of reference.md, 1 / 0.5 / 0. Half credit means the point is present but unqualified or only partly right, never "right direction, no source".
- Validity check BEFORE scoring, from the transcripts (not from the answers): ANY read, grep hit or listing of value_trial_it2_20261027/, the trial task JSONs (SB-IT2-VALUETRIAL-REF-20261027, VERIFY-VALUETRIALREF-20261027) or locator_audits/2026-10-27_value_trial_reference_verification.md VOIDS the run (the key is not in the clone, see README runner section); EXT run contains no read of a repository knowledge file; LOCAL run contains no network/MCP/adapter call; an answer breaching its allowed inputs is VOID and reported as such, not scored. COMBINED must have used both kinds of input, else it is reported as a degenerate run.
- Budget breach (more than 25 tool calls or 12 minutes in the transcript) is recorded; an answer written after the breach is scored but flagged.

## 2. Items and the five dimensions
| Dimension | Items (per case) | Max per case |
|---|---|---|
| Correctness of target / direction / context | V1: 1.1, 1.2, 1.4 ; V2: 2.1, 2.3 ; V3: 3.1 | 3 / 2 / 1 |
| Counter-evidence and limits found | V1: 1.5 ; V2: 2.4 ; V3: 3.2, 3.3 | 1 / 1 / 2 |
| Improper transfers (penalty dimension) | V1: 1.3 ; V2: 2.2 ; V3: 3.4 ; plus X.1 | 2 / 2 / 2 |
| Abstention quality | V1: 1.6 (reason) ; V2: 2.5 (abstention part) ; V3: 3.5 ; plus X.4 | 2 / 2 / 2 |
| Usefulness of the proposed next measurement | judged 0 / 0.5 / 1 per case (see 3) | 1 |
| Cross-cutting | X.2, X.3, X.5 | 3 |
Dimension sums are descriptive; the grand total is unweighted.

Exact count: reference items V1 6 + V2 5 + V3 5 = 16; cross-cutting X.1-X.5 scored once per case = 15 (X.1 and X.4 sit in the transfer and abstention rows above, X.2, X.3, X.5 in the last row); next-measure usefulness 3 (section 3). Grand total = 16 + 15 + 3 = 34. Report also the total WITHOUT the three next-measure rows (31), because that judgement is the most subjective.

## 3. Next-measure usefulness (the subjective row)
1 = a measurement that would discriminate between the stated alternatives, in a model matching the evidence, specific enough to run (analyte or readout, model, comparison) and not a treatment; 0.5 = a measurement that is relevant but generic or not discriminating; 0 = no measurement, a treatment, or a measurement in a model that cannot answer the question. An abstention with a reopening condition and no measurement scores on 1.6 / 2.5 / 3.5 only and 0 here.

## 4. Improper transfers
Counted both ways: the items above (1.3, 2.2, 3.4, X.1) and a separate TALLY of improper-transfer statements per condition (a sentence presenting another gene, disease, tissue or species as WWOX-DEE evidence or efficacy). The tally is reported as a count and is not netted against the score.

## 5. Observed cost versus self-estimate (the cost half of the trial)
Recorded per condition, per case set (one run covers all three cases):
| Quantity | Observed source (authoritative) | Self-estimate (reported separately, never substituted) |
|---|---|---|
| Tool calls | count of tool_use blocks in the subagent transcript jsonl, excluding none; also the harness `tool_uses` figure; if the two differ, both are stated (the P3A run showed 21 vs 23) | the number in the answer's RUN LOG |
| Tokens | the harness usage line returned when the subagent completes (total tokens), copied verbatim | any token figure the agent states |
| Wall time | the harness `duration_ms` of the subagent, and first-to-last transcript timestamp | minutes stated in the RUN LOG |
| Files / services touched | from the transcript | from the RUN LOG |
Report the ratio self-estimate / observed for each. An agent estimate is not a cost measurement; if the harness usage line is unavailable the token cell is "not measured" and no estimate fills it. Cost per quality point (observed tokens / grand total) is reported as a descriptive ratio only. Cost is measured for what was run, including the cost of reading registry text in LOCAL and COMBINED.

## 6. Pre-declared reading rule (set before the data)
- The result is descriptive. No claim of superiority, no ranking called a finding, no general statement about LEGEND's value. The earlier P3A C-versus-B margin of 0.5 points was not a finding and the same applies here.
- A difference between two conditions is called "visible" only if it is at least 4 of 34 points AND has the same sign on all three cases AND is not removed by dropping the next-measure rows AND the scorer was independent. Otherwise: "no distinguishable difference at this n".
- Even a "visible" difference is a statement about three cases, one run per condition, one model family, and says nothing about other cases.
- A result is worth reporting for the cost half even when the quality half is flat: tokens / time / calls per condition are observed quantities.

## 7. Declared weaknesses (carried from the P3A verification and new)
1. n = 3 cases, one run per condition, same model family; run-to-run variance is unknown. No repeat is planned; if budget allows, one repeat of the cheapest condition would measure it.
2. The reference is abstract-depth for every source (NA24 also full text, verifier) and was written by one actor. NI24, MO19, WA25 and YA25 are paywalled with no lawful full-text route for ANY condition, so items resting on them (1.4, 2.3, 3.1) are abstract-depth for EVERY condition and every verdict on them is abstract-level. Verification: locator_audits/2026-10-27_value_trial_reference_verification.md; corrections applied in this round.
3. The topics are absent FROM THE CARDS only. The repository holds registry rows for NI24, MO19, WA25, YA25, YO24, RI26, LU25, a partial full-text dossier of MO19, dossiers on WWOX case series and ferroptosis in epilepsy, and wave-4 vitamin B6 notes marked not-WWOX-evidence. LOCAL and COMBINED therefore START with those (the MO19 trap, the V1 negative and the V3 non-neural status are partly pre-resolved locally); that is local knowledge being tested, and the result must not be described as a test on unseen topics.
4. The same model family knows vitamin B6, SCN2A and ferroptosis in general; EXT is external for retrieval, not for prior knowledge.
5. The cases were chosen by the producer to have a fixable source-based reference and to contain a trap each; they are not a random sample of repurposing questions, and the trap design may favour whichever condition holds a relevant negative.
6. The producer of the design must not score or run the answers; the integrator should record who did what.
7. The 25-call / 12-minute budget is generous relative to P3A (about 20 calls, 2-4 minutes); a condition that needs more is penalised by the budget, not by the rubric.
