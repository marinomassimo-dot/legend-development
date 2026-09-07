---
artifact: benchmark isolation — durable lessons
class: methodological. Contains no scientific finding, no case answer, no case category,
  and no paper identifier. It is safe to read before adjudicating anything.
status: NON-CANONICAL. Mutates no canonical file, manifest, receipt or ledger.
---

# What kept defeating the blind surface

Every entry below is a failure that was **measured**, on an instrument that was reporting
success at the time. None is a hypothesis. They are ordered by how far out the leak was
found, because that turned out to be the pattern: each session found it one level further
from the files, and the last two levels were not in the repository at all.

---

## 1 · Branch isolation is not object-store isolation

An orphan branch shares an object store. `git show main:<path>` resolves from it,
`git log --all` enumerates every commit, and `git branch -a` enumerates every branch. A
blind surface built as a branch of the repository it is blind to is not blind.

**Isolation is a property of the object store, not of the commit graph.** No branch has
it. A fresh `git init` outside every working tree does.

**And the object store has more entrances than the two obvious ones.** Removing remotes
and `objects/info/alternates` is not enough: an object enters via `git hash-object -w` from
another repository's `cat-file` output, with no remote, no alternate and no visible ref,
and every name-based check sees nothing. The property that holds regardless of the route
in is **reachability** — every object in the store reachable from the surface's own single
ref, and nothing else resident.

### What that cost, measured

This section is the one the file's own preamble was written about: it was learned from a
surface that was **built, populated and withdrawn**, not from reasoning about git.

| | the withdrawn surface | the replacement |
|---|---:|---:|
| files carried | **585** | **6** |
| commits in history | 459 | 1 |
| merge-base with `main` | `788c357d` — a descendant | **none — a true orphan** |
| files on adjudicating paths | **175** | 0 |
| objects reachable from the ref | — | 13 |

It was branched from `main`, so it carried the registries, the deep-dive manifests and the
current files, and one case's answer verbatim. Nothing malfunctioned: `git` did exactly
what a branch does. The surface was withdrawn for that reason and rebuilt as an orphan.

> 🔴 **The 585 is the whole argument.** A blind surface does not leak because someone
> copied the wrong file in; it leaks because a branch brings everything with it by
> default, and the default is invisible until something counts it. The replacement's
> guarantee is not that its six files were checked — it is that there are only six files
> and thirteen objects to check, and no path from the ref to anything else.

*Denominator, stated because it moved:* "files on adjudicating paths" counts entries under
`registries/`, `deepdive_manifests/`, `commit_candidates/`, `research/` and `*_current.md`.
The withdrawal record recorded 101 against a narrower path set. Both describe the same
surface; neither is the other's correction.

---

## 2 · A digest certifies nothing about the build

A digest proves a file has not changed **since** the build. It proves nothing **about**
the build.

Measured: an answer, paraphrased, carrying no case identifier and no expectation-bearing
token, written into the one build-time-authored file *as if by a careless builder*, with
the manifest regenerated to match. It passed every language scan, every answer scan and
every digest check, because the manifest was written after it.

**The repair is not a wider word list.** Every file authored at build time must be
**rendered** from (template + declared inputs) and re-rendered by the checker, compared
byte-for-byte. Any sentence that is not in a template fails whatever its wording.
*Identity catches what pattern cannot.*

Corollary, learned by adding two more authored files later: the checker must iterate the
**list of renderers**, not name one file. An authored file left off that list is unchecked
by construction, and nothing announces it.

---

## 3 · A derivation check cannot see a leak in what it derives FROM

This is the sharp edge of §2 and it is easy to miss precisely because §2 worked.

If the checker re-renders the assignment **from the case specification** and compares
byte-for-byte, then a leak written into the **specification** renders faithfully and the
comparison succeeds. The check is working perfectly and seeing nothing. Its filename form
is the same: a destination name that states the answer is *allowlisted by construction*,
so the manifest cross-check cannot fire.

**No pattern decides whether a free-text question leaks.** So do not try to decide it.
Replace the undecidable question — *is this text clean?* — with a decidable one — *is this
the text that was approved?* Hash the participant-facing **projection** of the inputs, and
require the digest to appear in an approvals file.

This does **not** make the text clean. It makes a **change** to it visible, which is the
most a checker can honestly do. The cleanliness is established by a human or an
uncontaminated actor reading it once, and the approval records who, and what their
exposure was.

Two further rules fell out of it, each after the pin failed once:

- **Bind what a reader is HANDED, not one template.** Pinning one template caught the case
  whose spec was edited and let a second case pass while the text *its* reader would
  receive had changed too. Pin the digest of the rendered **output** of every renderer.
- **Required values live in the approvals file, never in the build manifest.** A checker
  that reads what the builder recorded lets a builder change silently relax the check.

---

## 4 · Blacklist leakage scans are structurally weak, and their weakness is measurable

A word list over filenames was, for one channel, the **only** defence — and it is
committed, so anyone can read it and route around it. Two names were chosen to miss it and
both passed a validator that reported zero findings.

The test that settles whether a blacklist is load-bearing is cheap: **construct the same
damage with wording the list does not contain.** If it passes, the control is decorative
on that channel and a structural comparison must replace it.

Where a structural comparison exists it strictly dominates: an allowlist catches *any*
injected file, whatever it is called. Keep the word list only where it is the last thing
standing, and record that this is what it is.

**The same incoherence has a scoping form.** A blanket scan over a surface fires on the
files that define the discipline — a taxonomy of overclaims legitimately contains the
vocabulary of overclaiming — and on the source itself, which is *supposed* to contain the
evidence. Scans must be scoped by **how each file got there**: inherited files by identity,
derived files by identity plus their own derivation's failure mode, authored files by
re-rendering, the source by identity alone.

---

## 5 · A check drawn wider than the property fires on what it protects

Twice, one session apart, in two different tools:

- a build-time rescan for a source paper's identifiers, applied to the whole surface,
  refused a legitimate build because the packet's own bibliography cited an author of an
  unrelated template source;
- a launch-directory scan for inherited instruction surfaces, started **at** the launch
  directory instead of above it, flagged the surface's own required and allowlisted files.

Both tools were correct about their predicate and wrong about its population. **State the
unit the property is about before writing the predicate**, and give every check a positive
control that must fire and a negative control that must not.

---

## 6 · A build-time guard is not a handover-time guard

The builder refuses a destination with an instruction surface above it. That refusal
happens at build time. The parent directory can be created **afterwards**, and the surface
is gated afterwards.

Any property that a later action can violate must be **re-checked at the moment the
surface is handed over**, not only at the moment it is made.

---

## 7 · An import is not the file on disk

A check that reads its reference value by importing a module is not reading the file.
Python validates a cached bytecode object by `(source mtime, source size)`. An edit that
preserves size and lands within the same second as the cached compile passes both, and the
stale module is served.

Measured on macOS, where that cache lives at `~/Library/Caches/com.apple.python/<absolute
source path>.pyc` — **outside the repository**, invisible to every repo-scoped search and
to any `__pycache__` check.

Read reference values from **source bytes**. And when the imported value and the source
value disagree, the correct verdict is **VOID, not FAIL**: if the runtime is serving stale
bytecode then every other import-based check is untrustworthy too, and a battery cannot
report on a runtime it cannot trust.

---

## 8 · Uniform text carries no signal; per-case text carries whatever distinguishes it

An instruction that offers an outcome **in the case where that outcome is the answer**, and
withholds it elsewhere, is a category label written into the assignment. Measured: across
the cases that existed, one such clause appeared in exactly the case whose answer was a
negative.

The repair is not to delete the clause — readers need it — but to make it **byte-identical
in every assignment**, where it cannot distinguish anything.

**This extends to counts.** A contamination declaration that states how many prior-reader
artifacts were removed leaks: a case with eight removed was worked harder than one with
four, and the reader learns that from the file written to protect them. Uniform text cannot
carry a per-case signal; anything per-case must be justified field by field.

---

## 9 · Derivability is not separation

A projection that drops adjudication from its **output** does not drop it from its
**input**. If the only structured source of a provenance record is a file that also states
conclusions about the same material, then the record is derivable and *not* separated —
and a requirement worded "derivable without reading an adjudication" is failed by the
derivation act, not by the emitted record.

Measured, this distinction moved a published count from five to zero. **Classify by the
source that must be opened, not by the fields that come out.** And aggregate by the
weakest row: an object is only as separated as its least-provenanced part, because any
other aggregation optimises the count.

Related, and a genuine conflict to resolve rather than paper over: a **crop rectangle is a
prior reader's attention**, stated more precisely than the renders that are already
excluded for encoding exactly that. A provenance schema that emits crops contradicts the
packet rule that excludes renders. Do not ship the contradiction.

---

## 10 · Repository-clean is not session-clean, and neither is memory-clean

A built surface removes three contaminations and cannot touch the fourth:

| | removed by a built surface |
|---|---|
| the files in front of the reader | yes — allowlist and checker |
| the checkout on disk | yes — outside every working tree |
| the object store | yes — fresh init, reachability verified |
| **what the actor already knows** | **no. Nothing removes it and no command reads it.** |

Between the third and the fourth sits a class that is **partly** decidable and was missed
entirely until it was looked for: **what the runtime hands the actor before it opens
anything.** Measured in one project checkout — a skill roster and agent definitions naming
the subject matter, and a per-project memory store whose index is loaded into context every
session. An actor started there is told the subject before its first tool call. No
allowlist reaches that, because it was never on the surface.

So: **four classes, never summed.** A single "eligible" verdict launders the weakest behind
the strongest. Report each separately, print `UNPROVABLE` — never `PASS` — for the one no
command can read, and state plainly that a clean exit means *nothing decidable is known
against this reader*, not that the reader is clean.

**Absence of evidence of exposure is not exclusion of exposure.** A probe that can only
ever move a label toward *contaminated* cannot establish *not-contaminated*, however many
times it returns zero.

---

## 11 · One clean actor is not enough, and the two pipelines are blocked on the same one

An actor who adjudicates a case has read its answer and can never be its reader. An actor
who reads a case has produced the output the adjudication grades. So each case needs **two
distinct uncontaminated actors**, in roles neither can swap into.

And the evaluation pipeline and the gold pipeline are short of the **same** resource, not
two different ones. When almost every case is adjudicated in the history every local actor
descends from, building better surfaces stops being the constraint. Count the actors before
counting the cases.

---

## 12 · Coverage without redundancy is not coverage

Fourteen contamination classes, all blocked, and **every one blocked by exactly one tool.**
No class has a second line of defence. That is worth reporting as a property of the gate,
because "14/14 blocked" and "14/14 blocked, each by one check" are the same number
describing very different systems — and a report that gives only the first is the more
reassuring and the less true.

**A mutation that does not apply proves nothing.** A hostile test must detect its own
inert cases and count them as failures against itself, not skip them quietly. And the
baseline must be verified clean before any mutation runs: a hostile test on a dirty
baseline attributes nothing.

---

> **Nothing here is medical advice.**
