# Baseline (ii): frequency-of-use ranking (HE, PRESIDIO-011), 2026-11-16

Written for: ADV, IT and SCI, as the second baseline frozen before any outcome table is opened (PLAN_8H, Rule v1 point 5). Non-canonical. Reference genotype class only. Counts only; no outcome, no recommendation, no dose.

What it is: the 15 classes of `rule.json` v1 ranked by how often the class appears in the A1 series, read from IT's feasibility census (`it_a1_feasibility_20261116/census.tsv`, blob `7d66ae4cd482fa1e4531bfb7efb165400cd39744`, sha256 `81242a5fff2f3b0a334f176736e682efa1f37260f7279b4a36a10cc49c843000`, committed 36b0dd1af at 2026-11-16T07:09:35Z). The measure is `children_with_a_row`, IT's upper bound (links marked possible are not merged). Ties stay ties (competition rank). Output: `baseline_ii.tsv`, written by `baseline_ii_frequency.py` (deterministic: two runs are byte-identical).

Judgement made here (the only one): the mapping from census rows to rule class ids, written in the script. Where the census has one merged row, the rule classes share it with the same value and the table says so: benzodiazepine and gabaa_pam_nonbzd (9, tied); t_type_calcium and ampa_antagonist (0, one census row for five groups); nmdar_pore_blocker, glun2b_nam and kv7_opener have no census row and are 0 by absence from the series. The five classes with 0 are therefore tied at the bottom, which says only that the series never mentions them.

What it can and cannot say: it is a prior with no mechanism. It ranks use, not match. A class ranked high here is one the case reports describe often, which case reports favour (report bias) and which the A1 table's own coding made visible (only four classes are coded for outcome). It is the baseline the matrix must beat on classifiable pairs; it is not a prediction about response.

Frozen by the commit that lands this folder. It reads the census only, never the A1 outcome columns.
