# Intake wave 12 (2026-10-04) — Scientist C reading note

`context_policy: SOURCE_FIRST` — for each paper the owed sections were re-opened on the bytes the
manifest already declares, and the first-pass measurements were written down before any landed
record was opened. Where a record was consulted afterwards, the comparison is marked as such.

Wave type: **RE-READ**. Every paper below is already held with at least one receipt and its
artefact is on disk. Group C question: *what do the owed panels and supplements add to or limit in
the mechanism layer — Wnt direction, oxidoreductase activity, and the glial/interneuron baseline?*

Nothing here is medical advice. All patient description is at class level only (allele class ×
zygosity × phenotype band); no individual-level record, no parent-of-origin wording.

Genotype caution: every datum below is carried with its transfer limit stated. A constitutive null
(organoid KO, mouse null, tumour-line knockdown) models no human missense allele; P47T ≠ Q230P ≠
G372R ≠ A141T ≠ P252A; an acceptor allele is not a donor allele.

---

## 1 · PMID 34268881 — WOREE/KO cerebral organoids (held: 6 receipts, partial)

Owed per the selection row: **supplement (captions_only)**. Artefact set declared in
`PMID34268881.json`: 22 artefacts, all present, no digest mismatch.

### What was re-read on the same bytes

| owed surface | artefact (declared) | what was done |
|---|---|---|
| Expanded-View Table EV1 (up list) | `EMMM-13-e13610-s006.xlsx` | read **cell-wise** from the sheet XML (1,246 data rows × 8 columns) |
| Expanded-View Table EV2 (down list) | `EMMM-13-e13610-s005.xlsx` | read **cell-wise** (1,021 data rows × 8 columns) |
| Expanded-View / glial / GABAergic / myelin marker panel | `s006.xlsx`, `s005.xlsx` | 50 named symbols matched cell-wise against both symbol columns |
| Review Process File | `EMMM-13-e13610-s007.pdf` | **NOT READ BY THIS READING** — halted by a model safety classifier at the first pass over the referee text; per the wave brief (items 13, 21, 33) the same passage was not re-attempted in other words, and nothing below rests on it. It is **not an outstanding debt**: an earlier reading already read it, and its content sits in this paper's dossier under *«Cosa aggiunge il peer-review file»*. |
| Appendix Figures S1–S6 | — | **still not distributed anywhere.** They are cited in the Results but are absent from the eight-item official supplementary package (`s001`–`s008`), and the labelled Appendix `s004.docx` contains Appendix Table S1 only. This is the same gap the manifest has declared since 2026-08-14; this re-read did not close it and could not. |

### Measured, cell-wise (the two numbers each ratio names are given)

Wnt-pathway membership of the two DE lists, by exact symbol match, with the table's own `padj` and
`log2FoldChange` cells:

| direction | symbol | padj (cell) | log2FC (cell) |
|---|---|---|---|
| up | WNT8B | 3.06e-3 | 3.17 |
| up | RSPO1 | 5.42e-2 | 2.12 |
| up | WNT5A | 3.75e-2 | 2.00 |
| up | RSPO3 | 1.22e-2 | 1.55 |
| up | WNT2B | 4.33e-2 | 1.26 |
| up | NKD1 | 4.56e-4 | 1.23 |
| up | TCF7L2 | 5.59e-4 | 1.04 |
| up | LEF1 | 1.22e-2 | 1.00 |
| up | AXIN2 | 1.26e-2 | 0.79 |
| up | CTNNB1 | 1.58e-2 | 0.56 |
| up | FZD1 | 5.79e-2 | 0.50 |
| down | FZD2 | 3.36e-2 | −0.51 |
| down | WNT5B | 1.49e-2 | −0.41 |

**Direction, measured and not merely cited:** 11 of the 13 Wnt-pathway genes present in the two
lists are in the *up* list, and they include four direct β-catenin/TCF transcriptional targets
(NKD1 +1.23, AXIN2 +0.79, LEF1 +1.00, TCF7L2 +1.04) plus CTNNB1 itself (+0.56). The two *down*
entries are a receptor (FZD2 −0.51) and a non-canonical ligand (WNT5B −0.41). So the transcript
layer of this paper supports *canonical-Wnt activation in the constitutive-null organoid*, in the
direction the authors state, and it supports it with target genes rather than with ligands alone.

**What the same cells also show, and what the body text does not say.** The lists are **nominal-P**
sets, not FDR sets:

- UP list: n = 1,246; `pvalue` max = 0.00999; `padj` max = 0.0684; rows with padj > 0.01: **728**;
  rows with padj > 0.05: **175**.
- DOWN list: n = 1,021; `pvalue` max = 0.00999; `padj` max = 0.0684; rows with padj > 0.01:
  **704**; rows with padj > 0.05: **195**.
- Of the 2,267 rows in the two lists together, **1,432 (63.2% = 1432/2267)** have an adjusted
  P above 0.01 and **370 (16.3% = 370/2267)** have an adjusted P above 0.05.
- Effect sizes: |log2FC| min 0.260 in both lists against the stated FC > 1.2 cut
  (log2 1.2 = 0.2630), i.e. the published tables round at the boundary (one row per list sits
  0.003 below it). UP log2FC max 11.05; DOWN min −7.07.

The body states the filter correctly — "a fold change greater than 1.2 (FC > 1.2) and a significant
*P*-value (*P* < 0.01)" — and the Methods say "differentially expressed genes were filtered, setting
alpha to 0.01". The cells show that alpha applied to the **nominal** Wald P, not to the adjusted P.
Any downstream sentence that calls these 1,246/1,021 genes *significantly* differentially expressed
without naming the nominal-P threshold is carrying more than the table holds.

Two further mechanical facts on the same bytes:

- **WWOX itself appears in neither list** (exact symbol match over both symbol columns: zero hits).
  This confirms by measurement the 2026-10-03 reading's statement; it is expected for a CRISPR KO
  whose transcript may escape the DE filter, and it means these tables carry no measurement of
  residual WWOX transcript.
- The body sentence "The analysis revealed 15,370 differentially expressed genes, of which 1,246 …"
  cannot be reconciled with the tables: the two tables hold 2,267 rows in total, and 15,370 is the
  size of the tested set, not of a DE set. The sentence is a wording defect in the paper, not a
  LEGEND defect; it is recorded because a reader quoting it would inflate the result ~6.8-fold
  (15370/2267).

### Glial, GABAergic and oligodendroglial markers in the same two tables

Exact-symbol match of a 50-gene panel against both lists (every value is the table's own cell):

| axis | symbol | list | padj | log2FC |
|---|---|---|---|---|
| astro | AQP4 | up | 5.69e-2 | 2.70 |
| astro | SOX9 | up | 3.75e-2 | 0.51 |
| astro / RG | VIM | up | 4.15e-5 | 0.82 |
| astro | ALDH1L1 | down | 6.74e-2 | −0.56 |
| astro | **GFAP, S100B, SLC1A3, NFIA, NFIB, HEPACAM** | **in neither list** | — | — |
| microglia | **AIF1, P2RY12, CX3CR1, TMEM119, ITGAM, PTPRC, CSF1R, TREM2** | **in neither list** | — | — |
| oligo / myelin | PDGFRA | up | 6.55e-3 | 3.02 |
| oligo / myelin | MBP | up | 4.46e-2 | 1.41 |
| oligo / myelin | **OLIG1, OLIG2, SOX10, PLP1, CSPG4** | **in neither list** | — | — |
| GABAergic | GAD1 | up | 1.22e-2 | 3.57 |
| GABAergic | SLC32A1 (VGAT) | up | 4.33e-2 | 3.28 |
| GABA_A | GABRB2 | down | 3.36e-4 | −1.78 |
| GABA_A | GABRB3 | down | 2.44e-3 | −0.92 |
| interneuron peptide | **NPY** | **down** | **4.62e-15** | **−6.24** |
| glutamatergic | **SLC17A7, SLC17A6** | in neither list | — | — |
| other | GAD2, PVALB, SST, VIP, CALB1/2, GABRA1, GABRG2, SLC12A5, SLC12A2, IL6, TNF, IL1B | in neither list | — | — |

Four readings follow, each with its limit:

1. **The astrocyte increase in this paper is an immunofluorescence and immunoblot finding, and the
   paper's own transcriptome does not carry it.** `GFAP` and `S100B` — the two markers the authors
   quantify by IF for the *«marked increase in astrocytic cells»* — are **in neither DE list** at
   the paper's own threshold. What the tables do carry is AQP4 (+2.70), SOX9 (+0.51) and VIM
   (+0.82) up and ALDH1L1 (−0.56) down. `AQP4`, `NPY` and `MBP` occur **zero** times in the
   article body: they exist only in the deposited tables. Limit: bulk RNA-seq of 2 WT vs 4 KO
   organoids with heavy regionalisation defects; a transcript non-finding is not a protein
   non-finding, and the IF result is not contradicted — it is *unaccompanied*.
2. **Microglia cannot be tested here at all.** Eight microglial markers are absent from both
   lists, as expected for a cerebral organoid, which has no microglia. The IBA1 axis of the
   murine baseline therefore has **no counterpart** in this system — an earned null for the
   platform, not a negative result about WWOX.
3. **NPY collapses in the human WWOX-KO organoid** (−6.24 log2FC, padj 4.6e-15 — the strongest
   signal in this whole panel), and the authors never mention it. Independently, a systemic
   murine constitutive null shows lower NPY-positive counts (in DG only). Two systems, two
   species, same direction for the same neuropeptide. Limit, stated hard: transcript versus
   marker-positive cell count, constitutive null in both, no regional resolution in an organoid,
   and **no transfer to any missense or splice allele** — this says nothing about P47T, Q230P,
   G372R, A141T, P252A or an acceptor allele.
4. **Myelin cell autonomy is untestable here.** PDGFRA (+3.02) and MBP (+1.41) are up, but
   OLIG1, OLIG2, SOX10, PLP1 and CSPG4 are absent from both lists, and a week-15 cerebral organoid
   has essentially no myelination. Two markers without a lineage do not make an oligodendroglial
   phenotype.

The RNA-seq layer also **confirms** the E/I marker pattern already landed: GAD1 up, VGAT up,
GABRB2/GABRB3 down, VGLUT1 (`SLC17A7`) absent from both lists i.e. not differentially expressed.
`GAD2` is absent from the DE tables — the landed wording that names GAD2 rests on the Fig 1D
**qPCR** panel, not on the RNA-seq, which is a different assay and not a contradiction.

### What this changes in the records that wait

Compared **after** the first pass was written (`registry_records.py get`):

- 🔴 **The selection row's premise is wrong on one point.** It names *CLAIM 005 (baseline)* as the
  baseline claim this paper gates. CLAIM 005's own measurements are **murine** (a systemic
  constitutive Wwox-KO: PV, NPY, IBA1/GFAP area fractions), its `Source` is that mouse paper, and
  PMID 34268881 enters it only as one row of a seizure-onset-versus-astrocyte table, marked
  `Unclear`. The `consolidated baseline` claim this paper actually founds is **CLAIM 002**
  (*WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype*), which names
  PAPER 039 directly. Both were read before classing the candidates.
- **CLAIM 002** (`consolidated baseline`) — **narrowed** on one phrase: its summary carries
  *«Astrogenesi aumentata»* without an assay, and the measurement above confines that to IF and
  immunoblot while the paper's own DE tables hold neither GFAP nor S100B. Candidate
  `CC-20261004W12-C-STEINBERG-ASTRO-01`, class **MAJOR**, with blind-audit triples. **Not edited
  here.** The same candidate carries the NPY datum as an addition, not as a correction.
- **CLAIM 005** (`consolidated baseline`) — its murine NPY finding gains an independent human
  concordance (point 3 above). Proposed in the same candidate as an addition to its evidence
  boundary, with the transfer limit written into the sentence. Nothing in CLAIM 005 is withdrawn
  or weakened.
- **CLAIM 030** — unaffected. Nothing in EV1/EV2 measures residual protein function.
- **DL-MOL-003** — this is where the re-read moves the most. Its evidence boundary of 2026-10-03
  states that *«No neural, organoid or patient datum on canonical Wnt activity in WWOX loss is
  cited by any of these sources»* and that the organoid abstract *«dice solo "impairment" senza
  verso»*. The EV tables are exactly that missing datum, and they are organoid, human and
  target-level. Candidate `CC-20261004W12-C-WNT-DIRECTION-01`, class **MINOR** (research-layer
  record, append-only, status unchanged).
- **CONFIRMED, not new:** the nominal-P character of the EV lists and the absence of `WWOX` from
  both of them were already in this paper's dossier. This re-read re-establishes both **by exact
  count on the same bytes** (728 + 704 rows with padj > 0.01; 175 + 195 with padj > 0.05; max padj
  0.0684; zero `WWOX` rows) rather than retiring or revising them.
- The **seizure-onset** gap the main text leaves `Unclear` is **not** closed and cannot be closed
  from this source: an organoid has no seizures and no onset age, so that cell of the table is
  better described as not-applicable than as unclear. The Appendix figures that might have carried
  the developmental timing are not distributed.

### What remains owed on this paper after this re-read

1. **Appendix Figures S1–S6** — not distributed by the publisher or by PMC; not recoverable here.
   What would unblock: the Appendix figure file from the journal, or an author-deposited copy. No
   external spend and no author contact (§21d reserved).
2. **Review Process File `s007.pdf`** — on disk, digest
   `e63bf1b975ced9afec7e678e9bd3e1c5eba9948a037af0f65751b5ea3acf339a`, but unread: a safety
   classifier halted the read. A different reader (or a different model) can discharge it; the bytes
   are already held, so this is not an acquisition debt.
3. **References (91 items)** — `not_read` as a section; the multihop enumeration in the manifest
   already lists the gene-direct subset, so this is a formal rather than a substantive gap.

---

## 2 · PMID 40524961 — Sengupta 2025, sterols and Dishevelled (held: 1 receipt, partial)

Owed: figures. Read as images: Figures 5 and 6 (native JPEGs, now declared with full digests) and
supplementary Figure S6 (page 9 of `mmc1.pdf` at 200 dpi).

**WWOX: an earned null for the gene.** `wwox` occurs **twice** in the whole article — one Discussion
sentence citing a head-and-neck cancer study, and its reference entry. The paper was read only for
the transferable question, and the transfer limit is absolute: sterol-synthesis inhibition in
HEK293T and iPSC-derived NSCs, no WWOX perturbation of any kind.

What the panels add: nuclear DVL2 rises under cholesterol-synthesis inhibition (Fig 5E, `**` and
`****`) while membrane and cytosolic DVL2 fall; the import route is PDZ-domain and FoxK2 dependent
and is abolished by the PDZ inhibitor (Fig 6B, 6E/6F `****`); and in Fig S6E the condition with the
most nuclear DVL2 carries the **lowest** canonical response — ≈12 against ≈55 for its own vehicle,
about 4.6-fold, read off the plot — with **no significance marker drawn anywhere on the panel** and
no test in the legend.

Record affected: **DL-MOL-003**, Op 2 of `CC-20261004W12-C-WNT-DIRECTION-01` (MINOR). The
dissociation of nuclear DVL from canonical activation is demonstrated **for that route**, which is
sterol-driven and not a tumour-suppressor silencing; it is not transferred to WWOX.
Still owed: `mmc2.xlsx` and `mmc3.xlsx` (interactome tables, undeclared binary supplements).

## 3 · PMID 41124647 — Zhang 2025, two SDR-region missense alleles (held: 2 receipts, partial)

Owed: figures — and only one of seven figure images was on disk. The package was acquired free from
the Europe PMC supplementaryFiles archive for PMC12767083; the already-declared supplement DOCX came
back **byte-equal**, which is the integrity check for the rest.

**Answer to this wave's question: no panel quantifies oxidoreductase activity, because there is no
enzymatic assay anywhere in the paper.** `oxidoreductase` occurs once (expanding the gene's name),
`SDR`, `enzyme`, `catalytic`, `dehydrogenase` and `short-chain` occur zero times. The measured loss of
function is phenotypic and post-translational, never catalytic.

Measured on the panels: Figure 2A shows the four compared lines are **not expression-matched** —
P252A faint in both cell lines, P282A visibly weaker than wild type in BCPAP, on an even GAPDH row,
with no densitometry published (a crude pixel integration attempted here was discarded as
unreliable, and no ratio is carried). Figure 4A shows they are **not transcript-matched** either:
relative transgene mRNA ≈ 72 (WT), 78 (P252A), **108 (P282A)**, so P282A carries ≈1.5× the WT
transcript; Figure 4B has P282A `ns` against WT at all five chase timepoints.

Supplementary Table 6, read cell-wise for the first time, is a **presence-only** interactome: 261
rows, `Lost Detection` in all three control columns of every row, no replicate, no fold change, no
p-value, no WWOX row. POLE4 is rank 52 of 261; **DVL2 is present** at rank 190 — a lead on the
WWOX–DVL axis, not a measurement of it.

Record affected: **DL-BIO-001**, `CC-20261004W12-C-SDR-ABUNDANCE-01` (MINOR). Genotype caution:
P252A ≠ Q230P, and an SDR-region missense is not an acceptor-site allele.

## 4 · PMID 33195192 — Chou 2020, Wwox-deficient mouse skin (held: 1 receipt, partial)

Owed: figures and supplement, both `not_read` and both absent from disk — the manifest declared the
article XML alone. The whole package (eight figure images, the supplementary legend PDF, ten
supplementary images) was acquired free from the Europe PMC archive for PMC7652735.

**Answer to this wave's question: the raised-WWOX caution is only cited here.** `transfect` occurs
zero times; both occurrences of `overexpress` sit inside citations; the single `ectopic` is
"ectopic p53" in a citation. Every measurement in the paper is a loss-of-Wwox measurement. The
landed record already words it that way, so this reading **confirms it and changes nothing**.

New from the owed supplement, all of it absent from the legends:

- Three exact P-values printed on panels — transepidermal water loss **P = 0.3894** (Fig S1A,
  n = 8/9/5), follicle number at E16.5 **P = 0.56** and follicle length at E18.5 **P = 0.62**
  (Fig S6A/B). The barrier is not measurably impaired even in the homozygous null, and follicle
  development to E18.5 is unaffected: three earned nulls, each with its number.
- A **measured heterozygote null**: epidermal TUNEL-positive cells ≈ 0.8 % (`+/+`), ≈ 0.85 % (`+/−`),
  ≈ 1.8 % (`−/−`), n = 5, with brackets drawn only against `−/−` (`*` from each) and **none between
  `+/+` and `+/−`**, which under the legend's all-pairwise Tukey means tested and not significant.

Limits: mouse skin, constitutive knockout, one postnatal day, n = 5 — weak evidence of absence, and
no transfer to a human heterozygote, to brain, or to any missense or splice allele. **No candidate:
nothing changes.**

## 5 · PMID 37781246 — Kałuzińska-Kołat 2023, four GBM lines (held: 1 receipt, partial)

Owed: figures and supplement, both absent; the package (five figure images, five supplementary
TIFFs, seven workbooks) was acquired free from the Europe PMC archive for PMC10540236.

**Answer: the proliferation phenotype cannot be panel-supported here, because the paper performs no
proliferation, viability or colony assay at all** — `MTT` 0, `BrdU` 0, `transfect` 0, and all three
occurrences of `viabilit` are narrative sentences about the group's preceding study. The work is
transcriptomic and network-analytic throughout. The landed record already attributes the phenotype
to the preceding paper: **confirmed**.

New: the supplement shows the transduction worked in **all four** lines (`WWOX` is in the
*«Upregulated in all cell lines»* set of Supp Table 5 and in all four cell-line columns of Supp
Table 3), so the one-of-four phenotype is not a failure of overexpression elsewhere — **but the
magnitude achieved per line is published only as node colour in Figure 3A, with no numeral anywhere
and no per-line column in any of the seven workbooks.** The question that would separate
line-specific biology from a dose difference is unanswerable from what is deposited.

Record affected: **CLAIM 011** (status `flagged for review`, not a baseline) —
`CC-20261004W12-C-GBM-DOSE-UNPRINTED-01` (MINOR).

## 6 · PMID 41345172 — common WWOX intronic deletion (held: 2 receipts, partial, wave-9 re-read)

Owed: supplement still `captions_only`; three of fifteen supplementary files were held. The other
twelve workbooks were acquired free from the Europe PMC archive for PMC12753814, and the three held
files returned **byte-equal**.

**Answer: the 1447-homozygote annotation survives.** Supplementary Figure 19 had been read at
70 dpi; re-rendered at **400 dpi** the row reads `DEL_16_156229`, 78371638–78384898, 13.3 kb, allele
count **7355**, allele number **21694**, AF **3.39e-1**, homozygotes **1447**; 7355/21694 = 0.33903.
Nothing to retire.

Two additions, both strengthening the standing rejection rather than weakening it:

- The row is the first of **fourteen** gnomAD structural variants inside WWOX, and three more in the
  same highlighted block are common too — `DEL_16_156234` (AF 0.318, **220** homozygotes),
  `INS_16_101038` (AF 0.186, 122), `INS_16_101054` (AF 0.101, **327**). WWOX carries several common
  intronic SVs; this one is the most frequent, not a singular event.
- **Supplementary Table 1, the authors' own rank-1 table, contains no WWOX-interval result.** 139
  packed result cells across every cohort, method and phenotype; the only chromosome-16 cell is
  `16:75296761; BCAR1`. For SANAD drug response the rank-1 cells (1.46e-5 and 1.7e-5) are both
  stronger than the deletion's best drug-response p of 1.68e-4.

Records: **DIS-036** (`CC-20261004W12-C-CNV-CONTEXT-01`, MINOR); **CLAIM 032** checked and left
unchanged — its figures are confirmed digit for digit.

---

## 7 · The assigned question, answered

*What do the owed panels and supplements add to or limit in the mechanism layer — Wnt direction,
oxidoreductase activity, and the glial/interneuron baseline?*

**Wnt direction: this is where the wave moves the model.** The direction now has a human, organoid,
**target-gene** measurement behind it — four β-catenin/TCF targets up in the WWOX-KO cerebral
organoid tables (NKD1 +1.23, TCF7L2 +1.04, LEF1 +1.00, AXIN2 +0.79, with CTNNB1 +0.56) — where the
research record said no neural, organoid or patient datum on canonical Wnt activity existed. Its
limits are equally measured: transcript only, no reporter, no β-catenin fractionation, 2 WT vs 4 KO,
nominal-P lists, constitutive null. And the one counter-datum in the corpus is now read at panel
level: in HEK293T, maximal nuclear DVL2 coincides with the **lowest** canonical response — by a
sterol-driven, PDZ- and FoxK2-dependent route that is not WWOX silencing, and on a panel that draws
no statistic. So: **direction supported in the organoid; the mechanism step DVL2-nuclear → canonical
activation still unmeasured.**

**Oxidoreductase activity: an earned null, and it is complete.** Neither paper that could have
carried it does. The SDR-missense paper has no enzymatic assay of any kind (`oxidoreductase` once,
in the gene's name; `SDR`, `catalytic`, `dehydrogenase` zero). What it measures is abundance and
decay rate — and the re-read shows its "clean" allele is clean about **decay rate** only, since the
lines are matched on neither transcript nor steady-state protein. The diagnostic question for a
destabilising SDR allele therefore stays where DL-BIO-001 put it — *is the protein present at normal
abundance, or degraded despite normal mRNA?* — and **not one datum in this corpus measures catalysis
for any WWOX allele.**

**The glial/interneuron baseline: narrowed in one place, extended in another, and untestable in a
third.** Narrowed: the organoid astrogenesis finding is carried by immunofluorescence and immunoblot
alone — GFAP and S100B appear in **neither** of the paper's own DE lists (zero rows in 2,267), while
AQP4 (+2.70), SOX9 (+0.51) and VIM (+0.82) rise and ALDH1L1 (−0.56) falls, and AQP4 is never
mentioned in the article. Extended: **NPY collapses in the human WWOX-KO organoid** (−6.24, padj
4.6e-15, the strongest signal of a 50-marker panel, unreported by the authors), in the same
direction as the murine NPY reduction a baseline claim records — two species, one neuropeptide.
Untestable: microglial markers are absent as a class (the platform has none), so the murine IBA1
axis has no organoid counterpart; and in mouse skin the **heterozygote is a measured null** on
apoptosis while the homozygote is raised.

### What would change the model if true, and what would falsify it

- **Would change it:** a TCF/LEF reporter or nuclear β-catenin quantification in WWOX-null *neural*
  cells confirming activation — that would move DL-MOL-003 from IPOTESI toward a direction with a
  mechanism, and it is a cheap experiment. Equally: an NPY measurement in a second human WWOX-loss
  system.
- **Would falsify what this wave carried:** a GFAP or S100B row in either organoid DE list; a
  single-cell re-analysis attributing the Wnt-target rise or the astroglial markers to composition
  rather than to cell-intrinsic change; an NPY row absent or positive on the same bytes; a
  densitometry of the SDR paper's Figure 2A showing P282A at wild-type abundance in both lines.

### Genotype caution, restated because every datum above needs it

Every measurement in this wave comes from a **constitutive null** (organoid KO, mouse KO) or from
**engineered overexpression in cancer lines**. None models a human missense or splice allele.
P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A; an acceptor allele is not a donor allele; a heterozygote is
neither a demonstrated negative nor a positive for haploinsufficiency. Nothing here is medical
advice.
