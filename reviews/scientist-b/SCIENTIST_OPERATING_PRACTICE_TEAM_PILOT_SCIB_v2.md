---
record: SCIENTIST OPERATING PRACTICE — observations from the team pilot (§13)
id: SCIENTIST_OPERATING_PRACTICE_TEAM_PILOT_SCIB_v2
supplements: SCIENTIST_OPERATING_PRACTICE_DISCOVERY_SCIB_v1 (committed 2261a15, unmodified)
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Evidence for later Plan/Mirror analysis. Redesigns nothing.
scope_difference_from_v1: v1 reconstructs the Scientist workflow from repository evidence. This
  file records only what *this exercise* produced — the independent adjudication, the edge typing,
  and the team protocol under load. Where the two agree, v1 is not repeated.
---

# What the team pilot taught, recorded as evidence and not as a proposal

§13 says: do not redesign the role contract during the scientific task. I do not. Every item below
is an observation with the incident that produced it.

---

## 1 · WHAT HELPED SCIENTIFIC QUALITY

**Extracting the declaring *sentence* instead of trusting the declaring *field*.** The export gives
each edge a `declaring_fields` label — `Wikilinks`, `Clinical meaning`, `Evidence boundary`. Those
labels made all twenty edges look comparable. Pulling the actual line that contains the wikilink
showed that **10 of 20 have no proposition in them at all**: seven are a name in a list, three are
"Vedi CLAIM NNN". That single move changed the whole adjudication from *typing twenty relations* to
*discovering that half of them have never been asserted by anyone*.

**Re-verifying artifact fingerprints before reading, not after.** All four PMID 32000863 artifacts
matched the manifest. That took seconds and it is what lets me say the panels I read are the panels
the manifest describes — rather than saying I read *the paper*, which names no object.

**Reading the figure at native resolution and again at 3× on the one row that decides.** The
densitometry row of Fig. 7c is the difference between *"GSK3β is elevated"* and *"GSK3β is
dis-inhibited"*. At half scale both readings survive. At 3× only one does.

**Verifying a causal story against observations rather than against its own plausibility.** Seven of
nine Wang 2012 locators failed a strict match. The tempting write-up is "seven bad locators". I
tested the hypothesis instead — re-ran the comparison whitespace-insensitively (9/9) and added a
fabricated negative control (not found). The finding is *"a presentation defect with one mechanical
cause; all nine locators are sound"*, which is the opposite operational conclusion.

**Running the objection against my own preferred reading.** The absence of a genotype × treatment
interaction test weakens the paper's genotype-specific reading of lithium. It weakens the
genotype-specific reading of *ethosuximide* by exactly the same argument, and that reading is the one
that makes my case look strongest. Writing both down cost one paragraph and is the only reason the
ethosuximide answer is honest.

---

## 2 · WHAT CREATED WASTE

**Finding the workset.** The task said to use the canonical packet. There is no canonical packet:
the Pathograph exists only in one working tree, untracked, and I spent the opening of the session
proving a negative across 50 refs before I could start. Not wasted effort — the negative is a
finding — but it was unbudgeted, and every other Scientist paid it independently.

**My own enumeration error.** I first wrote the §12 disposition list as five overlapping buckets that
summed to 16 of 20 edges. I caught it by adding the column. **Any classification of a fixed
population must be a partition, and the check is that it sums to the population.** This is the same
failure my own memory records from a previous session, committed again under time pressure.

**Chasing `--include=*.md` through zsh.** Unquoted glob, no matches, silent. Small, recurrent, and
the class is the one that produces silent false negatives.

---

## 3 · WHAT SHOULD BE MANDATORY

1. **A negative claim carries its searched surface, its denominator and a positive control.** Used
   throughout: *0 of 50 refs contain "pathograph", 50 of 50 contain "WWOX"*. Without the control the
   first number is indistinguishable from a broken sweep.
2. **Report state by naming the object.** Every count in my records is pinned to a blob or a commit —
   `claim_registry_current.md` at `9f4bcede`, "14 files at HEAD `8612baa`". Object-derived figures
   do not decay; population-derived ones do, and must say so.
3. **Exclude your own record from the command that reproduces its negative.** The moment I commit
   *"14 files assert X"*, my file becomes the fifteenth. Every sweep here carries
   `':!reviews/scientist-b'`.
4. **Declare reading depth per source, honestly.** I read PMID 32000863 and PMID 22193544 fully; for
   PAPER 057/058/059 I verified each endpoint's load-bearing quantity or negative verbatim and did
   not re-read end to end. Saying which is which is the difference between a record a reviewer can
   calibrate and one they must trust.
5. **If a claim cites a panel, open that panel.** The single figure-panel citation in the entire
   claim registry points at the wrong panel, and it survived a canonical propagation batch.

---

## 4 · WHAT SHOULD REMAIN TASK-MODE SPECIFIC

- **Reading depth.** Edge typing needs the endpoint quantities and the design; a deep dive needs the
  whole paper. Forcing deep-dive depth on twenty edges would have produced two edges and a debt.
- **Figure inspection.** Mandatory when a result depends on a panel; wasteful when the claim rests on
  a text-reported statistic with the test declared.
- **Multi-hop reference chasing.** Decisive for the lithium question — reference 10 is what shows the
  paper's own cited support attributes the effect elsewhere. Irrelevant to most of the edge work.

---

## 5 · WHAT SHOULD BE A REUSABLE SKILL

| Candidate | What it does | Evidence from this session |
|---|---|---|
| **Locator strict-match audit** | Match every manifest snippet against the declared artifact in strict and whitespace-insensitive modes, with a fabricated negative control; report both numbers and the diagnosed cause | Turned "2 of 9" into "9 of 9, one mechanical cause". The 32000863 manifest *predicted* this class for legacy manifests; the prediction is now confirmed on a second paper and the sweep is mechanical |
| **Panel-citation check** | For every figure-panel citation in a claim, open that panel in the declared artifact and confirm it shows what the claim says | Would have caught `Fig. 7b` at the batch that wrote it |
| **Declaration-content classifier** | For each graph edge, extract the sentence containing the cross-reference and report whether it is a proposition, a see-also, or a bare list entry | Produced the 7 / 3 / 10 split, which is the whole result |
| **Cross-surface wording drift** | Given a claim and its working-model mirror, diff the assertions | Would have caught that the mirror says *de-repression* while the claim still says *elevated* |

The first two are mechanizable outright. The third is mechanizable to the point of classification and
needs a Scientist for the judgement. The fourth needs a Scientist to decide which surface is right.

---

## 6 · WHAT SHOULD NOT BE IN THE SCIENTIST CONTRACT

- **A relation vocabulary.** §16 forbids creating one and it is right to. But the Scientist is the
  actor who discovers that the existing one does not fit — eight edges here carry real, sourced
  relations (*bounds*, *refutes the premise of*, *instantiates*, *supplies the assay for*) that
  `DIRECT / INDIRECT_UNKNOWN_INTERMEDIATES / ASSOCIATED / CONTROVERSIAL_OPEN` cannot express. The
  contract should oblige the Scientist to **report the gap with instances**, and forbid filling it.
- **Any obligation to reach a relation.** *Unsupported* is the majority verdict here and must stay
  costless to write.
- **Authority to promote a claim status.** Nothing in this session's findings — including the two
  canonical defects — should move a status without `BATCH_COMMIT` and the operator.

---

## 7 · WHAT REQUIRED ANOTHER SCIENTIST

**Nothing in the adjudication.** Every finding above is reproducible by one actor from the artifacts.

What genuinely requires a second Scientist is **the case where the first one's conclusion is already
in the tree** — see §9. A finding that agrees with what the repository already says is exactly the
finding one actor cannot validate alone, because agreement is unfalsifiable from inside.

⚠️ And it must be a *second reading*, not a second count. Two Scientists reporting "20 edges" have
verified nothing if neither compared the underlying set.

---

## 8 · WHAT REQUIRED MIRROR RATHER THAN SCIENTIST

Four items, handed over rather than acted on:

1. **The untracked workset.** That the Pathograph lives only on an ungated surface is a
   process-integrity question. I measured it; I did not move it.
2. **The independence leak (§9).** Whether a Phase I contaminated by the mandated existence check
   still counts as Phase I is a protocol ruling, not a scientific one.
3. **The wrong-reason success.** `therapy_levers.md` reaches the right word — *genotype-agnostic* —
   by the wrong derivation, and carries two overstatements with it. Scientists check whether a
   conclusion is true; Mirror checks whether it was reached for its reasons.
4. **The mirror/claim divergence.** `working_model_current.md:164` was corrected and
   `claim_registry_current.md:296` was not. That two canonical surfaces disagreed through an export,
   a blinding and a review is a propagation-integrity finding.

I deliberately did **not** open `reviews/mirror/PATHOGRAPH_HOSTILE_REVIEW_MIRROR_v1.md`, which exists
in the mirror worktree. Reading it during Phase I would import a process judgement into a scientific
adjudication, which is the boundary §14 draws.

---

## 9 · 🔴 THE PROTOCOL DEFECT THIS PILOT ACTUALLY DISCOVERED

**§3's independence rule and this repository's commit-message convention are mutually incompatible.**

§3 gates Phase II on all three first-pass artifacts **existing**. Checking existence means inspecting
peer worktrees. Running `git log --oneline -1` on Scientist C's branch returned:

> `c55c25c The panel was read before the claim that cites it, and the citation points at the wrong panel`

That subject line **states a conclusion** — the same conclusion as my own §8.1. My derivation was
complete and self-contained before the check, and I record the leak rather than let it pass.

**This is structural.** The convention here is to state the finding in the subject. Any actor
obeying both instructions is contaminated by the act of obeying. It is not a lapse and it will recur
for every actor, every phase, every time.

**Mitigations, none of which a Scientist is authorized to adopt:** check existence with
`git ls-tree --name-only` alone — which is how I checked Scientist A, whose artifacts are untracked
and therefore produced no subject line; or route the existence check through a non-adjudicating
actor; or suspend the subject-line convention for Phase I commits.

**And a second contamination that predates all three of us.** The repository already contained the
answers to the §12 questions, in a tracked analysis file and in the canonical claim itself. No
Scientist reading that paper *through this repository* can be independent of the repository's
conclusion about it. §12 therefore measures re-derivation of a recorded answer — worth measuring, and
not what the prompt says it measures. **Independence audits must test against the tracked tree, not
only against actor-to-actor contact.**

---

## 10 · WHAT REQUIRED ORCHESTRATOR

- **The workset's location.** Only Orchestrator can decide whether a task packet may live on an
  untracked surface. I could measure it and could not fix it.
- **Acquisition of the five missing full texts** (PMID 29808465, 24369382, 24456803, 30361190,
  27495153) that block six edges.
- **The `BATCH_COMMIT` for the four canonical defects.** Found, located, not applied.

Orchestrator framing risk, recorded per §15: §4 supplied the counts 20/17/3 *and* told me to
re-measure. I re-measured first and compared second; they agree. Had the instruction been only *"use
the ~20 edges"*, the count would have been inherited — as it was, the instruction to re-measure is
what made the agreement evidence instead of an assumption.

---

## 11 · WHAT, IF ANYTHING, JUSTIFIES A FUTURE NEW ACTOR

**Not a new actor. A new plane, and one existing actor already owns it.**

Eight edges carry real relations the causal vocabulary cannot express. Nine of 70 paper records
already write those relations, in 17 distinct free-text strings — `refutes its imported premise for
the mouse`, `bounds its imported premises`, `supplies the functional assay`, `tensions`,
`counter-directional`. The vocabulary exists and is unparsed; the assembler flattens all of it into
one undifferentiated `claim_links` kind.

That is **Plan's** work — a second relation plane and its governed vocabulary — and §16 forbids me
from starting it. The Scientist's contribution is what this record contains: the instances, measured,
with the count of how often each appears.

**One thing that might justify a new actor, stated as a question rather than a proposal:** every
integrity finding here — the untracked workset, the mirror/claim divergence, the propagation of a
unsupported wording through fourteen files, the panel-citation miss — was found by a Scientist doing
something else, and would have been found by no scheduled process. Whether that is a gap for an actor
or for a regression is a judgement I am not the right actor to make, and the evidence is recorded so
that whoever is can make it.
