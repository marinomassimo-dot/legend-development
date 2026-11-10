# IT43 P4: evaluation protocol, fixed before the figures are computed

Non-canonical working note. Written 2026-11-10 before `eval_it43.py` is run; later changes are dated addenda. Three values kept apart: source, qualification, generation. No predictive validation exists and none is claimed.

## Universe and questions
Questions not used to correct the method in IT42: **S9** (PDK inhibition, framed before search in `third_relation_it43.md`) and **S2/S3/S4** (HCN, Kv7, connexin: searched in IT41, never scored in IT42). Same universe per condition: the catalogue and caches pinned by `cache_manifest.json`.

## Conditions
* A0: ChEMBL curated mechanism rows by symbol. A1: A0 plus GtoPdb interactions. A2: A1 plus the DGIdb listing path. B: A1 qualified by the relation (verdicts CANDIDATE / EXCLUDED / UNKNOWN). B+L: B plus the listing rows kept as UNKNOWN listings.
* Generation (S9 only): the comparison engine (`compound_decisions_it43.tsv` logic) on the S9 molecules, with roles and the premise needed.

## Outcomes fixed first
1. **Source value**: molecules (distinct, labelled forms and empty names dropped, salts and stereo prefixes merged) in A0, A1, A2; of the A2-only molecules, how many have a typed action.
2. **Qualification value**: units with an unflagged error in A1 versus B (error types E1 direction, E2 site class, E3 subunit transfer, E4 duplicate, E5 identity); clean units kept; clean units lost without a record (must be 0).
3. **Generation value**: for S9, compounds that reach a role (reference, chemotype control, isoform probe) versus abstention; premises named; the experiment ordered by the premise. Conserved-as-conditional and abstained counts are reported next to any error reduction: removing everything is not an improvement.
4. **Missed opportunities and false exclusions**: rows excluded by the older generator that the path types (IT21 `unsigned_or_no_signed_direct_action` for the S9 molecules), and excluded rows whose reason fails on re-read.

## Independence
The scorer does not reuse the engine's verdict functions for the decisive premises. An independent reader (sonnet, high effort, one delegate, no escalation, read back afterwards) receives the original rows and re-derives, for S9, the direction, site and subunit statements of every row, and a declared random sample of 30 other rows from S2-S4; it does not see the engine verdicts. Disagreements are reported as findings, not absorbed.

## No graph step
No graph propagation is used in IT43; no graph baseline or specificity control is therefore added.

## Report
A table per condition, the independent reader's disagreements, the unchanged limits (reference positives exist for Q1 only; the scorer shares facts with the engine for the non-decisive rows).
