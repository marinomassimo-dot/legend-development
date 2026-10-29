# IT7 P3 (roadmap R3): first bounded network-prediction comparison - result

Scientist-a, 2026-10-29. **EXPLORATORY. Computational. Not medical advice; a computational result is not therapeutic efficacy.** Nothing here edits a scientific current file, a card or a need.
Pre-registration: `PRE_REGISTRATION.md` (commit eadbe26a, before any evaluation value was opened; AMENDMENT 1 in ae430b6d re-froze the inputs from the repaired P1 31446616, still before any value was opened). Deviations: `DEVIATIONS.md`.
The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used.

## 1. Verdict (as pre-registered; no criterion was changed after a result)

| Comparison (question) | Verdict | Reopening condition |
|---|---|---|
| **Primary.** Signed network (external-only, NET-EXT) vs unsigned frequency-corrected overlap reference (REF-1), ranking compounds by *observed* six-gene module opposition in held-out neuron-like LINCS contexts | **NO ADDED VALUE** (no detectable signal at rho >= 0.15) | a compound-response measurement in a WWOX-deficient human neural system with replication; potency from the ChEMBL activity endpoint; phase II signatures; a larger replicated module |
| Secondary S2. Transcriptional-signature route (SIG; six genes, progenitor-like cells to neuron-like cells) vs REF-1 | **NO ADDED VALUE** (signal criteria not met; rho 0.143 is just under 0.15 and under its own random-readout null) | same, plus a signature larger than six genes |
| Secondary S3. WWOX-enriched network (4 curated HIF1A edges added) vs external-only | **NO ADDED VALUE** (difference -0.0015, 90 % interval [-0.004, +0.0002]) | only if curated WWOX edges that reach compound targets exist |
| E1 (not a method comparison). Does the six-gene module transfer to an independent WWOX-loss contrast (P47T knock-in, animals as unit)? | **INCONCLUSIVE** | a replicated WWOX-deficient human neural contrast with a matched protein/activity readout; a larger P47T-type cohort |

"No added value" here means: **no detectable gain, with a minimum detectable effect of about rho 0.15** at |U| = 256 (SE about 0.063). Smaller effects are not excluded. It does not mean the compounds do not act on the module, and
it says nothing about efficacy. The missing comparison (named in the registration) is a compound-response measurement in a WWOX-deficient human neural system with biological replication and a matched readout; no such public record exists (IT6 P3 census, IT7 P0a).

## 2. Design as run (details in PRE_REGISTRATION.md)

* **Question:** among pilot compound families, which method ranks compounds by their observed opposition of the P1 six-gene glycolysis/lactate module (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down in the human WWOX-loss build systems) in LINCS neural-cell signatures that were not an input.
* **Universe U = 256 families**, a stated subset (578 families usable by both methods in P2, minus the 17 card-linked-only ones by firewall, restricted to families with a strict neural `trt_cp` signature in a progenitor-like context `NPC*` AND a neuron-like context `NEU*/MNEU.E` in LINCS phase I). **Not a screening of the catalogue** (256 of 40 268 families, chosen by input availability).
* **Outcome:** `O^E` = median per family of the scale-normalised opposition score of its neuron-like signatures (all doses/times kept in `signature_scores.tsv`: 1 239 signatures; cell id, dose, time, pert id retained).
* **Methods:** REF-1 (unsigned, IDF/promiscuity-corrected overlap of compound targets with first-order regulators of the readout genes); NET (signed propagation, K = 3, damping 0.5, 1/out-degree normalisation, promiscuity-diluted unit-norm target vector; external network = OmniPath-served SIGNOR + licence-filtered CollecTRI, 8 769 genes, 70 461 signed edges; no WWOX card, need or compound-response in it); SIG (the six-gene opposition score in the progenitor-like contexts, evaluated in the neuron-like contexts); BASE-promisc; REF-0 (direct module-node overlap: 0 families in U, degenerate as registered).
* **Why the evaluation is separate from the build:** module and signs fixed from GSE156243 + GSE126075 (P1); NET/REF take no expression; SIG is built and evaluated on disjoint cell ids; E1 uses GSE215425, an independent genotype and laboratory.
* **Firewall:** card-linked compounds (ethosuximide, lithium, vigabatrin ...) enter nowhere; only **one** card-linked family (sirolimus) is inside U and is reported descriptively below. The fly factorial is fully held-out and not used.

## 3. Results E2 (n = 256 families; `results/results_summary.json`)

Spearman rho against the held-out outcome (90 % bootstrap interval, 1 000 resamples); control nulls from 1 000 random matched readouts (C1) and random matched inputs (C2).

| Method | rho | 90 % CI | C1 null 95th pct (emp. p) | C2 null 95th pct (emp. p) | after removing frequent hitters |
|---|---:|---|---|---|---:|
| SIG (six genes, NPC* -> NEU*) | **0.143** | [0.039, 0.243] | 0.200 (0.179); null median 0.080 | - | 0.143 (0 flagged) |
| NET-EXT | 0.047 | [-0.060, 0.150] | 0.103 (0.209) | 0.137 (0.355) | 0.011 (38 flagged) |
| NET-WWOX | 0.046 | [-0.062, 0.147] | 0.104 (0.216) | - | 0.010 |
| REF-1 | -0.085 | [-0.186, 0.018] | 0.096 (0.939) | 0.052 (0.870) | -0.092 (26 flagged) |
| BASE-promisc | 0.031 | - | 0.125 (0.347) | - | - |
| REF-0 | 0 (constant) | - | - | - | - |

* **Signal criteria:** NET-EXT fails S1 (0.047 < 0.15), S2 against both nulls, S3 (bootstrap and edge-dropout stability), S4 (sign-permuted networks) and S5. SIG fails S1 (0.143 < 0.15) and S2 (C1 analogue: random 6-gene readouts also reproduce across contexts with a median rho of 0.080 - a shared transcriptional-magnitude axis - and the real value sits at the 82nd percentile of that null); it passes S3, S5.
* **Difference from the reference:** SIG - REF-1 = +0.228 [0.083, 0.367]; NET-EXT - REF-1 = +0.133 [-0.026, 0.296]. Both are produced mainly by REF-1 being slightly negative (25 of 256 families have a non-zero overlap at all), not by the methods being good; "added value" requires signal first.
* **Top-decile / matched sets:** hit rate of top-decile (chance 10 %): SIG 15 %, NET 7.7 %, REF-1 7.7 %. Mean rank of the method's top decile in the outcome vs matched random sets (target-count terciles): SIG p = 0.092, NET p = 0.916, REF-1 p = 0.911.
* **Direction-perturbed:** 200 sign-permuted networks: median -0.003, 90th percentile 0.084; the real NET (0.047) is at the 82.5th percentile (emp. p 0.175). Placing the single "down" gene on each of the six readout genes: the real placement (PDK1) gives the highest rho for both NET (0.047 vs <= 0.027) and SIG (0.143 vs <= 0.053), the weak pointer toward direction information, but 1 in 6 by chance and inside the noise. Global sign flip inverts rho (trivial check).
* **Structure sensitivity (NET-EXT):** 20 % edge dropout (100 replicates) median 0.030, 68 % positive; degree-preserving rewiring (100 replicates, 50 x |E| swaps) median -0.003 [-0.093, 0.134]. Not stable by the registered rule.
* **Frequent hitters:** NET flags 38 families (up to 43 % of random inputs; alvocidib, PHA-793887, AT-7519, plumbagin, saracatinib: kinase/transcription-regulating compounds that reach many regulators), REF-1 flags 26 (up to 98 %: bepridil, calcifediol, SB-216763, telmisartan, progesterone), SIG 0 (maximum 18.5 %). After removal NET-EXT falls to 0.011.
* **Swapped contexts** (build on neuron-like, outcome progenitor-like): SIG 0.143 (symmetric by construction), NET 0.020, REF-1 -0.022. **10 uM / 24 h only** (n = 255): SIG 0.057, NET 0.025, REF-1 -0.102. **Up-arm only (PDK1 dropped):** SIG 0.047, NET 0.028, REF-1 0.001. Including the direct (k = 0) target effect leaves NET unchanged (0.047, no pilot family hits a module node).
* **Known example (descriptive, no input role):** the only card-linked family in U is sirolimus (mTOR axis card); percentile (0 low, 1 high) in observed opposition 0.69, SIG 0.89, NET 0.53, REF-1 0.45. One family is an anecdote, not a recovery rate; ethosuximide, lithium and vigabatrin are not in U (no strict signature in both context classes in phase I).

## 4. Results E1 (P47T knock-in, `results/e1_p47t_summary.json`; GSE215425, 5 v 5 animals, regions not independent)

Hippocampus (registered primary): module contrast D = +0.329 (positive = WWOX-loss-like), decile-matched null 95th percentile 0.389, so **inside the null band**; exact one-sided p = 0.060 (252 assignments); 5 of 6 genes in the build direction (HK2 +0.66, LDHA +0.48, SLC2A1 +0.18, BNIP3 +0.03, PDK1 -0.08 as predicted; **LDHB -0.10 against**); up-arm mean +0.25. Verdict by the rule: INCONCLUSIVE (not TRANSFERS: D below the null 95th percentile and p > 0.05; not DOES NOT TRANSFER: p near 0.05 and 5/6 concordant).
Descriptive: PFC D 0.186 (p 0.163), parietal CTX 0.219 (p 0.194), CB 0.035 (3 v 4, p 0.343, cannot reach the registered alpha); animal-level mean over regions diff 0.179, exact p 0.147, sex-stratified p 0.15. The direction agrees with the human systems in three regions but no region passes. Reading: one partial-loss missense genotype leans the same way, with too few animals to say more; the earlier mouse P17 deposits (seen) argued against LDHA/LDHB and LDHB is again the discordant gene. The module is therefore **not shown to be a reproducible WWOX-loss feature**, and the compound results above carry no demonstrated WWOX-loss relevance (they are module opposition in wild-type neural cells). The 0.25 concordance rule that chose the readout genes passes about 4 of 24 genes by chance (P1 repair note); the decile-matched null is the reference used here.

## 5. Counter-evidence and honest limits

* **Counter-evidence to "no added value" for the signature route:** SIG's rho is positive (0.143, lower 5 % bound 0.039), its top-decile hit rate is 15 %, its matched-set p is 0.092, and the real direction placement ranks first of six. This is a weak, borderline reproducibility of module opposition across neural contexts, comparable to what random readouts also show (C1 median 0.08); it is not specific to the module at the registered threshold. It is the only result that could turn with more data (it is 0.007 below the registered 0.15).
* **Level mismatch:** NET propagates target *activity* effects, the outcome is *transcript*; the registered primary excludes direct node effects for that reason, but kinase/regulator edges from curated pathway resources are sparse, partly literature-biased, and context-free.
* **Power:** n = 256 families (not independent compounds: salts/duplicates are upper bounds), one concentration (10 uM) and mostly one time point, wild-type cells, no signature quality filter, no potency or exposure in any method, five of six readouts inferred (not measured) in L1000, and a single-gene down arm. Only phase I; phase II (GSE70138) was not added.
* **C2 is an easy null** (SD-matched random genes have few regulators); the added in-degree-matched C2b gives the same picture (NET p95 0.135, emp. p 0.358; not used in any verdict).
* REF-1 is nearly empty (25 of 256 non-zero); the reference is weak by construction, which is why "difference from reference" is not read as an advantage.
* The network is generic: the WWOX-enriched condition adds four HIF1A edges that the external network already largely contains, so S3 tested only that increment and says nothing about WWOX knowledge in general.
* Not used / not reopened: BioNAV/NeMoCAD (Zenodo 7692713 is `restricted`, no file, no licence field; no request sent, so the method here is not a reimplementation of it); TxGNN, MATRIX, ToolUniverse (documented limits unchanged); the fly factorial check (not run: ortholog mapping and amyloid context, and held-out). ChEMBL activity mode not used (not cached; no potency).

## 6. Costs and resources

E2 wall time 932 s on the shared 4-thread host (about 15 min; 112 s for 200 sign-permuted networks, about 13 min for 100 rewirings); E1 1 s. Memory not profiled (LINCS rows read from a memory map; the 1 239-row z matrix about 60 MB). Downloads: two OmniPath exports (about 30 MB raw, filtered to 0.6 MB gz), GSE215425 processed table 2.0 MB, LINCS metadata already on disk. Spend zero; no registration, contact address or access request. Development included three synthetic-noise runs.

## 7. Inputs, versions, hashes (`inputs/INPUTS.tsv` has the full list)

P1 subnetwork at 31446616 (repaired); P2 usable-compound tables at 7ad3e697; OmniPath exports 2026-10-29 (SIGNOR + CollecTRI, licence-filtered; raw sha256 8eb28a05... and d08018c0...); LINCS GSE92742 level 5 via the IT3 extract (`extract.npy` sha256 2939e0bf2e7c47b3ba56e546269552beeaf5ea00596634db6a097f8e0999e33d, `extract_rows.tsv` 33149888..., `extract_genes.json` e857bf9f...; built from the level 5 gctx by `gse156243/lincs_it3_local_level5.py extract`, gctx.gz sha512 6a3115cf... in that note); `sig_info` 19da29c0..., `gene_info` 741216cc...; GSE215425 `processed_data.csv.gz` sha256 d654f6bdd2a4ac5b3e24741f16962503a711575c72aa92a2c729a7a0cf04c18c (tab-delimited despite the name), series matrix 73aa99a6.... Attribution: SIGNOR (CC BY 4.0) and CollecTRI/DoRothEA constituent resources via OmniPath; LINCS (Subramanian et al. 2017, Cell); ChEMBL/GtoPdb share-alike via the P2 tables; no raw LINCS or GEO matrix is committed.

## 8. Reproduce

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 p3_run.py --help                                  # answers without work
python3 p3_run.py e1 --counts <GSE215425_processed_data.csv.gz> --out results
python3 p3_run.py e2 --geo <dir with GSE92742 sig_info, gene_info> --cache <dir with extract.npy, extract_rows.tsv, extract_genes.json> --out results
```
Deterministic (seed 20261029 + fixed offsets); a second full E2 run reproduced every number except the corrected sensitivity block. `P3_SYNTH=1` runs the E2 code on seeded noise. Files: `p3_run.py`, `inputs/`, `results/` (`results_summary.json`, `family_scores.tsv`, `signature_scores.tsv`, `e1_p47t_summary.json`), `DEVIATIONS.md`.

## 9. UNVERIFIED

Integer-count nature and age of the GSE215425 animals; HGNC symbol agreement between ChEMBL/DGIdb target symbols and OmniPath (656 targets, 493 present in the graph); OmniPath licence labels taken from its metadata on 2026-10-29 and not independently audited; whether LINCS signature quality metrics would change rho; whether any pilot compound reaches neural tissue (exposure UNKNOWN for all); independence of the neuron-like and progenitor-like LINCS cell lines beyond cell id; the E1 null uses a plain log2(CPM+1), not a count model.
