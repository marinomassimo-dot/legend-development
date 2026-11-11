# Brief — producer Q1 (SCI45 queue): primary sources of the K2P tool pointers IT45 may use, and the TREK-1 pH slope

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; reference genotype class only; no individual-level record). Task record `ledger/tasks/orchestrator/ORCH-SCI45-20261111.json` (queue branch). Working tree `/home/desktop/legend-development/.claude/worktrees/sci45q` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/k2p_pointers_sci45_20261111/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-x`; staged receipt event ids end in `-86` (never reuse an id in any `receipts/INDEX.tsv` of an earlier SCI folder). You are the only active delegate. Do not start agents.

## Read first
1. `membrane_hypotheses_20261108/BRIEF_COMMON.md` (plain curl, default user agent only, figures through the public PMC open-data bucket, depth honesty, receipts, TSV rules). A bot check, 403, 429 or captcha is recorded as unreachable and **not retried by another route, including a different API or render for the same article**. Replace its task record, tree and label by those above; ignore its two-phase protocol and deliverable list.
2. `ph_k2p_sci45_20261111/README.md`, `output/tools_roles.tsv`, `output/tools.tsv` (what the earlier producer and verifier established; do not redo those tools), `search/search_rows.tsv` (the pointers: ONO-TR-772 KCNK2 PMID 40365404; Cpd8l KCNK2 PMID 40040241; ONO-2920632 KCNK2 activator PMID 39981749; KU124 KCNK3 PMID 40635742; AVE1231 KCNK3 PMID 31001961).

## Questions (answer only these; stop when answered or shown unreachable)
* **Q1. ONO-TR-772 (40365404), first priority.** Identity (name, structure as drawn in the source, identifier), target and composition, assay (system, species, pH, temperature, activation protocol: basal, arachidonic acid, thermal, or acid), value with unit and relation, the selectivity panel actually measured (TREK-2, TRAAK, TASK-1, TASK-3, Kv, Kir, hERG, Nav, Cav) and what was not tested, whether the tool's potency was measured at more than one pH, evidence of an effect in neurons (preparation, age, what changed), alternative actions.
* **Q2. The other pointers**, one source each, same fields: Cpd8l (40040241), KU124 (40635742), AVE1231 (31001961); ONO-2920632 (39981749) as a TREK activator (is it an activator of basal current, and at what pH?).
* **Q3. The TREK-1 pH slope.** A primary full-text source that fits the extracellular-pH dependence of TREK-1 current with a stated Hill slope and pH50, with temperature and solutions; the earlier producer found slope about 0.7 in one poor fit and no slope in others. Find at most two sources (start from the founding TREK-1 pH papers, Cohen 2008 and Maingret 1999, and anything reporting TREK-1 pHo response at 30-37 C); report the table or figure values with locators. Say whether the slope is stated or read off a figure.

## Rules
Measured / declared / copied per statement. Species, temperature, solutions for every number. Figures viewed with the Read tool for every number that enters a row; an abstract is not full text; values read off a raster are INFERENZA. Absence claims state their perimeter and use two routes (name-led and target-led). No compound recommendation, no ranking, no claim on WWOX, no dose.

## Source budget
At most **8 sources newly read** (the five primary papers above are the aim; two for Q3; unreachable sources are recorded with route and depth).

## Deliverables (in `output/`)
1. `pointers.tsv`: one row per compound: `tool_id, name, synonyms, identifier, structure_checked_against_source (yes|no), target_composition, assay, value, unit, relation, selectivity_panel_measured, not_tested, tested_at_more_than_one_pH, neuronal_evidence, alternative_actions, role_proposed (probe|comparator|control|conditional|excluded), source, locator, depth`.
2. `trek1_ph_slope.tsv`: `row_id, system, species, temperature, solutions, pH_range, pH50, hill, stated_or_figure_read, source, locator, depth`.
3. `decisive.tsv` (8 to 12 rows): `prop_id, statement, question_id, source_pmid_or_doi, locator, producer_status, depth, kind, class`.
4. `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role, prop_ids, locator_quote (<=25 words verbatim), species_system, note`), `queries.tsv`, `figure_notes.tsv`, `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci45q --check-doi <file>`, not recorded), `phase_note.md` (<=12 lines), `answers.md` (<=1 page).
5. Do **not** write README, hypotheses, consumer_delta or COST_NOTE.

## Hard additions
No gates, lint, tests, batteries, commits. No e-mail, registration or service that needs a contact address; never send any address to any service. Keep downloaded publisher text in scratch, outside the repository. Not medical advice. Nothing is promoted.

## Final message
Sources newly read with depth; figures opened; unreachable items and routes; counts per deliverable; the one-line answer per Q with its deciding row; anything that surprised you.
