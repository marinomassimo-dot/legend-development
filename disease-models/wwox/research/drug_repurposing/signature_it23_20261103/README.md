# IT23 P2/P5: can dseqr turn a WWOX transcriptomic signature into pharmacological proposals?

Non-canonical research material, 2026-11-03. Public edition (WWOX-DEE reference genotype class). **Not medical advice.** A mimic or reverse score is a prompt for a hypothesis, never evidence of benefit, and nothing returned by a LINCS query is WWOX evidence. Zero spend, no account, no key, no e-mail address or personal datum sent anywhere (only HGNC gene symbols, their service entity ids, and integer PubChem CIDs). No author was contacted. Nothing from a third-party table is committed beyond derived compound tables.

## 1. Decision

**REJECT dseqr as a LEGEND route now (reopen condition below). The one query that could run, through the SigCom LINCS public API, adds no compound that LEGEND's current list contains, and under every composition scenario it returns largely the same library-specific compounds that IT2 and IT3 already judged non-specific.**

Reasons, each checked:
1. **dseqr's own data route is dead.** dseqr does not call CLUE or any API (no key, no credential anywhere in the code). It correlates a query against local effect-size matrices that `dseqr.data` downloads from `https://s3.us-east-2.amazonaws.com/dseqr/...`. On 2026-11-03 every such URL, including the bucket root and the three matrices, answered HTTP 404 with XML `Code NoSuchBucket`, `BucketName dseqr`: the bucket no longer exists. Neither repository names another mirror. The matrices cannot be rebuilt: the build scripts read the author's private objects from hard-coded `/home/alex/...` paths (13 files across the two repositories) and the L1000 limma matrix is never shipped. Route failed; stopped, as instructed.
2. **What is separable is tiny.** `query_drugs` (Pearson of the top-200 query genes against each signature) and `query_budger` (mean effect on a chosen gene list) are about 20 lines each, MIT, runnable alone, but they need that matrix. LEGEND already scored the same signature against the full GSE92742 level 5 matrix locally (IT3, 205,034 compound signatures, per-signature nulls and real-contrast controls) and found no compound-level reversal specific to it (`../gse156243/lincs_it3_local_level5_20261027.md` R4).
3. **The substitute pass (below) changes nothing in LEGEND's list.**

**Reopen only if** (a) a restored or mirrored `cmap_es_ind.qs` / `l1000_*_es.qs` appears with a stated data licence, AND (b) a question needs the old CMAP02 (Affymetrix, 1,309 compounds, 2006) or limma effect-size scoring that the local level 5 route cannot give. Neither holds today. A further SigCom pass on another signature is optional and cheap (about 2 minutes, 4 requests), but only once a second independent WWOX-deficient neural contrast exists.

## 2. What was read (item 1)

Commits: dseqr `69a3d2cf` (2026-01-22, version 0.37.0), dseqr.data `d6229b49` (2024-10-21, version 0.99.9). Licences, kept apart: **code MIT** (both); **data: no licence stated** in either repository (the matrices derive from Broad CMAP02 and LINCS L1000; those terms were not re-read here); **signatures returned by SigCom: terms not stated in the API metadata and not read**, L1000 data are public through GEO with citation requested. Function-level table: `dseqr_code_audit.tsv`. Component, URL, version, size and licence table: `assets.tsv`. R is not installed on this machine and dseqr was not executed (an install would still hit the dead bucket).

## 3. What LEGEND already did with signatures (item 2)

| Done | Where | Result |
|---|---|---|
| SigCom LINCS two-sided queries of the organoid KO v WT lists S1/S2/S3/S0 (iteration 1) and matched/shuffled/KO-split nulls (iteration 2) | `../gse156243/`, `tool_responses/`, `lincs_iteration2_interpretation_20261027.md` | rank-1 and rank-2 reversers (estradiol, clozapine) are frequent hitters; a KO split with no genotype contrast reaches the same strongest z-sum; the MCLF family fills both tails; 33 of 76 S1 reversers appear in a null |
| Local level 5 pass, whole matrix, no cap, per-signature nulls | `../gse156243/lincs_it3_local_level5_20261027.md` | S1 survivors (109 reverse, 124 mimic) lie inside the range of real-contrast controls (K1 306, K2 123); verdict: LINCS reversal stays out of the portfolio as a candidate source |
| LINCS shRNA knockdown (WATCH) | `../scout_it21_p6_20261103/` | 10 WWOX knockdown signatures; WWOX is not a landmark gene so the knockdown cannot be seen; 4 of 23 panel genes covered; no observable value |
| Composition confound | `../generation_it22_p1_20261103/p3_B_cellpop`, `p3_D_sweep`, `results_p4` | the hNPC library did not show WWOX lower (second system fails its gate); the organoid is 4 KO v 2 WT; glycolytic genes fall with culture time in 62 unperturbed spheroids; mouse P17 and P47T do not independently support the module; every proposal carries `SECOND_SYSTEM_PROGENITOR_GATE_FAILED` |

**What an additional dseqr/CMap pass could add:** (i) a second scoring rule (Pearson of effect sizes, different from SigCom's z-sum and from IT3's gene-set score) on the same lineage; (ii) CMAP02, a different, older platform; (iii) per-signature heat maps. **What it could not add:** a second independent WWOX contrast (dseqr scores the same organoid list); any control that separates WWOX from composition, maturation or within-KO heterogeneity (K1 already showed this limit); any evidence of benefit; and it shares the LINCS lineage for L1000, so its agreement with SigCom/IT3 would be one vote. The decisive gap is on the input side (one organoid contrast, 4 v 2), not the query side.

## 4. The comparison that ran (items 3 to 5)

**One signature: S1** = GSE156243 WWOX-KO v WT cerebral organoids, week 15, padj <= 0.01 and |log2FC| >= 0.26 (517 up, 317 down). Chosen because it is the only transcriptomic list in the repository that is human, FDR-filtered, authors' DESeq2 output and with a full gene table; the mouse P17 contrasts (GSE158681/2) and P47T (GSE215425) have no gene-level table in `files/geo`, and the hNPC library failed its gate. Its limits: 4 v 2 libraries, mixed populations, a KO not a patient allele. It applies to the questions whose seeds come from the organoid transcript: **Q2, Q4, Q8** (158 proposal rows, all `*_expression_tiersAB` seed sets); Q5 (mouse cytokines) and Q6 (single-cell MYC) are not covered by it.

**Coverage (honest):** 834 query genes; 18 not mapped by the service; 529 in the 12,328-gene L1000 space; **54 are measured landmark genes (6.5 percent)**; 475 are inferred, 305 are outside the space. So about 93 percent of the signature is either imputed by L1000 or invisible to it.

**Route:** SigCom LINCS `enrich/ranktwosided`, database `l1000_cp`, 300 signatures per tail of 693,215 ranked, 5 requests in total (4 in the first wave; a fifth, the broad-class sensitivity, was added after seeing that the primary composition class held only 26 genes; it is declared as a second wave). Rank-1 and rank-2 reversers equal those of 2026-10-22 (estradiol z-sum -16.65, clozapine -16.24), so the service answered reproducibly. Compound identity: PubChem InChIKey by CID, else GSE92742 `pert_info` by BRD id; a compound is one skeleton InChIKey (best signature kept). Not resolved: BRD-K09398529 (the most replicated MCLF compound, 6 signatures in 6 cell lines) and a few BRD-only codes. Cell context, dose, time, tissue, disease and library of the best signature are in `scenarios.tsv`.

**Composition class (analyst choice, declared in the script before the run):** declared markers (16 of the 27 are in S1) union genes with |Spearman rho| >= 0.6 against log10 culture day in GSE150123 (62 samples) and a KO direction equal to "less mature" (10 genes): 26 genes. Sensitivity class: declared markers plus every S1 gene with |rho| >= 0.4 in either direction: 209 genes. Both are crude; a real composition model (cell-type deconvolution) would assign far more genes and was not attempted. Treat "ignore composition" here as a lower bound on how much the class can matter.

**Scenarios** (role of the class assigned to composition; role of the rest):

| Id | Composition class | Rest | Query, tail |
|---|---|---|---|
| S1 | reverse | reverse | all genes, reversers |
| S2 | mimic | mimic | all genes, mimickers |
| S3 | (27 declared markers ignored) | reverse | minus declared, reversers |
| S4 | ignore | reverse | minus class, reversers |
| S5 | ignore | mimic | minus class, mimickers |
| S6 | mimic | reverse | class genes flipped, reversers |
| S7 | reverse | mimic | class genes flipped, mimickers |
| S8 / S9 | ignore (broad class, 209 genes) | reverse / mimic | broad-class-removed query |

**Overlap of the top 20 compounds (Jaccard; full matrix in `overlap.tsv`):**

| Pair | Jaccard | Shared |
|---|---|---|
| S1 v S3 (27 declared markers removed) | 1.00 | 20 |
| S1 v S4 (class of 26 ignored) | 0.91 | 19 |
| S1 v S6 (class mimicked, rest reversed) | 0.74 | 17 |
| S1 v S8 (broad class of 209 ignored) | 0.60 | 15 |
| S2 v S5 / S2 v S7 / S2 v S9 | 0.82 / 0.74 / 0.74 | 18 / 17 / 17 |
| any reverse scenario v any mimic scenario | 0.00 | 0 |
| **any scenario v LEGEND's resolved top 20 (H_HARM or H_PROTECT arm) or v all resolved LEGEND compounds of Q2/Q4/Q8** | **0.00** | **0** |

Reading: removing or flipping 3 percent of the genes barely moves the list; removing a quarter of them (broad class) replaces five of twenty. The selection is therefore driven by the remaining organoid pattern, not by the composition class as defined here; and **the direction choice (reverse v mimic) moves the list completely**, which is the role uncertainty LEGEND already carries as H_HARM v H_PROTECT. No scenario was preferred.

**Against LEGEND (identity by InChIKey, not name):** 115 of the 158 LEGEND Q2/Q4/Q8 rows are DGIdb-only families with no InChIKey in the catalogue, so they cannot be compared by identity at all (a name coincidence column is kept, informational, and is empty). For the 43 resolved rows, **none is in any scenario's top 20.** Looking through the whole returned depth (300 signatures per tail, five queries): two resolved LEGEND compounds appear, **Ve-821** (IT21P2-0117, Q4, H_PROTECT arm) at ranks 247 to 272 of the reverser tail (HELA, 0.37 uM, 24 h, z-sum about -11), and **acalabrutinib** (IT21P2-0063, Q4, H_HARM arm) at rank 175 of the mimicker tail of the broad-class query (HBL1, 10 uM, 24 h, z-sum 9.7). Both lie on the side opposite to the arm they belong to (H_HARM means "oppose the change", H_PROTECT "mimic it"), at ranks the service itself gives no weight, so they neither support nor contradict the LEGEND proposal. Of the LINCS top-20 rows, 8 to 11 per scenario are in LEGEND's compound catalogue by InChIKey (the catalogue is a list of substances, not of proposals; e.g. estradiol, clozapine, sildenafil, quetiapine in S1; entinostat, emetine, zileuton in S2). Entinostat is an HDAC inhibitor, a class LEGEND already carries as HDAC5 proposals, but the identity differs (class overlap, not compound overlap).

**Context limits.** 16 to 18 of the top 20 in every scenario are signatures of the 2021 `MCLF*` library at a fixed 4 uM and 6 h (a Broad library whose cell lines carry no tissue or disease field in the service; neural or not is unknown, not assumed). The remainder are tumour or primary cell lines at 24 h (PC3, VCAP, HELA, HBL1, PHH). No neural line stands out. The bulk organoid mixes radial glia, neurons and non-cortical regional populations (the S1 list holds regional-patterning genes such as SHH, LHX5, OTX2, DRGX), so a signature of composition difference is read as a pharmacological prompt; IT2/IT3 showed that a no-genotype split of the KO libraries yields the same score magnitude and that 43 percent of S1 reversers appear in a null. A z-sum of -16 is a property of the query gene set.

## 5. What this adds and what it cannot (summary)

Adds: a reproducible, scenario-explicit record that the LINCS top 20 depends on the role chosen for the whole signature (reverse v mimic: no overlap) and only weakly on a small composition class; coverage numbers (54 landmark of 834); an identity-keyed comparison showing no top-20 overlap with LEGEND's resolved Q2/Q4/Q8 compounds and two deep, direction-discordant hits.
Cannot: say anything about WWOX specificity, composition (the class is crude), benefit, safety, dose or CNS exposure; compare with the 115 DGIdb-only LEGEND rows (identity unresolved); replace a second independent contrast.

## 6. Files

`dseqr_code_audit.tsv`, `assets.tsv`, `scenarios.tsv` (180 rows: 9 scenarios x top 20, with cell line, tissue, dose, time, library, identity, catalogue and LEGEND membership), `overlap.tsv`, `composition_class.tsv` (per-gene class assignment and coverage flags), `legend_compounds_in_returned_depth.tsv`, `run_facts.json` (coverage, counts, response digests), `reproduce_dseqr_cmap_comparison.py`.

Reproduce: `python3 -I reproduce_dseqr_cmap_comparison.py run <repo_root> <geo_files_dir> <scratch_dir> <out_dir>` (live) or `analyse` (offline from stored responses; the raw service responses stay in scratch and are identified by sha256 in `run_facts.json`). Standard library only.
