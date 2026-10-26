# CC-20261026-SCIENTIST-B-SADA-LDH-01

- **Class:** ORDINARY (research layer; touches no consolidated baseline claim; no working-model change).
- **target_wm_version:** none.
- **Source:** package P2a of `scientist-b` (task branch `task/sci-b-p2a-sada2015`): `research/drug_repurposing/sada_ldh_precedent_p2a_20261026.md` (acquisition record, first-pass observations, four-layer comparison, reconciliation, discriminating experiments), the manifest `research/deepdive_manifests/PMID39769031.json` (PASS) and the staged receipt `research/receipt_staging/scientist-b/FTR-20261026-39769031-01.json` (`staged_receipt_check.py --check-doi`: OK). Extends the follow-up of `CC-20261026-SCIENTIST-C-LCFOLLOWUP-01` (landed as `HYP-20261026-11`, `DL-REPO-004`, card `E02`, map record `R-11`).
- **Everything here is NOT WWOX EVIDENCE:** every line concerns (enzyme, tumour and liver cells, rats, mice, other diseases). Class level, no dose, not medical advice. Statements about what a compound would do in WWOX-deficient tissue are INFERENZA or IPOTESI and owed a blind audit by someone other than the producer.
- **The target paper was NOT acquired.** Sada 2015 (PMID 25792327) is paywalled; the cascade is recorded in the note and in the wishlist (items 16 and 17). Everything below about it is abstract-level plus second-hand description.

## What changed in the readings (one paragraph)
Stiripentol's LDH potency is **unresolved**, not weak-and-closed: only single-concentration enzyme measures exist and none gives a fitted potency: about 40 percent at one concentration (second-hand, from the 2015 report); in the 2024 paper about 10 percent for the racemate and 34 to 38 percent for the enantiomers at that same concentration (so the enantiomers are close to the 2015 figure; the racemate-outside-enantiomers scatter, up to two-fold, recurs across its analogue table; its "IC50 above 500" is a bound and no stiripentol curve is reported); 7 percent at a four-fold higher concentration in the ChEMBL document (Bai 2019; lower row empty). (Corrected after the blind audit of 2026-10-27.) Stiripentol also inhibits mitochondrial complex I directly (2026), changes cellular lactate and respiration below the concentrations that inhibit LDH in lysate (2026 glioblastoma), and a 2024 review puts in-vitro LDH-effective concentrations at or above total plasma levels and far above free tissue estimates. A stiripentol arm in a WWOX experiment therefore **would not test LDH** without a prior assay-level stage and a complex I dissociation control. No source supports general inefficacy; none supports WWOX efficacy.

## Revision 2026-10-27 (repair after the blind audit, scientist-d)
Manifest entries narrowed and stamped (`contradicts_locator` + audit record): #4, #5, #9, #10, #12, #13 (1-based) and #17 (S66 steepness); two entries added (hepatotoxicity sentence in 2.4; the (2R*,5R*) rows). Note section 2.1 rewritten (the three measures do not "disagree": the ~10 percent is the racemate only); IC50 span 101.7-213.7; Guyon dose discrepancy downgraded to possible; card E02 rows -005 (no 'hippocampal') and -006/-007 (locators, dose wording) corrected. **Re-audit owed, by someone other than the producer and other than the first auditor where possible:** entries #4, #5, #9, #10, #12, #13, #17 and the two added entries (#18, #19).

Second repair 2026-10-27 (re-audit by scientist-a): #13 and note 2.1 causal wording replaced by 'cause not determined'; #18 gains the hepatoprotective-in-rats citation and the no-label-warning sentence; #10 absence word list widened; note 2.1 heading restricted to stiripentol; card DR-E02-006 'not attributable to LDH alone'. Still UNVERIFIABLE here: the Sada 2015 content (card row -005, second-hand) and the ChEMBL 7 percent at 2 mM (database row, article unread).

## Proposals (for the integrator; none was applied by the producer, except the research-layer files listed under "Landed on the branch")

1. **Record the staged receipt** `FTR-20261026-39769031-01` with `record_staged_receipts.py` in event-ID order; then add `"receipt": "FTR-20261026-39769031-01"` to row `DR-E02-004` of `E02` in `build_cards.py` and rebuild (the card checker requires an id already in the ledger, which is why the row does not yet carry it). `reading_depth` stays `partial_fulltext_read`.
2. **`HYP-20261026-11`, replace three bullets and extend one** (via `record_scoped_edit.py`, label EXPLORATORY; no status or ranking change; text below).
3. **`R-11` of `analysis/mechanism_intervention_map.md`, correct two cells** (text below). The cell "no source attributes its antiseizure action to LDH" is wrong as stated.
4. **`DL-REPO-004`, append one dated line** to its causal statement (text below); status stays `open`.
5. **Owed audits:** a blind `legend-locator-audit` of the propositions in `PMID39769031.json` (hand the two over-reach flags first: a bound read as a value; the racemate below both enantiomers); and of the INFERENZA lines of card rows `DR-E02-005`, `-006`, `-007` (second-hand or targeted-passage rows, no receipt).
6. **No registry edit is proposed beyond 2 to 4.** `research_lines_current` and the strategies surface are not touched.

## Landed on the branch (research layer, already in this commit)
- Card `E02` regenerated by `build_cards.py` (only `E02` changed; `E01`, `E03`, `E04` bytes unchanged): row `DR-E02-001` re-identified (document = Bai 2019), new rows `DR-E02-004` to `-007` (enzyme paper, the 2015 report at abstract level, cellular dissociation, exposure comparison), novelty line corrected ("not found by my query" is replaced by "identified, paywalled, abstract-level"), evidence for/against, pharmacology, gaps and `no_new_reading` updated. `check_cards.py`: 16 packets, 0 problems.
- Operator PDF wishlist: items 16 (Sada 2015) and 17 (Bai 2019).

## Text for proposal 2 — `HYP-20261026-11`

Replace the title's trailing clause "a weak approved candidate" with "an approved candidate whose LDH potency is unresolved".

- **Evidence PRO (fly, NOT WWOX-DEE; unchanged first sentence)** then add: "A 2015 report in epilepsy models (abstract-level; full text not acquired) describes stiripentol as an LDH inhibitor and an analogue that suppressed seizures in a mouse model; a second laboratory found enzyme inhibition by stiripentol in vitro (about a tenth for the racemate, about a third for the enantiomers, at one high-micromolar concentration) and four synthetic analogues with screen-grade potency (fitted IC50 about 100 to 214 micromolar with up to two-fold unexplained racemate-enantiomer differences (cause not determined); partial full-text reading, receipt staged). In rats at high doses stiripentol lowers urine oxalate and raises glycolate in hyperoxaluria models, a hepatic pathway readout. (None of this is WWOX evidence.)"
- **Evidence CONTRA (replace the clause "stiripentol inhibits LDH only weakly in the retrieved measurements and has other pharmacology"):** "stiripentol's LDH potency is **unresolved**: only single-concentration measures exist and none gives a fitted potency (the 2024 value for stiripentol is a bound, no stiripentol curve is reported, and its racemate and enantiomers differ about three-fold at one concentration); stiripentol inhibits mitochondrial complex I directly and changes cellular lactate, respiration and viability at concentrations at or below those that inhibit LDH in lysate, so a metabolic effect is not an LDH effect; a 2024 review puts in-vitro LDH-effective concentrations at or above total plasma levels and far above free tissue estimates and ranks LDH last among its mechanisms; no animal source measures brain LDH activity or lactate after stiripentol; a weak enzyme measure is not general inefficacy and is not read as such."
- **Minimal falsifying experiment (insert before the stiripentol-against-tool stage):** "Stage 0 (no WWOX): fitted potency and mode of stiripentol and its enantiomers on human LDHA and LDHB with a selective LDHA positive control, with and without detergent, at two substrate levels and in both directions, two enzyme lots; if the fitted potency is far above free tissue levels or collapses with detergent, the stiripentol arm of any WWOX test is not an LDH test. Stage 3 then adds a low-dose complex I inhibitor arm so that stiripentol's effect can be assigned to LDHA or to complex I." (Full design in `sada_ldh_precedent_p2a_20261026.md` section 6. A proposal; nothing authorised to run.)
- **Reopening condition (new, one line):** "A fitted stiripentol potency within reach of free tissue levels, detergent-insensitive, or the 2015 report's enzyme and exposure data once the article is obtained."

## Text for proposal 3 — `R-11`

- **NEAR_DISEASE_EVIDENCE**, replace the clause "its LDH inhibition is weak in the retrieved measurements (single-digit percent at a single high millimolar-range concentration; abstract-level papers: moderate but not potent); no source attributes its antiseizure action to LDH" with: "its LDH inhibition is unresolved, with single-concentration measures only: about forty percent at one high-micromolar concentration (second-hand, from a 2015 report whose full text is not held), about a tenth (racemate) to a third (enantiomers) at the same concentration and a bound for the potency in a 2024 paper (partial full-text reading), single-digit percent at a four-fold higher concentration in a database document (Bai 2019); the 2015 report attributes seizure suppression in epilepsy models to LDH inhibition (abstract-level) while a 2024 review argues, on exposure, that other mechanisms dominate its antiseizure action; stiripentol also inhibits mitochondrial complex I directly (2026)".
- **DECISIVE_PRECLINICAL_TEST**, insert at the front of its third clause: "an assay-level potency and mode determination of stiripentol on human LDHA and LDHB (with a selective LDHA positive control, detergent and substrate-level arms),".

## Text for proposal 4 — `DL-REPO-004` (append to "Causal statement")
"UPDATE 2026-10-26 (scientist-b, P2a): the stiripentol-LDH potency is unresolved rather than weak: only single-concentration measures exist (about forty percent second-hand from the 2015 report; about a tenth for the racemate and a third for the enantiomers in the 2024 enzyme paper, whose IC50 for stiripentol is a bound; single-digit percent at a higher concentration in the ChEMBL document, which is Bai 2019); stiripentol also inhibits mitochondrial complex I directly. The 2015 report was not acquired. A weak measure does not establish inefficacy and no source tests any LDH agent in a WWOX system."

## Discriminating experiments (proposals only; none authorised)
See `sada_ldh_precedent_p2a_20261026.md` section 6: E-A (assay level, no WWOX; decides whether stiripentol is an LDH tool at all), E-B (WWOX-deficient versus isogenic human neural cells, with LDHA-tool, LDHA-knockdown and complex I-control arms, isotope-resolved lactate and redox readouts), E-C (read the 2015 report if the operator obtains it). Each states question, model, controls, endpoint and the result that would change the interpretation.

## What was NOT proposed
- No claim, paper-registry or working-model edit; no change to `HYP-20261026-10`, `HYP-20260709-01` or the PDK/DCA position.
- No inference from any result in tumour cells, liver, rat or mouse seizure models to WWOX-DEE; no statement that stiripentol is ineffective on LDH.

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer; `WM_v7.27` preserved)
**Batch:** `BATCH_20261019_022` (2026-10-27, MINOR, MANUAL, ACTOR_ID `integrator`)

- **Proposal 1:** the receipt `FTR-20261026-39769031-01` was already in the ledger (873 events); the row `DR-E02-004` of card `E02` now carries it (`build_cards.py` edited, only `E02` rebuilt, `check_cards.py` 16 packets 0 problems); `reading_depth` stays `partial_fulltext_read`. The receipt had no registry identity, so `PAPER 568` and `LIT-0839` were added.
- **Proposal 2:** `HYP-20261026-11` title, Evidence PRO and CONTRA, the new Stage 0 and Stage 3 text and a new reopening condition; `generated`, no ranking, EXPLORATORY; Sada 2015 stays UNREAD (`UNVERIFIABLE_SURFACE`, second-hand), wishlist items 16 and 17.
- **Proposal 3:** `R-11` NEAR_DISEASE_EVIDENCE and DECISIVE_PRECLINICAL_TEST corrected, the superseded wording quoted.
- **Proposal 4:** one dated update in `DL-REPO-004`; status `open`.
- **Audits:** the manifest entries were blind-audited three times (`research/locator_audits/2026-10-27_PMID39769031_*`); the INFERENZA lines of card rows `DR-E02-005` to `-007` remain owed.
