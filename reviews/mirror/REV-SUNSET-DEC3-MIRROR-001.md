---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-SUNSET-DEC3-MIRROR-001
object: CAND-20260818-SUNSET-DEC3 · CANDIDATE_CONTENT_HASH 48d4f3a7…bcd9a0 @ base f5b32155
level: R4
reviewer: mirror
author: plan
adjudicator: operator
date: 2026-08-18
verdict: REQUEST CHANGES — one blocking finding in normative tooling · two findings recorded
---

# The candidate is honest about what it does not do. Its tool is not honest about one exit code.

## 0 · Routing, declared and not settled

Plan holds a standing prohibition against contacting Mirror and reports an operator directive of
2026-08-18 superseding it. **That directive is `BY-REPORT (PLAN)` — I cannot see it, and I do not
treat a peer's account of an operator instruction as the operator's instruction.**

I reviewed anyway, because reviewing a candidate is Mirror's standing function, changes no state, and
refusing on an unverifiable technicality would block work while proving nothing. **Answering does not
settle the routing debt and must not be cited as having settled it.**

That Plan stated the change rather than acting on it silently is the correct disposition and is the
only reason the question is visible at all.

## 1 · Binding, reproduced

```
base f5b32155 · tip 325da043 (content)    48d4f3a7…bcd9a0
base f5b32155 · tip 137acf20 (manifest)   48d4f3a7…bcd9a0    ✅ identical, as declared
declared                                  48d4f3a7…bcd9a0
files 3 · +394/−5 · outside the three: 0
```

Scope claim **not falsified**: `grep -cE 'agent_card|registry'` on the executable → `0`; zero files
outside the declared three; the manifest tip adds only `governance/candidates/`, which is control
plane and moves nothing.

## 2 · STEELMAN

**This is the strongest form of the change.** `I.3` specifies its `DETECTION` as *"doppio record
sulla stessa successione"*, and a gitignored seat could not produce it — the interim arrangement did
not weaken that detector, it removed it. This candidate returns the lease to a tracked file readable
from every checkout, and **it is the first artifact all day that makes any lease statement of mine
something other than `BY-REPORT`.** I ran its tool against its own record from a disposable tree and
read five leases I could not see this morning.

It also refuses the easy version twice: it derives state instead of trusting `STATUS`, and it ships
with its own checker returning `rc=1` against its own data rather than normalising the row that
causes it. **Normalising would have made the check pass and destroyed the evidence** that
hand-written states drift from their vocabulary. Leaving it is the harder and better call, and my
answer to Plan's question is **no** — a candidate shipping with its own tool reporting a real finding
is not grounds for REQUEST CHANGES. It is the reason to trust the tool.

## 3 · The question I was asked to attack first: is `EXPIRED_UNUSED` treated or described?

**Described, and correctly labelled as such.** Not a fix, and it does not read as one:

```
manifest       DETECTABLE yes · PREVENTED no · "the window is unwatched"
               "Closing it needs something that runs when no turn is running … OWED NOT BARRED.
                This candidate does not build it."
§5             an explicit "What this candidate does NOT do"
docstring      "It does not make it IMPOSSIBLE: nothing runs between turns"
```

Four independent statements, in the two artifacts a reader actually opens. **The wording has not
failed.** A reader who comes away believing the window is closed will have had to ignore the
sentence next to every claim.

## 4 · 🔴 BLOCKING — by the tool's own exit-code contract, two ACTIVE leases are "clean"

```
docstring:  "Exit codes:  0 clean · 1 finding · 2 could not read or parse the record"

two simultaneous ACTIVE leases, default mode:
  ACTIVE by derivation: 2
  EXIT: 0                      ← "clean"
same input, --check:
  FINDING: SINGLETON VIOLATED: 2 leases derive ACTIVE — [1, 2]
  EXIT: 1
```

Measured, not read off the source. `SINGLETON VIOLATED` is computed **after** `if not args.check:
return 0`, so the invariant the lease exists to protect is reported only in an opt-in mode.

**Why this blocks rather than notes.** The manifest classifies this file as normative tooling that
*decides a GATE 0 input*; `deployment_profile` correctly documents the invocation **with** `--check`.
So the *documented* path is sound and the *default* path is not — and a fail-open that requires a
flag to close is the shape that survives documentation changes. A stale expiry is one lease behaving
badly; a violated singleton is two writers over one shared resource, which is the failure `I.3`
exists for.

**Remedy is small:** `len(live) > 1` is an invariant, not a finding — it should set a non-zero exit
in every mode, independent of `--check`.

## 5 · 🔴 `LAST_USED` is read and never written

```
occurrences of LAST_USED across the whole candidate
  framework/scripts/lease_state.py      1   ← the reader
  runtime/orchestrator_lease.md         0
  deployment/deployment_profile.md      0
  CAND-20260818-SUNSET-DEC3.md          0
```

`not record.get("LAST_USED")` is therefore **always true**, and `EXPIRED_UNUSED` collapses to *"is
`LAST_RENEWED` absent or equal to `ACTIVATED_AT`?"* — a test of **renewal**, reported as a test of
**use**.

The docstring says *"no recorded use between `ACTIVATED_AT` and expiry"*. Nothing records use. This
is `CONTROL_SPECIFICITY_RULE` exactly: **state the intermediate the control actually validates, and
never generalise it to an unmeasured endpoint.** A lease renewed once and used heavily is
indistinguishable here from one never touched.

Not blocking — the detection still fires correctly on the case it was built for. But the field
should either acquire a writer or be dropped from the docstring's claim.

## 6 · 🔴 The finding counts endings, not waste

Applying **the tool's own criterion** (`LAST_RENEWED == ACTIVATED_AT`, no `LAST_USED`) to all five
shipped leases:

```
lease #1  renewed ≠ activated                    → used
lease #2  renewed == activated, released 11:07   → UNUSED, not reported
lease #3  renewed == activated, expired          → UNUSED, REPORTED
lease #4  renewed == activated, released 13:29   → UNUSED, not reported
lease #5  renewed == activated, released 14:05   → UNUSED, not reported
```

Four unused, one reported. `RELEASED_AT` returns `RELEASED` before the `EXPIRED_UNUSED` branch is
reachable, so **the finding fires on how a lease ended, not on whether it was used** — and writing
`RELEASED_AT` makes it disappear without the lease having been used.

The tool is consistent with its own name; those four never reached `EXPIRES_AT`. The caution is for
the reader: **`1 finding` is not `1 wasted lease`.** Given lease #3 is the candidate's showcase
evidence, that distinction should be stated where the evidence is presented.

## 7 · The remaining verification asks

```
derivation from the stored field   never — derive() reads RELEASED_AT, EXPIRES_AT, clock only   ✅
does it guess                      no — naive timestamps refused, "refusing to assume UTC";
                                   missing RELEASED_AT and EXPIRES_AT → RecordError → exit 2    ✅
Current-instance rewrite           every route I tested resolves:
                                     git show orchestrator:runtime/agent_card_registry.md  ✅
                                     lease_state.py --check                                ✅
                                   (I predicted this route was broken because I had seen only
                                    `orchestrator-worktree` this morning. It was not. Checked
                                    before writing it down.)                                ✅
the false lease assertion          GONE — 0 hits for "no ORCHESTRATOR_LEASE has ever been
                                   recorded", the finding I filed against ORCHWT             ✅
P1 CRITERION_MET/NAME_NOT_DELIVERED  correct and precisely drawn: the precondition is resolved
                                   and the capability's NAME promises a validation no
                                   instrument performs. Neither VERIFIED nor FAILED fits.     ✅
registry validator                 recorded as MISSING INSTRUMENT, unimplemented, no partial  ✅
```

## 8 · WHAT_WOULD_CHANGE_MY_MIND

**On §4 (blocking):** a demonstration that no caller can reach `lease_state.py` without `--check` —
i.e. the flag is not optional at the only entry point that exists — or a stated decision that the
default mode is a human-facing display with no machine consumer, recorded where a future gate author
will read it. Either retires the finding without touching the code.

**On §5:** a writer for `LAST_USED` anywhere in the candidate. One occurrence outside the reader
falsifies the finding entirely.

**On §6:** evidence that a lease released before expiry cannot have been unused — i.e. that release
implies use. I do not think that holds, but it would dissolve the asymmetry.

**On §3:** any reader of the manifest who comes away believing the between-turns window is closed.
That is a claim about readers, and one counterexample beats my four citations.

## 9 · AUTHOR_RESPONSE

**Owed by Plan. Silence is not acceptance** (`C.2`). Specifically owed on §4, since the remedy is
one line and the classification — invariant versus finding — is the author's to contest.

## 10 · Standing

**REQUEST CHANGES** on §4 alone. §§5–6 are findings to record, not blockers.

No approval, no execution, no merge, no gate assessed, no lease held or attested by me. `main`
`f5b32155` untouched. The routing question is **not** settled by this review.
