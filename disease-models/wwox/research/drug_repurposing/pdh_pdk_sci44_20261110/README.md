# SCI44 package A — PDH/PDK: which cells, which isoform, which action (2026-11-10)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; no compound is promoted. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI / ESPANSIONE. Task record `ledger/tasks/orchestrator/ORCH-SCI44-20261110.json`. Paths below are relative to this folder.

## Answer first: what became possible

1. **The generic "inhibit PDK" lever splits into three choices that sources now support.** (a) The premise measurement must be **read per cell class**, because the dominant kinase RNA differs by class and by species (mouse cortical neurons Pdk2; human cortical neurons PDK3; astrocytes PDK4 in both species; human oligodendrocytes PDK4; mouse oligodendrocyte lineage Pdk2 then Pdk3). (b) The **first probe is chosen by the dominant kinase and by the scaffold condition**, with a genetic knockdown of the dominant isoform as the reference: AZD7545 has core-bound inhibition rows only on PDK1 and PDK3 and stimulates the core-free kinases (PDK3 10-fold, PDK4 2.8-fold), so in PDK4-dominant classes its sign is unmeasured. (c) **Lowering PDK is also a risk arm**: documented harm directions and a lactate-supply role make a net benefit by class unknown.
2. **A new alternative lever and probe family at the same node** (lactate side: oxamate-type LDH inhibition, stiripentol as a mixed-mechanism comparator, MCT2 and MPC probes; fuel controls). Verified evidence says: LDH inhibition shortened status epilepticus in adult mice and lowered CA1 activity, an astrocytic lactate route is functionally real in adult dmPFC, and the sign of a lactate-side change depends on the cell compartment. It is a **probe and an arm that discriminates, not a lever with demonstrated benefit**.
3. **A link from the metabolic premise to the potassium branch of SCI43** that the producer wrongly closed and the independent verifier reopened: in juvenile (P13-24) rat and mouse barrel cortex, KATP modulators change Vm, Rin and firing (diazoxide roughly doubles whole-cell conductance) and 15 mM lactate roughly doubles firing through KATP closure (absent in Kcnj11-/-; perforated patch). Lactate closes KATP, which is a conductance loss with an E_K reversal. **PH4 (IPOTESI):** a lactate-closed KATP conductance could carry part of the Wwox Rin and rest pattern. It is conditional on lactate being raised in the KO slice and on the pipette ATP of the recordings (not recorded in the held table). It adds a tool-rich arm (diazoxide, sulfonylureas) to SCI43's difference-current ladder and shares the preparation.
4. **Nothing is promoted and no candidate is named.** Roles: dichloroacetate comparator (reference), VER-246608 probe, AZD7545 scaffold-sign probe (conditional), devimistat and four PDPK1-linked listings excluded from this lever, oxamate probe, stiripentol comparator, UK5099 probe, triheptanoin fuel control, KATP tools probes for PH4 (`output/tools_roles.tsv`).

## What was examined (coverage kept apart)

| Part | Sources | Depth actually reached |
|---|---|---|
| A2 expression (mouse GSE52564, human GSE73721, HPA documented downloads) | 360 rows, 9 papers newly read | per-sample GEO tables and HPA files re-extracted by the verifier with its own code (0 numeric defects in 360 rows); figures viewed: two (35355991); protein only coarse IHC; per-cell-type protein tables not reached (proof-of-work page, dead portal) |
| A2 function in neural cells | 15 rows | 5 PMC texts partial; 4 paywalled papers abstract only |
| A3 primary pharmacology | 10 sources | Kato 2007 text, Fig 2; Moore 2014 Table 1, Figs 2 and 3; Wynn 2008 Tables 2-3; Li 2009; the 2003 AZD7545 paper (14641019) **not reached** (HTTP 403, one route) |
| A4 alternative actions | 9 sources | partial full text; figures viewed by producer: three papers; by verifier: four; Sada 2015 **abstract only** (HTTP 403); oxamate sEPSC concentration unverifiable |
| Independent verification | V1 (A2 expression, A3), V2 (A4, A2 function rows) | 93 staged receipts of the producers and verifiers; `verify/v1/audit.md`, `verify/v2/audit.md` |

## What the verification changed (details in the audits and `output/CORRECTIONS_V1.tsv`, `output/CORRECTIONS_V2.tsv`)

* **Overturned:** the producer's absence claim that no source measured a metabolic-to-K+ effect in cortical neurons (A4D12), and the sentences "opposite sign" and "a fuel could only offset a loss if KATP-type". The dmPFC null on Vm and Rin is a GFAP-Cre conditional knockout, not an astrocyte-specific adult deletion. The acetate absence clause is refuted.
* **Corrected:** the HPA single-nucleus numbers are an 11-region, 34-supercluster aggregate (three postmortem donors; cortex-only values keep the ranks); the AZD7545 "sign depends on the scaffold" claim is the authors' for PDK3 (PDK1 core-free rise is "marginal"; PDK2 not tested in the paper; PDK4 core-bound unmeasured); a DCA datum on PDK4 was added; CHEMBL257158 is GlcNAc-thiazoline; D09, D11 and several n values; raster-read values relabelled INFERENZA.
* **Confirmed:** 360 of 360 expression rows; VER-246608 Table 1 and its two internal inconsistencies; the HGNC alias (PDK1 is an alias of PDPK1) and the UniProt accessions; the ChEMBL fan-out reading of the activity-only pointers; the devimistat statement.
* **Preregistered priors (A1):** P1, P2 and P4 failed; P3 and P5 held (`output/priors_scored.tsv`, verifier re-scored).
* **Route flag, for the integrator:** one producer source (22336956, a review) was read through NCBI efetch after its PMC page showed a reCAPTCHA. It is a documented API, but it is a second route to the same item; the row it supports (celecoxib as PDPK1) is also supported by the other symbol rows. The verifier did not repeat it.
* **Producer budget:** A3 touched 10 sources against a budget of 9 (one abstract-level over).

## Hypotheses, tools, experiment and outcomes

* `output/hypotheses.tsv`: PH1 (cell-resolved premise), PH2 (tool by isoform and scaffold), PH3 (two directions of one lever, lactate supply and the burst), PH4 (lactate-closed KATP and the K branch), PH5 (risk arm). Each carries observation (DATO), relation (INFERENZA), action (IPOTESI), favourable and opposite context, expected functional result, refuting measure, class (known-but-unused / new combination / novelty not assessed), consumer.
* `output/tools_roles.tsv`, `output/experiment_ladder.tsv` (executable now / indispensable new measurement / later validation / not resolvable by literature), `output/outcome_matrix.tsv`.
* `output/tool_by_cell_coverage.tsv` (in silico, runs now): for each cell class the share of four-kinase RNA carried by isoforms with a measured row for each tool. AZD7545 core-bound rows cover 0.65-0.84 of human neuronal and microglial RNA and 0.08-0.30 of astrocyte and oligodendrocyte RNA. An RNA share is not an activity share.
* **Shared preparation (the advantage, not the same question):** the INV-19 lysates serve INV-07 step 1; the SCI43 K-branch ladder preparation (capacitance, selection rule, junction potential, Ba2+ and K2P difference current per pF) can carry the PH3/PH4 arms (diazoxide, sulfonylurea, lactate and pyruvate add-back, pipette ATP stated) in the same cells.

## What the engine can now recompute

`engine/` holds the package in the layout of `ampa_comparison_it41_20261109/output` (`comparison.tsv`, `new_measurements.tsv`, `decisive.tsv`, `id_map.tsv`). `engine/derived_roles_check.tsv` is the result of running the engine's existing `derive` on the compound-view row V13 (dichloroacetate; AZD7545; VER-246608) with these inputs, read-only: the three names come out PRIMARY with premises M-P1 and M-P2, no hand-written exception. **Engine limits found** (proposals in `consumer_delta.md`): `comparison_engine.main` filters INV-05 only; its condition vocabulary has no assay scaffold or ATP, so AZD7545 core-bound and core-free values read COMPARABLE; the reference control is assigned only from a `pharmacological_action` column, so dichloroacetate is not marked control here.

## What cannot be resolved by more literature

Whether PDH is restrained in a WWOX-deficient neural cell; whether the glycolytic shift is cause or compensation; whether lactate is raised in the KO slice; whether any PDH or lactate-side change helps a functional outcome; brain exposure of any tool; per-cell-type kinase protein amounts (tables not reached).

## Reopen conditions

A neural WWOX PDH, lactate or pyruvate datum (premise); the AZD7545 2003 primary paper or a core-bound PDK2/PDK4 measurement; per-cell-type PDK protein tables (Sharma 2015 supplement) when reachable; Sada 2015 full text; the Wwox pipette ATP and bath glucose; a pyramidal-neuron KATP datum separating cell types in Karagiannis 2021.

## Files

`A1_before_search.md` (frame and priors, written before the searches); `BRIEF_A2..A4.md`, `VERIFIER_BRIEF_V1/V2.md`; `output/` (producers' verified tables with annotated corrections, `a3/`, `a4/`, `derived/`, `scripts/`, `receipts/`); `a4/` (relations, the unchanged search path output, catalogue by-target lookup, name-led identity table); `engine/`; `verify/v1`, `verify/v2`; staged receipts in `research/receipt_staging/sci44` (33 producer) and `sci44v` (60 verifier), all valid under `staged_receipt_check.py --check-doi`, none recorded; `consumer_delta.md`; `COST_NOTE.md`.

Update 2026-11-11 (package C, `potassium_shares_sci44_20261110/`): the KATP share of resting conductance in juvenile barrel cortex is about 11-17 percent (INFERENZA, upper bound, ATP-free whole-cell, glutamatergic regular-spiking cells; species and per-cell temperature unstated; 26 of 63 RS cells pyramidal by morphology). PH4 therefore **could carry a part of the 28 percent conductance loss, at most about half, not all**; a larger deficit would need Ba2+-sensitive Kir/K2P channels in addition. Two other juvenile preparations report no tolbutamide or diazoxide effect on rest. The statement in the README above that "the verifier reopened the link" stands; the size expectation is added here.
