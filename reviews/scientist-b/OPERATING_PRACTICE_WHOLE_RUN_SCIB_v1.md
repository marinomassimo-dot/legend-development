---
record: §11 — SCIENTIST OPERATING PRACTICE, OBSERVED ACROSS THE WHOLE RUN
id: OPERATING_PRACTICE_WHOLE_RUN_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot throughout;
  `roles/scientist.md` is `PROPOSED`, `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` records
  OPTION B `ACTIVATION_NOT_CONFIRMED`)
date: 2026-08-25
status: NON-CANONICAL. **Observed practice, not a proposed contract.** `roles/scientist.md` was not
  edited, and nothing here is drafted as contract language.
supersedes: nothing. Extends `SCIENTIST_OPERATING_PRACTICE_DISCOVERY_SCIB_v1` (repository-derived
  reconstruction) and `..._TEAM_PILOT_SCIB_v2` (Phase I only). This one covers I → V as run.
---

# What this run actually did, and which of it should survive contact with a contract

Each practice carries the six required fields. **Where a practice failed, the failure is the entry** —
a practice record of things that went well is a press release.

---

## P-1 · INDEPENDENCE

**OBSERVED.** All three Scientists declared independence from each other and held it. All three were
nonetheless non-independent of the **repository**, which already contained the answers.

**WHY IT FAILED.** `disease-models/wwox/analysis/locator_contract_live_test.md`, tracked since
2026-08-04, carries in prose the Figure 7d three-genotype reading, the ethosuximide inversion, and
*"'Elevated' is the wrong word … dis-inhibited, not more abundant"* — plus the premise tag and the
revival trigger. `CLAIM 016`'s own `Evidence boundary`, canonical, carries the same conclusion. **A
Scientist is required to read the claim record. Reading it is the contamination.**

**EVIDENCE.** My v1 pilot does not cite the analysis file and presents the conclusion as a bottom
line — a provenance gap that is mine. C declared an anchoring hazard from the deep-dive manifest and
named the narrower source. A restated its own disclosure as *"most of my Phase I was recognition,
not derivation"* and bounded it by counting what the tree does **not** contain (`S9A` 0, `ANOVA` 0,
`interaction` 0, `22193544` 0 over 454 lines).

**RECURRING.** Structural and permanent for any paper the model has already read.

**CANDIDATE.** `SKILL` + `VALIDATOR`: before Phase I, sweep the tracked tree for the paper's
identifiers and for the propositions about to be adjudicated, and **publish the contamination surface
as an input**, not as a disclosure afterwards. A's bounding method is the reusable part: measure what
the tree does *not* contain, so the concession is quantified rather than rhetorical.

**DO NOT PROMOTE YET** the idea of "independent adjudication" as a phase name. This run could not
deliver it and no rearrangement of actors would have. **What it can deliver is independent
re-derivation from primary artifacts**, which is a different and still valuable thing, and the
dispatch should say which one it is asking for.

---

## P-2 · PEER-REVIEW TIMING

**OBSERVED.** §3 gates Phase II on peer artifacts *existing*. Three actors evaluated that gate at
three instants and returned three different verdicts, each correct when taken.

**WHY IT FAILED.** A gate defined over mutable peer state, with no barrier and no agreed clock,
cannot be evaluated consistently by the actors it gates.

**EVIDENCE.** B commits 15:24:34 → C commits 15:37:28 → A publishes *"Phase II is blocked"* at
15:43:51, 6 min 23 s after the artifact that opened it → B measures at ~15:49 and proceeds. C,
measuring earliest, found both peers absent and declined Phases II–V entirely.

**RECURRING.** Will recur on every multi-actor gate.

**CANDIDATE.** `ROUTING`: the existence check belongs to a non-adjudicating actor, or the phase needs
a barrier rather than a predicate. **CANDIDATE FOR PROMOTION** — the cost here was C declining four
phases on a correct reading of a stale surface.

---

## P-3 · COMMIT-MESSAGE CONTAMINATION

**OBSERVED.** The mandated existence check leaks conclusions, because this repository states findings
in commit subjects.

**WHY IT FAILED.** git's cheapest existence primitives are not content-blind:

| Command | Answers "does it exist?" | Leaks |
|---|---|---|
| `git log --oneline -1 <ref>` | yes | **the subject** |
| `git log --format='%H %cI'` | yes | no |
| `git ls-tree -r --name-only` | yes | no |

**EVIDENCE.** Three independent hits in one run: I read `lettore-c@c55c25c`; C read mine; the
Orchestrator read C's. **The asymmetry is the finding**: I checked A by filename only because A's
work was still untracked, and C by subject because C's was committed. **The actor who commits
promptly — the behaviour everything else here rewards, including my own commit whose subject
complains that first-pass artifacts were left untracked — is the one whose conclusions leak first.**

**RECURRING.** Three hits, one run, four actors.

**CANDIDATE.** `SKILL`, one line: use the content-blind forms. **CANDIDATE FOR PROMOTION.**
**DO NOT PROMOTE** any change to the subject-line convention — it is one of the better things about
this history and I would not trade it for this. ⚠️ And a filename is not reliably blind either: mine
is `PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_…`, which names the object; a file named
`..._LITHIUM_NOT_GENOTYPE_SPECIFIC.md` would leak as surely as a subject.

---

## P-4 · NEUTRAL PACKET DESIGN

**OBSERVED.** I never opened the packet, deliberately, while holding for peers. The design finding
came from elsewhere: **the dispatch texts differed.** All three Scientists held one 17-section text;
the Orchestrator held a different one whose §10 capped the edge work at the 016-035-036 neighbourhood.

**WHY IT MATTERS.** The Orchestrator was about to select a reconciliation producer partly on the
edge-count spread — 11 / 1 / 0. C pointed out that if the texts differed, part of that spread is
paperwork and selecting on it would attribute to character what belongs to routing.

**EVIDENCE.** I supplied my headings verbatim; they matched C's structurally. A's dispatch was closed
without asking A, from eight section citations in A's own contemporaneous artifacts — the strongest
being *"Recorded per dispatch §7"* against my §7 = GRAPH-SPECIFIC DISCIPLINE, **a semantic match, not
a numeric one**. Zero cap-like citations across A's six artifacts.

**ONE-OFF in cause, RECURRING in class.** Multi-actor dispatches will diverge again.

**CANDIDATE.** `TOOL`: fingerprint every dispatch and cross-check at Phase 0, before any actor
measures anything about any other actor. **CANDIDATE FOR PROMOTION** — the cost of not doing it was
nearly scoring a routing artefact as disposition.

---

## P-5 · ACCESS TO PRIMARY ARTIFACTS ACROSS WORKTREES

**OBSERVED.** `files/` is git-ignored by privacy design, so evidence never travels with a branch.
My worktree held **13** fulltext entries — a real partial set, not an empty one — and none of them
was the paper under adjudication. I read from the shared checkout by absolute path. Mid-run the four
Cheng artifacts appeared locally and the count went to 16.

**WHY IT MATTERS BOTH WAYS.** The layering *is* the privacy design and should not be undone. But it
means **a peer on another machine can verify every registry claim in my work and no evidential
quotation.** I declared that boundary in my `OBSERVATION_SCOPE` and it was the right thing to declare.

**EVIDENCE.** C's Pathograph negative was worktree-confined and false; C's method was sound —
denominator, positive control 36/57, correct zsh braces — and it could not see another worktree's
disk. Cost: twelve adjudicable edges not adjudicated.

**RECURRING.**

**CANDIDATE.** `SKILL` + `ROUTING`: an evidence-availability preflight that resolves each task's
artifacts **before** the reading budget is set, and states which surface they live on.
**CANDIDATE FOR PROMOTION.** **DO NOT PROMOTE** any change to the `files/` rule.

---

## P-6 · TASK-BOUND EVIDENCE IDENTITY

**OBSERVED.** Fingerprint every artifact against the manifest **before** reading. Done on all four
Cheng artifacts and on Wang's XML; all matched. It converts *"I read the paper"* into *"I read this
blob"*.

**WHY IT FAILED ELSEWHERE — and it lands on a finding I started.** Verified by me at
`HEAD`, excluding my own records:

```
deepdive_manifests/PMID22193544.json  →  source_artifacts key: ABSENT
Wang XML  eb6f568d…  anchored in 10 tracked files
Wang PDF  8f994f95…  anchored in  0 tracked files
```

The image finding that moved the run's central question — Wang Fig 1d carries WWOX · pTau S396 · Tau
· actin and **no GSK3β row, no pS9 row** — **cannot come from the anchored artifact.** Blot rows are
not recoverable from JATS text. It rests on a PDF with no fingerprint anywhere in the tracked tree.

⚠️ **And it may be one file read twice.** If A and C both rendered the same unanchored PDF, that is
**peer agreement, not a second quantity** — two counts that agree verify nothing if nobody compared
the objects underneath. The Orchestrator has asked both; the question is the right one.

**RECURRING.** Schema-v1 manifests have no `source_artifacts` slot at all.

**CANDIDATE.** `VALIDATOR`: refuse a figure-derived locator whose artifact is not fingerprinted in
the manifest. **CANDIDATE FOR PROMOTION** — this is the one gap in this run that let a load-bearing
finding rest on an unidentified object.

---

## P-7 · FIGURE INSPECTION

**OBSERVED.** Read the image at native resolution, then again at 3–6× on the row that decides.

**WHY IT HELPED.** Every finding this run turned on came from pixels: the `****` marker undefined in
the legend; panel c's total absence of statistics; the heterozygote not intermediate; the `Wwox` row's
dosage gradient; and — decisively, and by C — a **missing blot row** in Wang Fig 1d, which is a
negative no text surface can express.

**EVIDENCE.** At half scale, both readings of the Fig. 7c densitometry survive. At 3× only one does.
A explicitly declined the native-resolution re-read in Phase I, then went back and did it, and
withdrew `REFUTED` as a result.

**RECURRING.**

**CANDIDATE.** `SKILL`, and sharpen it: **declare the sub-panel denominator** (C's *"6 of 6 genotype
× drug sub-panels inspected"*), not *"figures inspected"*. **CANDIDATE FOR PROMOTION.**
Add the reciprocal: *a figure-derived negative — "there is no such row" — must name the rendering and
its fingerprint*, per P-6.

---

## P-8 · DISAGREEMENT HANDLING

**OBSERVED.** Annotate in place, never rewrite; keep the superseded text above the correction.
Applied to my §1 (tense), my §4 (vocabulary premise), my §8.4 (two peer objections), my §4.4 (both
timing claims) and my Phase III edge type.

**WHY IT HELPED.** §9 forbids erasing the dissent trail and §17 forbids tidying a history so the
sequence reads better. A later reader can see *what was believed, by whom, on what evidence, and what
moved it*. Two of my dissent items closed by concession and are recorded as **closed, not deleted**.

**EVIDENCE.** Forced consensus was never applied. The one place the process produced agreement
without a criterion — A and I converging on `ASSOCIATED` — is exactly where C refused to join, and C
was right.

**RECURRING.**

**CANDIDATE.** `CONTRACT`. **CANDIDATE FOR PROMOTION.** ⚠️ With one caveat this run supplies: a
correction inherits the burden of the claim it replaces. I corrected *"C's sweep predates my commit"*
to its negation and **both were unwarranted** — the warrant, a commit timestamp read as a measurement
time, was identical and I only ever checked the direction.

---

## P-9 · SYNTHESIS AFTER PEER CRITIQUE

**OBSERVED.** Three first passes composed into an account no single pass contained: my readout
mismatch, A's S9A result, C's metabolic route, closed by C's dosage dissociation.

**WHY IT HELPED.** It is the only output of the run that peer interaction *created* rather than
corrected. Each leg is weak alone and they compose.

**EVIDENCE, INCLUDING AGAINST ITSELF.** Phase IV then took two legs apart — the dosage dissociation
does not discriminate (`CLAIM 032`), and the S9A pivot rests on a prediction neither paper tested.
**A composition is not corroboration**; three independent findings pointing the same way can share a
single unexamined premise, and here two of three did.

**RECURRING.**

**CANDIDATE.** `CONTRACT`, with the caveat attached. **CANDIDATE FOR PROMOTION.**

---

## P-10 · HOSTILE SCIENTIFIC REVIEW

**OBSERVED.** I was designated reviewer, objected to my own designation on scope, and the objection
changed the design: I review everything except what I originated; C reviews what I originated.

**WHY IT HELPED.** A single-reviewer design loses its adversarial property exactly where the reviewer
is the source. **Drawing the recusal list is the load-bearing act**, and drawing it narrow is
self-serving in a way that is visible, so it has to be published and contestable.

**EVIDENCE, AND THE FAILURE IN IT.** 🔴 **C caught that I used two criteria and applied each in the
direction that favoured the actor choosing it.** I diagnosed A's position with *having been corrected
by C* and recused myself on *having originated*. By my own L-7 criterion I was the worst-placed actor
to challenge C — C had corrected me three times — and I challenged C three times anyway, and those
were my best attacks.

**The resolution, which I owe rather than the concession:** the two criteria measure different things.
*Having been corrected* predicts **omission** — a failure to challenge — not unsoundness in a
challenge actually made. Applied to A it explained why three C-propositions entered consensus
unchallenged, and it was confirmed when I then found attacks on exactly those three. So the criterion
holds and **I should have said which one I was applying and why it differed.** Two criteria, silently,
each favouring its chooser, is the defect; the asymmetry itself was defensible and undeclared.

**Also observed:** two recused propositions ended **un-attacked by any actor** — I had originated
them, C recused under the symmetry rule, and A declined because putting the synthesiser in the
reviewer's seat reproduces the routing defect one step later. **That is the right call and it leaves
a real hole**, marked as a hole.

**And the review audited itself.** Enumerating the object first — 40 numbered propositions — found
that I had rejected the milligram argument in I-5 and left it standing in F-4 and F-5, the two
falsifiers built on it. Found by measuring coverage, **not** by rereading; rereading would not have
caught it, because the review felt complete.

**RECURRING.**

**CANDIDATE.** `ROUTING` + `CONTRACT`: recusal by origination, published and contestable; **and the
criterion must be declared, because an undeclared criterion drifts toward its author.**
**CANDIDATE FOR PROMOTION.**

---

## P-11 · GRAPH CONTRIBUTION

**OBSERVED.** Twenty edges; ten carry no proposition at all (7 bare wikilinks, 3 bare see-alsos);
of the ten that do, one is causal and one is a contradiction about a relation's sign.

**WHY THE INSTRUMENT FAILED.** Four governed tokens, **one gloss** — `DIRECT`, *"the same experiment
measures both endpoints"*. `ASSOCIATED` has a single **negative** constraint —
*"an `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`, and nothing downstream is allowed
to read it that way"* (`pathograph.py:153–156`, re-emitted at `:1117`) — **which prohibits exactly
the inference A and I both made**, and nothing enforces it because validation is membership-only.
The failure was foreseen, written down, published into the generated surface, and not applied.

**EVIDENCE.** Nodes carry `epistemic_type`; edges carry none, so *"contributes to"* and *"**may**
contribute to"* serialise identically — and *"may"* is the most important word in `CLAIM 016`'s
title. Meanwhile the registry already writes relation qualifiers in **17 distinct free-text strings
across 9 of 70 paper records** — `refutes its imported premise for the mouse`, `bounds its imported
premises`, `supplies the functional assay`, `tensions` — all flattened by the assembler into one
`claim_links` kind.

**THE DECIDABLE PART, WHICH IS NOT NOTHING.** `NOT_DIRECT` is decidable against the published
criterion **for all twenty edges today** — trivially for the three with no shared paper, and by A's
method for the seventeen with one. *"Edges carrying a declared relation type: 0"* is not uniformly
undoable; part of it is bounded work someone can finish.

**RECURRING.**

**CANDIDATE.** `CONTRACT`: oblige the Scientist to **report the vocabulary gap with instances** and
forbid filling it. `VALIDATOR`: enforce the negative constraint that is already written.
**DO NOT PROMOTE** any new relation token — §16 forbids it and the run demonstrated why: two actors
independently invented compatible semantics for an empty label and called it convergence.

---

## P-12 · CLOSURE AND HANDOFF

**OBSERVED.** A handoff naming commits, artifact refs, exact sources with fingerprints,
`OBSERVATION_SCOPE`, unresolved items, and what is owed to which actor — with an explicit
`scope_rule` that unadjudicated work is **undone, not out of scope**.

**WHY IT HELPED, AND WHERE IT SLIPPED.** A's handoff frontmatter said *"the eight edges left
unadjudicated"*; the eight are the **not-adjudicable** ones, while nineteen were left and **twelve
were adjudicable**. The scope rule named the blocked set and omitted the set a later reader would
quietly retire as done. **A under-claimed its own remaining scope, in the one line a packet quotes.**

**RECURRING.** Summary fields drift from the bodies they summarise; this run found the same shape in
`CLAIM 016`'s `Summary` versus its own later block, and in the working-model mirror versus its claim.

**CANDIDATE.** `VALIDATOR`: check frontmatter counts against the body. **CANDIDATE FOR PROMOTION** —
it is mechanical, and three instances turned up in one day.

---

## P-13 · DETECTING TRANSPORT VERSUS READING FAILURE

**OBSERVED.** The single most useful distinction of the run, and I got it wrong first.

**WHY IT FAILED.** I reported the Wang manifest as matching **2 of 9** locators strictly, diagnosed
markup whitespace, and concluded a legacy-manifest defect class was confirmed. A re-derived and got
**9 of 9**. Stripping tags to *empty* gives 9/9; stripping to a *space* gives 2/9. **My own
substitution inserted the whitespace I then diagnosed.** A reading failure reported where there was a
transport failure — and the transport was mine.

**THE GENERAL FORM.** I had run a negative control and it passed. **A negative control tests whether
a comparison is trivially permissive. It cannot test whether the surface compared against is the
right surface.** The missing control is to derive the surface a second, different way and see whether
the number moves.

**EVIDENCE — the class, and it is the largest finding of the run.** *"I chose the instrument, and the
instrument decided what I was counting."* Eight instances, four actors, one session: mine — tag
stripping; `DIRECT`/`ASSOCIATED` matching 56 and 44 of 57 refs as ordinary English; a regex anchored
`^| CLAIM ` missing the one **bolded** row that mattered; and a commit timestamp read as a
measurement time, **twice, in opposite directions**. C's `^learning/` sweep against an actor writing
to `reviews/`. C's worktree-confined Pathograph sweep. The Orchestrator's `PHASE2` filename sweep
matching canonical `dismech_phase2_*` files. **And one in the agreed layer**: the milligram comparison
that all three actors accepted into consensus.

That last one is the worst. **The class had been observed only in individuals until it appeared in the
consensus, which is what the process was supposed to add.**

**RECURRING.** Eight times in one day.

**CANDIDATE.** `SKILL` + `CONTRACT`: enumerate the population with an instrument that *cannot express
the property being hunted*, then measure into it; and before publishing a number that depends on a
transformation you wrote, derive it a second way. **CANDIDATE FOR PROMOTION**, and it is the one item
here I would promote first.

---

## P-14 · SELF-CORRECTION AS AN OBSERVED PRACTICE

Recorded because the Orchestrator asked me to weigh my own material rather than take his weighing.

**OBSERVED.** Four self-corrections plus a retraction: the 2/9 finding withdrawn outright; the edge
type revised twice (`INDIRECT…` → `ASSOCIATED` → `NOT_DIRECT`); *"disproven"* → *"unsupported"*;
*"already corrected"* → *"half-corrected"*; both timing claims withdrawn; an over-correction of my own
§4 withdrawn; and a gap in my own hostile review found and closed.

**WHICH ONE IS CATEGORICALLY WORSE, AND WHY.** The others were wrong numbers about objects. One was
an **attribution**: I explained *why a peer had missed my artifact* without running the two commands
that would have settled it. A wrong number about a file is a wrong number; a wrong number about why a
colleague missed something is a claim about their conduct. **It was also wrong in the generous
direction, which is why nobody caught it** — an exoneration reads as fairness and gets no scrutiny.

**AND ONE THING I DECLINED.** I refused a correction I did not need: the Orchestrator apologised for
a qualifier that was misattached in his message and not in mine, and I had measured the intersection
myself before writing. **Accepting a correction you did not need is the mirror image of the failure
being catalogued** — it puts a false defect in the record against you and makes the record less
accurate in the direction that looks humble.

**RECURRING.**

**CANDIDATE.** `CONTRACT`: self-correction is expected and costless; **and it carries the burden of
the claim it replaces**, so a retraction needs the same warrant as an assertion.
**CANDIDATE FOR PROMOTION.**

---

## WHAT I WOULD NOT PUT IN A CONTRACT

- **Any relation vocabulary.** §16 is right and this run showed why.
- **Any obligation to reach a relation.** *Unsupported* was the majority verdict on twenty edges and
  must stay costless to write.
- **"Independent adjudication" as a phase name** — P-1. Say *independent re-derivation from primary
  artifacts* and the phase becomes deliverable.
- **A scoring rule that rewards revision volume.** C warned it measures who published most, which
  measures who left the most addresses. My four self-corrections are not four units of virtue; the
  first of them was a finding I should not have published.

## WHAT REQUIRED WHICH ACTOR

- **Another Scientist:** the 2/9 retraction — A derived the surface differently and I could not have.
  The `ASSOCIATED` criterion problem — C refused an agreement two of us had already reached.
- **Mirror, not Scientist:** independence certification; whether the propagation defects are one
  systemic weakness; whether the leak class is a process failure.
- **Orchestrator:** the untracked workset; five missing full texts; producer designation; and — his
  own finding — that **low stake and directional deference are not the same property**, which is the
  routing defect my L-7 answer surfaced and which he recorded as his rather than A's.
- **A new actor:** nothing here justifies one. Every integrity finding was made by a Scientist doing
  something else, and every one is mechanically detectable. That argues for checks in the gate, not a
  new seat — and *"we found defects, therefore we need a reviewer"* is the tempting and wrong
  inference, since an actor that reads prose is exactly what failed here, repeatedly.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it, and
`roles/scientist.md` was not edited.*
