# D-galactose · UDP-Gal supply, Golgi access and terminal processing

26 November 2026 · SCI_CODEX · opening checkpoint · P17 mouse cortex and hippocampus and week-15 human bulk organoids, with pooled P17 hippocampal nuclear UMI counts

The prior D-mannose study found reasons to separate N-site occupancy from maturation of the glycans already attached there. D-galactose interrogates terminal extension more directly. The working question is whether an experimentally measured rise in UDP-Gal can restore specific terminal Gal residues despite altered Golgi organization. The one task in progress is D-galactose. [D-mannose disposition](../d_mannose/neural_site_checkpoint_20261126.md) · [Prespecified D-galactose question and panel](pretest_20261126.md)

## WWOX data

Five of 15 prespecified targets decreased in all three bulk datasets and at every one-library omission. Effect values are KO minus control in mean log₂(1 + abundance), using transcript-summed gene TPM in mouse and per-million processed counts in human. Cross-tissue signs are descriptive and the organoid libraries share lines. [All 45 contrasts](contrasts.tsv)

| Target | P17 mouse cortex | P17 mouse hippocampus | Human week-15 bulk organoids |
|---|---:|---:|---:|
| GALK1 | −0.24 | −0.70 | −0.39 |
| SLC35A2 | −0.65 | −0.79 | −0.16 |
| B4GALT2 | −0.61 | −0.75 | −0.39 |
| COG4 | −0.59 | −0.51 | −0.07 |
| COG6 | −0.33 | −0.16 | −0.86 |

The cortical GALK1 omission range comes close to zero and the organoid COG4 difference is small. B4GALT1 rises in human bulk (+0.85) while falling in mouse cortex (−0.32), consistent with the need to measure actual terminal glycoforms and possible enzyme compensation. In pooled P17 hippocampal nuclei the assigned excitatory SLC35A2 signal moves **11.64 → 12.08 CPM** (144→125 UMIs at different pool depths) and inhibitory signal **12.11 → 13.86 CPM** (20→26 UMIs). Assigned astrocytes move **25.32 → 22.66 CPM** (37→39 UMIs). GALK1 changes **3.39 → 3.38 CPM** in excitatory cells. B4GALT2 falls in that class (**9.94 → 7.73**, 123→80 UMIs) and rises in inhibitory cells (**4.84 → 9.60**, 8→18 UMIs). C1GALT1 and COG6 both have lower CPM in all three of those classes. One pooled control and one pooled knockout and low counts in several classes limit cell-type attribution. The comparison weakens the idea of a uniform neuron-intrinsic loss of SLC35A2. [Nuclear counts, all assignments](nuclei.tsv) · [GSE158684](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684)

## Discriminating prediction

In a stage- and lineage-matched WWOX experiment, use separated Gal-1-P, UDP-Gal and UDP-Glc concentrations and label fractions with an orthogonal lumen-access readout and same-cargo Gal maturation. Under a **galactose activation limit**, labelled Gal-1-P and subsequent UDP-Gal formation remain blunted at comparable external substrate. Under a **Golgi delivery limit**, cytosolic labelled UDP-Gal increases at comparable Gal-1-P but lumen access is reduced relative to a corrected comparator at the same donor level. Under a **transfer or trafficking limit**, donor delivery is preserved and the specified glycoforms or coatomer localization stay abnormal. A shift in labelled fraction with no increase in absolute mature glycoform output would represent carbon-source substitution in that assay.

Use Tn-to-core-1 extension for O-GalNAc and occupied-site terminal galactosylation for N-glycans. Check a glycosphingolipid readout independently when present. A primary SLC35A2-CDG fibroblast study reported small N-/O-linked protein changes with larger lipid glycosylation defects and direct Gal incorporation into improved lipid biosynthesis. A protein-versus-lipid dissociation can therefore be informative. Compare against a characterized residual-transport control before assigning an apparent donor rescue to supply. [SLC35A2-CDG tracer study, primary abstract](https://pubmed.ncbi.nlm.nih.gov/40576648/)

## Pediatric precedent and current disposition

The postsurgical MOGHE pilot enrolled **12** people aged **5–28**. Its composite global response was **9/12**, while a seizure-frequency reduction of at least 50% was reported for **3/6** in the seizure-frequency subgroup. Two participants reported abdominal discomfort. This is open-label evidence from an anatomically and genetically distinct epilepsy. A separate uncontrolled pilot enrolled nine participants with PGM1-CDG, with a documented donor metabolism defect. Neither establishes a useful neural exposure or effect in WWOX. [MOGHE pilot, primary abstract](https://pubmed.ncbi.nlm.nih.gov/37278968/) · [PGM1-CDG pilot, primary abstract](https://pubmed.ncbi.nlm.nih.gov/28617415/)

**Active.** The bulk signal spans activation, transport and processing, with the pooled nuclei weakening a shared neuronal transporter mechanism. Next extract the analytical specificity of lipid and O-GalNAc comparators in actual SLC35A2 disease tissue and cells. Check whether the published assay distinguishes Gal-1-P and UDP-Gal isomers and measures Golgi delivery directly or infers it from incorporation. A review may change the next assay if an apparent delivery measurement instead pools whole-cell metabolites. Pediatric WWOX trial priority remains unsupported.

Replay with `python3 -B galactose_screen.py FILES BULK_TSV NUCLEI_TSV`. The same held files and hashes as the D-mannose screen apply. [Inputs](../d_mannose/inputs.tsv) · [Code](galactose_screen.py)
