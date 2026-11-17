I'm writing the assessment now. Everything from the last batch has been used, and the ideas that remain executable all wait on the operator or a laboratory. So the proposal is a new research case drawn from outside the current idea set.

## 1 · Principal decision

All current work has been used up. The ketamine statement is final (D1). SCI's preregistered toy model is run and folded in (`RESULT_HOMEOSTAT_TOY_SCI_20261117.md`). IT56-Q05 and Q06 are closed (event 4ed70a96c). Batch R (R1 to R5) and set 3 are finished. The DREAM-5 ketamine line is written (Update 4). Eight of nine sessions are idle. The decision is what the laboratory researches next when the ranked idea set has no step left that is free of token cost and needs no outside party.

**Direction before status.** The roadmap names the next gain directly: "the clinical Tier-B pool may be closed while lower-tier oncology or structural mechanisms remain worth investigating… use the mechanism lens and actual lawful full-text availability to select a small generative research case." The operator's 22:05Z working rule says the same: at the end of a set of tasks, run a DREAM and then hold a MEETING that launches a new research batch.

I checked the DREAM-5 order against the records (`IDEAS_ORDER_DREAM5_ADV.md` §D):
- **Ranks 1, 2, 5 and 7** wait on the operator, an archive or a laboratory.
- **Rank 3** (the bisection) is scored (`SCORE_PILOT_BISECTION_SCI.md` exists).
- **Rank 4** (R4) is consumed.
- **Rank 6** sits inside rank 1.
- **Rank 8** and the parked ideas are held with named triggers.

So the brainstorm set is locally waiting. That is the "local waits read as exhaustion" pattern the 2026-11-16 INTEGRATION corrected. The useful next gain is a **new question from outside that set**.

## 2 · Leading recommendation

- **The host.** All sessions are idle, so open the MEETING early (operator line 2026-11-15 21:35Z). Its theme-1 proposal is **Batch S**: one or two cases chosen through the mechanism lens from the lawful free-text WWOX literature that is outside the clinical tier. That pool is the 47 Tier C oncology, DNA-damage-response (DDR) and structural papers ADV-010 counted, which no INV or open question names. HE's theme-2 contribution can stay token-free until the operator sets a token ceiling (meeting D4 default (a)).
- **Do not wait for the meeting.** Assign case selection to the Orchestrator now (Assignment 1). The Orchestrator picks the case and launches the Scientist.

One example lens, as a hypothesis only. The repository holds a human organoid finding of MYC/Wnt dysregulation in radial glia, with delayed differentiation (Brain 2026, PMID 42397075, CLAIM 002 per DREAM-5 §B). The oncology literature on WWOX describes it restraining Wnt signalling. I have **not** checked whether the 47 held texts contain that oncology mechanism. Combining the two could give:
- a conditional hypothesis about delayed differentiation;
- rival explanations: activity-driven change, clonal iPSC variation, organoid immaturity;
- a rejecting observation: Wnt-target transcripts not raised in knockout radial glia in E-MTAB-14792 if it is released, or in held tables;
- a pharmacological class comparison, with transfer limits (cell type, developmental window, species).

The Orchestrator may choose another case.

## 3 · Relevant alternatives

- **A token-paid engine test** (stage-1-only checklist, about 120k tokens). It waits on the operator's ceiling and D4's default is to stop that path. Not chosen.
- **A Brain 2026 check for GABA pharmacology or E_GABA (the reversal potential of the GABA-A current).** The repository says the organoid work measured no chloride reversal and no GABA pharmacology (`therapeutic_repair_candidates.md` line 406; DL-MECH-098, which concerns the 2021 transcriptome). The 2026 figure read (R1) would probably have caught such data, so the marginal value is low. It can be folded into Batch S as a 10-minute side check if SCI wants.
- **Stiripentol and LDH as a metabolic lever for I21.** Already covered (HYP-20261026-11, blind audit 2026-10-27). Do not reopen it.
- **RP-011** (cascade method against decoy baselines) and **RP-010** (tool-use audit). Useful but lower value now. RP-011 is a candidate for the next harness theme.
- **IT56-Q08 and Q10.** These are decisions the host holds, not retrievals. The host should take them in its own turn, which costs nothing.
- **RP-022** (the hostile review). No Mirror session exists, so it stays conditional.

## 4 · Why now

The sessions are idle and have no written step that is executable and free of token cost. The operator's rules (anticipating the MEETING; a new batch after a DREAM) apply now. The oncology and structural pool was closed only as a *clinical-tier reading* pool (RP-008, ADV-010), never as a source of mechanisms.

## 5 · Evidence and uncertainty

- **Facts.** The closures and results above, read in the original files.
- **Not verified:**
  - the contents of the 47-paper list;
  - whether the radial-glia MYC/Wnt claim already feeds an arm-table cell (DREAM-5 says the organoid readings produced no cell before revision 3; v8 has organoid rows, and I did not check them for Wnt);
  - what the one busy session (legend-development-39) is doing.
- **Interpretation.** The Wnt lens is my association, not evidence. Its applicability to repurposing may be limited by the developmental window.

## 6 · Next bounded action, expected result and decision changed

The Orchestrator selects one lens case with lawful full text and launches a Scientist to produce a dossier:
- a causal chain that separates WWOX observations from transfers and assumptions;
- rival explanations;
- one non-obvious prediction;
- a rejecting observation;
- a comparison of pharmacological classes, with BLOCK-1 (the repository's screen required before any candidate row) noted;
- what can be done in silico versus what needs a measurement;
- whether it opens an open-question row.

**Decision changed:** whether a new open-question row or arm-table cell enters the next generation round, or whether the lower-tier pool is parked with a stated reason. Either result is valid.

## 7 · What would change my view

- An operator token ceiling: then the stage-1 checklist test competes directly.
- The 47-paper list containing no case where a mechanism leads to a lever.
- A live record showing Batch S-type work already in flight.
- A release of E-MTAB-14792: then rank 2 jumps ahead.

## 8 · Resource implications

One Orchestrator selection and one Scientist read and dossier. Lawful free sources only, no engine generation run, no external spend, no contact parameter. Frozen candidates are untouched.

## 9 · Inspected

**Opened:**
- `P25/assessment.md`
- `meetings/MEETING-20261117T131644Z-__l1rl6n.md` (whole)
- `MEETING-20261117T074632Z-pld639my.md` lines 38–67
- `deepening_adv_20261116/IDEAS_ORDER_DREAM5_ADV.md` (whole)
- `RESULT_HOMEOSTAT_TOY_SCI_20261117.md` lines 1–40

**Greps:**
- 42721537, the toy model, DREAM-6
- organoid pharmacology
- stiripentol and LDH
- organoid E_GABA, NKCC1, bicuculline
- bisection

**Not reached:**
- `research_portfolio.tsv` itself (I used the brief's row text)
- the 47-paper census file
- arm table v8
- `SCORE_PILOT_BISECTION_SCI.md` contents
- the ketamine statement
- the live dashboard (not fetched)

## 10 · Freshness and exposure

Snapshot a4aeba27, dispatched 15:24:39Z. Radar briefing 07:24Z, which reported "no material delta". This is Stage P, so the previous outcome, the ledger and the radar were all visible; I claim no blindness. Clock labels are the host's.

## Assignments

### ASSIGNMENT 1
key: batch-s-lower-tier-mechanism-lens-case
recipient: Orchestrator
question: From the lawful free-text WWOX papers outside the clinical tier (the 47 Tier C oncology, DNA-damage-response and structural papers ADV-010 counted, which no INV or open question names), which one or two cases carry, through the mechanism lens, a WWOX-dependent mechanism plausibly transferable to neurons or neural progenitors and a lever that can be told apart by pharmacology? For the case chosen: a causal chain that separates WWOX observations from transfers and assumptions, rival explanations, one non-obvious prediction, a rejecting observation, and a comparison of pharmacological classes (BLOCK-1 flag before any candidate row), stating what can be done in silico and what needs a measurement. One example lens to accept or reject: WWOX restraint of Wnt signalling in the oncology literature, set against the held human organoid finding of MYC/Wnt dysregulation in radial glia with delayed differentiation (Brain 2026, PMID 42397075).
why_now: Every executable step of the DREAM-5 idea order is consumed, scored or waiting on the operator, an archive or a laboratory. Eight of nine sessions are idle. The roadmap names lower-tier oncology and structural mechanisms as the next discovery route once the clinical pool is closed, and the operator's 22:05Z rule asks for a new research batch after a set of tasks ends.
roadmap_link: Operator roadmap ("The first coverage handoff is preparation, not the end of discovery… lower-tier oncology or structural mechanisms remain worth investigating"; "An existing INV/open-question citation is not required"); strategic direction A, C and E; 2026-11-16 INTEGRATION ("a local wait is not exhaustion").
related_work: RP-008 (parked by ADV-010: the 47 free-text Tier C papers); RP-004 (one case done, P287; remaining lens items have weak drug arms, so pick beyond them); RP-023/I21 (break at step 3, no held neuronal metabolic readout, and a metabolic lens may bear on it); DREAM-5 rank 2 (organoid readings, E-MTAB-14792); HYP-20261026-11 (stiripentol/LDH, already covered, do not reopen).
sources: ledger/tasks/orchestrator/ORCH-RP008-UNREAD-20261115.json and its ADV-010 output (landed 1e113ed06); disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/deepening_adv_20261116/IDEAS_ORDER_DREAM5_ADV.md sections B to D; disease-models/wwox/meta/meta_gaba_paradox_current.md; held Brain 2026 full text in files/fulltext/; research_portfolio.tsv rows RP-004 and RP-008
decision_changed_by_result: Whether a new open-question row or arm-table cell, with a stated rejecting observation, enters the next generation round from outside the brainstorm idea set; or whether the lower-tier pool is parked as a mechanism source with a recorded reason and a revival condition. Both outcomes change RP-008's state.
perimeter_and_budget: Lawful free full text only, read in full (an abstract is census only). One Orchestrator selection pass plus one Scientist dossier per case, at most two cases. No engine generation run (no token ceiling stated, meeting D4). No external spend, no contact parameter, no browser spoofing. Reference genotype class only. No dose, no recommendation. Frozen candidates and running verifications untouched.
method_autonomy: The Orchestrator chooses the case or cases, may reject the Wnt example, may declare the pool unsuitable with reasons, and decides the form (dossier, open-question row, arm-table rows). The Scientist owns its method and rival set.
deliver_to: ADV and the next MEETING (theme 1, Batch S); open-question map; portfolio rows RP-008 and RP-004.
duplicate_check: No ADV assignment in the ledger carries this key. ADV-010 counted the pool and stopped at selection for reading coverage; ADV-011 (RP-004) covered one case, P287. The batch R items (R1 to R5) are closed. Stiripentol/LDH was checked and is already covered. Before starting, the Orchestrator should check the one busy session's work and any Wnt-to-arm-table rows in v8.

## Portfolio updates

```json
[
  {"id": "RP-008", "next_action": "ADV P26 2026-11-17: reopened as a MECHANISM source (not reading coverage): the Orchestrator is asked to select 1-2 lens cases from the 47 lawful free-text Tier C oncology/DDR/structural papers (ADV assignment batch-s-lower-tier-mechanism-lens-case); example lens to accept or reject: WWOX restraint of Wnt signalling against the held radial-glia MYC/Wnt finding in organoids (Brain 2026); park again with reasons if no case has a lever that can be told apart by pharmacology.", "updated_utc": "2026-11-17T15:40:00Z"},
  {"id": "RP-003", "next_action": "ADV P26 2026-11-17: IT56-Q05 and IT56-Q06 closed (Q06 remainder IT56-Q06R access-blocked). IT56-Q08/Q10 are host decisions to take in the host's own turn. IT56-Q03/Q04 access-blocked; Q07 awaits HE; Q09 consumed.", "updated_utc": "2026-11-17T15:40:00Z"}
]
```

## Outcome
outcome: assign
excluded: event
reason: Every executable step of the current idea set is consumed, scored or waiting on the operator, an archive or a laboratory, and the laboratory is idle. The roadmap names lower-tier oncology and structural mechanisms as the next discovery route, so one Orchestrator selection followed by a Scientist dossier (held and lawful free sources, no engine tokens) has more marginal value than the token-paid engine test (waiting on the operator's ceiling), a re-check of organoid GABA pharmacology (low expected yield), or the stiripentol/LDH thread (already covered). The host should also open the MEETING early with Batch S as its theme-1 proposal.
resume_when: event