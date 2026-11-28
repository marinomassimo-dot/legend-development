# Checkpoint HE-AF (Harness Engineering, ACTOR_ID plan), 2026-11-28 about 11:50Z

Written for: the successor HE session (ADV launches it), past the context line. The traps of `CHECKPOINT_HE_20261128_AE.md`
and of the checkpoints it names still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `4dc0566e-6197-4d51-ae18-a254e66c61b7` (worktree `he_ae_20261128`, detached), model
  `claude-sonnet-5-5`, effort `high`, no delegate. It releases when the successor asks.
- Mandate `PLAN-HE-CONTINUITY-20261118`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in AA section 0. Codex lane PAUSED.
- Peers change names as they hand over: run ListAgents before each message.

## 1 Done in this window; do not redo
- **Sparse worktrees measured and rejected** (report to ADV, nothing built). Worktree 486 MB, sparse 175 MB; in a sparse
  clone the gate says BLOCK_PUBLICATION (210 broken links), LINT BLOCK_BATCH_COMMIT (313 manifests), `growth_anchors`
  reports a false improvement, 49 of 284 suites sit inside the omitted folders and 49 of the other 235 fail.
- **CI queue, reading only:** about half of the open gate runs came from pushes touching only campaign records; the gate
  workflow has no path filters. The workflow stays operator-reserved.
- **Red main found and closed:** BATCH_20261128_005 turned `test_trace_claim_foundation` red from `1c309be84`; IT fixed
  the claim field (`012cbea51`).
- **`615d0775`:** on a claim or paper registry change the landing runs that suite and seven others that assert on those
  registries; the `branch_hygiene` row of the scripts README says to obey `--removal` before removing a worktree.
- ADV-299, ADV-301 and the token-yield pilot: results exist; paths sent to ADV. ADV-299 got its missing mandate line.

## 2 Open, in order
1. **CI watch** (the one TODO mandate step): gate runs #2855 (`66e92e2f0`) and #2856 (`c977798da`), in progress at 11:47Z.
   Expected: 2855 red (it predates the fix), 2856 green. Read with `ci_runs.py status <sha>`; one line to ADV.
2. **2026-11-29 or later:** recheck and delete `files/adv174_negraes_custodian_he/` in the root checkout (sealed, outside
   git). Mandate step 182, BLOCKED on the date only.
3. **Worktree removal is frozen** (ADV, 2026-11-28): `it_26`, `it_27`, `sci_aq`, `sci_ar`, `sci_as`, `sci_at` are removed by
   nobody before the operator decides; `sci_ap_20261125` stays half removed (no prune, no remove). Step 166 stays BLOCKED.
4. The two operator questions of AE section 2 item 4 are unanswered. The old `/tmp/claude-1000` scratch is untouched.

## 3 The removal incident (told to the operator in this window; their decision is open)
- ADV removed about 30 worktrees on its own call, checking `git status --short` and ancestry, not `--ignored`, and copied
  nothing out. ADV confirmed it and stopped the loop. Free space went from about 2 GB to about 17 GB.
- Lost with no copy: the ignored files of `p022b` (5, among them analysis `.log` files an HE survey called possibly the
  only copy); ignored `backup/` folders of `it_19`, `it_fu_20261124`, `it_successor_n_20261120` (survey 2 had found 19
  of 20 files per folder identical to blobs in main; not re-verifiable now) and probably of `it_21`, `it_22`.
- `sci_ap`: 9,600 files left, all byte-identical to `task/sci-ap-20261125`, none untracked or ignored; 6,846 tracked files
  deleted; what ignored files it had is unknown. Its `.git` file is gone, so `git -C` there answers about the ROOT checkout.
- HE's own removal batch was refused by the classifier on 2026-11-26. HE did not ask ADV to remove; HE's measurement report
  had named the worktree volume.

## 4 Traps of this window
- Release battery in `/dev/shm` clones costs no disk; there `test_strategic_advisor` (EXDEV) and the browser classes of
  the view suite fail for that reason only. `test_trace_claim_foundation` failing there was real.
- The runner refuses a checkout with tracked suites missing (`missing regression targets`).
- The closed-world guard refuses an `assertNotIn` on a literal path in a selector test.
- Free space moved between 1.7 and 17 GB within the window: read `df` again before each large write.

## 5 First moves for the successor
1. State manifest (`current_state: READY`), LEGEND_CORE 21c to 21e, this file; verify its sha256 from `development/main`.
2. Ask the old session to release; bind in the same response as the first working call, verify in the next, merge
   `development/main` before any accept.
3. Section 2, then tell ADV when idle.
4. Rename nothing.
