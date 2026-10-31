# IT11 P5 (E) targeted scouting from IT10/IT11 gaps (2026-10-30/31 UTC)

Perimeter: key-less GET only (GitHub API, Hugging Face API, Europe PMC, NCBI E-utilities without e-mail or tool parameter, Zenodo, BioStudies, GEO FTP); zero spend; no account; no e-mail or personal data sent; downloads in an own scratch directory, read with `python3 -I`. GitHub unauthenticated search hit its rate limit after about 20 queries and returned poor matches for multi-word phrases, so literature (Europe PMC) carried most of the searching. "Not found" is not "absent". Earlier IT8 scouting (`../scout_it8_20261029.md`, G-a to G-e) and IT10 P24 were reused, not repeated. Code, data, weights and services have separate terms; each row says which one was read.

## 1. Decision

| question | result |
|---|---|
| (1) compact explanation of signed multi-chain scores | **No external resource adds.** Nothing found that decomposes a signed multi-path sum (Europe PMC phrase search "signed network" + explanation: 0 hits; KG-explainability search: 6 hits, none signed). Adopt an internal convention (section 2). |
| (2) benchmarks for signature quality in reversal | **One new WATCH (abstract only); the rest already held.** IT8 ADOPT-as-reading (Lim and Pavlidis), OREVID design TRIAL and P24's pre-registered L1000 benchmark stand. |
| (3) WWOX-loss cellular data in neural cells | **No new neural dataset.** All neural/organoid WWOX deposits found are already in the repository. One new, non-neural, WWOX-null genome-wide CRISPR screen (GSE298081, HAP1): crude check shows no outlier; WATCH. |
| (4) protein-stability regulator resources | **Nothing adopted.** Two WATCH resources; one resource rejected for the Q230P question by domain size. |

## 2. (1) Signed multi-chain scores

| candidate | what it is / read depth | terms | verdict |
|---|---|---|---|
| REx (liseda-lab/REx; IJCAI 2025) | reinforcement-learning search for explanatory paths in an unsigned KG, reward = fidelity, relevance, simplicity; README and licence file read, paper not read | code Apache-2.0 (LICENSE file read); Docker + GPU | **REJECT as a tool** (a learned path search where an exact sum is available). **Idea kept**: fidelity (the chain connects seed to target), relevance, simplicity as three checks on a displayed chain |
| COMIC (BMC Bioinformatics 2026, CC BY), MegaKG, DrugReX | titles/abstract list only | not read | WATCH, UNVERIFIED |
| internal convention (no dependency) | because a score here is an exact signed sum over paths, explain it exactly: (a) net, gross positive, gross negative; (b) cancellation fraction = 1 - abs(net) / (gross positive + gross negative); (c) share of gross carried by the displayed chains and the unshown remainder; (d) whether the dominant displayed chain has the sign of the net; (e) diverging bar of the displayed chains plus one grey "not shown" bar. | none | **PROPOSE** for IT11 P1.1 (the Engine package) to test against its own tables; not tested here |

## 3. (2) Perturbation-reversal signature quality

| candidate | content / depth | terms | verdict |
|---|---|---|---|
| "A comprehensive evaluation of connectivity methods for L1000 data", Brief Bioinform 2020 (PMID 31774912) | abstract only: six similarity methods benchmarked by partial AUC against Drug Repurposing Hub drug-drug similarity; ZhangScore best at signature sizes 10 to 200. Not in the repository before (git grep: 0 hits) | not open access, no licence recorded | **WATCH**: it ranks similarity metrics, not signature quality, and its benchmark standard is drug-drug similarity |
| SSGCN, Protein Cell 2022 (PMID 34677780) | abstract only: compound-perturbation profiles matched to gene-knockdown profiles to infer targets | CC BY | WATCH: the same compound-versus-gene-perturbation matching problem as P24's JUMP trial; no data/code read |
| Lim and Pavlidis 2021; OREVID; glenritschel L1000 benchmark; preprint on consensus-signature similarity bias | read in IT8/IT10 | see those files | unchanged |

## 4. (3) WWOX-loss data in neural cells

| search | result |
|---|---|
| GEO DataSets, WWOX with neural/organoid/iPSC/astrocyte/brain terms: 107 records | the series found are GSE158681/2/4/5 (mouse), GSE215425, GSE156243, GSE126075, GSE229210 (glioblastoma lines, overexpression), GSE36665: **all already in the repository** (git grep) |
| GEO, WWOX with human and knockout/knockdown/CRISPR: 19 | adds **GSE298081 and GSE298085** (Cell 2026, "Global genetic interaction network of a human cell", PMID 42049019, CC BY-NC per Europe PMC): a genome-wide TKOv3 CRISPR screen in WWOX-null HAP1 cells (query line GIN352: guide-edited WWOX, 1 bp and 55 bp deletions, clone c2.2; T0 and 3 late replicates; rich medium). Not neural (HAP1 is derived from chronic myelogenous leukaemia). WWOX is not mentioned in the paper text (0 mentions); the screen is a query line of the network |
| Zenodo "WWOX": 11 records; BioStudies "WWOX": 791 (mostly Europe PMC article records) | Zenodo hits are glioblastoma/breast cancer items and a 2022 WW-domain study (CC BY 4.0), none a neural cell dataset; not read further |
| pathway-term searches without WWOX (HIF/VHL, KEAP1/NFE2L2, complex I, ISR in neurons/organoids; GEO) | 6, 3, 3, 8 hits; titles scanned: no neural loss-of-function series for these axes relevant enough to use; **GSE208530** (Ndufs4 knockout human iPSC and Leigh mouse) noted as WATCH for a complex I comparison (not read). The queries are crude (phrases not found for some terms, e.g. "NDUFAF"); this is a floor, not a census |

Crude check of GSE298081 (`gse298081_wwox_ko_screen_check.py`, output rows in `evidence/gse298081_wwox_ko_top_both_ends.tsv`): per-gene median guide log2 fold change (late vs T0, CPM-normalised) of the WWOX screen against 15 parental-WT screens of other batches in the same matrix (83.7 MB file, SHA not recorded). QC: WWOX-KO and WT agree (correlation 0.946 with the WT mean; leave-one-out WT screens 0.952); ribosomal genes depleted in all (median -1.55 in KO, -1.9 in WT). Genes beyond |z| of 4: WWOX-KO 6 (z below -4) and 1 (z above 4); a leave-one-out WT screen has a median 4 and 7. **The WWOX screen is within the range of WT screens; no sensitiser or suppressor is claimed.** Limits: one clone, batch-unmatched controls, a cancer-derived haploid line, not the authors' genetic-interaction score (their Data S tables were not read), 15 controls only. Verdict: **WATCH**; the next step would be the authors' interaction scores for the WWOX query, one clone and one cell type cannot show WWOX specificity or a neural phenotype.

## 5. (4) Protein-stability regulators

| candidate | content / depth | terms | verdict |
|---|---|---|---|
| Mega-scale stability data (Tsuboyama et al. 2023; HF `RosettaCommons/MegaScale`, 5 parquet groups up to 286 MB) | cDNA-display proteolysis stability for domains of at most 72 aa; HF card read via API | card licence `cc-by-4.0` | **REJECT for Q230P**: position 230 lies in the large oxidoreductase region, far beyond the dataset's domain size. Whether it holds WWOX WW-domain variants (WW domains are within the size range) was not checked: UNVERIFIED, WATCH |
| ThermoMPNN (Kuhlman-Lab; GitHub API) | stability change predictor, trained on the same data; README not read | MIT per API (LICENSE file not read) | WATCH; same size limit applies to its training data, prediction on a larger protein is a model extrapolation |
| UbiNet 2.0 (Database 2021, CC BY): 3,332 verified E3-substrate interactions | abstract read; the web address from the paper returned 404 today | article CC BY; database terms not readable | WATCH: could answer which E3 lists WWOX; unavailable now. (IT10 P23 already handles ITCH from primary papers) |
| "Derailed protein turnover in the aging mammalian brain" (Mol Syst Biol 2024, CC BY) and "Turnover atlas of proteome and phosphoproteome across mouse tissues and brain regions" (Cell 2025, not open, licence not shown) | per-protein brain half-lives could give a WWOX turnover figure; I downloaded the open paper's supplementary files (10 tables and source data) and searched them for the gene name: **0 hits**, so the WWOX value is not in the supplements (the full data are in a proteomics repository, not downloaded) | Mol Syst Biol CC BY | WATCH; no value obtained |

## 6. Adopted / not adopted

Adopted: nothing external. Proposed internal: the explanation convention in section 2. Spend: none. Personal data and e-mail sent: none (Europe PMC, NCBI, GEO FTP, Zenodo, BioStudies, GitHub and Hugging Face GETs carried queries and identifiers only).
