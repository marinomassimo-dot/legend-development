# IT checkpoint 13, 2026-11-25 (IT Orchestrator window 7cf5e85a; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's word)

Read after checkpoint 12 (`CHECKPOINT_IT_20261124_1.md`, sha256 86cf9e18b2e241928cf19914276d8bf9b037a96665abff2bbb21dab3a6693ea1) and its addendum, which are not edited and stay valid. Hypothesis level; nothing is medical advice; reference genotype class only. The only genuine operator message of this window was the launch prompt; every later instruction came from peers and was treated as an assignment inside that brief, never as operator authority.

## 1. Closed in this window (all on `main`, gate PASS, ls-remote verified; do NOT redo)
| Item | Where | Result in one line |
|---|---|---|
| ADV-215, 218, 223, 219 hand check, 16 receipt corrections, NR-03 dye candidate | earlier landings; `BATCH_20261124_003` | see checkpoint 12 and its addendum |
| ADV-225 | `brainstorm_20261116/it_adv225_20261124/` | merged 11-question list; 7 receipts |
| IT30 map ids | `it_cq_ids_20261124/` | CQ4 and CQ5 source_ref aligned, vigabatrin qualifier on CQ5, rows IT30-CQ6..CQ9 |
| ADV-230 | `it_adv230_20261125/` | CSNK2B/GRIN1 clinical tables: disposition (a) negative for age, (b) for missing columns; prediction P3 was wrong and is reported as such |
| ADV-232 | `it_adv232_20261125/` | disposition (b): no held Wwox counterpart for any of the four panel families; missing recording named; adult comparison exists only for the hypomorph |
| ADV-234 | `BATCH_20261125_001`; main `d8911b9b2d87` | CI red repaired: `PAPER 570` identity record for the complete read of one stub (see section 3) |
| ADV-236 | `it_adv236_20261125/` | per-animal values are NOT public for any of the four Wwox papers; draft letters A and B for the operator; map row `IT-ADV236-NQ1` |
| ADV-238 | `it_adv238_20261125/`; candidate `CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01` (PROPOSED) | leave-two-out wording applied to IT6 row 5 and IT12 README; cards, dossier and RP-036 go through the candidate and ADV (RP-036 patched by ADV) |
| ADV-240 | `it_adv240_20261125/` (push gate running when this was written; check `git log -- <folder>` on main) | **DONE, not queued:** 12 WWOX cases among 788 solved cases (1.5 percent; 1.3 to 1.6 leave-one-series-out) in seven gene-countable series; 4 of 14 series contain WWOX; PREREG predictions P1 and P4 wrong, P2 and P3 held; access list in the result |
| Map-owner state | `open_questions_map.tsv` | IT30 ids aligned; rows CQ6..CQ9; `IT-ADV222-NQA..NQG`; `ADV228-Q01` CONCLUDED to ADV-231 (Q02 stays OPEN); `ADV228-Q03` dated line only (status unchanged); `IT-ADV236-NQ1` new; IT-C on WO-03 and IT-B on NR-03 method lines |
| Session evaluation | `research/session_evaluations/2026-11-25_it_successor_adv230_238.md` | on main `f6840d03b6b1` |

## 2. Do NOT take ADV-240 again
ADV's message at 01:40Z said the successor would take ADV-240 as first item; the message crossed the work. It is finished. The successor's first item is whatever ADV assigns next; the open follow-ups are in section 5.

## 3. Lessons (for the active-lessons file of the role, not for a memory of the operator)
1. **A complete-read marker on a corpus stub is a trap.** The guard counts `PAPER` and `CORPUS P###` records and not `CORPUS-STUB-###`; `BATCH_20261124_003` gave a stub a complete-read status and main's CI went red for ten runs. Run `test_batch_queue` before any `BATCH_COMMIT`; a read stub becomes a `PAPER` record in the same batch (recipe: `BATCH_20261125_001`).
2. **Open the supplement bucket before declaring a column or file missing** (the PMC open-data bucket lists supplements by PMCID); ADV-230's "missing column" was revised by reading the bucket.
3. **A narrow phrase search beats a gene search; search animal identifiers, not only genes.** ADV-231 and ADV-233 searched genes and missed that IT12 had named the same two animals on 2026-10-31; ADV-238's first broad search returned thousands of rows for gene names in other datasets.
4. **Regenerate derived files on a committed tree.** `coverage_report` regenerated on an uncommitted merge state drifted; regenerate after the merge commit and check.
5. **Landing refused after a peer landed receipts first** (conflict only in generated files): take theirs, regenerate, never hand-merge; the gate takes 35 to 60 minutes plus about 6 minutes of lock queue per slot.
6. **Gate wording rule:** a person word (proband, patient-derived) near a drug name or a dose unit within about 700 characters trips `CLINICAL_CASE_LINKAGE`; none was triggered in the last four landings.
7. **A data statement is a printed sentence:** "RNA-seq only", "Not relevant" and "upon reasonable request" are results; the draft letters ask only for numbers that already exist, in two tiers.

## 4. DREAM line (legend-dream, today's results)
What the day changed that nobody had yet consumed: (a) the WWOX share among solved cases (ADV-240) is not yet quoted anywhere in RP-035 or the case-series readings; consumer ADV; (b) the J01 card sentence "positive in three forebrain regions" and the K01 card hypoxia sentence still read without the leave-two-out qualifier until the candidate is propagated; consumer the next `BATCH_COMMIT`, then a view regeneration; (c) the age problem (ADV-232) and the access finding (ADV-236) point at the same adult hypomorph holder: one reply from that group would serve NQ-A, NQ-B and the cortical PV question together, but outside contact is operator-reserved. EMPATHY: the operator's standing preferences seen in this window are unchanged (no contact, no spend, nothing sent in the operator's name; Italian in chat, English in files).

## 5. State, backlog and open work
* **Candidate backlog (3 queued):** `CC-20261120-ORCHESTRATOR-CLAIM035-S9-WORDING-01` part 2 and `CC-20261120-ORCHESTRATOR-WM103-DOSE-WORDING-01` part 2 are the operator's reserved items and stay queued; `CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01` is new and not reserved (MINOR wording). Run `test_batch_queue` first.
* **For the operator (nothing sent, nothing deleted by me):** the draft letters (`it_adv236_20261125/REQUEST_TO_AUTHORS_EEG_DRAFT_IT_20261125.md`); the access list of ADV-240 (Hamdan 2017, Trump 2016, the large JAMA and Lancet series) for the PDF request file; three superfluous untracked XML files in `files/fulltext/` saved by mistake (`PMID26355344_Chang2015_PMC4650446_epmc.xml`, `PMID25649963_Hsu2015_PMC4312067_epmc.xml`, `PMID19936220_LudesMeyers2009_PMC2777388_epmc.xml`; a removal was refused by the safety check and not worked around).
* **Optional carried clauses (ordinary edits only, no standalone landing):** myelin ADV-192 Codex-return-32 wording; ADV-191 organoid clause; INV-08 transferable distinction from ADV-196; ADV-197 lesson; INV-01 Fig 3 design-framework pointer.
* **Mandate:** `mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119`; two executable steps remained at the time of writing; the last bound step is OBJ_ACCEPTED[5] (operational continuation).

## 6. First moves for the successor
1. Read this file, then `git log origin/main --oneline -20`; confirm the ADV-240 push landed (folder `brainstorm_20261116/it_adv240_20261125/`).
2. Bind per the mandate recipe; proceed message right after BOUND; never end a turn on the bind.
3. Wait for ADV's next assignment; when none is open, follow `cross_session_transport.md` §12 (what comes next when the queue is empty) and the standing DREAM rule.
4. Landing recipe: new worktree from `development/main`, lint, reader-journey, structured-data integrity, view check, `safe_push.py development main --expect-sha <sha> --serialize` through nohup with an exit marker and a Monitor; no worktree changes while a gate runs.
