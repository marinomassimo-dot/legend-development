# Deviations from PRE_REGISTRATION.md (logged, none hidden; no criterion, threshold or universe was changed after a result was seen)

Order of events: eadbe26a (registration + inputs) -> synthetic-noise development runs (P3_SYNTH=1; no real z-score or count read) -> ae430b6d (AMENDMENT 1 + script) -> E1 first attempt crashed on the file format -> E1 and E2 run -> sensitivity bug found in E2 output -> fix and full re-run.

| # | What | When relative to results | Effect |
|---|---|---|---|
| 1 | Inputs re-frozen from the repaired P1 (31446616) via AMENDMENT 1; the four HIF1A edges are selected by content (ids renumbered) | before any evaluation value was opened | none on readouts, universe or criteria (PRE_REGISTRATION, Amendment 1) |
| 2 | E1: GSE215425 "processed_data.csv.gz" is tab-delimited; the first call crashed on the delimiter (IndexError) before any value was used; the script now sniffs the delimiter | after the amendment commit, before E1 produced any number | none |
| 3 | E2 sensitivity "10 uM / 24 h only" returned n = 0 in the first run because dose strings use the micro sign ("10 µM"); fixed (`startswith("10 ")`) and the whole E2 re-run | after the first E2 output; the sensitivity does not enter any verdict | all other numbers are identical between the two runs (checked: `results_summary.json` keys other than `sensitivities` compared) |
| 4 | REF-0 count: the registration states 1 pilot family hits a module node (an input-only count over the 595-family pilot). Within the 578 families actually used it is **0**: the one family is card-linked and outside the universe by the firewall | disclosed here | REF-0 is a constant zero (degenerate, as registered) |
| 5 | Control C2b (random inputs matched on in-degree in the external network instead of the SD decile) was **added**, not pre-registered, because SD-matched random genes mostly have few regulators, which makes C2 an easy null. It is labelled as such and does not enter any verdict | added while writing the script, before the run | none on verdicts; reported for transparency |
| 6 | Top-decile hit rate for tied scores (REF-0, REF-1 zeros) uses a stable sort of average ranks, so ties fall in input order; this secondary measure is not used in any verdict | script design | none |
