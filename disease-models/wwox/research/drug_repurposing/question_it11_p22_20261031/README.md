# IT11 P2.2: neurogenic output and the MYC-high radial-glia state (question Q6, widened)

Scientist `scientist-b`, task `ORCH-ROADMAP-IT11` package P2.2, branch `task/it11-p22`, 2026-10-30 UTC (the directory name carries 20261031 as assigned). Exploratory, non-canonical, **not medical advice**.
Reference genotype: a WWOX-DEE genotype class; no individual-level record. A compatible action of a network is not a predicted benefit; a conditional hypothesis is not a recommendation.
Nothing here edits a card, a need, the ranking, a registry, the four current files or the receipt ledger; the edits this work implies are in section 8.
No e-mail address, account or personal datum was sent to any service (Europe PMC REST and ChEMBL REST, key-less; no `mailto`).

## 0. Not blind

I read the IT9 and IT10 packages (section 1) **before** choosing the question and before any search, so every comparison below is informed by earlier results. The five phenotype leads and PLK1 were development inputs in IT10, not validation. IT10 showed no new compound activity in a WWOX system; the pre-existing WWOX results (A51 in the knockout organoid; AAV9 add-back) are the only compound- or intervention-level WWOX data on this axis.

## 1. What I had read when I chose

| Read | Depth |
|---|---|
| CLAUDE.md, state manifest (`current_state: READY`), LEGEND_CORE 21c/21d/21e via the router, brief, `matching_guidance_v3.md` method (via IT10 README) | named sections / README level |
| `generation_it9_p1_20261030/questions.tsv` (all seven questions and the dropped D1 to D6), `seeds.tsv` rows of Q5 and Q6 | full rows for Q5, Q6; other questions by title and counts |
| `generation_it10_p1_20261031/question_roles.tsv`, `README.md` (head), `results/dispositions_Q6.tsv`, `results/deepening_candidates.tsv`, `results/phenotype_first.tsv` (A51 and lithium rows), `results/disposition_counts.tsv` | tables computed (script `engine_q6_census.py`) |
| `cards/` heads of D01 (A51), D02 (Wnt), G01 (lithium) and the full K01 packet (schema), `check_cards.py` | read |
| `needs/needs.json` (`NEED-MYC-PROGENITOR-PROLIFERATION` in full; ids of all 23), `view/work_order.json` entry | read |
| `qualification_it9_p4c_e_20261030/selection_note_E.md` and `qualification_E.tsv` (E-01 to E-06) | read |
| `axis_it10_p22_20261031` (patch and packet conventions, P5 integration notes) | read |
| `gse156243/prediction_wnt_sign_20261025.md`, `disease-models/wwox/analysis/a51_antiproliferative_confound_20260921.md`, `fulltext_dossiers/PMID42397075_partial_locators.md` | read |
| `wwox_function_reference_it6_20261029.md`, `wwox_data_census_it6_20261029.md`, `mouse_wwox_p17_it6_p4_20261029/`, `ranking_it8_p9_20261029/` units | searched by key terms (MYC, radial glia, PMID 42397075); not read end to end. I did **not** read `uncarded_items.tsv` or the mouse P17 tables in full: stated so the omission is not hidden |

## 2. Decision (first)

| Item | Answer |
|---|---|
| Question chosen | **Q6 widened to "neurogenic output and the reversible part of the neuronal maturation state"**: is the MYC rise in WWOX-deficient radial glia a *driver*, a *marker of retained progenitor state* or a *consequence of the cell-cycle shift*; and which compartment (radial glia, prenatal; post-mitotic neurons) a lever could reach after birth. |
| Why this one | It has no card of its own (only D01 A51 and D02 Wnt, both abstentions), its question-table entry is "abstract-level confirmation only", and its IT10 engine output is one evidence origin (192 candidate rows from one article). The full text and three figures are in the repository and were readable, so premises could be checked at the source. |
| Not chosen, and why | Q5 myelin/glia (cards F02, J01, H02; IT10 P2.2 just worked NRF2 and corrected the Il6/Tnf-a premise); Q4 E/I (F01, F03, F04, H01, P11); Q3 ISR (E01; the sign is unmeasured, nothing new is readable); Q1 residual function (A, B, C cards; IT10 P2.3). Metabolic compensation other than HIF has no new data source (the MYC-glycolysis link is a discussion-level claim in the paper). |
| Outcome | **No candidate is strengthened** (corrected reading, IT11 P4, section 11: the authors read the A51 result as MYC-driven impairment of differentiation, NEUN+ up, SATB2 mildly up, CTIP2 unchanged; 'no candidate strengthened' rests on the non-selectivity of the multi-kinase compound A51 and on design gaps, namely no wild-type-plus-A51 arm and no supplement available locally, not on a result that contradicts the authors). One restated compound is narrowed, one is flagged as a risk for this window, one external name is dropped, and the Q6 engine rows are shown to be unable to answer the question. What survives is a discriminating experiment (T1 to T3) and a reframing: the layer-marker deficit that neuron-stage add-back restores is a **reversible neuron-stage state**, an endpoint for the neuron compartment, not a repurposing target. |
| Does the role of the observed change (IT10 `question_roles`) resolve? | **No: Q6 stays `unknown`.** Evidence is split (section 5); none of it is a role-stating source for a WWOX neural system. |

### Findings that move the reading (each with a locator in `premises.tsv`)

1. **MYC elevation is not sufficient for the radial-glia/neuron phenotype (PR2).** MYC-positive fraction of SOX2-positive cells is up in the engineered knockout, WOREE and SCAR12 (Fig 3K medians read by eye about 68, 55 and 45 against 18 percent in wild type), but SCAR12 radial glia are "similar to WT" and the neuron decrease "was not the case in our patient-derived organoids".
2. **The "top gene" is a fold-change ranking and OCT4 is as prominent (PR1).** MYC, POU5F1, EEF1B2, SFRP1 and TPM2 sit at the capped significance ceiling in Fig 3F; MYC has the largest fold change. A retained-pluripotency-programme reading (H-B) is as supported as a MYC-specific one.
3. **The inverse WWOX-MYC relation in reference human data is a developmental time course (PR6)** and MYC is phase-coupled in the knockout only (PR7): maturity and cell-cycle state can raise MYC without a driver role. The bulk Wnt readouts of the older organoid deposit correlate +0.99 with a radial-glia score (PR16): composition-entangled.
4. **Neuron-stage biology bounds what a radial-glia lever can matter for (PR3, PR4).** In mouse, Synapsin-Cre (post-mitotic neuron) deletion reproduces the null phenotype as nestin-Cre does; in WOREE organoids neuron-promoter add-back at week 10 raises CTIP2 and SATB2 fractions and lowers firing **without** touching radial glia. So at least part of the layer-marker deficit is a reversible neuron-stage state, and the severe mouse endpoints do not require a radial-glia correction. (Not shown: that radial glia are irrelevant for human cortical architecture; one human fetus and a rat show prenatal layering defects, PR17.)
5. **MYC-family dose is two-sided in cortex (PR9)** and progressive microcephaly is part of the WOREE picture (PR10, 4 of 5 in one cohort). A lever that pushes MYC-family output below normal is expected to shrink the progenitor pool; MYCN is not MYC, so this is a risk flag, not a result.
6. **The A51 arm is thinner than "MYC inhibition" suggests (PR5).** Knockout organoids only (no wild-type-plus-compound group attested), one of three experiments without independent differentiations, no randomisation or blinding stated for the whole study (the authors' clause is 'using multiple biological replicates'); panel values come from prior-session attestations because the supplement is not available locally.
7. **The IT10 Q6 table is one origin (PR14).** 292 rows; 192 candidate rows (100 opposes, 50 mimics, 27 and 15 flagged) all rest on one article at two readout levels; 240 families; 100 direct-search rows are diagnostic only. The 22 BRD4-family rows are placed under the arm that *raises* MYC, while BET inhibition lowers MYC transcription in myeloma cells (PR13): a different mechanism layer (a text-mined phosphorylation edge), but the label must not be read as "mimics the rise".

## 3. The cycle for this question (observation, interpretation, hypothesis, lever, compound, limit, test)

| Step | Content |
|---|---|
| Observation | MYC transcript up in knockout radial glia (PR1); SOX2+MYC+ fraction up in three mutant lines (PR2); radial-glia expansion and neuron loss in the knockout, not in SCAR12 (PR2); early-neuron signature in both patient lines; S/G2M enrichment and a "high potency" shift in knockout radial glia (PR7); neuron-stage add-back restores layer markers in WOREE with radial glia unchanged (PR4); Wwox/Trp53-null bone-marrow cells show MYC up and WWOX add-back lowers Myc protein (PR8). |
| Interpretations (rivals) | **H-A driver**: MYC holds radial glia in cycle and blocks the neurogenic switch. **H-B marker**: MYC (and POU5F1) are high because the cells are held at an earlier state; or maturity differs. **H-C consequence**: MYC rises as part of an S/G2M-enriched population (cycle) or through Wnt/TCF4 or DNA damage. **H-D split**: a prenatal radial-glia substrate and an independent, reversible neuron-stage state coexist. |
| Predictions that separate them | H-A: MYC lowering by a specific lever restores neuronal fractions in knockout beyond corrected cells; MYC stays higher within G1/G0 cells. H-B/H-C: the MYC difference vanishes within cell-cycle phase and potency strata; MYC lowering does not move neuronal fractions beyond a cytostatic control. H-D: stage-specific add-back separates a progenitor effect from a neuron effect. SCAR12 (MYC up, composition normal) is hard for a simple H-A and compatible with H-B, H-C or an H-A with a threshold. |
| Lever | Lower MYC (genetic first), lengthen G1 (cell-cycle lever), lower Wnt (D02), or add WWOX at the right stage. |
| Compound or intervention | A51 (WWOX-system result, non-selective); a PIN1 probe (IT9 E-06); CDK4/6 inhibitors as a cell-cycle arm; stage-specific WWOX add-back. Lithium acts in the same direction as the Wnt/MYC rise: a risk flag. |
| Limit | The radial-glia phase is prenatal in humans; every neural datum is one laboratory in organoids; MYC, cycle and potency are transcript-level or computational; no selective MYC lever has been used in a WWOX system. |
| Discriminating test | T1 to T3 (section 6). |

## 4. Candidate table (short; all columns in `candidates.tsv`)

State vocabulary: KEEP / CONDITIONAL / INCONCLUSIVE / DROP / REFERENCE-ONLY. Probe verdict and development verdict are separate. "Decisive datum" is the one datum that sets the state.

| Id | Compound or lever | Action | Context | Hypothesised benefit | Discriminating test | State | Decisive datum |
|---|---|---|---|---|---|---|---|
| M01 | A51 (restated; D01) | multi-kinase, lowers Wnt and MYC; no catalogue identity | knockout organoid weeks 8 to 15 | restores neuron output if the progenitor MYC/Wnt state is a driver | three-way split vs genetic MYC, genetic Wnt, cytostatic control, with wild-type-plus-compound group and cell counts | **CONDITIONAL** (probe; development NOT SUPPORTED) | attribution to MYC is open; no WT+A51 group, no denominators (PR5) |
| M02 | sulfopin (restated; IT9 E-06) | covalent PIN1 inhibitor | ex vivo neural progenitors over the neurogenic window | lowers MYC protein if MYC is a driver | beside genetic MYC lowering, stratified by cycle phase | **CONDITIONAL** (ex vivo probe only; development NOT SUPPORTED) | cannot settle driver vs marker by itself (PR2, PR3); no human exposure |
| M03 | STM2457 (IT9 E-04) | METTL3 probe | neural progenitors | none (opposite expected) | not proposed | **DROP** (IT9 stands) | reasons are role-independent |
| M04 | nirogacestat, D4476 (IT9 E-03, E-05) | gamma-secretase; CK1 | n/a | none | not proposed | **DROP** (IT9 stands) | chain-provenance and label reasons, not role reasons |
| M05 | **palbociclib, abemaciclib** (new names, 2) | CDK4/6 inhibition (database potency nanomolar) | radial glia ex vivo | lengthens G1 if shortening is causal | does the cycle shift persist at matched potency; G1 duration; then CDK4/6 vs genetic arms | **REFERENCE-ONLY** | G1-switch evidence is genetic and murine; G1 duration unmeasured in WWOX cells; no pharmacological study in cortical progenitors found (PR11) |
| M06 | **simvastatin** (new name, external WWOX path) | HMG-CoA reductase; lowered MCM7 and growth in Wwox/Trp53-null cells | bone-marrow cells (non-neural) | none identified for neural development | not proposed | **DROP** | cancer proliferation endpoint in a p53-null cell; no step to radial glia (PR8) |
| M07 | lithium (restated; G01), **new context hypothesis** | GSK-3 inhibition, Wnt activation | the neurogenic window (the G01 seizure lead is untouched) | none expected; adverse if Wnt/MYC elevation is harmful | Wnt reporter, SOX2+MYC+, NEUN+ and counts with lithium vs a GSK3-selective probe | **CONDITIONAL** (narrowed: not a Q6-axis benefit candidate; risk flag) | lithium expands progenitor pools through Wnt in vitro (PR12), same direction as the knockout Wnt/MYC rise |
| M08 | **Omomyc / OMO-103** (new name) | dominant-negative MYC mini-protein | ex vivo | MYC-specific reference | use only if genetic lowering is not feasible | **REFERENCE-ONLY** | modality; no catalogue identity; no neural exposure datum |
| M09 | BET inhibitors as a family (engine rows) | lower MYC transcription in myeloma cells | n/a | engine labels them "mimics" | not proposed | **REFERENCE-ONLY** (warning on the label) | pharmacology on the transcript is opposite to the engine arm (PR13) |
| M10 | stage-specific WWOX add-back (gene; C01, C04) | restores WWOX | organoids | neuron stage: layer markers restored; progenitor stage untested | add-back before week 4 vs week 10 with MYC and layer-marker readouts | **REFERENCE-ONLY** | a neuron-stage reversible component exists (PR4); the progenitor component is untested |

Counts, kept apart:
* **New compound names carried: 4** (palbociclib, abemaciclib, simvastatin, Omomyc/OMO-103). Qualified here: identity and aggregated database potency for palbociclib, abemaciclib, simvastatin, lithium carbonate; Omomyc and JQ1 did **not** resolve to a clean catalogue record by name search (not qualified). Label, paediatric status and trials were **not** searched for any of them.
* **New hypotheses on known compounds: 2** (lithium: context split, window risk flag; sulfopin: window-bound probe that needs a MYC-specific co-lever). A51 is restated, not counted (its three-way reading was already in the 2026-09-21 analysis).
* **Restated known, unchanged: 4** (STM2457, nirogacestat, D4476 from IT9; A51).
* The engine produced 192 Q6 candidate rows; the question did not use them as a list. **No name here was chosen by its engine rank.**

### Reconciliation with IT9 and IT10 qualifications
* STM2457, nirogacestat and D4476 were removed by specific IT9 paths (neural-fate precedent, chain-provenance and label reasons, FOXO6 direction); none of those reasons depends on the role of MYC, so the IT10 `H_HARM/H_PROTECT` split does not give them back (IT9 `role_dependent_reasons` lists only roxadustat and harmine). They are not reopened and not carried.
* Sulfopin: the IT9 record is `KEEP-AS-PROPOSAL, conditional on the seed valence experiment`; this package keeps it CONDITIONAL and adds that the valence experiment cannot be read from a PIN1 probe alone (PR2, PR3).
* A51: the D01 packet says layer-neuron production is not restored; the main text says NEUN+ rose, CTIP2+ unchanged and SATB2+ "mildly" up, and `needs` O3 says no significant change for SATB2 and CTIP2. These agree only if the SATB2 change is non-significant; the supplementary panel was not available to settle it (UNVERIFIED).
* Lithium: card G01 (non-specific seizure suppression in null pups) is unchanged; the new statement is only about the neurogenic window.
* Cross-card link (inference, not read in this package): the K01 packet already lists MYC as a rival arm for the organoid HIF-type transcripts (bulk MYC +0.56 log2) and notes composition. The finding that Wnt readouts track a radial-glia score at +0.99 (PR16) and that radial glia are expanded in the knockout supports giving the K01 step-0 MYC arm and a progenitor-composition control the same weight as the HIF arm. Proposed, not applied.

## 5. Evidence on the role of the MYC rise (kept separate from direction and from benefit)

| Reading | Supports | Against |
|---|---|---|
| Harmful driver (H_HARM) | A51 lowers progenitor fractions and raises NEUN+; MYC top fold-change; high-potency shift; MYCN gain of function gives megalencephaly by excess intermediate-progenitor proliferation (PR9) | SCAR12 dissociation; POU5F1 co-top; developmental co-variation; one non-selective compound; mouse neuron-stage deletion reproduces the null phenotype |
| Protective or compensatory (H_PROTECT) | microcephaly in patients and MYCN loss giving microcephaly (progenitor pool needs MYC-family dose); p53 raised in knockout neural stem cells (paper, supplement-level, not read here) | no source states a protective role; a compensatory reading is not tested anywhere |
| Marker or consequence | cycle coupling in knockout only; developmental time course; Wnt readouts track a radial-glia score | no stratified analysis exists (T1 proposes it) |

## 6. Discriminating tests (proposed, none run)

* **T1 (computational, needs the deposited single-cell data E-MTAB-14792; an access request draft exists in the module)**: MYC and POU5F1 difference between knockout and wild-type radial glia **within G1/G0 only** and **within matched potency strata**. Falsifies H-A if the difference vanishes. Also repeat for SCAR12 radial glia.
* **T2 (wet lab, two independent knockout clones and corrected lines)**: genetic MYC lowering (inducible degron or CRISPRi) against a cytostatic control and against A51 and a PIN1 probe, with SOX2+MYC+, pH3+ and NEUN+ fractions **and absolute cell counts per organoid**, wild-type-plus-compound groups included; stage-specific add-back (before week 4, at week 10) with MYC and CTIP2/SATB2 readouts. A CDK4/6 arm only after T1 shows the cycle shift persists at matched potency.
* **T3**: the same strata in SCAR12, to ask whether MYC elevation without a composition change is a stage effect.
* **Falsifier**: a specific MYC lever does not move neuronal fractions or the progenitor fraction in knockout cells beyond what it does in corrected cells, or the MYC difference disappears within phase and potency strata.

## 7. Limits and disclosures

* Non-blind reading, informed by IT9 and IT10; a same-actor fragment re-read (`selfaudit_reread.py`) is mechanical and is **not** a blind audit. No receipt was staged (section 8 proposes them).
* **Supplementary figures of PMID 42397075 are not in the repository** (supplementary PDFs absent): the A51 panel values, the p53 and TCF4 blots and Supplementary Figs 4 to 7 were not read here; they are carried as prior-session attestations or not at all.
* PMID 42397075 was read as the accepted-manuscript text plus Figures 3, 4 and 6 (images viewed); Figures 1, 2 and 5 were not viewed in this package; the Figure 5 percentages in the packet come from an earlier dossier entry.
* External sources are abstract or passage level (labelled); the MYCN, G1-length, lithium, BET and CDK4/6 rows are abstracts only. "Not found" for pharmacological CDK4/6 work in cortical progenitors means four oncology hits for one query, not absence.
* Aggregated ChEMBL potency ranges include extreme values and unaudited assay classes. Labels, trials and paediatric status were not searched. The packet's `label_lookup` is `NOT_ATTEMPTED`.
* The engine census describes the IT10 table; a count is not biology.
* `JAK2`-family rows (25 opposes rows by first node; IT9 flagged them as the next round) were **not examined**: no source connecting JAK2 to MYC in neural progenitors was found in this package.

## 8. For the batch path (proposals only, nothing applied)

1. **Place the packet** `M01_neurogenic_output_myc_window.packet.json` under `cards/` and build its card with the bridge. Validation done on a scratch copy: `check_cards.py` logic on the packet and its bridge-built card, **0 problems** (label_lookup `NOT_ATTEMPTED`, no dose-looking token or ellipsis, every compound row other than the A51 arm labelled NOT WWOX EVIDENCE, no score-like key, no receipt id invented).
2. **Needs patch** `needs_patch_proposal.json` (O2 limits appended; new observation O4 for the neuron-stage add-back; four counter-evidence lines; `do_not_assume` restated). `apply_and_check_patch.py` applies it to a scratch copy: `check_needs.py` exit 0 (output in `apply_and_check_output.txt`). The card pointer is excluded from that test until the card exists. **Overlap:** O4 touches the gene-addition need; it must not be counted twice across needs.
3. **Work-order patch** `work_order_patch_proposal.json` replaces the entry of `NEED-MYC-PROGENITOR-PROLIFERATION` (kind kept; the old A51 question is folded into Step 1; `feasibility_it` carries "non nota"). **Not validated** against `repurposing_view.py`.
4. **Ranking**: a unit for card M01 (mechanism probe, origin generated in IT11), and reference or DROP units for palbociclib/abemaciclib, simvastatin and Omomyc by the existing mechanism; group by the existing rule, not asserted here.
5. **Questions table**: Q6 `data_quality_note` ("abstract-level confirmation only") is out of date: the main text and Figures 3, 4, 6 were read here. Seed S117 ("no error bars") is confirmed from Fig 4C.
6. **D01 packet wording** on layer neurons: reconcile with the supplementary panel when it is obtained (see section 4).
7. **Proposed receipts (not written)**: partial read of PMID 42397075 accepted-manuscript text and Figures 3, 4, 6 with locators PR1, PR2, PR4, PR5, PR6, PR7; partial read of PMID 38182577 Results passages (PR8); partial read of PMID 33914858 Fig 1 and Results (PR3) if not already covered.
8. **Engine**: record that a text-mined edge sign can place a pharmacologically opposite family in the wrong arm (BRD4 rows, PR13); a check of edge sign against one primary pharmacology paper per cluster would catch it.
9. **K01**: give the MYC arm and a progenitor-composition control equal weight to the HIF arm in step 0 (inference; section 4).

## 9. Verification

* `selfaudit_reread.py` (output in `selfaudit_reread_output.txt`): 20 fragments of the three most decisive premises (PR2 SCAR12 dissociation, PR3 mouse conditional deletion, PR4 week-10 add-back) and the other premises found at the stated line windows; two figure hashes match. Fig 3K was viewed twice; medians stated as read by eye.
* Self-audit re-read of the three most decisive premises: PR2, PR3, PR4 re-found in the source text at the stated lines; PR2's panel numbers are visual estimates and are labelled so.
* Packet check: 0 problems; needs scratch check: exit 0.

## 10. Files

`README.md`, `candidates.tsv`, `premises.tsv`, `search_log.tsv`, `engine_q6_census.py`, `engine_q6_census.tsv`, `M01_neurogenic_output_myc_window.packet.json`, `needs_patch_proposal.json`, `work_order_patch_proposal.json`, `apply_and_check_patch.py`, `apply_and_check_output.txt`, `selfaudit_reread.py`, `selfaudit_reread_output.txt`.

## 11. Correction section (IT11 P4 integration, 2026-10-30 UTC; verifier corrections applied; original wording kept in `corrections_it11_p4.tsv` and in git history)

| # | Premise | Original wording | Corrected reading |
|---|---|---|---|
| a | PR2 | 'neurons are not reduced in the patient-derived lines' | holds for the single-cell neuron-cluster fraction (Fig 2F, text L585-586) and for SCAR12; WOREE shows reduced CTIP2 and SATB2 fractions (Fig 6B), so SCAR12 is the clean dissociation case. Text/figure mismatch, flagged: the text (L570) states a prominent RG increase in WWOX-KO and WOREE; Fig 2F (viewed again in IT11 P4, by eye) shows WOREE RG log2 fold change about +0.05 (KO about +0.9, SCAR12 about -0.2). Not resolved. |
| b | PR3 | Synapsin-Cre 'leaves progenitors largely WWOX-intact'; 'death by 4 weeks' | the progenitor statement is an inference (Synapsin I promoter, 'particularly in most of the differentiated neurons', L361-362; progenitor Wwox status not measured). 'by 4 weeks of age' is stated for nestin-Cre N-KO (L347, Fig 1F); Fig 1I shows premature death for S-KO without a stated age. |
| c | PR5 | 'one of three without independent differentiations; no randomisation or blinding' | full clause: 'Experiments were performed in independent differentiations, except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq, using multiple biological replicates' (L380, L386-387); 'No randomization or blinding was applied in this study' (L417) is study-wide, not specific to the A51 arm. |
| d | PR9 | MYCN dose acts 'in both directions' | the Mycn-null result also raised neuronal differentiation in null progenitor cultures (PMID 12381668 abstract): the dose effect is two-sided. |
| e | headline | 'No candidate is strengthened' | the authors read the A51 result as MYC-driven impairment of differentiation (NEUN+ up, SATB2 mild up, CTIP2 unchanged; L980-983). 'No candidate strengthened' rests on non-selectivity (multi-kinase A51, two pathways) and on design gaps (no WT+A51 arm, supplement unavailable), not on a contradicting result. |

Edited in place: `premises.tsv` (PR2, PR3, PR5, PR9), `M01_neurogenic_output_myc_window.packet.json` (measured-result notes), `needs_patch_proposal.json` (O2 sentence), this README. `candidates.tsv` holds no affected sentence. The supplement remains unavailable.
