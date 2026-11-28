# Melatonin, sleep timing and local neural effects in WWOX loss of function

**Data scope.** P17 mouse Wwox neuronal-deletion cortex and hippocampus TPM, human WWOX-knockout week-15 cerebral organoid library CPM, and P17 mouse hippocampal pooled cell-class UMI CPM. The external comparisons use pediatric sleep timing, sleep-stage shares, overnight EEG spikes per hour, infantile spasm outcomes, serum, saliva and plasma melatonin, and oxygen consumption in isolated mouse cerebellar and HEK293 mitochondria.

`context_policy: QUESTION_DRIVEN`. The [fixed panel and predictions](pretest_20261126.md) distinguish circadian and sleep responses from receptor-dependent neural effects and from redox actions. The [prior ramelteon assessment](../../qualification_it9_p4b_a_20261030/records/P3-02_ramelteon.md) already identified low MTNR1A/B signal in WWOX organoids and rejected the proposed MTNR1A-to-BNIP3 inference.

## Receptor availability and phase

| Model, unit and control / KO libraries | MTNR1A, control → KO | MTNR1B, control → KO | ARNTL, control → KO | PER2, control → KO |
|---|---:|---:|---:|---:|
| Mouse cortex, TPM (4 / 3) | 0.011 → 0.038 | 0 → 0 | 12.14 → 8.76 | 6.55 → 4.02 |
| Human week-15 cerebral organoid, CPM (2 / 4) | 0.044 → 0.044 | 0 → 0.053 | 7.31 → 10.22 | 16.49 → 26.62 |
| Mouse hippocampus, TPM (2 / 3) | 0.022 → 0.017 | 0 → 0 | 8.41 → 7.03 | 22.72 → 26.65 |

ARNTL declines in both mouse tissues and rises in organoids. Each direction survives all single-library omissions. PER2 declines in cortex and rises in organoids under all omissions, while its hippocampal omission range crosses zero. AANAT changes from 0.059→0.174 TPM in mouse cortex, 0.052→0.032 TPM in hippocampus and 0.167→0.289 CPM in organoids. ASMT is zero in both mouse bulk comparisons and below 0.04 CPM in both human groups. The snapshots lack a matched time series. They leave phase, amplitude and basal concentration unresolved and do not locate endogenous synthesis. [Bulk data and omission ranges](bulk.tsv)

The P17 nuclear pools add evidence of sparse but nonzero signal. Excitatory MTNR1B has 13→10 assigned UMIs (1.05→0.97 CPM, control to KO); inhibitory MTNR1B has 0→2 and astrocytic MTNR1B 0→2. MTNR1A is 2→0 in excitatory and 1→1 in inhibitory pools. ARNTL falls from 60.60→52.19 CPM in excitatory and 34.51→26.12 in inhibitory pools, and rises from 46.53→59.28 CPM in astrocytic pools. This analysis has one pooled library per genotype and no replicate animal estimate. Detection depends on assay depth. None of these measures establishes receptor protein, localization, intrinsic oscillator change or concentrations in the suprachiasmatic nucleus or pineal gland. [Assigned nuclear counts](nuclei.tsv)

Repudi's methods report mixed C57BL/6J–129Sv background for the conditional lines. The congenic C57BL/6J study shows that introducing CBA/CaJ alleles of Aanat and Asmt restores rhythmic pineal melatonin production. Mixed background and absent matching pineal or plasma measurements leave the endocrine phenotype of the WWOX cohort undetermined. A controlled timing experiment needs an endogenous melatonin measurement or verified background in each comparison. [Repudi et al., Methods, mouse model](https://doi.org/10.1093/brain/awab174) · [Zhang et al., congenic line](https://doi.org/10.1111/jpi.12509)

## Decision and reproduction

Keep a formulation-specific sleep hypothesis for WWOX with documented insomnia or sleep fragmentation. Park melatonin as an antiseizure or metabolic-rescue candidate for unselected pediatric WWOX. Reopen the direct neural hypothesis for preserved or improved functional output within the same vigilance state and clock phase, plus measured exposure and a mechanistically informative respiratory comparison. [Quantitative external evidence and disposition](exposure_and_disposition_20261126.md)

Run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY` from this folder. Source file identities and checksums are in the [held input manifest](../creatine/inputs.tsv). Use each model's native scale and the mean log2(1 + abundance) contrast for omission. Repository accessions are [mouse cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682), [mouse hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681), [human organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) and [nuclear pools](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684).
