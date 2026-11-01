# IT18 P-PROTON — does PROTON add relations LEGEND does not retrieve, and can WWOX knowledge qualify them?

Actor `scientist`, 2026-11-01. Non-canonical research material; **not medical advice**; computational link prediction only. Public edition, WWOX-DEE genotype class. Nothing here is WWOX efficacy evidence. The preliminary Tier 1 classification was a reason to evaluate, not an adoption decision, and nothing below shows PROTON to work for WWOX.

Design fixed before any score: [`PRE_REGISTRATION.md`](PRE_REGISTRATION.md) (commit `a5f46424`). Tool: `proton_probe.py` (`--help` has no side effect; standard library except the `run` subcommand, which needs torch and numpy). Tests: `python3 test_proton_probe.py` (13 tests, verbosity 2, offline).

## 1 · Identity, availability, terms

Current revision re-resolved on 2026-11-01: code `7d2bae9feeca8e476e6ceedf973f389680cdd214` (2025-12-27) — **the same commit as the preliminary examination**; no commit since. Code, model and data are three separate artefacts with separate terms; the full table is [`availability_terms.tsv`](availability_terms.tsv).

| Part | What | Open? | Terms |
|---|---|---|---|
| Code | GitHub `mims-harvard/PROTON` | yes | MIT |
| Model | HF `mims-harvard/PROTON` rev `6ae9fb07b734`: `model.ckpt` 8.74 GB, `embeddings.pt` 301 MB (147,020 x 512), `decoder.pt` 284 KB (94 x 512), `edge_types.pt` (94 ordered types), `disease_splits/` for 25 neurological diseases | yes, not gated | MIT on the model card |
| Graph | NeuroKG, Dataverse `doi:10.7910/DVN/ZDLS3K` v1.0: `nodes` 10 MB, `edges.csv.zip` 250 MB (2.9 GB unzipped, 14,733,490 directed rows = 7,366,745 undirected edges x 2) | yes, no login; md5 of both files equal the record | CC BY 4.0 on the record |
| Upstream sources | DrugBank 5.1.10 (drug-protein edges), ChEMBL via Open Targets 23.09, SIDER, DisGeNET, UMLS, CTD and 30 others | mixed | **not cleared by the CC BY 4.0 record**: DrugBank open data CC BY-NC 4.0 and full XML under an academic licence; SIDER CC BY-SA 4.0; DisGeNET and UMLS not verified (restricted use known) |
| Paper | arXiv 2512.13724v1, preprint | yes | CC BY 4.0 (paper p15) |

The Dataverse deposit is open: the one-endpoint error the brief warned about did not occur here (native API 200, both files downloaded).

**Coverage** ([`coverage.json`](coverage.json), from `coverage`):

| Entity | In NeuroKG? | Detail |
|---|---|---|
| WWOX (NCBI Gene 51741) | yes, node 602 | `drug_protein` edges: **0** (no ligand, as in PrimeKG and ChEMBL); disease neighbours include DEE28, SCAR12 and the DEE group term |
| **WOREE = DEE28** (MONDO:0014533) | **yes, its own node 30298** "developmental and epileptic encephalopathy, 28" — unlike PrimeKG, where it was merged into an 87-member group | 1 `disease_protein` edge (WWOX), 26 phenotypes, 2 disease-disease; **no drug edge of any type** |
| SCAR12 (MONDO:0013687) | yes, node 33934 | disease_protein WWOX and SIL1; no drug edge |
| DEE group term (MONDO:0100062) | yes, node 36594 | 70 disease genes; indication vigabatrin; off-label corticosteroids and tetracosactide; strong evidence cannabidiol |
| the word "WOREE" | absent as a node name | a synonym, not a node |
| 45 intervention-target genes of the needs | **all 45 present** | `drug_protein` edges: 0 for EIF2AK3, EIF2B1-5, TNKS, TNKS2, NLRP3; 1-3 for EIF2AK4, PDK1-4, PANX1, RELA, STAT3, NFE2L2; up to 104 (CHRM1) |
| node tables, mappings | yes | nodes with source ids (NCBI, MONDO, DrugBank, HPO, GO...); `data/mappings` in the code repo documents DrugBank/MONDO-EFO/HGNC mapping files |

No DEE or WOREE disease-centric split exists: the 25 released splits are other neurological diseases (epilepsy is one), and the paper evaluates 17 of them (p48). A published split for another disease is not an evaluation for WOREE.

## 2 · Minimal execution path (ran)

Precomputed embeddings + decoder, no checkpoint (the 8.74 GB file was not needed and not downloaded). Throwaway venv outside the repository (CPU torch 2.5.1, numpy). Score = sigmoid(sum(leaky_relu(e_x) * w_r * leaky_relu(e_y))), the formula of `HGT.get_scores_from_embeddings` at the pinned commit; decoder pickle read with an allow-list of four globals.

| Check (pre-registered) | Result |
|---|---|
| relation order: `edge_types.pt` equals the sorted canonical edge types built from `edges.csv` | **equal** (94 = 94) |
| official example: full-model BD screen, cholecalciferol #16, alfacalcidol #102, calcitriol #114 of 8,160 (paper p10) | **reproduced exactly**: 16, 102, 114 |
| sanity on training pairs (622 in-graph drug-target pairs of the 45 genes vs 622 random pairs) | AUROC 0.72 (a training-set figure) |
| operating cost | 9 s wall, 0.39 GB RAM for every score in this package; one 2.9 GB streaming pass (about 1 min) for the graph extract; 560 MB of downloads; zero spend |

## 3 · Comparative trial (pre-registered, one question)

Question: for the 45 intervention-target genes, does PROTON's `drug_protein` prediction add drug-target relations LEGEND lacks? Outputs: [`results.json`](results.json), [`reference_pairs.tsv`](reference_pairs.tsv), [`top_unknown.tsv`](top_unknown.tsv), [`chembl_check.tsv`](chembl_check.tsv).

**(a) Recovery of LEGEND-only relations — not evaluable.** Of the catalogue's ChEMBL curated mechanisms on the 45 genes that map to NeuroKG drugs, 65 of 83 (78 percent) are already NeuroKG edges (in-graph, excluded as training data: e.g. 6 of 9 per T-type gene, 4 of 5 for GRIN1). Only **18 LEGEND-only pairs** remain, over 12 genes, and **1** is SINGLE PROTEIN (filgotinib-JAK2). The rule needed 20 over 5 genes: **figures only, no statement**. The 17 group-level pairs are dominated by the ChEMBL group defect found in `../matching_it18_p4_20261101/` (gabapentinoids spread to CACNA1G/H/I; dichloroacetate to PDK1-4). Descriptively, recall at 5 percent: PROTON 0.29, B2 neighbourhood 0.24, B1 degree 0.00 on group-level pairs; PROTON ranks the gabapentinoid-T-type pairs high and the NMDAR group pairs low (B2 does the opposite). 58 catalogue DrugBank ids are not NeuroKG drug nodes.

**(b) Added information — no supported relation from either method.** For the 13 genes of the three directed needs, top-5 unknown drugs per gene, checked against ChEMBL bioactivities (pChEMBL >= 5): **PROTON 0 of 61 mappable supported (4 unmappable); B2 0 of 56 (9 unmappable)**. Positive controls of the query: mibefradil-CACNA1G 23 records (works); memantine-GRIN2B 0 on SINGLE PROTEIN targets but 7 when PROTEIN COMPLEX targets are included, so the registered check is blind to receptor-complex records; the post-hoc variant with complexes ([`chembl_check_posthoc_complexes.tsv`](chembl_check_posthoc_complexes.tsv), not pre-registered) still gives **0 supported for both**. L, the contextual path, labels all PROTON-added relations **indeterminable**: PROTON predicts an undirected link without action, and no added relation has a curated mechanism.

**Non-specificity of PROTON's added links (descriptive, post hoc).** Scores are saturated: for the median gene, 99.9 percent of candidate drugs score above the model's 0.5 threshold and 50 percent above 0.9, so only ranks carry information. Across all 45 genes the 225 top-5 slots hold **33 distinct drugs** (B2: 83); obinepitide is top-5 for 30 genes, beta carotene 23, N-cyclohexyltaurine 15, bepridil and caffeine 14 each (added after independent verification). The same few drugs are proposed for NMDA, AMPA, T-type, GABA-transaminase and pannexin targets alike: a hub pattern, not target knowledge.

**(c) Is WOREE distinct for PROTON? No.** DEE28 indication scores over 8,160 drugs correlate with its 87 numbered DEE siblings at median Spearman **0.973** (range 0.894-0.997; epilepsy 0.812): **not shown to be WOREE-specific**. DEE28 has no drug edge; its top-ranked drugs (benzylpenicillin, prednisolone, triheptanoin, bevacizumab, dexamethasone...) mirror the group's corticosteroid edges and generic hubs. Recovery of known DEE-group drugs is not generative capability. WWOX `drug_protein` top-10 (obinepitide, encenicline, zinc acetate...) is recorded in `results.json` as discovery-only and not promoted.

**Independence and leakage.** NeuroKG drug-gene edges come from DrugBank and from ChEMBL via Open Targets (paper p25-26); LEGEND's catalogue is ChEMBL-based, TxGNN's PrimeKG shares the DrugBank backbone: agreement among them is not confirmation. ChEMBL bioactivities used in (b) are a different record type of the same database. The paper's 0.9145 AUROC is a random 80/15/5 edge split (p38), and its disease-centric splits cover 17 other diseases (p48).

## 4 · Scientific limits for WWOX

- **Undirected graph** (p23, p33): a predicted link carries no agonism/antagonism, no useful direction, no stabilisation, compensation or benefit. WWOX knowledge can declare the need's direction, but cannot qualify an undirected link: every added relation stays indeterminable.
- **Adult brain atlases** (p3-4: 3.76 million cells from adult donors; PD nuclei): no developing-brain, infant, cell-type-of-onset or genotype layer; nothing represents WWOX loss of function, its alleles or the developmental window of WOREE.
- **Sparse rare diseases and degree bias** stated by the authors (p13): DEE28 has one gene edge and no drug edge, and the measured hub concentration is the bias they describe.
- PD, BD and AD results stay evidence in their own systems; none transfers to WOREE.

## Decision

**Discard for the current question** (drug-target relations for the WWOX needs' targets): PROTON runs proportionately and reproduces its own published example, but on this question it added no supported relation (0 of 61), its added links are non-specific hubs, it cannot express direction, WOREE is not distinct from other DEEs in its space, and the LEGEND-only reference is too small to measure recovery. No hypothesis emerged; **no card, IPOTESI or queue entry was created**, and no compound was promoted.

Reopen if any of: a signed or directed drug-target relation (or a mechanism-level head) is released; a developmental-brain or WWOX-relevant cell-type layer is added to NeuroKG; a DEE/WOREE disease-centric split or fine-tune is published; or an independent per-edge-type evaluation shows `drug_protein` ranking beyond degree/hub baselines. The minimal path above (embeddings + decoder, about 10 s) makes any reopening cheap.

## Reading and receipts

Targeted reading of the paper (arXiv PDF) under the standing method: receipt [`receipt_FTR-20261101-ARXIV2512.13724-01.json`](receipt_FTR-20261101-ARXIV2512.13724-01.json), `partial_fulltext_read`, 19 page locators; `record --dry-run` passed against the ledger tail `614dacd8`; staged for the integrator to record. Artefacts in the shared `files/fulltext/`: the paper PDF and the supplement PDF (digests in the receipt). Earlier comparable outcome: TxGNN reasoned wait (`../p3b1/txgnn_matrix_outcomes_20261026.md`).

## What is in git and what was removed

In git: this README, the pre-registration, the tool and its tests, coverage and results JSON, four TSVs of ids, ranks and coarse classes, the receipt JSON. Not in git: no PROTON weights, no NeuroKG rows, no third-party README or contact. Removed from scratch after the run: the venv (780 MB), embeddings/decoder/edge types (301 MB), NeuroKG nodes and edges (258 MB), the code clone (45 MB), the graph extracts and the ChEMBL response cache.

## Verification note (2026-11-01, independent actor; added)
Confirmed: licences, node/edge claims (needs.json holds 47 intervention-target rows over 45 distinct genes), the 0/61 versus 0/56 check, saturation figures, decision perimeter, receipt shape, 13 tests. Not provable from git: that no scratch score was computed before the pre-registration commit (the digests of the pre-registered inputs equal those used). Open minor point: the AUROC uses 622 positive pairs while `coverage.json` sums to 625 edges over distinct genes; unexplained, does not touch the decision. The two positive controls (mibefradil 23 records, memantine 7 with complexes) are documented only in this README, not in a data file.
