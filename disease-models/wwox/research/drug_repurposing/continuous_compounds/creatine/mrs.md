# What pediatric spectroscopy can establish about creatine in WWOX loss

**Decision.** Park creatine monohydrate as a mechanistic candidate for absolute metabolite and recovery measurements. Two primary intervention studies measure different endpoints in other populations. Neither demonstrates a phosphocreatine deficit, restoration after activity, or benefit in children with WWOX loss. The reviewed WWOX case does not report an absolute creatine value. The laboratory's initial transcript signal is insufficient to prioritize a pediatric trial. [First analysis](README.md)

## A water-referenced trial in healthy children

Merege-Filho et al. randomized healthy 10–12-year-olds to creatine monohydrate or placebo for seven days. Of 67 completers, 26 were selected for imaging and five missed the baseline scan. A further two to five regional acquisitions were missing. The authors estimated total creatine in mmol/L using water as reference and corrected for voxel composition. This signal combines creatine and phosphocreatine. From the rounded published group means we reconstructed the following differences in changes. [Original randomized study, Table 3 and Fig. 2](https://doi.org/10.1139/apnm-2016-0406)

| Region | Evaluable children across both arms | Creatine minus placebo change, mmol/L | Range from rounding alone |
|---|---:|---:|---:|
| Left dorsolateral prefrontal cortex | 19 | −0.40 | −0.60 to −0.20 |
| Left hippocampus | 16 | −0.10 | −0.30 to +0.10 |
| Occipital lobe | 18 | +0.10 | −0.10 to +0.30 |

The authors report group-by-time p values of 0.50, 0.80 and 0.70, respectively. The rounding ranges allow independent rounding of each mean by 0.05 mmol/L. They do not address sampling uncertainty. Applying the authors' five-person pilot coefficients of variation to the approximate baseline concentrations gives 0.39, 0.53 and 0.38 mmol/L. These are calibration scales, not treatment confidence intervals. Small group averages and missing scans preclude declaring equivalence or excluding a response after longer exposure. [Calculated quantities](total_creatine.tsv)

**Internal consistency check.** The accepted manuscript prints a placebo prefrontal post-treatment SD of 0.09 mmol/L. The Fig. 2A endpoints span approximately 4.9 to 8.0. Even a conservative span of 2.9 and the maximum ten children requires a sample SD of at least 0.68, because the two extremes alone contribute at least half the squared range to the sum of squared deviations. Two printed placebo change intervals in Table 3 also fail to contain the differences of rounded group means even allowing rounding. We did not correct those entries, reconstruct a confidence interval from them, or change the authors' reported test. These discrepancies refer to the inspected accepted manuscript. [Original study](https://pubmed.ncbi.nlm.nih.gov/28079396/)

## A phosphorus ratio can give a different answer

Kondo et al. studied girls and young women eligible at ages 13–20 with SSRI-resistant depression. After eight weeks, 28 contributed completer data across placebo and three creatine arms. Frontal phosphorus signals were normalized to total phosphate (TP) to reduce acquisition-related variation. Table 2 reports p = 0.69 for the between-group comparison of percentage change in PCr/TP. In our calculation, the highest-exposure arm changed by +9.09%, versus −0.67% with placebo. The descriptive difference is +9.76 percentage points. [Kondo et al., acquisition methods and Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC4974294/)

Re-expressing PCr relative to β-NTP using the same group means removes the apparent high-arm separation. The recalculated changes were +5.91% and +6.01%, respectively, a difference of −0.10 points. The middle arm, by contrast, increased by 8.64 points more than placebo on that reference. The highest arm's original PCr/TP change is compatible with unchanged absolute PCr if the denominator fell by 8.33%. We did not measure that denominator change. β-NTP can itself change, and a ratio of group means does not give the participant-level mean ratio. This sensitivity check establishes how strongly the apparent effect depends on the chosen reference. Both measures were at rest. [All three arms and denominator sensitivity](phosphorus.tsv)

**Pediatric feasibility.** The healthy-child trial studied a defined monohydrate product for one week and recorded no self-reported adverse effects. The longer study enrolled an older population on SSRIs and recorded gastrointestinal symptoms in every arm including placebo. Neither addresses chronic tolerability in the younger WWOX population, formulation or swallowing needs, background antiseizure polytherapy, nor the reliability of repeated scans in severely affected children. The gain from a further WWOX study would depend first on evidence of a modifiable deficit and a measurement likely to detect its correction.

## Disease-specific evidence and reopening criterion

In the report of a child with homozygous WWOX exon 6 deletion, the spectroscopy narrative describes amino-acid signals and low lactate. It provides no absolute creatine, phosphocreatine, spectral calibration or recovery measure. Low lactate cannot supply the missing estimate. This check covers one case. A separate healthy-age-group phosphorus study (Solis et al.) was identified, but its full acquisition and group-specific estimates were not verified in this increment. It remains a source lead only. [WWOX case, neuroimaging paragraph](https://pmc.ncbi.nlm.nih.gov/articles/PMC6296882/) · [Lead for the cross-tissue study](https://pubmed.ncbi.nlm.nih.gov/28572496/)

**Reopen** for WWOX-specific absolute creatine or PCr data, a validated time course of PCr recovery after matched demand, or drug exposure with a native biochemical response. In a neural preparation, distinguish substrate entry from phosphorylation with matched initial depletion, cell composition, absolute creatine, PCr and ATP. A rise in total creatine with persistently slow PCr recovery would weigh against simple substrate limitation. Independent review of the cell-composition calculation is tracked separately and can reopen that inference.

**Reproduction.** Run `python3 spectroscopy.py /path/to/PMC4974294.1.xml`. The script parses Kondo Table 2 directly, recomputes all denominator comparisons and applies the graphical SD bound and the rounding calculation to the healthy-child summary. Only derived results and reading records are distributed. [Calculations](spectroscopy.py) · [Reading records](receipts/)
