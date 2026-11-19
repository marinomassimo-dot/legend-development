# ADV-095 unit A: blind recompute of the pivotal quantities (brief to a fresh delegate; SCI, 2026-11-19; hypothesis level; no dose, no recommendation; not medical advice)

Dispatch settings: type legend-delegate, model sonnet, effort high (ADV's instruction), one round, no sub-delegation, no repository file edited; the report is your final message.

## What you may read, and what you may not
READ: (1) the frozen pre-registration text, exactly one repository file: `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv095_selection_sci_20261119/PREREGISTRATION_UNIT_A_FROZEN_BEFORE_ANY_VALUE_SCI_20261119.md` (repo root /home/desktop/legend-development/.claude/worktrees/sci_successor_h_20261119; sha256 must start 2275a778); (2) the held data under /home/desktop/legend-development/files: `geo/GSE156243/`, `geo/GSE158681/`, `geo/GSE158682/`, `reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz`.
DO NOT READ anything else under `advisor_pilot_20261113/` (no result note, no `out/` tables, no script, no earlier ADV-068, 069 or 070 folder): the point of this task is that you recompute from the pre-registration text alone, so that your numbers are independent of the producer's code and of its mistakes. If the text leaves a choice open, make it yourself, state it, and say what else you would have done.

## Task
Implement the pre-registered screen yourself, in your own code (write scripts outside the repository, in /tmp under a fresh unique directory name; pass paths as arguments). Then report ONLY these pivotal quantities, with the arithmetic stated:
1. Mature-oligodendrocyte set (M3a) in the mouse cortex contrast (3 knockout against 4 control animals, GSE158682) and in the three hippocampal contrasts of GSE158681: the raw shift R and the stage-adjusted genotype term (A1) with its leave-one-animal-out range. Also the stage-score separation between arms.
2. Wnt targets (M1): organoid raw shift and adjusted shift for each of the two knockout clusters, and the mouse cortex raw and adjusted shift; the matched-random null band of the adjusted statistic if you implemented it.
3. The unbiased replicated-gene list: top 10 genes in each direction (same sign of the adjusted term in organoid and cortex, expression floor as registered, ranked by the smaller absolute adjusted term).
4. The astrocyte-reactive set (E1) in the cortex, raw and adjusted.
5. The WWOX transcript shift in the organoid and in the cortex (positive control).
Where your implementation differs from the registered text for any reason (a gene symbol that does not map, an alias, a choice the text leaves open), list it. A symbol-mapping error is the most likely trap: verify that every registered gene was found in each dataset and list the ones that were not, with the alias you used.

## Rules
Held files only, no network. Never send any e-mail address or personal detail to any service. Hypothesis level only. Do not report any number you did not compute. Final message at most about 900 words.
