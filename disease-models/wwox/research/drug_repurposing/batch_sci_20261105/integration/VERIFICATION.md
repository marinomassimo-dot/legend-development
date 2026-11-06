# Verification record: who checked what, with which result, and what remains unverified

Non-canonical research record. Not medical advice. Producers and verifiers were different subagent contexts; verifiers saw no producer conclusions in the blind audits. Models as shown in the runtime's own notices: producers `claude-opus-5` / `claude-opus-5-5`; verifiers mostly `claude-fable-5-1`; the map reader ran on a smaller model. The `model` parameter is a request: the per-turn model was not read back from every transcript. All verdict files are in `verify/`.

## Layers

1. **Mechanical (Orchestrator):** table widths and headers, quote length, staged-receipt validators with the PubMed DOI check on every receipt, wording the public gate would block, headline counts recomputed from the tables (the combined matrix is rebuilt from the tables, not from READMEs), a trial record of all staged receipts in a throwaway clone (**TRIAL OK**, 109 receipts).
2. **Blind quote audit** (auditor sees only the row's fields and quote, acquires the source itself): first pass on every evidence row, then a delta pass on every changed or added row.
3. **Adversarial review of conclusions** (reviewer sees README, tables and module inputs; recomputes numbers, runs its own searches, judges overreach, double counting, vocabulary against the consumer files).
4. **Author response** (`RESPONSE.md` in each package) after each round; the Orchestrator then adjudicated and applied narrowing edits where only wording was at stake (`ORCHESTRATOR_EDITS.md` in B1, R1, R2).

## Results by package

| Package | Blind audit (rows) | Review (statements) | Delta audit (rows) | Residue |
|---|---|---|---|---|
| A1 WWOX reports, outcomes and denominators | 57: 45 supported, 7 overshoot, 5 undershoot | 24: 5 hold, 17 narrow, 2 reject (schema) | 33 (29 A1 + 4 A2 rows): 33 supported | A1 first-round claims were written after some re-reads began (declared) |
| A2 infantile-spasm baseline | 43: 40 supported, 2 overshoot, 1 undershoot | 14: 7 hold, 7 narrow | (4 rows, in the A1 pass) | its derived power figure (about one in four) was recomputed by the reviewer: exact |
| B1 vigabatrin white matter | 38: 25 supported, 9 overshoot, 2 undershoot, 2 attestations | 19: 0 hold, 9 narrow, 1 reject (decision); proposals 2 hold, 5 narrow, 2 reject | 23: 12 supported, 7 overshoot, 3 undershoot, 1 attestation | 14 narrowing edits by the Orchestrator **not re-audited** |
| R1 restoration, syndromic models | 62: 42 supported, 6 overshoot, 6 undershoot, 8 unverifiable | 67 statements shared with R2: 21 hold, 39 narrow, 7 reject | 50: 39 supported, 6 overshoot, 3 undershoot, 2 attestations (verified to hold); the two sources first unreachable were then audited | 19 narrowing edits **not re-audited** |
| R2 restoration, DEE and human | 64: 55 supported, 7 overshoot, 1 not in source (mis-assigned locator), 1 unverifiable | (shared) | 34: 27 supported, 5 overshoot, 1 undershoot, 1 attestation (verified true) | 10 narrowing edits **not re-audited** |
| Map | none (not a literature package) | none | Orchestrator spot checks of three claims (scout-plan table limit, FlyBase/ORCS mentions, public site): all held | rows are file-evidence statements; not independently re-derived |

## What the independent checks changed (the findings that mattered)

* The shared headline "myelin after onset has never been tested" in both restoration packages was a search artefact; withdrawn and replaced by the narrower, true statement (sheath morphometry after onset in a neuron-driven lesion).
* B1's "start age decides does not survive a full-text human reading" was rejected: it inverted the human record; the age band is supported in infants, the animal half is abstract level.
* B1's "four independent cohorts" were three centres; a hormonal association was wrongly called absent; a request for a non-existent card-level harm tag was withdrawn.
* A1's "11 read in full text" contradicted its own receipts; its discordant children all had qualified responses with no sustained instrumented response; the Choi 2026 children probably belong to a 64-child cohort that supplies the denominator.
* A2's arm-level nulls are undemonstrated differences (power about one in four), not shown absences.
* Both restoration packages proposed vocabulary that already existed or was unnecessary; the observation identifiers collided; the consolidated set replaces both.
* Self-caught by an author: a plausible replacement quotation written from memory was re-checked against the source and found not verbatim (R2, row R58).

## Unverified or weaker-than-full evidence that travels with the package

* Edits listed in `b1_whitematter/ORCHESTRATOR_EDITS.md`, `r1_restoration_ndd/ORCHESTRATOR_EDITS.md`, `r2_restoration_dee/ORCHESTRATOR_EDITS.md` were made from the auditors' governing passages without reading the sources and were not re-audited.
* Rows resting on abstracts (B1 29 rows, R2 10, A2 21, A1 2 plus manifest-reused ones) support conditional leads only; the depth is in every row's `source_depth`.
* No figure image was inspected in any source; no supplement was read except where a row says so. No receipt is a complete read.
* The two WWOX children of the vigabatrin MRI report: abstract only; full text not reachable; overlap with the 64-child cohort is probable and unproven.
* Not executed: map rows `WO-06` and `RS-R6` (stopped twice by the account usage limit), `IT29-P12`, `TS-01`.
