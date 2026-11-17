# Arm table v7: origin_row on SCI's revision 2 and three assumption signs (IT, keeper; host clock 2026-11-17 ~07:50Z; non-canonical; not medical advice)

File: `ideas_arm_table_v7_20261117.tsv` (76 lines x 10 columns, same columns as v6), built from v6 by `build_arm_table_v7.py` against SCI's revised transfer table (sha256 prefix f098e4aa, as on main). cell_id values are unchanged. The builder asserts unique cell_id and that every origin_row id exists in the transfer table; it passed.
**Origin coverage (counted by value3):** 38 of 75 cells have an origin row (v6: 32), 37 do not, and **0 cells carry a sign (+, -, 0) in value3 without an origin row** (v6: six). The ~20 cells that carry a directional phrase in the sign column without an origin (ADV's wording-based count) are not touched here.
**What changed (6 cells gained an origin; 3 cells' text changed; nothing else):**
* C018 GABA-A PAM I10: no held reading; value3 now '. (assumed)'; the old value is kept in the note.
* C038 Remyelination I5: origin R08c supports the premise only (tier 2); the sign 'rate -' is an ASSUMPTION; value3 '. (assumed)'; old value in the note.
* C015 GABA-A PAM I9: origin R17a (simulation, tier 3); the sign stays; the qualifier 'only after maturation' is an ASSUMPTION (status says so).
* T-type I10 origin R13 (transfer only, tier 3); NMDAR pore blocker I4 origin R17c (the I1 sign carried over, tier 3); the Cacna1g transfer row (now one string for I1/I10) origin R13.
* The duplicated-key pairs still share an origin_row (SCI's table names the string, not the cell); SCI adds cell_id in revision 3 and the match then becomes by cell.
Limits: the origin of a cell is the existence of a reading that names its arm|idea string, not a check that the reading supports the sign (the transfer table's tier and direction columns say that); 37 cells still have no origin row.
