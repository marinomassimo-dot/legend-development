# IT8 P4: marginal value of the WWOX inputs in the IT7 network comparison (diagnosis of the inputs)

Scientist-b, 2026-10-29. **Exploratory, computational, descriptive. Not medical advice; a computational result is not therapeutic efficacy.**
The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used. This folder edits no scientific current file, card, need, ledger, or any IT7 file
(the IT7 P3 pre-registration, criteria, results and history are untouched; they are read here and nothing in them is re-judged).

## 1. Decision (stated first)

**A new computational comparison is NOT justified by the WWOX inputs now held.** No pre-registration and no new run were written. The folder closes as a diagnosis of the inputs.

| Question asked | Answer | Where |
|---|---|---|
| How many qualified WWOX inputs could change the IT7 network input without exposing held-out truth? | **0 of 211** classified inputs | section 3 |
| How many network edges, nodes or signs would actually change? | **0 edges, 0 nodes, 0 signs.** The four HIF1A edges that IT7 called the WWOX-enriched condition were all already in the external network, with the same sign | section 4 |
| Could a paired comparison detect a change of this size? | No. The whole IT7 "delta" moved no family score by more than 1.4e-5 (0.01 SD of the score); detecting a rank-correlation change of 0.03 needed roughly 6,400 added random edges (9 percent of the network) in a sizing simulation | section 5 |
| Does any other ground for a new experiment exist (new data, new question, pharmacological qualification, independent control, better signatures)? | None that changes the answer; one is open and unverified (IT8 P3), one costs power (signature filters) | section 6 |

Reopening condition: section 7.

## 2. What was done (all numbers are re-derivable)

* `classify_inputs.py` builds `wwox_inputs_classified.tsv` (rectangular, 211 rows, 12 columns) from four sources: `needs/needs.json` observed items (85), IT7 P1 `edges.tsv` (85), the IT7 P4 context matrix (14 quantities, each across 13 contexts), `cards/*.card.json` (27). The needs rows are assigned by an explicit reviewable table at the top of the script; P1 edges, P4 quantities and cards by stated rules.
* `marginal_delta.py` re-derives, from the committed IT7 P3 inputs and results only, the exact input delta (section 4), a power-only sizing simulation (section 5), LINCS signature-quality counts that touch no outcome (section 6), and the sizes of the only WWOX out-edges that could be written (section 4). Output: `marginal_delta_results.json`. It reproduces the IT7 NET-EXT and NET-WWOX family scores to 5e-8 (max absolute difference), which is the check that it propagates the same graph.
* Reproduce: `python3 classify_inputs.py --root <drug_repurposing dir> --out wwox_inputs_classified.tsv` (seconds) and `python3 marginal_delta.py --p3 <network_comparison_it7_p3_20261029> --out <dir> [--lincs <GSE92742 dir>]` (about 2.5 min, needs numpy; `--help` answers without work).
* The held-out IT7 outcome `O_E` is used **only** to size how much a paired difference can fluctuate. It was opened in IT7, so nothing computed from it here is a test or a verdict.

## 3. Classification of the WWOX inputs

What the method can consume (read from `p3_run.py`): signed gene-to-gene edges, compound-to-target actions with a sign, a fixed six-gene readout (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down), and LINCS signatures. Anything else has no place to enter.

| Class | needs (85) | P1 edges (85) | P4 quantities (14) | cards (27) | Total |
|---|---:|---:|---:|---:|---:|
| ALREADY REPRESENTED | 5 | 18 | 2 | 0 | **25** |
| NEW BUT NOT USABLE | 36 | 5 | 4 | 16 | **61** |
| USABLE WITHOUT CONTAMINATING THE EVALUATION | 0 | 0 | 0 | 0 | **0** |
| NOT SUFFICIENTLY SUPPORTED | 44 | 62 | 8 | 11 | **125** |
| Total | 85 | 85 | 14 | 27 | 211 |

Reason codes (column `reason_code`, text in `reason`): A1 content is the six-gene readout already fixed from the two human build systems (14 P1 edges, 4 needs rows, 2 P4 quantities); A2 gene-to-gene edge already in the external network (the 4 HIF1A edges, and the HIF1A-PDK1 reading of one MEF observation); N1 wrong level (function, protein, phospho, flux, activity, clinical, histology: 23 needs rows plus 5 P1 edges, 1 P4 quantity); N2 intervention response or held-out evaluation datum (firewall; 7 needs rows, 16 cards); N3 variant, lesion, stage or cell-type context with no node or filter (4 needs rows, 2 P4 quantities); N4 self-reference to the IT7 result (2); N5 no readout in the perturbation resource (myelin); S1 not WWOX evidence (6); S2 other species or non-neural context (10); S3 single system, n=1 or 4 v 2, discordant, or sign unresolved (19 needs rows, 62 P1 edges, 5 P4); S4 unmeasured (5 needs, 2 P4, 11 card abstentions); S5 case-series or single-patient report (4); S6 concordant absence of signal (1).

What the external network lacks for WWOX, dimension by dimension, and why none of it reaches a score:

| Dimension | What a WWOX observation could add | Why the method cannot take it |
|---|---|---|
| Direction | sign of a gene change in WWOX loss | enters only as the readout set, already used (A1); the signs outside the six genes are conflicting or inside noise (S3). The only function-level concordance (hyperexcitability, P4 Q14, mouse and organoid and patient organoid) is an electrophysiological endpoint, not a transcript |
| Compartment | protein, phospho, activity (HIF1A protein, GSK3B Ser9, PDH activity) | the graph has transcript-regulatory and signalling edges, no protein-state or activity node; the HIF1A protein rise was seen in non-neural cells (MEF, fibroblast) |
| Variant or lesion | splice exon skipping, protein loss of the missense allele, knock-in | no variant node or filter; LINCS cells are wild-type |
| Cell type, age, stage | progenitor vs neuron, week 15, P17 | only the choice of LINCS context classes (NPC vs NEU) carries it, and IT7 already used that split |
| Endpoint | seizure, bursts, myelinated axons, glia, glycaemia | not a node; no compound-level link |
| Response to an intervention | gene addition, T-type blocker, lithium, vigabatrin, DCA, clinical series | these are the held-out truth the firewall protects; of 19 card-linked pilot families only 2 are usable by both methods and 1 (sirolimus) is in the 256-family universe |

Honest limits of the classification: it is a judgment table. The `could_add` column is a keyword heuristic over the source fields (what the observation could in principle add), not a finding, and should not be counted. A verifier should re-derive a sample from the cited locator (`source_ref`) and challenge the class, not the heuristic.

## 4. The input delta, exactly

| Quantity | Value |
|---|---|
| External network (IT7 P3 committed tables) | 70,461 signed edges, 8,769 genes |
| Edges IT7 added in the WWOX-enriched condition | 4 (HIF1A to HK2, SLC2A1, LDHA, PDK1) |
| Of those, already in the external network with the same sign | **4 of 4** (new edges 0, new nodes 0, sign conflicts 0) |
| HIF1A to all six readout genes in the external network | all six present, sign +1 (CollecTRI for SLC2A1, LDHA, HK2; SIGNOR for the rest, HIF1A-PDK1 through the expanded ARNT/HIF1A complex) |
| What the "added" edges actually did | duplicated four existing edges: parallel edges that double their weight and raise HIF1A out-degree from 306 to 310 (dilution of its other targets) |
| Families whose NET score differs, EXT vs WWOX | 80 of 256 (143 have a non-zero score); largest change 1.36e-5 = 0.0097 SD of the score; none above 1e-4; Spearman between the two score vectors 0.99993 |
| IT7 paired difference | -0.0015, 90 percent interval [-0.004, +0.0002] (re-derived: bootstrap SE 0.0013) |

**Correction to carry forward (not an edit of IT7):** the IT7 wording "the WWOX-enriched condition adds four HIF1A edges that the external network already largely contains" is stronger than stated: it contains all four. S3 was therefore a test of a duplicate-weight perturbation of 0.006 percent of the edges, and its "no added value" says nothing about WWOX knowledge. This agrees with the caution that it cannot be called a test of the WWOX heritage.

The only other gene-level relations the P1 table holds that involve WWOX are the measured "WWOX loss gives gene X change" rows. They are disease-state observations, not regulation by WWOX:

* WWOX is a **sink** in the external network (7 in-edges: NFKB1, NFKB2, REL, RELA, RELB, TFAP2C, E2F1; 0 out-edges).
* **0 of the 256 universe families** have WWOX as a target and **0** have a direct target among its 7 regulators, so a compound cannot reach a WWOX out-edge within the 3 propagation hops that matter.
* Sizing scenarios (not proposals, never an arm): S_A one edge WWOX to HIF1A (-1; the MEF and cancer-cell observation) changes **0 families** (change 0.0). S_B six edges WWOX to the six readouts in the module direction would be circular by construction (the answer for the readout genes is written into the network) and changes 24 families by at most 3.0e-5 (0.021 SD), delta rho 1.7e-5. S_C (both) the same. No relation was invented to make the arms differ; these were computed to show that even the most favourable honest and dishonest encodings do not move the scores.

## 5. Power statement

* IT7 comparison of a method against a reference at n = 256 families: SE of a rank correlation about 0.063, minimum detectable effect about 0.157 (one-sided 5 percent, 80 percent power); re-derived here as 0.1563.
* A paired difference between two nearly identical score vectors is far more precise than that (bootstrap SE 0.0013 at the observed delta). Precision is not the problem; **there is nothing to detect**: the delta is below the numerical scale of the score.
* How large would a delta have to be? Sizing simulation (HYPOTHETICAL random sign-random edges between external-network nodes, 12 to 30 replicates per size, never WWOX relations): 4 edges change 0 families (|delta rho| 0); 100 edges (0.14 percent) change a median 17 families, |delta rho| median 0.0003, 95th percentile 0.012; 400 edges, 55 families, 0.003 / 0.013; 1,600 edges (2.3 percent), 108 families, 0.010 / 0.022; **6,400 edges (9.1 percent), 152 families, 0.028 / 0.069**. The registered S3 threshold (0.03) is reached about half the time only at the 9 percent scale. The WWOX record supports at most 7 candidate out-edges, 0 of them reachable. Random edges are a bound on size, not on targeted placement, but no targeted WWOX placement exists (S_B above).
* So the detectable range of a paired edge comparison starts around |delta rho| 0.03 and needs on the order of 10^3 to 10^4 relation changes. The WWOX inputs supply 0.

## 6. Other grounds for a new experiment, checked

| Ground | State | Consequence |
|---|---|---|
| New data (compound response in a WWOX-deficient human neural system; human WWOX RNA programme; organoid single-cell record) | none released: IT7 census and scout (compound-response record absent; Unravel/Foundation RNA map "underway", no accession; E-MTAB-14792 not accessible, no request sent) | nothing new to test |
| Different question | the question the same inputs can answer is the IT7 one; none of the 211 inputs changes it | no |
| Relevant pharmacological qualification | IT8 P3 runs in parallel; at the time of this check `.claude/worktrees/it8-p3` held no committed output | UNVERIFIED; this is the condition most likely to change the answer (section 7) |
| Independent control | the only independent WWOX-loss contrast, GSE215425 P47T, was already used as E1 (INCONCLUSIVE); the mouse P17 deposits are "seen" | spent; nothing independent left |
| Signature quality | IT7 applied no quality filter. Counts (no outcome opened): of 1,239 IT7 signatures, 324 of 788 progenitor-like and 140 of 451 neuron-like pass distil_cc_q75 >= 0.2 and pct_self_rank_q25 <= 5 (25 and 14 have no value); only **63 of the 256 families** keep a passing signature in both context classes, so the SE would rise from 0.063 to about 0.13 and the MDE from 0.157 to about 0.32. Of the six readouts only BNIP3 is a measured landmark gene; the other five are inferred in L1000 | a filter trades purity for power and cannot be chosen against the opened IT7 outcome without being post hoc; it does not add WWOX information |
| Phase II (GSE70138) | 236 neural compound perturbagens, 46 of the 256 universe families have one | adds replicate signatures to a minority of families; a method-power question on wild-type cells, not a WWOX one; IT7 reopening condition (c) |

## 7. Reopening condition

Reopen a WWOX-informed network comparison only if at least one of these holds, and then register first:

1. a compound-response measurement in a WWOX-deficient human neural system with biological replication and a matched readout, which would also supply the first usable evaluation truth and turn the N2 rows from firewall items into held-out outcomes; or
2. WWOX-derived relations that a compound can reach: signed regulatory edges from or to WWOX or its regulators in neural cells, or a validated WWOX interactor that is itself a drug target, in numbers of the order of hundreds (section 5), not units; or
3. a replicated WWOX-deficient module (at least three libraries per arm in one human neural platform) larger than six genes, replacing the n=1 readout and removing the S3 rows; or
4. a qualified pharmacological table from IT8 P3 (potency, exposure, neural reach) that changes which families are usable, evaluated with a fresh outcome (phase II signatures, or a quality-filtered set fixed before it is opened).

Until then the honest statement is: the WWOX record, as it stands, adds **no usable input** to this method; it is not evidence that WWOX knowledge is useless for repurposing, only that this method has no place to put it.

## 8. UNVERIFIED

* The class of each of the 211 rows is judgment; a verifier will re-derive a sample. The P4 and card rows rest on the cycle texts they cite, not on a new reading of any paper.
* Whether IT8 P3 (running in parallel) will change the pharmacological qualification; nothing of it was read.
* The sizing simulation uses random edges; targeted edge sets near the readouts could behave differently, but none exists for WWOX.
* The signature-quality counts use conventional thresholds (cc_q75 0.2, self-rank 5 percent) taken as descriptive, not as a recommendation; the 63-family figure is the count of universe families with a passing signature in both context classes by perturbagen id.
* The fraction of HIF1A edges' sources that are complex expansions (SIGNOR ARNT/HIF1A to HIF1A and ARNT) was not audited.
* Phase II counts use a copy of the GSE70138 signature table in the session scratch area (not committed) and the phase I pilot context table for family membership.

## 9. Files

`README.md` · `wwox_inputs_classified.tsv` · `classify_inputs.py` · `marginal_delta.py` · `marginal_delta_results.json`
