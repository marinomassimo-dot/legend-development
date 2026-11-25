# PREREG A, ADV-287: error rate of fold, ratio, range, percent and "versus" statements in the cards (SCI, 2026-11-25; hypothesis level; not medical advice)

Frozen BEFORE the universe is counted and before any source is opened. Part B (the counted universe, the sample and its seed) is frozen as a second file before any source is opened. Held bytes only; no search, no spend, no contact; the Obeid 2026 article (PMID 42422765) is not touched.

## Definitions

* **Card text** = every string in `cards/*.packet.json` (the packet is the input; `cards/*.card.json` is the bridge's rebuild of it and repeats the packet text, so the packet is the unit and a string repeated inside one packet counts once).
* **Statement** = one sentence (split on ". ", "; " and line breaks) inside a card-text string that carries a quantitative comparison. Quantitative comparison patterns (route 2 regexes, case-insensitive): number followed by "fold" or "x" or "times"; the word "ratio" with a number in the sentence; a numeric range ("N to M", "N-M", "N–M") with a unit, percent or "range"; a number with "%" or "percent"; "versus", "vs", "v." or "against" with a number on each side.
* **Route 1 (structured-field scan):** the same sentences, but taken only from the packet fields that carry measured results by design (`drug_assertions[].measured_result_note`, `.endpoint`, `.note`, `.locator`; `disease_assertions[]` same four; `p4_card.evidence_for_and_against.*`, `p4_card.clinical_census`, `p4_card.pharmacology`, `p4_card.next_measurement`; `evidence_against`, `not_known`), each kept only if the sentence carries a digit.
* **Route 2 (text search):** the regexes above over every string of the packet.
* The two counts and the difference (which sentences, which fields) are reported; the universe is the union, de-duplicated by exact sentence text within a card.
* **Exclusions:** cards D02, F02, E03, I01, H01 (re-derived by IT this week); any statement whose only source is the Obeid 2026 article (locator or receipt naming PMID 42422765 or "Obeid" and no other source): counted and listed as excluded, never opened.
* **Sample:** 20 statements, stratified by card family (letter A to P), seed 287, at least 6 card families; strata rule and seed are written in part B before sampling.
* **Classification (step 1, each statement):** recomputed from the WHOLE held source table or answer (never the quoted row): CORRECT, INCOMPLETE (comparator, row or document left out), WRONG (number, count or unit), NOT ASSESSABLE (source not held, with the reason). One blind reader gets the verbatim sentence plus the whole table.

## Predictions (frozen)

1. Universe (union, after de-duplication and before exclusions): 250 to 500 statements; route 1 returns 40 to 70 percent of the union (the free-text route also reads descriptive prose).
2. Of the 20 sampled statements, NOT ASSESSABLE (source not held or not a statement of one source): 3 to 8.
3. INCOMPLETE-or-WRONG among the assessable: **central 25 percent, range 10 to 45 percent** (HE's 27 percent on sheets; my 41 percent on null-note sentences; cards are older and IT re-derived five, so lower than the sheets is plausible).
4. Class mix: INCOMPLETE (comparator or row left out) at least as common as WRONG (number, count, unit), as in HE's classes.

## Rejecting observation

INCOMPLETE-or-WRONG at or below 10 percent of the assessable statements (HE's rule): the cards are in better shape than the sheets and the audit stops there. With about 12 to 16 assessable statements, one error is 6 to 8 percent and two are 12 to 17 percent: the stop therefore needs at most one error; the sampling interval (exact binomial) is reported beside the rate.

## Step 2, only if the rate is above 10 percent

Corrected sentences to IT with a stated extension (which strata to sample next).
