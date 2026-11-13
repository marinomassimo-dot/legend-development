# IT50 case: the lost eIF2B-probe proposal of INV-02, fixed before execution

Non-canonical working note. Not medical advice. Reference genotype class only. IPOTESI unless a line says DATO or INFERENZA. No rank, sign or qualification changes.

## Question
Can the proposal that the INV-02 case lost (an eIF2B activator as a research probe, the node the card cares about) be represented in the generator so that its output differs from the pre-run **only** by new, labelled rows, with the ISR protein-level sign kept as an unmet precondition and no direction or prediction invented?

## Input
The existing ISR knowledge on disk (`isrib_discrim_20261108` cards, design and audited units; the INV-02 row of `investigations_it20.tsv`); the INV-02 case result (`generation_it49_20261112/p5_case_inv02/`). The by-target activity route cannot be run today (the ChEMBL API answers HTTP 500; `activity_search.py` finds no cached release): stated, not worked around.

## Paths
* Simple reference: target search for EIF2B1-5, EIF2AK1-4 (IT49 arm 1): 12 rows, 0 for eIF2B activation, 6 of 12 not primary-target.
* Current path: `package_rows()` as on main (24 rows, five layouts, no INV-02 row).
* Path under test: a hypotheses-layout package for INV-02 written from those records (each cell cites its source line), registered in the manifest with a mapping entry; generator rerun.

## Expected from the improvement (fixed now)
E1. Three new rows for INV-02, each with observation and source, relation, preparation context, hypothesised action, probe or compound (named, not ranked, ISRIB identity stated as an unnamed catalogue record), unresolved premise (the protein-level ISR sign), declared rivals, discriminating result, reopen or abandon condition; no stated prediction (the slot says "not stated by the package").
E2. The other 24 rows are byte-identical before and after; the output files differ only by the new rows.
E3. The cell-class join for the ISR genes stays "no held table carries these genes" (unknown, not low).
E4. The simple search's six non-primary kinase rows are not carried into the package as hits.
E5. The mapping needs a manifest row and a mapping entry; if it needs code, the code change is stated (the INV list in `package_rows()` was hardcoded).

## No benefit or worse
* any of the 24 existing rows changes;
* a row states a direction, a prediction or a favourable compound the sources do not;
* a cell is not supported by its cited source (independent reader);
* the three rows are the existing design restated with no row that a reader could use differently from the INV-02 card (then it is access, not generation).

## Evidence level that can be reached
New for LEGEND as a representation; no novelty claim against the literature; no validated prediction. A single retrospective case scored by its builder, with an independent reader checking cell support against sources.
