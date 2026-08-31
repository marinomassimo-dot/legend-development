---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0010
actor_id: plan
role: Plan
date: 2026-08-19
task: ORCHSURF-001 · directive v1 · generation 1 — Orchestrator work/batch/routing-surface
  semantics; stale role labelling; whether a filesystem location may identify an actor
scope: one stale frontmatter line corrected and typed; the same stale claim found in a SECOND
  live artifact the prior analysis had not named; a cross-actor rule written stating that working
  directory is prohibited as an identity discriminator; five requirements recorded for a future
  resolver. Annex D.1 untouched. Routing NOT implemented, no session elected.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-3 corrects a reason published in a canonical candidate
  while leaving that candidate's conclusion standing, and Mirror decides whether that is one
  observation or two.
derived_from: [SLR-plan-0009, SLR-plan-0008, SLR-mirror-0014, SLR-mirror-0015]
---

# SLR-plan-0010 — the label was true when it was written, and the file that repeats it tells a new operator what to do

## Context

`roles/orchestrator.md` says, in frontmatter, `worktree: the repository root checkout`. Annex D.1
says `WORK_COMMIT` happens on an actor's own branch and `CANONICAL_BATCH_COMMIT` happens in the
root. The deployment profile says the Orchestrator's worktree is `orchestrator`. Three statements,
two of which agree, and the third had never been wrong — only overtaken.

The prior session measured this and deliberately did not fix it. This session was asked to fix it
without letting the fix become Routing.

---

## WORK COMPLETED

```
IDENTITY          rehydrated fail-closed · pwd == git top-level == evidence-index ·
                  roles/plan.md read in full · governance 3.1.1
CANONICAL MAIN    04693e68 verified from git, not from the prompt. Its tree is byte-identical
                  to the branch tip it merged (f450ec39), which is why a diff between them is
                  empty — verified with a positive control rather than accepted
FINGERPRINTS      all four recomputed and matched before any edit
EXECUTION         Annex D.1 FROZEN, rank 1 vs a role rule's rank 4. NOT ambiguous, NOT touched
LABEL             STALE — introduced a8cd125 (2026-08-16), never updated by e861dc4 (2026-08-17).
                  `roles/orchestrator.md` has been touched exactly once in its life
SECOND SITE       BOOTSTRAP.md line 86 carries the same stale row — not previously named
MEASUREMENT       root 17 · orchestrator worktree 0 · evidence-index 1 · mirror 10 · absent path 0
REMEDIATION       role label corrected + typed; cross-actor cwd rule; resolver requirements
BLAST RADIUS      one fingerprint. orchestrator 88dea7a6… → 42b8575c…; three unchanged
```

---

## L-1 · A high-precedence rule can make execution deterministic while a low-precedence label stays dangerous

**CONFIRMATION_CLASS proposed: CONFIRMED — first observation of this shape.**

Annex D.1 settles where each kind of commit happens, is `FROZEN`, and outranks a role contract
four levels under body §5. Nothing about execution was ever unclear, and nothing executing today
was at risk. It is tempting to conclude from that that the stale label was cosmetic.

It was not, and the reason is that the two rules answer different questions. D.1 answers *where
does this commit go*. The frontmatter answers *where does this actor live* — and that second
question has no high-precedence answer anywhere, so the stale sentence was the only answer
available to whoever asked it next.

**What this changes for me:** "the higher-precedence document is correct" closes the question of
what is *authoritative*. It does not close the question of what is *readable*, and a resolver, a
new operator or a future session reads what is in front of it. I now treat *precedence* and
*reachability* as two separate audits.

---

## L-2 · Correct the class, not the instance — the same stale claim was in a second file, and that one gives instructions

**CONFIRMATION_CLASS proposed: CONFIRMED.**

The prior analysis named one site: the role frontmatter. I swept for the phrase instead of going
to the named line, and found `BOOTSTRAP.md` carrying the same row in a table headed **"The chats
to open"** — the instructions a human follows when standing up the laboratory from nothing.

That distinction matters more than the duplication does. The role contract is *described* state;
BOOTSTRAP is *prescribed* action. A fresh bootstrap performed against the file as it stood would
have placed the Orchestrator in the root, restoring the standing writer in the root that
`e861dc4` removed — and `GATE 0` requires the root clean, with `ONE_WRITER` calling it *"critico
nella root"*. The defect was one bootstrap away from re-executing itself.

**What this changes for me:** when a stale statement is found, the finding is *the claim*, not
*the line*. Grep the claim across the tree before proposing the fix, and sort what is found by
whether it describes or instructs — the instructing copy is the urgent one even when it looks
like a duplicate.

---

## L-3 · A conclusion can be right while its published reason is false, and the reason is what the next session inherits

**CONFIRMATION_CLASS proposed: CONFIRMED — offered as distinct from the instrument class.**

`CAND-20260819-P5DOMAIN` §8.3 is canonical and argues that a root-cwd reading is useless for
identifying the Orchestrator because *"every worktree lives under the root at `.claude/worktrees/`"*
— calling the result *"the universal set shaped like one"*.

The conclusion is correct. The reason is false: seven of this machine's fourteen worktrees are
outside the root entirely. The true statement is the narrow one — **all six named actor worktrees
are under the root, 6/6** — and it supports the same conclusion by a different route: the root
query is not universal, it is **over-broad for actor discrimination**.

The difference is not pedantry. A future reader who accepted the universal would conclude that
containment is a structural property of the repository and could be relied on; it is a property of
where six worktrees happen to have been created, and the codex worktrees on this machine already
violate it.

**What this changes for me:** when I inherit a conclusion I agree with, I now re-derive the
*reason* rather than the *verdict*, because agreement on the verdict is exactly the condition
under which nobody re-checks the premise.

---

## L-4 · cwd is evidence about an environment; the runtime has no opinion about identity at all

**CONFIRMATION_CLASS proposed: CONFIRMED.**

I expected to be weighing how *much* corroboration a working directory provides. The measurement
made that the wrong question: the runtime exposes `cwd`, `kind`, `name`, `pid`, `sessionId`,
`startedAt`, and **no field naming an actor or a role**. There is no identity attribute to weigh.

Worse for the corroboration idea, `name` is derived from the `cwd` leaf — 17/17, with a negative
control that matches nothing. Keying on cwd *and* name looks like two attributes agreeing and is
one attribute repeated. That is the shape Mirror has recorded before under a different name: two
measurements that agree because they cannot disagree.

**What this changes for me:** before treating two attributes as corroborating, I now test whether
one is a function of the other. Agreement between a value and its own derivative is not evidence.

---

## L-5 · A special-authority actor needs typed surfaces; forcing symmetry on the ordinary ones would be the second error

**CONFIRMATION_CLASS proposed: PROPOSED — a design judgement, not a measurement.**

The obvious tidy fix was to rename `worktree:` to `work_surface:` in all four role contracts so
the schema matches. I did not, and the reason is that the asymmetry is real: Orchestrator is the
only actor whose work surface and canonical-commit surface differ, because it is the only actor
with canonical-commit authority. Ordinary actors have one surface, and `ACTOR_ID ↔ worktree` is
simple and correct for them.

So `worktree:` keeps one meaning everywhere — *the actor's work surface* — and the second concept
gets its own name in the one contract that has one. The untyped word is fixed by making it mean
exactly one thing, not by renaming it in three files that were never ambiguous. That also holds
the blast radius to a single fingerprint.

**What this changes for me:** schema uniformity is a benefit, not a goal. When one member of a set
genuinely differs, encoding the difference is cheaper and more honest than flattening it.

---

## WHAT I DID NOT DO

```
Annex D.1                    NOT modified — verified correct, and it is FROZEN
P5 / P5DOMAIN                NOT reopened
C-9 §7.2                     NOT altered
Routing                      NOT implemented — no resolver, no registrar, no actors.yaml,
                             no generations, no CURRENT, no session elected or superseded
Lease state                  NOT mutated — runtime/orchestrator_lease.md is IN_DOMAIN and
                             was read only
Scientist A/B                NOT activated · Scientist C untouched · BENCH-AB-001 NOT started
main                         UNCHANGED at 04693e68
Other actors' branches       NOT touched — including the stale WORKTREE row in
                             runtime/agent_card_registry.md on branch `orchestrator`, which is
                             runtime state on another actor's surface and is REPORTED, not edited
```

---

## OPEN, AND ROUTED TO ITS OWNER

- **Which session is current for an ACTOR_ID** remains unresolved. This session removed a wrong
  answer; it did not supply a right one, and four holds still block the resolver.
- **`runtime/agent_card_registry.md` on branch `orchestrator`** carries `WORKTREE: the root
  checkout # branch main`. It is not canonical and not mine. Orchestrator owns it.
- **Whether L-3 is one observation or two** — a false premise under a true conclusion, and a
  correction to a canonical candidate's reasoning that does not disturb its verdict. Mirror decides.
