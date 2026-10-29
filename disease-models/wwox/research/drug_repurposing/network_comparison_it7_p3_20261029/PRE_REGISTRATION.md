# PRE-REGISTRATION: first bounded network-prediction comparison (IT7 package P3, roadmap R3)

Scientist-a, 2026-10-29 (registered 15:1x UTC, before any evaluation value was opened). Exploratory. Computational. Not medical advice; a computational result is not
therapeutic efficacy, and a "module opposition" score is not a rescue. The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used.

**What was and was not opened before this file was committed.** Opened (inputs, metadata, not outcomes): the P1 subnetwork tables, the P2 usable-compound census and pilot tables,
the LINCS `sig_info` / `gene_info` metadata (to count signatures per context and to confirm the six genes are in the 12,328-gene space), the OmniPath licence list and the
two network downloads (edge counts and the neighbours of the six readout genes in the network, a build-side fact), the GEO series-matrix of GSE215425 (sample titles, regions,
genotypes; **no expression value**). **Not opened:** any LINCS level 5 z-score of the pilot compounds, any expression value of GSE215425, any propagation or overlap score.
One input-only count was made and is disclosed because it changes the design (section 4, REF-0): only **1** of 578 pilot families has a documented action on a module node.

## 0a. Coordinator notice received before the first commit (P1 verifier, HIGH firewall finding) and its handling

The P1 verifier found that the fly factorial (E-MTAB-14948/9) fed the P1 network while being listed as held-out; P1 is being repaired (fly rows dropped; the 0.25 concordance rule passes about 1338 of 8123 genes
genome-wide, so about 4 of 24 network genes would pass by chance, P(>=6) about 0.19). Handling here: (1) the **fly factorial is fully held-out and is not used in any way**; (2) the copy of P1 in `inputs/` is the **pre-repair commit
8b9861d5** (nodes.tsv sha256 3624b97d..., edges.tsv sha256 da44eebb...), recorded in `inputs/INPUTS.tsv`; I use from it only (a) the six readout genes and their directions, which rest on the two human systems only (organoid + progenitor library), (b) the
list of 20 module gene nodes (REF-0 and exclusion list), and (c) the gene-to-gene edges **ED080, ED081, ED082, ED083** (HIF1A -> HK2, SLC2A1, LDHA, PDK1; non-neural WWOX work / a non-WWOX paper) for NET-WWOX. No fly column, fly ortholog, lactate node or ED077/ED085/ED086 row is used. NET-WWOX is
therefore restricted to exactly ED080-ED083. (3) Because the six-gene rule may be partly chance, **E1 is judged against the decile-matched null, never against the 0.25 bin**; the readout set is fixed as given and the verdict wording on any compound result already says "module opposition in wild-type cells". (4) When the repaired P1 commits land I will re-diff `nodes.tsv`/`edges.tsv`; if any of (a)-(c) changes I log it in `DEVIATIONS.md` and record the new hash **before step B**; this registration is not edited.

---------------------------------------------------------------------------------------------------------------------------------

## 1. Question (one sentence, fixed)

**Among the pilot compound families, does a lightweight signed-network method, built only from public generic resources and the documented compound actions, rank compounds by
their *observed* opposition of the six-gene glycolysis / lactate transcript module (the P1 question) in held-out LINCS neural-cell signatures better than a simple unsigned
frequency-corrected target-overlap reference, and does the transcriptional-signature route (same six genes, a different cell context) add anything?**

Three further statements are asked and kept secondary: (S2) the signature route against the same reference; (S3) whether the P1 curated WWOX-specific edges add anything to the
external-only network; (E1, separate from the method comparison) whether the module itself transfers to an independent WWOX-loss contrast (the P47T deposit).

It is **not** a test of any compound's effect on WWOX loss: no public record has a compound response in a WWOX-deficient system with a molecular readout (IT6 P3 census,
narrowed in IT7 P0a). Everything at compound level is **mechanism recovery in an independent perturbation resource, i.e. recovery of a held-out observed response in
wild-type neural cells**, not accuracy against a WWOX truth. **The missing comparison** is a compound-response measurement in a WWOX-deficient human neural system with
biological replication and a matched protein/activity/flux readout. Label: EXPLORATORY.

## 2. Reference state, readout and direction

* Reference state: WWOX loss versus control in the two human neural build systems of P1 (GSE156243 organoid knockout, 4 v 2 libraries; GSE126075 shRNA progenitors, 1 library per arm).
  Build data are those two. Nothing in the evaluation data (section 5) enters any score.
* **Readout genes R (the P1 rule, copied, not re-derived): up = SLC2A1, HK2, LDHA, LDHB, BNIP3 (d = +1); down = PDK1 (d = -1).** PDK1 is "lower in sign only" in P1 and is kept because the chain
  predicts it; its arm weight is equal to the up arm's (convention of the earlier LINCS work: mean of the up arm minus mean of the down arm). A sensitivity drops PDK1 (up5 only).
* **Six-gene signature decision (made before running).** All six genes are in the LINCS level 5 gene space (BNIP3 is a measured landmark; SLC2A1, HK2, LDHA, LDHB, PDK1 are
  *inferred* values, computed by the LINCS pipeline from landmark genes). Six genes are small, and five of six values are inferred rather than measured. The signature route is therefore run
  **but is declared weak a priori**: it can show "no detectable signal", never a positive claim stronger than "cross-context reproducible module response". A larger gene set was NOT
  substituted, because the P1 question is these six genes and the equivalent-inputs rule fixes them for every method.
* Opposition: lowering the up genes and raising PDK1 ("opposes" the WWOX-loss module). Direction is the sign of the compound's effect on the **transcript module in wild-type cells**.

## 3. Candidate universe (a stated subset, **not** a screening of the catalogue)

* From P2 `pilot_subset.tsv`: families with `usable_by_both_Mnet_and_Msig_neural == yes` (578). The 17 families that are in the pilot only because a WWOX card links them are **excluded**
  (membership must be set by input availability, never by cards: this is part of the firewall, section 6).
* Cross-context universe **U**: families (of the 578) with at least one strict-tier neural `trt_cp` signature in a **build context** (cell ids `NPC`, `NPC.CAS9`, `NPC.TAK`) AND at least one
  in an **evaluation context** (`NEU`, `NEU.KCL`, `MNEU.E`), taken from LINCS GSE92742 phase I (level 5 is held locally; GSE70138 was not downloaded: families with neural signatures only
  from GSE70138 are outside U). `FIBRNPC` (lineage UNKNOWN) is not used. Expected |U| = **256** (counted from `sig_info` metadata: 1 239 signatures, 507 families with any, 256 with both). The exact
  figure is reported; if |U| < 150 the signature-route comparison and every "no added value" call are declared INCONCLUSIVE-by-size.
* Minimum detectable effect, stated: with |U| of about 256, the standard error of a Spearman rho is about 0.063; rho >= 0.15 is the smallest effect detected at one-sided 5 percent with about 80 percent power.
  Smaller effects are not claimed absent.
* Families are the unit (a family is not an independent compound: duplicates and salts are upper bounds, P2). Signatures of one compound across cells, doses and times are not independent;
  they are aggregated by the **median per family and context class** and kept in a signature-level table.

## 4. Methods, every parameter

All stdlib + numpy. Master seed **20261029**; sub-seeds = master + k, k fixed per component in the script. Deterministic.

**Per-signature opposition score (the observed outcome and the signature route).** For a level 5 (MODZ) signature with z-scores z over the 12,328 genes:
`OS = -( mean_{up5} z - z_PDK1 ) / s`, `s = 1.4826 * MAD(z over all genes)`. Higher = opposes. The scale s removes the general transcriptional-magnitude axis of the signature (the
known confound: reversal scores follow magnitude). Family value `O^X` = median of OS over the family's signatures in context class X (B build-like, E evaluation-like), **all doses and times kept as separate signatures**;
retained in `signature_scores.tsv` with cell id, dose, time, pert id.

**SIG (transcriptional-signature route).** Score of family f = `O^B_f`. Evaluated against `O^E_f`. Disease signature = the six genes above only. Library: LINCS L1000 phase I level 5 (GSE92742), compound
perturbagens `trt_cp`, cell contexts as in section 3; wild-type cells, no WWOX-deficient context exists. The earlier knockout-signature query (IT2/IT3 GSE156243 work) is **not repeated as new evidence**.

**Outcome (held-out observation).** `O^E_f`. For REF and NET no expression is an input, so every evaluation context is independent of them; for SIG the build and evaluation contexts are disjoint cell ids.

**External network G_ext** (the generic resource, licence-compatible): OmniPath export of (i) interactions in which SIGNOR is a source, datasets omnipath/pathwayextra/kinaseextra/tf_target, and (ii) dataset
collectri, **keeping only rows whose every listed source has an OmniPath licence purpose "commercial" or is a named composite** (excludes non-commercial-licensed rows; GEREDB-sourced rows, AFL, are dropped);
human; downloaded 2026-10-29; edge sign = consensus stimulation XOR consensus inhibition (ambiguous rows dropped); protein complexes ("A_B") expanded to their members; a (source,target) pair with both signs
is dropped. Frozen as `inputs/signor_omnipath_edges.tsv.gz` and `inputs/collectri_omnipath_edges.tsv.gz` (hashes in `inputs/INPUTS.tsv`); the build never touches the network again. Attribution: SIGNOR (CC BY 4.0),
CollecTRI/DoRothEA constituent resources as listed in each row's `sources` column, via OmniPath (Turei et al.). **Contains no WWOX card, need, curated WWOX edge or compound-response record.**

**Compound -> target edges.** From P2 `pilot_net_actions.tsv` (ChEMBL curated mechanism, GtoPdb, DGIdb-other claims; identity as served, signs: inhibitor/antagonist/blocker... = -1, agonist/activator... = +1; potency and
concentration are UNKNOWN for all rows and are **not used**). A family's vector `x0`: for each target symbol the mean sign over its rows (conflicting rows average toward 0), complex/group targets expanded to their members, then **L2-normalised
(promiscuity dilution)**. The ChEMBL activity endpoint is not cached; its absence is a stated limit (no potency-weighted variant).

**NET (signed propagation, the lightweight signed network method).** `W[j,i] = sign(i->j) / outdeg(i)` over G. `y = sum_{k=1..K} gamma^(k-1) W^k x0`, **K = 3, gamma = 0.5**; k = 0 (the direct effect on a target's own node)
is **excluded in the primary** because the evaluation is transcript-level (an enzyme inhibitor changes enzyme activity, not necessarily its mRNA). Score `NET_f = -( mean_{up5} y - y_PDK1 )` (same arm form as OS; higher = predicted to oppose).
Sensitivity NET-direct adds k = 0. Variants: NET-EXT = G_ext only (primary); NET-WWOX = G_ext + the non-measured P1 edges among gene nodes (`edges.tsv` rows of type inferred / hypothesised / association whose two ends are gene nodes, signed as
given, association unsigned and dropped); the P1 measured edges (WWOX-loss -> gene per system) cannot carry a compound effect and are not added; **no agent edge, no card, no need is in either**. BioNAV/NeMoCAD is a methodological reference only (section 7).

**REF (simple references).**
* **REF-0, direct module-node overlap** (targets in the 20 P1 module gene nodes). Input-only count: it hits **1** pilot family, so it cannot rank and is reported only as a degenerate baseline.
* **REF-1 (the primary reference), unsigned frequency-corrected overlap with the first-order regulators of the readout genes**: Reg = every node with an edge in G_ext into any readout gene (either sign);
  `REF1_f = sum_{t in T_f ∩ Reg} idf_t / sqrt(|T_f|)`, `idf_t = ln((N+1)/(n_t+1))`, N = 578 pilot families, n_t = families targeting t, T_f = the family's targets. Unsigned by design: it is the "annotation overlap" a reader would compute without a model.
* **BASE-promisc** = |T_f| (number of targets): the null predictor that a method must beat.

**Statistics.** Primary measure `rho_M` = Spearman correlation (average ranks for ties; ties are frequent for REF/NET zeros and are kept, never broken) between a method's score and `O^E` over U.
Secondary: top-decile hit rate (share of the method's top 10 percent of U that is also in the top 10 percent of `O^E`; chance 10 percent), with a permutation p from the matched-set null below.

## 5. Evaluation data and why they are separate from the build data

| Evaluation | Data | Unit | Separation from build |
|---|---|---|---|
| **E2 (compound level, the method comparison)** | LINCS GSE92742 level 5, neuron-like contexts `NEU`, `NEU.KCL`, `MNEU.E`, signatures of the pilot compounds | family (median of signatures) | NET and REF take no expression as input. SIG is built on the disjoint progenitor-like contexts (`NPC*`). The six-gene module and its signs were fixed from GSE156243 + GSE126075 (P1) and are not tuned to LINCS. LINCS cells are wild-type for WWOX. |
| **E1 (module transfer, not a method comparison)** | GSE215425 P47T knock-in versus wild type, 5 v 5 animals (cerebellum 4 v 3), RNA-seq counts, public; regions PFC, HPC, parietal CTX, CB | **animal** (all four regions come from the same animals, so regions are not independent) | independent mouse genotype (a partial-loss missense in the WW1 domain, not a null) and independent laboratory from the build systems. The earlier mouse P17 deposits are "seen" (IT6 P4) and are never evaluation. The weaker fly factorial check (E-MTAB-14948/9) is **not run** (ortholog mapping is not one-to-one, amyloid background, perturbation depth not visible): a stated omission. |

**E1 decision rules (fixed here).** Primary region: **hippocampus (HPC)** (chosen a priori: the neural region of the build systems and of the seen mouse hippocampal data; one primary region so that one test carries the alpha).
Per gene: centred log2 ratio = (mean log2(CPM+1) mutant - wild type) minus the median of that quantity over genes with mean CPM >= 1 in the region (the earlier "centred" convention); mouse symbols by case: Slc2a1, Hk2, Ldha, Ldhb, Bnip3, Pdk1.
Module contrast `D = mean_{up5} cLFC - cLFC_PDK1` (positive = WWOX-loss-like). Per-animal module score `s_a = mean_{up5} (x_ga - mean_g) - (x_PDK1,a - mean_PDK1)`, x = log2(CPM+1); exact label permutation over all
252 assignments of 5 mutant labels to 10 animals (one-sided). Null band: 1 000 random sets (5 up + 1 down, same formula) matched on the mean-expression decile of each real gene (seed 20261029+31).
* **TRANSFERS** (HPC): D > 95th percentile of the matched null AND exact one-sided p <= 0.05 AND at least 4 of 6 genes in the build direction (up5 up, PDK1 down) AND mean of up5 cLFC > 0.
* **DOES NOT TRANSFER** (HPC): D inside the null band AND exact p > 0.05 AND at most 3 of 6 genes concordant.
* **INCONCLUSIVE:** anything else.
* Secondary, descriptive, no verdict: PFC, CTX, CB (CB is 4 v 3: the smallest exact p is 0.029, so it cannot reach 0.0125 and is not powered); the animal-level mean of `s_a` over the four regions (animals as unit, exact permutation, 252 assignments); a sex-stratified permutation (males 3 WT v 2 mutant, females 2 v 3, 100 assignments) as sensitivity.
* Reading fixed in advance: a flat result is the expected null (the seen mouse P17 contrasts already argue against LDHA/LDHB); a positive result is one partial-loss mouse genotype agreeing with two human systems, not a mechanism or a rescue.
  If the module does not transfer, the compound results (E2) remain what they are (module opposition in wild-type neural cells) and are labelled as carrying no demonstrated WWOX-loss relevance.

## 6. Controls and firewall

**Controls (all pre-declared, all reported):**
1. **Matched/random outcomes (C1).** 1 000 random 6-gene readouts (5 up + 1 down), each gene drawn from the LINCS 12,328-gene space **excluding** the 20 P1 module genes and any gene whose symbol starts with SLC2A, HK, LDH, PDK, PFK, PGK, ENO, ALDO, PKM, PGAM, TPI, GAPDH, PDH, and **matched to each real gene's decile of across-signature SD** (computed over all pilot neural strict signatures; seed 20261029+11). For each, `O^E_rand` and `O^B_rand` as above. Null for method M: distribution of `rho(score_M, O^E_rand,k)`.
   For SIG the null is `rho(O^B_rand,k, O^E_rand,k)` (same random readout in both contexts).
2. **Matched/random inputs (C2).** For NET and REF-1: 1 000 random readout sets (same random sets as C1) used as the *query* of the method, correlated with the **real** `O^E`. The real input must beat both nulls (C1 and C2).
3. **Matched family sets.** Top-decile families of each method versus 1 000 random decile-sized sets from U matched on target-count tercile (BASE-promisc): empirical p of the mean `O^E` rank.
4. **Direction-perturbed.** (a) 200 networks with edge signs permuted among edges (topology kept; seed +21): the real-sign NET must exceed the 90th percentile of their rho. (b) The 6 placements of the single down gene among the six readout genes (real one included): the real placement's rank is reported. (c) Global sign flip is a trivial check (rho changes sign) and is reported once.
5. **Sensitivity to network structure.** 100 replicates with 20 percent of edges dropped (seed +22) and 100 degree-preserving rewirings (50 x |E| swaps, seed +23): NET rho distribution; "stable" = median >= 0.10 and at least 90 percent of replicates > 0 (dropout).
6. **Frequent hitters / promiscuity.** Using the 1 000 random inputs/readouts: a family is a frequent hitter of a method if it is in that method's top decile in >= 25 percent of them (chance 10 percent). Reported: n flagged, whether they dominate the top decile, and rho recomputed without them (must stay >= 0.10).
7. **Stability.** 1 000 bootstrap resamples of the families of U (seed +24): 90 percent interval of each rho and of each paired difference `rho_M - rho_REF1`.
8. **Swapped contexts.** Roles of B and E exchanged (SIG built on E, outcome `O^B`; REF/NET against `O^B`; the SIG-eligible family set is the same U). A sensitivity restricted to signatures at 10 uM / 24 h. Neither alters a verdict, except the stated condition in section 8.
9. **Baseline predictors.** BASE-promisc and REF-0 are reported with their rho.

**Firewall (expected answers never enter the network or the cards used).** (i) Neither network contains any WWOX card, need, curated WWOX edge between a compound and a target or any perturbation-reversal output; NET-WWOX adds only the gene-to-gene
P1 edges listed above. (ii) The universe is set by input availability, not by card links. (iii) Compound responses in WWOX systems from cards/needs (ethosuximide, lithium, vigabatrin and the
other card-linked compounds) are **held-out descriptive checks only**: after the run, the percentile of card-linked families inside U is reported, as "recovery of known examples", with no input role and no tuning. (iv) No result of the
IT2/IT3 knockout-signature query (reverser lists, frequent-hitter tables, level-5 summaries) is read or used. (v) No evaluation value of E1 or E2 is looked at before the script is run once as pre-registered; the script is
developed on synthetic outcomes. Deviations are written to `DEVIATIONS.md` with timing, never hidden.

## 7. Resources, terms and what could not be used

* **BioNAV / NeMoCAD** (Zenodo record 7692713, "NeMoCAD: Network Models for Causally Aware Discovery"): the Zenodo API (2026-10-29) shows `access_right: restricted`, no listed file and no licence field. It cannot be installed or run; no access request was sent (an access request is not a licence). It is cited as a methodological reference only. The lightweight method here is **not** a reimplementation of it and must not be described as such.
* **TxGNN, MATRIX, ToolUniverse:** not reopened; their documented limits (earlier iterations) are unchanged and no new availability or terms were examined. LINCS: the IT3 local level 5 work is reused (matrix and extract on disk, git-ignored); the knockout confound is not repeated.
* Licences: OmniPath-served rows restricted as above; ChEMBL and GtoPdb fields are share-alike with attribution; DGIdb is not cleared as a whole for public release (P2), so only the already-committed derived P2 tables are reused. LINCS and GEO data are public (cite Subramanian et al. 2017 Cell; GEO terms), no licence text on the records, so **only derived tables are committed, never a raw matrix**.
* No registration, e-mail or contact address, spend or access-control bypass is involved. Both external downloads are open HTTP.

## 8. Budget and verdict rules (fixed)

* **Budget:** wall time <= 2 h for the full run, <= 6 GB memory, zero spend, one directory of plain scripts. Overrun = stop and report what was finished; no new framework.
* **Signal of a method M** (all required): (S1) `rho_M >= 0.15`; (S2) `rho_M` above the 95th percentile of both nulls (C1, C2; for SIG the C1 analogue); (S3) bootstrap 5th percentile of `rho_M` > 0 and, for NET, dropout stability; (S4, NET only) real signs above the 90th percentile of sign-permuted networks; (S5) `rho_M >= 0.10` after removing frequent hitters.
* **ADDED VALUE of M over REF-1** (M = NET-EXT primary; SIG and NET-WWOX secondary): M has signal AND `rho_M - rho_REF1 >= 0.05` AND the lower end of the 90 percent bootstrap interval of the difference > 0 AND, in the swapped analysis, `rho_M >= 0.10` and `rho_M > rho_REF1` (point estimates).
* **NO ADDED VALUE:** (i) |U| >= 150 and M has no signal (S1-S5 not all met), or (ii) M has signal but the point difference is < 0.05 and the upper end of the 90 percent interval of the difference is <= 0.10.
* **INCONCLUSIVE:** every other outcome, including |U| < 150, a difference whose interval spans both sides of the thresholds, or a swap analysis that contradicts the primary direction.
* **S3 (WWOX knowledge):** NET-WWOX adds value over NET-EXT only if `rho_WWOX - rho_EXT >= 0.03` with the lower end of the 90 percent bootstrap interval > 0; otherwise no added value (the expected outcome: the HIF1A edges are already in the external network and the remaining P1 edges end at nodes no compound reaches). This contrast covers exactly two increments (those edges) and says nothing about WWOX knowledge in general.
* **Prediction made before the run:** the expected outcome is NO ADDED VALUE or INCONCLUSIVE for NET and SIG: single-gene readouts at 10 uM / 24 h in wild-type cells are noisy, the REF-1 overlap is a close relative of one-hop NET, and the signature route is weak. A positive result would be the surprise and would need the controls above to survive.
* **Reopening condition (stated now):** reopen if (a) a compound-response measurement in a WWOX-deficient human neural system with replication becomes available (it replaces the held-out wild-type observation), (b) potency/concentration of the documented actions (ChEMBL activity endpoint) is added, (c) phase II (GSE70138) signatures are added to U, or (d) the six-gene readout is replaced by a larger replicated module.

## 9. Planned outputs

`README.md` (results, verdict, limits, UNVERIFIED), `p3_run.py` (`--help` answers without work; stages `inputs`, `e2`, `e1`, `report`), `inputs/INPUTS.tsv` (versions, hashes), small result tables (`signature_scores.tsv`, `family_scores.tsv`, `results_summary.json`, control tables), `DEVIATIONS.md` (if any). Raw downloads stay outside git; hashes are listed.

---------------------------------------------------------------------------------------------------------------------------------

## AMENDMENT 1 (2026-10-29, after commit eadbe26a, before any evaluation value of E1 or E2 was opened): inputs re-frozen from the repaired P1

Section 0a said the P1 copy was the pre-repair commit 8b9861d5 and that a re-diff would follow. P1 was repaired (D1 e190b14c, final **31446616**; fly rows removed, E13 dropped, PDH/MEF/MRS retyped, edge and observation ids renumbered, PKM alias fixed).
`inputs/nodes.tsv`, `edges.tsv`, `systems.tsv`, `p1_derived_gene_values.tsv` are re-copied from 31446616 (new sha256: nodes 2ffa5f6b..., edges 7f02a941..., systems 1e8eec13..., derived 6e858fbb...; full values in `inputs/INPUTS.tsv`).

What changed in what P3 uses: (a) the six readout genes and directions are **unchanged** (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down); (b) the 20 module gene nodes are **unchanged**; only the PKM concordance label changed (UNKNOWN to not_concordant, PKM now has two CAGE values); (c) the four HIF1A -> HK2/SLC2A1/LDHA/PDK1 inferred edges used by NET-WWOX are the same four, **renumbered ED077-ED080** (was ED080-ED083); the script now selects them by content (inferred, both ends HGNC gene nodes, sign up/down), not by id. No fly row, lactate node or PDH edge is used (unchanged). The 0.25 rule's genome-wide pass rate (1338/8123, about 4 of 24 by chance, P(>=6) about 0.19) is acknowledged: E1 is judged only against the decile-matched null, as already registered.
No parameter, criterion, universe, control or threshold of this registration is changed. **No evaluation value had been opened**: the only runs so far used P3_SYNTH=1 (seeded noise instead of LINCS z-scores) to test the code. 
