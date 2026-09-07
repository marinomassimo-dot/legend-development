---
artifact: MIRROR POST-TRANSCRIPTION FIDELITY VALIDATION — was exactly the authorized transcription
  applied to the candidate, and nothing else
record_id: REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY
actor_id: mirror
role: Mirror — hostile review + metacognitive layer
object_validated: Plan WORK_COMMIT b14a0d1466962aa79d1bbd0065a0d1141f4a0eab on branch
  `plan-orchsurf-r4-transcription` — NOT MODIFIED by this record
authorized_specification: reviews/orchestrator/REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION.md
  @ 1e2fabd3 · blob ab3a946c · sha256 758b45bf…2f63b — NOT MODIFIED by this record
validated_by: mirror
validated_at: 2026-08-22
question_answered: did Plan apply exactly the authorized transcription? That question ONLY
validation_result: FAITHFUL — scoped to transcription fidelity and to nothing else
review_round: NONE. This is not a C.3 round. REV-ORCHSURF-MIRROR-002 stays closed and is not
  reopened; no round is opened, spent or closed by this record
authorizes_nothing: not an ORCHSURF approval, not HUMAN_APPROVAL, not a canonicalization, not a
  D.2 interpretation, not a governance change, not a resolution of any UNRESOLVED item
scope_negative: no existing file is edited; the candidate, the patch specification, ADD-002, the
  DEC, Plan's commit and canonical `main` are untouched; no ORCHESTRATOR_LEASE is acquired or
  claimed; no defect is repaired
provenance: every value below was re-derived by me, in this session, from repository objects with
  `git`, `shasum` and `python3`. NOTHING is imported from conversation history, from the dispatch
  prompt, from Plan's commit message, or from any earlier Mirror validation. Where Plan's commit
  message asserts a value, that value was re-measured and is reported as my measurement — see §6
discipline: append-only
---

# `REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY`

## 0 · Identity and rehydration — read from the repository, none from the prompt

```
ACTOR_ID          mirror — roles/mirror.md frontmatter `actor_id: mirror`, `worktree: mirror`
ROLE SOURCE       roles/mirror.md · CLAUDE.md § 1 (router → governance/, roles/)
AUTHORITY         inspect repository evidence, compare objects, produce this report. Mirror
                  "holds no command over any actor and produces no primary evidence"
                  (roles/mirror.md). Nothing below is a verdict on ORCHSURF
BOUNDARY          Mirror does NOT edit the candidate, Plan's commit, the patch specification or
                  any governance file; does not transcribe; does not repair; does not create
                  HUMAN_APPROVAL; does not resolve any UNRESOLVED item

branch            mirror
HEAD              71694319cd009a4b6cf8056fa7cdca303d5f2a76
worktree          <REPO_ROOT>/.claude/worktrees/mirror
git status        clean, 0 entries, at the instant this record was written
```

**The validated objects are not on this branch and were read as repository objects.** Branch
`plan-orchsurf-r4-transcription` is checked out in a different worktree
(`.claude/worktrees/evidence-index`). Nothing was checked out, merged or fetched to read it:
every value comes from `git cat-file` / `git ls-tree` / `git diff-tree` against the object store.

---

## 1 · Source binding — every named object resolved before it was trusted

```
OBJECT                                    TYPE     RESOLVES
b14a0d1466962aa79d1bbd0065a0d1141f4a0eab  commit   YES — Plan WORK_COMMIT
aa49df9aa204961487861a288227402d1c756d5f  commit   YES — parent candidate commit
92c1b7d8be169232613ae8b219112a09d7b315dc  blob     YES — candidate BEFORE
e0f3f7299b482d0dd69d5ee7a9e058d2fa410f5c  blob     YES — candidate AFTER
1e2fabd3c73a908bca2439cf080a7c83e8b17d30  commit   YES — patch specification commit
ab3a946c21c61b59a1a85fa3b413947725b30452  blob     YES — patch specification
```

```
PLAN COMMIT       b14a0d1466962aa79d1bbd0065a0d1141f4a0eab
tree              198f5c9b58d2bc4bad5ea1d5fe5016fe9034d574
parent            aa49df9aa204961487861a288227402d1c756d5f — exactly ONE parent, and it is the
                  parent the dispatch names. Not a merge
author/committer  The LEGEND project <legend-project@users.noreply.github.com>
branches          `git branch -a --contains` returns exactly ONE ref:
                  plan-orchsurf-r4-transcription, which is also its tip
NOT contained by  main · orchestrator · orchestrator-surface · mirror — verified individually
                  with `merge-base --is-ancestor`. Nothing canonical carries this commit
```

**Candidate blobs, measured not assumed.**

```
BEFORE  blob 92c1b7d8  @ aa49df9, path governance/candidates/CAND-20260819-ORCHSURF.md
        sha256 19a7daeec7e0d410aca59f6bb32fb36c530cd610737b61808b41f0eeec5f0759
        1114 lines · 79 917 bytes
        `ls-tree` at aa49df9 returns this blob at this path — the dispatch's value, confirmed
        at the object rather than carried

AFTER   blob e0f3f729  @ b14a0d1, same path
        sha256 44573a553d8c6534d0680ae6f4ab5376927e6868c38d0be7ac1eeb5a58e3d378
        1149 lines · 83 026 bytes
        `ls-tree` at b14a0d1 returns this blob at this path
```

---

## 2 · `CHECK 4` — patch specification binding · **MATCH**

Checked first, because nothing downstream means anything if the authority is not the object the
dispatch names. **The branch tip was not used as authority**; the commit was.

```
commit resolves   1e2fabd3c73a908bca2439cf080a7c83e8b17d30 — commit object
blob resolves     ab3a946c21c61b59a1a85fa3b413947725b30452 present in that commit's tree at
                  reviews/orchestrator/REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION.md
                  (`git ls-tree -r 1e2fabd`). The blob is bound to a path in the named commit,
                  not merely resident in the object store
blob id re-derived  `git cat-file -p ab3a946c | git hash-object --stdin` → ab3a946c21c61b59a1…
                  The content hashes back to its own name
sha256 matches    RECOMPUTED 758b45bf74f2d4aaeb9204676050999c9be9dfeca2ca2afc777a16642592f63b
                  DISPATCHED 758b45bf74f2d4aaeb9204676050999c9be9dfeca2ca2afc777a16642592f63b
                  IDENTICAL

PATCH_BINDING     MATCH
```

**The authorized text was extracted programmatically from blob `ab3a946c`, never retyped.** Each
of §3, §4 and §5 of the specification contains exactly two fenced blocks and no more — verified by
enumerating every fence line in 207–303: `211/214 · 219/229` (L-1), `237/242 · 247/270` (L-2),
`278/281 · 288/301` (L-3). The first block of each pair is labelled *"Current text, verbatim"*, the
second *"Proposed replacement"*. There is no third block that could have been the intended one.

---

## 3 · `CHECK 1` — commit scope · **MATCH**

```
git diff-tree -r --no-commit-id --raw b14a0d1

:100644 100644 92c1b7d8… e0f3f729… M  governance/candidates/CAND-20260819-ORCHSURF.md

entries                 1
paths changed           1
mode change             none — 100644 → 100644
additions / deletions   none. Rename/copy detection (-M -C) surfaces nothing further
unrelated changes       NONE. A whole-tree recursive diff between aa49df9 and b14a0d1 differs
                        at this single path
governance files        untouched · review records untouched · learning records untouched

COMMIT_SCOPE            MATCH — only the candidate file changed
```

---

## 4 · `CHECK 2` — the three authorized loci · **MATCH at all three**

**Each locus was located by its content at each blob, never by an inherited line number.** The
method is a byte-exact search for the authorized text in the blob, with the occurrence count
reported — so a locus that appeared twice, or not at all, would be visible rather than assumed
away. Line numbers below are *outputs* of that search, not inputs to it.

Digests are SHA-1 truncated to 12 hex over the extracted region including its trailing newline —
the method the specification's §2 states for itself, applied here to reproduce it.

```
LOCUS  L-1 · frontmatter `supersedes:` clause
before digest    3d44eb0b221d   (2 lines)
after digest     a677e9fcce56   (9 lines)
located          BEFORE text occurs exactly 1× in blob 92c1b7d8, at lines 53–54
                 AFTER  text occurs exactly 1× in blob e0f3f729, at lines 53–61
negatives        AFTER text occurs 0× in the parent · BEFORE text occurs 0× in the committed blob
replacement      the authorized §3 replacement, byte-for-byte
                 MATCH

LOCUS  L-2 · § 1 manifest `MIRROR_REVIEW` field
before digest    176bae1745ae   (4 lines)
after digest     09afebb56c45   (22 lines)
located          BEFORE text occurs exactly 1× in blob 92c1b7d8, at lines 158–161
                 AFTER  text occurs exactly 1× in blob e0f3f729, at lines 165–186
negatives        AFTER text occurs 0× in the parent · BEFORE text occurs 0× in the committed blob
replacement      the authorized §4 replacement, byte-for-byte — the WHOLE field, opening line
                 included, which is what the specification's OBS-1 requires
                 MATCH

LOCUS  L-3 · § 17.3 first bullet
before digest    c0a63e189914   (2 lines)
after digest     f260e6425e8a   (12 lines)
located          BEFORE text occurs exactly 1× in blob 92c1b7d8, at lines 1086–1087
                 AFTER  text occurs exactly 1× in blob e0f3f729, at lines 1111–1122
negatives        AFTER text occurs 0× in the parent · BEFORE text occurs 0× in the committed blob
replacement      the authorized §5 replacement, byte-for-byte
                 MATCH
```

**The four negatives above are the load-bearing part**, and they are stated as measurements rather
than as absence of complaint. That each BEFORE text occurs **0×** in the committed blob is what
rules out a replacement applied *in addition to* rather than *in place of* the old text; that each
AFTER text occurs **0×** in the parent rules out the replacement having already been there.

**The specification's own §2 digest table reproduces**, by its own stated method, at the surfaces
this transcription actually used:

```
       RECORDED @ §2      RECOMPUTED by me      
L-1    3d44eb0b221d       3d44eb0b221d          MATCH
L-2    176bae1745ae       176bae1745ae          MATCH
L-3    c0a63e189914       c0a63e189914          MATCH
```

---

## 5 · `CHECK 3` — bidirectional scope proof · **MATCH in both directions**

The two directions are not one check written twice. Direction A establishes that the authorized
replacements are **sufficient** to produce what was committed — nothing extra was needed. Direction
B establishes that they are **exhaustive** — removing them leaves nothing behind. Together they
close the gap a one-directional check leaves open: a change *outside* the three loci would survive
direction A's construction and be exposed by direction B, and vice versa.

```
A) parent blob 92c1b7d8, with ONLY the three authorized replacements applied, each to its single
   located occurrence:

   reconstructed  sha256 44573a553d8c6534d0680ae6f4ab5376927e6868c38d0be7ac1eeb5a58e3d378
   committed      sha256 44573a553d8c6534d0680ae6f4ab5376927e6868c38d0be7ac1eeb5a58e3d378
   IDENTICAL — byte-for-byte, whole file

B) committed blob e0f3f729, with ONLY those three replacements reverted:

   reverted       sha256 19a7daeec7e0d410aca59f6bb32fb36c530cd610737b61808b41f0eeec5f0759
   parent         sha256 19a7daeec7e0d410aca59f6bb32fb36c530cd610737b61808b41f0eeec5f0759
   IDENTICAL — byte-for-byte, whole file

BIDIRECTIONAL_SCOPE_PROOF   MATCH
```

**Consequence, stated plainly.** Not one byte outside the three authorized loci differs between the
parent candidate and the committed candidate. This is positive evidence, not the absence of a
finding: the reconstruction was performed and its hash agrees.

### 5.1 · An apparent fourth changed region, and why it is not one

A line-level differ over the two blobs reports **four** changed regions rather than three. I did not
dismiss this as noise, and I did not let it stand as a defect either — I measured what causes it.

```
replace  parent line 54                            → contained in L-1
replace  parent lines 158–161                      → contained in L-2
replace  parent line 1086                          → contained in L-3
insert   between parent lines 1087 and 1088        → contained in L-3

all four regions contained within the three authorized loci:  YES
```

The split has a single cause: **two lines that the authorized replacement text re-emits verbatim.**

```
parent line 53   == committed line 53
  "  Annex D.2 invalidates them because the bound content moved. REV-ORCHSURF-MIRROR-001 reviewed"
  present inside the AUTHORIZED §3 replacement text: YES
  — the specification states this at §3: "The first sentence of line 53 is re-emitted unchanged"

parent line 1087 == committed line 1116
  "  revision 1's review was conducted under the opposite direction, so it does not transfer."
  present inside the AUTHORIZED §5 replacement text: YES
```

A line-oriented differ pairs a re-emitted line with its original and calls it *equal*, which splits
one logical replacement into a replace plus an insert. That is a property of the differ, not a
change to the file. The byte-for-byte bidirectional proof in §5 is the authority on scope, and it
matched in both directions; this section exists so that a reader who runs a line diff and counts
four regions is not left to guess whether Mirror saw the same thing.

---

## 6 · Plan's own claims, re-measured rather than carried

Plan's commit message asserts several values. Under this record's provenance rule, none was
accepted as read; each below was re-derived from the objects. They are reported because a
validation that silently agrees with the thing it validates has not demonstrated that it looked.

```
CLAIMED                                   MEASURED BY ME                              
parent aa49df9, branch created there      commit has exactly one parent, = aa49df9    CONFIRMED
candidate blob 92c1b7d8 @ aa49df9         ls-tree at aa49df9 returns 92c1b7d8         CONFIRMED
patch spec blob ab3a946c @ 1e2fabd        ls-tree at 1e2fabd returns ab3a946c         CONFIRMED
sha256 758b45bf…92f63b                    recomputed identical                        CONFIRMED
L-1 sha1-12 3d44eb0b221d                  recomputed identical                        CONFIRMED
L-2 sha1-12 176bae1745ae                  recomputed identical                        CONFIRMED
L-3 sha1-12 c0a63e189914                  recomputed identical                        CONFIRMED
L-1 at 53–54, L-2 158–161, L-3 1086–1087  located by content, same spans              CONFIRMED
"1114 lines -> 1149"                      1114 → 1149                                 CONFIRMED
"one path is staged, by name"             diff-tree: exactly 1 entry                  CONFIRMED
scope proof reverses to 92c1b7d8          reproduced independently, both directions   CONFIRMED
```

**The pre-existing YAML observation, verified rather than repeated.** Plan reports that the
candidate's frontmatter does not parse under a strict YAML reader, that the failure is pre-existing,
and that it is not repaired. Measured: `yaml.safe_load` over the frontmatter fails identically at
both blobs — same construct, an unquoted `:` inside a folded scalar in the `supersedes:` block —
and lines 1–52 of the two blobs are byte-identical. The failure is therefore untouched by this
commit, which the §5 scope proof independently entails. **Mirror does not repair it and does not
rule on it**; it is recorded as measured, and the repair question is not opened here.

**One boundary Plan's message does not cross and neither does this record.** The specification's
§2 argues that no fourth locus exists. That is a claim about whether the *specification* is
complete, not about whether the *transcription* was faithful. It is out of this validation's scope
and is neither confirmed nor disputed here. What §5 does establish is narrower and sufficient for
the question asked: whatever the specification authorized, exactly that and only that was applied.

---

## 7 · Result

```
MIRROR_POST_TRANSCRIPTION_FIDELITY

DATE                 2026-08-22
ACTOR_ID             mirror
QUESTION             did Plan apply exactly the authorized transcription?

COMMIT_SCOPE                 MATCH
LOCUS  L-1                   MATCH
LOCUS  L-2                   MATCH
LOCUS  L-3                   MATCH
PATCH_BINDING                MATCH
BIDIRECTIONAL_SCOPE_PROOF    MATCH

FINAL_RESULT                 FAITHFUL
```

**What `FAITHFUL` means here, and what it does not.** It means: the object at
`governance/candidates/CAND-20260819-ORCHSURF.md` in commit `b14a0d1` is the parent object
`92c1b7d8` with the three replacements specified by `REV-ORCHSURF-ADD-002-PATCH-SPECIFICATION`
applied at the three loci ADD-002 named, byte-for-byte, and with no other change of any kind. It
does **not** mean the specification was right, that the replacement text is correct, that the
candidate is now accurate, or that anything may proceed. Per `roles/mirror.md`, a Mirror
confirmation means *"no defect found given the available evidence bundle"* — never *"true"*.

### 7.1 · What this record does NOT establish

```
ORCHSURF approval        NOT GRANTED. No reviewer issued PASS on revision 4. This is not a
                         review of ORCHSURF and produces no verdict on it
HUMAN_APPROVAL           UNCHANGED. No APPROVAL_ID exists and none is created here
canonicalization         NONE. `main` is untouched, no ORCHESTRATOR_LEASE is acquired or
                         claimed, no GATE is asserted, no CANONICAL_BATCH_COMMIT occurs
UNRESOLVED-D             REMAINS OPEN, untouched, not re-decided
UNRESOLVED-A, -B, -C     not resolved by this record
D.2 amendment            NONE. No reading of Annex D.2 is adopted, proposed or implied
governance change        NONE. No governance file is read into a decision or modified
C.3 review round         NONE opened, spent or closed. REV-ORCHSURF-MIRROR-002 stays closed
candidate binding        NOT re-bound. This record supplies no binding for any canonical
                         batch operation
defect repair            NONE. The YAML observation at §6 is reported, not fixed
```

---

## 8 · Standing at the instant this record was written

```
branch mirror         HEAD 71694319 → this commit. Working tree clean before and after
files changed         reviews/mirror/REV-ORCHSURF-R4-POST-TRANSCRIPTION-FIDELITY.md — this
                      file only. One path, staged by name
Plan commit b14a0d1   NOT modified, NOT amended, NOT merged, NOT cherry-picked
branch                plan-orchsurf-r4-transcription — ref unmoved, still at b14a0d1
candidate             CAND-20260819-ORCHSURF, blobs 92c1b7d8 and e0f3f729 — read only
patch specification   blob ab3a946c — NOT edited
main                  04693e68 — not written to, not read into any decision
lease                 none acquired, none claimed. This is a WORK_COMMIT, not a
                      CANONICAL_BATCH_COMMIT
this record           reviews/mirror/ — control plane. It describes a validation; it
                      constitutes no candidate, authorizes no act, and clears no gate
```
