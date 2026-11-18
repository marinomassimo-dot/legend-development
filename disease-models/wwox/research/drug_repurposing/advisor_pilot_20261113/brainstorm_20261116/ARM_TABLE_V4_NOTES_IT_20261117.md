# Arm table v4: what changed from v3 and why (IT, keeper of the arm table; host clock 2026-11-17 ~07:00Z; non-canonical; hypotheses; not medical advice)

File: `ideas_arm_table_v4_20261117.tsv` (76 lines x 7 columns, same columns as v3; v3 and earlier are kept unchanged). Built from v3 by script; the five rows below are the only differences.
Inputs: SCI's transfer-qualification table (`deepening_sci_20261116/TRANSFER_QUALIFICATION_SCI_20261117.tsv`, sha256 prefix cc227c0f; 61 rows: 5 rows change a v3 cell, 32 re-label support only, 24 change nothing), read by me in SCI's worktree before it landed; ADV's reading of the S-line single-nucleus table (R08 values) and ADV's flag on I8 and I17. I did not re-read the single-nucleus table myself: R08's values are taken from ADV's re-read (limit).

| arm | idea | v3 | v4 | basis |
|---|---|---|---|---|
| Sodium-channel blocker (non-selective) | I11b | 'may aggravate rebound phenotype' (+, predicts) | '.', conditional: aggravation only if the interneuron effect exceeds the pyramidal effect by about 2.5 in log terms | R17b simulation; ratio not measured for any agent class; IT is owner of I11b and accepts |
| NKCC1-directed or GluN2B-directed route | I17 | '+ (neonatal)' | '.', sign not entitled for Wwox; strongest sentence: excess not shown | R08 transcripts are not NKCC1 or GluN2B function; ages unmatched; IT is owner of I17 and accepts |
| Sodium-channel blocker | I8 | '+ / graded by Nav1.1 density' | value kept, CAPS_ONLY | SCI proposed a value change; ADV and I read a transcript (Scn1a inhibitory +0.18, interval crossing 0, one animal or pool per arm, pseudo-replicated nuclei) as unable to grade a protein-density idea; I8 owner is HE, whose confirmation is pending |
| Substrate (glucose down, ketone added) | I1 | 'interval changes' | wording conditional: 'duration first, interval secondary' IF the arm maps onto the model resource class (mapping ASSUMED) | R17c; value unchanged |
| same | I4 | same | same | same |
Not consumed: the 32 re-labels (tier caps only) are not written into v4 cells; they stay in SCI's table as the support record. The 24 no-change rows need no edit.
Owner confirmations still pending: I8 (HE), I1 and I4 (SCI/ADV for the mapping), v3 pending items carried. A status of 'conditional' or 'not entitled' is not a refutation.
