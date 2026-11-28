# ADV-319 result (SCI bc, 2026-11-28): eIF2B epsilon S540E preprint, full text NOT reached (route result)

Hypothesis level; reference genotype class only; not medical advice. Frozen note: `PREREG_ADV319_EIF2B_S540E_SCI_20261128.md` (sha256 619e57c5d7534401506aa0eb88df9118fbb793825d421651253fedc32683e90c, written 2026-11-28T12:02:48Z before any source attempt of this window). Source: bioRxiv doi 10.1101/2025.11.03.686297 (Europe PMC PPR1113314), versions 1 (2025-11-04) and 2 (2025-12-09), licence `cc_no`, API field `published`: `NA`. No receipt is recorded: no full text was read. No delegate.

## Route attempts (UTC, 2026-11-28)
| # | Route | Result |
|---|---|---|
| 1 | Europe PMC search by DOI, core record | HTTP 200; `isOpenAccess` N, `inEPMC` N, `inPMC` N, `hasPDF` N, no PMC id |
| 2 | bioRxiv API details | HTTP 200; two versions, no published journal version; returns the abstract |
| 3 | bioRxiv JATS source XML, v2, 12:03:13 | HTTP 429, `error code: 1015`, `retry-after: 74` |
| 4 | Europe PMC `PPR1113314/fullTextXML`, 12:03:23 | HTTP 500 |
| 5 | bioRxiv JATS source XML, v2, one retry, 12:05:49 (after the stated wait) | HTTP 429, `error code: 1015`, `retry-after: 82` |

Deviation from the frozen note, stricter: its listed PDF request through the web-fetch agent was NOT made. After two 429 answers from the same publisher, a second network client would be a way round the limit. No PMC id exists, so the PMC open-data bucket has no entry to ask for (inference from the record; the bucket was not queried). The same 429 was met on 2026-11-21 (`../rp018_eif2b_s540e_fulltext_sci_20261121/`). Not a held status for the paper: a later window from the publisher, or a journal version, stays open.

## Exact missing observation
In the body or figures of this preprint (or of its journal version): (1) eIF2B epsilon S540E beside wild type AND S540A in the same cells, with the protein level of each form shown; (2) a global synthesis (puromycin or equivalent) or ATF4 readout for S540E, not only the BACE1 5' UTR reporter; (3) the replicate unit and number and per-replicate or per-group values; (4) whether any dead form (E572A in the retinal paper's numbering, or F259L) was tested.

## What the abstract says (ABSTRACT LEVEL ONLY; not a read; seen after the freeze through the bioRxiv API)
* "both eIF2Bε silencing and a phosphomimetic mutant eIF2Bε-S540E increased BACE1 5 UTR-driven translation (P<0.001)": SH-SY5Y; the readout named for S540E is the reporter.
* "GSK-3β inhibition significantly reduced ATF4 and BACE1 protein levels in SH-SY5Y cells in a dose-dependent manner [...] independent of eIF2 phosphorylation" (western blot; the inhibitor is NP031112; the identity NP031112 = tideglusib is not stated in the abstract and is not checked here).
* "NP031112 reversed stress-induced eIF2Bε phosphorylation at Ser540 (P<0.001)."
* The abstract names no S540A or other phospho-resistant arm, no dead form, no global translation readout, and gives no n and no value. An abstract's silence is not evidence that the arm is absent.

## Prediction outcome
H1 (usable control) against H2 (reporter-only): **NOT DECIDABLE**. The abstract is compatible with H2 (my lean) and cannot exclude H1. The counterexample (S540E not different from wild type, S540A same way, or lower S540E protein) cannot be tested. Window X's P1 to P4 of 2026-11-21 stay unscored.

## What changes
| Item | Change |
|---|---|
| Control premise (ADV-114 slice design; IT47-Q02) | **None.** "A phosphomimetic exists, abstract level, not validated" stands. The dead-form-alone arm stays missing. |
| RP-018 status | **None** (waiting). The abstract's ATF4 protein line is a preprint abstract in a neuroblastoma line with no WWOX perturbation: I do not count it as the row's resume trigger. |
| Compound roles | **None.** For the tideglusib dossier owner only: the abstract proposes pS540 eIF2B epsilon as something NP031112 moves under H2O2 stress; if the body ever confirms it with values, it is a candidate engagement readout to examine (lead, not a claim). |

## Next lawful move
Re-check the bioRxiv API `published` field and Europe PMC `inEPMC` at a later portfolio pass (a journal version is the likely route). Nothing else is owed now.
