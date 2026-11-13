# HE50: design-only knowledge and pharmacological roles that keep their context

Non-canonical working note. Not medical advice. Task record `ledger/tasks/plan/PLAN-HE50-DESIGN-ONLY-PHARMACOLOGY-20261113.json`. Technical capability only: nothing here shows that a hypothesis, comparison or experiment became better; whether the new rows change a later choice is for the Orchestrator and the scientific owners.

## Which previously unusable knowledge can now contribute
* **The ISR design (INV-02): six steps with their preconditions, controls, outcome branches and the decision each informs.** Before, the generator held nothing of it (`hypothesis_package.py show --inv INV-02`: `NO_DESIGN_LISTED`; no row in any generator output); the case note of IT49 recorded this as IT49-Q03. Now `conditional_proposals.py` writes six rows (`conditional_design_steps_it50.tsv`) from `isrib_discrim_20261108/output/design.tsv`, each cell verbatim under its own column name.
* **A second structure: the myelin levers, seven experiments (INV-12).** `levers_bc/output/experiments.tsv` (the science session's folder, read only; registration agreed) keeps its controls in separate columns (`comparator`, `mechanism_control`, `engagement_check`), its contrary outcome in `weakened_by`, `endpoint_scope` and `not_a_substitute_for` as cells of their own, and `hyp_id`, which is what tells EX5 to EX7 (hypothesis H2) from EX1 to EX4 (H1, the investigation INV-12): one investigation per registration, so the link cell travels and no H2 row raises INV-12.
* **Reagent roles for the NRF2 pair and its neighbours.** The comparison engine now reads the packages' own role tables: RA839 and sulforaphane are **comparators** (they were derived as probes from the evidence tier alone), KI-696 stays a probe **with the conditions and the systems each role was stated for** in `package_roles`.
* **Two identities:** ML133 (ChEMBL record without a name, InChIKey equal to the PubChem record that lists ML133) and RA839 (ChEMBL id, with the by-hand comparison of its printed systematic name stated as the weaker basis).
* **Twelve ISR genes in the held cell-class RNA tables** (`../isr_cellclass_he50_20261113/`): none neuron-enriched, PPP1R15A strongly enriched elsewhere; the case's own count of eleven was one short of its twelve.

## Reproduced problems, minimal changes
| Problem | Reproduced as | Change | Size |
|---|---|---|---|
| Design-only knowledge is not consumed (IT49-Q03) | INV-02 `NO_DESIGN_LISTED`; the ISR package unlisted (`6 design steps unreachable` in `hypothesis_package.py check`) | a fourth role `design_only` in the existing reader (verbatim rows by table and key, nothing mapped), one `DESIGN_MAP` and one function in the existing consumer, two manifest rows | about 90 lines of code, 9+6 tests |
| A reagent shown as a probe where the package says comparator | `compound_decisions_inv08_it44.tsv`: RA839 probe, sulforaphane probe, KI-696 probe; the package's `output/matrix.tsv` states per system and endpoint: comparator, comparator, probe (microglia, molecular) and comparator (viability, lines) | `ROLE_TABLES` in the engine (two packages): a package role can lower a derived role, never raise one; every row travels with its system; rows naming several compounds are assigned to none | about 45 lines, 12 tests |
| Identity of a mention | ML133 `NOT_FOUND_BY_NAME`; RA839 `NAME_EXACT` with no reconciliation | two declarations in the existing table, each with both keys and its basis | 2 rows |
| ISR genes unknown in the join | all twelve unknown (`NOT_IN_TABLE`) | the existing extraction made parametric (`--genes`, `--prefix`), default output byte-identical | 25 lines |

## Before and after
**INV-02 design (the generator output):** before: no row; after, for step 1, among six rows (cells verbatim, abbreviated here):
```
step: 1 first fork: is the phospho-eIF2alpha route engaged and limiting | question: ... | arms: ... | readouts: ...
precondition_unmet_until_the_step_before_is_run: condition_on: step 0 passed
controls_as_documented_by_the_package: controls_already_qualified_in_module: as step 0; Torin-1 or rapamycin arm separates an mTOR-type block (EI05, E19)
possible_outcomes_conditions_and_cautions_not_observed: if_result_X_then: (a) ... ISR-P route ...; (b) phospho-eIF2alpha not raised and translation lowered: go to step 2; (c) translation not lowered: stop ...; (d) engagement control fails: uninformative, repeat step 0
conditioned_decision: decision_it_changes: prioritises the ISR need against the GSK3 chain; the existing ISR modulator card stays a class card
scope_and_what_the_result_is_not: not stated by the package (no such column)
observation: absent: a design states no observation; its outcome cells are possible results, not data
```
Step 2's controls cell keeps "second chemotype is NOT qualified in the module"; the E and EI ids are module evidence references, not observations of this design.
**Roles (`compound_decisions_inv08_it44.tsv`):** RA839 `probe` → `comparator` (reason: capped, rows M01 and M02); sulforaphane `probe` → `comparator`; KI-696 `probe` unchanged and now carrying "probe (conditional: with a verified NRF2-loss arm and a KEAP1-loss occlusion arm in the same cell)", "M20 probe: primary rat microglia, molecular", "M21 comparator: primary rat microglia, viability" and the lines and bronchial cells; dimethyl fumarate and monomethyl fumarate stay unresolved and the row naming both is marked shared and assigned to none. Bardoxolone methyl stays unresolved although its package role is a conditional comparator: a tier ceiling is not lifted by a package, and the disagreement is visible. The other two engine outputs (INV-05, INV-07) differ only by an empty new column. **Consequence found by the battery, not foreseen:** the committed views embed the engine roles, so the role change made the full view, the five shareable pages and the package stale (three tests); they were regenerated on the merged tree, and the V19 passage that said "the engine has no comparator role yet" was updated (its four translations reuse the old ones with the one changed sentence translated). The page's group label stays "probe or comparator".

## What was consumed, at which level
Accessible: the manifest lists the packages. Read: `hypothesis_package.design_for` returns their rows (`hypothesis_package.py check`: 77 rows over 15 packages). Used: `python3 disease-models/wwox/research/drug_repurposing/generation_it40_20261109/conditional_proposals.py` writes the design rows next to its two other outputs, which are byte-identical to before; `python3 disease-models/wwox/research/drug_repurposing/generation_it43_20261110/comparison_engine.py --inv INV-08` writes the roles. **Not yet used downstream:** no dashboard row, question or decision reads the design rows, and the page keeps its coarse "probe or comparator" group for roles (it never said "probe" alone).

## Limits still open
* `isrib_discrim_20261108/output/grid.tsv` (twelve outcome patterns with what each leaves compatible and when it is uninformative) is reachable and **not mapped**: its columns were not part of what the owners confirmed.
* The SCI50 myelination package could be a third structure; not waited for.
* An absent role table means the engine reads as before; only SCI46 and SCI48 declare one, and SCI49's roles file is read by no engine because INV-18 has no engine pass.
* The cell values for the ISR genes and the identity of RA839 rest on stated bases (RNA class means of one age each; a hand comparison); none of it says anything about a protein-level ISR direction or a role.
* Deltas for the owners: (1) V19's closing sentence was updated here with the regeneration (the owners should read it); (2) the symbol list staged for the INV-02 hypotheses had eleven genes (PPP1R15B missing); (3) registering the two ISR RNA tables in `cell_context.TABLES` lets the existing join answer for them.

## Turning it off
* Design rows: delete the two `design_only` rows of `hypothesis_packages.tsv`; `DESIGN_MAP`, `design_rows` and the output file can then be deleted, and `hypothesis_package.py` keeps working without the role (nothing else calls it).
* Roles: delete `ROLE_TABLES` entries (or the dict) in `comparison_engine.py`; the engine then reads as before; regenerate the three `compound_decisions` files.
* Identities: delete the two rows of `catalog/tool_identity_declarations.tsv` and their test.
* ISR extraction: delete `isr_cellclass_he50_20261113/` and the two options of `targets_expression.py` (default behaviour is unchanged by them).
