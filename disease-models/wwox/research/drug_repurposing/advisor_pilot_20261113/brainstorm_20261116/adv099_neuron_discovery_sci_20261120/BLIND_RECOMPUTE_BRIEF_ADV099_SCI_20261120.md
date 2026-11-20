# ADV-099: blind recompute of the pivotal quantities (brief to a fresh delegate; SCI successor, 2026-11-20; hypothesis level; no dose, no recommendation; not medical advice)

Dispatch settings: type legend-delegate, model sonnet, effort high (ADV's instruction for verification), one round, no sub-delegation, no repository file edited; the report is your final message (at most about 900 words).

## What you may read, and what you may not
READ: (1) exactly one repository file, the frozen pre-registration: `/home/desktop/legend-development/.claude/worktrees/sci_successor_i_20261120/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv099_neuron_discovery_sci_20261120/PREREGISTRATION_ADV099_NEURON_DISCOVERY_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md` (its sha256 starts 63faafa4); (2) held data under `/home/desktop/legend-development/files`: `geo/GSE158684/` (10x matrices, ctrl and ko), `geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz`, `reach_audit_downloads/MSigDB_Hallmark_2020.gmt` only if you need it. Python with numpy only is available (no scipy).
DO NOT READ anything else under `advisor_pilot_20261113/` (no result, `out/` table, script or earlier note): the point is that you recompute from the pre-registration text alone, so that your numbers are independent of the producer's code and of its mistakes. If the text leaves a choice open, make it yourself, state it, and say what else you would have done. Write scripts outside the repository in `/home/desktop/.claude/jobs/2d2e7085/tmp/blind_adv099_20261120/`; run Python with `-I`.

## Task
Implement the registered rule yourself, in your own code, and report ONLY these quantities, with the arithmetic or the choice stated:
1. After the nuclei filter (total counts at least 500) and the registered class assignment (marker scores divided by the 99th percentile over both arms; maximum class if at least 0.2), the number of excitatory and of inhibitory nuclei in each arm. Where the text leaves the marker handling open, say what you did.
2. For each neuron class: the number of genes analysed in the nuclei (detected in at least 10 percent of the class nuclei in at least one arm), the median of the maturity-adjusted arm coefficient used for centring, and the number of genes with centred coefficient at least +0.25 (UP) and at most -0.25 (DOWN), before and after the half-split stability condition.
3. In the organoid: the number of genes analysed (mean CPM at least 1), the median used for centring, and the number of genes passing the O rule UP and DOWN (including the group-agreement condition).
4. The number of genes analysed in both systems after matching mouse and human symbols by upper-casing, and per neuron class and direction the observed number of genes replicated (both rules, same sign).
5. Your own permutation null (at least 1,000 permutations) following the registered rule: for each class and direction, the null mean and the 97.5th percentile, and the registered verdict.
6. The Spearman correlation between the centred nuclei coefficient and the centred organoid coefficient across the genes analysed in both systems, per class.
Where your implementation differs from the registered text for any reason, list it. Do not report any number you did not compute.

## Rules
Held files only, no network. Never send any e-mail address or personal detail to any service. Hypothesis level only. Final message at most about 900 words.
