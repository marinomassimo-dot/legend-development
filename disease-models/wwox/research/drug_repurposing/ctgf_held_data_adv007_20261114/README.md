# ADV-007 — is CTGF/CCN2 moved in the KO direction in the held WWOX-loss data, and does it survive composition and maturation? (2026-11-14)

Non-canonical research material. Not medical advice; no dose, route or recommendation; reference genotype class only. In silico, files already held, no download, no external request, zero spend, no contact. Assignment: ADV-007 of the ADV presidio campaign (`advisor_pilot_20261113/assignments/ADV-007.md`); record `ORCH-ADV007-20261114`. Labels: DATO (read in an original table), INFERENZA (computed or inferred here).

## Answer first

**Verdict: inconsistent or composition-explained.** Not "consistent and not composition-explained", and not "not assessable": the question can be assessed once the flags are computed, and the held data do not show a consistent KO-direction rise that is independent of cell composition.

1. **The one concordant table cannot be separated from a progenitor-state shift (DATO + INFERENZA).** In the human KO organoid (GSE156243, 4 v 2 libraries) CTGF is up: authors' DESeq2 log2FC 1.32, padj 0.00707; every KO library is above both WT libraries (minimum KO / maximum WT 1.53). But in the calibration set GSE150123 CCN2 tracks the progenitor markers within line (R² 0.61 NES, 0.37 VIM, 0.24 SOX2), and the KO organoids carry raised NES/VIM. The composite progenitor-minus-neuronal projection is **+1.21 against the observed +1.15**; single markers range from -0.31 to +1.53 (median +0.26). So a progenitor-state shift of the size the markers show would carry the whole rise. This projects what a shift would carry; it does not show one occurred. With 4 v 2 libraries the exact two-sided permutation floor is 0.13, stated beside the model-based padj.
2. **The mouse tables disagree in sign (DATO).** P17 hippocampus: null deletion DOWN (committed gene level 2.73 v 5.91 TPM, centred log2 -0.77, animals separate, 2 v 3); N deletion UP (9.90 v 5.30, +1.11, animals separate, 2 v 2); S deletion and S cortex not in the committed called lists and animals not separated. P47T (a missense model, Wwox mRNA unchanged): hippocampus +1.60 (raw p 0.0083, padj 0.16), prefrontal -0.27, cortex +0.43, cerebellum +0.10; nothing at padj < 0.05.
3. **The one mouse single-nucleus pair rises 4.5-fold in the pool (31 v 125 UMI) but the pools differ in composition (DATO).** Wwox falls 110 → 12 CPM, endothelial markers rise (Cldn5 9 → 40), Gfap 16 → 41, the oligodendrocyte marker Plp1 392 → 136; 35 of 57 Ccn2+ KO nuclei carry endothelial-marker UMI against 8 of 24 in control. About 2x remains in nuclei without such UMI. One pool per arm: descriptive only.
4. **Cell-type origin (DATO, GSE73721):** CTGF is high in human endothelium (22.8 and 53.3 FPKM), tumour-core astrocytes (median 41.7) and fetal astrocytes (median 5.8); low in adult astrocytes (median 0.4), oligodendrocytes (0.6), myeloid cells (0.4). An organoid has no endothelium, so immature or reactive glia is the plausible source (INFERENZA).
5. **The human NSC CAGE pair is uninformative:** progenitors 181.3 v 173.8 TPM with the deposit's own control failed; neurons 0.80 v 1.42 TPM.

Per-table summary with sizes and confound status: `per_table.tsv`.

## Corrections to the draft's premises (stated before any reading was relied on)

* `composition_class.tsv` line 198 (CCN2): log2fc and rho are blank and every flag is 0. They are **defaults, not a computed clean result**: the generator looks the gene up under the authors' older symbol (CTGF) in a table keyed by the older symbol after the S1 set had been renamed to the current symbol (CCN2). All 15 blank rows (IRAG1, CCN2, DRC4, MNMIP1, POFUT4, MTCL2, ATOSB, HDIP1, BBLN, ADPRS, CIRSR, H1-2, H1-10, H4C15, ZNRD2) are renames (`output/symbol_trace.tsv`, `output/organoid_maturation_ctgf.json`). Computed properly with the same rule, rho vs log10 day over the 62 samples is -0.009 and nothing is flagged — for the wrong reason: the time course is non-monotone (line-centred day-bin means +1.61, -0.36, -1.03, -0.21, +0.91; a 15-week organoid sits near the trough; for day 60 and later the slope turns positive), which a monotone rank rule cannot see.
* `novelty.tsv` of `relations_it23_p2_20261103` has 15 CCN2 rows (not CTGF, which is why a grep for CTGF finds none). They are drug-gene annotation rows (LINCS-derived and CTD-type edges for compounds such as capivasertib, dactolisib, curcumin), not Wwox expression data, and are not used here.
* The SCI51 consumer delta is not pending (consumed by IT50); no precedence conflict.

## What it changes, and does not (decision for the integrator; no consumer was edited)

* **INV-06 row 7** "the Wwox-CTGF link is unsupported": the verdict neither supports nor reverses it. The precise statement the data license is in `consumer_delta.md`; whether to use it is the integrator's decision.
* **X1 arm**: the held Wwox expression data give no ground to name CCN2 as the product. If the positive-control or neutralisation arm names a candidate, the ground is the neuron-specific Tsc literature read in SCI50 (not re-read here), labelled as such.
* **SCI50 DREAM line** (expression check in held data): executed and closed with this reason; no new wet question arises beyond OQ11, which already measures the medium.

## Transfer, and what expression is not

Expression is not secretion; no table here measures a medium, a protein or a conduction readout. The human KO organoid (a mixed, progenitor-rich tissue without endothelium, 15 weeks) is not the neuron-specific Tsc co-culture of the SCI50 literature, and the mouse P17 deletions are other alleles in other tissue. Nothing here is evidence about a patient.

## Verification

One blind verifier (legend-delegate; asked sonnet/high, read back from the transcript sonnet x44 turns, effort high x44), Stage A written from the originals before the producer output was opened (`verify/stage_a.md`), then 32 claims (`verify/verdicts.tsv`): 26 CONFIRMED, 3 NARROWED, 3 UNVERIFIABLE, 0 CONTRADICTED. Its report is `verify/report.md`. The three narrowings were applied before delivery: (1) the single-marker median understated what a combined score projects, so the composite projection is now reported and the "minority" reading dropped; (2) the mouse proxy transcript is unique only inside a 85-100 percent window (three rows at 70-105 percent), so committed gene-level values are quoted wherever they exist and the proxy only for H_S and C_S, labelled a lower bound; (3) the CAGE row, the permutation floor and the meaning of "360; 199" (line positions) were added or corrected. The verifier also found the same verdict independently (its verdict: b on both legs, and (c) only for the shipped flags).

## Limits

4 v 2 organoid libraries from one line (independence of the 4 KO organoids not stated; two other WT libraries failed QC per the GEO design text, as read by the verifier); the calibration is an unperturbed spheroid time course, not a KO v WT contrast, and its between-line interval includes zero; the Ensembl cDNA map is not held, so the P17 S-allele and cortex contrasts for this gene are a transcript proxy; one pool per arm in the snRNA; the verifier's cell-class split of the snRNA UMI is a crude marker-score view (reported, not relied on). Not checked: the paper's own statements on CTGF, clone independence, committed P17 gene-level numbers from the originals.

## What could change the verdict

A replicated organoid contrast with more than 2 WT libraries or independent KO clones; the cDNA map; cluster-resolved snRNA with replicate pools; cell-state markers measured in the same organoid libraries rather than borrowed from the time course.

## Files and reproduce

`output/` (nine tables and two JSON files), `per_table.tsv`, `consumer_delta.md`, `VERIFIER_BRIEF.md`, `verify/`. `python3 -I ctgf_organoid_maturation.py run <out>` and `python3 -I ctgf_mouse_celltype.py run <repo_root> <files_dir> <out>` (both `--help`); inputs are the held files named in `VERIFIER_BRIEF.md`; the calibration inputs are pinned by digest in `gse156243/maturation_calibration.py`.

## Dated corrections (2026-11-15, SCI as package owner, after the IT second read)

IT recomputed three numbers from the held tables and all three matched (GSE156243 log2FC 1.32 and padj 7.07E-03 with 4 v 2 libraries and min KO / max WT 1.53; P17 hippocampus N deletion 9.90 v 5.30 and null deletion 2.73 v 5.91, n 2 v 2 and 2 v 3; the GSE158684 pair recounted from the mtx files, 31 v 125 Ccn2 UMI, 24 v 57 Ccn2+ nuclei, 8 v 35 with an endothelial-marker UMI). Two labelling points came with it. Nothing below changes a number or the INV-06 wording.

1. **Order in `per_table.tsv` row T7.** It replaces nothing in the file; it states what the row already contains. Every figure in T7 that is written "a v b" is **control first, KO second**: 31 v 125 UMI, 24 v 57 nuclei, 1.68 v 7.50 CPM, 3182 v 2920 nuclei, Wwox 110 v 12 CPM, Cldn5 9 v 40, Gfap 16 v 41, Plp1 392 v 136. The other rows of that file, and the T7 `table` column ("S deletion pool v control pool"), are KO-first, so the two orders sit in one row; read T7's numbers as control v KO (output/snrna_ccn2.tsv, where the control pool has 3182 nuclei and 31 Ccn2 UMI, is the source). The 4.5-fold rise in the README (point 3) is KO over control.
2. **The proxy transcript is an inference.** `ENSMUST00000020171.11`, used for the P17 TPM tables (T4, T5 and the per-animal values in T3), was identified by number matching against the four published gene-level means (`output/mouse_proxy_identification.json`: status "inference by number matching, not by annotation"; the proxy is 87.5 to 99.6 percent of the published values, so it is a lower bound). The IT second reader checked only the committed gene-level table (the T3 means 9.90 v 5.30 and 2.73 v 5.91), **not** the proxy identification; the T4 and T5 proxy values and the per-animal values in T3 are therefore checked by the producer and the blind verifier only.
3. **Still unchecked by anyone else:** the composite projection (+1.21).
