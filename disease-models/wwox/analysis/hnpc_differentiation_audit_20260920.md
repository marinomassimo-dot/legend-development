# hNPC differentiation audit — PMID 31543760 (Kośla/Bednarek 2019)

**Auditor:** Scientist B · **Date:** 2026-09-20 · **Status:** non-canonical analysis. READ-ONLY toward
`disease-models/wwox/registries/**` and `framework/**`. No commit candidate is produced by this file.

## Header — provenance and read depth

| Field | Value |
|---|---|
| PMID | 31543760 — **verified** via `mcp__PubMed__convert_article_ids` |
| PMCID | **PMC6730490** — verified; the PMCID supplied in the task was correct |
| DOI | [10.3389/fncel.2019.00391](https://doi.org/10.3389/fncel.2019.00391) |
| Title | "The [WWOX] Gene Influences Cellular Pathways in the Neuronal Differentiation of Human Neural Progenitor Cells" |
| Journal / date | *Frontiers in Cellular Neuroscience* 13:391, 2019-08-30 |
| Authors | Kośla K, Płuciennik E, Styczeń-Binkowska E, Nowakowska M, Orzechowska M, **Bednarek AK** — all Dept. of Molecular Carcinogenesis, Medical University of Łódź |
| Licence | CC BY 4.0, `is_open_access: true` (PMC OA subset) |
| **Declared read depth** | **FULL TEXT READ, END TO END** — Introduction, Materials and Methods, Results, Discussion, Conclusion, Data Availability, Author Contributions. Retrieved via `mcp__PubMed__get_full_text_article`, the only permitted route. |
| **Figures** | **NOT INSPECTED — impossible.** All 11 figure panels are present only as stripped captions. Every phenotype below (Western blot silencing efficiency, redox, adhesion, zymography, 3D growth, GSEA plots, STRING networks, PCA) is reported as the authors' *text* states it. No panel was read. |
| **Supplementary data** | **NOT OBTAINABLE.** The extraction strips every supplementary callout to a bare comma or period: *"The detailed results are available as."*, *"High resolution figure with legible gene names available in,"*, *"seefor all involved genes."* **The full differentially-expressed-gene lists, the 14 enriched gene sets, the STRING node table and the PCA loading table all live in supplementary files LEGEND does not hold.** |
| **GEO accession** | **NOT RECOVERABLE.** Stripped: *"deposited in NCBI Gene Expression Omnibus (GEO) Database with accession number."* and *"can be found in NCBI GEO Database,."* The raw CAGE data exists but its accession is not obtainable through this route. |
| Extraction artefact | The extractor deleted the italicised gene symbol **WWOX** throughout. Quotes below are **verbatim as extracted**; where the missing symbol changes readability it is restored in square brackets `[WWOX]` and that insertion is **editorial, not in the source string**. |

---

## Q1 — What system, exactly?

**Answer: a commercial H9-hESC-derived human neural stem cell line, reclassified by the authors themselves as a progenitor; growth-factor withdrawal for 14 days; exactly TWO timepoints (undifferentiated, day-14). Not iPSC, not primary fetal tissue, not an organoid.**

> "The human neural stem cells (hNSC, Thermo Fisher Scientific) are derived from H9 embryonic stem cells (hESC). According to manufacturer description they have the potential to differentiate into neurons, astrocytes and oligodendrocytes." — PMID 31543760, Methods

> "Spontaneous differentiation of the cells was triggered by culturing in medium without the addition of EGF and FGFb growth factors for 14 days." — PMID 31543760, Methods

**Load-bearing self-correction by the authors — the line matters for anything LEGEND might infer about lineage:**

> "Although the supplier claims that the cells are able to differentiate into neurons, astrocytes and oligodendrocytes upon growth factor removal, in our conditions all the cells were found to undergo differentiation into neurons, which was confirmed by immunocytochemistry. All differentiated cells were found to be positive for neuronal markers MAP2 and TUJ1 and negative for astrocytes – GFAP or oligodendrocytes – GalC markers (). This suggests that the cells lose their multipotence and instead of being neural stem cells are rather a neural progenitors (hNPC) and were regarded in this study as such." — PMID 31543760, Methods

Consequence: **this system produced no astrocytes and no oligodendrocytes.** Any myelination or glial question is structurally unanswerable here (see Q3).

Culture geometry is two-armed and the arms dissociate: 2D on thin Geltrex coat, versus 3D in a thick scaffold —

> "For a 3D culture assay, 16,000, 25,000, and 35,000 cells were seeded on a solidified 2 mm layer of growth factor-reduced Geltrex basement membrane matrix (Thermo Fisher Scientific)." — PMID 31543760, Methods

**No gestational age is assignable to any of this.** "Progenitor" here is a culture state, not a developmental date. There is no embryonic day, no gestational week, no in vivo tissue.

---

## Q2 — What was done to WWOX? (does the paper license a causal claim?)

**Answer: stable lentiviral shRNA KNOCKDOWN with a scrambled-shRNA control and Western-blot verification. This IS a perturbation, not correlative profiling across differentiation. It therefore CAN support a causal claim — but a knockdown-level, partial-loss, cell-autonomous, in-vitro one.**

> "The [WWOX] gene was silenced by a shRNA lentiviral delivery system (Santa Cruz Biotechnology). The control cells were transduced with the same type of vector harboring scrambled shRNA sequence instead of targeting investigated gene." — PMID 31543760, Methods

> "The stable transductants were selected with 0.4 μg/ml puromycin. The gene silencing efficiency was assessed with Western blot." — PMID 31543760, Methods

> "After confirmation of [WWOX] gene silencing by Western blot () the hNPC/shWWOX cells and control hNPC/shScrambled were cultured…" — PMID 31543760, Results

**Four limits on the causal reading, all from the text itself:**

1. **The residual-protein level is never stated numerically in the text.** The quantification lives in a figure (densitometry against GAPDH) that cannot be inspected. So "how much WWOX is left" is unknown to this audit. A knockdown is not a null, and WOREE/WWOX-DEE is predominantly a null or near-null genotype.
2. **One shRNA construct, no rescue.** The text describes a single silencing vector and no WWOX re-expression arm. Off-target contribution is not excluded by any experiment reported.
3. **No isogenic patient allele.** No WOREE variant, no truncation, no Q230P, no splice allele. Nothing here is allele-specific.
4. **Cell-autonomous monoculture.** No tissue, no non-cell-autonomous contribution, no migration substrate other than Geltrex.

**Verdict on Q2: causal at the level of "reducing WWOX in a human neural progenitor changes X." Not causal for any statement about human cortical development in vivo.**

---

## Q3 — What changed transcriptionally, and does it touch pathways LEGEND tracks?

Platform is CAGE (5'-end TSS sequencing), analysed with MOIRAI → CAGEr → GSEA against GO BP.

> "It was found that 2282 genes were differentially expressed between hNPC/shScrambled and hNPC/sh[WWOX] (log2 FC > ±1,< 0.05) and 7392 differed between differentiated neurons/shScrambled and neurons/sh[WWOX]." — PMID 31543760, Results

### The gene-set headline, and the threshold that qualifies it

> "Enrichment analysis was performed for 9427 genes between shWWOX and shScrambled, classified as phenotype labels separately for hNPC and neurons through-test with a weighted scoring scheme and a permutation type regarding phenotype. **Significance threshold was set as FDR < 0.25.**" — PMID 31543760, Methods

**FDR < 0.25 is the permissive GSEA default, not a stringent one.** Every gene-set claim in this paper — including the migration claim — carries that threshold. Flag it wherever it is reused.

Top enriched sets in the WWOX-competent cells (Table 1, enrichment scores as printed):

| Gene set (enriched in hNPC with native WWOX) | n | ES |
|---|---|---|
| GO_neural_crest_cell_differentiation | 33 | 0.622 |
| GO_neural_crest_cell_migration | 21 | 0.677 |
| GO_homophilic_cell_adhesion_via_plasma_membrane_adhesion_molecules | 53 | 0.511 |
| GO_cell_cell_adhesion_via_plasma_membrane_adhesion_molecules | 69 | 0.428 |
| GO_negative_regulation_of_axon_extension | 21 | 0.578 |

Note what the top two actually are: **neural CREST**, not cortical neuron. Neural crest is a peripheral/craniofacial lineage. The paper's cortical framing rests on the *further* sets ("regulation of neuron migration") that are named only in passing and whose detail is in the unavailable supplement.

### Pathway-by-pathway against LEGEND's tracked axes

| LEGEND axis | What this paper actually shows | Evidence class |
|---|---|---|
| **Neuronal lineage commitment** | Supported, with a directional detail | GSEA + leading-edge lists |
| **Migration** | Asserted; **no migration assay was performed** | GSEA + gene identity only |
| **Cortical layering** | **NOTHING.** No tissue, no layers, no laminar readout | absent |
| **Wnt** | **NOT in this paper's Results.** Wnt appears only in Introduction/Discussion background and in citations to the authors' *prior GBM* work | **do not cite this paper for Wnt** |
| **MYC** | **Entirely absent** — the string does not occur | absent |
| **GABA / chloride** | **No original data.** One citation to a murine KO study | second-hand |
| **Myelination** | **Structurally impossible** — no oligodendrocytes formed (Q1) | absent |
| **Metabolism / OXPHOS** | One *measured* readout + one *expression programme* — see below | mixed |
| **Cell cycle** | No enriched cell-cycle set; only a phenotypic "did not proliferate" in 3D | phenotype only |

**Lineage commitment — the leading-edge direction is the informative part:**

> "In the hNPC/shScrambled the leading edge subset (considered as the most upregulated and promising genes) included LOXL3, JAG1, SOX21, ERBB4, KITLG, GPM6A, EFNB1, FGF10, NRG1, WWTR1, RUNX2, LAMA5, MSI2, SEMA4D, BCHE, FOXC1, SMAD4, SEMA5A, SEMA5B, SEMA6C, SEMA3A, SEMA6A, SEMA3C, GSK3B, BMP7, SFRP1, SEMA4F, and SEMA4B, whereas the hNPC/sh[WWOX] leading edge subset included HHEX, FGFR2, GBX2, SNAI1, GREM1, MSX2, and MSX1." — PMID 31543760, Results

The WWOX-competent edge is dominated by **semaphorins** (nine SEMA genes — axon guidance / repulsive steering) plus NRG1/ERBB4 and JAG1 (Notch). The knockdown edge is a short, non-neural, mesenchymal/patterning set (SNAI1, MSX1/2, GREM1, GBX2, HHEX). That directional contrast is a real and quotable finding.

**Pathways named in the Results/Discussion — note the absence of Wnt:**

> "Our analysis of the functional networks of the differentially expressed genes revealed that [WWOX] expression in hNPC is associated with transcription regulation of genes of neural differentiation that take part in such pathways as Notch, PI3K kinase, PDGF, Cadherin, Hedgehog, and Endothelin signaling pathway." — PMID 31543760, Discussion

**Cytoskeleton — this is the part PMID 32581702 carried forward:**

> "We showed that [WWOX] silencing in neural progenitor cells significantly changed expression of a large set of genes connected to cytoskeleton organization, e.g., MAP2/4/6, DCLK, NEFM, and NEFL that are engaged in microtubule and neurofilament assembly." — PMID 31543760, Discussion

**Adhesion — two named genes with directions:**

> "The changes in [WWOX] expression influence the levels of a number of pivotal adherence proteins, e.g., CDH2 (expression doubled in hNPC/shScrambled in compare to hNPC/sh[WWOX]) and ITGβ1 (expression lowered twice in hNPC/shScrambled in compare to hNPC/sh[WWOX])." — PMID 31543760, Discussion

I.e. knockdown **lowers CDH2 (N-cadherin) ~2-fold** and **raises ITGB1 ~2-fold** — a coherent switch from cell–cell to cell–matrix adhesion, and consistent with the measured fibronectin-adhesion increase.

**Metabolism — the flux-versus-programme line, drawn explicitly:**

*Measured* (a real assay, but a crude one — resazurin reduction reports cellular/mitochondrial reductive capacity, **not** an OXPHOS flux, not a Seahorse OCR):

> "The mitochondrial metabolic activity was measured using PrestoBlue reagent (resazurin based, Thermo Fisher Scientific)." — PMID 31543760, Methods

> "[WWOX] silencing reduced the mitochondrial redox activity of the cells () and strongly affected their adhesion to ECM proteins." — PMID 31543760, Results

*Programme only* (PCA over a curated MSigDB gene set — **expression, not rate**):

> "The analysis involved 362 genes of several oxidative stress response/antioxidant defense/oxygen species activity connected groups form The Molecular Signatures Database (MSigDB), a collection of annotated gene sets." — PMID 31543760, Methods

> "Examples of genes mostly involved in such differentiation are: Hexokinase 2 (HK2), Pyruvate Dehydrogenase Kinase 1 (PDK1), Lactate Dehydrogenase A (LDHA), Ferredoxin Reductase (FDXA), Cytochrome C (CYCS), Superoxide Dismutase 1 and 2 (SOD1 and SOD2), and Peroxiredoxin 2 (PRDX2)…" — PMID 31543760, Results

**LEGEND's organoid-era rule applies verbatim here: HK2/PDK1/LDHA is a glycolytic *expression* signature, not a measured glycolytic rate. The only measured metabolic datum in this paper is one resazurin reduction assay.** The authors' own conclusion is hedged and should be carried hedged:

> "Therefore, we conclude that [WWOX] might have considerable impact on neurons through modulation of oxygen metabolism and mitochondria functioning." — PMID 31543760, Discussion

### The strongest *functional* result — 3D, and only 3D

> "Most striking was that in 3D culture, the hNPC with silenced [WWOX] remained as isolated, single cells that did not proliferate nor differentiate, while cells with unaltered [WWOX] expression differentiated and exhibited extensive network formation (,). This observation was confirmed in three separate experiments and was not influenced by the seeding density (data not shown). **No such phenomenon was observed when the cells were cultured in 2D as a monolayer** ()." — PMID 31543760, Results

The 2D/3D dissociation is the most useful mechanistic hinge in the paper: **the requirement for WWOX is conditional on a three-dimensional matrix context.** It is also, honestly, a morphological observation scored from images this audit cannot see, with "data not shown" doing work on the seeding-density control.

---

## Q4 — Does it say anything about developmental *timing*?

**Answer: two things, and the batch's abstract-versus-results discipline applies to both.**

### (a) A stage asymmetry in the authors' own data — real, and under-discussed by them

> "Significantly greater numbers of enriched gene sets was found for undifferentiated cells (44 for hNPC/shScrambled and 109 for hNPC/sh[WWOX], FDR < 0.25) than for differentiated neurons (**no gene sets for neurons/shScrambled and four sets in neurons/sh[WWOX]**)." — PMID 31543760, Results

Set against the DEG counts (2282 in progenitors, **7392** in neurons), this is an **internal tension the paper never reconciles**: three times as many individual genes move in the differentiated neurons, yet the coherent, annotatable biological programme collapses from 153 enriched sets to 4. Read conservatively, WWOX loss produces an *organised* programme disruption **at the progenitor stage** and a larger but *incoherent/diffuse* one after differentiation. That is a genuine, if indirect, stage-dependence signal, and it is the paper's best contribution to the batch's life-stage question. It is a gene-set-enrichment argument only — no orthogonal validation.

### (b) A fetal-versus-adult expression datum — and it points the OPPOSITE way to a "prenatal peak"

> "An analysis of NGS data deposited in the RIKEN Fantom5 Project data repository indicates that the level of [WWOX] expression in the human brain varies according to location (). The highest levels are observed in the corpus callosum and medulla oblongata, and the lowest in the postcentral and paracentral gyrus. Moreover, **adults display greater [WWOX] expression in the brain as a whole than 20–33 weeks fetuses, 17.7 TPM RLE (tags per million, relative log expression) vs. 9.2 TPM RLE.**" — PMID 31543760, Results

**Handle this with care. Three caveats, all decisive:**

1. It is **not this paper's experiment** — it is a re-read of the public FANTOM5/Zenbu repository, reported without n, without dispersion, without a test statistic.
2. It is a **bulk whole-brain average** at a single fetal window (20–33 gw) versus "adults." It is cross-sectional across two grossly unmatched groups, not a trajectory.
3. **It does not support a prenatal WWOX expression peak — it argues against one.** Fetal brain WWOX is reported at roughly *half* the adult level. Any LEGEND narrative that wants WOREE severity to track a prenatal WWOX expression maximum cannot recruit this datum; it cuts the other way. What the paper instead implies is that a *lower* fetal baseline may leave the developing brain with less reserve — but the paper does not say that, and LEGEND must not put it in their mouth.

**There is no window, no stage-gating experiment, and no timed intervention anywhere in this paper.**

---

## Q5 — Human data bearing on WOREE, or cancer biology in developmental clothing?

**Answer: genuinely human and genuinely neurodevelopmental in intent — but with a heavy oncology centre of gravity and a demonstrable abstract-over-reach. Call it a hybrid, weighted toward the developmental side.**

**For the developmental reading:** PubMed keywords are `CAGE, SCAR, WOREE, WWOX, neural progenitor cells, neurodegeneration, neuronal differentiation`. WOREE and SCAR12 are named and correctly described in the Introduction, including the allele-class distinction LEGEND already holds:

> "All known patients suffering from SCAR12 carry a homozygous missense mutation in [WWOX] coding region (139C > A or 1114G > C) that causes a partial loss of gene function… The WOREE patients exhibiting more severe neurological disorders harbor nonsense/frameshift mutations and/or robust deletions of whole exons of [WWOX] gene" — PMID 31543760, Introduction

The stated aim is developmental, not oncological:

> "The aim of the present study was to investigate in detail the impact of [WWOX] on human neural progenitor cell (hNPC) maintenance and how depletion of [WWOX] disturbs signaling pathways playing a pivotal role in neuronal differentiation and central nervous system (CNS) organogenesis." — PMID 31543760, Abstract

**For the oncology reading:** every author is in a **Department of Molecular Carcinogenesis**; roughly the first third of the Introduction is tumour-suppressor and glioblastoma biology; the experimental design is transplanted wholesale from the group's prior GBM work —

> "In our previous report we demonstrated that differentiation of [WWOX] expression influences the 3D growth of the GBM T98G cell line, with upregulation of its expression disturbing the growth and spread of cancer cells in an ECM matrix ()." — PMID 31543760, Discussion

The 3D-Geltrex assay, the adhesion assay, the MMP2/9 zymography and the "non-classical tumour suppressor / haploinsufficiency" framing are all a cancer-cell-biology panel applied to neural cells. This is not disqualifying — but it explains why **no** neurodevelopmentally specific assay (migration assay, laminar readout, electrophysiology, GABA measurement) was run.

### Abstract-versus-Results check — ONE INVERSION FOUND (batch item #5)

**The abstract states a non-significant result as a finding.**

Abstract: *"hNPC with a silenced [WWOX] gene exhibited lowered mitochondrial redox potential, **enhanced adhesion to fibronectin and extracellular matrix protein mixture**, downregulation of MMP2/9 expression and impaired 3D growth."*

Results, same claim, with the number:

> "The hNPC cells with silenced [WWOX] demonstrated considerably stronger adhesion to the ECM protein mixture (= 0.0626) and to fibronectin alone (< 0.05) ()." — PMID 31543760, Results

And the paper's own figure caption concedes it outright:

> "Adhesion of [WWOX] silenced hNPC cells to ECM protein mixture (Geltrex,), **the tendency not reaching the statistical significance (0.0626)** and to fibronectin,< 0.05." — PMID 31543760, Figure 3 caption

**p = 0.0626 with the authors' own declared threshold of p < 0.05** ("The results are described as significant when< 0.05.", Methods). The fibronectin arm is significant; the ECM-mixture arm is **not**, and the abstract conjoins them as though both were. Anyone reading only the abstract acquires a result the paper did not obtain.

**Second, smaller over-reach in the same abstract sentence:** *"downregulation of MMP2/9 **expression**."* MMP2/9 was never assayed at the expression level. It was gelatin zymography on conditioned medium — a **secreted-protein / gelatinolytic-activity** assay:

> "The level of metalloproteinase 2 and 9 was examined by gelatin zymography. The cells were cultured on a six-well plate for 48 h and the **culture medium** was collected for protein analysis." — PMID 31543760, Methods

> "It was also found that downregulation of [WWOX] lowered pro-MMP2 and pro-MMP9 metalloproteinase **secretion** ()." — PMID 31543760, Results

Results says *secretion*; the abstract says *expression*. Note also that only the **pro-** (zymogen) forms are reported as changed — the paper does not demonstrate a change in active enzyme.

### The claim the paper makes that its assays cannot carry

> "…our findings suggest that the WWOX protein might be an important regulator of neuronal migration and synaptogenesis." — PMID 31543760, Discussion

**No migration assay was performed. No synapse was measured.** There is no transwell, no scratch/wound, no time-lapse tracking, no slice, no synaptic marker, no electrophysiology in the Methods. "Migration" and "synaptogenesis" are inferred entirely from **GO gene-set membership at FDR < 0.25 plus the names of cytoskeletal and adhesion genes**. This is exactly the slide the batch was told to watch for, and it should be recorded against this paper wherever the migration link is reused.

---

## VERDICT

> **PARTIALLY USEFUL — states the narrow part that is**

**The narrow part that is useful:** this is a **perturbation** experiment (shRNA knockdown, scrambled control, Western-verified) in **human** neural progenitors of embryonic-stem-cell origin, and it yields (i) **measured cell-biological phenotypes** that LEGEND does not currently hold from a human developmental system — complete failure of 3D growth/differentiation, increased fibronectin adhesion, reduced pro-MMP2/9 secretion, reduced mitochondrial redox activity — and (ii) a **progenitor-versus-neuron asymmetry in programme coherence** (153 enriched sets at the progenitor stage against 4 after differentiation) that is a genuine, if indirect, stage-dependence signal.

**What it is NOT, and must not be inflated into:** it is **not embryonic in vivo data**, not a gestational-age anchor, not a migration measurement, not a layering measurement, not a metabolic flux measurement, not a null allele, and not allele-specific. It **cannot close the life-stage mismatch** the Chang/NCKU batch exposed, because a cultured progenitor has no developmental date. And its one explicit fetal-versus-adult expression datum (**9.2 vs 17.7 TPM RLE**) is a third-party database re-read that **argues against** a prenatal WWOX expression peak rather than for one.

**It is not a cancer paper wearing developmental clothing** — the intent, the keywords and the WOREE/SCAR12 framing are sincere. But it is a cancer *lab's assay panel* applied to neural cells, which is why its neurodevelopmental conclusions outrun its measurements.

---

## What it adds beyond PMID 32581702 (already read)

PMID 32581702 (Iacomino/Salpietro/Striano 2020, [10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644)) re-used **this transcriptome** — Kośla and Bednarek are co-authors there — and its abstract already delivers the migration-gene layer: *"Transcriptomic analyses of Wwox-depleted human neural progenitor cells showed an impaired expression of a number of neuronal migration-related genes encoding for tubulins, kinesins and associated proteins."* **LEGEND therefore already holds the headline. The upstream primary adds five things the downstream re-analysis does not carry:**

1. **The measured functional phenotypes, absent from 32581702 entirely** — the 3D-growth collapse (isolated, non-proliferating, non-differentiating single cells, three independent experiments, seeding-density-independent), the fibronectin adhesion increase (p < 0.05), the reduced pro-MMP2/pro-MMP9 secretion, and the reduced resazurin-reduction redox activity. 32581702 is a transcriptomic and histopathological paper; these are cell-biological readouts.
2. **The 2D-versus-3D dissociation** — the WWOX requirement appears *only* in a three-dimensional matrix and is invisible in monolayer. This is a mechanistic condition on the phenotype and a directly testable design constraint for any future LEGEND-relevant model system.
3. **A human-progenitor metabolic node** — one measured redox decrement plus a glycolysis/antioxidant expression signature (HK2, PDK1, LDHA, CYCS, SOD1/2, PRDX2). LEGEND's metabolic evidence has been rodent-weighted; this is human, with the flux-versus-programme caveat attached.
4. **The stage-coherence asymmetry (153 vs 4 enriched sets), together with the internal tension against the DEG counts (2282 vs 7392) that the paper never reconciles.** This is the only quantity in either paper that speaks, however indirectly, to *when* in a differentiation trajectory WWOX loss does organised damage.
5. **The directional adhesion switch (CDH2 down ~2×, ITGB1 up ~2×) and the semaphorin-rich WWOX-competent leading edge** (nine SEMA genes, plus NRG1/ERBB4, JAG1) — gene-level detail that the downstream summary compresses away.

**Two corrections this audit contributes to how LEGEND should cite the pair:** (a) **do not cite PMID 31543760 for Wnt** — Wnt appears only in its background prose and in citations to the authors' prior GBM work, never in its own results; and (b) the **migration link in both papers traces back to GO gene-set enrichment at FDR < 0.25 on a single shRNA knockdown with no migration assay** — 32581702 supplies the independent in vivo migration evidence (human fetus, `lde` rat), the transcriptome does not.

---

## Not done, by instruction

No canonical file was read for edit or written. No commit candidate. No therapeutic inference. The raw full text was **not** cached to `files/fulltext/` — the task specified exactly one output file — so it is re-retrievable only via `mcp__PubMed__get_full_text_article(["PMC6730490"])`.

*Source: PubMed / PMC. Kośla K, Płuciennik E, Styczeń-Binkowska E, Nowakowska M, Orzechowska M, Bednarek AK. Front Cell Neurosci. 2019;13:391. [DOI: 10.3389/fncel.2019.00391](https://doi.org/10.3389/fncel.2019.00391). Comparator: Iacomino M et al. Front Neurosci. 2020;14:644. [DOI: 10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644).*
