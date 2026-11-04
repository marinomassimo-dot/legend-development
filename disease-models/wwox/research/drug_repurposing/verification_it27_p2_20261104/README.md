# IT27 P2: independent verification of the MTBLS12344 part (section 4) of wwox_data_it24_p4_20261104 (2026-11-04)

Verifier: not the IT24 producer. Zero spend, no registration, no contact. All downloads public (MetaboLights FTP, Europe PMC); nothing sent anywhere.
Subject: MTBLS12344, Drosophila head HILIC metabolomics, pan-neuronal Wwox RNAi x Abeta42 (Lucas-Clarke et al., Brain Commun 2026, PMID 42909904, PMC13684411).

## 0. Verdict (short)

**VERIFIED with a narrower perimeter and three corrections.** The producer's numbers reproduce within noise; its group assumption is now resolved (it was right); its reading
stands only as a *context-dependent metabolite-pool difference in an Abeta42 fly*, not as a WWOX-loss effect and not as flux or enzyme activity.

| Item | Producer | This verification | Status |
|---|---|---|---|
| Letter code -> group (C ctrl/LacZ, D Wwox RNAi/LacZ, G ctrl/Abeta42, H Wwox RNAi/Abeta42) | assumed, UNVERIFIED | **Resolved**: ISA sample sheet `s_MTBLS12344.txt` gives exactly this map; the assay sheet's `Sample Name` column is the corrupted one (see 1.2); independent data check (1.4) | confirmed |
| 2-HG, Wwox RNAi inside Abeta42 | +0.92 log2 (FDR 0.013) | +0.94 log2 (raw), +0.94 (TIC), 95% CI +0.44..+1.44, p 0.0010-0.0014, Holm over my 6-test primary family 0.006 | reproduced |
| 2-HG, Wwox RNAi in LacZ | +0.11, no call | +0.13, CI -0.37..+0.63, p 0.59 | reproduced |
| Interaction (not tested by producer) | "no interaction test" | **nominal only**: log2 +0.81 (ratio of ratios 1.76), p 0.027 (TIC), permutation 0.026; Holm-6 0.13; leave-one-out p 0.005-0.054; authors' own FDR 0.53 | added |
| Lactate QC gate | FAIL 0.657 (not analysed) | 0.741 under my pre-declared window; **8 of 20 window variants pass, range 0.21-0.80**; blank = 50% of a median sample | producer's fail is window-dependent; lactate stays unusable, but "pooled-QC order disagrees with the deposit" is not the cause |
| Itaconate | FAIL 0.64 + fragment doubt | FAIL 0.27; the 129.0193 peak at 750 s is the 2-HG water-loss fragment (ratio 0.098, CV 8%, constant across all four groups, log-r 0.97 with 2-HG); no resolved peak at the deposit RT 771 s | confirmed, sharpened |
| Replication unit | "pool of 10 heads, 5 per cell" | confirmed (study protocol + paper); day-14 mated females | confirmed |
| 2-HG identity | "TCA-adjacent metabolite pool" | MS-only assay **cannot separate L- from D-2-HG** nor 3-hydroxyglutarate/citramalate; one dominant peak at 750-751 s | added limit |
| Novelty | implicit | the authors already published the same effects (Supp Table 4: 2-HG KD main effect, Abeta42 main effect, lactate interaction); this is a re-derivation, not a new finding | added |

## 1. Group assignment and unit of replication (built from metadata first)

### 1.1 What the deposit says
* Investigation file `i_Investigation.txt`: "Samples were n=5 replicates of pooled heads (10 heads per rep) of day 14 female Drosophila melanogaster". Two experiments in one deposit: a **knockdown** experiment (RNAi control + LacZ; Wwox knockdown + LacZ; RNAi control + AB42; Wwox knockdown + AB42) and an **overexpression** experiment (control gRNA / Wwox gRNA x LacZ / AB42). Extraction chloroform:methanol:water 1:3:1; ZIC-pHILIC; Q Exactive polarity switching; matrix blanks and pooled samples as controls.
* Sample sheet `s_MTBLS12344.txt` (factor values): `C1-C5_KDExp` = RNAi Control / LacZ; `D1-D5_KDExp` = Wwox RNAi / LacZ; `G1-G5_KDExp` = RNAi Control / AB42; `H1-H5_KDExp` = Wwox RNAi / AB42; `I`-`L` (`_OEExp`) = overexpression experiment (Control gRNA/Wwox gRNA x LacZ/AB42). Letters E and F do not exist in the deposit. All factor values Age = 14 day. 40 experimental samples (20 KD + 20 OE), 12 pooled QC, 6 matrix blanks, 2 fragmentation runs.
* Genotypes (paper Supplementary Table 1B, row "Metabolomics", Fig 5A-C): `elav-GAL4/w-;+;RNAi Control/LacZ`, `elav-GAL4/w-;+;Wwox TRiP/LacZ`, `elav-GAL4/w-;+;RNAi Control/Abeta42`, `elav-GAL4/w-;+;Wwox TRiP/Abeta42`; RNAi control = BDSC 8622 (attP2), Wwox TRiP = BDSC 51747, LacZ = BDSC 8530, Abeta42 (Arctic E693G) = BDSC 33774; N=5. The ISA files do not carry the genotypes; the paper's supplement does. Knockdown depth: Supplementary Fig 1 (qPCR, newly eclosed females, N=3 x 15 heads); **not measured at the day-14 metabolomics time point**, value not extracted here (image only).
* Unit of replication: **one pool of 10 heads = one sample file**; 5 pools per cell; the 4 cells share one genetic background cross design (elav-GAL4 x TRiP line x UAS line); no animal-level or cross-level replicate is recorded.

### 1.2 The shifted column: which link is right?
In the assay sheets (`a_..._profiling-1.txt` = negative-mode derived files; `a_..._profiling.txt` = positive-mode) every row carries two competing sample links:
* link A, `MS Assay Name` (e.g. `C1_KDExp`): matches the raw/derived file letter code in 40 of 40 sample rows (`C1_KDExp` <-> `C1.raw` <-> `Negative/C1.mzXML`) and is the key used by the MAF columns;
* link B, `Sample Name` column of the same row: an alphabetically sorted list, offset by about 20 rows against the rows (row of `C1.raw` says `H5_KDExp`; row of `pooled_2_04.raw` says `C1_KDExp`). It equals the MS Assay Name in **0** rows and assigns pooled and blank files to sample names. It cannot be a true link.

### 1.3 Data adjudication (`v_mapping.py`, `results/v_mapping_adjudication.json`)
Each link was used to build the four cells and the two-way effects (TIC-normalised log2). The published Supplementary Table 4 (authors' PiMP ANOVA) was used only as an external check, not to tune anything.
| metabolite (effect, log2) | link A (MS Assay Name) | link B (Sample Name col.) | published (Supp Table 4) |
|---|---|---|---|
| L-lysine (neg.), Wwox RNAi main | -1.31, p 8e-7 | +0.83, p 0.64 | -1.25 |
| orotate, Wwox RNAi main | -0.89, p 3e-4 | invalid (cells contain zero-area blank files) | down (F 18) |
| D-glucuronate, Wwox RNAi main | +0.71, p 9e-4 | +0.51, p 0.64 | up |
| 2-HG, Abeta42 main | +1.14, p 4e-6 | -3.42 (wrong sign, blank files in cells) | +1.33 |
| lactate, interaction | +1.75 | +0.39 | +1.73 (KD in Abeta +1.30, in LacZ -0.43) |
Link A reproduces every published direction and size to within ~0.2 log2; link B fails and puts blank/pool files into cells. **Resolution: link A, i.e. C/D/G/H as the producer assumed.** Residual, stated plainly: the ISA map itself is the authors' deposit; the only independent confirmation is that the published effects are reproduced; the raw filenames carry no genotype.

## 2. Peak integration (own windows; `v_extract.py`, `v_integrate.py`)
58 negative-mode mzXML files (40 sample + 6 blank + 12 pooled; sha256 in `results/v_mzxml_neg_sha256.txt`; all 34 files the producer listed have the identical digest). Targets [M-H]- from formulas: lactate 89.0244, 2-HG 147.0299, citrate 191.0197, itaconate 129.0193 (+ lysine, orotate, glucuronate, 6 amino acids for normalisation and mapping checks). Rules fixed before looking at any sample area: +-5 ppm; anchor RT = deposit MAF RT, search +-30 s; window from the mean pooled-QC EIC (apex of [1,2,1]-smoothed trace, edges at baseline + 5% of height or at a local minimum, capped 40 s); per-file window = same half-widths around the file's own apex (+-8 s re-centring; blanks not re-centred); linear baseline; trapezoid area (`results/v_windows.json`, `v_areas_long.tsv`).
Windows: 2-HG 723-777 s (apex 750), lactate 543-585 (563), citrate 830-863 (841), "itaconate" 726-764 (750, see 2.3).

### 2.1 QC gate (rank correlation with the 12 deposited pooled values >= 0.7, never altered)
Pool-name mapping from the assay sheet (`pooled_7..12` = Pool1_1..6; `pooled_2_04` = Pool2_6, `pooled_2_05..09` = Pool2_1..5). The pooled files form two batches (deposited lysine Pool2/Pool1 = 1.8; own 1.89), so the 12-point rank correlation largely tests batch.
| feature | rho (pre-declared rule) | within Pool1 (6) / Pool2 (6) | window variants passing | range over 20 variants | producer |
|---|---|---|---|---|---|
| 2-HG | 0.825 PASS | 0.60 / 0.60 | 20/20 | 0.73-0.98 | 0.979 |
| citrate | 0.930 PASS | 0.94 / 0.89 | 20/20 | 0.79-0.98 | 0.965 |
| L-lactate | **0.741 PASS (marginal)** | 0.31 / 0.94 | **8/20** | 0.21-0.80 | 0.657 FAIL |
| itaconate (750 s fragment window) | 0.273 FAIL | -0.43 / -0.20 | 4/20 | -0.27-0.83 | 0.643 FAIL |
The 20 variants = {5, 10 ppm} x {half-width 8, 12, 15, 20, 30 s} x {re-centred, fixed} (`v_diagnostics.json: gate_window_sensitivity`); all variants are reported, none is chosen. A fixed +-15 s window gives 2-HG 0.958, citrate 0.951, lactate 0.713 (producer-like window, but I add a baseline and use trapezoid area). **Lactate: no robust verdict either way.** Under the producer's window it fails, under mine it passes by 0.04; the gate is a weak instrument at CV 3-18% in 12 near-identical pools. I do not rescue lactate (threshold unchanged, no lactate analysis is carried into the verdict); the failed producer result is kept.
Because the producer's tight windows and mine differ, the producer's rho 0.98 for 2-HG is a window-specific high; the pass itself is robust.
Mapping control (diagnostic): the sequential alternative (`pooled_2_04` = Pool2_1) lowers 2-HG to 0.66 and citrate to 0.52, i.e. the assay-sheet mapping is the better one for the features that otherwise agree.

### 2.2 Blanks, pooled-QC behaviour
* 2-HG: blank mean 2.9% of a median sample, rising with blank order (0.64 -> 1.52 x 10^6; carry-over), smallest sample 12x the largest blank. Citrate: blank 0.4% (three late blanks 0.5 x 10^6), smallest sample 78x. Itaconate-window: 4%.
* **Lactate: blank mean = 50.5% of a median sample (deposit's own blank/pool 43%)**, rising 1.65 -> 5.15 x 10^6 along blank order; smallest sample (0.61x) lies below the largest blank. This is a background problem independent of the gate.
* Pooled-QC CV (same-batch, 6 each): 2-HG 3.4%/3.6%, citrate 5.3%/8.2%, lactate 5.7%/17.6%, itaconate window 8.2%/5.6%.
* TIC by group relative to median: 0.99-1.00 (flat). Pooled TIC batch 1 = 1.01, batch 2 = 0.91 of the sample median. Run order of the sample files is not recoverable from the mzXML (no acquisition timestamps), so drift and QC-interleaved normalisation could not be tested.

### 2.3 Identification: itaconate, 2-HG isomers, L/D
* **m/z 129.0193 at the 2-HG apex is a 2-HG fragment.** The EIC of 129.0193 has its largest peak at 750-751 s (identical RT as 2-HG), and area(129 at 750)/area(2-HG) = 0.113 / 0.100 / 0.098 / 0.091 in C / D / G / H (pooled QC 0.098, CV 7.6%; log-Pearson 0.966 over the 20 samples). A proportional constant ratio across groups that differ about 3-fold in 2-HG is what in-source H2O loss (C5H8O5 -> C5H5O4-) does. At the deposit's itaconate RT (771 s) the trace is a plateau/tail of that peak, no resolved apex: area(765-777 s) is 0.3-0.9% of the 2-HG area (pooled mean 2.4 x 10^5 vs blank 1.4 x 10^4). Citrate also leaks into 129 (5% of its height at 841 s). So the published "itaconate up with Wwox KD" is not an independent signal in this data; a true, small itaconate at 771 s cannot be excluded or quantified.
* **L- vs D-2-HG cannot be distinguished**: achiral ZIC-pHILIC, no chiral derivatisation, no chiral column, MS1 only. Same for 3-hydroxyglutarate, citramalate, 2-methylmalate (all m/z 147.0299; the authors' annotation lists them). One dominant peak at 750-751 s and a ~10% minor peak at ~712 s; I cannot say which isomer the authors' standard confirms. Same for L- vs D-lactate and citrate vs isocitrate (a minor 191.0197 peak at ~814 s, 9% of the 841 s peak; the deposit lists citrate at 824.3 s, 17 s off the dominant peak, unexplained).
* Citrate in-source CO2 loss would give 147.0299 at 841 s: observed 0.5% of citrate height, so it does not contaminate the 2-HG window (723-777 s).

## 3. Statistics (`v_stats.py`, `v_extra.py`, `vstats.py`; no scipy: own incomplete-beta t and F tails, checked against known values)
Units = 20 pools (5 per cell). log2 area. Normalisations: raw; TIC (area / file MS1 TIC x median TIC); reference panel (median ratio of leucine, methionine, aspartate, glutamate, phenylalanine, tryptophan; panel fixed before looking). Two-way model with pooled MSE, df 16 (effects as contrasts); Welch t as a cross-check. Pooled-QC normalisation is not possible (no interleaved QC, no run order).
**The reference panel is confounded with the cell it should adjust**: mean panel factor H 0.74 vs C 1.06, D 1.05, G 1.08, so panel normalisation inflates the Wwox RNAi x Abeta42 contrast (2-HG interaction 1.38, p 0.0008). It is reported, not used. **TIC is primary** (flat across groups); raw agrees.

### 3.1 2-HG (primary question), TIC-normalised, log2 (95% CI), p
| contrast | effect | CI | p | raw-area effect / p | panel (not used) |
|---|---|---|---|---|---|
| Wwox RNAi in LacZ (D vs C) | +0.13 | -0.37..+0.63 | 0.59 | +0.12 / 0.64 | +0.14 |
| Wwox RNAi in Abeta42 (H vs G) | **+0.94** (1.92x) | +0.44..+1.44 | 0.0010 | +0.94 / 0.0014 | +1.52 |
| Wwox RNAi main effect | +0.54 | +0.18..+0.89 | 0.0054 | +0.53 / 0.0075 | +0.83 |
| Abeta42 main effect | +1.14 | +0.78..+1.49 | 4e-6 | +1.14 / 6e-6 | +1.38 |
| Abeta42 in control RNAi (G vs C) | +0.73 (1.66x) | | 0.0019 (Welch) | | |
| **interaction (genotype x background)** | **+0.81** (ratio of ratios 1.76) | +0.11..+1.52 | **0.027** | +0.82 / 0.030 | +1.38 / 0.0008 |
Cell geometric means (TIC, area units): C 2.69e7, D 2.94e7, G 4.46e7, H 8.56e7. Interaction on the additive (linear-area) scale p 0.009; residual-permutation p 0.026 (20000, seed 1). Leave-one-out (TIC): estimate 0.64-0.99, p 0.005-0.054, 18 of 20 fits p<0.05; the influential pool is H2 (area 132 vs 57-93 for the other H pools). Authors' own PiMP result (Supp Table 4): interaction F 7.19, raw p 0.016, adjusted 0.53 (not significant); KD in Abeta +1.10, in LacZ +0.17; Abeta42 main +1.33 (adj p 0.0006); KD main +0.82 (adj p 0.026).
**Does the data support an interaction?** Nominally yes (p 0.03, three tests agree), weakly: it does not survive multiplicity (Holm over the six primary tests 0.13; BH over all 120 tests 0.050) and is sensitive to one pool. **What is firm** is the within-Abeta42 difference (Holm-6 0.006) and the absence of a detectable effect in the LacZ background (CI includes zero but also +0.63, i.e. a doubling-scale effect cannot be excluded at n 5). The honest statement: "Wwox RNAi raises 2-HG in the Abeta42 background (1.9x), a difference from the LacZ background that is nominally but not robustly significant".

### 3.2 Citrate and the diagnostic features (TIC)
* Citrate: Wwox RNAi in LacZ -0.40 (CI -0.76..-0.03, p 0.035, Holm-6 0.14); in Abeta42 -0.21 (p 0.25); interaction +0.19 (p 0.45); main KD -0.30 (p 0.025). Panel normalisation: KD main -0.00 (p 0.98). No call (producer: no call; agree).
* Lactate (gate unstable, blank-dominated; diagnostic only, NOT a finding): KD in LacZ -0.41 (p 0.16), in Abeta42 +1.34 (p 1.6e-4), interaction +1.75 (p 3.6e-4), published +1.30 / -0.43 / +1.73. It reproduces the authors' lactate interaction even though the gate is marginal; it stays outside the verdict because of the blank (50%) and gate fragility.
* Itaconate window (= 2-HG fragment): mirrors 2-HG (KD in Abeta42 +0.83, interaction +0.90). Not independent evidence.

### 3.3 Number of contrasts examined (all counted)
* Primary pre-declared family: 2 features (2-HG, citrate) x 3 contrasts (KD in LacZ, KD in Abeta42, interaction) = **6** (Holm).
* In `v_stats.tsv`: 5 features (2-HG, citrate, lactate, itaconate-window, lysine) x 3 normalisations x 8 tests (3 Welch + 5 two-way effects) = **120** tests (BH and Holm over all 120 reported; not independent, conservative in the dense direction).
* Mapping adjudication: 5 metabolites x 3 effects x 2 links = 30 more effects; 20 leave-one-out fits x 2 normalisations (2-HG interaction); 20 window variants x 4 features (gate only); one permutation test. None of these gates a claim except the 6-test primary family.
* Producer: 2 features x 2 contrasts (+ lactate/itaconate dropped at the gate), BH over 2 features, no interaction.

## 4. Verdict and perimeter
**Verified (with downgrade of scope).** The producer's quantitative result reproduces independently; its group map is confirmed; its caveats (pool not flux, RNAi depth, single lab, mixed head) are right and are extended.
Corrected perimeter, what the datum is:
* In day-14 female heads, pan-neuronal Wwox TRiP RNAi (partial knockdown; depth at day 14 unknown) raises the **abundance** of an m/z 147.0299 / 750 s metabolite pool (annotated 2-HG, enantiomer unresolved, isobars unresolved) ~1.9x **only when Abeta42 (Arctic) is co-expressed**; no detectable change without Abeta42 (CI -0.37..+0.63 log2). Abeta42 alone already raises it 1.66x.
* It is a head-level metabolite pool: **not flux, not LDH/IDH/PDH activity, not a pyruvate or lactate readout** (pyruvate is not among the 14 deposited features; lactate unusable here), and not cell-type resolved.
* Relevance to WWOX loss versus the Abeta42 context: the Wwox-dependent part is a conditional modifier inside an Abeta42 stress state, not a WWOX-null signature (no effect in the LacZ background). It is a fly neuronal RNAi in an amyloid model; it does not model WWOX-related epileptic encephalopathy, a complete loss, or the human cell types. Direct relevance to the reference genotype is therefore low; it is relevant to the question "does Wwox reduction change a lactate/2-HG/TCA-adjacent pool when neurons are under proteotoxic (ISR/UPR) stress" (the authors link it to Atf4 and Ldh).
* Citrate: no call. Itaconate: not established (fragment). Lactate and pyruvate: not resolvable from this deposit (blank 50%, gate unstable, no per-sample table).
May it guide a pharmacological selection? **No.** It does not give a direction or a target of treatment (abundance only, enantiomer unknown, one cell of four with nominal interaction, single lab). **It may narrow a question**: "is the 2-HG/lactate rise a stress-state readout (Abeta42/Atf4/Ldh arm) rather than a primary WWOX-loss readout". **Discriminating experiments it points to** (none run here): (i) chiral LC-MS (D- vs L-2-HG, e.g. derivatisation or chiral column) in the same cells: L-2-HG would fit an Ldh/MDH promiscuity or acid stress arm, D-2-HG an ADHFE1/IDH arm; (ii) targeted lactate and pyruvate with a clean blank and heavy-isotope internal standards; (iii) the existing overexpression arm (deposit `I`-`L`) and an Ldh knockdown arm are available in the authors' work; (iv) a Wwox-null or ISR-inhibited (e.g. PERK pathway) cell state in a WWOX-relevant model, measuring 2-HG/lactate/PDH activity directly.

## 5. Blindness of steps
* **Blind to the producer's numbers** (but not to its qualitative claims: I had read, in a first grep of the README, that letters C/D/G/H were assumed, that lactate and itaconate were reported as failing the gate and that 2 of 4 features failed; I had seen no producer area, rho, window or p value): metadata resolution (section 1.1-1.2), the mapping adjudication, mzXML integration and my gate values (2.1), diagnostics (2.2-2.3), all statistics (3.1-3.3), and the interaction analysis were produced and written to files **before** I read the producer's numeric results (`mtbls_*` files, README numbers). The window rule (anchor = deposit MAF RT, apex from pooled QC) is a method choice that resembles the producer's by design (the deposit gives the RTs).
* **Not blind**: after producing my own results I compared with the producer (section 0, 2.1 last column, 3.3). The published Supplementary Table 4 and the paper text were read **before** integration (for the genotype table and design); they were used only for the genotype map and as an external check of the group map, never to select windows. I looked at the published 2-HG/itaconate/citrate RT values (MAF + Supp Table 4) before integrating; the 2-HG, lactate and itaconate RTs are public deposit metadata.
* One concrete difference of approach, not an error correction: the producer fixed +-15 s windows around the pooled apex without baseline; mine re-centres per file with a linear baseline. No correction after seeing results was made to my code; the integration rule and the 0.7 gate were not changed. The only edit after first run was widening the diagnostic set (15 s fixed window, all four features) in the sensitivity table, reported in full.

## 6. Limits
Positive-mode files not used (not needed). Fragmentation (MS2) runs `FRAG_NEG` not inspected. Wwox knockdown efficiency at day 14 not in any file; no sample-run order. Isobar identity depends on the authors' standard mix (not in the deposit). n=5 pools, one lab, one fly cross design. The mapping check relies on the authors' published ANOVA as external evidence; it validates the group map (four different features, direction and size) but cannot replace sample-level metadata from the authors. I did not read the full text for the project's receipt ledger: nothing here is recorded as a LEGEND full-text read; no receipts were generated.

## 7. Files and checksums
Code (this folder): `v_extract.py` (EIC), `v_integrate.py` (windows, areas, gate), `v_stats.py` (statistics), `v_diag.py` (mapping check vs published, fragment test, blanks, TIC/panel, LOO, gate sensitivity, CV), `v_mapping.py` (link A vs B), `v_extra.py` (interaction views, permutation), `vstats.py` (t/F, Welch, Spearman, BH, Holm, two-way), `xlsx_dump.py` (stdlib xlsx reader).
Run: `systemd-run --user --scope -p MemoryMax=4G -p MemorySwapMax=0 python3 -I v_extract.py <neg_dir> <eic_dir>`; then `v_integrate.py <eic_dir> <isa_dir> results`; `v_stats.py results`; `v_diag.py results <eic_dir> Supplementary_tables.xlsx <isa_dir>`; `v_mapping.py results <isa_dir>`; `v_extra.py results`.
Results: `results/v_areas_long.tsv`, `v_windows.json`, `v_qc_gate.json`, `v_stats.tsv`, `v_stats_full.json`, `v_diagnostics.json`, `v_mapping_adjudication.json`, `v_extra.json`, `v_panel_factors.json`.
Checksums: negative mzXML (58 files) `results/v_mzxml_neg_sha256.txt`; ISA/MAF/announcement `results/v_isa_sha256.txt`; paper XML, supplement zip, Supplementary_tables.xlsx, Supplementary_material.docx `results/v_paper_files_sha256.txt`. ISA digests: `i_Investigation.txt` 46c967e0..., `s_MTBLS12344.txt` 69387159..., `m_..._v2_maf.tsv` 8bd1add7..., both assay sheets in `v_isa_sha256.txt`. Source: `https://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public/MTBLS12344/` (the `ws/studies/.../download/public` route returned "no study" for the ISA files on 2026-11-04, the FTP route worked); paper via Europe PMC PMC13684411.
Data copies live only in the scratchpad (not in the repository).
