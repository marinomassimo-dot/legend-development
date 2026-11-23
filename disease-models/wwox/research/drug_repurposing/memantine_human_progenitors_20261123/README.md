# Memantine in human neural progenitors – a donor-held-out test

**Research decision, 23 November 2026.** The six-hour, 10 nM exposure in this human progenitor screen produced no reproducible transcriptional response across held-out control donors by our frozen rule. The independent WWOX organoid comparison even changed direction when the genes were selected in the other discovery donors. A developmental rescue claim based on this signature would be unfounded. The result is informative at this exposure and developmental stage. It leaves activity-dependent effects in more mature neurons open. [Readhead et al.](https://doi.org/10.1038/s41467-018-06515-4) · [GEO superseries](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119291)

## Direct exposure, independent donors

The original supplementary table lists 24 memantine-treated neural progenitor lines. We recovered gene expression for 21, including 11 designated controls and ten schizophrenia lines. The three remaining profiles were assigned to plate MSA208 in the authors' workbook; the public GEO superseries lists MSA201 through MSA207 for this phase, and the MSA208 GEO search yielded no record. The workbook supplies a schizophrenia-specific summary score for each line, which cannot replace its gene measurements. All 21 available lines had 11–12 same-line, same-plate vehicle wells. There was one memantine-treated well per line. The dose was 0.01 µM for six hours, one seventieth of the separate mouse cortical 0.7 µM exposure. Different concentrations, compartments and times make these separate questions. [Study workbook, Supplementary Data 1](https://pmc-oa-opendata.s3.amazonaws.com/PMC6200740.1/41467_2018_6515_MOESM3_ESM.xlsx) · [Basal mouse cortical test](../memantine_cortex_20261123/README.md)

From the 978 assayed landmark probes explicitly marked LM by the supplier, 957 mapped unambiguously through Entrez and HGNC; 938 distinct mapped genes were also present in the WWOX organoid table. We excluded all probes flagged as inferred on the platform. For each drug well, we subtracted same-line median vehicle expression. Using just six control donors, we selected ten increased and ten decreased genes, then applied the locked panel to five different control donors. The WWOX values were not used for selection. [Platform](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL25480) · [Prospective prediction](prediction.md)

| Contrast in held-out control donors | Memantine, primary split | Memantine, swapped split | Trichostatin A, primary split | Trichostatin A, swapped split |
|---|---:|---:|---:|---:|
| Donors with positive score | 3/5 | 3/6 | 5/5 | 6/6 |
| Median up-minus-down score | +0.003 | +0.007 | +1.858 | +2.179 |
| Matched pseudo-vehicle 95th percentile | +0.852 | +0.612 | +0.145 | +0.148 |

The apparent memantine contrast fell from +0.901 in its six discovery donors to +0.003 in the held-out donors. Its planned negative arm actually rose by +0.056 in validation. Against the two nearest vehicle wells the held-out median was −0.298, while against same-row controls it was +0.346. The drug occupied a fixed area of every plate. Neither position check supports a stable effect. Each concentration was originally selected for this screen; direct engagement of NMDA receptors at 10 nM in these cells was not measured. [Held-out results](results/validation.tsv) · [All donor contrasts](results/donors.tsv) · [Prospective positional sensitivity](plate_position.md)

## Two checks on how much the assay can tell us

Trichostatin A was a positive control on the same plates. Selecting its first well by well coordinate gave one treated well per line, as for memantine. Under the same gene-selection and donor-splitting method its learned transcriptional response validated in both splits. Thus the study can reveal a large, cross-donor response despite the one-well-per-donor comparison. The magnitude of a histone deacetylase inhibitor response does not set a detectable minimum for memantine. [Plate control results](results/plate_positive_control.tsv)

The study independently sequenced methylparaben- and loxapine-treated progenitors. Memantine was absent from that sequencing arm. In a separate calibration for methylparaben at 10 µM, five exact clone identifiers had matched treatment and control in both assays. Across the common expressed landmarks, rank correlations of treated expression ranged from 0.47 to 0.55 and those of vehicle expression from 0.46 to 0.52. Correlations of **treatment-induced changes** were much smaller, from −0.057 to +0.147. Baseline agreement between platforms provides limited assurance about subtle drug effects. These calibration rows are exploratory, use different donors across comparisons and are not an independent experiment on memantine. [Sequencing arm](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119290) · [Paired calibration](results/cross_platform_control.tsv)

## The apparent disease reversal fails its control

Applying the first discovery panel to four untreated WWOX-knockout and two control organoid libraries gave a drug-up minus drug-down contrast of **−0.398**. Both arms rose, and the value remained within the expression-matched decoy interval (−0.457 to +0.264). Changing discovery donors produced **+0.206**. The first direction alone might be mistaken for disease reversal. Its failure to reproduce across donors prevents that inference. No cell or organoid here received both WWOX perturbation and memantine. [Disease-side scores](results/disease.tsv) · [Organoid study](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243)

## Reproduction

The two scripts use standard Python 3 and NumPy. Download GEO series matrices GSE119282–GSE119289 into PLATES (the first is a drug-negative plate), the platform's full text record in SOFT format, the HG-U133A annotation, the authors' first supplementary workbook, the organoid count table and complete HGNC mapping from the laboratory cache. For the methylparaben control also provide the GSE119290 series matrix and gene-count table. The deposited expression values are already log2 transformed. The code joins the accession columns exactly, parses each metadata cell individually because vehicle columns omit the dose field, and preserves distinct donor lines. Only original scripts and computed results are distributed.

```bash
python3 analyze.py "$PLATES" "$WORKBOOK" "$GPL25480" "$GPL96" "$HGNC" "$WWOX_COUNTS" results
python3 calibration.py "$PLATES" "$WORKBOOK" "$GPL25480" "$GPL96" "$HGNC" "$WWOX_COUNTS" "$RNA_MATRIX" "$RNA_COUNTS" results
```

[Input hashes](results/sources.tsv) · [RNA-seq input hashes](results/rnaseq.sha256) · [Public well matching](results/design.tsv) · [Selected genes](results/panels.tsv) · [Landmark coverage](results/coverage.tsv) · [Individual pseudo-vehicle results](results/vehicles.tsv) · [HG-U133A annotation](https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL96/annot/GPL96.annot.gz)
