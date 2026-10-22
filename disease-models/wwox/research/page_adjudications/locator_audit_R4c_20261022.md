# Blind locator audit, R4c lot (2026-10-22)

One separate agent received only (proposition, quote, anchor) triples and the source files (images opened for figure items) and no dossier, note or conclusion. 49 triples: 21 from PMID 42542632, 5 from 42594875, 10 from 42494992, 8 from the 38015929 resume, one from 42286026, 2 from 40162009, one each from 42446932 and 41531035. The manifest D01 card text was not audited here (it re-uses the earlier audited locators of PMID 40665325).

**Result: 42 SUPPORTED (four with clauses that live outside the file audited and were checked against the main text by me), 4 not SUPPORTED:** 38015929 entry 33 NOT_IN_SOURCE; 42494992 entry 22 OVERSHOOT; 38015929 entry 30 OVERSHOOT (minor); 40162009 entry 19 OVERSHOOT (minor). All four narrowed as the auditor suggested. Entries 30, 33 (38015929) and 19 (40162009) were already committed on the task branch, so each carries a `contradicts_locator` object; entry 22 of 42494992 was narrowed before its first commit.

| Manifest | Entry | Verdict | Change |
|---|---|---|---|
| PMID38015929 | 33 | NOT_IN_SOURCE | "of 67 individuals" deleted: the schematic names no number of individuals |
| PMID38015929 | 30 | OVERSHOOT (minor) | the 78-individual denominator is stated for the forecasting analysis, not for the tree; only leaf 2 and leaf 7 are 2 percent leaves; reworded as inference |
| PMID40162009 | 19 | OVERSHOOT (minor) | the treated curve drops twice (about 0.94 near month 6, about 0.83 near month 25); main-analysis comparison left to the main-text entry |
| PMID42494992 | 22 | OVERSHOOT | "provide outcome-assessment services" removed; the quote names an employer only |

Not-checkable-from-the-file clauses (kept, with their sources): 40162009 entry 18 (main-analysis hazard ratio 0.08 is the main text, entry 5 of that manifest), 42286026 entry 16 (the different partner is main-text Fig 1/2, entry 9 of that manifest), 42446932 entry 22 (164 and 159 participants are main-text entry 16).
