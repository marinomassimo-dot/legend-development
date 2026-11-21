# ADV-162 addendum 1: pre-registration of ONE coarse stage-level correlation of the public WWOX-KO organoid bulk set onto NeuRoDev's compact pseudobulk columns (SCI successor Y, 2026-11-21; hypothesis level; no dose; no contact; not medical advice)

Fixed BEFORE the first correlation was computed. Read when this was written: the NeuRoDev compact tables for WWOX and five marker rows only (WWOX, GAPDH, SLC17A7, GAD1, MBP, SOX2, GFAP, PDGFRA); the query count table's header, row count and first rows (35,337 genes; columns cko1 to cko4 and cwt1, cwt2); the GEO family file (WiBR3 hESC line, cerebral organoids by the Lancaster and Knoblich protocol, age 15 weeks, CRISPR WWOX knockout against age- and batch-matched wild type; 4 KO and 2 WT samples kept after quality control).

## What this is and is not
It is a coarse stage-level and subclass-level correlation of one public bulk set against the pooled pseudobulk columns of three reference networks, in plain Python. It is NOT a NeuRoDev mapping: `mapNetwork` works on cluster signatures, a correlation-based network embedding, the 15 nearest reference clusters, a mapping confidence and the package's own normalisation, none of which can be reproduced from the compact tables; the reference columns here are pooled marginals (a stage or a subclass across studies and across the other axis), not clusters. Any result carries the label "coarse correlation".

## Method (fixed)
* Query: `GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz` (held in the repository tree, files/geo/GSE156243), gene symbols as rows; CPM per sample; log2(CPM + 1). The unit is the SAMPLE (organoid replicate: 2 WT, 4 KO, one engineered hESC line, so one line, not a line replicate).
* Reference: the stage pseudobulk and subclass pseudobulk tables, each of the three networks, taken as log-normalised pseudobulk (assumed log2(CPM + 1); a uniform scale or offset does not change a Pearson correlation of centred profiles).
* Genes: symbols present in both; keep genes with mean query log2 CPM of at least 2 across the six samples (a fixed expression floor).
* Centring: reference row mean across all columns of the same table is subtracted from every reference column and from every query sample (the reference's own frame; no centring on the query set).
* Similarity: Pearson correlation across genes, per sample against each reference column.
* Outputs per sample: the best three subclasses and the best three stages in each network; the same for the mean of the 2 WT and of the 4 KO samples (descriptive).

## Prediction and the "no information" outcome (fixed)
* **P-A (plausible, 15-week cortical organoid):** in the corticogenesis network the best subclass of every one of the six samples is a progenitor or early-neuron class (cRG, RG, IPC, miEN, imNIT, eEN, imIT) and the best stage is prenatal (stages 1 to 5 of the table).
* **P-B (WT and KO nearly the same at this resolution):** the best subclass and the best stage are the same for WT mean and KO mean; any KO-minus-WT difference in the correlation to a subclass is reported as descriptive (n = 2 against 4, one line).
* **NO INFORMATION:** if the best subclass of the six samples is a mature glial, immune or interneuron class (Astro, Oligo, Micro, SST, VIP, PVALB, LAMP5) or the best stage is postnatal in any network, or if the correlation spread between the best and the tenth reference column is below 0.05 for any sample, then the coarse correlation cannot place the organoids and I state that it carries no information; no identity or stage is then inferred. A correlation also cannot show a cell class is ABSENT from a bulk sample (no composition test: the "no interneuron cluster" item stays untestable by bulk).
* No inference about any WWOX effect on identity: with 2 against 4 samples, one line and pooled marginal columns, a KO-versus-WT shift is a descriptive observation only.

## Consumer
ADV (whether a mapping step on public data is feasible; the answer feeds HE's ADV-163 assessment of R and the package).
