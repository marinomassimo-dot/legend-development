# L-fucose | Fast release and measured substrate response

27 November 2026 · SCI_CODEX · `context_policy: QUESTION_DRIVEN`. External comparators were selected after the WWOX RNA pretest. This is an active checkpoint.

## Source physiology

**Data.** Di Lucente et al., Results and Figs. 1–2 captions, describe a rapid increase in WT mouse hippocampal fEPSP within 1–2 min. The Fig. 1E paired-pulse ratio falls (reported n=8), and Fig. 1F miniature EPSC frequency rises with mean amplitude unchanged (reported n=16 at the cell recording level). These convergent measures favor greater presynaptic recruitment. They leave the animal-level estimates and release direction in juvenile neocortex unresolved. The Fig. 2A caption reports n=3 WT and n=5 Fcsk-null, alongside eight degrees of freedom for an unpaired Student test. The counts and test degrees of freedom do not reconcile from the caption. Treat this as qualitative FCSK dependence until the allocation and original graph are verified. Bulk fucose-lectin blots were reported unchanged up to five hours (source Results referring to Fig. S6). These are insensitive to some site-specific effects. The manuscript abstract reports increased cerebral tissue free L-fucose after dietary supplementation. This is distinct from the available extracellular concentration during electrophysiology. Exact free-parent units and tissue handling require checking. [Di Lucente primary](https://doi.org/10.1126/sciadv.adt4123)

## Reproducible transcript comparison

| Model | Control and comparison libraries | FUK | FPGT | FUT8 | VAMP1 | STX1B |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| WT hippocampal slices, L-fucose versus aCSF at 5 h | 6/6 | +0.096 | +0.783 | +0.108* | +0.293 | +0.806 |
| Basal 5xFAD versus WT on control diet | 6/6 | −0.154 | −0.016* | −0.200 | −0.190 | −0.157 |
| 5xFAD, one month L-fucose versus control diet | 6/6 | −0.028* | +0.009* | +0.117 | +0.118 | +0.112 |

Values are contrasts of mean log₂(1+posted normalized count). An asterisk marks sign instability under single-library omission. Deposited values are fractional and GEO describes them as normalized counts despite the filenames. The comparison uses no DESeq2 inference and assumes no within-animal pairing. The chronic series lacks a WT-fucose group, so treatment effects cannot be compared across genotypes. The mapped SLC35C1 row is zero in all 12 five-hour columns, limiting interpretation for that gene. FPGT is the strong five-hour signal in this panel. The chronic arm moves FUT8, VAMP1 and STX1B up in 5xFAD while evidence for greater FPGT or FUK RNA is weak. The latter does not dispute a protein result. The 5-hour RNA response follows the 1–2-minute physiological effect and provides no timing evidence about its initiation. [GSE295285](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295285) · [GSE295460](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE295460) · [Replay outputs](external_fucose_rna.tsv) · [Replay script](replay_fucose_comparator.py)

Download the [5-hour CSV](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE295nnn/GSE295285/suppl/GSE295285_Raw_Count.csv.gz) and the [one-month workbook](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE295nnn/GSE295460/suppl/GSE295460_Raw_Counts.xlsx) to the same directory. Run `python3 -B replay_fucose_comparator.py <input-directory>`. Both file digests and the columns are verified. Genes in the short CSV are mapped by matching stable Ensembl IDs to the author-annotated chronic workbook. The result is descriptive at six libraries per group.

## Interpretation and next step

A parallel fast response is plausible even if a delayed core-fucosylation response takes place. The timed distinction needs a chemically specific readout. A WWOX decrease in FPGT RNA could limit GDP-fucose production after initial FCSK activity. FCSK dependence alone would not prove FUT8-dependent incorporation or distinguish fucose-1-phosphate from downstream signaling. Quantify labeled fucose-1-phosphate, GDP-fucose and one normalized core-fucosylated site separately. A release change that precedes site correction and requires FCSK is compatible with a separate salvage-dependent response. Compare metabolite timing to distinguish fucose-1-phosphate and GDP-fucose as candidates. Cell type and brain region constrain transfer. An orthogonal FUT8 contrast could test the requirement for glycan incorporation if native output is present.

Next examine Xu et al. Fig. 1 and Supplement 2 for the tissue and linkage-resolved evidence, compare cerebral total with free/extracellular parent, and audit the pediatric peripheral responder and nonresponder precedents. Test whether fucose restores any persistently low candidate neural site without increasing initial excitation or recurrence. [Xu primary](https://doi.org/10.1016/j.jbc.2023.105513) · [WWOX first checkpoint](salvage_pretest_20261127.md)

[Completed compartment comparison and disposition](compartments_and_disposition_20261127.md).
