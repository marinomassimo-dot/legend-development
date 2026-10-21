# Self-evaluation - repurposing batch group R4b and the R4 repair, scientist-d (2026-10-21/22)

## Scope and executable verdict
- Tasks `REPURP-10H-R4b-D-20261022` (ten readings) and `REPURP-10H-R4-REPAIR-D-20261022` (landed first, on its own branch). NOT WWOX EVIDENCE throughout.
- Receipts: ten staged `FTR-20261021-<pmid>-01` (four `complete_fulltext_read`, six `partial_fulltext_read`); ten manifests, all STRICT PASS, 13 to 18 locators each; `staged_receipt_check.py --check-doi` OK on all ten; `locator_contradiction_audit.py --working-tree` clean after the repair.
- Local verdict: PASS. Nothing here is audited by a second reader; the repairs to eight manifest entries and eight cards are declared unaudited.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | Figures opened as images for every paper that has them; supplements read for 42334048, 36538782, 40162009 (tables only); not read for 35499850, 41250984, 42286026, 39093319, 39439575 (partial receipts) | partial | supplements named in the note |
| Main message | One confirmed repurposed drug (a seizure count, no development endpoint), one external comparator that held up (steep hard-endpointed decline), a measured untreated cohort drift (SCN2A, small in the mean), and missense precedents whose response was post hoc or case-report level | strong | none |
| Hidden gold | A WWOX row (n = 1, not a responder) inside a fenfluramine registry supplement; a 16 percent worsening bar beside a 68.8 percent median reduction; global impression separating only at the "much improved" threshold; a variant class that looks mixed in homomeric cells but partial loss with its partner subunit | strong | blind audit owed |
| Source parity | Review and protocol read as syntheses and designs, primaries as data; the confirmation of fenfluramine rests on a review and a registry because the primary Dravet trials are paywalled | partial | primaries unread |
| DATO/INFERENZA/IPOTESI | Table rows are DATO; transfer sentences INFERENZA | strong | none |
| Existing claims touched | None narrowed; the single WWOX row is recorded, not promoted | strong | none |
| Multi-hop | Ten papers; four candidates carried over; five found by dated searches; three parked with the cascade run | partial | listed in the note |

## What differed in how the R4 manifests were written, against the blind audit's 4 percent adverse rate (16 to 36 percent elsewhere) - a practice to copy
1. **Every trial number was recomputed from the printed table or figure before it went into a proposition** (ratios, percentages, counts), and a discrepancy was written into the proposition instead of being smoothed: three severity-high items were found by the author this way (Fig 4a caption against its bars; a count of 13 against 12; a coverage overstated), and the audit found the source's own table errors only because the manifest quoted the counts.
2. **Intervals were carried as intervals.** Where a quote contained a confidence interval the proposition named it; the eight failed triples were nearly all places where I later paraphrased an interval or a count into a word ("null", "did not differ", "count-type", "three to five") that the quote did not carry. The repair is the same discipline applied to the last mile: **the proposition may not be stronger or rounder than its quote.**
3. **Quotes were captured while the document was open, verbatim, from the artefact, one per proposition**; no ellipsis and no stitching (the audit found none of 184).
4. **Figure attestations list their own readings**, so the audit could recompute the ratio from the attestation itself (that is how the 3-to-5 and 3-to-5-fold errors were caught: against my own attested values). This cuts both ways: it exposes the error, and it is why the error was cheap to repair.
What I did not do and should: re-read each proposition against its quote once more after writing the note, since all eight failures came from the note-to-manifest step and not from the reading.

## Persistence diagnosis
- Note: `disease-models/wwox/research/repurposing_10h_scientist-d_20261022b.md` (tables A and B extended; answer changes tied to rows). Repair record: `repurposing_10h_scientist-d_20261021.md` (section appended) and `repurposing_10h_scientist-d_cards_20261022.md`; task JSONs.
- Receipts staged only. Manifests under `deepdive_manifests/`.

## Process and capability diagnosis
- Skills used: paper_packet claim/packet, pubmed_identity_check, pmc_bucket_fetch, staged_receipt_check, deepdive_manifest, locator_contradiction_audit, repurposing_bridge, check_cards. Declined: `legend-discovery-method` (no novelty claim), `legend-hypothesis-forge` and `legend-safety-triage` (no compound proposed for WWOX), `legend-commit` (not mine).
- Friction: non-breaking hyphens (U+2011) in publisher XML defeat the spec builder's hyphen fallback; `pmc_bucket_fetch.py --root` must be the checkout root, not `files/fulltext` (it nested the files and had to be moved); the verifier accepts a PMC page HTML as the article artefact; a bot-challenged PMC page cannot be reached and was parked.
- Micro-upgrade (CHANGE = NONE in code, evidence for the Harness agent): the spec-to-manifest builder now handles U+2010 and U+2011 and exists only in a session scratchpad; it is disease-agnostic and worth promoting to `framework/scripts` with its test. Second repetition of this gap.
- Residual risk: audits owed (listed in the note); partial readings; the single WWOX row in a registry supplement must be checked against the docx before anyone quotes it.

ATTRIBUTION_CENSUS
incidents: 6
machine: 3   blind_auditor: 0   peer: 0   self: 3
severity_high: 1   of which self: 1
undetected_known: 0
