# CHECKPOINT_IT_20261126_2 (IT27 to its successor; written 2026-11-26)

Task ORCH-ROADMAP-IT59-20261119, ACTOR_ID orchestrator. Hypothesis level; nothing here is medical advice. Reply to the
operator in Italian, write files in English. IT27 ran as session 6f4e0008; its context passed ADV's restart line.

## 1. Landed (development/main 42248ee7d, gate PASS)
* Breton 2021 sentences of SCI's ADV-289/290/291, two blind checks: brief section 13.11 (Addendum 21), slice package, NMDAR
  README, report row W3 and ledger V3, dossier PMID34634460, ADV-046 Part A, dated files for ADV-094 and FB08 (hashed
  originals untouched), CLAIM 021 by BATCH_20261126_001. Records: `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv289_291_consumers_it_20261126/`.
  Own catch: Fig S4 a2 axis zero is 20 pA BELOW rheobase.
* ADV-292 consumers, three blind rounds (records: `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv292_consumers_it_20261126/`): cards A01 (drug_assertions 0, 1, 3,
  genotype label), A03, A04 corrected; DL-MECH-170 and PAPER 219 by BATCH_20261126_002; view trio, language pages, package
  done; copied-sentence check 0 held; view suite 241 OK, i18n 31 OK.
* ADV-294 result `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv294_card_negatives_it_20261126/RESULT_ADV294_IT_20261126.md`: 1 of 9 assessed (N02), 8 STAND, N10 NOT
  ASSESSED (classifier stop; operator list; nobody retries or rewrites it). ADV decided: no sweep now.

## 2. Open, in ADV's order
1. **Apply N02** (card F04 `p4_fields.functional_evidence_available`): wording in the ADV-294 result section 2, blind-checked
   once (verdict ADD, needs the d-APV clause and the layer II/III location, both already in the wording). Do it with the
   next card batch (card + packet pair, `repurposing_bridge.py` rebuild, `check_cards.py`: no digit+unit tokens, then the view
   trio and `run --lang all` for both sources, package, copied_card_sentences.py, view suite and i18n via nohup).
2. **ADV-282 INC4-6 section 3.1** (SCI, sha256 f83403a07dab01f39e43a5fd5b84996df032b5999f3cc7837dc0af36f8c90a73, on main):
   DR-A01-007, DR-B01-002, DR-W2-004, DR-H02-036 (one clause; the first clause stays UNSETTLED), DR-I01-014; each through a
   blind packet with the whole source table. Section 3.2 held apart (ADD only), section 4 ADD only. SCI audits A01 after
   my sha; I promised no H02 edits before about 04:30Z.
3. **ADV-285 S1 to S8** with the ADV-288 corrections (Cheng Fig 2b/2c brackets, Palma P, n per arm 24 not 12): map in
   checkpoint 25 section 4.
4. **ADV-286**: START by 2026-12-01, freeze by 2026-12-04 (AES poster 1.019 on 2026-12-05; Table EV1 / E-MTAB-14792 not before
   2026-12-06). ADV: begin the design note in parallel (arms, hold date, comparator-completeness metric with the 25 to 45
   percent bar from five samples). Author-request drafts stay UNSENT. Brief: `assignments/ADV-286.md`.
* Not mine: PAPER 219 item (ii), B7 (SCI's re-read); the Pages deploys #129, #130, #132 (operator); the PDF
  `report_pilot_ketamine_20261123/render/out/ketamine_brief_pilot_final.pdf` page 2 row W3 still carries the old sentence
  (rebuild is operator-reserved); the worktree removal (operator).

## 3. Facts and traps for the next window
* CI at last check: #2573 and #2575 SUCCESS; #2586 (gate) and Pages #134 on 42248ee7d in progress: report the result to ADV.
* Delegates: `legend-delegate`, model sonnet, effort high stated in each dispatch, one at a time; sources are copied into a
  job-tmp folder; save every report with `extract_handback.py` before use. A blind reader of a figure needs the figure in
  its folder (the Wang 2024 Supp Fig S3 bar chart was in no file I could open: docx images were S1-S2 heatmaps).
* A card text change owes: bridge rebuild, `check_cards.py`, join/coverage/ranking runs (digest ff38fcaa61295a5a must not
  move), `repurposing_view.py titles --refresh`, `run`, `--source shareable run`, `run --lang all` (both), `package`.
* `pkill -f <string>` from the tool shell kills the shell (exit 144). Wait for background suites with an until-loop.
* Mandate rows: 72 steps, 4 executable remain; close the IT25/IT26 rows with evidence, remainder moved to IT27.
* Held files only in the root checkout `/home/desktop/legend-development/files/`. Obeid 2026 (PMID 42422765) stays unread.
* Obligations carried: every SCI sentence goes through a blind packet that carries the whole source table; EMPATHY habits
  (label numbers by panel and row, state unit and species, negatives carry date and query, a stated value is not an
  informative one, define the comparator first).
