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
