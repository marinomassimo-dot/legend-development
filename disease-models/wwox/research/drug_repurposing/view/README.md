# Curated research view (local, regenerable)

`index.html` (full) and `index_shareable.html` (shareable) are each one self-contained file (inline CSS and JS, data embedded as
JSON, no network resource, works from file://). They are generated; do not edit them by hand. Non-canonical research
material: not a ranking of treatments, not a probability of benefit, not medical advice.

```bash
python3 -B framework/scripts/repurposing_coverage.py run
python3 -B framework/scripts/repurposing_view.py run
python3 -B framework/scripts/repurposing_view.py run --source shareable
python3 -B framework/scripts/repurposing_view.py check
python3 -B framework/scripts/repurposing_view.py viewports
python3 -B framework/scripts/repurposing_view.py titles --refresh   # only to refresh source_titles.json
python3 -B framework/scripts/repurposing_view.py audit-shareable      # proof that the shareable output holds no non-allowlisted value
python3 -B framework/scripts/repurposing_view.py package              # shareable_package/ (local preview)
python3 -B framework/scripts/test_repurposing_view.py
```

The first refreshes the module data (offline), the second writes the full view, the third the shareable view, the fourth exits 1 if either file is stale (use `--source full` or `--source shareable` to check one), the fifth runs the regressions (browser tests skip when no Chromium is found; no sandbox-bypass flag is used).

## What the page is (revision 4, IT5 P12)

The page is in Italian for the physician: every orientation text (titles, labels, explanations, filters, legends, buttons, how-to-read notes) is Italian; scientific citations (source titles, quotations, identifiers, source passages, card prose, compound names) keep their original form. The Italian strings are data: `UI_IT`, `POS_IT`, `SCOPE_IT`, `GOALS_IT`, `THREAD_IT`, `NEED_IT`, `STATUS_IT`, `COUNTRY_IT` and `CRIT_IT` in `framework/scripts/repurposing_view.py`, embedded as `D.ui` for the page script and filled into the assets as `{{key}}` tokens (an unknown key fails the build). The renderers (`render_overview`, `render_charts`, `render_banner`) and `assets/curated.{html,css,js}` are presentation only; `build_payload` is the data layer.

Reading order: (1) first screen: a one-line warning (research material, not medical advice; sources in a limited state), the meaning of the letters F / C / P, then one synthetic card per biological thread (goal as two separate dimensions plus Track as a third field; compounds and interventions to study; the reason for the priority; type of evidence; the decisive gap) and the two goals, the units; (2) five graphics, server-rendered inline HTML and CSS: funnel with explicit units (records, families, families with a target listed, families with a stated action on a need target, cards), access categories (US evidence, denominator stated), needs x interventions per thread (letter and word in every cell), targets to candidates (declared actions), coverage and gaps per need; (3) navigation need -> mechanism -> compounds -> evidence -> next question, with filters; (4) candidate profiles with six short answers (why, WWOX result, external precedent or prediction, counter-evidence, missing proof, next step) and, one click further, the criteria and the full tables; (5) research-priority groups; (6) comparison of two to four cards; (7) "Dettagli tecnici", a closed drill-down holding versions, digests, the regeneration command, the source-state table and the whole catalogue screening (technical English, exhaustive, unranked). Counts of pathways are never shown as a measure of efficacy.

Evidence scopes keep their own labels everywhere (glyph, border style and text; colour is never the only carrier). Letters keep one meaning: F green (solid, dashed, dotted border for F1-F3), C red, P grey.

### Source titles

`source_titles.json` (PMID -> title, journal, year) is a tracked cache; the builder reads only files (offline, deterministic). Refresh it with `python3 -B framework/scripts/repurposing_view.py titles --refresh` (NCBI esummary, keyless, one call per 100 ids, 0.5 s between calls, no `email` or `tool` parameter, no contact string); `titles` alone reports coverage. It covers every PMID the cards and the needs reference.

### Real viewports

`python3 -B framework/scripts/repurposing_view.py viewports [--source shareable] [--shots DIR]` drives Chromium over the DevTools protocol (stdlib websocket client, no sandbox-bypass flag), sets real device metrics at 360, 390, 768 and 1280 px (360 and 390 with and without mobile emulation) and A4 print media, and prints `innerWidth` and `scrollWidth` for the first screen, a filtered thread, the comparison, the card export and the technical drill-down. It prints SKIP when no Chromium exists and exits 1 on overflow. Measured results: `preview/README.md`.

### Research priority (not efficacy)

Positions, not scores (IT5 P11; rules and worked cases in `../priority_rules_it5_20261029.md`): one position per card and per need, in three families with different labels: F1-F3 favourable hypothesis (controlled WWOX readout, naming the row that carries it / thin WWOX readout / from the target, intervention not tested in WWOX), C1-C3 counter-evidence to clarify (null or unfavourable / mixed / harm or null from outside WWOX), P1-P3 premise missing (abstention / no next step / nothing favourable recorded or no WWOX observation). A card has no single position: the profile lists one per need and the overview shows the set of need-level positions, never the best. Tags show a tool compound, counter-evidence rows outside WWOX, a beside-it 'not normalised vs wild type' arm and wild-type-only rows counted neither way. The criteria met and not met, with the facts behind them (WWOX result, depth and comparators, outside-WWOX rows, counter-evidence, decisive premise, next step, feasibility actually known), are printed with each position. Listing order is a grouping by kind of reason, not a ranking; inside a position the order is alphabetical. No score, probability or cure ranking exists. `python3 -B framework/scripts/repurposing_view.py positions` prints every card x need with its inputs.

### Export

Each profile has "Export this card (print / PDF)"; the URL `#export=<card id>` (several ids separated by commas) opens the export view, which prints as A4 (date and perimeter, rationale, evidence by scope, counter-evidence, limits, next experiment, sources). Sources are public identifiers printed as text and as links: PubMed, DOI, ChEMBL. Repository-relative paths are not used in the export. "Download as standalone HTML" saves the same card as a separate file. Reviewable previews: `preview/README.md`.

## Data boundary

`run --source full` (default) embeds every row and writes `index.html`; DGIdb-derived rows are not cleared for public release and ChEMBL content is CC BY-SA 3.0, so this file is for local use. It is nevertheless tracked in the public repository (checked 2026-10-28), which is an open exposure for the operator.

`run --source shareable` writes `index_shareable.html` and embeds a third-party row only when its provenance is class A in the allowlist `shareable_sources.json`: our own cards, needs and priority text; DGIdb rows whose claim source is FDA, CIViC or DoCM; per-compound access categories stated from openFDA NDC; MATRIX names (none occurs in the current output). Everything else appears as identifiers and counts. IT5 P13 changes (the policy of the licence reconciliation, `../catalog/README.md`, as corrected by its independent verification):

- NCI moved to counts-only (its terms were not read at NCI); MATRIX is class A only for the fields its authors own, never for the ATC, DrugBank and ChEBI identifiers inside it; no DrugBank, ChEBI, ATC, UNII or InChIKey value is embedded.
- Every claim source of the catalogue is classified (A attribution, B share-alike, C identifiers and counts, D local only) in `claim_source_policy`; an unclassified source fails the audit.
- Per-row status class and modality are never embedded (they derive from ChEMBL, MATRIX and DGIdb statements); a card row keeps an access category only when the catalogue states it from openFDA NDC (`prescription`, `OTC`) or as an absence (`unknown/unverified`); `experimental` (ChEMBL) and `supplement` (DSLD) are counts-only.
- The names and gene of the DGIdb rows listed under "excluded from counts" are withheld (the string audit found them in the first version of this boundary).
- No link leaves the document except to public identifiers: a card is reached through its profile in the same page (`#cand-<id>`); repository file names are printed as text.
- The footer lists the sources actually embedded, the sources that contributed counts or identifiers only, the identifier and bibliographic sources, and the class-B file shipped apart.

No attribution is removed to make data look distributable. The licence analysis behind the allowlist is a separate record; this mechanism does not change its conclusions and is not legal advice. The full file is already tracked in the repository.

### Proof, not just a mechanism (IT5 P13)

```bash
python3 -B framework/scripts/repurposing_view.py audit-shareable            # static: provenance map, forbidden values, structure, links
python3 -B framework/scripts/repurposing_view.py audit-shareable --dynamic  # plus the rendered first screen, every export and standalone download, comparisons, PDF text
python3 -B framework/scripts/repurposing_shareable_audit.py fetch-labels --out DIR   # optional: openFDA label JSON of the cited drugs, for the text audit
```

The audit builds a reference of forbidden values from the FULL catalogue (names and synonyms of records whose name source is not allowlisted, ChEMBL mechanism and target wording, DrugBank/ChEBI/ATC/UNII/InChIKey/MATRIX identifiers, claim sources) and fails when any string, row or identifier traceable to it is in the output, wherever it sits: JSON leaf, key, visible text, attribute, script literal, rendered text. Every JSON field must match a provenance rule (own text, bibliographic fact, identifier, count, class-A row, source metadata, or must-be-empty). A value that both a third-party source and our own cards, needs or code contain is counted as co-attested and reported, never silently dropped; a co-attested ChEMBL wording longer than 8 words fails. The text audit compares every output string with the third-party texts held locally (full texts, abstracts, label JSON): an unquoted run over 25 words, or a marked quotation over 12 words without an attribution phrase (30 with one), fails. Mutation tests in `framework/scripts/test_repurposing_view.py` (class `ShareableAudit`) inject a class-C compound name, a whole class-C row with attributes, a non-allowlisted claim source in a pair, ChEMBL wording, DrugBank and ATC identifiers, an unclassified field, a repository link and an e-mail-like string, and require the audit to fail on each; a mutated policy file is also caught.

### Static package (local preview, not published)

```bash
python3 -B framework/scripts/repurposing_view.py package [--zip PATH]   # writes shareable_package/ (and a deterministic zip)
python3 -B framework/scripts/repurposing_view.py package --check
```

`shareable_package/` holds `index.html` (same bytes as `index_shareable.html`), `NOTICE.md` (sources, terms, credit lines, how each condition is met), `COMPARISON.md` (what the full version holds and the package withholds, with counts), `README.md`, `manifest.json` (embedded sources with row and field counts, withheld counts by class, file digests, audit summary), `TEXT_PROVENANCE.json` (written when a local text corpus exists, carried over otherwise), `LICENSES/` (licence texts pinned by sha256 in `shareable_sources.json`) and `class_b/chembl_cc-by-sa-3.0/` (the ChEMBL records of the twelve card compounds as a separate CC BY-SA 3.0 file with its own licence text and credit line). Class-B decision: ChEMBL is shipped apart because its conditions (URL and release in the credit, same licence for the adaptation) can be met exactly and the page embeds no ChEMBL content; GtoPdb (two licences on the same rows) and ClinPGx (policy page unread) stay counts-only. **The package is a local preview. Publishing it on any external surface is the operator's decision and has not been done.**

## Inputs and layout

Reads `coverage/` (summary, matrix, priorities, pertinence table, associations), `catalog/` (stats, cache manifest, card links), `needs/needs.json`, `cards/` and `cards_early/`, and `join/pubmed_cache` (titles). `assets/curated.html`, `assets/curated.css` and `assets/curated.js` are the curated layer, inlined at build time; the earlier sections are built by the script. Every headline number carries `data-k` / `data-v` attributes that the tests compare with the source JSON. The build reads no clock; the data date is the later of the needs record date and the catalogue build date.

Size: about 1.5 MB per file; lists of the full data layer are paginated (30 per page). A failed, stale, truncated or never-fetched source is shown with its own badge and is never rendered as an empty or OK result.

## Revision history of the full data layer

Revision 2 (corrected coverage layer): headline links are intervention targets only, with pathway members, effector constraints (MAPT) and readout markers shown apart; excluded rows are listed with reasons; L3/L4 use the new state vocabulary (observed in a WWOX system, case-level, measured null, other-disease precedent, enzyme or cell-free engagement, safety signal) and are never summed; dispositions show cells and distinct families; the source-state vocabulary (OK, STALE_EXPORT, STALE_AFTER_FAILED_REFRESH, PARTIAL, FAILED, INCOMPLETE, NOT_FETCHED) is shown with a banner whenever a source is not OK (today DGIdb STALE_EXPORT and DSLD PARTIAL); a section lists the catalogue-derived leads and lead dispositions (`coverage/lead_dispositions.json`) with links to cards and records. All of it is read generically from the JSON.

Revision 3 (association-layer repair): the funnel and the tiles headline the records with a stated action on a need target first (630 records / 594 families) and name the larger count 'target listed' (1,218 records / 1,189 families; 588 state no action), each with its unit.

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
