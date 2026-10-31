# IT11 P5: operations (publication preparation, old mandate, radar and continuity, licences, scouting) (scientist-f, 2026-10-30/31 UTC)

Branch `task/it11-p5ops`. Nothing reserved was executed: no push, no setting change, no Pages enablement, no contact, no spend; no e-mail or personal data sent anywhere. The page is **not published**. Not medical advice; reference-genotype level only.

## 1. Decisions first

| # | question | answer |
|---|---|---|
| A | Is publication of the view authorised? | **No.** Not recorded anywhere I could read; LEGEND_CORE 21d reserves any public surface other than a development push. The repository is already public; a Pages site would be a second surface. |
| A | What can be done from this host? | Git over SSH (key authenticates as the repository owner); **no GitHub token**; settings/Pages/permissions API answer 404/401 without one. So Pages cannot be enabled or the workflow dispatched from here (two click-level owner acts, plus authorising the push). |
| A | What is ready? | Package regenerated from main `d6ccf8d1`, static and dynamic audit PASS (0 violations), `package --check` current; text made true before and after publication; `noindex,nofollow` meta by default; workflow with a read-only post-deployment `smoke` job; activation patch; local rehearsal under `/legend-development/` (200s, same digest). Single request: `operator_request_publish_view_it11.md`. |
| A | URL and requirement | `https://marinomassimo-dot.github.io/legend-development/` (404 today); Pages source = GitHub Actions. |
| B | Is the old 10-hour mandate concluded? | **Yes.** COMPLETE, 5 of 5 steps DONE, hourly monitor says COMPLETE since 2026-10-30 15:37Z; closing commit on remote main. Nothing to decide. Its residual debts are real and are kept (28 UNVERIFIABLE figure triples, optional Mirror review): `mandate_and_continuity_it11.md`. |
| B | Does the monitor behave? | Yes (code, 85 tests OK, 653 events): distinguishes live/job/stop/concluded, never restarts COMPLETE, no repeated notification without change (only a deliberate probe repeated). **Not modified.** |
| C | Radar and hourly check | Hourly: 60 of 60 slots present to 2026-10-31 06:37Z, no gap above 1.5 h, 0 failures since the probe. Radar: ran 10-29, 10-30, 10-31 at 05:20Z, no errors; 10-28 unprovable. |
| C | **Urgent** | **IT11 is `UNKNOWN` in every hourly check since 23:37Z: no `MANDATE_BOUND: ORCH-ROADMAP-IT11-20261031` line exists, so the watch could not revive the session that was interrupted.** The session must emit that line. |
| D | Licences for new content | One gap: IT10 ChEMBL-derived tables (CC BY-SA 3.0) are not in `THIRD_PARTY_NOTICES.md`; ready text in `licences_it11.md` section 3. JUMP data CC0; openFDA CC0 with a reservation; quotations catalogued by paper licence. No repository-wide claim, no history change. |
| E | Scouting | Nothing external adopted. New WATCH: GSE298081 (WWOX-null HAP1 genome-wide CRISPR screen; crude check shows no outlier), a 2020 L1000 method benchmark (abstract only), UbiNet 2.0 (site down), brain turnover data (WWOX value not in the supplements). Mega-scale stability data rejected for Q230P by domain size. `scouting_it11.md`. |

## 2. What was checked

| check | result |
|---|---|
| `repurposing_view.py check` | full view current; shareable view stale before regeneration (expected after the text change), regenerated; both current |
| `package` / `package --check` | 13 files, "package is current" |
| `audit-shareable`, `audit-shareable --dynamic` | PASS, 0 violations, both files |
| `test_repurposing_view.py` (150 tests, 545 s) | 1 failure (an assertion of the old "LOCAL PREVIEW" wording), test updated to the new wording plus new assertions (no preview claim, one robots meta, none on the full view), re-run of that test OK; deployment class 4 tests OK; mandate tests 85 OK |
| `public_release_gate.py` | PASS, 0 BLOCK (a first run blocked on an address in my own notes; removed) |
| action pins | all four SHAs answer 200 and their tags still point to them |

## 3. Disclosures

* **Generator edits.** The coordinator asked not to edit generator logic without a reproduced defect. I had already changed, before that message: `repurposing_view.py` (one constant `SHAREABLE_ROBOTS_META` and one placeholder in the page head; the full view is byte-identical to before) and `repurposing_shareable_package.py` (wording only). Justification: the package text "local preview, not published" becomes false on deployment (defect shown in IT9 DEPLOY.md section 6), and the indexing choice was a task item. Tests added. If the Orchestrator prefers not to take them, `git checkout main -- framework/scripts/repurposing_view.py framework/scripts/repurposing_shareable_package.py framework/scripts/test_repurposing_view.py` and regenerate; the operator request then needs the meta decision re-stated.
* The view, shareable view, package and DEPLOY.md file table were regenerated here; the Orchestrator regenerates at the end and should re-run `package --check`.
* One process interruption occurred while I applied the activation patch for a test; I confirmed the working tree afterwards and reversed the patch (the workflow file is not in `.github/`).
* Non-blind: all scouting and licence reading was informed by the IT8 to IT10 files named above.
* GSE298081 check is a crude screen-level comparison with batch-unmatched controls (see `scouting_it11.md`); not a finding.

## 4. UNVERIFIED

SIGNOR, Enrichr, PubChem contributor terms, GEO disclaimer; whether SSH pushing a workflow file is accepted (not tested: no push); Pages settings and plan (no login); current per-manifest unverifiable figure count (`locator_audit.py --working-tree` not run); whether a dedicated second pass on the P4 card repairs exists; the 10-28 radar slot; WW-domain content of the mega-scale dataset; abstracts only for PMIDs 31774912 and 34677780.

## 5. Files

`operator_request_publish_view_it11.md`, `activate_workflow.patch`, `mandate_and_continuity_it11.md`, `continuity_it11.py` (executable, `--help` safe), `licences_it11.md`, `scouting_it11.md`, `gse298081_wwox_ko_screen_check.py`, `evidence/` (continuity output, Europe PMC licence fields, registry yaml copy, GSE298081 summary rows). Outside the package: `view/` (regenerated), `view/DEPLOY.md` (sections 6 and 7 text), `view/DEPLOY_pages_workflow.proposal.yml`, the two generator files and the view test file.

## 6. For the batch path

* Mandate record: P5 DONE with this README; do not reopen ORCH-REPURPOSING-10H (COMPLETE); carry the 28 UNVERIFIABLE figure triples as a locator-audit debt, and optionally a Mirror ex-post review. Add `MANDATE_BOUND: ORCH-ROADMAP-IT11-20261031` to the resumed session now.
* `THIRD_PARTY_NOTICES.md`: apply the three entries of `licences_it11.md` section 3 (ChEMBL release number to be copied from `service_log_identity_it10_p21.tsv`).
* After landing: regenerate (`run`, `run --source shareable`, `package`), `package --check`, `audit-shareable --dynamic`; push main before the operator dispatches anything.
* On operator "yes": `git apply activate_workflow.patch && git add .github/workflows/publish-shareable-view.yml`, commit with the patch, push.
* `scout_daily_pending_log.md` holds 2 TO_TRIAGE entries: `scout_daily.py --append-log` on a task branch.
* Receipts/ledger/registries: no receipt proposed (no full-text decisive premise was relied on). No scientific current file touched.
