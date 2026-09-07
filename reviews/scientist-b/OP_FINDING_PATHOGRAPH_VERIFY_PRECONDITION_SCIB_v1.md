---
record: TOOLING FINDING — `pathograph.py --verify` has an unwritten precondition
id: OP_FINDING_PATHOGRAPH_VERIFY_PRECONDITION_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
requested_by: Orchestrator session legend-public-49 — *"Yes, record it — as a standalone note …
  Write it against the OBJECT — which invocations the precondition binds — not against the strings."*
status: NON-CANONICAL. **A record, not a repair.** No file was modified, no generator changed, no
  regeneration performed over any real path. Every run below wrote only into a session scratchpad.
not_a_defect_report: the committed harness is correct and passes. See §4.
---

# `--verify` compares a re-derivation carrying *your* argument strings against a file carrying the *original* ones

## 1 · The precondition, stated against the object

**`pathograph.py --verify` answers "has this file drifted from its sources?" only when it is invoked
with the same `--out` / `--export` argument *strings* that produced the file. Under any other
invocation it answers a different question, and answers it `DRIFT`.**

The precondition is a property of **invocations**, so it is stated as one. It does not decay when
written down, and it holds for any file this generator produces, at any path, in any checkout:

| Invocation shape | Answers "has the content drifted?" |
|---|---|
| Same argument strings that generated the file (relative constants, cwd = repo root) | **yes** |
| Same file, same content, **absolute** paths instead of relative | **no** — reports `DRIFT`, exit 1 |
| Re-derivation written to a scratch path, then compared | **no** — reports `DRIFT`, exit 1 |
| Any invocation from a different cwd such that the relative strings differ | **no** |

## 2 · Why — the mechanism, in one sentence

The generator **echoes the literal `--out` and `--export` argument strings into the header of the
file it writes**, inside that file's own regeneration-command block. `--verify` then re-derives and
compares whole files. So the argument strings are part of the compared content, and a comparison
that changes them reports a difference in the content.

## 3 · Measured, four invocations, one tool, one set of files

Run against the WWOX inventory and export, generator at sha256 `c59750d5…`:

| # | Invocation | Result |
|---|---|---|
| 1 | regenerate to scratch, compare export against the committed blob | **byte-identical** |
| 2 | regenerate to scratch, compare inventory against the committed blob | differs — **6 diff lines, all in the header's echoed paths** |
| 3 | `--verify`, absolute canonical paths | `VERIFY: DRIFT`, **exit 1** |
| 4 | `--verify`, the same scratch strings that generated the scratch file | `VERIFY: CURRENT`, **exit 0** |

Content-only comparison for #2, both files with the two echoed-path lines removed:

```
committed    225c9330cc8841bb1845d6d6502fc140220cdbade313ce8dc2bb05a58a34e37b
regenerated  225c9330cc8841bb1845d6d6502fc140220cdbade313ce8dc2bb05a58a34e37b
```

**Identical.** The canonical file has not drifted. #3 is a false positive and #4 is the control that
identifies the cause: change nothing but the argument strings and the verdict flips.

*(Independently reproduced by the Orchestrator, same two invocations, same content-only digest,
arrived at without seeing my figure.)*

## 4 · 🔴 This is NOT a defect in the commit that preserved the Pathograph

I nearly filed it as one and checked first.

- `framework/scripts/test_pathograph.py:422` — `test_the_generated_surfaces_have_not_drifted` invokes
  `--verify` with the **relative constants at `cwd=ROOT`**, which is exactly the invocation the
  header matches.
- `test_pathograph.py:431` — `test_verify_without_a_target_refuses_rather_than_passing`.
- 30 tests; the release battery runs the file and the CLI smoke test exercises the binary.

I replicated the test's exact invocation read-only: **`VERIFY: CURRENT`, exit 0.** The inventory
header's claim — *"A regression re-derives it and fails if this file has drifted"* — **is true.**

So the finding is **"`--verify` has a precondition nobody wrote down"**, not *"the wiring is broken"*.
Keeping the generator, its test and its wiring atomic was right, and this note does not undercut it.

## 5 · Why it is worth writing down rather than shrugging at

The cause is cosmetic. **The consequence is not**, and it is the whole reason this note exists:

> **The correct discipline for auditing a generated file is to regenerate it to a scratch path and
> diff — never over the original, which would destroy the evidence under examination. This
> generator defeats exactly that discipline, because the scratch path lands inside the output being
> compared.**

Two good practices, and following the second makes the first report a failure that is not there.
An auditor doing the careful thing gets `DRIFT` on a correct file, and may then either chase a
phantom or — much worse — "fix" a file that was right.

I hit it myself and read it as real drift for the length of one diff. The Orchestrator hit the same
`DRIFT` earlier the same day, diagnosed the cause correctly, and stopped at the cause without
reaching the consequence.

## 6 · The option space, named and NOT taken

The fix is one line and it is **not a Scientist's to make** — the dispatch's authority boundary
forbids Pathograph architecture changes, and the Orchestrator, who owns this lineage, has declined
it on the record for the same reason.

Named so the option exists, proposed as nothing:

1. Echo the **canonical relative paths** in the header regardless of what `--out` / `--export` were
   given.
2. Or omit the paths entirely and print the bare command.

Either makes `--verify` invocation-independent and makes the scratch-regeneration discipline work.

**Neither is adopted.** A finding that repairs itself before it has been reviewed stops being
evidence.

## 7 · Scope

**Establishes:** that `--verify`'s answer depends on its own argument strings; that the dependence
is caused by the generator echoing them into its output; and that the canonical WWOX inventory and
export have **not** drifted from their sources.

**Does not establish:** anything about any other generator in this repository. I measured one.
Whether the pattern recurs elsewhere is unmeasured and I do not assert it.

**Does not do:** repair anything, or touch any real path. All regeneration went to a session
scratchpad; `git status --porcelain` over `disease-models/wwox/analysis` and `framework/scripts` in
the shared checkout was empty after every run, checked each time.
