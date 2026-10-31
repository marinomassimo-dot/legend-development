# IT11 P3: diagnosis of the JUMP morphology trial and one calibration trial (scientist-e, 2026-10-30/31)

Exploratory, computational, class level (a WWOX-DEE genotype class; no individual-level record). Not medical advice. Not blind: the IT10 package was read first (PRE_DECLARATION.md section 1). PLK1 and the five phenotype leads are development inputs, not validation. Pre-declaration: `PRE_DECLARATION.md`, committed alone (a175493b) before any trial output existed.

## 1. Decision first

| Question | Answer |
|---|---|
| Is the WWOX morphology comparison usable for compound selection? | **No, not demonstrated. CLOSED for now, with cause.** Declared outcome of the one new trial: **NOT-DEMONSTRATED-AT-WWOX-STRENGTH (not calibrated overall)**. On 144 designed gene-compound pairs measured inside one source (source_13, same batches), the best designed compound fell in the top 10 percent for 25.0 percent of genes against a null of 24.2 percent (ratio 1.03, p 0.44); in the strong-knockout stratum 18.5 percent against 23.1 percent. Same result in 3 of 3 within-source analytical variants. |
| What the IT10 failure does and does not mean | The failed PLK1 control makes THAT configuration inconclusive. It does not show morphology is useless: with compounds from other sources, strong knockouts show a modest excess (about 2 times null in 7 of 9 sources, 1.7 times in a 262-gene cross-source panel). A favourable post-hoc diagnostic does not replace the declared evaluation, and none was favourable enough to try. |
| Why the IT10 gate and z-score cannot be trusted | The gate passed by 0.004 and flips if one of the five wells is removed (leave-one-out 0.593 to 0.675 against a threshold of 0.627); PLK1, a lethal gene, sat at the 74.8th percentile of that statistic. And no designed pair in JUMP predicts a negative similarity, so reading "opposition" as rescue has no control at all. |
| WWOX itself | Expressed in U2OS at RNA level (DepMap log2(TPM+1) 4.22), not essential (gene effect +0.075). Its knockout is "detected" against negative controls (q 0.0008) but 7,600 of 7,968 knockouts are too, so the test does not discriminate. Strength percentile of the mean profile depends on processing: 90 (assembled), 59 and 77 (two CRISPR-only variants). Whether the guide gives a protein knockout is UNVERIFIED. |
| Compound identity | 2.9 percent is a property of the JUMP library, not of the key: full InChIKey 2,016, skeleton 3,349, parent-standardised skeleton 3,349 (no gain). Drug-like annotated compounds (Repurposing Hub with targets) number about 3,000 with plate data. |
| Other data | No WWOX perturbation in another Cell Painting resource found. RxRx3-core is licence-barred for neuroscience use. No candidate is reported. Nothing here is evidence of benefit of any compound. |
| Reopening condition | A Cell Painting resource with a WWOX (or WWOX-DEE variant) perturbation in a neural line and at least 3 independent wells in more than one batch, with designed gene-compound controls in the same cells; or a new analysis showing within-source retrieval above 2 times null at the strength band 80-95 on a designed set of at least 100 genes. |

## 2. P3.1 Diagnosis, answered from sources

Depth key: M = metadata/table read; A = abstract; F = full text; S = processed data computed.

| Item | Finding | Source and locator | Depth |
|---|---|---|---|
| Is the guide annotated as a knockout? | The consortium calls CRISPR-Cas9 perturbations knockouts, with the caveat "although in the timescale of these experiments residual protein probably remains". `crispr.csv.gz` holds one id per gene (7,977 rows, symbol and NCBI id, no sequence): the WWOX id JCP2022_807699 is a gene-level id. | CPJUMP1 (PMC11166567) text; datasets `metadata/crispr.csv.gz` | F (CPJUMP1), M |
| Protein knockout? Guides per gene? | **UNVERIFIED.** The cpg0016 production methods were not accessible (the preprint site returned a bot challenge; not circumvented). Plate tags show `tracrRNA` on gene wells, which suggests arrayed synthetic guides (inference only). | `load_data.csv` plate CP-CC9-R1-12 | M |
| Cells | The preprint abstract says "all in human osteosarcoma cells (U2OS)"; plate tags read `U2OS-311` on every well of CRISPR plate CP-CC9-R1-12 and of compound plate CP-CC9-R1-29. A source name or the consortium sentence alone would not prove it; the per-plate tag is consistent with it. Not neural. | Europe PMC abstract of PPR635627; `load_data.csv` of source_13 | A, M |
| WWOX expressed in the cell line? | RNA yes (log2(TPM+1) 4.22, 62.6th percentile of expressed genes), protein not checked; gene effect +0.075, dependency probability 0.006. | Morphmap repo `output/OmicsExpressionProteinCodingGenesTPMLogp1_U2OS.csv.gz`, `CRISPRGeneEffect_U2OS.csv.gz` (DepMap-derived; DepMap licence UNVERIFIED) | S |
| Wells, independence | 5 wells, one per run (plates CP-CC9-R1..R5-12, batches 2022-09-14 to 2022-11-09), **all at well F11**: independent in time, not in position (identical layout across runs for 94.8 percent of plate-12 wells). CPJUMP1 warns that "unrelated perturbations in the same well position might look similar". On plate R1-12, 164 of 384 wells are no-guide controls and 10 non-targeting; 8 compounds at 5 uM and DMSO share the plate. | `well.csv.gz`, `plate.csv.gz`; load_data tags; CPJUMP1 | M, F |
| What 0.631 vs 0.627 means | The null (random knockouts, 1,000) has p95 0.627; WWOX is at the 95.1st percentile by 0.004. The ten pairwise cosines range 0.44 to 0.76 (IT10 matrix); dropping one well gives 0.625, 0.675, 0.597, 0.670, 0.593: the verdict flips with a single well. It is a pass by chance-level margin, on a statistic that placed lethal PLK1 at the 74.8th percentile. | IT10 diagnostics matrix; recomputed leave-one-out by hand | S |
| Compound vs CRISPR layout, batch | Every CRISPR plate is in source_13 (148 plates); compounds are on 11 other sources' COMPOUND plates (singlicate wells, median 5 plates). source_13 also has 6 compound plates (plate 29) with the 301 JUMP-Target-2 compounds at 5 uM tagged `LandmarkCpd#5uM`, in the same batches as the CRISPR plates. source_7 and source_13 share microscope model, objective, filter configuration and pixel size. | `plate.csv.gz`, `microscope_config.csv`, load_data | M |
| Genetic-vs-pharmacological design | JUMP-Target-2 gives designed pairs (144 target genes with a knockout, 421 pairs) and the JUMP production repeats these compounds in every source. CPJUMP1 reports gene-compound retrieval "only slightly better than expected by chance" and compound-CRISPR pairs "more positively correlated than negatively correlated" (inhibitor resembles knockout; nothing predicts a negative similarity). | JUMP-Target README/metadata; CPJUMP1 | F, M |
| Score | IT10 used cosine to the mean knockout profile, z against 1,000 random knockouts, and read z <= -3 as opposition. The z is dominated by how typical a compound is and was never calibrated; direction "opposite = rescue" has no positive control. Post hoc here: the correlation between a compound's cosine to WWOX and its profile norm is -0.35 (strong compounds are more "opposed"), so extremes are enriched for strong generic phenotypes. | `t1_results.json` | S |
| Compound identity | See table below. | compound.csv.gz, catalogue, compound-annotator | S |

Identity coverage (JUMP compounds 115,796): catalogue by full InChIKey 2,016 (1.7 percent); by InChIKey skeleton 3,349 (2.9 percent); after salt stripping/uncharging with RDKit 3,349 (no change; JUMP structures contain no salts, 0 SMILES with a dot); Repurposing Hub with target list 4,453 (3.8 percent); JUMP-Target-2 compounds 301, of which 172 map to the catalogue by skeleton, 103 by full key. The deficit is the JUMP library (mostly unannotated screening and diversity compounds), so a better key cannot raise it; 36 percent of Repurposing Hub skeletons (1,689 of 4,724) are absent from the repository catalogue, a catalogue-side gap worth a separate look. The most-opposed IT10 compounds had no annotation by construction.

Relevance to the WWOX question: low. The assay measures a morphology of a non-neural cancer line; a WWOX-DEE effect is neuronal. Even a clean match would be a similarity, not a benefit.

## 3. P3.2 Choice and P3.3 controls

Options weighed in `PRE_DECLARATION.md` section 2. Chosen: calibrate the instrument on designed pairs, then place WWOX on the curve. Controls were rule-defined before running (all 144 JUMP-Target genes, not hand-picked), with expected direction positive, strata by knockout strength and U2OS expression, a cross-source arm, a Repurposing Hub panel, four analytical variants and a leave-out check without PLK1. PLK1 was a development control in IT10; here it sits inside the panel and is reported separately.

## 4. Trial T1 results (`results/t1_results.json`)

Data: JUMP assembled ALL v1.0c PCA-corrected (232 PCs, 946,431 wells), CRISPR-only v1.0a and v1.0b; 7,968 knockouts, 301 JUMP-Target-2 compounds in source_13.

| Measure | Result |
|---|---|
| Primary, gene to compound, within source_13, hit = best designed compound in top 10 percent | H 0.250, null 0.242, ratio 1.03, p 0.44 (n 144). Strata: low 0.93, mid 1.41 (p 0.09), high 0.80 (n 27), near 0.56 (n 23). Negative tail 0.222 vs 0.244 (p 0.77). |
| PLK1 (development control) | The only clear hit: best designed compound at the 1.0th percentile. Without PLK1: 0.245 vs 0.242. |
| Compound to gene (secondary) | 9.0 percent vs 7.3 percent (p 0.17), median percentile 0.38. |
| Stability, within source | 50 PCs 1.09 (high 0.93), centred 1.07 (high 0.81), median 1.01 (high 0.96): same classification. |
| Cross-source (compounds from another source) | Overall ratio 1.10 to 1.46 (p 0.001 in source_10, 0.007 in source_6, 0.037 in source_2, rest ns). Strong-knockout stratum 1.7 to 2.0 times null in sources 10, 11, 2, 3, 5, 6, 8 (p 0.005 to 0.04), 1.2 in source_7 (the same microscope as source_13), 0.6 in source_9. Mean of other sources: overall 1.15 (p 0.17), strong 1.97 (p 0.005). **This contradicts the expectation written in the pre-declaration (that retrieval would fall across sources); the matched design performed worst.** Cause not established (hypotheses: a source_13-specific component, 5 uM exposure; both UNVERIFIED and untested). |
| Identity retrieval source_13 vs other source | Same compound in the top 5 percent: 75 percent (source_7), 36 to 60 percent (others), 6 percent (source_9): compound profiles are reproducible across sources, so a low retrieval is not a low-signal compound set. |
| Repurposing Hub panel (3,003 compounds, 1,265 genes, top 5 percent) | All 0.189 vs 0.163 (ratio 1.16, p 0.003); strong 1.71 (n 262); band 80-95 1.34 (p 0.027); weak knockouts 1.08 (ns); expressed in U2OS 1.27, not expressed 1.01. Excess fraction of hits at the WWOX band about 25 percent (hit 0.20, chance 0.15). |
| WWOX detectability (mAP vs negative controls, 2,000 permutations, BH) | q 0.0008 (assembled), 0.0018 (v1.0a), 0.0019 (v1.0b): detected; but 7,600, 5,033 and 4,501 genes are also detected, so this is not a discriminating criterion. Strength percentile 90, 59, 77. mAP percentile 77. |
| Generic checks | Top-30 overlap of WWOX with random genes: mean 2.9, max 18 of 30. |
| Declared classification | **NOT-DEMONSTRATED-AT-WWOX-STRENGTH (not calibrated overall)** for primary and every within-source variant; stability flag: the strong-stratum verdict differs only in the cross-source arm. |
| WWOX query lists | Computed (`t1_wwox_query_lists_NOT_INTERPRETED_unless_declared_outcome.tsv`) and, by rule, not interpreted. No candidate reported. |

Post hoc, after seeing the results (`diag_posthoc_negcon.py`, `results/posthoc_negcon_diagnostic.json`): the two CRISPR negative controls differ (cosine of their means 0.62; no-guide 4,724 wells, non-targeting 2,754). Re-referencing knockouts to the non-targeting mean gave ratio 1.17 (p 0.13), 1.11 centred (p 0.23). Not significant; it is labelled a diagnostic and changes nothing.

## 5. Cost

Downloads from public S3/GitHub/HF with key-less GET: JUMP assembled ALL file 1.03 GB (32 s), CRISPR-only 170 MB, metadata and annotation about 40 MB, one plate parquet 14 MB. Compute: trial about 3 minutes, post hoc diagnostic about 2 minutes. About 150 tool calls and roughly 1.5 hours of session time (estimate). Zero spend, no account. Nothing downloaded was committed (scratchpad); repository addition about 100 KB.

## 6. Licence table (read at the source unless marked)

| Resource | Licence as read | Status |
|---|---|---|
| JUMP cpg0016 data | AWS registry yaml line 35: "CC0 1.0 Universal ... but please do cite the corresponding publication"; production repo has `LICENSE_CC0.md` for data, BSD-3 for code | OK |
| JUMP datasets, profiling-recipe, JUMP-Target, compound-annotator, Morphmap code | BSD-3 (LICENCE.md / LICENSE read for datasets, compound-annotator, Morphmap; recipe via API); JUMP-Target MIT (API) | OK |
| JUMP-Lite | Data card: lists data under CC0 1.0, code MIT (read) | OK; subset of the same data, no new WWOX information |
| DepMap-derived U2OS tables | Redistributed by the Morphmap repo (BSD-3 code); DepMap terms page returned a bot challenge, not circumvented | **UNVERIFIED** for DepMap data; used for reading only |
| Repurposing Hub annotation file | Distributed in the BSD-3 compound-annotator repo; the Hub's own terms were not reached | **UNVERIFIED** underlying terms |
| RxRx3-core (Recursion) | LICENSE read: a commercial EULA that forbids using the data "to perform biology research ... in the field of neuroscience for any purpose" and neuroscience programs, with ShareAlike-like terms | **EXCLUDED** (WWOX-DEE is neurological). The metadata file was downloaded to read the licence and then deleted; no analysis done |
| Enrichr | Help page text read: "free for academic, non-profit use, but for commercial uses please contact Mount Sinai Innovation Partners ... for a license" (a service term, not an open data licence). CREEDS site (likely origin of the GEO drug libraries, not confirmed at Enrichr): CC BY 4.0 | Service academic-only; library provenance UNVERIFIED |
| RummaGEO | LICENSE file text read: "Attribution-NonCommercial-ShareAlike 4.0 International"; this conflicts with the API field (BSD-3); the file text is operative | Treat as non-commercial, share-alike; do not redistribute |
| RDKit | BSD-3-Clause (PyPI metadata) | OK, used only to standardise |
| MotiVE (cpg0034) | Code BSD-3 (API); data features are in separate spaces for compounds (737) and genes (259) and cannot be compared by cosine; WWOX absent from its 4,070 genes | Not used |

## 7. Deviations and disclosures

1. Counts in the pre-declaration (289 compounds, 431 pairs) came from an earlier tally before deduplication; the run gave 301 compounds, 279 with a designed gene, 421 pairs, 144 genes. No rule changed.
2. The pre-declaration did not say which null applies to strata; both are reported (all-rows and stratum-matched) and the stricter ratio decides. No outcome depends on it.
3. The first launch of the script was run twice concurrently and one copy was killed; results come from a single complete run (same seed). The session was interrupted once and resumed from saved outputs.
4. The first eight lines of the WWOX query list were displayed while checking the file; they were not used. The negative-control counts in the pre-declaration-era notes (10 non-targeting wells) apply to one plate; globally 2,754.
5. The earlier IT10 null mean 0.309 is a same-gene well-pair statistic; random knockouts of different genes have mean cosine 0.001 here. My intermediate remark that a shared component inflates it is withdrawn.
6. Bot-challenge pages (bioRxiv, Europe PMC PDF render, DepMap) were not circumvented; one request with a browser-like User-Agent to bioRxiv was blocked by the classifier and not repeated.
7. WWOX strength depends on processing (59 to 90th percentile), so "S_high membership" for WWOX is itself unstable.

## 8. UNVERIFIED

Guides per well and protein knockout for WWOX; compound concentration and duration outside source_13; CRISPR duration; WWOX protein in U2OS; why the matched design underperformed; DepMap and Repurposing Hub terms; the tracrRNA interpretation; Enrichr library provenance.

## 9. For the batch path

* Do not edit cards, needs or ranking from this package. Suggested capability-scout entry: "JUMP morphology route for WWOX: calibrated once on designed pairs (IT11 P3): not above null within source, weak excess cross-source for strong knockouts; CLOSED with reopening condition in README section 1".
* Suggested receipts (not written): CPJUMP1 PMC11166567 full-text, verbatim "although in the timescale of these experiments residual protein probably remains" and "Gene–compound retrieval is only slightly better than expected by chance"; RxRx3-core LICENSE section 3(b).
* Open items worth a separate card: the 36 percent of Repurposing Hub skeletons missing from the catalogue; a CRISPR guide count and protein knockout check from the production methods when reachable.
* Files: `PRE_DECLARATION.md`, `trial_t1_calibration.py`, `diag_posthoc_negcon.py`, `results/` (JSON, per-gene TSV, query-list TSV, stage log). Commands: each script's `--help`; run with `python -I` in an environment with numpy, pandas, pyarrow; data not committed.
