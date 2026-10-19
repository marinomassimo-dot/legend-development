# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-G4-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), metabolic batch 2026-10-19 group G4, branch `task/metab-g4-d`.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (registry identity records and one queue note; no claim status and no working-model block changes).
**Not medical advice.** Class-level statements only.

## Target and need
Sixteen of the nineteen lot papers had no registry record at the start (`registry_records.py get --pmid` returned `NO RECORD MATCHED`); one had a queue mention only (`FT-167`); two had corpus placeholders (the parked pair). The integrator needs `PAPER` and `LIT` identity records so that the staged receipts have something to attach to. Provisional numbers are left to the integrator. Every row below is a comparator or adjacent source: **none carries a WWOX patient or a WWOX measurement.**

| PMID | Short title | Source type | Genotype/model | Transferability | Role (one line) | Receipt |
|---|---|---|---|---|---|---|
| 37328865 | Wainberg 2023 ADRD/PD/ALS loci | GWAS summary-statistics analysis | human, common variant | T3 | Locus near MAF/WWOX shared by ADRD and PD at OR 1.04; WWOX named by proximity argument | FTR-20261019-37328865-01 |
| 39570186 | Sathe 2025 symptomatic VABAM | retrospective cohort | human infantile spasms, non-WWOX | T3 | All symptomatic VABAM had concurrent hormonal therapy; causation not established | FTR-20261019-39570186-01 |
| 39641935 | Stevering 2025 VABAM in TSC | registry cohort | human TSC infants | T3 | VABAM-like change in unexposed children; hormonal therapy tied to symptoms, not to MRI | FTR-20261019-39641935-01 |
| 37443770 | Ng 2023 DTDS review | narrative review | human SLC6A3 | T3 | DTDS CSF signature (raised HVA, ratio 5.0-13.0) | FTR-20261019-37443770-01 |
| 40291937 | Al Sari 2025 DTDS/PKDYS2 review | narrative review | human SLC6A3, SLC18A2 | T3 | Comparison table; internally inconsistent on anticholinergic/benzodiazepine use | FTR-20261019-40291937-01 |
| 42483444 | Naranjo-Lobo 2026 pediatric parkinsonism | narrative review | human | T3 | Age-stratified CSF/imaging work-up tables; AI language editing disclosed | FTR-20261019-42483444-01 |
| 40183510 | Sugiyama 2025 Dravet parkinsonism | case report, n = 2 adults | human SCN1A | T3 | Low CSF HVA/5-HIAA in two adults; no non-parkinsonian Dravet control | FTR-20261019-40183510-01 |
| 35053314 | Ferraro 2022 nigra meta-analysis | computational meta-analysis | human post-mortem bulk expression | T3 | WWOX named as network-central protein, not differentially expressed | FTR-20261019-35053314-01 |
| 38330420 | Bian 2024 HPA axis and epilepsy | narrative review | mostly rodent | T3 | Background on CRH/ACTH/glucocorticoids and seizures | FTR-20261019-38330420-01 |
| 41470225 | Abdygalyk 2025 infantile spasms | narrative review | human, mixed | T3 | One sentence and one table row on WWOX; neurosteroid hypothesis for ACTH, unmeasured | FTR-20261019-41470225-01 |
| 42782811 | Bagyinszky 2026 ERBB4 and HPA axis | narrative review | rodent, human genetics | T3 | ErbB4-HPA bridge called largely speculative | FTR-20261019-42782811-01 |
| 41573381 | Alammary 2026 GABA-T deficiency | case report, three siblings | human ABAT | T3 | Genetic counterpart of vigabatrin's target; GABA values retrospective, mixed units | FTR-20261019-41573381-01 |
| 41977367 | Dumitrescu 2026 chloride microdomains | conceptual review | mixed | T4 | No measurement relevant to depolarising GABA in WWOX loss | FTR-20261019-41977367-01 |
| 42643745 | Nikkhah 2026 SLC18A2 splice-acceptor | case report | human SLC18A2 | T3 | Oculogyric crises read as seizures; EEG non-epileptic; CSF not done | FTR-20261019-42643745-01 |
| 42245405 | Almutair 2026 SLC18A2 siblings | case series, n = 2 | human SLC18A2 | T3 | Same variant, different severity and tolerability; CSF not done | FTR-20261019-42245405-01 |
| 32546684 | Shi 2020 NRG1-ErbB4 | narrative review | mouse circuits | T4 | Proposed direction is to lower ErbB4 in PV+ cells; no WWOX | FTR-20261019-32546684-01 |
| 41914335 | Li 2026 serotonin and SUDEP | narrative review | mostly DBA mice | T4 | Serotonin-SUDEP evidence mostly animal; no WWOX | FTR-20261019-41914335-01 |

## Queue and register notes
- `FT-167` (Ferraro 2022): add a line that the paper names WWOX once, as a network-central protein, with no expression value; the "method-only transfer" rating stands.
- Parked, for the full-text queue as `OA-but-bot-blocked` with the cascade in `metabolic_wave_20261019_scientist-d.md` section 6: PMID 40139278 (Yuan 2025), PMID 17909041 (Aqeilan 2007). Newly found and closed to retrieval: PMID 38407561 (Nishino 2024, a WOREE case with ACTH recorded; **highest value**), PMID 39933386 (Martin 2025), PMID 33074286 (Kunkle 2021).
- Correct the batch selection file's description of `PAPER 003`: the source is registered but has no receipt.

## Discovery-ledger proposals (not appended; the ledger is propagated only by `BATCH_COMMIT`)
Leads L1-L4 of the analysis note (`IPOTESI`), each with a falsifier in the note.


---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_001` · 2026-10-19 · ACTOR_ID `orchestrator` (stated assumption, batch integrator)
**Working model:** WM_v7.20 -> WM_v7.21 (MINOR)
**Class re-judged (§7):** MINOR
**Blind locator audit:** not run — no baseline claim is narrowed and no MAJOR contingency is declared; the candidate's locator triples are carried for a later audit.
**What landed:** 17 PAPER record(s) (PAPER 293, PAPER 294, PAPER 295, PAPER 296, PAPER 297, PAPER 298, PAPER 299, PAPER 300, PAPER 301, PAPER 302, PAPER 303, PAPER 304, PAPER 305, PAPER 306, PAPER 307, PAPER 308, PAPER 309) with their LIT records. Queue note on `FT-167` applied; parked retrieval items minted as FT-197 to FT-200. The correction of the selection file's description of `PAPER 003` is not a registry edit (the selection file is a research file) and is carried in the `CLAIM 001` wave note.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record is carried.
