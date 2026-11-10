# IT44: from qualified knowledge to hypotheses actually generated and used

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No predictive validation exists. Task record `ORCH-ROADMAP-IT44-20261110`.

## P2: a by-target activity path for what the mechanism tables do not hold (`activity_search.py`, `test_activity_search.py`)

**Problem.** The mechanism path reads curated mechanism rows and registry interactions. A compound with only measured activities on the target is invisible to it: SCI43 found azetukalner (a clinical-stage Kv7 opener with a human EC50 on KCNQ2) reached by name only.
**Path (no name exception).** For the gene symbols of any relation row it resolves the human target records in the cached ChEMBL target file, reads the public activity endpoint page by page, caches every raw page (gitignored cache, SHA-256 and completeness per target) and writes one row per activity and one per molecule, joined to the tracked catalogue **by ChEMBL id**. Kept apart: molecule identity, target record and organism, quantity as reported (type, relation, value, unit, assay type), direction (never taken from the activity type), transfer to WWOX (always open). Every molecule is `ACTIVITY_ONLY` with its unknown fields named; a truncated read is `TRUNCATED`, never absence; a relation whose targets are measured against more than 1,000 molecules is `FLOOD` (a screening or reporter-assay target) and lists nothing as a pointer.
**Result** (`summary_it44.tsv`, `pointers_it44.tsv`; the full activity tables are regenerable from the cache, not committed):

| Relation | Molecules with a measured activity | With a catalogue status (pointers) | Not reached by the mechanism path | Research compounds, no status |
|---|---|---|---|---|
| S3 Kv7 | 359 | 7 | 4 (quinidine, flupirtine, azetukalner, one tool probe) | 352 |
| S2 HCN | 55 | 4 | 3 | 51 |
| S7 GAT-1 / GABA-transaminase | 221 | 11 | 9 | 210 |
| S9 PDK | 433 | 3 | 2 (the acid form of the reference compound; one steroid) | 430 |
| S10 KEAP1/NFE2L2 | 5,566 | read state FLOOD, none listed | 0 | 5,412 |
| S4 connexin/pannexin | 0 | symbols GJD2 and PANX1 have no target in the cached index: **unread**, not empty | 0 | 0 |
| S11 Kir2/K2P (below) | 1,039 | 375 are screening-deposit rows (not listed); 30 listed pointers, mostly IC50 (blockers) with two EC50 (the approved glutamate-release modulator and a fenamate); KCNK4, KCNK1, KCNK13, KCNJ4, KCNJ12 unread | 30 | 634 |

The known control (azetukalner) is reached: **coverage, not prediction**. A different case, S9, reaches the acid form of the reference compound that the mechanism path holds only as its sodium salt (an identity to reconcile, not a molecule), and S7 reaches the substrate GABA itself, vanillin and a flavone, which shows why an activity is not an action. The S10 flood (compounds active in cell reporter assays) is the reason for the flood guard.
Limits: ChEMBL activity text is not curated mechanism; organisms and assay compositions vary; no primary source was read for any pointer (that is the next step, in a separate context); the path needs the network once (public endpoint, no contact data) and then runs from the cache.

## P4: a role for every entity, not "ion = remove" (`role_rules_it44.tsv`, `role_overrides_it44.tsv`, `entity_roles.py`, `effect_roles.py`, `test_entity_roles.py`)

IT43's independent reader found inorganic ions returned as drug candidates. The fix keeps them visible with the right role: the roles are `candidate`, `probe`, `control_or_reagent`, `physiological_intervention`, `unqualified_entity`, assigned by rules from data (GtoPdb ligand type by id, catalogue status by ChEMBL id) in a rule table; a reviewer's change is a row with a reason in the override table, which wins and keeps the rule's role next to it. A role is not a verdict: an EXCLUDED row stays excluded for its relation.
**Effect** (`effect_roles_it44.tsv`): S2 shows 13 engine candidates of which 11 are drug candidates (a monovalent cation is a reagent, a divalent ion a physiological variable); S4 shows 5 of which 3 are drug candidates (a divalent ion and a lipophilic alcohol used as a chemical tool are not); S3 and S5 each hold one endogenous lipid or neurosteroid shown as physiological, not as a drug (the neurosteroid is a physiological GABA-A lever and keeps its engine verdict). **Opportunities not lost:** magnesium and zinc, excluded for the GluN2B and GABA-A questions, are kept as physiological variables, which is what the INV-05 conditions list already treats them as (bath magnesium in M01/M06, tonic zinc in D03); the glycine-site agents and amino acids excluded for S1 are likewise visible as manipulations of the preparation, not candidates.
**Limits:** the registry's "Metabolite" type is a classification, not a function (octanol is a chemical tool: an override, labelled INFERENZA from the use, not read per paper); overrides are mine and unreviewed; 335 rows still default to `candidate` because nothing contradicts it, which is not a qualification; no consumer outside this folder reads the roles yet (the shortlist counts and the dashboard text are the next consumers).

**Defect found by Harness (HE44) and what was done.** `target_index()` reads the cached target file, which holds only targets linked to a curated mechanism, and a symbol with no target there was skipped without a state: HCN1-3, GJD2, PANX1, KCNK4 and others yielded "no compounds" when they were never read. Now every symbol is recorded in the manifest as `TARGETS_FOUND` or `UNRESOLVED_IN_CACHED_INDEX` and the summary lists `unread_symbols`; S2 is read from HCN4 only and S4 reads nothing, stated as such. Harness's `target_activity.py` resolves exact targets by UniProt accession with a state per symbol (117 more human targets) and an adapter with retry and cache validation: IT44 adopts it for target resolution and fetching when it is on `main` (this file keeps the relation-level qualification: read state, screening-deposit guard, catalogue join by id, `ACTIVITY_ONLY`). Pre-registered control and second case of HE44 (azetukalner EC50 on KCNQ2; tiagabine on SLC6A1, complete) agree in kind with the Kv7 control here.

## P3 and P8: two generative cases (details in the files named)
| Case | Files | What it produced |
|---|---|---|
| S11 adding a resting K+ conductance | `relation_s11_frame_it44.md` (before), `relations_s11_it44.tsv`, `s11/`, `relation_s11_result_it44.md`, `verify_s11/VERDICTS.md`, `apply_it44_s11.py` | openers exist only for the weakly Ba2+-sensitive K2P subfamily; the Ba2+ concentration at which a lost current is blocked decides whether any opener is relevant; the first experiment gains a two-concentration Ba2+ step; V14 on the cards; open questions IT44-Q01/Q02 |
| S12 astrocytic K+ buffering | `relation_s12_frame_it44.md` (before), `relations_s12_it44.tsv`, `s12/`, `relation_s12_result_it44.md` | no enhancer in the held tables; the engine's excluded blockers become discriminators; the activity path stopped at target resolution (KCNJ10/KCNJ16 unread): reopen when the HE44 resolver is on main |

## P1: consumption of the HE43 components (what changed, before/after)
| Component | Consumer | Before | After |
|---|---|---|---|
| `measurement.measure` | `activity_search.py` (activity rows and molecule table) | a value and unit printed as served; no converted scale; no flags | every row carries `converted_nM` (labelled conversion) and `measurement_flags`; over the three runs (11,084 rows): 5,413 clean, 5,000 of kind Potency (a screening potency, not an affinity: flagged `KIND_UNRECOGNISED`), 374 censored bounds, 276 with no value, 17 with an unrecognised unit, 4 approximate; the molecule table gains `n_measurement_flags` and `best_nM` (censored values never count) |
| `compound_identity.parent_form` | `dgidb_listing.py` key | salts merged, a single stereo letter stripped by a pattern (two enantiomers merged) | key = parent name plus its stereo/isotope prefix: the new-molecule count over S1-S8 moves 106 to 104 and an enantiomer pair stays two molecules |
| READ_INCOMPLETE / ID_NOT_RESOLVED | identity join | EMPTY_RESULT | already carried as non-evidence states by the view; nothing else to change here |
| `action_search.py` quantity columns | not yet | the affinity is one string | Harness's HE44 edits that file (quantity columns); IT44 takes them when HE44 lands rather than editing the same lines |
Not yet consumed: the seven registry rows whose nM column is exactly 1000 off (Cs+ on HCN1/2/4 among them) enter the S2 search table only through HE44's change; no S2 verdict depends on them.
