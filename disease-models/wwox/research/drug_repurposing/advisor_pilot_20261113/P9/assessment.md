I've finished reading. Recommendation: send the Orchestrator one small assignment, a dated scan for new WWOX literature, because no scan has been found since the pool was declared exhausted on 2026-10-05.

## 1 · Principal decision

ADV-007 (the CTGF check) has been delivered and mostly consumed, and the lever thread is closed. The question is what the portfolio should fund next, or whether the presidio should wait for the 24-hour trial review (RP-014, due after 2026-11-15T15:29Z).

## 2 · Leading recommendation

**Assign one small Orchestrator item (RP-008).** It is a dated, scoped census of WWOX/WOREE/SCAR12/EIEE28 literature published since 2026-10-01, deduplicated against what the repository already holds. Each new item is triaged by the open question or need it could change.

**Facts**
- `INTAKE-OVERNIGHT-20261002.json` OBJ_STANDING_NEXT_WAVES (line 132–135) is BLOCKED, and its declared unblock is "a new WWOX/WOREE/SCAR12/EIEE28 paper appears". Item (6) of the same rule is a "periodic fresh-literature scan … by date".
- The pause that declared the pool exhausted is dated 2026-10-05 (line 158–160). `ORCH-METABOLIC-BATCH-20261019` is blocked for the same reason.
- At least one WWOX paper appeared after that pause: PMID 42941930, first published 2026-10-15 (`radar_p4_it15_20261101/README.md` §2). It was reached only through a question-driven radar query, not through a scan by genotype name and date.

**Interpretation**
- I found no dated scan by genotype name since 2026-10-05. I searched two ways:
  - `ledger/tasks` for `pubmed_corpus_harvest` or a fresh-literature scan; only INTAKE and two harness self-test records matched.
  - `disease-models/wwox/research` for a dated harvest, census or scan; nothing matched.
- This absence is limited to those searches. It is not a proof.

**Strategic judgment**
- This is the shared upstream uncertainty behind both blocked mandates and behind RP-017/RP-018, whose revival conditions are "new measured premise or new discriminating evidence".
- It is cheap, free, touches nothing under verification, and an empty result is useful: it renews the date of the "pool exhausted" claim.

## 3 · Relevant alternatives

- **Keep waiting until the trial review.** This is valid only if nothing cheap is executable, and here something is. The waits in the brief block on lawful access, which this census could lift.
- **RP-005, a new prospective test of the generator.** This would be the strongest test of direction G. But IT52 closed its case under ADV's no-further-reader rule (`generation_it52_20261114/result_it52_rerun.md`, "Closing line"), and the one other lever package (SCI50) is suspended until gate 0 or the M1/EBP question moves. No second case is ready, so starting one now would mean inventing a case. I queue it as the conditional follow-up instead (§7).
- **RP-003, reconciling open questions.** This is high value but a large job (the open-questions map is 176 KB). It is better fed by the census, which may add or retire questions.
- **Regenerating `composition_class.tsv` for the 15 renamed symbols.** IT already wrote the caveat (`signature_it23_20261103/README.md` "Update 2026-11-14"). Regenerating moves at most 15 of 834 query genes, and it is the owner's decision. Revive it only if a candidate decision is shown to rest on QD/QF membership.
- **Optional ADV-007 delta row 1 (the INV-06 wording).** This belongs to the integrator. It is optional by the producer's own wording, and the verdict "neither supports nor reverses" means it changes no decision. Not drafted.
- **Radar NP3P3 / NP3A1.** Unchanged from P8, and the feed (05:21Z) is stale.

## 4 · Why now

- ADV-007 closed with verdict (b) (`ctgf_held_data_adv007_20261114/README.md` "Answer first"). Its rows 3 and 4 were consumed: IT's dated update in signature_it23, and the DREAM disposition in the SCI50 README.
- No delivery is pending that this item depends on. Every session but one is idle.
- The executable queue holds only the HE portfolio record, now at landing.
- Six weeks without a dated scan is long enough that the "exhausted" premise may be stale, as the 2026-10-15 paper shows.

## 5 · Evidence and uncertainty

- **Facts:** listed in §2. ADV-007's own record shows a blind check (32 claims: 26 confirmed, 3 narrowed, 0 contradicted) and a battery that passed with skips (`ORCH-ADV007-20261114.json`).
- **Uncertainty: odds of a hit.** Some of the new WWOX literature will be cancer biology. The yield of neuro or metabolic items that change a decision may be zero, and I treat that as an acceptable result.
- **Uncertainty: what counts as evidence.** A census is discovery, not evidence; an abstract is not a read (CLAUDE.md routing). Full text may be paywalled again.
- **Uncertainty: open state of the delivery.** `ORCH-ADV007` still reads MANDATE_STATE IN_PROGRESS with a RESUME list, although the package has landed. Closing it is SCI's bookkeeping, not this decision.

## 6 · Next bounded action

**Question:** since 2026-10-01, which new WWOX/WOREE/SCAR12/EIEE28 publications, corrections, supplements or public datasets exist? Which of them is lawfully readable, and which open question, need or blocked mandate could each one change?

**The result that counts:** a dated note giving:
- the query strings and date window;
- counts before and after deduplication;
- per item: label (new, already held, or correction), lawful route, and the question it could change, or "none";
- a verdict per blocked mandate: unblocked, or still exhausted as of the new date.

## 7 · What would change my view

- The census or an operator instruction showing that a dated scan already ran after 2026-10-05.
- An operator PAUSE line.
- A new lever or measurement package appearing. Then RP-005 becomes the better investment.
- **Conditional follow-up, queued and not drafted:** if the census finds a lawful neuro or metabolic item, the standing wave rule in INTAKE already dispatches it. If it finds nothing, the next Advisor evaluation should consider RP-003 or RP-005 rather than another census.

## 8 · Resource implications

- **This assignment:** one Orchestrator pass using existing tools (`pubmed_corpus_harvest.py`, dedup against the discovery ledger). It needs no blind verifier, because no claim is promoted. It spends nothing.
- **No e-mail to any service:** the e-mail or contact parameter must never be sent to PubMed, Europe PMC or Unpaywall (memory `never-send-operator-email-to-services.md`).
- **Counters:** this is the 9th Advisor invocation, and drafts would be 8 of the historical 9. These are flagged as history in continuous mode, not hidden.

## 9 · Inspected

**Read in full:**
- `research_portfolio.tsv`
- `advisor_pilot_20261113/P8/assessment.md`
- `ledger/tasks/plan/PLAN-LIVING-RESEARCH-PORTFOLIO-20261114.json`
- `ctgf_held_data_adv007_20261114/README.md` and its `consumer_delta.md`
- `ledger/tasks/orchestrator/ORCH-ADV007-20261114.json`
- `generation_it52_20261114/result_it52_rerun.md`

**Read in range:**
- `ORCH-ADV-FOLLOWTHROUGH-20261114.json`, lines 224–369
- `INTAKE-OVERNIGHT-20261002.json`, lines 120–166
- `signature_it23_20261103/README.md`, lines 87–90

**Grep or Glob only:**
- searches for ADV-007, CTGF folders and harvest/scan records
- radar READMEs, matched lines only, including `radar_p4_it15_20261101/README.md` §2 identity rows

**Not reached:**
- the dashboard page (not fetched)
- the open-questions map
- `investigations_it20.tsv`
- the ADV-007 verify files
- `discovery_ledger_current.md`
- DREAM folders
- the HE radar README (`radar_inputs_he52_20261114`)
- `budget.json` and `CONTINUOUS.json`

## 10 · Freshness and exposure

- **Freshness:**
  - No uncommitted paths.
  - The scout feed is stale (05:21Z, remote `1c8ed97f15fe`), and I used none of it as evidence.
  - The dashboard source revision (2a18966) predates ADV-007.
- **Exposure:** the presidio's trial log shows its own handling of ADV-007, including that the presidio corrected my P8 premises before sending (two of the three were mine and were wrong or incomplete). No preferred next plan was visible.

## Assignments

### ASSIGNMENT 1
key: wwox-literature-census-since-pause
recipient: Orchestrator
question: Since 2026-10-01, which new publications, corrections, retractions, supplements or public datasets on WWOX loss of function exist (WWOX, WOREE, SCAR12, EIEE28/DEE28, and the WWOX-direct metabolic themes of ORCH-METABOLIC-BATCH-20261019)? For each new item: is it already held, is there a lawful free full-text route, and which open question, need, investigation or blocked mandate could it change ("none" is a valid entry)? Conclude, for INTAKE-OVERNIGHT-20261002 and ORCH-METABOLIC-BATCH-20261019, whether their unblock condition is now met or the "pool exhausted" state is re-dated.
why_now: No dated scan by genotype name was found after the 2026-10-05 pause (INTAKE-OVERNIGHT OBJ_WAVE12_CONSOLIDATION). At least one WWOX paper (PMID 42941930, published 2026-10-15) appeared afterwards and was caught only by a question-driven radar query. Both blocked mandates name a new paper as their unblock condition. ADV-007 and the lever thread are closed, and the queue holds no other science item.
roadmap_link: Portfolio RP-008 (P1). Roadmap priorities 2–3: knowledge reaching the comparisons, and depth versus other questions. Strategic direction C (return questions to research).
related_work: INTAKE-OVERNIGHT-20261002 (standing wave rule; this census is its item 6 and may trigger it); ORCH-METABOLIC-BATCH-20261019; PLAN-LIVING-RESEARCH-PORTFOLIO-20261114 (HE, at landing; no file overlap); the daily harness scout's Europe PMC channel (question-driven, not a by-date scan; do not duplicate its dispositions). The current work keeps priority: queue this assignment, and anticipate its independent parts if resources and dependencies allow. Before starting, check that results that arrived since have not changed its usefulness.
sources: ledger/tasks/orchestrator/INTAKE-OVERNIGHT-20261002.json (OBJ_STANDING_NEXT_WAVES and OBJ_WAVE12_CONSOLIDATION, whole); ledger/tasks/orchestrator/ORCH-METABOLIC-BATCH-20261019.json (whole); disease-models/wwox/research/drug_repurposing/radar_p4_it15_20261101/README.md (whole, as the example of a post-pause paper); disease-models/wwox/research/discovery_ledger_current.md (Grep by identifier only, for dedup); framework/scripts/README.md (pubmed_corpus_harvest and dedup routing); framework/master/gold_is_in_the_details.md (a census is not evidence; an abstract is not a read).
decision_changed_by_result: Whether either blocked mandate resumes, through the standing wave rule. Whether any open question, investigation or need gets a new lawful source to read. If the result is empty, the "pool exhausted" premise is re-dated, and the next Advisor evaluation moves to RP-003 or RP-005 instead of another census.
perimeter_and_budget: Free public metadata endpoints only, with no e-mail or contact parameter sent to any service. No paid access, no download of paywalled text, and no full reading inside this item (a lawful item with a decision attached goes to the standing wave rule). No edit to any registry, ranking, need or candidate. Output is one dated note with the query strings, date window and counts. Run as a single pass, with no blind verifier needed because nothing is promoted. It leaves HE's landing and any battery their resources.
method_autonomy: The recipient chooses the query strings, the window boundaries, the dedup route and the endpoints. It may widen the scope to adjacent indications if it states why, may declare the census uninformative, and may decline the item if it shows that a dated scan already ran after 2026-10-05. An empty result is a full result.
deliver_to: The presidio (ADV session) for portfolio row RP-008 and the follow-through record; INTAKE-OVERNIGHT's standing rule, if an item qualifies; SCI, only if an item bears on a package it owns.
duplicate_check: Searched ledger/tasks for pubmed_corpus_harvest, "fresh-literature scan" and "new WWOX paper/studies" (only INTAKE-OVERNIGHT and two harness self-test records match). Globbed disease-models/wwox/research for November harvest files (none). Grepped research Markdown for dated harvest, census or scan lines (none). Grepped the radar READMEs (question-driven Europe PMC channels only). Checked drafted keys ADV-001 to ADV-007 (none is a literature census) and the portfolio (RP-008 unassigned). Not checked: chat-only reports, and whether the operator supplied PDFs outside the repository.

## Portfolio updates

```json
[
  {"id": "RP-008", "status": "assigned", "next_action": "Dated census since 2026-10-01 by genotype name; dedup; per-item question it could change; re-date or lift the INTAKE/METABOLIC unblock", "outcome": "P9: drafted to the Orchestrator (key wwox-literature-census-since-pause); not yet taken in charge", "updated_utc": "2026-11-14"},
  {"id": "RP-017", "outcome": "ADV-007 (2026-11-14) verdict (b): the held Wwox expression data do not support a Wwox-CTGF link independent of composition; OQ11 (null-neuron medium) stays the decisive measurement; the X1 arm gets no product from Wwox data", "sources": "disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations.tsv;disease-models/wwox/research/drug_repurposing/ctgf_held_data_adv007_20261114/README.md", "updated_utc": "2026-11-14"},
  {"id": "RP-005", "resume_when": "a new lever or measurement package exists to serve as a prospective case (IT52 case closed; SCI50 levers suspended until gate 0 or M1/EBP moves)", "updated_utc": "2026-11-14"}
]
```

## Outcome

outcome: assign
excluded: waiting until the trial review (a cheap independent item exists and it bears on both blocked mandates); RP-005 now (no ready prospective case; IT52 closed, SCI50 suspended); RP-003 now (large, and better fed by the census); composition_class regeneration (owner's call, IT already wrote the caveat, no decision shown to rest on it); ADV-007 row 1 (optional and the integrator's; changes no decision); radar NP3P3/NP3A1 (stale feed; already handled or too costly).
reason: the lever thread and ADV-007 are closed and their consumption is done or optional; both blocked mandates name a new paper as their unblock condition; no dated genotype scan was found since 2026-10-05, although a WWOX paper appeared on 2026-10-15; the census is cheap, free and independent, and an empty result usefully re-dates the "exhausted" premise.
resume_when: event