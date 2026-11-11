# IT45 P3 second case / P9: S12 (astrocytic K+ buffering) reopened — the same method on a different mechanism

Non-canonical working note. Not medical advice. Same `activity_search.py`, dose-response types only (IC50, EC50, Kd, Ki), `--max-pages 20`; relation row unchanged (`../../generation_it44_20261110/relations_s12_it44.tsv`). The reopen condition written in IT44 ("when the HE44 resolver is on main") was met.

## Result
* **KCNJ10 (Kir4.1): COMPLETE**, target CHEMBL2146348, 6 rows, 6 molecules, none with a catalogue status. All six are IC50 rows of the form "greater than" 10, 30 or 100 micromolar in "inhibition" assays (five assays say Kir4.1 "unknown origin", one is a thallium-flux assay). They are counter-screens that found no inhibition, **not** activator rows. No enhancer, opener or positive modulator row exists in the held ChEMBL activity data for this target.
* **KCNJ16 (Kir5.1): state `NO_TARGET_FOR_ACCESSION`.** The resolver found no ChEMBL target for the accession: a state of the source, not a statement that no compound exists. The Kir4.1/Kir5.1 heteromer, the form relevant to astrocyte buffering, is therefore **not reached** by this path.
* The IT44 sentence "no enhancer exists" now rests on two reads for one subunit (mechanism tables and activity rows) and on none for the other subunit.

## Joined with the cell class (same method as the Kv7 case)
Mouse P7 RNA (`../../kchan_expression_sci44_20261111/`): Kcnj10 astrocytes 184.76, oligodendrocyte lineage 58–99, neurons 8.12 (FPKM; RNA only). So the lever is anatomically well placed (an astrocytic and glial conductance), and pharmacologically empty: the only activity data are inhibition counter-screens. INFERENZA.

## What it changes
* The astrocytic-buffering explanation of a raised resting K+ stays an explanation without a drug lever; it becomes a **measurement** question (Kir4.1-dependent current and extracellular K+ clearance in Wwox-deficient astrocytes), not a repurposing one. No compound is proposed.
* The six inactive inhibition rows are usable as negative-selectivity evidence for a tool arm (compounds that were measured not to inhibit Kir4.1 at the stated concentrations), after their identities are read; they are not pointers to candidates.
* Transfer check: the method (frame before the join, dose-response read, cell-class join, state of each piece) ran on a different mechanism with no new code and gave a different outcome from the Kv7 case (no lever instead of an engageable one). That shows the path distinguishes the two; it does not show that either biological premise is right.
* Reopen when: a Kir4.1/Kir5.1 activity set is deposited, or Kir5.1 acquires a target record.
