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
