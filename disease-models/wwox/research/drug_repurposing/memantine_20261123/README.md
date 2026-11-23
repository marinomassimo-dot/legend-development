# Memantine and activity-dependent transcription in WWOX deficiency

**Decision, 23 November 2026.** A pattern of gene expression that detects prolonged NMDA stress in stimulated mouse neurons fails its prespecified test in untreated Wwox-deficient mouse brain. This lowers the priority of memantine as a means of correcting **sustained, widespread NMDA-dependent suppression of activity-regulated transcription**. A short-lived or cell-specific effect during bursts remains plausible. No sample in the WWOX studies analyzed here received memantine. The comparison gives no estimate of seizure reduction or patient benefit.

## A control for ordinary loss of neuronal firing

The causal question is whether loss of WWOX adds a stress response that memantine could interrupt while preserving useful neuronal signaling. Both intense NMDA activation and ordinary cessation of firing can reduce activity-induced transcripts. We used the Oberländer et al. experiment in which sister hippocampal cultures from five mouse preparations were stimulated and then silenced. The paired contrast measures what adding NMDA to the silenced culture does. This design controls duration of prior activation, duration after silencing and preparation. The experiment also included an inhibitor of glutamate uptake (TBOA) as a separate challenge. [Original study](https://doi.org/10.1038/s42003-025-09074-9) · [GSE184681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184681)

The [prediction](prediction.md) was committed before the target calculations. Three preparations supplied 171 activity-induced genes meeting the expression criteria. Seventy decreased with NMDA in all three. We paired the 20 strongest with 20 comparison genes drawn from 29 that changed little with added NMDA. Matching considered starting abundance, induction by firing and passive loss after silencing. The largest residual difference was 0.205 standard deviations for passive loss. The two withheld preparations supplied the following tests. Values are differences in mean log2(CPM + 1), hits minus matched comparison genes.

| Challenge | Preparation 7 | Preparation 8 |
|---|---:|---:|
| NMDA added after identical silencing, 1 h | −1.069 | −1.004 |
| Shorter NMDA interval, 30 min | −0.656 | −0.498 |
| Glutamate uptake inhibition vs continued stimulation, 1 h | −0.259 | −0.326 |
| Passive silencing vs continued stimulation, 1 h | +0.137 | +0.068 |

The signature distinguishes the two causes of transcriptional decline in this culture system. TBOA changes neuronal activity as well as extracellular glutamate. Its weaker signal supports transfer to a different perturbation within this experiment. [Per-preparation results](results/validation.tsv) · [Gene pairs](results/pairs.tsv)

## Transfer to WWOX loss

Each tissue value is a genotype or injury difference in the within-library mean of hit minus comparator expression. Lower values were predicted. Animal/library is the unit. No ratio or pooled estimate is taken across preparations, species, tissues or expression platforms.

| Untreated WWOX context or acquired injury | Units (case/control) | Matched pairs | Hit change | Comparator change | Difference | Leave-one-library-out range |
|---|---:|---:|---:|---:|---:|---:|
| Mouse hippocampus, neuronal Wwox deletion | 3/2 | 20 | −0.195 | −0.164 | −0.031 | −0.242 to +0.114 |
| Mouse cortex, neuronal Wwox deletion | 3/4 | 20 | −0.222 | −0.302 | +0.080 | +0.044 to +0.111 |
| Mouse hippocampus, 14 days after kainate | 6/6 | 17 | +0.058 | +0.010 | +0.048 | −0.003 to +0.153 |
| Human cerebral organoid, week 15, WWOX knockout | 4/2 | 17 | +0.088 | +0.138 | −0.050 | −0.093 to −0.004 |

In cortex, the hit genes decrease, yet their controls decrease more. In hippocampus, omitting one animal can reverse the difference. Under the primary rule neither region shows the required reproducible shutdown. A single gene pair can also reverse the cortical sign. As a sensitivity test, we repeated the matching 500 times in different random orders. All 500 retained negative NMDA contrasts in both withheld preparations. **Zero of 500** gave a negative disease contrast in both mouse regions that survived removing any one animal. These runs reuse the same data and quantify sensitivity to the matching decision. [Mouse hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Acquired injury](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319769) · [Matching-order results](results/rematching.tsv)

In human organoids, both arms increase on average. Three genes highlighted by the source authors, INHBA, BDNF and HOMER1, do each decrease (−0.365, −0.129 and −0.374). Cell mixture, cortical development, and differences between resting tissue and acutely activated neurons can produce this pattern. In the mouse knockout, Inhba rises in both tissues, and Bdnf shows little consistent change. In particular, gene-level BDNF in tissue does not isolate the exon-IV-specific readout used in culture. The named genes and exploratory human result give a reason to compare the same cell state across genotypes. They do not establish active NMDA signaling in an organoid. [Human organoid deposit](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Per-gene results](results/named_markers.tsv) · [Coverage and pair-by-pair contrasts](results/tissue_pairs.tsv)

## What the actual drug did in the source experiment

We recalculated arithmetic means from Figure 5 source values. After NMDA challenge, induced cell death at 24 h averaged **50.8% with vehicle, 11.0% at 10 µM memantine and 0.5% at 100 µM** (four independent preparations per condition). The stronger protection came with markedly weaker transcription during physiological stimulation. At 10 µM, induced Bdnf exon IV was 94% of the stimulated control and Npas4 was 64%. At 100 µM they were 24% and 3%, respectively. Under NMDA challenge, 10 µM moved Bdnf exon IV from 48% to 78% of stimulated control and Inhba from 8.5% to 26.7% (six preparations). These are separate assays. The Npas4 estimate at 10 µM is variable and the source describes its induction as broadly preserved. [Source study, Fig. 5 and Supplementary Data 2](https://doi.org/10.1038/s42003-025-09074-9) · [Recalculated means, counts and dispersion](results/figure5.tsv)

Exposure limits the inference. In an adult primary pharmacokinetic study, measured serum memantine spanned 0.025–0.529 µM and paired CSF concentrations were lower. A later study measured CSF directly in 22 adults with Alzheimer’s disease and reported a mean of 65.33 ng/mL (approximately 0.36 µM as free-base equivalent). The lower culture concentration was thus approximately 27 times that adult mean. CSF concentration, neuronal extracellular concentration during a burst and nominal bath concentration are distinct measurements. The experiment gives no concentration-response estimate near the human CSF mean, and no pediatric WWOX pharmacokinetics. [Kornhuber and Quack](https://pubmed.ncbi.nlm.nih.gov/7478269/) · [Vališ et al., Tables 1–2](https://doi.org/10.3389/fphar.2019.00943)

**Alternative mechanism and decision-changing observation.** Repeated prolonged bursts could produce an NMDA-dependent calcium load in a subset of cells that is invisible in resting bulk tissue. A Wwox slice study reports altered excitatory and inhibitory activity. The separation between synaptic and extrasynaptic blockade also depends on agonist timing, calcium and receptor subunit. A discriminating observation would be excess sustained calcium or NMDA current in WWOX-deficient neurons at matched firing, followed by selective relief with memantine at verified free exposure, alongside preservation of brief evoked responses and BDNF induction. Equivalent changes in controls or loss of the brief responses would weaken that case. Existing non-WWOX DEE trial findings do not establish this mechanism in WWOX. [Wwox slice physiology](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609180/) · [Autaptic current study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2932667/) · [Activation- and subtype-dependent block](https://pmc.ncbi.nlm.nih.gov/articles/PMC5628409/) · [DEE crossover trial](https://pubmed.ncbi.nlm.nih.gov/36256600/)

## Reproduction and reuse

Use Python 3 and NumPy. Download the [GSE184681 counts](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE184nnn/GSE184681/suppl/GSE184681_counts.csv.gz), [study metadata](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE184nnn/GSE184681/soft/GSE184681_family.soft.gz), [mouse NCBI Gene cross-references](https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Mus_musculus.gene_info.gz), and [Oberländer et al., Supplementary Data 2](https://pmc-oa-opendata.s3.amazonaws.com/PMC12678830.1/42003_2025_9074_MOESM4_ESM.xlsx). Hashes of the inputs were recorded. The LEGEND cache contains the original tissue matrices, Ensembl mouse release 92 annotation and HGNC cross-references. The NCBI Gene download changes over time. The frozen tissue-pair table records the applied Ensembl, mouse and human mapping. We require an unambiguous human-gene link through MGI/HGNC, with NCBI Gene filling gaps in the sequence-header identifiers. Missing members exclude an entire pair from its tissue score. The accompanying figures, primary data tables and article are left with the original distributors. Figure 5 summaries are our calculations from Oberländer et al. under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The drug comparisons above use the figure, its source values, and targeted passages. [Input hashes](results/inputs.sha256)

Run in this directory with FILES pointing to the laboratory cache and the other variables pointing to the four downloaded files.

```bash
python3 learn_signature.py "$COUNTS" "$SOFT" results
python3 test_wwox.py "$FILES" "$GENE_INFO" results/pairs.tsv results
python3 matching_sensitivity.py "$COUNTS" "$SOFT" "$FILES" "$GENE_INFO" results
python3 figure5.py "$FIGURE5_WORKBOOK" results
```
