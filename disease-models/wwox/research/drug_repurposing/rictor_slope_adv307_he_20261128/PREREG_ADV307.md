# PREREG ADV-307: in the Rictor callosal deposit, does the fitted slope depend on early recruitment? (HE, 2026-11-28)

Assignment ADV-307 (ADV message of 2026-11-28; key rictor-callosal-deposit-slope-versus-recruitment-targeted-analysis).
Data: doi:10.5061/dryad.gk117, `Conduction Velocity.xlsx` (public copy zenodo.org/records/4999038, MD5
9d2bad794c4eff1a2390941593ff58c4). Frozen before any slope-versus-amplitude statistic was computed.

## Not blind (declared first)

HE opened the whole sheet during ADV-306, minutes before this assignment: all 24 value rows were printed, and HE did one
rough end-to-end slope for the first slice in passing. No per-slice fit, correlation or test was computed. The proxy, the
statistic, the threshold and the prediction are ADV's, written in the assignment; HE cannot claim a blind freeze of
anything it adds below.

## Frozen

- Unit: one slice (block of four rows in sheet1 with the same animal label and genotype). Usable: all four distances
  (0.5, 0.75, 1.0, 1.25) with N1 time and an N1 amplitude at 0.5.
- N1 time: the column "N1 time" as printed. The deposit does not define it (peak or onset, zero point); the paper says
  velocity is the inverse slope of the regression of response times. Units are not labelled; ms and mm are inferred.
- Fit: ordinary least squares of N1 time on distance, per slice: slope (ms/mm), intercept (ms), R squared, 1/slope.
- Proxy for absolute early recruitment: "N1 Amp" at distance 0.5. Stimulus intensity is not in the deposit.
- Statistic: Spearman rho of slope against that amplitude, (1) pooled, n = 6, exact two-sided permutation p over 720
  orders; (2) "within genotype": rho of slope against amplitude after subtracting each genotype's mean from both, n = 6;
  (3) per genotype, n = 3, descriptive only.
- Leave one slice out: range of the pooled rho over the six.
- Decision: (B) slope tracks recruitment if pooled |rho| >= 0.5. (A) slope independent if pooled |rho| < 0.3 AND the
  within-genotype |rho| (2) < 0.3. Otherwise INDETERMINATE. Fewer than 4 usable slices: the deposit cannot answer.
- Printed ratios: recompute column G as distance / N1 time and column I as the mean of the four G of a slice.

## Two weaknesses of the rule, found before computing

- With n = 3 a Spearman rho can only be 0.5 or 1 in size, so ADV's "below 0.3 within genotype" cannot be met on the two
  groups taken separately. Statistic (2) replaces it; (3) is reported without a verdict.
- With no association at all, n = 6 gives |rho| >= 0.5 with probability 0.297 and |rho| < 0.3 with probability 0.436.
  Neither verdict from this deposit is strong evidence; the label goes with the number and its p.

## Prediction (ADV's)

Pooled |rho| at least 0.5 (B), while the paper's own "velocity unchanged" stands. Rejecting: |rho| below 0.3 pooled and
within genotype (A), or fewer than 4 usable slices.

## Limits

n = 6 slices, 3 per genotype; not a Wwox line; one age (P32-42); no stimulus intensity; no velocity is claimed for any
Wwox preparation.
