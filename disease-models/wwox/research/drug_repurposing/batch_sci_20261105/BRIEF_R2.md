# Brief R2 (label `sb-r2`): restoration after onset in epilepsy and encephalopathy models, antisense and AAV approaches, human timing precedents

Read `BRIEF_COMMON.md` first; it binds. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/r2_restoration_dee/`. Receipt `NN` = `25`. Scratch (downloads, outside the repository): `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/sb-r2/`. Your sibling `sb-r1` covers syndromic neurodevelopmental models (Mecp2, Ube3a, Fmr1, Tsc/Pten, Syngap1, Cdkl5, Shank3); do not read their sources (check with `paper_packet.py claim`).

## Challenge `CH-SB-POSTONSET-RESTORATION` (task record `ORCH-SCIBATCH-DR-20261105`, part 2)

**Question.** In developmental and epileptic encephalopathy (DEE) and hypomyelination models, and in the human gene-therapy timing precedents with a CNS endpoint, when the gene or its expression is restored or corrected AFTER the phenotype has appeared (conditional re-expression, antisense oligonucleotide, AAV, genome-targeting activation), which endpoint classes recover, which do not, and what decides the difference? Endpoint classes, kept apart: survival; seizure or network hyperexcitability; motor; cognition and behaviour; neuronal structure (spines, dendrites, interneuron number); myelin and glia; systemic and metabolic. Place every study on the module's vocabulary: **PREVENTED**, **RECOVERED**, **EARLY-WINDOW**, **UNMEASURED**, **UNVERIFIED** (definitions in `BRIEF_R1.md`, read that first), and as full, partial, none or worse.

**Decision at stake.** The investigation `INV-01` (rank 1) and the work order `NEED-WWOX-GENE-ADDITION`: external precedents for which endpoints can be expected to recover after onset, with emphasis on seizure and interneuron endpoints and on myelin, the two classes the WWOX add-back results touch, and on delivery by AAV (the module's gene-addition card) as against other modes.

## Done: cite, do not repeat

* `disease-models/wwox/research/drug_repurposing/rescue_window_it6_20261029.md` (WWOX prevented v recovered) and `advance_it8_p5_20261029/loop2_broad_recovery/README.md` (three leads: Shank3, Meis2, Csnk2b).
* The IT29 readers P3-C (myelin transfer conditions) and P3-E (compensatory-role problem in developmental epilepsy) are on the branch `task/it29`: `git -C /home/desktop/legend-development show task/it29:disease-models/wwox/research/drug_repurposing/phenotype_first_it29_20261105/p3_C/README.md` and `.../p3_E/README.md`. P3-E records that Soh 2018 and Wong 2018 bear on interneuron survival being activity-dependent in early postnatal windows; use them as context only.

## New work (hints only; verify every identifier in PubMed)

1. DEE models with restoration or correction after onset: Scn1a (Dravet; gene activation or re-expression after symptom onset; antisense upregulation), Stxbp1, Scn2a, Scn8a (antisense), Kcnt1 (antisense), Kcnq2. For each: age of intervention relative to seizure onset; seizure, survival and cognitive endpoints; interneuron endpoints where measured; authors' stated limits.
2. A hypomyelination precedent where the deficit has been corrected after onset (for example antisense suppression in a PLP1 overexpression model of Pelizaeus-Merzbacher disease): the myelin endpoint, the age at treatment, what did and did not recover, and whether the effect depended on treating before myelination peaked.
3. Two or three human timing precedents with a CNS endpoint and an AAV or equivalent vector delivered pre-symptomatically versus after symptoms (for example spinal muscular atrophy, metachromatic leukodystrophy): outcome by stage at treatment as the primary reports present it, with the limits (small n, historical controls, different endpoints).
4. One counter-search: restoration after onset that failed, was partial, or caused harm.

## Table

`evidence_r2.tsv` columns, identical to `BRIEF_R1.md` (`row_id, role, gene_model, disorder_class, lesion_class, restoration_mode, cells_restored, age_at_restoration_vs_onset, endpoint_class, endpoint_detail, status_vocab, outcome, follow_up, comparator_and_controls, cell_autonomy_stated, authors_stated_limit, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`); for a human precedent put the species in `gene_model` ("human, <disease>") and the stage-at-treatment in `age_at_restoration_vs_onset`.

README addition: a matrix of endpoint class by restoration timing with counts of studies (not a meta-analysis; state publication bias and that models differ); a section "What the added arm of `INV-01` must measure, given these precedents" in at most 10 lines labelled IPOTESI; a section "Conditions under which these precedents do not transfer to the neuron-restricted, short-lived, hypomyelinated Wwox null".

## Consequences fixed before you search

| Return | Consumer action |
|---|---|
| seizure and interneuron-linked endpoints recover after onset in at least one model with an untreated same-genotype comparator | an external-precedent line on the seizure and network endpoint is added to the `NEED-WWOX-GENE-ADDITION` window states; the INV-01 added arm keeps ECoG and a network readout |
| myelin recovers only when treatment precedes the myelination peak | the peak and its anchor become a transfer condition for the timing of the added arm, and the claim "recovery of myelin after onset" is not made for WWOX |
| human precedents show stage at treatment dominating outcome | stated as a human timing precedent with its limits, never as a WWOX expectation |
| nothing reachable for an endpoint class | stated as UNMEASURED in the matrix with the queries |

Breadth: 8 to 12 sources read at full text. Stop when answered or exhausted and say which.
