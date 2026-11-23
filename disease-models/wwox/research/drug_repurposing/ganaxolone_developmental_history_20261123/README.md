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

## Reproduction and sources

The first analysis needs the GSE156243 count table, the GSE150123 deposited archive of sample counts and sample matrix, and the archived complete HGNC mapping. The second uses the two molecule matrices for GSE93811. The output files include input hashes. Only our code and original calculated summaries are distributed. Source inspection for this analysis used targeted results, figure descriptions, methods, metadata and data availability statements. Steroid and WWOX organoid protocols and developmental stages differ.

```bash
python3 analyze.py /path/to/legend/files results
python3 region_mix.py GSM2462860_hCS_MolPerCellPerGene.csv.gz GSM2462861_hSS_MolPerCellPerGene.csv.gz results/genes.tsv results
```

[WWOX counts](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Time-course counts](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150123) · [Pallial data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2462860) · [Subpallial data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2462861) · [Primary input hashes](results/sources.tsv) · [Regional input hashes and counts](results/region_sources.tsv) · [All label allocations](results/allocations.tsv)
