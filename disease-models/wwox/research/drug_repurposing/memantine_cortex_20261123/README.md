# Memantine at 0.7 µM in primary cerebrocortical cultures

**Decision, 23 November 2026.** A direct low-exposure memantine experiment offers little evidence for either tonic relief of an NMDA-sensitive transcriptional shutdown or suppression of that transcriptional program under ordinary culture conditions. The 19-pair estimate was slightly positive, but the nine vehicle samples showed wider variation and only 12 pairs moved in the same direction. Keep the mechanistic question restricted to the interaction with excessive glutamatergic activity. The experiment included neither a Wwox mutation nor an imposed excitotoxic challenge. [Hadwen et al.](https://doi.org/10.1093/hmg/ddy221) · [Memantine sample](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2983284)

## Direct exposure test

In a separate hippocampal study, the shutdown signature identified activity-induced genes that decreased more when NMDA was added during silencing, compared with matched genes exposed to the same silencing. The previously frozen 20 pairs validated in independent preparations within that study. Here we applied those pairs to an external cortical culture screen. The authors' public application displays the option “Memantine HCl (0.7 uM)” under Drug. Cultures received drug for eight hours at DIV21. The exposure is about twice the mean CSF concentration measured in one adult patient series, with different matrices and no pediatric WWOX exposure measurement. The nominal concentration is fourteen times lower than the 10 µM arm of the earlier excitotoxicity study. Differences in challenge, cells and timing preclude joining these exposures into one concentration-response curve. [Frozen pairs and earlier analysis](../memantine_20261123/README.md) · [Original challenge study](https://doi.org/10.1038/s42003-025-09074-9) · [Public drug database](http://bigbear.med.uottawa.ca:1000/apps/mouseCorticalRNA-app/) · [CSF study](https://doi.org/10.3389/fphar.2019.00943)

| Frozen comparison | Outcome |
|---|---|
| Coverage | 20/20 pairs mapped. Nineteen met the abundance threshold. The remaining comparator, C2cd4b, had median vehicle CPM of 0.49. |
| Memantine minus median vehicle, 19-pair score | +0.149 log2 units. Nine vehicle pseudo-treatments ranged from −0.405 to +0.642 when compared with the remaining eight. |
| Directional consistency | 12/19 positive pairs, below the required 13. Removing one pair gave +0.121 to +0.190. Against the vehicle in the same identifier block, the change was +0.183. |
| Normalization and coverage sensitivity | Median-ratio normalized score +0.149 with the same 12/19 positive pairs. All 20 mapped pairs without the abundance floor gave +0.141. |
| Movement of the arms | Mean hit expression increased by +0.165 and comparator expression by +0.034 relative to their respective vehicle medians under CPM normalization. Each arm uses its own median and their difference need not equal the paired score. |
| Independent extraction control | For the previously validated levothyroxine–Pmp22 interaction, the drug sample was +1.263 above median vehicle on the log scale and exceeded every vehicle. |
| Three previously named markers | Inhba +0.443, Bdnf +0.275, Homer1 +0.081. Each remained inside its observed vehicle range. Whole-gene Bdnf includes transcripts other than exon IV. |

The memantine score exceeded 157 of the 217 other drug samples, an empirical rank within a heterogeneous screen. Its stable positive sign across analysis variants is compatible with a weak baseline effect. The single memantine library precludes estimating variability among independently treated cultures. The nine vehicles and the sensitivity calculations do not supply this missing replication. In particular, this result cannot establish equivalence between memantine and vehicle or absence of NMDA engagement.

## What would change the research priority

The untreated Wwox mouse brain analyses also failed to show a consistent disease-specific shutdown across regions. The remaining hypothesis predicts a **drug × activation × genotype interaction**. At a verified low free exposure, a WWOX-deficient preparation would preserve activity-induced trophic transcription and neuronal survival specifically after a pathological activation episode, beyond an isogenic control and a comparator matched for overall suppression of firing. A change already present before challenge or equal suppression of normal activity-induced transcription would weaken that interpretation. The existing screen provides only the unchallenged, genotype-unselected drug arm of that comparison. [Original disease-side and challenged-culture results](../memantine_20261123/README.md)

## Reproduction

The [decision rule](prediction.md) was frozen in commit 946167ee1 before computing the panel outcome. Download the [GEO counts](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/suppl/GSE110256_combined.count.txt.gz) and [sample matrix](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/matrix/GSE110256_series_matrix.txt.gz). From this directory use Python 3 and NumPy as below. The unversioned Ensembl IDs had unique matches. All samples were aligned by library ID. The median-ratio sensitivity estimated size factors from genes positive throughout the screen and scaled effective library sizes to the median deposited count total. An independent standard-library calculation reproduced the main 19-pair estimate. Only original code and calculated results are distributed. Selected source results, methods and public database entries were consulted.

```bash
python3 analyze.py GSE110256_combined.count.txt.gz GSE110256_series_matrix.txt.gz ../memantine_20261123/results/pairs.tsv results
```

[Summary](results/summary.tsv) · [Coverage](results/coverage.tsv) · [Gene-pair contributions](results/pairs.tsv) · [Library-level scores](results/libraries.tsv) · [Ancillary markers](results/markers.tsv) · [Input hashes](results/sources.tsv)
