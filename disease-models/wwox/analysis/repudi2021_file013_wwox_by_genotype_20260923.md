# Repudi 2021 Supplementary File013 — what the pooled `Wwox log2FC ≈ −3.14` hides

**SCIENTIST-B · 2026-09-23 · READ-ONLY toward every canonical file and every ledger. No commit candidate, no receipt, no registry edit, no `*_current.md` touched.**

🔴 **Not medical advice. Mouse transcript data only. No therapeutic interpretation is drawn here.**

Source artefact on disk: `files/fulltext/PMID33914858_Repudi2021_suppl_File013.xlsx` — Repudi S, *et al.* *Brain* 2021;144(10):3061–3077, PMID [33914858](https://pubmed.ncbi.nlm.nih.gov/33914858/), DOI [10.1093/brain/awab174](https://doi.org/10.1093/brain/awab174). Genotype nomenclature cross-checked against `files/fulltext/PMID33914858_Repudi2021_OUP.html` (same paper).

---

## 1 · The single sheet and its EXACT headers

One sheet only: **`KO_WT_7_vs_7_unBatch`** — 17,042 data rows × **33 columns** (not 30).

Verbatim, in file order:

```
ensg | symbol | EntrezID | pvalue | padj | log2FoldChange | l2fcShrink | description | type |
chr | start | end | strand | baseMean |
KO1_Hippo_NrmlCount | KO2_Hippo_NrmlCount |
WT1_Hippo_NrmlCount | WT2_Hippo_NrmlCount | WT3_Hippo_NrmlCount |
N-KO1_hippo_NrmlCount | N-KO2_Hippo_NrmlCount |
N-Crtl1_Hippo_NrmlCount | N-Ctrl2_Hippo_NrmlCount |
S-KO1_Hippo_NrmlCount | S-KO2_Hippo_NrmlCount | S-KO3_Hippo_NrmlCount |
S-Ctrl1_Hippo_NrmlCount | S-Ctrl2_Hippo_NrmlCount |
lfcSE | stat | ENStID | RefSeqID | UCSCID
```

**14 columns end in `NrmlCount`** — exactly the 7 v 7. Typos are reproduced as printed: `N-Crtl1` (transposed), lower-case `hippo` in `N-KO1`, and `Crtl`/`Ctrl` inconsistent between the two N- control columns.

### 1.1 · How each column was mapped to a genotype — and the honest limit

🔴 **No header states a genotype.** Each header states only a *prefix* + index. The prefix→genotype mapping is **NOT in the sheet**; it was taken from the paper body, quoted:

> *"we conditionally generated mouse models harbouring a Wwox deletion in either neural stem and progenitors (using Nestin-Cre; **N-KO**), mature neurons (Synaspin I-Cre; **S-KO**), oligodendrocytes (Olig2-Cre; O-KO) or astrocytes (GFAP-Cre; G-KO), and studied their phenotypes … together with our previously described **Wwox-null** mice."*

| Header prefix | Genotype | Basis |
|---|---|---|
| `KO1`, `KO2` | constitutive **`Wwox`-null** (no Cre prefix; the only remaining mutant line in the paper) | paper body; **inferred, not printed in the sheet** |
| `WT1–3` | wild-type | header |
| `N-KO1/2` · `N-Crtl1`/`N-Ctrl2` | **Nestin-Cre** conditional KO + its littermate controls | paper body |
| `S-KO1/2/3` · `S-Ctrl1/2` | **Synapsin I-Cre** conditional KO + its littermate controls | paper body |

🟡 **The `KO`/`WT` prefix pair is the one inference.** It is unmarked in the sheet and is read as the constitutive null because that is the only non-conditional mutant the paper carries and because it is the only prefix without a Cre letter. **UNASSIGNABLE columns: none** — all 14 map, but the `KO`/`WT` pair carries lower mapping confidence than the `N-`/`S-` pairs.

🔴 **Strain-background hazard, printed in the Methods and not visible in the sheet:** the null line *"maintained in an **FVB** background"*, the conditional lines are B6/`Wwox^flox/flox`. The sheet is explicitly **`unBatch`** — un-batch-corrected. Cross-cohort ratios are therefore confounded.

---

## 2 · Positive controls FIRST — proving the columns are read in the right orientation

| Gene | baseMean | sheet `log2FoldChange` | sheet `padj` | Read |
|---|---|---|---|---|
| **Hprt** | 1,911.19 | **−0.10** | 0.482 (ns) | 🟢 flat, as a housekeeper must be |
| **Sdha** | 8,097.51 | **+0.01** | 0.968 (ns) | 🟢 flat |
| **Actb** | 68,063.13 | +0.76 | 4.27E−4 | 🟡 **not flat** |
| **Gapdh** | 46,333.98 | +0.68 | 8.06E−3 | 🟡 **not flat** |
| **Tbp** | 822.00 | +0.85 | 2.50E−3 | 🟡 **not flat** |

Magnitudes are also right: `Actb` > `Gapdh` ≫ `Sdha` > `Hprt` > `Tbp`, spanning 68,000 down to 822 — the expected ordering for hippocampal bulk RNA-seq. `Hprt` per-sample values run 1,490–2,137 across all 14 columns with no group structure. **Orientation and column mapping are corroborated.**

🔴 **But the controls also carry a warning.** `Actb`/`Gapdh`/`Tbp` are ~1.8–2.6× *up* in `N-KO` and `S-KO` versus their own controls while flat in `null KO` vs `WT` (`Gapdh` ratio 1.05, `Tbp` 1.02). That is a library-composition / cohort effect, consistent with an un-batch-corrected matrix. It does **not** invalidate a ~10× depletion, but it forbids treating small between-genotype `Wwox` differences as exact.

---

## 3 · The `Wwox` row — all 14 samples, before pooling

Sheet row 2. `ENSMUSG00000004637` · `Wwox` · EntrezID 80707 · `chr8:114,439,655–115,352,708` (+).

| Genotype group | n | Per-sample normalized counts | Mean | Median | SD | CV | Range |
|---|---|---|---|---|---|---|---|
| **`Wwox`-null (`KO`)** | **2** | 28.29 · 32.45 | 30.37 | 30.37 | 2.94 | 9.7 % | 4.16 |
| **WT** | **3** | 294.42 · 307.32 · 303.32 | **301.69** | 303.32 | 6.60 | 2.2 % | 12.90 |
| **Nestin-Cre KO (`N-KO`)** | **2** | **5.06** · **25.52** | 15.29 | 15.29 | 14.47 | 🔴 **94.6 %** | 20.46 |
| **N-control** | **2** | 219.76 · 232.13 | 225.94 | 225.94 | 8.75 | 3.9 % | 12.37 |
| **Synapsin-Cre KO (`S-KO`)** | **3** | 32.52 · 33.04 · 49.01 | 38.19 | 33.04 | 9.37 | 24.5 % | 16.49 |
| **S-control** | **2** | 195.23 · 212.87 | 204.05 | 204.05 | 12.47 | 6.1 % | 17.64 |

🔴 **n is as observed in the headers, not assumed:** 2 / 3 / 2 / 2 / 3 / 2. The mutant arm (2+2+3 = 7) and the control arm (3+2+2 = 7) are the "7 v 7".

### 3.1 · Published DESeq2 statistics on that row — and whether they reproduce

| Field | Value in sheet |
|---|---|
| `baseMean` | **140.78** |
| `log2FoldChange` | **−3.14** |
| `l2fcShrink` | −3.09 |
| `lfcSE` | 0.27 |
| `stat` | −11.82 |
| `pvalue` | 2.90E−32 |
| `padj` | **2.51E−28** |

✅ **Reproduces the paper's ≈ −3.14 exactly** — it is printed in the sheet, not merely implied. Two independent internal checks:

- Pooled mean of mutants **29.41** ÷ pooled mean of controls **252.15** = 0.1167 → **log₂ = −3.10**, against the fitted −3.14. A 0.04-unit gap is the expected difference between a ratio-of-means and a DESeq2 negative-binomial GLM fit.
- `log2FoldChange / lfcSE` = −3.14 / 0.27 = −11.63, against the printed `stat` −11.82 — consistent to the printed rounding of `log2FoldChange`.
- `baseMean` 140.78 vs the mean of all 14 normalized values (140.78) — 🟢 identical.

---

## 4 · VERDICT — what the pooling hides

**GRADED DEPLETION, plus a residual floor that is not zero in any genotype.** Recomputing each mutant against **its own control arm**:

| Contrast | Ratio | Residual `Wwox` | log₂FC |
|---|---|---|---|
| Nestin-Cre KO vs N-control | 0.0677 | **6.8 %** | **−3.89** |
| `Wwox`-null vs WT | 0.1007 | **10.1 %** | **−3.31** |
| Synapsin-Cre KO vs S-control | 0.1872 | **18.7 %** | **−2.42** |
| *(pooled, as published)* | 0.1167 | 11.7 % | *−3.14* |

🎯 **Quantified: the three per-genotype values span 1.47 log₂ units — a 2.8-fold spread in effect size — and the single published −3.14 sits in the middle of a range it represents for none of them.** The Synapsin-Cre model is **0.72 log₂ units (1.6×) shallower** than the pooled figure; the Nestin-Cre model is 0.75 log₂ units deeper.

**Two further things the pooled number conceals:**

1. 🔴 **No genotype reaches zero. The floor is 6.8–18.7 % of control, and in the constitutive null it is 10.1 %.** For the two **conditional** lines the Methods explain it directly: the floxed allele carries *"two loxp sites (`Wwox flox/flox`) flanking **exon 1** of the `Wwox` genomic locus"* — **exon 1 only**, verified verbatim in the OUP HTML by the Orchestrator.
   ⚠️ **ORCHESTRATOR CORRECTION, 2026-09-23 — this explanation does NOT automatically extend to the constitutive null, and an earlier draft of this paragraph let it.** The null is a **different allele from a different line**: *"The generation of `Wwox`-null mice has been previously documented[19]; and these mice were maintained in an **FVB** background"*, whereas the conditional lines are `Wwox flox/flox` on a B6;129sv background. **This paper does not state which exons the null allele removes.** So the null's 10.1 % floor is *unexplained by anything in this paper* — it may share the gene-level-counting cause, or it may not. 🔴 **Treat the null's residual as UNEXPLAINED, and the conditional lines' residual as plausibly-but-not-provenly a counting artefact.** The correction makes the caveat narrower and the unknown larger, which is the honest direction. The locus spans ~913 kb; exons 2–9 remain intact in the genome and any read falling on them is still summed into a gene-level count. Competing explanations, none discriminated by this table: (a) residual exon-2–9 transcription counted at gene level; (b) incomplete Cre recombination; (c) non-recombined cell types. **The discriminating measurement is exon-level coverage across `Wwox` exon 1 versus exons 2–9 — which requires the alignments, and is not in this or any supplementary table on disk** (File012 is the S-KO cortex+hippocampus 6 v 6 matrix, same gene-level format).
2. 🔴 **The apparent ordering is not statistically secure.** `N-KO` is "deepest" only because of `N-KO1 = 5.06`; its partner `N-KO2 = 25.52` is indistinguishable from the null pair (28.29, 32.45). At **n = 2 with CV 94.6 %**, the defensible statement is **`Wwox`-null ≈ Nestin-Cre KO < Synapsin-Cre KO**, not a three-step gradient.

**Is the shallowest group biologically expected? Yes — and that is why it is not a discovery.** Synapsin I-Cre recombines in mature neurons only, so glia, endothelium and interneurons in a bulk hippocampal homogenate retain both alleles; Nestin-Cre recombines from ~E10.5 across the whole neural lineage. A shallower bulk depletion under a narrower Cre is the predicted result of cell-type composition, not of allele biology.

### 4.1 · Classification

**`USEFUL DATASET DISAGGREGATION`.** The three-way test for a new biological hypothesis is **not** met: (i) the genotype separation is real and measurable, but (ii) it changes no existing *biological* interpretation — the ordering is what the Cre drivers predict — and (iii) the one discriminating follow-up that would matter (exon-level coverage) is not runnable from any artefact LEGEND holds.

**What it does change is methodological, and that is recorded rather than promoted:**

- 🔴 Any future statement of the form *"`Wwox` transcript is reduced ~89 % in Repudi's mutants"* is **wrong for every individual genotype** and right for none: the true per-model figures are 93.2 %, 89.9 % and 81.3 %.
- 🔴 **This dataset must not be used as a residual-function / dose–response model for hypomorphic human alleles.** The 6.8–18.7 % residual is most probably a gene-level counting artefact of an exon-1-only deletion, not surviving WWOX function. Reading it as partial activity would import a quantification artefact into allele-severity reasoning.

---

## 5 · Bounds — stated, not implied

1. 🔴 **Transcript, not protein.** These are normalized RNA-seq counts. The paper's own protein work is separate and is not read here. An exon-1 deletion removes the start codon, so transcript retention and protein loss are fully compatible.
2. 🔴 **n ≤ 3 per genotype** (2, 3, 2, 2, 3, 2). No group supports a dispersion estimate worth quoting as a confidence interval; SD on n = 2 is a range in disguise.
3. 🔴 **A conditional-KO floor reflects Cre efficiency and cell-type composition, not allele biology.** Bulk hippocampus is a mixture; the number measures how much of that mixture the driver reached.
4. 🟡 **Un-batch-corrected, mixed strain background** (FVB null line vs B6 conditional lines), with three of five housekeepers drifting ~2× between cohorts. Between-genotype differences smaller than ~1 log₂ unit should not be treated as exact.
5. 🟡 **Hippocampus only, P17 only.** One region, one age.
6. 🟡 **Prefix→genotype mapping for `KO`/`WT` is inferred from the paper body**, not printed in the sheet (§1.1).

---

## 6 · Reproducibility

This deployment has no `openpyxl` and no `pandas`. The sheet was read with a stdlib-only `zipfile` + `xml.etree` reader (`sharedStrings.xml` + `xl/worksheets/*.xml`). Every number above is a cell value or an arithmetic function of cell values; nothing is transcribed from the paper's prose except the genotype nomenclature and the floxed-allele description in §1.1 and §4, both quoted.

