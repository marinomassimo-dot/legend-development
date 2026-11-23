# Ganaxolone, interneuron axons and the placement of myelin

**Decision, 23 November 2026.** Keep internode length and myelinated branch points as discriminating measurements for a future ganaxolone experiment. The available Wwox RNA data give insufficient support for promoting ganaxolone as a modifier of this process. A change in fast-spiking interneuron markers occurred in both affected brain regions, but the same panel varies with normal development and acquired epileptic injury. None of the Wwox preparations in this analysis received ganaxolone. [Prospective criteria](prediction.md) · [Specificity challenge](comparator_prediction.md)

## Why examine axon geometry?

A GABA-A modulator can influence the firing of a developing interneuron as well as GABA signaling in an oligodendrocyte precursor cell (OPC). The two routes can predict different structural outcomes at the same level of seizure suppression. In a separate genetic mouse model, removing the GABA-A γ2 subunit in OPCs disrupted myelin placement on fast-spiking axons. The primary studies distinguish this phenotype from global oligodendrocyte production. The direction of a developmental subunit deletion does not predict the direction of a positive allosteric modulator in Wwox loss. Ganaxolone can act through several receptor assemblies. [Balia et al.](https://pubmed.ncbi.nlm.nih.gov/28795438/) · [Benamer et al. and source data](https://pmc.ncbi.nlm.nih.gov/articles/PMC7555533/) · [Direct ganaxolone receptor pharmacology](../ganaxolone_developmental_history_20261123/README.md)

## What the controlled manipulation establishes

We extracted per-cell values from Benamer et al., figures 1–2. Five control and three OPC-γ2-deletion mice contributed cells. The source spreadsheet omits cell-to-mouse identifiers. We enumerated every assignment of cells to the stated number of nonempty mouse groups and calculated the contrast giving equal weight to mice. The bounds below describe these observed cells under all such assignments. Sampling uncertainty in animals remains unknown. [Allocation rule](geometry_bounds.md) · [Results for all five endpoints](results/geometry.tsv)

| Axonal measurement | Cells, control / deletion | Control → deletion, cell means | Difference | Possible difference after equal mouse weighting |
|---|---:|---:|---:|---:|
| Mean internode length | 8 / 9 | 32.23 → 55.65 µm | +23.42 µm | +10.90 to +41.48 µm |
| Branch points covered by myelin | 7 / 7 | 4.17% → 40.00% | +35.83 percentage points | +18.17 to +50.50 points |
| Mean node length | 7 / 8 | 2.03 → 3.56 µm | +1.53 µm | +0.81 to +2.60 µm |

## Is the relevant receptor detectable in Wwox-deficient OPCs?

The P17 hippocampal nuclei comprise one pooled library per genotype. Of the 242 control and 352 mutant nuclei assigned to OPCs, 53 and 77 respectively contained transcripts from α, β and γ2 GABA-A subunit classes together. Of these, 51 and 73 also carried a neuronal marker. Restricting the analysis to nuclei with two OPC markers and no detected neuronal marker left 43 and 50 nuclei, respectively. These contributed only 3 and 5 γ2 molecules, below the ten-molecule floor in either pool. Triple detection survived in 2 and 3 nuclei. The strict selection excludes most assigned OPCs, so both dropout and co-isolated neuronal RNA matter. Purified normal mouse OPCs independently expressed Gabrg2 (4.16 and 3.23 FPKM, compared with 20.48 and 27.78 in neurons). The data support baseline plausibility and leave receptor protein assembly, location, function and disease-related changes unmeasured. [WWOX single-nucleus deposit](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684) · [Purified neural cells](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52564) · [Nucleus counts](results/lineage.tsv) · [Purified-cell values](results/purified.tsv)

## Does the Wwox tissue signal distinguish this mechanism?

We compared the mean log2(1 + expression) of Pvalb, Kcnc1 and Kcnc2 against that of Gad1, Gad2 and Lhx6 within each sample. In P17 neuronal Wwox deletion the mutant-minus-control shift was −0.509 in cortex (3 mutant, 4 control) and −0.965 in hippocampus (3 mutant, 2 control). All single-animal omissions retained a decrease beyond the prespecified 0.25-unit floor in both regions. Tissue composition, neuronal survival and maturation all contribute to this measurement. [Cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Genes and omission ranges](results/fast_spiking.tsv)

The fixed panel rose by 0.540 units in healthy developing mouse forebrain from P14 to P28 (four samples per stage). After kainate, it fell relative to time-matched saline by 0.649, 0.267 and 0.307 units at days 3, 7 and 14 (six per arm at each time). All injury contrasts stayed negative after single-sample omission. These comparisons use each study's own expression scale and controls. They show that a delayed developmental state or acquired injury can generate the direction seen in Wwox tissue. Neither measures axonal structure. [Developmental series](https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-6798) · [Injury series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE319769) · [Development results](results/development.tsv) · [Injury results](results/injury.tsv)

## Observation that would change the decision

Measure internode length and branch-point coverage on identified fast-spiking axons in matched WWOX-deficient and isogenic control preparations with vehicle and ganaxolone. A structural modifier hypothesis requires a reproducible pretreatment geometry difference and a genotype-dependent shift toward the control distribution at comparable firing, maturation and overall myelin abundance. A firing-matched comparator and conduction timing along the same axons would help distinguish indirect seizure control from local structural improvement. A direct OPC mechanism would additionally require that selectively interrupting neurosteroid-sensitive signaling in OPCs attenuate the structural response while neuronal firing remains matched. Neither histology in an unrelated knockout nor the disease RNA profiles establish these effects.

## Reproduction and reuse

From this directory run the following against the laboratory cache of public inputs. The morphology workbook is the authors’ source data file, `41467_2020_18984_MOESM4_ESM.xlsx`. Results are original recalculations, including the missing-assignment bounds. No raw article, image or expression matrix is redistributed. [Benamer et al.](https://doi.org/10.1038/s41467-020-18984-7) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · [Input checksums](results/inputs.tsv)

```bash
python3 geometry.py source_data.xlsx results
python3 lineage.py /path/to/legend/files source_data.xlsx results
python3 comparators.py /path/to/legend/files results
```
