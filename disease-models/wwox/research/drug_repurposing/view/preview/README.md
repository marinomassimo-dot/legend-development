# Previews of the curated view (IT5 P12)

Captures of `../index_shareable.html` taken with headless Chromium driven over the DevTools protocol
(`python3 -B framework/scripts/repurposing_view.py viewports --source shareable --shots <dir>`; no sandbox-bypass flag).
Each width is a REAL device-metrics emulation (`Emulation.setDeviceMetricsOverride`), not a window size: the page's own
`window.innerWidth` and `document.documentElement.scrollWidth` are read after loading and printed by the command. For 360 and
390 px the page is measured twice, with mobile emulation (as a phone) and without (fixed layout viewport); with mobile
emulation a page that overflows would report an `innerWidth` larger than requested, so the check is `scrollWidth <= requested`.
Screenshots at 360 and 390 px use the mobile emulation. The earlier previews (a 500 px window clamp) were replaced.

Re-measured after the verification fixes (same results). The command also prints the bottom of the F/C/P legend on the first screen: 408 css px from the top at both 360x780 and 390x844, i.e. all three letters are above the fold (a test asserts it).

Measured on the shareable build (innerWidth / scrollWidth in CSS px; all scenarios of the table below were `ok`, none overflowed):

| Requested | Mobile emulation | innerWidth / scrollWidth | Scenarios measured |
|---|---|---|---|
| 360 | yes | 360 / 360 | first screen, filtered thread, comparison, export card, technical details open |
| 360 | no | 360 / 345 (scrollbar 15) | same five |
| 390 | yes | 390 / 390 | same five |
| 390 | no | 390 / 375 | same five |
| 768 | no | 768 / 753 | same five |
| 1280 | no | 1280 / 1265 | same five |
| 794 (A4, print media) | no | 794 / 779 | first screen; export card (4 PDF pages; the whole page prints to about 85 pages, so use the card export to print) |

| File | Purpose | Measured viewport | What to look at |
|---|---|---|---|
| `01_first_screen_360px.png`, `_390px`, `_768px`, `_1280px` | The first screen (top of the page) at four widths | 360/360, 390/390, 768/753, 1280/1265 | Compact header and one-line source warning; overview; letters F/C/P; the first thread cards |
| `02_filtered_thread_390px.png`, `_1280px` | Navigation after "Esplora questo filone" (hash filter on a thread) | 390/390, 1280/1265 | Need rows, mechanism, candidates with letters, evidence, next question; filter bar |
| `03_comparison_390px.png`, `_1280px` | Comparison of two cards | 390/390, 1280/1265 | Table fits; overlap, complementarity, no synergy inferred |
| `04_export_card_360px.png`, `_1280px`, `04_export_card_print_A4.pdf` | Export view of one card (screen at 360 and 1280; print to A4) | 360/360, 1280/1265; PDF at 794 px | Date and perimeter, rationale, evidence by scope, public identifiers with titles |
| `05_charts_funnel_access_1280px.png` | Graphics 1 and 2: funnel with units; access categories | 1280/1265 | Each row has its own unit; denominators stated; US evidence only |
| `06_matrix_by_thread_390px.png` | Graphic 3: needs x interventions, one table per thread, stacked on a phone | 390/390 | Letter plus word in every cell; legend of the nine positions |
| `07_coverage_gaps_1280px.png` | Graphic 5: what is measured in a WWOX system, per need | 1280/1265 | Text yes/no with the counts behind them |
| `08_card_profile_390px.png` | Candidate profiles: six short answers | 390/390 | Letters with plain-words reason, six answers, disclosure for the rest |
| `09_priority_groups_1280px.png` | Research-priority groups with reasons | 1280/1265 | Position, reason, criteria met and not met |

Graphic 4 (target to candidate list) is empty in the shareable build by design (the declared actions come from third-party rows
outside the allowlist) and says so; see it in the full local build.

Regenerate with the commands in `../README.md`, then capture again.

## IT6 P13 additions (one-page synthesis, evidence graph, work order)

Measured with `python3 -B framework/scripts/repurposing_view.py viewports --shots DIR` on the shareable build; scenarios `brief`, `evidence_graph` and `work_order` were added to the five earlier ones and run at every viewport.

| Viewport | Mobile emulation | innerWidth / scrollWidth (each of the three new scenarios) |
|---|---|---|
| 360 | yes / no | 360 / 360 and 360 / 345 (scrollbar) |
| 390 | yes / no | 390 / 390 and 390 / 375 |
| 768 | no | 768 / 753 |
| 1280 | no | 1280 / 1265 |
| 794 (A4 print media) | no | `print_brief` (the longest synthesis): 1 PDF page; `print_brief_all` (every card): 36 pages for 36 cards, so each prints on exactly one A4 page |

| File | What to look at |
|---|---|
| `10_it6p13_brief_390px.png`, `_1280px`, `10_it6p13_brief_print_A4.pdf` | The `#brief=` view of the longest synthesis: eight numbered fields, data date and catalogue build as two separate dates, pointer to the full dossier |
| `10_it6p13_evidence_graph_360px.png`, `_1280px` | The five chains as inline SVG; at 360 px the figure scrolls inside its own container, the page does not |
| `10_it6p13_work_order_390px.png`, `_1280px` | Work order per need inside the priorities section, with the research-update date apart from the catalogue date |

## IT7 P7 additions (selection funnel, hypotheses, predictive test and contexts, printable sections)

Measured with `python3 -B framework/scripts/repurposing_view.py viewports --shots DIR` on the shareable build. Scenarios `selection`, `hypotheses`, `predictive`, `contexts`, `section_selection` and `section_predictive` run at every viewport: innerWidth equals the requested width and scrollWidth does not exceed it at 360 and 390 with mobile emulation (360/360, 390/390), at 768 (753 with the scrollbar) and at 1280 (1265). A4 print, through the `#section=` routes: selection 4 pages, hypotheses 9 pages, predictive test with contexts 5 pages.

| File | What to look at |
|---|---|
| `11_it7p7_selection_390px.png`, `_1280px` | The funnel: present in the catalogue against evaluated, then the five steps with unit, denominator and the unknown share with its reasons |
| `11_it7p7_hypotheses_390px.png`, `_1280px` | Nine hypotheses, each with priority, model position and observed evidence in separate blocks |
| `11_it7p7_predictive_390px.png`, `_1280px`, `11_it7p7_contexts_360px.png` | The exploratory predictive test and the context concordance table |
| `11_it7p7_section_*_print_A4.pdf` | Each new section printed on its own |

