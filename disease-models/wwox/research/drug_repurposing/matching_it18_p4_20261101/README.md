# IT18 P4 — matching comparison (T / X / L)

Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit claim. Public edition, WWOX-DEE genotype class.

## Stage 1 — answers locked (2026-11-01)

Written before the GtoPdb reference of any EVAL compound was read (`load_gtopdb_split` drops EVAL rows on read in the `answers` and `dev` commands).

- `answers.tsv`: T/X/L labels for all 205 universe rows (186 parent compounds; 111 DEV rows, 94 EVAL rows). Columns `L_v2`/`L_v2_reason` hold the dated second rule below, fixed on DEV before the lock.
- `priors.tsv`: the X prior per target (DEV GtoPdb majority, global DEV majority DECREASE where unseen or tied).
- `answers_lock.json`: digests of the script, `direction_task.py`, `priors.tsv`, `answers.tsv`, catalogue, needs and ChEMBL target file.

Pre-lock DEV observations (ChEMBL side only, no EVAL reference read):
1. Every X prior on the three directed needs' targets is DECREASE, so X = L on every directed row (0 of 72 rows differ). The WWOX contribution to accuracy on directed needs is therefore zero by construction, before any scoring.
2. **Method defect found on DEV**: ChEMBL group-level records spread one action to all components. The 26-component "Voltage-gated calcium channel" PROTEIN COMPLEX GROUP puts bepridil, terodiline, suloctidil and phloroglucinol (BLOCKER) and the gabapentinoids (MODULATOR, an alpha2delta ligand class) onto CACNA1G/H/I, so T proposes them for the T-type need and L v1 labels the blockers compatible. Minimal fix to the L rule only (`L_v2`): abstain (`group_record_mostly_outside_module_targets`) when every ChEMBL record that reaches the need has fewer than half of its components among the module's intervention targets (all needs). A first version that used the single need's targets wrongly abstained on the T-type family record (3 components) for the seizure need, which lists only CACNA1G; it was replaced before the lock. v2 changes 8 rows (4 compounds × 2 needs), all CACNA1G/H/I. Run 1 (registered rule v1) is the primary result; run 2 (v2) is reported as a separate, dated, labelled run.
