# COMMIT CANDIDATE — CC-20261019-SCIENTIST-C-W4-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, task W4-W2A-C-20261019, 2026-10-20.
**Target working-model version:** the current one at integration (no WM bump requested).
**Change class:** **MINOR.** It creates registry presence for eight papers that have none and records negatives for the W2 axes; it narrows no baseline claim and reverses none. No scientific current file is touched. `context_policy: SOURCE_FIRST` for all eight (first reads). **Not medical advice.** Rows 6-8 are SUBSTITUTES and are not WWOX evidence.

## 0 · Why

Group W2 (metabolic axes not yet covered) first half, file order, excluding the known-unreachable Teslovich row. Five rows are WWOX-direct or WWOX-locus (tumour genomics or tumour genetics), three are disease-class substitutes. The result for every axis is a stated absence of WWOX evidence with the reason.

## 1 · Numbers are provisional

The Orchestrator owns numbering; placeholder ids `PAPER W01`-`W08` and no `LIT` numbers are claimed.

## 2 · Ops — `disease-models/wwox/registries/paper_registry_current.md` (op `append`, new record each, no `old`)

| provisional id | PMID | record text |
|---|---|---|
| `PAPER W01` | 25779665 | **Short title:** Chen 2015, UV/cold shock switches apoptosis to bubbling cell death at low temperature (WWOX/WOX1, p53, TRAF2, NOS2) · **Journal:** Oncotarget · **DOI:** 10.18632/oncotarget.3153 · **Evidence depth:** per receipt FTR-20261020-25779665-01 · **Role:** the only WWOX-direct temperature paper: cultured cell lines and MEFs; temperature is a post-irradiation culture condition; Wwox-/- MEFs RESIST bubbling death (about 0-2% versus 28/45/85%); one frostbite IHC pair with no stated n; ATP independence and HIF1A involvement are "data not shown"; nine movies unretrievable. No thermoregulation or in vivo cold datum. |
| `PAPER W02` | 36587184 | **Short title:** Friemel 2022, single-cell ploidy in NASH-induced HCC and NAFLD/NASH (miFISH, WWOX probe) · **Journal:** Sci Rep · **DOI:** 10.1038/s41598-022-27173-z · **Evidence depth:** per receipt FTR-20261020-36587184-01 · **Role:** WWOX copy-number loss in 4 of 11 HCC (headline) and none in 11 NAFLD/NASH specimens; Figure 3A marks 15% WWOX loss in case 1, absent from Table 1; no loss threshold stated; Supplementary Figure 3 case 3 WWOX 44 in the gains column coloured green in one copy and red in the other; cases 4 and 5 have no panel. Tumour genomics only. |
| `PAPER W03` | 41141138 | **Short title:** Sharma 2025, WWOX and RUNX2 IHC in Ewing sarcoma, 7 cases versus 5 unspecified controls · **Journal:** Cureus · **DOI:** 10.7759/cureus.93160 · **Evidence depth:** per receipt FTR-20261020-41141138-01 · **Role:** WWOX unchanged (P = 0.876), RUNX2 higher (P = 0.005); controls never identified; survival caption (median 45 months), curve (median about 8 months, plateau about 29%) and table (6 of 7 dead) disagree; no stratified survival. A pilot-power negative for WWOX. |
| `PAPER W04` | 37686047 | **Short title:** Rushing 2023, NCI-60 multi-omics and alkylating-agent sensitivity · **Journal:** Int J Mol Sci · **DOI:** 10.3390/ijms241713242 · **Evidence depth:** per receipt FTR-20261020-37686047-01 · **Role:** WWOX is a CNV gene-list line (22 markers, Q4 mean about -0.17 versus +0.19); transcript not significantly different (fold 0.73-0.95, smallest P about 0.074); CREAMMIST expression correlates weakly negatively with IC50 for five agents (rho -0.20 to -0.25; Table S3, not in the text); the metabolic result is purine metabolism, not WWOX. |
| `PAPER W05` | 22842668 | **Short title:** Płuciennik 2012, genetic alterations of WWOX in Wilms' tumour (23 tumours) · **Journal:** Oncol Rep · **DOI:** 10.3892/or.2012.1940 · **Evidence depth:** per receipt FTR-20261020-22842668-01 · **Role:** the "LOH in 30.4%" is observed hemizygosity; Table I gives predicted LOH 4.4% (intron 8) and 0 (intron 1); methylation (about 2-3 tumours) goes with lower expression; semi-nested 77-cycle PCR; six-sample blot does not match the 40-280-fold mRNA range; no renal-function or metabolic readout. |
| `PAPER W06` | 29899766 | **Short title:** Mastrangelo 2018, treatable inborn errors of metabolism causing epilepsy (narrative review) · **Journal:** J Pediatr Neurosci · **DOI:** 10.4103/JPN.JPN_160_16 · **Evidence depth:** per receipt FTR-20261020-29899766-01 · **Role:** SUBSTITUTE. The work-up checklist (Table 1 image) and the statements that a lacking pyridoxine response "has no diagnostic value" and that the folate disease is defined by CSF 5-methyltetrahydrofolate. No WWOX occurrence. |
| `PAPER W07` | 36980111 | **Short title:** Mastrangelo 2023, epilepsy phenotypes of vitamin B6-dependent diseases (systematic review, 497 patients) · **Journal:** Children (Basel) · **DOI:** 10.3390/children10030553 · **Evidence depth:** per receipt FTR-20261020-36980111-01 · **Role:** SUBSTITUTE. Pyridoxine: 173 seizure-free and 38 reduced of 312 treated; a seizure endpoint only, possibly delayed; EEG response not a criterion; no comparator; reporting gaps (IQ for 50 of 497). |
| `PAPER W08` | 38978529 | **Short title:** Girgis 2024, cerebral folate transport deficiency, two Egyptian cases · **Journal:** J Epilepsy Res · **DOI:** 10.14581/jer.24005 · **Evidence depth:** per receipt FTR-20261020-38978529-01 · **Role:** SUBSTITUTE. CSF 5-methyltetrahydrofolate not measured (diagnosis by exome); routine metabolic screen normal; response to folinic acid unquantified; case 1 variant labelled nonsense but written p.R128W. |

## 3 · Claim-level and axis proposals — all MINOR, none narrows a claim

1. **W2 axes with no WWOX evidence stay empty, with reasons:** body temperature (cell-death assays only, and WWOX loss protects in the one assay), liver steatosis (tumour genomics; no change in NAFLD/NASH tissue), bone and RUNX2 (pilot-power negative), one-carbon and amino acids (a gene-list line plus an unsupported text sentence), kidney (tumour genetics, LOH rate overstated in the text), vitamin B6 and folate (substitutes only).
2. **Hypothermia in the whole-body null** (read in the HELD-PARTIAL wave) has no mechanistic bridge in 25779665: record "no WWOX evidence for a thermoregulatory mechanism".
3. **CLAIM 025 and RL-003:** no change; the NCI-60 expression-IC50 correlation and the NASH-HCC copy-number data are tumour-context observations and must not be cited as metabolic evidence.

## 4 · Reading debts carried

- Chen 2015: nine supplementary movies not retrievable; the laboratory's UV/TRAF2/p53 primaries (references 12-17, 20, 22) not opened.
- Friemel 2022: Table 1 versus Figure 3A count and Supplementary Figure 3 case 3 colour conflict need the authors or the workbook; cases 4 and 5 unverifiable.
- Sharma 2025, Płuciennik 2012, Rushing 2023: gene-direct references have no PMIDs in the markup or PDF; none asserted; Rushing Tables S1, S4, S6 dumped but only searched.
- Mastrangelo 2018 and 2023, Girgis 2024: substitutes; their cited primaries were not opened.

## 5 · Staged discovery leads (not appended to the shared ledger; the Orchestrator appends)

1. **WWOX expression against alkylator sensitivity in the NCI-60 panel (Rushing, Table S3):** test the weak negative correlation (rho about -0.2) against copy number and methylation per cell line; falsifier: the correlation disappears after tissue-of-origin adjustment.
2. **Count WWOX loss properly in the NASH-HCC series (Friemel):** request or re-derive per-case loss percentages at a stated threshold; falsifier: case 1 below the threshold used for cases 2, 3, 7, 8.
3. **Temperature as an in vivo variable in Wwox-null pups (Chen 2015 with Chou 2020):** core temperature against body weight in weight-matched controls; falsifier: equal temperature at equal weight.
4. **Normalised redox and amino-acid panel in a WWOX-deficient neural line:** carried from the earlier HELD-PARTIAL candidate; nothing here changes it.
