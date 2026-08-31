---
artifact: MIRROR REVIEW PACKAGE — independent hostile review requested
handoff_id: HANDOFF-20260830-RTBRIDGE10-MIRROR
candidate: CAND-20260829-RTBRIDGE10
from: plan
to: mirror
opened_by: nobody yet. Annex C.3 — a review is opened only through Orchestrator.
date: 2026-08-30
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
---

# Review package — `CAND-20260829-RTBRIDGE10`

## 0 · What is asked

An **independent hostile review** of the frozen revision-10 candidate. No verdict is
suggested here and none should be inferred from the way any section is written. Confirming
this candidate and refuting it are equally useful outcomes; the second is more useful if it
is true.

Revision 9 was green by its own instruments too.

## 1 · The object, exactly

```
CANDIDATE_ID     CAND-20260829-RTBRIDGE10
CANDIDATE_BRANCH plan-runtime-bridge-p00-rev10
BASE_SHA         278782c146a4253f027c5883c7749808dd4d563d   the revision-9 TIP
CANDIDATE_TIP    cb3b2c14598cbb144b41a71285911b64beda04ef   carries the manifest
CONTENT_TIP      da0fb7299195a6c16eee647e6b49e312351eafb6
CONTENT_HASH     e59cbf4849790dcddb641aa41fb5b0a0e5e8399e5ffb51c86029edde8eb69e93
FILES            25 in the CONTENT domain — 3 new, 22 modified
REVIEW UNITS     10, each one commit, each independently revertible
```

```bash
# reproduce the hash — it is INVARIANT between the two tips above, because every
# commit after da0fb72 touches only governance/candidates/, which P5.1 excludes
python3 governance/scripts/candidate_content_hash.py \
  --base 278782c146a4253f027c5883c7749808dd4d563d \
  --tip  da0fb7299195a6c16eee647e6b49e312351eafb6
python3 governance/scripts/candidate_content_hash.py \
  --base 278782c146a4253f027c5883c7749808dd4d563d \
  --tip  cb3b2c14598cbb144b41a71285911b64beda04ef

# read the object at source, without merging
git show plan-runtime-bridge-p00-rev10:governance/candidates/CAND-20260829-RTBRIDGE10.md
git show plan-runtime-bridge-p00-rev10:framework/protocols/runtime_bridge.md
git log --oneline 278782c..cb3b2c1
```

**Untouched, and verified untouched at freeze:** `main` at `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5`,
`plan-runtime-bridge-p00-rev9` at `278782c…`, whose content hash still reproduces as
`5c6ba023…899d7`. Nothing pushed. No Codex spend.

## 2 · Evidence locations

| What | Where |
|---|---|
| The candidate manifest | `governance/candidates/CAND-20260829-RTBRIDGE10.md` |
| The protocol | `framework/protocols/runtime_bridge.md` §§ 4.9–4.11, 5.0.3, 5.1, 5.2 |
| The session binding | `framework/scripts/session_binding.py` |
| The runtime-config scope | `framework/scripts/runtime_config.py` |
| Registration + probe preconditions | `framework/scripts/codex_registration.py` |
| The committed hostile corpus | `framework/scripts/hostile_corpus.py` — 88 cases |
| The mutation suite | `framework/scripts/mutate_guard_suite.py` — 91 operators |
| The ten suites | `framework/scripts/test_*.py`, `scripts/test_guard_bash_command.py` |

Every number below is reproducible from the tree. None is quoted from a session.

```bash
# the corpus, four engines, all reconstructed from COMMITTED objects, one denominator.
# --scene-dir must point OUTSIDE scratch space or rev7/rev8 report NOT ATTRIBUTABLE
python3 framework/scripts/hostile_corpus.py --scene-dir <a non-scratch dir> \
  --revision rev7 --revision rev8 --revision rev9 --revision rev10 \
  --engine-sha rev10=da0fb7299195a6c16eee647e6b49e312351eafb6

python3 framework/scripts/mutate_guard_suite.py          # 91 operators
python3 framework/scripts/guard_revision.py              # the census, read-only
python3 framework/scripts/codex_registration.py --routes
python3 framework/scripts/codex_registration.py --config .codex/config.toml
```

## 3 · What this candidate claims, so that each can be attacked

Stated as claims rather than as conclusions. Each is meant to be re-derived, not read.

**R1 · the assigned worktree is session-bound.** `EXECUTION_WORKDIR` resolves relative
operands; `SESSION_ASSIGNED_WORKTREE` decides the authority perimeter and is never read from
`workdir`, `cwd`, a `-C` operand or anything in `tool_input`. 32 cross-product cells through
the production adapter. The claim to attack is that the separation is complete — that no
model-writable field reaches the perimeter by any path, including ones neither of us has
enumerated.

**R2 · the live probe can identify the engine that answered.** Revision 9's discriminator is
byte-identical in the legacy blob. Revision 10 emits a structured trailer, and every one of
the 17 decision codes is asserted absent from that blob. The claim to attack is that the
discriminator cannot be produced by anything but a revision-10 engine, and that
`probe_receipt_state` cannot reach `DEMONSTRATED` from a refusal both engines produce.

**R3 · the registration is recorded as not deployable.** `.codex/config.toml` is
`UNANCHORED`; the Claude side is `RUNTIME_ANCHORED` and resolves to a REV10 engine. No route
is selected. The claim to attack is the route table, and in particular whether route D's
dependency on an unmeasured Codex anchor variable is stated correctly.

**R4–R12** each have a row in § 7 of the manifest naming the defect, the repair, the file,
the test and the residual limitation.

**Regression against REV9.** Clone-to-clone, same environment: the release-regression set is
identical, and the parity suite goes from 2 failures to 0 in a fresh clone. The claim to
attack is that no behaviour was loosened without being declared — the corpus asserts that a
case moving DENY → ALLOW must be a declared positive control, and four did.

**Development-main integration readiness = READY**, meaning candidate CODE readiness for the
development baseline and **not** runtime Codex write validation. Those are separate
questions and this candidate answers only the first.

**`LIVE_CODEX_PROBE_MEANINGFUL_NOW = NO`**, on three of its own seven preconditions.

## 4 · Where to attack first, from the author's own record

Not a list of what is wrong. A list of where this candidate has already been wrong once,
which is the best available evidence about where it is still wrong.

**Eight defects were found in this candidate by its author, and NOT ONE by reading the
code.** Every one came from running an instrument, or from reading an instrument against a
document that had just been rewritten:

```text
the corpus, first run after R1        two bypasses the R1 repair had itself opened
the corpus, reading its own output    five case ids colliding with revision-9 families
the parity suite in a fresh clone     a placeholder naming the actor's own tree
the anchor check, before a run        six mutations attacking nothing
the instrument, read after the doc    a probe receipt still deciding on one bit
the mutation run                      four survivors with four different causes
```

Five content hashes were superseded by that work. All five are recorded in the manifest.

🔴 **The single most useful thing to distrust: `G` — `NO_KNOWN_STRUCTURAL_BYPASS`.** What is
measured is that this candidate's own corpus reports 0 bypasses of 60 at object `da0fb72`,
and that 91 mutations died. What `G` asks is whether *no known structural bypass remains*,
and "known" is a property of who has looked. Revision 9 reported 0 bypasses of its own
corpus and then Mirror demonstrated six spellings of one it did not contain. That
precondition is declared by the caller, and the author is the wrong caller.

**Two more the author cannot settle.** Whether `RUNTIME_CONFIG`'s membership is the right
set rather than a set that happens to cover the three shapes measured — it is
equal-or-ancestor over a resolved surface, and a runtime that reads a fourth file is not
covered. And whether the strictness-only overlay in `classify_target` is genuinely monotone,
or whether some combination lowers a scope; the argument is written down and an argument is
not a proof.

## 5 · Emphases requested

- **R1–R12**, each re-derived rather than read;
- **regression against REV9**, including the clone-to-clone measurement, which is the only
  same-environment comparison available;
- **the hostile corpus** — its cases, its denominators, and whether its families close what
  Mirror demonstrated rather than only the thirteen command strings;
- **mutation and test quality**, including whether the 91 operators attack the guarantees or
  their spellings, and whether any is equivalent;
- **development-main integration readiness**, as candidate code readiness;
- **whether a live Codex probe is now mechanically meaningful** — this candidate says NO and
  names the three preconditions that fail.

## 6 · What is NOT asked

No merge, no push, no deployment, no Codex spend. This package requests a review and
nothing else; opening one is Orchestrator's under Annex C.3, and placing a registration
route is the operator's under `ARCHITECTURE_DECISION_REQUIRED`.

Two items are `TRUE_HUMAN_REQUIRED` and neither is prefilled: the spend-bearing probe, and
the on-disk executable bit on 19 paths that this candidate's own guard correctly refuses to
set at `REF_WRITE`.
