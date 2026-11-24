# ADV-219 result: do the coverage labels of partial-depth receipts match the held artefacts? (SCI, 2026-11-24)

Hypothesis level; reference genotype class; nothing here is medical advice. Pre-registration: `PREREG_ADV219_SCI_20261124.md` (committed a482773b2 at 22:33Z, before the audit script was run on any record; digest in `PREREG_ADV219_SHA256.txt`). Mandate step OBJ_ACCEPTED[98]. No download, no ledger edit, no registry edit, no outside contact. A flag says "readable from held bytes", never "read".

## 1. Answer first

| | Frozen rule: latest receipt per study | Sensitivity: best state across all receipts of the study |
|---|---|---|
| Primary population (latest depth `partial_fulltext_read`) | 1077 ledger studies | same studies |
| With a held artefact and assessable | 575 | 575 |
| No held artefact (outside both denominators) | 497 | 497 |
| Not assessable (no text layer) | 5 | 5 |
| **Class A, MISLABEL** (label `not_present`/`unavailable`, section is in the held file): studies, flags | **24 of 575 (4.2%)**, 27 flags | **19 of 575 (3.3%)**, 19 flags |
| **Class B, OWED BUT HELD** (label `not_read`/`captions_only`, section is in the held file): studies, flags | **422 of 575 (73.4%)**, 1059 flags | **350 of 575 (60.9%)**, 767 flags |
| Any flag | 432 of 575 (75.1%) | 360 of 575 (62.6%) |
| Class B in a data-bearing section (results, tables, figures, supplementary) | 137 studies, 153 flags | 92 studies, 100 flags |

* **Precision of the flag rules (hand check, seed 20261124, 15 flags): 14 of 15 = 0.93** on question (i), above the 0.8 threshold, so the numbers stand as measured, not as upper bounds. Class A subset: 7 of 8 (0.88). The one failure is a rule failure: a section title that merely contains the word "methods" ("Newer approach for monitoring and screening methods") was counted as a Methods section.
* **The frozen "latest receipt" rule overstates the debt.** Of 428 ledger studies with more than one receipt, 172 have a latest receipt that records fewer `read` sections than an earlier one (a narrow re-read replaces the wide one; the ledger has no carry-forward). Under best state 300 of the 1086 primary flags (286 class B, 8 class A, 6 other) disappear, because an earlier receipt already marks the section `read`. Both columns are given; the right-hand one is the better estimate of what is really owed.
* **Mislabel (class A) is small; the debt is class B.** The receipts are mostly honest about what was read; the held files simply have not been read to the end. The cheap part of the debt: of the 100 best-state class B flags in data-bearing sections, 91 point at the very file the receipt names (digest equal), so closing them needs reading, not acquisition.
* **Ten records, frozen ranking plus manual link check:** all ten are Wwox/WWOX-subject records with an accepted link to an OPEN row, but **8 of the 10 lose every flag under best state** (an earlier receipt already read those sections). So the strict ten is mostly a labelling artefact; the two that survive carry only a references flag. Under the sensitivity set, **none of the first ten data-bearing survivors has an accepted OPEN-row link** (section 5). Plainly: the reading that could still move an OPEN row is not where the held-but-unread bytes are.

## 2. Method as run

* Script `labelling_flags_adv219.py` (print-only, no shebang, not executable, `--help`, no network, writes only stdout), run once with the frozen rules over `files/fulltext` and `files/deepening_downloads` of the root checkout (read only), `python3 -I`, started 22:33Z, finished in about 20 seconds of wall time over 575 assessed studies.
* Study key as the ledger keys it (PMID, else DOI, else the event-id token). Known limit: a preprint receipted twice under two keys (a DOI key in an old receipt, an event-id token in a newer one) appears as two studies; PAPER 157 is the case I know of, and it was read in ADV-216 an hour earlier, so I kept it out of the ten.
* Not applicable / zero: `unknown_legacy` in any primary latest receipt: 0.
* Secondary population (latest depth `queried_not_full_read` or `abstract_only`): 604 studies, 471 with no held artefact, 133 assessed; class A in 2, class B in 20 (latest-receipt rule). Small, because most of them have nothing held.
* Digest annotation (never used to include or exclude): class A flags in the latest-receipt set, 18 of 27 point at the file the receipt names, 9 at another copy; in the best-state set 17 of 19 equal. The 9 "other copy" cases (for example a receipt made from a PMC text-service copy while a PDF or XML of the same paper is held) are mismatches between two copies: the receipt's `not_present` may have been true of its own copy.
* Registry-restricted view (post hoc, for comparison with ADV-216's 283 PMID-bearing registry partial rows): 255 of them have a held PMID-named artefact; under the frozen rule 15 carry a class A flag, 140 a class B flag and 34 a data-bearing class B flag.

## 3. The 15-flag hand check

`precision_sample_adv219.tsv` has one row per flag (study, section, label, class, verdicts, note). 14 of 15 real sections: Methods in a narrative review (271 characters), Strengths and limitations (3583), Table 1 with numeric rows, Figure 1 images in two PDFs, two XML tables (37 rows), references lists, abstracts, Introduction/Results sections of 3.6 to 13 thousand characters. Failure: sample 8, a topic heading containing "methods". A second pattern appears among the other class A flags and is not in the sample: "methods" also matches "methodologies" (one more study, seen in its evidence string, not opened), and one "limitations" flag whose heading I did not open. Rule risks are marked in the `rule_risk` column of the class A list; I kept them there and did not recompute.

## 4. Consequences, as hypotheses

1. **The reading debt measure should be taken from best state, not from the latest receipt.** A re-read of one section writes a receipt that marks the other nine `not_read`; the registry's "partial" and the coverage report then understate what was read (this is the same direction of error ADV-216 found inside three coverage maps, and probably the larger source of it).
2. **A carry-forward rule would remove most class B flags at no reading cost** (286 of the 1059 vanish). This is a proposal for harness engineering, not a change I made.
3. **Class A is worth correcting by receipt, not by reading**: 19 studies where the held file shows a section the receipt calls absent (mostly tables, 16 of the 27). The list is `proposed_label_corrections_class_a_adv219.tsv`, for IT's batch route (not applied; three rows marked `rule_risk` need a look first).
4. **Acquisition, not reading, is the other half**: 497 of 1077 primary studies (46%) have no held artefact, so their partial label cannot be judged from bytes at all.

## 5. The ten (frozen ranking, manual link check, then the sensitivity)

Ranking by the frozen score is `ranking_prereg_latest_receipt_adv219.tsv`. The token rule (+1 per row sharing two rare title tokens) mostly matched generic words ("repurposing", "against", "current", "neurons", "status"), as expected; the manual check rejected a link unless the record is about the row's subject. Rejections, in rank order: PAPER 444 (4-PBA in an STXBP1 model, tokens "repurposing" and "against" only), PAPER 448, 450 and 461 (T-type and Ih precedents: same strand, not the same question; kept as reserve), PAPER 496, 213, 467, 535 (no link), PAPER 243, 344, 407, 109, 305 (token only). Duplicates of one record (CORPUS stubs) are one record.

| # | Record | Flagged section(s), latest-receipt rule | OPEN row it could narrow | Decision it could move (hypothesis) | Survives best state? |
|---|---|---|---|---|---|
| 1 | PAPER 006 (Wwox deletion, interneuron numbers and glia) | introduction, discussion, tables | RS-NP3A1 (fewer PV cells, less Pvalb per cell, or delayed maturation) | the reading of lower Pvalb; the PV/interneuron strand | no |
| 2 | PAPER 011 (neuron-specific WWOX gene therapy, dose-dependent rescue) | abstract, methods, discussion, references | WO-02 (restoration after first spike-wave discharge) | whether late restoration has a precedent | no |
| 3 | PAPER 022 (WWOX and neuronal differentiation of human progenitors) | abstract, introduction, discussion, tables (`not_present` is class A) | WO-22 (GSK3 output in WWOX loss) | the one-datum premise in WO-22 | no |
| 4 | PAPER 007 (P47T partial loss-of-function) | abstract, introduction, methods, discussion, figures | WO-34 (glial density before first spike), IT59-Q03 (heterozygote deficit) | the sign conflict on glia; graded heterozygote | no |
| 5 | PAPER 056 (WWOX promotes neuronal differentiation via GSK3beta) | references | WO-22 | citation leads only | yes, references |
| 6 | PAPER 094 (WWOX-MYC organoids) | abstract, introduction, results, discussion, tables | RS-R9 (names the record) | whether the faint mutant bands are WWOX | no |
| 7 | PAPER 031 (Wwox knockout oscillations and excitability) | abstract, introduction, discussion, tables | IT56-Q02 (independent origin of the three pillars) | independence of the excitability pillar | no |
| 8 | PAPER 475 (clemastine impairs developmental myelination) | abstract, introduction, discussion, tables | WO-27 (pro-myelinating signal), IT30-CQ3 | a counter-precedent for a pro-myelinating agent | no |
| 9 | PAPER 562 (dichloroacetate and pyruvate, neuronal survival after seizure) | references | WO-07 (PDK inhibitor in WWOX-deficient cells) | a neural PDK-inhibitor precedent | yes, references |
| 10 | PAPER 005 (neonatal neuronal WWOX gene therapy) | introduction, methods, results, discussion | WO-02 (and WO-01) | restoration timing | no |

For each, the section to read is the flagged one that survives; for the eight with no surviving flag the earlier receipt already has them as `read`, and the proposed action is a receipt/registry look (what that earlier receipt actually quotes), not a new reading.

**Sensitivity (post hoc, not frozen).** I re-ranked with only flags that survive best state and sit in a data-bearing section or class A (`rank` over 119 flags, 107 studies). The first ten of that ranking (PAPER 496, 467, 243, 407, 305, 180, 405, 449, CORPUS 193, 118) have **no accepted OPEN-row link**: token matches or none. The surviving debt in data-bearing sections therefore sits in records no OPEN row asks about; two caveats: my link test needs two shared rare title tokens, so a real link with fewer would be missed (for example the hypoglycaemia papers against IT59-Q04, which I noticed by hand and did not count), and I checked only the first ten of that ranking, not all 92 studies.

## 6. What surprised me

That the ledger's "latest receipt" is the wrong unit: the latest receipt of PAPER 094 carries five `not_read` flags although an earlier receipt already marks all five sections `read`, and the frozen ranking kept it among the ten. I froze the rule before looking, so the result stands as measured and the correction is stated beside it rather than replacing it. Second, how small class A is: the receipts under-claim far more often than they contradict the files.

## 7. Limits

* One ledger snapshot (main at the time of the run, 2712 chained receipts, those of ADV-216 included); held-file search over two folders; the 497 no-artefact studies may be held elsewhere or under names the three match rules do not catch.
* Extraction by rules: sections are detected by heading or element, not by reading; 14 of 15 hand-checked flags were real, 1 was not; the class A share carries the larger relative error (7 of 8).
* The best-state view treats an earlier receipt's `read` as true of the study; it is only as good as that receipt.
* Link judgment in section 5 is mine, by title and row text, not by opening the papers; blind recheck not run.

## 8. Files in this folder

`PREREG_ADV219_SCI_20261124.md` (+ digest, time) · `labelling_flags_adv219.py` · `rank_adv219.py` (print-only) · `flags_all_latest_receipt_adv219.tsv` (every flag, both populations, with evidence string and digest annotation) · `proposed_label_corrections_class_a_adv219.tsv` (best state, 19 rows, for IT's batch route, not applied) · `class_b_data_bearing_held_best_state_adv219.tsv` (100 flags, 92 studies) · `precision_sample_adv219.tsv` · `ranking_prereg_latest_receipt_adv219.tsv`.

## 9. DREAM line

Changed: the measure of reading debt (best state, not latest receipt). Consumer: ADV (direction of the next reading batch: far less debt in data-bearing sections than the registry suggests, and none of it linked to an OPEN row in the top of the list), IT (class A corrections), harness engineering (carry-forward rule proposal). Nothing here moves a scientific claim.
