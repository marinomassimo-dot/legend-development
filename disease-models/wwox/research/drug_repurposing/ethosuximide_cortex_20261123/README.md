# Ethosuximide at 700 µM in primary cerebrocortical cultures

**Decision, 23 November 2026.** Lower the priority of acute induction of a four-gene cell-cycle panel as a general neural mechanism of ethosuximide in WWOX deficiency. At 700 µM for eight hours in ordinary mouse cerebrocortical cultures, one of four genes increased relative to vehicle, and the panel mean decreased. This direct drug experiment covers an exposure close to the 710 µM N2A condition that had also failed to show significant induction. It leaves a distinct progenitor-specific fate mechanism open. The primary mouse experiment had one drug library and measured mixed cultures without a Wwox manipulation. [Hadwen et al.](https://doi.org/10.1093/hmg/ddy221) · [Drug sample GSM2983478](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2983478) · [Original N2A study, Fig. 4a](https://doi.org/10.1186/s13024-015-0046-3)

## What was predicted and observed

The [prospective prediction](prediction.md) imported the four induced genes and five same-assay comparators from the [WWOX dossier](../ethosuximide_20261123/README.md). Dose was still unconfirmed when the prediction was fixed. We subsequently retrieved the drug concentration from the authors' public application. Select Drug, search Ethosuximide, and select the option labelled “Ethosuximide (700 uM)”. This nominal concentration is 0.099 mg/mL using molecular weight 141.17. The positive N2A concentrations were 0.56 and 1 mg/mL. [Authors' searchable database](http://bigbear.med.uottawa.ca:1000/apps/mouseCorticalRNA-app/) · [Methods](https://academic.oup.com/hmg/article/27/18/3206/5036793)

| Predeclared test | log2(CPM + 1) | Median-ratio normalization |
|---|---:|---:|
| Mean difference across four genes, drug minus median of nine vehicles | −0.249 | −0.220 |
| Genes increasing, required at least three | 1/4 | 1/4 |
| Primary minus five comparator genes | +0.012 | +0.035 |
| Corresponding range across nine vehicle pseudo-treatments | −0.108 to +0.172 | −0.095 to +0.178 |

All nine genes met the coverage rule. The primary log differences were +0.017 for Ccng2, −0.255 for Cdkn1b, −0.260 for Rbl2 and −0.499 for Gadd45a. A second implementation checked the direct CPM calculation against individual vehicles. The primary mean was lower than each of the nine and remained −0.267 to −0.226 after omitting one vehicle from the reference. The small positive comparator-adjusted difference fell inside the vehicle range. It exceeded 143 of 217 other drugs, but only two of 15 other drugs sharing the HI.3140 identifier block, which had no vehicle. Neither rank estimates biological uncertainty.

The authors' analysis removed four principal components and evaluated each library against the larger screen. As a sensitivity check, its independent processing of the same single drug library also yielded only one positive primary-gene z-score (Cdkn1b +0.91; the other three ranged from −0.39 to −0.10). The target with a positive sign changed under reprocessing. None of the four had an author-displayed adjusted P-value below 0.95. This comparison supports lack of coordinated induction under these conditions. It does not show specific repression by the drug. [Author methods and interpretation](https://doi.org/10.1093/hmg/ddy221) · [Displayed results](http://bigbear.med.uottawa.ca:1000/apps/mouseCorticalRNA-app/)

## Implication for WWOX research

The originally observed decrease in the untreated WWOX organoids remains. Reversal of that decrease by ethosuximide at this exposure now lacks support from two neural preparations. The primary-culture result adds a normal brain-derived compartment beyond N2A, with a different stage, exposure duration and comparator. Because the treated library lacks an independent replicate and a same-identifier-block vehicle, neither effect magnitude nor its direction should be generalized to WWOX-deficient human progenitors. Cell-type proportions, timing, and concentration remain plausible modifiers. A model-specific low-dose increase in neuronal yield independent of the four-gene panel is a separate prediction. A genotype-by-drug contrast for lineage-normalized survival and absolute mature-neuron yield would distinguish that possibility from a change in marker proportions. [Earlier disease-side analysis and criteria](../ethosuximide_20261123/README.md)

## Reproduction

Run with Python 3 and NumPy. Download the count matrix and sample annotations below and use their local paths in this order. The script aligns columns by the deposited library identifiers, requires unique annotations for all panel genes, calculates library totals over all deposited rows, and uses the geometric mean of genes positive in all samples for median-ratio size factors. Its output includes all screen contrasts and the input hashes. Only our code and calculated summaries are distributed. Source methods and selected database entries were consulted for this check.

```bash
python3 analyze.py GSE110256_combined.count.txt.gz GSE110256_series_matrix.txt.gz results
```

[Counts](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/suppl/GSE110256_combined.count.txt.gz) · [Library metadata](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/matrix/GSE110256_series_matrix.txt.gz) · [GEO series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110256) · [Gene-level output](results/genes.tsv) · [Screen contrasts](results/screen.tsv) · [Summary](results/summary.tsv) · [Input hashes](results/sources.tsv)
