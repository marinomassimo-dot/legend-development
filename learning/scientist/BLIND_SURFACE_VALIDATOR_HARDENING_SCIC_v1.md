---
artifact: LEGEND scientific evaluation — VALIDATOR HOSTILE TEST, PROVENANCE CLASSIFICATION,
  READER ELIGIBILITY CLASSES, PILOT PACKET, GOLD PIPELINE
id: BLIND_SURFACE_VALIDATOR_HARDENING_SCIC_v1
class: evaluator-side record. It attacks and repairs the instruments that gate a blind
  surface. It is NOT a benchmark manifest and authorizes no run.
continues: BLIND_SURFACE_CONSTRUCTION_AND_FRESH_READER_EVAL_SCIC_v1
actor: scientist-c (autonomous queue, operator absent)
worktree: lettore-c · branch lettore-c
date: 2026-08-26
audience: EVALUATOR ONLY
scope: EVALUATION INFRASTRUCTURE. No governance, role-contract, schema or architecture change.
status: NON-CANONICAL. Mutates no canonical file, manifest, receipt or ledger.
canonical_mutation: NONE
---

# The surface passed. The validator did not.

> **Nothing here is medical advice.** · **A and B were not contacted. No blind replication
> was run. No case was dispatched.**

---

## 0 · The one line

Last session built a blind surface and shipped two validators that reported zero findings on
it. This session attacked the validators instead of the surface. **Four contamination
classes walked straight through a gate that was reporting clean**, and the deepest one could
not be fixed by any pattern, because it was a leak in the file the checker derives its
reference value *from*.

```
before          7 mutation classes, all blocked by check_blind_surface.py
after          14 mutation classes, all blocked — 6 of them only by a tool
                that did not exist this morning
```

And the repairs cost four more defects, every one of them in my own instruments, every one
found by running the previous repair rather than reasoning about it.

---

## 1 · C1 — the surface rebuilds

Four builds from scratch, two cases into two neutral roots. Hashes re-derived by a **second
implementation of the written recipe** that does not import the builder — a builder printing
its own hash is self-attestation.

```
BLIND-FR-001   19 files   4957981272b835a94ba322268dead233592e7805b92965f2a7925789d02d72d6
BLIND-FR-003   17 files   12f0e2c80979a5f8ae48cc49c26c98a632261a942b369af697a84c7675a01c64
                          identical across r1 and r2 · byte-identical trees under diff -r
```

The prototype root that named this repository in its own directory name — a declared
residual last session — is now `/private/tmp/lgbench/{r1,r2}`, and **an approved-root check
replaces the memory of it**. The upward walk confirmed why it matters: `.claude` exists at
`<HOME>`, so any surface under the operator's home inherits an instruction surface.

The eleven required properties hold. Three of them were not checked by anything last session
and are checked now — see §2.

---

## 2 · C2 — the hostile test, and what it found

### 2.1 · Four classes passed a validator reporting zero findings

Measured against `check_blind_surface.py`, on a surface it passed clean:

| | class | result |
|---|---|---|
| M8 | answer written into the **commit message** | 🔴 NOT CAUGHT |
| M9 | local git identity unset → `~/.gitconfig` signs the commit | 🔴 NOT CAUGHT |
| M10 | `CLAUDE.md` created in the parent **after** the build | 🔴 NOT CAUGHT |
| M13 | answer written into the **case spec's `question`** | 🔴 NOT CAUGHT |

### 2.2 · 🔴 M13 is the structural one

The checker re-renders `ASSIGNMENT.md` from (template + case spec) and compares byte-for-byte.
That defeats a leak written into the assignment — it was last session's repair, and it works.
It cannot defeat a leak written into the **spec**, because then the leak renders faithfully
and the comparison succeeds. *The check is working perfectly and seeing nothing.*

Its filename form passed too. An answer-bearing `dest` is **allowlisted by construction**, so
only the committed word list stands in its way:

```
supplement_01_kinase_never_measured.pdf          FAIL   (the list contains "never")
supplement_01_zero_kinase_signal_any_panel.pdf   PASS
supplement_01_title_claim_lacks_assay.pdf        PASS
```

**No pattern decides whether a free-text question leaks.** So the control is not a pattern.
The participant-facing **projection** of the spec — exactly the fields that reach a reader,
derived from the two renderers rather than guessed — is hashed, and the digest must appear in
`cases/approved_inputs.json`.

That converts an undecidable question (*is this text clean?*) into a decidable one (*is this
the text that was approved?*). **It does not make the text clean. It makes a change to it
visible**, which is the most a checker can honestly do.

### 2.3 · The battery, and where the required values live

`surface_properties.py` gates what a file walk cannot see. Required values live in the
**approvals file, never the build manifest** — a checker that read what the builder recorded
would let a builder change silently relax the check.

| property | why a name-based check misses it |
|---|---|
| ANCESTRY | re-walked **at handover**: the builder's refusal is a build-time guard, and the parent can be created afterwards |
| IDENTITY | config *and* every commit's author/committer, against declared constants |
| METADATA | commit message re-derived against a constant; refs, reflog, `ORIG_HEAD`, `packed-refs`, stash, notes |
| OBJECT STORE | **reachability** — an object enters via `hash-object -w` with no remote, no alternate and no visible ref, and every name-based check sees nothing |
| APPROVAL | the projection digest, and the digest of everything a reader is handed |

### 2.4 · Fourteen classes, and the coverage nobody would have reported

```
S1  answer text, post-build                BLOCKED  files   DERIVATION,DIGEST
S2  evaluator artifact                     BLOCKED  files   LANGUAGE,UNALLOWLISTED
S3  answer-bearing filename (injected)     BLOCKED  files   FILENAME,UNALLOWLISTED
S4  remote + alternate                     BLOCKED  files   HISTORY
S5  extra file                             BLOCKED  files   UNALLOWLISTED
S6  provenance object w/ adjudication      BLOCKED  files   ADJ_FIELD,ANSWER,UNALLOWLISTED
S7  answer injected DURING build           BLOCKED  files   DERIVATION
S8  answer in git metadata                 BLOCKED  props   METADATA,OBJECTSTORE
S9  global git identity leakage            BLOCKED  props   IDENTITY,METADATA,OBJECTSTORE
S10 parent CLAUDE.md                       BLOCKED  props   ANCESTRY
S11 hidden git history (no ref)            BLOCKED  props   OBJECTSTORE
S12 modified source byte                   BLOCKED  files   DIGEST
S13 case spec carries the category label   BLOCKED  props   APPROVAL
S14 answer in filename via spec `dest`     BLOCKED  props   APPROVAL
```

🔴 **Every class is blocked by exactly one tool.** There is no redundancy anywhere in this
gate. "14/14 blocked" and "14/14 blocked, each by a single check" are the same number
describing very different systems, and the first is the more reassuring and the less true.

---

## 3 · C3 — provenance: the count went down

🔴 **I published `PROVENANCE_SEPARATION_COUNT 5` last session. Measured structurally, it is
0.**

`--feasibility` counts papers whose six fields are **derivable**. I carried that number
forward under the name **separated**. The projection drops adjudication from its *output* and
cannot drop it from its *input* — and `verbatim_locators` is present in **64 of 64** deepdive
manifests, carrying, in the one I opened, prose stating the paper's finding outright.

```
PROVENANCE_SEPARATED              0
CONTAMINATED                      5     derivable only by opening a file that states
                                        conclusions about that same material
MISSING_PROVENANCE_STRUCTURE     53     identified by digest; the debt closes by adding
                                        page/crop/dpi or a fetch URL
UNRESOLVABLE                      0
                                 333 figure rows · 40 with a recipe · 333 identified
```

Nothing changes for the participant: the surface never holds a manifest. What fails is the
claim MSR-1..MSR-4 actually make — that a record be derivable *without reading an
adjudication*. **The derivation act fails it, not the emitted record.**

Papers classify by their **weakest** figure row; any other aggregation optimises the count.

**Separation was specified and not executed, and the reason is a contradiction worth not
shipping.** All 5 are separable by emitting the whitelisted projection standalone — but 3
carry `crop_xyxy`, and **a crop is a prior reader's attention, stated more precisely than the
renders the case specs already exclude for encoding exactly that.** Emitting crops as
"participant-safe provenance" would contradict the packet rule, in a repository whose problem
is contaminated artifacts.

---

## 4 · C4 — four classes, never summed

```
SURFACE_CLEAN      PASS        allowlist · digests · derivation · language · filenames
REPOSITORY_CLEAN   PASS        ancestry · root · identity · metadata · object store · approval
SESSION_CLEAN      PASS*       * on a neutral root. FAILS in this checkout — see below
MEMORY_CLEAN       UNPROVABLE  and it prints UNPROVABLE, never PASS
```

🔴 **SESSION_CLEAN is the class a built surface cannot reach, and nothing had looked for it.**
Measured in this checkout:

```
.claude/skills/     21 skills named legend-*, incl. legend-aso-designer, legend-proband-*
.claude/agents/     wwox-scout.md · legend-deepdive.md · fulltext-dossier.md
project memory      46 files, 25 naming the gene or project; MEMORY.md auto-loaded EVERY session
```

**An actor started in this project is told the gene, the pipeline and the therapeutic
programme in its system prompt, before its first tool call.** No allowlist reaches that,
because it was never on the surface. The requirement is on the **launch**, and it is now
measured at the launch directory rather than promised.

Four things remain undecidable by any filesystem check and are therefore stated as
requirements: the system prompt, the tool roster (a web tool makes the packet boundary *a
rule the reader is asked to keep, not a wall that keeps them*), additional working
directories, and prior turns of the same conversation.

**Absence of evidence of exposure is not exclusion of exposure.** A probe that can only move a
label toward *contaminated* cannot establish *not-contaminated*, however many zeroes it returns.

---

## 5 · C5 — the pilot packet

**`BLIND-FR-003`**, chosen on the queue's own criterion — *does not reveal its category
through the assignment*. Its question asks for a taxonomy and presupposes no tension.

🔴 **The other candidate revealed its category, and the tell was in a place nobody inspects.**
`BLIND-FR-001`'s stop condition offered *"or record that the published record does not decide,
naming the exact object that would"* — and across the two cases that exist, **that clause
appeared in exactly the one whose answer is a negative.** An outcome offered where it is the
answer and withheld elsewhere is a category label written into the assignment.

Repaired by making it **byte-identical in every assignment**, where it cannot distinguish
anything, and where it now declares its own uninformativeness to the reader.

The packet was **five of seven**. The two missing components are now rendered, not written:

- **`PROVENANCE.json`** — whitelisted structural fields and per-kind uniform assertions.
  It does **not** emit the corpus filename (first author and year), nor the spec's per-case
  prose. It **refuses** any packet kind it has no uniform assertion for, because describing
  that kind per case is the leak.
- **`CONTAMINATION_DECLARATION.md`** — byte-identical for every case, and that is a
  constraint, not a convenience. 🔴 **The count of what was removed is itself a fact about the
  case**: eight excluded renders means a paper worked harder than one with four, and the
  reader learns that from the file written to protect them.

The declaration also tells the reader the three things a surface cannot remove, including
that the packet names its source by published identifier.

`PILOT_PACKET_READY: YES · DISPATCHED: NO`. The dispatch gate fails, correctly, because no
approver on record has `NOT_SEEN` exposure.

---

## 6 · C6 — the gold pipeline

```
NO_ADJUDICATION 3 · FIRST_ONLY 3 · TWO_UNCOMPARED 0 · GOLD_READY 0
UNCONTAMINATED ACTORS ON RECORD  0
```

🔴 **The reading pipeline and the gold pipeline are short of the same resource**, and each
case needs **two distinct** instances of it:

> An actor who adjudicates a case has read its answer and can never be its reader. An actor
> who reads a case has produced the output the adjudication grades.

I supplied no second adjudication. I hold three firsts and am disqualified for all three. For
the pilot case my exposure is `UNKNOWN`, not `NOT_SEEN`, which disqualifies me from its
**first** adjudication too — an adjudication by me would fix the answer using knowledge I
cannot rule out having.

---

## 7 · Self-corrections — five, all mine, all found by running

| | what I got wrong | how it surfaced |
|---|---|---|
| 1 | `PROVENANCE_SEPARATION_COUNT 5` — I reported derivability under the name separation | measuring the source files instead of the emitted fields |
| 2 | the launch-directory scan flagged the surface's **own** allowlisted `CLAUDE.md` and `.git` | running it; population drawn wider than the property |
| 3 | the memory probe **decoded** the store key, so it matched nothing and reported an absence it was unable to look for | a positive control that should have fired and didn't |
| 4 | pinning the case spec left the **other** case passing while its reader's text had changed | changing the template and watching the wrong thing happen |
| 5 | pinning `ASSIGNMENT_TEMPLATE` missed two more participant-facing templates I had just added | a one-byte edit to the declaration that both cases passed |

And one that is a class of its own —

🔴 **6. The template pin read its reference value BY IMPORT, and certified a template that
was not the one on disk.** Python validates cached bytecode by `(source mtime, source size)`.
A hyphen→space edit preserved size and landed in the same second as the cached compile, so
both matched and the stale module was served. On this platform that cache lives at
`~/Library/Caches/com.apple.python/<absolute path>.pyc` — **outside the repository**,
invisible to every repo-scoped search and to any `__pycache__` check.

The residue is worse than the defect: `check_blind_surface.py` imports `render_assignment`
for the DERIVATION check, which is the **primary leak control**. So a disagreement between
the imported and the source template is now **VOID, not FAIL** — a battery cannot report on a
runtime it cannot trust. Verified: exit 2 under a deliberately staled cache, exit 0 once
cleared.

---

## 8 · What this does not claim

- **It authorizes no run and dispatches nothing.** Nothing was handed to anyone.
- **`GOLD_READY_COUNT: 0`**, and I did not self-supply a second adjudication.
- **`PROVENANCE_SEPARATED: 0`**, and I did not emit files to raise it.
- **The gate has no redundancy.** Fourteen classes, fourteen single points of failure.
- **A leak phrased outside the `LANGUAGE` list still passes any file the derivation and
  approval checks do not cover.**
- **`MEMORY_CLEAN` is unprovable and will remain so.** Nothing here makes A or B eligible.
- **Nothing here is medical advice.**

---

## 9 · Summary

```
BLIND_SURFACE_REPRODUCIBILITY   4 builds, 2 cases x 2 neutral roots, hashes re-derived by a
                                second implementation that does not import the builder.
                                Identical per case; trees byte-identical under diff -r.
                                FR-001 495798127... 19 files · FR-003 12f0e2c80... 17 files

VALIDATOR_HOSTILE_STATUS        14/14 classes blocked, up from 7. Four were measured NOT
                                CAUGHT against the previous gate on a surface it passed
                                clean. Every class is blocked by exactly ONE tool.

FRESH_READER_ELIGIBLE_COUNT     15 (unchanged; the constraint was never the surface)
A_B_ELIGIBILITY                 0 cases, either reader. Unchanged and not re-litigated:
                                a surface removes SURFACE, CHECKOUT and REPOSITORY, and
                                removes nothing of SESSION or MEMORY.

PROVENANCE_SEPARATION_STATUS    0 SEPARATED · 5 CONTAMINATED · 53 MISSING · 0 UNRESOLVABLE
PILOT_PACKET_READY              YES — BLIND-FR-003, 7/7 components, both validators PASS.
                                NOT DISPATCHED. Dispatch gate fails on approver exposure.
GOLD_READY_COUNT                0
UNRESOLVABLE_COUNT              0 provenance · 1 case category (proven, not dispatchable)

TRUE_EXTERNAL_READER_REQUIREMENT
                                Not one actor. TWO distinct actors per case, in roles
                                neither can swap into, each launched from a directory whose
                                upward walk reaches no .claude, with no project memory bound
                                to it, with no skill or agent roster naming the subject, and
                                with no tool that reaches the open web — because the packet
                                names its source by published identifier, so the boundary is
                                a rule the reader keeps, not a wall that keeps them.
```

🔴 **The line to carry.** Last session's line was *the contamination work is done; what
remains is an actor.* It was half right. The contamination work was not done — it was
**unmeasured**, because the instrument that would have measured it had never been attacked.
Attacking it took an afternoon and found four open channels, and every repair opened a
smaller one: bind the spec and the template leaks, bind the template and the declaration
leaks, read the template by import and the interpreter serves you yesterday's. **The
instruments are now hostile-tested and still have no redundancy. The actor is still missing,
and it turns out we need two.**
