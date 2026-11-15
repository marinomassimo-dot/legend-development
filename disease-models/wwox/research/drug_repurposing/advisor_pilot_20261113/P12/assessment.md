## 1 · Principal decision

What should the idle part of the lab work on next? Three operator steps have moved since my last complete assessment (P10):
- **PRESIDIO-004 (the gene-symbol lookup trial) is closed.** Science's independent reference agreed on 15 of 15 rows. IT kept all 15 conversions, discarded none and left the benefit inconclusive, with no regeneration.
- **ADV-009 has been used.** IT applied the INV-03 and WO-25 wording at commit bee8e7bed.
- **PRESIDIO-005 has been delivered to Science and is landing with its test battery** (`ORCH-ADV-FOLLOWTHROUGH-20261114.json`, entries for 07:3x–08:0x Z).

IT and HE are idle. P11's wait is no longer in force (`PLAN-ADV-CONTINUOUS-RESEARCH-20261115.json`, live_repair at 08:13:34Z).

## 2 · Leading recommendation

**Assign RP-008 to the Orchestrator: sort the unread placeholders, then pick one question.** The task is to sort the older WWOX placeholders that have no reading receipt and, only if some can be read for free and bear on a decision, choose a small full-text batch with its decision stated in advance.

**Facts**
- `advisor_continuity_20261115/README.md` §"Reachable research…": on baseline `39e887fa2`, `unread_gold.py --all` found 149 eligible placeholders. 27 have a partial or complete reading receipt; 122 have neither. The default high-priority filter returned nothing, and that filter does not cover the whole corpus.
- `INTAKE-OVERNIGHT-20261002.json` lines 134–135 and 158 call the neuro-WWOX pool "exhausted": 356 declared artefacts are absent and the key targets have no lawful free route.

**Interpretation.** These two records cannot both be fully true as written. Either most of the 122 are the same paywalled or absent items, or the "exhausted" claim was based on a narrower selector. Three rival explanations fit the gap (the README names the last two):
- the relevant evidence really is exhausted;
- the query or filter was too narrow;
- reading state was never propagated. Memory `declaration-is-not-attestation.md`: a registry's "full text reviewed" note is counted as a reading even without a receipt.

Comparing whole records against receipts, against the INTAKE absent list and against `evidence_presence.py --search` separates these explanations cheaply.

**Strategic judgement.** This is the only P1 row that is ready, not waiting on an event, and specifically requested in the operator's integration of 2026-11-15 ("Assess the coverage of older unread WWOX literature…"). A negative result is useful too: if nothing is lawfully readable and relevant, RP-008 can be parked with evidence instead of staying "ready".

It does not repeat ADV-008. That draft was declined because it claimed a new WWOX-model paper, which was false (OBJ_12_ADV008). This draft rests on a count recorded by a tool, and I say plainly that I have not re-run it.

## 3 · Relevant alternatives

- **RP-002 (first five units of the selection table).** Ready, but it is a large read with no decision named yet (presidio log, 03:3x Z). It is the next choice if RP-008 comes back empty.
- **RP-001 / Contrastive replay.** The presidio kept this as an option to revive after the trial report (RP-001 outcome, HE audit). Not overridden.
- **RP-016 remainder (the Cav3 pair).** The operator said not to reassign retrieval that has already been used. IT has narrowed WO-25. The remaining values (two isoforms for one agent, a same-condition comparison, hERG) have no new access route on record.
- **RP-021.** Disposed. It revives only if a decision comes to rest on the two live LINCS queries (S8/S9), or the operator authorises them.
- **RP-017 / RP-018.** Waiting on new measured evidence. PRESIDIO-005 already covers the first question for X1.
- **RP-020 / harness radar (ToolUniverse delta).** No scientific obstacle is waiting on either. The feed dates from 05:21Z and is a lead, not evidence.
- **Wait until the trial report.** Not supported: IT and HE are idle and the report is the presidio's own work (continuity README, "Observed failure").

## 4 · Why now

The executable queue holds only the PLAN mandate. Both blocked literature mandates point to a pool this coverage count partly contradicts. The roadmap names this exact gap, and its last open step ("observe a useful autonomous next handoff", PLAN record OBJ_REPAIR step 4) needs a real handoff.

## 5 · Evidence and uncertainty

- I have not run the 149/122 figures myself.
- How much the 122 overlap with the 356 absent artefacts is unknown. A large overlap is the most likely single outcome.
- The value depends on reaching a sorted subset tied to an INV or open question. I don't expect a large batch.

## 6 · Next bounded action

The Orchestrator re-runs the census on current main and sorts each item into one of four buckets:
- read, but the receipt was never propagated (a representation loss);
- lawfully accessible and unread;
- access-limited;
- not relevant.

If the accessible-and-unread bucket holds items that bear on a named investigation or open question, it selects a small full-text batch for Science and states the decision each item could change. Optionally, it records beforehand what the current outputs predict, so the reading also gives RP-005 a prospective case.

**Decision changed.** Either RP-008 gets a real batch, or it is parked with a revival trigger and the INTAKE "exhausted" claim is confirmed or corrected.

## 7 · What would change my view

- The census shows the 122 lie almost entirely inside the absent list. RP-002 then comes next.
- An operator PAUSE line.
- PRESIDIO-005 returns a result that reopens X1.
- A record showing RP-008 was already taken after 07:59Z. I grepped ledger/tasks and found none.

## 8 · Resource implications

- One Orchestrator pass with tools the repository already has, plus at most one Science batch if one is justified.
- Zero spend. No contact address goes to any service (memory `never-send-operator-email-to-services.md`).
- Nothing frozen is touched. PRESIDIO-005's landing has priority.

## 9 · Inspected

**Read in full:**
- `advisor_pilot_20261113/P10/assessment.md`
- `PLAN-ADV-CONTINUOUS-RESEARCH-20261115.json`
- `PLAN-HE-IT23-SYMBOL-TRIAL-20261115.json`
- `ORCH-ADV009-20261115.json`
- `assignments/PRESIDIO-005.md`
- `advisor_continuity_20261115/README.md`
- portfolio rows RP-001 to RP-008

**Read in part:**
- `ORCH-ADV-FOLLOWTHROUGH-20261114.json`: lines 196–215, 250–261 and 443–481
- `INTAKE-OVERNIGHT-20261002.json`: lines matched by grep

**Grep only:** ledger/tasks (for RP-008, for IT23/PRESIDIO, for unread_gold) and `framework/scripts/README.md`.

**Not reached:** the dashboard page, `ranking.json`, the open-question map, DREAM folders, `unread_gold` output, the PRESIDIO-004 and ADV-009 assignment files.

## 10 · Freshness and exposure

- Snapshot 5191106, with no uncommitted paths.
- The radar file is from 05:21Z on main 9aa28b3, and I did not use it as evidence.
- **Exposure:** I saw the presidio's own decisions in the follow-through log, including its choice not to assign the RP-001 replay now. I did not see a preferred next action for this tick.
- **Host action required by the roadmap:** at the next active boundary, reconcile the recall text with the canonical `strategic_advisor.py recall` text. I cannot inspect the recall job.

## Assignments

### ASSIGNMENT 1
key: rp008-unread-placeholder-reconciliation
recipient: Orchestrator
question: Of the WWOX corpus placeholders that `unread_gold.py --all` reports without a matched partial/complete reading receipt (122 of 149 on baseline 39e887fa2, per advisor_continuity_20261115/README.md), how many fall into each bucket on current main: (a) read, but the reading is declared without a receipt, (b) lawfully accessible free and unread, (c) access-limited or absent (cross-check the INTAKE-OVERNIGHT-20261002 absent list and evidence_presence.py --search), (d) not relevant to any investigation or open question? If bucket (b) is non-empty, select a small full-text batch for Science, naming for each item the INV or open-question row and the comparison, hypothesis or experiment it could change; if it is empty, state that and the revival trigger.
why_now: RP-008 is ready and P1, and the operator integration of 2026-11-15 asks for exactly this coverage assessment. IT and HE are idle, PRESIDIO-004 and ADV-009 have been used, and PRESIDIO-005 is landing. The two blocked literature mandates declare the pool exhausted, a claim the 122 count partly contradicts; one of the two records needs correcting.
roadmap_link: Portfolio RP-008 (also feeds RP-003, RP-004 and optionally RP-005); operator integration 2026-11-15 "continuous useful research"; strategic directions B, C, D and G.
related_work: INTAKE-OVERNIGHT-20261002 and ORCH-METABOLIC-BATCH-20261019 (blocked, exhausted-pool claims: reconcile, do not duplicate); ADV-008 (declined on a false premise; this draft does not revive that premise); PRESIDIO-005 (SCI landing, no file overlap). The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: disease-models/wwox/research/drug_repurposing/advisor_continuity_20261115/README.md; ledger/tasks/orchestrator/INTAKE-OVERNIGHT-20261002.json (blocker and unblock lines); research_portfolio.tsv row RP-008; framework/scripts/README.md (unread_gold, reading_state, coverage_report, evidence_presence); framework/master/gold_is_in_the_details.md; framework/protocols/fulltext_read_receipt.md.
decision_changed_by_result: Whether RP-008 gets a sourced full-text batch tied to named decisions or is parked with evidence and a revival trigger; whether the INTAKE "pool exhausted" blocker is confirmed or corrected; whether declared-but-unreceipted readings need propagating (an RP-006 representation loss).
perimeter_and_budget: Lawful free routes only; zero spend; no contact address or e-mail parameter to any service; abstracts are census, not reading; no ranking, need, candidate or frozen package is edited. Size the batch to the decisions found; no quota. Do not touch PRESIDIO-005's worktree or battery.
method_autonomy: The Orchestrator chooses tools, buckets, the case and the Scientist method. It may correct the 149/122 premise, merge buckets, decline with a reason, or attach a prediction frozen before reading so the item serves RP-005.
deliver_to: ADV presidio (rows RP-008, RP-003, RP-005); the owner of INTAKE-OVERNIGHT-20261002 for its blocker text; Science if a batch is selected.
duplicate_check: Grepped ledger/tasks for RP-008, "unread_gold --all" and "122": the only matches are planning or follow-through records, with no mandate executing it. Checked drafted keys ADV-001 to ADV-009 and PRESIDIO-001 to 005: only ADV-008 touched RP-008, and it was declined on a different, false premise. Not checked: chat-only messages after 08:17Z.

## Portfolio updates

```json
[
  {"id": "RP-008", "next_action": "Drafted P12 to the Orchestrator: sort the 122 receipt-less placeholders into read-without-receipt / free-unread / access-limited / not relevant, cross-checked with the INTAKE-OVERNIGHT absent list; select a decision-tied full-text batch only if the free-unread bucket is non-empty, else park with a trigger", "updated_utc": "2026-11-15"},
  {"id": "RP-021", "outcome": "PRESIDIO-004 disposed by IT (b2eb309fb): KEEP the 15 conversions, DISCARD none, INCONCLUSIVE on benefit; one query's membership changed (QF_minus_broad_maturation 365/260 to 363/257); class unchanged; no regeneration; SCI reference 15/15 agree (same HGNC release, so the independence is limited)", "resume_when": "a decision rests on LINCS queries S8/S9, or the operator authorises the two live queries", "updated_utc": "2026-11-15"}
]
```

## Outcome

outcome: assign
excluded: RP-002 (large read with no named decision; next if RP-008 comes back empty); RP-001 replay (the presidio holds it until after the report); RP-016 remainder (operator: retrieval that was already used is not reassigned; WO-25 has already been narrowed); RP-017/RP-018 (waiting on new measured evidence); RP-021 (disposed, revival conditions recorded); RP-020 and the radar (no scientific obstacle waits on them); a whole-portfolio wait (IT and HE idle, the report is the presidio's own work)
reason: The open P1 coverage question named by the operator can be run now. It reconciles a 122-item receipt gap with a declared-exhausted pool, and either outcome changes RP-008 and the blocker records.
resume_when: event