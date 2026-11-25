# PREREG, ADV-282 increment 1: activity or engagement check of the first eight queued null notes (SCI, frozen 2026-11-25T19:47:25Z)

Hypothesis level; reference genotype class; nothing here is medical advice. Actor orchestrator (SCI), session ae0002e7, claude-sonnet-5-5, effort high. Brief: `advisor_pilot_20261113/assignments/ADV-282.md`. Written before any held source was opened for this assignment.

## Already done before this window

Part (A), acquisition of PMID 31806980 and 27211851, and part (C), the table of the six equivalence rows, were done by the previous window (ADV-281 folder, RESULT section 8 and `equivalence_rows_adv281.tsv`). This window runs part (B) only.

## What was already seen when this was written

The note text, `source` label, `direction` and `reading_depth` of ranks 1 to 16; checkpoint AM; the ADV-281 PREREG and RESULT. No held source, deposit table or figure.

## Population and order

The 48 NULL rows of `screen_adv281.tsv` that ADV-281 did not audit, on today's cards: none is gone and no note text changed. One row is a new route hit since ADV-281, DR-A02-001 (an ADV-279 rewording about measurement weakness on a row coded INCREASE); it is not a null result and is not added. Order: `queue_ordered_adv282.tsv` (sha256 `678d1caac82a854d7451a007449d0763979203ea43b3c118f4adf1fc6c689e99`), rule in the header of `step0_list_adv282.py`: units that carry the row's study by HE's `consumer_count.py`, then files naming the id, then id. The count is per study, so rows of one study tie; it says that a record names the study, not that it depends on the row.

Increment 1, ranks 1 to 8: DA-GSE-PDK-003, DA-L01-003, DA-W2-012, DA-J01-007, DA-K01-002, DA-I01-001 (deposit GSE156243, PMID 34268881), DA-W2-011, DA-I01-006 (PMID 42422765).

## Classes (ADV-281, reused verbatim)

Question per note: does the HELD source (main text, supplement, source data actually held) carry an activity or engagement check for the manipulation whose result is null?

* **CHECK PRESENT:** a positive control, dose-response, target-engagement readout or an effect of the same manipulation shown in the same source, in the same preparation (species and cell type or tissue), at the same or lower dose and the same or shorter exposure as the null.
* **CHECK PRESENT BUT NOT MATCHED:** such a check exists but differs in dose (higher), time, cell type, species or assay; a citation of another paper's result counts here, never as present.
* **CHECK ABSENT:** none in the held bytes; the negative carries its date and the query (epistemic_discipline.md section 2.4).
* **NOT ASSESSABLE:** bytes missing or not what their name says.

A control that only shows the readout can move is an assay control, not an activity check. "In-study check yes/no" is recorded beside every class. Strict = ABSENT; loose = ABSENT or NOT MATCHED. The class never decides a direction.

For a genetic manipulation (the six deposit rows) the check is loss of the target shown in the same preparation (protein, or a transcript that the edit removes) or another effect of the same knockout in the same libraries or tissue. For a vector arm it is expression of the transgene in the tissue read.

## Second column for rows with printed numbers

Every printed ratio, count and p of the six deposit rows is recomputed from the held count table, with the table, row and sample columns named, the replicate unit and species beside it, and the comparator (which libraries, which normalisation) written before the value is computed: CPM per library, ratio of the group means of knockout over wild type, on the libraries the note names (4 knockout, 2 wild type). A second normalisation is reported only if the first does not reproduce the printed value.

## Predictions

Base rate (ADV-281, the nine survivors of the ten): loose 4 of 9, strict 1 to 2 of 9; over 15 audited, loose 5 to 7. Adjusted down because six of these rows are knockout-against-wild-type readings, where loss of the target is normally shown.

* P1 strict: 1 of 8, range 0 to 2.
* P2 loose: 2 of 8, range 1 to 4.
* P3 blind sentence reader, MUST CHANGE: 1 of 8, range 0 to 3 (ADV-281: 2 of 13).
* P4 blind sentence reader, MUST CHANGE or ADD: 6 of 8, range 4 to 8 (ADV-281: 12 of 13).
* P5 deposit rows whose printed values do not all reproduce: 1 of 6, range 0 to 3.

Rejecting observation, for the decision this feeds (a positive-control field in the card template): if increments 1 and 2 together give loose 3 of 16 or fewer, the genetic and transcript nulls are mostly checked and any proposed field is limited to compound and delivery rows.

## Blind check

One blind reader per increment (legend-delegate, claude-sonnet-5-5, effort high). It gets the verbatim repository sentence built by script from the card JSON and the held-source paths, never the first reader's class or facts; it may not open this folder, the ADV-281 folder or any card text. Verdicts MUST CHANGE / ADD / STANDS and its own class. No receipt is written: this is a targeted check, not a completed read.
