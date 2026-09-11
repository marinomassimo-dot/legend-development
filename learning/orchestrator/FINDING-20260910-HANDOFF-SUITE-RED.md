# Finding — `test_legend_handoff.py` is red, and was red before this session touched anything

**Recorded by:** `orchestrator`, 2026-09-10 · **Status:** OPEN, not repaired here · **Owner:** harness

## What was measured

`scripts/run_release_regressions.py` over the full inventory returns
`REGRESSION VERDICT: FAIL` with three suites red:

| Suite | Status |
|---|---|
| `framework/scripts/test_batch_queue.py` | **known red** — readings have outrun the paper-registry ratchet; only a `BATCH_COMMIT` clears it, and that is the operator's (`2026-09-09_actor_retrospective.md` § 6.4 I6) |
| `framework/scripts/test_surface_census.py` | **known red** — `files/` is gitignored by design, so a checkout holds none of the bytes its manifests fingerprint (§ 6.4 I4) |
| `framework/scripts/test_legend_handoff.py` | 🔴 **not on any known-red list**, 4 of 14 failing |

## It is not a regression from this session's work

Measured, not assumed. A detached worktree at `c1701be` — the tip as this session opened,
before the commit wrapper, the R4 trigger, the attribution census, the internal-edges
resolver, the receipt-writer fix or the dependency screen — fails **the same four cases**:

```
test_bundled_checked_out_branch_is_landed
test_negative_control_authority_never_silently_survives
test_negative_control_checked_out_branch_diverged
test_roundtrip_is_lossless
```

So §21e item 2's landing precondition — *no suite that was green before the change is red
after it* — holds for everything landed today. This red is inherited.

## Diagnosis, as far as it was taken

```
RESUME_FAIL ... refs restored: 5   dirty patches applied: 0
! dirty patch dirty/source.patch belongs to 21e794ce08a9 but destination HEAD is HEAD
```

`destination HEAD is HEAD` is the tell. At `legend_handoff.py:1185` the guard reads

```python
_, dest_head, _ = git_ok(into, "rev-parse", "HEAD")
```

and **discards the return code**. `git rev-parse HEAD` against an **unborn** HEAD exits
non-zero and echoes the unresolved argument — the literal string `HEAD` — on stdout. The
comparison on the next line therefore succeeds in the worst way: it compares a real commit
against the word `HEAD`, never matches, and refuses every dirty patch with a message that
names no actual commit.

🔴 **The message is wrong, and that is the smaller half.** The guard's purpose is real — a
patch applied to a destination sitting at a different commit is applied blind — and with an
unborn HEAD there is no checked-out content to apply to at all, so *refusing* is defensible.
What the failing test asserts is that the roundtrip should have **succeeded**, which means
the destination was expected to have HEAD at the restored commit. The refusal is then a
symptom: the resume restores 5 refs and leaves HEAD unborn. **Whether the defect is the
discarded return code, the un-set HEAD, or both, is not settled here** — that is the repair,
and it belongs to whoever takes it with the fixture in front of them.

## Why it matters more than a red counter

`legend_handoff.py` is the cross-host transport, and this repository moved hosts on
2026-09-09/10 — `/root/legend-development` to `/home/desktop/legend-development`. A red in
the tool that performs the move is not cosmetic, and `learning/orchestrator/VPS-LOSSLESS-PREFLIGHT-001.md`
documents a *different* handoff defect (`test_documented_commands.py` against flags
`cross_host_handoff.md` documents and the suite does not expose). This one is not that one
and appears in no record found by a repository-wide search.

## What a repair must show

- the four cases green, and a **mutation** that re-discards the `rev-parse` return code
  turning at least one of them red again — the discarded status is the kind of defect that
  a test can pass straight through, which is how it survived;
- a case where the destination HEAD is genuinely unborn, asserting the message names that
  condition rather than printing the word `HEAD` as if it were a commit;
- the release inventory re-run, with `test_batch_queue` and `test_surface_census` still red
  for their own declared reasons and nothing else new.

## Resolution

**Repaired by:** `plan` (Harness Engineering), `HARNESS-HANDOFF-001`, 2026-09-10 · **Status:** CLOSED.
The diagnosis above is left as written: it is the record of what was believed before the fixture
was run, and half of it was right.

### The settled diagnosis: (c) both — but not the (b) that was hypothesised

Measured with the fixture, git 2.43.0, no global git configuration, at `c1701be` and at `4840f72`:

1. **The unborn HEAD pre-existed `resume`; `resume` did not leave it.** The fixture built its
   bare "development remote" with `git init --bare` and no `-b main`. On a host without
   `init.defaultBranch` that remote's HEAD names a `master` nobody ever pushes; `git clone` of it
   prints *remote HEAD refers to nonexistent ref, unable to checkout* and the destination arrives
   on an unborn `master` with an empty tree. In the fixture `main` is published, so it is never
   bundled, so `resume` restored 5 refs and never had a reason to touch HEAD. The hypothesis
   "the resume restores 5 refs and leaves HEAD unborn" was therefore false as a statement about
   the tool and true as a statement about the destination.
2. **The discarded return code was real, at two sites** (`legend_handoff.py` old lines 1132 and
   1185). `git rev-parse HEAD` against an unborn HEAD exits non-zero *and echoes the word
   `HEAD`*; the guard kept the word and dropped the status, which is why the refusal named no
   commit. `worktree_state` (old line 209) already honoured its status and was not a third site.
3. All four reds trace to (1) through (2): the landing test's positive control saw `master`
   instead of `main`; the roundtrip and the authority test hit the mis-named refusal; the
   divergence control committed onto the unborn `master`, which created a **new root commit**,
   so the repo-identity gate fired ("foreign history") before the refusal it was asserting.

### The red was environment-dependent, in both directions

| `init.defaultBranch` | unmodified suite (`c1701be`) | repaired suite |
|---|---|---|
| unset — this host | 4 of 14 red | 16 of 16 green |
| `master` | 4 of 14 red | 16 of 16 green |
| `main` — the Mac the suite was written on | **14 of 14 green** | 16 of 16 green |

Not a git-version difference: git 2.43.0 and 2.50.1 both default `git init` to `master` unless
`init.defaultBranch` is set. The protocol's own re-derive command `test_legend_handoff.py --table`
crashed on this host from the same cause and runs again (14 fields compared, 0 mismatches).
Recorded in `cross_host_handoff.md` § 5.2 and limitation 10.

### The repair (commit named in the task JSON, `ledger/tasks/plan/HARNESS-HANDOFF-001.json`)

- `legend_handoff.py`: `head_commit()` uses `rev-parse --verify -q HEAD^{commit}` and returns
  `None` for an unborn HEAD; the dirty-patch guard refuses by name (`destination HEAD is UNBORN —
  branch 'main' has no commit and nothing is checked out`) and does not let
  `--apply-dirty-anywhere` force a patch onto no tree; the checked-out-branch landing treats an
  unborn HEAD as "nothing to discard" and lands the bundled tip there, while a destination with
  its own commit is still refused.
- `test_legend_handoff.py`: bare remote pinned `-b main`; `fresh_destination` refuses an unborn
  clone by name; the landing test asserts HEAD itself, not only the ref; two new cases —
  `test_negative_control_unborn_destination_head_is_named` and
  `test_unborn_destination_lands_bundled_checked_out_branch`.

### Mutation matrix (each mutation applied to a scratch copy, run, discarded)

| # | Mutation | Result |
|---|---|---|
| M1 | dirty-patch guard re-discards the `rev-parse` status | red: `unborn_destination_head_is_named` (message reads `destination HEAD is HEAD` again) |
| M2 | landing re-discards the status | red: `unborn_destination_lands_bundled_checked_out_branch` |
| M3 | landing always `reset --hard`, never refuses | red: `negative_control_checked_out_branch_diverged` — the control is not passing by accident |
| M4 | unborn guard names the condition but falls through to `git apply` | red: `unborn_destination_head_is_named` (`does not apply cleanly` appears) |
| M5 | fixture bare remote without `-b main`, `init.defaultBranch` unset | 7 errors, each naming "the fresh clone has an UNBORN HEAD"; the same mutant is 16/16 green under `init.defaultBranch=main` |

### Release battery after the repair

`test_batch_queue` and `test_surface_census` red for their declared reasons; `test_legend_handoff`
green; `scripts/test_locator_obligation_reaches_every_route.py` red **before and after** this work
(a peer's file, in flight this afternoon) — reported, not touched.
