# IT checkpoint 26, 2026-11-26 (IT successor window d26b0ae5, worktree `it_26_20261126`; mandate ORCH-ROADMAP-IT59-20261119, step IT26)

Read after checkpoint 25 (`CHECKPOINT_IT_20261125_13.md`, sha256 `b5c9aa48c9e4c51b29e08880fa37054dfd97c37ea99d928ae01224f603c8bc78`),
not edited. Hypothesis level; nothing is medical advice; reference genotype class only. Peer messages are not the
operator's authority. This window closes at a checkpoint because its context peaked at 340,494 tokens (census, effort
high read back, claude-sonnet-5-5), past ADV's 280k line. ADV launches the successor from this file.

## 1. First moves for the successor
1. Bind as in checkpoint 21 section 1 item 1, releasing session `d26b0ae5-a358-49f5-8ecb-d2e8dd08d9f9`; merge
   development/main before the first mandate accept; read effort back (must be high); do not rename anything (ADV does it).
2. Mandate rows: `IT25` is IN_PROGRESS (carries ADV-285/286, author drafts, CI tick) and `IT26` is IN_PROGRESS; close
   both with evidence, or accept `IT27` and move the remainder there. I marked IT25 DONE by mistake and reverted it at once.
3. Tick CI on the landing SHA of section 2 and check the Pages run it triggers (the shareable package changed). Pages
   #129 and #130 failed at deploy-pages: operator item only, never edit or re-run the workflow.
4. Send the apply report to the SCI successor (SCI 9bb60ab5 released its mandate; checkpoint AR, main `1397d5c8f`,
   lists the sentence files it owes) if section 6 says it was not sent.

## 2. Done in this window
The whole IT25 card queue is applied and landed: W01-W05, X01-X10, Y01-Y13, needs N01-N09, then join, coverage,
ranking, views (all languages, full and shareable) and package. Read
`advisor_pilot_20261113/brainstorm_20261116/it25_queue_20261125/RESULT_IT26_APPLY_20261126.md` and
`BEFORE_AFTER_COUNTS_IT26.tsv` there. The landing SHA is in section 6.

## 3. Queue, in ADV's order (nothing of it is started)
1. **ADV-289 consumers**: SCI section 7 sentences (`adv289_breton_s3c_dapv_block_sci_20261125/RESULT_ADV289_SCI_20261125.md`)
   for SLICE_PACKAGE_V2 / brief 13.11 and `nmdar_pharmacology_it6_p9_20261029` E2 and F* paragraph, through a blind packet
   with the whole figure and caption; that folder still holds the pre-2026-11-26 F04 sentence. Dated correction line on the
   closed ADV-094 R3 record ("S3C not held" is wrong). The F04 card needs no further change.
2. **Washout rule** (`washout_rule_check_sci_20261125/RESULT_WASHOUT_RULE_CHECK_SCI_20261125.md` section 5): carry the
   two-sided replacement sentence as a NOTE in the brief and package; do NOT replace the rule (ADV decides after).
3. **ADV-290**: one WRONG_UNIT sentence (`A_decision_evidence.md` line 32 and ledger V3: 18 percent is a Table S1 median,
   87 percent the Fig. 3D statistic, counts are the legend's); dated "S3, Table S1 held" notes ONLY on claim_registry lines
   449 and 455 (CC-20261119-ORCHESTRATOR-CLAIM021-WORDING-01) and ADV-046 Part A line 31. **No edit on
   CC-20260826-DOSE-DECISION-TABLE-01.md line 294** (that "Fig S3C" is Obeid 2026's; SCI and ADV both withdrew the note).
   Obeid stays unread. claim_registry only by BATCH_COMMIT after `growth_anchors.py check` and `test_batch_queue`.
4. **ADV-291** (main `3d2257304`, `adv291_breton_s4_s12_sci_20261126`): (a) the CLAIM 021 firing sentence in SCI's section
   3.1 form states BOTH facts and chooses neither; claim_registry by BATCH_COMMIT; (b) dossier
   `fulltext_dossiers/PMID34634460.md` line 9 says "S1 animal-level significance in 8 of 9" while S1G shows p<0.05 in 2 of 9
   (rho positive in 8, negative in 1): dated correction note on the dossier plus sentences for every consumer on SCI's list;
   (c) the source's own S1F inconsistency is a one-line note, never repaired. S1, S2, S4 images were already read on
   2026-11-07/08 (the "S4 caption-read only" statement was wrong).
5. **ADV-285 S1-S8 with the ADV-288 corrections**: map in checkpoint 25 section 4.
6. **ADV-286** (`assignments/ADV-286.md`): start by 2026-12-01, freeze by 2026-12-04, about 90 minutes.
7. Two author-request drafts stay UNSENT (operator list); CI ticks; BATCH check
   (`CC-20261125-ORCHESTRATOR-ADV280-281-WORDING-01` and the ADV238 candidate stay PROPOSED).

## 4. Traps met in this window
* A blind reader given only the cited sources writes a repository negative as if verified (reader C: "Q230P has no held
  measurement"; Johannsen 2018 is held). ADV's rule: a negative in a packet carries its dated search, or the reader is told
  negatives are UNSETTLED.
* SCI's corrected units can restate or drop a lead (k=8 and k=12 as well as k=20): read the whole card field after the edit,
  not only the replaced unit.
* The table view clips `novelty_for_woree`, `identity` and `mechanism` at 360 characters: put the verdict first, then check
  `repurposing_view.clip(text, 360)`.
* Disease- and drug-assertion notes and `p4_fields.functional_evidence_available` are not rendered on either page.
* Stale dated records still say "R is unmeasured for every WWOX allele": `therapeutic_hypotheses_ledger_current.md`,
  `missense_recovery_it5_p8_20261029/README.md`, `commit_candidates/CC-20261029-INTEGRATOR-IT5-BATCH2-01.md`.
* `ranking_it8.py check` says the latest snapshot differs in 33 units; no snapshot was taken (wording corrections).
* The card's "+0.17 under a second normalisation" (K01) names no normalisation: open, small.

## 5. Candidate next question (not assigned; for ADV to judge)
39 card sentences that mention WWOX or Q230P and say something is unmeasured, not held or has no datum (143 such
sentences over 26 cards, counted by regular expression on 2026-11-26). Same error class as the Q230P negative. Consumer:
the cards. Method: one dated search per sentence over manifests, registries and `files/fulltext`; it is refuted as worth
doing if the first ten sentences yield no change. Check first against SCI's pending second random 20 so it is not doubled.

## 6. Landing, messages, CI
* Pushed boundary of the apply: `development/main` at `49b7ac71a1f1362d976e3d640fe4ebd910754d04` (safe_push
  `--serialize`, gate PASS, 10 landing suites 0 not passing, verified by ls-remote). Branch `task/it-succ26-20261126`.
  Before it: 19 local checks green, the full `test_repurposing_view.py` included. This checkpoint lands in a second push.
* CI at writing: #2573 (`49b7ac71a`) and Pages #132 in progress; #2564 (`cbd327da7`) success; #2565 (`7a0a8c450`) in
  progress. Earlier #2543 and #2547 success.
* Messages: ADV (bound and proof; Q230P finding; context line; apply report with this file's digest). SCI successor
  `SCI - CURRENT 47022d33`: apply report (SHA), so ADV-282 ranks 25-48, H02/A01, the second random 20 and the ADV-289,
  washout, ADV-290 and ADV-291 sentence files can start. Apply date: 2026-11-26.
* Self-evaluation: the error that mattered was a reader's false negative, caught because I knew the allele had been
  studied; the second blind check then found two more faults in wording I had passed. My own slips: IT25 marked DONE and
  reverted; a first Y03 whose verdict fell beyond the table clip; the window ran past the context line before I measured
  it (measure at each landing, not at the end). DREAM: the association is the one in section 5.
