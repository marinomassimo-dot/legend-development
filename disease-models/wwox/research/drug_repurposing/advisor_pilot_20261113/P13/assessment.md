I'm drafting one assignment to the Orchestrator: run a mechanism-first case under RP-004, which no one has assigned yet. It isn't limited to the clinical tier or to sources an investigation already cites.

## 1 · Principal decision

**The decision:** what should the lab do next, now that ADV-010 (RP-008) has been delivered and used?

**What has happened since my last assessment (P12):**
- **RP-008 is parked.** IT's census found that none of the Tier B placeholders can be read lawfully for free. The 47 items with free text are all LOW-tier oncology papers, and no investigation or open question names any of them. The "pool exhausted" blockers hold as defined (`rp008_unread_census_it55_20261115/README.md` §Answer first; `ORCH-RP008-UNREAD-20261115.json` COMPLETE).
- **At 08:41Z the presidio chose not to assign anything new.** It weighed RP-002 and turned it down.
- **The PLAN session then recorded a discovery gap.** An item only counted as eligible if an investigation already cited it and it sat in a clinical tier, and nobody intended that filter (`PLAN-ADV-CONTINUOUS-RESEARCH-20261115.json` LIVE_OBSERVATION.discovery_gap). PLAN made RP-004 actionable: a mechanism-lens run found 74 candidates, 60 of them without a receipt (portfolio row RP-004).
- **The operator's roadmap line of 2026-11-15 asks for exactly this.** Lower-tier oncology and structural mechanisms stay worth investigating, and a new question doesn't need an existing citation.

So the choice is between a wait (the 08:41Z decision) and the mechanism-first case that the roadmap and the corrected portfolio now call for.

## 2 · Leading recommendation

Assign RP-004 to the Orchestrator. It picks **one** mechanism-first discovery case from the `unread_gold.py --mechanism` list. A case qualifies only if its full text can be read lawfully, and the eligibility test is whether a mechanism could change a pharmacological comparison or experiment, not whether an investigation already cites it. The Orchestrator then launches a focused Scientist batch, queued behind PRESIDIO-005, which Science is still working on.

**Facts:**
- The lens ignores tier and disease context by design (`framework/scripts/unread_gold.py` lines 91–136, the "DOMAIN_PARITY" lens with its catalysis and substrate-class clauses).
- No ledger task mentions RP-004 or `--mechanism`. I grepped `ledger/tasks` and found no match.

**Seed lead (an option only; the Orchestrator picks the case):** the WWOX SDR substrate question. Two published sources disagree:
- **Steroid substrates.** A 2011 enzymology study (PMID 21476439) measured activity on steroid substrates with oxidation only. It has been read completely (receipt FTR-20261004-21476439-01). A verifier note says its 78–89 % substrate-consumption figure can't be reproduced (`wwox_function_reference_it6_20261029.md` item 12).
- **Retinal substrate.** A 2015 structural review (PMID 25662954, census row P376, which has a PMC id) proposes that WWOX reversibly converts all-trans-retinal. It is "catalogued only" in `batch_queue.md`, and no receipt matched.

`unread_gold.py` itself calls these two proposals "mutually inconsistent … neither adjudicated". The retinal idea appears in no investigation or open-question row (my grep for "retin" in the map and `investigations.tsv` found only an unrelated eIF2B retina item, IT47-Q01).

**Interpretation:** this is held knowledge that has never been turned into a pharmacological comparison. The two substrate classes would point to different pathway levers (retinoic-acid signalling versus steroid or neurosteroid handling). The first rejecting observation would be that the review's proposal rests only on homology or modelling, with no measured reduction of retinal.

**Caution:** the SDR function thread was worked heavily in September (`analysis/q230p_*_20260922.md`, `function_per_molecule_assay_design_20260922.md`). So it is "new for drug repurposing", not new for LEGEND. The Orchestrator must check those files before choosing it.

## 3 · Relevant alternatives

- **RP-002:** weighed at 08:41Z. Its next steps depend on wet-lab work and its units have been through many rounds. Excluded, and I agree.
- **RP-001 contrastive replay:** held by the presidio until after the trial report. Not overridden.
- **RP-005:** not a separate assignment. The RP-004 case can carry a prediction frozen before reading, which would make it a prospective case at no extra cost.
- **RP-016 remainder:** the operator ruled out reassigning retrieval that was already used.
- **RP-017 / RP-018:** waiting on new measurements. PRESIDIO-005 is still in progress.
- **RP-021:** disposed.
- **RP-006, a small finding:** the census lists P290 (PMID 25703206) as unreceipted, yet `discovery_ledger_current.md` line 1206 records "Full text letto integralmente" ("full text read in full") from the 2026-07-12 mechanism audit. That is another reading declared without a receipt, outside the `drug_repurposing/` area IT scanned (IT itself lists that scan as not done). It is worth a note in the RP-006 row, not a separate assignment. The RP-004 selection must skip it, or record its receipt, rather than read it again.
- **RP-020 and the radar (ToolUniverse v1.5.10):** no scientific obstacle is waiting on either.

## 4 · Why now

- IT and HE are idle, and Science is busy with PRESIDIO-005, which takes priority.
- The operator's roadmap line and PLAN's correction name this exact case.
- The 08:41Z wait predates that correction, so its premise has changed.
- The trial report at 15:29Z is a reporting duty, not a reason to hold back capacity.

## 5 · Evidence and uncertainty

- **I didn't run `--mechanism`.** The 74/60 figures come from the RP-004 row.
- **Lawful access is unconfirmed.** For P376, "PMC id present" is not proof that the text is readable.
- **25662954 is a review.** The retinal proposal may rest on homology alone. That would itself be a useful negative, because it would leave the steroid assay as the only measured result.
- **Some of the 60 may be duplicates.** Readings declared without receipts, like P290, may also be among them.

## 6 · Next bounded action, expected result, decision changed

**Next action:**
1. The Orchestrator runs `--mechanism` on current main.
2. It removes items already read or declared read, including entries in the discovery ledger and the September analysis files.
3. It checks lawful access for the remaining items.
4. It picks one case and freezes, before reading, what the current outputs predict.
5. It launches one Scientist batch, queued behind PRESIDIO-005.

**Expected result:** one new question or conditional pharmacological contrast, with its transfer limits, rival explanations and a rejecting experiment. A supported abstention is also an acceptable result.

**Decision changed:** whether a new investigation or open-question row is created, which would also be RP-008's revival trigger; whether RP-005 gains a prospective case; and whether the substrate conflict moves into the repurposing loop or is closed with a reason.

## 7 · What would change my view

- The September analyses already settle the retinal-versus-steroid question. In that case the Orchestrator picks another lens item.
- All 60 items turn out to be paywalled or already read. RP-004 is then parked with evidence.
- PRESIDIO-005 reopens X1, which would compete for Science.
- An operator PAUSE line.

## 8 · Resource implications

- One Orchestrator selection pass using existing tools, then one Scientist batch, queued.
- No spend, and no contact parameter sent to any service.
- Nothing frozen is touched, and the PRESIDIO-005 worktree and battery are left alone.

## 9 · Inspected

**Read in full:**
- `advisor_pilot_20261113/P12/assessment.md`
- `research_portfolio.tsv`
- `ORCH-RP008-UNREAD-20261115.json`
- `PLAN-ADV-CONTINUOUS-RESEARCH-20261115.json`
- `rp008_unread_census_it55_20261115/README.md`

**Read in part:**
- `ORCH-ADV-FOLLOWTHROUGH-20261114.json`, lines 486–505
- `unread_gold.py`, lines 88–142
- `open_questions_map.tsv`, line 154

**Grep only:**
- `census.tsv` (selected rows)
- `discovery_ledger_current.md` (around line 1206)
- `wwox_function_reference_it6_20261029.md`
- registries for 25662954
- `ledger/tasks` for RP-004 and `--mechanism`
- the state of `ORCH-PRESIDIO004B-005` (IN_PROGRESS)

**Not reached:**
- the September SDR analyses
- `ranking.json`
- the live dashboard
- DREAM folders
- the `--mechanism` output itself

## 10 · Freshness and exposure

- **Snapshot:** b88a2c251, with no uncommitted paths. The radar file is from 05:21Z, and I treated it as a lead, not evidence.
- **Exposure:** I saw the presidio's 08:41Z "no further assignment" decision in the follow-through log, and I disagree with it because of PLAN's later correction.
- **Host duty still open:** the roadmap asks the host to reconcile the existing recall with the canonical `strategic_advisor.py recall` text. I can't inspect it.

## Assignments

### ASSIGNMENT 1
key: rp004-mechanism-lens-generative-case
recipient: Orchestrator
question: From `unread_gold.py --mechanism` on current main, with no tier, relevance or existing-INV filter, which one mechanism item, once already-read or declared-read items are removed (including the discovery-ledger and September analysis readings, e.g. P290 / PMID 25703206) and lawful free full text is confirmed, gives the best chance of a new conditional pharmacological contrast or discriminating experiment for WWOX loss of function? Launch one focused Scientist batch on it. One seed option, not an instruction: the unadjudicated WWOX SDR substrate conflict, 2011 measured steroid oxidation (PMID 21476439, read) against the 2015 proposal of reversible all-trans-retinal activity (PMID 25662954, census P376, unreceipted), which no repurposing investigation or open question represents.
why_now: RP-008 parked the clinical-tier pool; PLAN recorded that an INV-citation/tier filter had become an unintended eligibility gate and made RP-004 actionable; the operator's 2026-11-15 roadmap line asks for exactly a mechanism-lens case; IT/HE idle; the 08:41Z wait predates the correction.
roadmap_link: Portfolio RP-004 (feeds RP-001, RP-005, RP-003; RP-008 revival trigger); operator integration 2026-11-15; directions A, B, C, E.
related_work: ORCH-RP008-UNREAD-20261115 (consumed, do not redo the census); PRESIDIO-005 (Science, IN_PROGRESS, keeps priority); September SDR analyses (analysis/q230p_*_20260922.md, function_per_molecule_assay_design_20260922.md, wwox_sdr_function_per_molecule_census_20260921.md) must be checked before choosing the seed. The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: framework/scripts/unread_gold.py (lines 91–136); research_portfolio.tsv RP-004/RP-008; rp008_unread_census_it55_20261115/README.md and census.tsv; PLAN-ADV-CONTINUOUS-RESEARCH-20261115.json LIVE_OBSERVATION; discovery_ledger_current.md ~line 1206; wwox_function_reference_it6_20261029.md; framework/master/gold_is_in_the_details.md; framework/protocols/fulltext_read_receipt.md.
decision_changed_by_result: Whether a new investigation or open-question row and a conditional pharmacological contrast, with transfer limits, rivals and a rejecting experiment, enter the repurposing loop, or the lens case is closed with a supported abstention; whether RP-005 gets a prospective case (prediction frozen before reading); whether declared-without-receipt readings like P290 need recording (RP-006).
perimeter_and_budget: Lawful free full text only, zero spend, no contact parameter; an abstract is census, not a reading; one case, one Scientist batch, no compound quota; no ranking, need, candidate or frozen package is edited; do not touch PRESIDIO-005's worktree or battery; no treatment, dose or route content.
method_autonomy: The Orchestrator chooses the case (the seed is optional), the tools and the Scientist method; it may correct the 74/60 premise, choose an oncology or structural item instead, or decline with a reason.
deliver_to: ADV presidio (rows RP-004, RP-005, RP-008, RP-006); repurposing consumers via the existing open-question map and consumer links if a question results.
duplicate_check: No ledger task contains RP-004 or --mechanism (grep, this tick); drafted keys ADV-001 to ADV-010: ADV-010 was the clinical-tier census (consumed), none was mechanism-first; PRESIDIO-005 concerns X1, no overlap. Not checked: chat-only messages after 08:41Z.

## Portfolio updates

```json
[
  {"id": "RP-004", "status": "assigned", "next_action": "Drafted at P13 to the Orchestrator: select one mechanism-lens case (no tier or INV-citation filter) after removing already- or declared-read items and confirming lawful full text; freeze a prediction before reading; one Scientist batch queued behind PRESIDIO-005. Optional seed: the SDR substrate conflict (steroid PMID 21476439, read, versus retinal PMID 25662954, unreceipted); check the September SDR analyses first", "updated_utc": "2026-11-15"},
  {"id": "RP-006", "outcome": "P13 observation, to be verified: census P290 (PMID 25703206) is listed without a receipt while discovery_ledger_current.md (~line 1206) declares a complete reading from the 2026-07-12 mechanism audit; it is a declared-without-receipt reading outside drug_repurposing/, the scope IT left unscanned", "updated_utc": "2026-11-15"}
]
```

## Outcome

outcome: assign
excluded: RP-002 (wet-lab-dependent units, weighed and turned down at 08:41Z); RP-001 replay (held until after the report); RP-016 remainder (operator: already-used retrieval is not reassigned); RP-017/RP-018 (waiting on measurements; PRESIDIO-005 in progress); RP-021 (disposed); RP-020 and the radar (no scientific obstacle waits on them); a whole-portfolio wait (IT/HE idle, a roadmap-named case is executable)
reason: PLAN's correction and the operator's 2026-11-15 line make the mechanism-first case (RP-004) the one P1 opportunity that is executable now, unassigned and not duplicated. It is queued behind Science's current work, and either a new question or a supported abstention changes the portfolio.
resume_when: event