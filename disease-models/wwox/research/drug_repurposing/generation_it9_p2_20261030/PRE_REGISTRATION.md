# PRE-REGISTRATION: seed-based generation engine, function and sensitivity proof (IT9 P2)

Scientist-b, 2026-10-30, written BEFORE the engine was run on any seed set. Exploratory. Computational. Not medical advice. The reference genotype
class is a WWOX-DEE genotype class; no individual-level record is used. This registration fixes what will be called a pass; it proves FUNCTION AND
SENSITIVITY of a method, **not** therapeutic accuracy, and no test below measures whether a proposed compound would help anyone.

## 0. What was opened before this file

Opened (inputs, descriptions): IT8 P4 README, IT7 P3 README and the code of its NET propagation, the IT7 P2 funnel README, the IT7 P1 subnetwork tables, the
catalogue file structure (field names of the target rows). **Not opened:** any score of this engine on any seed set; any LINCS z-score for this question; the P1
(IT9) seeds (the file did not exist at the time of writing). The engine did not exist yet.

## 1. Method (fixed)

**Seed vector s** over human genes: `s_g = direction x level`, where direction is +1 / -1 (the sign of the WWOX-loss change) and level in (0,1] (stated weight).
A seed whose direction is not established (`direction_status != defined`) keeps only a level and is **not** assigned a sign: it is run as conditional arms
(all uncertain seeds +, all uncertain seeds -), and because the score is linear the exact range over every possible sign pattern is also reported.

**Network**: the IT7 external signed network (SIGNOR via OmniPath + licence-filtered CollecTRI; 70,461 signed edges, 8,769 genes; complexes split into members;
edges with conflicting sign between duplicates dropped; weight sign/out-degree). It is context-free (no tissue, cell type, stage).

**Compound action vector a_f** of a family f: per target gene, mean of the signed actions (inhibitor/antagonist/blocker = -1; agonist/activator = +1) over the usable
rows of the family (catalogue rules of IT7 P2: stated action, not a catalogue artefact, human target with a stable identifier; conflicting up/down on the same gene
averages to 0 and the gene is dropped); unit L2 norm over the family's targets (promiscuity dilution, as in IT7 NET).

**Propagation**: signed K-hop, K = 3, damping 0.5 per extra hop (identical to IT7 NET), applied to the compound; by linearity this equals a backward propagation of the
seed vector, `v = sum_{k=0..3} 0.5^(max(k-1,0)) (H^T)^k s` (hop 0 = the seed gene itself), and the score is `Q_f = - sum_t a_ft v_t`.
Positive Q = the compound's predicted effect on the seed genes OPPOSES the seed change (reported as **compatible action: opposes**); negative = MIMICS.
It is a compatibility of directions through curated regulatory edges, not a predicted benefit, and it is at the level the network edges carry (regulation of
activity/expression), not at the protein or function level.

Arms (all from the same machinery, so every comparison is like with like):
* **DIRECT** (reference, hop 0 only): the family's own targets are seed genes. `Q_direct = - sum_{t in seeds} a_ft s_t`. This is the simple "target -> compounds" search
  with the direction kept. It assumes transcript direction ~ activity direction, stated as an assumption and not a finding.
* **NET-IND** (primary; hops 1-3 only, the registered IT7 primary excluded direct node effects for the same level reason) and **NET-FULL** (hops 0-3).
* **PROX** (unsigned proximity, NOT a benefit prediction): mean over the family's in-graph targets of the directed shortest-path length to the nearest seed
  (capped at 6, unreachable = 7), z-scored against 500 degree-matched random target sets of the same size (degree bins = in+out degree deciles). Reported as proximity only.
* **INTERACTOR reference**: families with a target among the network regulators of WWOX (the 7 in-edges: NFKB1, NFKB2, REL, RELA, RELB, TFAP2C, E2F1) are listed
  as a separate descriptive arm; no other WWOX interactor list is used as input (none is held in a signed, sourced form in the repository).
* **SIG** (signature route, secondary): for each LINCS GSE92742 compound signature in a neural cell context (NPC*, NEU*, MNEU.E), `O = - sum_g s_g z_g / sum|s_g|`
  over the seed genes present in the L1000 space (z = level 5, divided by the MAD scale of the signature, as IT7), median per family. Called informative
  only if it passes T2 and its cross-context reproducibility (progenitor-like vs neuron-like) exceeds the 95th percentile of random matched seed sets (as in IT7 C1); otherwise reported as not informative.

## 2. Firewall (what is excluded, fixed now)

Not inputs, anywhere: the held-out intervention-response data (T-type blocker, lithium, vigabatrin, dichloroacetate, gene addition, clinical series), the IT7 held-out
LINCS outcome `O_E` and its family scores, the compounds named on the cards, the card `stated outcome` fields, and any statement of which compound "should" win.
Seeds may come only from transcript or measured-state contrasts of WWOX loss versus control (`evidence_class` in {transcript_contrast, protein_state, activity_state, phenotype_state});
a seed row whose class is `intervention_response`, `held_out` or `card` is refused by the engine at load time (tested). Card-linked families are used **after the fact**
only as known-answer probes for the leakage test (T3) and are labelled as such.

## 3. Tests and pass criteria (all fixed before running)

Universe for tests: the **examined set** = M-net-usable families (IT7 P2 rule) with at least one signed target present in the network graph, computed from the full
catalogue (denominators are reported at every funnel step; "examined" is a count, not a screening of the world's compounds). N_null = 1000 draws for every null,
seed = 20261030 + test index; deterministic.

**T1 The seeds enter the computation** (PASS iff all hold, tolerance 1e-5 relative for float32):
(a) zero seed vector gives max|Q| = 0 exactly for every arm; (b) scaling s by c scales Q by c; (c) the per-seed contributions sum to Q for every compound
(exact additive decomposition); (d) removing each seed with nonzero influence changes at least one compound's Q by more than 1e-6; seeds with no influence
(no in-network path to any compound target within K) are listed as inert, not as failures.

**T2 Replacing the seeds changes the result when it should** (PASS iff all hold; otherwise the method is declared NOT SEED-SPECIFIC for that seed set, a valid outcome):
(a) 1000 degree-matched random seed sets (same number of seeds, same multiset of signed levels, each seed gene replaced by a random gene of the same in+out-degree decile,
real seed genes excluded): median Spearman(real Q, null Q) over the examined set <= 0.50 AND median overlap of the top-100 <= 20 compounds (chance about 0.2 x set size/13,379);
(b) sign shuffle (1000 permutations of the signs among the DEFINED-direction seeds; run only if there are at least 4 defined seeds, else reported as not testable): median Spearman <= 0.80;
(c) a decoy seed set from another process of the same dataset (the myelin set of P1, when the seeds include one; for P1 seeds, the seeds of a different system if supplied): Spearman with the real Q <= 0.50.
Effect size: 1 - Spearman and the standardized difference (real Q - null mean)/null SD per compound (reported: count with |z| > 3).

**T3 No identity error or answer-in-construction behind the change** (identity PASS iff (a) and (b); leakage is a reported flag with the rule in (c)):
(a) the firewall check of section 2 is satisfied automatically (seed table classes; no seed gene is a card-linked compound's name);
(b) identity audit: seed genes found in the graph (count, listed missing); mouse seeds carry a stated ortholog mapping or are refused for the human arm; share of distinct signed
target symbols of the usable families found in the graph; restricted-universe check: Spearman(Q on the families whose every signed target symbol is in the graph, Q on all examined) >= 0.90;
(c) leakage: for each card-linked known-answer family (probe; never an input) with a nonzero Q: rank percentile under the real seeds; rank percentile when every seed that is its own
direct target is removed (leave-own-target-out); share of its |Q| that is hop-0. Flag `RECOVERED_ONLY_VIA_OWN_TARGET` when the percentile falls by more than 0.20 after that removal.
This is reported for each probe, no pass is attached to a known-answer compound ranking high or low (it would be a claim of accuracy).

**T4 Added information relative to the direct search** (outcome is one of ADDS, LIMITED, NONE; no pass/fail on the method's worth):
Reported: Spearman(NET-IND, DIRECT) over examined families; Spearman(NET-FULL, DIRECT); top-50 and top-100 overlap of NET-IND with DIRECT (ordered by Q, DIRECT nonzero only); the number of top-100 NET-IND families
with DIRECT = 0 and no INTERACTOR membership ("new"); of those, the number whose per-compound z against the T2(a) null exceeds 3 ("new and seed-specific").
ADDS iff at least 50 of the top 100 NET-IND are new and at least 25 are new and seed-specific; NONE iff fewer than 10 are new and seed-specific; LIMITED otherwise. A top-k list from a method that
fails T2 is labelled as not seed-specific whatever T4 says.

**T5 Mutation tests** (PASS iff all hold): (a) seeds removed (empty vector) -> every arm's Q identical to the no-WWOX baseline (all zeros; the seed-free reach baseline is reported next to it);
(b) all signs flipped -> Q exactly negated, so the ordering reverses and the opposing/mimicking labels swap; (c) one defined seed's sign flipped -> Q changes for exactly the set of compounds with nonzero influence of that seed and by exactly -2 times that seed's contribution;
(d) uncertain-direction arms: Q(U+) - Q(U-) = 2 x (sum of uncertain contributions) exactly, and the min/max range brackets both arms; (e) network sign mutation (every edge sign randomized 200 times) changes Q (median Spearman with real <= 0.9), i.e. the signed structure is used;
(f) a seed given zero level is identical to removing it.

## 4. External resources (trial rule)

For each external resource named in the task (TxGNN, MATRIX, Open Targets, DGIdb/ChEMBL/GtoPdb, LINCS/SigCom) a verdict is recorded as a TRIAL result:
availability, licence and pertinence verified at the primary source and, where it can be done without installing a framework, a contained trial on a declared
query. A verdict is `ADOPTED`, `USED AS INPUT ALREADY`, `NOT PERTINENT (reason)`, `NOT AVAILABLE (reason)`, or `UNVERIFIED (what could not be reached)`; "WATCH" is not used for something that could be tried.
No e-mail address, operator identity or account identifier is sent to any service.

## 5. What a pass means and does not mean

PASS of T1, T2, T5 means: the seed vector is read, its entries move the scores, the movement is specific to those seeds and the direction logic behaves. T3 means: no
detected identity or construction leak. T4 states how much is new relative to direct targeting. None of it says a proposed compound would help; there is no
compound-response measurement in a WWOX-deficient system to test it against (IT6 P3, IT7 P0a, IT8 P4). Seed sets are re-run under exactly these criteria when the P1 seeds appear
(the first run, on the provisional set derived from the IT7 P1 subnetwork, is labelled PROVISIONAL and is a test of the engine, not of the question).
