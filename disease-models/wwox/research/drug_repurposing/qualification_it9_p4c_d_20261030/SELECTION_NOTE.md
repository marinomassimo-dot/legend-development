# IT9 P4c-D selection note (second qualification round, v3 generation path)

Scientist-a4, 2026-10-30, branch task/it9-p4c-d (from main 0ddd02cf). Exploratory, computational; not medical advice. A compatible action of a context-free signed network is not a predicted benefit. Reference genotype: a WWOX-DEE genotype class; no individual-level record.

## Part 1. Rules (written 2026-10-30 BEFORE any ChEMBL, ATC, phase, route, literature or edge-record datum was fetched for any pool family, and before any family was chosen)

### 1.0 What had been seen before this part was written (disclosure)

* Read: `generation_it9_p2_20261030/v3/README.md` and `PRE_REGISTRATION_V3.md`; `exploration_it9_p3_20261030/selection_rules.md` (rules applied again, below); the P4b round-1 READMEs (headline decisions).
* Seen: the `name`, `arm`, three z values and first edge chain of the first rows of `v3/results/candidates_Q5.tsv` and `candidates_Q4.tsv` (top 50 opposes, top 25 mimics, direct-search arms), and a cluster table of `v3_seed_specific_all_nulls.tsv` (Q5 and Q4 expression: main target, seed, arm, chain, up to 12 names per cluster). So the NAMES of many pool families and of the clusters were seen. No pharmacological, feasibility or literature datum was seen. The rule below was therefore written knowing that the BET, RORC, NFE2L2, EZH2, JAK2, ROCK2, BTK and HMGB1 clusters exist; it is mechanical and contains no family name except where the Orchestrator named an axis (1.5).
* Not seen: any ChEMBL field, any HGNC group, any card match, any literature count for any pool family.

### 1.1 Pool and unit

Pool = all rows of `generation_it9_p2_20261030/v3/results/v3_seed_specific_all_nulls.tsv` with question Q5 (expression; seeds IL6, IL1B, TNF up) or Q4 (expression; seeds NPY, GRIN2C and others), arms `opposes` and `mimics` (z beyond 3 in all three nulls, not prodrug-flagged; 355 + 84 rows). The `direct_search` arms (hop-0 target on a seed gene; Q5 are anti-cytokine biologics, Q4 are NMDAR ligands already carded) are not network proposals and are not in the pool. Q2, Q6 and Q4 protein are out of scope for this round.
Unit = ChEMBL parent compound (several catalogue families may share one parent). Cluster = (main target, arm), main target = first node of `edge_chain_main_target_to_seed_1`. One selected family per cluster; at most one cluster per HGNC mechanism group (first HGNC gene group of the main target; `NO_GROUP` counts as its own group per target).

### 1.2 Exclusions (feasibility axis, applied after and shown beside the promise columns; reasons are listed in `excluded_selection_p4c_d.tsv`)

E1 not in the pool of round 1 (curcumin, belnacasan, fosfestrol, balsalazide, ramelteon, belzutifan, ceperognastat, implitapide, harmine, pomalidomide, lenalidomide, defosbarasertib, AT-9283, pinometostat, sirolimus, AR-12, dichloroacetate, felbamate, memantine and every other P3-01 to P3-20 item); JTE-151 may be re-opened (1.5).
E2 P3 F1 cytotoxic anticancer (ATC L01A, L01B, L01C, L01D, L01XA, or a stated cytotoxic mechanism: topoisomerase, tubulin, DNA alkylation/synthesis). Targeted oncology agents are flagged `oncology_targeted`, kept eligible, and judged case by case in Part 2 with a stated reason for chronic neurological use.
E3 P3 F2 topical or local only. E4 modality: antibody, fusion protein, enzyme, vaccine, cell product, other protein (excluded as biologic with reason; an oligonucleotide or peptide is eligible only if ChEMBL type and route fit, judged in Part 2). E5 P3 F4: no ChEMBL parent (identity unresolved). Identity routes as in P3 Amendment 2; a family selected through a name-exact route is marked identity UNVERIFIED and the record starts with structure verification. E6 P3 F5: no human exposure statement (`max_phase` below 1 or absent and no approved/clinical status in the catalogue): tool compounds and research probes, stated as 'no human exposure information', not 'unsafe'. E7 P3 F6 withdrawn. E8 promiscuous: 5 or more signed targets in the v3 compound table (hub-artefact control logic of P3; none is taken as a candidate). E9 research codes and generic names such as 'Compound 12 [Pmid: ...]' resolve only through ChEMBL; unresolved ones fall under E5.

### 1.3 Ordering

Among clusters with at least one eligible parent, in this order: (a) mechanism group not yet represented in the selection; (b) seed gene (IL6, IL1B, TNF, NPY, GRIN2C ...) not yet represented; (c) not `class_known` to LEGEND (a card, IT8 P9 unit or queue match by catalogue id, or a name in `cards/` file names; a class-level match counts as class_known); (d) higher min(|z| of the three nulls), each |z| capped at 20; (e) lower catalogue family id. Representative of a cluster = eligible parent with the highest ChEMBL `max_phase`; ties: higher min|z|; ties: family id. (Choosing the representative by phase is a feasibility choice and is stated as such; the promise columns of the other members of the cluster are kept in the selection table.)
At most 6 clusters. At least one from Q4 expression if an eligible Q4 cluster exists (the Q4 list rests on 10 edges and 2 seed genes: the weakest base, reported as such). `opposes` and `mimics` are both eligible; which direction is useful depends on the unresolved valence, and the arm is recorded.

### 1.4 What the selection does not use

Potency, brain exposure, dose, safety, trials, counter-evidence, the quality of the edge record: all in Part 3 (qualification), after selection. The edge-provenance check of Part 3 may DROP a selected candidate; that is an outcome, not a reason to re-select within this round.

### 1.5 Orchestrator axes and the JTE-151 re-open (declared before the run)

The Orchestrator named the BRD4/BET axis and the HMGB1 axis as examples of mechanisms to include. Rule: each named axis reserves one slot if its cluster has at least one eligible parent under 1.2; if it has none, the axis is reported as excluded with the reason for each member (not forced in). JTE-151 may be re-opened only to fetch its published RORgamma potency and human data (round 1: INCONCLUSIVE for lack of these); if the RORC cluster is selected by the ordering rule, JTE-151 is its representative candidate and the edge reading of Part 3 applies as for any other. Slots reserved by 1.5 count toward the 6.

### 1.6 Limits (stated in advance)

Thresholds (z cap 20, promiscuity 5, 6 families, phase-based representative) are judgment settings fixed here, not tuned. HGNC group, ChEMBL and ATC fields may fail for some ids: the state is then UNKNOWN and the F-test 'not evaluable' (family stays eligible, flagged), never silently passed.
