---
record_type: WORK_ANALYSIS
id: PLAN-CANDIDATE-METADATA-ADOPTION-001
title: The precedent is six sevenths uniform and its hash names an object one branch has
date: 2026-08-26
role: PRODUCER
mode: EXECUTABLE HARDENING / MEASUREMENT
authority: Plan role contract. **No new schema requirement is created here.** A minimal adoption
  is proposed and not enacted; no candidate file is edited.
status: populations measured · derivability tested per candidate · two fabrication sites named
---

# CANDIDATE METADATA — MEASUREMENT AND A MINIMAL ADOPTION PROPOSAL

> **Nothing here is medical advice.** Candidate shape only. No scientific content read, altered
> or judged.

---

## 1 · The populations, at current tips

`disease-models/wwox/research/commit_candidates/`, counting only candidates **not already on
`main`**, because the 17 inherited ones are the same objects on every branch.

| | Scientist A (`lettore` `ccddc28`) | Scientist B (`lettore-b` `bf88c1a`) | `lettore-c` (`7642673`) |
|---|:--:|:--:|:--:|
| candidates on the branch | 41 | 24 | 17 |
| **not on `main`** | **24** | **7** | **0** |
| `**Candidate ID:**` | 20/24 | **7/7** | — |
| `**Author:**` | **0/24** | **7/7** | — |
| `**Base head:**` | **0/24** | **7/7** | — |
| `**Change class:** MAJOR\|MINOR\|PATCH` | 9/24 | **0/7** | — |
| a receipt referenced | 11/24 | 5/7 | — |
| machine-readable frontmatter | 0/24 | 0/7 | — |

⚠️ **`Change class` disagrees with the previous session's figure (B 7/7), and the instrument is
the reason.** Mine requires a labelled field `**Change class:** MAJOR|MINOR|PATCH`; B's
candidates carry no such field, and a looser probe that accepts the token anywhere in the body
would count them. The stricter number is reported because *a gate would have to parse a field*,
not find a word. `lettore-c` contributes nothing new — its 17 are `main`'s.

---

## 2 · 🔴 The precedent is not as uniform as it was described

B's seven were all introduced by one commit (`bf88c1a`), and their declared `Base head` is:

```
6 of 7   `b80ae8b`
1 of 7   `main`          <- a moving ref name, not an identifier
```

And `b80ae8b` is **B's own previous commit**: contained by `lettore-b` and by no other head.
`merge-base(main, b80ae8b) = 788c357d`.

⇒ **B's `Base head` means "the tip of my working branch when I wrote this", not "the canonical
state this is written against".** It is a real and useful field — it binds the candidate to a
reproducible object — but the object is branch-local, and one of the seven binds to a name that
will mean something different next week. **Adopting the field wholesale would propagate both.**

---

## 3 · Is adding these fields semantics-preserving?

| Field | Semantics-preserving? | Derivable? | Fabrication risk |
|---|---|---|---|
| **`Author`** | **yes** — pure attribution, changes no claim, no delta, no class | **24/24 and 7/7**, from the branch that introduced the file | **none.** It records the actor *seat*, which the repository already knows. It does **not** come from `git log --format=%an`: that field is the shared project identity on every commit and attributes nothing |
| **`Base head` (canonical)** | **yes** — states which canonical state the candidate was written against; asserts nothing about the delta | **24/24**, as `merge-base(main, last commit touching the file)` | 🔴 **conditional — see § 4** |
| **`Base head` (B's branch-local shape)** | yes | trivially (the parent of the introducing commit) | names an object only one branch holds; a reviewer elsewhere cannot resolve it |

### The canonical derivation, measured

```
A's 24 candidates, merge-base(main, LAST touching commit):
    17 x 788c357d      7 x 9b0cf470          -> two values, both genuine canonical heads
                                                (9b0cf470 IS an ancestor of main)
first-touch vs last-touch: 23 of 24 identical
                            1 differs  (CC-20260826-PROVENANCE-01: 9b0cf470 -> 788c357d)
B's 7: 0 of 7 differ
```

**The derivation is stable for 30 of 31 candidates**, and the one exception is a candidate edited
after a canonical head moved — for which the *last*-touch value is the honest one, because that is
the state the final text was written against.

---

## 4 · 🔴 Where adding it retrospectively would fabricate provenance

A's candidates already carry a base slot, and it holds a **policy** rather than an identifier:

```
8 of 24   **Target WM:** current at BATCH_COMMIT time; rebase required
7 of 24   **Target WM:** current at BATCH_COMMIT time
9 of 24   (no Target WM field)
```

The eight that say **`rebase required`** are declining to bind, deliberately. Writing a hash into
that slot would replace an author's refusal with an assertion the author did not make. The seven
that say `current at BATCH_COMMIT time` say the same thing more weakly.

**The derived value is nonetheless true.** `merge-base(main, last touch)` is a fact about the
repository, not a claim about what anybody read. The fabrication is not in the value — it is in
**putting a derived value in a slot reserved for a declared one**, where no reader can tell which
it is.

Two distinct fabrication sites, then:

1. overwriting `Target WM` for the 8 that say `rebase required`;
2. presenting any derived hash as though the author had declared it — all 24.

---

## 5 · Minimal adoption proposal — no new schema requirement

The queue's constraint is explicit: **do not create a new schema requirement.** What follows
therefore adopts fields that already exist in this repository, and adds a single word.

1. **`**Author:**`** — adopt B's field for A's 24. Value: the actor seat that introduced the file,
   derived from the branch. Semantics-preserving, no fabrication site, uniform across both sets.
2. **`**Base head:**`** — adopt B's field, with the value derived as
   `merge-base(main, last commit touching the file)`, and written as
   **`**Base head:** \`788c357d\` (derived)`**. The parenthesis is the whole proposal: it costs one
   word and it is the only thing that keeps a derived value out of a declared slot.
3. **Leave `Target WM` untouched.** It is A's own record of a base *policy*, and it does not
   contradict a derived base head — the two answer different questions, which is precisely the
   distinction § 4 says must not be collapsed.
4. **B's own set gets one correction**, not a migration: the candidate declaring
   `**Base head:** main` should name the hash `main` pointed at, so the field survives `main`
   moving. That is B's to make.
5. **Nothing about `Change class` is proposed.** No gate can derive a reviewer floor from either
   set, and that remains the governance question already routed. It is not reopened here.

**Not enacted.** No candidate file is edited by this record.

---

## 6 · PMID36828035 — the routing question, answered

The reported condition was that `PMID36828035.json` remained **untracked** on the scientific
surface.

**It is tracked, and the worktree is clean.**

```
lettore  ccddc28   disease-models/wwox/research/deepdive_manifests/PMID36828035.json   TRACKED
                   CC-20260826-PMID36828035-01.md                                      TRACKED
                   CC-20260826-PMID36828035-02.md                                      TRACKED
added by ed4f177  "The figure I said would reconcile the two doses excluded the only explanation I had"
git status in .claude/worktrees/lettore: clean
```

**Durability is now the only open half, and it is a routing fact, not a defect:**

> The manifest is tracked on **1 of 60 heads**. `main` does not have it, and no other branch does.

No scientific content was read, manufactured or altered here — the question asked was whether an
object exists on a ref, and that is what was measured.

**Handoff required, exactly:** `lettore`'s three PMID36828035 objects reach `main` only through
the same route as every other scientific candidate — a `CANONICAL_BATCH_COMMIT` that Plan does
not hold. **The precise handoff is: `lettore` must be enrolled in the next batch, or its three
objects cherry-picked onto a ref that is.** Until then the object exists and is durable on one
branch, which is not the same as being in the repository everyone reads.
