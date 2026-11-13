# IT50 case result: the lost eIF2B-probe proposal of INV-02, against the pre-registration

Non-canonical working note. Not medical advice. Reference genotype class only. IPOTESI throughout. No rank, sign or qualification changed. Pre-registration: `prereg_it50.md` (commit 575b0dc6, before any row existed). Reader: `../isr_inv02_it50_20261113/verify/VERDICTS.md`.

## What was done
Three hypothesis rows (ISR1 route discrimination with an eIF2B activator probe; ISR2 node comparison, conditional on a high protein-level sign; ISR3 a potentiation arm as the equally defensible rival) were written from records already on disk (the INV-02 row, `isrib_discrim_20261108` cards and design, the identity note, the IT49 case), registered in the manifest (`hypothesis_packages.tsv`) and mapped (`PKG_MAP`). The generator was rerun. ISR1 reaches the dashboard as one reader row (five languages).

## Against the expectations
* **E1 (three rows with every slot filled or stated missing): held** after the reader's corrections: no prediction (the slot says so), the ISR protein-level sign as an unresolved premise, ISRIB as a probe whose catalogue record is unnamed, rivals and reopen conditions only where a source states them.
* **E2 (the other rows byte-identical): held.** Before and after, the 24 earlier package rows and the six earlier conditional rows are identical (compared by proposal id and by file); only three rows were added; the earlier order is kept (test).
* **E3 (cell join unknown, not low): held** ("no held table carries these genes").
* **E4 (kinase-panel rows not carried as hits): held** (test), and the reader's check of the counts passed (12 rows, 0 for eIF2B activation, 6 not primary-target, two PERK primary-target rows).
* **E5 (manifest row and mapping entry, code only if stated): partly.** One code change was needed and is stated: the investigations list in `package_rows()` was hardcoded to three; it is now read from the manifest (earlier three first, so order is kept). Without it a new investigation could not be reached.

## Verification (independent reader, originals in full)
27 cells: 14 supported, 12 partly, 1 not supported at first reading. The failures were in my connective clauses: two reopen rules that no source states (a sign-to-direction rule), a claim that the potentiation arm is a rival, a card-versus-INV-02 attribution, borrowed statements not labelled, and "which is why the proposal was lost". All twelve corrections were applied; the reader's verdict stands: **no row holds a proposition that INV-02, CARD-A1 and design.tsv do not already hold.**

## What this shows and does not show
Shows: knowledge that sat in a design package and an investigation row now acts inside the generator in the layout it reads, with its blocking premise, its rivals and its reopening condition, and the generator gained a manifest-driven investigation list; the simple target search remains poor for that node (0 rows). **New for LEGEND** as a representation; **not** a novelty against the literature; **no** validated prediction. ISR3 adds little a reader could use differently from the INV-02 row: that is access to existing knowledge, not generation. Whether any row changes a later choice is not shown. The by-target activity route for eIF2B could not be run (the ChEMBL API answered HTTP 500 and no release is cached): a dependency, not a result.
One case, retrospective, scored by its builder with an independent reader for cell support; the generative claim is therefore limited to representability.

## Cost
Software: seconds. Reader: sonnet, high, 62,025 subagent tokens, 9 tool uses, about 2.5 minutes. Translator: one sonnet delegate for six passages. Orchestrator time about two hours (not measured by a tool).

## Update 2026-11-13 (ADV-003)
The by-target activity route that this note records as not runnable (HTTP 500) was run later the same day under a responding service (ChEMBL_37): 28 rows on the eIF2B subunits, none an eIF2B activator; 0 curated-mechanism rows; an activator is found by molecule, not by target (`../isr_target_route_adv003_20261113/README.md`). The dependency is lifted; the conclusion of this note (representability, no predictive claim) is unchanged.
