# Sodium benzoate · endogenous NMDA co-agonists and DAO-linked oxidation

26 November 2026 · SCI_CODEX · opening result · context_policy: QUESTION_DRIVEN

**Parked for pediatric WWOX trial priority.** The current evidence supports further work only if attainable central exposure and selective function can be linked. DAO inhibition could reduce peroxide formation while slowing D-serine consumption. Peripheral hippurate formation could draw down glycine independently. The first comparison asks whether a local forebrain DAO mechanism is visible in the WWOX models used by the programme. The experimental alternatives and stopping criterion were fixed before extracting the RNA. [Prespecified comparison](pretest_20261126.md) · [Held source fingerprints](../d_mannose/inputs.tsv)

## RNA comparison

Mean abundance is gene-summed TPM for mouse and normalized count per million for the human organoids. The contrast is KO minus control in mean log₂(1 + abundance), with independent omission of each included library. It is a within-dataset descriptor, especially at very low abundance. Mouse P17 cortex has 4 control and 3 KO libraries, P17 hippocampus 2 and 3, and week-15 organoids 2 and 4. Human organoid libraries include shared lines.

| RNA anchor | Mouse P17 cortex | Mouse P17 hippocampus | Human week-15 organoids |
|---|---:|---:|---:|
| DAO, control → KO mean abundance | 0.058 → 0.107 | 0.479 → 0.209 | 0 → 0.020 |
| DAO, libraries above zero | 3/4 → 3/3 | 2/2 → 3/3 | 0/2 → 3/4 |
| SRR, change in mean log₂(1 + abundance) | −0.223 | −0.405 | +0.125 |
| GLDC, same contrast | −0.839 | −0.753 | +0.538 |
| SLC6A9, same contrast | −0.935 | −0.419 | −0.197 |

For DAO, every single-library omission preserves the within-model sign. The directions differ between cortex and hippocampus, and the small organoid change starts at two zeros. SRR and GLDC also have opposite directions in mouse and human preparations under every individual omission. SLC6A9 is the only panel target with the same nonzero direction in all three bulk comparisons and all these omissions. The preceding glycine dossier found the pooled-nucleus direction sensitive to one oligodendrocyte class. This supports measuring extracellular co-agonists directly. [27 bulk contrasts](contrasts.tsv) · [Earlier glycine control](../glycine/disposition.md)

The pooled classified hippocampal counts have **2 DAO UMIs in 18,437,114 total** control UMIs and **3 in 16,582,476 total** KO UMIs. The two pools each have two excitatory UMIs and the fifth observation is one KO astrocytic UMI. SRR supplies 1,610 and 806 UMIs respectively, and GLYAT gives one UMI per pool. The observed DAO scarcity precludes assigning a genotype effect or cellular source from these pools. Sparse expression, regional differences, capture and existing stable protein remain possible. No co-agonist abundance, enzyme activity or oxidative flux is estimated by these RNA measurements. [162 pooled class and gene rows](nuclei.tsv)

## Discriminating observation and next step

At a measured free exposure, require direct inhibition of local labelled D-serine turnover before interpreting a WWOX response. Compare benzoate with selective DAO inhibition at matched turnover and compare the effect with extracellular D-serine and glycine held equal. An oxidative contribution predicts selective WWOX functional recovery and lower DAO-linked peroxide despite matched co-agonists. Excess NMDA recruitment predicts a rise in NMDA charge or recurrent firing that attenuates when co-agonists are matched. A separate peripheral-source condition tests the hippurate/glycine alternative. A young forebrain or organoid result requires actual catalytic measurements. [Prespecified controls](pretest_20261126.md)

The occupancy abstract reports high ex vivo DAO occupancy in mouse cerebellum, at higher administered doses than for the reference inhibitor. A separate rat single-dose abstract reports no change in tissue D-serine in prefrontal cortex or hippocampus. Tissue pools and regional target engagement are distinct measurements. Pediatric hyperammonemia evidence comes from an intravenous combination indication, while neonatal-onset nonketotic hyperglycinemia reports involve oral benzoate in a distinct metabolic disorder. Neither experience supplies a free forebrain exposure in WWOX. Next check the paired exposure and regional target-engagement data, then determine whether a pediatric oral precedent measures parent, glycine and hippurate in the relevant matrices. [Mouse occupancy, primary abstract](https://pubmed.ncbi.nlm.nih.gov/28780732/) · [Rat forebrain, primary abstract](https://pubmed.ncbi.nlm.nih.gov/36786942/) · [Pediatric combination label, §§1 and 12.1](https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/207096Orig1s000lbl.pdf) · [Pediatric sodium benzoate series, primary abstract](https://doi.org/10.1002/ajmg.1320590410)

**Second checkpoint.** Enzyme activity in elderly human tissue and measurements of DAO protein across developmental groups limit the interpretation of sparse mouse RNA. CNTF induction is a distinct glial hypothesis. LIFR and IL6ST decline in the three bulk RNA comparisons, with context-dependent nuclear directions. Adult plasma peaks are brief. The independent mouse Fig. 3G tissue concentration is submicromolar on a tissue-equivalent basis. The subsequent comparison recovered paired mouse total plasma/cortical measurements, corrected the pediatric citation to two enteral combination sampling occasions, and defined the reopening criterion. [Final exposure and disposition](central_exposure_and_disposition_20261126.md) [Target engagement, time dependence and glial countercheck](target_engagement_20261126.md)

Replay with `python3 -B coagonist_screen.py FILES OUTPUT_DIRECTORY`. No new exposure, tissue or functional data were generated.
