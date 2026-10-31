# IT14 pview: optional comparison figure in the work-order entry

## Decision
Added one generic, data-driven inline-SVG block to the work-order entry (full and shareable pages), driven by an optional `figure` field in `view/work_order.json`. The shareable edition carries the same figure (counts and genotype labels only; the data object passes the leak audit). `figure` may be one object or a list; the new entry NEED-INHIBITORY-HYPOFUNCTION carries two: burst incidence by genotype and resting potential by genotype. No ranking, card, need or scientific file was changed.

## Before / after
Before: the entry showed question, data, would-change and feasibility only; the genotype comparison was prose. After: below the question a figure shows 0/11, 4/23, 36/42 slices with bursts as proportion bars with the counts printed, the unit (slices), the caption stating non-independence, the source, and a compact adjacent table repeating every number (visible, fixed layout, so it never overflows at 360 px).

## Rendered block (described, not screenshotted)
Incidence: a bordered card; bold title; three rows (Wild type, Heterozygote, Knockout), each a label line above an outlined track 252 units wide with a filled bar proportional to events/total (empty for 0/11) and the count "0/11", "4/23", "36/42" at the right. Below: unit line, caption, source line (page tokens, light and dark). Values: label, a dot at the mean with a whisker of the given spread and end caps, value text "-79.25 +/- 1.99" and "n = 13" at the right (minus drawn as U+2212). SVG viewBox 360 wide, width 100%, max 420 px: no horizontal scroll at phone width. `role="img"` with title and desc; the table (`wo-fig-tab`) is plain visible HTML (a first version hidden by clipping overflowed in the 360 px viewport test, so it was made visible). No JavaScript, fonts, images or libraries; no p-values, no trend lines.

## Schema and validator
`figure` = {title, kind "incidence"|"values", unit, caption, source, rows, (values only) value_unit, spread_label}. Incidence rows {label, events, total}; values rows {label, n, mean, spread}. Validator `validate_figure`: rows non-empty, labels non-empty (max 44 chars), ints, 0 <= events <= total, total >= 1, spread >= 0, caption must contain "independent", unit required, any row field matching score/rank/probab/p_value/trend refused, unknown fields refused.

## Data used (verified record only)
Bursts WT 0/11, HT 4/23, KO 36/42; resting potential -79.25 +/- 1.99, -75.51 +/- 1.81, -73.62 +/- 1.36 mV, cells 13/15/40 from 5/6/15 animals (function_pharm_it14_p3_20261101 PRE_REGISTRATION.md section 1 and README; verification README). Not added: the input-resistance spreads (11.74, 15.49, 8.88) given in the task are not present in either package, so they were not used; the type of spread (SEM or SD) is not stated in the repository record and the figure says so. A verifier needs Breton 2021 Table 1 to confirm the spread values and their type.

## Files
framework/scripts/repurposing_view.py (WO_KEYS, validate_figure, resolve_work_order, render_figure, CSS, UI strings); framework/scripts/test_repurposing_view.py (class WorkOrderFigure, 6 tests); view/work_order.json (figure on the new entry); regenerated view/index.html, view/index_shareable.html, view/shareable_package/.
