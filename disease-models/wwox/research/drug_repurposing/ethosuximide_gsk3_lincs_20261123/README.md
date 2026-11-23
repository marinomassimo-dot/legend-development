# Does ethosuximide produce a GSK3-inhibitor-like response at 10 µM?

**Decision, 23 November 2026.** The two validated 24-hour cell contexts give no reproducible broad response meeting the prespecified criteria. Keep the 100–700 µM neural WNT observation as a priority for targeted replication. The 10 µM data narrow its interpretation: a strong, general GSK3-inhibitor-like transcriptional response across these cell types is unsupported. In PC3 cells there is a partial association that depends on the comparator. All samples used here are ordinary human cancer cell lines. [Prior neural analysis](../ethosuximide_wnt_fate_20261123/README.md) · [Frozen landmark test](prediction.md) · [Broad LINCS deposit](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742)

## Direct observations

The deposited dataset contains one 10 µM ethosuximide consensus at each condition (four, three and three underlying instances). Of the original WNT markers, AXIN2, NKD1 and APCDD1 are absent, while LEF1 is inferred. We used the 978 directly measured landmarks and SB-216763 as a chemical reference matched for cell line, dose and time. The two endpoints were the correlation across all landmarks and half the difference between the mean responses of the 20 reference-induced and 20 reference-repressed genes. Both had to be positive and above their respective 95th percentiles. A held-out inhibitor with a distinct chemical identifier had to pass before interpreting the test. [Primary platform study](https://pubmed.ncbi.nlm.nih.gov/29195078/) · [Replicate counts, structures and signature quality](results/profiles.tsv) · [Direct marker coverage](results/markers.tsv)

| Cell and time | Ethosuximide correlation | Ethosuximide signed score | What the reference controls permit |
|---|---:|---:|---|
| MCF7, 6 h | +0.009 | −0.070 | Neither held-out inhibitor passed both criteria. Uninformative for excluding a response. |
| MCF7, 24 h | −0.094 | −0.056 | GSK-3-inhibitor-IX passed both full and plate-matched backgrounds. CHIR-99021 passed the full background and missed the signed-score plate threshold. |
| PC3, 24 h | +0.139 | +0.491 | GSK-3-inhibitor-IX passed both backgrounds. Ethosuximide passed the correlation threshold alone. |

The primary random-background test and the follow-up enumeration of all eligible chemicals gave the same decisions. In PC3, 100/5,293 full-background chemicals and 3/358 on the ethosuximide plate had a correlation at least as large as ethosuximide. For the signed score, the corresponding counts were 447/5,293 and 37/358. These are ranks within a perturbation screen. They do not measure independently replicated gene effects or directly quantify enzyme activity. Ethosuximide's inter-replicate concordance metric in the deposit was 0.12 at MCF7 6 h, 0.24 at MCF7 24 h and 0.35 at PC3 24 h. [Random background](results/scores.tsv) · [All eligible controls](results/scores_all_chemicals.tsv)

**Does the PC3 result survive changing the GSK3 inhibitor?** When GSK-3-inhibitor-IX supplied the reference, the full-landmark PC3 correlation with ethosuximide was +0.194. A larger raw correlation ranks lower against this reference: 1,267/5,293 chemicals and 48/358 plate-matched chemicals reached it. The signed score was −0.023. SB-216763 itself failed the reverse-reference signed-score criterion in PC3, limiting the portability of the 40-gene panel even across inhibitors. Thus the original high rank is contingent on the chemical reference. Compound-specific actions, growth state, dose and batch can all contribute. [Post-primary rule](cross_reference.md) · [Swapped reference results](results/reference_swap.tsv)

## Relation to WWOX and next decision

The prior RNA result in a single neural library was a selected, early response at 700 µM, and a separate stem-cell study used 100 µM. The present concentration was 10 µM, shared with the earlier negative nuclear β-catenin screen. Cell type, exposure and phenotype all differ. To determine whether ethosuximide affects WWOX biology through this route, an independent neural exposure series should relate early signaling changes to nuclear β-catenin, subsequent target transcription and surviving cortical-neuron yield in matched deficient and corrected cells. A positive in the cancer lines would have informed breadth. Their results leave the direction and efficacy in WWOX neural tissue open. [Earlier nuclear assay and direct cortical comparison](../ethosuximide_wnt_fate_20261123/README.md)

## Reproduction

Use the GSE92742 Level 5 COMPZ.MODZ matrix with 473,647 signatures and its matching gene, perturbagen, signature and metric files. Decompress the GCTX into the same folder. The deposit includes a SHA512 manifest for the compressed matrix, beginning `6a3115cf3aaa402b`. The deposited consensus z values already reflect the study's controls and processing. The analysis retains distinct compound names within condition, excludes named compounds and their matching connectivity identifiers from backgrounds, and uses the median if there is more than one eligible signature for a compound. “Plate” here means the prefix of the signature identifier; a composite reference can span more than one prefix. All percentiles are descriptive. No raw matrix is redistributed. [GEO files](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742) · [Metadata checksums](results/metadata_inputs.tsv)

```bash
python3 analyze.py GSE92742 results
python3 analyze.py GSE92742 results --all-controls
python3 analyze.py GSE92742 swapped_results --all-controls --swap
```
