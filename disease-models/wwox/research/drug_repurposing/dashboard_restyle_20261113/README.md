# Dashboard restyle: scientific-report layout, readable first screen

Non-canonical working note. Not medical advice. Task record `ledger/tasks/plan/PLAN-DASHBOARD-READABILITY-20261113.json`. The page is `view/shareable_package/` (published at the GitHub Pages address named in `view/DEPLOY.md`).

## What a visitor can now understand and find more easily
* **What the page is and what to do first**, without scrolling: a title, two sentences on what is studied, three entry points (research priorities, evidence chains, compounds and interventions) and one general caution, instead of five repeated cautions and legends.
* **A research question and why it matters**: the ordered priority list comes first, and each of its first five rows reads question → reason for the priority → solidity of the evidence → decisive uncertainty → next test, in short paragraphs; the others show their question and open on request. Ties stay marked "(tie)", and the sentence that the order is research priority and not efficacy stays above the list.
* **The evidence chains** (observation → need → mechanism → intervention → evidence → experiment, with experimental result, inference and association drawn differently and a node's scope under it) are reachable from the first screen and sit right after the priority list; a node can be selected by click, touch or keyboard to reach its explanation and sources, and the text alternative now reads on a phone.

## Before and after (published page of 2026-11-13 against this change; same generator, English shareable build)
| Distance from the top of the page (css px) | Before, desktop | After, desktop | Before, phone | After, phone |
|---|---|---|---|---|
| first investigation row | 4,420 | 993 | 8,997 | 1,763 |
| evidence chains | 90,743 | 6,366 | 195,051 | 10,021 |

Screenshots in `screens/` (before and after: first screen, a representative row, the chains; desktop 1280 px and phone 390 px; the first screen also in Italian). They were taken in the real Chromium the view tests use (`measure_restyle.py`, which also prints these distances).

## What changed
* `view/assets/editorial.css` (new, additive): serif for reading text (Charter, Iowan Old Style, Palatino, Georgia, Cambria, Noto Serif), sans-serif for navigation, labels, controls and badges; body 17 px (16.5 px on a phone), line height 1.6 to 1.65, prose width about 42 rem; flat sections separated by space and a hairline instead of nested boxes; rows as a numbered reading list; badges lighter; WWOX blue accent unchanged. System fonts only: no download, no external request.
* Header: lead sentence, start-here row, one general note (the existing wording of "To keep in mind"), language links on the brand row; the second "Overview" title, the F/C/P legend, the repeated warning and the sub-line caution before the content are gone from the first screen. The F/C/P legend, the definition of a need and the how-to moved into the existing "How to read" opening.
* Investigations: five notes about order and labels now sit behind one opening; the compound cards follow the list; the long-tail lists (conditional hypotheses, further investigations) use the same reading card as the main rows.
* Long fields (over about 520 characters) are clamped behind an explicit "Show the full text" with `aria-expanded`; the whole text stays in the page, and without script it shows in full.
* The edge table of each chain stacks on a phone (labelled cells) and names the edge type in the page language.
* New interface texts: three short strings in five languages; the translation inventory was regenerated and checks clean.

## Meaning kept
No curated passage was rewritten. Conditional hypotheses keep their dashed "conditional hypothesis, never presented as qualified" mark while closed; origin, kind and identity states keep their words and border styles (none depends on colour); counter-evidence, premises and "what is missing is not negative" notes stay where they were. The clamp hides nothing from the page, and the first sentences it leaves open are the test itself.

## Checks
* Real browser, English and Italian: the three start-here targets exist; a permalink to a compact row scrolls to it, opens its details and focuses it; the clamp button toggles; the origin filter hides rows; selecting a chain node shows its relations; no horizontal overflow at 1280 or 390 px; dark mode reads.
* Test suite: view tests updated where they pinned the old first screen (the F/C/P legend above the fold became the start-here row and general note above the fold; the stacked-table count includes the five edge tables); battery result in the task record.

## Limits
* Rendered here with the environment's fallback serif; a visitor's device uses Charter, Georgia, Palatino or Cambria, which are narrower, so lines are shorter there, not longer.
* The page is still about 180,000 px tall on a desktop: three lists account for most of it (the ranking about 56,000, the candidate cards about 45,000, the research priorities about 19,000). They were not collapsed, to keep every direct link and test path intact; collapsing them with a reveal-on-link is the next step if wanted.
* Headings of the technical drill-down (funnel, filters, needs, matrix, dispositions, leads, limits) are still Italian in the other languages' pages; the drill-down is closed by default.
* Five-language check by build and screenshots of the first screen (English, Italian, French, Spanish, German on the first screen and at 390 px); the translations of the three new strings are the assistant's.

## Turning it off
Delete `view/assets/editorial.css` and the `+ read_asset(dr, "editorial.css")` in `repurposing_view.render`; delete the last block of `view/assets/curated.js` (the clamp). The header and list structure stay; regenerate the views with `repurposing_view.py run`, `run --source shareable` and `package`.
