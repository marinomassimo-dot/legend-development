# Pre-registration: the independent unit behind each numeric n in the claim records (SCI; hypothesis level; not medical advice)

ADV default offered after ADV-259 (no assignment number at freezing). Extends ADV-247 from carried inferences to claims. Frozen before any n-statement of a claim record is read with its source in this task.

## Already seen by the writer

The counts only: 47 claim records, 24 named in the working model; a pattern for a numeric n matches 13 of those 24, plus CLAIM 007 and 014 named by ADV. Earlier results of ADV-244 and ADV-247 (the GSE156243 knockout organoids are one clone) are known.

## Scope

CLAIM 002, 003, 005, 007, 011, 014, 021, 025, 031, 032, 033, 034, 038, 042, 047. In each record, every statement that gives a numeric n or a counted number of units (mice, animals, people, families, lines, clones, libraries, organoids, samples) for a result the record uses. A number that is not a replicate or subject count (a dose, an age, a fold change) is not a statement. `working_model_history` and update logs inside a record count only if the current text of the record relies on them.

## Unit taxonomy and effective n

As frozen for ADV-247: ORG (organism or person, independent), DER (separately derived clone, line or donor, independent for the derivation), CULT, TECH, CELL (not independent), POOL (the pool is one), NS (not stated). Effective n is the count of distinct units at the level where the difference between arms was created. For a count of reported people or families, the unit is the person or family, and overlap between reports is noted.

## Dispositions

independent; non-independent (both numbers given); not stated; not a comparison (a descriptive count).

## Reading rule

The unit is taken from the paper (methods, legend, results, supplement, sample record), read in two places where two exist, else marked "one source". A registry or dossier sentence is not a source. A source that cannot be reached leaves the statement "not checked".

## Expectations

* C1: between 10 and 35 percent of comparison n-statements are non-independent.
* C2: at least two claims carry a headline sentence whose n is non-independent and not already said so in the record.
* C3: most people and family counts are what they say (independent).
