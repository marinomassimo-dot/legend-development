# IT20 P6: a quicker public dashboard (2026-11-02)

Non-canonical research material; not medical advice; no individual-level record (WWOX-DEE genotype class). Scientist, branch `it20-dash`. Presentation work on the curated view; no engine file (`repurposing_search.py`, `repurposing_coverage.py`) was edited, no rule or position changed.

## What changed (method in `../view/README.md`, section "Quick guide, reproducible funnel and explorer (IT20 P6)")

| Question a reader has | Before | After |
|---|---|---|
| Which biological threads look promising, and on what kind of evidence? | Thread cards with F/C/P letters and evidence scopes, below a long first block | "In breve" table per thread: links with a measurement in WWOX, inference from outside WWOX only, hypothesis only, C links, and coverage as "needs with a WWOX observation of the thread's needs" |
| Which interventions deserve study, and why? | Spread across overview chips, profiles and ranking | The F1/F2 links (favourable WWOX-system result) listed with the plain reason, what weakens them, the missing measurement and the named next test |
| Measurement vs inference vs hypothesis | Ten evidence scopes, no summary class | Three classes plus "not classified", glyph + word + border style, read from facts already computed per link |
| Funnel | IT7 selection section (record/family indicators) | Five stages from `catalogue_funnel_it18_p2_20261101/funnel.tsv`: 44,211 records / 16,475 of 40,268 families reconciled -> 3,756 usable -> 21 evaluated -> 40 of 294 family-need pairs comparable (4 of 51 unit-need pairs) -> ready for a named test **not measured** in that unit (card-unit figures printed apart) |
| Need -> interventions, compound -> actions / needs / counter-evidence / gaps | Navigation list with filters; card profiles | Explorer with two pickers and an inline SVG subgraph (need - target - action - compound), text table alternative, deep links `#x=need:` / `#x=cand:` |
| First screen | Dates, perimeter and reading notes in the opening block; four-row sticky navigation on phones | Dates and perimeter moved into the drill-down beside the how-to notes; research-material notice kept; one scrollable navigation row on phones |

`funnel.py run --out <scratch>` was re-run on 2026-11-02: `funnel.tsv` byte-identical to the committed file (`funnel_reasons.tsv` likewise), so the page shows current numbers.

### Addendum: "Principali indagini da portare avanti"

The first block of the page renders the hypothesis branch's `ranking.json["investigations"]` (contract and shareable rules in `../view/README.md`). Until that key lands the page shows "in preparazione" and no row; the renderer is tested on a fixture of the contract (`It20P6Investigations`). What depends on the data landing: the rows themselves, their order and ties, the origin classes, the novelty perimeters and movement reasons, and, for any non-carded compound, a class label in `shareable_sources.json` (`investigations_shareable.class_labels`); without one the shareable page shows a withheld note and the name stays in the full view. After the key lands: regenerate (`run`, `run --source shareable`, `package`), then `audit-shareable --dynamic`.

## Evidence

`before/`: the served shareable package as of `main` at the IT20 task-record commit (same bytes as the online page per DEPLOY.md), `after/`: the regenerated package. Same scenario names; at 1280, 768, 390 and 360 px. Notes: `before/explore_need_*` is the old navigation section (`#navigate`), `before/funnel_*` the old selection section, `before/explore_compound_*` the card list; `after/` shows `#explore` and `#funnel-it20`. `after/explore_compound_detail_*` is the compound view of ethosuximide in the shareable edition (actions withheld, compound -> needs -> declared targets). Full-edition screenshots (with ChEMBL-derived action rows) are deliberately not committed.


**Recapture (2026-11-03, branch `it20-dash2` from the integrated `it20-orch` with the hypothesis data merged).** `after/first_screen_{1280,768,390,360}px.png` were taken again from `view/shareable_package/index.html` after `ranking.json` gained its `investigations` key (10 rows). At 1280 and 768 px the first screen shows the block "Principali indagini da portare avanti" with its purpose sentence ("Ordine delle indagini da finanziare: valuta il valore del prossimo test discriminante, non l'efficacia di un intervento.") and the first row. At 390 and 360 px the block starts just below the research-material notice, under the fold, so those two images look the same as before. `after/investigations_{1280,390}px.png` show the block itself with the real rows. `repurposing_view.py viewports` measures `view/index_shareable.html` by default, not the package file. The package page was therefore also measured with `viewports --out view/shareable_package/index.html` at the four widths (360 and 390 with and without mobile emulation, 768, 1280, plus A4 print). Result: 129 measurements, 0 overflow, exit 0; the F/C/P legend ends at 393 css px, above the fold at 360x780 and 390x844.

Seen on the recapture and not changed here: the shareable projection keeps a name only when it exactly equals a card's own short name or full name. That is why row 1 ("AAV9-delivered human WWOX (gene addition)"), which is close to but not equal to the carded "AAV9-delivered human WWOX", shows the withheld note. A class label in `shareable_sources.json` (`investigations_shareable.class_labels`), or the generator using the card name, would show it.

Fixed on the recapture: once the data landed, the existing guard `Curated.test_positions_are_reasoned_and_unscored` failed, because the curated payload must carry no `rank` key. The page projection now stores the generator's `rank` as `position`. The guard is unchanged, and `ranking.json` keeps its contract field `rank`.

Known pre-existing item, out of scope: IT8 dose and exposure wording in ranking and card text that comes from `pharmacological_qualification_it8_p3_20261029/comparison.tsv` (rows Q01 and Q07). Not edited here.

## What could not be shown, and why

- Compound actions on targets in the shareable edition: they come from ChEMBL (CC BY-SA 3.0) and DGIdb rows not cleared for redistribution; the page says so and keeps the card-declared link. Shown in the full local edition.
- Stage 5 of the funnel in the family-need unit: no reproducible table exists; stated, not substituted.
- Engine fields of the parallel branch (original vs republishing source of an action, effective target level of a DGIdb copy of a ChEMBL group action, specific evidence such as a per-subunit measure): not on `main` yet. The full-edition explorer prints any extra action field generically; the shareable edition needs a `PATH_RULES` classification and the allowlist first.
- Jurisdiction and date of access: only the catalogue's access category (openFDA NDC, mostly US), the catalogue build date and the country class exist per card; no per-product date or non-US jurisdiction is recorded.
