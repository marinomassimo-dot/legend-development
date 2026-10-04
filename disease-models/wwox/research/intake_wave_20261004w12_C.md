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
