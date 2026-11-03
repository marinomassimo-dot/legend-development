# IT22 P6 reverse analysis: six cases, reasons first, then what the generator did (2026-11-03)

Non-canonical research material. Independent reverse-analysis actor. Public edition, WWOX-DEE reference genotype class; not medical advice. Zero spend, no registration, no e-mail or contact string sent to any service. No existing file edited, no code edited, no receipt recorded, no git state change. Written only here.

Order followed: (1) `reasons_blind.tsv` (63 reasons) and `priors_blind.md` were written from repository sources and primary literature BEFORE the forward snapshot, `results_p1/p2/p3`, `results_p2b` or any proposals/hand-over table was opened (I did read `inputs_it22/`, `decision_scope_it22.tsv` and `p3_*` dossiers, which are inputs and sources, not outputs); (2) `reverse_table.tsv` compares each reason with the stage tables (`diagnosis_it21_v1/results_v1`, `results_p2b`, `results_p3`); (3) `generalisation.tsv` tests each proposed fix on a second case. The nine-category vocabulary the brief mentions is not in `diagnosis_it21_v1_20261103/README.md` (it has none), so I used the seven classes named in the brief: consumed, represented-not-executed, executed-not-consumed, not represented (omission), justified exclusion, missing datum, representation limit.

Literature (according to PubMed, abstracts only): tapinarof AhR agonism and AhR dependence, PMID 28595996 ([DOI](https://doi.org/10.1016/j.jid.2017.05.004)); tapinarof dual AhR/NRF2 activation in keratinocytes, PMID 40945864 ([DOI](https://doi.org/10.1016/j.taap.2025.117559)); AHR-NRF2 axis in keratinocytes, PMID 38929171 ([DOI](https://doi.org/10.3390/antiox13060732)); cream formulation, PMID 30612986 ([DOI](https://doi.org/10.1016/j.jaad.2018.10.037)). No full text was read and no read receipt claimed.

## 1. Verdict per case

| Case | Blind prior | What the stage tables show | Verdict |
|---|---|---|---|
| 1 vorinostat | HOLD, never qualify; metabolic route stopped on attribution, stability arm deferred | Unchanged from V1 to IT22 P3 (checked in three tables): `main_target_weak_attribution`, fold 2769.2, HDAC5 Ki 3600 vs HDAC1 1.3 nM. The stability arm (card A01) is represented only in a side view; the A01 class-I caution is on no limit field | Correct, nothing to reopen. Residual: the surviving reason is not attached to the row (G2) |
| 2 tapinarof | HOLD at most; abstain equally defensible | IT21P2-1008 is **handed over** (Q8, H_HARM, chain AHR -T(+)-> NFE2L2): the topical-only fact (ATC D05AX07, IT9 F2) and the failed second-system gate are not in the limits, "dev limits: unspecified", the direct route (omaveloxolone) is absent, the only listed alternative is Tcdd | Status right (conditional, unqualified); hand-over too generous. Three omissions: T5, T8, T3 |
| 3 omaveloxolone | Known thread, HOLD; no new compound-level decision | Q5 rows carried as KEEP (0175) and identity (0176); Q8 direct_search rank 1 and 2, signed +1, DIAGNOSTIC_ONLY, not in proposals or hand-over | Exclusion from SCORING justified (post-translational activator, transcript seed, no null for hop-0). Omission in the READING: executed, signed, not consumed (G1). Not a failure to reach the compound |
| 4 EZH2 inhibitors | HOLD as a cell-type-resolved in vitro question; hazard flag for dual EZH1/2 | 0198-0200 eligible, GSK2816126 handed over on Q8 with an empty limit list; differentiation hazard, efflux and dual EZH1/2 not represented; Q5 sibling limit carries the stale IT21 wording that the P6 dossier corrects | Status right; limit text incomplete (G2, G5, G6). The P6 dossier is not a decision source |
| 5 BTK inhibitors | Q4 NPY arm abstains, exclusion scoped to the compartment | 57 BTK-main-target rows, all Q4 and NPY-first; 24 blocked `shared_premise_refuted`, 30 identity, 1 decided, 1 modality, 1 reach; none eligible. BTK in another chain: 0 rows. No BTK row in the Q5 tables. S116 caveat on 75 NPY-first rows, 1 handed (AT-13148) | **Exclusion correctly scoped now; no leak found.** The caveat is a second, independent reason (sign contested) and is consumed as a limit, never a veto |
| 6 pracinostat, quisinostat, CUDC-101 | HOLD as conditional; release justified on own pharmacology, not as evidence | Typed IC50 (my re-run of `class_alternatives_it22.py`): pracinostat HDAC5 47 vs HDAC1 49 nM (fold 1.2 to best, HDAC10 40); CUDC-101 11.4 vs EGFR 2.4 (4.7); quisinostat 3.69 vs 0.11 (33.5, borderline potent); nanatinostat 200 vs 3 (66.7, now SECONDARY_ACTIVITY_MEASURED, held only by its own record) | **Release justified** on attribution. It adds no evidence for the route (one muscle edge, role unknown) and "attributable" is not "specific": 4 co-potent HDAC targets for pracinostat, 8 within 10x for CUDC-101 (G5) |

## 2. What the stage tables confirm, with numbers (checked against `results_p3`, `results_p2b`, `results_v1`)

* Eligible 217, handed over 16 (IT22 P3; IT21 V1: 154 and 11). Hand-over contains pracinostat (0005), GSK2816126 on Q8 (0993) and tapinarof (1008).
* Vorinostat 0031: identical blocker and fold in all three stages.
* EZH2 siblings 0198-0200 were blocked `mechanism_cluster_examined_earlier` in V1 and are eligible from IT22 P1 on (H8 scoping), as intended; the Q5 sibling limit text is the IT21 wording.
* IT22 P2 changed a tier: a measured main target of 100-1000 nM is `SECONDARY_ACTIVITY_MEASURED`, not WEAK; WEAK needs more than 1000 nM. Nanatinostat (HDAC5 200 nM) therefore left the screen's veto and is held only by its P4a record; vorinostat (3,600 nM) stays WEAK. The 1000 nM threshold is a stated convention.
* Cosmetic: `attribution_fold` is printed to one decimal, so 14 rows show 0.0 (GSK343 is 4/240).

## 3. Reasons that existed before IT22 and were still lost

T5 (topical-only) and the IT10 omaveloxolone development verdict existed since IT9/IT10. The OPC-differentiation hazard (E7), the corrected sign reading (E6), the CSF datum (V3) and the stability-lever reading of HDAC6 (V10) are IT22 P6 material and are in no generator input, which is the intended boundary of a seed-graph generator; the question is only whether class-level limits can travel (G2).

## 4. Generalisation (see `generalisation.tsv`)

Held (tested on a second case): G1 direct-hit cross-link (Q8 and Q2/Q5, with a filter); G2 class_limit scope (EZH2 and the HDAC5 cluster); G3 deposit-level second-system annotation (both Q8 rows); G4 catalogue route/phase into dev limits (tapinarof route, three HDAC twins phase); G5 co-potent target count (pracinostat, CUDC-101, ibrutinib: 55 of 106 assessed rows have two or more other targets within 10x).

Partly: G6 InChIKey join for GtoPdb ligands without a ChEMBL id helps tazemetostat only; valemetostat and tulmimetostat have no catalogue family, so they need a catalogue change.

Did NOT generalise: G7 seed-conditioned `target:` premise key (BTK only; the key occurs once), G8 stale carried wording (a data correction for EZH2, no second case). What also does not generalise: the BTK exclusion itself (a compartment finding about one seed) and the EZH2 differentiation hazard (a target-class fact).

## 5. What I could not verify

Full texts of all cited papers (abstract-level only for tapinarof; the P6 EZH2 reads are partial by their own statement). Whether the omaveloxolone Q8 direct hit was meant to be shown elsewhere (no README of IT22 P3 states the intent; `generation_it22_p1_20261103/` has no README). Brain exposure for every compound. Whether the catalogue carries a route flag beyond ATC and openFDA products (the profile `topical` flag is IT9-only). The 758 InChIKey matches overlap with the existing reconciliation. The mouse Btk/Npy co-expression check (GSE158684) was never run by anyone, so the BTK refutation is organoid-and-HPA-level. HDAC-inhibitor and AhR neurodevelopmental toxicity statements are background, unsourced (rows V14, T9). Whether the cluster cap (one hand-over per mechanism cluster) is what kept quisinostat, CUDC-101 and the Q8 EZH2 siblings out of the hand-over was read from the rule text (H5), not re-run.

## 6. Files

`reasons_blind.tsv`, `priors_blind.md`, `reverse_table.tsv`, `generalisation.tsv`, this README. Scratch re-runs used `LEGEND_CATALOG_CACHE=/home/desktop/legend-development/disease-models/wwox/research/drug_repurposing/catalog/cache`.
