# COMMIT CANDIDATE — CC-20261019-SCIENTIST-C-H4-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, task INTERV-H4-C-20261019, 2026-10-19.
**Change class:** **MINOR.** It creates registry presence for fifteen papers that have none, records reading debts and carries staged leads; it narrows no claim and reverses none. No scientific current file is touched. Not medical advice; class level only.
`context_policy: SOURCE_FIRST` for every paper. Analysis note: `interventions_wave_20261019_scientist-c.md`.

## 0 · Why

Group H4 (oxygen, hypoxia/hyperoxia, HIF) of `interventions_batch_selection_20261019.md` was read in tier order: fifteen new rows. **None of the fifteen studies oxygen as an intervention in a WWOX-deficient system, and WWOX is named in only one body (a gene list); the group's WWOX-direct anchor, Liu 2022 (PMID 36364214), was receipted in wave 1 of this actor and was not re-read.** Registry identities (`registry_records.py get --pmid N --hops 1`) were empty for all fifteen, which is a statement about that query over those files.

## 1 · Numbers are provisional

The Orchestrator owns `PAPER` and `LIT` numbering across four Scientists. Placeholder ids `PAPER H01`-`H15` are used.

## 2 · Ops — `disease-models/wwox/registries/paper_registry_current.md` (op `append`, new record each, no `old`)

| provisional id | PMID | record text |
|---|---|---|
| `PAPER H01` | 42420651 | **Short title:** Garg 2026, hypoxia rescues an HTRA2-deficient mouse by a complex I mechanism (not WWOX) · **Journal:** Nat Metab · **DOI:** 10.1038/s42255-026-01566-0 · **Evidence depth:** per receipt FTR-20261019-42420651-01 · **Role:** tier 1 substitute, analysis note section 2 |
| `PAPER H02` | 39087877 | **Short title:** Zhao 2025, OSA inflammatory-protein Mendelian randomisation with WWOX as one positional gene hit · **Journal:** Sleep · **DOI:** 10.1093/sleep/zsae169 · **Evidence depth:** partial, per FTR-20261019-39087877-01 · **Role:** section 3 |
| `PAPER H03` | 26578889 | **Short title:** Lopez-Ramos 2015, brain glycogen, hypobaric hypoxia and seizure susceptibility in a glycogen-synthase knockout mouse · **Journal:** Front Cell Neurosci · **DOI:** 10.3389/fncel.2015.00431 · **Evidence depth:** per FTR-20261019-26578889-01 · **Role:** section 4 |
| `PAPER H04` | 38074156 | **Short title:** Ma 2023, intermittent hypoxia as the link between OSAS and epilepsy (narrative review) · **Journal:** Front Pharmacol · **DOI:** 10.3389/fphar.2023.1230313 · **Evidence depth:** per FTR-20261019-38074156-01 · **Role:** section 5 |
| `PAPER H05` | 37726428 | **Short title:** Villa 2023, repeated postictal hypoxia and interictal cognition in kindled rats · **Journal:** Sci Rep · **DOI:** 10.1038/s41598-023-42741-7 · **Evidence depth:** per FTR-20261019-37726428-01 · **Role:** section 6 |
| `PAPER H06` | 37876811 | **Short title:** Liang 2023, HIF-1 alpha/HO-1, ferroptosis markers and epilepsy (WWOX in a DisGeNET list only) · **Journal:** iScience · **DOI:** 10.1016/j.isci.2023.108098 · **Evidence depth:** partial, per FTR-20261019-37876811-01 · **Role:** section 7 |
| `PAPER H07` | 41324728 | **Short title:** Kuang 2025, HIF-1 alpha/BNIP3 autophagy and KC7F2 in LiCl-pilocarpine rats · **Journal:** Mol Neurobiol · **DOI:** 10.1007/s12035-025-05406-2 · **Evidence depth:** per FTR-20261019-41324728-01 · **Role:** section 8 |
| `PAPER H08` | 41039661 | **Short title:** Huang 2025, MeCP2, hypoxia and oxidative stress in Rett syndrome (narrative review) · **Journal:** Epigenomics · **DOI:** 10.1080/17501911.2025.2568303 · **Evidence depth:** per FTR-20261019-41039661-01 · **Role:** section 9 |
| `PAPER H09` | 42428241 | **Short title:** Khaksari 2026, fNIRS cortical oxygenation in Glut1 deficiency (title says reduced; body shows higher left-prefrontal HbO and mostly null intervals) · **Journal:** Front Neurosci · **DOI:** 10.3389/fnins.2026.1838150 · **Evidence depth:** per FTR-20261019-42428241-01 · **Role:** section 10 |
| `PAPER H10` | 28119904 | **Short title:** Perrone 2016, oxygen use in neonatal care (review) · **Journal:** Front Pediatr · **DOI:** 10.3389/fped.2016.00143 · **Evidence depth:** per FTR-20261019-28119904-01 · **Role:** section 11 |
| `PAPER H11` | 40022130 | **Short title:** Serdar 2025, prenatal inflammation plus 80 percent oxygen in the neonatal rat brain · **Journal:** J Neuroinflammation · **DOI:** 10.1186/s12974-025-03389-4 · **Evidence depth:** partial, per FTR-20261019-40022130-01 · **Role:** section 12 |
| `PAPER H12` | 42763430 | **Short title:** Moore 2026, 2 versus 20 percent oxygen in mouse OPC culture (the title's hyperoxia is room air) · **Journal:** ASN Neuro · **DOI:** 10.1080/17590914.2026.2698260 · **Evidence depth:** per FTR-20261019-42763430-01 · **Role:** section 13 |
| `PAPER H13` | 42652189 | **Short title:** Alekseeva 2026, AMPA versus NMDA blockade in rat hyperbaric-oxygen seizures · **Journal:** Biomedicines · **DOI:** 10.3390/biomedicines14081807 · **Evidence depth:** per FTR-20261019-42652189-01 · **Role:** section 14 |
| `PAPER H14` | 39965572 | **Short title:** Blume 2025, HypoxyStat, a haemoglobin left-shifter, in Ndufs4 knockout mice · **Journal:** Cell · **DOI:** 10.1016/j.cell.2025.01.029 · **Evidence depth:** per FTR-20261019-39965572-01 · **Role:** section 15 |
| `PAPER H15` | 38206902 | **Short title:** June 2024, acute seizures in neonatal inflammation-sensitised hypoxia-ischaemia in mice · **Journal:** PLoS One · **DOI:** 10.1371/journal.pone.0295860 · **Evidence depth:** partial, per FTR-20261019-38206902-01 · **Role:** section 16 |

## 3 · Claim-level proposals — all MINOR, none narrows a claim

1. **CLAIM 009 (WWOX, mitochondrial quality control, redox and energy efficiency):** add a scope note only. The two hypoxia-therapy papers (Garg 2026, Blume 2025) show hypoxia rescues disease when an electron-transport lesion lowers tissue oxygen use and raises tissue oxygen; that precondition is **not established** for WWOX loss (the respiratory-complex report is unavailable). Villa 2023 shows seizure-linked tissue hypoxia and lowered mitochondrial respiration in kindled rats (non-WWOX). Supports a stated gap, not a link.
2. **CLAIM 025 (WWOX/HIF1A axis, theme hit):** support-level mention only: Liang 2023 and Kuang 2025 show HIF-1 alpha raised in two acquired-epilepsy rodent models, so **raised neural HIF-1 alpha is not specific to WWOX loss** and cannot serve as a WWOX marker. Garg 2026 finds HIF targets LOWER in a hyperoxic mutant striatum, so the direction of the HIF signal depends on the primary lesion.
3. **No claim on oxygen as an intervention:** the repository holds no WWOX-deficient evidence on supplemental oxygen, nocturnal helmet or CPAP, intermittent hypoxia, hyperbaric oxygen or hypoxia therapy; four oxygen-group papers state the opposite risks (hyperbaric oxygen provokes seizures; hyperoxia injures developing oligodendrocytes; the lower saturation target raised neonatal death in SUPPORT and BOOST II; drug-based hypoxia is covalent and not acutely reversible). This is a standing negative for the intervention register, class level only.

## 4 · Reading debts carried

- **Closed-body WWOX-direct papers (cascade: Europe PMC search, OpenAlex open-access flag, 2026-10-19; Unpaywall not used because it needs an e-mail parameter):** PMID 23566416 (TAZ versus WWOX in HIF-1 activation under hypoxia), PMID 25447306 (hypoxia, HIF-1 alpha and Hippo regulators, WWOX mentioned), PMID 19737107 (hypoxia-regulated WWOX adenovirus), PMID 26390919 (WWOX and the respiratory complex; already BLOCKED). All four: not in Europe PMC, OpenAlex closed. Manual PDF requests.
- **Two WWOX/WOX1 Alzheimer's-disease reviews** (PMIDs 22202011 and 23277037, same title, 2012 and 2013): no PMC body; ROS and cell-death content only.
- **Primaries behind the oxygen reviews, not opened:** the SUPPORT, BOOST II, COT, STOP-ROP and BOOST I reports (Perrone), the 1994 CPAP series (Ma), Farrell 2016 postictal hypoxia (Villa), Yuen 2014 and Allan 2021 HIF-1/Olig2 (Moore).
- **Supplements declared not_read** in four partial receipts: Zhao Tables S1-S17 and S1-S2 figures; Liang Tables S1 and S3; Serdar nine supplementary figure panels; June (three identical workbooks, structure only).
- **PubMed CommentIn on Zhao 2025** (a Sleep 2024 comment on Mendelian randomisation in OSA biomarker studies): not read.

## 5 · Staged leads (not appended to the discovery ledger)

1. **WWOX case-report oximetry scan (IPOTESI):** scan reports already in the repository for overnight oximetry, polysomnography or breathing-pattern statements; record "none stated" per report. Falsifier: any report stating normal sleep oximetry. Counter: absence of a statement is not absence of the finding.
2. **Incubator-oxygen control for WWOX-null oligodendrocyte cultures (IPOTESI):** culture at 2 versus 20 percent oxygen; Moore 2026 shows mouse OPC growth and survival differ about 2.6-fold in apoptosis; any WWOX-null versus control myelination readout is confounded by oxygen unless matched.
3. **Tissue pO2 in a WWOX-null brain (IPOTESI):** the hyperoxia rationale of hypoxia therapy needs a measured tissue oxygen or iron-sulfur protein proxy (Garg 2026 used the proxy); without it, hypoxia or HIF logic cannot be transferred.
4. **fNIRS feasibility note (ESPANSIONE):** Khaksari 2026 shows task fNIRS is feasible at a patient conference in older, higher-functioning patients; its own headline conflicts with its figures, so it is a feasibility datum, not a biomarker.
5. **Neonatal oxygen-window caution (DATO, class level):** the only trial-derived numbers in the group are preterm saturation targets (90 to 95 percent suggested for infants under 28 weeks); they do not apply to a genetic encephalopathy without a stated gap.

## 6 · Safety (BLOCK-1) summary, class level

Hyperbaric oxygen (6 ATA in rats within tens of minutes; clinical protocols 1.5 to 2.5 ATA) provokes generalised seizures; hyperoxia (80 percent for 48 h in rat pups) injures oligodendrocytes without a second hit; low saturation targets raised death in extremely preterm trials; hypoxia therapy in mice is irreversible when delivered by haemoglobin modification and raises haematocrit to about 52 to 59 percent. None of this was tested in WWOX-deficient systems. Nothing here is medical advice.
