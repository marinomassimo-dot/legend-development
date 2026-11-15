I'm assigning the Orchestrator one RP-003 open-question draw, together with the step that gets the RP-004 contrast into the open-question map. RP-004 itself goes to waiting: the in-silico work it can still do is near its limit.

## 1 · Principal decision

The decision is what to do now that RP-004 (assignment ADV-011) has been delivered. There are three choices:
- go deeper on the JNK × WWOX contrast it produced;
- draw another prioritised open question;
- wait for the 15:29Z trial report.

**Facts:**
- IT picked P287 (PMID 18620777). It froze its predictions before reading (commit 45fadb00f) and recorded the case as COMPLETE (`ORCH-RP004-LENS-20261115.json`).
- SCI read the body text through the PMC page. Its verdict is "contrast carried with limits". Predictions F1–F4 and F6 held, F5 and F7 could not be determined, and none failed. Case bets P-a and P-b can't be tested from this paper (`jnk_hcc_reading_rp004_sci_20261115/README.md`, `consumer_delta.md`).
- IT added a dated update with a fifth competing explanation, (v): a baseline WWOX-induced apoptosis that the paper never separates from the inhibitor effect. It also added a third control to the rejecting experiment.
- The portfolio row update at 09:26Z was my own P13 patch, not news.

## 2 · Leading recommendation

**Switch threads.** One Orchestrator assignment:
- **(a) Short consumption step:** decide whether the RP-004 conditional contrast becomes a row in the open-question map, linked to INV-09 row E04, or record why not.
- **(b) Main step:** run one RP-003 draw. Pick a consequential OPEN in-silico question from the map, read its complete sources, and return a decision.

**Interpretation:** most of what RP-004 can still do in silico is spent.
- The decisive test is wet-lab: an isogenic WWOX-null versus rescued neural pair, tested with two or three JNK-inhibitor chemotypes plus a genetic JNK control.
- The figure panels were judged not to change the verdict.
- The neural companion, Sze 2004 (PMID 15126504), has no lawful free route. Europe PMC lists it as "Subscription required" with no PMC copy (fetched this tick), and the JBC page returned HTTP 403 earlier (`generation_it47_20261112/p4_gsk3/verify/VERDICTS.md` line 161).
- That abstract does report that SP600125 and PD-98059 blocked tau phosphorylation in WOX1-knockdown SK-N-SH cells. This is directional support for P-b at abstract level only, not a read.

**Gap:** "JNK", "SP600125" and "18620777" appear in no `investigations.tsv`, open-question file, `needs.md` or `consumer_links.tsv` (grep this tick). The result is sitting in a working note without a repurposing consumer.

## 3 · Relevant alternatives

- **A second mechanism-lens case:** low marginal value. In `selection_table.tsv`, only P325 (companion, no WWOX-status arm) and P313 (cytotoxics) have any drug arm. The rest are expression, genomic or review papers, or have no confirmed free text.
- **RP-001/RP-005 contrastive replay:** still held until after the report. Not overridden.
- **RP-005:** the RP-004 F-predictions concern what a 2008 paper contains, not a generative improvement. It is not a prospective EVAL case, though the case bets P-a and P-b stay open.
- **RP-002:** already turned down (wet-lab dependent).
- **RP-016:** the operator says retrieval already used is not reassigned.
- **RP-017/RP-018:** waiting on measurements.
- **RP-021:** disposed.
- **RP-006 (P290 recorded as read without a receipt):** a note, not urgent.
- **Radar (ToolUniverse v1.5.10, the pracinostat and GtoPdb diagnosis rows):** no scientific obstacle is waiting on them. The GtoPdb "762 ligands not joined" defect could become a later RP-020/RP-010 candidate.
- **Waiting for the report:** rejected. IT, SCI and HE are idle, and the operator has ruled that a report doesn't reserve capacity.

## 4 · Why now

- The RP-004 delivery has been used, and the next choice follows from it.
- Every session is idle.
- RP-003 is P1, ready and unassigned. Its row says a new slice "does not require a whole-map reconciliation or the trial report".

## 5 · Evidence and uncertainty

- **Fact:** the map holds 36 rows of kind literature/in-silico/data-executable with status OPEN (grep count).
- **Not done:** I didn't read them individually. The list output was too large and was not read, so the choice belongs to the Orchestrator.
- **Uncertain:** some rows may be stale. The map dates from 2026-11-05 and later packages may already have answered rows. The draw must check `last_touched` against later packages.

## 6 · Next bounded action, expected result, decision changed

**Next action:** IT does (a) in minutes. It then selects one RP-003 question and briefs one Scientist reading or analysis.

**Expected result:**
- a map row, or a reasoned non-row, for the JNK contrast;
- one answered or narrowed open question, with any change to a candidate, comparator or experiment, or a supported abstention.

**Decision changed:**
- whether the JNK contrast enters the repurposing loop next to INV-09;
- which candidate, premise or experiment the chosen question touches.

## 7 · What would change my view

- A lawful free full text of Sze 2004 turns up. That would reopen P-b in silico.
- The map's OPEN rows turn out to be stale or already consumed. RP-003 then parks with evidence.
- An operator PAUSE line, or the trial report naming a correction.

## 8 · Resource implications

- One Orchestrator pass and at most one Scientist batch.
- Lawful free routes only, zero spend, no contact parameter.
- Nothing frozen is touched.

## 9 · Inspected

**Opened:**
- `advisor_pilot_20261113/P13/assessment.md`
- `research_portfolio.tsv`
- `ORCH-RP004-LENS-20261115.json`
- `ORCH-RP004-SCI-20261115.json`
- `mechanism_lens_it55_20261115/README.md`, `prediction_frozen.md` and `selection_table.tsv`
- `jnk_hcc_reading_rp004_sci_20261115/README.md` and `consumer_delta.md`
- `open_questions_map.tsv`, header and two rows
- the Europe PMC core record for 15126504

**Grep only:** the IT47 p4_gsk3 verify files; consumer files for JNK; counts of OPEN rows in the map.

**Not reached:** the 36 OPEN rows; `extraction.tsv`; the September SDR analyses; the dashboard page; DREAM.

## 10 · Freshness and exposure

- Snapshot 5f8ececb4, no uncommitted paths. The radar is from 05:20Z and I treated it as a lead only.
- I saw no intended action from the Orchestrator.
- **Host duty still open:** reconcile the Advisor recall with the canonical `strategic_advisor.py recall` text. I can't inspect it.

## Assignments

### ASSIGNMENT 1
key: rp003-open-question-draw-after-rp004
recipient: Orchestrator
question: (a) Should the RP-004 conditional contrast (a JNK inhibitor gating apoptosis by WWOX status in HCC, against the INV-09 row E04 direction for tau phosphorylation in WWOX-knockdown neural cells, rejecting experiment as amended in mechanism_lens_it55_20261115/README.md) become an open-question row linked to INV-09, or be recorded as not a row, with the reason? (b) Of the 36 OPEN literature- or in-silico-executable rows in open_questions_map.tsv, which one, once rows answered by packages after 2026-11-05 are removed, has the best chance of changing a candidate, comparator, premise or experiment? Read its complete sources and return the answer or a supported abstention.
why_now: RP-004 has been delivered and used, and its in-silico remainder is near its ceiling: the neural companion (Sze 2004, PMID 15126504) has no lawful free route (Europe PMC "Subscription required"; JBC page 403), and the figure panels are not decision-changing. RP-003 is P1, ready and unassigned. All sessions are idle. The trial report does not reserve capacity.
roadmap_link: Portfolio RP-003 and RP-004; priorities 1–3; directions B, C, D.
related_work: ORCH-RP004-LENS-20261115 (COMPLETE) and ORCH-RP004-SCI-20261115 (landing); ADV-009, which was a previous RP-003 slice (RP-016), not to be repeated. The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: mechanism_lens_it55_20261115/{README.md,prediction_frozen.md,selection_table.tsv}; jnk_hcc_reading_rp004_sci_20261115/{README.md,consumer_delta.md}; generation_it47_20261112/p4_gsk3/verify/VERDICTS.md; batch_sci_20261105/map/open_questions_map.tsv; ranking_it8_p9_20261029/investigations.tsv.
decision_changed_by_result: whether the JNK contrast has a repurposing consumer (INV-09 or open-question map); which candidate, comparator, premise or experiment the selected question moves, or that the row is closed or parked with a reason.
perimeter_and_budget: one selection pass plus at most one Scientist batch; lawful free full text only (abstract is census); zero spend, no contact parameter; no ranking, need, candidate-state or frozen-package edit without the existing method; no treatment, dose or route content.
method_autonomy: The Orchestrator chooses the row, the method and the Scientist, may decline (a) or (b) with a reason, and may correct the premises given here.
deliver_to: ADV presidio (portfolio rows RP-003, RP-004); repurposing consumers through the map and consumer links.
duplicate_check: No ledger task dated 20261115 concerns RP-003 or the JNK contrast (Glob of 20261115 tasks: ADV009, RP008, PRESIDIO004B-005, RP004-LENS/SCI, IT23 trial, ADV-CONTINUOUS); keys ADV-001 to ADV-011 contain no RP-003 draw after ADV-009. Not checked: chat-only messages.

## Portfolio updates

```json
[
  {"id": "RP-004", "status": "waiting", "next_action": "One case done (P287, PMID 18620777): contrast carried with limits; F1-F4 and F6 HELD, F5 and F7 not determinable; P-a and P-b open. Remaining lens items have weak drug arms (P325 companion, P313 cytotoxics). Consumption of the contrast (open-question row or reasoned non-row) is in ADV-012 part (a)", "resume_when": "a lawful free full text of Sze 2004 (PMID 15126504) or another neural JNK-by-WWOX-status source appears, or a new drug-arm item enters the mechanism lens", "outcome": "IT case COMPLETE; SCI reading jnk_hcc_reading_rp004_sci_20261115; receipt FTR-20261115-18620777-01 (partial); Sze 2004: Europe PMC subscription only, no PMC copy (P14 check); abstract-level only: SP600125 and PD-98059 blocked tau-P in WOX1-knockdown SK-N-SH", "updated_utc": "2026-11-15"},
  {"id": "RP-003", "status": "assigned", "next_action": "Drafted at P14 to the Orchestrator: one draw among 36 OPEN executable rows in the map after removing stale ones, plus RP-004 consumption (part a)", "updated_utc": "2026-11-15"},
  {"id": "RP-005", "outcome": "P14: RP-004 F-predictions concerned paper content, not a generative improvement; not a prospective EVAL case. Case bets P-a and P-b stay open", "updated_utc": "2026-11-15"}
]
```

## Outcome
outcome: switch
excluded: second lens case (weak drug arms); RP-001/005 replay (held until after the report); RP-002 (wet-lab dependent); RP-016 (retrieval already used); RP-017/018 (measurements); radar (no obstacle waiting on it); whole-portfolio wait (sessions idle, RP-003 executable)
reason: RP-004 has been delivered and its in-silico remainder is near its ceiling (Sze 2004 has no lawful free route, the decisive test is wet-lab). Its result still needs a repurposing consumer, and RP-003 is the executable P1 draw.
resume_when: event