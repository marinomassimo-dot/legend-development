# Orchestrator operating practice — observed in the PMID 32000863 team pilot

> **Non-canonical.** Observed practice from one operator-directed run, recorded as evidence for
> a later role-contract repair. It is **not** a draft contract and `roles/orchestrator.md` is not
> edited here. No lease, no role activation, no `BATCH_COMMIT`, no canonical mutation.
>
> **Public edition.** The human role is `Operator`. Nothing here is medical advice.

Session `legend-public-49`, 2026-08-25. Five peer actors: three Scientists (`lettore`,
`lettore-b`, `lettore-c`), Plan (`evidence-index`), Mirror (`mirror`, not engaged — §14 holds
it until Phase V).

Format per item: **observed behaviour · why it helped or failed · evidence from this run ·
recurring or one-off · candidate class · promotion verdict.**

---

## 1 · Route only what routing can change; measure the rest

**Observed.** Three actors reported irreconcilable views of one repository and it was framed to
me as a possible scientific disagreement. I did not route it. I measured it, and it dissolved.

**Why it worked.** `pathograph.py` was present in **0 of 57 refs**, positive control `CLAUDE.md`
in **56 of 57**. Scientist B had reported `0/50` and Scientist C `0/57`. Both were true
negatives against nested ref sets — `50 = 44 heads + 6 remotes`, `57` adds 5 tags, the stash and
a codex checkpoint; C later proved the nesting with `comm -23` returning empty. There was never
a disagreement to adjudicate. Routing it as one would have consumed two Scientist passes and
produced a reconciliation of two correct numbers.

**Evidence.** My sweep, plus B's and C's independent confirmations, plus Plan's `50 of 50`
against a third denominator — four measurements, one object, zero conflicts once each carried
its denominator.

**Recurring.** Yes. This is the second failure mode of the same shape in this run (see §4).

**Candidate.** Routing rule + validator. *CANDIDATE FOR PROMOTION.*

> A disagreement between numbers is not a disagreement until each number carries its
> denominator and its population. Orchestrator's first move on a reported conflict is to
> re-derive both, not to convene the parties.

---

## 2 · A negative needs a positive control, or it is not a measurement

**Observed.** Every absence claim in this run carries a control. `0 of 57` for the Pathograph is
only meaningful beside `56 of 57` for a file that must be there.

**Why it matters.** Without the control, `0 of 57` is indistinguishable from a sweep that cannot
return a hit at all — a mistyped path, a shell-quoting bug, a wrong root. C independently
carried one (`roles/scientist.md`, 36/57) and B carried one (`WWOX`, 50/50). All three of us
arrived at the same discipline separately, which is what makes it a convention rather than a
preference.

**Evidence.** The one absence claim in this run that had **no** control was mine and it was
wrong: I inferred from a hash sweep that the supplementary PDF and Figure 7 had no canonical
anchor. Both are anchored — in the deep-dive manifest. I had searched and misread the result.

**Recurring.** Yes.

**Candidate.** Validator. *CANDIDATE FOR PROMOTION.*

---

## 3 · Do not accept a peer's routing fact; re-derive it

**Observed.** Scientist A reported, as a routing fact offered to me rather than a scientific
claim: *"Scientist C has no first pass on PMID 32000863 and holds 0 commits ahead of main."* On
that basis A had measured the Phase II gate as CLOSED.

I checked. `git rev-list --count main..lettore-c` → **1**. The first pass exists — blob
`4be1f97`, 41,547 bytes, committed `c55c25c` at 15:37:28, nine minutes *before* A's own commits.
The gate was open. Had I relayed A's fact, the pilot would have stalled on a false negative
produced by a careful actor acting in good faith.

**Why it happened, and why it is a class.** C made the mirror-image error, sweeping `^learning/`
for peer artifacts while B writes to `reviews/scientist-b/`. Both let an existing directory
convention define a population instead of enumerating it. Neither error is carelessness; both
are the same defect wearing different clothes.

**Recurring.** Yes — twice in one run, by two different actors, in opposite directions.

**Candidate.** Contract clause + routing rule. *CANDIDATE FOR PROMOTION.*

> An actor's report about **another actor's state** is a lead, never a fact. Cross-actor state
> is Orchestrator's to measure, because only Orchestrator has a reason to look at all of it.

---

## 4 · The transport failure was structural, and reading it as a reading failure cost three passes

**Observed.** The pilot had stalled on what looked like inconsistent competence: A worked "from
related surfaces", B and C measured zeroes, Plan alone held the paper.

**The mechanism, and it is design.** `.gitignore:7` excludes `files/` entirely under a privacy
hard-guard, and the same file states the rule at lines 11–18: *"publish the derivation, not the
derived."* **Primary evidence cannot travel by git.** A branch carries the manifest that names
and fingerprints the evidence; it does not carry the evidence. Measured: A held 34 full texts and
not this one, B held 13 and not this one, C held 0, `evidence-index` held it by an
unreconstructible manual copy. Every actor was correct about the tree it stood in.

**What made it invisible.** The deep-dive manifest is byte-identical (`c7e27e72…`) in all seven
worktrees. So the surface that *names* the evidence transports perfectly while the evidence
itself transports not at all — and an actor holding a valid manifest has every reason to believe
it holds the study.

**The repair, and it was already written down.** The manifest's own note had diagnosed this on
2026-08-10: *"the FOUR MAIN FIGURES WERE INSPECTED AT READING TIME AND NEVER PERSISTED … It is
the `files/` rule from the other side — the manifest survived, the evidence did not travel with
it."* The diagnosis sat in a tracked file for fifteen days and changed nothing, because nothing
executes prose.

**Recurring.** Structural, permanent, and will recur on every paper until a mechanism exists.

**Candidate.** Tool. *CANDIDATE FOR PROMOTION.* A `provision-evidence` step that reads
`source_artifacts` from a manifest, places the bytes into a target worktree's ignored `files/`,
and verifies each digest — the operation performed by hand here.

---

## 5 · Declare the digest, not the route

**Observed.** I asked Plan how the evidence had reached its worktree, intending to reuse the
route. Plan refused to reconstruct it: it had run no copy, the route predated its session, and
inode comparison proved only that the two files were distinct objects with identical content.
Instead it said: *declare the digest, not the route.*

**Why it is the better artifact.** The route is unverifiable and not what makes the evidence
sound. The digest is checkable from any tree against a tracked, chain-anchored record —
`FTR-20260804-32000863-01`, `source_fingerprint 792b5b29…`, plus `source_artifacts` in the
manifest. I adopted it verbatim as the packet's design.

**The hazard it also surfaced.** A re-fetch of the same article from PMC is reported to return a
**different** snapshot — `7d235c00…`, 158,798 B against 156,335 B. Re-fetching rather than
verifying would have produced an evidence set that fails its own manifest. A mismatch there is a
finding, not a retry.

**Candidate.** Protocol clause. *CANDIDATE FOR PROMOTION.*

---

## 6 · Place the bytes, but make the receiver verify them

**Observed.** I copied the four declared artifacts into three Scientist worktrees, after running
`git check-ignore -q files/` in each **before** writing and confirming `git status --porcelain --
files/` was empty **after**. No tracked surface created; no branch reachable. Then I told each
Scientist the expected digests and instructed them not to trust the placement.

**Why the second half matters more than the first.** Two Scientists verified independently and
reported all four matching. One of them — C — had detected the placement before my message
arrived (*"provisioned by someone else after my reading, mtime 16:54"*) and fingerprinted it
rather than assume. That is the correct reflex, and it only has something to check against
because the identity was declared first.

**Failure on my side, and it is mine.** I placed the files before announcing it. C had to
discover an unexplained mutation of its own working tree and reason about whether it was an
integrity event. Announce first, then place.

**Candidate.** Routing rule. *CANDIDATE FOR PROMOTION.*

---

## 7 · Independence can be absent before any actor spends it

**Observed.** The pilot was designed around protecting Scientist independence, and §5 treats it
as already spent by peer contact. Both framings understate the problem.

**Evidence, found by Scientist B and verified by me.**
`disease-models/wwox/analysis/locator_contract_live_test.md` has been **tracked since
2026-08-04**. Lines 375–395 contain, in prose: *"Figure 7d has three panels … lithium suppresses
seizures in all three"*; *"Figure 7b marks it non-significant in +/+ and +/− and significant only
in −/−"*; *"'Elevated' is the wrong word … dis-inhibited, not more abundant"*; the premise tag on
*"lithium is a GSK3β inhibitor"*; and the alternative-mechanism argument from the paper's own
Discussion. CLAIM 016's Evidence boundary carries the same conclusions, propagated 2026-08-10.

⇒ **No Scientist reading this paper through this repository could be independent of the
repository's own conclusion about it.** Independence was not spent by peer contact. It was never
available. What the pilot measured was re-derivation of a recorded answer — worth measuring, and
not what the design says it measures.

**Consequence for Orchestrator.** Withholding peer outputs is theatre unless the tracked tree has
been swept for the same conclusions first. Blindness is a property of the **whole reachable
surface**, not of the actor-to-actor channel.

**Recurring.** Yes, and it will worsen: every propagated claim makes the next reading of that
paper less independent.

**Candidate.** Contract clause + tool. *CANDIDATE FOR PROMOTION.* Before dispatching a reading,
sweep the tracked tree for the paper's identifiers and hand the actor the list of surfaces that
already state conclusions about it — so contamination is disclosed *by construction* rather than
discovered in hindsight.

---

## 8 · The commit-subject convention defeats the quarantine, structurally

**Observed.** This repository writes findings into commit subject lines. `lettore-c@c55c25c`
reads: *"The panel was read before the claim that cites it, and the citation points at the wrong
panel."*

**Why it defeats the quarantine.** §3 requires checking whether peers have produced artifacts.
That check is `git log`. So the mandated existence check cannot be performed without reading
peers' conclusions. As Scientist B put it: *any actor obeying both instructions is contaminated
by the act of obeying.*

**Evidence.** Three independent hits in one run — B read C's subject line, C read B's filename,
and I read C's subject line while verifying A's routing claim.

**Candidate.** Protocol clause. *CANDIDATE FOR PROMOTION.* Mitigations exist (`ls-tree
--name-only` only; a non-adjudicating actor performs the check; suspend the subject-line
convention during a blind phase). None is adopted here — this run records the class.

---

## 9 · Preserve the object with its wiring, or preserve a regression

**Observed.** I enumerated the Pathograph work as four untracked files. Plan corrected the object
from Mirror's own frontmatter: *"4 new + 5 modified"*. Three of the five are wiring —
`run_release_regressions.py` registers the test, `test_cli_smoke.py` registers the CLI, and
`prompt_batch_commit.md` adds the regeneration to a **normative** phase of `BATCH_COMMIT`.

**Why it was load-bearing.** Preserve the four without the three and the tool is unregistered
with any suite. Preserve the three without the four and the release battery names a test that
does not exist. Committed as one change set, `d422829`.

**Candidate.** Preservation rule. *CANDIDATE FOR PROMOTION.* The unit of preservation is the
change set the reviewer reviewed, not the file list the preserver noticed.

---

## 10 · Verify the baseline in the same population, or the regression hides

**Observed, and this is my worst error of the run.** After preserving, the release battery
returned **FAIL**. I compared against a baseline worktree at `30cb4f3` which showed 6 failing
suites against my 8, and my first reading was that 6 pre-existed and 2 were new. That reading was
right by luck: the baseline worktree had **no sibling worktrees on disk**, a different population,
and the comparison could equally have hidden a regression instead of revealing one.

Re-run properly — clean trees at both commits — it was unambiguous: 6 at baseline, 8 at my HEAD,
and both new suites **passed** at baseline. I caused them. Seven references across three
preserved documents, three classes: four prose (`./file.py` illustrating that mode 644 launches
nowhere), one genuinely stale (`record_conventions.py` does not exist; the file is
`test_record_conventions.py` — the scanner was right and the audit was wrong), two citing a
sibling worktree by full path. Repaired in `f7c0795`; a clean tree at the repaired HEAD returns
exactly the 6 baseline failures.

**Candidate.** Validator. *CANDIDATE FOR PROMOTION.* A before/after comparison is only valid when
both sides are measured in the same population. State the population with the verdict.

**A framework finding, recorded and not repaired.** Every remaining hit in those two suites comes
from `.claude/worktrees/**` and `backup/**` — both gitignored, one of them five sessions' private
working trees. The release battery walks the filesystem into them and reports their contents as
defects of this repository. A prior session had already written this down, inside one of the
files preserved here — *"IGNORED, and the suite scans it anyway"* — and it survived as prose
because nothing executes prose. Changing what the release gate scans is architecture, and this
run's authorization covers preservation. *DO NOT PROMOTE YET.*

---

## 11 · Coordinate the graph without authoring the biology

**Observed.** I read four locators of the 25 and stopped. Enough to build a task frame and to
confirm two defects mechanically; not enough to form a view on the biology.

**Why the line sits there.** Two defects are **mechanical** — a pointer and a wording drift — and
verifying them requires comparing two records, not judging evidence:

- **Panel pointer.** CLAIM 016's Evidence-boundary block cites **Fig. 7b** for the lithium
  result. The manifest anchors lithium to **Figure 7d** (entry 0) and Figure 7b to ethosuximide
  (entry 1). The claim attributes the lithium finding to the panel carrying the ethosuximide
  finding — and the tracked analysis file it derives from has it *right*, so this is a
  propagation error, not a reading error.
- **Abundance/activation drift.** CLAIM 016's `Summary` still reads *"GSK3β is elevated"* while
  manifest entry 2 records total GSK3β **flat** across all genotypes and regions. The same record
  corrects itself further down. The drift is *within one record*, between its summary and its own
  mechanism block.

Whether lithium's effect licenses a causal edge to GSK-3β is **not** of that kind, and I did not
touch it. Recorded as findings under §13; nothing propagated.

**Candidate.** Contract clause. *CANDIDATE FOR PROMOTION.* Orchestrator may adjudicate
record-to-record consistency and must not adjudicate evidence-to-claim sufficiency.

---

## 12 · Low stake is not directional neutrality — the producer selection was wrong in a way nobody could see from inside it

**Observed.** I selected the reconciliation producer on the criterion the dispatch specifies —
independence and conflict position — and chose the actor holding the lowest stake: both its
contested positions withdrawn, no prior synthesis to defend. I recorded the reasoning, including the
argument against. The producer then flagged, in its own document, that it could not answer whether
this under-preserved dissent *against one specific peer*, and left the question open rather than
resolving it in its own favour.

**The hostile reviewer answered it: yes, mildly, and specifically.** Three propositions originating
with one actor entered the consensus layers **without a recorded challenge**, and three of the
reviewer's five landed attacks were against exactly those three.

**The mechanism, in the reviewer's words, and it is mine:**

> The mechanism is routing, not care. **An actor corrected by C three times is the worst-placed
> actor to challenge C's fourth claim.**

**Why I missed it.** Low stake is what I measured. But that low stake had been *produced* — by the
actor being corrected, repeatedly, by one particular peer. **A producer that withdrew both contested
positions *to a specific actor* is not neutral with respect to that actor, whatever its total
stake.** I treated "has nothing left to defend" and "has no direction of deference" as one property.
They are two.

**Evidence.** The reviewer could not break the selection on any other axis and said so — the
reconciliation preserved a dissent *against* the actor whose position had prevailed, marked
single-actor items as such, declared its conflict in the first paragraph, and left the open question
open. The defect is not in the producer's diligence. It is upstream, in mine.

**Recurring.** Structural. It will recur wherever a producer is chosen for low stake in a group
where positions have converged.

**Candidate.** Routing rule + validator. *CANDIDATE FOR PROMOTION.* The repair already exists one
step later in this same run: the hostile reviewer recused itself from what it had originated. The
same logic applies to the producer, one step earlier — and the deference is measurable, because
*who withdrew what to whom* is written in the Phase II artifacts.

---

## 13 · The un-attacked pair, and why I refused to fill the hole

**Observed.** The Phase-IV split left two propositions reviewed by nobody: one Scientist recused
under the symmetry rule it had itself volunteered, and the other had originated them. The recusing
actor asked explicitly that they not be made to look reviewed.

**What I refused.** Routing them to the synthesiser — the only remaining actor. That would have put
the synthesiser in the reviewer's seat one step after the routing defect above, reproducing it
exactly. The synthesiser independently reached the same conclusion and declined.

**What was done instead.** They are marked `UN-ATTACKED — no actor was positioned to review this`,
with the reason, in their own item under open disagreements. Not folded into a reviewed layer.

**Why this is the finding and not the failure.** A three-actor group with a recusal rule cannot
always produce three independent reviews, and the honest output is a declared gap. **An acknowledged
hole is a result; a laundered one is the failure this entire run spent the day cataloguing.**

**Candidate.** Contract clause. *CANDIDATE FOR PROMOTION.* A review phase needs a vocabulary for
"nobody was positioned to check this", or the coverage it reports will always be the coverage it
wishes it had.

---

## 14 · The class reached the consensus layer, which is what the process was supposed to add

**Observed.** *"I chose the instrument, and the instrument decided what I was counting"* — eight
instances across four actors in one session, mine included.

🔴 **Seven were individual. The eighth was in the agreed layer.** The reconciliation justified
withdrawing a comparison with `3 × 60 = 180 mg/kg` against `150 mg/kg` — a comparison **in
milligrams between a monovalent cation and a T-type Ca²⁺ channel blocker**. The withdrawal was
right; the stated reason licensed nothing. Three independent readers, multiple retractions each, and
the consensus still carried an incommensurable-unit argument.

**Why.** Agreement was reached on the *conclusion*, and nobody re-derived the *argument*. Every
actor had already agreed the contrast should be withdrawn, so the sentence justifying it was read as
a summary rather than as a claim.

**Consequence for Orchestrator.** Peer review as run here catches wrong conclusions well and wrong
warrants for right conclusions badly. Two independent instances in one day — this, and a corrected
timing claim whose correction checked the direction and never the warrant. **A conclusion everyone
accepts is exactly where nobody looks at the reasoning.**

**Candidate.** Protocol clause. *CANDIDATE FOR PROMOTION.* A consensus layer needs its *arguments*
re-derived, not just its conclusions ratified — and the cheapest form is that whoever agrees last
states why in their own words rather than assenting.

---

## 15 · What I got wrong

Recorded because §17 says failures are data and the history is not to be optimized.

1. **Placed evidence before announcing it** (§6). C had to detect an unexplained mutation of its
   own working tree and rule out an integrity event.
2. **Claimed two artifacts had no canonical anchor** (§2). Both were anchored in the manifest. I
   searched, misread, and asserted.
3. **Compared a regression against a differently-populated baseline** (§10), and read the result
   correctly by luck.
4. **Wrote a vacuous set operation** into three identity challenges — *"MINUS yourself"* on a set
   that already excluded the recipient. Two Scientists flagged it independently. Harmless, and it
   means the challenge was looser than it read.
5. **Under-enumerated the preservation object** as four files when the reviewed change set was
   nine (§9). Caught by Plan, from a document I already had.

Three of the five were caught by peer actors, not by me. That is the strongest single argument in
this run for the multi-actor design, and it is worth more than any item above.
