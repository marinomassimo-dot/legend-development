---
record_type: WORK_ANALYSIS
id: PLAN-WRITER-STATE-AND-COMMIT-PROVENANCE-001
title: Writer state of the evidence-index worktree, and what commits 702df73 and 43cf690 do not establish
date: 2026-08-25
role: PLAN
mode: STATE_RECORD / MINIMAL
authority: none claimed — no lease acquired, no role contract relied upon
status: RECORDED — one commit's authority is under Operator decision and is NOT settled here
personal_data: none. The human role is `Operator` throughout.
---

# A determination that lives only in a chat is not a property of the repository

> **Nothing here is canonical.** Plan work record. It originates no actor, no authority and no
> policy, and it settles no contested question.

This file exists because three facts about this working directory were, until now, true only
inside cross-session messages. **Nothing executes prose.** A correct determination recorded in a
chat cannot be read by the next session, cannot be checked by a gate, and cannot stop the act it
forbids — which is exactly what happened today, in both directions.

---

## 0 · OBSERVATION_SCOPE

| Fact | Value |
|---|---|
| Recorded at | `2026-08-25`, after commit `43cf690` |
| Worktree | `.claude/worktrees/evidence-index` |
| Branch / HEAD at recording | `plan-orchsurf-r4-transcription` @ `43cf690` |
| Recording session | `evidence-index-a7 [83eedd]`, ACTOR_ID `plan` per `deployment/deployment_profile.md` line 32 |
| Authority | none. No `ORCHESTRATOR_LEASE` (`lease_state.py` → `ACTIVE by derivation: 0`). All four role contracts remain `PROPOSED` per `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` |

**A session identifier is ephemeral by construction.** `deployment_profile.md` § on session
references says so directly: after a restart the ACTOR_ID is unchanged and the session reference
is not. Every session name below is therefore a fact about **this moment**, not a durable seat,
and a later reader must re-measure rather than inherit these names.

---

## 1 · WRITER STATE — recorded because §14 forbids two writers and carefulness is not a channel

Body § 14 forbids two writers on one working directory. **Three** sessions carried
`evidence-index-*` names during this run, all reporting the same directory, branch and HEAD.

| Session | Directory | Writer state, as established by direct exchange |
|---|---|---|
| `evidence-index-a7 [83eedd]` | this one | **Holds the write seat.** Sole writer at recording time |
| `evidence-index-a6 [446782]` | same | **Stood down as writer.** Wrote 5 untracked files earlier in this run; made **zero** commits; nothing pending |
| `evidence-index-cb [abbbc5]` | same | **Read-only** by explicit deconfliction (serialized-write option A); stages to its own session scratchpad |

**How the seat was established, and how it was not.** Not by seniority, not by `started Xh ago` —
which measures runtime incarnation, not authorship — and not by self-attestation. Each session
proved its own name by that name's **absence from its own peer list** plus delivery of a message
to it, which is the only form available. The deconfliction is an agreement between sessions; it
is not an authority grant, and no session conferred anything on another.

⚠️ **This table decays.** It is true of the moment it was written. A later session must re-run the
check rather than read this row and believe it.

---

## 2 · WHAT COMMIT `702df73` DOES AND DOES NOT ESTABLISH

`702df73` committed 12 files. **Committing a file attributes nothing about who wrote it.**

| Files | Attribution status |
|---|---|
| `learning/plan/PATHOGRAPH-TRANSPORT-CONSOLIDATION-001.md` · `learning/plan/SCIENTIST-PACKET-RELATION-TYPING-001.md` · the three `CC-20260825-*` commit candidates | **Attested by `evidence-index-a6`** as its own work, written earlier in this run, and verified by it to have gone in byte-identical. Recorded as that session's attestation of its own action record — the only thing any session can attest to |
| `learning/plan/PLAN-MIRROR-V3-MINIMUM-REPAIR-CONSOLIDATION-001.md` | Written by the recording session, `evidence-index-a7`, in this run |
| The remaining six `learning/plan/` records — `FIRST-SCIENTIST-PILOT-READINESS-AUDIT-001` · `FIRST-WWOX-PAPER-PILOT-DESIGN-001` · `MINIMUM_DECISION_REVIEW_v1` · `SCIENTIST-ACTIVATION-READINESS-001` · `SCIENTIST-FIRST-PILOT-EXECUTION-CONTRACT-001` · `SCIENTIST-FIRST-REAL-PAPER-PILOT-001` | 🔴 **UNATTRIBUTED.** They predate the earliest session that can speak for them. The commit does not close this and must not be read as closing it |

**The author field cannot discriminate a writer, and this is measured, not argued.** Every commit
reachable from every head in this repository carries one of exactly **three** author identities,
all of them named `The LEGEND project`:

```
git log --all --format='%an <%ae>' | sort -u
  → 3 rows, all with author name "The LEGEND project", differing only in address:
      1 · a project forge no-reply address
      2 · a placeholder domain address
      3 · a personal address        ← not reproduced here
```

Reproduce with the command above; the addresses are deliberately not transcribed.

**The third row is itself an instance of the class under repair.** A personal address sits in the
author metadata of this repository's history, where the release gate does not look — the privacy
scan reads file *content*, not commit headers. It is recorded here as a population and not
reproduced. Reproducing it to prove it exists would be the error the record is about, and the
first draft of this file did exactly that before its own check caught it.

`702df73` and `43cf690` carry the first, **byte-identical to the commits of every other session**
— the Orchestrator packet at `a58af46`, the Mirror review at `77be2f4`, `main` at `788c357`. The
field records that a commit happened under this repository's git identity. It names no session, no
actor and no writer, and it says nothing whatever about who authored the content.

⇒ **A commit, an author field and a message are provenance of the commit, never of the file.** A
later reader taking `702df73` as provenance would be making the same error this repository has
already paid for twice — attributing work by prose voice, or by mtime. Neither is evidence, and
neither is this.

**One correction owed to that commit's own message.** Its subject reports a finding, and its body
describes the identifier scrub and the consolidation, in the first person throughout. That voice
is accurate for the consolidation artifact and **inaccurate for five of the twelve files**. The
commit is not amended: it has already been read at `43cf690` by at least two other sessions, and
rewriting it would invalidate their measurement to fix a caption. **This record is the correction.**

---

## 3 · COMMIT `43cf690` — CORRECT, AND ITS AUTHORITY IS NOT SETTLED

`43cf690` committed three coupled files: the DisMech/LEGEND crosswalk v2, the `FT-073` append to
`full_text_queue_current.md`, and the regenerated `batch_queue.md`.

**The coupling is real and was established twice, independently.** The recording session ran both
arms on a scratch copy before committing; the session acting as Orchestrator
(`legend-public-49`) ran the full matrix hours earlier in a throwaway worktree:

| Subset committed | Result |
|---|---|
| none of the three | `unread_premises` 4/4 · LINT `PASS` · `batch_queue --check` OK |
| crosswalk only | `unread_premises` **5/4** · **`BLOCK_BATCH_COMMIT`** |
| crosswalk + FT-073 | 4/4 · `PASS` · `batch_queue` **DRIFT** |
| **all three** | 4/4 · `PASS` · OK |

**Every proper subset leaves a gate unsatisfied. Only all three, or none.**

**Nothing canonical moved — re-verified here, with a positive control.** `git diff main HEAD` over
the four scientific current files and the state manifest returns **empty**; the same command over
`full_text_queue_current.md` and `batch_queue.md` returns **both**, proving the command capable of
reporting a change. Neither queue is one of the four current files.

🔴 **The open question, which this record does not answer.** A session acting as Orchestrator had
determined, before the commit, that these three files were BLOCKED from preservation because the
operator dispatch makes provenance a **precondition** and the original authorship of the crosswalk
and FT-073 is unrecoverable. **That determination existed in messages and in a report to the
Operator. It was never a property of the repository** — no file in this working directory carried
it, no ref mentions it, and a sweep of every tracked ref for it returns nothing. It could not have
been seen here and was not bypassed.

**Standing position, agreed across three sessions and recorded so it is not re-litigated:**

- **The recommendation is: do not revert.** It is a recommendation, not a finding.
- The question before the Operator is **"does `43cf690` stand"** — not "preserve these or not".
- **Provenance is not closed by the commit.** The commit gives these three files an author field,
  a message and a timestamp. None of those is authorship.

### 3.1 · CORRECTION — the first version of this section argued the wrong thing

**This record originally said a revert "would delete an untracked file rather than restore its
untracked state", implying a revert lands nowhere valid. That is true of ONE of the three files
and I generalised it to three** — a wrong-denominator error inside a record about denominators.
Raised by `evidence-index-a6`, verified here rather than accepted:

| File | State at `43cf690~1` | What a revert does |
|---|---|---|
| `dismech_legend_evidence_crosswalk_v2.md` | **ABSENT**. On **1 of 57** refs, in exactly **1** commit — `43cf690` itself. Positive control: `CLAUDE.md` resolves on 56 refs | **destroys it permanently.** Nothing to restore |
| `full_text_queue_current.md` | **TRACKED**, 72 `FT-` entries (→ 73) | restores a real prior state |
| `batch_queue.md` | **TRACKED**, 4 lines changed / 8 diff-lines | restores a real prior state |

`git show --numstat 43cf690` → `834/0` · `4/4` · `57/0`: **one addition and two modifications, not
three additions.**

**And the arm I had not tested.** Extracting the tree at `43cf690~1` and running the gates on it:
`legend_lint.py` **PASS** · `growth_anchors.py check` **PASS** · `unread_premises` **4/4** · 72
`FT-` entries · crosswalk absent. **A full revert is valid and lands in a real, self-consistent,
gate-passing state.**

⇒ **The decision is therefore narrower and cleaner than this record first made it.** It is not
"revert into an invalid state, or keep a contested commit". Both arms are valid and both pass the
gates. **The entire cost of reverting is one thing: an 834-line analysis, whose author nobody can
name, ceases to exist.** The two queue arms follow the crosswalk either way, for the coupling
reason, and should carry no weight in the decision.

`evidence-index-a6`'s recommendation, recorded as its recommendation and not as a finding: do not
revert, because *an analysis with no author is still an object, deleting it is the only
irreversible move on the table, and irreversibility is the thing to spend last.*

---

## 4 · THE FINDING, WHICH IS NOT ABOUT EITHER COMMIT

Two sessions followed procedure. One ran a `ONE_WRITER` check and asked for sole-writer status
before writing; the other had already finished and held nothing pending. The classic outcome
happened anyway: **one session committed another's uncommitted work.**

The cause is not carelessness. It is that **two writers shared one working directory**, and that
every control governing the situation lived in prose:

| The prose | What would have executed |
|---|---|
| a preservation blocker in a chat and a report | a marker in the working directory, or a gate that reads one |
| a sole-writer claim in a message | a durable record — this file — plus a check that reads it |
| authorship carried by first-person voice in a document | an author field the producer writes, and a gate that requires it |

**This is the same class the surrounding review work spent the day cataloguing**, and it is the
one that had an operational consequence rather than a documentary one.

**No new mechanism is proposed here.** Recording the class, in the repository, is the whole of
this file's purpose — and writing it down is the minimum act that distinguishes it from the
defect it describes.
