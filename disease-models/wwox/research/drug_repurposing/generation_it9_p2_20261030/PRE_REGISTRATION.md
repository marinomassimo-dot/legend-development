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

---

## AMENDMENT 1 (2026-10-30, after the first engine run on the PROVISIONAL seeds, before any run on the P1 seeds; full disclosure of what had been seen)

Seen before this amendment (provisional seeds only, 15 seed units from the IT7 P1 subnetwork, 6 with defined direction): the engine runs end to end (examined 12,560
families); T1 PASS; T5 PASS; T2 criterion (a) and (c) met, criterion (b) not met (sign shuffle: median Spearman 0.92, 167 of 1000 shuffles identical to the real signs, because 5 of 6
defined seeds share one direction, so a shuffle rarely changes anything); T3 identity restricted-universe check returned 1.0, which is near-tautological (a family whose every
target is in the graph has the same score in any engine built on it); T4 outcome by the rule above: NONE (9 of the top 100 NET-IND "new and seed-specific"), i.e. the raw Q ranking
is dominated by network position (HDAC inhibitors and other multi-target regulators), which a degree-matched null exposes. The amendments below were written after seeing this and are
therefore exploratory for the provisional set; they are fixed in advance for every later seed set (the P1 seeds). Nothing in sections 1-5 is changed; the registered results are reported as registered.

* **A1.1 NET-Z arm (new).** `Z = (Q_real - mean_null) / max(sd_null, floor)` per family, with the null = 500 degree-matched random seed sets (seed 20261030+11) built exactly as in T2(a),
  separately for the two uncertain-direction arms (U+: uncertain seeds +, U-: uncertain seeds -), and floor = the 5th percentile of the positive null SDs (stops a near-zero denominator creating a large z).
  Ranking key `Z_robust`: min(Z_U+, Z_U-) when both are positive (opposes under either sign assumption), max when both negative (mimics under either), else 0. NET-Z answers
  "does this compound's score exceed what the same number of equally connected random genes would give", i.e. it removes the hub effect; it is still a compatibility of directions, not a benefit prediction.
  T2(a) and T4 are evaluated for NET-Z too, with null draws INDEPENDENT of the draws used for its z (T2 nulls: seed 20261030+1, 1000 sets; the same per-family moments are applied to them).
* **A1.2 DIRECT-ANY reference (new).** Families with ANY catalogue target row (signed or not, stated action or not) on a seed gene: the unsigned form of the simple "target -> compounds" search.
  In T4 "new" now means: not in DIRECT (signed), not in DIRECT-ANY and not in INTERACTOR. This can only shrink the "new" count.
* **A1.3 T3(b) added diagnostics (reported; the registered criterion stays as registered and its near-tautology is stated):** (i) Spearman between Q with the unit norm taken over all signed targets and Q with the norm taken over in-graph targets only;
  (ii) a table of the unmapped signed target symbols by number of families (so alias errors can be spotted), and the count of M-net-usable families with no gene symbol at all (cannot enter any gene-level method).
* **A1.4 T2(b) power note.** When fewer than 3 defined seeds disagree in sign with the rest the sign shuffle cannot be expected to move the ranking; the registered criterion is still applied and a failure is reported as a failure.
  Reported next to it: a "flip-the-minority" mutation (the single seed of the less common sign flipped), which is deterministic and does move the ranking where that seed matters.
* **A1.5 Probes.** Percentile uses mid-ranks for ties. Probe scores are reported for the defined-only arm and for both conditional arms (U+, U-), not for U+ alone.

---

## AMENDMENT 2 (2026-10-30, after the first runs on the P1 seed sets; written before the in-degree variant was run)

Seen before this amendment: the P1 sets (`seeds_p1/`, adapter `p1_adapter.py`) were run once under sections 1-3 and Amendment 1 with total-degree matching. Per set the
registered verdicts exist in `results/tests_p1_*.json`. What prompted this amendment: (i) the backward propagation of a seed flows over the INCOMING edges of the seed gene, yet the registered
null matches on in+out degree; for a sink such as WWOX (7 in-edges, 0 out-edges) a random gene of the same total degree has a very different in-degree, so its null is not like with like (Q1: the NET-Z
top-100 shares a median of 59 families with the null lists); (ii) in sets where every defined seed has the same direction (Q2 expression, Q4 protein) the registered sign shuffle is the identity and
returns Spearman 1.0 by construction.

* **A2.1 Matching variant M2.** Every test and the NET-Z moments are also run with the null genes matched on the in-degree decile (unique quantile edges; real seed genes excluded; genes absent from the graph matched to absent-from-graph target genes) instead of in+out degree.
  Both variants are reported side by side; a statement in the README that depends on the null (T2, T4 "specific", NET-Z) is made only if it holds in both, otherwise it is reported as "depends on the null".
  Criteria are unchanged (section 3). Label suffix `_indeg`.
* **A2.2 T2(b) is applied as registered** (>= 4 defined seeds): a degenerate shuffle (identity because all defined seeds share one sign) therefore counts as NOT MET; the summary table also gives the criteria vector (a, a', b, c) so a reader can see
  T2 without (b). This is a registered-verdict-plus-decomposition, not a relaxation: no set is passed because (b) is skipped.
* **A2.3 T1(d) on a set whose only defined seeds are inert** (no in-network path to any compound target and not a target themselves) is reported as FAILED (d) with the reason, not rescued.

---

## AMENDMENT 3 (2026-10-30, after P1 final was merged; written before the reserved-row check was run)

P1 final (seeds.tsv sha256 65817737...; 111 rows, 58 usable, 17 reserved) yields byte-identical engine seed tables to the version used for Amendments 1-2 (only the recorded hash differs), so the
test results are unchanged and are not rerun. Adopted from the coordinator's note: `unchanged` is non-directional (already not a seed); Q2 module genes must not be scored by reversal of the IT7 P3 readout and
Q3 ISR reversal must not be used to score candidates (the SIG arm output for those sets is a generator output only and is never an evaluation); uncertain-direction questions run as conditional arms (already so).
**Reserved-row check (new, descriptive, no pass/fail):** (i) list every reserved row whose gene also appears as a seed in any set (shared gene) and confirm no reserved row is a seed row;
(ii) for the genes of reserved gene-level rows (WWOX, LDHA, CACNA1G, PANX1, GFAP, MYC, CTNNB1), report in each set's proposals the number of families with a target on that gene, their best Z_ind_robust rank and the share of those families that are
direct hits. Reserved process/state rows (GO, STATE:) have no gene representation and cannot be checked. Nothing from the check is fed back into any score; a high rank of a drug that acts on a reserved gene is reported as non-independent when the gene is also a seed, and is never a validation.

---

## AMENDMENT 4 (2026-10-30, P1 v2 merged: seeds.tsv sha256 76952333..., 131 rows, 65 usable, 26 reserved; written before any run on v2)

**Seed set v2.** Questions Q1-Q7 (Q6 MYC/radial glia and Q7 GSK3B phospho are thin secondary questions). The adapter reads the new columns `guard_tag` and `change_ref`. Seed rows are still only `usable_for_generation=yes` and `reserved_for_evaluation=no`; the same level-separation rules apply (one set per question and readout level).

**Guard handling, read mechanically from `guard_tag` (code: `apply_guards`, `sig_eligible` in `seed_engine.py`; the mutation tests are in `test_seed_engine.py` and fail if a guard is ignored):**
* `ISR_SIGN_UNRESOLVED` (Q3 ISR rows): the unit's sign is forced to 0 (uncertain direction) whatever the direction column says, so these seeds enter ONLY as conditional arms (U+, U-); and they are excluded from the signature arm.
* `IT7_READOUT6` (Q2 six-gene readout and the glycolysis/lactate set): the units may seed network generation (the NET arms are generation, not evaluation), but they are excluded from the signature arm (scoring a candidate by reversal of that readout in LINCS is exactly the guarded use). Every proposal table carries `evaluation_forbidden_on` listing the tags present, and the README states that no NET proposal from such a set may be evaluated by reversal of the IT7 readout.
* `HELD_OUT_ENDPOINT` (state rows without gene members, and GFAP/IBA1 area rows): units are kept as seeds only where gene-level; the tag travels into `contributions` and `evaluation_forbidden_on`; they are excluded from the signature arm; a candidate is never scored on the endpoint quantity the row came from.
* Phospho-level rows (Q7 GSK3B pSer9): a phospho site observation is not a change in kinase activity (P1: activity unmeasured); the adapter writes such rows with direction `uncertain` (conditional arms) and a note. This is a level rule, fixed here.
* Mutation test (T6, new, pass/fail): (a) a Q3-like table whose ISR row says `down` loads with sign 0 under the guard and with sign -1 when the guard is disabled, and the scores differ; (b) `sig_eligible` drops IT7_READOUT6, ISR_SIGN_UNRESOLVED and HELD_OUT_ENDPOINT units and keeps untagged ones, and differs from the unguarded list; (c) the tags present in each real set equal the tags in the P1 table for the rows placed (no tag lost by the adapter). T6 PASS iff all hold.

**Expected changes (written before the run).** Q2 gains the PDK-family and hallmark rows (20 usable v2 rows vs 17 units in v1 tables) and its SIG arm loses its six readout units (the SIG verdict for Q2 will be "no eligible seeds or reduced"); Q3 NET changes little (13 usable rows were already mostly uncertain; the one defined ISR unit becomes uncertain, so Q3 will have 0 defined seeds, T2(b) not testable, T1(d) concerns defined seeds only and will read as vacuous, which I will report as such, not as a pass); Q4 has more gene rows (GRIN2C, KCNA2, GRM3 transcript down, GAD67, NPY), so more power; Q1 has fewer rows; Q5 expression/protein will change with the TNF/IL6 corrections; Q6 and Q7 sets will be 1-2 units and are expected to show little beyond hub effects; Q7 will be wholly conditional. I expect no change in the T1 and T5 verdicts (they are exact), possible changes in T2(b) where the defined-seed count changes, and T4 outcomes to track the number of defined gene seeds.

**Candidate tables.** `candidates_<question>.tsv` per question and arm: opposes arm = top 50 families by Z_ind_robust (z against the degree-matched seed null, not raw Q) with Z > 0, mimics arm = the 25 with the most negative Z; plus the direct-search arm (DIRECT-ANY families, unsigned, listed with their signed direct score where defined). Per row: contributing seeds (top two by |contribution|: seed id, gene, seed direction, hop 0 or 1-3, main target), compatible action (opposes/mimics only), conditional flag, whether the family is also found by the direct target search, z under both nulls (total and in-degree) and `seed_specific_both_nulls` (z > 3 in both). Ranking never uses raw Q.

**Amendment 4b (same day, before any v2 run).** On seeing the adapter output (set list only, no score) I fixed one more level rule: gene rows typed `pathology` in P1 v2 (cell counts and area fractions such as PVALB or NPY cell counts, GFAP/IBA1 area) are measurements of cell number or tissue state, not of the gene's activity or expression; they are not gene-level seeds, are counted in `adapter_counts.json` (`pathology_level_gene_row_not_a_gene_seed`) and do not enter the engine. The Q1 set is empty in v2 (its only gene-level human protein row, S004, became unusable), which is reported as such.
**Amendment 4c (before any v2 run).** Because Q1 has no tier A or B gene-level seed in v2, the adapter is also run with tiers A,B,C and only the Q1 sets are kept (`Q1_*_tiersABC`; tier C = non-neural human cells and blood, the WWOX protein and transcript rows). They are labelled tier C throughout and are not pooled with the other questions.
