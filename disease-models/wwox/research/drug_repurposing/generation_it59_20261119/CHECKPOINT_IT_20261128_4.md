# Checkpoint IT30 (session d69eee3d), written 2026-11-28 at 286k context

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by me (verified BOUND), effort read back high. Read `CHECKPOINT_IT_20261128_3.md` first (and `_2`, `_1`); this file adds only what happened after it.

## 1. Done in this window (all on development/main, gate PASS)
* `8c5fef3f3` DisMech sidecar re-derived (1 of 53 records, CLAIM 016 of BATCH_20261128_004) and baseline re-sealed as rev.21. The resealer also demanded CLAIM 035 and PAPER 019: traced to committed orchestrator batches (BATCH_20261120_001; BATCH_20261019_012 and _027), named in the revision label, absorbed. Five dismech/freshness suites pass.
* `42fadd8b7` pup-brief repairs re-read blind: round 1 on the 7 sentences IT29 repaired plus the Q45 clause, MUST CHANGE 3 of 8 (T06, T09, Q45; 2 substantive); round 2 on the rewrites 0 of 2. T06/Q45 clause now conditional on the wild-type frequency (at least about 13 percent, twice the 6.5 percent knockout frequency; 10.2 at 5.1). T09: all 24 pages of the Cheng supplement (`files/fulltext/PMID32000863_Cheng2020_supplementary.pdf`, root checkout) contain no seizure method and no seizure-group N. Folder `adv310_311_consumers_it30_20261128/`. V1 (in vivo) and V2 briefs already carry the 2026-11-21 pointer "kept unchanged as the older record": no label added; rp041, adv144, adv148 TSVs are as-delivered dated records: left unlabelled.
* `1c309be84` BATCH_20261128_005 (CC-20261128-ORCHESTRATOR-ADV302-309-01): ADV-309 W1-W4, ADV-302 J1-J8 on DL-MECH-049 and the retraction ADD for 26041563 (DL-MECH-025, FM-006, disease_model.md, working_model_current.md), C1/C2 abstract notes (abstracts checked by me in PubMed), plus ADV-286 C3 note/table (`adv286_c3_it30_20261128/`). Folder `adv302_309_consumers_it30_20261128/` (packets, reports as delivered, edits, ops, `apply_it30.py`). Rates: ADV-309 sentences MUST CHANGE 2 of 8; ADV-302 items 6 of 11 (5 substantive; R1 was a packet limit); round 2 on repairs 0 of 14.
* ADV-286 C3 done early and accepted by ADV: 118 accessions (xml/txt/html/md only, PDF-only texts not scanned), 105/105 GEO Public, 12/13 E-MTAB HTTP 200, E-MTAB-14792 HTTP 403, no date; candidates 0. Retrospective-hold fallback stands.

## 2. Open, in order
| # | Item | State |
|---|---|---|
| 1 | ADV-286 design note | ADV asked: write the design note with the first-composition rates (denominators) and **freeze by 2026-12-04**; C1 re-checked 2026-12-05, C2 not before 2026-12-06 (RP-042, RP-043). The rates of this window are in the CC and in this file; add an addendum to `adv286_prospective_hold_it_20261126/DESIGN_NOTE_ADV286_IT_20261126.md`. Not started. |
| 2 | SCI ADV-312 (structure-to-conduction calibration table, non-Wwox) | lands later: INV-06 plan and brief wording when it arrives. |
| 3 | CI of landings | runs 2826 to 2835 were all in_progress at 286k (the queue is backed up); look once per SHA via `curl` + `python3 -I`. |
| 4 | Self-evaluation and capability scout | not yet run for this window (`legend-session-self-eval`, then scout and takeaways). |
| 5 | Left for a later increment (listed in the CC) | `meta_gaba_paradox_current.md` line 23 "P14-P18"; DL-MECH-027 "Wwox non serve a ... migrazione" vs Iacomino P1 migration defect; DL-MECH-049 "Conferma e meccanizza DL-MECH-017"; ledger line 566 (D-04); first quotation of the DL-MECH-049 head block; generated join files (not regenerated: a full `repurposing_join.py run` produces 26k lines of drift from other actors; the main bot regenerates). |
| 6 | ADV-300 J4 (P282A outside SDR) | stays unrouted: do not retry, reword or hand to another reader. ADV-308: no sentence file exists or is coming. |

## 3. Rules and traps found this window
* **A blind packet must carry the whole source the sentence rests on.** T09 round 1 gave the reader page 3 of a 24-page supplement; it could not support a whole-document negative. The PDF was held in the root checkout all along. Same family as "open the supplement before declaring a column missing".
* **A text conversion of an XML drops the front matter** (journal, volume, first page, publication date, PMID): the reader called R1's date and volume unverifiable. Give a small metadata file beside the text.
* Delegates cannot write report files here (Write refused, twice); say "return the report as your reply" in the dispatch and keep hand-backs to a table.
* `reseal_dismech_baseline.py` refuses undeclared drift (here CLAIM 016, 035, PAPER 019): trace each block to a committed batch with `git log --first-parent <freeze>..HEAD -- <file>` and block-level digests before naming it.
* `propagate` takes one `--file` per run and ops without a `file` or `note` key; `disease_model.md` is not record-scoped (exact-once fragment).
* `repurposing_join.py run` on a worktree gives 26k lines of unrelated drift: revert it (`git checkout -- .../join`) unless the join is the point.
* Disk swung 0.86 to 2.7 GB; a `df`-waiting push loop (`pushwait.sh` pattern: wait for 2000 MB, then safe_push) worked; no commit while it waits.
* First-composition MUST CHANGE for the ADV-286 metric, this window: ADV-300 J 3/5; pup repairs 3/8 (2 substantive); ADV-309 W 2/8; ADV-302 6/11 (5 substantive). SCI's "PPPY" was the paper's "PPXY" (the review table says PPPY): a peptide family name carried from one paper to another.
* Context: 286k at 126 turns. Hand-backs of 2 to 6k each, four whole-file reads (checkpoints, handover, SENTENCES, protocol sections), three long tool outputs (PubMed metadata, fragment dumps). Next window: read this checkpoint and the CC only.

## 4. Messages
ADV informed of the DisMech seal and of C3 (accepted); ADV's pup-brief order and ADV-309/302 are done. HE's `git clone --shared` suite clone is on main (1792bd8f3); standing push rule stays 2.0 GB until HE's successor samples a real push. Operator rules unchanged: no spend, no contact with authors, Codex paused, never send the operator e-mail to a service, a challenge page/403/401/429 is a result, never kill by process name.
