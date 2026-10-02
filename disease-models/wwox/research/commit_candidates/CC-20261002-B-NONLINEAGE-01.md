# COMMIT CANDIDATE — CC-20261002-B-NONLINEAGE-01

**Candidate ID:** CC-20261002-B-NONLINEAGE-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** scientist-b (ACTOR_ID `scientist`), intake wave 2026-10-02, branch `task/sci-B-20261002`.
**context_policy:** `SOURCE_FIRST` for the readings; this candidate was written after
`FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` (see
`disease-models/wwox/research/intake_wave_20261002_B.md`).
**Change class:** **MINOR** (prompt_batch_commit §7). No `consolidated baseline` claim is narrowed or reversed; no
claim text changes; no working-model change. The ops correct triage metadata and one research-queue sentence.
**Readings:** receipts prepared as `FTR-20261002-25537520-01`, `FTR-20261002-28763065-01`,
`FTR-20261002-41378749-01` (JSON files `sciB_25537520_1.json`, `sciB_28763065_1.json`, `sciB_41378749_1.json`,
not appended at preparation time — the integrator names the event IDs it appends).
**Not medical advice.**

---

## 1 · Why

1. `CORPUS P263` / `LIT-0263` (PMID 25537520, Chang 2014 review) were never read and carry triage metadata that the
   reading falsifies: **primary pathway "P6 — DDR / genome stability"** (the review is about neuronal injury,
   tau/GSK-3β, TGF-β/TIAF1 and neurodevelopment; it never discusses DNA damage) and **species "rat"** (a review of
   human, mouse, rat and Drosophila literature; no primary data). The record should also say that the review is a
   provenance map whose Chang-lineage statements are single-laboratory, so nobody later cites its sentences as
   independent support.
2. `FT-142` says of PMID 28763065 and PMID 41378749: *"Neither paper is a WWOX paper."* Both papers report a
   WWOX-locus association in their abstracts and main tables (an intronic SNP sub-threshold for infant white-matter
   volume; three imputed intronic SNPs nominally associated with spina bifida). They are not WWOX-**function**
   papers, and neither result is a finding; but "not a WWOX paper" is a negative that hides a WWOX-locus statement,
   the kind of silent negative `epistemic_discipline.md` §2 warns about.

## 2 · Ops

Record-scoped, one op per statement (`prompt_batch_commit.md` §4.0). Every `old` was measured unique **in its
record** (count 1 in the record span; command: a span count over the record lines returned by
`registry_records.py get --id`, 2026-10-02).

### 2.1 `disease-models/wwox/registries/paper_registry_current.md` — record `CORPUS P263`

| # | op | old (verbatim, unique in record) | new |
|---|---|---|---|
| P1 | replace-within | `**Status:** screened — corpus placeholder` | `**Status:** read — partial full text (FTR-20261002-25537520-01; figures captions only) — no claim promoted` |
| P2 | replace-within | `**Primary pathway:** P6 — DDR / genome stability` | `**Primary pathway:** review — neuronal injury, tau/GSK-3β, TGF-β/TIAF1, neurodevelopment (triage value "P6 — DDR / genome stability" corrected 2026-10-02 by CC-20261002-B-NONLINEAGE-01)` |
| P3 | replace-within | `**Model/species:** rat` | `**Model/species:** review — secondary source, no primary data (triage value "rat" corrected 2026-10-02 by CC-20261002-B-NONLINEAGE-01)` |
| P4 | replace-within | `**Note:** FASE 1 triage 221–400 — no deep-dive performed.` | `**Note:** FASE 1 triage 221–400. Read 2026-10-02 (dossier fulltext_dossiers/PMID25537520.md): a provenance map, not evidence. Its epilepsy and developmental sentences rest on PMID 24369382, PMID 24456803 and PMID 19500159, each held from the primary; its tau-inhibitor, TIAF1 (cited as "unpublished") and in-vivo transcription-factor statements are the authors' own laboratory, and its Conclusion asserts in-vivo transcription-factor control that its own body says "remains to be established". Do not cite its sentences as independent support.` |

### 2.2 `disease-models/wwox/registries/literature_tracking_log_current.md` — record `LIT-0263`

| # | op | old (verbatim, unique in record) | new |
|---|---|---|---|
| L1 | replace-within | `**Date processed:** triage only` | `**Date processed:** 2026-10-02 (partial full text; FTR-20261002-25537520-01)` |
| L2 | replace-within | `**Status:** screened` | `**Status:** background_only` |
| L3 | replace-within | `**Primary pathway:** P6 — DDR / genome stability` | `**Primary pathway:** review — neuronal injury, tau/GSK-3β, TGF-β/TIAF1, neurodevelopment (corrected 2026-10-02 from "P6 — DDR / genome stability", CC-20261002-B-NONLINEAGE-01)` |
| L4 | replace-within | `**Species:** rat` | `**Species:** review — secondary source (corrected 2026-10-02 from "rat", CC-20261002-B-NONLINEAGE-01)` |
| L5 | replace-within | `**Current status:** screened — B` | `**Current status:** background_only — provenance map, read in full except the four schematic figure images; no claim link` |
| L6 | replace-within | `**Next action:** full-text retrieval; depth pass if model-shifting` | `**Next action:** none for evidence; figure images owed for a complete read (PMC CDN or Europe PMC bundle)` |

`background_only` is in the log's own `## Status vocabulary` ("Archived as context, no operative function").
`processed` was rejected because the vocabulary defines it as "Fully read", and the figure images are still owed.

### 2.3 `disease-models/wwox/research/full_text_queue_current.md` — record `FT-142` (research layer)

| # | op | old (verbatim, unique in record and file) | new |
|---|---|---|---|
| Q1 | replace-within | `⚠️ **Neither paper is a WWOX paper.**` | `⚠️ **Neither paper is a WWOX-function paper — but both report a WWOX-locus association** (narrowed 2026-10-02 from "Neither paper is a WWOX paper.", CC-20261002-B-NONLINEAGE-01): PMID 28763065, rs10514437 (WWOX intron, genotyped, MAF 0.03) with infant white-matter volume, P 1.56e-8 against a study threshold of 1.25e-8, unreplicated, minor allele associated with *more* white matter; PMID 41378749, three imputed WWOX intron-8 SNPs nominally associated with spina bifida (OR about 6.2, p 2.2e-6, suggestive threshold only), absent from the technical replication. Neither is a finding. Both read 2026-10-02 (FTR-20261002-28763065-01, partial; FTR-20261002-41378749-01, complete).` |

The record's next sentence ("They are queued as developmental-timing context, and must never be cited as WWOX
evidence") stays: it is still correct.

## 3 · What this candidate does NOT do

- It adds no claim and moves no claim status. None of the five readings of this wave supports a canonical claim
  change (see the analysis note, §5).
- It does not create paper-registry records for PMID 37501399, 28763065, 41378749 or 31315632. Whether nominal or
  null readings get `PAPER` records is the integrator's call; the dossiers and manifests carry them meanwhile.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (The review's body says in-vivo transcription-factor regulation in neuronal survival or death is not established | Whether WWOX regulates the function of transcription factors in neuronal survival or death in vivo remains to be established. | PMID 25537520, "WWOX in neuronal death signaling", para 1)
- (The review's Conclusion asserts substantial in-vivo evidence for transcription-factor control | In conclusion, substantial evidence has shown that WWOX participates in the control of the function of transcription factors in vivo. | PMID 25537520, Conclusion and perspectives)
- (The review supports the WWOX–TIAF1 interaction with unpublished data | WWOX is able to interact with TIAF1 (Chang et al., unpublished) | PMID 25537520, "WWOX in neurological disease pathology", para 3)
- (The review's neurodegeneration-inhibitor statement rests on the authors' own work | We have shown that WWOX is an inhibitor of neurodegeneration, because of its interaction with tau | PMID 25537520, Introduction, para 2)
- (The review's statement on WWOX downregulation in AD cites only reviews | and that downregulation of WWOX in AD causes neuronal damage | PMID 25537520, "WWOX in metabolic syndrome and neural development", para 3)
- (The infant GWAS's WWOX SNP fell short of the study's genome-wide threshold for white matter | An intronic SNP in WWOX (rs10514437) fell just short of genome-wide significance for WM | PMID 28763065, Results, para 1)
- (rs10514437 is genotyped, not imputed | Note that all SNPs are imputed with the exception of rs10514437 | PMID 28763065, Table 1 footnote)
- (rs10514437 was not tested in either comparison cohort | rs10514437 WWOX -6617 1.56E-08 NA NA NA | PMID 28763065, Supplementary Table 10)
- (The G allele of rs10514437 is the common allele | rs10514437 G A 0.03 0.97 0.98 0.83 1.00 0.98 0.95 | PMID 28763065, Supplementary Table 8)
- (A1, the allele the effect is given for, is the effective allele | A1 is the effective allele and A2 is the reference allele. Diff./allele is the ratio of effect size over mean brain volume. | PMID 28763065, Table 1 footnote)
- (The spina-bifida WWOX variants are intronic | Three variants on chromosome 16 were within the 8th intron of WWOX | PMID 41378749, Results, Association Without Folate)
- (Multiple testing was handled only by a suggestive threshold | We addressed multiple comparisons by only considering loci above the suggestive threshold | PMID 41378749, Methods, Association Studies)
- (The technical replication replicated two other loci | Two previously identified nominal loci were replicated using the imputed dosages computed on the Michigan Imputation Server | PMID 41378749, Results, Technical Replication Results)
