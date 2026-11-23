# Ethosuximide, WNT signaling and cortical fate in WWOX loss

**Research decision, 23 November 2026.** A direct drug exposure gives a reason to take WNT engagement seriously. In ordinary mouse cortical cultures exposed to 700 µM ethosuximide for eight hours, the three reliably measured WNT readouts rose together. Across 218 treatments, the panel ranked third using our count-based calculation and **tied for second** after processing by the study authors. Both calculations used the same single treated library. The corresponding WNT readouts were already elevated in untreated human WWOX-null organoids. Simple transcriptional reversal is therefore a poor rationale at this stage. Whether the drug increases or reduces the yield of surviving cortical neurons in the WWOX condition remains unresolved. [Hadwen et al.](https://doi.org/10.1093/hmg/ddy221) · [Earlier disease-side analysis](../gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md)

## The direct drug observation

A previous ethosuximide study in rat hippocampal neural stem cells reported enhanced proliferation and differentiation, with functional perturbations implicating PI3K/Akt/Wnt at 100 µM. The mechanistic connection we tested was that this action might reinforce an already elevated WNT program in developing WWOX-deficient tissue. The independent drug screen used mouse mixed cerebrocortical cultures at DIV21. These preparations differ in exposure, stage and lineage. [Tiwari et al., primary study](https://pubmed.ncbi.nlm.nih.gov/26420483/) · [Direct ethosuximide sample](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2983478)

| WNT readout | Median control CPM | Drug minus median vehicle, log2 | Authors' robust z after technical correction |
|---|---:|---:|---:|
| AXIN2 | 16.77 | +0.062 | +2.10 |
| NKD1 | 7.14 | +0.511 | +1.21 |
| APCDD1 | 8.94 | +0.402 | +1.90 |
| LEF1 | 0.19 | −0.097 | Below our coverage floor; excluded |

The mean over eligible genes was +0.325, against leave-one-vehicle-out values from −0.219 to +0.212. Median-ratio normalization gave +0.337. Only 51 of 10,000 random triplets matched for baseline expression and control variation achieved a value at least as large. The drug exceeded 215 of the other 217 agents and 14 of the 15 other agents in its library identifier block. On the authors' screen, which removes four principal components, one drug had a higher mean z and a second tied with ethosuximide at the displayed precision. None of the three individual gene results had an adjusted P value below 0.83. Shared technical effects, the selected panel and the lack of a treated biological replicate limit both ranks. A three-gene RNA change cannot establish nuclear β-catenin activity or dependence on WNT signaling. [Count results](results/drug_summary.tsv) · [Specificity calibration](results/drug_specificity.tsv) · [Author processing](results/author_processing.tsv) · [Author-based rank](results/author_rank.tsv)

## The regional-fate prediction fails

We applied marker panels from an independent day-21 human neural organoid perturbation study to the week-15 WWOX knockout. A classical posterior shift would lower telencephalic progenitor markers and raise at least one posterior or diencephalic progenitor panel. Instead **all four progenitor panels increased**. The CNS-neuron panel decreased. Quantities are WWOX knockout minus control mean differences on log2(CPM + 1), four vs two libraries. They measure marker expression in whole tissue.

| Marker panel | Eligible genes | WWOX difference | Range after omitting a library |
|---|---:|---:|---:|
| Telencephalic progenitors | 11 | +0.286 | +0.245 to +0.341 |
| Diencephalic progenitors | 10 | +0.272 | +0.148 to +0.395 |
| Hindbrain progenitors | 6 | +2.085 | +1.131 to +3.039 |
| Spinal cord progenitors | 6 | +1.196 | +0.636 to +1.756 |
| CNS neurons | 11 | −0.146 | −0.214 to −0.077 |

Each mean also retained its sign on dropping a gene. A higher relative progenitor contribution or altered expression within cells could generate this pattern. The source diencephalic markers include cortical hem. Bulk RNA cannot resolve regional cell counts or total neuronal yield. [GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Transferred markers](results/disease_markers.tsv) · [Checks](results/disease_scores.tsv)

The GSK3 inhibitor CHIR99021 also produced different lineage outcomes across human organoid conditions. In the HES3 SMG2 series (days 0–9; eight organoids per concentration; endpoint day 21), the odds of a telencephalic progenitor among sampled cells relative to control decreased at 0.6 and 1 µM (each OR about 0.13), were unresolved at 1.4 µM and increased at 1.8 µM (OR 6.16). In another experiment, H9 CHIR_E gave strong telencephalic depletion and hindbrain enrichment (OR 14.25). Retinoic acid also produced this joint direction in some conditions. The source's cell-level enrichment tests and their adjusted P values do not quantify uncertainty across independent organoids. CHIR acts on GSK3, has a different mechanism from ethosuximide, and its concentrations cannot be converted into ethosuximide concentrations. These outcomes explain why elevation of a transcriptional pathway cannot by itself predict regional benefit or harm. [Sanchís-Calleja et al., Fig. 2, Supplementary Fig. 1 and Table 3](https://doi.org/10.1038/s41592-025-02927-5) · [All source contrasts, including XAV939](results/reference.tsv)

In a post-primary check, the WWOX peripheral-progenitor panel rose (+0.199, five eligible genes). Neither neural crest nor peripheral neuronal panels met the four-gene coverage floor. Among the high CHIR conditions the reference supplies no PNS-progenitor row linking that specific finding to the drug proxy. The lack of a row is an unavailable comparison. This sensitivity supplies no alternative regional match. [Post-primary rules](sensitivity.md) · [Peripheral-lineage transfer](results/peripheral_scores.tsv) · [Source comparisons](results/peripheral_reference.tsv)

## What would change the decision

**Working prediction.** If the developmental action depends on where a progenitor starts on the WNT response curve, identical ethosuximide exposure could increase neuronal yield in a WNT-low compartment while having little benefit or a detrimental effect on cortical fate in a WNT-high compartment. Classify cultures by pretreatment canonical WNT activity independently of genotype, then compare the within-lineage change in absolute surviving cortical neurons per starting progenitor between WWOX-null and isogenic cultures. Measure nuclear β-catenin and cycling alongside neuronal yield, and compare with both a WNT-normalizing condition and another agent matched for reduction of network activity. Recovery of absolute cortical-neuron yield at verified exposure without further WNT elevation in the deficient compartment would favor developmental benefit through another route. A rise restricted to progenitor number or marker-positive percentages would leave that question open. No WWOX-deficient preparation in these datasets received ethosuximide. [Prior four-gene drug test](../ethosuximide_cortex_20261123/README.md)

## Reproduction and permissions

The [initial rules](prediction.md) were committed before extracting new expression values, enrichment odds or marker rankings. Supplementary Tables 1 and 3 of Sanchís-Calleja et al. (2025) were used under CC BY 4.0; this is a new selection, calculation and interpretation by the LEGEND laboratory. Only derived summaries and original code are distributed. Source checks used selected primary methods, reported endpoints, the figure design and data tables.

Download the [GSE110256 counts](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/suppl/GSE110256_combined.count.txt.gz), [sample annotations](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/matrix/GSE110256_series_matrix.txt.gz), [Table 3](https://pmc-oa-opendata.s3.amazonaws.com/PMC12904787.1/41592_2025_2927_MOESM5_ESM.xlsx), [Table 1](https://pmc-oa-opendata.s3.amazonaws.com/PMC12904787.1/41592_2025_2927_MOESM3_ESM.xlsx), and [WWOX series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243). Pass the paths to each script in that order. Python 3 and NumPy suffice.

```bash
python3 analyze.py "$DRUG_COUNTS" "$DRUG_META" "$TABLE3" "$TABLE1" "$WWOX_COUNTS" results
python3 sensitivity.py "$DRUG_COUNTS" "$DRUG_META" "$TABLE3" "$TABLE1" "$WWOX_COUNTS" results
python3 author_rank.py "$AUTHOR_TABLES" results
```

For the independent processing check, use Gene Symbol in the [authors' public application](http://bigbear.med.uottawa.ca:1000/apps/mouseCorticalRNA-app/). Select Axin2, Nkd1 and Apcdd1 in turn. Keep the full positive and negative z ranges including outliers. Copy both tables for each gene into a tab-separated file with that symbol as its name. The script handles duplicate displayed zeros, enforces 218 unique drug conditions and uses decimal values for ties. [Input hashes](results/sources.tsv)
