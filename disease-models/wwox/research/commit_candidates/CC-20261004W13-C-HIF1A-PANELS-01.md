# COMMIT CANDIDATE — CC-20261004W13-C-HIF1A-PANELS-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 13 2026-10-04, branch `task/sci-C-20261004w13`.
**context_policy:** `QUESTION_DRIVEN` (CLAIM 009 and DL-MECH-020 were held before the panels were opened).
**Not medical advice.**

## Target

1. `disease-models/wwox/registries/claim_registry_current.md` · `CLAIM 009` (`in observation`,
   INFERENZA) — a source-scope sentence is added after the Summary.
2. `disease-models/wwox/research/discovery_ledger_current.md` · `DL-MECH-020` — a bracketed panel
   reading is appended to its 2026-09-21 update.

## What is wrong or missing now

PMID 35328751 was previously read with its figures as captions only and its supplement `unavailable`.
Wave 13 acquired twelve figures and the supplementary ZIP from the PMC OA bucket. It inspected Figures
5–6 as images and read the S1–S6 captions.

* **CLAIM 009** names "Baryła et al. 2022" first among its sources, under a summary of "ROS increase,
  energetic inefficiency and mitochondrial quality-control stress". On every surface searched — body by
  term, twelve captions, Figs 5–6 as images, S1–S6 captions — this paper measures **no ROS, no ATP, no
  respiration, no membrane potential and no mitochondrial-QC endpoint**. Its oxidative-arm measurements
  are PDH and citrate synthase activity, and **neither changes** with WWOX loss (Fig 5b, 5e). What it
  supports is a glycolytic shift: lactate is higher in all four conditions (Fig 5d). The claim is not
  `consolidated baseline`, so this is MINOR, but the source's scope belongs in the record.
* **DL-MECH-020**'s update says the cytoplasmic HIF1α protein "scende (~2×, p<0.01)". The text reports
  the decrease in two of four conditions. In Figure 6a the knockout bar equals control in normoxia
  hyperglycemia and is above control in hypoxia hyperglycemia. One repetition is shown. The panel also
  confirms that PDH activity is unchanged, so the PDK↑ ⊣ PDH step has an mRNA and **no measured
  enzymatic consequence**. One Results sentence mislabels the PDH assay as "PDK".
* **Not read:** the supplementary TIFFs and ten of the twelve main figures as images.

## Change class

**MINOR.** Neither target is `consolidated baseline`; no status changes.

## Ordering

Receipt `FTR-20261004-35328751-03` (`scratchpad/receipts_pending_w13/sciC_35328751_1.json`) first.

## Op list (record-scoped; dry runs EXECUTED, nothing written)

```json
[
 {
  "file": "disease-models/wwox/registries/claim_registry_current.md",
  "op": "replace-within",
  "id": "CLAIM 009",
  "old": "Baryła 2025 rafforza il framework HIF1A/glicolisi.",
  "new": "Baryła 2025 rafforza il framework HIF1A/glicolisi. **Source scope (wave 13, 2026-10-04, `CC-20261004W13-C-HIF1A-PANELS-01`):** Baryła 2022 (PMID 35328751), read with its twelve figures and six supplementary figures, measures in one immortalised human skin fibroblast line a glycolytic shift under WWOX depletion (lactate higher in all four oxygen × glucose conditions) and finds the oxidative arm NOT changed by WWOX loss (pyruvate dehydrogenase and citrate synthase activity, Figure 5b and 5e); it measures no ROS, no ATP, no respiration, no membrane potential and no mitochondrial quality-control endpoint on any surface. It supports the glycolysis component of this claim only, not its ROS, energetic-inefficiency or mitochondrial-quality-control components."
 },
 {
  "file": "disease-models/wwox/research/discovery_ledger_current.md",
  "op": "replace-within",
  "id": "DL-MECH-020",
  "old": "e la proteina HIF1α **citoplasmatica scende** (~2×, p<0.01).",
  "new": "e la proteina HIF1α **citoplasmatica scende** (~2×, p<0.01). [Wave 13 panel reading, 2026-10-04 (`CC-20261004W13-C-HIF1A-PANELS-01`): the cytoplasmic decrease is condition-specific — Results § 2.6.1 reports it in normoxia normoglycemia (2-fold, p < 0.01) and hypoxia normoglycemia (nearly 2-fold, p < 0.001) only; in Figure 6a, hand readings, the knockout bar is about equal to control in normoxia hyperglycemia and higher than control in hypoxia hyperglycemia (about 2.45 versus 2.1), and the text states \"One repetition is shown\". Figure 5b: pyruvate dehydrogenase activity shows no knockout-versus-control difference in any of the four conditions (the one bracket is a hyperglycemia effect within control), and one Results sentence calls this activity \"pyruvate dehydrogenase kinase (PDK)\", a mislabel. No PDK protein, no ROS, no ATP and no respiration measurement appears on any surface, supplement included (Figures S1-S6 are the overexpression arm).]"
 }
]
```

Dry runs at commit `b07016a0`:
* `CLAIM 009` → `scope 'CLAIM 009': span 64259→67926`, `DRY RUN — nothing written; 1 op(s)`.
* `DL-MECH-020` → `scope 'DL-MECH-020': span 148548→159350`, `DRY RUN — nothing written; 1 op(s)`.

Each `old` string occurs once in its file.

## Registry records for this PMID

None owed (`PAPER 023` exists).

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The cytoplasmic HIF1α decrease is reported for two of four conditions | the expression of HIF1α protein was significantly decreased in 1BR.3.N WWOX KO in comparison to CONTR in normoxia normoglycemia (2-fold; p < 0.01) and hypoxia normoglycemia (nearly 2-fold; p < 0.001) in cytoplasm fraction | PMID 35328751, Results 2.6.1, `files/fulltext/PMID35328751_Baryla2022_PMC.xml`
2. The blot shown is a single repetition | One repetition is shown in the Figure 6. | PMID 35328751, Results 2.6.1, same artefact
3. Nuclear HIF1α is not changed by WWOX loss | We didn’t observed WWOX influence on HIF1α protein in nuclear fraction. | PMID 35328751, Results 2.6.1, same artefact
4. The text names the unchanged activity as PDK although the assay is pyruvate dehydrogenase | while the activities of pyruvate dehydrogenase kinase (PDK) and citrate synthase (CS) were not changed | PMID 35328751, Results, enzyme-activity section, same artefact
5. The supplement is the overexpression arm | Figure S4: WWOX and HIF1α western blot analysis of cytoplasmic (a) and nuclear (b) fractions of WT | PMID 35328751, Supplementary figures captions, `files/fulltext/PMID35328751_assets/s001/Supplementary_figures_captions_pdftotext.txt`
