# Forward snapshot, IT21 V1 (vorinostat as a retrospective diagnostic case)

Non-canonical research material. Actor `orchestrator-delegate`, package V1, task branch `task/it21-v1`, written from `task/it21-orch` at the commit recorded in the git history of this file.
**This file is the forward path only. It contains no reverse argument for or against the compound, and it is committed before any such argument is opened** (compare `git log` for this directory: this commit is the first). It reuses existing artefacts; nothing was re-run. Not medical advice; public edition, the subject is the WWOX-DEE reference genotype class.

Machine-readable parts, built by `forward_snapshot_it21_v1.py` from existing files: `forward_snapshot_inputs.tsv` (artefact, git blob, last commit), `forward_snapshot_vorinostat_trace.tsv` (stage-by-stage record of the compound), `forward_snapshot_contrast_cases.tsv` (forward rows of the contrast cases).

## 1. The biological question the forward path asked

Generate, from observed WWOX-deficient changes (not from a list of drugs), conditional hypotheses of the form compound, action, biological context, hypothesised benefit, discriminating experiment. Seven questions (Q1 to Q7: protein level, glycolysis and HIF, ISR, neuronal-subtype shift and cytokine and MYC axes). Seeds: `generation_it9_p1_20261030/seeds.tsv` (131 rows, 65 usable, 29 gene symbols; unchanged since 2026-10-30). The role of the observed change (harmful or protective) is stated by none of the usable rows, so each question keeps two conditional arms (`H_HARM`, `H_PROTECT`). Nothing leaves the `CONDITIONAL_*` vocabulary by pipeline.

## 2. Usable compound universe at the time of the forward run

Catalogue 44,211 entries (`catalog_stats.json`); 13,307 compound families, 32,954 signed (family, gene) pairs under the IT9 table, of which 13,034 lose their sign under the IT19/IT20 guards (group-transfer, republished claim, documented-level waiver, conflict or glue receptor); 980 seed-specific rows remain under four nulls (three IT10 nulls and the reach-matched null). Identity: 693 of the 980 rows are catalogue families with no ChEMBL id (DGIdb-only). Source for all counts: `generation_it21_p2_20261103/results/summary_it21.json`, `README.md` sections 1 to 3.

## 3. Paths that were run, in order, and what each did with the compound

| Order | Path (artefact) | Compound state after the path |
|---|---|---|
| 1 | IT7 P2 pilot subset, LINCS neural contexts (`usable_compounds_it7_p2_20261029`) | ChEMBL family present in the pilot (6 neural contexts); IT7 P3 network comparison scores it (O_E -1.26) |
| 2 | IT9 P2 seed-graph generator, v3 (`generation_it9_p2_20261030/v3`) | DGIdb twin generated, Q2 opposes rank 34, seed-specific in three nulls; Q6 direct-search hit on MYC, diagnostic only |
| 3 | IT9 P3 exploration (`exploration_it9_p3_20261030`) | both families merged under parent CHEMBL98; direction CONFLICT; `not_taken:promiscuous(>=5 targets)`; written to `excluded.tsv` |
| 4 | IT9 P4c-e selection (`qualification_it9_p4c_e_20261030/selection_note_E.md`) | cluster HDAC5 to SLC2A1 (35 members) not taken, for diversity |
| 5 | IT10 v4 + dispositions (`generation_it10_p1_20261031`) | Q2 `CONDITIONAL_IF_HARMFUL`, DOMINANT_CHAIN; not in `deepening_candidates.tsv` |
| 6 | IT21 P2 refreshed generator (`generation_it21_p2_20261103`) | `IT21P2-0031 CONDITIONAL_H_HARM`, qualified=no; not handed over, blocker `identity_not_resolved` |
| 7 | IT21 P3b path B levers; IT21 P5 decoy evaluation | listed as an HDAC6 lever (NAMED_ALREADY); P5 real row eligible=0 for the same blocker |
| 8 | Queue, ranking, investigations, dashboard (`ranking_it8_p9_20261029`, `view`) | no row; the compound is in the view only as a catalogue listing |

Stage levels (present, generated, qualified, visible) per artefact: `forward_snapshot_vorinostat_trace.tsv`. In short: present in the catalogue (two records); generated in IT9, IT10 and IT21 P2 (metabolic side, one chain); never qualified (no qualification record names it); not visible as a candidate.

## 4. Filters, selections and destinations as they stood

* Engine: signed network, one regulatory level, no tissue context; compound side = the family's signed targets; scores are z against degree-, in-degree-, admissibility-matched and reach-matched nulls; the chain is read from the family's listed target to the seed.
* IT9 P3: promiscuity rule (at least 5 signed targets) and mechanism-group rules; IT9 P4c-e: diversification across mechanism classes.
* IT21 P2 `eligible()` (`run_generation_it21.py`, rules H1 to H8): the order of checks is arm, seed-specific, reach z, then `has_chembl` (identity), modality, stated benefit hypothesis, earlier decision; a mechanism cluster with an earlier decision is not re-handed over (H8). Cap of 3 per question and hypothesis.
* Destinations: handed over 13 (to IT21 P4a, 6 qualified: 1 kept conditional, 2 inconclusive, 3 rejected as informative), the remainder stays as conditional rows in `proposals_it21.tsv`.
* Not part of the forward path: any LEGEND knowledge outside the generator that concerns the compound (cards, the literature census, the CTD direction audit, the local GtoPdb affinity table, the IT5 P8 potency tables). Whether such knowledge reached the generator is what the reverse analysis examines; this file records only that the forward path has no input from them.

## 5. Contrast cases registered before the compound is introduced as a target

Chosen from existing P2, P3b, P4a and P8 outputs, by role, not by outcome. Forward rows in `forward_snapshot_contrast_cases.tsv`.

| Case | Role | Forward result as it stands |
|---|---|---|
| C1 GSK343 (IT21P2-0195) | plausible proposal | handed over; P4a `KEPT_CONDITIONAL`, narrowed to mouse glia |
| C2 tizaterkib (IT21P2-0374) | conditional (H_PROTECT role probe) | handed over; P4a `INCONCLUSIVE`; status `CONDITIONAL_H_PROTECT` |
| C3a nanatinostat (IT21P2-0006) | contrary signal in an HDAC-class compound | handed over; P4a `REJECTED_INFORMATIVE` (HDAC5 weakest target), `NEG-03` |
| C3b pomalidomide (CRBN) | abstention required (glue-type action) | direction withdrawn at the main target (`action_conflict_or_glue_modulator`); no proposal row |

Prediction recorded now, before any change: a general fix must leave C1 and C2 conditional and unqualified, must not move C3b into the proposals, and may only move C3a in the direction the P4a record already took.

## 6. Open at the time of freezing

Unravel's selection of vorinostat is an external reference; no repository artefact holds it. It is not a positive WWOX label and is not used as one. WWOX-specific unknowns (HIF and ISR protein in a WWOX-deficient neural cell; the role of the observed changes; any HDAC data in a WWOX system) stay unknown.
