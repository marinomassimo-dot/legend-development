# COMMIT CANDIDATE — CC-20261002-INTAKE-WAVE-ORPHANS-01

**Candidate ID:** CC-20261002-INTAKE-WAVE-ORPHANS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist E), batch integrator of the 2026-10-02 intake wave,
branch `task/batch-20261002-intake-2`.
**Change class:** **MINOR** — paper additions and triage-metadata corrections (`prompt_batch_commit.md`
§7). It creates no claim, moves no claim status, redefines no working-model block, narrows and
reverses nothing.
**Not medical advice.** Class-level records from public literature only.

---

## 1 · Why this candidate exists

The seven authored candidates of this wave leave four of the wave's seventeen readings with **no
structured landing** — a PMID and a real record ID in the same Markdown section, which is what
`session_self_eval.has_structured_landing` requires and what `legend_lint.py` enforces as
`ORPHAN_COMPLETE_READ` → `BLOCK_BATCH_COMMIT` for a `complete_fulltext_read`.

Measured on this branch at `main` f5f9468:

```
python3 framework/scripts/legend_lint.py .        # exit 2, VERDICT: BLOCK_BATCH_COMMIT
  ORPHAN_COMPLETE_READ: FTR-20261002-29390993-01 (PMID 29390993)
  ORPHAN_COMPLETE_READ: FTR-20261002-24949445-01 (PMID 24949445)
  ORPHAN_COMPLETE_READ: FTR-20261002-31315632-01 (PMID 31315632)
  ORPHAN_COMPLETE_READ: FTR-20261002-37501399-01 (PMID 37501399)
```

`CC-20261002-INTAKE-A-REGISTRY-01` lands the first two (`PAPER 121`, `PAPER 122`). The other two
are landed here. `CC-20261002-B-NONLINEAGE-01` § 3 states explicitly that it creates no `PAPER`
record for PMID 37501399, 28763065, 41378749 or 31315632.

Per-PMID landing state after the seven candidates, measured with
`python3 framework/scripts/registry_records.py get --pmid <P> --hops 0 --json` (2026-10-02):

| PMID | Landing after the seven | This candidate |
|---|---|---|
| 30746283 · 37095367 · 29390993 · 24949445 · 40191585 · 32081867 | `PAPER 119`–`124`, `LIT-0421`–`0425`, `CORPUS P253`/`LIT-0253` | — |
| 25537520 | `CORPUS P263` / `LIT-0263` (updated by B) | — |
| 28763065 · 41378749 | `FT-142`, same section as both PMIDs (narrowed by B) | — |
| 42395553 | `FT-047`, same section as the PMID | — |
| 37781246 | `DL-MECH-053` / `DL-MECH-054`, same section as the PMID | — |
| **37501399** | **none** | `PAPER 125` · `LIT-0426` |
| **31315632** | **none** | `PAPER 126` · `LIT-0427` |
| **34204789** | **none** | `PAPER 127` · `LIT-0428` |
| **17679088** | **none** | `PAPER 128` · `LIT-0429` |
| 33195192 | `CORPUS-STUB-083` / `LIT-0106`, both `not_processed` / `discovered` | promoted: `PAPER 129`, stub and `LIT-0106` annotated |
| 37897534 | `CORPUS-STUB-077` / `LIT-0100`, both `not_processed` / `discovered` | promoted: `PAPER 130`, stub and `LIT-0100` annotated |

The last two are not orphans — they already have a landing — but their triage records say
`not_processed` / `discovered`, which this wave's readings make false. Promoting the existing
placeholder is the cheaper route than a second record, and it follows the pattern
`CC-20261002-INTAKE-A-REGISTRY-01` uses for `CORPUS P253`: the placeholder is kept as history and
carries a sentence pointing at its promotion.

**Numbers are provisional**, re-measured on this branch with
`python3 framework/scripts/registry_records.py catalog --source paper_registry_current` and
`… --source literature_tracking_log_current`: live highest `PAPER 118`, `LIT-0420`, so
`PAPER 119`–`124` / `LIT-0421`–`0425` go to Scientist A's candidate and this one takes
`PAPER 125`–`130` / `LIT-0426`–`0429`.

## 2 · Reading depth is carried as it was measured, never upgraded

Each receipt's own `evidence_depth` (`python3 framework/scripts/fulltext_receipts.py status --pmid <P>`,
2026-10-02) is what the record states. **Not one record of this candidate declares `full text
reviewed`**, and the three partial ones name what is still owed:

| PMID | Receipt | `evidence_depth` | What is owed |
|---|---|---|---|
| 37501399 | `FTR-20261002-37501399-01` | `complete_fulltext_read` | — |
| 31315632 | `FTR-20261002-31315632-01` | `complete_fulltext_read` | — |
| 34204789 | `FTR-20261002-34204789-01` | `partial_fulltext_read` | figure panels, supplement |
| 17679088 | `FTR-20261002-17679088-01` | `partial_fulltext_read` | figure panels, supplement |
| 33195192 | `FTR-20261002-33195192-01` | `partial_fulltext_read` | figure panels (incl. Suppl. Fig. S9), supplement |
| 37897534 | `FTR-20261002-37897534-01` | `partial_fulltext_read` | figure panels, supplement |

## 3 · Op list — `paper_registry_current.md` (record-scoped)

```json
[
 {
  "op": "insert-after",
  "id": "PAPER 124",
  "text": "\n## PAPER 125\n**Short title:** Yang 2023 Zoological Research — marmoset colony WGS; a 17-SNP intronic WWOX haplotype suggestively associated with handling-evoked seizures\n**Full title:** Population genetics of marmosets in Asian primate research centers and loci associated with epileptic risk revealed by whole-genome sequencing\n**Authors:** Yang X et al.\n**Year:** 2023\n**Source type:** primary research — population-genetics WGS with pedigree association\n**Journal/source:** *Zoological Research* 2023;44(5):837-847\n**Identifier:** PMID 37501399 / PMCID PMC10559097 / DOI 10.24272/j.issn.2095-8137.2022.514\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator) to land a reading that `CC-20261002-B-NONLINEAGE-01` § 3 deliberately left without a registry record.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-37501399-01`; manifest `deepdive_manifests/PMID37501399.json`; dossier `research/fulltext_dossiers/PMID37501399.md`\n**Primary pathway:** non-lineage association signals / intron 8\n**Model/species:** common marmoset (*Callithrix jacchus*), 38 animals in two captive colonies\n**Genotype/model:** no WWOX copy-number event; 17 intronic SNPs on one haplotype in the last intron of the marmoset WWOX model transcript\n**Transferability:** T3 (non-coding primate association; no WWOX function measured)\n**clinical relevance:** BACKGROUND — an earned near-null, recorded so it is not later counted as primate evidence that WWOX variation causes epilepsy\n**Claim links:** none — `CLAIM 037` is explicitly untouched (`research/intake_wave_20261002_B.md` § 2)\n**Role:** 🔴 The abstract's deletion sentence is about a **KCTD18-like** CNV, not WWOX: the CNV tables hold no WWOX event. The WWOX signal is SNP-only, suggestive (LAMP P 2.4e-6 to 9.2e-6 against a 1e-5 threshold), with λ 0.825, carriers among unaffected animals in one colony, and no genome-wide signal by the authors' own statement. Annotated into `DL-MECH-107` by `CC-20261002-B-INTRON8-01` as **not** convergence.\n**LIT link:** [[literature_tracking_log_current#LIT-0426]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 125",
  "text": "\n## PAPER 126\n**Short title:** Chou 2019 Cell Commun Signal — p53/TIAF1/WWOX triad; the brain-aggregation statement rests on one xenograft arm\n**Full title:** A p53/TIAF1/WWOX triad exerts cancer suppression but may cause brain protein aggregation due to p53/WWOX functional antagonism\n**Authors:** Chou PY, Lin SR, Lee MH et al.\n**Year:** 2019\n**Source type:** primary research — cell and xenograft study\n**Journal/source:** *Cell Commun Signal* 2019;17:76\n**Identifier:** PMID 31315632 / PMCID PMC6637503 / DOI 10.1186/s12964-019-0382-y\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator) to land a reading that `CC-20261002-B-NONLINEAGE-01` § 3 deliberately left without a registry record.\n**Evidence depth:** `complete_fulltext_read` — receipt `FTR-20261002-31315632-01`; manifest `deepdive_manifests/PMID31315632.json`; dossier `research/fulltext_dossiers/PMID31315632.md`\n**Primary pathway:** aggregation / TIAF1 lineage\n**Model/species:** cell lines plus nude-mouse xenograft (Wwox-intact)\n**Genotype/model:** no WWOX-DEE genotype; overexpression and knockdown in tumour lines\n**Transferability:** T3 (tumour-bearing mice with intact Wwox; no neural WWOX-loss arm)\n**clinical relevance:** BACKGROUND — an earned null for the brain\n**Claim links:** none — `CLAIM 003`, `CLAIM 006`, `CLAIM 030`, `CLAIM 037` are all untouched by this reading\n**Role:** 🔴 Single-laboratory lineage, not independent support: 26 of 56 references, and all six behind the brain-aggregation background sentence, are the same laboratory, and `WWOX AND TIAF1 NOT Chang NS[au]` returns 0 on PubMed. The brain statement rests on **one** xenograft experiment, one lane per condition, with non-reducing blots in which the α-tubulin housekeeping control also aggregates; the authors state the mechanism is unknown, and the SDR-vs-WW binding account contradicts itself inside the paper. It down-weights nothing and adds no independent replication to `DL-BIO-004`.\n**LIT link:** [[literature_tracking_log_current#LIT-0427]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 126",
  "text": "\n## PAPER 127\n**Short title:** Kałuzińska 2021 Cancers — PLEK2/RRM2/GCSH, a 'WWOX-dependent' glioma triad defined by a correlation, not a perturbation\n**Full title:** PLEK2, RRM2, GCSH: A Novel WWOX-Dependent Biomarker Triad of Glioblastoma at the Crossroads of Cytoskeleton Reorganization and Metabolism Alterations\n**Authors:** Kałuzińska Ż et al.\n**Year:** 2021\n**Source type:** primary research — bioinformatic analysis of public bulk tumour expression data\n**Journal/source:** *Cancers* 2021;13(12):2955\n**Identifier:** PMID 34204789 / PMCID PMC8231639 / DOI 10.3390/cancers13122955\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator); the reading's own candidate, `CC-20261002-BIOMARKER-REJECTIONS-01`, records the rejection and creates no registry record.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-34204789-01`; manifest `deepdive_manifests/PMID34204789.json`; dossier `research/fulltext_dossiers/PMID34204789.md`. Figure panels and supplement are **not** read and are owed.\n**Primary pathway:** biomarkers (rejected)\n**Model/species:** human bulk tumour RNA-seq (672 samples, public data)\n**Genotype/model:** none — WWOX is a stratifying variable, never a manipulated one\n**Transferability:** T3 (glioma classification; no neural WWOX-loss system)\n**clinical relevance:** BACKGROUND — recorded so the title is not transferred to this model\n**Claim links:** none — the rejection is `DIS-026` (`CC-20261002-BIOMARKER-REJECTIONS-01`)\n**Role:** 🔴 *«WWOX-dependent»* here means a cut-point on WWOX transcript abundance (222.6) plus a Spearman correlation (|R| 0.42–0.44). **There is no knockdown, no overexpression, no rescue and no protein measurement in the study**, so none of the three genes is a readout of a WWOX state. The authors do not overclaim: *«usefulness of PLEK2 , RRM2 , and GCSH as diagnostic or predictive biomarkers is yet to be confirmed»*. Same department as `PAPER 128`'s companion reading PMID 37781246 (Bednarek, Łódź) — the two are not independent.\n**LIT link:** [[literature_tracking_log_current#LIT-0428]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 127",
  "text": "\n## PAPER 128\n**Short title:** Zhang & Freudenreich 2007 Mol Cell — the FRA16D Flex1 AT-repeat stalls replication forks and breaks chromosomes in yeast\n**Full title:** An AT-rich sequence in human common fragile site FRA16D causes fork stalling and chromosome breakage in *S. cerevisiae*\n**Authors:** Zhang H, Freudenreich CH\n**Year:** 2007\n**Source type:** primary research — yeast genetics / replication\n**Journal/source:** *Mol Cell* 2007;27(3):367-379\n**Identifier:** PMID 17679088 / PMCID PMC2144737 / DOI 10.1016/j.molcel.2007.06.012\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator); `CC-20261002-BIOMARKER-REJECTIONS-01` § 4 states deliberately that this paper is **not** entered in the biomarker ledger in either direction.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-17679088-01`; manifest `deepdive_manifests/PMID17679088.json`; dossier `research/fulltext_dossiers/PMID17679088.md`. Figure panels and supplement are **not** read and are owed.\n**Primary pathway:** locus fragility / FRA16D architecture\n**Model/species:** *Saccharomyces cerevisiae* (often `rad52Δ`/`rad50Δ`, with hydroxyurea)\n**Genotype/model:** none — a human DNA sequence element assayed in yeast; no WWOX protein, transcript or function is measured\n**Transferability:** T3 — **OFF-AXIS for the assigned hypothesis.** Every measurement is somatic and mitotic, and the authors' own prediction terminates in *«cancer-causing rearrangements»*; it supports no statement about germline exon-scale deletions or about why one allele class is deleted. *«WWOX»* occurs 9 times in 189,143 bytes.\n**clinical relevance:** BACKGROUND — a mechanistic precedent, not evidence about WWOX\n**Claim links:** none\n**Role:** What transfers is one mechanistic precedent: FRA16D carries a characterised replication-barrier element (Flex1; Flex4 and Flex5-p do **not** increase fragility), which is a real reason this locus is rearrangement-prone. 🔴 The paper never states which WWOX intron or exon Flex1 lies in — the fact the hypothesis would turn on is absent from the body. Carried as `LEAD-C1` (Flex1 AT-repeat length as a candidate rearrangement-risk covariate, `IPOTESI`, blocked on acquiring Finnis 2005) in `research/intake_wave_20261002_C.md` § 4, and as neither a biomarker nor a rejected biomarker.\n**LIT link:** [[literature_tracking_log_current#LIT-0429]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 128",
  "text": "\n## PAPER 129\n**Short title:** Chou 2020 Front Cell Dev Biol — `Wwox−/−` mouse skin; pERK and total ERK1/2 reduced in keratinocytes\n**Full title:** Wwox Deficiency Causes Downregulation of Prosurvival ERK Signaling and Abnormal Homeostatic Responses in Mouse Skin\n**Authors:** Chou PY et al.\n**Year:** 2020\n**Source type:** primary research — constitutive knockout mouse tissue study\n**Journal/source:** *Front Cell Dev Biol* 2020;8:558432\n**Identifier:** PMID 33195192 / PMCID PMC7652735 / DOI 10.3389/fcell.2020.558432\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator), promoting the corpus placeholder `CORPUS-STUB-083`, which is kept as history.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-33195192-01`; manifest `deepdive_manifests/PMID33195192.json`; dossier `research/fulltext_dossiers/PMID33195192.md`. Figure panels and the supplement — including Supplementary Figure S9, which carries the total-ERK half of the result — are **not** read and are owed.\n**Primary pathway:** ERK signalling / tissue homeostasis\n**Model/species:** mouse (constitutive `Wwox−/−` and littermates), HaCaT cells\n**Genotype/model:** constitutive null; **no** overexpression arm (loss of function only)\n**Transferability:** T2 for the perturbation, T3 for the tissue — keratinocytes, hair follicles, dermis and fat; **no neural tissue anywhere in the paper**\n**clinical relevance:** MODERATE — the one WWOX-dependence in this wave shown by a real perturbation, in a tissue a living patient can be biopsied from\n**Claim links:** none — `CLAIM 011` is annotated by `CC-20261002-WWOX-DOSE-CEILING-01`, which cites this paper for a two-sided statement about level, not as support\n**Role:** Supplies two things and no more. (a) The pERK observation (*«keratinocytes expressed significantly reduced levels of pERK and total ERK1/2 protein»*, IHC over 25 regions from 3 mice), **rejected as a disease biomarker on specificity and retained by name only as a possible pharmacodynamic readout inside a controlled system** — `DIS-027`. (b) The explicit statement *«A certain amount of WWOX expression may be necessary for maintaining normal physiological functions in cells»*, with raised WWOX increasing proliferation in HT29 **cited from Nowakowska 2014, which is unread**. 🔴 Same Tainan laboratory and same knockout line as `PAPER 130`: the two are one group, not two.\n**LIT link:** [[literature_tracking_log_current#LIT-0106]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "insert-after",
  "id": "PAPER 129",
  "text": "\n## PAPER 130\n**Short title:** Cheng 2023 Cell Mol Life Sci — `Wwox` loss, senescence escape and genome instability in MEFs and fibroblasts\n**Full title:** Loss of the fragile WWOX gene leads to senescence escape and genome instability\n**Authors:** Cheng YY et al.\n**Year:** 2023\n**Source type:** primary research — knockout and knockdown cell study\n**Journal/source:** *Cell Mol Life Sci* 2023;80(11):338\n**Identifier:** PMID 37897534 / PMCID PMC10613160 / DOI 10.1007/s00018-023-04950-1\n**Status:** processed\n**Record provenance:** created by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (intake wave 2026-10-02, batch integrator), promoting the corpus placeholder `CORPUS-STUB-077`, which is kept as history.\n**Evidence depth:** `partial_fulltext_read` — receipt `FTR-20261002-37897534-01`; manifest `deepdive_manifests/PMID37897534.json`; dossier `research/fulltext_dossiers/PMID37897534.md`. Figure panels and the supplement are **not** read and are owed.\n**Primary pathway:** senescence / genome instability / redox\n**Model/species:** mouse embryonic fibroblasts, HEK293T, human dermal fibroblasts — **no neural and no in vivo arm**\n**Genotype/model:** `Wwox−/−` knockout plus knockdown; ⚠️ the comparator in most figures is `Wwox+/−`, **not** wild type\n**Transferability:** T2 for the perturbation, T3 for the phenotype (culture passages 20–30)\n**clinical relevance:** MODERATE — carries one therapeutic-direction lead and four rejected biomarker candidates\n**Claim links:** none — adjacent to `CLAIM 009` (redox, *in observation*) and `CLAIM 034` and resolving neither\n**Role:** Source of `DIS-028` (γ-H2AX rejected as a WWOX readout because it rises both when WWOX is **lost**, here, and when WWOX is **added**, PMID 42395553 — the two papers do not cite each other, and the observation belongs to reading them together) and of `DIS-029` (SA-β-gal, p16/p21/p27 and microsatellite instability rejected as generic and unsamplable). The **NAC rescue** — *«during the passage culture prevented microsatellite instability and resulted in senescence induction in the late-passage Wwox −/− MEFs»* — is carried as `LEAD-C2` (`IPOTESI`) in `research/intake_wave_20261002_C.md` § 4 and is **deliberately not promoted**: it is a fibroblast-culture result with no neural and no in vivo arm. 🔴 Same laboratory and knockout line as `PAPER 129`.\n**LIT link:** [[literature_tracking_log_current#LIT-0100]]\n**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.\n"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-083",
  "old": "**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.",
  "new": "**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. **Promoted 2026-10-02 to [[paper_registry_current#PAPER 129]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (first-hand `partial_fulltext_read`, receipt `FTR-20261002-33195192-01`); this placeholder is kept as history and its `Status: not_processed` describes the placeholder, not the paper.**"
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-077",
  "old": "**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.",
  "new": "**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record. **Promoted 2026-10-02 to [[paper_registry_current#PAPER 130]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01` (first-hand `partial_fulltext_read`, receipt `FTR-20261002-37897534-01`); this placeholder is kept as history and its `Status: not_processed` describes the placeholder, not the paper.**"
 }
]
```

## 4 · Op list — `literature_tracking_log_current.md` (record-scoped)

`Status` values are taken from the log's own `## Status vocabulary`. `processed` is used with an
explicit `partial_fulltext_read` in `Evidence depth` and the owed surfaces named — the shape
`LIT-0420`, `LIT-0056` and `CC-20261002-INTAKE-A-REGISTRY-01` already use. No record says
*fully read* for a partial reading.

```json
[
 {
  "op": "insert-after",
  "id": "LIT-0425",
  "text": "\n## LIT-0426\n**Short title:** Yang 2023 Zoological Research — marmoset colony WGS; a 17-SNP intronic WWOX haplotype suggestively associated with handling-evoked seizures\n**Authors:** Yang X et al.\n**Year:** 2023\n**Source type:** primary research — population-genetics WGS with pedigree association\n**Journal/source:** *Zoological Research* 2023;44(5):837-847\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 37501399 / DOI 10.24272/j.issn.2095-8137.2022.514 / PMC10559097\n**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)\n**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-37501399-01`)\n**Discovery source:** Orchestrator selection record of intake wave 2026-10-02\n**Status:** processed\n**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Primary pathway:** non-lineage association signals / intron 8\n**Species:** common marmoset (*Callithrix jacchus*)\n**Transferability:** T3 (non-coding primate association; no WWOX function measured)\n**clinical relevance:** BACKGROUND — an earned near-null\n**Claim links:** none — `CLAIM 037` explicitly untouched\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-B-INTRON8-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID37501399.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0426",
  "text": "\n## LIT-0427\n**Short title:** Chou 2019 Cell Commun Signal — p53/TIAF1/WWOX triad; the brain-aggregation statement rests on one xenograft arm\n**Authors:** Chou PY, Lin SR, Lee MH et al.\n**Year:** 2019\n**Source type:** primary research — cell and xenograft study\n**Journal/source:** *Cell Commun Signal* 2019;17:76\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 31315632 / DOI 10.1186/s12964-019-0382-y / PMC6637503\n**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)\n**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-31315632-01`)\n**Discovery source:** Orchestrator selection record of intake wave 2026-10-02\n**Status:** processed\n**Status note:** `complete_fulltext_read`; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Primary pathway:** aggregation / TIAF1 lineage\n**Species:** mouse xenograft (Wwox-intact) and human cell lines\n**Transferability:** T3 (no neural WWOX-loss arm)\n**clinical relevance:** BACKGROUND — an earned null for the brain; single-laboratory lineage\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261002_B.md` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Next action:** none owed\n**Evidence depth:** `complete_fulltext_read` — manifest `deepdive_manifests/PMID31315632.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0427",
  "text": "\n## LIT-0428\n**Short title:** Kałuzińska 2021 Cancers — PLEK2/RRM2/GCSH, a 'WWOX-dependent' glioma triad defined by a correlation, not a perturbation\n**Authors:** Kałuzińska Ż et al.\n**Year:** 2021\n**Source type:** primary research — bioinformatic analysis of public bulk tumour expression data\n**Journal/source:** *Cancers* 2021;13(12):2955\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 34204789 / DOI 10.3390/cancers13122955 / PMC8231639\n**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)\n**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-34204789-01`)\n**Discovery source:** Orchestrator selection record of intake wave 2026-10-02\n**Status:** processed\n**Status note:** `partial_fulltext_read` — figure panels and supplement unread; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Primary pathway:** biomarkers (rejected)\n**Species:** human bulk tumour expression data\n**Transferability:** T3\n**clinical relevance:** BACKGROUND — the title is not transferable to this model\n**Claim links:** none — the rejection is `DIS-026`\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261002_C.md` · `CC-20261002-BIOMARKER-REJECTIONS-01` · `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Next action:** figure panels and supplement owed for a complete read\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID34204789.json`\n"
 },
 {
  "op": "insert-after",
  "id": "LIT-0428",
  "text": "\n## LIT-0429\n**Short title:** Zhang & Freudenreich 2007 Mol Cell — the FRA16D Flex1 AT-repeat stalls replication forks and breaks chromosomes in yeast\n**Authors:** Zhang H, Freudenreich CH\n**Year:** 2007\n**Source type:** primary research — yeast genetics / replication\n**Journal/source:** *Mol Cell* 2007;27(3):367-379\n**Identifier type:** PMID / DOI / PMCID\n**Identifier value:** PMID 17679088 / DOI 10.1016/j.molcel.2007.06.012 / PMC2144737\n**Date discovered:** before 2026-10-02 (reading queue; selected for intake wave 2026-10-02)\n**Date processed:** 2026-10-02 (first-hand read, `FTR-20261002-17679088-01`)\n**Discovery source:** Orchestrator selection record of intake wave 2026-10-02\n**Status:** processed\n**Status note:** `partial_fulltext_read` — figure panels and supplement unread; **OFF-AXIS for the assigned hypothesis**; record created by `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Primary pathway:** locus fragility / FRA16D architecture\n**Species:** *Saccharomyces cerevisiae*\n**Transferability:** T3 — somatic, mitotic, in yeast; no WWOX function measured\n**clinical relevance:** BACKGROUND — a mechanistic precedent plus `LEAD-C1`; **not** a biomarker entry in either direction\n**Claim links:** none\n**Working Model impact:** none — no block is redefined\n**Report mentions:** `research/intake_wave_20261002_C.md` § 4 (`LEAD-C1`) · `CC-20261002-INTAKE-WAVE-ORPHANS-01`\n**Next action:** Finnis 2005 owed before anything is asserted about where Flex1 sits inside WWOX; figure panels and supplement owed for a complete read\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID17679088.json`\n"
 },
 {
  "op": "replace-within",
  "id": "LIT-0106",
  "old": "**Status:** discovered",
  "new": "**Status:** processed\n**Status note:** read 2026-10-02 at `partial_fulltext_read` depth (receipt `FTR-20261002-33195192-01`); figure panels and the supplement, including Supplementary Figure S9, are unread. Promoted to [[paper_registry_current#PAPER 129]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01`; the triage fields below are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0106",
  "old": "**Date processed:** not yet processed",
  "new": "**Date processed:** 2026-10-02 (partial full text; `FTR-20261002-33195192-01`)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0106",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** figure panels and the supplement (Suppl. Fig. S9 carries the total-ERK half of the pERK result) owed for a complete read"
 },
 {
  "op": "replace-within",
  "id": "LIT-0106",
  "old": "**Claim links:** none",
  "new": "**Claim links:** none\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID33195192.json`"
 },
 {
  "op": "replace-within",
  "id": "LIT-0100",
  "old": "**Status:** discovered",
  "new": "**Status:** processed\n**Status note:** read 2026-10-02 at `partial_fulltext_read` depth (receipt `FTR-20261002-37897534-01`); figure panels and the supplement are unread. Promoted to [[paper_registry_current#PAPER 130]] by `CC-20261002-INTAKE-WAVE-ORPHANS-01`; the triage fields below are kept as history"
 },
 {
  "op": "replace-within",
  "id": "LIT-0100",
  "old": "**Date processed:** not yet processed",
  "new": "**Date processed:** 2026-10-02 (partial full text; `FTR-20261002-37897534-01`)"
 },
 {
  "op": "replace-within",
  "id": "LIT-0100",
  "old": "**Next action:** screening and tier assignment",
  "new": "**Next action:** figure panels and the supplement owed for a complete read"
 },
 {
  "op": "replace-within",
  "id": "LIT-0100",
  "old": "**Claim links:** none",
  "new": "**Claim links:** none\n**Evidence depth:** `partial_fulltext_read` — manifest `deepdive_manifests/PMID37897534.json`"
 }
]
```

## 5 · What this candidate deliberately does NOT do

- **It adds no claim, moves no claim status and redefines no working-model block.** Every record
  above is a landing for a reading, with its depth and its limits; none is support for a claim.
- **It does not re-judge any peer's reading.** The `Role` lines restate what the wave's own
  analysis notes and candidates concluded, with their caveats attached — the single-laboratory
  lineage of `PAPER 126` / `PAPER 129` / `PAPER 130`, the untested dependence of `PAPER 127`, the
  off-axis verdict on `PAPER 128`.
- **It creates no biomarker and no endpoint record**, and it does not enter PMID 17679088 in the
  biomarker ledger in either direction (`CC-20261002-BIOMARKER-REJECTIONS-01` § 4).
- **It upgrades no reading depth.** Four of the six records say `partial_fulltext_read` and name
  what is owed.

## BATCH DISPOSITION — `BATCH_20261002_001` (2026-10-02, ACTOR_ID `scientist`), append-only

**Nothing above this line was rewritten.**

**Verdict:** PROPAGATED

Branch `task/batch-20261002-intake-2`. Both op lists applied as written, record-scoped, exit 0:
19 ops on `paper_registry_current.md` (shared with `CC-20261002-INTAKE-A-REGISTRY-01` and
`CC-20261002-B-NONLINEAGE-01`) and 24 on `literature_tracking_log_current.md`. `PAPER 125`–`130`
and `LIT-0426`–`0429` were confirmed free at propagation time (`registry_records.py catalog`:
live highest `PAPER 118`, `LIT-0420`). `ORPHAN_COMPLETE_READ` after propagation: **0** (4 before).
