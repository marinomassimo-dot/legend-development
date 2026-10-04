# COMMIT CANDIDATE — CC-20261004W7-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 7 2026-10-04, branch `task/sci-A-20261004w7`.
**context_policy:** `SOURCE_FIRST` — each first pass was written before any registry record about the paper was opened; comparison afterwards (`research/intake_wave_20261004w7_A.md`).
**Not medical advice.** No individual-level record; class-level statements only.

## Target
- `paper_registry_current.md`: **create** `PAPER 201`–`PAPER 204` for the four PMIDs read in this wave; **promote** `CORPUS-STUB-132` (PMID 32368285), which becomes `PAPER 201`.
- `literature_tracking_log_current.md`: **create** `LIT-0494`–`LIT-0496` for the three PMIDs with no LIT record; **update** `LIT-0493` (PMID 33958783), landed by `CC-20261003W6-A-REGISTRY-01` as `discovered` and unread.

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? | receipt (prepared, not appended) |
|---|---|---|---|---|
| 32368285 | `PAPER 201` (new; promotes `CORPUS-STUB-132`) | `LIT-0494` (new) | yes | `FTR-20261004-32368285-01` **partial** |
| 42558002 | `PAPER 202` (new) | `LIT-0495` (new) | yes | `FTR-20261004-42558002-01` **complete** |
| 40937943 | `PAPER 203` (new) | `LIT-0496` (new) | yes | `FTR-20261004-40937943-01` **partial** |
| 33958783 | `PAPER 204` (new) | `LIT-0493` (exists; updated `discovered` -> `processed`) | PAPER only | `FTR-20261004-33958783-01` **partial** |

**Numbers are provisional.** Measured 2026-10-04 with `registry_records.py catalog` on this branch at commit `eff9ca8920cd` (highest landed: `PAPER 200`, `LIT-0493`, `FT-192`, `CLAIM 045`, `CORPUS-STUB-179`). Wave 6's open candidates and this wave's peers B and C may claim the same numbers. The integrator renumbers in event order and updates the wikilinks in the `CORPUS-STUB-132` and `LIT` ops and the `insert-after` anchors.

## Ordering
1. The four receipts must be appended before this candidate is propagated. All four were dry-recorded in event order against throwaway copies of the ledger and the state manifest taken from `main`: four `RECORDED`, exit 0 each, `verify` OK on the copy at 379 chained receipts, real ledger and manifest untouched (`git status` empty for both paths).
2. `CC-20261003W6-A-REGISTRY-01` has already landed (`main` at 70513cd), so no ordering constraint remains against it; its `LIT-0493` is updated here rather than duplicated.

## Registry statements compared with the source (correction 12)
- `CORPUS-STUB-132` carries the title and identifiers of PMID 32368285 correctly and makes no claim; it is a placeholder and is promoted, not corrected.
- `DL-MOL-003` names Celebi 2020 as one of three studies that "fix the direction" of the Wnt axis. Now that the paper is read, that statement needs the boundary carried by `CC-20261004W7-A-DVL-01`; it is not corrected here.
- No registry statement cites PMID 42558002, PMID 40937943 or PMID 33958783.

## Reading-debt discharge (correction 15)
- **PMID 33958783 discharges a debt named in wave 6.** `research/intake_wave_20261003w6_A.md` and the manifest of PMID 42135313 record it as the unread discovery source of rs8050111. It is now read. The statements that rested on it stand with two qualifications the primary itself supplies: its authors call the WWOX signal **suggestive**, and WWOX is the **nearest-gene** label of an imputed common variant, with no eQTL or fine-mapping.
- **PMID 32368285 discharges one of the three Dvl primaries named as unread in wave 6.** The remaining two (PMID 19465938, PMID 23030478) are still unread and still closed access.

## Change class
**MINOR** — record creation, one placeholder promotion and one status update. No claim status, no working-model block, no consolidated-baseline claim is touched by this candidate.

## Op list — `paper_registry_current.md` (record-scoped; provisional numbers)

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 200",
  "text": "\n## PAPER 201\n**Short title:** Celebi 2020 J Cancer — WWOX siRNA in a non-cancer oesophageal epithelial line shifts the Dvl cytoplasm/nucleus ratio; no Wnt output measured\n**Full title:** Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer\n**Authors:** Celebi A, Orhan C, Seyhan B, Buyru N\n**Year:** 2020\n**Source type:** primary research — human cell lines and tumour/normal tissue pairs\n**Journal/source:** *J Cancer* 2020;11(14):4030-4036\n**Identifier:** PMID 32368285 / PMCID PMC7196265 / DOI 10.7150/jca.40840\n**Status:** processed\n**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A); promotes [[paper_registry_current#CORPUS-STUB-132]]. Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-32368285-01` (article read end to end; partial because its single gene-direct reference, PMID 19465938, has no lawful free route and stays a declared manifest gap); manifest `deepdive_manifests/PMID32368285.json`; dossier `research/fulltext_dossiers/PMID32368285.md`\n**Primary pathway:** P3 — Wnt/DVL (cancer context)\n**Model/species:** human HET-1A (oesophageal squamous epithelial, non-cancer) and SCC-15 (tongue SCC); 98 HNSCC tumour/normal pairs, 50 of them for protein\n**Genotype/model:** transient siRNA knockdown; no allele, no null\n**Transferability:** T4 — epithelial knockdown with a band-intensity ratio readout; no neural, glial or developmental measurement\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** The assay behind LEGEND's WWOX-Dvl direction, now read. 🔴 The silencing was done in HET-1A, a non-cancer oesophageal line, not in a head-and-neck cancer line; the quantity is a cytoplasm/nucleus band-intensity ratio with no replicate count, dispersion or p value (Table 4); the siRNA blot is not shown (Figure 4 has no siRNA lane and no nuclear-fraction marker); no beta-catenin or TCF/LEF readout exists anywhere in the paper; and Figure 1B prints p = 0.227 for the DVL-3 difference the Results call significant.\n**LIT link:** [[literature_tracking_log_current#LIT-0494]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 201",
  "text": "\n## PAPER 202\n**Short title:** Lange 2026 J Neurosci Res — astrocytes in genetic epilepsies; all four WWOX rows marked Unclear on cell autonomy\n**Full title:** Astrocytes in Genetic Epilepsies: Supporting Actor or Key Player?\n**Authors:** Lange J, Zhao E, O'Connell E, Gillham O, McTague A\n**Year:** 2026\n**Source type:** review (narrative)\n**Journal/source:** *J Neurosci Res* 2026;104(8):e70148\n**Identifier:** PMID 42558002 / PMCID PMC13444675 / DOI 10.1002/jnr.70148\n**Status:** processed\n**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261004-42558002-01`; manifest `deepdive_manifests/PMID42558002.json`; dossier `research/fulltext_dossiers/PMID42558002.md`\n**Primary pathway:** astrocyte biology / neuroinflammation (background)\n**Model/species:** review of mouse, zebrafish, iPSC and organoid models\n**Genotype/model:** four WWOX rows: constitutive null, P47T, human organoids (KO and a canonical splice-acceptor allele), conditional knockouts\n**Transferability:** none — re-description of primaries LEGEND already holds\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** The first third-party, non-WWOX group to tabulate the WWOX astrocyte evidence. 🔴 Every one of its four WWOX rows is marked **Unclear** on the reactive-versus-cell-intrinsic axis, and it concludes the astrocyte phenotype is downstream of neuronal dysfunction. Two defects of its own: a Table 1 cell reads 'No seizures' where the narrative says only that no seizure activity was reported, and the narrative calls the organoid primary 'iPSCs edited to carry a patient variant' where that paper used CRISPR-engineered ES cells for the knockout and separately patient-derived iPSCs.\n**LIT link:** [[literature_tracking_log_current#LIT-0495]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 202",
  "text": "\n## PAPER 203\n**Short title:** Ramirez 2025 Alzheimers Dement — WWOX transcript differs by donor ancestry in iPSC-derived oligodendrocytes; no WWOX perturbation\n**Full title:** Ancestral genomic functional differences in oligodendroglia: implications for Alzheimer's disease\n**Authors:** Ramirez AM, Nasciben LB, Moura S, et al.; Vance JM\n**Year:** 2025\n**Source type:** primary research — iPSC multiome (snRNA-seq, snATAC-seq, Hi-C)\n**Journal/source:** *Alzheimers Dement* 2025;21(9):e70593\n**Identifier:** PMID 40937943 / PMCID PMC12426912 / DOI 10.1002/alz.70593\n**Status:** processed\n**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A). Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-40937943-01` (figure panels read as captions only; thirteen supplementary tables not fetched); manifest `deepdive_manifests/PMID40937943.json`; dossier `research/fulltext_dossiers/PMID40937943.md`\n**Primary pathway:** oligodendrocyte-lineage expression (background)\n**Model/species:** human, 12 iPSC lines (four per ancestry) differentiated to neural spheroids with oligodendrocyte-lineage cells\n**Genotype/model:** no WWOX manipulation; ancestry and APOE genotype are the contrasts\n**Transferability:** T4 — usable only as a baseline-variance denominator for WWOX transcript in that lineage\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** The only record in LEGEND where WWOX transcript is quantified in named human oligodendrocyte-lineage cells: iOL fold change -1.34 (AF vs AI, adjusted p 1.95E-05) and -1.33 (EU vs AI, adjusted p 9.59E-03), plus an all-female iOPC result. 🔴 What varies is donor ancestry, not WWOX dose; the MAST model carries no donor random effect, so the p values are nucleus-level; the authors' own sex-stratified check dropped seven of nine AD-GWAS genes; and the Results sentence says 'five' while naming six genes.\n**LIT link:** [[literature_tracking_log_current#LIT-0496]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 203",
  "text": "\n## PAPER 204\n**Short title:** Liu 2021 Nat Genet — genome-wide survival study; WWOX rs8050111 a suggestive PD-dementia progression locus\n**Full title:** Genome-wide survival study identifies a novel synaptic locus and polygenic score for cognitive progression in Parkinson's disease\n**Authors:** Liu G, Peng J, Liao Z, et al.; Scherzer CR\n**Year:** 2021\n**Source type:** primary research — genome-wide survival analysis, longitudinal cohorts\n**Journal/source:** *Nat Genet* 2021;53(6):787-793\n**Identifier:** PMID 33958783 / PMCID PMC8459648 / DOI 10.1038/s41588-021-00847-6\n**Status:** processed\n**Record provenance:** created by `CC-20261004W7-A-REGISTRY-01` (intake wave 7 2026-10-04, Scientist A); discharges the reading debt recorded in wave 6. Provisional number.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261004-33958783-01` (supplementary data not fetched; Extended Data Fig. 5 inspected as pixels); manifest `deepdive_manifests/PMID33958783.json`; dossier `research/fulltext_dossiers/PMID33958783.md`\n**Primary pathway:** adult neurodegeneration genetics — off-genotype\n**Model/species:** human, 3,821 Parkinson's patients over 31,053 visits\n**Genotype/model:** one imputed common variant, rs8050111, risk allele frequency 0.066\n**Transferability:** none to a biallelic loss-of-function genotype class\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** The discovery source of the WWOX PD-progression SNP that LEGEND met second-hand in PMID 42135313. HR 2.12 (1.63-2.75), discovery p 1.08E-06, replication p 0.01, combined p 2.37E-08; the authors call it **suggestive** and WWOX is the nearest-gene column, with no eQTL or fine-mapping. 🔴 Extended Data Fig. 5 contradicts the sentence that calls WWOX expression neuron-specific: see `CC-20261004W7-A-NEURONSPEC-01`.\n**LIT link:** [[literature_tracking_log_current#LIT-0493]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-132",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 201]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-132",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — read at full text in intake wave 7 (2026-10-04), receipt `FTR-20261004-32368285-01`"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; provisional numbers)

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0493",
  "text": "\n## LIT-0494\n**Identifier:** PMID 32368285 / DOI 10.7150/jca.40840\n**Title:** Silencing of Wwox Increases Nuclear Import of Dvl proteins in Head and Neck Cancer\n**Authors:** Celebi A, Orhan C, Seyhan B, Buyru N\n**Year:** 2020\n**Source type:** primary research — human cell lines and tumour tissue\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-32368285-01`\n**clinical relevance:** LOW\n**Why tracked:** the one open-access primary of the three behind LEGEND's WWOX-Dvl direction; read in intake wave 7.\n**Paper link:** [[paper_registry_current#PAPER 201]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0494",
  "text": "\n## LIT-0495\n**Identifier:** PMID 42558002 / DOI 10.1002/jnr.70148\n**Title:** Astrocytes in Genetic Epilepsies: Supporting Actor or Key Player?\n**Authors:** Lange J, Zhao E, O'Connell E, Gillham O, McTague A\n**Year:** 2026\n**Source type:** review (narrative)\n**Status:** processed — `complete_fulltext_read`, receipt `FTR-20261004-42558002-01`\n**clinical relevance:** LOW\n**Why tracked:** an independent group's tabulation of the WWOX astrocyte evidence, with its own cell-autonomy verdict.\n**Paper link:** [[paper_registry_current#PAPER 202]]\n**Note:** class-level record. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0495",
  "text": "\n## LIT-0496\n**Identifier:** PMID 40937943 / DOI 10.1002/alz.70593\n**Title:** Ancestral genomic functional differences in oligodendroglia: implications for Alzheimer's disease\n**Authors:** Ramirez AM, Nasciben LB, Moura S, et al.; Vance JM\n**Year:** 2025\n**Source type:** primary research — iPSC multiome\n**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-40937943-01`\n**clinical relevance:** LOW\n**Why tracked:** the only held record quantifying WWOX transcript in human oligodendrocyte-lineage cells.\n**Paper link:** [[paper_registry_current#PAPER 203]]\n**Note:** class-level record. Not medical advice.\n"
 }
]
```

### LIT record for PMID 33958783 — conditional op

`CC-20261003W6-A-REGISTRY-01` **has landed** (seen on `main` at `70513cd`, merged into this branch at `bac93bc`): the record it proposed as `LIT-0459` is on disk as **`LIT-0493`**, `Status: discovered`, `Date processed: not yet processed`, discovered by multihop from `FTR-20261003-42135313-01`. It is therefore updated, not created, and `PAPER 204` links to it.

```json
[
 {
  "op": "replace-within",
  "id": "LIT-0493",
  "old": "**Status:** discovered",
  "new": "**Status:** processed — `partial_fulltext_read`, receipt `FTR-20261004-33958783-01`; paper record [[paper_registry_current#PAPER 204]]"
 },
 {
  "op": "replace-within",
  "id": "LIT-0493",
  "old": "**Date processed:** not yet processed",
  "new": "**Date processed:** 2026-10-04 (intake wave 7, Scientist A)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0493",
  "old": "**Next action:** read only if the PD-progression WWOX signal is ever cited in support of a WWOX-DEE statement",
  "new": "**Next action:** none — read at full text in intake wave 7. 🔴 Two qualifications the primary supplies about the signal it is cited for: its own authors call it *suggestive* (genome-wide significance only in the combined discovery-plus-replication analysis), and WWOX is the nearest-gene label of an imputed common variant with no eQTL or fine-mapping."
 }
]
```

Both `old` strings were read from the landed record with `registry_records.py get --id LIT-0493 --open-section` on 2026-10-04 at `bac93bc`; the integrator should re-verify them if further batches land first.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Identity and status propositions only; the scientific triples are in the three companion candidates.)

- (The paper's own table caption calls HET-1A an oesophageal epithelial line | `HET-1A: Human esophageal squamous epithelial cell line` | PMID32368285 Table 3 caption, `files/fulltext/PMID32368285_Celebi2020_PMC.xml`)
- (The review states its own inclusion rule and reports no new measurement | `Research papers were included on the basis that astrocyte function was investigated in models carrying known pathogenic variants.` | PMID42558002 Introduction, `files/fulltext/PMID42558002_Lange2026_PMC.xml`)
- (The oligodendroglia panel is twelve lines, four per ancestry | `We generated a total of 12 iPSC lines (four AF, four AI, and four EU) in this study` | PMID40937943 Results, `files/fulltext/PMID40937943_Ramirez2025_PMC.xml`)
- (The WWOX locus is one imputed common variant with its hazard ratio and three p values | `16 78.28 rs8050111 G 0.066 2.12 1.63–2.75 1.08 × 10−6 0.01 2.37 × 10−8 WWOX` | PMID33958783 Table 1, `files/fulltext/PMID33958783_Liu2021_PMC.xml`)


---

## BATCH DISPOSITION

**Verdict:** `PROPAGATED` by `BATCH_20261004_001` (2026-10-04, MINOR, WM_v7.13 → WM_v7.14; ACTOR_ID `scientist`, Scientist K, batch integrator).
**Surfaces written:** paper_registry_current.md · literature_tracking_log_current.md

`PAPER 201`–`204` created with `LIT-0494`–`0496`; `CORPUS-STUB-132` promoted to `PAPER 201`; `LIT-0493` (PMID 33958783) moved `discovered` → `processed`. **The provisional numbers were the applied ones** — A declared `PAPER 201`–`204` and `LIT-0494`–`0496` and `registry_records.py catalog` on `main` `520c726` confirmed `PAPER 200` / `LIT-0493` as the ceiling, so A was applied first in event order and kept its numbers.
Four integrator changes. (1) **Two stale cross-links repaired:** the candidate's `PAPER 184` and `PAPER 186`/`PAPER 185` in the `ASTROCYTE`/`NEURONSPEC` texts were wave-6-era numbers — `PAPER 184` is PMID 42422766 — and became `PAPER 202`, `204` and `203`. (2) **The literal `partial full text` was inserted beside every `partial_fulltext_read`**, because `coverage_report.PARTIAL_MARKERS` does not recognise the token on its own. (3) **The three new `LIT` rows' compound `Status` lines were split** into a bare `processed` plus a `Status note`, and given an `Evidence depth` field and the surface's own field names (`Short title`, `PAPER link`): `Title`/`Paper link` occur nowhere else in that log, and `Short title` is 475 of 475. (4) **`PAPER 202` gained `Claim links: CLAIM 005`**, the reciprocal entry owed because `CLAIM 005`'s new evidence boundary names PMID 42558002.
One deliberate omission, carried from `BATCH_20261003_005`'s decision on `LIT-0110`: **`LIT-0493` restates no depth marker**, because a registry depth declaration counts as a reading in `coverage_report.py` and `PAPER 204` already declares this PMID's depth. The row says so in its own `Status note`.
