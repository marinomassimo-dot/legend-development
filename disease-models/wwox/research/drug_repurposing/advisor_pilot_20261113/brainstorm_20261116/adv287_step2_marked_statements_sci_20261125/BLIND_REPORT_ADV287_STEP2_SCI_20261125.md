# BLIND_REPORT_ADV287_STEP2_SCI_20261125

Blind reader report, package ADV-287 step 2 (16 card sentences, src_02 to src_22). Hypothesis level; reference genotype class only; nothing here is medical advice.

Setting: requested model sonnet (Sonnet 5.5), effort high. The effort actually applied is not visible to me; a reasoning-effort marker in my context read 10 (scale not stated), so the Orchestrator should read the transcript, not this line.

Inputs used: the 16 files blind_packet/src_KK.md. Beyond them I opened only what a src file points to: the package `missense_recovery_it5_p8_20261029/` (README sections 3, 4, 6 and `required_fold_arithmetic_20261029.tsv`, for src_02), and the held figure images `files/figures/PMID42157447/ACN3-9999-0-g003.jpg` (src_02), `files/figures/PMID30266908/41467_2018_6507_Fig3_HTML.jpg` (src_03), `files/figures/PMID34634460_r2/gr4.jpg` and `gr5.jpg` (src_12). Helper scripts: `/home/desktop/.claude/jobs/488a3ad0/tmp/adv287s2b/` (s06.py, s09.py, s20.py, s22.py; run with `python3 -P -E`). I did not open the Obeid 2026 article or any of its files (no src file pointed only to it), the frozen RP-045 prediction, or any ADV-174/ADV-175 material. No access control refused anything. No web, PubMed, search, download or contact.

Rule used for figure readings: a by-eye or pixel difference is turned into a verdict only when it exceeds the stated reading error.

---

## k = 02 (card A01_pba_class, against/5; marked word "every" in "unmeasured for every WWOX allele")

**Sentence.** "...parity needs the reciprocal of (amount times function per molecule), which is unmeasured for every WWOX allele, and observed gains (about 1.05 to 9 fold) also apply to wild type."

**(a) Claims.** (1) Parity fold = 1/R, with R = amount x function per molecule relative to wild type. (2) R is unmeasured for every WWOX allele (universal over WWOX alleles). (3) Observed amount gains in non-WWOX precedents span about 1.05 to 9 fold (range with two extremes). (4) The gains also apply to wild type.

**(b) Recomputation.**

Claim (1): arithmetic only. R 0.5, 0.25, 0.1, 0.01 gives parity fold 2, 4, 10, 100 (`required_fold_arithmetic_20261029.tsv`, rows 1 to 6). Correct.

Claim (2). The set is WWOX alleles with any protein-level or function measurement. Members in the material:
- Q230P, patient fibroblast, Johannsen 2018: abundance only (transcript comparable, protein band not detected on one membrane). No function, no quantity.
- P252A, Zhang 2025, stable overexpression in CAL-62 and BCPAP thyroid-cancer lines, xenografts in nude mice: protein "much lower" than wild type, faster turnover, rescued by chloroquine or NH4Cl; loss of growth, invasion and migration inhibition. All qualitative statements, no fraction of wild type.
- P282A, same paper: protein similar to wild type, loss of the same cancer-suppressor readouts. So amount is about wild type and function is reported "lost", but never as a fraction of wild type, in a non-neural overexpression system.
- Package README section 3: six WWOX missense have any protein-level measurement; "function (none)"; "No enzymatic assay of any kind". The repository files for the other four are not reproduced in the src file, and I read only the package's summary row, not the underlying census.
- No allele has R, or either factor of R, as a quantified fraction of wild type in the held material. A qualitative "lost" exists for P252A and P282A in a cancer assay. I read "unmeasured" as "not quantified". Under that reading the word is supported. If the card means no function readout of any kind, it is overstated for these two alleles.

Claim (3). Folds recomputed.
- DeLeeuw 2026 Figure 4G (GAT-1 heterozygous, HEK293T, bars as % of WT; pixel table in the src; baseline row 990, WT = 297.6 px). PBA/vehicle:
  - D52Y: vehicle (990-942)/297.6 = 0.161, PBA (990-718)/297.6 = 0.914, fold 5.7 (5.3 to 6.0 with +-3 px on the vehicle bar).
  - V125M: 0.141, 0.988, fold 7.0 (6.5 to 7.5).
  - A357V: 0.081, 1.045, fold 13.0 (11.5 to 14.8).
  - G566H: 0.071, 1.364, fold 19.3 (16.9 to 22.6).
  - The src's rounded table gives 5.6, 7.0, 13.0, 19.3. TUDCA/vehicle: 4.3, 5.0, 11.6 (G566H not measured).
  - I looked at the image: vehicle bars of A357V and G566H sit near 0.1 and treated bars near 1.05 and 1.37, so the fold is about 10 to 17 by eye at lowest. Every reading is above 9 for two of the four variants, and the excess is far outside the +-3 px error.
- The package row quoted in the src reads GAT-1 "about 6 to 9 (R1 reading, Fig 4G)". That does not match the bars.
- Guiberson 2018 (Munc18-1; package readings, not recomputed here): neurons about 1.0 to 1.7 (src_03 package table per variant, PB_total_fold 1.05, 1.25, 1.25, 1.4, 1.65); HEK293T about 1.5 to 2.1. The "1.05" lower end exists as the package value for P480L (neurons) and as butyrate on the G544D mutant in HEK293T (README section 4). The package notes that values near 1.05 are not separable from 1.0.
- Song 2026 (GABRA1, HEK293T, PBA 2 mM, from the verbatim percentages): all increases give 1.19 (WT or F325L) to 2.68 (A322D, Fig 3B, 168.4%); the largest variant increase in Fig 2B is 2.63 (A322D 163%). The package's "1.6 to 3.1" top value of 3.1 is not in the text I hold (maximum 2.68). This does not move the overall range.
- DeLeeuw Figure 5F (HA-tagged WT GAT-1 total protein, PBA/vehicle, by eye, no pixel error stated): WT about 2.4, A288V 1.4, S295L 2.2, V511M 1.3. Butyrate A288V about 1.05.
- Derived range across the precedents: about 1.05 to about 19 fold (GAT-1 Figure 4G, bar reading, mouse and human-cell mix not applicable: all HEK293T or neurons, unit = blots/wells/experiments). The stated top "9" is below the held bars for two of four GAT-1 variants.

Claim (4):
- Wild-type gains are observed in Munc18-1 (WT raised about 1.2 to 2 in the same experiments, package), Song (WT total α1 1.19 to 1.46, from the percentages 19.2, 29.8, 46.2), DeLeeuw Fig 5F (WT about 2.4 by eye), and Shah 2025 (small molecules enhanced WT GABA uptake, text only).
- Figure 4G has no treated-WT bar, and Figure 4A states "PBA and TUDCA had no effect in WT cells" for uptake (function).
- The wild-type gains observed are 1.2 to about 2.4, not 6 to 19. The large folds arise from a baseline of 0.07 to 0.16 of WT and are not shown to apply to WT.

**(c) Class: WRONG** (number: top of the range).

**(d) Carrier: OTHER.** The marked word "every" is supportable in the "not quantified" sense (qualification above). The error sits in "(about 1.05 to 9 fold)" and, secondarily, in the claim that the whole range "also apply to wild type" (observed WT gains are about 1.2 to 2.4).

**Corrected sentence.** "...parity needs the reciprocal of (amount times function per molecule), which no held WWOX measurement quantifies for any allele (P252A and P282A are reported as losing growth-suppressor function in thyroid-cancer overexpression assays, without a fraction of wild type), and the observed amount gains in non-WWOX precedents (derived about 1.05 to about 19 fold, the top from GAT-1 Figure 4G bar readings; derived about 1.2 to 2.4 fold on wild type in the same precedents) are also seen on wild type."

---

## k = 03 (card A01_pba_class, against/6; marked words "the only" in "is not the only candidate")

**Sentence.** "The measured turnover difference (about 1.5 to 3 fold) explains only a small part of a 12 to 25 fold steady-state deficit in the soluble precedent, so the 'made then cleared' branch is not the only candidate even where turnover is measured."

**(a) Claims.** (1) Turnover difference about 1.5 to 3 fold. (2) Steady-state deficit 12 to 25 fold. (3) Turnover explains only a small part of (2). (4) "Not the only candidate" (a non-uniqueness statement: at least one other explanation is open).

**(b) Recomputation.** Guiberson 2018 Figure 3, Munc18-1 variants; panels a, b mouse knockout neurons (lentivirus, n = 3 independent experiments), panels c to f HEK293T (n = 4 to 6).
- Deficit = 100 / (% of WT total protein), Fig 3a pixel table: R406H 100/8.7 = 11.5; P480L 100/4.7 = 21.3; G544D 100/7.0 = 14.3; G544V 100/9.3 = 10.8; P335L 100/66 = 1.5 (the fifth variant, excluded as "four of five"). Four-variant range 10.8 to 21.3 (pixel reading, +-0.5 pp gives about 10.2 to 23.8).
- The package reading (R406H 8, P480L 5, G544D 4, G544V 7) gives 12.5, 20, 25, 14.3, so 12.5 to 25. The two readings differ for G544D (4 vs 7.0) and G544V (7 vs 9.3), more than +-0.5 pp. The enlarged thumbnail I opened cannot arbitrate (bars about 5 to 9 %). So "12 to 25" follows the package reading; the packet's pixel reading gives about 11 to 21.
- Turnover. Fig 3b, neurons, % of 0 h: WT 44 at 24 h; mutants 8 to 25. First-order rate ratio k_mut/k_WT at 24 h: ln(1/0.25)/ln(1/0.44) = 1.69 to ln(1/0.08)/ln(1/0.44) = 3.08. At 3 h (WT 78, mutants 52 to 62): 1.9 to 2.6. At 8 h (WT 54, mutants 22 to 37): 1.6 to 2.5. Fig 3e (HEK293T photoconversion, % of 0 h at 24 h): WT 53, other four 26 to 35 gives 1.65 to 2.1; P335L 43 gives 1.33. So "about 1.5 to 3" holds.
- Log share: ln(1.7 to 3.1) / ln(11 to 25) is about 0.2 to 0.35, so a minor part. At equal synthesis the turnover ratio would give at most about 3 fold against about 11 to 25.
- The legend and text state mRNA is unchanged (Supp Fig 4a to c), so a synthesis-side or early-loss explanation is open and untested.

**(c) Class: CORRECT** for the marked words. The non-uniqueness claim follows from the rate arithmetic, as long as synthesis is equal across variants (not shown either way).

**(d) Carrier: none.** Residual flag on a number (OTHER, not a verdict): the endpoints 12 and 25 depend on the package's readings (G544D 4 %); the packet's own pixel table gives about 11 to 21. Suggested wording: "a deficit of about 11 to 25 fold (two readings of Figure 3a)".

---

## k = 06 (card D01_a51, against/2; marked word "the one" in "than at the one below")

**Sentence.** Seven dose levels, N 1, 1, 3, 3, 3, 8, 5; printed CVs 4.1 to 79 percent (cohorts of three or more); day 5 AUC roughly proportional to dose from the second to the sixth cohort (log-log slope about 0.95 by end points, about 0.98 over five points); supralinear only when the lowest cohort (one patient) is included (slope about 1.38); 1.27-fold higher at the top cohort than at the one below for a 2.0-fold dose ratio.

**(a) Claims.** N list; CV range; two slopes; the 1.38 slope with the 1 mg cohort; a fold ratio between the top cohort and "the one below" (a unique cohort: the immediate predecessor in dose order).

**(b) Recomputation** (Supplemental Table 3, adult BTX A51 phase 1, patients, mean AUC day 5 ng*hr/mL): doses 1, 3, 5, 8, 11, 21, 42 mg; AUC D5 43.0, 600, 702, 937, 1820, 3773, 4773.
- N column: 1, 1, 3, 3, 3, 8, 5 (matches).
- CVs printed in the table, all columns: 45, 22, 58, 69, 6.4, 51, 15, 4.1, 26, 79, 26, 77, 64, 46, 50, 48, 79, 22, 30. Range 4.1 to 79; cohorts N=1 carry none. Matches (AUC D5 alone: 4.1 to 77).
- Two-point slope, 3 mg to 21 mg: ln(3773/600)/ln(7) = 0.945. Five-point regression (3, 5, 8, 11, 21 mg): 0.983. Matches.
- Six points including 1 mg (1 to 21 mg): 1.382; all seven points: 1.215; 3 to 42 mg: 0.891; 1 mg to 3 mg step alone: 2.40. So the supralinear value 1.38 is the 1 to 21 mg regression (the seven-point value is 1.21, still supralinear). Every subset I tried without the 1 mg point gave a slope below 1 (0.89 to 0.98).
- Top cohort vs the one below: the cohort below 42 mg is 21 mg. 4773/3773 = 1.265, dose ratio 42/21 = 2.0. Matches.

**(c) Class: CORRECT.**

**(d) Carrier: none.** Note: the means are from N=5 (42 mg, CV 30 %) and N=8 (21 mg, CV 48 %); the 1.27 is a ratio of two means with wide CVs. The 1.38 slope is for 1 to 21 mg, not all seven cohorts (1.21).

---

## k = 07 (card E02_ldh_inhibition, against/6; the heading names no marked word, so I tested its universals "no enzyme-level support" and "no fitted LDH potency")

**Sentence.** "...there is no enzyme-level support for stiripentol as a way to test the LDH node - 7 percent inhibition at 2 millimolar (ChEMBL) and about 10 percent at 0.5 millimolar (independent report), no fitted LDH potency among the curated database entries read for it, a label that does not name LDH;"

**(a) Claims.** (1) ChEMBL 7 % at 2 mM. (2) About 10 % at 0.5 mM, independent report. (3) No fitted LDH potency among the database entries read. (4) The label does not name LDH. (5) No enzyme-level support (universal negative over enzyme-level readings of stiripentol on LDH).

**(b) Recomputation.**
- Rows parsed: 88 of 88; by type AC50 37, Inhibition 20, Activity 15, FC 4, IC50 3, Potency 3, ED50 2, EC50 1, Ki 1, %max 1, Inhibition index 1 (matches the stated count).
- Rows whose assay text or target mentions LDH, lactate or dehydrogenase: 8. Rows 26 and 27 (CHEMBL4311969, human LDH5 and LDH1, 2 mM, "=" 7.0 %); rows 28 and 29 (0.5 mM, no relation and no value); rows 47 to 50 (CHEMBL5120856, FC cell rows). None of the IC50 (rows 18, 43, 44), Ki (19), EC50 (24) or Potency (1, 2, 15) rows concerns LDH. So (1) and (3) hold. The ChEMBL 0.5 mM rows are empty, so the ChEMBL source gives no 0.5 mM value.
- (2): Rico-Molina 2024 Table 2, recombinant human LDHA, 500 uM, racemate 9.9 +- 2.3 % (n = 4 per the repository). Holds for the racemate.
- (4): the label text names GABA-A and CYP inhibition as possible mechanisms and says the mechanism is unknown. Holds.
- (5): the same Rico-Molina Table 2 gives (-)-(S)-stiripentol 34.0 +- 2.1 % and (+)-(R)-stiripentol 38.4 +- 1.6 % at the same 500 uM; the Discussion attributes about 40 % at 500 uM to Sada 2015 (second-hand, abstract only held); the repository record adds a treated-cell lysate with significant LDH inhibition at 250 and 500 uM (Yadav 2026). These are enzyme-level or lysate-level inhibition readings of stiripentol on LDH, single concentration, no IC50. The sentence cites only the racemate (about 10 %) and the ChEMBL point (7 %). The spread within the held record is about 7 to 40 % (7 % at 2 mM; 9.9, 34.0, 38.4 % at 0.5 mM; about 40 % at 0.5 mM second-hand).

**(c) Class: INCOMPLETE** (comparator rows left out). The parts about 7 %, about 10 %, no fitted potency and the label are correct.

**(d) Carrier: WORD** (the universal "no ... support" over the enzyme readings). Corrected: "there is no fitted LDH potency for stiripentol among the 88 ChEMBL rows read, and the enzyme-level readings are single-concentration partial inhibitions without an IC50: 7 percent at 2 millimolar (ChEMBL, human LDH5 and LDH1), 9.9 percent for the racemate and 34.0 and 38.4 percent for the enantiomers at 0.5 millimolar (Rico-Molina 2024, recombinant human LDHA), about 40 percent at 0.5 millimolar attributed second-hand to Sada 2015; the label does not name LDH;".

---

## k = 08 (card E02_ldh_inhibition, next_measurement; no marked word named, so I tested "the one cell-level signal", "no enzyme-level support" and the numbers)

**Sentence.** "...stiripentol is not sufficiently supported as an LDH-engagement probe, because the readable enzyme data give 7 percent inhibition at 2 millimolar and about 10 percent at 0.5 millimolar (no fitted value: no enzyme-level support), the US label names no LDH mechanism, and the one cell-level signal found (four rows of a 2022 glycolate-oxidase and LDHA double-inhibitor series: relative oxalate output 0.27 to 0.70 at 10 micromolar in mouse hepatocytes) does not establish LDH engagement;"

**(a) Claims.** Same enzyme and label claims as k=07. New: "the one cell-level signal found" is four rows, relative oxalate output 0.27 to 0.70, 10 uM, mouse hepatocytes, 2022 series; the signal does not establish LDH engagement.

**(b) Recomputation.** The 88-row table is identical to k=07 (diff of the two tables shows no difference).
- The four FC rows (47 to 50, CHEMBL5120856): 0.27 (PH2, 24 h), 0.33 (PH2, 48 h), 0.70 (PH3, 24 h), 0.49 (PH3, 48 h) relative oxalate output at 10 uM, mouse primary hepatocytes. Range 0.27 to 0.70, matches. Three more rows of the same document (51 to 53) are cytotoxicity rows with no value.
- Among the 88 ChEMBL rows these four are the only cell-level rows tied to LDH (rows 28 to 29 and 26 to 27 are enzyme-level). If "found" means "found in the ChEMBL pull", the one-document claim is true.
- The sentence does not say "in ChEMBL". The repository record in the src (section 2.2) lists cell-level LDH-related signals from the literature: Guyon 2022 (glioblastoma stem-like cells, lactate production -50 % over 24 h at 500 uM, Laconic FRET); Le Dudal 2019 (HepG2, dose-dependent fall in oxalate, LDHA siRNA also lowers it, stiripentol on top of siRNA lowers it "mildly", n = 4); Yadav 2026 (U87, ECAR and OCR fall, 10 to 60 uM viability); Bouchez 2026 (respiration down, complex I). These were in the record (dated 2026-10-26 to 27) before the IT8 P3 text (2026-10-29). So "the one cell-level signal found" is not the only one in the held material; none isolates LDH.
- The enzyme-level incompleteness of k=07 (enantiomers 34.0 and 38.4 %, second-hand about 40 %) also applies to "the readable enzyme data give 7 and about 10 percent".

**(c) Class: INCOMPLETE.**

**(d) Carrier: WORD** ("the one cell-level signal"). Corrected: "...and, among the ChEMBL rows read, the only cell-level rows tied to LDH are four rows of CHEMBL5120856 (relative oxalate output 0.27 to 0.70 at 10 micromolar, mouse hepatocytes); the held literature adds cell-level lactate, oxalate and ECAR changes (Guyon 2022 lactate -50 percent at 500 micromolar; Le Dudal 2019 HepG2 oxalate; Yadav 2026 ECAR), none of which establishes LDH engagement;". The enzyme clause also needs the k=07 wording (the 34.0, 38.4 and about 40 percent readings).

---

## k = 09 (card E02_ldh_inhibition, next_measurement; marked word "every" in "30 fold or more on every pair")

**Sentence.** "...205 qualify, 116 have no LDHB datum at all, and, of the 89 with a same-document LDHA and LDHB pair, 74 have a pair under 10 fold and only 2 are 30 fold or more on every pair..."

**(a) Claims.** 205 molecules; 116 with no LDHB datum; 89 with a same-document pair (205 - 116 = 89); 74 with a pair under 10 fold; exactly 2 with ratio at least 30 on every pair (universal over pairs, per compound, with a count of exactly 2).

**(b) Recomputation** (ChEMBL human LDHA CHEMBL4835 and LDHB CHEMBL4940, pull of 2026-10-30; script s09.py over the two complete tables).
- Table 1: 205 unique molecule ids; all `ldha_best_nM_equals` at most 100 (none above); `n_ldhb_rows` = 0 for 116; the reading column splits 116 "no LDHB row" and 89 "same-document pair". Parent ids are unique (2 child records, no duplicates of a parent).
- Table 2: 185 pairs over 89 compounds (the set equals the 89 of Table 1); 182 with a ratio, 3 not formed (CHEMBL4065858 LDHA "<10"; CHEMBL4536094 and CHEMBL4543194 LDHA ">50000"). Table 1 pair counts agree with Table 2 for all 89.
- Compounds with at least one pair under 10 fold: 74. Under 1 fold: 30. At least one pair 30 fold or more: 23. Median of per-compound minima 2.545.
- Compounds with minimum ratio at least 30 (every formed pair at least 30): exactly 2: CHEMBL3763437 (one pair, LDH5/LDH1 Ki 30 nM / 8000 nM, ratio 266.7) and CHEMBL5597066 (one pair, IC50 44 nM / 15480 nM, ratio 351.8). Next highest minimum is CHEMBL4860066 at 21.8 (pairs 730.8, 21.8, 34.5; two of its three pairs pair a cell-based LDHA assay with recombinant LDHB). None of the three compounds with a not-formed pair changes the count: the censored pair of CHEMBL4065858 (LDHA below 10 nM against LDHB 441 nM, at least about 44 fold) sits beside formed pairs of 1.04, 1.04, 1.67 and 0.0075; the other two have formed ratios 3.5 and 3.8.

**(c) Class: CORRECT.**

**(d) Carrier: none.** Context, not an error: each of the 2 compounds has a single pair from a single document, so "every pair" is one pair each; the pairs in other compounds mix assay formats within a document.

---

## k = 10 (card F03_bumetanide_chloride_gradient, novelty; marked word "the one" in "the one human knockout deposit")

**Sentence.** "New: (1) the transcript-level ratio in the one human knockout deposit does not point to a depolarising gradient (descriptive, confounded);"

**(a) Claims.** (1) SLC12A2/SLC12A5 ratio is not higher in knockouts. (2) "The one human knockout deposit": exactly one deposit with a human WWOX knockout in the set of public or announced transcript deposits of the census.

**(b) Recomputation.**
- Ratio, GSE156243 (human cerebral organoid, bulk RNA, culture week 15, unit = one library): cko1 5.02/20.97 = 0.239; cko2 5.55/19.22 = 0.289; cko3 5.49/41.33 = 0.133; cko4 5.53/39.03 = 0.142; cwt1 5.82/19.97 = 0.291; cwt2 4.65/15.64 = 0.297. Knockout 0.13 to 0.29, wild type 0.29 to 0.30 (4 vs 2 libraries, one knockout clone per the card's not_known entry). Not higher in knockouts. Holds (descriptive; SLC12A5 higher in two knockouts, GAD1 about ten-fold different).
- The set of human-knockout deposits in the census material:
  - GSE156243: human organoid, engineered knockout, public, 4 KO vs 2 WT. A member.
  - E-MTAB-14792 (ArrayExpress; Steinberg et al., Brain 2026): human organoid, "WWOX loss"; libraries WT, WWOX-KO, SCAR12, WOREE, WOREE-WWOX. The record exists (BioStudies returns 403, not 404) and is not publicly accessible. It is an announced deposit with a human knockout library. A member of "public or announced". It is single-cell, not bulk.
  - GSE126075: the census text describes WWOX knockdown of unquantified depth in hNPC and neurons (CAGE), not knockout. Not a member.
  - GSE229210: human glioma lines, WWOX overexpression. Not a member. GEO queries: 39 series, 16 with knockout, knockdown, mutant or siRNA terms, 7 neural WWOX-perturbation series.
- So the set has two members (one accessible, one announced and not accessible), not one. "The one" holds only for the accessible one.

**(c) Class: INCOMPLETE.**

**(d) Carrier: WORD** ("the one"). Corrected: "New: (1) the transcript-level ratio in the one publicly accessible human knockout deposit found (GSE156243; 4 knockout vs 2 wild-type organoid libraries, ratio 0.13 to 0.29 against 0.29 to 0.30) does not point to a depolarising gradient (descriptive, confounded); a second human WWOX-knockout organoid library exists in E-MTAB-14792 but returned 403 and is unread;".

---

## k = 11 (card F04_nmdar_intervention_class, DR-P9-006; marked word "the one" in "the one addition is I150V")

**Sentence.** "the one addition is I150V, which keeps potency but reaches 31 percent maximal inhibition against 85 percent at wild type)."

**(a) Claims.** Among the 27 variants, exactly one lies outside the 5 potency-loss variants yet has significantly reduced maximal inhibition: I150V. I150V keeps potency (33 nM vs 35 nM) with 31 % against 85 %.

**(b) Recomputation** (Banke 2026 Table 2, human GluN1/GluN2B in Xenopus oocytes, two-electrode voltage clamp; n = recordings per variant; asterisk = P < 0.05 after FDR).
- Potency-loss set (asterisked IC50 higher than WT 35 nM): A639V 1041, I655F 181, A652G 113, M818T 79, S810R 53 nM. That is five, as the text states (23, 4.5, 3.2, 2.8, 1.9 fold). Potency gain (asterisked IC50 lower): W607S 20, G611V 24, N616I 25, N616S 22, E657G 21.
- Asterisked maximal inhibition: I150V 31 %, A639V 37 %, A652G 71 %, I655F 66 %, M818T 81 %. Five variants, the same five the text names. No other row carries an asterisk on inhibition (lowest unmarked value: V620M 77 %).
- Variants with reduced maximal inhibition and no potency loss: only I150V (n = 10; IC50 33 nM, no asterisk, 31 % with asterisk, against WT 85 %, n = 253). The four others are in the potency-loss set. S810R is a potency loss without a maximal-inhibition change. No GluN1 variant is asterisked.
- 31 vs 85: ratio 0.36 (the text's "2.0 to 4.4 fold" is expressed on residual current, not shown here and not checked).

**(c) Class: CORRECT.**

**(d) Carrier: none.**

---

## k = 12 (card F04_nmdar_intervention_class, evidence_against/0; marked word "largest")

**Sentence.** "The largest synaptic change in the source is inhibitory (sIPSC amplitude 27.5 against 57.3 pA in controls, frequency also reduced), not excitatory."

**(a) Claims.** Among every synaptic measure reported in Breton 2021 (mouse Synapsin-Cre Wwox knockout, neocortical slices P13 to P17; mEPSC, sEPSC, sIPSC amplitude and frequency; evoked neocortical NMDAR response; evoked hippocampal fEPSP and population spike), the largest change is the sIPSC amplitude; the quoted numbers; frequency also reduced.

**(b) Recomputation** (S-CTL = heterozygote plus wild type; means with SD of pooled events; cells: sEPSC S-CTL 18 cells/10 animals, S-KO 17/10; sIPSC S-CTL 14/7, S-KO 9/5).
- sIPSC amplitude 27.5 vs 57.3 pA: ratio 0.480, change -52 %. Matches.
- sIPSC frequency 8.4 vs 10.3 Hz: ratio 0.816, -18 %. Reduced, matches.
- sEPSC amplitude 24.7 vs 23.3 pA: +6.0 %. sEPSC frequency 10.1 vs 9.9 Hz: +2.0 %.
- mEPSC amplitude: no mean printed. In Fig 4B (image gr4.jpg) the S-KO cumulative curve shifts by a few pA in the large-amplitude tail and the inset averages sit near -10 pA (KO slightly larger than WT), roughly 10 percent by eye; I do not turn that into a number. mEPSC frequency: S-WT vs S-KO p = 2.4e-4 and S-WT vs S-HT p = 0.0018, no magnitude printed; decay time 5.18 vs 4.84 ms. 
- Evoked neocortical NMDAR response: "larger than S-WTs at multiple stimulus strengths", appears in S-KO and "not observed in the wildtype controls"; the magnitudes sit in Supplementary Fig S3, which is not held. Not assessable.
- Evoked hippocampal: Fig 5D, maximal population spike, CA1 to CA3 direction, S-WT about 1.3 mV and S-KO about 2.25 mV by eye (p = 0.0312, WT n = 6 slices/5 animals, KO n = 8/4); the difference of about 0.95 mV is far above the bar-reading error (about 0.05 mV), so about +70 % (different scale and a field spike, not a synaptic current). CA3 to CA1 PS and both fEPSPs: no difference (p 0.72, 0.99, 0.79).
- On the measures with printed means, the sIPSC amplitude is the largest change (-52 % against +6, +2 and -18 %). Across the named set, a +70 % evoked PS in one direction is of the same order and bigger in percent (smaller in fold: 2.1-fold decrease against about 1.7-fold increase); the neocortical evoked response and the mEPSC amplitude have no printed magnitude.

**(c) Class: INCOMPLETE** (comparators in the named set, evoked responses and mEPSC, left out or with no printed magnitude; ranking depends on the metric).

**(d) Carrier: WORD** ("largest"). Corrected: "Among the spontaneous synaptic currents with printed means, the largest change is the sIPSC amplitude (27.5 against 57.3 pA in controls, derived -52 percent; frequency 8.4 against 10.3 Hz, derived -18 percent) against sEPSC amplitude +6 percent and frequency +2 percent (derived); the mEPSC amplitude is increased without a printed size, and the evoked neocortical NMDAR response and the CA1-to-CA3 population spike (about +70 percent by eye) are not compared on the same scale."

---

## k = 13 (card G01_lithium_gsk3, not_known/2; marked word "independent" in "four independent experiments")

**Sentence (fragment).** "...(the legend says postnatal day 20 and the Methods say 14) reports LOWER phospho-Ser9, as a ratio to beta-actin, with representative results of four independent experiments and the number of animals not stated (registry CLAIM 035 Evidence boundary..."

**(a) Claims.** The source reports lower pSer9-GSK3b/actin in knockout brain; the legend says "representative results of four independent experiments"; the animal number is not stated; legend P20, Methods P14.

**(b) Recomputation.** Cheng 2020, Figure 7c, mouse Wwox +/+, +/-, -/- lysates, one lane per genotype per region, one blot per protein (nine lanes), no N.
- pSer9/actin, +/+ vs -/-: cerebellum 2.7 vs 1.3 (ratio 0.48), hippocampus 3.6 vs 2.0 (0.56), cortex 3.9 vs 2.5 (0.64). Lower in all three. Total GSK3b/actin: 2.2, 2.3, 2.2 vs 2.4, 2.6, 2.6 (ratio 1.09, 1.13, 1.18), not lower. pSer9 to total: 0.54, 0.77, 0.96 in -/- vs 1.23, 1.57, 1.77 in +/+.
- The legend verbatim says "The representative results of four independent experiments are shown." The sentence reports what the legend says, and attributes it. Legend "postnatal day 20" and Methods "postnatal day 14" both present. Panel c carries no N; Methods name only anti-WWOX, anti-DCX and anti-beta-actin antibodies.
- "Independent" is the authors' word. The held material shows one blot and does not show whether the four experiments used independent animals or repeated lysates, so independence is not verifiable here.

**(c) Class: CORRECT** as a report of the legend.

**(d) Carrier: none.** Suggested hedge if the card is quoted elsewhere: "described in the legend as representative of four independent experiments (one blot shown, animal number not printed)".

---

## k = 16 (card H02_gabaat_inactivator_myelin_exposure, DR-H02-009 locator; marked word "every" in "ERGs every 3 to 6 months")

**Sentence.** "ERGs every 3 to 6 months without abnormality;" (within the locator: about 100 events a day before, 25 to 30 after about a year and a half; 18-hour EEG no electrodecremental responses; vigabatrin concurrent for the first year then weaned; ketogenic diet and clobazam; no repeat MRI described.)

**(a) Claims.** ERGs obtained at an interval of 3 to 6 months, all without abnormality; plus the locator's context items.

**(b) Recomputation.** Doumlele 2016, one human child, open-label case report. Text: "During treatment with CPP-115, electroretinograms (ERGs), complete blood count, and comprehensive metabolic panel were obtained every 3-6 months with no abnormalities." Discussion: "no evidence of retinal damage seen on regular ERGs". Context items: ~100 seizures per day before, ~25 to 30 per day after 1.5 years; 18-hour EEG "complete lack of electrodecremental responses"; vigabatrin given concurrently during the first year and weaned within 1 year; ketogenic diet and clobazam; no repeat MRI in the text. All match. The number of ERGs and their dates are not stated (the interval is stated, not a count); the paper adds "we cannot exclude long-term retinal toxicity" and the child had baseline cortical blindness.

**(c) Class: CORRECT.**

**(d) Carrier: none.**

---

## k = 17 (card H02_gabaat_inactivator_myelin_exposure, DR-H02-013; marked word "none" in "none in the other group")

**Sentence.** "...concomitant rapamycin (60 children, all in the tuberous sclerosis group, none in the other group) is associated with lower odds of the abnormality (multivariate odds ratio 0.152, 95 percent interval 0.028 to 0.715, p = 0.019, Table 3);"

**(a) Claims.** 60 rapamycin-treated children; all 60 in the tuberous sclerosis (IST) group; zero in the other-etiology (ISO) group; multivariate OR 0.152 (0.028 to 0.715), p = 0.019.

**(b) Recomputation.** Wan 2022 (human children, one centre; unit = child). Table 1: concomitant rapamycin IST (n = 80) 60, ISO (n = 92) 0, chi-square 105.96, p < 0.001. Text: "There were no children in the ISO group who received concomitant rapamycin therapy"; 60 + 0 = 60 = the stated total. Table 2: with rapamycin 60, without 20, 60 + 20 = 80 = IST. Table 3 multivariate (LASSO): rapamycin OR 0.152, CI 0.028 to 0.715, p = 0.019. All match. The TSC term in the same model is OR 0.788 (0.214 to 2.557), p = 0.702 (collinearity noted).

**(c) Class: CORRECT.**

**(d) Carrier: none.** "Associated with" is the right verb; rapamycin is collinear with the TSC group (all 60 treated children are in it).

---

## k = 18 (card H02_gabaat_inactivator_myelin_exposure, DR-H02-031; marked word "none" in "none of 56 unexposed children")

**Sentence.** "7 of 22 exposed children (32 percent, after excluding the index detection) against none of 56 unexposed children with infantile spasms;"

**(a) Claims.** 7 of 22 = 32 %; none of 56 unexposed children with infantile spasms showed the abnormality (zero count in a stated comparison group).

**(b) Recomputation.** Pearl 2009 (PMID 18783433), abstract only held: "7 of 22 (32%) patients treated with vigabatrin ... none of 56 patients with infantile spasms who were not treated with vigabatrin showed the same abnormalities." 7/22 = 31.8 %; 8/23 = 34.8 % with the index case (Discussion). The 56 are the only unexposed group of that study. Other unexposed groups in the batch rows are other studies: Stevering 2025, 7 of 52 untreated (13.5 %: 2 of 23 TSC, 5 of 29 non-TSC epilepsy) had VABAM-like abnormalities; PMID 20384718, 0 of 12 unexposed infantile-spasm children normal. These are not the Pearl cohort and not a contradiction of the sentence, but "none" is true only inside this source.

**(c) Class: CORRECT.**

**(d) Carrier: none.** Scope note: abstract-level source; keep the sentence tied to this study (for example "in that series") so the zero is not read across to the Stevering untreated groups.

---

## k = 20 (card K01_hif_axis_glycolytic_shift, functional_evidence_available; marked word "every" in "leaving out M6 changes every region")

**Sentence (with its clause).** "...the Adm increase in the three forebrain regions is a two-animal effect (M6 and F8; the other three mutants are within the wild-type range), so that leaving out M6 changes every region."

**(a) Claims.** (1) The Adm increase in HPC, CTX and PFC is carried by M6 and F8. (2) The other three mutants (M7, F9, F10) are within the wild-type range. (3) Leaving out M6 changes every region (referent not defined: four regions, or the three forebrain regions).

**(b) Recomputation** (GSE215425, mouse bulk RNA-seq, P47T/P47T vs WT/WT, one animal per library; Adm logCPM with prior 2 from the src's Table 1; script s20.py).
- Full-contrast Adm log2FC (P47T minus WT): HPC 0.957, CTX 1.194, PFC 0.809, CB 0.363. These equal the IT12 rows.
- Leave out M6: HPC 0.492, CTX 0.703, PFC 0.445, CB 0.372. Falls of 49, 41 and 45 percent in the three forebrain regions (all stay positive); CB moves from 0.363 to 0.372 (no change).
- Leave out M6 and F8: HPC 0.237, CTX 0.408, PFC 0.028, CB 0.282 (CB has one mutant left; CB also has no two-animal story, M6 CPM 1.41 vs WT 0.92 to 1.37).
- Six-gene set HIF_SEL_UP6 (src Tables 4 and 5): HPC 0.218 to 0.046; CTX 0.108 to -0.068 (sign flips); PFC -0.068 to -0.138; CB 0.187 to 0.174. So for the set, CB changes by 7 % and the PFC changes inside a null.
- "Other three within the wild-type range" (Adm CPM, WT min to max in the same region): PFC WT 1.92 to 3.36: M7 2.07, F9 2.04, F10 3.16, all within. CTX WT 1.17 to 3.19: M7 3.30 (+3 % above the maximum), F9 2.70, F10 2.54. HPC WT 1.42 to 2.17: M7 2.22 (+2 %), F10 2.58 (+19 %, above), F9 1.32 (-7 %, below). So the statement holds for PFC, is borderline for CTX (M7) and fails for HPC (F10, and M7 marginally). With Poisson noise at about 100 counts (about 10 %), F10 is about 1.8 noise units above.
- After removing both M6 and F8 the CTX Adm increase is still +0.41 log2 (1.33 fold), so "two-animal effect" is complete only for PFC.

**(c) Class: INCOMPLETE** (the referent of "every region" and the comparators are not specified; the claim does not hold for CB).

**(d) Carrier: WORD** ("every region"), with OTHER on the "within the wild-type range" clause. Corrected: "the Adm increase in the three forebrain regions falls by derived 0.36 to 0.49 log2 when M6 is left out (hippocampus 0.957 to 0.492, cortex 1.194 to 0.703, prefrontal 0.809 to 0.445) and to derived 0.03 to 0.41 when M6 and F8 are both left out; the cerebellar Adm value does not move (0.363 to 0.372); the other three mutants are above the wild-type range in hippocampus (F10, M7) and cortex (M7) by 2 to 19 percent in CPM."

---

## k = 21 (card K01_hif_axis_glycolytic_shift, next_measurement; marked word "independent" in "two independent knockout clones or lines")

**Sentence.** "Step 0: in WWOX-deficient versus corrected (isogenic add-back, two independent knockout clones or lines) human neural cells measure HIF-1alpha and HIF-2alpha protein..."

**(a) Claims.** A proposed design: two independent knockout clones or lines with isogenic add-back. No count, extremum or observed fact.

**(b) Recomputation.** The src states the field cites no data table or publication. Nothing to recompute. For orientation only (from src_10, not a verdict): the one accessible human knockout deposit, GSE156243, has four organoids of ONE clone (1B) and the other clone (A2) was not sequenced, so the existing deposit does not meet the design's "two independent clones". That bears on feasibility, not on the sentence.

**(c) Class: NOT ASSESSABLE** (a proposed design with no source claim; nothing to test).

**(d) Carrier: not applicable.** If a rule is wanted in the card, "independent" should be defined (for example two clones from different guide RNAs, each with its own add-back).

---

## k = 22 (card L01_nrf2_axis, functional_evidence_available; marked words "at least" and "every")

**Sentence.** "...in the deposited P47T brain the NRF2 target transcripts Hmox1 and Srxn1 are modestly higher in all four regions (+0.3 to +0.7 log2), Nqo1 is mixed, Gclm and Txnrd1 flat [ADV-239: Srxn1 keeps at least 70 percent of its rise without any one animal in every region;"

**(a) Claims.** (1) Hmox1 and Srxn1 up in all four regions, +0.3 to +0.7 log2. (2) Nqo1 mixed. (3) Gclm and Txnrd1 flat. (4) After leaving out any one animal, Srxn1 keeps at least 70 % of its rise, in every region (lower bound over all single removals, over all four regions).

**(b) Recomputation** (GSE215425, mouse bulk RNA-seq, one animal per library; HPC, CTX, PFC 5 WT vs 5 P47T, CB 4 vs 3; script s22.py from the per-animal Srxn1 unit values).
- Hmox1 log2FC: 0.710, 0.512, 0.343, 0.297 (HPC, CTX, PFC, CB). Srxn1: 0.417, 0.543, 0.476, 0.307. Joint range 0.297 to 0.710, matches "+0.3 to +0.7".
- Nqo1: 0.349, -0.156, -0.014, 0.425 (mixed, matches). Gclm: 0.039, -0.051, 0.070, -0.074 (flat). Txnrd1: 0.116, 0.103, 0.071, -0.096 (small; HPC and CTX Welch p 0.049 and 0.044, exact permutation 0.056 and 0.032; at or below 0.12 log2, so "flat" is defensible).
- Leave-one-out for Srxn1 over all units of both arms, ratio = effect without the animal / effect with all animals: HPC min 0.709 (drop M6), max 1.256; CTX min 0.718 (M6), max 1.153; PFC min 0.777 (M6), max 1.169; CB min 0.876 (F8), max 1.176. These equal the ADV-239 table. Lowest of the four regions: 0.709, so "at least 70 percent" holds, with a margin of 0.009 in HPC (a per-animal log2 difference, effect 0.417 to 0.296).
- All four regions are covered ("every region"); CB, with three mutants, is the only region where every mutant is above every control.
- Limit that the clause does not state: this is one removal at a time. Removing M6 and F8 together leaves Srxn1 at 0.358 (HPC), 0.554 (CTX), 0.553 (PFC) and 0.648 (CB, one mutant left) of the full rise (derived from the same unit values). That pair test is a separate rule in ADV-239 and is not what the clause claims.
- Hmox1 in CTX is "one-animal-driven" in the ADV-239 table (min ratio 0.441, M6), so "modestly higher in all four regions" for Hmox1 is a full-sample direction, not a robustness statement. The clause is about Srxn1 only.

**(c) Class: CORRECT.**

**(d) Carrier: none.** Suggested precision: "...keeps at least 70 percent of its rise (derived minimum 0.709, hippocampus, M6 left out) when any single animal is left out in each of the four regions; with M6 and F8 both left out it keeps 0.36 to 0.65 of its rise."

---

## Summary table

| k | class | carrier | one-line reason |
|---|---|---|---|
| 02 | WRONG | OTHER | Fold range top "9" is below the Fig 4G bars (derived PBA/vehicle 5.7, 7.0, 13.0, 19.3); "unmeasured for every allele" holds only as "not quantified" (P252A and P282A reported as function lost, qualitatively); WT gains seen are about 1.2 to 2.4 fold |
| 03 | CORRECT | none | Rate ratios 1.7 to 3.1 (derived, Fig 3b/3e) against a deficit of about 11 to 25 fold; "not the only candidate" follows; endpoints 12 and 25 depend on the package reading (pixel table gives about 11 to 21) |
| 06 | CORRECT | none | N 1,1,3,3,3,8,5; CV 4.1 to 79; slopes 0.945, 0.983, 1.382 (1 to 21 mg); 4773/3773 = 1.265 for 21 mg to 42 mg, dose ratio 2.0 |
| 07 | INCOMPLETE | WORD | "No enzyme-level support" omits Rico-Molina enantiomers 34.0 and 38.4 % and the second-hand about 40 % at 0.5 mM; 7 %, about 10 %, no fitted potency (88/88 rows), label all correct |
| 08 | INCOMPLETE | WORD | "The one cell-level signal" is true only among ChEMBL rows (4 FC rows, 0.27 to 0.70); held literature adds Guyon lactate -50 %, Le Dudal HepG2 oxalate, Yadav ECAR; enzyme clause shares the k=07 gap |
| 09 | CORRECT | none | 205, 116, 89, 74 and exactly 2 compounds at 30 fold or more on every pair (CHEMBL3763437 267, CHEMBL5597066 352; each has one pair) all recomputed from both complete tables |
| 10 | INCOMPLETE | WORD | Ratios 0.13 to 0.29 vs 0.29 to 0.30 correct; E-MTAB-14792 holds a human WWOX-KO library (exists, 403), so "the one" holds only for the accessible deposit GSE156243 |
| 11 | CORRECT | none | Only I150V has an asterisked maximal inhibition (31 vs 85 %) with no potency loss; the other four reduced-maximum variants are in the five-variant potency-loss set |
| 12 | INCOMPLETE | WORD | sIPSC amplitude -52 % is the largest among printed means (sEPSC +6 %, sIPSC frequency -18 %), but mEPSC amplitude, the neocortical evoked response (S3 not held) and CA1-to-CA3 PS (about +70 % by eye) have no comparable magnitude |
| 13 | CORRECT | none | Legend states "four independent experiments" verbatim; pSer9/actin lower in all three regions (ratios 0.48, 0.56, 0.64); one blot shown, animal number unstated, P20 vs P14 as quoted |
| 16 | CORRECT | none | Doumlele 2016: ERGs, CBC and CMP "every 3-6 months with no abnormalities"; the locator's other items all match the text |
| 17 | CORRECT | none | Table 1: rapamycin 60 in IST, 0 in ISO; Table 3 multivariate OR 0.152 (0.028 to 0.715), p = 0.019 |
| 18 | CORRECT | none | Pearl 2009 abstract: 7 of 22 (32 %) vs none of 56; zero holds only inside this study (Stevering untreated 7 of 52 are other cohorts) |
| 20 | INCOMPLETE | WORD (plus OTHER) | Dropping M6 changes Adm by -0.36 to -0.49 log2 in the three forebrain regions (all stay positive) but not in CB (0.363 to 0.372); "other three within WT range" fails for HPC F10 (+19 %) and marginally M7 |
| 21 | NOT ASSESSABLE | not applicable | A proposed design with no source claim; nothing to test |
| 22 | CORRECT | none | Srxn1 leave-one-out minimum ratio 0.709 (HPC), 0.718, 0.777, 0.876; Hmox1/Srxn1 +0.297 to +0.710; one animal at a time only (M6 plus F8 gives 0.36 to 0.65) |

Counts: CORRECT 9 (03, 06, 09, 11, 13, 16, 17, 18, 22); INCOMPLETE 5 (07, 08, 10, 12, 20); WRONG 1 (02); NOT ASSESSABLE 1 (21).

## Not reached or not done

- k=02: the package's underlying "stability census" and other repository files for the four WWOX missense beyond Q230P, P252A and P282A were not opened; I relied on the package README row (six missense with any protein-level measurement, function none). The Munc18-1 fold readings (1.0 to 2.1) were taken from the package, not re-measured; the GABRA1 "3.1" is not in the held text I have (maximum 2.68).
- k=03: Fig 3a bar tops were not re-measured at pixel level (the thumbnail cannot separate 4 from 7 %); both readings are reported.
- k=08, k=07: the 2022 CHEMBL5120856 paper itself, Sada 2015, Guyon 2022, Le Dudal 2019 and Yadav 2026 were not opened; their content is as quoted in the src's repository record.
- k=12: Supplementary Figures S2 and S3 are not held, so the evoked neocortical response magnitude is unavailable; the Fig 5D reading (about 1.3 vs 2.25 mV) is by eye with error bars of about 0.3 mV.
- k=13, k=22, k=10, k=20: the underlying count file for GSE215425 was not reopened; I used the src's tables (the Adm values match the IT12 rows to three decimals).
- No Obeid material was opened (none was pointed to). No access control refused any read.
