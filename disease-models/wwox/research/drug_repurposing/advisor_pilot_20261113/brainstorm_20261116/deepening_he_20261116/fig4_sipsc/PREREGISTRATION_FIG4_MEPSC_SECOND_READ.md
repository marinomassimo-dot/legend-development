# Fig. 4 panels B and C (mEPSC, three genotypes plotted): method and decision rule, committed BEFORE any curve is read (HE, 2026-11-16; non-canonical; not medical advice)

Written for: ADV, SCI. **This is NOT the sIPSC measurement ADV asked for.** For sIPSC (panels G and H) S-HT is not plotted separately (curves are S-CTL and S-KO), so that reading stopped under `PREREGISTRATION_FIG4.md` rule 3. Panels A to C plot S-WT (black), S-HT (blue) and S-KO (red) as mEPSC (TTX; N = 10 cells each, 4 to 5 animals): B cumulative amplitude, C cumulative frequency. SCI named mEPSC amplitude as a candidate graded factor for burst incidence; this reads its three genotype distributions.

## Method (fixed now)
1. Figure file: `gr4.jpg` from the Europe PMC REST `supplementaryFiles` zip (raster 708 × 675 px, sha256 384ee6a8f13cc04a1f60bd243abecf7d90065ebeb5d5dbc4f7bddd3aec99f1b5); no larger version is available through the routes that do not stop at an interstitial.
2. Quantity read: the **median** of each genotype's distribution, the x value at which the cumulative probability equals 0.5, in panel B (amplitude, pA; more negative = larger event) and panel C (frequency, Hz).
3. Calibration by script: x-axis tick marks found as short dark vertical segments just below the x-axis line of the panel; the labelled values are assigned by order (B: −50 to 0 in steps of 5 pA; C: 0 to 80 in steps of 10 Hz); y-axis ticks likewise (0 to 1 in steps of 0.2); linear map from pixel to value. Colour classes: black (all channels < 90), blue (blue > 140, red and green < 110), red (red > 170, green and blue < 90). For each class the median x is the mean x of its pixels in the rows within ±1 px of the p = 0.5 row, inside the plot area and outside the inset of panel B. If a class has no pixel in that band (hidden under another curve) it is reported as hidden, not guessed.
4. Uncertainty: ±1.5 pixel on the x position (line width and tick position), converted to the axis unit with the calibrated scale; reported per median.
5. Reported: the three medians with their uncertainty for amplitude and for frequency; f = (S-HT − S-KO)/(S-WT − S-KO) with its propagated uncertainty (the extremes of the pixel bands).

## Decision rule (SCI's frozen rule as relayed by ADV; the file itself is in SCI's local batch and was not read by me; this is my transcription)
f ≥ 0.75: **near controls**; 0.25 ≤ f < 0.75: **midway**; f < 0.25: **near knockout**; **not separable** if |S-WT − S-KO| is not larger than the combined pixel uncertainty. If the class changes between the nominal f and the extremes of its uncertainty band, the result is reported as undecided (calibration-limited). The rule is applied to amplitude first, then to frequency.

## What the result is allowed to say
Only the position of the S-HT median between S-WT and S-KO in a mEPSC cumulative plot of 10 cells per genotype. It says nothing about sIPSC and nothing about incidence beyond SCI's use of it as a graded factor candidate; the legend's KS p-values (S-WT vs S-HT 2.0e-4 for amplitude; 1.8e-3 for frequency) are not used.
