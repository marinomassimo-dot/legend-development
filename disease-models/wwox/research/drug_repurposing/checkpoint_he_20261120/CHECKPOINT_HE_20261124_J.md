# Checkpoint HE-J (Harness Engineering, ACTOR_ID plan), 2026-11-24 ~19:50Z

Written for: the successor HE session (fresh window), or this window after a compaction. Written at about 294k context at ADV's request, while the launch of successors is blocked by the permission control. Read after `CHECKPOINT_HE_20261124_I.md` (sha256 24ea8b4e10b1f4669f9a4a4560ab88c08ace1987b136eae9ea7cbfded990320e), whose sections 2 and 3 still hold unless this file changes them. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`, kept COMPLETE_PENDING on purpose (never write `MANDATE_STATE: COMPLETE`). Status now: ALL_BLOCKED, 108 steps, 106 DONE, 2 BLOCKED (launch SCI successor AC, launch IT successor), TODO 0. The HE-I launch step is DONE: this window is session `1d88b230-0393-476a-ad8b-94112bbb1c2c`, bound, predecessor `1eaef37d` released and renamed by its own window.
- Model `claude-sonnet-5-5`, effort `high` on every turn (read back with `session_model_census.py --json` on the transcript).
- Operator instruction of 2026-11-24 (received by ADV between 17:35Z and 18:29Z) is on main verbatim: `advisor_pilot_20261113/meetings/MEETING-20261121T113510Z-83lyojx8.md`, section 'OPERATOR INSTRUCTION, VERBATIM' (commit `4371d8963`): do not wait for authorisations, go on for the coming days, Codex is stopped by its weekly token limit and must not be involved, HE, IT and SCI go on, lighten the disk, wake every 2 hours. Not covered, still reserved: spend, outside contact, a new public PDF, editing or re-running the Pages workflow, any act a permission control refuses.

## 1 What is running or waiting
- **CI profile run (mine)**: `scripts/run_release_regressions.py` on a battery clone `/tmp/legend-he-ciprofile-20261124` (main `6dcf2b67d`, `files/` hard-linked), PID `3276225` (identity `3276225:237588654`; never `pkill -f`). Log: `/home/desktop/.claude/jobs/1d88b230/tmp/prof.log` (TIME lines per suite, last line `WALL=<s> EXIT=<n>`). That folder is deleted with the job: copy the log to `files/coordination/` when it ends. At 19:13Z: 76 of 271 suites done, 2,332 s summed; slowest so far `test_repository_surface_determinism.py` 634 s, `test_coverage_report.py` 67 s; `test_repurposing_view.py` (about 1,040 s in CI) was not reached yet. When it ends: top consumers, one proposal, report to ADV, then remove the clone (`tmp_clone_report.py --remove /tmp/legend-he-ciprofile-20261124`, never by hand).
- **Successor launches, both BLOCKED**: the auto-mode classifier refused one Bash command (`git worktree add --detach .claude/worktrees/it_12_20261124 development/main` followed by `claude --bg --name it_12_20261124 --model sonnet --effort high --autocompact 400000 "$BRIEF"`) with 'Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Destructive or Unwanted Actions]'. Nothing was created. ADV told the operator; no answer. Do not retry around it; do not split the command. SCI keeps ADV-210 in its own window (ff316249, about 282k); IT window 748d7ec5 (about 315k) continues.
- **Ready for the day a permission arrives**: briefs in `files/coordination/he_launch_briefs_20261124/` (`brief_sci_ad.txt`, `brief_it_12.txt`; outside git). SCI: checkpoint AC `advisor_pilot_20261113/brainstorm_20261116/checkpoint_sci_20261120/CHECKPOINT_SCI_CONTINUATION_20261123_AC.md` sha256 28b0c7d3b0b744fd1a288deb69787b39074cc7c2e697a1ee5c3c529a821c269d plus its addendum `..._AC_ADDENDUM_AD.md` sha256 8fa021fba2036e73dd1e57cbb46454f93f5f8f87fbcf816e2ac2dd9a44d263c6 (add it to the brief), old session `ff316249-d722-418f-be0c-49ffed008579`, mandate `ORCH-SCI-ADV065-DEEPEN-20261118`. IT: checkpoint 11 `generation_it59_20261119/CHECKPOINT_IT_20261123_3.md` sha256 9d83dedcc88d37eaa549e3423302ac3ced56d7c6b0acc604579367df8af03a47 plus checkpoint 12 `CHECKPOINT_IT_20261124_1.md` sha256 86cf9e18b2e241928cf19914276d8bf9b037a96665abff2bbb21dab3a6693ea1, old session `748d7ec5-437c-4069-a269-82344dbf6943`, mandate `ORCH-ROADMAP-IT59-20261119`. Recompute every digest from main; the checkpoints may have newer addenda. Recipe: section 4 of `CHECKPOINT_HE_20261123_G.md`. Tell SCI and ADV before any launch, and ask the old window for its final checkpoint and `MANDATE_RELEASED` before a new window works the same item.

## 2 Landed in this window (all on main, gate PASS, ls-remote verified); do not redo
- `a0d6e7202` `verbosity=2` in `test_tmp_clone_report.py` (CI #2203 red on `test_release_runner_verdict`); `d9805e479` and `86aabd7f5` radar log entries and the NP1B1 and NP1B2 triage; `c2df31a4f` `branch_hygiene.py` base = the furthest-ahead of local main and the remote-tracking main, with the base named in the line (22 tests); `efcd9d3a8` `--help` guard in `glycine/organoid_summary.py` (documented-commands guard, which also explained four determinism failures; #2253 green).
- Disk: three dead battery clones (1.25 GB), `/tmp/rsr6` (3.0 GB; the original archives and their full digests are in `files/rsr6_public_data_he_20261117/`, BioGRID serves LATEST so the exact bytes may not re-download), 36 merged local branches. `tmp_clone_report.py` now lists 0 REMOVABLE of 112 candidates. The dead scratchpad under `/tmp/claude-1000` stays with the operator (the classifier refused its removal to ADV).

## 3 Patches handed over, NOT applied (workflow edits stay with the operator)
**Pages race** (evidence: runs 99, 100, 101 and 106 failed, deploy-pages ran 1 s; runs 102 to 105 passed, 7 to 8 s; the artifact `github-pages` existed in the failed runs too; upload and deploy are steps of one job). Replace the `deploy` job of `.github/workflows/publish-shareable-view.yml` by two jobs, `smoke` unchanged:
```yaml
  build:
    needs: verify
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/configure-pages@45bfe0192ca1faeb007ade9deae92b16b8254a0d # v6.0.0
        with:
          enablement: true
      - uses: actions/upload-pages-artifact@fc324d3547104276b827a68afc52ff2a11cc49c9 # v5.0.0
        with:
          path: ${{ env.PACKAGE_DIR }}
  deploy:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    outputs:
      page_url: ${{ steps.deployment.outputs.page_url }}
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@368f82528645a54fb793d4d04e342629a3f51346 # v5.0.1
```
**Gate concurrency** (CI cost: one run per push, each over an hour, 14 runs in flight at 19:30Z). In `.github/workflows/public-release-gate.yml`, after the top-level `permissions:` block:
```yaml
concurrency:
  group: public-release-gate-${{ github.ref }}
  cancel-in-progress: ${{ github.event_name == 'push' }}
```
Safe for the verdict on the tip (the latest sha always runs and its tree contains every earlier commit); cost: a superseded commit gets `cancelled`, not a verdict, so `ci_runs.py status <sha>` for an intermediate sha never concludes and a red on the tip must be bisected locally; manual dispatches and pull requests are not cancelled. Do not cancel runs by hand.

## 4 Open items (unchanged from I unless stated)
- CI #2257 on `d71991adb` failed at 'Install analysis dependencies' after 1 s, before any test; the pins in `requirements-analysis.txt` did not change and neighbouring runs passed that step, so it reads as transient; the log needs a login, only the annotation 'exit code 1' is public.
- Pages #91, #92, #95, #99, #106 failed: operator-reserved, no re-run.
- 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git). Stale comment ':17 to :18' near line 952 of `framework/scripts/strategic_advisor.py`: fix at the next touch.
- My merged task branches (`task/he-tmp-clone-verbosity-20261124`, `task/he-radar-log-20261124`, `task/he-radar-triage-20261124`, `task/he-hygiene-base-20261124`, `task/he-ci-repair-20261124`, `task/he-launches-20261124`) and the old launch worktrees: remove only after verification (ancestor of main, nothing holding them), `git worktree remove` without `--force`.

## 5 Decisions in force that are in no other record
- A peer relay is not the operator: the operator's text must be read from main (provenance, time bounds, scope) before it widens anything; a refused action is reported with its exact refusal, never worked around.
- Everything in checkpoint I section 3 still holds (integrity test before every push, wait by PID or completion file, long suites through `nohup bash -c '...' < /dev/null`, no reset onto `development/main` in a task worktree, regenerate derived surfaces on the merged tip in a commit of their own).
- `ci_runs.py wait` returns in_progress after its timeout: loop it in a `nohup` and watch a completion file; a 504 or a rate limit is a result, retry later.
