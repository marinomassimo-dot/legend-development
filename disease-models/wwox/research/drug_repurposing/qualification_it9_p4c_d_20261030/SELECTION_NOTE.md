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

## Part 2. Result of applying Part 1 (2026-10-30; produced by `select_p4c_d.py`, tables `selection_pool.tsv`, `selection_clusters.tsv`, `selected_p4c_d.tsv`, `excluded_selection_p4c_d.tsv`)

### 2.1 The six families (rule outcome, not re-chosen)

| # | Family (cluster: main target, arm) | Q / seed | Slot | Representative chosen by | Feasibility facts at selection (ChEMBL, fetched 2026-10-30) |
|---|---|---|---|---|---|
| 1 | apabetalone (BRD4, opposes) | Q5 / TNF | reserved BET axis (1.5) | highest max_phase in cluster (3) | small molecule, phase 3, no ATC; other eligible BET members: molibresib 2, birabresib 2, ezobresib 2, mivebresib 2, amredobresib 2, pelabresib 3 (L01XX84), RO-6870810 1 |
| 2 | JTE-151 (RORC, opposes) | Q5 / IL6 | order (a to e) | only eligible opposes member | small molecule type 'Unknown' in ChEMBL, phase 1; re-open allowed by 1.5 |
| 3 | infigratinib (FGFR3, mimics) | Q5 / IL1B | order (a to e) | max_phase 4 tie with futibatinib and pemigatinib; lowest family id | L01EN03, oral; flagged `oncology_targeted` |
| 4 | dimethyl fumarate (KEAP1, mimics) | Q5 / TNF | order (a to e) | max_phase 4 tie with diroximel fumarate, equal z; lowest family id | L04AX07, oral; prodrug family of monomethyl fumarate |
| 5 | gamcemetinib (MAPKAPK2, opposes) | Q4 / NPY | order (a to e) | only eligible member | name-exact identity UNVERIFIED (no structure check); phase 2 |
| 6 | ceralasertib (ATR, mimics) | Q4 / GRIN2C | Q4 slot (1.3) | max_phase 3 | no ATC; ATR inhibitor |

Counts (units: ChEMBL parent x cluster rows): pool 362 (360 distinct parents or unresolved families) from 439 pool rows (Q5 355 + Q4 84); 64 clusters (main target, arm); clusters with at least one eligible parent 31; exclusions (a row can carry several): E6 no human-exposure statement 193, E5 identity unresolved 153, E8 promiscuous 38, E4 modality 7, E1 round-1 5, E7 withdrawn 4, E3 topical 3; dispositions: selected 6, excluded 234, not taken (not representative or cap) 122.

### 2.2 The two Orchestrator axes

* **BET axis:** one slot reserved and filled (apabetalone as representative by phase). Other BET members are kept in `selection_pool.tsv` with their z values; the qualification record covers BET inhibitors as a class (tool compounds JQ1 and I-BET762/molibresib, birabresib, pelabresib) for CNS exposure and class toxicity, but the candidate of record is apabetalone.
* **HMGB1 axis: NO eligible family; not forced in.** bifonazole (HMGB1 -T-> IL1B; ChEMBL phase 4) is excluded E3 (topical only by ATC D01AC10; no oral or parenteral route); CD24Fc is excluded as a biologic (an Fc fusion protein; the code marked it E8 promiscuous, 5 signed targets, because ChEMBL types it 'Unknown' and the modality test did not fire; the exclusion intended by 1.2 E4 is the same outcome); L6H21 (LY96 -P-> HMGB1 -T-> IL1B) and neoceptin-3 are excluded E5 (identity unresolved) and E6 (no human exposure). The decisive edge of the whole axis, HMGB1 -T-> IL1B, is nevertheless read in Part 3 for BET-independent reasons (it is the top Q5 text-mined edge with 78 references), as an edge reading with no compound qualified.
* **Omaveloxolone** (NFE2L2 -T(-)-> IL1B, approved, eligible) was NOT taken: the ordering key (a to e) put six other clusters first (its z, capped at 20, was 6.6 and its seed IL1B was already represented). It is listed as the first not-taken eligible cluster with a stated rule reason, not as a judgement of merit.

### 2.3 Case-by-case judgments required by 1.2 E2 (oncology-targeted agents; written before Part 3)

* infigratinib is an oral FGFR1-3 tyrosine kinase inhibitor (cholangiocarcinoma) kept eligible because ChEMBL/registry knowledge suggests a paediatric non-oncology programme (achondroplasia); that expectation is general knowledge, UNVERIFIED, and is checked in Part 3 (registry search); if absent the exposure statement is oncology-only.
* ceralasertib is a DNA damage response (ATR) inhibitor developed with chemotherapy or immunotherapy; no chronic non-oncology use is known to me (UNVERIFIED). It stays because 1.2 excludes only cytotoxic agents and 1.3 reserves a Q4 slot; its Q4 base is the weakest (ATR -P-> ETV1 -T-> GRIN2C). A DROP on the edge or on neurodevelopmental toxicity is an admissible outcome.
* The other flags: none.

### 2.4 Deviations from Part 1 and incidents (disclosed)

1. **Tie-break implementation.** The first run of `select_p4c_d.py` ordered ties inside a cluster by `-len(family_ids)` instead of by lowest family id as written in 1.3. The only changed outcome: cluster KEAP1 (mimics) had diroximel fumarate (one DGIdb-only family id, name-matched identity) as representative; with the written tie-break it is dimethyl fumarate (ChEMBL id). The first-run table is kept as `selected_first_run_tiebreak_bug.tsv`; the code was corrected and the selection recomputed offline from the saved pool (`select_p4c_d.py reselect`). Seen before the correction: the first-run names.
2. **Service log.** The first live run crashed at its last statement (writing the service log from list rows); all tables except `selection_service_log.tsv` had been written. The live part was re-run in full after the fix (log kept; the pool table of the re-run is compared with the saved one in the README).
3. **Code gap, no outcome effect:** CD24Fc modality (2.2).
4. Identity of 'name_exact_unique' parents (gamcemetinib, among others) is UNVERIFIED by structure; verification is item 1 of its record.
