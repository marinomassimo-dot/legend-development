# Fig. 4 of Breton 2021 (PMID 34634460): what could and could not be read (HE, 2026-11-16; non-canonical; not medical advice)

Written for: ADV, SCI. Methods and rules were committed before reading: `PREREGISTRATION_FIG4.md` (3f9d98682), `PREREGISTRATION_FIG4_MEPSC_SECOND_READ.md` (dbc93e052), `AMENDMENT_1_CALIBRATION.md` and `AMENDMENT_2_EXTRACTION.md` (committed before the runs they govern). Figure file: `gr4.jpg` from the Europe PMC REST `supplementaryFiles` zip (the PMC article page and the Europe PMC `bin` route answer with a reCAPTCHA / 'Just a moment' interstitial and were not circumvented); raster 708 × 675 px, sha256 384ee6a8f13cc04a1f60bd243abecf7d90065ebeb5d5dbc4f7bddd3aec99f1b5; no larger or vector version is in the zip.

## 1 · sIPSC (the measurement asked for): STOP, S-HT is not plotted separately
Panels G (traces and mean waveform) and H (cumulative probability of amplitude h1 and frequency h2) show TWO groups, S-CTL (black: S-WT and S-HT pooled; 14 cells, 7 animals) and S-KO (red; 9 cells, 5 animals). The legend gives KS p-values for 'sWT vs sKO' and 'sHT vs sKO' and N = 7 cells (4 animals) each for s-WT and s-HET, but no S-HT curve or mean is drawn; KS p-values depend on event counts and are not distances. **S-HT sIPSC amplitude and frequency cannot be recovered from the figure.** The remaining route is the authors' per-cell values (for the operator).

## 2 · mEPSC (panels B and C; a different measurement, labelled so): medians from curve geometry
Three groups are plotted (S-WT black, S-HT blue, S-KO red; N = 10 cells each, 4 to 5 animals; pooled events). Calibration: axis-line anchors with a label cross-check (panel B largest label deviation 3.0 px, panel C 0.8 px); scale 0.217 pA per pixel (B) and 0.348 Hz per pixel (C). **The first extraction run was discarded** (text of the inset and the legend line were inside the search band; `results/fig4_mepsc_first_run_DISCARDED.json`); the numbers below are from the amended run, committed before it was executed.

| panel | S-WT median | S-HT median | S-KO median | f = (S-HT − S-KO)/(S-WT − S-KO) | classification by the frozen rule |
|---|---|---|---|---|---|
| B amplitude (magnitude, pA) | 13.86 ± 0.47 (5 rows only: mostly hidden under the blue curve) | 13.98 ± 0.47 | 15.32 ± 0.46 | nominal **0.915**; band 0.28 to 2.55 (anchors treated as independent errors, as preregistered) | **undecided (calibration-limited)**: nominal near controls, the band spans midway and near controls |
| C frequency (Hz) | 4.91 ± 0.85 | **hidden** (3 rows only) | 4.11 ± 0.84 | not computable | S-HT curve hidden under the others: nothing is guessed |

Sensitivity (NOT preregistered, labelled as such): the three curves share the same calibration, so the anchor error is common to all three and cancels in differences. Using only the per-curve position uncertainty (fit standard error combined with ±1.5 px, about 1.5 px each), f for amplitude is 0.91 with a range of 0.46 to 1.68: still undecided between midway and near controls. 

## What it says (and not)
* **Amplitude (mEPSC):** the S-KO median is about 1.3 to 1.5 pA larger than the S-WT median (about +10%); the S-HT median sits at the S-WT median (a 0.1 pA difference, far inside the uncertainty). The rule cannot classify it (undecided), but the nominal position is near controls, i.e. at the median the heterozygote does not look graded between WT and KO. The legend's KS tests say the S-WT and S-HT distributions differ (p 2.0e-4) over their whole range, so the whole-distribution difference is not at the median.
* **Frequency (mEPSC):** S-KO median 4.1 Hz against S-WT 4.9 Hz (a difference of 0.8 Hz against an uncertainty of 0.85 Hz): not separable; S-HT is hidden.
* **Size for SCI:** an mEPSC amplitude shift of about +10% between S-WT and S-KO at the median, of the same order as the +6% sEPSC figure used in the model's excitatory term; the S-HT position is not decided by this figure.

## Limits
Raster only (708 px wide, blurred; about 4.6 px per pA in panel B and 2.9 px per Hz in panel C); pooled-event cumulative curves (cells with more events weigh more); the curves overlap, so S-WT in panel B is read from 5 rows and S-HT in panel C is hidden; 10 cells per group; the cumulative curves were read at probability 0.5 only. SCI's frozen rule was transcribed from ADV's relay; the file itself was not read.
