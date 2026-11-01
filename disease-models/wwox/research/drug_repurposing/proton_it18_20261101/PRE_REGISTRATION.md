# IT18 P-PROTON pre-registration: does PROTON add drug-target relations for the WWOX needs' intervention targets?

Written 2026-11-01 by `scientist`, **before any PROTON score was computed** and before any NeuroKG `drug_protein` edge of the target genes was inspected. At writing time only the following had been looked at: the PROTON code at `7d2bae9feeca`, the Hugging Face file listing, the Dataverse dataset record, the NeuroKG node table (node types, the WWOX / DEE28 / SCAR12 node rows), the 94 ordered edge types and the first rows of `edges.csv`. Non-canonical research material; not medical advice; computational link prediction only, no benefit claim. Public edition, WWOX-DEE genotype class.

## Question
For the intervention-target genes of the module's needs (`needs/needs.json`, `target_kind == intervention_target`; 45 distinct genes), does PROTON's `drug_protein` link prediction (a) rank drug-target relations that LEGEND's catalogue holds but NeuroKG lacks above simple baselines, and (b) propose relations absent from both that an independent record supports, more often than a baseline does? Can the LEGEND contextual path (need direction + documented action direction) qualify the relations PROTON adds?

## Universe and inputs (fixed)
- PROTON artefacts: Hugging Face `mims-harvard/PROTON` at revision `6ae9fb07b734`: `embeddings.pt` (sha256 `e4fadfb7ddc7dec28f609085d5b3277e686b3f2fec4c9057a613b90a9abb25e1`), `decoder.pt` (`eda13520906f968c1ca6c8131b5491f8a798e226d53a17af0ce3cb2661d32c47`), `edge_types.pt` (`39600af074270d6cc960b0d4e1cab5eb24c96c5a76e0fb003b275a82f4bfbda4`). No checkpoint, no training, no fine-tuning.
- Graph: NeuroKG, Dataverse `doi:10.7910/DVN/ZDLS3K` version 1.0: `nodes.csv` (md5 `e0e120d82fefa9c054f2a1584b2d10ab`), `edges.csv.zip` (md5 `7aff4066087f7f16b10c72916faf5f5e`).
- Relation scored: `('drug', 'drug_protein', 'gene/protein')`, its index in the ordered edge-type list; score = sigmoid(sum(leaky_relu(e_drug) * w_r * leaky_relu(e_gene))), the formula of `HGT.get_scores_from_embeddings` at the pinned commit.
- Drugs: all 8,160 NeuroKG drug nodes (DrugBank ids). Genes: the 45 intervention-target symbols matched to NeuroKG `gene/protein` node names; unmatched symbols are reported, not substituted.
- LEGEND reference: `catalog/catalog.jsonl.gz` as committed on `it18-orch` (`2e327c22`), target rows with `source == "ChEMBL curated mechanism"`, `direct_interaction == 1`, organism `Homo sapiens`, gene symbol equal to the target gene. The catalogue compound is joined to the NeuroKG drug node through the catalogue's DrugBank id (`ids.drugbank`), parent and child entries both counted once per drug node. Primary stratum: `target_type == SINGLE PROTEIN`; group-level rows (PROTEIN COMPLEX / FAMILY / GROUP) are a secondary stratum, because ChEMBL spreads one group action to all components (defect found in `../matching_it18_p4_20261101/`).

## Pair classes
For each (target gene g, drug d):
- **G, in graph**: NeuroKG holds a `drug_protein` edge between d and g. A training relation; never counted as a prediction, never evaluated.
- **R, LEGEND-only reference**: not G, and the catalogue holds a qualifying mechanism of d on g.
- **U, unknown**: all others. Unknown is not negative.

## Methods compared (same candidates per gene: all drugs not in G for g)
- **P, PROTON**: the score above.
- **B1, degree**: number of NeuroKG `drug_protein` edges of d (the popularity a degree-sensitive model can exploit; the paper names this bias).
- **B2, neighbourhood**: number of NeuroKG `drug_protein` targets t of d (t != g) with a NeuroKG `protein_protein` edge t-g; ties broken by B1.
- **B0, random**: expected percentile 0.5, recall@5% = 0.05.
- **L, LEGEND contextual**: labels, not ranks: for a relation with a catalogue action direction and a need with direction down/up, compatible or opposite; otherwise indeterminable with its reason (need direction uncertain; no documented action direction).

## Primary measure (a)
Per R pair, the percentile rank of d among g's candidates (average rank for ties; 0 = best). Pooled over R pairs: recall@5% (share with percentile <= 0.05), recall@1%, median percentile, per method. Stratified by whether d has a G edge to another target gene of the same need (sibling transfer; a trivially easier case) and by SINGLE PROTEIN vs group level.

**Decision rule (a).** "PROTON ranks LEGEND-only relations better than the simple baselines" only if: at least 20 R pairs (SINGLE PROTEIN stratum) over at least 5 genes; PROTON recall@5% exceeds the better of B1 and B2 by at least 10 points; and a two-sided paired sign test on per-pair percentiles (PROTON vs that baseline) gives p < 0.05. Fewer pairs: figures reported, no statement. Recovery of R pairs is retrospective validity of the link predictor, **not** generative capability.

## Secondary measure (b): added information
For the 13 genes of the three directed needs (EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, SEIZURE-CONTROL-SYMPTOMATIC, T-TYPE-CALCIUM; direction down) present in NeuroKG: the top 5 U drugs per gene by P and by B2. Each (drug, gene) is checked once against ChEMBL activities (public REST, plain GET, no key): supported if any activity on a human SINGLE PROTEIN target of that gene has `pchembl_value >= 5`. The DrugBank-to-ChEMBL map is the catalogue's; a drug without a catalogue ChEMBL id is **unmappable** (abstention, not a failure). Reported: supported / not supported / unmappable per method, and how many supported P relations L can label compatible or opposite. ChEMBL activities are not independent of NeuroKG's ChEMBL-derived edges in source; they are a different record type (bioassay vs clinical/mechanism evidence) of the same database, stated as such. A supported relation is a binding/activity record, not a direction, not a benefit.

## Tertiary, descriptive (c): is WOREE a distinct node for PROTON?
NeuroKG has a DEE28 node (MONDO 0014533, node 30298). Indication scores of DEE28 over all drugs are compared with each sibling `developmental and epileptic encephalopathy, N` node and with `epilepsy` (39348) by Spearman correlation. If the median Spearman with siblings is >= 0.9, DEE28's ranking is recorded as **not shown to be WOREE-specific**. DEE28's own NeuroKG edges (indications, disease-protein incl. WWOX) are counted. WWOX `drug_protein` top predictions are recorded as discovery-only and not promoted.

## Stage-2 checks that gate the trial
1. The ordered edge-type list equals the sorted canonical edge types built from `edges.csv` (DGL orders canonical edge types this way, and the decoder row index depends on it).
2. Official example: the paper's full-model BD screen (Methods 4.3; Results) gives cholecalciferol #16, alfacalcidol #102, calcitriol #114 among 8,160 drugs. Reproduced if all three ranks are within +-2 of these from `embeddings.pt` + `decoder.pt` for node 39528 and relation `('disease','indication','drug')`. If not reproduced, the trial still runs and every figure carries the flag.
3. Sanity: AUROC of P on the G pairs of the 45 genes against an equal number of random U pairs of the same genes (seed 18). This is a training-set figure, reported as such.

## Conservation
Unknown is not negative; one curated origin counts once; PROTON, TxGNN and LEGEND's catalogue share DrugBank/ChEMBL lineage, so agreement is not independent confirmation; the published disease-centric splits are for 17 other neurological diseases and do not evaluate WOREE. No figure is rescued by widening the universe after the scores are seen.
