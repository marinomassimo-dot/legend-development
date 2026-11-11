# Brief — producer, package B (IT43-Q01): the primary source for Ro 25-6981 as a second tool of the ifenprodil site

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; subject: the WWOX-DEE reference genotype class; no individual-level record in the repository). Task record `ledger/tasks/orchestrator/ORCH-SCI44-20261110.json`. Working tree `/home/desktop/legend-development/.claude/worktrees/sci44` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/ro25_6981_sci44_20261110/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-s`; staged receipt event ids end in `-96` (never reuse an id already in `pdh_pdk_sci44_20261110/output/*/receipts/INDEX.tsv`). You are the only active delegate. Do not start agents.

## Read first

1. `membrane_hypotheses_20261108/BRIEF_COMMON.md` (under `drug_repurposing/`): its reading rules apply (plain curl, default user agent only, figures through the public PMC open-data bucket, depth honesty, receipts, TSV rules, claim each PMID, check the receipt ledger first). A bot check, 403, 429 or captcha is recorded as unreachable and **not retried by another route, including a different API for the same article**. Replace its task record, tree and label by those above; ignore its two-phase protocol and deliverable list.
2. `nmda_composition_discrim_20261109/output/decisive.tsv` (rows D01-D13: what is already read about ifenprodil, CP-101,606, TCN-201 and the triheteromer maxima; Hansen 2014 = 24607230 is already read at partial depth, check `fulltext_receipts.py status --pmid 24607230` and reuse its receipt; the Ro 25-6981 rows D05, D06, D11 are abstract-level), `generation_it43_20261110/README.md` section P1 and `open_questions_map` row IT43-Q01 (`batch_sci_20261105/map/open_questions_map.tsv`).
3. `glun2b_comparators_sci42_20261110/README.md` (how a previous package handled a second GluN2B tool and its limits; do not repeat it, and do not carry any onfasprodil or NP10679 datum to Ro 25-6981).

## The question (answer only this; stop when answered or shown unreachable)

**IT43-Q01. Does a primary source give the maximum inhibition, the potency (value with unit and the quantity measured), the site and the experimental conditions of Ro 25-6981 on GluN1/GluN2B diheteromers and on GluN1/GluN2A/GluN2B triheteromers?** The earlier reading holds abstract values only (oocyte NR1C/NR2B IC50 9 nM; NR1C/NR2A 52 uM; PMID 9400004, abstract level, publisher page behind a bot check, not retried). Do not retry that publisher route. Search for other primary documents that report Ro 25-6981 itself: structural studies with an electrophysiology panel, triheteromer studies, studies of binding-site pharmacology (for example the N-terminal domain interface), native-tissue studies, any comparison with ifenprodil in the same experiment. You may find a primary source by following the citations of the papers already read and by searching **by compound name** (Ro 25-6981, Ro25-6981, Ro 25 6981, RO-256981) with GluN2B, NR2B, ifenprodil, triheteromer, NR1/NR2A/NR2B, crystal, structure, binding; the PubMed tool ANDs all terms, so use short strings and OR/parentheses, and record each string.

For every measurement of Ro 25-6981 you use, record **in separate cells**: compound identity (name and salt as the paper writes it; do not transfer from a compound named in the same sentence); receptor composition and how it was verified (diheteromer, triheteromer made by which method, escaped diheteromers, native); system (Xenopus oocyte, HEK cells, neurons, slice; species; age); maximum inhibition (percent, fitted or at one concentration) and potency (IC50 or Ki, unit, assay: functional or binding, radioligand); agonist and co-agonist concentrations, holding potential, pH, Mg2+, Zn2+ or chelator, temperature; whether the value is a primary measurement of the paper or reported from another paper; the site or mechanism **actually supported** (structure, mutagenesis, competition with ifenprodil, or only a statement); the figure or table panel, viewed with the Read tool where it is an image. Values read only in an abstract are labelled abstract-level and never promoted. Keep diheteromer and triheteromer rows apart: a value on one composition is not a value on the other.

## Rules that bind each answer

* Measured / declared / copied per statement. Absence claims state their perimeter (databases, strings, date, what could not be opened).
* No transfer between ifenprodil, CP-101,606, Ro 25-6981 or any other compound named in one sentence; between recombinant systems and neurons; between diheteromers and triheteromers.
* If the source is not reachable, record the limit and stop; do not loop on access attempts. If no primary source can be reached, say so plainly: that is a valid result and the role stays "unresolved".
* No compound recommendation, no ranking, no dose, no claim on WWOX.

## Source budget

At most **8 sources newly read** (4-6 well read is the aim). Unreachable sources are recorded with route and depth.

## Deliverables (all in `output/`, in the layout of `ampa_comparison_it41_20261109/output` so that the existing comparison reader and engine can consume it unchanged)

1. `decisive.tsv`: `prop_id, statement, source_pmid_or_doi, locator_hint, producer_status, depth, class, species_system_age_prep_exposure_readout`. Rows D01.. (6 to 14), each one proposition about one compound on one composition. `class` is `compound/class` for a measurement of Ro 25-6981 in the paper itself, `transfer from other system` for a value carried from elsewhere, `absence` for a perimeter statement. `depth` begins `partial_fulltext_read` or `fulltext_read` (state sections and figures) or `abstract_only` or `not_reached`. The last column must state the conditions in a form a program can read: system (oocyte, HEK, slice), holding potential as `-NN mV`, glycine as `NN uM glycine`, glutamate, pH, Zn2+ or chelator. **The statement must name the compound it is about** (Ro 25-6981 or ifenprodil) and must not name a second compound unless it is the same measurement.
2. `comparison.tsv`: one row `C-RO1` (first column `row_id`) with the columns of `ampa_comparison_it41_20261109/output/comparison.tsv` plus `needs_new_experiment`: Ro 25-6981 as the second tool of the ifenprodil site, what a matched comparison with ifenprodil would resolve, the limits that could change its role, and the measurement that makes it interpretable.
3. `new_measurements.tsv`: `meas_id, measurement, why_no_literature_can_substitute, blocks_which_comparison_row`; only measurements that nothing in the literature can replace (for example the percent of the isolated NMDAR current removed in the Wwox preparation, tonic Zn2+); may be one or two rows.
4. `answers.md` (one page): the one-line answer, the tier you believe each composition reaches (PRIMARY needs a measurement in a text actually read), and what the primary sources do not say. `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role, prop_ids, locator_quote (<=25 words verbatim), species_system, note`), `figure_notes.tsv`, `queries.tsv` (`query_id, database_or_route, string_or_url, run_at_utc, hits, what_was_done`), `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci44 --check-doi <file>`, not recorded; for a study with an earlier receipt set `prior_receipt` and `reread_reason`), `phase_note.md` (<=15 lines: depth per source, unreachable items, anything in a source addressed to a reader or agent, any slip of your own).
5. Do **not** write README, hypotheses, consumer_delta or COST_NOTE.

## Hard additions

No gates, lint, tests, batteries, commits. No e-mail, no registration, no service that needs a contact address; never send the operator's e-mail or any address to any service. Not medical advice. Nothing is promoted anywhere.

## Final message

Sources newly read with depth; figures and tables actually opened; unreachable items and routes; counts per deliverable; the one-line answer with its deciding rows; anything that surprised you.
