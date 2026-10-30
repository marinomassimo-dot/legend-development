# IT10 P2.4: is there a second logic with a real increment over the IT9 propagation? (scientist-b, 2026-10-30)

Exploratory, computational, class level (a WWOX-DEE genotype class; no individual-level record). Not medical advice. A compatible action of a network, a reversed signature or a morphological similarity is not a predicted benefit. Pre-declaration: `PRE_DECLARATION.md` (committed before any output was opened; one amendment-free run, deviations in section 4).

## 1. Decision first

| Question | Answer |
|---|---|
| Does a second logic give a real informational increment over the IT9 propagation on Q2, Q5 or Q6 at zero cost? | **No, not demonstrated.** Logic 12 (JUMP Cell Painting) ran end to end and is **INCONCLUSIVE**, with a precise cause (section 3.1). Logic 3 with a library of another lineage (GEO-derived, Enrichr) is **NO-ADVANTAGE** on the declared measure, with one concordance (estradiol) and no actionable new compound (section 3.2). Logic 5 is a variant of the same graph by construction; logic 7 and 11 had no zero-cost input that fits (section 2.3). |
| Why not run them on the Q2/Q5/Q6 seeds? | The seeds are too small for any signature or morphology route: Q5 has 3 genes (IL1B, IL6, TNF), Q6 has 1 (MYC), Q2 has a 10-gene set whose six IT7 genes are guarded (IT7_READOUT6). A reversal or similarity query needs a genome-wide input. This is itself a finding: logics 3/12 cannot be driven from the IT9 seed tables, only from a genome-wide WWOX contrast, so the two trials used WWOX-level inputs (JUMP WWOX knockout; the GSE156243 organoid knockout signature already declared in IT2). Reported as a deviation (section 4). |
| Which connector is worth keeping? | One, optionally: `trial2_enrichr_geo.py` (about 70 lines, standard library only, key-less, sends gene symbols only) as a second-lineage reversal probe. Not an adapter, not a dependency. Its library licence is UNVERIFIED (section 2.1), so nothing from it may be redistributed until read. |
| Remove | pyarrow/pandas/scipy venv and the 1.03 GB JUMP profile file (deleted); ToolUniverse stays removed; the 1 GB JUMP download is not worth repeating unless a morphology question is named (see `jx`/JUMP-lite for a lighter route). |
| Independent of the propagation? | JUMP: yes by data (no shared edge, expression or L1000 data) but it produced no overlap at all (0 of the 100 strongest specific opposers map to the catalogue; the 66 of 479 IT9 candidate families that have a JUMP profile have median z -0.02, none at or beyond -3). So it neither confirms nor contradicts anything. Enrichr GEO: independent lineage from L1000 and from the graph, but a single query (the organoid knockout signature) that the IT2 SigCom route already used; concordance with SigCom is one name (estradiol), in different contexts. |

## 2. Scouting

Perimeter: zero spend, key-less GET only, no account, no e-mail or contact address sent anywhere (the Enrichr call carried gene symbols only), nothing installed in the repository. Searches: GitHub repository search 17 queries (10 returned nothing relevant; unauthenticated rate limits stopped 3 first attempts, which were re-run), 11 GitHub API/raw reads for licences and READMEs, Hugging Face 10 model/dataset searches, Europe PMC 8 queries plus 1 record read, Enrichr 3 reads. Depth: licences, READMEs and one abstract were read; no paper was read in full text. WWOX was not required in the searches (as the brief asks); WWOX-specific searches for cell painting and genetic modifiers found nothing (two Europe PMC queries; the top hits were unrelated reviews; "not found" is not "absent").

### 2.1 Resource table (one row per project; GitHub, Hugging Face and the paper of one project are one source)

Licence column quotes what was read; "API" means the GitHub API licence field only. Cost in hours for a first useful use. Verdicts are not a quota.

| Resource | What it does / input / output | Adds over what the repository has | Licence read (source: text) | Maintenance | Cost h / removal | Verdict |
|---|---|---|---|---|---|---|
| **JUMP Cell Painting, cpg0016** (jump-cellpainting/datasets; Cell Painting Gallery; assembled profiles on S3; paper: CPJUMP1, Nat Methods 2024) | Image-based profiles: about 116k compounds, 7,977 CRISPR knockouts, 15,132 ORFs, cell type per source not read here (the CRISPR arm is taken as U2OS from the consortium description, UNVERIFIED). In: a gene or compound id. Out: well-level profile vectors (232 PCs in the 1 GB "ALL v1.0c PCA corrected" file); gene to compound similarity | A measurement of a different kind (morphology) and a route from a gene to compounds that needs no network, no signed edge and no expression. Nothing like it in `framework/` or the catalogue | Data: awslabs open-data-registry yaml, line 35: "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication, but please do cite the corresponding publication". Metadata repo code: BSD-3-Clause (API). Paper abstract (Europe PMC, read): "identifying matches between chemical perturbations and genetic perturbations is a challenging task" | Active: datasets repo pushed 2026-10-26; profile files dated 2025-06-30 | 1 GB download 46 s; script 40 s; about 3 h to design and run with controls; removal: delete the file | **TRIAL done: INCONCLUSIVE; WATCH.** Not adopted: the cross-modality match is the authors' own stated hard problem |
| JUMP-Lite (afermg/JUMP_lite) | Compact subset: 6 sources, 24,356 identities, images, per-site embeddings, curated annotations (29,142 rows over 1,526 perturbations) | Annotations and embeddings may give a smaller, better-controlled gene-compound subset; images 237 GB to 4.8 TB (too large), embeddings not measured | Code: MIT (LICENSE read: "MIT License, Copyright (c) 2026 Broad Institute / JUMP_lite contributors"). Data: stated as part of the Gallery; its own DATA_CARD licensing section not read: UNVERIFIED | Release 2026-10-19; push 2026-10-29 | 3-4 h; delete | **WATCH** (read the data card and the 1,526 curated rows before any use) |
| jx (broadinstitute/jx), jump_hub (CC0-1.0 API) | Marimo notebooks that retrieve JUMP profiles by perturbation and a skill for an agent to compose analyses | Would replace the 1 GB download by targeted retrieval (nb01 "Pull JUMP morphological profiles by perturbation"; not run) | BSD-3-Clause (API); LICENSE file not read | pushed 2026-08-21 (jx), 2026-10-22 (hub) | 2-3 h plus marimo | **WATCH** (not run; the claim of targeted retrieval is the README's) |
| Haghighi et al. Nat Methods 2022 repo (carpenter-singh-lab/2022_Haghighi_NatureMethods), same group as JUMP | Four datasets with L1000 and Cell Painting on the same perturbations (28,000) and evaluation metrics | The only public place to ask whether morphology carries information that expression does not, on matched perturbations | BSD 3-Clause (LICENSE read: "Copyright (c) 2021, carpenterlab") | push 2025-08-11 | 2 h reading | **WATCH** (a method-choice reference if a morphology question is named) |
| mantispy (scverse), DeepProfiler (cytomining) | Analysis framework for profiles; image-based deep profiling | Nothing the trial needed (pandas/numpy sufficed); DeepProfiler needs images | BSD-3-Clause (API, both) | pushed 2026-10-29 / 2026-10-13 | n/a | **REJECT** (no named need) |
| **Enrichr GEO libraries** (Drug_Perturbations_from_GEO_up/down, 906 terms each; Ma'ayan lab; the same project family as SigCom LINCS, Enrichr, L2S2 and RummaGEO) | Gene-list enrichment against drug-perturbation signatures extracted from single GEO experiments. In: up and down symbol lists. Out: terms with adjusted p; the term string carries compound, PubChem/DrugBank id, species, GSE and sample, no tissue | A second signature lineage (GEO experiments, not L1000). The repository had only L1000 routes (SigCom, L1000FWD) | **UNVERIFIED**: no licence text found on the Enrichr main and help pages (two fetches, grep for licence/terms/commercial returned nothing); source experiments are public GEO | live service | trial 43 s, script 70 lines; removal: delete the script | **TRIAL done: NO-ADVANTAGE; keep the script as an optional probe, WATCH** |
| RummaGEO (MaayanLab/rummageo; Patterns 2024; library `RummaGEO_DrugPerturbations_2025`, 5,344 terms in Enrichr) | Gene sets auto-mined from GEO | Larger GEO library | **Conflict**: GitHub API says BSD-3-Clause; the LICENSE file begins "Attribution-NonCommercial-ShareAlike 4.0 International" | push 2026-10-05 | n/a | **REJECT** for anything redistributable until the conflict is resolved; same lineage as the Enrichr trial |
| L2S2 (MaayanLab/L2S2; NAR 2025) | LINCS L1000 chemical and CRISPR-KO signature search | A gene knockout side (CRISPR KO signatures) that SigCom queries lack; still L1000 | Apache-2.0 (API); data terms not read | push 2026-08-03 | 2-3 h | **WATCH** (same data lineage as SigCom: not an independent vote) |
| glenritschel/l1000-repurposing-benchmark (preprint with code; single author) | Pre-registered retrospective benchmark of L1000 connectivity scoring against approved repurposings | README, read: seven cases, mean percentile 0.387 against a null of 0.501, p = 0.098, "The pre-registered criterion (p < 0.05) was not met". Another negative for L1000 reversal, alongside OREVID (IT8) and Lim and Pavlidis | no licence file (API: none): reading only | push 2026-10-01 | 1 h | **WATCH** (a reading; the numbers are the author's, no replication) |
| Hugging Face (10 searches: cell painting, jump cellpainting, L1000, perturbation, drug repurposing) | Cell-painting LoRA checkpoints, a VAE, generic perturbation datasets | Nothing pertinent: no JUMP, L1000 or drug-signature resource; `weililab/perturbation-embeddings` and `genbio-ai/foundation-models-perturbation` are single-cell/genetic perturbation resources listed by title only, not opened | not read | n/a | n/a | **REJECT** (nothing usable found) |
| GitHub signature-reversal repositories (ALS, schizophrenia, ovarian; 0 stars) | One-off pipelines on L1000 | Nothing beyond SigCom use; no licence on two of three | MIT (ALS repo, API); others none | 2026 | n/a | **REJECT** |

### 2.2 Biological terms searched (pathway and process, then WWOX-free)

* HIF1A/hypoxia signature plus compound reversal: GitHub 0 repositories; Europe PMC returned reviews on cancer and mitochondria (no method). No reversal resource specific to HIF was found. The GEO library trial is the only HIF-neutral use.
* Microglia / IL1B inflammation perturbation: GitHub "neuroinflammation drug repurposing" 0; Europe PMC mostly reviews and an in vivo Perturb-seq paper (genetic, not drug). Not used.
* MYC: nothing method-like surfaced; MYC remains a one-gene seed.
* WWOX cell painting, WWOX genetic modifier screens: nothing found (two Europe PMC queries, results irrelevant). The JUMP set contains one WWOX CRISPR id and one WWOX ORF id (found in the metadata), 5 wells each, one source.

### 2.3 Logics not trialled, and why (matching_guidance_v3 section 4)

* 5 interactome proximity: another variant of the same graph class (curated interactions), so not independent by the brief's own rule.
* 7 genetic suppressor / synthetic rescue: the only zero-cost genome-wide input is DepMap-type essentiality. It measures lethality in cancer lines, i.e. a vulnerability (the opposite of rescue), so a result would answer a cancer question; the DepMap licence was not read (UNVERIFIED). No published WWOX modifier screen was found. Verdict: not applicable until a rescue screen exists.
* 8 direct phenotypic rescue: needs a measured WWOX-deficient phenotype with compounds; none is public (the IT8 radar still shows no human WWOX RNA release). Not applicable at zero cost.
* 11 metabolic constraints: not examined (no measured fluxes in a WWOX-deficient neural system exist, per the Q2 reserved-for-evaluation note); a model would be assumption-driven.

## 3. Trials

### 3.1 Trial 1, logic 12: JUMP morphology (pre-declaration section "Trial 1")

Input: WWOX CRISPR knockout wells (5 wells, 5 plates, all source_13, U2OS) against the same pipeline's gene-matched null of 1,000 random knockouts; universe 115,788 compounds with wells on at least 2 plates. Data: JUMP assembled ALL v1.0c PCA-corrected profiles, 946,431 wells (downloaded 2026-10-30).

| Declared measure | Result |
|---|---|
| Gate: WWOX mean pairwise cosine among wells of distinct plates at or above the null 95th percentile | **Pass, marginally**: 0.631 against p95 0.627 (percentile 95.1; null mean 0.309, p99 0.819). Only 5 wells in one source |
| Method control: PLK1 knockout, at least one known PLK1 inhibitor among the 100 highest-z compounds | **Failed as declared**: none in the top 100 by z (PLK1 itself is at the 74.8th percentile of reproducibility). Post hoc (diagnostics, not declared): by raw cosine rank, five of six PLK1 inhibitors present in JUMP rank 55 to 333 of 115,788 (rigosertib 55, onvansertib 105, GSK461364 106, volasertib 221, BI-2536 333; TAK-960 14,139), i.e. the cross-modality signal exists but the declared z-ranking and catalogue-name matching were the wrong instrument |
| Specific opposers (z <= -3, top 100) | 100 compounds, z down to -5.8, cosine down to -0.87; **0 map to the catalogue** (only 3,348 of 115,788 JUMP compounds, 2.9 percent, map by InChIKey skeleton; 0 of 300 is far below the 8.7 expected, so these are enriched for unannotated library compounds) |
| Overlap with IT9 (Q2/Q5/Q6, all arms) and SigCom S1 top 100 | 0 and 0. 66 of the 479 IT9 candidate families have a JUMP profile; median z -0.02; none at or below -3; one (a nucleoside, mizoribine) at +5.7 on the mimic side, which is a similarity, not a prediction |
| New compound names / new hypotheses / known leads re-found | none / none / none |

Post-hoc diagnostics (disclosed, not pre-declared; `results/trial1_diagnostics.json`, `trial1_source_check.py` code, numbers below): the WWOX mean profile has norm 2.99 (88th percentile of random knockouts); well-to-well cosines 0.44 to 0.76; the 100 most-opposed compounds share on average 0.27 members with those of 60 random genes (max 16), so they are not a generic list; but the 300 most-opposed come disproportionately from compound sources 9, 5 and 11 (831, 362 and 329 of 1,950 wells; source_9 is 19.6 percent of compound wells), while all CRISPR wells come from source_13. A source-linked (batch) component of the cross-source alignment therefore cannot be excluded, and the knockout profile itself rests on 5 wells.

**Outcome: INCONCLUSIVE.** Precise causes: (i) WWOX replicability passes only at the 95.1th percentile on 5 wells of one source; (ii) the declared control failed (and its post-hoc rescue by a different statistic is not a pass); (iii) the opposers are not drug-like catalogue compounds, so even a clean signal could not be compared with the propagation; (iv) U2OS is non-neural and WWOX expression there was not checked (UNVERIFIED). It is not evidence that WWOX loss has no morphology, and not evidence of any compound's effect.

### 3.2 Trial 2, logic 3 with a GEO-derived library (pre-declaration section "Trial 2")

Input: the exact IT2 sets (S1 517 up / 317 down, S3 505/313, S0 random 517/317, S1P and S1P2 direction shuffles), against Enrichr Drug_Perturbations_from_GEO_down (for the up set) and _up (for the down set); both arms adjusted p < 0.05.

| Set | Reverser terms (both arms) | Mimic terms (both arms) |
|---|---|---|
| S1 | **9** | 13 |
| S3 (markers removed) | 9 | 8 |
| S0 random | 0 | 0 |
| S1P shuffle | 0 | 4 |
| S1P2 shuffle | 2 | 0 |

Declared rule (S1 at least 3 times the largest control, at least 3): met (9 against 2). But the S1 reversers are not direction-specific (13 mimic terms; the same input both reverses and mimics, the pattern that made the IT2 SigCom result uninterpretable), and the nine terms are: hypochlorous acid x3 (one GEO study, GSE11630, so one observation), estradiol (mouse), ascorbic acid, retinoic acid (mouse), coenzyme Q10 (mouse), harman, doxorubicin. Terms carry no tissue annotation, so neural versus non-neural cannot be stated (UNVERIFIED for all nine).

| Comparison | Result |
|---|---|
| Overlap with SigCom S1 top 100 (L1000) | **estradiol only** (SigCom rank 1; here a mouse experiment, GSE2195). Two libraries, two contexts, one name: concordance of two accesses of drug-in-cell-line transcript data, not a confirmation, and not WWOX evidence |
| Overlap with IT9 propagation (Q2, Q5, Q6) | estradiol esters (cypionate, valerate) are in the flagged arms (prodrug flag) and must not receive the estradiol observation; retinoic acid corresponds by name to tretinoin in the Q2 **direct-search** arm (rank 42), not in a propagation arm (identity by name only, not checked by structure). Nothing else |
| New compound names | hypochlorous acid, ascorbic acid, coenzyme Q10, harman, doxorubicin; all generic redox or cytotoxic perturbations, none actionable for the three questions |
| Independence | Another library, not independent of the input: the same organoid knockout signature (and its composition/maturation confound, already known) drives every row |

**Outcome: NO-ADVANTAGE** for this input: a second reversal library reproduces the structure of the first (context-driven, bidirectional) and adds no actionable compound.

## 4. Deviations and non-blind steps

1. The trials were not run on the Q2/Q5/Q6 seeds (reason in section 1); the questions entered only at the comparison step.
2. Trial 1 declared control failed; the post-hoc cosine-rank reading and the source-concentration check were run after seeing the result and are labelled as such; none changes the declared outcome.
3. First execution of `trial1_jump.py` crashed on a null catalogue name before any result (fixed by `or r["id"]`); no output was seen from the crashed run.
4. Before writing the pre-declaration I saw JUMP metadata columns, WWOX presence, bucket listings and the IT9/IT2 documents; no values.
5. `trial1_source_check.py` is the code run inline (it was run as a heredoc, not from this file); the file was written afterwards and not re-executed.
6. Wall-clock: about 45 minutes of tool time for scouting, trials and writing (estimate, not a stopwatch); JUMP download 46 s, trial 1 compute about 20 s per run, trial 2 43 s; about 70 tool calls.

## 5. UNVERIFIED

Licence of the Enrichr libraries and of the JUMP-Lite data card; the RummaGEO code licence conflict; DepMap licence; whether U2OS expresses WWOX; tissue/cell annotation of every GEO term; the PubChem id to tretinoin identity beyond names; cos and z values depend on the harmonised PCA space and may change with the other JUMP processing versions (v1.0a/b profiles not tried); jx targeted retrieval; the claim that these data are U2OS-only (the metadata lists sources, not cell types, in what I read). Nothing was read in full text.

## 6. For the batch path

* Do not edit cards, needs or ranking from this package. Suggested record: capability scout entry "logic 12 (JUMP) and a GEO signature library tried once on WWOX-level inputs: INCONCLUSIVE and NO-ADVANTAGE; neither reaches the Q2/Q5/Q6 seed tables, which are too small for signature routes".
* A genuine test of morphology needs: more than 5 WWOX wells (source overlap with compounds), a control validated by gene-target ground truth with an InChIKey-based target list, and a neural line. If JUMP-Lite's curated annotations or `jx` give targeted retrieval, reopen with that.
* A reversal route on Q2/Q5/Q6 needs genome-wide contrasts (for Q2 from a neural model, but still guarded by IT7_READOUT6 for the six genes), not the seed tables.
* Estradiol: two lineages name it for the organoid knockout signature; the IT9 estradiol rows are esters under the prodrug flag. Transfer is not allowed; if anyone asks, the parent compound needs its own card question.
* Files: `trial1_jump.py`, `trial1_diagnostics.py`, `trial1_source_check.py`, `trial2_enrichr_geo.py`, `results/` (about 68 KB). Commands: see each script's `--help`; trial 1 needs pyarrow, pandas and numpy in an isolated venv and the 1 GB profile file (not committed).
