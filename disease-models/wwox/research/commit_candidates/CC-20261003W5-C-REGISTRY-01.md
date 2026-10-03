# CC-20261003W5-C-REGISTRY-01 — registry landing for the six group-C PMIDs

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-03 · **Author:** Scientist C, intake wave 5 · **Change class:** MINOR
**Branch:** `task/sci-C-20261003w5`

> **All numbers in this candidate are PROVISIONAL.** They were measured with
> `registry_records.py catalog` on `task/sci-C-20261003w5` at commit `49e7ba59978d`, where the
> highest existing identifiers are `PAPER 150`, `LIT-0443` and `CORPUS-STUB-179`. Other branches
> land continuously; **the integrator re-measures and renumbers in event order**, and updates the
> `LIT link` / `Paired with` anchors in both directions.

---

## 1 · Why this candidate exists

Wave 1 left eight PMIDs with no registry presence and LINT blocked `BATCH_COMMIT` with
`ORPHAN_COMPLETE_READ`. All six group-C PMIDs were confirmed absent from every registry before
reading — `paper_packet.py packet --pmid N`, six times, each returning *"manifest: none — this is a
first reading"*, *"prior read: depth=none · receipts=0"* and *"acquisition: no route recorded"*.
This candidate gives each a structured landing so the six receipts can be recorded without orphaning.

**Does each PMID need registry records?** Yes — all six. Each has a dossier, a validated manifest and
a prepared receipt, and none has any registry record today.

**Record kind chosen: paired `PAPER` + `LIT`**, following the precedent set by
`CC-20261003W3-B-REGISTRY-01` for non-WWOX primaries (see `PAPER 146` / `LIT-0443`). A
`CORPUS-STUB` would be the lighter alternative; it is rejected here because all six were read in
full-text depth with locators persisted, which a stub does not represent.

**Every one of the six is an earned null for the gene: WWOX occurs zero times in all six articles.**
That is recorded explicitly in each record so that no later reader mistakes a delivery-safety source
for a WWOX source.

## 2 · Ops — paper_registry_current.md

For each, `op: APPEND` a new record at the end of the PAPER section of
`disease-models/wwox/registries/paper_registry_current.md`. There is no `old` text: these are
appends, not edits.

### PAPER 162 (provisional) — PMID 41966056

```
## PAPER 162
**Short title:** Wang 2026 Mol Ther - first-in-human single-patient intra-cisterna magna AAV9 in severe MPS I, >5.5 years
**Full title:** First-in-human intracisternal dosing of RGX-111 in severe MPS I is well tolerated and generates sustained neurodevelopment without HSCT
**Authors:** Wang RY, et al.
**Year:** 2026
**Source type:** primary research - single-patient open-label clinical report
**Journal/source:** *Molecular Therapy* 2026
**Identifier:** PMID 41966056 / PMCID PMC13239742 / DOI 10.1016/j.ymthe.2026.04.016
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41966056-01`; manifest `deepdive_manifests/PMID41966056.json`; dossier `research/fulltext_dossiers/PMID41966056.md` (figure panels not rendered; supplementary documents not fetched)
**Primary pathway:** CSF-route AAV9 delivery - human safety and tolerability
**Model/species:** human, single patient, dosed in the second year of life
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: route, immunosuppression and monitoring transfer; the cargo, the pharmacodynamic readout and the disease do not
**clinical relevance:** LOW for WWOX biology; MODERATE as the only human intracisternal AAV9 datum in the second year of life
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** Carried for four things only: (1) the intra-cisterna-magna route tolerated at ~20 months with next-day discharge; (2) 48 weeks of triple immunosuppression, with 16 of the 17 first-year adverse events attributed by the investigators to the immunosuppression rather than the vector; (3) ⚠️ **the dose literal is printed with an impossible negative exponent in BOTH the abstract and the body** and must never be carried as printed - see `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`; (4) ⚠️ **DRG toxicity was not measured** - the authors state no nerve conduction studies were performed and rest the inference on absence of reported paraesthesia in a toddler. The selection record called this "a first-in-human cohort"; it is n = 1. An intraventricular tumour with vector genome integration after the same route and vector in a different child is **cited** here, not measured, and is an open reading debt.
**LIT link:** [[literature_tracking_log_current#LIT-0452]]
**Note:** class-level record; no individual-level detail is carried in this public edition. Not medical advice.
```

### PAPER 163 (provisional) — PMID 41210171

```
## PAPER 163
**Short title:** Vono 2025 Mol Ther Methods Clin Dev - pre-existing anti-AAV9 immunity does not bound CNS biodistribution after intrathecal dosing in macaques
**Full title:** Impact of pre-existing immunity on safety and biodistribution of a single AAV9 vector intrathecal injection in cynomolgus monkeys
**Authors:** Vono M, et al.
**Year:** 2025
**Source type:** primary research - non-GLP non-human primate toxicology and biodistribution
**Journal/source:** *Molecular Therapy: Methods & Clinical Development* 2025
**Identifier:** PMID 41210171 / PMCID PMC12590263 / DOI 10.1016/j.omtm.2025.101602
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41210171-01`; manifest `deepdive_manifests/PMID41210171.json`; dossier `research/fulltext_dossiers/PMID41210171.md` (Figure 6 rendered and read at panel level; supplement fetched and read; Figures 1-5 captions only)
**Primary pathway:** CSF-route AAV9 delivery - pre-existing immunity, biodistribution, histopathology
**Model/species:** 15 female cynomolgus macaques, ~41 months, no immunosuppression, 4 weeks, terminal endpoints
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: the eligibility conclusion and the immunity/biodistribution dissociation transfer; the cargo (mCherry under a strong ubiquitous promoter) does not
**clinical relevance:** LOW for WWOX biology; MODERATE for any future CSF-route eligibility criterion
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** Carried for: high serum anti-AAV9 titre leaving CNS vector-genome biodistribution intact while **reducing** load to DRG, liver and heart and increasing it to spleen; and the authors' conclusion that serostatus should not alone exclude a candidate from intrathecal dosing. ⚠️ **The study has ONE dose level** (1.2 × 10¹³ vg/animal across all treated groups, read from the Figure 6C panel), so it cannot speak to dose at all. ⚠️ **The DRG finding has no incidence or severity count anywhere** - zero tables in the article, Figure 6C tabulates brain only, and the fetched supplement holds only titre tables. ⚠️ Figure 6C further shows the meningeal infiltrate in **2 of 3 vehicle animals**, the immunity "trend" resting on one animal of four, and perivascular infiltrate **non-monotonic** in titre. Female-only, no infant, no male, 4 weeks.
**LIT link:** [[literature_tracking_log_current#LIT-0453]]
**Note:** class-level record. Not medical advice.
```

### PAPER 164 (provisional) — PMID 41257285

```
## PAPER 164
**Short title:** Aihara 2025 Mol Ther Methods Clin Dev - empty capsid and promoterless vector do not reproduce the liver and DRG toxicity of a full AAV9 vector
**Full title:** Transcriptional changes in non-human primate tissues after intrathecal delivery of serotype 9 adeno-associated viral vector: Insights into organ toxicities
**Authors:** Aihara Y, et al.
**Year:** 2025
**Source type:** primary research - non-human primate transcriptomics across two toxicology studies
**Journal/source:** *Molecular Therapy: Methods & Clinical Development* 2025
**Identifier:** PMID 41257285 / PMCID PMC12621450 / DOI 10.1016/j.omtm.2025.101617
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41257285-01`; manifest `deepdive_manifests/PMID41257285.json`; dossier `research/fulltext_dossiers/PMID41257285.md` (figures captions only; supplementary figures and tables not fetched)
**Primary pathway:** CSF-route AAV9 delivery - mechanism of organ toxicity; interferon / antigen-presentation transcriptional response
**Model/species:** 40 female cynomolgus macaques, 12-50 months, seronegative-selected, no immunosuppression, 28 days
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T3 for WWOX: the capsid-versus-expression discrimination bears directly on any WWOX restoration cassette, which is a promoter-driven protein transgene and therefore falls on the toxic side of this paper's dividing line
**clinical relevance:** LOW for WWOX biology; HIGH as the mechanistic layer under any CSF-route WWOX programme
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The most mechanistically informative source in group C and the only one whose design separates capsid from expression: **hepatic and DRG toxicity occurred only with the full expressing vector, not with empty capsids and not with a promoterless genome at comparable capsid dose.** Also carries the interferon/JAK-STAT rather than NF-κB argument for why glucocorticoid prophylaxis may be insufficient (the authors' hypothesis; no immunosuppressed arm was run). ⚠️ **Counterweight from the same paper:** transgene transcript was highest in heart and skeletal muscle, the tissues *without* pathology, so expression **magnitude** does not predict which tissue is injured - this is in tension with [[paper_registry_current#PAPER 167]]'s attribution of DRG toxicity to supraphysiological expression, and the tension is recorded, not resolved. ⚠️ **The NfL correlation, the histopathology and all in-life toxicity are CITED to the authors' prior report, not measured here** - an open reading debt. Female-only, seronegative-only; must not be pooled with [[paper_registry_current#PAPER 163]], which selected the opposite.
**LIT link:** [[literature_tracking_log_current#LIT-0454]]
**Note:** class-level record. Not medical advice.
```

### PAPER 165 (provisional) — PMID 41948127

```
## PAPER 165
**Short title:** Stavrou 2026 Mol Ther Nucleic Acids - intrathecal AAV9 RNAi for CMT1A in mice and macaques; DRG lesions also present in half the vehicle controls
**Full title:** Safety, efficacy, and distal nerve Schwann cell biodistribution in mice and NHPs to support translation of AAV9 RNAi therapy for CMT1A
**Authors:** Stavrou M, et al.
**Year:** 2026
**Source type:** primary research - murine efficacy/toxicology plus non-human primate safety and biodistribution
**Journal/source:** *Molecular Therapy: Nucleic Acids* 2026
**Identifier:** PMID 41948127 / PMCID PMC13051718 / DOI 10.1016/j.omtn.2026.102881
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-41948127-01`; manifest `deepdive_manifests/PMID41948127.json`; dossier `research/fulltext_dossiers/PMID41948127.md` (Figure 5 rendered and read at panel level; Table 1 not read; supplementary pathology reports not fetched)
**Primary pathway:** CSF-route AAV9 delivery - peripheral nervous system biodistribution, DRG safety, functional electrophysiological monitoring
**Model/species:** CMT1A mice; 20 cynomolgus macaques, 10 male and 10 female, 6 and 12 weeks
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: the monitoring design, the control-arm DRG incidence and the slow-infusion procedure transfer; the cargo does not - this is knockdown of an over-expressed gene, the opposite direction from WWOX restoration, driven by a U6 small-RNA cassette rather than a promoter-driven protein transgene
**clinical relevance:** LOW for WWOX biology; HIGH for the DRG-attribution question and for safety-monitoring design
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The load-bearing datum is in the **control** arm: minimal-to-mild DRG lesions in **2 of 4 saline-dosed macaques**. Supplies the group's best patient-transferable monitoring design (serial NCV and CMAP at baseline, 6 and 12 weeks, plus troponin I, ECG, ophthalmic examination) and its only explicit dose threshold (murine: 5E11 anti-inflammatory, 1E12 pro-inflammatory). ⚠️ **The Figure 5A caption denies DRG abnormality while the body reports lesions in 40% of animals**; the rendered panel supports the body. ⚠️ **Three internal quantity contradictions**: the low NHP dose is 6E13 in text but 5E13 in the Figure 5A row labels; the infusion volume is 4 mL in Results and 3 mL in Methods; the Figure 5A scale bars are stated in millimetres where the panel prints micrometres. See `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`. ⚠️ NfL is used here as a marker of **benefit** where [[paper_registry_current#PAPER 164]] uses it as a marker of **toxicity**.
**LIT link:** [[literature_tracking_log_current#LIT-0455]]
**Note:** class-level record. Not medical advice.
```

### PAPER 166 (provisional) — PMID 42205472

```
## PAPER 166
**Short title:** Engelhard 2026 Front Drug Deliv - CSF circulation variability and why a CSF-route dose is a distribution rather than a number
**Full title:** Variability in the circulation of cerebrospinal fluid: causes and clinical implications for intraventricular drug delivery
**Authors:** Engelhard HH, et al.
**Year:** 2026
**Source type:** narrative review - no primary measurement
**Journal/source:** *Frontiers in Drug Delivery* 2026
**Identifier:** PMID 42205472 / PMCID PMC13201979 / DOI 10.3389/fddev.2026.1735474
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-42205472-01`; manifest `deepdive_manifests/PMID42205472.json`; dossier `research/fulltext_dossiers/PMID42205472.md` (Tables 4 and 7 read cell-wise; remaining tables by title; Supplementary Material 2 not fetched)
**Primary pathway:** CSF physiology - production, pathway anatomy, flow dynamics, clearance; determinants of delivered dose at target
**Model/species:** human physiology with laboratory-species comparisons; review
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T4 for WWOX: a framing and method source, not an evidentiary one
**clinical relevance:** LOW for WWOX biology; MODERATE for dose-setting method on any CSF route
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** ⚠️ **Scope correction: this paper is about INTRAVENTRICULAR delivery, not intrathecal delivery**, contrary to the title under which it was assigned - route is the variable the reading set exists to separate from dose. Carried for: age named among the top three drivers of variability in delivered dose at a CSF route; the statement that fixed dosing across a population is current practice and inadequate for this route; and isotope-labelled AAV9 capsid PET as the only named route to measuring delivery in a living patient rather than at necropsy. ⚠️ **Table 4, the only cross-species scaling table in the group, has a single undated adult "human" row and therefore cannot set an infant dose**; its CSF volumes do independently reproduce the 371-fold mouse-to-macaque factor used in [[paper_registry_current#PAPER 165]]. Every number in this review is attributed to a cited primary and none was read.
**LIT link:** [[literature_tracking_log_current#LIT-0456]]
**Note:** class-level record. Not medical advice.
```

### PAPER 167 (provisional) — PMID 42134074

```
## PAPER 167
**Short title:** Kagiava 2026 eBioMedicine - the human intrathecal gene therapy record, the regulatory history of the DRG question, and the immunosuppression pattern keyed to predicted-null recipients
**Full title:** Progress and challenges in intrathecal gene therapy for neurological disorders
**Authors:** Kagiava A, et al.
**Year:** 2026
**Source type:** narrative review - no primary measurement
**Journal/source:** *eBioMedicine* 2026
**Identifier:** PMID 42134074 / PMCID PMC13196305 / DOI 10.1016/j.ebiom.2026.106294
**Status:** processed
**Record provenance:** created by `CC-20261003W5-C-REGISTRY-01` (intake wave 5 2026-10-03, Scientist C). Provisional number; the integrator renumbers in event order.
**Evidence depth:** `partial_fulltext_read` - receipt `FTR-20261003-42134074-01`; manifest `deepdive_manifests/PMID42134074.json`; dossier `research/fulltext_dossiers/PMID42134074.md` (Table 1 read cell-wise; clinical sections read in full; preclinical sections by title only)
**Primary pathway:** CSF-route gene therapy - human clinical record, dose envelope, immunosuppression regimens, DRG safety history
**Model/species:** human clinical programmes plus preclinical index; review
**Genotype/model:** no WWOX genotype - WWOX is not mentioned in this paper
**Transferability:** T3 for WWOX: the immunosuppression pattern keyed to predicted-null recipients applies to a biallelic loss-of-function WWOX genotype by construction; the nearest disease precedent (a paediatric neurodegenerative seizure-bearing disorder dosed intrathecally with the same capsid) is a precedent only
**clinical relevance:** LOW for WWOX biology; HIGH as the human layer under any CSF-route WWOX programme
**Claim links:** none
**Role:** 🔴 **Earned null for the gene.** The selection record called this "deliberately the weakest member" of its group and advised dropping it first; **that judgement is reversed here** - it is the only source carrying the human evidence base. Carries: the regulatory hold placed on a human paediatric intrathecal programme because of primate DRG findings; the human DRG outcome (sensory, mild, improved with symptomatic treatment where it appeared, and absent on MRI and nerve conduction at the highest human doses); and the pattern of **triple immunosuppression where the recipient is predicted null for the transgene product** versus a steroid alone where endogenous protein is present. ⚠️ **One paragraph's four hepatotoxicity percentages are internally incoherent as printed** - it compares one route to itself and gives a sham-control rate exceeding the treated rate - and none may be carried; the same paragraph calls a study single-arm while listing its sham groups. ⚠️ Its attribution of DRG toxicity to supraphysiological expression level is in tension with [[paper_registry_current#PAPER 164]]'s tissue-level data. Every datum is secondary; none of the cited primaries was read.
**LIT link:** [[literature_tracking_log_current#LIT-0457]]
**Note:** class-level record. Not medical advice.
```

## 3 · Ops — literature_tracking_log_current.md

`op: APPEND` six records at the end of the LIT section of
`disease-models/wwox/registries/literature_tracking_log_current.md`. Shared fields for all six:

- **Date discovered / Date processed:** 2026-10-03
- **Discovery window:** intake wave 5 2026-10-03 (Scientist C, group C)
- **Discovery source:** Orchestrator wave-5 selection record
- **Discovery query:** AAV9 / intrathecal / intracisternal / neonatal delivery safety as a human and NHP evidence base
- **Status:** processed
- **Genotype/model tag:** no WWOX genotype
- **Claim links:** none
- **Working Model impact:** none
- **Report mentions:** `research/intake_wave_20261003w5_C.md`
- **Next action:** none
- **Flags:** created by `CC-20261003W5-C-REGISTRY-01`; provisional number

| id | Short title | Authors | Year | Journal | Identifier | Source type | Primary pathway | Transferability | clinical relevance | Paired with | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LIT-0452 | Wang 2026 single-patient intracisternal AAV9 in MPS I | Wang RY, et al. | 2026 | *Mol Ther* | PMID 41966056 / DOI 10.1016/j.ymthe.2026.04.016 | primary research - single-patient clinical report | CSF-route AAV9 human safety | T4 | MODERATE as the only human intracisternal datum in the second year of life | `PAPER 162` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`). WWOX absent — earned null. ⚠️ dose literal printed with an impossible sign; ⚠️ DRG not measured. |
| LIT-0453 | Vono 2025 pre-existing anti-AAV9 immunity, intrathecal, macaque | Vono M, et al. | 2025 | *Mol Ther Methods Clin Dev* | PMID 41210171 / DOI 10.1016/j.omtm.2025.101602 | primary research - NHP toxicology/biodistribution | CSF-route AAV9 immunity and biodistribution | T4 | MODERATE for CSF-route eligibility criteria | `PAPER 163` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`; Figure 6 read at panel level, supplement fetched). WWOX absent — earned null. ⚠️ single dose level; ⚠️ no DRG incidence anywhere. |
| LIT-0454 | Aihara 2025 transcriptional response to intrathecal AAV9 in macaques | Aihara Y, et al. | 2025 | *Mol Ther Methods Clin Dev* | PMID 41257285 / DOI 10.1016/j.omtm.2025.101617 | primary research - NHP transcriptomics | mechanism of CSF-route AAV9 organ toxicity | T3 | HIGH as the mechanistic layer under a CSF-route WWOX programme | `PAPER 164` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`). WWOX absent — earned null. Empty capsid and promoterless vector did not reproduce the toxicity. ⚠️ in-life toxicity data are cited to a prior report. |
| LIT-0455 | Stavrou 2026 intrathecal AAV9 RNAi, mice and macaques | Stavrou M, et al. | 2026 | *Mol Ther Nucleic Acids* | PMID 41948127 / DOI 10.1016/j.omtn.2026.102881 | primary research - murine and NHP safety/biodistribution | CSF-route AAV9 PNS biodistribution and DRG safety | T4 | HIGH for DRG attribution and monitoring design | `PAPER 165` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`; Figure 5 read at panel level). WWOX absent — earned null. DRG lesions in 2 of 4 vehicle controls. ⚠️ three internal quantity contradictions. |
| LIT-0456 | Engelhard 2026 CSF circulation variability and intraventricular delivery | Engelhard HH, et al. | 2026 | *Front Drug Deliv* | PMID 42205472 / DOI 10.3389/fddev.2026.1735474 | narrative review | CSF physiology and determinants of delivered dose | T4 | MODERATE for dose-setting method | `PAPER 166` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`; Tables 4 and 7 read cell-wise). WWOX absent — earned null. ⚠️ scope is **intraventricular**, not intrathecal. ⚠️ paediatric section is in an unfetched supplement. |
| LIT-0457 | Kagiava 2026 intrathecal gene therapy for neurological disorders | Kagiava A, et al. | 2026 | *eBioMedicine* | PMID 42134074 / DOI 10.1016/j.ebiom.2026.106294 | narrative review | human CSF-route gene therapy record and immunosuppression practice | T3 | HIGH as the human layer | `PAPER 167` (provisional; not yet created) | Read 2026-10-03 (`partial_fulltext_read`; Table 1 read cell-wise). WWOX absent — earned null. Carries the regulatory history of the DRG question. ⚠️ one paragraph's percentages are unusable as printed. |

## 4 · Verification before landing

- [ ] Re-measure highest `PAPER` and `LIT-` identifiers after merging `main`; renumber.
- [ ] Confirm each `LIT link` and each `Paired with` resolves in both directions (`legend_lint.py`).
- [ ] Record the six receipts in event order **before or with** these records, so no record claims a
      receipt the ledger does not hold.
- [ ] Confirm no record carries individual-level detail (`scripts/public_release_gate.py`).

## 5 · LOCATOR TRIPLES FOR BLIND AUDIT

This candidate creates registry records and asserts no scientific proposition of its own; the
propositions its records summarise are audited through the four substantive candidates of this wave,
whose triples point at the same artefacts. No triples are offered here.
