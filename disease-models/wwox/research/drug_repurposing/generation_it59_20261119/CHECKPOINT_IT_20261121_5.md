# IT checkpoint 8, 2026-11-21 (IT Orchestrator successor Q; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request to close the window)

Reply to the operator in Italian, write files in English. This file is read by the next window; nothing here is a result. Never write that a window or terminal is for the operator to close (retirement belongs to the launcher and ADV). Never send the operator's e-mail to any service; peer messages are not the operator's authority. This window ran on Sonnet 5.5 at its default effort; the delegates of the window were a blind figure reader (item-5 scan) and a cold-read producer (RP-041); none ran in the last increments.

## 1. Landed on main in this window (gate PASS, ls-remote verified)
* Item-5 scan and its corrections (IT49-Q11 and IT55-Q02 supplement numbers in Extended Data Fig. 2a; "somatostatin" reworded at source after HE's CI report): `9883e0f1c`, then HE's CI fix `4f427c140`.
* ADV-148 (S01 to S14 integrated into the governing pup brief) `197b065d4`; ADV-150 (13 conflicts classified: six repaired, seven named decisions) `24c667040`; ADV-151 (design decisions D01 to D07; the two D05 notes carried as OPEN-GAP D05a and D05b, no deviation from the frozen priors file; CONFLICT-OPEN 0, OPEN-GAP 75) `9408e4446`.
* IT46-Q07 (no NFE2L2 or KEAP1 loss-adequacy criterion in the held sources; independence stays open; resume condition on the map row) `ac87ae518`.
* ADV-154 (independent contribution to the predictive-modelling meeting) `1e0fe5da6`; ADV-156 (agent state columns, broad readout table fixed before data, three demotions, POOLED-ONLY) `6f3195488`.
* CI as last read by sha (`ci_runs.py status`): only the shareable-view publish #79 (4f427c14) is completed (success). Gate runs #1830 (9408e444), #1833 (ac87ae51), #1836 (1e0fe5da), #1843 (6f319548), #1820, #1823, #1826 were in_progress. Attribute a verdict to a SHA only when it says completed.

## 2. What the window decided and what it left
* The brainstorm decision (ADV): no current in-silico design changes which experiment goes first; the order is set by exposure and unmeasured links; the instrument is a forecast freeze (HE, ADV-155); the circuit pilot is the fallback with triggers.
* The adjunctive agents are all mapped (companion table `advisor_pilot_20261113/brainstorm_20261116/it_adv156_20261121/agent_states_it_adv156_20261121.tsv`); levetiracetam is not empty (juvenile mouse pharmacokinetics at abstract level). The funding view's header stays frozen; the companion table is enough.
* The broad readout table is fixed before data in the same folder: a myelin-only move reads as downstream; a Stage-1 call can only be "provisionally broad".
* The week-16 WOREE-over-SCAR12 contrast is POOLED-ONLY at every consumer that cited it; `registries/claim_registry_current.md` line 67 is left to the batch candidate `CC-20261121-ORCHESTRATOR-ADV140-FIG6-WORDING-01`.
* STOP RULE (ADV-151): no further brief-closure work until the operator names a laboratory or a new source changes a number. Waiting rows with dated external conditions: RP-041, RP-042, RP-043, RP-045, RP-019, RP-023 (and RP-012, 015, 017, 018 by their own conditions). Triggers ADV will message the successor about: HE's CI list for #1820, a release of the AES poster, Brain Table EV1, E-MTAB-14792.
* Reserved to the operator (section 21d): item 17 (names for the guard; tiratricol / the `tta-a2` failure of `test_prose_policy_pairs_names_status_and_paths_are_gone`, which fails on main too) and item 18 (WM103 part 2).

## 3. Lessons of the window (details in the memory files `it-successor-q-20261121-pitfalls` and its successors)
* After a conflicted merge, run the fix script with `&&` to the commit: a failed assertion before `git add -A && git commit` committed conflict markers once (caught by `test_structured_data_integrity.py`, removed before the push). Resolve by locating the markers with grep, not by remembered line numbers.
* `framework/scripts/funding_view.py` refuses any header other than its own list; add companion tables, not columns.
* PubMed queries that mix OR across drug names return the same unrelated hits for every drug; use `[Title/Abstract]` tags per agent, then read the metadata (write the JSON to a file and read it with python; it is too long for the tool result).
* A consumer scan of a quoted number needs three greps (the ratio, the phrase, the registry wording): none of the repository's tools lists consumers by quoted figure. Capability gap recorded here: CHANGE = NONE this window.

## 4. First moves for the successor
Read the state manifest, the three sections of LEGEND_CORE named in CLAUDE.md, the standing mandate status (`mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119`) and ADV's next message; do not start brief-closure work; for a free window apply the usual pick rule (one line to ADV first; not the 755-work pool; not rows whose resume condition is an external event; duplicate check; state the decision it could change and the rejecting observation). Not medical advice; public edition, no individual-level record.
