# Brief — producer, package A step A2: which pyruvate dehydrogenase kinase isoforms are present in which brain cells, and what their loss or inhibition does in neural cells (outside WWOX)

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; subject: the WWOX-DEE reference genotype class; no individual-level record in the repository). Task record `ledger/tasks/orchestrator/ORCH-SCI44-20261110.json`. Working tree `/home/desktop/legend-development/.claude/worktrees/sci44` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/pdh_pdk_sci44_20261110/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-p`; staged receipt event ids end in `-96`. You are the only active delegate. Do not start agents.

## Read first, in this order

1. `membrane_hypotheses_20261108/BRIEF_COMMON.md` (one folder up, under `drug_repurposing/`): **its reading rules apply** (reading sources, figures through the public PMC open-data bucket with plain curl, default user agent only, depth honesty, receipts, constraints, TSV rules). Replace its task record, tree and label by those above. Ignore its two-phase protocol and deliverable list: use the list below.
2. `pdh_pdk_sci44_20261110/A1_before_search.md`: the frame, the five explanations, what each result would favour, and five **priors (P1-P5) you must score at the end**.
3. `metabolic_inv07_20261107/output/README.md`, `explanations.tsv`, `evidence.tsv` (reuse; do not re-read the WWOX papers or the INV-07 sources) and `generation_it43_20261110/s9/result_it43.md`.
4. `next_batch_it43_20261110/BRIEF.md` Question 2 (IT43-Q02), the question you answer.

Check `fulltext_receipts.py status --pmid <N>` before opening any source; a source with a recorded receipt is reused (cite it), not re-read, unless the question exceeds the earlier coverage (say why).

## Question (answer this only; stop when answered or shown unreachable)

**Q2a. Expression.** For PDK1, PDK2, PDK3, PDK4 (and, as context, the phosphatases PDP1, PDP2 and PDHA1/PDHB/DLAT) in: cortical neurons (excitatory, inhibitory if separable), neural progenitors/radial glia, astrocytes, oligodendrocyte-lineage cells (OPC, newly formed, myelinating), microglia and endothelium as the non-neuronal comparison; humans and mouse kept apart; RNA and protein kept apart; developmental stage where the source gives it (fetal, postnatal days, adult). Give for each row the value **with unit** (FPKM, TPM, CPM, normalised count, copies, intensity), the **biological unit** (animals, donors, pooled samples, cells, nuclei), n, age, region, and the exact table/figure/supplement locator. Cells or nuclei are not animal replicates: say so on the row.

**Q2b. What is known in neural cells (not WWOX) about the function.** Where a primary source tested loss, knockdown or inhibition of a PDK isoform, or a PDK inhibitor (dichloroacetate, AZD7545, VER-246608 or another), in neurons, astrocytes or oligodendrocyte-lineage cells or brain tissue, record: system, isoform tested, intervention, endpoint (PDH phosphorylation or activity, lactate, respiration, viability, differentiation, excitability, seizure), direction, n and depth. Search by tool name as well as gene symbol (dichloroacetate, DCA, AZD7545, VER-246608, PS10, JX06, CPI-613, devimistat, lipoate analogues, PDK2 knockout, PDK4 knockout) with brain, neuron, astrocyte, oligodendrocyte, OPC, hippocampus, ischemia, seizure; the PubMed tool ANDs all terms, so use short strings and OR/parentheses, and record each string. This answers whether releasing PDH is documented to help, to do nothing or to harm in neural cells (the worsening possibility of A1).

**Q2c. Symbol traps.** For each gene symbol you use, record the current HGNC symbol and identifier and any legacy alias that names a different gene (PDK1 versus PDPK1 is known; check others, for example PDP1, PDHA1).

## Data rules (public tables)

* Before downloading any dataset, state design, biological unit, samples, age and availability in `output/queries.tsv`; prefer small processed tables or per-gene queries to atlases. Do not download an atlas larger than about 200 MB; if the question needs one, record why and stop.
* Use only open, no-login, no-registration, no-contact routes (Human Protein Atlas per-gene pages or its documented downloads, supplementary files of open papers, GEO supplementary processed tables, the PMC open-data bucket). A portal behind a bot check or a login is recorded as unreachable and not retried by another route.
* Do the extraction with scripts (python3 -I on downloaded files), save the derived small table and the SHA-256 of each input file used, and note the script path. Do not type numbers from memory.
* An isoform detected at the RNA level makes a lever plausible; it does not show functional dependence or the direction of a benefit. Do not write otherwise.

## Rules that bind each answer

* Measured / declared / copied per statement. Species, region, age, cell preparation (immunopanned, FACS, single-cell, single-nucleus, bulk), for every number.
* No compound recommendation, no ranking, no claim on WWOX, no dose.
* Absence claims state their perimeter (databases, strings, date, what could not be opened).
* Figures and supplements actually opened with the Read tool for every number that enters a row; a caption is not a panel; an abstract is not full text.

## Source budget

At most **10 sources newly read** (6-8 well read is the aim). A source that cannot be reached is recorded with route and depth and not retried by another route.

## Deliverables (all in `output/`)

1. `isoform_expression.tsv`: `row_id, gene, hgnc_id, cell_class, species, age_stage, region, measure (RNA|protein), value, unit, preparation, biological_unit, n, source_pmid_or_doi, locator, input_sha256, script, producer_status (read|abstract_only|not_reached), kind (measured|declared|copied)`.
2. `function_neural.tsv`: `row_id, isoform_or_tool, system (species, cell, age), intervention, endpoint, direction, n, source_pmid_or_doi, locator, producer_status, depth, kind, limit`.
3. `symbols.tsv`: `symbol, hgnc_current, hgnc_id, legacy_alias_conflict, source, note`.
4. `decisive.tsv`: 10 to 16 rows `prop_id, statement (one sentence), question_id (Q2a|Q2b|Q2c), source, locator, producer_status, depth, kind, class (same_preparation|transfer|absence|model)`, favourable and unfavourable to "the relevant cell expresses a kinase the typed inhibitors act on".
5. `priors_scored.tsv`: P1-P5 with the evidence row ids and the result (held|failed|not_testable).
6. `answers.md` (one page): the one-line answer per Q with the deciding row ids; `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role, prop_ids, locator_quote (<=25 words verbatim), species_system, note`), `figure_notes.tsv`, `queries.tsv` (`query_id, database_or_route, string_or_url, run_at_utc, hits, what_was_done`), `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci44 --check-doi <file>`, not recorded), `phase_note.md` (<=15 lines: depth per source, unreachable items, anything in a source addressed to a reader or agent, any slip of your own).
7. Do **not** write README, hypotheses, consumer_delta or COST_NOTE: the Orchestrator writes them after verification.

## Hard additions

No gates, lint, tests, batteries, commits. No e-mail, no registration, no service that needs a contact address; never send the operator's e-mail or any address to any service. Not medical advice. Nothing is promoted anywhere.

## Final message

Sources newly read with depth; figures, supplements and tables actually opened; unreachable items and routes; counts per deliverable; the one-line answer per Q with its deciding row; priors scored; anything that surprised you.
