# Ethosuximide and neural cell-cycle exit during WWOX loss

**Research decision, 23 November 2026.** Keep a developmental hypothesis for a direct perturbation test. The four transcripts induced by ethosuximide in a mouse cell line are collectively lower in untreated WWOX-knockout human organoids. Independently counted human neuronal promoters give partial support, although the same-assay specificity comparison depends on promoter width. The data do not establish that the drug restores neural development in WWOX deficiency. The experiments used to make this comparison contain no ethosuximide-treated WWOX-deficient sample.

## Why these four genes?

Differentiated N2A cells exposed to ethosuximide increased expression of Ccng2, Cdkn1b, Rbl2 and Gadd45a. The authors also assayed Cdkn1a, Bcl2l11, Cat, Sod2 and Eif4ebp1. These five provide a comparator from the same experiment. The first three primary genes regulate cell-cycle progression. GADD45A also responds to DNA damage. The upstream FOXO dependency was established in a worm neurodegeneration experiment. The mammalian assay measured transcripts. WWOX-deficient human organoids exhibit altered radial-glial cell cycling, impaired neuronal generation and dysregulated MYC/Wnt signaling. Our inference is that restoring cell-cycle exit in the appropriate progenitor state could increase neuronal yield. It could also reduce yield by depleting precursors or eliciting a damage response. [Chen et al., Fig. 4a](https://doi.org/10.1186/s13024-015-0046-3) · [Steinberg et al., 2026](https://pubmed.ncbi.nlm.nih.gov/42397075/)

## Frozen prediction and outcome

[prediction.md](prediction.md) fixes both panels and a two-context decision before the WWOX calculations. Effects below are WWOX-loss minus control differences in mean log2(expression + 1). The organoid analysis uses sample CPM, the mouse analyses deposited transcript TPM summed by Ensembl gene symbol. Each sample has equal weight. The human H9 gene table uses deposited CAGE tags per million. No cohorts were pooled.

| System | Primary effect | Primary minus comparator | Interpretation |
|---|---:|---:|---|
| Human week-15 WiBR3 organoids, 4 KO vs 2 WT | −0.185, 4/4 decrease | −0.132 | Both effects stay negative after omitting any one library. Individual genes decrease by 0.057–0.286 log units. |
| Human differentiated H9, 1 library per arm, deposited gene table | Insufficient coverage | Insufficient coverage | Only CDKN1B and GADD45A present. The former is below 1 TPM in both. |
| Human differentiated H9, direct BED recount, 100 bp | −0.878, 3/3 measurable decrease | Insufficient coverage | Only 3/5 comparators meet the count floor. GADD45A is nearly unchanged. |
| Same H9 libraries, direct recount, 500 bp | −0.873, 3/4 decrease | −0.366 | All three cell-cycle genes decrease. GADD45A increases slightly (+0.036). Four comparators qualify. |
| Mouse neuronal deletion, cortex, 3 vs 4 | −0.098, 3/4 decrease | −0.021 | Both effects can change sign after omitting one animal. |
| Mouse neuronal deletion, hippocampus, 3 vs 2 | −0.199, 2/4 decrease | −0.145 | Ccng2 is influential. Omitting one gene can reverse the primary effect. |

In organoids the difference stays between −0.213 and −0.144 after omitting a library. The differentiation panel decreases (−0.286), while the smaller cycling-panel increase (+0.095) changes sign in a leave-one-library-out check. Changing the mix of cell types could explain all four primary decreases. Among all 15 two-control allocations the recorded group labels produced the lowest primary score. In a separate, exploratory comparison, 10.1% of 100,000 expression-matched random gene quartets fell at least as low, and 4.3% fell as low with every gene negative. These describe specificity within this dataset. Correlated genes, organoid derivations and the small control group limit inference. [Steinberg and Aqeilan, GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [2021 organoid study](https://doi.org/10.15252/emmm.202013610)

### What the original H9 reads added

The deposited gene table lacks CCNG2 and RBL2. Reassigning the deposited FANTOM5-mapped clusters to curated promoters still misses both. A separate [prediction for the BED recount](raw_prediction.md) fixed the reference-build test, count floor, uniqueness rule and two windows before counting. Off-panel calibration on 120 genes favored hg38 over hg19 (median Spearman correlation across four libraries at 100 bp, 0.621 vs 0.129). The wider window recovered 228 vs 140 CCNG2 reads, 117 vs 49 CDKN1B reads and 170 vs 41 RBL2 reads (control vs WWOX knockdown). The fourth gene had 162 vs 208 tags. Both denominators give the same differentiated-neuron result because the BED and inferred library totals agree. These two normalizations provide no independent replication. [Kośla et al., H9 model and CAGE methods](https://doi.org/10.3389/fncel.2019.00391) · [GSE126075](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126075)

The H9 precursor control has 31,702,049 complete BED records against an inferred 51,007,825 tags. It has a malformed terminal record and grossly incomplete chromosome coverage. Count normalization cannot restore missing chromosomal intervals. We exclude the raw precursor comparison and its developmental interaction from biological interpretation. The processed H9 cycling-panel interaction is −1.172, based on one library per condition. A subset of the promoter data supports relative deficiency of three cell-cycle transcripts in the differentiated cells, but the stricter comparison fails the coverage rule at 100 bp. The prediction therefore remains partly supported. [Coverage by chromosome](results/raw_chromosomes.tsv) · [Per-gene recount](results/raw_genes.tsv) · [Mouse cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Mouse hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681)

## Exposure is a second, independent constraint

- Chen et al. found no significant induction at 0.1 mg/mL (0.71 mM). Positive N2A exposures were 0.56 and 1 mg/mL (3.97 and 7.08 mM, molecular weight 141.17). The lower positive nominal exposure was 5.6 times the upper end of the label's 40–100 µg/mL total plasma interval. Culture medium, free brain exposure and human total plasma are different measurements. This weakens translation of the four-gene mechanism. [Chen et al., Fig. 4a](https://doi.org/10.1186/s13024-015-0046-3) · [DailyMed, ethosuximide](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a825265d-ace9-4463-a16d-f6d5e1e31188)
- In primary neonatal rat forebrain cells after growth-factor withdrawal, the investigators reported 7.18% MAP2-positive cells in controls, 21.77% at 0.1 µM and 41.57% at 1 µM. They also observed increased proliferation. This different preparation and endpoint leave open a low-exposure route to altered cell fate. Its 1 µM condition is roughly 4,000 times below the first positive N2A exposure. The rat result alone cannot connect differentiation to those four transcripts. A separate toxin-injury rat study implicates PI3K/Akt/Wnt. The direction of Wnt dysregulation in WWOX organoids makes extrapolation particularly uncertain. [Rat forebrain study, abstract](https://pubmed.ncbi.nlm.nih.gov/24354536/) · [Tiwari et al., abstract](https://pubmed.ncbi.nlm.nih.gov/26420483/) · [WWOX organoid study](https://doi.org/10.15252/emmm.202013610)

**Discriminating prediction.** At a verified exposure overlapping the pharmacologically relevant range, WWOX-deficient progenitors would need to produce more surviving, functionally differentiated neurons per starting progenitor, together with a movement of the three cell-cycle transcripts toward isogenic controls. Compare within lineage and developmental stage, with a comparator matched for suppression of network firing. Track precursor survival and absolute neuronal yield as well as marker-positive fractions. A response confined to high nominal exposure, an increase in marker percentage accompanied by cell loss, or equivalent improvement after matched firing suppression would each weaken the specific cell-cycle hypothesis. A low-exposure gain in absolute yield without the transcript response would favor a different mechanism. None of these treatment outcomes has been observed here.

## Reproduction and provenance

Only original calculations, short data summaries and code are distributed. Use the public GEO deposits and the [NCBI RefSeq Curated annotation distributed by UCSC](https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/). Input filenames and SHA-256 values are in results. The raw recount uses the four supplementary BED files GSM3590948–GSM3590951 and ncbiRefSeqCurated.txt.gz from both hg19 and hg38. Mouse annotation is Ensembl GRCm38 release 92. Exposure and model claims above use the cited figure, abstracts, label or dataset metadata, with no claim of a newly completed paper reading.

Run these from this directory with Python 3 and NumPy. FILES is the LEGEND files cache. BEDS contains the four public .bed.gz files. HG19 and HG38 point to the respective downloaded RefSeq tables.

```bash
python3 analyze.py "$FILES" results
python3 organoid_specificity.py "$FILES"/geo/GSE156243/*count_table.txt.gz results
python3 promoter_sensitivity.py "$FILES"/geo/GSE126075/*F5mapped.txt.gz "$HG38" results
python3 raw_promoters.py "$FILES/geo/GSE126075" "$BEDS" "$HG19" "$HG38" results
```

[Panel results](results/panels.tsv) · [Library values](results/libraries.tsv) · [Gene coverage](results/genes.tsv) · [Raw calibration](results/raw_calibration.tsv) · [Sensitivity analysis](results/raw_panels.tsv) · [Matched quartets](results/organoid_matched.tsv)

## Cross-syndrome comparison and burst experiment

The [27 November follow-up](dismech_comparison_20261127.md) reconciles direct Wwox and published clinical exposure, tests the waveform alternative to scalp phase–amplitude coupling, and defines the next acute comparison with verified native CaV3 engagement. This follow-up keeps the developmental response and direct seizure effect separate.
