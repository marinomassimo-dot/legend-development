# IT14 p1a: model identity and replicate structure behind GSE158681 / GSE158682 / GSE158684 (SuperSeries GSE158685); is per-library identity of the snRNA nuclei recoverable?

Scientist p1a, task ORCH-ROADMAP-IT14-20261031, branch `task/it14-p1a` (from task/it14), 2026-10-31 (Europe/Rome). Exploratory, non-canonical, **not medical advice**. Reference genotype class only. No contact address, account or personal datum was sent anywhere; GEO contact fields were not used or stored.

## 0. Decision (first)

**The deposit permits one thing and forbids three.** Permits: describing GSE158684 as one Cell Ranger-called nuclear pool per genotype (S-Control 3182 nuclei, S-KO 2920) from hippocampus at P17, for the genetic contrast Synapsin-Cre neuronal Wwox deletion versus a Cre-only (Wwox +/+; Synapsin-Cre+) control, 10x Chromium 3' v3, exon-only reference. Forbids: (1) any replicate statistic across animals or libraries (the files hold no library or animal index and the paper states n = 1 per arm); (2) the words "same animals" for bulk and snRNA (no source says so; write "same genetic contrast"); (3) reading the lower nuclear Wwox in glia as neuron-restricted deletion until it is explained (section 4).

**P1.4 reprocessing is not feasible now, and would not decide the question even if it were.** All 29 SRA experiments of the SuperSeries (SRX9206251-79, including the eight snRNA SRX9206272-79) carry NCBI status `hup` on 2026-10-31: no runs listed, efetch answers "not public", BioSample records come back empty, ENA has a header-only filereport. There is nothing to download, so no download was made. Separately, this host has 4 cores, 15 GB RAM (about 10 GB available), 87 GB free disk and none of cellranger, STAR(solo), kallisto/bustools, salmon, samtools, sra-toolkit or scanpy; and the target counts are too small: PV-class nuclei number 12-19 per arm (IT13b proxy PV-B) so at best 3-5 per animal; an exact conditional test on 14 vs 7 gives p = 0.19, and a Poisson simulation (my quick calculation, animal-to-animal variance ignored, so optimistic) gives about 25% power to detect a 2-fold fall at 14 per arm and about 80% at 50 per arm. Per-animal PV counts from this experiment cannot be had even with perfect library identity.

**Proposed narrowed text for trigger NP3A1** (replaces the IT13b condition; "edits this implies", section 6):
> NP3A1 (nucleus-resolved PV composition in neuronal Wwox deletion): PARTIAL. GSE158684 holds one Cell Ranger-called pool per arm (3182 vs 2920 nuclei); library and animal index absent; paper n = 1 per arm; Pvalb 70 vs 37 UMI, PV-class nuclei 12-19 per arm: undecidable at this power. Raw reads (SRX9206272-79) are `hup` (not public) as of 2026-10-31, so re-aggregation by library is not executable. REOPEN when any of: (a) the eight snRNA SRX leave `hup` (re-query NCBI esummary status) AND the barcode-overlap test in the reads shows at least 3 independent libraries per arm AND at least about 50 PV-class nuclei per arm are recoverable; (b) a deposited library/animal index for GSE158684 appears; (c) per-animal PV immunostaining counts in neuronal Wwox deletion versus Cre-only controls, at least 3 animals per arm; (d) an independent snRNA/spatial dataset of neuronal Wwox deletion with at least 3 animals per arm and a PV-enriched capture. Absence of PV change in GSE158684 is not evidence of no change.

## 1. What I read, at what depth, and what I knew before

* GEO text (series GSE158681, GSE158682, GSE158684, GSE158685; all 8 snRNA GSM pages in full; the 21 bulk GSM pages for title, genotype, SRX, SAMN) via the public `acc.cgi ... form=text` route. Read in full.
* Paper: PMID 33914858 (Repudi 2021, Brain). Operator-supplied OUP print text and supplement File009 (`files/fulltext/`, existing receipt FTR-20260923-33914858-01 and later). I read the Methods "Mice" and "Electrophysiology" sections, the Results paragraphs on neuronal deletion, RNA-seq and snRNA-seq, the Fig 3 and Supp Fig 1 and 4 legends, the Data availability statement, and the supplementary methods for RNA-seq and nuclei/snRNA. Not read: abstract, introduction, discussion (one passage only), the figures themselves (legends only), the xlsx tables. Figure content was therefore not inspected.
* SRA/ENA metadata via public NCBI E-utilities and ENA portal (esearch/esummary/efetch; no scraping).
* Own computation on the six deposited matrices (sha256 verified against the IT13b SHA256SUMS): `identity_checks.py`.
* Known before looking: the IT6 census (Cre drivers from the paper; link GSE158681/2/4 to the paper by identical n), the IT13b result and its flag on glial Wwox. New here: the SRA `hup` status; Cell Ranger cell-calling is the only filter; Y/Xist composition; the GEO-versus-paper conflicts on aggregation and Seurat thresholds.

## 2. Model identity and design (locators in `identity_table.tsv`)

| Item | Established | Status |
|---|---|---|
| S driver | Synapsin I-Cre (Jax 003966); S-KO = Wwox flox/flox (exon 1 floxed); Synapsin-Cre+ | read |
| N driver | Nestin-Cre (Jax 003771), neural stem/progenitor; in hippocampal bulk only | read |
| Expected cell types | Nestin: neurons, astrocytes, oligodendrocytes; Synapsin: differentiated neurons from E12.5 (authors' words) | read |
| Controls | S-Control = Wwox +/+; Synapsin-Cre+ (Cre-only; stated for the electrophysiology cohort, inferred for the sequenced animals). N-Control and WT/null background not stated | read / inferred / not stated |
| Age, region | P17; whole hippocampus (GSE158681), whole cortex (GSE158682, S arm only), hippocampal nuclei (GSE158684) | read |
| Nuclei prep | Dounce, Nuclei EZ, no sorting, no multiplexing or hashing, 10x v3 3', Cell Ranger 3.0.2, exon-only mm10 | read |
| SuperSeries | GSE158685 = GSE158681 (14 GSM) + GSE158682 (7) + GSE158684 (8) | read |
| Replicates, original | bulk: 14 hippocampi (WT 3, null 2, S-Ctrl 2, S-KO 3, N-Ctrl 2, N-KO 2) and 7 cortices (S-Ctrl 4, S-KO 3); snRNA: paper n = 1 per arm, GEO 4 GSM per arm | read |
| Replicates, analysable | bulk: per-sample TPM (transcript level) usable as n = 2-4 per arm; snRNA: one pooled matrix per arm, nuclei are not replicates | derived |
| "Filtered" | Cell Ranger cell calling only; no Seurat filter applied (386+ genes, but 1281/1067 nuclei above 2500 genes, 122/118 above 15000 UMI) | verified |
| Bulk and snRNA same animals | not stated anywhere | not stated |

GEO and the paper disagree on the processing (GEO: cellranger-aggr, Seurat 3.2.0, >=300 genes; paper: separate count per arm, Seurat 3.1.5, 200/2500 genes, 15000 reads, 3% mt). The deposited barcodes are all `-1` and sorted, as one `cellranger count` output would be, not as aggr output (suffixes -1..-4 grouped); the control and KO barcode lists share 4 barcodes (chance expectation about 2-3). Four GSM per arm therefore have three readings the deposit cannot separate: one library registered four times, four animals pooled in one load, or four libraries merged with the suffix removed. Only the reads (cell-barcode overlap across the four SRX of an arm) could separate them, and they are not public.

## 3. SRA feasibility (P1.4)

`samples_sra.tsv`: GSM to SRX to BioSample and SRA status for all 29 GSM. All `hup`. Study-level accessions SRP285667/8/9 and BioProjects are indexed (PRJNA666185 exists) but contain no public run. No hashing, genotype-based demultiplexing or sample multiplexing is described, and the animals are a C57BL/6J;129sv mixed background (a source of SNPs, in principle usable by a demultiplexer, but only from reads). Sex cannot help: both pools are mainly male (Y-linked transcripts in 83% and 81% of nuclei, Xist >=2 UMI in 4 and 0 nuclei). Host: 4 cores, 15 GB, 87 GB free, no extractor or aligner installed; a kallisto/bustools or STARsolo run on a 3' v3 library of unknown depth would need an installation (not done), index memory near the host limit for STARsolo, and hours per library. Because no reads exist, the estimate is qualitative; I did not measure a size or a read count. **Stop at documented feasibility.** Nothing was downloaded or added to `files/`.

## 4. Why glial Wwox falls (2041 to 204 UMI overall)

Per 1e4 UMI (control to KO, `results/wwox_glia_ambient.tsv`): excitatory 0.81 to 0.09, inhibitory 2.24 to 0.30, oligodendrocyte 1.75 to 0.04, astrocyte 2.24 to 0.11. The total fall is mostly neuronal in UMI because neurons dominate the nuclei, but the fold change is deeper in glia (20-44x) than in neurons (7-9x). In control, Wwox per 1e4 in glia is higher than in excitatory neurons while their neuronal ambient (Snap25) is 7x lower, so neuronal ambient RNA does not explain the control glial signal; Wwox-positive glia nuclei carry only slightly more Snap25 (1.4 vs 1.0 and 1.6 vs 1.4 per 1e4) and more depth, which is expected from detection. Rivals, none decided here:
1. **Cre activity beyond neurons** (Synapsin-Cre expressed from E12.5, possibly in progenitors or a glia-fated subset; my background knowledge of known caveats of this transgene is not checked in this package). Test: the Rosa26-tdTomato reporter that all conditional animals carry, co-stained with Olig2/Sox10/GFAP, or sorted-glia genotyping of the floxed exon. Against it: the paper's IF shows intact WWOX protein in CC1+ cells of the corpus callosum (RNA is not protein; one region, no quantification).
2. **Non-cell-autonomous down-regulation** in a seizing, hypomyelinated P17 brain (state-dependent expression). Test: Wwox in a glia-restricted or null-neighbour context; or sorted glia from S-KO.
3. **Pool-level technical difference** (one library per arm, 3.7x different ambient myelin RNA). A uniform technical factor would give the same fold in neurons and glia, which is not seen; a class-specific one is not excluded.
4. **Class calls in the KO pool**: only 70 oligodendrocyte-called nuclei, and immature or mixed nuclei may be called glia. This does not apply to astrocytes (275 vs 281 nuclei, 20x fall).
Bulk context (IT6 own sums of the TPM table, not recomputed here): S-KO whole-hippocampus Wwox TPM 0.3-0.8 against a null floor of 0.3-0.4; compatible with near-complete loss including glia, equally with a neuronal-dominated signal. Consequence for use: S-KO is a neuron-targeted deletion by design and by the authors' protein check, but the RNA data cannot be called neuron-restricted.

## 5. Contrast discipline for downstream use

Neuronal deletion versus Cre-only control, at P17, in a mixed background, in animals that are seizing and about to die (3-4 weeks): transcript differences mix cell-autonomous Wwox loss, activity-dependent change and oligodendrocyte-lineage composition. The Cre-only control removes Cre load as a confound but not litter, sex or the mixed background. Whole-tissue bulk and nuclei cannot be added as replicates (different assay, animal overlap not stated). Marker transcripts are not cell counts, not protein, not function.

## 6. Edits this implies (proposals only; nothing here touches a card, need, ranking, registry, current file, view or ledger)

* `functional_it13_p3a_20261031/reopen_searches_it13_p3a.tsv`, row NP3A1: replace the condition by the text in section 0 (adds: SRA `hup`, power figure, barcode-overlap test, >=3 libraries, >=50 PV nuclei).
* Census (`wwox_data_census_it6_20261029.md`, row for GSE158684): "Cell Ranger cell calling only; Seurat filters not applied; SRA experiments `hup` on 2026-10-31; GEO and paper conflict on aggregation and Seurat settings; four GSM per arm with one matrix per arm unresolved".
* IT13b README sentence "library index lost in the deposit": add "and the raw reads are not public (`hup`)", and soften "the Cre driver is not named in the GEO text" with the paper's Synapsin-Cre/Nestin-Cre statements (already in the IT7 census).
* P3a finding: keep "Pvalb transcript lower, not localisable"; add that glial Wwox also falls in the nuclear pool, so the S contrast is a neuron-targeted design with unexplained glial Wwox loss in RNA.

## 7. What an independent verifier must check (single decisive datum)

NCBI esummary for `db=sra` ids 11991543-11991550 (SRX9206272-79) must still say `status="hup"` with empty `Runs` (the reopening trigger is that status changing); then, if reads appear, whether the four SRX of an arm share cell barcodes. Recompute `results/deposit_prefilter_qc.tsv` (minimum genes 386/390; 1281/1067 nuclei above 2500 genes) and `wwox_glia_ambient.tsv` from the six files with independent code.

## 8. Limits

* The Cre-expression statements for Synapsin-Cre come from the authors; the transgene's published leak profile was not looked up. The glial-fold analysis uses IT13b class labels (rule-based, not independently verified here).
* The paper's figures and xlsx tables were not opened; the bulk animals per GSM are assumed, not stated.
* The power numbers are a Poisson approximation and optimistic.
* `receipts_proposed/` holds a proposed receipt with the coverage actually had; I did not write the ledger.

## Files

`README.md`, `identity_table.tsv` (22 rows, locators and depth), `samples_sra.tsv` (29 GSM), `identity_checks.py` (exec bit, `--help` safe), `results/{deposit_prefilter_qc,sex_genes_by_arm,wwox_glia_ambient,sra_experiment_status_esummary}.tsv`, `receipts_proposed/FTR_proposed_33914858_p1a.json`.
