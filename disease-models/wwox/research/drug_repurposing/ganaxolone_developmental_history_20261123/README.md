# Ganaxolone hypothesis under a developmental neurosteroid challenge

**Research decision, 23 November 2026.** A developmental history of exposure to allopregnanolone followed by its removal leaves a late imbalance between receptor and downstream signaling transcripts in human ventral organoids. WWOX-null organoids at week 15 do not reproduce the published direction of that imbalance. The observed directions are reciprocal, but two of five receptor genes are essentially unmeasurable in the control tissue. More importantly, independently generated dorsal and ventral organoids of precisely the same age can reproduce both arm directions by changing their relative contributions. This lowers the priority of a generalized developmental steroid-replacement interpretation of these bulk transcripts. An unresolved GABRB3 decrease is a narrower lead for testing within a defined neuronal lineage. [Neurosteroid source](https://doi.org/10.3389/fncel.2025.1715823) · [WWOX organoid source](https://doi.org/10.15252/emmm.202013610) · [Regional reference](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE93811)

## Why the timing matters

The source investigators treated ventral and dorsal organoids with 125 nM endogenous allopregnanolone from day 28 to 67 and then followed them to day 138. In ventral organoids they reported an early GABRB3 decline after removal and later increases in five GABA-A receptor transcripts, alongside a persistent aggregate deficit of eight downstream GABA-signaling elements. Tissue was compared with vehicle-exposed controls; a group maintained continuously on steroid through the late readout would be needed to isolate an effect of withdrawal itself. Histologic outcomes were fractions of DAPI-positive cells. The study involved neither WWOX loss nor ganaxolone. Transferring its program to WWOX disease was our hypothesis. [Source, Fig. 3–4 and supplement](https://doi.org/10.3389/fncel.2025.1715823)

## What the genetic model shows

The [frozen primary test](prediction.md) required at least four of the five receptor genes to average at least 1 CPM in the two control libraries. Only GABRA5, GABRB3 and GABRG2 qualified. GABRA1 had 0.027 CPM and GABRB1 had zero. All eight effector genes qualified. Units below are WWOX knockout minus control mean differences on log2(CPM + 1), four vs two libraries.

| Panel | Difference | Range after omitting a library |
|---|---:|---:|
| Three quantifiable GABA-A receptor genes | −0.358 | −0.533 to −0.183 |
| Eight downstream effectors | +0.643 | +0.527 to +0.759 |
| Receptors minus effectors | −1.001 | −1.103 to −0.886 |
| Four interneuron markers | +1.953 | +1.138 to +2.768 |
| Four broadly neuronal markers | −0.317 | −0.394 to −0.240 |

Including all five mapped receptors yielded −0.205 and preserved the qualitative discrepancy with the late steroid condition. The WWOX differential is unusual relative to unrelated genes chosen for similar expression and age slopes in unperturbed cortical spheroids at days 40–160 (23 libraries, four informative lines). Only 4/2,000 matched panel differences fell below −1.001. The central 95% of decoys spanned −0.739 to +0.852. This specificity comparison cannot repair insufficient receptor coverage. Elapsed culture time also cannot account for regional identity or cell mixture. [Gene results](results/genes.tsv) · [Decoys and all-age sensitivity](results/development_controls.tsv) · [Independent maturation reference](https://doi.org/10.1038/s41593-021-00802-y)

## Could regional identity produce the pattern?

We fixed a [second prediction](region_prediction.md) before extracting a separate human reference, which included pallial and subpallial spheroids collected at day 105 from one iPSC line. A mixture was fitted on four GABA-lineage markers independently of both outcome panels. The pooled reference contains 7,124 pallial and 4,714 subpallial cell profiles. The different cells represent two deposited regional samples, each without a second independent replicate.

Every positive subpallial weight tested in the pooled-count analysis gave a receptor decrease and effector increase. The best grid weight, 0.3 subpallial RNA contribution to an initially pallial mixture, predicted **−0.182 receptors and +0.396 effectors**, compared with **−0.358 and +0.643 observed**. Giving equal weight to cells with at least 500 molecules selected a mixture weight of 0.2 and gave −0.055 and +0.374. Those fitted weights refer to external synthetic mixtures, with a different measurement platform and differentiation protocol. They cannot be used to estimate tissue proportions in the WWOX samples. [Mixture grid](results/region_grid.tsv) · [Independent same-age regional profiles](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA362464)

| Gene | WWOX observed | Best pooled mixture |
|---|---:|---:|
| GAD1 | +3.033 | +3.011 |
| GAD2 | +1.412 | +1.252 |
| SST | +2.903 | +2.961 |
| CALB2 | +0.464 | −0.393 |
| GABRB3, outside the marker fit | −0.942 | −0.191 |
| GABBR2, outside the marker fit | +1.043 | −0.089 |

Regional patterning reproduces three marker shifts and the sign of both panels. It misses CALB2, underestimates GABRB3 loss and gives the wrong sign for GABBR2, a metabotropic receptor. These residuals can arise from subtype or developmental differences as well as intrinsic regulation. The study's public single-cell accession for WWOX organoids, E-MTAB-14792, returned HTTP 403 to the public BioStudies request on 23 November. No cell-level disease estimate is claimed. [Per-gene transfer](results/region_genes.tsv) · [WWOX single-cell study](https://pubmed.ncbi.nlm.nih.gov/42397075/)

**Discriminating prediction for ganaxolone.** Within the same identified neuronal subtype and developmental stage, ask whether GABRB3 protein and neurosteroid-sensitive GABA-A currents remain altered despite matching lineage proportions. Then test whether ganaxolone changes those currents and whether effects on maturation persist during continued exposure versus after its removal. Compare isogenic controls, matched firing suppression, and the same lineage at the same age. A signal confined to total-tissue measurements or to differences in lineage yield would favor the tissue-composition hypothesis. A within-lineage signal could support drug testing while leaving the direction of benefit open. The data here provide no evidence that human neural WWOX loss depletes endogenous allopregnanolone.

## What the actual drug adds to the developmental analogy

**The specific prediction changes when ganaxolone is compared directly with allopregnanolone.** Modgil and colleagues measured both drugs at two recombinant receptors. The maximum response to ganaxolone was larger at α1β2γ2 than at α4β3δ (400% versus 225% of the respective GABA-alone current). The ordering reversed with allopregnanolone (229% versus 426%). Both had a lower EC50 at α4β3δ. Lower EC50 therefore cannot identify which receptor contributes the larger maximum gain. Each summary was based on three observations per receptor and compound. [Modgil et al., Table 1 and methods](https://pubmed.ncbi.nlm.nih.gov/27743930/) · [Derived comparisons](results/receptor_anchors.tsv)

Consider a **hypothetical substitution** at fixed total baseline GABA current, where a fraction of baseline current carried by α1β2γ2 transfers to α4β3δ. The predicted change in total percentage potentiation equals that fraction times the difference between the two gains. At saturation, a 10 percentage-point shift would change the ganaxolone response by −17.5 percentage points and the allopregnanolone response by +19.7. The opposite signs survive changing each reported maximum independently by one SEM. These are calculations from observed endpoints. Interpolation also needs Hill slopes, which were unavailable here. In a sensitivity grid (slopes 0.7, 1 or 1.5 for each receptor, independently varying both pEC50 and maximum by one SEM), the predicted substitution effect at 100 nM spans both signs for ganaxolone. At 1,000 nM its sign is negative throughout this chosen grid and positive for allopregnanolone. These are assay concentrations and illustrative parameter bounds. The calculation does not estimate brain exposure, subunit stoichiometry or the mix in WWOX. [Model values and sensitivity bounds](results/receptor_mixture.tsv)

In 15-week WWOX-null organoids, bulk GABRB2 and GABRB3 both fell (−1.65 and −0.94 log2 units), whereas GABRA1 and GABRA4 each averaged below 0.1 CPM in both genotypes. At a 1 CPM floor, **zero of six libraries** detected all three components of either exact recombinant assembly. In a separate healthy cortical organoid series, for the descriptive age window 80–139 days spanning the disease study, all five libraries from four lines detected the α1β2γ2 transcripts and three of five detected the α4β3δ transcripts. Protocol, line and maturation affect this transfer. Bulk detection also cannot show that three subunits occupy the same cell or receptor. Consequently the genotype-dependent mixture required for the quantitative prediction is unmeasured. Alternative α subunits and other neuronal lineages remain possible. [WWOX subunit estimates](results/receptor_composition.tsv) · [Threshold sensitivity](results/receptor_detectability.tsv) · [Independent organoid reference by line and day](results/receptor_reference_ages.tsv)

**Time separates a second mechanism.** In juvenile male wild-type mouse dentate granule cells, 100 nM ganaxolone acutely increased tonic current by 36.7 pA in six paired cells (reported P=0.004). In a separate experiment, following 15 min exposure at 1 µM and 30–60 min washout, its mean was 13.5 pA above vehicle (reported P=0.14), compared with +51.9 pA for allopregnanolone. A direct descriptive difference between post-washout drug means was −38.4 pA (±25.0 pA as twice the independent-group SE from the published summaries). This interval calculation assumes independence across groups and lacks animal-level covariance. Figure 6 tested β3 phosphorylation and surface expression for allopregnanolone and SGE-516; it supplies no direct ganaxolone protein measurement. Acute responses were paired within cells while post-washout responses compared separate groups at a different concentration. These values cannot give a drug retention fraction. [Modgil et al., Figs. 1, 3 and 6](https://pubmed.ncbi.nlm.nih.gov/27743930/) · [Washout calculations](results/washout_comparisons.tsv)

**Discriminating WWOX prediction.** At matched developmental age, lineage and *initial* current potentiation, lasting neurosteroid effects should be tested separately for the actual drug and allopregnanolone after removal. If both drugs initially potentiate GABA currents yet only the endogenous steroid retains tonic current or changes maturation after removal, its developmental history is a poor proxy for ganaxolone. A reproducible ganaxolone-specific persistent change in WWOX-null cells relative to isogenic controls would reopen that route. To connect it to cell benefit, measure maturation and surviving neuron yield separately at matched suppression of firing. The adult-type receptor mixture model sharpens where the drugs can diverge. The present bulk dataset fails to identify the relevant assembly in the disease cells.

## Reproduction and sources

The first analysis needs the GSE156243 count table, the GSE150123 deposited archive of sample counts and sample matrix, and the archived complete HGNC mapping. The second uses the two molecule matrices for GSE93811. The output files include input hashes. Only our code and original calculated summaries are distributed. Source inspection for this analysis used targeted results, figure descriptions, methods, metadata and data availability statements. Steroid and WWOX organoid protocols and developmental stages differ.

```bash
python3 analyze.py /path/to/legend/files results
python3 region_mix.py GSM2462860_hCS_MolPerCellPerGene.csv.gz GSM2462861_hSS_MolPerCellPerGene.csv.gz results/genes.tsv results
```

[WWOX counts](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Time-course counts](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150123) · [Pallial data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2462860) · [Subpallial data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2462861) · [Primary input hashes](results/sources.tsv) · [Regional input hashes and counts](results/region_sources.tsv) · [All label allocations](results/allocations.tsv)

The targeted pharmacology review used the methods, Table 1 and Figures 1, 3 and 6 of Modgil et al. Numerical inputs and code for our derived calculations are in [receptor_transfer.py](receptor_transfer.py). Reproduce with `python3 receptor_transfer.py` and `python3 receptor_coverage.py /path/to/files/geo results`. The latter reuses the hashed GEO and HGNC inputs of the first analysis. No source artwork or supplementary workbook is distributed.
