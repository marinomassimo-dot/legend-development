# Self-evaluation — scientist-a, P5 (REPURP-10H-P5-A-20261022), 2026-10-22

Executed, not asserted: `p5_check.py` (202 cells, 0 problems; tables reproduced byte-identically); `fulltext_receipts.py verify` (791 chained receipts OK, tail anchored); LINT is run by `task_close.py` at landing. No paper read, no receipt, no reading claim.

**Diagnosis.** (1) Risk that a table passes for a ranking: every cell is verbatim or UNKNOWN, V in the matrix is declared not favourable, the dominance relation is empty and said so rather than filled; abstentions are not called non-dominated. (2) Risk of the comparability gate being tuned to give an answer: it was fixed before the pairs were read (same endpoint, same genotype class) and a sensitivity was stated for the one borderline pair. (3) Risk of laundering a coordinator relay into a card cell: the A51 exposure statement is kept outside the verbatim cells, labelled superseded, unaudited, and without a dose. (4) Weakest part: the origin counts and the staleness flags are one reader's reading of packet text, not checked against the sources; they are marked OWED. (5) Not done: no blind audit, no label search, no rerun of the lookup with per-gene pagination (the tool does not report it).

**Micro-upgrade (the answer, not a promise).** `p5_check.py` makes "the cell is the card's own words" executable, and `build_p5.py` regenerates the tables when a card is repaired; it exposed two stale fields the cards' own checker could not (S2, S4) and one the coordinator relayed (S1).

ATTRIBUTION_CENSUS: 0 triples touched; 0 consolidated baselines touched; 0 commit candidates; 8 stale-field flags and 8 bridge gaps recorded; blind audit owed on every reader's derivation in p5_comparison.md.
