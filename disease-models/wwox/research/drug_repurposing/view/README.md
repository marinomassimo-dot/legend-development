# Curated research view (local, regenerable)

`index.html` (full) and `index_shareable.html` (shareable) are each one self-contained file (inline CSS and JS, data embedded as
JSON, no network resource, works from file://). They are generated; do not edit them by hand. Non-canonical research
material: not a ranking of treatments, not a probability of benefit, not medical advice.

```bash
python3 -B framework/scripts/repurposing_coverage.py run
python3 -B framework/scripts/repurposing_view.py run
python3 -B framework/scripts/repurposing_view.py run --source shareable
python3 -B framework/scripts/repurposing_view.py check
python3 -B framework/scripts/test_repurposing_view.py
```

The first refreshes the module data (offline), the second writes the full view, the third the shareable view, the fourth exits 1 if either file is stale (use `--source full` or `--source shareable` to check one), the fifth runs the regressions (browser tests skip when no Chromium is found; no sandbox-bypass flag is used).

## What the page is (revision 3)

A physician who does not know the repository reads, in order: (1) overview: research goal, WWOX perimeter, data date, the two open possibilities (broad durable recovery; useful partial benefit) as two separate panels, Track A / Track B as a separate field, the 22 needs grouped into six biological threads, what to study next, the decisive gaps, and counts with explicit units (needs, cards, records, families are never one number); (2) navigation need -> mechanism -> compounds and interventions -> evidence -> next question, with filters (biological area, need, access category, country evidence, evidence scope, Track, recovery goal, research status, text); (3) candidate profiles (31 cards): five short answers (why, what was observed in WWOX, what comes from other diseases or predictions, counter-evidence, missing proof and informative step) and, one click further, the technical details and full tables; (4) research-priority groups per need or per goal (see below); (5) comparison of two to four cards (overlap, complementarity, OPPOSED actions; synergy is never inferred); then the full data layer of the earlier revisions (funnel, access, needs, matrix, dispositions, leads, limits, technical details); the attribution footer closes the page.

Evidence scopes keep their own labels everywhere: WWOX experiment in a DEE system; WWOX clinical case report (uncontrolled); WWOX biology in another context; other-disease precedent; computational result; enzyme or cell-free assay; external database record; safety signal; unverified hypothesis; scope not recorded at assertion level. A glyph and the full label always accompany the colour.

### Research priority (not efficacy)

Positions, not scores (IT5 P11; rules and worked cases in `../priority_rules_it5_20261029.md`): one position per card and per need, in three families with different labels: F1-F3 favourable hypothesis (controlled WWOX readout, naming the row that carries it / thin WWOX readout / from the target, intervention not tested in WWOX), C1-C3 counter-evidence to clarify (null or unfavourable / mixed / harm or null from outside WWOX), P1-P3 premise missing (abstention / no next step / nothing favourable recorded or no WWOX observation). A card has no single position: the profile lists one per need and the overview shows the set of need-level positions, never the best. Tags show a tool compound, counter-evidence rows outside WWOX, a beside-it 'not normalised vs wild type' arm and wild-type-only rows counted neither way. The criteria met and not met, with the facts behind them (WWOX result, depth and comparators, outside-WWOX rows, counter-evidence, decisive premise, next step, feasibility actually known), are printed with each position. Listing order is a grouping by kind of reason, not a ranking; inside a position the order is alphabetical. No score, probability or cure ranking exists. `python3 -B framework/scripts/repurposing_view.py positions` prints every card x need with its inputs.

### Export

Each profile has "Export this card (print / PDF)"; the URL `#export=<card id>` (several ids separated by commas) opens the export view, which prints as A4 (date and perimeter, rationale, evidence by scope, counter-evidence, limits, next experiment, sources). Sources are public identifiers printed as text and as links: PubMed, DOI, ChEMBL. Repository-relative paths are not used in the export. "Download as standalone HTML" saves the same card as a separate file. Reviewable previews: `preview/README.md`.

## Data boundary

`run --source full` (default) embeds every row and writes `index.html`; DGIdb-derived rows are not cleared for public release and ChEMBL content is CC BY-SA 3.0, so this file is for local use. It is nevertheless tracked in the public repository (checked 2026-10-28), which is an open exposure for the operator.
`run --source shareable` writes `index_shareable.html` and embeds a third-party row only when its provenance is on the allowlist `shareable_sources.json`: our own cards, needs and priority text; DGIdb rows whose claim source is NCI, FDA, CIViC or DoCM; openFDA; the MATRIX drug list. Everything else (ChEMBL, other DGIdb claim sources, DSLD, UniChem) appears as identifiers and counts: withheld compound names are replaced by the catalogue identifier, per-row status and modality are dropped, excluded-row details keep reasons only. The footer of the output lists the sources actually embedded with licence and attribution, and separately the sources that contributed counts or identifiers only. No attribution is removed to make data look distributable. The licence analysis behind the allowlist is a separate record; this mechanism does not change its conclusions and is not legal advice. Note that the full file is already tracked in the repository.

## Inputs and layout

Reads `coverage/` (summary, matrix, priorities, pertinence table, associations), `catalog/` (stats, cache manifest, card links), `needs/needs.json`, `cards/` and `cards_early/`, and `join/pubmed_cache` (titles). `assets/curated.html`, `assets/curated.css` and `assets/curated.js` are the curated layer, inlined at build time; the earlier sections are built by the script. Every headline number carries `data-k` / `data-v` attributes that the tests compare with the source JSON. The build reads no clock; the data date is the later of the needs record date and the catalogue build date.

Size: about 1.5 MB per file; lists of the full data layer are paginated (30 per page). A failed, stale, truncated or never-fetched source is shown with its own badge and is never rendered as an empty or OK result.

## Revision history of the full data layer

Revision 2 (corrected coverage layer): headline links are intervention targets only, with pathway members, effector constraints (MAPT) and readout markers shown apart; excluded rows are listed with reasons; L3/L4 use the new state vocabulary (observed in a WWOX system, case-level, measured null, other-disease precedent, enzyme or cell-free engagement, safety signal) and are never summed; dispositions show cells and distinct families; the source-state vocabulary (OK, STALE_EXPORT, STALE_AFTER_FAILED_REFRESH, PARTIAL, FAILED, INCOMPLETE, NOT_FETCHED) is shown with a banner whenever a source is not OK (today DGIdb STALE_EXPORT and DSLD PARTIAL); a section lists the catalogue-derived leads and lead dispositions (`coverage/lead_dispositions.json`) with links to cards and records. All of it is read generically from the JSON.

Revision 3 (association-layer repair): the funnel and the tiles headline the records with a stated action on a need target first (630 records / 603 families) and name the larger count 'target listed' (1,218 records / 1,189 families; 588 state no action), each with its unit.

Sections: funnel with explicit units (records, families, pairs, interventions; "evaluated against
WWOX" has its own definition), access categories with the unknown share and scope note, needs panel,
matrix (four levels side by side, never summed), priorities with the seven distinct dispositions and
per-criterion reasons, honest limits, technical details (sources, versions, licences, source states,
digests, regeneration command). Filters: access, need, need evidence scope, observation scope,
Track, recovery goal, disposition, text. Filters can be set through the URL hash, for example
`#f=disp:exploration_candidate&need:NEED-ISR-ATTENUATION`.

Size: about 1.5 MB; matrix and priorities are embedded as a trimmed projection, lists are paginated
(30 per page). A failed, stale, truncated or never-fetched source is shown with its own badge and is
never rendered as an empty or OK result. DGIdb-derived rows are not cleared for public release (per-source terms: `catalog/README.md`, "Licence reconciliation").
