# REPRODUCE: the commands that reproduce the 2026-11-16 programme's numbers from a clean checkout (HE; non-canonical)

Written for: the operator, or a laboratory, who wants to check the numbers without asking us. Python 3 only, no network, no key, no spend; every command runs from the repository root and finishes in seconds unless noted. Let `B=disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116` and `D=disease-models/wwox/research/drug_repurposing`. **Verified by HE at commit b007645ecb9d on 2026-11-16: every "expect" below was observed.** Where a result depends on something that is not in git, it says so.

## 1 · The two rules (what was fixed before any cell)
`sha256sum $B/rule.json $B/rule_v2.json` — expect `679a60894100d26bf4e550e2f49a888e39b8451dfbf428c2157f8b0cb2d94982` (v1) and `2cb4a908002aae48c6d4cc68baa9f8451e4bbb287fe6f47b4ccd6f7c5785f112` (v2). The generator refuses to run when the digest differs (`--expect-rule-sha256`).

## 2 · The generator, v1 and v2
* v2 on SCI's filled matrix: `python3 framework/scripts/aed_matrix.py score $D/matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv $B/rule_v2.json --expect-rule-sha256 2cb4a908002aae48c6d4cc68baa9f8451e4bbb287fe6f47b4ccd6f7c5785f112 --out /tmp/v2.tsv` then `cmp /tmp/v2.tsv $D/matrix_v2_cells_sci_20261116/output/scores_v2.tsv` — expect no output (byte-identical); run it twice and compare the two files: identical.
* v1 on SCI's frozen cells: the same command with `$D/aed_matrix_sci_20261116/output/cells_form.tsv`, `$B/rule.json`, the v1 digest, then `cmp` with `$D/aed_matrix_sci_20261116/output/rerun_frozen_scores.tsv` — expect identical. `official_scores.tsv` in that folder was written by the generator as it stood at the freeze (commit 094dd8c86), before the set-stability and origin-collapsed columns existed, so it differs from a run today by those columns; that is the version, not the rule.
* The tests pin all of this: `python3 framework/scripts/test_aed_matrix.py` — expect `Ran 70 tests ... OK` (a v1 output digest pinned from before R1-R3, both rule digests, a double run on the filled v2 matrix equal to the committed scores).

## 3 · The scoring and its cross-check
* IT's scoring: `python3 $B/it_scoring_20261116/score_class_pairs.py > /tmp/it.txt; cmp /tmp/it.txt $B/it_scoring_20261116/result_main.txt` — expect identical (reads only the sealed extraction, sha256 `9defc6540794cd5a3b97e07a2d5f6e69d8a88b111b1f21d2b7bab937967f95c1`; `sha256sum $B/it_extractor_20261116/sealed/extraction.tsv`).
* HE's independent cross-check: `python3 $B/he_crosscheck_20261116/crosscheck_it_scoring.py | diff - $B/he_crosscheck_20261116/crosscheck_result.txt` — expect no difference; its VERDICT line says the two computations agree, and its last section gives the like-for-like margin over the PTZ baseline (0.00 on the 7 shared pairs). It re-derives the counts from the sealed table, reads the frozen predictions from SCI's freeze commit `f5b71a3f4` with `git show`, and uses the generator's `compare` arithmetic (`python3 framework/scripts/aed_matrix.py compare PRED.tsv COUNTS.tsv`).
* Baseline (ii): `python3 $B/baseline_ii_he_20261116/baseline_ii_frequency.py $B/it_a1_feasibility_20261116/census.tsv /tmp/b2.tsv; cmp /tmp/b2.tsv $B/baseline_ii_he_20261116/baseline_ii.tsv` — expect identical.

## 4 · Order of events: the prediction ledger and the guard
* `python3 framework/scripts/prediction_ledger.py check $B/prediction_ledger.tsv | tail -1` — at the time of writing `rows 172; violations 84; order unknown=167, yes=5` (a violation is a limit git can show, e.g. predictor equals scorer; the count moves as rows are added). `yes=5` are SCI-P010-F1..F5: the freeze commit precedes the sealed table's commit.
* The guard, run after the fact on the sealed table: `python3 framework/scripts/prediction_ledger.py guard $B/prediction_ledger.tsv --outcome $B/it_extractor_20261116/sealed/extraction.tsv --require $B/rule.json=679a60894100d26bf4e550e2f49a888e39b8451dfbf428c2157f8b0cb2d94982 --require $D/aed_matrix_sci_20261116/FREEZE_PREDICTIONS.md --require $B/baseline_ii_he_20261116/baseline_ii.tsv` — expect a line starting `OUTCOME_MAY_OPEN:`; any `OUTCOME_REFUSED:` line is a stop.
* The candidate sweep: `python3 framework/scripts/prediction_ledger.py sweep | head -1` lists the files with frozen predictions (152 candidate files when first run; it grows with the repository).

## 5 · The third method (signatures)
`python3 $B/signature_triangulation_he_20261116/signature_ranking.py && python3 $B/signature_triangulation_he_20261116/triangulate.py && git status --short $B/signature_triangulation_he_20261116` — expect no change to any committed file. Held tables only; the frozen ranking is `FREEZE_BEFORE_COMPARISON.md` (commit `817ffe1c4`).

## 6 · The suites and what CI says
`python3 framework/scripts/test_prediction_ledger.py` (31 tests), `python3 framework/scripts/test_hypothesis_package.py`, `python3 scripts/test_release_surface.py`, `python3 scripts/test_tool_routing.py` — expect OK. The public publication gate: `python3 scripts/public_release_gate.py` (about 6 minutes). CI per commit: `python3 framework/scripts/ci_runs.py status <full 40-digit SHA>`.

## 7 · What cannot be reproduced from git alone
* **Cost** (`$B/programme_cost_he_20261116/PROGRAMME_COST.md`): read from session and delegate transcripts that are not in the repository; `programme_cost.py` needs the operator's transcripts directory. The figures are as measured at the time.
* **The delegates' outputs** (the extractor, the judge runs, arms A and B) are committed as files; re-running a delegate would give a different text. What is checkable is that the committed tables hash to the digests written before the key or the outcome was opened (`FREEZE.md`, `SEAL.sha256`, `JUDGE_SETUP.md`, `SETUP_1B.md`).
* **Who read what** and model memory of a published paper are declarations; the ledger says which rows carry them.
