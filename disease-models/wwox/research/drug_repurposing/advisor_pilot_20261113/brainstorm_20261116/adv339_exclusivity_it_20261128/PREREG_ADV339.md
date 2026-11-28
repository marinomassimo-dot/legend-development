# PREREG — ADV-339: line/arm exclusivity sentences in the claim registry (IT41, 2026-11-28, written before any source is opened)

Hypothesis level; nothing here is medical advice. Assigned by ADV (2026-11-28). Mandate ORCH-ROADMAP-IT59-20261119.

## Population and enumeration rule
A **counted sentence** is a sentence (split on period or semicolon) of a record in `claim_registry_current.md` that gives an endpoint, readout, measurement or piece of experimental evidence to **one** line, arm, genotype, preparation, cell type or model **to the exclusion of others** — by a marker (`only`, `alone`, `every`, `all remaining`, `no other`, `none`; `solo`, `soltanto`, `solamente`, `unico`, `ogni`, `tutti`, `nessun`, `esclusivamente`) or by named-arm exclusivity ("these are the X line's").
**Not counted:** literature or repository counts ("only paper", "no study"), process statements about LEGEND, quotations of a superseded wording kept for history, and sentences already repaired by `BATCH_20261128_011`.
**Candidate net:** a script over the records returned by the record tool, using the markers above. **Stated recall limit:** exclusivity written with no marker is missed.

## Which sentences are checked
Counted sentences whose evidence comes from a source with a **complete-read** receipt, ordered by claim number, then position. Sentences already judged in the ADV-081..084 or ADV-089 folders are skipped and listed. Check the **first six**; if all six hold, stop and report. Otherwise continue to at most twelve (budget about 90 minutes).

## Competing explanations and predictions (share of checked sentences that do not hold)
* **E1** (written from complete reads, mostly right): under 10 percent.
* **E2** (a substantial share give evidence to the wrong arm or to a single arm that does not own it): 30 percent or more.
* Between 10 and 30 percent: undecided.

## Grades (per sentence, from the source passages: article, legends, methods)
* `HOLDS` — every atom, including the exclusion, is supported.
* `TOO_NARROW` — another arm, line or preparation also carries what the sentence gives to one.
* `WRONG_ARM` — the named arm does not carry it.
* `UNSETTLED` — the held source cannot decide the exclusion (named why).
A sentence does not hold if it is `TOO_NARROW` or `WRONG_ARM`; `UNSETTLED` is reported and left out of the denominator.
**Boundary, one row each side:** "no EM was done in line X" is counted (it excludes an arm); "only one paper reports X" is not counted (a literature count).

## Readers and reporting
First reader labels atoms by figure, panel, genotype, age, unit and n. A second reader (sonnet, effort high) sees only each sentence and the source passages or originals, not the first grades. The rate is reported with denominators (sentences and atoms); disagreements are shown, not collapsed.

## Decision
Which exclusivity sentences are narrowed (BATCH_COMMIT after `test_batch_queue` only where a decision changes, else a dated pointer) and which of RP-016, RP-017, RP-019 need a dated correction (ADV's). Six holding sentences close the pattern.
