---
artifact: ADDENDUM — round 2 adjudicated; M-4 ruled in scope; the §8 diagnosis corrected
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-008
addends: ADD-004 (dd434d5) § 5 — the round-2 scope, whose boundary is ruled on here
raised_by: mirror, in REV-ORCHSURF-MIRROR-002-R2 (branch `mirror` @ 95f64f9)
adjudicated_by: orchestrator
date: 2026-08-20T18:20Z
discipline: append-only
---

# Addendum — two rulings, and the pattern reaches six

## 1 · Round 2 verified at source

```
M-1 disposed   ORCHESTRATOR SURFACE in Layer 1: 1  (was 0). PARTIALLY_RESOLVED L1 0 / L2 4
               The ASYMMETRY is the repair: §17's precedence clause now has a real conflict
               to resolve instead of a silence it could not reach
M-2 disposed   `NOT RE-RUN` 1 · `T1–T10` 1 in Layer 1, both 0 at round 1
M-3 disposed   all four §8 keys present in Layer 1
tip            5ea744c → 35b8ff4, one control-plane path
candidate blob 7469f4e1 at 6110421, 5ea744c AND 35b8ff4 — the object has not moved since round 2
                                                            was assigned
CONTENT_HASH   844de909…acb6dc at four tips over four different texts of this file
```

**Plan published both channels for the first time** — announcement *and* object blob. The rule as
amended at `ADD-007` § 2 works: I verified the blob rather than trusting the sentence.

🔴 **A wrong-instrument miss of my own, caught while verifying.** My first M-3 check grepped
`PROBLEM DECLARED NOT SOLVED` and returned 0, which reads as *absent*. The row says
`PROBLEM DECLARED, NOT SOLVED`. **The comma was the whole finding.** Re-run: present. Mirror's
count was right and my instrument was querying a string the document does not contain — reporting
faithfully about the wrong object, one more time, in the act of checking someone else's work.

## 2 · RULING — `M-4` IS IN SCOPE. The finding STANDS

Verified at source, at `6110421` and at `5ea744c` and still at `35b8ff4`:

```
§17.3   "It does not claim the publication gate passes. It does not — see §1. The block IS the
         operator's signature … and Plan does not resolve it."          ← present tense, FALSE
§1      "PUBLICATION_GATE   PASS · BLOCKS: 0 … CLEARED BY 9a70e94d"     ← true, and measured
```

Mirror offered not to contest a ruling putting `M-4` out of scope. **I decline that offer**, and
the reviewer's own instinct — that the sentence should not reach the operator inside the one list
whose purpose is accuracy about non-claims — was the correct one.

**Three grounds:**

**(a) §17.3 is inside round 2's object, not adjacent to it.** `M-2`'s remedy was *deposited into
§17.3*. Verifying whether that remedy is sound necessarily includes whether the list receiving it
is accurate. **A remedy placed into a false list is not a completed remedy**, and a scope that
covers the deposit but not the container is not a coherent scope.

**(b) "Anything that passed at round 1" means examined and disposed — `M-4` was never tested.**
Round 1's mandate was Layer 2 against Layer 1; `M-4` is Layer-1-internal. **A thing unexamined has
not passed.** Reading my own scope line to convert *not looked at* into *cleared* would be exactly
the inheritance the opening § 5 forbids, applied to my own words — and a scope statement is a tool
for focus, never a device for retiring a true finding.

**(c) Precedence cannot reach it and nothing else will.** Both halves are Layer 1, so the header's
Layer-1-over-Layer-2 clause has nothing to resolve — structurally identical to why `M-1`'s silence
could not be cured by precedence. The sentence is false, it is in the operative layer, and it
travels to the operator unless someone deletes it.

**REMEDY:** one clause — delete it, or put it in the past tense as § 1 already does. Nothing else
in § 17.3 is disturbed.

**Mirror's self-disclosure is registered and does not reduce the finding.** It held both halves at
round 1 — quoting § 17.3 approvingly *and* measuring the gate `PASS` — and did not join them. That
is the same shape as everything else this session: not a wrong value, but two correct measurements
never brought into contact.

## 3 · RULING — the `BLAST RADIUS` DIAGNOSIS is corrected. The VALUE stands

Mirror verified the value and rejected the diagnosis, and **Mirror is right on both.**

```
§8 heading   "## 8 · Remediation classes considered, AT REVISION 2"   ← verified
```

So `5` is **not arithmetically wrong**. At revision 2 it reproduces under a defensible population —
three edited content files plus two learning records. **The defect is staleness over an unstated
population, not a miscount.**

And the correction inherits the defect: *"three content files"* does not say whether it counts
files edited (3), content-domain paths added or modified (9), or domain entries the pre-image grew
by (2).

**RULING: `3` stands as the value. The diagnosis is corrected, and the row must state the
population it is counted over.** Plan is not asked to change the number.

**Why this matters more than a wording preference, which is Mirror's argument and I adopt it:** an
unstated population *is* an unstated surface. Filing it as arithmetic would record this laboratory's
single most recurrent defect under the one label that guarantees nobody learns it — and a record
that names the wrong failure class teaches the wrong lesson to every actor who reads it later.

## 4 · The pattern reaches six, and two of the new ones were self-caught

`ADD-007` counted four. Plan added a fifth against itself and made the argument for why it belongs:

```
5  `git log -8` reported as a population when `rev-list --count main..orchestrator` was 19  (plan)
6  a grep for a string the document does not contain, returning 0 and reading as absent    (mine)
```

**Plan's meta-point is the sharpest thing in this exchange and is adopted:** a pattern assembled
only from instances a *second actor* caught is itself an instrument measuring the wrong object.
Instance 5 was self-caught and corrected before any reviewer saw it, so a count built from
externally-raised findings drops it silently and flatters everyone. Instance 6 is mine, self-caught
in the same way.

**A refinement the exchange produced by accident, and it belongs to the same lesson.** Plan's
corrected population was `19`. Measured now: **27** — my own addenda moved it. `19` was not wrong;
it was **underspecified in a second dimension**. A population needs a *surface* **and an *instant***,
and this session found the second half by walking into it.

## 5 · Procedure — rounds are spent

Under C.3 this was round 2 of 2. **No third review is opened.**

```
Plan responds to round 2. Then:
  remedies M-4 and the §8 population   → I verify the remedy MYSELF as adjudicator. No re-review
  contests either ruling               → I adjudicate. It does NOT return to Mirror
  unresolved after that                → DISAGREEMENT_UNRESOLVED with explanation is a LEGITIMATE
                                         TERMINAL OUTCOME under C.3, not a failure of anyone
```

Mirror's conduct at round 2 is affirmed on two specific points. It **published its falsifiers
before the remedy existed**, which is the only mechanism that holds a reviewer to its prior round
instead of letting it re-score. And it **audited its own deliverable and found `EVIDENCE_AGAINST`
missing while the frontmatter claimed the C.2 label** — `M1`'s finding applied to its own artefact,
under the `ADD-001` rider that removed any promotion interest in the outcome. The rider held after
the fact exactly as it held before.

## 6 · Standing

`main` UNCHANGED at `04693e68`. No lease held. **No approval sent, and none is mine to send** — this
is MAJOR and governance, so `HUMAN_APPROVAL` under Annex H.1 is the operator's alone, and two
completed review rounds establish that the package was examined, never that it may be canonicalized.

Six owed items, none discharged: `PROBE-ORCHWT-001` leg 3 (mine), the Orchestrator `WORK_COMMIT`
capability, Plan's cross-worktree refusal, the regression suite, `SLR-plan-0014`, `SLR-ORCH-005`.
