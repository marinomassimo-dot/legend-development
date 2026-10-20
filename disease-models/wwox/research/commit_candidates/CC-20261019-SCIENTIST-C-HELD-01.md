# COMMIT CANDIDATE — CC-20261019-SCIENTIST-C-HELD-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, task HELD-PARTIAL-WWOX-C-20261019, 2026-10-19 and 2026-10-20.
**Target working-model version:** the current one at integration (no WM bump requested).
**Change class:** **MINOR.** It closes figure and supplement debts on ten WWOX-direct partial receipts, adds one metabolic datum to an existing record and corrects labels. It narrows no baseline claim and reverses none. No scientific current file is touched. `context_policy: QUESTION_DRIVEN` throughout. **Not medical advice.**

## 0 · Why

The HELD-partial rows of the two selection files were re-read each against a question written before the owed section was opened (note: `held_wave_20261019_scientist-c.md`, section 1). Eight re-reads closed figure or supplement debts; two WWOX-direct rows (Gao 2025, Chong 2023) could not be acquired lawfully and are parked. The numbers below are provisional; the integrator assigns ids.

## 1 · Ops on existing records (integrator's form)

| target | op | content |
|---|---|---|
| `PAPER 129` (Chou 2020, Wwox-/- mouse skin) | `update` role and evidence depth | Add the metabolic content the record omits: Figure 8, subcutaneous fat layer about 10 versus 270 um (n = 3), few shrunken FABP4-positive adipocytes, dorsal skin surface temperature 31.3 versus 35.8 C (n = 15 versus 12), heterozygote indistinguishable from wild type; the authors' sentence that fat loss causes hypothermia is untested; no body weight, glycaemia or intake is reported and the Figure 4 photographs show the null pups runted from P2. Record the pERK comparison as region-level (25 regions, 3 mice). Evidence depth: figures now read (receipt FTR-20261019-33195192-03); references unread. |
| `PAPER` record of Baryla 2022 | `update` | Figures 1-4, 7-12 and S1-S6 now read. Uptake sign is condition-specific (knockdown above control only in normoxia normoglycaemia; the Discussion sentence "upregulated in WWOX KO cells" generalises it); hypoxia plus hyperglycaemia is not a depleted contrast (WWOX mRNA and protein unchanged in that condition); uptake assay is serum-free for 48 h; Methods fractionation 6 h versus Figure S4 caption 48 h; overexpression also raises lactate. Lactate remains the one direction-stable readout. |
| `PAPER` record of Hammouz 2026 | `update` | Main figures acquired and read: no survival panel in Figures 1-5; Hallmark glycolysis and hypoxia enriched in low-ratio groups in four of five strata, MYC targets in high-ratio groups in all five, no oxidative-phosphorylation row although the Results state enhanced oxidative phosphorylation for high ratios; HIF1A is in the ratio's denominator; glycolysis does not track DFS across subtypes; FDR up to 0.25. CLAIM 025's evidence boundary is unchanged. |
| `PAPER` record of Kosla 2019 | `update` | Figures 2 and 11 and Supplementary Table 1 read: PrestoBlue curve about 32% lower in knockdown hNPC at 270 min, raw RFU with no normalisation and no n; oxidative-gene PCA has one point per group; Table S1 gives contributions not directions, HIF1A ranks last of 35, HK2 29th. The record may carry "one un-normalised redox readout in a human neural cell" and no HIF1A or glycolysis statement. |
| `PAPER` record of Cheng 2023 | `update` | Figure 6 read (previously recorded not read): ROS is one unquantified DHE histogram; NAC rescues SA-beta-gal and CDK-inhibitor levels with WWOX still absent; ROS not re-measured after NAC; the p53 point mutations are one clone; p16 or p21 re-expression restores senescence downstream of WWOX; Supplementary Figure 8 early-passage redox transcript signature (G6pdx, Nfe2l2, Nqo1, one sample per genotype) precedes any measurable ROS difference. |
| `PAPER` record of Liu 2021 (TUBB, WWOX SNPs, dyslipidaemia) | `update` | Figures read: Table 6 prints the G-T haplotype odds ratio as 111.055 with a CI of 7.818-15.633 that excludes it (stray digit; the adjusted value is 15.08); D' between the two WWOX SNPs is 0.87 and 0.81; effects behind the stars are about 0.1-0.2 per carrier; Table 3 header prints 1229 for 1129. Boundary unchanged. |
| `PAPER` record of Liu 2021 Nature Genetics (progression to dementia in Parkinson's disease) | `update` and label correction | Supplement read: Supplementary Table 3 holds a second WWOX-region variant (HR 3.49, discovery P 2.72e-8, replication P 0.59) distinct from the main-text one (HR 2.12, replication 0.01); "the WWOX locus" is two signals about 240 kb apart; no WWOX-region row in Supplementary Data 1. **The selection file's phrase "AD progression signal" is wrong: the disease is Parkinson's disease dementia.** |
| `PAPER` records of the Zfra review, Dong 2022 | `update` | Zfra review: all figures read, none holds a WWOX-null metabolic arm. Dong 2022: Figure 2 is an LDLR panel with no WWOX datum. |

## 2 · Claim-level proposals — all MINOR, none narrows a claim

1. **RL-003 next action ("CNS-specific data and metabolic biomarkers").** Record two CNS-adjacent items with their limits: the hNPC PrestoBlue curve (one assay, un-normalised) and the whole-body-null fat and temperature figures (a runted, near-lethal animal). Neither is a neural metabolic measurement in a WWOX-null brain.
2. **Uptake as a carrier readout.** Any proposal that names glucose uptake as a WWOX readout must name oxygen, glucose and serum condition; the only supporting panel reverses sign between conditions and between loss and gain.
3. **CLAIM 025.** No change.
4. **Disease-model coverage.** The Parkinson's-dementia label must not be read as Alzheimer's anywhere the selection file was quoted.

## 3 · Reading debts and parked items (carried, not closed)

- **Gao 2025 (WWOX-related developmental and epileptic encephalopathy) and Chong 2023 (WWOX epileptic encephalopathy): parked.** Cascade run on 2026-10-20: Europe PMC (not open access, not in PMC), Unpaywall (closed), OpenAlex (closed, no repository copy), Semantic Scholar (openAccessPdf status CLOSED), Crossref (publisher link only), CORE (no hit). No lawful body is available. Routes left to the operator: publisher access through an institutional login, or an author request. The earlier operator-supplied PDF of Gao 2025 was not retained.
- **Schuchardt 2013 (WW1 and ErbB4 binding):** figures are not retrievable by a lawful route in this session (the PMC bucket carries XML and text only, Europe PMC refused the image URLs, the PMC site returned a reCAPTCHA after one successful landing-page request). Binding biophysics; the question expected a negative. See the note for the state at close.
- Hammouz 2026 manifest keeps five inherited waived deep-dive slots (group, field density, multihop, cross-query, retraction).
- Cheng 2023: supplementary figures other than Supplementary Figure 8 not rendered as images.

## 4 · Staged discovery leads (not appended to the shared ledger; the Orchestrator appends)

1. **Normalised redox readout in WWOX-depleted human neural progenitors (Kosla).** Repeat resazurin with cell-number or protein normalisation plus a second mitochondrial readout (membrane potential dye, oxygen consumption) in the same hNPC knockdown. Falsifier: no difference after normalisation.
2. **Weight-matched or pair-fed controls for the Wwox-/- fat and temperature phenotype (Chou).** Compare subcutaneous fat, FABP4 and core temperature in null pups against weight-matched wild-type pups or pair-fed littermates. Falsifier: equal fat and temperature at equal weight.
3. **Direction of the G6PD and NFE2L2 contribution in the hNPC data against the mouse fibroblast heatmap (Kosla, Cheng).** Obtain the fold changes behind Supplementary Table 1 and compare with the early-passage Wwox-null redox set. Falsifier: opposite signs.
4. **ROS re-measurement under NAC (Cheng).** DHE flow in NAC-treated null MEFs and p53 sequencing in NAC-treated clones. Falsifier: ROS unchanged by NAC, or p53 mutation unchanged.
5. **Serum-replete glucose uptake (Baryla).** Repeat the 2-deoxyglucose assay in the four conditions with and without serum and with a dose series of WWOX depletion. Falsifier: sign does not depend on serum, or tracks dose monotonically.
