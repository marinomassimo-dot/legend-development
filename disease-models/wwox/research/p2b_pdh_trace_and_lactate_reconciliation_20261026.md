# P2b: tracing «PDH activity unchanged», and reconciling the lactate statistics (2026-10-26, scientist-a)

Class-level, public, de-identified. Nothing here is medical advice. Both subjects are non-human or
non-neural systems (a human skin fibroblast line; a *Drosophila* amyloid model) and neither is
WWOX-DEE evidence.

## 1. «PDH activity unchanged» (the `HYP-20260709-01` bullet)

**Verdict: the locator is traced; the statement is supported with four qualifiers the bullet does not carry,
and one of its two cited receipts is not the source of it.**

### Where the sentence comes from

| Item | Finding |
|---|---|
| Source paper | `PMID 35328751` only (Baryla 2022, Int J Mol Sci; primary research, immortalised human skin fibroblast line 1BR.3.N). |
| `FTR-20260921-35328751-01` | Carries the sentence in prose (`evidence_basis`: "PDH activity unchanged in all four conditions") with no persisted locator. |
| `FTR-20260921-36271927-01` | The review (`PMID 36271927`). Its text reports PDK1 upregulation and describes PDK1 as the PDH inactivator; it reports **no PDH activity measurement**. It is not a source of this sentence. |
| Persisted locators | Manifest `PMID35328751.json` entries 7 (Fig 5b, hand reading of the panel, receipt `FTR-20261004-35328751-03`), 8 (the Results sentence that mislabels the Fig 5b activity as «pyruvate dehydrogenase kinase (PDK)») and 3 (citrate synthase, Discussion). |

### What was measured (panel, table, method, model, comparison)

- **Quantity:** enzyme **activity** of pyruvate dehydrogenase, a colorimetric kit (Methods 4.10) on
  **lysates / cell homogenate** (Results 2.5), unit mU/mL; Fig 5b. Citrate synthase activity: Fig 5e, Methods 4.11.
- **Model and dose:** one line; CRISPR/Cas9 polyclonal "KO" that is a partial depletion (WWOX mRNA about 3-fold lower, protein about
  8.5-fold lower, Results 2.1); comparator is the empty-vector/scrambled control; 48 h.
- **Conditions:** normoxia or hypoxia crossed with normoglycaemia or hyperglycaemia. Statistics: ANOVA with Tukey post-hoc, mean ± SEM.
  **No n or replicate count is stated in the text or the Fig 5 caption.**
- **Comparison:** knockout versus control within each condition. Results text, per condition: NN «activities of pyruvate dehydrogenase
  kinase (PDK) [sic: the Fig 5b quantity is PDH] and citrate synthase … were not changed»; NH «did not contribute to the changes in
  hexokinase, pyruvate dehydrogenase, and citrate synthase activity»; HN «We didn't observed any significantly important differences
  in the activity of pyruvate dehydrogenase, lactate dehydrogenase, and citrate synthase»; HH «WWOX silencing exhibited no significant
  effect on enzymes activity». So three conditions name PDH (one under the mislabel) and the fourth is covered by a blanket sentence.
- **Panel (re-inspected 2026-10-26, hand reading, approximate):** Fig 5b KO versus control about 3.0 vs 2.3 (NN), 6.1 vs 6.7 (NH),
  7.2 vs 4.8 (HN), 5.5 vs 5.6 (HH) mU/mL; error bars are large (NN and HN KO bars overlap their controls only because the SEM is wide); the single
  bracket in the panel joins two control bars (a glucose effect). No knockout-versus-control bracket.

### Distinctions the bullet needs

| Layer | Status in this paper |
|---|---|
| PDH enzyme **activity** (lysate, kit) | measured; no significant KO-vs-control difference in any condition |
| PDHA **expression** (mRNA, Fig 4l) | measured; no KO change reported in the Results text for NN/NH; PDHA is up 3-fold with overexpression in NH (S2) |
| PDK **expression** | mRNA only (up in NN, p < 0.05; reported up in HH by the Discussion); **no PDK protein, no PDK activity** |
| PDH **phosphorylation** (inhibitory state) | not measured; Methods 4.10 do not say whether the homogenate preserved it |
| **Flux** (pyruvate to acetyl-CoA, OCR, ECAR, Seahorse), pyruvate, acetyl-CoA | not measured |
| **Metabolites** | medium lactate (up in all four conditions, Fig 5d); glucose uptake (sign flips) |

### Qualifiers owed

1. «Unchanged» means «no significant difference at ANOVA with Tukey, n not stated, SEM wide», not demonstrated equivalence; two of four
   panels (NN, HN) show numerically higher KO bars.
2. **HH is not a verified depleted contrast:** WWOX mRNA is significantly lower only in NN, NH and HN (Results 2.4; also
   `held_wave_20261019_scientist-c.md` point 2). «All four conditions» therefore contains one condition without a shown depletion.
3. The assay reports total PDH activity in a homogenate; it cannot see an inhibitory phosphorylation or an in-cell flux change, so it does
   not refute a PDK-mediated block either. It also does not support one.
4. The overexpression arm (Results 2.5, Fig S3, text only here) reports PDH activity **lower** under overexpression in both hypoxic
   conditions (p < 0.001), not under loss; Fig S3b was not re-opened.

### Limit

I did not find a source that the two cited receipts' evidence reaches beyond this primary. What stays untraced: the sentence-level
quote in `FTR-20260921-35328751-01` (still prose, receipt not altered), the replicate number, and Fig S3b. This is a limit on the
persisted trace, not a refutation of the statement or of the HIF1A-PDK-PDH hypothesis.

### Wording candidate for the bullet

See `commit_candidates/CC-20261026-SCIENTIST-A-P2B-01.md`.

## 2. Lactate statistics in Lucas-Clarke 2026 (`PMID 42909904`, `PAPER 567`)

Source: Results «Wwox knockdown in the presence of Abeta42 increases lactate concentrations via Atf4», Supplementary Table 4 L-lactate row
(manifest entries 37, 38, 39, 40), Fig 5A-C (entries 43). Text layer read with `pdftotext` without `-layout`; Fig 5C re-opened as the
embedded raster of page 12.

| Term (two-way ANOVA, top 200 features by variance, 10% FDR) | F | padj | Significant at the paper's 10% threshold? | log2 |
|---|---|---|---|---|
| Wwox knockdown **main effect** | 7.524 | 0.0636 | yes, marginally (Fig 5A labels L-lactate just above the dotted line) | +0.68 |
| Abeta42 **main effect** | 27.846 | 0.0050 | yes (Fig 5B) | +0.97 |
| Wwox knockdown × Abeta42 **interaction** | 23.606 | 0.0174 | yes; the only metabolite with a significant interaction | +1.30 (knockdown effect in the Abeta42 background); -0.43 in the LacZ background |

Fig 5C (mean ± SEM, five points per bar, no per-cell significance mark; bar heights are my hand reading): LacZ control RNAi about 4.9e5,
LacZ + knockdown about 3.6e5, Abeta42 control RNAi about 4.8e5, Abeta42 + knockdown about 1.2e6.

**Reconciliation.** All three terms pass the paper's own threshold, so the sentence «only the Abeta42 main effect is significant» is wrong,
and it contradicts the same audit's row a2 (which reports the interaction). What the audit rightly caught stands: the main effect
averages both RNAi backgrounds, and the cell pattern (Abeta42 with control RNAi at the LacZ level; the rise only with knockdown) is the
interaction. The arithmetic is consistent (log2 of 1.2e6/3.6e5, about 1.7, against 0 for the control background gives a mean near
0.9, the reported +0.97). The PDF reports **no simple Abeta42-versus-LacZ test for lactate within the control-RNAi background**, so
«Abeta42 alone raises lactate» is neither shown nor excluded by a test; it is not visible in Fig 5C. (The Ldh half, Abeta42 versus LacZ, +1.11 in
the table and 1.19 in the text, is a transcript contrast and is unaffected.)

Surfaces checked: `PAPER 567` note (states the interaction and both directions; the sentence that the Abeta42 main effect did not raise
lactate refers to the **overexpression** cohort, Supp Table 7, a different experiment, and is correct); dossier `PMID42909904.md`
(lists all three terms); manifest entries 37-40 and 43 (accurate; entry 43 says only that Abeta42 alone does not *visibly* raise lactate
in the panel); E02 and E04 cards (state the interaction; no «only main effect» text). **Affected, and corrected on this branch:**
`biological_needs.md` row C3 (clarifying clause) and an erratum under the audit table that carried the false «only». No manifest entry
changed, so no manifest entry needs a re-audit; the C3 edit and the erratum are verifiable against Supp Table 4 by a reader other than me.
