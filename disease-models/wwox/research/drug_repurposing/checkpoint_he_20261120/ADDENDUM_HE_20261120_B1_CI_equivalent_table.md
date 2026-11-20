# Addendum B1 to checkpoint HE-B (HE successor, 2026-11-20): the CI-equivalent table of main 241a1f602 and the GitHub job steps

Reference-genotype class only; nothing here is medical advice; no personal data. Checkpoint B stays unedited; this file adds to it.

## The CI line (one line)
The CI red on main is exactly three repository-side test failures in one suite (`framework/scripts/test_repurposing_view.py`): the package-current test and two shareable-page name tests; the browser step is green on GitHub, so the three Chromium reds seen on the HE host are host-only.

## Evidence
- GitHub, public API, no login (jobs and check-run annotations): run #1649 (head 2d3e72b6, completed, failure) and the older red run #1638 (completed, failure). In both, job `release-gate` steps: `Browser startup and keyboard regression` = success; `Regression tests` = failure; `Upload regression log` = success; `Structural framework lint` = skipped; `Public release gate` = success. The workflow sets `CHROME_BIN=/usr/bin/google-chrome` (packaged Chrome), not the snap Chromium of the HE host.
- Annotations of both runs name the same one failing suite and the same three failing tests: `ShareableAudit.test_package_is_current_deterministic_and_self_describing` (list differs from empty), `ShareableAudit.test_prose_policy_pairs_names_status_and_paths_are_gone` ('tta-a2' found), `It21P7InvestigationsContext.test_live_conditional_rows_are_never_qualified_and_shareable_names_stay_out` ('tiratricol' found). Suite time 1,292 s (#1649) and 1,232 s (#1638).
- HE host, clean clone at 241a1f602 (`scripts/run_release_regressions.py`): 270 suites, 269 exit 0; the view suite run class by class gave 218 tests and 6 red: the same three plus `test_every_chain_node_can_be_selected_by_keyboard_and_shows_its_relations` in `BriefBrowser`, `CuratedBrowser` and `It7P7Browser` (page never ready in 60 s, "Page load failed: ERR_FILE_NOT_FOUND" in the snap Chromium 3593 log). Not run on the host: `RealViewports` (hangs there) and `ShareableAuditRendered`.
- Reading rule applied: a failed or missing read is never read as green; here every step conclusion was read from the API response, not inferred.

## Decisions in force (source ADV, 2026-11-20)
The names `tiratricol` and `tta-a2` are guard names: nobody rewords or loosens the tests (item 17). The package-current failure is the known stale package. Run #1650 and #1651 were still in progress when this was written.
