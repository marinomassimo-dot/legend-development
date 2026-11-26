# Reader 6 (batch 12): HE verification against the original (ADV-293, 2026-11-26)

Reader: legend-delegate, sonnet, effort high, no search, nothing outside the packet (pirenzepine label not read: openFDA had
no label match). Report as delivered: `R6_batch12_as_delivered.tsv` (95 units, rebuilt from the reply in the agent transcript).

| units | OK | ADD | MUST CHANGE (reader) | MUST CHANGE (HE confirmed) | UNSETTLED | NOT A CLAIM |
|---:|---:|---:|---:|---:|---:|---:|
| 95 | 29 | 14 (after two regrades) | 10 | 8 (7 distinct errors) | 33 | 11 |

Strict rate: 8/51 assessable = 15.7 percent (reader's own grades 10/51 = 19.6). Class T: 4/22 assessable = 18.2 percent
(U12.15, U12.31, U12.89, U12.92); class S: 4 (U12.3, U12.35, U12.36, U12.58). U12.3 and U12.36 are one error written twice.

## Confirmed against the original
- U12.3 / U12.36 "the six are named only in an Extended Data figure / not named in the text layer": the Hubler text names
  "only clemastine and benztropine inhibited EBP in OPCs ... enhanced oligodendrocyte formation" (the sheet quotes it at U12.35).
- U12.35 p-fluorohexahydro-sila-difenidol "not found in the text layer": line 40 of the held full text, Methods list,
  "(abbreviated in figures as Sigma H127)"; line 157, Fig 3 legend, "abbreviated as Sigma H127". Text typed from memory of a search.
- U12.31 "off-target rows are two": activity 934837 (CHEMBL1123907) Ki above 100 nM against the imipramine receptor, rat cortex,
  [3H]-imipramine, is a fourth non-muscarinic row beside BSEP (1) and SARS-CoV-2 (2).
- U12.89 "three human-receptor documents": at least six with two or more subtypes by target organism (CHEMBL1129005, 1132561,
  1137537, 1155803, 2311283, 3351363); the reader said five plus one, HE counted six by the target-organism field.
- U12.15 / U12.92 range "1.7 to 180" and "4 to 180": CHEMBL1124523 (human Kd, M2 120 against M1 170 nM, 0.7) and CHEMBL3351363
  (functional rows, M4 1.148 against M1 1.479 nM, 0.8; other pairs 21 and 51) run below 1; 1.66 (M5/M1, CHEMBL1137537) is the
  lowest binding ratio above 1. U12.92 also contradicts the sheet's own 1.7. The range had been corrected once already on 2026-11-25.
- U12.58 "none is an oligodendrocyte-lineage experiment": 24657831 (Kassis 2014, listed in the same sentence) measures HDACs in NG2+
  OPCs and APC+ oligodendrocytes (expression, immunohistochemistry). Absolute word; the intent (perturbation) is in U12.7.

## Regraded by HE
- U12.8 and U12.62 (reader MUST CHANGE, "class IIa myelin results with a function readout are peripheral") to ADD: the abstract of
  27103167 (MC1568, rat stroke, MBP lowered, functional outcome not improved) is a CNS result, but the sheet's own U12.60 names it
  and reads it as confounded by viability, and 'function readout' is undefined in the sentence. Sensitivity: counted, 10 of 51 = 19.6.
- U12.75 stays ADD (reader): "No oligodendrocyte-lineage experiment was found" is scoped by "found", but it would join U12.58 if absolute words are read strictly.

## Not applied (reader additions)
U12.1/U12.81 (two of the six are named), U12.4, U12.16, U12.17/U12.18 (documents repeat values: potential_duplicate flags),
U12.20 (65 rows with no subtype), U12.21 (BSEP and SARS-CoV-2 rows also hold both compounds), U12.37/U12.91 (Fig 3c is a direct
biochemical EBP assay), U12.48.
