# IT18 P4 controls and evaluation-method decisions (2026-11-01, dated addition)

Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit claim. Public edition, WWOX-DEE genotype class. Adds two controls to the P4 comparison in `../` and records three evaluation-method decisions (OREVID, the npj benchmark, MATRIX/TxGemma). The locked P4 files are read, never written; the P4 decision is unchanged. No third-party raw data is tracked here; OREVID and npj files were read in the session scratch area only.

## 1. Controls applied to P4 (`controls.py`, `controls_result.json`)

Pre-registered in `PRE_REGISTRATION.md` (commit `e8bf80ce`) before the script existed; one dated amendment of the popularity definition (commit `6d5803ed`) after a first run whose popularity values were all 0 (the catalogue attaches DGIdb rows only to DGIdb-only records). **Post hoc on EVAL**: the EVAL reference had already been read in P4 runs 1 and 3. Labels: locked `answers.tsv`, L v1. Rows: the 76 directed (need, compound) rows, 43 DEV + 33 EVAL; 8 have a determinate GtoPdb reference (6 DEV, 2 EVAL), all truly compatible.

| Control | Figure | Pre-registered reading |
|---|---|---|
| C1a popularity of what L proposes | median DGIdb-gene percentile 79.5 for the T set, 79.5 for L-compatible (55 rows), 79.5 for the rest; median ATC5 codes 0 (T) vs 1 (L-compatible) | **L adds no popularity selection over T** (difference 0.0 points, threshold 10) |
| C1b popularity-only path P (k = L's count per need) | Jaccard P vs L 0.53 pooled (glutamate 0.72; seizure and T-type 0.33 each); precision on determinate rows P 7/7, L 6/6, T 8/8 | **popularity and L cannot be discriminated by this reference** (every determinate row is compatible); not a result for either |
| C1c reference-coverage bias | AUC of popularity for determinate vs other rows **0.55** on 8 determinate rows (their percentiles 67 to 95) | **no popularity bias of the reference measured at this denominator** (rule needs at least 5 rows and AUC at least 0.70) |
| C2 construction leakage | **4 leaked rows**: ethosuximide (T-type, the need is labelled after its experiment), vigabatrin (seizure), perampanel and memantine (glutamate), all L-compatible; 1 of them determinate (vigabatrin, DEV) | **the pooled reference figure contains a circular row**: L 6/6 becomes 5/5 without it. The EVAL principal figure (2/2, tezampanel and amantadine) contains no leaked row and is unchanged |
| C2 near-equivalent disease (ATC N03) | 14 of 55 L-compatible rows are antiepileptics (glutamate 3, seizure 6, T-type 5); all 14 N03 rows of T are L-compatible | an existing-indication lookup puts forward a quarter of L's directed output with no WWOX input |

**What C1 shows beyond the numbers.** The P4 universe is already the well-studied end of the catalogue (median 79th percentile), because the universe is "compounds with a curated mechanism on the need's genes". The proxy is also confounded by the group-record defect P4 documented: 10 of the 76 rows have exactly 26 DGIdb genes, the size of the voltage-gated calcium channel group record, so on the calcium needs "popularity" partly measures how far one ChEMBL record fans out. The low Jaccard on the seizure and T-type needs is mostly that effect: among the ten most "popular" rows there, five are gabapentinoids (MODULATOR, group record), on which L abstains.

**WWOX contribution after the controls.** Unchanged and not increased: zero on directed needs (P4 part a). The controls add that part of L's directed output is reachable without WWOX in two other ways: a popularity ranking (overlap 0.53) and an antiepileptic-indication lookup (14 of 55). Four directed rows are compounds the needs were written from, so their compatibility is partly circular.

Reproduce (about 5 s; cache is the gitignored catalogue cache, no download):

```bash
cd disease-models/wwox/research/drug_repurposing
C=catalog/cache
python3 matching_it18_p4_20261101/controls_it18_20261101/controls.py run \
  --catalog catalog/catalog.jsonl.gz --needs needs/needs.json \
  --chembl-targets $C/chembl/targets.jsonl.gz --gtopdb-dir $C/gtopdb \
  --dgidb-interactions $C/dgidb/interactions.tsv
python3 matching_it18_p4_20261101/controls_it18_20261101/test_controls.py   # 9 tests, verbosity=2
```

Controls not run, because P4 already has them by design: same candidate universe for T, X and L; unknown kept as unknown and abstentions reported with reasons; a shared-PubMed-id check with the shared-literature caveat (P4 README, Independence).

## 2. OREVID — the IT8 TRIAL, checked again

**Earlier records.** `../../scout_it8_20261029.md` G-e (registration: TRIAL the design, not the data: (1) hit rate per evidence line, (2) hub exclusion from shared-evidence lines, (3) leakage check of known answers); `../../scout_it8_verifier_20261030.md` (licences and README numbers confirmed; the "0.59 before, 0.37 strict" leak figure not located); `../../complementary_it10_p24_20261031/README.md` and `../../ops_it11_p5_20261031/scouting_it11.md` (cited as a negative LINCS result; TRIAL "stands"). **Proposed:** all three design items. **Implemented before today:** none found (git grep over the repository: no hub-exclusion, per-line hit-rate or leakage-audit code citing OREVID). **Proved:** only the licence facts and that the author's documents contain the quoted numbers; no OREVID number was reproduced at any point.

**Revision now vs examined.** IT8 read the GitHub repository at the 2026-10-29 push (preprint v3, Zenodo `10.5281/zenodo.23323226`). Current: commit `bbff661a994e` (2026-10-30, release v1.3.0, new Zenodo `10.5281/zenodo.23800955`; OREVID predictions changed by two gene-level columns). Hugging Face `orevid/orevid-bench` is at `115ab61a9887` (2026-10-22), older than v1.3.

**The three artefacts do not carry one number set** (author claims, none reproduced here):

| Quantity | IT8 record | HF card (2026-10-22) | GitHub v1.3 | preprint v3 PDF in the repo |
|---|---|---|---|---|
| zero-shot Recall@100, OREVID | 0.811 | 0.811 | 0.812 | 0.812 |
| disease areas, OREVID | — | 0.617 | 0.627 | 0.627 |
| "fair" zero-shot vs TxGNN | 0.809 vs 0.421 | — | 0.809 vs 0.421 | 0.815 vs 0.421 |
| popularity baseline, zero-shot | — | — | 0.358 | 0.358 |

The HF `results.json` files differ byte-wise from the GitHub ones. No OREVID figure is used by LEGEND and none transfers to LEGEND or WOREE (different task: disease-to-drug ranking over PrimeKG; WWOX-DEE has no known treatment row to rank against).

**Licences checked.** Code MIT (GitHub API and LICENSE). `LICENSE-DATA.md` at `bbff661a994e`: tasks, predictions and derived results CC BY-NC-SA 4.0, because PrimeKG aggregates DrugBank (CC BY-NC 4.0), SIDER and DisGeNET (CC BY-NC-SA 4.0); HF card `license: cc-by-nc-sa-4.0`, not gated. Nothing was copied; only the idea is reused (no dataset import, no code copy).

**What OREVID adds to P4, and what it does not.** The useful transferable idea is OREVID-bench's insistence on a disease-ignoring popularity baseline and its leakage audit: implemented as C1 and C2 above. The per-evidence-line hit rate needs a reference with enough determinate rows (P4 has 2 on EVAL) and is not applicable now. Hub exclusion has a P4 analogue already in place: the run-2 rule that abstains on group records whose components lie mostly outside the module's targets.

**Decision on the TRIAL: ADOPT-LIMITED.** Keep the leakage check (needs text against candidate names) and the popularity comparison as controls of any future P4-style matching comparison, as code here, not as a framework. Per-evidence-line hit rate: **wait**, reopen when a matching reference has at least 40 determinate EVAL rows. OREVID data and rankings: not imported (NC-SA; different task). Reopen the whole item if the module ever ranks drugs for a disease rather than labelling direction.

## 3. npj benchmark (Nguyen et al., npj Syst Biol Appl 2026, doi 10.1038/s41540-025-00633-8; repository `thng4165/Drug-Repurposing` at `0f974f01a6d4`)

**Read depth.** Sections read in the article HTML (CC BY 4.0): abstract, the introduction paragraph on evaluation flaws, Results (overall, per method, per dataset, sparsity, evaluation strategies), Discussion, Methods (Datasets, Cross-validation, Evaluation metrics, Parameter setting, the IBCF and DRDM descriptions). Not read: the remaining method descriptions, Table 2 values, supplements. This is a section read, not a full read, so no `FULLTEXT_READ_RECEIPT` is written. Repository: README and file tree only; GitHub API `license: null` (no licence file), so nothing may be copied; datasets come from a Zenodo record of Li et al. 2024 whose terms were not read, and from DrugBank/CTD-derived sources with non-commercial terms.

**What was examined, with locators (article text).**
- Task: drug-by-disease association matrix completion from three matrices: "Each data contains three matrices of drug-drug similarity, disease-disease similarity, and drug-disease association" (Methods, Datasets).
- Split: pair-level, "stratified k-fold cross-validation" over 1 and 0 pairs, k = 10, 25 repetitions; held-out positives are zeroed and the adjacency matrix is recomputed on the training set (Methods, Cross-validation). Every test disease keeps its other known drugs: there is no cold-start disease.
- Unknown associations: counted as negatives ("non-associations"; for example "271 associations, 13079 non-associations"); the paper's own point is that subsampling them inflates AUPR: "previous studies overestimating performance by omitting many negative instances" (Abstract).
- Metrics: AUC and AUPR on the per-disease ranked matrix (Methods, Evaluation metrics). No popularity baseline appears among the ten methods; the simplest is IBCF (item-based collaborative filtering, R `recommenderlab`), average AUPR 0.148 against 0.211 for OMC (Results, method-specific).
- Dataset dependence: "no single method consistently outperforms all others across all datasets"; AUPR tracks sparsity (Results).
- Reproduction cost of the simplest reference (IBCF): an R environment with `recommenderlab` and the `.RData` files; not built, because no demonstrated need follows (below).

**Answer: the P4 baseline stays.** None of the ten methods is a credible reference for P4. P4's task labels the direction of a curated compound action against a need's stated direction on named genes; the benchmark's task fills drug-disease cells from similarity matrices, needs a disease row with known treatments (WWOX-DEE has none), and treats unknown pairs as negatives, which P4 forbids. The simple, credible reference for P4 remains the one already chosen: **T (target-only base rate)** and **X (target prior without WWOX)**, now with the popularity path P beside them (section 1). One lesson transfers and P4 already follows it: score on the full universe without subsampling unknowns, and keep unknown separate from negative. No change to P4 is needed.

## 4. MATRIX and TxGemma — conditions only

- **MATRIX (Every Cure).** Documented state kept (`../../p3b1/txgnn_matrix_outcomes_20261026.md`; inconclusive trial; the scores table states no licence). Check on 2026-11-01: the daily scout of 05:20 UTC reports `EveryCure-MATRIX-scores` UNCHANGED; HF `everycure/matrix-scores` at `d6b121bf3811` (last modified 2026-07-01), not gated, `license` absent from the card. **No condition changed; no reopening.**
- **TxGemma (Google).** No earlier record exists in the repository (git grep over all branches: 0 hits), so this is the baseline. HF `google/txgemma-{2b,9b,27b}-predict` (last modified 2025-04-10) are gated (`gated: auto`, licence `other`, "Access TxGemma on Hugging Face"): access needs accepting terms, which this package may not do on anyone's behalf. Local resources: 4 CPUs, 15 GB RAM, no GPU; the smallest model has about 2.6 billion parameters. Training data are TDC tasks, so a prediction on a compound from a TDC set is not an independent estimate, and a BBB classification is not brain exposure (no unbound brain-to-plasma ratio). **No condition met; WAIT.** Reopen if the operator accepts the terms, and a question arises that needs a prediction on compounds outside TDC that a measured value cannot answer.

## Kept, removed, waiting

Kept: `controls.py`, its tests and result; the OREVID decision (adopt-limited) and the npj answer (P4 baseline confirmed). Removed: nothing. Waiting: OREVID per-line hit rate (40 determinate EVAL rows), MATRIX scores (licence), TxGemma (terms accepted by the operator plus a need). All scratch downloads (OREVID docs and preprint PDF, npj article HTML) stay outside the repository.
