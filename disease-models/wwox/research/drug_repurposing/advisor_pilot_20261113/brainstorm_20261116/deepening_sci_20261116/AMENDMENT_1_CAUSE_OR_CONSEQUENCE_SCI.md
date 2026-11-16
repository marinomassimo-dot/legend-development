# Amendment 1 to the candidate [4] pre-registration: outcome of the dataset selection rule and the readout for sorted data, written and hashed BEFORE any expression value of any seizure-model series is opened (SCI, 2026-11-16; non-canonical; hypothesis; mechanism level; not medical advice)

Written for: ADV, HE, IT. Base file: `PREREGISTRATION_CAUSE_OR_CONSEQUENCE_SCI.md` (sha256 1d4baaae0292a7bdced6d926c4119413246d8c914c7c603121799af88b22ac21; landed on main in commit 2b5d55c23 before this amendment). What I opened since: **series metadata only**, from the NCBI E-utilities and the series-matrix header files on the NCBI FTP host (no web page, so no interactive challenge); no count file has been downloaded. The metadata copies are in `files/deepening_downloads/` (gitignored).

## 1 · Application of the rule (read from series metadata; nothing else)
| Series | Design as stated in its metadata | Rule result |
|---|---|---|
| GSE319769 (HE's first candidate) | intra-amygdala kainate vs intra-amygdala saline, mouse ipsilateral hippocampus, bulk RNA-seq, time points **3, 7 and 14 days** (the authors call 14 days "chronic"); 6 per group per time point; raw counts file | **FAILS criterion 3** (the latest time point is 14 days, the rule requires at least 21 days or a stated spontaneous recurrent seizure phase). Not used for the primary test. Read afterwards as **secondary**, labelled "authors' chronic, 14 d, fails the rule" |
| GSE330624 | intracortical kainate vs NaCl (sham), mouse right hippocampus, FACS-sorted **NeuN+ (neuronal) and NeuN- (glial) nuclei**, RNA-seq (SMART-Seq v4), 1 h, 24 h and **3 months**; 3-month groups of n=4 per fraction (each sample pools 2 animals); counts as an R `.rds` file | **Qualifies**: sequencing-based; mouse hippocampus with intact Wwox; 3 months after the insult; controls in the same series; n=4 per group; downloadable without a challenge. Not bulk tissue (criterion 1 allows a sequencing-based method; the sorting is stated in the readout below) |
| GSE50079 | pilocarpine vs saline control (and a ketogenic-diet arm), rat dorsal hippocampus, bulk mRNA-seq on an older platform, observation period 84 days with continuous monitoring; counts txt file | **Qualifies** (chronic by the stated 84-day observation; n=3 per group; rat symbols needed) |
| GSE72402, GSE122228 | (HE's metadata) controls not stated; array | not used (criteria 3 and 1) |
| GSE241219 | pilocarpine CA1, 6 to 72 hours only | fails criterion 3 |
Ranking among qualifying series (rule: larger chronic-phase group, then stated control, then earlier accession): **GSE330624 first** (4 v 4 per fraction), **GSE50079 second** (3 v 3). The primary test is GSE330624; GSE50079 is a **second, independent-system** test (different species, model and decade) read after the first and reported beside it, never pooled.

## 2 · Readout for sorted nuclei (fixed now)
The base file defines C = log2(mean chronic / mean control) on bulk tissue. GSE330624 gives two fractions per animal-pair, so, before any value is seen:
1. C is computed **per fraction** (NeuN+ and NeuN-) from the counts, normalised by library size (counts per million of the genes shared by all samples of the fraction), log2 of (CPM + 1) used for the mean, the 3-month samples only.
2. **Primary fraction per gene.** NeuN- for the glial/astrocytic genes **Gfap, Gja1, Kcnj10, Adk, and the reactivity marker Aif1**; NeuN+ for every other gene of the 25 panel (Gabrd, Gabra5, Gabra1, Gabrg2, Slc6a1, Npy, Npy2r, Sst, Pvalb, Gad1, Grin2b, Grin2a, Cacna1h, Cacna1i, Hcn2, Slc12a5, Slc12a2, Kcnk2, Kcnq2, Adora1). Wwox is reported, not scored. The other fraction is reported beside each gene as secondary.
3. The 'readable' rule (|C| at least 0.4), the comparison with the S-line hippocampus value from `ww1_panel.tsv`, and the count criterion are as in the base file. Sign predictions and the 0.55 count probability are unchanged and now apply to the primary fraction of each gene.
4. **Uncertainty.** n=4 per group makes single-gene calls weak: each C is given with a bootstrap 95% interval over the 4+4 samples (10,000 draws, seeded), and a gene whose interval includes both 0 and the S-line value is 'not separable', as in the panel classification.
5. For GSE50079 (rat): the same C on CPM of the 3 pilocarpine-standard-diet against the 3 control samples; the ketogenic-diet arm is not used; rat symbols are mapped by symbol case-insensitively and a gene with no match is reported unmapped.

## 3 · What I name as limits before the data
Sorted nuclei remove most of the composition problem of bulk tissue (the base file's main limit) and add others: nuclear RNA is not whole-cell RNA; pooled pairs reduce between-animal variance estimates; NeuN- is a mixture of glial types; the S-line values are bulk TPM at P17. A match or a mismatch of sign is a transfer test of a hypothesis generator, not a mechanism.

## 4 · Tooling note (not a rule change)
The counts of GSE330624 are an R `.rds` object and no R is installed here; I read the serialisation with a short pure-Python reader (`read_rds_matrix.py`, no package installed), and I check it by reading the sample names and matrix dimensions against the series matrix before any gene is looked at.
