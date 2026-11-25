# PREREG, ADV-281: positive-control audit of null-wording card notes (SCI, frozen 2026-11-25T18:56:42Z)

Hypothesis level; reference genotype class; nothing here is medical advice. Actor orchestrator (SCI), session 9cc174db, claude-sonnet-5-5, effort high. Brief: advisor_pilot_20261113/assignments/ADV-281.md. Written before any source was opened for this assignment.

## What was already seen when this was written

SCI's ten candidate ids (from the brief); the card JSON field layout; the counts 257 assertion rows, 246 distinct ids; the list of ids whose `direction` is `NO_CHANGE` among drug assertions; the note text of DR-A01-003; the brief's chloroquine examples (38378758, 38740822, 30202070), so DR-A02-002 does not count as an independent test of the prediction.

## STEP 0: population and the two routes

Population: every assertion row of `cards/*.card.json` under `input.drug_assertions`, `input.disease_assertions`, `input.disease_assertion`, deduplicated by assertion id.

* **Route S (structured field, no text):** `direction` equals `NO_CHANGE`.
* **Route T (text):** `measured_result_note` or `note` matches, case-insensitively, one of the phrases in `list_adv281.py` (constant `PHRASES`, written with this file and not edited after the first run).

Screening of every row found by S or T, from the card text alone:

* **NULL** (listed): the row or its note says that a manipulation (compound, genetic, diet, delivery) was applied and a named readout did not change, was not rescued or was not significant.
* **X-EVIDENCE** (excluded): the phrase is about what was read, measured or can be concluded, not about a result.
* **X-NOMANIP** (excluded): an absence with no applied manipulation (observation, correlation, expression level).
* **X-OTHER** (excluded): anything else, with the reason written.

The brief's rule for the ten: each is reported as supported by both routes, by T only, by S only or by neither. A T-only member stays because the brief says to add what the second route finds; an S-only note is a structured null without null wording and is also listed, flagged as such. A member of the ten supported by neither route is dropped. Every exclusion is written with its id and reason.

## STEP 1: classes (one per listed note, each with a locator in the HELD source)

Question: does the held source (main text, supplement, source data actually held) carry an activity or engagement check for the manipulation whose result is null?

* **CHECK PRESENT:** a positive control, dose-response, target-engagement readout, or published-by-the-same-paper effect of the same manipulation, **in the same preparation** (same species and cell type or tissue), at the same or a lower dose and at the same or a shorter exposure as the null.
* **CHECK PRESENT BUT NOT MATCHED:** such a check exists but differs in dose (higher than the null's), time, cell type, species or assay system, so it does not show activity under the null's conditions. A citation of another paper's result is NOT MATCHED unless that preparation is the same and the locator is in a held source.
* **CHECK ABSENT:** no such check in the held bytes; the negative carries its date and the query (section 2.4 of epistemic_discipline.md).
* **NOT ASSESSABLE:** source not held or the held bytes do not match their name.

The class never decides a direction. Only the wording and the consumers change.

## Order and perimeter

The surviving members of SCI's ten first (two increments of five, in id order), then the additions in order of consumer count, as far as the budget of about 150 minutes allows; what is not reached is queued by id. Held bytes and the receipts ledger only: no acquisition, no spend, no contact. IT's cell-line identity question is left to IT.

## Predictions (for the surviving members of the ten)

* P1: CHECK ABSENT (strict): 3 of 10, range 1 to 5.
* P2: CHECK ABSENT or NOT MATCHED (loose): 6 of 10, range 4 to 8.
* P3: blind sentence reader returns MUST CHANGE on 2 of 10, range 0 to 4 (calibration: ADV-280 strict 2 of 10, loose 9 of 10).
* P4: the text route finds at least one NULL row outside the ten.

Rejecting observation: if the loose count is 2 of 10 or fewer, unchecked nulls are not a general class in the card notes, and no positive-control field is proposed for the card template.

## Blind check

The blind reader gets the verbatim repository sentence (the note) and the paths of the held sources, not the first reader's class or facts; verdicts MUST CHANGE / ADD / STANDS and its own class from the four above. Model and effort are named in the dispatch.
