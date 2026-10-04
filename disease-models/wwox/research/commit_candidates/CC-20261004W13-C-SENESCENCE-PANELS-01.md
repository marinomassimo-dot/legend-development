# COMMIT CANDIDATE — CC-20261004W13-C-SENESCENCE-PANELS-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 13 2026-10-04, branch `task/sci-C-20261004w13`.
**context_policy:** `QUESTION_DRIVEN` (DIS-028 and DIS-029 were held before the panels were opened).
**Not medical advice.**

## Target

`disease-models/wwox/research/dismissal_ledger_current.md`: `DIS-028` (a qualification is appended) and
`DIS-029` (its premise sentence is corrected). Both rejections **stand**. The change is to their premises,
not their verdicts.

## What is wrong or missing now

Both entries were written over a reading of PMID 37897534 that did not open the figure panels or the
supplement. The wave 13 reading opened Figures 1 and 2 as images and the supplement legends (Table 1,
Figures S1–S9).

* **DIS-028** cites the loss-side γH2AX rise as a plain fact. Figure 1d qualifies it:
  * the comparator is the heterozygote;
  * the difference is N.S. at early passage (about 4.5 % vs 7.5 %) and is *** only at passages 20–30
    (about 20.5 % vs 35.5 %);
  * passage alone raises the heterozygote about 4.6-fold, more than genotype adds at late passage
    (about 1.7-fold).

  No surface read carries a wild-type γH2AX arm or a WWOX re-expression arm, so this source cannot meet
  the entry's revival trigger.
* **DIS-029** says *"All four respond to WWOX loss in that system"*. Measured on the panels:
  * nothing differs at early passage;
  * SA-β-gal *falls* with loss (about 41 % vs 12 % at late passage);
  * p27 mRNA does not respond at either passage, and only p27 protein falls (Supp Fig 6).

  "Knockout plus knockdown" holds: shRNA in HEK293T and in primary human skin fibroblasts (S3–S4).

**FIND-X surfaces:** the body (searched by term), all seven captions, Figs 1–2 as images, and Supp
Table 1 with Figs S1–S9. **Not read:** Figure 6, whose inspection was halted by a model safety
classifier; Figures 3, 4, 5 and 7 as images. Figure 6 carries the microsatellite and NAC panels. Any
statement about those panels in DIS-029 therefore remains **unverified on the panel**.

## Change class

**MINOR.** These are research-layer dismissal entries, not `consolidated baseline` claims. Neither verdict
changes.

## Ordering

Receipt `FTR-20261004-37897534-02` (`scratchpad/receipts_pending_w13/sciC_37897534_1.json`) must be
recorded first.

## Op list — `dismissal_ledger_current.md` (record-scoped; dry runs EXECUTED, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "DIS-028",
  "old": "It says γ-H2AX cannot serve as the instrument.",
  "new": "It says γ-H2AX cannot serve as the instrument. [Wave 13 panel reading of PMID 37897534, Figure 1d, hand readings: the loss-side rise is measured against the heterozygote, not wild type; it is not significant at early passage (about 4.5 versus 7.5 percent positive cells) and reaches significance only after 20-30 serial passages (about 20.5 versus 35.5 percent), where passage alone has already raised the heterozygote about 4.6-fold. No surface read carries a wild-type gamma-H2AX arm or a WWOX re-expression arm, so this paper cannot meet the revival trigger. Figure 6 of that paper was not read (classifier halt). `CC-20261004W13-C-SENESCENCE-PANELS-01`.]"
 },
 {
  "op": "replace-within",
  "id": "DIS-029",
  "old": "All four respond to WWOX loss in that system, and the perturbation is genuine (knockout plus knockdown).",
  "new": "All four respond to WWOX loss in that system, and the perturbation is genuine (knockout plus knockdown). [Corrected 2026-10-04 by the wave 13 panel reading (`CC-20261004W13-C-SENESCENCE-PANELS-01`): the responses are late-passage only — none of SA-β-gal, p16, p21 or γH2AX differs at early passage (Figures 1d, 2b-d); SA-β-gal FALLS with WWOX loss (about 41 versus 12 percent, senescence escape); p27 mRNA does not respond at either passage and only p27 protein falls (Supplementary Figure 6); the knockdown arm is shRNA in HEK293T and primary human skin fibroblasts (Supplementary Figures S3-S4).]"
 }
]
```

Dry runs: `record_scoped_edit.py replace-within --file disease-models/wwox/research/dismissal_ledger_current.md`
→ `scope 'DIS-028': span 62554→64632` and `scope 'DIS-029': span 64632→65954`, both
`DRY RUN — nothing written; 1 op(s)`, at commit `b07016a0`.

## Registry records for this PMID

None owed. The PMID is already landed in the research layer, and no new PAPER/LIT records are created by
a re-read (rule 35).

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The γH2AX comparison is against the heterozygote and is quantified in a separate panel | Immunofluorescent staining of γH2AX (red) in Wwox+/− and Wwox−/− MEFs at early- and late-passages. | PMID 37897534, Figure 1d caption, `files/fulltext/PMID37897534_Cheng2023_PMC.xml`
2. The senescence stain is compared between heterozygote and null at two passage stages | The percentages of SA-β-gal-positive senescent MEFs are shown in the right panel. | PMID 37897534, Figure 2b caption, same artefact
3. p27 mRNA does not differ | We determined comparable p27Kip1 mRNA levels among all groups of MEFs | PMID 37897534, Results, same artefact
4. The knockdown arm is in human HEK293T cells | Fig. S3 WWOX-knockdown decreases senescence induction in HEK293T cells. | PMID 37897534, Supplementary Figure S3 legend, `files/fulltext/PMID37897534_assets/18_2023_4950_MOESM1_ESM_pdftotext.txt`
5. The knockdown arm also covers primary human skin fibroblasts | Fig. S4 WWOX-knockdown decreases senescence induction in human skin | PMID 37897534, Supplementary Figure S4 legend, same artefact
