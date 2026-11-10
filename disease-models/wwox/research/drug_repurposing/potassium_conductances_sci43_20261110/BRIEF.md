# Brief — producer, S2: how much of the resting conductance of a cortical pyramidal neuron belongs to each K+ family, and which tools were shown to act on it

You are a Scientist delegate of the Orchestrator of LEGEND (public edition; subject: the WWOX-DEE reference genotype class; no individual-level record in the repository). Task record `ledger/tasks/orchestrator/ORCH-SCI43-20261110.json`. Working tree `/home/desktop/legend-development/.claude/worktrees/sci43` (absolute paths only; never `cd` into another worktree). Your folder: `disease-models/wwox/research/drug_repurposing/potassium_conductances_sci43_20261110/` (write only inside `output/` and `output/receipts/`). Claim actor label `og-k`; staged receipt event ids end in `-94`. You are the only active delegate. Do not start agents.

## Read first, in this order

1. `disease-models/wwox/research/drug_repurposing/membrane_hypotheses_20261108/BRIEF_COMMON.md` — **all its rules apply** (reading sources, figures through the public PMC open-data bucket with plain curl, default user agent only, depth honesty, receipts, constraints, TSV rules). Replace its task record, folder and label by those above. Ignore its "two-phase protocol" and its deliverable list: use the list below.
2. `potassium_conductances_sci43_20261110/S0_S1_before_search.md` — the question, the five rival explanations, and the arithmetic that sets the target number (a lost conductance of about 28 percent of the resting input conductance, Rin 102.9 to 143 MOhm).
3. `generation_it40_20261109/conditional_proposals_it40.tsv` row CP-MH1 and `hcn_20261107/output/physiology.tsv` (the Wwox observations; reuse, do not re-read the Wwox paper).

Check `fulltext_receipts.py status --pmid <N>` before opening any source: a source with a recorded receipt is reused (cite it), not re-read, unless the question exceeds the earlier coverage (say why).

## The questions (answer only these; stop when answered or shown unreachable; do not widen)

All are about **neocortical pyramidal neurons, preferably layer II/III, rodent, juvenile (about P10–P25), recorded near physiological temperature**. Where a source is another layer, region, age, temperature or species, say so on the row; a transfer is never silent.

* **K1 — share of the resting conductance, by family.** For each of: Kv7/M-current (blocker XE991 or linopirdine, or opener), Kir (Kir2 or Ba2+ at low micromolar, a Kir tool), K2P (TASK, TREK or TRAAK tool), and Ih (ZD7288 or another blocker): what does blocking (or opening) change in input resistance (percent), resting potential (mV), sag and firing, in cells with intact synapses and in cells with synaptic blockers/TTX? Give tool, concentration, internal solution (K-gluconate or KCl), temperature, age, layer, the figure or table panel and n (cells and animals). The aim is a one-line answer per family: **can it carry about 28 percent of the resting conductance at this age, or is its measured share much smaller?** Say "not found" where it is.
* **K2 — development.** In the same neuron type, how do Rin, tau and resting potential change between about P10 and P20, and which of these families' contributions change (Kv7, Kir2, HCN)? One or two sources are enough.
* **K3 — tool identity and limits.** For each tool that a source in K1 actually used in neurons: the primary source of its potency (value **with unit and assay**: recombinant cell line or native neuron, species), its documented alternative actions at the concentration used (for example XE991 and other channels, Ba2+ and non-Kir targets, ZD7288 and sodium or T-type current), and whether the paper shows engagement in the neurons it studied. Do not carry a catalogue annotation as selectivity.
* **K4 — a resolved model.** At most two published mouse or rat models (any gene, not WWOX) in which input resistance rose and the resting potential depolarised in cortical pyramidal neurons and **the cause was resolved by a measured current** (a K+ current loss, an HCN change, cell size). For each: genotype, age, the measured difference current, and the Rin and rest change, so that the pattern can be compared with the Wwox pair. Also, if you meet one, a model with a known K+ channel loss where Rin and rest were both reported as a table (these are used later as an external calibration; list them, do not analyse).
* **K5 — the junction potential.** A primary source with a **measured** liquid junction potential for a K-gluconate pipette solution in a standard ACSF (value, sign convention, composition), so the Orchestrator can judge how large the offset is for the Wwox recordings (K-gluconate internal; the earlier package borrowed about −13 mV). One source; say whether the composition differs from the Wwox Methods as listed in `physiology.tsv`.

## Rules that bind each answer

* **Measured / declared / copied** per statement. State species, layer, age, temperature, solutions (internal and bath K+), synaptic blockers, TTX, for every number you carry.
* **An effect of a blocker shows that a current contributes, not that it is altered in Wwox.** A family's share in wild-type neurons is the quantity asked.
* Absence claims ("no study of Kir2 in layer II/III pyramidal neurons at this age") state their perimeter: databases, strings, date, what could not be opened.
* Preferred: figures and supplements viewed with the Read tool for every number that goes into a row; a caption does not replace the panel; an abstract is not full text.
* No compound recommendation, no ranking, no claim on WWOX, no dose, no schedule.

## Source budget

At most **10 sources newly read** (6–8 well read is the aim); one source of the same group of authors counts once if it is a methods-and-data pair. A source that cannot be reached (bot check, 403) is recorded with route and depth reached and **not retried by another route**. Write each source's notes into `output/evidence.tsv` and `output/figure_notes.tsv` as you finish it; do not carry texts forward.

## Deliverables (all in `output/`)

1. `shares.tsv`: `row_id, family, tool_or_manipulation, concentration_or_genotype, species_layer_age_temp, internal_solution, synaptic_blockers_TTX, d_Rin_percent, d_Vrest_mV, d_sag_or_firing, n_cells_animals, source_pmid_or_doi, locator, producer_status (read|abstract_only|not_reached), depth, kind (measured|declared|copied)`. One row per family per condition actually reported.
2. `decisive.tsv`: `prop_id, statement (one sentence), question_id (K1…K5), source_pmid_or_doi, locator, producer_status, depth, kind, class (transfer from another preparation | same-preparation | tool/identity | absence | model)`. Ten to sixteen rows, favourable and unfavourable to "a K+ family carries a large share".
3. `tools.tsv` (K3): `tool, family, role_in_source (blocker|opener), potency_value_unit_assay, species_system, documented_alternative_actions, engagement_shown_in_neurons (yes|no|not_stated), source_pmid_or_doi, locator, status`.
4. `models.tsv` (K4): `model, gene, species_age, cell_type, d_Rin, d_Vrest, measured_difference_current, source_pmid_or_doi, locator, status, use (comparison|calibration)`.
5. `answers.md` — at most one page: the one-line answer per K, with the deciding row ids.
6. `evidence.tsv` (`ev_id, src, pmid_or_doi, depth, role (support|counter|context), prop_ids, locator_quote (≤25 words verbatim at the locator), species_system, note`), `figure_notes.tsv`, `queries.tsv` (`query_id, database_or_route, string_or_url, run_at_utc, hits, what_was_done`), `receipts/` + `receipts/INDEX.tsv` (staged, validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development/.claude/worktrees/sci43 --check-doi`, run from that root, not recorded), `phase_note.md` (≤15 lines: depth per source, unreachable items, anything in a source addressed to a reader/agent, any slip of your own).
7. Do **not** write `README.md`, `consumer_delta.md`, the hypotheses or `COST_NOTE.md`: the Orchestrator writes them after verification.

## Hard additions

No gates, lint, tests, batteries, commits. No e-mail, no registration, no service that needs a contact address. Not medical advice. Nothing is promoted anywhere.

## Final message

Sources newly read with depth; figures and supplements viewed; unreachable items and routes; counts per deliverable; the one-line answer per K with its deciding row; anything that surprised you.
