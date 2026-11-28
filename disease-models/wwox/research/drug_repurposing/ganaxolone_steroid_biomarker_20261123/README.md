# Does low circulating allopregnanolone sulfate identify ganaxolone responders?

context_policy: QUESTION_DRIVEN. SCI_CODEX, 2026-11-23. Targeted registered outcomes, statistical plan, trial results and supplement, and FDA subgroup review. All public sources were accessed without charge. The repository holds original analyses and selected numerical summaries only.

## Decision for WWOX

Do not use low baseline plasma allopregnanolone sulfate (Allo-S) as an eligibility criterion or a reason to prioritize ganaxolone in WWOX deficiency. In a separate genetic epilepsy in which the trial actually stratified randomization by this biomarker, the observed placebo-adjusted **responder proportion** was numerically smaller in the low group under all seven compatible quartile conventions tested. There were four participants per arm above the cutoff. The data support neither a reversed eligibility rule nor a validated interaction. A brain-specific steroid deficit remains a distinct question. Plasma sulfated allopregnanolone, free unconjugated allopregnanolone in brain and the C19 compounds examined in mouse Wwox are different analytes. [WWOX steroid flux audit](../ganaxolone_steroid_flux_20261123/README.md)

## VIOLET gives a test of enrichment

The randomized 17-week PCDH19 trial enrolled 21 girls and stopped recruitment early. Low Allo-S was defined at screening as ≤2.5 ng/mL. The endpoint counted seizures over 28 days, with change measured relative to baseline. The primary all-participant comparison was inconclusive (p=0.17). The registers give quartiles and medians for the full cohort and low subgroup, plus the total number with a reduction of at least 50%. The public US results do not give that count by subgroup. The statistical plan specified SAS 9.4 or later and stratum-specific responder summaries. [Trial report](https://pubmed.ncbi.nlm.nih.gov/36870093/) · [US trial data](https://clinicaltrials.gov/api/v2/studies/NCT03865732) · [European results](https://www.clinicaltrialsregister.eu/ctr-search/trial/2018-004496-12/results) · [Statistical plan, §7.1.3](https://cdn.clinicaltrials.gov/large-docs/32/NCT03865732/SAP_003.pdf)

| Screening plasma Allo-S | Ganaxolone responders | Placebo responders | Sample drug–placebo difference |
|---|---:|---:|---:|
| All, reported totals | 5/10 | 4/11 | +13.6 percentage points |
| ≤2.5 ng/mL, inferred | 2/6 | 2/7 | +4.8 points |
| >2.5 ng/mL, inferred by subtraction | 3/4 | 2/4 | +25.0 points |

Low-minus-high interaction on this scale is **−20.2 percentage points** in this sample. Changing a single response in one high stratum moves its arm proportion by 25 points. This descriptive difference cannot establish an interaction in the population.

### Why the inferred counts are constrained

With the usual empirical percentiles that average at exact rank boundaries (Hyndman–Fan type 2), the low ganaxolone group's second ordered change is −86.48%, so at least two responded. Its fifth value is −24.32% and its median is −35.90%. Consequently its third value must be at least −47.48% (up to rounding): it cannot be a third responder. For low placebo, the second value is −85.74%, implying at least two responders. In the full placebo arm the third value is −88.24%. At most one low-placebo outcome can reach that value. At least two high-placebo outcomes must therefore respond. The total is four, leaving exactly two low responders. Decreases are ordered from greatest reduction to greatest increase. No individual's outcome or identity was reconstructed.

Enumerating every low-versus-high rank allocation and bounding the unpublished high-stratum median reproduces these counts. Under type 2 the high-stratum ganaxolone-minus-placebo difference of medians lies between −41.8 and −9.4 points, whereas the reported low-stratum medians differ by −17.19 points. Thus **the seizure-frequency median contrast does not establish which stratum gains more**, even when the binary responder contrast is determined. These bounds describe compatibility with rounded study summaries, with no sampling uncertainty attached.

Type 6 yields the same binary result. Type 7 cannot reproduce the published summaries in either arm. A subsequent sensitivity scan across all nine standard quartile methods, with the ordinary median held fixed, finds seven simultaneously compatible methods. All seven give two low responders per arm. Discarding the quartiles allows either direction for the responder-rate interaction (−101.2 to +100.0 percentage points on a difference-of-differences scale). The inference requires the same individual endpoint and analysis population underlying all three outcome summaries. The studies do not identify a clinical decision cutoff in WWOX.

### Independent disease comparator

In CDKL5 deficiency, the 17-week Marigold trial reported Hodges–Lehmann ganaxolone–placebo shifts in major motor seizure change of −21.0 points at low Allo-S (39/37 treated/placebo), −48.0 at intermediate Allo-S (5/12) and −47.9 at high Allo-S (4/2). Corresponding intervals were [−47.3,+2.2], [−149.4,−16.8] and [−83.1,+6.2]. They are within-stratum intervals and cannot test interaction by comparing their significance. The protocol was amended to exclude screening values ≥6.0 ng/mL, limiting the high subgroup further. The FDA review reports a slightly different high-stratum treated-arm median from the manuscript supplement (−39.03% versus −34.3%); both report the same rounded between-arm shift. The stratum shifts, endpoint definition and denominator are the comparisons used here. Pooling this result with the PCDH19 responder endpoint would mix different estimands. [Marigold, supplemental Table 2](https://discovery.ucl.ac.uk/id/eprint/10153307/3/Cross_D-21-00849R2_Pestana%20Knight_MARIGOLD_MS_2022-01-26.pdf) · [FDA clinical review, pp. 51–53](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2022/215904Orig1s000MedR.pdf)

## Reproduction and follow-up

Save the US registry JSON linked above and run `python3 analyze.py registry.json` with NumPy and SciPy (tested with SciPy 1.16.3, BSD). The retrieved JSON has SHA-256 `3c1cfac0b1822161537afc84aac3e9dbc83aaa62ebdd55e0c00e747d922404c6`. Compare with results.tsv. Scores are bounded below at −100%, ordered within arm and allowed to vary within 0.006 points of reported summaries. The analysis uses no patient-level records.

To reopen a WWOX substitution mechanism, a more informative pairing is the measured local free steroid profile and a matched cell-specific GABA response, with WWOX correction and a direct ganaxolone comparison. The trial biomarker analysis cannot answer whether ganaxolone changes glial maturation, receptor composition or survival in WWOX.

Independent adversarial review returned an ACK at 12:57:37 UTC. The other laboratory session confirmed the endpoint and denominator against the statistical plan, reproduced the order-statistic reasoning for both arms, and confirmed two low responders per arm under all seven compatible methods. The plan names SAS and leaves its quartile option implicit. [SAS percentile conventions](https://support.sas.com/documentation/cdl/en/procstat/68142/HTML/default/procstat_univariate_details14.htm)

The targeted follow-up checks why plasma and regional measures cannot establish a WWOX brain deficit and verifies the distinction between Marigold primary frequency and responder endpoints. [Ganaxolone follow-up](../continuous_compounds/ganaxolone/neurosteroid_replacement_and_disposition_20261127.md)
