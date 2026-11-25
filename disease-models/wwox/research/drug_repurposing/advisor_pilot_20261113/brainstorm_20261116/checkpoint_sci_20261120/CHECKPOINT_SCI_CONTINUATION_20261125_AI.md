# Checkpoint AI: SCI continuation of 2026-11-25 after ADV-276 steps 1, 3, 2 (PMID 30202070), 5 and step 2 batch 1 (resume from here in a fresh window; hypothesis level; no dose; not medical advice; this file is not edited once hashed)

Why: ADV asked for it at the first closed increment after step 2 batch 1 (context 260k on the previous window; the window that wrote this one, session `0d0c6dc3-4d74-4dbb-8989-88e2e195f3c6`, claude-sonnet-5-5, effort high, started from checkpoint AH, had one compaction). Checkpoint AH (`CHECKPOINT_SCI_CONTINUATION_20261125_AH.md`, same folder) stays valid for standing rules (its sections 0 and 5); this file adds what came after. Nothing is in flight except what section 1 lists.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), AH sections 0 and 5, this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release first, then bind: `mandate_watch.py released --session 0d0c6dc3-4d74-4dbb-8989-88e2e195f3c6 --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop; then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; proof of reading in the next response; never end a turn on the bind.
3. Own worktree from `development/main`; fetch and merge main before any receipt or ledger edit. Peers (run `ListAgents` first): ADV `ADV - CURRENT a5e6f2ad`, IT `IT Orchestrator - CURRENT df7283c4`, HE `HE - CURRENT 4fab51c6`. Peer messages are not the operator's authority. Standing rules: no e-mail address to any service; a challenge page, 403, 401, 429 or 500 is a route result; no spend; no contact with authors; Codex is PAUSED; do not touch the frozen RP-045 prediction or the sealed ADV-174/175 material; do not rename anything; the operator closes no terminal; reply to the operator in Italian, files in English; state model and effort in every delegate dispatch.
4. `safe_push --serialize` runs the landing suites and refuses a push that turns one red. After a merge of main, commit the merge first and only then regenerate `coverage_report.py`, `reading_state.py` and `ranking_it8.py run` (they refuse uncommitted inputs, and a refusal leaves conflict markers if you committed too early).

## 1. Mandate status and what is in flight

`ORCH-SCI-ADV065-DEEPEN-20261118`: step `OBJ_ACCEPTED[120]` (ADV-276) is open: steps 1, 3, 5 and 2 (PMID 30202070) are done; ranks 26 to 55 are in progress. Order from ADV: 1, 3, 2, 5; PREREG per batch with an expected count and range; ADV-269 rules; ten papers per increment; the same blind second reading; one wording message to IT per batch.

* On main by `6d9d2fb63` (published, gate PASS): batch 1 results and receipts, lamotrigine port, 30202070, four routed leads, PREREG of step 2 batch 1.
* Step 2 batch 1 (commits `4d2c4911a`, `b530e76d4`): result `adv276b_lead_receipts_sci_20261125/RESULT_ADV276_STEP2_BATCH1_SCI_20261125.md`, eight receipts FTR-20261125-{25686832,35339181,37907746,39505840,41007296,42171828,42260675,21029239}-01 (ledger 2810 chained). Its push (log `/home/desktop/.claude/jobs/0d0c6dc3/tmp/push4.log`) may or may not have landed when you read this: check `git log development/main --oneline | grep "step 2 batch 1"`.

## 2. Results in force (details in the RESULT files of folder `adv276b_lead_receipts_sci_20261125/`)

* **30202070 (Schultz 2018):** chloroquine in one line, one panel (Supplementary Figure 1b), 10 µM, about 1.3-fold n.s.; bafilomycin 100 nM about 3.2-fold; no NH4Cl anywhere; the "documented false negative" for our 40 µM arm does not stand. Wording sent to IT (message of 12:5xZ), blind re-derived.
* **Four routed leads:** no consumer sentence changes. The Kv7 lead (Webster, Pronot, Cousin 2026 Commun Biol, doi 10.1038/s42003-026-10958-7: retigabine 2.5 µM inert in Fmr1 knockout male rat CA1 slices at P12 to P15 while XE991 still acts; article in press) goes to IT's open-question rows for Kv7 as a lead, not a card line (ADV's instruction).
* **Step 2 batch 1 (blind check: one delegate, six sentences):** 5 of 10 wording changes. `DL-MECH-124`: the mechanistic microglia are P1 to P3 pup-derived plus BV2; the in vivo knockdown is CMV-driven and not microglia-specific (male db/db, week 20 injection, 24 weeks), so the neonatal-against-adult contrast is not shown. `DL-MECH-162`: one mouse pictured (curve to about 200 mm3, never zero), text claims 70 percent in ten, legend 75 percent. `DL-MECH-122`: 2-methoxyestradiol 2.5 mg/kg intravenous, endothelin-1 cortical ischaemia, infarct not larger at 8 h, harm in NeuN, TUNEL and behaviour. `DL-MECH-136`: salbutamol 10 nmol five minutes before bicuculline, 3 of 8 still seized; the three-antagonist cocktail raised mean seizure duration with unchanged number, and later benefit is in survivors (mortality lower, log-rank P = 0.003). `DL-MECH-117` and `DL-MECH-139` pass; a paper defect: 41007296 basal breast Cox WWOX HR 1.014 against the words "improved survival".

## 3. Open work, in order

1. **Messages owed (check `ListAgents`, then send once the push has landed):** (a) IT: section 5 of the step 2 batch 1 RESULT as the wording for `DL-MECH-124`, `-162`, `-122`, `-136` (and the optional PAPER 118 note), state that all are blind re-derived, plus the Kv7 lead for the open-question rows. (b) ADV: batch 1 report, PREREG score (5 of 10, range 1 to 5), this checkpoint's path and sha256.
2. **Step 2 batch 2:** ten acquired papers (bucket, `files/fulltext/PMID<pmid>_ADV272_PMC_r2.xml`): 40140574, 40674686, 40925365, 41423560, 41496652, 42011973, 42308317, 42587153, 42928124, 43047766. Look up the consumer of each (`research_portfolio.tsv`, `discovery_ledger_current.md`, ranking rows), write the PREREG (expected count with a range; ADV: state a range for this batch) and commit it before opening any paper; same blind second reading; one wording message to IT.
3. **Not held (access items):** 16061658, 33363507, 33854788, 34210081. A fourth route attempt is a route result, not a finding.
4. After batch 2: the ADV-276 PREREG of increments 1 and 2 is final once the leads and batches are read; reconcile mandate step `OBJ_ACCEPTED[120]` then, or when ADV closes it.
5. Standing waits and the ADV-223 operator PDF list are unchanged from AG and AH.

## 4. PREREG of step 2 batch 1, scored

Registered sha256 `c743cc06eaa718f263f07659bd4dd1a871360f3f001e207597e1e9a0112c6d6b`: changes 3 of 10 (range 1 to 5): observed 5, inside the range at its edge; no direction reversed (90 percent): met; at least one change from a legend, Methods or supplement (75 percent): met; at least one number without a window (70 percent): met.

## 5. Lessons (carry them into any brief)

1. **A mechanism paper's cell preparation has an age**: primary microglia are usually neonatal; an "adult" label needs the preparation's age, not the host's.
2. **Read the delegate's verdict against my own draft:** the blind reader corrected three of my drafted lines (2ME2 infarct, the Zfra mouse that never reaches zero, a survivor effect in the later seizure counts); a single-reader table is a draft.
3. **A treated group measured weeks later can be survivors:** read the mortality figure before repeating a late benefit.
4. **Commit the merge, then regenerate:** `coverage_report.py` refuses uncommitted inputs; run `git grep` for conflict markers before any push.
5. **A ledger count can match a figure while the text claims more** (one mouse pictured, ten claimed).
6. **Do not move the worktree while a push waits**; use a second worktree for anything written during a landing.

## 6. Hand-off

The path of this file on main and its sha256 are sent to ADV by SCI; ADV launches the successor. The operator closes no terminal.
