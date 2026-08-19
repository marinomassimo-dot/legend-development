---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0011
actor_id: plan
role: Plan
date: 2026-08-19
task: ORCHSURF-001 · directive v2 · generation 1 — targeted remediation of
  CAND-20260819-ORCHSURF after REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES (C.2: REFINED)
scope: the editable half of the BOOTSTRAP defect closed; the FROZEN Annex I.2 half declared,
  owned and routed rather than overridden; two overclaims withdrawn; one residual owner corrected
  and its extent enumerated. Annex I.2 NOT amended. Routing NOT opened. Annex D.1 NOT touched.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-4 is offered as REPLICATION and not as a new observation;
  L-1 is offered as an extension of SLR-plan-0010 L-2 rather than a re-claim of it, and Mirror
  decides which it is.
derived_from: [SLR-plan-0010, SLR-plan-0010-COR-001, SLR-plan-0009, REV-ORCHSURF-MIRROR-001]
---

# SLR-plan-0011 — I corrected the row the defect was written in, and the instruction two paragraphs above it went on saying the same thing in different words

## WORK COMPLETED

Revision 2 of `CAND-20260819-ORCHSURF`, against Mirror's blocking finding B-1 and non-blocking
N-1. `BOOTSTRAP.md` no longer contains an instruction that seats a standing Orchestrator in the
repository root, and it does not replace one with an instruction the governance has not authorized
either: it stops at step 9, records `BLOCKED_BY_GOVERNANCE` (body §48), and names the operator as
the owner of the transition. `deployment/deployment_profile.md` and `roles/orchestrator.md` carry
the same residual, declared with an owner and a convergence route. `SLR-plan-0010-COR-001` corrects
the ownership attribution and enumerates the residual's real extent. Two claims that said the
defect was discharged are withdrawn.

## PROBLEMS

**P-1 — the correction I published was not the correction I claimed.** Revision 1 corrected the
`BOOTSTRAP.md` table row at line 86 and asserted, in three places, that the bootstrap defect was
repaired. It was not. Lines 31–35 of the same file still said *"The same chat is promoted — you do
not need to open a second one"*, and step 3 still created five worktrees, omitting the very
`orchestrator` worktree the corrected table pointed at. A fresh bootstrap run against Revision 1
still ended with the Orchestrator resident in the root.

**P-2 — the document that outranks the one I was editing was named in the file I was editing.**
`BOOTSTRAP.md` line 5: `authority: Annex I.1, I.2, I.6`. FROZEN `Annex I.2` steps 1, 6 and 9–10
mandate the topology Revision 1 forbade. The candidate referenced Annex I.2 **zero** times — I
verified this myself against the Revision-1 tree before accepting the finding, across all four
content files.

**P-3 — I routed a residual to the wrong owner.** I said Orchestrator owns
`runtime/agent_card_registry.md`. Its own frontmatter says `maintained_by: plan`, body §43 says
Plan updates it, and finding C-5 on the Orchestrator's own branch says *"Owner: Plan."*

**P-4 — I named one file and the residual is two, plus a third nobody had named.** Mirror found
`runtime/runtime_inventory.md`. I then found `runtime/bootstrap/STEP5-session-open-plan.md`, which
is the more interesting one: it is a *session-opening plan*, the same genre as the table I
corrected, one layer down, and it says *"The Orchestrator chat is already open in the root checkout
and is not reopened."*

## SOLUTION

**Not a better instruction — a refusal to give one.** Both executable repairs available to me were
wrong. Telling the operator to promote the root chat recreates the standing writer that `GATE 0`
and `ONE_WRITER` forbid. Telling the operator to open a chat in the `orchestrator` worktree adopts
a topology no approved act authorizes, from a `status: PROPOSED` document, against a `FROZEN`
rank-1 annex that the same document names as its own authority. The third option is the only
truthful one: **surface the conflict, stop, and name whose decision it is.**

What that meant concretely: the promotion step now carries a stop before its acquisition verb; the
operator-facing chat list is held at the five `Annex I.2` step 6 requires and the sixth line is
explicitly withheld; the `orchestrator` row of the table is marked `BLOCKED, do not open` and
re-described as *the work surface canonical main assigns*, not as an instruction; and a dedicated
section states the conflict, both sources, the reason the I.2 topology is defective, and the reason
that is still not this file's decision.

**One thing was safe to repair outright.** Step 3 now creates the `orchestrator` worktree too.
Creating a directory opens no chat and promotes nobody, and the worktree is canonical at `main`
through `CAND-20260817-ORCHWT` — so the authority question is which chat is promoted, not which
directories exist. That distinction is what let the blocked half stay narrow.

## LEARNING

**L-1 · A remediation search keyed to the defect's wording finds the wording. Restate the defect as
an executable outcome first.** SLR-plan-0010 L-2 already said *the finding is the claim, not the
line* — and I applied it, grepped the claim, found a second site, and stopped. But *"the claim"* as
I stated it was `worktree: the repository root checkout`, which is still a wording. The behaviour
was *"a fresh bootstrap seats the Orchestrator in the root"*, and that behaviour was alive two
paragraphs above the site I fixed, in a sentence that contains none of the defect's words. The
search that would have worked is not a grep at all: it is walking the procedure and asking, at each
step, where does an operator following this end up. Offered as an extension of L-2, because L-2 is
correct and insufficient by exactly one step.

**L-2 · The precedence chain is part of the file set, and the pointer is usually in the file being
edited.** A completeness audit that enumerates *other files repeating the claim* is a sideways
search. It misses *documents that outrank this one*, which is an upward search, and the upward
search is the cheaper of the two: governance artifacts here declare `authority:` in their
frontmatter, so the list of documents to read before editing one is already written at the top of
it. I edited `BOOTSTRAP.md` without opening the annex its own line 5 names.

**L-3 · When the conflict is with law you may not change, the deliverable is a fail-closed stop,
not a resolution.** A lower-precedence document that "fixes" a contradiction with a higher-precedence
one has not fixed anything; it has created a second contradiction and hidden the first. Declaring
the residual with an owner and a route is not a lesser outcome than repairing it — against
higher-ranked law it is the *only* outcome available, and the failure mode it prevents is a
document that reads as authoritative while contradicting the thing that authorizes it.

**L-4 · Ownership comes from durable ownership metadata, not from physical location.** I reasoned
from *the file is on a branch I may not write* to *the file is not mine*. Location decides the
route; `maintained_by`, body §43 and the recorded finding decide the owner. Offered as REPLICATION
of the class SLR-plan-0010 L-4 already records — an attribute that describes *where* a thing is
does not establish *what* it is — and recorded in full in `SLR-plan-0010-COR-001`.

**L-5 · The contradiction was created by a canonicalization and survived every gate that reviewed
it.** `CAND-20260817-ORCHWT` corrected the deployment profile and left `Annex I.2` mandating the
arrangement it replaced. Measured, not assumed: the ORCHWT manifest contains **0** references to
`I.2` and **0** to `Annex I`; `REV-ORCHWT-MIRROR-001` and `REV-ORCHWT-MIRROR-002` contain **0** of
each. Two hostile reviews and an operator approval passed over it, and it took a fourth candidate,
two revisions later, to surface it. **No gate in this pipeline asks what else asserts the thing a
candidate is changing** — and the annex was not hidden, it was one frontmatter line away from the
file everyone was reading.

## MICRO-UPGRADE

**Adopted for the next Plan candidate that edits a governance artifact, and stated as a procedure
because it is not a script:** before the first edit, read the documents the target file's
`authority:` frontmatter names, and record in the manifest what each of them says about the
statement being changed — including "nothing", which is the answer that makes the check cheap.

It is one read per named annex, the list is already machine-readable, and applied to Revision 1 it
would have returned `Annex I.2` on the first line of the first check. **Not built, not claimed as
built:** no script parses `authority:` today, and the value of recording it in the manifest is that
a reviewer can see whether the check ran, which is the part a script would not supply anyway.

Offered to Mirror as a candidate `PROVISIONAL_OPERATIONAL_PRACTICE` (E.3) rather than adopted as
governance — success criterion: it names an outranking document that the sideways search misses;
failure criterion: three consecutive candidates where it returns only "nothing" and the sideways
search finds everything.

## IMPACT

**What the laboratory gains.** `BOOTSTRAP.md` cannot now walk a fresh operator into a standing root
Orchestrator, and cannot walk them into an unauthorized one either. The residual against FROZEN
`Annex I.2` is declared in three places with one owner and one route, so the next reader inherits a
known-open question instead of a document that quietly disagrees with its own authority. The
agent-card residual has the right owner and its real extent — two tracked files, seven occurrences,
one of them previously unnamed by anyone.

**What it does not gain, stated because Revision 1 blurred exactly this line.** The Orchestrator
surface is **not resolved**. The bootstrap transition is **not adopted**. `Annex I.2` is unchanged
and still mandates the legacy topology; the candidate makes that visible and does not touch it. No
routing mechanism exists, no session is elected, and the three holds that block Candidate B are
where they were.

**Cost.** One further rotation of the orchestrator fingerprint — `88dea7a6…` at BASE, `42b8575c…`
at Revision 1, `9d8d823c…` at Revision 2 — invalidating orchestrator checkpoints for resume and no
one else's. Plan, mirror and scientist are byte-identical to BASE, verified at both tips.

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1  ORIGINAL_OBSERVATION   (offered as an extension of SLR-plan-0010 L-2)
                 L-2  ORIGINAL_OBSERVATION
                 L-3  ORIGINAL_OBSERVATION
                 L-4  REPLICATION            (of the class in SLR-plan-0010 L-4)
                 L-5  ORIGINAL_OBSERVATION
                 ALL PROPOSED — E.2 curation is Mirror's; Plan does not self-ratify, and the
                 vocabulary is E.2's own (ORIGINAL_OBSERVATION | REPLICATION |
                 EXPOSURE_AFTER_BROADCAST), which SLR-plan-0010 did not use — N-2, accepted

SCOPE            L-1  wider scope — any remediation of a stated defect in any governed system
                 L-2  wider scope where artifacts declare their own authority; laboratory-
                      internal in the specific `authority:`-frontmatter form
                 L-3  wider scope — it is a statement about precedence, not about this repository
                 L-4  wider scope in its general form
                 L-5  laboratory-internal as a process finding; the general form — *a correction
                      to A does not audit what else asserts A* — is offered for wider scope

EVIDENCE         P-1  BOOTSTRAP.md at CONTENT_TIP b3afdde, lines 31–35 and step 3, read in full
                      rather than grepped; the Revision-1 diff touches 8 lines of that file
                 P-2  `grep -c 'Annex I\.2'` over the four Revision-1 content files → 0 0 0 0;
                      BOOTSTRAP.md line 5 `authority: Annex I.1, I.2, I.6`
                 P-3  three sources agreeing — agent_card_registry frontmatter `maintained_by:
                      plan`; body §43 line 419; finding C-5 on branch `orchestrator`
                 P-4  seven occurrences enumerated in SLR-plan-0010-COR-001 §2, across
                      agent_card_registry.md, runtime_inventory.md and
                      runtime/bootstrap/STEP5-session-open-plan.md
                 L-5  `git show <rev>:reviews/mirror/REV-ORCHWT-MIRROR-00{1,2}.md | grep -c` →
                      0 for both `I.2` and `Annex I`, at both recorded revisions; ORCHWT
                      manifest → 0
                 T7–T9 and the re-run of T1–T6 are in CAND-20260819-ORCHSURF revision 2 §9,
                      each with its expected reason and its controls

REVIEW           L-3 is the entry most worth attacking, and the attack is specific: a reviewer
                 who holds that `BOOTSTRAP.md` is *merely descriptive* would say a fail-closed
                 stop over-reacts to a documentation lag. My answer is that its own heading calls
                 it *"Procedure for the first chat"* and that steps 9–10 are the act, not a
                 description of one — but that is a reading, and Mirror owns whether it holds.

LEARNING_ID      no LEARNING_ID is claimed here. LEARNING_INDEX does not exist (Annex E.2,
                 ABSENT — recorded in runtime_inventory C-list and unchanged by this session),
                 so an ID minted now would name nothing. Durability of the index is Plan's and
                 is not in this candidate's scope.
```
