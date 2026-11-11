# Brief — producer N1: proton sensitivity of NMDA receptors and ASIC1a, and the native juvenile cortical evidence (SCI45 follow-up)

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; reference genotype class only; no individual-level record). Task record `ledger/tasks/orchestrator/ORCH-SCI45B-20261111.json`. Working tree `/home/desktop/legend-development/.claude/worktrees/sci45n` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/nmda_asic_ph_sci45_20261111/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-z`; staged receipt event ids end in `-84` (never reuse an id in any `receipts/INDEX.tsv` of an earlier SCI folder). You are the only active delegate. Do not start agents.

## Read first
1. `membrane_hypotheses_20261108/BRIEF_COMMON.md` (plain curl, default user agent only, figures through the public PMC open-data bucket, depth honesty, receipts, TSV rules). A bot check, 403, 429 or captcha is recorded as unreachable and **not retried by another route, including a different API or render for the same article**. Replace its task record, tree and label by those above; ignore its two-phase protocol and deliverable list.
2. `ph_k2p_sci45_20261111/next_brief_sci45_20261111.md` (the question), `S8_coda.md` §2, `README.md` (K2P side, verified) and `glun2b_comparators_sci42_20261110/S3_design.md` §4 (what is already held on pH and GluN2B: NP10679 at abstract level; do not redo). The priors are in `PREREGISTRATION.md` of your folder (do not edit it).

## Questions (answer only these; stop when answered or shown unreachable)
* **N1. NMDA receptors, recombinant.** Proton sensitivity of GluN1/GluN2A, GluN1/GluN2B and, if reachable, triheteromers and the GluN1 splice forms: pH of half-inhibition (IC50 or pK), Hill slope, residual current at saturating acid, fraction of current remaining at pH 7.4, 7.2 and 7.0 (read from tables/figures), holding potential, Mg2+, glycine/glutamate concentrations, temperature, system (oocyte/HEK), species. Start from the founding primary papers (find them by search; do not rely on memory), then at most one source on GluN2B-containing receptors, one on triheteromers or a temperature effect.
* **N2. NMDA receptors, native and juvenile.** Proton inhibition of NMDA current in native neurons (cortical or hippocampal, any age first, then juvenile P5-P25): preparation, age, temperature, Mg2+, pH step and effect size. Whether the effect depends on subunit (GluN2B-selective tools such as ifenprodil-site NAMs in the same experiment).
* **N3. ASIC1a.** pH threshold, half-activation, steady-state desensitisation range (pH at which channels are inactivated before the stimulus), and native evidence in cortical pyramidal neurons (age, temperature): does a fall from 7.4 to 7.2-7.1 produce current or only desensitise?
* **N4. One cell, several targets.** Any source that measures the net effect of a mild extracellular acidification (about 0.1-0.3 unit) on excitability, Rin, rest or bursting in cortical or hippocampal neurons or slices, with the receptor contributions separated. Name-led and pH-led strings; record each.

## Rules
Measured / declared / copied per statement. Species, temperature, Mg2+ (NMDAR!), glycine/glutamate, pH buffer for every number. Figures viewed with the Read tool for every number that enters a row; an abstract is not full text; a value read off a raster is INFERENZA and says so. A recombinant value is not a native value; a native value from one region is not a value for layer II/III. Absence claims state their perimeter and use two routes. No compound recommendation, no ranking, no claim on WWOX, no dose.

## Source budget
At most **12 sources newly read** (about 4 for N1, 3 for N2, 2 for N3, 2 for N4; unreachable sources are recorded with route and depth). If the budget ends before a question is answered, name the question and the first undone step.

## Deliverables (in `output/`)
1. `proton_sensitivity.tsv`: `row_id, target (GluN1/GluN2A | GluN1/GluN2B | triheteromer | native NMDA | ASIC1a), system (recombinant|native), species, age, temperature, Mg2+_mM, agonists, pH_midpoint, hill, residual_at_saturating_acid, fraction_at_7.4, fraction_at_7.2, fraction_at_7.0, source, locator, depth, kind (measured|declared|copied|inferred_from_figure), note`.
2. `native_evidence.tsv`: `row_id, current, cell_type, region, age, temperature, mg_mM, pH_step, effect (value, unit), n, source, locator, depth, kind, transfer_gap_to_cortical_L2_3`.
3. `decisive.tsv` (10 to 16 rows): `prop_id, statement, question_id, source_pmid_or_doi, locator, producer_status, depth, kind, class`.
4. `answers.md` (one page: one line per N with the deciding rows; the score of priors N1-N5), `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role, prop_ids, locator_quote (<=25 words verbatim), species_system, note`), `figure_notes.tsv`, `queries.tsv` (`query_id, database_or_route, string_or_url, run_at_utc, hits, what_was_done`), `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci45n --check-doi <file>`, not recorded), `phase_note.md` (<=12 lines).
5. Do **not** write README, hypotheses, consumer_delta, COST_NOTE or the net-sign table.

## Hard additions
No gates, lint, tests, batteries, commits. No e-mail, registration or contact-address service; never send any address to any service. Publisher text stays in scratch outside the repository. Not medical advice. Nothing is promoted.

## Final message
Sources newly read with depth; figures opened; unreachable items and routes; counts per deliverable; the one-line answer per N with its deciding row; prior scores; anything that surprised you.
