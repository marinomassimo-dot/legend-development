# COMMIT CANDIDATE — CC-20261019-SCIENTIST-C-G3-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, task METAB-G3-C-20261019, 2026-10-19.
**Change class:** **MINOR.** It creates registry presence for thirteen papers that have none, records reading debts and carries staged leads; it narrows no claim and reverses none. No scientific current file is touched.
`context_policy: SOURCE_FIRST` for new rows, `QUESTION_DRIVEN` for the three HELD-partial resumes. **Not medical advice.**

## 0 · Why

Group G3 (mitochondria, iron, ferroptosis) was read in tier order: sixteen new rows plus three HELD-partial resumes. `registry_records.py get --pmid N` run per paper shows identity records for six of the nineteen (the three resumes, the Sze commentary, Liu 2022 and Lo 2015, the last two only as corpus stubs) and none for the thirteen below. Per-paper results and receipts are in `metabolic_wave_20261019_scientist-c.md`; every staged receipt is under `receipt_staging/scientist-c/`.

## 1 · Numbers are provisional

The Orchestrator integrates four Scientists in one batch and owns the numbering. This candidate uses placeholder ids `PAPER P01`–`P13` and does not claim `LIT` numbers; the integrator assigns `PAPER` and `LIT` ids at integration (disjoint from peers) and writes the twin `LIT` rows with the bare `Status` vocabulary of the log.

## 2 · Ops — `disease-models/wwox/registries/paper_registry_current.md` (op `append`, new record each, no `old`)

| provisional id | PMID | record text |
|---|---|---|
| `PAPER P01` | 35571988 | **Short title:** Li 2022, mitochondrial 1555 G>A and childhood glioblastoma with a WWOX intronic hit · **Journal:** Neuro-Oncol Adv · **DOI:** 10.1093/noajnl/vdac045 · **Evidence depth:** per receipt FTR-20261019-35571988-01 · **Role:** read in metabolic wave G3, analysis note section 3 |
| `PAPER P02` | 40808923 | **Short title:** Xu 2025, Ferroptosis and epilepsy: bidirectional pathogenic links and therapeutic implications (narrative review) · **Journal:** Front Neurol · **DOI:** 10.3389/fneur.2025.1635441 · **Evidence depth:** per receipt FTR-20261019-40808923-01 · **Role:** read in metabolic wave G3, analysis note section 4 |
| `PAPER P03` | 38570643 | **Short title:** Kawabata 2024, chronic replication stress, parkin and mitochondrial dysfunction · **Journal:** Sci Rep · **DOI:** 10.1038/s41598-024-58656-w · **Evidence depth:** per receipt FTR-20261019-38570643-01 · **Role:** read in metabolic wave G3, analysis note section 5 |
| `PAPER P04` | 42434280 | **Short title:** Ganapathy 2026, commentary on STAT3 blockade, ferritinophagy and ferroptosis (toosendanin) · **Journal:** J Gastrointest Oncol · **DOI:** 10.21037/jgo-2026-1-0151 · **Evidence depth:** per receipt FTR-20261019-42434280-01 · **Role:** read in metabolic wave G3, analysis note section 6 |
| `PAPER P05` | 41822170 | **Short title:** Petrillo 2026, ferroptosis-induced epileptiform activity in mouse cortical slices · **Journal:** Front Cell Neurosci · **DOI:** 10.3389/fncel.2026.1758230 · **Evidence depth:** per receipt FTR-20261019-41822170-01 · **Role:** read in metabolic wave G3, analysis note section 7 |
| `PAPER P06` | 42601505 | **Short title:** Puertas-Frias 2026, PUFA sequestration and mitochondrial dysfunction-induced ferroptosis · **Journal:** EMBO Rep · **DOI:** 10.1038/s44319-026-00898-y · **Evidence depth:** per receipt FTR-20261019-42601505-01 · **Role:** read in metabolic wave G3, analysis note section 8 |
| `PAPER P07` | 39995090 | **Short title:** Liang 2026, HIF-1a inhibitor PX-478 and hippocampal ferroptosis in PTZ-kindled mice · **Journal:** Neural Regen Res · **DOI:** 10.4103/NRR.NRR-D-24-01007 · **Evidence depth:** per receipt FTR-20261019-39995090-01 · **Role:** read in metabolic wave G3, analysis note section 9 |
| `PAPER P08` | 41002898 | **Short title:** Truong 2025, mitochondria-associated membrane dysfunction in neurodegeneration (narrative review) · **Journal:** Membranes · **DOI:** 10.3390/membranes15090263 · **Evidence depth:** per receipt FTR-20261019-41002898-01 · **Role:** read in metabolic wave G3, analysis note section 10 |
| `PAPER P09` | 34354738 | **Short title:** Munk 2021, an 80 kb PRKN intron deletion lowers its fragility without changing expression · **Journal:** Front Genet · **DOI:** 10.3389/fgene.2021.695172 · **Evidence depth:** per receipt FTR-20261019-34354738-01 · **Role:** read in metabolic wave G3, analysis note section 11 |
| `PAPER P10` | 27066568 | **Short title:** Schule 2015, Is PARKIN parkinsonism a cancer predisposition syndrome? (case note) · **Journal:** Neurol Genet · **DOI:** 10.1212/NXG.0000000000000031 · **Evidence depth:** per receipt FTR-20261019-27066568-01 · **Role:** read in metabolic wave G3, analysis note section 12 |
| `PAPER P11` | 25833766 | **Short title:** Ambroziak 2015, PARK2 rearrangement breakpoints in a Polish Parkinson cohort · **Journal:** J Appl Genet · **DOI:** 10.1007/s13353-015-0282-9 · **Evidence depth:** per receipt FTR-20261019-25833766-01 · **Role:** read in metabolic wave G3, analysis note section 13 |
| `PAPER P12` | 34937577 | **Short title:** Zhang 2021, Mitophagy in neurological disorders (narrative review) · **Journal:** J Neuroinflammation · **DOI:** 10.1186/s12974-021-02334-5 · **Evidence depth:** per receipt FTR-20261019-34937577-01 · **Role:** read in metabolic wave G3, analysis note section 14 |
| `PAPER P13` | 42219438 | **Short title:** Bjorklund 2026, Iron dysregulation in the central nervous system: implications for autism spectrum disorder (narrative review) · **Journal:** Biometals · **DOI:** 10.1007/s10534-026-00833-7 · **Evidence depth:** per receipt FTR-20261019-42219438-01 · **Role:** read in metabolic wave G3, analysis note section 15 |

Stub upgrades (op `update` on an existing record, integrator's form): the corpus stubs for Liu 2022 and Lo 2015 become full `PAPER` records with the receipt ids FTR-20261019-36364214-01 and FTR-20261019-25595191-01; the Sze 2015 row keeps its `LIT` record and gains receipt FTR-20261019-26355344-02.

## 3 · Claim-level proposals — all MINOR, none narrows a claim

1. **CLAIM 034 (context dependence of the WWOX-ROS sign):** add support-level mentions only: Liu 2022 (overexpression raises ROS and a senescence marker in rat tumour cells, ROS-dependence illustrated not shown) and Carvalho 2022 (high-glucose pTyr33-WWOX with higher mitochondrial H2O2 in SH-SY5Y; the peptide effect on H2O2 and on pTyr33 against glucose is not significant in either arm). Neither is a loss-of-function neuron measurement.
2. **CLAIM 010 (mitochondria, not senescent cells, as target):** the mitophagy review read here carries no senescence content and cannot arbitrate; record it as generic context support only.
3. **WWOX-ferroptosis sign:** two reports point opposite ways in non-neural systems (one read at abstract level, one unread); the working-model cell stays empty. No change.
4. **Kawabata 2024:** the WWOX row sits in a figure panel and a supplementary table, not in the text; the roughly 40 percent drop in WWOX transcript under chronic replication stress is recorded as hypothesis-grade (mRNA, one dividing cell type).
5. **Carvalho 2022:** the HELD-partial reading is closed at complete depth; text-versus-panel mismatches (Figures 2, 3, 5, 7 and 9) and the missing total-WWOX blot are recorded in the manifest and note. The registry revival trigger (a total WWOX report beside pTyr33-WWOX) is not met.

## 4 · Reading debts carried (gene-direct references not read here)

- **Lo 2015 minireview:** fifty-seven gene-direct references, thirteen with complete receipts; the unread primaries to prefer are the photoreceptor mitochondrial translocation paper (a blocked row), the MPP+ and Tyr33 paper, the two Zfra papers and the 2004 tau paper (receipted nowhere).
- **Carvalho 2022:** seven references with no receipt of any kind (Chang 2003, Sze 2004, Lo 2008, Teng 2012, Tabarki 2015, Huang 2018, Chang 2007) and seven with partial receipts only.
- **Sze 2015 commentary:** Sze 2004, Hsu 2009 and Lo 2008 have no receipt; Chang 2014 and Chang 2015 partial (the latter now extended by this wave's movie reading).
- **Ganapathy 2026:** reference 14 (WWOX protective against ferroptosis in acute lung injury) is paywalled; manual PDF request logged.

## 5 · Staged leads (not appended to the discovery ledger: one shared file, the Orchestrator appends)

1. **PUFA-TG and lipid-droplet bridge (Puertas-Frias):** in donor-derived WWOX-deficient fibroblasts read BODIPY area per cell, targeted TG lipidomics and GPX4. Falsifier: no difference at equal passage.
2. **Replication-stress hypomorph dose (Kawabata):** WWOX protein and mitochondrial ROS in a donor-derived line under the same aphidicolin schedule; a protein null closes the lead.
3. **Junction microhomology of human WWOX copy-number alleles (Ambroziak):** score published breakpoints against a chance model, with PARK2 as comparator (CLAIM 029 context). Counter: germline events from earlier generations.
4. **BNIP3 and BNIP3L under WWOX loss (Zhang):** transcript plus LC3/TOMM20 colocalisation in the WWOX-deficient lines.
5. **Iron observables in WWOX case reports (Bjorklund):** scan reports already in the repository for ferritin, haemoglobin or susceptibility imaging; record "none stated" per report.
6. **MAM terms against the WWOX interactome (Truong):** look up the seven tether and channel proteins in the interactome paper already receipted.
7. **Total WWOX beside pTyr33 with an inactive-peptide arm (Carvalho):** the experiment that would separate peptide inhibition from WWOX consumption.

## 6 · Parked rows and retried routes (blocked rows of the G3 table)

Retried with new routes on 2026-10-19 and left closed: the Drosophila respiration paper (repository record has no file), the 2025 and 2023 ferroptosis papers and the 2005 paper named in the selection file (no open copy through PMC, Europe PMC, Unpaywall, OpenAlex or Wayback). The 2026 hybrid open-access paper (PMID 41443103) returns HTTP 403 from the publisher and the publisher API needs a key, which is reserved and was not used. Cascade for each: operator-supplied PDF, or a licensed route.

## 7 · Shared surfaces left to the Orchestrator

batch_queue, coverage_report, reading_state and pathograph were not regenerated by this task; the commit gate was passed with the stale-surface override each time (recorded in the task contract DEFAULTS_TAKEN).

### LOCATOR TRIPLES FOR BLIND AUDIT

No scientific proposition in a current file is changed by this candidate; the triples below pin the three findings most likely to be quoted.

- [PMID 35984507, artefact `files/fulltext/PMID35984507_Carvalho2022_PMC11071800_wayback20240101.html`] (Zfra1-31 diminished (~ 64%) the levels of activated WWOX (pWWOX tyr33) | Zfra1-31 diminished (~ 64%) the levels of activated WWOX | Results, inhibition of WWOX activation by Zfra1-31 protects)
- [PMID 35984507, artefact `files/fulltext/PMID35984507_Carvalho2022_PMC11071800_wayback20240101.html`] (the EI condition promoted a twofold reduction in the levels of this lipid peroxidation marker | the EI condition promoted a twofold reduction in the levels of this lipid peroxidation marker | Results, oxidative stress and damage)

**Not medical advice.**
