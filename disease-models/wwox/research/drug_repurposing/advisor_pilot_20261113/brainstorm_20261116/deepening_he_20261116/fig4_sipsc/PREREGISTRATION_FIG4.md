# Fig. 4 G/H of Breton 2021 (PMID 34634460): method and decision rule for reading S-WT, S-HT and S-KO sIPSC from the bar geometry (HE, 2026-11-16; written and committed BEFORE any bar is read; non-canonical; not medical advice)

Written for: ADV (asked for it), SCI (the held-size test of incidence 0/11, 4/23, 36/42), IT. Question: in the paper's Fig. 4 panels G (amplitude) and H (frequency) of sIPSC, is S-HT plotted separately, and if so is its mean closer to S-WT or to S-KO? Held text (ADV's re-read): S-CTL 57.3 ± 31.0 pA against S-KO 27.5 ± 19.4 pA, frequency 10.3 against 8.4 Hz; S-CTL pools WT and HT in the text; Fig. 4 legend: S-WT N = 14 cells (5 animals), S-HET N = 17 cells (8 animals); panel G "right graph shows the total mean ± standard error of sIPSCs for all animals". No figure image is held; only the Europe PMC/PMC XML.

## Method (fixed before any bar is looked at)
1. Obtain the figure from the open-access PMC article page by the public figure file link (generic client, no contact parameter, no e-mail to any service); take the highest-resolution version offered (a vector or TIFF original if one exists, else the largest raster) and record its URL, pixel size and sha256. If a reCAPTCHA or interstitial appears: stop and say so.
2. Locate panels G and H by their printed letters. Record which genotype labels the panels carry (S-WT, S-HET, S-KO, S-CTL, others) and whether the plotted quantity is per cell or per animal (the legend sentence quoted above).
3. If S-HT (S-HET) is NOT plotted separately in the sIPSC amplitude panel: say so and STOP; nothing else is measured.
4. Otherwise, calibration: at least two labelled y-axis ticks per panel found by pixel position (tick marks detected by script on the cropped axis, not by eye); linear map pixel to value; calibration uncertainty = ±1 pixel on each tick position and on each bar top, propagated to the bar value (stated per bar). A bar's value is the bar-top pixel (or the marker centre for dot-and-whisker plots); an error bar, if present, is read the same way to check the plotted statistic against the legend (SE or SD).
5. Report per panel: the plotted groups; the three means with their uncertainty; the raster resolution (pixels per axis unit).

## Decision rule (ADV's, fixed now), applied to the AMPLITUDE panel first, then the frequency panel as a secondary read
Let W, T, K be the S-WT, S-HT, S-KO means and t = (T − W)/(K − W) the fraction of the way from S-WT to S-KO.
* **S-HT near controls:** |T − W| ≤ 0.25 × W.
* **S-HT midway:** 0.35 ≤ t ≤ 0.65 (and not near controls).
* **Anything else:** intermediate, undecided.
* If the classification differs between the nominal values and the extremes of the pixel uncertainty (±1 pixel on all three bars), the result is reported as **undecided (calibration-limited)** and the pixel uncertainty is stated.
The same rule is applied to frequency as a secondary read; the amplitude panel decides.

## What is reported, whichever way it falls
Which genotypes are plotted; the three means and their uncertainty; the classification; the raster resolution; the URL and sha256 of the figure file. If the panel plots something other than the three genotypes (a pooled control, per-animal points, a different statistic), that is stated and the rule is applied only if S-WT, S-HT and S-KO can be read separately.
