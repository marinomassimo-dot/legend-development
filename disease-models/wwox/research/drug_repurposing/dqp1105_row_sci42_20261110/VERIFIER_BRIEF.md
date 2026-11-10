# Brief — blind verifier, S5: the DQP-1105 registry row

You are an independent Scientist delegate of the Orchestrator of LEGEND (public edition). Task record `ledger/tasks/orchestrator/ORCH-SCI42-20261110.json` (sibling worktree; do not open it). Working tree `/home/desktop/legend-development/.claude/worktrees/sci42b` (absolute paths only). Claim actor label `dq-v`; claim each PMID you open (`paper_packet.py claim --pmid <N> --actor dq-v --note ORCH-SCI42-20261110`). Write only into `verify/`. Constraints: those of `disease-models/wwox/research/drug_repurposing/membrane_hypotheses_20261108/BRIEF_COMMON.md` (plain curl, default user agent only, never a browser identity; bot-check/403 recorded as unreachable and not retried by another route; no gates, lint, tests; no delegation; no e-mail, registration, spend; labels DATO / INFERENZA / IPOTESI; depth honesty).

## What you receive
`output/decisive.tsv` (P1–P8), `output/row_resolution.tsv`, `output/evidence.tsv`, `output/queries.tsv`, `output/receipts/`. Do **not** read `output/phase_note.md` or any README before your verdicts are written. The three registry rows are in `generation_it41_20261109/search_rows.tsv` (git grep DQP-1105) and described in `generation_it41_20261109/verify/VERDICTS.md` C2.

## Check (narrow; do not rebuild)
A. Each proposition P1–P8 against the source you open yourself: the PubMed abstract of 21807990 (and its Europe PMC record), and PMC10485906 (PMID 37566734) full text via Europe PMC (open access). SUPPORTED / PARTLY / NOT SUPPORTED / UNVERIFIABLE with depth. Digits and units digit by digit (nM against µM!).
B. The arithmetic and logic of P3, P6, P8 (inferences): is each valid from the stated premises, and is anything stated stronger than its premises? Is "unit error" the only reading that fits, or can a subunit mislabel or a different assay explain the registry numbers? Say what each reading predicts.
C. Own measurement versus citation: is the 7.0 and 2.7 µM in 37566734 clearly a citation of 21807990, and is the Table 2 value the authors' own measurement with the stated system?
D. Re-run the absence claims: the registry set versus the abstract, "no GluN2B value in 37566734", "ChEMBL has no document for 21807990", and the unreachability of the Acker full text (record the route only; no evasion, one plain attempt at most).
E. Evidence rows: quotes verbatim ≤25 words, each carrying its proposition (checked, correct, defective); spot-check the receipts' fingerprints and section lists.
F. The classification: is "unresolved, with a strong unit-error inference" what the evidence supports, and is the comparator statement (exclusion rather than GluN2B comparator) stated no stronger than the abstract allows?

Write `verify/audit.md` with verdicts, corrections (file, row, wording), and what you could not reach. Final message: counts, substantive errors, whether the outcome stands.
