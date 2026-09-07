# PHASE I — Scientist operating-practice observations

**Actor:** Scientist A, worktree `lettore`. **Status:** NON-CANONICAL evidence for later
Plan/Mirror analysis. The dispatch says explicitly: *record evidence, do not redesign the role
contract during the scientific task.* Nothing here is a proposal to edit a contract.

Every observation below is tied to something that actually happened in this session. Where I have
no evidence, I say so rather than filling the heading.

---

## WHAT HELPED SCIENTIFIC QUALITY

**1 · Measuring the population before measuring anything about it.** The dispatch supplied
expected counts (~20 / ~17 / ~3) and told me to re-measure. I did — and then re-derived the same
counts *programmatically* from the inventory table crossed against the paper registry and the
filesystem. My hand count agreed. That agreement is worth nothing on its own; what it bought was
that a **third** class appeared which no hand count would have produced: four "shared evidential
paper" edges whose paper is not on this disk. The mechanical pass found a category, not just a
number.

**2 · Reading the panel before reading the sentence about the panel.** The paper's Results text
states *no result* for Fig. 7c — it names the method, cites the figure, and moves on. Everything
that panel establishes had to be read off the image. A caption-first or Results-first workflow
returns nothing here and does not notice that it returned nothing.

**3 · Deriving my own text surface, in the right order.** Strip tags to empty **first**, unescape
entities **second**. A prior session of mine got that backwards and silently deleted a
significance threshold from a legend. Re-deriving today rather than trusting a cached extraction
is what let me quote the Fig. 7c legend with confidence — and the legend is where the `n = 4,
representative` disclosure lives, which is the whole answer to dispatch question 4.

**4 · Scoping every negative to the surface searched.** *"Zero occurrences of `GSK`, `lithium`,
`Ser9`, `PTZ` in 24 pages / 17 844 characters of the supplementary text layer, 9 figure legends
read, individual supplementary panels not adjudicated."* The scoped version is usable by the next
reader; *"the supplement has nothing on GSK3β"* is not, because it hides which surface was looked
at.

**5 · Testing the negative against my own preferred conclusion.** Having found the wild-type
lithium response, the attractive move was to treat the whole GSK3β story as weak. The panel does
not support that: the Ser9 effect is ~2×, consistent across three regions, and real. Writing that
down — that my §1.3 says *no statistics*, not *no finding* — is the single correction in this
session that most changes what a downstream reader does with it.

## WHAT CREATED WASTE

**1 · No index from `PAPER nnn` to an identifier.** Resolving the thirteen shared papers meant
parsing a 6 000-line registry with a regex. The mapping is a derived fact about canonical state
and should be cached by the tool that maintains it, exactly as `CLAUDE.md` §3 requires of facts
about external databases. At twenty edges this cost minutes; at five hundred it is the task.

**2 · Two crop rectangles that missed their target vertically.** I published a recipe only after
looking at what the crop contained, so nothing wrong escaped — but the first pair were guessed
from a half-scale overview instead of measured. Cost: one cycle. Cheap here, and the same guess
against a 46%-of-page adjudication crop would not be.

**3 · Searching for a canonical task packet that does not exist.** Not waste in itself — the
dispatch requires the check, and the absence is a finding. It is waste that the check costs a
57-ref sweep instead of one lookup, because there is no registry of which surfaces are canonical
task surfaces.

## WHAT SHOULD BE MANDATORY

**1 · 🔴 An adjudicability pre-flight before any edge-typing assignment is accepted.** For each
edge: does the shared evidential paper have a local fingerprinted artifact, and a work manifest?
This session it reclassified the workset from *"17 adjudicable, 3 not"* to *"12 adjudicable now,
1 with a bare PDF, 4 whose evidence is not on this disk, 3 with no shared paper."* Without it, a
scientist starts an edge and discovers four papers in that the work cannot be done — or worse,
types the edge from prose about a paper instead of the paper.

**2 · 🔴 A first pass is not recorded until it is committed.** At session start my own first pass
existed only as an untracked file; Scientist C's still does; Scientist B's commit message names
the identical problem in its own words. Three actors, one failure mode, independently. Untracked
files are the surface no gate inspects, and "durably recorded" in a phase gate has to mean
something a peer can address.

**3 · Denominators on every negative.** Already repository doctrine; it earned its place three
times in one session.

**4 · The layer partition, produced as output rather than held in the reader's head.**
ENTITY / OBSERVATION / RELATION / HYPOTHESIS / INTERVENTION / PHENOTYPE. Producing it forced the
finding that *"GSK-3β inhibition suppresses seizures"* is an **intervention→phenotype** edge
wearing a mechanism edge's name — which is the same defect, in a different vocabulary, that the
pilot found in the downstream representation.

**5 · Verify the addressee of a dispatch before acting on its role assignments.** The dispatch
attributed the existing pilot to Scientist B. It was right about B *and* incomplete: a second,
independent pilot existed in my worktree. Checking cost two commands and prevented me from either
disowning my own first pass or wrongly assuming I was B.

## WHAT SHOULD REMAIN TASK-MODE SPECIFIC

- **Figure adjudication at native resolution and the crop-recipe publication.** Mandatory when a
  result depends on a panel; pure overhead when it does not. It is a property of the *evidence*,
  not of the role.
- **Re-deriving a text surface.** Needed where a cached surface's provenance is unknown or where
  quotes will be published; wasteful where a validated schema-v2 manifest already carries verified
  locators against a matching fingerprint.
- **The depth of a read.** This session used a *targeted verification read* of `PAPER 056` —
  locators re-verified, the passages the edge turns on read in full, no receipt emitted, no
  reading debt cleared. That is the right depth for edge typing and the wrong depth for a claim
  promotion. The mode belongs in the task, not in the contract.

## WHAT SHOULD BE A REUSABLE SKILL

**1 · 🔴 The edge adjudicability triage.** It is mechanical: edge table × paper registry
identifiers × `files/fulltext/` × `deepdive_manifests/` → one of four classes. No judgement
enters it. It should be a script emitting a cached artifact, not a paragraph a scientist writes
by hand — and by `CLAUDE.md` §3 a fact of this shape is *derived and cached, never
hand-declared*. It also self-maintains: the four unreachable papers reclassify automatically the
day their artifacts land.

**2 · The claim-title decomposition scan.** The inventory already lists the 18 relational titles;
turning one into `(latent source, latent relation, latent target, latent condition, would
decomposition change meaning?)` is a repeatable reading procedure and produced DC-1 to DC-3 here.

**3 · The layer partition template.** Six rows, one table.

## WHAT SHOULD NOT BE IN THE SCIENTIST CONTRACT

- **Which worktree is which actor.** That is addressing, and it belongs to the control plane. It
  currently sits in the contract's own frontmatter, where an actor reads its own identity out of
  the document whose authority is what is in question.
- **Named tools and versions.** PIL, `fitz`, a converter, a resampling filter — these age, and a
  contract that names one is a hand-pinned constant in prose. The requirement is *deterministic
  extraction, fingerprinted artifact, re-executable recipe*; the tool is the task's business.
- **Numeric thresholds tied to today's corpus size.** 39 claims, 20 edges, 64 manifests. Any rule
  keyed to those is an alarm that goes quiet at scale.
- **Anything that lets a scientist adjust the workset to what it can reach.** The four unreachable
  papers are a finding to report, never a reason to redraw the boundary of the task.

## WHAT REQUIRED ANOTHER SCIENTIST

**Nothing in Phase I — and that is the design working.** Independence is the product; if Phase I
had needed a peer it would have failed as Phase I.

What requires another scientist is **Phase II, and it is blocked**: Scientist C has recorded no
first pass on this paper. I did not read Scientist B's pilot. The one thing I would most like to
know — whether an independent reader also found the wild-type lithium response, and what they
made of Fig. 7c's absent statistics — is exactly the thing I must not look up yet.

Worth recording for whoever designs the next round: **A and C were dispatched to adjudicate the
same paper, and C read a different one.** Whether that was a routing failure or a deliberate
re-scope is not visible from here, and it is not a scientific question.

## WHAT REQUIRED MIRROR RATHER THAN SCIENTIST

1. **Whether two `PROPOSED` design artifacts authored by a Scientist belong under
   `framework/protocols/`.** They sit on a canonical-looking path with non-canonical frontmatter;
   a future reader finds them by location. I flagged and did not move them — placement of a
   framework artifact is a governance judgement.
2. **Whether the untracked-surface pattern is systemic.** Three actors, one failure mode, plus a
   whole pathograph toolchain living on 0 of 57 refs. That is a process-integrity question.
3. **Independence verification.** I assert I did not read peer artifacts. My assertion is not the
   evidence; the transcript is. Self-attestation of independence is precisely what an auditor
   exists to not accept.
4. **Whether this session's conclusions are right for the right reasons.** Artifact 02 reaches a
   conclusion (`ASSOCIATED`, not `INDIRECT_UNKNOWN_INTERMEDIATES`) that happens to align with the
   preserved pilot's scepticism. Alignment is not confirmation, and I am the wrong actor to check
   whether I found a new reason or dressed up an old one.

## WHAT REQUIRED ORCHESTRATOR

1. **The Phase II gate.** Blocked on C's missing first pass. A scientist cannot route around it
   and must not.
2. **Acquisition tasks** for the five papers that block six edges: PMID 29808465 (blocks three
   edges, and `CLAIM 019` is `consolidated baseline`), 24369382, 24456803, 30361190, 27495153.
3. **Whether to re-scope the pilot** from 20 edges to the 12 that are adjudicable today. That is
   scope, which §15 assigns to Orchestrator. I measured it and did not decide it.
4. **Whether `pathograph_inventory.md` is the canonical task surface**, given it exists on no ref.

## WHAT, IF ANYTHING, JUSTIFIES A FUTURE NEW ACTOR

**On this session's evidence: nothing.** Stated plainly because the honest answer to this heading
is usually "nothing" and the tempting answer is always "something".

The two gaps found are real and neither is a new role:

- **Artifact acquisition** — five missing full texts. Existing capability (`find-fulltext`), no
  new actor.
- **Registry↔graph reconciliation** — DC-1 to DC-3, the `CLAIM 016` internal inconsistency, the
  registry/mirror wording divergence. Integration work, and the repository already separates
  proposing from integrating.

Manufacturing an actor out of one session's friction is how a soft routing signal fossilises into
a specialisation, which is the thing Mirror is told to guard against. If a case exists it should
be made from a pattern across sessions, not from this one.

---

## Postscript — the session's own methodological finding

Three of the mismatches recorded in artifact 01 §4.3 have the same shape: **the claim and its
qualification sit on different surfaces, and nothing reads them together.** The figure title
asserts causation no panel tests. The Results text is empty where the panel carries the evidence.
The downstream representation quotes an abstract sentence whose qualification lives only as ink
in a panel. And in our own registry, `CLAIM 016`'s `Summary` says one thing while a later block
of the same record says that wording is wrong.

That is not four coincidences. It is a structural property of how scientific claims are stored —
in papers and in this repository alike — and it predicts where the next error will be found:
**wherever a summary field and an evidence field of the same object are maintained by different
acts.** It is testable, and testing it does not require new evidence, only a pass over the
records that already exist.

---

*Non-canonical. Nothing here is medical advice.*
