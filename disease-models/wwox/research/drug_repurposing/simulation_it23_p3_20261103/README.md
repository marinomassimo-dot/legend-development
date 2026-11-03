# IT23 P3: NORDic as an optional capability for simulating interventions on a small WWOX network

Public edition (WWOX-DEE reference genotype class). Computational, exploratory, not medical advice. Closeness of a simulated state to a healthy attractor is NOT proof of functional benefit, and no outcome here is a probability.

## Decision: WATCH

- **NORDic as a package: WATCH.** Do not adopt its pipeline. Its network identification (NI), drug scoring (DS) and screening (DR) modules need LINCS, DisGeNET or STRING credentials (registration is not allowed here), and its drug-target aggregator converts unknown and contrasting actions into inhibition (see `conversion_defect.md`). What NORDic actually uses to simulate is the `mpbn` engine (most-permissive Boolean networks); a perturbation there is a clamp.
- **The method it exemplifies (Boolean what-if with explicit scenarios) is usable as a structural, optional tool** at a cost of hours: `sim_q5.py` is about 150 lines on `mpbn`, runs 3,072 cells in 38 s, and does not need NORDic. It can show which interventions are redundant or sign-dependent under stated premises. It cannot tell which scenario is true, and its inputs for Q5 are not qualified enough to rank interventions. Re-evaluate when the missing inputs below exist.
- Not REJECT because: MIT licence, installs in a venv from PyPI/clone in minutes (about 520 MB venv, no download over 300 MB), imports and runs its simulator offline, and the structural outputs were informative.

## Licences (code, data, weights separately)

| item | status |
|---|---|
| code | MIT, Copyright 2025 (LICENSE file in the repository at commit 9db480d, 2026-08-07; README says the same). Single-commit repository; PyPI latest release 2.8.1 lists no licence field |
| data | example data (notebooks, `Application_*`) have no separate licence file. An older CC BY-NC-SA 4.0 notice for earlier PyPI releases appeared in a search summary and was not verified. The databases it calls have their own terms and mostly need an account (LINCS, DisGeNET, DrugBank, STRING); none was used |
| weights | none shipped (no trained model) |
| LEGEND inputs used | IT7 SIGNOR (CC BY 4.0) and CollecTRI-based tables as licence-filtered in `network_comparison_it7_p3_20261029/inputs/resource_licences.tsv`; only 28 edge rows were derived, no raw third-party file copied |

## Install and inputs

Install route used: `uv venv` + `uv pip install mpbn pandas numpy` and, to import the real NORDic code, its listed dependencies plus `--no-deps` install of the cloned repository (venv under the session scratchpad; nothing system-wide; no heavy step needed more than seconds). NORDic inputs: a `.bnet` rule file (or inferred by NI from credentialed databases), an initial state table (binary), a drug-target table (genes x drugs with -1/0/+1) and a score definition. Outputs: attractors (as dictionaries with `*` for oscillating nodes), similarity to control/treated profiles, a drug score. Full audit of what LEGEND holds: `inputs_audit.tsv`.

Adequacy verdict: signed edges, WWOX seeds with levels and explicit compound actions exist and are qualified; Boolean logic, ligand-receptor edges, the WWOX-to-cytokine link, cell type, pathway-activity readouts and a measured cytokine-to-myelin link do not. Q5 was run anyway because the structural questions (redundancy, hub dependence, sign dependence) do not need those inputs to be answered under labelled premises; every premise is declared and varied.

## Why Q5 (cytokines)

Q5 has 10 usable seed rows over three levels (expression for IL6, IL1B and TNF in two mouse models; histological pathology for GFAP/AIF1; myelin pathology from neuron-specific deletion), against 2 usable rows for Q6 (MYC, one gene, no network around it) and 1 for Q8 (NFE2L2 transcript in a maturity-confounded organoid). Q5 is still thin: cytokines are expression-only, mouse, cell type unresolved, rat model opposite for glia.

## What ran

1. `defect_repro.py`: the real NORDic `retrieve_drug_targets` on five synthetic rows (`logs/defect_repro.log`). Result in `conversion_defect.md`: `?`/`binding` in TTD become +1, presence-only becomes -1, contrasting becomes -1.
2. `nordic_encoding_check.py`: NORDic's own `MPBN_SIM` on one network cell (`logs/nordic_encoding_check.log`). A "perturbation" is `mutation_permanent={node:"0"}`, i.e. the node's rule is replaced by the constant 0. A fixed boolean node at 0 is therefore not an inhibitor administered: it is a clamp with no dose, no timing, no partial effect and no state dependence, and it is the same call for a genetic knockdown and for a drug. The only difference between the two is which layer the user picks. In `sim_q5.py` pharmacological modulation is an explicit drug-switch input `D_x` that modifies the target's activity rule and is switched on only after the disease state has formed (reversal), whereas a genetic knockdown clamps the node from the start (prevention) and may be set on the transcript layer, so `IL6_tx` (the seed's level, expression) and `IL6_sig` (the neutralisable signal) stay distinct nodes.
3. `build_inputs_q5.py` then `sim_q5.py` then `analyze_q5.py`: 21 network nodes (18 rule nodes plus 3 scenario inputs) plus 9 drug-switch inputs = 30 variables; qualified edges (28, from IT7) and ASSUMED edges (9, labelled) in `inputs_q5/`; 32 premise combinations (cytokine promoter logic OR vs cofactor-required; receptor edges present/absent; negative feedback on/off; qualified positive self-loops on/off; IL1B needs caspase-1 or not) x 6 scenarios x 16 interventions = 3,072 cells (`results/sim_q5_all.tsv`, summary `results/sim_q5_summary.md`, log `logs/`).
   Scenarios for the unknown role of the raised cytokine program: damaging (as mediator; joint with the neuronal route; redundant with it), compensatory, consequence (downstream of damage), feedback (transient trigger, self-sustaining), and unresolved (damaging vs compensatory compared cell by cell, section 4 of the summary).

## Findings (structural, under premises)

- **Single-cytokine neutralisers are inert on the network readouts in all 32 premise combinations** (IL6, TNF or IL1B neutralised alone), because RELA/STAT3 drive all three transcripts; only the triple blockade or a hub hit (IKK, RELA, EP300 under cofactor logic) switches the cytokine signal off. This is partly a consequence of the node subset (IL6 has 96 incoming signed edges, five were used), so it says "redundant in this subset", not "redundant in the brain".
- **Which outcome follows is set by the scenario, not by the intervention.** The same intervention is benefit in damaging, harm or no change in compensatory, and nothing in the network moves myelin under "damaging_redundant" or "consequence". The triple blockade and RELA knockdown are sign-dependent (benefit if damaging, harm if compensatory) in 32 of 32 combinations, EP300 inhibition in 16 and IKK inhibition in 8 (the others give no change); this restates the premise and is not new information about WWOX.
- **Does the simulation separate what the current method treats as equivalent? Only conditionally.** BRD4 and EP300 inhibitors (both inhibit, both have a qualified positive edge onto the TNF/IL6 seeds, both H_HARM in `generation_it22_p1_20261103/results_p4/proposals_it21.tsv` for Q5) are separated in 16 of 32 combinations, all under the unqualified cofactor-required logic, and in 0 of 16 under OR logic. The separation exists only if an assumption absent from the data is made. Pharmacological vs genetic at the same node differ only on layers (transcript vs signal) and on prevention vs reversal in the transient-trigger scenario; at full effect the Boolean outcome is identical.
- **Comparison limit:** IL6, TNF, IL1B, JAK2 and STAT3 are not main targets of any Q5 row in `proposals_it21.tsv` (main targets there include BRD4 43 families, SYK 31, FGFR3, ROCK2, RORC, EZH2), so only the BRD4/EP300 pair could be set against the current method.
- **Feedback:** a transient trigger leaves a self-sustaining state in 24 of 32 combinations (8 resolve, only when neither receptor edges nor the qualified RELA/EP300 loops exist). The sustaining loops come from two kinds of edge: assumed receptor steps, and a qualified but crude positive self-edge (RELA to RELA, RELA to EP300 to RELA) which a Boolean rule turns into bistability.

## What did not run, and why

- NORDic NI, PMR, DS, DR end to end: need LINCS, DisGeNET or STRING credentials; no registration. `bonesis` network synthesis not run.
- No human-system run, no mouse-to-human mapping beyond symbol identity, no fitting to any expression data (the only Q5 expression contrast, S079, is UNUSABLE for maturity/composition).
- No attempt to estimate how likely any scenario is: Boolean outcomes are listed, never weighted.
- Q6 and Q8 not simulated (one and two usable rows; nothing to build a network around).

## Missing inputs and the measurement that would supply each (exact list)

1. Cell type that makes IL6/IL1B/TNF in Wwox-deficient brain: cell-resolved transcript (single-nucleus RNA-seq or sorted-cell qPCR) at the age already measured.
2. Protein-level cytokines and pathway state (IL1B/IL6/TNF protein, phospho-STAT3, nuclear p65, cleaved caspase-1) in the same tissue: tells whether the RELA/STAT3 hub is on and whether the transcript rise is a signal at all.
3. A measured signed link from the cytokine axis to myelin in a WWOX system: one cytokine-axis perturbation (receptor or ligand loss, or a neutraliser) in a Wwox-deficient model with a myelin endpoint (g-ratio, myelinated-axon count). This is the discriminating experiment among damaging, compensatory, consequence and feedback; endpoints of this type are held out as reserved in the seeds file and were not used.
4. Signed ligand-receptor-pathway edges and promoter logic for the cytokine genes: a curation and qualification step on public tables, not a measurement; until then they stay ASSUMED.
5. Exposure and CNS penetration of any compound named: absent from the actions table, so a simulated drug is a target sign only.

## Files

`README.md`, `inputs_audit.tsv`, `conversion_defect.md`, `defect_repro.py`, `nordic_encoding_check.py`, `build_inputs_q5.py`, `sim_q5.py`, `analyze_q5.py`, `inputs_q5/` (edges_qualified, edges_assumed, actions_explicit, seeds_q5), `results/` (sim_q5_all.tsv, sim_q5_summary.md, defect_repro.json), `logs/`. Reproduce: `python3 build_inputs_q5.py`; then with the venv python `-I`: `defect_repro.py`, `nordic_encoding_check.py`, `sim_q5.py`; then `python3 analyze_q5.py`.
