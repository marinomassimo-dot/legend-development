# ADV-264 pre-registration: how many of the "no held artefact" studies were read? (SCI, 2026-11-25)

Written before any recount. Actor `orchestrator` (SCI). Hypothesis level; no spend, no contact, no network request is planned (a route test is a sample at the end, if time allows). Brief: `assignments/ADV-264.md`. Reads `disease-models/wwox/registries/fulltext_read_receipts.jsonl` of this tree (main at 58bbcb393 plus my two unlanded commits that add one receipt) and the held folders. Writes only under this folder. `coverage_report.md` and `reading_state.md` are not edited.

## Population
ADV-219's primary population, re-derived on the current ledger: studies whose **latest contemporaneous receipt** has depth `partial_fulltext_read`, with **no held artefact** by ADV-219's frozen match rule (`labelling_flags_adv219.py`, functions `load_ledger`, `index_files`, `match_files`, over `files/fulltext` and `files/deepening_downloads` of the root checkout). ADV-219 counted 1,077 primary, 575 held, 497 not held, 5 not assessable on its ledger snapshot; the ledger has moved, so the re-derived number is reported next to those. All studies of the population are examined if the SHA-256 index of `files/` is built in under 10 minutes; otherwise a stratified 120 (strata: DOI-keyed, PMID-keyed, preprint-keyed; seed 20261125).

## Classes (first match, one per study)
* **K1 earlier complete:** at least one receipt of the study has depth `complete_fulltext_read`.
* **K2 substantial partial:** no complete receipt; the union of its receipts' coverage marks `methods` and `results` both `read`.
* **K3 thin partial:** the rest of the partial population.
Second axis, bytes (independent of the class):
* **B1 found by digest:** the `source_fingerprint` of any of the study's receipts equals the SHA-256 of a file under `files/` of the root checkout or of any worktree `files/` (a misplaced or renamed copy).
* **B2 restorable by the documented tool:** a deepdive manifest of the study declares artefacts with digests, and `evidence_presence.py --pmid X --search <dir>` reports them recoverable (`--restore` is not run in this assignment; the list is proposed).
* **B3 no bytes found:** neither. These go to one list; the operator list is the subset with no open copy known (no network test unless time allows, then a sample).

## Counts to report (each by two independent computations, "two-hit")
1. Population size and the three classes K1, K2, K3.
2. Best-state depth over **all** ledger studies (best depth across every receipt of a study): complete, partial, `queried_not_full_read`, `abstract_only`, other; compared with ADV's cited 313, 1049 and 570 and with ADV-219's latest-receipt rule.
3. Corrected counts if the earlier complete receipts of K1 are counted: the change in best-state complete and in the partial figure.
4. B1, B2, B3 counts.
Two-hit rule: the first computation uses the ADV-219 code path (parsed JSON, key = PMID else DOI); the second re-reads the raw ledger lines with a different key rule (the event id) and a different counting method; a difference is stated and resolved, never averaged.

## Predictions (fixed now)
* K1 share of the not-held population: **0.08** (plausible 0.03 to 0.20). ADV-216 found 6 of 286 PAPER rows with an earlier complete receipt (0.02); the ledger-level population is larger and has more re-reads.
* B1 share: **at most 0.05**.
* Best-state complete count rises by **fewer than 5 percent** when K1 is counted (the union view already counts earlier receipts; only the latest-receipt rule hides them).
* At least one of the briefs' cited figures (313, 1049, 570) does not reproduce under my best-state definition because the sources count different units (registry records against ledger studies): **0.7**.

## Out of scope
No byte is restored; no network request for text; no claim file, no registry, no coverage report is edited. Corrected counts are proposals for HE or the regenerate step.
