# IT9 P2 v3: provenance repair of the generation path (record mode, identity, active moiety)

Scientist-b, 2026-10-30, branch task/it9-p2b (from main 140b3b79). **Exploratory, computational. Not medical advice. A compatible action of a context-free signed network is not a predicted benefit; a chain that is mode-compatible is not a verified mechanism.**
Reference genotype: a WWOX-DEE genotype class; no individual-level record. v2 (`../README.md`, `../results/`) is untouched. Pre-registration: `PRE_REGISTRATION_V3.md` (Amendment 5 written before any v3 run; 5b and 5c are disclosed there with what had been seen).

## 1. Decision (first)

| Question | Answer |
|---|---|
| Did the three filters remove the proposals that failed at the provenance of the chain (S1)? | **Yes for all seven registered artefacts.** ceperognastat, belnacasan, fosfestrol, ramelteon and implitapide leave the seed-specific arms of the set they came from (edge-mode filter; implitapide also by the complex-member rule); AR-12's PDK1 credit is dropped (alias collision) and it is absent from the Q2 direct-search arm; balsalazide is kept out of the robust arms by the active-moiety flag (it still scores: z -3.5 / -3.2 / -2.7, listed under `flagged_*`). |
| Did the repair lose proposals that were not provenance failures (S2)? | **No loss under the registered two nulls; one loss under the stricter three-null rule.** JTE-151 (z 20.0 / 18.3 / 15.8) and curcumin (6.6 / 5.3 / 4.8) stay robust; dichloroacetate (direct rank 6), felbamate (46) and memantine (50) stay in the direct-search arm. **Belzutifan stays seed-specific in the two registered nulls (3.49 / 3.37) but not in the admissible-degree null added in Amendment 5c (2.75)**, so it is `SPECIFIC_IN_TWO_NULLS_NOT_ADM`; I report it as lost under the stricter rule, not as kept. |
| Do the filters leave candidates? | **Yes, but not where the WWOX data are thinnest.** Seed-specific in all three nulls and not flagged: Q2 46 opposes / 20 mimics, Q4 expression 60 / 24, Q5 expression 189 / 166, Q6 expression 296 / 247, Q6 protein 118 / 59 (1,225 family rows in all, `results/v3_seed_specific_all_nulls.tsv`, each with its seed and edge chain). **Zero** for Q1 (both levels), Q3, Q4 protein and Q7. |
| Did the filters shrink the seed-specific lists as I predicted? | **No; my expectation (a quarter to a half fewer) was wrong in direction for the totals.** Of the v2 seed-specific "opposes" families, 64 percent (Q2), 58 percent (Q5 expression), 49 percent (Q6 expression) and 27 percent (Q6 protein) survive all three nulls, but the v3 lists are larger than v2's because the nulls got tighter (the null seeds lose their post-translational noise), so more families clear z > 3. The enlarged lists are NOT validated: they have not been through any qualification. |
| What prevents more? | Seeds and edges, not the compound side: section 6. |

## 2. The filters as implemented (rules fixed in PRE_REGISTRATION_V3.md)

* **F1 edge mode against seed level** (`seed_engine_v3.py`, `Graph3`): each edge is typed from the OmniPath record: T transcriptional, P post-translational, C coupling (a P record whose target is a G-protein subunit gene, GNA*/GNB*/GNG*), U other. Expression seeds accept chains `P* T` (at most two P edges, then one T edge into the seed; no C; no T before the last). Protein and phospho seeds accept `P+` only. Network after typing: **70,542 edges: T 37,251, P 32,687, C 604, U 0** (`results/network_modes.json`). So for an expression seed the 604 coupling edges are removed everywhere and the 32,687 P edges can no longer be the last edge; for a protein seed the 37,251 T and 604 C edges are removed.
* **F2 identity** (`build_actions_v3.py`): every compound target is resolved to an HGNC id (ChEMBL by UniProt, DGIdb/GtoPdb by concept id; HGNC complete set of 2026-10-30, sha256 d93ce6b2...); network, seed and catalogue symbols are mapped to approved symbols. Counts over 106,315 target rows: no HGNC id 9,979 rows (76 of them usable signed rows, dropped); 182 ChEMBL rows resolved only by symbol fallback; **72 alias-collision rows dropped** (an unverified claim naming gene X when the same compound has a verified target Y whose alias is X: AR-12 PDK1 vs PDPK1; others: ADRA1A/ADRA1D, TUBB/TUBB2A, CSNK2A1/2, SLK/FYN); complex members: **25 usable rows not credited** (named-member rule on PROTEIN COMPLEX and PROTEIN-PROTEIN INTERACTION types) plus **24 DGIdb copy rows dropped**, **234 rows credit all members with the flag COMPLEX_MEMBERS_UNRESOLVED**. Implitapide keeps MTTP only; lenalidomide and pomalidomide keep CRBN only (CUL4A, DDB1, RBX1 no longer inherit the sign).
* **F3 active moiety**: **350 families carry a catalogue prodrug flag, 168 of them have signed targets**; their target credits are flagged UNCERTAIN_ACTIVE_MOIETY, they stay scored but are placed in separate `flagged_*` arms and never in the robust arms (no metabolite record exists in the catalogue to credit instead).
* **Amendments** (disclosed): 5b narrowed F2(iii) after the first build removed 3,921 usable rows including legitimate class-level channel groups; 5c added the third null (admissible in-degree) after I saw the totals rise.

## 3. Registered success criteria (section 3 of the pre-registration)

| Criterion | Result |
|---|---|
| S1 artefacts out | met for the seven families (above). `results/p3_proposals_status_v3.tsv` gives, per P3 proposal, the status and which filter removed it (edge-mode filter alone, identity filter alone). |
| S2 non-failures kept | met in the registered two nulls for JTE-151, curcumin, belzutifan, dichloroacetate, memantine, felbamate; **belzutifan fails the added third null**. |
| S3 mutation tests | `test_v3_filters.py` passes; each assertion is inverted when its filter is off: (a) a P edge into an expression seed contributes 0 in v3 and nonzero in `--mode all`; (b) a T edge into a protein seed contributes 0; (c) a coupling edge in a chain contributes 0; (d) P4HB is credited in the v2 table and not in v3 (also in the DGIdb copy); (e) AR-12's PDK1 claim is present in v2 and dropped in v3; (f) balsalazide's family is flagged. |
| S4 engine tests | T1 to T6 under the three nulls (`results/tests_summary.tsv`). T5 and T6 pass everywhere except **Q4 protein** (T5 fails: only 1 non-zero family, the mutation checks are degenerate) and **Q1 protein** (every score is 0: T1, T2, T3, T5 fail; no admissible edge reaches a WWOX protein seed). T2(b) is not met in Q2, Q4 expression and the provisional set (all defined seeds share one direction), as in v2. T4: ADDS for Q2, Q4 expression, Q5 expression, Q6; NONE elsewhere. |
| S5 comparison | section 4. |

## 4. v2 vs v3 (families; `results/v2_vs_v3_counts.tsv`, `results/v2_specific_families_lost_in_v3.tsv`)

"Seed-specific" = z beyond 3 in the same direction in the two registered nulls (v2 has only these); "all three" adds the admissible-degree null. Non-zero = families with a non-zero score in some arm.

| Seed set | Non-zero v2 -> v3 | Specific opposes v2 -> v3 (all three) | v2 opposes surviving (all three) | Lost to F1 / F2 only / both-or-other / moved to F3 flag | Specific mimics v2 -> v3 (all three) |
|---|---|---|---|---|---|
| Q1 expression (tier A,B,C) | 2,190 -> 1,305 | 0 -> 0 | 0 | - | 0 -> 0 |
| Q1 protein (tier A,B,C) | 2,190 -> 0 | 0 -> 0 | 0 | - | 0 -> 0 |
| Q2 expression | 4,935 -> 2,454 | 53 -> 62 (46) | 34 of 53 | 11 / 0 / 4 / 1 | 71 -> 71 (20) |
| Q3 expression | 4,962 -> 2,599 | 0 -> 0 | 0 | - | 0 -> 0 |
| Q4 expression | 2,701 -> 1,502 | 0 -> 72 (60) | 0 | - | 0 -> 25 (24) |
| Q4 protein | 2,828 -> 1 | 47 -> 0 | 0 | 35 / 0 / 12 / 0 | 5 -> 0 |
| Q5 expression | 5,187 -> 2,867 | 115 -> 274 (189) | 67 of 115 | 9 / 0 / 0 / 2 | 45 -> 244 (166) |
| Q6 expression | 3,219 -> 2,628 | 332 -> 431 (296) | 163 of 332 | 102 / 0 / 2 / 23 | 159 -> 309 (247) |
| Q6 protein | 3,219 -> 1,005 | 332 -> 122 (118) | 90 of 332 | 237 / 0 / 2 / 1 | 159 -> 67 (59) |
| Q7 phospho | 4,235 -> 2,017 | 0 -> 0 | 0 | - | 0 -> 0 |

Reading: the F1 filter is the one that removes families (394 of the 441 lost v2 opposes families; 20 are lost for both or other reasons); F2 on its own removes none of the v2 seed-specific families (its effect on the test list is through the combination with F1, e.g. implitapide), F3 moves 27. Q4 protein collapses because only P edges can reach GAD1/GAD2 protein and the network holds none (0 incoming P edges, 23 T). Nothing in this table is evidence of benefit.

## 5. Top lists for qualification (all three nulls beyond 3 and not flagged; full lists in `results/candidates_Q2.tsv` ... `Q6.tsv` with arms opposes / mimics / flagged_* / direct_search, and `results/v3_seed_specific_all_nulls.tsv`)

Ranked by the smallest |z| over the three nulls. Chain = strongest admissible edge chain from the main target to the seed, with record mode (T/P) and source labels; seeds are P1 v2 rows. "Conditional" arms apply where seed direction is uncertain (none of the lists below depends on that). Names are catalogue family names (salts and duplicates appear as separate rows).

* **Q5 expression (IL6, IL1B, TNF up; 189 opposes)**: JTE-151 (RORC -T-> IL6; z 20 / 18 / 16; qualified as INCONCLUSIVE in P4b: no data), other RORC inverse agonists mirror it in the mimics arm; HMGB1-axis compounds (CD24Fc, bifonazole, L6H21: HMGB1 -T-> IL1B); BRD4-axis compounds (BI-2536 and dual BRD4/PLK1 inhibitors: BRD4 -T-> TNF); curcumin (EP300 -T-> TNF; PAINS flag from P4b, not a chain issue).
* **Q6 expression (MYC up; 296 opposes)**: PIN1 inhibitors (sulfopin, AG-17724, BJP-06-005-3: PIN1 -T-> MYC), NOTCH-axis compounds (tarextumab: NOTCH3 -T-> MYC; gamma-secretase inhibitors osugacestat, MK-0752: APH1A -P-> NOTCH3 -T-> MYC); mimics arm: DYRK1A and CSNK1A1 inhibitors (GNF4877, GNF2133, D4476: kinase -P-> FOXO6 -T-> MYC). **Harmine, which I predicted would leave the expression arm, stays through DYRK1A -P(-)-> FOXO6 -T(+)-> MYC** (a different chain from the one P4b examined: FOXO6 expression in the relevant cells is UNVERIFIED).
* **Q6 protein (MYC protein up; 118 opposes)**: DOT1L inhibitors (pinometostat, EPZ004777, SGC0946: DOT1L -P-> MYC), AURKB inhibitors (defosbarasertib, AT9283, JNJ-7706621: AURKB -P-> MYC), METTL3 inhibitors via USP13 (STM2457, STC-15); mimics: BRD4-axis (JQ1, PFI-1, MS436: BRD4 -P-> MYC). The z values of this single-gene set (hundreds to thousands for some rows) are saturated by tiny null SDs and rank nothing finer than "seed-specific".
* **Q2 expression (glycolysis/lactate up; 46 opposes)**: HIF1A-axis compounds (PX-478, the anti-HIF1A LNA antisense oligonucleotide, nitroglycerin: HIF1A -T-> BNIP3), XIAP antagonists (SM-122, SM-337, AZD5582: XIAP -P-> HIF1A -T-> BNIP3); mimics: sorafenib/regorafenib via ZHX2, XCT790 via ESRRA, HIF prolyl hydroxylase inhibitors (daprodustat, roxadustat, desidustat) via EGLN2 -P-> FOXO3 -T-> SLC2A1/BNIP3. All Q2 rows carry the IT7_READOUT6 guard: none may be evaluated by reversal of the IT7 six-gene readout.
* **Q4 expression (4 seed units, 2 in the network, 10 transcriptional edges; 60 opposes, 24 mimics)**: ATR/ATM/DNA-PK-axis mimics (berzosertib, ceralasertib: ATR -P-> ETV1 -T-> GRIN2C) and MAPKAPK2, GRK2, BTK compounds reaching NPY through FOXO1 or STAT3. These rest on 10 edges and 2 seed genes: the weakest base of any list.

## 6. What prevents candidates, and what data type would help

* **Q1 (residual function, protein fate): zero candidates by construction.** The WWOX protein seed has no incoming post-translational edge in the network (its 7 incoming edges are all transcriptional: NFKB1/2, REL, RELA, RELB, TFAP2C, E2F1); the transcript seed is reachable only through those seven and nothing is seed-specific. Needed: signed regulators of WWOX protein stability or localisation in neural cells (E3 ligases, kinases, chaperones, protein-protein interactions with direction), which no curated edge resource holds.
* **Q3 (ISR) and Q7 (GSK3B pSer9): zero robust proposals** because every seed is direction-uncertain (ISR sign unresolved in human; a phospho site is not kinase activity), so the two conditional arms disagree for every family. Needed: the human ISR sign, and GSK3B kinase activity (not only pSer9).
* **Q4 protein (GAD1, GAD2 protein down): zero** because no post-translational edge reaches GAD1/GAD2 protein. Needed: protein-level regulation edges for GABAergic proteins; and a cell-composition model, because the interneuron cell counts (PVALB, NPY) cannot be gene seeds at all.
* **Q4 expression**: only 2 of the 4 seed genes are in the network and they have 10 transcriptional regulators in all; the list is real but thin.
* **Where candidates exist (Q2, Q5, Q6)** the evidence base is curated transcription-factor edges (CollecTRI, partly text-mined and from non-neural cells) and SIGNOR. Every row therefore needs its edge record qualified in a neural context before it is read as anything more than a direction compatibility; the source labels are listed per chain, the literature references (PMIDs) are not in the committed edge tables and must be fetched (as P4b did live).
* **Single-seed sets (Q6, Q7, Q1)**: z measures specificity to that one gene's regulator neighbourhood, not specificity to WWOX loss beyond the single datum.
* **Level mismatches that remain**: seed observations are mouse or organoid transcripts/proteins; network edges are context-free; molecular-glue and modulator actions (CRBN) carry a source sign that is not activity-down: lenalidomide and pomalidomide flip from "mimics" (v2) to "opposes" (v3 expression) through CRBN -P-> IKZF1 -T-> MYC, and I do not trust that sign (they were the artefact controls).

## 7. Commands

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 build_actions_v3.py --out results/actions                         # compound side, 7 s
python3 seed_engine_v3.py network-report --out results/network_modes.json
python3 run_battery_v3.py --seeds-dir ../seeds_p1 --extra ../seeds_provisional.tsv --out results    # full v3, F1-only, F2/F3-only; both registered nulls
python3 run_adm_v3.py --seeds-dir ../seeds_p1 --extra ../seeds_provisional.tsv --out results         # admissible-degree null (Amendment 5c)
python3 seed_engine_v3.py run --seeds ../seeds_p1/Q5_expression_tiersAB.tsv --actions results/actions --label p1_Q5_expression_tiersAB --out results --top 3500   # contributions for all robust families
python3 seed_adjacent_edges.py --seeds-dir ../seeds_p1 --out results/seed_in_edges_by_mode.tsv
python3 make_candidates_v3.py --seeds-dir ../seeds_p1 --results results --out results
python3 compare_v2_v3.py --v3 results --out results
python3 test_v3_filters.py && python3 ../test_seed_engine.py
```
For P3-style use on a declared universe: `seed_engine_v3.py run ... --universe universe.tsv` as in v2 (`--mode all` reproduces the unfiltered edge use). One readout level per run; one set per question and level.

## 8. UNVERIFIED and limits

* The OmniPath `type` field is a coarse record-level label (99.8 percent of SIGNOR rows read post_translational): a P edge may be an activity change, a binding or a stability effect, and some SIGNOR "post_translational" records are really transcriptional regulation by a protein complex; the mode rule is therefore necessary, not sufficient. Coupling is detected by target gene family only (604 edges).
* Edge literature references are not in the committed tables; chains list source-database labels, not papers. No chain was read against its paper here.
* HGNC licence statement not re-verified here; prodrug flags are ChEMBL's, with unknown (-1) not flagged; the active-moiety record itself is absent.
* The window of "at most 2 P edges then 1 T edge" is a design choice; mRNA-to-protein steps inside the network are still assumed when a TF is the intermediate node (T edges into TF genes are excluded as non-final edges, but a P edge into a TF then a T edge to the seed assumes the TF protein acts).
* Amendment 5b and 5c were written after seeing counts (disclosed); belzutifan's classification depends on 5c.
* No new compound-response data exist; nothing here has a truth to be tested against.

## 9. Files

`PRE_REGISTRATION_V3.md` · `build_actions_v3.py` · `seed_engine_v3.py` · `run_battery_v3.py` · `run_adm_v3.py` · `seed_adjacent_edges.py` · `make_candidates_v3.py` · `compare_v2_v3.py` · `test_v3_filters.py` · `hgnc_lookup.tsv.gz` (+ `.source.txt`) · `results/` (`actions/` compound tables and `build_funnel_v3.json`, `network_modes.json`, proposals, contributions (gz), tests JSON and `tests_summary.tsv`, `per_question_counts_v3.tsv`, `seed_in_edges_by_mode.tsv`, `candidates_Q1..Q7.tsv`, `v3_seed_specific_all_nulls.tsv`, `v2_vs_v3_counts.tsv`, `v2_specific_families_lost_in_v3.tsv`, `p3_proposals_status_v3.tsv`).

## 10. For the batch path

Record the folder as IT9 P2 v3 research material and the method note "the generation engine types edges by record mode, resolves targets by HGNC id and flags prodrugs; 7 of 7 registered provenance artefacts removed; seed-specific lists remain where seeds have transcriptional regulators". No registry, card or need edit is proposed.
