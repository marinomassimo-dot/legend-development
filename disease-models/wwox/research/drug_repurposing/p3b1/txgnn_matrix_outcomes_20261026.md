# P3B-1 — TxGNN and Every Cure MATRIX: one proportionate outcome each

Actor `scientist-d`, package P3B-1, 2026-10-26. Non-canonical research material under `research/`; **not medical
advice**, no wet-lab or clinical action. Nothing was trained, nothing was installed outside a throw-away scratch
environment, no key, account, payment or e-mail address was used. Every external source below is **NOT WWOX
EVIDENCE**: it is a retrieval surface or a prediction resource. A database record, a GitHub issue and a model output are
**discovery depth**, not a reading; this note carries no `FULLTEXT_READ_RECEIPT` and cites no paper as read.

Status vocabulary follows `../tool_survey_20261022.md`: `MEASURED` = produced here on 2026-10-26 by the named command;
`THIRD-PARTY` = what someone else reports, not reproduced here; `INFERENCE` = the reader's derivation.

## Outcomes (one each)

| Resource | Outcome | In one sentence |
|---|---|---|
| **TxGNN** (MIT code, PrimeKG v2.1 data) | **REASONED WAIT** | Coverage is real but coarse (WWOX is a node; DEE28 and SCAR12 exist only inside grouped disease nodes); no published per-disease predictions are retrievable (explorer offline), the released checkpoints are evaluation-split models that cannot be run on this host without a legacy stack, and third parties report that they do not reproduce the paper's metric. No WOREE-specific performance exists anywhere |
| **Every Cure MATRIX** (Apache-2.0 code; scores table with **no declared licence**) | **INCONCLUSIVE TRIAL** | A small extract was read: the WOREE node exists and is scored against 1 748 drugs, carries **no** training label, and its drug ordering is statistically close to that of its sibling DEE nodes (so it is not shown to carry WWOX-specific information). The scores table may not be reused or redistributed until its licence is stated; the CC BY 4.0 drug and disease lists may |

Neither outcome is an exclusion: both resources stay reachable for the reopening conditions at the end.

## 1 · TxGNN

### 1.1 Identity and version

| Item | Value | Status |
|---|---|---|
| Code | `mims-harvard/TxGNN`, commit `0e0203c3939f` (2024-05-06, "add reproduce info"), **no commit since**; licence MIT (`LICENSE` read) | MEASURED (GitHub API) |
| Paper | Huang et al., medRxiv 2023 (DOI as printed in the repository README); project page `zitniklab.hms.harvard.edu/projects/TxGNN/` HTTP 200 | MEASURED (not read; abstract-level) |
| Package | PyPI `TxGNN` 0.0.3 (MIT): `uv pip install` fails at the sdist build (`requirements.txt` missing from the sdist) | MEASURED |
| Stack it demands | Python 3.8, DGL 0.5.2 (README). On this host (Python 3.12) DGL 0.5.2 has wheels only for `cp36m/cp37m/cp38`; no torch, no GPU (`nvidia-smi` absent), 4 CPU, 15 GB RAM | MEASURED |
| Knowledge graph | PrimeKG, Harvard Dataverse (dataset record, version 2.1), file `kg.csv` — **the md5 of the stream read here equals the md5 Dataverse publishes** (`aac8191d4fbc5bf09cdf8c3c78b4e75f`), and equals the md5 of the file the TxGNN code downloads | MEASURED |
| Pretrained weights | the main README also links a second "example" weight file (Drive, not examined). The reproduce note links one Google Drive zip, about 199 MiB, reachable without login: 55 checkpoints = 11 splits × 5 seeds (`complex_disease`, `random`, nine disease-area splits). **There is no `full_graph` checkpoint**, which the README says is the setting for deployment on a specific disease | MEASURED (zip central directory read by range request, nothing extracted) |
| Explorer | `txgnn.org` answered **HTTP 503** on 2026-10-26 (project page still points to it) | MEASURED |

### 1.2 Licences, kept separate

| Part | Terms | Note |
|---|---|---|
| TxGNN code | MIT | free to run and adapt |
| PrimeKG code | MIT (its README) | |
| PrimeKG data | Dataverse record declares **CC0 1.0**, but the PrimeKG README says the code licence "is distinct from any licenses governing the PrimeKG dataset itself" and the graph integrates DrugBank, DisGeNET, DrugCentral, SIDER, UMLS and others | CC0 on the record is **not** a clearance of the upstream content. Here only counts, node ids and five drug names (relations of the DEE group) were kept |
| Pretrained weights | **no licence stated in the repository** (its reproduce note only links the Drive file; the Drive page was not read) | treat as unlicensed until stated; never redistributed here |
| Explorer outputs | no terms found (site offline) | |

### 1.3 Coverage of the relevant entities (`primekg_coverage.py`, output `primekg_coverage_20261026.json`)

| Entity | In PrimeKG / TxGNN? | Detail |
|---|---|---|
| **WWOX** (NCBI Gene 51741) | **yes**, node 602 | 740 relation rows; types incl. `disease_protein` (74 rows), `protein_protein` (342), anatomy/GO/pathway; **`drug_protein`: 0** (no ligand of WWOX in the graph — consistent with ChEMBL "0 targets" in the survey) |
| **DEE28 = WOREE** (MONDO 0014533) | **only merged**: it is one of 87 member ids of the grouped node `developmental and epileptic encephalopathy` (node 28005) | The graph TxGNN trains on has no WOREE-specific disease node. The group carries `indication` edges to cannabidiol, stiripentol, vigabatrin and `off-label use` edges to eight corticosteroid/ACTH drugs, and a `disease_protein` edge to WWOX. A TxGNN output "for DEE28" is therefore an output for a 87-disease group |
| **SCAR12** (MONDO 0013687) | **only merged**: one of 18 member ids of `autosomal recessive spinocerebellar ataxia`; no drug relation | same |
| undetermined early-onset EE (MONDO 0018614) | own node (33095), no drug relation, no WWOX edge | |
| the word "WOREE" | **absent** as a node name (also absent from `txgnn/data_splits/kg_grouped_diseases.csv` at the pinned commit, and from the Dataverse PrimeKG `kg_grouped_diseases.tab`) | a synonym, not a node |
| Neither group node is in any of the nine disease-area test lists (`data/disease_files`) | | they would be held out only by the random `complex_disease` split |
| **PDK1-4** (5163-5166) | yes | `drug_protein` rows: PDK1 4, PDK2 6, PDK3 4, PDK4 4 (rows are directed; halve for edges). Dichloroacetate is linked to PDK1 |
| **LDHA / LDHB / LDHC / PDHA1 / PDHB** | yes | LDHA 14, LDHB 10 drug rows (oxamic acid, stiripentol among them) |
| **ISR: EIF2AK1/2/3/4, EIF2S1, ATF4, DDIT3, PPP1R15A/B** | all present | `drug_protein` rows: EIF2AK1/2/4 2 each (fostamatinib), ATF4 2, **EIF2AK3 (PERK) 0, EIF2S1 0, DDIT3 0, PPP1R15A 0, PPP1R15B 0** — the graph holds no ISR-modulator ligand edges beyond that |

`INFERENCE`: because DEE28 and SCAR12 are merged into large groups, any TxGNN ranking "for WOREE" would be driven by the
group's labelled treatments and by the WWOX edge shared by all group members' neighbourhood; the model could not
separate WOREE from the other 86 DEEs.

### 1.4 The smallest comparison obtainable without training — and why it stops here

What was possible and done: identifier, coverage, licence and reproducibility audit above (no model run).

What was **not** possible, and the missing proof:
1. **No published predictions to compare.** The only public carrier of per-disease predictions is the explorer; `txgnn.org` returned 503 when tried here, while a verifier's single attempt got no HTTP response (curl 000) — the failure mode is uncertain, the conclusion (no retrievable per-disease predictions) is unchanged.
   The repository ships no prediction table. The paper's metrics were computed on held-out disease areas, none of which
   contains the DEE or AR-SCA group.
2. **Checkpoints cannot answer the WOREE question.** They are evaluation-split models (the diseases of the test area
   have their treatments removed). Prediction for a named disease needs a model trained with `full_graph` (README);
   that checkpoint is not released, and a third party asking for fine-tuned weights has no answer (issue 31, open).
3. **Running them needs a legacy stack** (Python 3.8, DGL 0.5.2) and a graph build from the 1 GB `kg.csv` — not heavy
   in disk but a separate environment this task was told not to build.
4. **The published metric is itself contested by third parties** (`THIRD-PARTY`, issues open on 2026-10-26, not
   reproduced here): issue 29 reports mean AUPRC 0.032 against the published 0.437 with the released checkpoints;
   issues 25 and 23 report values 0.1-0.2 lower than the paper's and inconsistent between runs; issue 18 reports
   output that does not match the explorer (its author later wrote that `full_graph` fixed his case; a later commenter says it did not for them); issue 17 is about access to zero-shot embeddings, not an explorer mismatch. A reply in the thread suggests the paper's AUPRC pairs each positive with one
   random negative; that is the reply's speculation, unverified.
5. **No WOREE performance can be assumed from general results**: no evaluation of TxGNN on WWOX-DEE exists in what was
   found, and the structure in 1.3 says why it would not be a fair test of gene-level information.

### 1.5 Reopening conditions (what would make it useful)

Any one of: (a) a dated, versioned, downloadable prediction table with a stated licence that includes the DEE group;
(b) a released `full_graph` checkpoint with a stated licence **and** a maintainer-confirmed reproduction of the paper
metric; (c) a case where a card has a concrete drug-disease question that a graph-neighbourhood predictor could
discriminate — then run `disease_eval` on CPU in a Python 3.8 environment, with a frequency/lookup baseline on the same
split (the roadmap's own rule for predictors), keeping the output as a prediction. Until then the survey row stays WATCH.

## 2 · Every Cure MATRIX

### 2.1 Origin, version, terms (code and data separately)

| Part | Version measured | Terms | Status |
|---|---|---|---|
| Pipeline code `everycure-org/matrix` | `main` = `25e1272fe14f4029627e91e1ad90a576e312ade4` (2026-10-13, the drug_list v1.9.3 commit the roadmap names); latest release `v0.15.0-matrix` (2026-02-05) | **Apache-2.0** (GitHub licence API) | MEASURED |
| Scores `everycure/matrix-scores` | HF commit `d6b121bf38112cf28e7c813d0a062651757c52a1`, last modified 2026-07-01, about 39.5 M pairs, 11 parquet shards | **no licence in the dataset card metadata, no LICENSE file, no licence section in the card**; the Every Cure "Public Data Releases" page lists only kg-nodes, kg-edges, drug-list and disease-list as published datasets and states CC BY 4.0 for "the public datasets" — `matrix-scores` is not among them. **Status: licence undeclared** | MEASURED |
| Drug list `everycure/drug-list` | HF commit `dc75f85084baf6f014bb8242cacf14e2b301715d`, 2026-10-13, 1 935 rows | **CC BY 4.0** declared in card | MEASURED |
| Disease list `everycure/disease-list` | HF commit `c302a048c4018c94c855635a14849ca4a848e95f`, 2026-08-03, 23 224 rows | **CC BY 4.0** declared in card | MEASURED |
| EC knowledge graph `kg-nodes`, `kg-edges` | HF commits `c9c60b2c55e72cedb757b0422f4ea160a9bffc5c`, `fcd0585957ab5137771b256dad3714dcaf44b7db` (2026-05-28) | CC BY 4.0 for Every Cure's integration only; upstream licences (including Share-Alike / Non-Commercial where present) **remain in force** per its `LICENSE.md` | MEASURED |

Consequence: the scores table was read **once into scratch, never committed**; the repository holds only aggregates
(`matrix_trial_summary_20261026.json`) and the four shard digests-of-record. Reuse of the scores beyond this note waits for a
stated licence. Nobody was contacted to ask for one.

### 2.2 Provenance and evaluation method (docs read: "Deep dive: Evaluation suite", "Ground Truth Lists", "Matrix generation")

- The model is trained on a ground truth of curated positives/negatives (KGML-xDTD set, the Every Cure indications list)
  over a graph merged from ROBOKOP and RTX-KG2; scores exist for every drug × disease pair of two curated lists.
- Its published evaluation is **population-level**: Recall@n and AUROC over the whole matrix, Hit@k and MRR over
  diseases that already have a known positive in the test set, accuracy/F1 over known positive/negative pairs, plus a
  time-split on 2023 trial data and an off-label set. **No metric is computed for rare monogenic encephalopathies or
  for any disease without a known positive**, which is exactly the WOREE situation (see 2.3).
- The card names its three outputs "probabilities" and the transformed score blends the raw treat score with drug-wise
  and disease-wise rank terms. Under the module's rules (`harness_mandate_20261022.md` § 5) none of that may be used as a
  probability of efficacy, as a score in a join, or as a best-candidate ordering. The survey already records MATRIX as
  "a list without provenance as a candidate universe".

### 2.3 The small extract and what it shows (`matrix_scores_extract.py`, `matrix_scores_from_shards.py`, `matrix_trial_summary.py`)

Route: the datasets-server `filter` API answered 5xx/422 for most of 20 minutes (a first full page of 1 748 rows came
through once), so the table was read from the 11 shards instead (about 3.8 GB to scratch, deleted after; SHA-256 of each
shard is in the summary JSON). Rows for five disease nodes were extracted; aggregates only are kept.

| Node | Scored against | Publisher's training/evaluation flags set (known positive / known negative / trial / off-label) |
|---|---|---|
| DEE28 = WOREE (MONDO 0014533) | 1 748 drugs | **none** |
| SCAR12 (MONDO 0013687) | 1 748 | none |
| undetermined early-onset EE (MONDO 0018614) | 1 748 | none |
| DEE1 (MONDO 0010632), a sibling used as a specificity control | 1 748 | none |
| genetic DEE parent (MONDO 0100062) | 1 748 | 6 off-label flags |

Over the whole table: 24 371 disease nodes, 25 046 known-positive pairs, 38 408 known-negative pairs. So the WOREE node
has **no label**: the model had nothing to learn from for it directly — its scores come from the graph neighbourhood.

Specificity test (aggregate, no per-drug value): agreement between disease nodes in how the 1 748 drugs are ordered by the
raw treat score.

| Pair | Spearman rho | top-50 overlap |
|---|---|---|
| DEE28 vs DEE1 | 0.84 | 30 of 50 |
| DEE28 vs genetic-DEE parent | 0.83 | 32 |
| DEE28 vs SCAR12 | 0.82 | 29 |
| DEE28 vs undetermined EOEE | 0.79 | 29 |
| **baseline: DEE28 vs 86 other disease nodes** (deterministic hash sample of 100 nodes, keeping the 86 that share at least 1 000 drugs with the WOREE node; not matched) | median 0.66 (min 0.13, max 0.81) | median 8 (max 26) |

`INFERENCE`, stated with its limit: the WOREE node's ordering matches its neurological siblings more closely than a
typical unrelated node (top-50 overlap 29-32 against a median of 8), but it matches them about as well as they match each
other, and SCAR12 — a different clinical entity — is as close as DEE1. This is what a neighbourhood-driven prior looks
like; **nothing in the extract shows information specific to WWOX loss**. The baseline sample is not matched for node
degree or disease class, so the 0.66 median is a rough yardstick, not a null distribution. The test says nothing about
whether any listed drug works.

### 2.4 Coverage of the module's candidate axes in the drug list (identifier level only)

Present in `drug-list`: sodium phenylbutyrate and glycerol phenylbutyrate, TUDCA, ursodeoxycholic acid, bortezomib,
stiripentol, vigabatrin, cannabidiol, valproic acid, fenfluramine, ganaxolone, arimoclomol, metformin, nicotinamide,
alpha-lipoic acid, beta-hydroxybutyrate ketone esters, trazodone, guanabenz, fasudil (added in the drug_list v1.9.3
commit; listed `NOT_APPROVED`, which is a regulatory label, not a reading about WOREE). **Absent:** dichloroacetate (the
PDK card), amlexanox (readthrough card), ISRIB and salubrinal (ISR card). A drug that is absent cannot be scored or
screened out by MATRIX; absence is not a negative about the drug.

The Every Cure KG itself (`kg-nodes`, 7.35 M nodes, read from its shards) holds nodes for WWOX (`NCBIGene:51741`), DEE28,
SCAR12, undetermined EOEE, PDK1-4, LDHA/B, PDHA1, EIF2AK2/3/4, EIF2S1, ATF4, DDIT3, PPP1R15A/B. One label defect: the
node `NCBIGene:27102` is named "STK33 protein, human" while its identifiers (HGNC, UniProt Q9BQI3, Ensembl) are those of
**EIF2AK1** (HRI), the ISR kinase — checked against NCBI, UniProt and HGNC. A name-based match for HRI in that graph would
miss it and a symbol join would mislabel it; use the identifiers.

### 2.5 What MATRIX is allowed to be here

- **Allowed:** the CC BY 4.0 drug and disease lists as an identifier spine (MONDO / CHEBI / EC ids) and, if a card needs it,
  a statement of whether a compound exists in the list; with attribution to Every Cure.
- **Not allowed:** a per-drug score, rank, "top candidates" list or any probability from the scores table in a LEGEND
  record, and no use of the table until its licence is declared.
- **Reopening conditions:** (a) a licence is stated for `matrix-scores` (a file, a card field or the Public Data Releases
  page); (b) a held-out evaluation exists for diseases without a known positive, ideally monogenic encephalopathies;
  (c) the roadmap's P1 drift check (catalogue v1.9.0 against v1.9.3 with the same scores) is wanted — it needs a public
  v1.9.3 scores table, which this package did not find (HF scores last modified 2026-07-01, older than the catalogue
  change of 2026-10-13).

## 3 · Cost

Zero external spend. Network: about 4.3 GB to scratch (11 score shards, 8 KG-node shards, the 1 GB PrimeKG stream read
twice without storing, small lists); scratch environment `duckdb` + `pyarrow` via `uv` outside the repository; time about
two hours of which most was waiting on a rate-limited, unstable service. Nothing was installed in the repository.

## 4 · Claims for independent verification (producer ≠ verifier)

1. `matrix-scores` carries no licence: the HF dataset API `cardData` has no `license` field; the repository tree has only
   `README.md` and the parquet shards; the card text has no licence section; the docs "Public Data Releases" page lists four
   datasets without it.
2. `drug-list` and `disease-list` are declared CC BY 4.0; `kg-nodes` / `kg-edges` carry the pass-through `LICENSE.md`.
3. PrimeKG record on Dataverse declares CC0 1.0 and the PrimeKG README disclaims it for the dataset content; `kg.csv` md5 is
   `aac8191d4fbc5bf09cdf8c3c78b4e75f` on the record and from the stream.
4. In the Dataverse PrimeKG file `kg_grouped_diseases.tab` (which lists 14533 and 13687 as disease rows with their group names; a same-named `.csv` also sits at `txgnn/data_splits/` in the TxGNN commit, path in its git tree, which the first verifier did not find) and in PrimeKG `nodes.tab`, MONDO ids 14533 and 13687 are members of the
   grouped nodes 28005 and 27803; there is no node named WOREE; WWOX is node 602 with 0 `drug_protein` rows.
5. `MONDO:0014533` and `MONDO:0013687` exist in `disease-list`; the five-node extract has no known-positive flag on the first
   four nodes and has 1 748 rows each in the shards of commit `d6b121bf…`; the Spearman / top-50 figures in 2.3 (recompute
   with `matrix_trial_summary.py` on a fresh extract; the baseline needs `matrix_scores_from_shards.py`).
6. TxGNN: last commit date 2024-05-06; PyPI 0.0.3 sdist build failure; DGL 0.5.2 has no cp312 wheel; the checkpoint zip holds
   55 checkpoints (11 splits × 5 seeds) and no `full_graph`; `txgnn.org` returned 503 on 2026-10-26 (service state may change).
7. The third-party reproduction reports are quoted from open GitHub issues 29, 25, 23, 18, 17, 31 as they stood on
   2026-10-26; their numbers were **not** reproduced and may be wrong.
8. EC KG node `NCBIGene:27102` is labelled "STK33 protein, human" with EIF2AK1 identifiers.

## 5 · Limits

Reading depth is database/documentation, never a paper full text. The MATRIX evaluation description comes from the
vendor's own documentation, not an independent review. `matrix_scores_extract.py` (the API route) was run through one
complete 1 748-row disease once before the service degraded; its final retry settings were not run to completion — the
shard route (`matrix_scores_from_shards.py`) produced every number above. The baseline in 2.3 is a convenience sample.
Nothing here changes the working model, a registry or a claim.
