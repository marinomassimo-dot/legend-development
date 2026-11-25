# ADV-276 continued, batch 1: the five lead papers re-opened and receipted (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. PREREG `PREREG_ADV276B_BATCH1_SCI_20261125.md` (commit 0029f5182, 12:20:33Z, before any paper was opened in this window; not blind to checkpoint AH). Bytes: the ADV-272 XML under `files/fulltext/PMID<pmid>_ADV272_*` (root checkout; digests in the receipts; five of five are byte-identical to the files the earlier receipts fingerprinted). New today by permitted routes: supplements of PMC3783369, PMC9756969 and PMC3938399 from the Europe PMC `supplementaryFiles` endpoint; figures and supplements of PMC7617807 from the PMC open-data bucket (`pmc_bucket_fetch.py`). Route results, not obstacles: Europe PMC returned 500 for PMC3315540 and 503 for PMC7617807; the PMC article page of PMC7617807 returned a reCAPTCHA check and was not pursued. No delegate, no spend, no contact.

## 1. Answer first

* **Three consumers need a wording change**, two pass.
* **40500435 (fructose): the "2.7-fold" is the labelled lactate, not whole-brain lactate.** The total lactate pool rose about 2.5-fold.
* **36530994 (ADI-PEG 20): every number in `DL-MECH-057` reproduces from the supplement, but the lead names the wrong first author** (Chu, not Chen).
* **24086726 (Sakai): "power 42 percent" is at alpha 0.05, not at the study's own Bonferroni 0.0055** (about 14 percent there, my approximation); Table 4 prints an HOMA-IR effect that does not fit its own SE and p.
* 23435430 and 22479346 pass. The p73 negative of 23435430, which rested on a sentence, now rests on the figure (Supplementary Figure S3).
* Checkpoint AH said the Sakai and Santini supplements were not held, which was true then; and it said "power 42 percent needs Table S3". Table S3 and S2 had been read by `scientist-b` in October (dossier lines 14 and 15), so the number was not unsupported.

## 2. Predictions scored

| | Prediction | Observed |
|---|---|---|
| 1 | consumer wording changes for 4 of 5 (3 to 5) | 3 of 5: inside the range, below the point value |
| 2 | at least one AH locator or number does not reproduce (30 percent) | not met for locators; one AH reading is corrected (the "2.7-fold" read from the figure panel is the labelled series) |
| 3 | a consumer carries an error AH did not report (60 percent) | **met**: the author name in `DL-MECH-057`; the series confusion in the fructose candidate; the alpha of the power figure |
| 4 | no direction reversed (85 percent) | met |

## 3. Per paper

### 3.1 23435430, Santini 2014, ATM and ITCH (human HEK293T and HepG2 cells; Atm-null mice). Consumer `DL-METH-093`: **passes**

Read: Results, Discussion, Methods, supplement legends (7 pages); images of Figure 4 (panels A to D) and Supplementary Figures S2 (A) and S3.

* Figure 4A: both lanes carry transfected ATM and ITCH; they differ only by KU-55933. No lane without ATM. The phospho-serine antibody is pan (ab9332). Confirmed.
* Ser161: "identified as putative phosphorylated sites" by NetPhos and ScanSite; "pull down experiments allow to speculate" is in the Discussion. Confirmed.
* **p73 (Supplementary Figure S3, panel labelled B):** HEK293T, ITCH-Myc wild type with p73-HA and Ub-FLAG, without and with ATM: the ubiquitin smear is not increased by ATM. One blot; no densitometry and no replicate count printed. The lead's "p73 non cambia" is about p73 **ubiquitination**, not p73 protein level.
* Searches in the XML text and in the supplement text, 2026-11-25, case-insensitive: `WWOX` 0; `K48`, `K63`, `linkage`, `polyubiquitin chain` 0; `kinase assay`, `in vitro kinase`, `mass spectrometry` 0.
* Wording for IT: none. Optional precision for the lead: "p73 ubiquitination (one blot, Supplementary Figure S3)".

### 3.2 22479346, Yang 2012, young-onset hypertension (human; 400 matched pairs, Han Chinese in Taiwan). Consumers `DL-MECH-180`, `run_B_after_report.md`, `PAPER 324`: **passes**

Read: abstract, Results with Tables 2 and 3, Discussion with its limitations, Methods.

* IGF1 (12q23.2) and WWOX (16q23.3 to q24.1) are two of the four genes of 17 that replicated in the Hong Kong family study; none of the four replicated in the British data. `IGFBP7`: 0 hits (2026-11-25), so that half of the consumer's sentence rests on PMID 28763065 alone.
* The Discussion groups IGF1, SLC4A4 and WWOX as earlier candidates "primarily associated with obesity, glucose metabolism, and ion homeostasis". That is a literature grouping of three genes, not a measured WWOX to IGF link.
* The expression step is 12 against 12 genotype-extreme people chosen from the same data; `PAPER 324` already says "genotype-extreme pairs".
* Wording for IT: none.

### 3.3 36530994, Chu 2022, ADI-PEG 20 in advanced hepatocellular carcinoma (humans; post-hoc). Consumers `DL-MECH-057`, candidate G2-HUMAN-AXIS: **numbers reproduce; one attribution error**

Read: Methods, Results, Discussion; supplement Tables S2, S5 and S8 (`DataSheet_1.docx`).

| Cohort | Table | GG / non-GG (patients) | Mean OS, months | Univariate HR (95% CI), p | Adjusted HR (95% CI), p |
|---|---|---|---|---|---|
| monotherapy, 113 | S2, row `WWOX-rs13338697 "GG"` | 9 / 104 | 15.1 (6.7 to 23.4) / 8.1 (6.8 to 9.3) | 0.382 (0.165 to 0.887), 0.025 | 0.420 (0.180 to 0.980), 0.045 |
| plus mFOLFOX6, 47 | S5, same row | 5 / 42 | 10.3 (0.0 to 22.8) / 10.1 | 1.716 (0.571 to 5.153), 0.336 | not entered |
| pooled, 160 | S8, same row | 14 / 146 | 13.4 (7.2 to 19.4) / 8.7 | 0.602 (0.311 to 1.164), 0.131 | not entered |

* 9 + 104 = 113; 5 + 42 = 47; 14 + 146 = 160; 9 + 5 = 14.
* **`DL-MECH-057` cites "Chen et al. 2022"; the first author is Chu (Chu YD, Liu HF, Chen YC, Chou CH, Yeh CT).**
* `interaction`: 0 hits in the main text and in the supplement (2026-11-25): the lead's demand for a treatment by genotype interaction test stands, and none is reported.
* Table S2 prints 24 univariate hazard ratios for overall survival (my count of its rows); no multiplicity correction is stated; the multivariate model holds only the two that passed.
* The Discussion prints the SNP as `rs13339697` several times against `rs13338697` elsewhere.
* Wording for IT (not applied): in `DL-MECH-057`, "Chen et al. 2022" to "Chu et al. 2022".

### 3.4 24086726, Sakai 2013, Japanese replication (human blood DNA; 5,315 cases, 2,064 controls). Consumer candidate G2-HUMAN-AXIS and its dossier: **two precisions**

Read in full: abstract, Introduction, Methods, Results, Tables 1 to 4, Discussion; supplement Tables S2 and S3 (S4 in part, S1 not).

* Table 3, row rs17797882, risk allele C, frequency 0.799 / 0.792: unadjusted p 0.3355, OR 1.04 (0.95 to 1.14); adjusted p 0.7521, OR 1.01 (0.91 to 1.12). Table 2 genotype counts 3,349 / 1,709 / 199 and 1,289 / 664 / 92 give allele frequencies 0.7996 and 0.7927 and an allelic OR of 1.04: reproduces.
* Table 4 uses **controls only**: HOMA-IR and HOMA-beta n = 893, fasting glucose n = 1,325, not 7,379.
* **Table 4, HOMA-IR effect printed "0.0015 (0.028), p 0.5941": the effect does not fit its SE and p** (0.0015 / 0.028 gives p about 0.96; 0.015 / 0.028 gives about 0.59). My inference: a misplaced digit in the source. The candidate's entry 4 copies the printed value.
* **Table S3, row rs17797882: power 42 percent is for alpha = 0.05** (CaTS, prevalence 10 percent, reported OR 1.08, allele frequency 0.792), the lowest of the nine. The study's own threshold is 0.0055: my normal approximation of an allelic test gives 40 percent at 0.05 and **about 14 percent at 0.0055**.
* The same table's required-sample column (66,327 cases at 0.05; 110,247 at 0.0055) is on another basis (Quanto) and does not scale with its own power column; do not quote it as this study's shortfall without saying so.
* Table S2: with controls aged 50 or older (n = 1,057) OR 0.94 / 0.95; 60 or older (n = 622) 0.89 / 0.88; 40 or older (n = 1,424) 0.99 / 1.00. The candidate's entries 7 and 8 reproduce.
* Wording for IT (not applied): "power 42 percent" to "power 42 percent at alpha 0.05 (about 14 percent at the study's Bonferroni 0.0055, SCI approximation)"; add "(printed value; probably 0.015)" beside the HOMA-IR effect.

### 3.5 40500435, Wang 2025, neonatal high fructose and microglia (mice). Consumer candidate G2-FRUCTOSE: **change**

Read: the Results subsections on microglial metabolism and on behaviour, the legends of Figures 3 and 4, Methods (mice, diet, NMR, statistics); Figure 3 image (`EMS206505-f003.jpg`, 800 x 443, sha256 `335ff7c7941d2e99f12d0350f2bef112a1abbb206262e18646a38fab4e30e310`). Not a read of the whole paper.

Measured by me from Figure 3b pixels (axis ticks located; means from the error-bar caps or the bar top; about 3 to 5 percent measurement error):

| Figure 3b panel | WT control diet | WT high fructose | Ratio | Mice |
|---|---|---|---|---|
| `[2-13C]-lactic acid`, umol/g | 0.138 | 0.373 | **2.7** | 4 / 5 |
| `1H NMR - lactic acid pool`, umol/g | 4.33 | about 10.6 | **about 2.5** | 4 / 5 |
| GLUT5 knockout, pool | 4.40 (control diet) | 3.73 (high fructose) | | 5 / 5 |

* The labelled lactate is about 3.5 percent of the pool in the high-fructose pups (0.37 of 10.6).
* In the pool panel, of the five high-fructose wild-type pups one dot (about 5) lies inside the control range (about 4 to 5); in the labelled panel the two groups do not overlap.
* Timing and dose: P7 pups, **15 minutes** after one injection of 4 g/kg `[2-13C]-fructose` (about 20 mg in 200 uL). The text and legend say intraperitoneal; the Methods say "intraperitoneally via the quadriceps". Both values are after the injected load, in dams-on-diet pups; no uninjected brain lactate is reported in these passages.
* Unit: mice; litter as a unit is not stated.
* `WWOX`: 0 hits (2026-11-25).
* Wording for IT (not applied): "raises whole-brain neonatal lactate about 2.7-fold" to "15 minutes after a 4 g/kg labelled fructose injection at P7, labelled lactate is about 2.7-fold and the total brain lactate pool about 2.5-fold higher in pups of fructose-fed dams (about 4.3 to 10.6 umol/g; Figure 3b, 4 and 5 mice; SCI pixel measurement)".

## 4. Which wording lines are blind re-derived

None is blind: the window had read checkpoint AH. The fructose series assignment, the author name, the alpha of the power figure and the HOMA-IR digit were **not** in AH; they are single-reader findings and want a second reader before a card or claim edit.

## 5. Coverage and limits

Depths in the receipts `RECEIPT_ADV276B_<pmid>_SCI_20261125.json`: four `partial_fulltext_read`, 40500435 `queried_not_full_read`. No receipt is a complete read. Figure images unopened except those named. The 14 percent and the pixel values are my computations.

## 6. Lamotrigine port (commit 313a5438a, diff text sha256 `eab24a33fa4dcd08ebdb3e4bd7165d884f24816c9f719b7969334ee162cecc76`)

* **Most of it was already on main.** Commit `df514a059` (24 November) had landed a condensed `lamotrigine/clinical_review.md`, the lamotrigine README paragraph and the link from the continuous-compounds README.
* Of the diff's content lines, what main lacked was per-source precision. It is added as a dated study-level note in `clinical_review.md` after re-reading the three primary records; the title, the review paragraph, the abstract-only line for PMID 42721537 and both README lines were not ported because main already says them.
* All three source rows of the diff reproduce. One sentence was reworded from the source: the affected relative was never seen by the authors and not genotyped. "Nor excluding a possible effect" is carried in substance.
* Receipts: `FTR-20261125-24456803-01`, `FTR-20261125-31353122-02`, `FTR-20261125-35792847-01`, all `queried_not_full_read`.
