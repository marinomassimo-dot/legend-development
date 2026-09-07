---
record: OPERATING-PRACTICE FINDING — stated once, standalone
id: OP_FINDING_INDEPENDENCE_VS_COMMIT_SUBJECTS_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
requested_by: Orchestrator session legend-public-49, dispatch of 2026-08-25 — *"stated once, cleanly,
  as an operating-practice item rather than buried in a §10.2 … Record it; do not repair it."*
status: NON-CANONICAL. **A record, not a repair.** It proposes no change, adopts no mitigation, and
  modifies no protocol, convention or contract.
supersedes_nothing: the original disclosure stays where it was made, in
  `PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md` §10.2. This does not replace it.
---

# The independence rule and the commit-subject convention cannot both be obeyed

## The finding, in one sentence

**A Phase I independence rule that gates on peer-artifact *existence*, running in a repository whose
convention is to state the finding in the commit subject line, cannot be obeyed: the mandated check
is itself the leak, and any actor obeying both instructions is contaminated by the act of obeying.**

## The two instructions, quoted

**The gate**, operator dispatch §3:

> *"Only after all three first-pass artifacts exist may Phase II begin."*

and §12:

> *"Only after A and C have durably recorded independent outputs may they read Scientist-B's pilot."*

Existence and durability are properties of *other actors' branches*. Establishing them requires
reading those branches.

**The convention.** This repository states the finding in the subject line. It is not an accident and
it is not a lapse — it is a deliberate and, in my judgement, good convention, visible across the
whole history. A sample from the refs involved in this pilot:

| Ref | Subject |
|---|---|
| `lettore-c@c55c25c` | *"The panel was read before the claim that cites it, and the citation points at the wrong panel"* |
| `lettore@5b681f2` | *"Phase I closes; Phase II is blocked, and the block is named rather than routed around"* |
| `lettore-b@8612baa` | *"Eighteen of twenty edges are not causal, and the vocabulary that types them only types causal"* |
| `legend-operating-convention-v1@d422829` | *"The Pathograph existed on disk and on no ref, and its three wiring lines went with it"* |

Each of those is a conclusion, legible to anyone running `git log --oneline -1`.

## Why it is a class and not an incident — three independent hits, one exercise

1. **Scientist B (me).** Performing the §3 existence check, I ran `git log --oneline -1` on
   `refs/heads/lettore-c` and read `c55c25c`'s subject. It states the panel-attribution conclusion —
   the same conclusion as my own finding. My derivation was complete and self-contained before the
   check (caption verbatim → Results verbatim → panel at native resolution → the single
   `Fig. 7[a-d]` occurrence in the claim registry), and I disclosed the leak rather than let it pass.
2. **Scientist C**, independently, hit the same wall reading *my* subject line.
3. **The Orchestrator**, independently, hit it reading `lettore-c@c55c25c`.

Three actors, three routes, one exercise. **The rate is what makes it structural.** Nobody
shortcut anything; each was executing the instruction it was given.

## The precise mechanism

The leak is not in reading a peer's *file*. Every actor here refused that, correctly. It is that
**git's cheapest existence primitives are not content-blind**:

| Command | Answers "does it exist?" | Leaks a conclusion |
|---|---|---|
| `git log --oneline -1 <ref>` | yes | **yes** — the subject |
| `git log --format='%H %cI' <ref>` | yes | no |
| `git ls-tree -r --name-only <ref>` | yes | no — filenames only |
| `git status --porcelain` (peer worktree) | yes | no |

The two content-blind forms exist and are no harder to type. **What is missing is not a tool. It is
the observation that the check has a content-blind form and that the obvious form does not.**

⚠️ **A filename is not always blind either.** My own artifact is named
`PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md`, and Scientist A's
`TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` names the edge it adjudicates. Neither states a
*verdict*, which is why `--name-only` held for me — but the boundary is a naming habit, not a
guarantee, and a file named `..._LITHIUM_NOT_GENOTYPE_SPECIFIC.md` would leak as surely as a subject
line.

## Observed asymmetry worth recording

I checked Scientist A by filename and Scientist C by subject line, and **that difference was luck,
not judgement.** A's artifacts were untracked at the moment I looked, so there was no commit and no
subject to read; I fell back to `ls` because nothing else was available. C's were committed, so
`git log` was the natural reach and it leaked.

**The actor who commits its work promptly — the behaviour every other part of this system rewards —
is the actor whose conclusions leak first.** That is the part of this finding I would least like to
see lost.

## The mitigations, listed and NOT adopted

Recorded so the option space is on the record, and explicitly **not** taken. Each would change a
convention or a protocol, and neither is a Scientist's to change (§16; §15 puts routing with
Orchestrator).

1. **Check existence content-blind.** `git ls-tree -r --name-only` and
   `git log --format='%H %cI'` only; never `--oneline`, never `%s`. Cheapest, and it leaves the
   filename channel open.
2. **Route the existence check through a non-adjudicating actor.** The gate is a routing fact, not a
   scientific one; §15 already puts routing with Orchestrator. Costs a round trip.
3. **Suspend the subject-line convention for Phase I commits.** Highest cost by far. The convention
   is one of the better things about this repository's history and I would not trade it for this.

**I adopt none of them, and I record that the Orchestrator adopted none either.** A finding that
repairs itself before it has been reviewed stops being evidence.

## A second-order note, since it applies to this file

This record now contains the subject lines it is a finding about. **Recording a negative falsifies
it** — anyone who greps for the leaked conclusions will now find them here, quoted by the document
that reports the leak. That is unavoidable and is the same class as the Pathograph sweep, where
re-running my own 0-of-50 measurement now returns 3 refs and all eleven hits are the three
scientists' own records of the absence.

**The durable form of such a finding is about the object, not the string.** For the Pathograph:
`git ls-tree -r --name-only` over all refs. For this one: the finding is about *which git commands
the protocol forces an actor to run*, and that does not decay when the finding is written down.

## Scope of this record

**What it establishes:** that the two instructions conflict, that the conflict fired three times in
one exercise, and that the conflict is in the protocol, not in any actor's conduct.

**What it does not establish:** that any conclusion in this pilot was *caused* by the leak. Mine was
not — my derivation was complete before the check, and it is reproducible from the primary artifact
without reference to any peer. I make no claim about C's or the Orchestrator's.

**What it does not do:** repair anything.
