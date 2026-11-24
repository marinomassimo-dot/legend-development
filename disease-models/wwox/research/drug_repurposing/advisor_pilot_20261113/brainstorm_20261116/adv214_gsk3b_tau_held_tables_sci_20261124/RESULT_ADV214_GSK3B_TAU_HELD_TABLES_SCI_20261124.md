# RESULT ADV-214 (SCI window AB): the GSK3B-Tau limb, one held-table search

Hypothesis level; reference genotype class; no dose, no treatment recommendation, nothing is medical advice. Pre-registration frozen at `PREREG_ADV214_TIME_UTC.txt` (SHA-256 in `PREREG_ADV214_SHA256.txt`, commit 5633a49fb) before any table was opened for GSK3B, Tau or phospho content. No delegate, model call, spend, contact or new source (one plain Europe PMC title lookup of the parent studies of swept files). Files: `sweep_adv214.py` and `sweep_hits.tsv` (the frozen sweep), `sweep_study_titles.json`, `rna_posthoc_adv214.py` and `.tsv` (post hoc, labelled).

## Answer first
**Disposition (b), with the searched-tables list of (c) so nobody repeats it.** No held table holds a protein-level phospho measurement of GSK3B, its substrates, Tau sites or its upstream regulators in WWOX-deficient material. Every WWOX-deficient table that carries the listed genes is RNA-only or total protein. The limb stays parked, and lithium's single in vivo result keeps its present reading: seizure suppression in all three genotypes including wild type, with no test of on-mechanism action.

## Per-table verdict (frozen pass rule: WWOX-deficient vs control; phospho-protein readout; at least three independent units per arm; species, tissue, age stated; not the withdrawn densitometry)
| table | material | listed genes present | verdict |
|---|---|---|---|
| GSE158682 | mouse cortex, neuron-restricted deletion (by table name), 4 control / 3 KO, bulk TPM | yes (transcripts) | RNA-ONLY |
| GSE158681 | mouse hippocampus mutant, 2 control / 3 KO, bulk TPM | yes (transcripts) | RNA-ONLY |
| GSE156243 and the organoid differential lists (three supplement tables of the organoid study) | human WWOX-knockout cerebral organoids, 15 weeks, 2 control / 4 KO | yes (transcripts; differential lists are thresholded, so absence of a gene is uninformative) | RNA-ONLY |
| GSE158684 | mouse hippocampal nuclei, one pooled specimen per genotype | features list and matrices (transcripts) | RNA-ONLY |
| Zeng 2024 Table S1 (held as files/i18_proteome) | human neural stem cells, WWOX-silenced vs control, 2031 proteins, total protein | GSK3B and PPP2CA present; Tau and every phospho-site absent | **PROTEIN-TOTAL** (fails readout (ii); replicate structure not read here). GSK3B total log2 fold change +0.02 (BH-adjusted p 0.92) and PPP2CA +0.05 (0.44): total GSK3B protein unchanged, which agrees in direction with the literature-level statement that total GSK3B is unchanged and says nothing about phosphorylation |
| P47T hypomorph supplements (prefrontal cortex and cerebellum sheets) | mouse, differential RNA lists | MAP1B only | RNA-ONLY (thresholded list) |
| files/supplement/GSE158681_GSE158682_r2b | the two bulk TPM tables again | as above | RNA-ONLY (no new content) |
| Drosophila orthologue study supplement | fly, spot-identification table of a two-dimensional gel | none of the listed genes (the phospho hit was phosphoglycerate kinase) | ABSENT |
| Wwox-null mouse chemistry supplement; neuronal-migration table | mouse | none (the phospho hit was serum phosphorus; MAP2 is a label) | ABSENT |
| the remaining studies with token hits (about thirty) | WWOX appears only as a gene row in genome-wide tables of unrelated studies (hypertension GWAS, glioma, NCI-60, HTRA1, ASO guidelines and others; titles in the json) | yes, as rows | not WWOX-deficient material, fail (i) |
Sweep numbers: 121 tabular files with a token hit across 37 studies and 3 non-study folders; the frozen cap of 40 files was exceeded, so I classified by parent study (titles looked up) and opened the files of every WWOX-deficient study, a deviation from the cap rule that costs no coverage. The phospho-term token was too loose (it matches RPS9 and phospholipid); I did not rely on it, and every WWOX-deficient file was opened by hand.
Not searched, by the PREREG limits: figure images, PDFs and prose, in which the one primary that reports GSK3B and Tau immunoblots in WWOX-deficient material (and the withdrawn densitometry) lives. Those are literature-level readings already made in the Chang NCKU wave 1 and 2 analyses; I did not repeat them.

## Post hoc: bulk RNA direction of the frozen genes (not pre-registered; transcript only)
GSK3B transcript is nearly flat in all three bulk sets (mouse cortex -0.28, mouse hippocampus -0.20, human organoid +0.04 in mean log2(1+x), KO minus control). Mouse sets show many neuronal-signalling transcripts lower together (cortex MAPT -0.66, AKT2 -0.89, MAPK10 -0.74, CDK5R1 -0.58; hippocampus MAPK10 -1.24, MAP2K1 -1.12, DPYSL2 -0.67), as expected if oligodendroglial and neuronal composition changed (ADV-210 showed the composition sensitivity of such mouse signs) and not as evidence about phosphorylation. The human organoid values here use raw counts, which ADV-210 showed overstate the KO-minus-control delta by roughly 0.4 (depth), so only large human values (AXIN2 +0.94, CTNNB1 +0.61, MAP2K1 +0.62) mean anything, and even those cannot be read as kinase activity. Conclusion: the RNA tables neither support nor contradict a GSK3B-Tau limb.

## What lithium's result means now
RP-026's single laboratory, single provoked-seizure assay found suppression in wild-type, heterozygous and knockout animals alike. With no phospho-protein datum held, nothing separates a GSK3B-mediated effect from the general anticonvulsant action of lithium, so the result stays "not shown to be on-mechanism". This disposition does not weaken the GSK3B-docking claim itself; it says that no held table tests the limb.

## Minimum assay that would move the limb (hypothesis level, from the literature-level conflict)
Material: WWOX-deficient neuronal tissue or cultures from the existing hypomorph or knockout (juvenile), or knockout organoids, with matched controls; at least three animals or lines per arm (the unit named in the report, not sections or wells). Readouts: phospho-specific quantification, as a phospho-to-total ratio, of **GSK3B pY216 and pS9 together** (the source warns that pS9 alone gives a false negative), Tau pS396 and pS404, a substrate independent of the S9 route (CRMP2 pT514 or beta-catenin pS33/37/T41), and AKT pS473 for the S9 route. Add a lithium-versus-vehicle arm in wild type and knockout to read RP-026 and a docking-motif-mutant control. Wave 1 also points to JNK and MEK inhibition (the better-evidenced lever on this axis in the earlier analysis); a phospho-JNK and phospho-ERK readout in the same samples costs almost nothing extra.

## Searched, so nobody repeats it
Everything in the table above and in `sweep_hits.tsv`; the frozen directories were files/supplement, files/figures, files/reach_audit_downloads, files/deepening_downloads and files/i18_proteome; the gene and site lists are in the PREREG and the script.

## Second deliverable
`NOTE_SHARED_ANCHOR_SCI_20261124.md` (the measurement most of the 58 dossiers wait for, which assay could supply it, who holds a system in the held record).

## What surprised me
The single protein-level table that exists for WWOX loss in the held material is a total-protein proteome in which GSK3B does not move; the whole GSK3B-Tau limb, which ADV-213 scored first, rests on literature-level immunoblots and no held table can test it.

Limits: tabular files only; classification by parent study; the sweep tokens matched loosely; replicate structure of the proteome not read here; transcripts read without normalisation for the human set.
