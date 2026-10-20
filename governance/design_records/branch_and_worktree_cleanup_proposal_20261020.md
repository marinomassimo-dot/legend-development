# Proposal — the two unlanded branches and the fifteen worktrees (2026-10-20)

> **Non-normative design record.** Written by the Orchestrator at the operator's request after the
> metabolic batch. **Both acts proposed here are reserved to the operator** (§21d: irreversible
> deletion of unique material; and `destructive-git-cleanup-permissions`: worktree removal needs
> written authorisation). Nothing in this file has been executed, except the one preparatory step
> in § 3, which only adds files. Measured on `main` `329bbaac`, pushed to `development`.

---

## 1 · Point one — `codex/drug-repurposing-bridge`

**What it is, measured.** One commit, `de15c4f0`, authored 2026-10-15 by `legend-desktop` on the
VPS. Eight files, **all harness**, no scientific current file, no registry, no ledger:

| File | Lines |
|---|---:|
| `framework/scripts/repurposing_bridge.py` | +118 |
| `framework/scripts/test_repurposing_bridge.py` | +127 |
| `docs/repurposing_bridge_20261015.md` | +122 |
| `.claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py` | +89 / −16 |
| `.claude/skills/legend-hypothesis-forge/references/evidence_bridge.md` | +48 |
| `.claude/skills/legend-hypothesis-forge/references/evidence_bridge_example.json` | +48 |
| `.claude/skills/legend-hypothesis-forge/SKILL.md` | +22 |
| `framework/scripts/README.md` | +1 |

**What it does.** Builds non-canonical candidate cards for drug repurposing from *explicitly
qualified* local assertions. Its own docstring states the discipline it keeps: no network, no
ranking, no source verification, no scientific promotion; direction is a comparison on the same
target, endpoint and context, never inferred from graph proximity; it carries the
`DATO / INFERENZA / IPOTESI / ESPANSIONE` tags and the reading-depth vocabulary. It is exactly the
kind of tool the therapeutic side of the model lacks.

**Verified in a throwaway worktree at that commit:** `test_repurposing_bridge.py` 5 tests OK;
`kg_thin_slice.py --help` runs; `test_tool_routing.py` OK; `test_release_surface.py` OK.

**Mergeability:** one conflict, `framework/scripts/README.md` — one added routing row against the
rows this batch added. The same shape resolved twice today by keeping both rows.

**One real gap:** `test_repurposing_bridge.py` is **not** enrolled in
`scripts/run_release_regressions.py`, so the battery does not run it. Landing it without enrolling
it would add an untested surface to the repository.

### Recommendation: LAND it, with the enrolment added in the same commit

Under §21e this is ordinary harness work at T0: no gate, no review precondition. §21e item 5 says a
`codex/*` branch is landed by its author at task end — the author here is a machine identity, not an
ACTOR_ID, so nobody is coming back for it; it has sat five days, which already makes it
`LAND_OVERDUE`. Retiring it instead would delete 559 lines of working, tested harness, and
**that** is the reserved act — landing is not.

What I would do on your word: merge `main` into the branch, keep both README rows, enrol the test in
the battery, run the battery on a fresh clone of the landed SHA, land with `task_close.py`, push.
Estimated one hour, mostly battery time.

**If you prefer not to land it,** the alternative is not deletion either: say so and I will record
it as deliberately abandoned with its content summarised, which is what §21e item 4 requires before
a branch may be retired — and the retirement itself stays yours.

---

## 2 · Point one, continued — `backup/vps-main-2026-09-25`

325 commits ahead of `main`, last commit 2026-09-17. Listed as `LAND_OVERDUE` by
`branch_hygiene.py`, which is the tool applying a rule written for task branches to a branch that
is not one.

**Recommendation: keep it, and say in the record why it is exempt.** Memory and the task record
both carry the fact that this branch plus a bundle are the only copy of the VPS line's history. It
is not a task branch and it must not be landed or retired. The useful, non-destructive move is a
one-line exemption so the weekly hygiene sweep stops reporting it as overdue — a `backup/*` prefix
exemption in `branch_hygiene.py`, which is harness and which I can do without asking. I have **not**
done it, because it changes what a tool reports and you may prefer the noisy reminder.

---

## 3 · Point two — the fifteen worktrees

**State, measured.** All fifteen are **clean** (no modified tracked file) and all are at
**ahead=0** — every branch they carried is landed on `main`. They are detached at their last HEAD,
which is what `task_close.py` leaves behind. Total **1.2 GB**; disk is 33 GB used of 193 GB, so
space is not pressing.

| Worktree | Scientist / role |
|---|---|
| `metab-g1-a`, `metab-g2-b`, `metab-g3-c`, `metab-g4-d` | wave 1 |
| `interv-h1-a`, `interv-h3-b`, `interv-h4-c`, `interv-h5-d` | wave 2 |
| `gold-b`, `held-c`, `debt-d` | wave 3 |
| `w4-b`, `w4-c`, `w4-d` | wave 4 |
| `plan-harness` | Harness Engineering |

**The question that decides whether removal is safe: would anything unique be lost?**

Checked by digest, not by assumption. 213 files live in the worktrees' gitignored `files/` trees.
Of their digests, **196 exist nowhere in the root `files/` tree** (which holds 4,466 files, 4,316
distinct digests). So the answer was *yes, something unique would be lost* — and then the question
is *what*:

- **All 196 are `paper_packet.py check` detail logs** (`files/check_runs/PMID*.json|.txt`, plus six
  under one worktree's `files_local_bak/`). They are the record of what each check examined.
- **No evidentiary artefact is unique to a worktree.** No full text, no figure, no page render, no
  supplement. That is consistent with the evidence-locality rule the Scientists followed: evidence
  went to the shared root `files/`, which is why every manifest validated against it.
- **No manifest, registry record or receipt names a path inside a worktree as an artefact.** Zero
  manifests reference `worktrees/`; the seven receipts that mention one do so in prose, naming the
  worktree a 2026-08 reading happened in (`lettore`, `lettore-b`, which no longer exist).

**Preparatory step already taken (additive only, nothing deleted).** All 196 files are copied into
the shared tree at `files/check_runs/from_worktrees/<worktree>__<path>`, 196 files, 868 KB, and
every one of the 196 digests is verified present there. `files/` is gitignored, so this adds nothing
to git and changes no tracked state. **After this step, removing the worktrees loses nothing.**

### Recommendation: remove all fifteen

Reasons, in order of weight:

1. **§21e item 3 says so**: *"A worktree whose chat is closed and whose branches are landed is
   removed."* All fifteen chats are closed — they were task-scoped subagents, not persistent chats,
   so the "keeps its worktree as a home" clause does not apply to them.
2. **They are stale copies of a moving repository.** Each holds a detached checkout from hours ago.
   The real risk is not disk, it is a future session reading a registry or a protocol from one of
   them and believing it. That failure has a precedent in this repository: a validator was run from
   a worktree and reported every artefact missing, which cost a micro-upgrade to diagnose.
3. **Re-creating one is cheap**: `git worktree add -b task/<id> <path> main`, seconds.
4. **Nothing unique is at stake**, per the digest check and § 3's preparatory step.

What I would do on your word: `git worktree remove` on each (git refuses a dirty one, and all are
clean), then `git worktree prune`, then re-run `branch_hygiene.py` and the battery. Minutes.

**A narrower option, if you want one kept:** keep `plan-harness` only. Harness Engineering is the
one role that will almost certainly be dispatched again soon, and its worktree is the only one whose
next task is foreseeable. The other fourteen go.

---

## 4 · What the operator pastes back

One line is enough for each point; both can be answered together, and either can be refused.

- **Point one:** `land codex/drug-repurposing-bridge` · or `abandon it, record the content` · or
  `leave it` (and, separately, `exempt backup/* in branch_hygiene` if you want the sweep quiet).
- **Point two:** `remove all fifteen worktrees` · or `remove all but plan-harness` · or
  `leave them`.

If you say nothing, nothing happens: both acts stay reserved, the preparatory copy in § 3 is
harmless either way, and the next weekly hygiene sweep will report the same two branches again.
