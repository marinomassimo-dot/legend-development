# IT18 P4 run 3 pre-registration: a resolution-aware GtoPdb join for the reference

Written 2026-11-01, after runs 1 and 2 were scored and before the run-3 reference is joined for EVAL. Non-canonical research material; not medical advice; pharmacological compatibility only. Runs 1 and 2 and their lock are not modified.

## Why
Run 1 had a determinate reference on 2 of 33 EVAL directed rows. Run 1's join keyed GtoPdb on (parent ChEMBL id, UniProt) for human rows only, while 72 of the 76 directed rows enter through ChEMBL records above the subunit level. Structure checks done before this registration, on DEV ligands only: GtoPdb human rows already list NMDAR and Ca_v3 subunits individually with UniProt (GluN1 to GluN3B, Ca_v3.1 to 3.3), so complex expansion alone adds little; GtoPdb target ids are species-independent and `targets_and_families.csv` maps each to its human SwissProt id; for example a rat GluN2C row and a human GluN2C row share target id 458.

## What is fixed (unchanged from runs 1-2)
Labels: read from the locked `answers.tsv` (digests checked against `answers_lock.json`); L v1 is primary, L v2 reported beside it. Universe, split, truth rule (compatible / opposite / mixed / no direction / unknown), Wilson interval, the 40-row floor and the decision rules of `PRE_REGISTRATION.md`.

## What changes: two reference levels, stated before reading EVAL
- **R3a, primary: orthologue-aware join on the need's own genes.** Every GtoPdb interaction whose ligand maps to a catalogue ChEMBL id is keyed on (parent id, human UniProt of its GtoPdb target id), whatever the target species. Truth is computed on the need's own target genes exactly as in run 1. Rows determinate only through a non-human interaction are counted and listed separately (orthologue evidence: weaker, not the same claim as a human measurement).
- **R3b, secondary, descriptive: family-level reference.** R3a plus GtoPdb interactions on the other human components of the ChEMBL record that brought the compound into the need, only for records with at least half of their components among the module's intervention targets (the v2 criterion; it keeps the NMDAR group, the AMPAR group and the T-type family, and excludes the 26-component calcium-channel group). It answers "does the reference agree at the resolution the module's record is written in", not "at the need's gene". No decision statement is drawn from R3b.

## Measures and decision
For each level and each L rule: EVAL directed determinate rows (was 2/33), L compatible precision with interval, T base rate, errors, abstentions. The run-1 decision rule applies to R3a only. If R3a stays below 40 determinate EVAL rows, the figure is reported with its interval and **no improvement statement** is made, as before. Remaining absence is broken down by cause: compound has no GtoPdb ligand with a ChEMBL id; ligand present but no interaction on the need's genes (R3a) or on the family (R3b); interactions present but no direction.

## Conservation
Unknown is not negative. An orthologue row is not a human measurement. ChEMBL and GtoPdb share part of their literature, so agreement is not independent confirmation. Code and this file are committed before the EVAL reference of run 3 is joined; a DEV-only dry run is allowed for debugging. Any change to the script after the EVAL read is a new, separately labelled run.
