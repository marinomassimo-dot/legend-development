# CC-20261004W12-C-WNT-DIRECTION-01 — the organoid datum DL-MOL-003 says is missing now exists

- **Wave:** intake wave 12, 2026-10-04, Scientist C (RE-READ wave)
- **context_policy:** SOURCE_FIRST — the two Expanded-View workbooks were read cell-wise before
  DL-MOL-003 was opened; the comparison below was written afterwards.
- **Target record:** `DL-MOL-003` in `disease-models/wwox/research/discovery_ledger_current.md`
- **Change class:** **MINOR.** The target is a research-layer, non-canonical, append-only lead;
  its `Status` stays `IPOTESI` and its `Belief` is not raised by this candidate. No consolidated
  baseline claim is narrowed or reversed by this file.
- **Source read:** PMID 34268881 (DOI 10.15252/emmm.202013610), Expanded-View Tables EV1/EV2,
  artefacts `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx` (sha256
  `83857ec6006928d9810f7a4c284b93b04266792fce38d960e21731f72f944eeb`) and
  `…-s005.xlsx` (sha256 `82a03fc996b2ca3da0ff96032ba6a6b011458f9cf0df29a6129165bc7bed2718`),
  both declared in `deepdive_manifests/PMID34268881.json` and verified PRESENT with matching digest.
- **Receipt of the producing reading:** `FTR-20261004-34268881-07` (prepared, not recorded;
  `reread_reason: inadequate_prior_coverage`, `prior_receipt: FTR-20261003-34268881-06`).

## Why

DL-MOL-003's evidence boundary of 2026-10-03 states that no neural, organoid or patient datum on
**canonical** Wnt activity under WWOX loss is cited by any of its sources, and that the organoid
paper's abstract gives *«solo "impairment" senza verso»*. The organoid paper's own deposited
differential-expression tables do give a direction, at the level of β-catenin/TCF **target genes**
rather than ligands. That closes the specific gap the boundary names, without touching the step the
boundary rightly calls un-measured (DVL2 nuclear entry → canonical activation): the tables measure
the output of the pathway, not the mechanism by which it is reached.

## Exact op

**File:** `disease-models/wwox/research/discovery_ledger_current.md`
**Record:** `DL-MOL-003`
**Op:** `append_to_field` — append the following sentence block to the end of the existing
`- **Evidence boundary (2026-10-03, ...)` bullet (the last bullet of the record), leaving every
existing word intact.

`old` (verbatim, measured unique within `DL-MOL-003`):

```
No neural, organoid or patient datum on canonical Wnt activity in WWOX loss is cited by any of these sources. Status unchanged (IPOTESI); Belief should not be raised on the strength of the 2025 citations.
```

`new`:

```
No neural, organoid or patient datum on canonical Wnt activity in WWOX loss is cited by any of these sources. Status unchanged (IPOTESI); Belief should not be raised on the strength of the 2025 citations. 🔵 **Addition 2026-10-04 (`CC-20261004W12-C-WNT-DIRECTION-01`, intake wave 12 Scientist C, re-read of PMID 34268881 at receipt `FTR-20261004-34268881-07`): that datum now exists, and it is this paper's own deposited tables rather than a citation.** Read cell-wise from Expanded-View Tables EV1/EV2 (`EMMM-13-e13610-s006.xlsx`, `…-s005.xlsx`), eleven of the thirteen Wnt-pathway genes present in the two lists are **up** in WWOX-KO cerebral organoids, and four of them are direct β-catenin/TCF transcriptional targets: `NKD1` log2FC 1.23 (padj 4.56e-4), `TCF7L2` 1.04 (5.59e-4), `LEF1` 1.00 (1.22e-2), `AXIN2` 0.79 (1.26e-2), plus `CTNNB1` itself 0.56 (1.58e-2) and the ligands `WNT8B` 3.17 (3.06e-3), `RSPO1` 2.12 (5.42e-2), `WNT5A` 2.00 (3.75e-2), `RSPO3` 1.55 (1.22e-2), `WNT2B` 1.26 (4.33e-2), `FZD1` 0.50 (5.79e-2); the only downregulated entries are `FZD2` −0.51 (3.36e-2) and the non-canonical ligand `WNT5B` −0.41 (1.49e-2). ⚠️ **Four limits travel with it and none of them is removable from this source:** (1) transcript only — these tables contain no TCF/LEF reporter and no nuclear-versus-cytosolic β-catenin ratio, so the pathway's **output** is measured and its activation **step** is not; (2) the lists are nominal-P sets (`pvalue` < 0.01 with fold change > 1.2; `padj` runs up to 0.0684, and `RSPO1` and `FZD1` above sit above padj 0.05), so the direction rests on the four targets whose padj is below 1.3e-2, not on the whole set; (3) bulk RNA-seq of **2 WT versus 4 KO** organoids with declared regionalisation and maturation defects, which does not separate a cell-intrinsic pathway change from a change in cellular composition; (4) a **constitutive null** in an engineered human line — it models no missense allele and no splice allele, and nothing here transfers to P47T, Q230P, G372R, A141T, P252A or to an acceptor allele. 🔵 **What the addition does NOT change:** the step `DVL2 nel nucleo → iper-attivazione Wnt/β-catenin` of the Mappa ABC stays un-measured, because the HEK293T reporter datum that moved the other way (PMID 40524961, Fig. S6E) is about that step and is not contradicted by a transcriptional read-out in a different system; the therapeutic inference (`Wnt_inhibitor —may_correct→`) stays `IPOTESI` with its prenatal-window and systemic-toxicity counter-evidence intact; and the direction remains unmeasured in any **patient-derived** neural system, since the two patient-derived organoid lines of this paper are not the ones in the RNA-seq comparison. **Not medical advice.**
```

## Registry records

**None owed.** PMID 34268881 is already registered as `PAPER 039` (status `claim_linked`) with
`LIT-0365` and the superseded placeholder `CORPUS P365` as its audit trail. This candidate creates
no `PAPER`/`LIT` record and no `CORPUS-STUB`.

## What would falsify this addition

A TCF/LEF reporter or a nuclear β-catenin quantification in WWOX-null **neural** cells showing no
activation, or a single-cell re-analysis of the same organoids showing the target-gene rise is
carried entirely by a shift in cell composition. Either would return the direction to un-measured
in the neural context without touching the oncology primaries.

### LOCATOR TRIPLES FOR BLIND AUDIT

1. (Canonical β-catenin/TCF target genes are up in WWOX-KO cerebral organoids in this paper's own deposited differential-expression table | `[spreadsheet attestation — read cell-wise from the workbook XML] Table EV1 (upregulated list) carries NKD1 padj 4.56E-4 log2FoldChange 1.23; AXIN2 padj 1.26E-2 log2FoldChange 0.79; LEF1 padj 1.22E-2 log2FoldChange 1.00; TCF7L2 padj 5.59E-4 log2FoldChange 1.04; CTNNB1 padj 1.58E-2 log2FoldChange 0.56; WNT8B padj 3.06E-3 log2FoldChange 3.17.` | Table EV1, rows matched by exact gene symbol in the 'symbol' column; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx`)
2. (Only two Wnt-pathway genes are in the downregulated list, and neither is a β-catenin transcriptional target | `[spreadsheet attestation — read cell-wise from the workbook XML] Table EV2 (downregulated list) carries FZD2 padj 3.36E-2 log2FoldChange -0.51 and WNT5B padj 1.49E-2 log2FoldChange -0.41, and no other Wnt-pathway symbol.` | Table EV2, rows matched by exact gene symbol in the 'symbol' column; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s005.xlsx`)
3. (The two lists are nominal-P sets rather than FDR sets, so the direction rests on the individual rows' adjusted P values and not on list membership | `[spreadsheet attestation — read cell-wise from the workbook XML] Over the 1,246 rows of Table EV1 and the 1,021 rows of Table EV2 the 'pvalue' column maxima are both 0.00999 while the 'padj' column maxima are both 0.0684; rows with padj above 0.01 number 728 and 704, rows with padj above 0.05 number 175 and 195, and the minimum absolute log2FoldChange is 0.260 in each list against a stated fold-change cut of 1.2 whose log2 is 0.2630.` | Tables EV1 and EV2, 'pvalue', 'padj' and 'log2FoldChange' columns, all rows; read cell-wise from xl/worksheets/sheet1.xml — `files/fulltext/PMID34268881_assets/EMMM-13-e13610-s006.xlsx`)
4. (The RNA-seq comparison behind these tables is two wild-type against four knockout samples | `These two samples were extracted from further analysis, giving a total of six samples used for further analysis.` | Materials and Methods, Library preparation and RNA sequencing — `files/fulltext/PMID34268881_Steinberg2021_PMC.xml`)
