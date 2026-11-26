# Self-evaluation - SCI window AQ successor (9bb60ab5), ADV-291 and the ADV-292 pre-registration, 2026-11-26

## Scope and executable verdict

- Actor `orchestrator` (SCI), `claude-sonnet-5-5`, effort high on every turn read back (109 turns at the time of writing; peak context about 365k, cache-inclusive; one context compaction). One delegate: blind figure reader, `legend-delegate`, asked sonnet and high, read back `claude-sonnet-5-5`, high on 16 of 16 turns.
- Receipts written: none (ADV-291 re-read held supplement images; no completed reading is claimed). `session_self_eval.py`: PASS (declared gaps shown are older records). Receipt ledger OK (2,852 chained, tail anchored). Structural LINT: warnings only, none from this window's files.
- This is a compact diagnosis by dimension; the 27 protocol questions were not answered one by one.

## Content diagnosis

| Dimension | Answer | Grade | Debt or correction |
|---|---|---|---|
| Rule fixed before the sources | ADV-291 PREREG with a frozen rejecting observation, committed before the images were opened; own read saved before the blind reader reported | strong | its premise "no earlier window read these images" was false: three had been viewed on 2026-11-07/08 (result section 4) |
| Source reading | values read by pixel profile with calibration; two reads agree within about 0.2 Hz; printed r and p recomputed | strong | low-resolution rasters; the a2 statistic is not identified |
| Corrections to own side | ADV-290 note on the dose-decision candidate was false (another paper's S3C); reported to ADV and IT before it was applied | strong (honest) | the error was found one unit late; the line had not been read in its file |
| Direction proposal (ADV-292) | proposed ten records from a count that used the old matching and no standing exclusions; four could not be read as stated, and ADV had registered them; found when reading the earlier PREREG, before any source and before a PREREG | weak | checklist bullet added (below); the count must be right before it is sent, not after the go |
| Reporting of thresholds | ADV's stated condition (more than ten records with two or more consumers) was reported as met and was not (7) | weak | corrected to ADV, who recorded it |
| Delivery to consumers | ADV-291 consumed by ADV; sentences of ADV-289 to ADV-291 not yet messaged to IT (held for IT's apply report) | adequate | ADV believed they were with IT; stated otherwise in checkpoint AR |
| Context discipline | ADV-292 GO accepted above the 280k checkpoint line; the reading was handed to a successor | adequate | the window ran well past the line during ADV-291 closure |

Who caught what: the blind reader independently confirmed the S1G reversal; SCI caught the ADV-290 line error and its own ADV-292 list; no check or peer caught the latter first.

## Micro-upgrade (done, not promised)

A bullet in `adv276b_lead_receipts_sci_20261125/PRE_READ_CHECKLIST_ADV276_SCI_20261125.md`: a reading-queue count is quoted only after the corrected consumer matching, the content check, the standing exclusions and the declared-figure check.
