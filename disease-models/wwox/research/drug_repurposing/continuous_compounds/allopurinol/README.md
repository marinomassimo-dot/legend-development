# Allopurinol and endogenous purine retention in WWOX loss of function

**Data scope.** Mouse neuronal-deletion cortex and hippocampus in transcript-summed TPM, human WWOX-knockout cerebral organoids at week 15 in library CPM, and P17 mouse hippocampal nuclei in assigned UMI CPM. External data are isotope percentage in young-adult mouse blood, brain and kidney, neonatal human plasma concentrations and outcome counts, and normalized cell or synapse measures per well in human MPS IIIA cortical cultures.

`context_policy: QUESTION_DRIVEN`. The [fixed panel and competing predictions](pretest_20261126.md) distinguish retention of endogenous purine base from the delivery of exogenous [inosine](../inosine/salvage.md) or [D-ribose](../d_ribose/README.md).

## Held WWOX comparison

| Model, unit and control / KO libraries | XDH, control → KO | HPRT1, control → KO | ADSL, control → KO |
|---|---:|---:|---:|
| Mouse cortex, TPM (4 / 3) | 0.606 → 0.693 | 65.85 → 65.83 | 40.15 → 37.82 |
| Human week-15 cerebral organoids, CPM (2 / 4) | 0.275 → 1.022 | 14.52 → 18.07 | 71.38 → 56.83 |
| Mouse hippocampus, TPM (2 / 3) | 0.432 → 1.842 | 70.25 → 45.87 | 26.63 → 20.34 |

XDH is low on the original scales. Its positive contrasts survive all single-library omissions in organoids and hippocampus. The cortical omission range crosses zero. HPRT1 shifts in opposite directions in human organoids and mouse hippocampus. ADSL is lower in all three, with the sign surviving every omission. ADSS2 and PRPS1 are lower in hippocampus with stable sign, and the ADSS2 contrast in organoids crosses zero on omission. These results leave more than one possible limit downstream of the extracellular precursor. They measure expression rather than enzyme activity or fractional salvage. [Full bulk panel](bulk.tsv)

In P17 hippocampal pools, assigned XDH counts were 6 → 4 in excitatory nuclei, 1 → 2 in inhibitory nuclei, 1 → 1 in astrocytic nuclei and 0 → 0 in microglial nuclei. The absence of assigned UMIs in one class does not establish absence of enzyme. The assay pools one library per genotype, and does not localize the increase in bulk XDH. HPRT1 in astrocytic nuclei was 42.43 → 22.08 UMI CPM (62 → 38 assigned gene UMIs), and in excitatory nuclei 31.27 → 25.32 UMI CPM. ADSL fell in excitatory, inhibitory and astrocytic pools. These pools contain no independent replicate animals and are reported descriptively. [Nuclear counts and denominators](nuclei.tsv)

The source references use mouse `Hprt` and `Adss`, and human `ADSS`. The harmonized outputs label these HPRT1 and ADSS2. The mouse FASTA gives two older and overlapping Ensembl IDs to `Pnp`. The common bulk loader sums by source symbol, while the nuclear panel contains ENSMUSG00000115338. A separate ID trace found negative changes for each mouse ID in each bulk region, so the reported bulk direction survives the annotation ambiguity. Cross-assay PNP magnitudes are kept separate. [Mouse HPRT1](https://www.mmrrc.org/catalog/locus_detail.php?mgi_id=MGI%3A96217) · [Mouse ADSS2](https://www.informatics.jax.org/marker/MGI%3A87948) · [Mouse PNP](https://www.ncbi.nlm.nih.gov/gene/18950)

## Decision and replay

Retain as a mechanistic comparator for peripheral precursor retention and separate it from direct neural XOR inhibition. Park for unselected pediatric WWOX trial priority. Reopen for documented local substrate availability with net adenylate and evoked recovery in a matched WWOX preparation. The [source replay and disposition](exposure_and_disposition_20261126.md) tests blood-to-brain transfer, an external human cortical culture signal and the interpretation of neonatal PK/PD.

Run `python3 -B replay_expression.py HELD_INPUT_DIRECTORY OUTPUT_DIRECTORY` from this folder. The [held input manifest](../creatine/inputs.tsv) lists filenames and SHA-256 digests. The original data are [GSE158682](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682), [GSE158681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681), [GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) and [GSE158684](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684). Omission uses the contrast of mean log2(1 + abundance) after removing one library per iteration. The separate PNP sensitivity is reproduced by assigning the transcript keys ENSMUSG00000021871 and ENSMUSG00000115338 separately in the existing `load_target` reader.
