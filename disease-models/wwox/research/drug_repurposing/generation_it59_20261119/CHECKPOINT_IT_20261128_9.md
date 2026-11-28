# Checkpoint IT35 (session 1c914d1b), written 2026-11-28 at about 330k context (measured: session_model_census peak 330565)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by IT35 (verified BOUND), effort read back high. Read this file only (`_8` is IT34's, done). Codex is never contacted. I told ADV "about 215k" in one message by mistake; the measured figure is 330k (correct it, state measured numbers only).

## Done
* **INV-06 Crawford sentence applied** (both TSVs, ranking.json, titles, view trio, i18n collect): landed `80f76390f` (gate PASS). Suites: investigations 52, ranking 74, view 241, `view check` current. IT34's self-evaluation/scout/takeaways file landed in the same push: `research/session_evaluations/self_eval_orchestrator_it34_20261128.md`.
* **ADV-325 GSK3 census (SCI, second-read)**: judged, no register or working-model edit (decision unchanged: the same-animal phospho-substrate panel stays a new lab observation; pT181 pointer declined with a reopening trigger). Sent to ADV.
* **Dream pass (ADV)**: population marker vs functional phenotype kept only as "amplitude/area and velocity can move apart" (Crawford EAE N1 amplitude ratio about 0.5-0.6 vs velocity ln -0.074; cuprizone PMID 31140740 velocity under the frozen 0.05); "Wwox N1 half-width" has no source; already consumed by INV-06 next_test; ADV accepted.
* **ADV-328 (my pick, registered by ADV)**: landed `6794836c8`; `meta/meta_gaba_paradox_current.md` line 23 reworded; folder `advisor_pilot_20261113/brainstorm_20261116/adv328_metabolic_confound_conditional_alleles_it_20261128/` (PREREG sha256 b0d32c78b9c7e18b9885194277cb9a76de854892279aa7c60fb0ffa97edd1a47, census, `DELEGATE1_...`, `RESULT_ADV328_IT_20261128.md`, `FINAL_LINE23_IT35_20261128.md`). Result sent to ADV with the cell-by-cell comparison against HE's ADV-329 table (identical RNA-seq cells; File013 is 7 v 7 pooled knockout lines, HE left it "not stated").
* **Rates with denominators:** round 2 MUST CHANGE 3 of 15 (Brain 1 of 7, EMBO 2 of 8); round 3 on repaired clauses 3 of 11 (Brain 2 of 6, EMBO 1 of 5). The final E7 repair (delegate's own wording) was not re-read.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | CI | run 2897 (`36d9289646ade5d630904f87b90ecaa45a68740a`, HE's i18n test fix) and run 2900 (`80f76390f19c06e51735f84216c4dc9c6e798c04`, INV-06 landing) were in progress at 14:40Z; runs 2883, 2884, 2888, 2890, 2891 are red only on `test_repurposing_view_i18n.py` (old test defect, fixed by HE). Also read the run of `6794836c8`. `framework/scripts/ci_runs.py status <full sha>`; a red: annotations at `api.github.com/repos/marinomassimo-dot/legend-development/check-runs/<job id>/annotations` |
| 2 | ADV-328 follow-ups (ADV's call) | RP-019 design requirement is ADV's row (text sent); dated pointers from `mechanism_intervention_map.md:148`, `wwox_independent_downstream_rescue_20260922.md:420`, `superior_node_search_20260922.md:167`, `PV_REPORTS_TABLE.tsv`; ADV-074 glucose-axis note says Appendix S1C/D "NOT held" but `files/supplement/PMID34747138_r2/EMMM-13-e14599-s001.pdf` has been held since 2026-10-19 (owner SCI) |
| 3 | ADV-286 dates | C1 re-check 2026-12-05 (poster); C2 not before 2026-12-06; UNRESOLVED 2026-12-12 if no printed poster date |
| 4 | Owed text of this window | self-evaluation, capability scout and takeaways for IT35 (IT34's are written) |
| 5 | Not applied by IT | CLAIM 047 bound (1); tCAG "maximum 5.8 percent" vs plot about 3.1; PMID 42422765 (Obeid 2026) not opened by standing instruction |

## Rules and traps (new this window)
* A suite missing from `.github/workflows/*.yml` can still be in CI: the workflow calls `scripts/run_release_regressions.py`. I said "not in the gate" and had to correct it (memory `it35-pitfalls`).
* An absent artefact is often misplaced: ADV-074 called the EMBO Appendix "NOT held" 30 days after it was copied in.
* First reading of a supplementary table can be wrong: I took File013 for a systemic-null table; the blind read showed three pooled knockout lines.
* Repairs carry new errors: round-3 repaired clauses 3 of 11 MUST CHANGE; a P9 seizure onset belongs to S-KO only; "no marker data" was too wide (O-KO has MBP staining).
* The frozen rule did not say whether a bulk transcript counts as a marker read; report both readings, pick neither.
* Delegates (sonnet 5.5, effort HIGH stated) resumed by SendMessage keep their sources: cheap clause rounds. `openpyxl` is not installed: `$CLAUDE_JOB_DIR/tmp/xl.py` style zip reader works.
* Measure context with `session_model_census.py --json --dir <project folder>` before stating it to a peer.

## Peers at writing
ADV a5e6f2ad, SCI 7e0f7b15 (re-run ListAgents), HE 4441b7bf. Worktree `it_35_20261128`, branch `task/it35-inv06` (landed; main is the base). Disk 12 GB free at the last look.
