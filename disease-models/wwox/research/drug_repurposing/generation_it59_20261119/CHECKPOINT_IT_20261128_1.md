# Checkpoint IT28 (session 54ca757b), written 2026-11-28 under a disk emergency

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119.

## 1. First moves for the successor
1. `df /` first: on 2026-11-28 the disk was at 100 percent (571 MB free, 2 GB later). No clones, downloads or view rebuilds (each rebuild writes about 60 MB) until ADV says the disk is clear; deletions are not mine (classifier denied ADV's cleanup).
2. Read the three result files: `advisor_pilot_20261113/brainstorm_20261116/adv282_inc46_consumers_it_20261126/RESULT_IT28_APPLY_20261126.md`, `adv285_288_consumers_it_20261126/RESULT_IT28_ADV285_288_20261126.md`, `adv287ext_consumers_it_20261126/RESULT_IT28_ADV287EXT_20261126.md`.
3. ADV-295 block 1 (SCI) is DONE and landed: 81d9523bc, BATCH_20261128_001 (CLAIM 032, DL-THER-089, DL-REPO-003, DL-METH-118, RP-033). Open for SCI: ledger says Table S7, Qin cites S6; optional B1/B3 ADDs not applied. Nothing else is queued from SCI; next, ask ADV for the next held-source question (no idle lab).
4. ADV-286: decision point 2026-11-30 (say if C1 AES poster and C2 are unretrievable; fallback is the retrospective-hold design), freeze 2026-12-04. Design note: `adv286_prospective_hold_it_20261126/DESIGN_NOTE_ADV286_IT_20261126.md`.
5. DR-A01-002 "every target of the lot" stays withdrawn pending SCI's re-read of 30266908, 42157447 and 42587736.

## 2. Closed in this window (do not redo)
ADV-282 INC4-6 + N02 + L01-003 (24 sets), ADV-285/288 consumers, ADV-287 extension H02/A01/random 20, HE's ADV-293 M01 clause and ADV-295 block 1; all on development/main (last landing 81d9523bc, gate PASS; CI #2598 and Pages #136 success for 45576bfcb; CI for 81d9523bc not yet checked). N10 never touched. No BATCH_COMMIT for the card batches (cards only); BATCH_20261128_001 for ADV-295 (CLAIM 032 by `batch_commit.py propagate --ops <file>`; the discovery ledger is not a record-scoped file and was edited by exact-once fragment replacement).

## 3. Rules and traps (new)
* A card sentence can also sit in the hand-kept INV tables (E04 ketogenic sentence in investigations.tsv): `copied_card_sentences.py` finds it only after the card commit; run it, edit the rows, run `ranking_it8.py run`, rebuild the views, then `i18n --what collect` BEFORE `safe_push` (it refuses on a stale inventory, twice here).
* Fragment edits (card, where, old, new) with an exact-once old fragment are safer than rewriting a whole field: `adv287ext_consumers_it_20261126/apply_287ext_it28.py`.
* Every blind round changed wording: over-generalisation (class for one compound), an inherited label (N2 unmyelinated is Palma's, not Repudi's), "normal" for "n.s.", an animal-count order that did not follow the group order, "shows" for a small single study.
* Blind readers cannot see a repository-held label or a repository-search clause: those stay OUTSIDE and rest on SCI's verification.
* A subagent grep on a named supplement folder can print a repository reading note: disclosed by the reader, no verdict rested on it.

## 4. Messages and state
ADV and SCI informed of the landings; HE's M01 sentence applied. SCI's ADV-295 message (abf15a728) answered only by this checkpoint.
