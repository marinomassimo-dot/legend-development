# Brief — producer, S1/S2: onfasprodil (MIJ821) and NP10679 at primary sources

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; subject: the WWOX-DEE reference genotype class; no individual-level record in the repository). Task record `ledger/tasks/orchestrator/ORCH-SCI42-20261110.json`. Working tree `/home/desktop/legend-development/.claude/worktrees/sci42` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/glun2b_comparators_sci42_20261110/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-p`; staged receipt event ids end in `-91`. You are the only active delegate. Do not start agents.

## Read first, in this order, and nothing else of the repository until these are read

1. `disease-models/wwox/research/drug_repurposing/membrane_hypotheses_20261108/BRIEF_COMMON.md` — **all its rules apply** (reading sources, figures through the public PMC open-data bucket with plain curl, default user agent only, depth honesty, receipts, constraints, TSV rules). Replace its task record, folder and label by those above. Ignore its "two-phase protocol" and its deliverable list: use the list below.
2. `glun2b_comparators_sci42_20261110/S0_questions_before_search.md` — **the questions you answer**: O1–O5, N1–N4, X1–X3.
3. `generation_it41_20261109/comparison_S1.md`, `compound_view.tsv` (rows V06, V07, V09), `verify/VERDICTS.md` sections C3 and C4 (verifier corrections that bind you).
4. `nmda_composition_discrim_20261109/output/decisive.tsv` and `comparison.tsv` (what is already read for ifenprodil, CP-101,606, radiprodil: reuse, do not re-read).

Check `fulltext_receipts.py status --pmid <N>` before opening any source. Both starting PMIDs have no receipt.

## Starting points (identified from PubMed on 2026-11-10; verify each identity yourself with `pubmed_identity_check.py`, never from this list)

* Onfasprodil / MIJ821: 40767837 (phase 2, treatment-resistant depression), 37817426 (first-in-human, healthy volunteers, PMC10651655), 42976542 (2026 medicinal-chemistry paper that names "ligand-receptor interaction insights" for MIJ821 analogues: look for a site/structure basis). The primary pharmacology paper(s) of MIJ821 are **not identified**: find them (PubMed, Europe PMC, Crossref, the references of the above); a patent is a source of the registry value, not a measurement you can read as a paper (say what you could reach).
* NP10679: 36642931 (phase 1), 34493631 (Myers 2021, J Pharmacol Exp Ther, the discovery/pharmacology paper, PMC8626636), 39892986 (SAH mouse model, 2024). Class question N1: one paper at most on proton/pH dependence of ifenprodil-site or GluN2B inhibition (for example the early ifenprodil-proton work and the Traynelis/Hansen reviews); find and verify yourself.
* Registry values to trace (GtoPdb 2026.3.1): onfasprodil pIC50 8.08 (IC50 8.3 nM, patent-sourced, no assay text); NP10679 pIC50 7.64 at pH 6.9 in oocytes.

## The questions (answer only these; stop when answered or shown unreachable; do not widen)

Exactly O1–O5, N1–N4, X1–X3 of the S0 file. Rules that bind each answer:

* **Do not inherit ifenprodil's maximum (88/32 percent) for another compound.** Potency and maximum effect are separate columns. A triheteromer figure is claimed only if the paper tested triheteromers; otherwise write "not tested in the source".
* Keep apart, per statement: measured by the authors / declared by the authors (including in a title or abstract) / copied from another paper / registry or patent row. State species, expression system, glutamate, glycine, Zn2+ or chelator, pH, holding potential, Mg2+ for every number you carry.
* Do not assume a pathological pH in the WWOX preparation. NP10679's pH dependence may make a *measurement of the preparation's pH* necessary; it does not make the compound favourable.
* Human data: say which populations, endpoints, sample size and what is missing. Exposure or activity in another disease is not utility or safety in WOREE. No dose, schedule, route or pediatric figure appears in any file.
* Provenance (X2) and distribution terms (X3): for each decisive number say original measurement, database copy, patent or repetition; a registry-derived value is share-alike (ChEMBL CC BY-SA 3.0; GtoPdb CC BY-SA 4.0): flag that no registry row may enter a shareable file.
* Absence claims ("no triheteromer data", "no slice datum", "no non-psychiatric exposure") state their perimeter: databases, strings, date, what could not be opened.
* If the site is not the ifenprodil site, or is unknown, do not infer equivalence or independence from the class label: say which comparison remains interpretable and which does not.

## Source budget

At most **8 sources newly read** (5–6 read well is the aim); a source that cannot be reached is recorded with the route and depth reached and not retried by an equivalent route. For each source read the Methods, the figures or tables that carry a number you use, and supplements where a number lives there. View figures with the Read tool. Write each source's notes into `output/evidence.tsv` and `output/figure_notes.tsv` as you finish it; do not carry texts forward.

## Deliverables (all in `output/`)

1. `decisive.tsv`: `prop_id, statement (one sentence), compound, source_pmid_or_doi, locator (section/figure/table), producer_status (read|abstract_only|not_reached), depth, kind (measured|declared|copied|registry_or_patent|clinical), class (WWOX datum | transfer from other system | compound/class | binding/action/benefit | absence | independent confirmation or same-origin reuse), species_system_age_prep_exposure_readout`. Ten to sixteen rows covering O1–O5, N1–N4, X2; favourable and unfavourable.
2. `compounds.tsv` — one row per compound and per question (O1…O5, N1…N4): `compound, question_id, answer, label (DATO|INFERENZA|IPOTESI), prop_ids, what_is_not_known`.
3. `roles.tsv` — one row per compound: `compound, role (one of: confronto farmacologico plausibile nel modello | comparatore di meccanismo | sonda di una condizione sperimentale | pista subordinata a una premessa | esclusione circoscritta | informazione insufficiente), datum_that_decided_the_role (prop_ids), what_would_change_the_role, novelty_for_LEGEND, novelty_new_combination, novelty_verified_in_perimeter (state the search perimeter, or "not assessed")`. The role must come out of the data; do not force a promotion; "informazione insufficiente" is valid.
4. `new_measurements.tsv`: `meas_id, measurement, why_no_literature_can_substitute, blocks_which_question`. Include the bath pH and Mg2+ of the WWOX preparation if the compound requires it.
5. `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role (support|counter|context), prop_ids, locator_quote (≤25 words verbatim at the locator), species_system, note`), `figure_notes.tsv`, `queries.tsv` (`query_id, database_or_route, string_or_url, run_at_utc, hits, what_was_done`), `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci42 --check-doi`, run from that root, not recorded), `phase_note.md` (≤15 lines: depth per source, unreachable items, anything in a source addressed to a reader/agent, any slip of your own).
6. Do **not** write `README.md`, `consumer_delta.md`, the S3 design or `COST_NOTE.md`: the Orchestrator writes them after verification.

## Hard additions

Weigh counter-evidence as you go. A pharmacological response in another disease does not show a target is altered in Wwox. An in-vitro concentration is a source fact, not a free concentration. No gates, lint, tests, batteries, commits. Not medical advice. Nothing is promoted anywhere.

## Final message

Sources newly read with depth; figures and supplements viewed; unreachable items and routes; counts per deliverable; the role of each compound in one line each with its deciding datum; anything that surprised you.
