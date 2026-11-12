# Priority questions as usable briefs (IT47)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reuses the investigations table and the open-questions map (rows IT45-Q01..IT47-Q03); no registry is created. The order is the decision each answer can change, not an efficacy order.

## B1. Which targets can a held cell-class table assign to neurons? (in silico, zero spend)
* **Decision it can change:** whether a slice or mixed-culture arm needs a cell-specific control for that target (the dashboard's "cannot be assigned to neurons").
* **Unresolved premise:** 48 of 75 relation-gene pairs have no row in any held table (glutamate receptors, gap-junction and pannexin genes, PDK genes, parts of the Kir family).
* **In-silico work:** the same extraction as SCI44/IT46 on the same hash-recorded inputs for those symbols, predictions fixed before the run, then re-count `relation_context_summary.py`. No new download.
* **Stop criterion:** each symbol has a row or a stated absence in the table; stop when the count is recomputed.
## B2. Cell-specific control as a design requirement
Every arm in a slice or mixed culture names the cell classes that carry its target (from `cell_context`) and includes either a cell-restricted perturbation, a purified preparation or the target protein by class. Used by: INV-18 R5a/R5b, INV-10 S5/S7, INV-08 X1-X3, INV-09 baseline.
## B3. GSK3 / eIF2B baseline (wet) — IT47-Q03 and Q01
Baseline phospho-Ser535 of eIF2B epsilon, total GSK3 and per-cell translation with replicates in WWOX-deficient human neural cells against corrected controls; the catalytically dead epsilon in tissue with intact Gsk3b. **Outcome that changes the proposal:** no raised baseline (the null H5) removes the GSK3 route from the thread.
## B4. E_GABA with rest, threshold and conductance (wet) — IT46-Q01, Q10
The sign of any GABA-supply or modulation lever; read per the dated update of `p9_two_levers_it46.md`.
## B5. Literature-executable (zero spend)
IT46-Q02 (panel entry labelled ABAT), IT46-Q03 and Q11 (INV-10 base rate and benzodiazepine reports), IT47-Q02 (a Ser535 phosphomimetic; DYRK2 in neurons), IT46-Q06 (Winkel 2015 full text), IT46-Q09 (sulforaphane null arm).
