# CC-20261027-SCIENTIST-D-LDHREADS-01

- **Class:** ORDINARY (research layer; no consolidated baseline claim; no working-model change). **target_wm_version:** none.
- **Source:** package W1.3, task `SD-IT2-LDHREADS-20261027`, branch `task/sd-it2-ldhreads`: `research/drug_repurposing/ldh_readings_w13_locators_20261027.md` (54 verbatim triples, all exact-matched against the artefacts, plus figure readings), `sada_ldh_precedent_p2a_20261026.md` sections 0, 2.2, 2.3, 7, 8, and five staged receipts `research/receipt_staging/scientist-d/FTR-20261027-{42035940,36278433,41570991,38443647,30946030}-01.json` (`staged_receipt_check.py --check-doi`: OK).
- **NOT WWOX EVIDENCE.** Tumour cells, liver cells, isolated mouse mitochondria, rats, mice. Class level, not medical advice.

## What the re-read changed (and what it did not)
Unchanged: direction (stiripentol decreases LDH activity / lactate in these systems), species and cell types of rows -006 and -007, the doses and concentrations as printed, "potency unresolved", and the verdict of card E02. None of the five sources states the stereochemistry (racemate versus enantiomer) used; the clinical racemate is implied for the Bacq review and Le Dudal ("Diacomit", Biocodex) only.
Changed or added:
1. **Ordering of effective concentrations (INFERENZA; no potency comparison).** Stiripentol effects on NADH oxidation by isolated mouse mitochondria occur at lower nominal concentrations (25 to 100 uM; Bouchez Fig 5: heart about 48, 5, 1 percent remaining at 25, 100, 150 uM; liver about 67, 36, 23) than LDH inhibition in a treated-cell lysate and on recombinant enzyme (250 to 500 uM). No assay compares them and no LDH IC50 exists, so potencies are not comparable. Row -006 should read "complex I NADH oxidation inhibited in isolated mouse heart and liver mitochondria from 25 uM (plot readings, auditor-confirmed, about +/- 3 points)". The previous "about 50 to 150 uM" lower bound was wrong. A source-internal contradiction (Results last sentence) is recorded. Yadav's assay is a lysate of cells treated in the dish, not cell-free.
2. **Bouchez text-versus-figure:** "about 70 percent at 100 uM" is 51 to 53 percent raw (57 to 58 net of antimycin) at 100 uM in Supplementary Fig 2 (about 80 raw, 88 to 89 net at 200 uM). Row -006 should not carry the 70.
3. **Guyon:** the 150 mg/kg in the Results and legend is not stated anywhere in the Methods (100 mg/kg appears in the bevacizumab sentence, in a paragraph on knockout cohorts with n = 8 per group, whereas Fig 6F has n 15 to 16, so the Methods probably do not describe the Fig 6F cohort; not established); median survival 80 versus 97 days; human stem-like cells in immunodeficient mice. Genetic LDHA/B double knockout raises respiratory capacity whereas stiripentol lowers it (INFERENZA: the drug does not phenocopy LDH ablation on respiration).
4. **Le Dudal:** Results 200 mg/kg/day for 48 h versus Methods 200 mg/kg "twice" (most simply 200 mg/kg once a day over two days); patent declared by two authors; human data (8 Dravet children versus 40 cystinuria controls; one case) are oxalate only. Its in vitro "therapeutic concentration" (5 to 100 ug/mL) extends above the serum range it quotes (4 to 22 ug/mL).
5. **Bacq:** manufacturer-authored review; its Table 2 LDH "effective concentration" range rests on three rows: the 2015 report (500 uM, second-hand), Guyon (500 uM, cellular lactate), Le Dudal (42 to 427 uM, indirect oxalate). Row -007 stays INFERENZA, secondary.
6. **Yadav:** the size of the LDH inhibition is not in the text and Fig 1E could not be retrieved; the enzyme-assay text is ambiguous about the enzyme source. Row -006 keeps "moderate", no number.
7. **Correction to my own earlier sentence** (note 2.3): "no animal result in these sources measures brain LDH activity or lactate" was too absolute; two second-hand statements exist (Sada via Guyon; a rat ischaemia study via Bacq). Reworded.

## Proposals for the integrator
1. Record the five staged receipts in event-ID order (`record_staged_receipts.py`).
2. In `build_cards.py`, row `DR-E02-006`: replace the receipt `null` with the five event IDs only if the checker accepts several (else cite `FTR-20261027-41570991-01` and `-42035940-01`, the two that carry the numbers), set `reading_depth` to `partial_fulltext_read`, replace "oxygen consumption and complex I NADH oxidation are inhibited directly and immediately" by the quantified wording of item 1 and add the Guyon respiration dissociation; row `DR-E02-007`: add receipt `FTR-20261027-38443647-01`, depth `queried_not_full_read`, and "manufacturer-authored review". Rebuild only E02; `check_cards.py`.
3. `HYP-20261026-11`, Stage 0 (assay level): add a complex I NADH-oxidation arm in the same preparation at a 25 to 150 uM bracket next to the LDH arm, because the readings now place complex I below LDH in concentration. Direction of the hypothesis unchanged; its CONTRA sentence on complex I gains "from 25 uM in isolated mouse heart mitochondria (plot estimate)". No ranking change.
4. No change to `R-11` or `DL-REPO-004` beyond citing the receipts.

## Needs an independent verifier (not the producer)
- A blind `legend-locator-audit` of `ldh_readings_w13_locators_20261027.md` (54 triples); first the five that carry the corrections: B2, B5, G4, L4, Q7.
- The Fig 5 and Supplementary Fig 2 readings (F1 to F6): they are plot estimates by one reader; a second reader, ideally measuring points on the PDF page at higher resolution.
- Item 1 (ordering of effective concentrations only; blind-audited 2026-10-27 and reworded as above).

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer; `WM_v7.27` preserved)
**Batch:** `BATCH_20261019_023` (2026-10-27, MINOR, MANUAL, ACTOR_ID `integrator`, task `INT-IT2-BATCH-20261027`)

- **Proposal 1:** the five staged receipts recorded in event-ID order after a trial in a throwaway clone (ledger 873 to 878 events; staged JSON unchanged by the stamp).
- **Proposal 2:** card `E02` rows `DR-E02-006` (receipts `FTR-20261027-42035940-01` and `-41570991-01`; `partial_fulltext_read`; quantified wording with the Guyon respiration dissociation) and `-007` (receipt `-38443647-01`; manufacturer-authored review) in `build_cards.py`; the card checker forbids numbers adjacent to concentration units, so the concentrations are written as "tens" and "hundreds of micromolar" in the card and kept numerically in `HYP-20261026-11`.
- **Proposal 3:** `HYP-20261026-11` Stage 0 gains the complex I arm (25 to 150 uM), the CONTRA sentence carries the plot estimate, and the "no animal source" sentence is reworded. No ranking change.
- **Proposal 4:** `R-11` and `DL-REPO-004` unchanged.
- **Still owed:** a second reader for the Fig 5 and Supplementary Fig 2 plot readings. The receipt for `36278433` declares only the abstract as read although the locator file quotes its Methods and Results: not edited (ledger is append-only); a correction receipt is owed by the author if the coverage is wrong.
