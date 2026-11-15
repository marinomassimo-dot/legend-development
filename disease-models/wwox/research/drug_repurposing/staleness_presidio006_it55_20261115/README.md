# PRESIDIO-006: staleness pass over the open-question map (IT, 2026-11-15)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. It classifies; it answers no row. No ranking, need, candidate state or frozen package was edited. Table: `staleness.tsv` (one row per question); mechanical scan: `scan_identifiers.py` (git grep of each row's own identifiers in files committed after its `last_touched`, then reading the lead hits).

## Answer first
Of the 34 rows now OPEN with `literature_executable` or `data_access_blocked` and zero-spend yes or partial (35 this morning; WO-11 was concluded today): **2 ANSWERED** (IT29-P12, IT49-Q02), **8 NARROWED** (WO-12, WO-25, WO-32, RS-R6, IT44-Q01, IT46-Q02, IT48-Q01, IT49-Q06), **24 STILL OPEN**, one of which has a **lapsed blocker** (IT49-Q11). So the pool was partly stale, as the Advisor suspected: 8 rows had a cell out of date against a later result and 3 more received a tested access state, so 11 rows now carry a dated note; the two answered rows are marked CONCLUDED with the path of the answer.
* **IT49-Q11 is the cheap candidate the pass found.** The VU6080824 paper is PMID 40959251, PMC12434521 (open access). The earlier bot check was on another route: the PMC article page answered one plain request today (HTTP 200, 192,000 bytes, an article, VU6080824 named 11 times, a Supporting Information section named; the supporting file itself was not requested). Named decision: whether VU6080824 can be called a probe (a second reading of the counter-screen). Not read by me.
* **Two access tests confirmed a block rather than lifting it:** IT45-Q04 (Harde 2023, PMID 38042151: Europe PMC isOpenAccess N, no PMCID) and IT49-Q08 (2026 Kir2.1 HTS paper, PMID 41701551: isOpenAccess N, no PMCID). One Europe PMC search request each; abstract is census.
* **Order for the portfolio (reasoned, no score):** 1. IT49-Q11 (route lapsed, a named probe decision, one page plus its supporting file); 2. WO-32's remaining half (Hdac7/Hdac9 along the oligodendrocyte lineage; a search with a working Europe PMC; decision: the class-IIa myelin residue); 3. IT49-Q06's remainder (the pH of the hERG deposit; Kir2.4 and K2P untested). Not ordered: the STILL OPEN rows with no later identifier hit are not shown to be unread-by-anyone, only unmentioned in result files.

## Corrections to the Advisor's premises
* Count: 35 at the start (my filter and the Advisor's agree); 34 after WO-11.
* The example IT29-P12 is right: IT30 withdrew S1-32 and S1-33 and read the supplements (c5a4c3ebb, 2026-11-06); the row was last touched 2026-11-05 and is now CONCLUDED.
* **IT46-Q02 is not a lapsed blocker**: SCI48 tested it on 2026-11-12 (SGC probe page a single-page application, PDSP Ki download HTTP 403, not retried); its map cell had never been updated, now it carries the sharper reason.
* WO-06 is as the Advisor says (nothing blocks it; unscheduled). IT44-Q05 is not an access state ("not measured or not reached").
* IT49-Q06 is mostly narrowed, not unreachable: the ML133 numbers were read in SCI49 B; what remains is the pH of one deposit.

## Limits
A row with no later identifier hit is classified STILL OPEN by absence of a mention, not by a reading. The scan keys on PMIDs, PMC and ChEMBL ids and the row id; a result that names only a gene or compound would be missed. Lead hits were read at the answer-first sections of the packages, not in full. No paper body was read in this pass except the structure of one PMC page (title, size, section names).
