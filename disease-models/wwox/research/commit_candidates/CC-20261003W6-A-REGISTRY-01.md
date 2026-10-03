# COMMIT CANDIDATE — CC-20261003W6-A-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist A), intake wave 6 2026-10-03, branch `task/sci-A-20261003w6`.
**context_policy:** `SOURCE_FIRST` — first pass written from each source before any registry record about it was opened; comparison afterwards (`research/intake_wave_20261003w6_A.md`).
**Not medical advice.** No individual-level record; class-level statements only.

## Target
- `paper_registry_current.md`: **create** `PAPER 168`–`PAPER 173` (six intake-wave-6 PMIDs) inserted after `PAPER 164`; promote `CORPUS-STUB-033` (two field updates).
- `literature_tracking_log_current.md`: **create** `LIT-0454`–`LIT-0458` (five PMIDs with no LIT record) and `LIT-0459` (PMID 33958783, discovered by multihop, unread) after `LIT-0453`; correct `LIT-0059` (eight field updates, including clinical relevance HIGH → LOW).

## Registry landing per PMID handled (wave-1 correction 8)
| PMID | PAPER record | LIT record | needs creation? | receipt (prepared, not appended) |
|---|---|---|---|---|
| 36291747 | `PAPER 168` (new) | `LIT-0454` (new) | yes — no record existed | `FTR-20261003-36291747-01` complete |
| 34852950 | `PAPER 169` (new; promotes `CORPUS-STUB-033`) | `LIT-0059` (exists; corrected) | PAPER yes | `FTR-20261003-34852950-01` complete |
| 42135313 | `PAPER 170` (new) | `LIT-0455` (new) | yes | `FTR-20261003-42135313-01` complete |
| 40377402 | `PAPER 171` (new) | `LIT-0456` (new) | yes | `FTR-20261003-40377402-01` partial |
| 40524961 | `PAPER 172` (new) | `LIT-0457` (new) | yes | `FTR-20261003-40524961-01` partial |
| 40507943 | `PAPER 173` (new) | `LIT-0458` (new) | yes | `FTR-20261003-40507943-01` complete |
| 33958783 | — (unread) | `LIT-0459` (new, `discovered`) | LIT only | none |

**Numbers are provisional.** Measured 2026-10-03 with `registry_records.py catalog` on `main` 59022b2: highest landed `PAPER 164`, `LIT-0453`. The open wave-5 candidate `CC-20261003W5-C-REGISTRY-01` claims `PAPER 165`–`167` (measured by `git grep` over `commit_candidates/`); wave-6 peers B and C may claim the same numbers as this candidate. The integrator renumbers in event order and updates the `PAPER 169` wikilinks in the `CORPUS-STUB-033` and `LIT-0059` ops and the `insert-after` anchors.

## Registry statements compared with the source (correction 12)
- `LIT-0059` (PMID 34852950) carried Year *unknown*, Authors *not yet extracted*, Source type *not yet screened* and **clinical relevance HIGH**. The source is a 2022 adult autopsy association study of common non-coding variants; for this disease model the relevance is LOW. Corrected below.
- `CORPUS-STUB-033` is an identity placeholder with no claim; promoted.
- No registry statement cited any of the other five PMIDs.

## Reading-debt discharge (correction 15)
None of the six papers is the primary behind an existing registry statement. Two of them re-cite primaries that are behind `DL-MOL-003` (Bouteille 2009, Celebi 2020) and one restates the axis behind `CLAIM 027`; those primaries remain unread and the consequences are carried by `CC-20261003W6-A-WNT-01` and `CC-20261003W6-A-HYAL2-01`.

## Change class
**MINOR** — paper additions, placeholder promotion, identity-field corrections and a relevance correction on a LIT record (§ 7). No claim status or working-model block changes.

## Ordering
1. `CC-20261003W5-C-REGISTRY-01` first if it is in the same batch (it creates `PAPER 165`–`167`); otherwise anchor the first insert on the highest `PAPER` then present.
2. The six receipts must be appended before this candidate is propagated.

## Op list — `paper_registry_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` on `main` 59022b2: exit 0, 8 op(s))

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 164",
  "text": "\n## PAPER 168\n**Short title:** Reinehr 2022 Biomolecules — rat autoimmune glaucoma; retinal Wwox mRNA lower (microarray probe fails FDR; qPCR 0.24-fold, n 3-4)\n**Full title:** Heat Shock Protein Upregulation Supplemental to Complex mRNA Alterations in Autoimmune Glaucoma\n**Authors:** Reinehr S, Safaei A, Grotegut P, et al.; Joachim SC\n**Year:** 2022\n**Source type:** primary research — experimental animal model (rat)\n**Journal/source:** *Biomolecules* 2022;12(10):1538\n**Identifier:** PMID 36291747 / PMCID PMC9599116 / DOI 10.3390/biom12101538\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-36291747-01`; manifest `deepdive_manifests/PMID36291747.json`; dossier `research/fulltext_dossiers/PMID36291747.md`\n**Primary pathway:** CNS injury expression (retina) — off-genotype\n**Model/species:** rat (Lewis), immune-mediated retinal ganglion cell loss\n**Genotype/model:** no WWOX genotype; acquired injury model\n**Transferability:** T4 — expression change in an acquired injury; no transfer to a loss-of-function genotype class\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** The only in-vivo record in LEGEND of Wwox expression falling in a non-genetic CNS injury. 🔴 The microarray 'fold change 0.864' is a ratio of log-scale means (linear about 0.47) and fails FDR (0.187); whole-retina qPCR 0.24-fold, p 0.002, n 3-4; mRNA only; the authors' 'regulatory role in the retina' is speculation.\n**LIT link:** [[literature_tracking_log_current#LIT-0454]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 168",
  "text": "\n## PAPER 169\n**Short title:** Dugan 2022 Neurobiol Aging — WWOX/MAF locus variants and autopsy endophenotypes (LATE-NC, HS, arteriolosclerosis)\n**Full title:** Association between WWOX/MAF variants and dementia-related neuropathologic endophenotypes\n**Authors:** Dugan AJ, Nelson PT, Katsumata Y, et al.; Fardo DW\n**Year:** 2022\n**Source type:** primary research — locus-restricted genetic association meta-analysis (two autopsy cohorts)\n**Journal/source:** *Neurobiol Aging* 2022;111:95-106\n**Identifier:** PMID 34852950 / PMCID PMC8761217 / DOI 10.1016/j.neurobiolaging.2021.10.011\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-34852950-01`; manifest `deepdive_manifests/PMID34852950.json`; dossier `research/fulltext_dossiers/PMID34852950.md`\n**Primary pathway:** adult neurodegeneration genetics — off-genotype\n**Model/species:** human, adult autopsy cohorts (European ancestry)\n**Genotype/model:** common non-coding variants; no loss-of-function allele\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Locus-wide (not genome-wide) associations with LATE-NC, hippocampal sclerosis and arteriolosclerosis. 🔴 The LATE-NC and arteriolosclerosis variants' only brain eQTL link is to MAF, not WWOX; the deposited Supplemental Table 6 (basis of 'independent of ADNC') repeats identical values across the NACC, ROSMAP and meta columns. Promotes [[paper_registry_current#CORPUS-STUB-033]].\n**LIT link:** [[literature_tracking_log_current#LIT-0059]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 169",
  "text": "\n## PAPER 170\n**Short title:** Kang 2026 npj Parkinsons Dis — multi-locus burden and dementia in PD; WWOX SNP rs8050111 one of five loci\n**Full title:** Multi-locus genetic dosage shapes cognitive disease progression in Parkinson's patients: 15-year meta-analysis of 24 cohorts\n**Authors:** Kang X, Lin Z, et al.; Scherzer CR\n**Year:** 2026\n**Source type:** primary research — multi-cohort longitudinal survival meta-analysis\n**Journal/source:** *NPJ Parkinsons Dis* 2026;12\n**Identifier:** PMID 42135313 / PMCID PMC13424109 / DOI 10.1038/s41531-026-01367-y\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-42135313-01`; manifest `deepdive_manifests/PMID42135313.json`; dossier `research/fulltext_dossiers/PMID42135313.md`\n**Primary pathway:** adult neurodegeneration genetics — off-genotype\n**Model/species:** human, adult Parkinson's disease cohorts\n**Genotype/model:** one common SNP (rs8050111), carrier vs non-carrier\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** 🔴 The 'dose' is the number of loci carried, not WWOX allele dose. WWOX HR 1.56 overall but 1.16 (n.s.) in biomarker cohorts; design-subgroup heterogeneity significant in the supplement (p 0.02) and not reported in the main text; null MMSE slope; not independent of the 2021 discovery study (PMID 33958783).\n**LIT link:** [[literature_tracking_log_current#LIT-0455]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 170",
  "text": "\n## PAPER 171\n**Short title:** Pascual 2025 Biochem J — review: excess Wnt in neurological disease; one WWOX table row\n**Full title:** Excess Wnt in neurological disease\n**Authors:** Pascual DM, Jebreili Rizi D, Kaur H, Marcogliese PC\n**Year:** 2025\n**Source type:** review\n**Journal/source:** *Biochem J* 2025;482(10):601-618\n**Identifier:** PMID 40377402 / PMCID PMC12203940 / DOI 10.1042/BCJ20240265\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-40377402-01` (all read; partial because its single WWOX source, PMID 19465938 / `FT-180`, is unread); manifest `deepdive_manifests/PMID40377402.json`; dossier `research/fulltext_dossiers/PMID40377402.md`\n**Primary pathway:** P3 — Wnt/DVL (background)\n**Model/species:** review\n**Genotype/model:** DEE28 named; no allele class\n**Transferability:** none — citation of a cancer-cell primary\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** Table 1 row: WWOX, DEE28, 'preventing the nuclear import of the Dvl proteins', citing Bouteille 2009 only; the text never discusses WWOX. Adds no evidence independent of that primary (see `CC-20261003W6-A-WNT-01`).\n**LIT link:** [[literature_tracking_log_current#LIT-0456]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 171",
  "text": "\n## PAPER 172\n**Short title:** Sengupta 2025 iScience — sterols regulate DVL2 membrane/nuclear localisation; nuclear DVL2 with inhibited TCF/LEF signalling\n**Full title:** Dishevelled localization and function are differentially regulated by structurally distinct sterols\n**Authors:** Sengupta S, Yaeger JDW, Schultz MM, May DG, Roux KJ, Francis KR\n**Year:** 2025\n**Source type:** primary research — cell, iPSC-derived NSC and mouse\n**Journal/source:** *iScience* 2025;28(6):112704\n**Identifier:** PMID 40524961 / PMCID PMC12167792 / DOI 10.1016/j.isci.2025.112704\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261003-40524961-01` (Figures 1-6 legends only; its single WWOX source, PMID 32368285, unread); manifest `deepdive_manifests/PMID40524961.json`; dossier `research/fulltext_dossiers/PMID40524961.md`\n**Primary pathway:** P3 — Wnt/DVL (background; inference check)\n**Model/species:** HEK293T; human iPSC-derived NSC; Dhcr7 mutant mouse cortex\n**Genotype/model:** no WWOX manipulation\n**Transferability:** none for WWOX data; bears on the inference step of DL-MOL-003\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** One WWOX sentence citing Celebi 2020. Its own data show DVL2 moving to the nucleus while a TCF/LEF reporter is inhibited (Fig S6E): nuclear DVL2 and canonical Wnt hyperactivation come apart in this system (see `CC-20261003W6-A-WNT-01`). WWOX absent from its TurboID dataset (detection, not interaction, evidence).\n**LIT link:** [[literature_tracking_log_current#LIT-0457]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 172",
  "text": "\n## PAPER 173\n**Short title:** Hsu 2025 IJMS — review: hyaluronan in cancer and neural disease; HYAL-2/WWOX/SMAD4 and C1q-WWOX restated\n**Full title:** Hyaluronan: An Architect and Integrator for Cancer and Neural Diseases\n**Authors:** Hsu CY, Nguyen-Tran HH, Chen YA, et al.; Chang NS\n**Year:** 2025\n**Source type:** review\n**Journal/source:** *Int J Mol Sci* 2025;26(11):5132\n**Identifier:** PMID 40507943 / PMCID PMC12155404 / DOI 10.3390/ijms26115132\n**Status:** processed\n**Record provenance:** created by `CC-20261003W6-A-REGISTRY-01` (intake wave 6 2026-10-03, Scientist A). Provisional number: the integrator renumbers if taken and updates the `LIT link`.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261003-40507943-01`; manifest `deepdive_manifests/PMID40507943.json`; dossier `research/fulltext_dossiers/PMID40507943.md`\n**Primary pathway:** ECM / HYAL-2 / SMAD4 (background)\n**Model/species:** review of DU145 prostate-cancer cell work\n**Genotype/model:** over-expression paradigm; no loss-of-function genotype\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Role:** All WWOX data re-presented are DU145 over-expression experiments from the authors' laboratory; the nervous-system section never mentions WWOX; the Alzheimer-risk sentence cites five non-Alzheimer papers; a patent is listed beside a no-conflict declaration (see `CC-20261003W6-A-HYAL2-01`).\n**LIT link:** [[literature_tracking_log_current#LIT-0458]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-033",
  "old": "**Status:** not_processed",
  "new": "**Status:** promoted — see [[paper_registry_current#PAPER 169]]"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-033",
  "old": "**Next action:** screening / triage required",
  "new": "**Next action:** none — upgraded to [[paper_registry_current#PAPER 169]] by `CC-20261003W6-A-REGISTRY-01` (receipt `FTR-20261003-34852950-01`); this placeholder is kept as history"
 }
]
```

## Op list — `literature_tracking_log_current.md` (record-scoped; dry run 2026-10-03 on `main` 59022b2: exit 0, 14 op(s))

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0453",
  "text": "\n## LIT-0454\n**Short title:** Reinehr 2022 Biomolecules — rat autoimmune glaucoma; retinal Wwox mRNA lower (microarray probe fails FDR; qPCR 0.24-fold, n 3-4)\n**Authors:** Reinehr S, Safaei A, Grotegut P, et al.; Joachim SC\n**Year:** 2022\n**Source type:** primary research — experimental animal model (rat)\n**Journal/source:** *Biomolecules* 2022;12(10):1538\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 36291747 / PMC9599116 / DOI 10.3390/biom12101538\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)\n**Date processed:** 2026-10-03\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`\n**Primary pathway:** CNS injury expression (retina) — off-genotype\n**Transferability:** T4 — expression change in an acquired injury; no transfer to a loss-of-function genotype class\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0454",
  "text": "\n## LIT-0455\n**Short title:** Kang 2026 npj Parkinsons Dis — multi-locus burden and dementia in PD; WWOX SNP rs8050111 one of five loci\n**Authors:** Kang X, Lin Z, et al.; Scherzer CR\n**Year:** 2026\n**Source type:** primary research — multi-cohort longitudinal survival meta-analysis\n**Journal/source:** *NPJ Parkinsons Dis* 2026;12\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 42135313 / PMC13424109 / DOI 10.1038/s41531-026-01367-y\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)\n**Date processed:** 2026-10-03\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`\n**Primary pathway:** adult neurodegeneration genetics — off-genotype\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0455",
  "text": "\n## LIT-0456\n**Short title:** Pascual 2025 Biochem J — review: excess Wnt in neurological disease; one WWOX table row\n**Authors:** Pascual DM, Jebreili Rizi D, Kaur H, Marcogliese PC\n**Year:** 2025\n**Source type:** review\n**Journal/source:** *Biochem J* 2025;482(10):601-618\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40377402 / PMC12203940 / DOI 10.1042/BCJ20240265\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)\n**Date processed:** 2026-10-03\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`\n**Primary pathway:** P3 — Wnt/DVL (background)\n**Transferability:** none — citation of a cancer-cell primary\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0456",
  "text": "\n## LIT-0457\n**Short title:** Sengupta 2025 iScience — sterols regulate DVL2 membrane/nuclear localisation; nuclear DVL2 with inhibited TCF/LEF signalling\n**Authors:** Sengupta S, Yaeger JDW, Schultz MM, May DG, Roux KJ, Francis KR\n**Year:** 2025\n**Source type:** primary research — cell, iPSC-derived NSC and mouse\n**Journal/source:** *iScience* 2025;28(6):112704\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40524961 / PMC12167792 / DOI 10.1016/j.isci.2025.112704\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)\n**Date processed:** 2026-10-03\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`\n**Primary pathway:** P3 — Wnt/DVL (background; inference check)\n**Transferability:** none for WWOX data; bears on the inference step of DL-MOL-003\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `partial_fulltext_read`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0457",
  "text": "\n## LIT-0458\n**Short title:** Hsu 2025 IJMS — review: hyaluronan in cancer and neural disease; HYAL-2/WWOX/SMAD4 and C1q-WWOX restated\n**Authors:** Hsu CY, Nguyen-Tran HH, Chen YA, et al.; Chang NS\n**Year:** 2025\n**Source type:** review\n**Journal/source:** *Int J Mol Sci* 2025;26(11):5132\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 40507943 / PMC12155404 / DOI 10.3390/ijms26115132\n**Date discovered:** 2026-10-03 (Orchestrator selection record, intake wave 6)\n**Date processed:** 2026-10-03\n**Discovery source:** Orchestrator selection record of intake wave 6 2026-10-03\n**Status:** processed\n**Status note:** record created by `CC-20261003W6-A-REGISTRY-01`\n**Primary pathway:** ECM / HYAL-2 / SMAD4 (background)\n**Transferability:** none to WWOX-DEE\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261003w6_A.md` · `CC-20261003W6-A-REGISTRY-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0458",
  "text": "\n## LIT-0459\n**Short title:** Liu 2021 Nat Genet — genome-wide survival study of cognitive progression in Parkinson's disease (discovery source of the WWOX SNP rs8050111)\n**Authors:** Liu G, et al.; Scherzer CR\n**Year:** 2021\n**Source type:** primary research — genome-wide survival study\n**Journal/source:** *Nat Genet* 2021;53:787-793\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 33958783 / DOI 10.1038/s41588-021-00847-6 / PMC8459648\n**Date discovered:** 2026-10-03 (reference 17 of PMID 42135313)\n**Date processed:** not yet processed\n**Discovery source:** multihop from `FTR-20261003-42135313-01`\n**Status:** discovered\n**Primary pathway:** adult neurodegeneration genetics — off-genotype\n**Transferability:** none expected to WWOX-DEE (common SNP)\n**clinical relevance:** LOW\n**Claim links:** none\n**Working Model impact:** none\n**Report mentions:** `CC-20261003W6-A-REGISTRY-01`\n**Next action:** read only if the PD-progression WWOX signal is ever cited in support of a WWOX-DEE statement\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Authors:** not yet extracted",
  "new": "**Authors:** Dugan AJ, Nelson PT, Katsumata Y, et al.; Fardo DW"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Year:** unknown",
  "new": "**Year:** 2022 (epub 2021-10-29)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Source type:** not yet screened",
  "new": "**Source type:** primary research — locus-restricted genetic association meta-analysis (two adult autopsy cohorts)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Journal/source:** not yet extracted",
  "new": "**Journal/source:** *Neurobiol Aging* 2022;111:95-106"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Date processed:** not yet processed",
  "new": "**Date processed:** 2026-10-03 (`FTR-20261003-34852950-01`, complete_fulltext_read)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Status:** discovered",
  "new": "**Status:** processed"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**clinical relevance:** HIGH",
  "new": "**clinical relevance:** LOW — common non-coding variants in adult neurodegeneration; no transfer to WWOX-DEE (corrected from HIGH by `CC-20261003W6-A-REGISTRY-01`)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0059",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** none owed; landed as [[paper_registry_current#PAPER 169]]"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
- (Supplement Table S1 gives the Wwox probe's per-animal normalised log-scale intensities (ONA 6.80, 7.36, 6.77; control 8.35, 7.56, 8.30), raw p 0.030, FDR-adjusted p 0.187 and Bonferroni p 1; the tabulated 0.864 equals the ratio of the two group means of these log-scale values (6.977 / 8.072), whose linear equivalent is about 0.47 (reader's arithmetic from these cells). | row 281 | A_64_P028011 | 6.7978751499999994 | 7.3594074000000003 | 6.774756 | 8.3509779999999996 | 7.5604937000000003 | 8.3041219999999996 | 3.0104636546742052E-2 | 0.18689652778858501 | 1 | 0.86440327705035791 | PMID 36291747, Supplement Table S1, sheet 'analysis normalized', row 281 (columns: probe, ONA 15/19/17, CO 20/16/18, p-value, p_fdr, p_bonferroni, FC ONA vs CO), `files/fulltext/PMID36291747_Reinehr2022_supplement/biomolecules-1935305-supplementary_cells.txt`)
- (Whole-retina RT-qPCR used three to four retinae per group. | Each RT-qPCR was performed in duplicates from each retina (n = 3–4/group). | PMID 36291747, Methods 2.3, `files/fulltext/PMID36291747_Reinehr2022_PMC.xml`)
- (The authors' only interpretation of Wwox is a suggested regulatory role in the retina, drawn from prior literature, not from a test in this study. | The findings of previous studies and our results have in common that loss of Wwox can affect and alter various components of the central nervous system, suggesting a regulatory role of Wwox in the retina. | PMID 36291747, Discussion, paragraph on Gdf15 and Wwox, `files/fulltext/PMID36291747_Reinehr2022_PMC.xml`)
- (Significance was a locus-wide Bonferroni threshold over effective tests (3.67e-5), not genome-wide. | The larger of these two estimates was used to compute the Bonferroni-corrected threshold for the WWOX/MAF locus +/− 250kb of 3.67×10−5 (0.05/1,364). | PMID 34852950, Results, Variant Prioritization, `files/fulltext/PMID34852950_Dugan2022_PMC.xml`)
- (Two LATE-NC variants passed the locus-wide threshold in the meta-analysis under an additive model, with odds ratios about 1.4. | Two of these variants, rs6564590 and rs7404901, were associated with LATE-NC assuming an additive MOI (OR=1.43, 95% CI: (1.22, 1.68), p=1.07×10−5 and OR=1.44, 95% CI: (1.22, 1.69), p=1.56×10−5, respectively) | PMID 34852950, Results, Variant Prioritization, `files/fulltext/PMID34852950_Dugan2022_PMC.xml`)
- (In BRAINEAC the two LATE-NC variants were nominal eQTLs for MAF, not for WWOX. | Both of the LATE-NC variants, rs6564590 and rs7404901, had nominally significant eQTL associations with MAF (brain tissue-wide p=0.040 and p=0.012, respectively) | PMID 34852950, Results, Downstream Analyses, `files/fulltext/PMID34852950_Dugan2022_PMC.xml`)
- (Only the two hippocampal-sclerosis variants were nominal eQTLs for WWOX in BRAINEAC. | The two HS variants, rs9925100 and rs9930659, had nominally significant eQTL associations for WWOX (both brain tissue-wide p-values < 3.9×10−3) | PMID 34852950, Results, Downstream Analyses, `files/fulltext/PMID34852950_Dugan2022_PMC.xml`)
- (WWOX was coded as carrier versus non-carrier of the minor allele; the burden model counts loci carried, not WWOX allele dose. | Footnotes:aBased on comparison of carriers versus non-carriers of minor allele for single-nucleotide polymorphisms in RIMS2, TMEM108, and WWOX | PMID 42135313, Table 2 footnote, `files/fulltext/PMID42135313_Kang2026_PMC.xml`)
- (For WWOX the random-effects HR is 1.56 overall but 1.16 (0.81-1.66) in biomarker cohorts, 2.30 in population-based and 1.85 (0.69-4.98) in clinical-trial cohorts. | WWOX 1.56 (1.17, 2.07) 21 1.16 (0.81, 1.66) 11 2.30 (1.38, 3.83) 6 1.85 (0.69, 4.98) 4 | PMID 42135313, Table 3, random-effects block (re-extracted cell-wise), `files/fulltext/PMID42135313_Kang2026_PMC.xml`)
- (The WWOX forest plot's own test for subgroup differences by study design is significant (random effects p = 0.02), and its legend is numbered Supplementary Figure 4, not S3. | Test for subgroup differences (random effects): χ2 2= 7.42, df = 2 (p = 0.02) Supplementary Figure 4. Forest plot of associations between rs8050111 in the WWOX locus | PMID 42135313, Supplement, WWOX forest plot and its legend (vector text layer), `files/fulltext/PMID42135313_Kang2026_supplement/41531_2026_1367_MOESM1_ESM.txt`)
- (Fifteen of the 24 cohorts were harmonised in the authors' earlier work, so the WWOX estimate is not independent of its discovery data. | We previously reported data harmonization for 15 of the cohorts here included in refs. | PMID 42135313, Methods, Cohorts and study participants, `files/fulltext/PMID42135313_Kang2026_PMC.xml`)
- (The review's only WWOX statement is a Table 1 row assigning DEE28 the Wnt role of preventing nuclear import of Dvl proteins, cited to ref 63. | WWOX Developmental and epileptic encephalopathy 28 AR 616,211 Preventing the nuclear import of the Dvl proteins [63] | PMID 40377402, Table 1, WWOX row, `files/fulltext/PMID40377402_Pascual2025_PMC.xml`)
- (Ref 63 is the 2009 Oncogene paper on WWOX inhibition of the Wnt/beta-catenin pathway (PMID 19465938). | Inhibition of the Wnt/beta-catenin pathway by the WWOX tumor suppressor protein Oncogene 28 2569 2580 | PMID 40377402, References, ref 63, `files/fulltext/PMID40377402_Pascual2025_PMC.xml`)
- (The paper's only WWOX statement is one discussion sentence citing a head-and-neck cancer study (ref 79). | It has been shown that silencing of the Wwox tumor suppressor increases nuclear DVL2 in head and neck cancer.79 | PMID 40524961, Discussion, paragraph on DVL2 protein-protein interactions, `files/fulltext/PMID40524961_Sengupta2025_PMC.xml`)
- (Under the same conditions that put DVL2 in the nucleus, a TCF/LEF reporter showed canonical Wnt signalling inhibited, which the authors read as nuclear DVL acting independently of beta-catenin. | Our findings show a clear inhibition of canonical Wnt signaling in response to cholesterol inhibited conditions (Figure S6E),30,31 suggesting nuclear DVL is functioning in a β-catenin independent manner. | PMID 40524961, Results, DVL2 localisation (Figure S6E), `files/fulltext/PMID40524961_Sengupta2025_PMC.xml`)
- (The HYAL-2/WWOX/SMAD4 experiment re-presented in Figure 1 used transfected tagged constructs in DU145 prostate cancer cells. | (A,B) WWOX functional prostate DU145 cells were transfected with three indicated expression plasmids tagged with ECFP, EGFP, or DsRedl and then added native HA. | PMID 40507943, Figure 1 legend, `files/fulltext/PMID40507943_Hsu2025_PMC.xml`)
- (The authors state that whether the HYAL-2/WWOX/SMAD4 complex is overexpressed in vivo is unknown. | Whether the HYAL-2/WWOX/SMAD4 complex is overexpressed in vivo is unknown. | PMID 40507943, Section 6.6, `files/fulltext/PMID40507943_Hsu2025_PMC.xml`)
- (The review calls WWOX a risk factor for Alzheimer's disease, citing refs 5, 29, 204, 205 and 206. | WWOX is a known tumor suppressor and is a risk factor for Alzheimer’s disease [5,29,204,205,206]. | PMID 40507943, Section 6.1, `files/fulltext/PMID40507943_Hsu2025_PMC.xml`)
