# ADV-002 result (Harness): routes to the two SCI51-blocked artefacts

Taken in charge by Harness in `ledger/tasks/plan/PLAN-PROACTIVE-ADVISOR-20261113.json` (block `ADV_ASSIGNMENTS`), 2026-11-13. Bounded attempt, zero spend, no bot-check circumvention, generic client identity, no address or identifier in any request. No scientific record, ranking or qualification was touched.

## What was reached

| Target | Route | Outcome |
|---|---|---|
| IT51-Q03: Hubler 2018 (PMID 30046109, PMC6423962, open access) | Europe PMC `fullTextXML` | **Reached**: full text and every Extended Data legend. The heatmap is Extended Data Fig. 6p ("inhibition of muscarinic receptor isoforms M1, M3 and M5 by the indicated small molecules at 2 uM, GeneBLAzer NFAT-bla CHO-K1 cells, n = 2 wells"); the Results text states that the panel of six muscarinic antagonists "all showed near-completed inhibition" of M1, M3 and M5 at 2 uM (Extended Data Fig. 6m,p). |
| same | Europe PMC `supplementaryFiles` | Returns a zip with one **0-byte** placeholder image; no content. |
| same | figure image on europepmc.org (`/articles/PMC6423962/bin/...jpg`) | **HTTP 403** (HTML block page). Not retried or varied. |
| same | NCBI PMC OA service (`oa.fcgi`) | HTTP 404 for the id. |
| IT51-Q04: PMID 30773481 (PMC6474808, not open access) | Europe PMC `supplementaryFiles` | Answers "Article ... is not open access one". No route found without a publisher page; the publisher page was the bot check recorded by SCI51. |

## Reading

* Per-compound M1/M3/M5 numbers (the cell values of Ext. Data Fig. 6p) are **not reached**; the text-level statement, which says all six antagonists inhibited the three subtypes, **is** reached and is a locator for Science to read in full. It bears on IT51-Q03's decision (missing M1 tone vs M1 independence): the paper's text says the inert antimuscarinics did inhibit M1 in that assay. Interpretation and extraction belong to Science, not to this note.
* IT51-Q04 (CW compound structures in the data supplement; TASIN-1 drawing in the earlier paper): **no permitted route found**; recorded as unreachable by the routes below, not as inactive or absent.
* Reusable: for an open-access paper, Europe PMC `fullTextXML` gives the complete legend text, including Extended Data, when the publisher or PMC page is bot-checked; it does not give image bytes. Nothing was built or added for this; it is one line for the next searcher, and `framework/scripts/README.md` already routes retrieval.
* Observed in passing for ADV-001: the ChEMBL REST API answered HTTP 200 on 2026-11-13 (status and one molecule), after the HTTP 500 recorded earlier that day. Whether the by-target activity routes work was not tested.

## Deliver to

Science (reads the Ext. Data Fig. 6 legend and text lines; IT51-Q03 locator) and Orchestrator (records outcome against IT51-Q03/Q04 and any consumer consequence). Receipts, if any, through the normal ledger path by whoever may claim them; none is claimed here.
