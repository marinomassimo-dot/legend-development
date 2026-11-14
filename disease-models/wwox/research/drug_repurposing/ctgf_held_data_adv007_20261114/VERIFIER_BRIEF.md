# Verifier brief — ADV-007, blind check of a CTGF/CCN2 reading in held data (2026-11-14)

You are an independent verifier (legend-delegate). Do not start agents. No network, no download, no contact with anyone, no e-mail address or other contact identifier to any service. Not medical advice. Everything you read is held in the repository or in the gitignored `files/` of the main checkout (`/home/desktop/legend-development/files`; read only, write nothing there). Write only under `verify/` of this folder.

## The question the producer was asked

Do the WWOX-loss expression data already held show CTGF/CCN2 moved in the KO direction consistently, and does the signal survive the declared composition and maturation confounds? Per table: direction, effect size, confound status. Conclude with one of: (a) consistent and not composition-explained; (b) inconsistent or composition-explained; (c) not assessable because the confound flags were never computed for this gene.

## Stage A — before you open anything in `output/` or any `*.py` of this folder

Read the originals yourself and write `verify/stage_a.md`: your own per-table reading and your own verdict, with the numbers you computed and how. The held tables are:
- Human organoid WWOX KO v WT (4 v 2 libraries): `files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz`; the authors' lists in `disease-models/wwox/research/drug_repurposing/gse156243/derived/` (`list_padj_le_0.05.tsv`, `symbol_validation.tsv`, `query_sets.json`); gene is listed there under its older symbol.
- Composition and maturation: `disease-models/wwox/research/drug_repurposing/signature_it23_20261103/composition_class.tsv` and the script `reproduce_dseqr_cmap_comparison.py` that wrote it; the calibration set `files/geo/GSE150123/` (62 samples, six iPSC lines, 25 to 650+ days) with the committed estimators in `gse156243/maturation_calibration.py` (read it; you may import its functions).
- Mouse P17 bulk TPM tables (transcript rows): `files/supplement/GSE158681_GSE158682_r2b/`; the committed per-gene summaries `wwox_data_it24_p4_20261104/results/` and `verification_it27_p1_20261104/results/`. The Ensembl cDNA map that turned transcripts into genes is not held; say how you would handle that and what it limits.
- Mouse P47T knock-in: `verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz`.
- Mouse snRNA pools, one per arm: `files/geo/GSE158684/`.
- Human NSC shWWOX CAGE: `files/geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz` (its own control failed in progenitors; read `disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/README.md` section 2, row O6).
- Cell-type origin: `files/geo/GSE73721/GSE73721_Human_and_mouse_table.csv.gz`.

Things to settle yourself: what the gene is called in each table; whether each contrast has replicates and whether animals or libraries separate; whether the composition flags in `composition_class.tsv` for this gene were computed or are blanks; and whether the maturation and cell-composition confounds can account for the size of any rise.

## Stage B — only after `verify/stage_a.md` is written

Open `output/` and the two scripts `ctgf_organoid_maturation.py` and `ctgf_mouse_celltype.py` of this folder, re-run them (`python3 -I <script> run ...`, usage with `--help`), and write `verify/verdicts.tsv`: one row per claim in `output/` and in the table you reconstruct, with columns `claim`, `my_stage_a_value`, `producer_value`, `status` (CONFIRMED / NARROWED / CONTRADICTED / UNVERIFIABLE), `note`. Then `verify/report.md`: your verdict (a, b or c) and where the producer's reading is stronger or weaker than the data. Report what could change the verdict, and anything you could not check, as such. A claim you cannot reach the original for is UNVERIFIABLE, not unsupported.

Keep what you read in the original apart from what you infer. Report model and effort you ran under in the last line of `verify/report.md`.
