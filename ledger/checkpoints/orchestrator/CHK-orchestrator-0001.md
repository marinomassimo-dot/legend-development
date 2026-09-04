# CHK-orchestrator-0001 — TASK-0B-GUARD52, measured before it is repaired

Recorded 2026-09-04 at HEAD `4ec79ce`. This is a measurement checkpoint, not a repair:
the task is left open and claimed. It exists because the numbers below decay and because
two of them contradict the brief they came from — and a contradiction that lives only in a
transcript is a contradiction the next actor re-discovers from scratch.

## 1 · The population is 146, not 52

The task was dispatched as "the guard rebuilt against the 52 cases". The instrument
enumerates a different number, and it enumerates the same number at every revision:

```
$ python3 framework/scripts/hostile_corpus.py --revision <rev>
rev      cases   BYPASSES(ALLOW)   controls wrongly refused
main     146     96                0
rev7     146     — (146 of 146 not attributable)
rev8     146     — (146 of 146 not attributable)
rev9     146     58                4
rev10    146     37                0
rev11    146     2                 0
rev12    146     0                 0
```

No revision has 52 cases. `52` appears nowhere in the guard, the corpus or the battery;
the only two hits in the repository are in a WWOX evidence crosswalk and are a different
population entirely. Either `52` names a subset nobody has written down, or it is a figure
that decayed. **It is not adopted here.** Measuring against a denominator the instrument
does not produce is how a negative gets published with the wrong scope, and this repository
has done that before.

## 2 · At REV12 the corpus is already clean, so the corpus is not where the defects are

`0` bypasses and `0` controls wrongly refused across all 146 shapes. That is a PASS
sentence, and every clause of it has to be probed rather than believed: it says the guard
answers correctly on the 146 shapes **somebody thought to write down**. All four defects
named in the task are outside that set — none of them is a corpus case, and none of them
would move the bypass count by a single unit.

## 3 · The four named defects, measured

| # | Claim | Measured | How |
|---|---|---|---|
| 1 | fail-closed if the hook dies | NOT MEASURED here | needs a harness-level fault injection, not a policy call |
| 2 | hook registered on `Write`/`Edit` | **CONFIRMED ABSENT** | `.claude/settings.json` declares exactly one `PreToolUse` entry, `matcher='Bash'` |
| 3 | false refusal of `git worktree add` | **CONFIRMED, and it is dead code — not a policy** | below |
| 4 | codex/claude token | NOT MEASURED here | |

### 3.2 · Only the Bash channel is guarded

```
PreToolUse: matcher='Bash' -> python3 "$CLAUDE_PROJECT_DIR/scripts/guard_bash_command.py"
```

One entry, one matcher. A `Write` or `Edit` aimed at a peer worktree is never evaluated.
This is a property of the REGISTRATION, not of `guard_policy.py`, which is why no amount of
corpus work reaches it: the corpus feeds Bash command lines to a policy that would answer
them correctly.

### 3.3 · `git worktree add` — the branch that would allow it cannot be reached

`guard_policy.py:3086` holds

```python
elif sub == "worktree" and second == "add":
    findings.append(Finding("FILE_WRITE", "git worktree add", ...))
```

and it never runs. Twenty lines above, at `:3078`:

```python
if sub in GIT_SUB_READ:
    if second in GIT_SUB_READ[sub]:
        return
elif sub in ("branch", "tag"):
    ...
elif sub == "worktree" and second == "add":
```

`worktree` **is** a key of `GIT_SUB_READ` (`{"list"}`), so for `git worktree add` the outer
`if` matches, the inner `second in {"list"}` fails, nothing returns — and because the outer
`if` already matched, the entire `elif` chain below it is skipped. Control falls through to
the generic ref handling and the command is refused as a ref mutation.

Confirmed against behaviour and not only by reading, because absent logic and unreachable
logic produce identical evidence from a failing case and have opposite repairs. The live
denial is:

```
$ git worktree add ../legend-scientist-a -b scientist-a
DENY | A command that moves git refs or rewrites history is blocked.
      DECISION_CODE=REF_WRITE_REQUIRED
```

`REF_WRITE_REQUIRED`, not a `FILE_WRITE` judged by destination. The dead branch would have
produced the second. The verdict observed is the one that branch does **not** emit, which
is what makes this unreachability rather than a mis-scoped allowance.

**So the refusal is DECLARED DEBT, not policy.** `guard_policy.py:2658-2668` says so in its
own words: the wider question "is outside R1–R12 … and changing it here would be a
behaviour change nobody reviewed". §21d's operator decision of 2026-09-03 already grants
worktree provisioning to agents *"once the guard false refusal is fixed (0B)"* — so the
authority exists and only the mechanism is missing.

## 4 · Why this task is not closed in one pass

The repair is a guard change from DENY to a destination-judged ALLOW. That is exactly the
class the guard's own comment declines to make unreviewed, and it needs its own corpus
cases plus a blind Mirror round. Splitting it is an Orchestrator decision under §21d, not
an operator question: the four named defects have different owners, different surfaces and
different blast radii, and defect 2 is not in `guard_policy.py` at all.
