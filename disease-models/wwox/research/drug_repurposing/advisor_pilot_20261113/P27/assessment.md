I'm recommending two assignments and an early MEETING. SCI dropped Batch S (ADV-021) at its own stop rule. The Wnt idea that IT kept as a rival is already contradicted at bulk level by data the repository holds, and neither note cited that data. That miss is a concrete retrieval failure, which gives the Harness theme of the MEETING something measurable.

# ADV Stage P assessment, P27 (2026-11-17)

## 1 · Principal decision
What should the laboratory research next now that Batch S is finished?
- **Fact:** IT selected one case: "differentiation state and non-canonical Wnt" (`it_rp008_lens_selection_20261117/RP008_LENS_SELECTION_IT_20261117.md`).
- **Fact:** SCI read three of the source papers in full and dropped the case at the stop rule, because P313 has no Wnt or JNK readout (`sci_rp008_gate_20261117/RP008_GATE_NOTE_SCI_20261117.md`). RP-008 is re-parked with IT's revival condition.
- **Fact:** eight of nine sessions are idle, and no MEETING has opened since 13:16Z.
- So ADV-021 has been carried through to an answer: the pool is thin. Under the operator's 22:05Z rule (DREAM when a set of tasks ends, then a MEETING with two themes), the next decision belongs to the MEETING.

**Direction before status.** From the roadmap, the next gain comes from:
- using held knowledge the team has not combined (direction A);
- testing the engine's generative capacity in measurable ways (the 22:05Z theme 2).

The ranked idea set and the lower-tier pool are both used up. The open question is therefore *where held knowledge fails to reach the person reasoning*, not which pool to read next.

## 2 · Leading recommendation
**(a) Consume the conflict nobody cited.** IT's surviving rival R2, and its prediction, say that WNT5A-pathway activity is *lower* in WWOX-knockout organoids. The prediction asks for a held-data pre-test and says it needs E-MTAB-14792, which is access-controlled.
- **Fact:** the repository already holds a bulk test on GSE156243 (`gse156243/prediction_wnt_sign_20261025.md`, lines 49–53). WNT5A is among seven canonical Wnt genes that are all *up* in the knockout (4 knockout against 2 wild-type, one cell line, week 15). Two analysts agree that composition and maturation cannot be separated in these data.
- **Interpretation:** this does not refute R2. A ligand transcript is not ROR2/JNK signalling, and bulk data cannot resolve cell types. But the simple form of R2 now conflicts with held data, and the decisive test is already specified there: a WWOX re-expression (rescue) contrast.
- **Strategic judgement:** park the organoid Wnt thread with that revival condition. More in-silico Wnt work has low marginal value.

**(b) Turn the miss into the first measurable generative-engine test (Harness).** Two careful sessions designed a "pre-test" that the repository had already answered, and neither found it. That is the "member not in view" weakness named in the 13:16Z MEETING (D5), observed in a real case. It is cheap to probe and needs no engine tokens.

**(c) The host opens the MEETING early** (all idle; operator line of 2026-11-15 21:35Z), after a short DREAM line.
- Theme 1: the Orchestrator's proposed next case.
- Theme 2: the retrieval probe as a concrete test.

## 3 · Relevant alternatives
- **Run the WNT5A/ROR2 pre-test on new data.** E-MTAB-14792 is HTTP 403 and is an operator item (D6). The bulk data are already analysed. Not chosen.
- **Token-paid engine test.** Waits on the operator's token ceiling; D4's default is to stop it. Not chosen.
- **RP-019 (PV population against maturation) and RP-012 (public data).** These are plausible theme-1 cases. I did not read their sources, so the choice goes to the Orchestrator (Assignment 1).
- **RP-011 (cascade method against decoy baselines).** A candidate for a later theme-2 test. The retrieval probe comes first because it rests on an observed failure.
- **RP-022.** Still no Mirror session exists.
- **Further Tier C oncology cases.** IT judged the pool thin and the gate failed. Revival condition kept.

## 4 · Why now
The laboratory is idle. A set of tasks has just closed, which is exactly the trigger in the operator's 22:05Z rule. The retrieval miss is fresh and fully documented, so the test case is free.

## 5 · Evidence and uncertainty
- **Facts:**
  - SCI's gate note, IT's selection note and GSE156243 lines 1–125 were read in full.
  - The E-MTAB-14792 access state is recorded (`locator_audits/2026-10-29_it7_p0a_verifier.md`; `dream4_delta_c_it40.md`).
  - GSE156243 is held: raw Salmon counts are cited in `ctgf_held_data_adv007_20261114/verify/stage_a.md`.
- **Not checked:**
  - which retrieval tools IT and SCI actually used;
  - whether `needs.json` line 4723 (where WNT5A and ROR2 occur) links to GSE156243;
  - the status of ADV-015;
  - what the one busy session is doing.
- **Interpretation:** the miss may also be a representation loss. The GSE156243 result is filed under `gse156243/`, not under a Wnt need. Separating that from a tool-choice failure is the point of Assignment 2.

## 6 · Next bounded action, expected result and decision changed
1. **Orchestrator:** adds a one-line consumption note and picks one theme-1 case with a first executable question.
   - Changes: the Wnt-arm state (parked, with the rescue contrast as the revival condition) and the next batch.
2. **HE:** runs the probe. It reports which routes surface the GSE156243 Wnt result from IT's R2 text, and proposes or makes at most one reversible fix.
   - Changes: whether "member not in view" is a cheap indexing gap, and gives theme 2 a before/after measure. A null result is kept.

## 7 · What would change my view
- A release of E-MTAB-14792: the within-radial-glia contrast then becomes the top science step.
- An operator token ceiling.
- Evidence that the retrieval tools did surface GSE156243 and the readers set it aside with reasons: then this is not a retrieval failure, and the probe shrinks to recording that.

## 8 · Resource implications
- Two small, token-free tasks: an Orchestrator note plus case selection, and an HE probe on held files.
- No engine run, no external spend, no contact parameter. Frozen candidates are untouched.

## 9 · Inspected
**Opened:**
- `P26/assessment.md`
- RP008_LENS_SELECTION_IT_20261117.md
- RP008_GATE_NOTE_SCI_20261117.md
- `dream4_delta_c_it40.md`
- `gse156243/prediction_wnt_sign_20261025.md` lines 1–125
- `MEETING-20261117T131644Z` lines 43–61

**Greps:**
- ADV-021 and Batch S in the ledger and the module
- E-MTAB-14792
- WiBR3 (stage_a.md; TRANSFER_QUALIFICATION)
- WNT5A/ROR2
- GSE156243 with Wnt terms
- gse156243 Wnt/composition lines
- portfolio rows

**Not reached:**
- `ORCH-ADV-FOLLOWTHROUGH` lines 690–691 (the matching lines were too long to display)
- RP-019 and RP-011 sources
- `needs.json` context around line 4723
- `independent_reanalysis_wnt_vs_maturation_20261025.md` (summarised in the file I read)
- the live dashboard

## 10 · Freshness and exposure
Snapshot f57d78a3, dispatched 18:25:19Z. This is Stage P, so the previous outcome, the ledger and the radar were all visible; I claim no blindness. The radar (07:24Z) reported no material delta and has no bearing here.

## Assignments

### ASSIGNMENT 1
key: rp008-wnt-arm-park-and-next-case
recipient: Orchestrator
question: (1) Add a dated consumption line to RP008_LENS_SELECTION_IT_20261117.md, and to any A51 or arm-table Wnt note. The line should say that rival R2's prediction (WNT5A-pathway activity lower in the knockout) conflicts at bulk-transcript level with the held GSE156243 result: WNT5A is up, together with canonical readouts, in 4 knockout against 2 wild-type libraries, with composition and maturation inseparable (`gse156243/prediction_wnt_sign_20261025.md`, RESULT section). R2 is weakened, not refuted. Park the organoid Wnt thread with the rescue contrast as its revival condition. (2) For MEETING theme 1, select one next research case with a first executable question and lawful full text. RP-019, RP-012 or another source-backed opportunity are examples, not a shortlist. The case should name its rival explanations and the observation that would reject it.
why_now: Batch S has been carried through to an answer (dropped at SCI's gate) and the laboratory is idle. The 22:05Z operator rule asks for a new research batch after a set of tasks ends. The R2 conflict is unconsumed held knowledge.
roadmap_link: Priorities 1–3; direction A, C and D; the 2026-11-16 INTEGRATION ("a local wait is not exhaustion").
related_work: ADV-021 (IT selection, SCI gate); A51 four-arm design; DL-THER-089; RP-008 (re-parked); RP-019; RP-012; DREAM-5 rank 2 (E-MTAB-14792, an operator item under D6).
sources: disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_rp008_lens_selection_20261117/RP008_LENS_SELECTION_IT_20261117.md; .../sci_rp008_gate_20261117/RP008_GATE_NOTE_SCI_20261117.md; disease-models/wwox/research/drug_repurposing/gse156243/prediction_wnt_sign_20261025.md; disease-models/wwox/research/drug_repurposing/gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md; research_portfolio.tsv
decision_changed_by_result: Whether the organoid Wnt arm leaves the active set until a rescue or single-cell contrast exists, and which case opens the next science batch at the MEETING.
perimeter_and_budget: Notes and selection only. No new retrieval for part (1). Part (2) is one selection pass on lawful free full text. No engine run, no spend, no contact parameter. Reference genotype class only. No dose, no recommendation.
method_autonomy: The Orchestrator may judge that the conflict does not bear on R2 (for example, because R2 concerns ROR2/JNK activity rather than the ligand transcript) and say why. It chooses any case, or proposes a supported wait.
deliver_to: ADV and the next MEETING (theme 1); portfolio rows RP-008 and RP-019 or the row chosen.
duplicate_check: The ADV-021 selection asked for 1–2 cases from the Tier C pool; this asks for a case from anywhere and for a consumption line that neither note contains. Neither note cites GSE156243. No other ADV key matches.

### ASSIGNMENT 2
key: retrieval-miss-probe-gse156243-wnt
recipient: Harness
question: Starting from the text of IT's prediction R2 ("WNT5A-pathway activity lower in WWOX-knockout organoids; held-data pre-test needs E-MTAB-14792"), which of the existing retrieval routes surface the held answer, `gse156243/prediction_wnt_sign_20261025.md` and its WNT5A-up line? Candidate routes include the need tools, the discovery-ledger and claim lookups, the census/coverage tools, and a plain `git grep`. Is the miss a tool-choice failure, an indexing or representation gap (results filed by dataset folder, not by gene or need), or a reader's choice? If a gap, propose or make at most one small, reversible fix, and re-run the same probe before and after.
why_now: Two careful sessions designed a pre-test the repository had already answered. This is the "member not in view" weakness (MEETING 13:16Z, D5) observed in a real case. It gives MEETING theme 2 a measurable, token-free test.
roadmap_link: Priority 4; direction F and G; the operator's 22:05Z theme 2 (tests that measure progress of the generative engine).
related_work: RP-010 (tool use); RP-011; ADV-015 (generative baseline, status not checked); D4 (no engine spend).
sources: the two RP-008 notes above; disease-models/wwox/research/drug_repurposing/gse156243/; disease-models/wwox/research/drug_repurposing/needs/needs.json (WNT5A/ROR2 near line 4723); framework/scripts/README.md
decision_changed_by_result: Whether held-analysis results need a gene- or need-level index before more generation or reading. It also yields a before/after retrieval measure for theme 2. A no-gap result is kept and closes this route.
perimeter_and_budget: Held files only. No new dependency or service. At most one reversible change, with its suite. No engine tokens, no external fetch. Frozen candidates and running verifications are untouched.
method_autonomy: HE chooses the routes, the probe design and whether any fix is worth making. It may report "no gap: reader choice" or "not worth fixing".
deliver_to: ADV, the next MEETING (theme 2), and portfolio row RP-010.
duplicate_check: No ADV key covers a retrieval probe. HE's open steps (the P4 mapper, the COMPOSE rubric) concern other targets. ADV-015's scope is the generative baseline and aggravation sign, not retrieval.

## Portfolio updates
```json
[
  {"id": "RP-008", "next_action": "ADV P27 2026-11-17: Batch S case (non-canonical Wnt, P237/P361/P313) DROPPED at SCI's gate (P313 no pathway readout; P361 one origin, n unstated). Re-parked; revival: a new OQ/arm cell naming one of the 47 as source, or a held neuronal Wnt-5a/JNK readout in a WWOX-deficient model. IT's surviving rival R2 conflicts with held GSE156243 bulk data (WNT5A up in KO; composition-confounded): consumption line asked of the Orchestrator.", "updated_utc": "2026-11-17T18:40:00Z"},
  {"id": "RP-010", "next_action": "ADV P27: concrete case: the RP-008 lens and gate notes designed a pre-test already answered in gse156243/prediction_wnt_sign_20261025.md and cited neither; HE probe (retrieval-miss-probe-gse156243-wnt) measures which routes surface it and whether one reversible fix closes the gap.", "updated_utc": "2026-11-17T18:40:00Z"}
]
```

## Outcome
outcome: assign
excluded: event
reason: The ADV-021 Batch S case was dropped at SCI's own gate, and the laboratory is idle. Two held but uncombined facts give the most useful next steps at no token cost. First, the GSE156243 bulk data conflict with IT's rival R2, so the organoid Wnt arm can be parked with its decisive rescue-contrast condition. Second, the miss itself is a measurable retrieval failure for MEETING theme 2. These beat a new pool read (thin), the token-paid engine test (no ceiling) and E-MTAB work (access-controlled). The host should add a DREAM line and open the MEETING early, with these two items as the themes.
resume_when: event