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
| S4 connexin/pannexin | 0 | no ChEMBL target record in the cached index | 0 | 0 (a coverage gap, not absence) |

The known control (azetukalner) is reached: **coverage, not prediction**. A different case, S9, reaches the acid form of the reference compound that the mechanism path holds only as its sodium salt (an identity to reconcile, not a molecule), and S7 reaches the substrate GABA itself, vanillin and a flavone, which shows why an activity is not an action. The S10 flood (compounds active in cell reporter assays) is the reason for the flood guard.
Limits: ChEMBL activity text is not curated mechanism; organisms and assay compositions vary; no primary source was read for any pointer (that is the next step, in a separate context); the path needs the network once (public endpoint, no contact data) and then runs from the cache.

## P4: a role for every entity, not "ion = remove" (`role_rules_it44.tsv`, `role_overrides_it44.tsv`, `entity_roles.py`, `effect_roles.py`, `test_entity_roles.py`)

IT43's independent reader found inorganic ions returned as drug candidates. The fix keeps them visible with the right role: the roles are `candidate`, `probe`, `control_or_reagent`, `physiological_intervention`, `unqualified_entity`, assigned by rules from data (GtoPdb ligand type by id, catalogue status by ChEMBL id) in a rule table; a reviewer's change is a row with a reason in the override table, which wins and keeps the rule's role next to it. A role is not a verdict: an EXCLUDED row stays excluded for its relation.
**Effect** (`effect_roles_it44.tsv`): S2 shows 13 engine candidates of which 11 are drug candidates (a monovalent cation is a reagent, a divalent ion a physiological variable); S4 shows 5 of which 3 are drug candidates (a divalent ion and a lipophilic alcohol used as a chemical tool are not); S3 and S5 each hold one endogenous lipid or neurosteroid shown as physiological, not as a drug (the neurosteroid is a physiological GABA-A lever and keeps its engine verdict). **Opportunities not lost:** magnesium and zinc, excluded for the GluN2B and GABA-A questions, are kept as physiological variables, which is what the INV-05 conditions list already treats them as (bath magnesium in M01/M06, tonic zinc in D03); the glycine-site agents and amino acids excluded for S1 are likewise visible as manipulations of the preparation, not candidates.
**Limits:** the registry's "Metabolite" type is a classification, not a function (octanol is a chemical tool: an override, labelled INFERENZA from the use, not read per paper); overrides are mine and unreviewed; 335 rows still default to `candidate` because nothing contradicts it, which is not a qualification; no consumer outside this folder reads the roles yet (the shortlist counts and the dashboard text are the next consumers).
