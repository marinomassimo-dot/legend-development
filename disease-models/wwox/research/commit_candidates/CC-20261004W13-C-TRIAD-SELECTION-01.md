# COMMIT CANDIDATE — CC-20261004W13-C-TRIAD-SELECTION-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 13 2026-10-04, branch `task/sci-C-20261004w13`.
**context_policy:** `QUESTION_DRIVEN` (DIS-026 was held before the surfaces were opened).
**Not medical advice.**

## Target

`disease-models/wwox/research/dismissal_ledger_current.md` · `DIS-026`. The premise wording is
corrected. The rejection **stands**.

## What is wrong or missing now

DIS-026's central negative is that the study has no perturbation and no protein measurement. It was
written with the figure panels and supplement unread. The wave 13 FIND-X search tested it and **it
survives**. Surfaces searched:

* the body, by term: siRNA, shRNA, knockdown, silencing, overexpress, transfect, rescue, western,
  immunohistochemistry, Protein Atlas, protein level, CRISPR. The only hits are in background prose and
  references.
* all ten figure captions, with Figures 8 and 9 inspected as images. Figure 8's "spatial expression" is
  a UMAP of bulk tumour samples, not tissue and not protein.
* Tables 1–3, read cell-wise.
* Table S1, a literature table that never names WWOX.
* Supplementary Files S1 and S2, which are gene-membership lists.

**Unavailable:** the Figure S1 and S2 TIFFs were not rendered. Their captions describe transcript-level
profiling.

One premise phrase is imprecise: *"the three genes were then ranked by Spearman correlation with WWOX
transcript abundance (|R| = 0.42–0.44)"*. The coefficients are correct (Table 3: GCSH 0.43, PLEK2 −0.44,
RRM2 −0.42), and so is Spearman. But the source selected the three on **four criteria together** — AUC,
DFS, correlation with WWOX and UMAP clarity — and three other top genes correlate more strongly with
WWOX: RNF141 0.58, COL3A1 −0.51, RXRG 0.45. "Ranked by correlation" understates how little the
triad's selection rests on WWOX.

## Change class

**MINOR.** Research-layer dismissal entry; the verdict is unchanged.

## Ordering

Receipt `FTR-20261004-34204789-02` (`scratchpad/receipts_pending_w13/sciC_34204789_1.json`) first.

## Op list — `dismissal_ledger_current.md` (record-scoped; dry run EXECUTED, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "DIS-026",
  "old": "and the three genes were then ranked by **Spearman correlation with WWOX transcript abundance** (|R| = 0.42–0.44).",
  "new": "and the three genes were then ranked by **Spearman correlation with WWOX transcript abundance** (|R| = 0.42–0.44). [Corrected 2026-10-04 by the wave 13 reading (`CC-20261004W13-C-TRIAD-SELECTION-01`): the three were SELECTED on four criteria together — AUC, DFS, correlation with WWOX and UMAP clarity — not ranked by correlation; in Table 3 (read cell-wise) RNF141 (R = 0.58), COL3A1 (R = −0.51) and RXRG (R = 0.45) correlate with WWOX more strongly than any of them; GCSH correlates positively, PLEK2 and RRM2 negatively. The FIND-X search over body, ten figure captions, Figures 8-9 as images, Tables 1-3 and the supplement (Table S1, Files S1-S2) found no perturbation and no protein measurement; the supplementary TIFFs were not rendered.]"
 }
]
```

Dry run: `record_scoped_edit.py replace-within --file disease-models/wwox/research/dismissal_ledger_current.md
--id DIS-026` → `scope 'DIS-026': span 58868→60621`, `DRY RUN — nothing written; 1 op(s)`, at commit
`b07016a0`.

## Registry records for this PMID

None owed: this is a re-read of a PMID already landed (rule 35).

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The triad was selected on four criteria, of which correlation with WWOX is one | The selection of three the most relevant genes was based on their predictive value (AUC), effect on survival (DFS), correlation with WWOX, and transparency of expression difference across UMAP dimensions. | PMID 34204789, Results, `files/fulltext/PMID34204789_Kaluzinska2021_PMC.xml`
2. The correlation method is Spearman's rank coefficient computed in a web platform | was used to correlate the top genes with WWOX using Spearman’s rank correlation coefficient. | PMID 34204789, Methods 5.8, same artefact
3. The directions of the triad's correlations with WWOX differ | each of the three genes significantly correlated with WWOX (GCSH positively, PLEK2 and RRM2 negatively) as shown in Table 3. | PMID 34204789, Results, same artefact
4. The authors themselves leave the biomarker use unconfirmed | usefulness of PLEK2, RRM2, and GCSH as diagnostic or predictive biomarkers is yet to be confirmed | PMID 34204789, Discussion/Conclusions, same artefact

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 4 triples — 3 SUPPORTED, 1 NOT_SUPPORTED_AS_LABELLED
**What landed, and what the audit changed:** The adverse verdict: the authors' *«yet to be confirmed»* caveat covers diagnostic and predictive use only, while they assert prognostic and therapeutic status in the same sections — landed in the corrected form. The audit also reconstructed the full denominator chain and named the four steps that are judgement-based or unstated, including that three non-selected genes correlate more strongly with WWOX than any member of the final three.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
