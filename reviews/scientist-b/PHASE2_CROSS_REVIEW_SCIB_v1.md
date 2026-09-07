---
record: PHASE II — CROSS-REVIEW by Scientist B of Scientist A and Scientist C
id: PHASE2_CROSS_REVIEW_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Mutates nothing. **No peer artifact was edited, moved or rewritten** (§8).
reviewed_at_fingerprint: see §1.2 — each peer artifact is named by sha256, so this review reports
  on objects and not on decisions.
---

# Phase II — reviewing A and C, and retracting one of my own findings

> **Nothing here is medical advice.**

---

## 1 · The gate, and why I proceeded where both peers stopped

### 1.1 The gate is a race, and all three of us were right

§3 opens Phase II when all three first-pass artifacts exist. Measured from commit timestamps:

| Time (2026-08-25) | Event |
|---|---|
| 15:24:34 | **B** commits its first-pass durable — `2261a15` |
| 15:37:28 | **C** commits `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md` — `c55c25c` |
| 15:41:50 – 15:42:16 | **A** commits artifacts 00–03 — `d3fcfc0`, `17bf62c` |
| 15:43:51 | **A** commits its handoff declaring the gate **closed on C** — `5b681f2` |
| 15:46:25 – 15:49:34 | **B** commits its edge adjudication and addendum |

🔴 **A declared the gate closed on C six minutes and twenty-three seconds after C committed the
artifact that opens it.** A's handoff records C as *"0 commits ahead of `main`; all work
untracked"*; C was one commit ahead of `main` at the moment A wrote that.

**This is not an error of method.** A measured, recorded the measurement, and named it as a routing
fact for Orchestrator — which is correct conduct. The measurement simply decayed between being taken
and being published, which is what every population-derived figure does. C, measuring earlier still,
found *both* peers absent and declined Phases II–V for the same reason.

**So three actors evaluated one gate at three instants and returned three different verdicts, and
each was correct at its instant.** A phase gate defined over mutable peer state, with no barrier and
no agreed clock, cannot be evaluated consistently by the actors it gates. That is a finding about the
protocol, not about any of us.

I proceeded because at **15:49** all three artifacts existed and were durable, which is the condition
§3 states, and because the dispatch says not to route between phases through the Operator when the
authority already permits the transition.

### 1.2 What I read, named by object

| Artifact | sha256 |
|---|---|
| A · `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` | `b443526aeb760a591c2d2c09c539f2abc99712d6e93bce9f0efab9bec42d99f2` |
| A · `TEAM_PHASE1_LETTORE_00_AUTHORITY_AND_WORKSET.md` | `12fd53b8703e0cec5e8ba87a8ed1f66ea7cacf7b96e648e363bf843de60fc347` |
| A · `TEAM_PHASE1_LETTORE_01_PMID32000863_ADDENDUM.md` | `a66678addf0c3954c8ce0b72ed1f8978fa3b3b3dc1340b9587ce9382457cae31` |
| A · `TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` | `636df2d05fa1b06e61c97cddfb669bcc0c71ed18fa50c87fc5653c6a9350ed60` |
| A · `HANDOFF_LETTORE_TEAM_PHASE1.md` | `3a544f06b0f76b38a9444ad0bdd3a4a4ee89d33c192e5382403935e5b3d322a0` |
| C · `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md` | `b7c53c03a5cd32859b20b6e8f24a21ef0910c08720215e411edb77ed9533ae5b` |

A's `03_OPERATING_PRACTICE` was read for §13 material only and is not reviewed scientifically here.

**Every load-bearing peer claim reported below was re-derived by me from the artifacts before being
accepted or disputed.** Where a peer's number decided something, I recomputed it.

---

## 2 · 🔴 What I got wrong — retracted before reviewing anyone

**Scientist A refuted a finding of mine, and A is right.**

My Phase I §11 reported that the nine locators in `deepdive_manifests/PMID22193544.json` matched the
Wang 2012 JATS artifact only **2 of 9** strictly, diagnosed one mechanical cause (markup-derived
whitespace around `β` and subscripted residue ranges), and concluded that the legacy-manifest defect
class predicted by the PMID 32000863 audit note was **confirmed on a second paper**.

A re-derived the same surface and reported **9 / 9**. I tested the difference:

| Tag stripping | Strict matches |
|---|---|
| `<[^>]+>` → **space** (mine) | **2 of 9** |
| `<[^>]+>` → **empty** (A's) | **9 of 9** |

**The locators match strictly. There is no defect in that manifest. My finding is withdrawn**, and
the retraction is written into the Phase I record itself rather than only here.

I named the right mechanism and attributed it to the wrong object: my own substitution inserted the
space I then went on to diagnose. **I had run a negative control** — a fabricated sentence, correctly
not found — and it passed, which made the measurement look validated. A negative control tests
whether a comparison is trivially permissive; **it cannot test whether the surface being compared
against is the right surface.** The control I needed was the one A ran without meaning to: derive the
surface a second way and see whether the number moves.

This is the single clearest demonstration in the whole pilot of what a second Scientist is for.

---

## 3 · Review of Scientist A

### 3.1 Strongest agreement

We converge, independently and by different routes, on the four things that matter most:

| Proposition | A | B | Agree |
|---|---|---|---|
| Lithium suppresses PTZ seizures in all three genotypes | yes | yes | ✅ |
| No WWOX-specific rescue is demonstrated | yes | yes | ✅ |
| GSK-3β is not established as lithium's operative target | yes | yes | ✅ |
| Total GSK-3β is flat; what falls is Ser9 phosphorylation | yes | yes | ✅ |
| CLAIM 016 cites `Fig. 7b` for a `Fig. 7d` result | yes | yes | ✅ |
| The pS9 readout mismatch between CLAIM 016 and CLAIM 035 | yes | yes | ✅ |

The sixth line is worth pausing on. A, C and I each found the readout mismatch independently, and
none of us had it before this session. **Three independent derivations of a finding that was
available in the registry for weeks** is the strongest evidence the pilot produced that the
adjudication was real work rather than transcription.

### 3.2 🔴 Evidence A noticed that I missed

**(a) Wang 2012's S9A mutant — and it is decisive.** A's observation 7:

> *"Transfection with GFP–GSK3β WT and S9A notably decreased SH-SY5Y cell differentiation, whereas KD
> and R96A did not affect SH-SY5Y cell differentiation"*

A GSK-3β that **cannot be switched off by Ser9 phosphorylation behaves exactly like wild type** in
the assay Wang uses. I had only observation 6 — pS9 unchanged while output falls — which shows the
Ser9 axis is *not engaged*. A's obs. 7 shows it is *dispensable*, by design, with internal controls.
**That is a second, orthogonal demonstration and it converts my "readout mismatch" from an
inference into a designed result.** I did not read the mutant panel.

**(b) The operator decision on activation.** I derived the authority condition from
`roles/scientist.md` frontmatter alone. A went to
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`. **I verified it on `main`:**
it records 🔴 **OPTION B — `ACTIVATION_NOT_CONFIRMED`**, *"No actor authority may be assumed from
these contracts"*, and *"A new, explicit activation act is required"*. Same conclusion as mine,
**properly sourced where mine was inferred.** A's provenance is better and I adopt it.

**(c) The shared evidential paper contains no seizure endpoint at all.** A counted over the whole
Wang 2012 text surface: `seizure` 0, `epilep` 0, `convuls` 0, `lithium` 0, `LiCl` 0, in 49,334
non-abstract characters, denominator declared. I made the same argument structurally in my §3.1 —
that "shared evidence" is a bibliographic and not an evidential relation — and **A instantiated it
with a count on the one edge that matters most.** The instance is worth more than my generalisation.

**(d) The Results text states no result for Fig. 7c.** A's §4.1. The entire Results treatment of the
panel names the method and the figure and reports **no direction, no magnitude, no comparison** — the
finding exists only in the legend and the pixels, and is then joined by *"Together, these results
suggest…"*. I read that paragraph twice and did not notice. **A curation pipeline reading Results
extracts nothing from panel c and then meets a conclusion asserting an important role for GSK-3β.**

**(e) The figure title is the strongest causal claim in the paper.** *"Increased GSK3β activity in
the brain tissues **leads to** hypersusceptibility to drug-induced seizure in Wwox knockout mice."*
I quoted that title verbatim in my own Phase I record and did not flag it. A did.
**Figure titles are short, declarative, causally phrased, and therefore the most extractable and
least evidenced sentences in a paper** — that is a general finding, not a note about this figure.

**(f) The adjudicability triage.** A classified all 20 edges by whether the shared paper's primary
evidence is *reachable and manifest-backed*: 12 `PRIMARY_AVAILABLE` / 1 `ARTIFACT_ONLY_NO_MANIFEST` /
4 `SHARED_PAPER_NO_LOCAL_ARTIFACT` / 3 `NO_SHARED_PAPER`. My §7 has the artifact axis and **not the
manifest axis**. A's partition is the better instrument.

**(g) PAPER 041 is abstract-only, and three edges rest on it.** **Verified:** PAPER 041's
`Evidence depth` reads *"abstract only — full text paywalled"*, and its `Claim links` are
`019, 030, 032`. CLAIM 019 is `consolidated baseline`. I recorded PMID 29808465 as "no local full
text" and **never checked what the registry claims about having read it** — which is the difference
between a logistics note and a finding.

### 3.3 Where I extend A rather than dispute it

A's finding (b) in artifact 00 §3.3 — *"four papers the registry records as fully read have no
artifact and no manifest"* — is correct and **understated**. I verified all four and found that
**three canonical surfaces disagree with each other about the same four readings**:

| Surface | What it says about PMIDs 24369382 · 24456803 · 30361190 · 27495153 |
|---|---|
| `paper_registry_current.md` | `Evidence depth: full text reviewed` — three of the four add `coverage_status: complete_fulltext_read` |
| `reading_state.md` | **`partial_fulltext_read`**, all four, every section `unknown_legacy` |
| `fulltext_read_receipts.jsonl` | legacy reconstructions; the `evidence_basis` of each is *the paper registry's own declaration* |
| `files/fulltext/` · `deepdive_manifests/` | **0 artifacts, 0 manifests**, all four |

So the receipt's warrant is the registry's claim, and the reading-state table contradicts the
registry outright. **It is not only that the inputs are gone — the surfaces never agreed on what was
read.** A's conclusion stands and the ground under it is softer than A said.

### 3.4 🔴 Strongest disagreement — and A wins it

**A types edge `CLAIM 016 ↔ CLAIM 035` as `ASSOCIATED`. I typed it
`INDIRECT_UNKNOWN_INTERMEDIATES`. A is right and I change my position.**

A's argument, quoted:

> *"`INDIRECT_UNKNOWN_INTERMEDIATES` … asserts a causal path with unspecified intermediates. Here
> the intermediates are not merely unknown — the one bridging measurement offered (Ser9) is the one
> the mechanism paper shows is not the operative channel. Typing it this way would encode as
> unknown-but-real something that is untested."*

**This is a disagreement of interpretation, not of evidence** — A and I read the same two artifacts
and agree on every observation. I chose `INDIRECT_UNKNOWN_INTERMEDIATES` *because* of the readout
mismatch, reasoning that an unmeasured intermediate must exist. That reasoning assumes the path
exists and is merely unmapped. **The evidence does not establish that the path exists at all**, and
A's obs. 7 — which I did not have — is what makes the distinction decisive rather than semantic.

I note one tension A's choice creates and A does not address: in my own record I rejected
`ASSOCIATED` for other edges on the ground that it *asserts a biological association no source
claims*. That objection does not apply here — Wang's mechanism and Cheng's observation are both real
and both concern GSK-3β in WWOX-deficient systems, so an association is genuinely evidenced. **The
token is right here and wrong for a bare wikilink, and that difference should travel with it.**

**REVISED POSITION (B):** `ASSOCIATED`, direction `035 → 016` only, with A's qualification block
attached verbatim. My directionality finding is unaffected and A reaches it too — A licenses
direction *"for the 035 half only"*.

### 3.5 Unsupported inferential steps in A

I looked for one and found **no unsupported causal step**. Two smaller notes:

1. A's artifact 00 §5 gate verdict is stale (§1.1). Not an inference error — a decayed measurement,
   published as a routing fact.
2. A's §3.3(b) reports the four papers as recorded `complete_fulltext_read` without recording that
   `reading_state.md` says `partial_fulltext_read`. **Incomplete, not wrong**, and the omission
   understates A's own case (§3.3 above).

### 3.6 Missing negative evidence in A

A's own §5 *"Negative evidence sought against my own reading"* is the best-executed section in either
peer document, and it pre-empts most of what I would have raised — including the correction that
**"elevated" is weak, not invented**, since the abundance direction really is upward by 9–18%.

**I concede that against my own wording.** My Phase I §8.4 called it a *"disproven wording"*. It is
not disproven; it is unsupported and misdescribed. C reaches the same conclusion independently
(*"a misdescribed premise, not a reversed conclusion"*). **Two peers converging against one of my
words is exactly the correction this phase is for**, and I adopt theirs.

The one negative A did not seek: A never tests whether the Ser9 fall has a **non-WWOX systemic
cause**. A names CLAIM 036 as *"a standing confound"* and stops. C does not stop — see §4.2.

---

## 4 · Review of Scientist C

### 4.1 Strongest agreement

C converges with me on all eight §12 answers, on the panel-attribution defect (D-1), on the
"elevated" misdescription (D-2), and on the CLAIM 016 / CLAIM 035 S9 tension (D-4). C's D-1
formulation is better than mine:

> *"The pointer routes a verifier to the refutation of the claim it anchors."*

and C adds the disjunction I did not state: under the charitable reading in which `Fig. 7b` governs
the ethosuximide clause, **the lithium assertion is left with no figure locator at all, in the one
sentence that constitutes its evidence boundary. Defective either way.**

### 4.2 🔴 Evidence C noticed that I missed — including the best finding in the pilot

**(a) The metabolic alternative explanation, and it is the strongest scientific contribution any of
us made.** GSK-3β Ser9 phosphorylation is the canonical output of insulin/IGF-1 → PI3K → AKT. Cheng's
blot is at **P20** in a systemic constitutive null that CLAIM 036 documents as hypoglycaemic
(143.5 vs 250.6 mg/dL), acidotic (bicarbonate 14.50 vs 21.67) and uraemic (BUN 37.25 vs 17.67) at
P18. **A hypoglycaemic, catabolic, acidotic animal has reduced AKT activity and therefore reduced
Ser9 phosphorylation — precisely the direction and precisely the readout Figure 7c reports.**

C holds it at the right strength — *"an untested confound of high prior plausibility, not a
demonstrated one"*, with the timepoint and strain differences declared — and names the falsifier:
pair-fed or glucose-clamped nulls, or the brain-restricted conditional allele CLAIM 036 notes was
built and never used in this direction.

🔴 **I adjudicated edge `CLAIM 005 ↔ CLAIM 036` in my own Phase I record. I had CLAIM 036 open, I
verified its glucose and BUN values verbatim against the primary, and I did not connect it to
CLAIM 016.** C did, and it supplies the *mechanism* for the readout mismatch that A and I could only
name as a gap. **The three findings — my mismatch, A's S9A mutant, C's metabolic route — compose into
one coherent account, and none of us had all three.**

**(b) C's exhaustive enumeration that the molecular and pharmacological arms are never joined.**
Every occurrence of `lithium`/`LiCl` across 71,916 characters of cleaned XML, plus a search of the
24-page supplement (17,570 extracted characters, zero occurrences of `ithium`, `LiCl`, `GSK`,
`thosuximide`). **No panel and no sentence reports any molecular measurement in a lithium-treated
animal.** I wrote "no target engagement"; C proved it with two independent surfaces and denominators.

**(c) The exposure confound between the two drug arms.** Ethosuximide is a **single** 150 mg/kg dose
at −45 min; LiCl is *"pretreated three times within 1 h"* at 60 mg/kg — **180 mg/kg cumulative across
three administrations.** I read that exact Methods sentence and quoted it in my own pilot without
drawing the consequence. **The ETS-vs-LiCl specificity contrast — which my pilot, the canonical
evidence boundary and A's pilot all lean on — is confounded by exposure.** This weakens a finding I
am attached to, and C is right.

**(d) The WWOX-dosage / pSer9 dissociation.** Panel c's own Wwox row shows protein absent in `−/−`
and visibly reduced in `+/−`, while pSer9 in `+/−` sits at or above wild-type. **Gene dosage is
plainly visible at the level of WWOX protein and entirely absent at the level of pSer9.** Half the
WWOX yields full Ser9 phosphorylation. I recorded the non-intermediate heterozygote; C read the
*dosage control in the same panel* and turned it into a constraint on any stoichiometric model.

**(e) The reporting asymmetry, stated precisely.** For ethosuximide the text reports the control
result explicitly and negatively; for lithium — same figure, same design — the control result is
positive and the text is silent. C's formulation: *"the authors demonstrably knew how to report
control-genotype outcomes and did so for the drug where the result was negative, and not for the drug
where it was positive."* I wrote "the text is incomplete". **C's is a materially stronger and more
precise statement about the same two sentences.**

**(f) The pSer9/total ratio the paper never computes.** C computed it — cerebellum 1.23·1.29·0.54,
hippocampus 1.57·1.46·0.77, cortex 1.77·1.58·0.96 — and confirmed both the direction and the
non-intermediate heterozygote survive renormalisation. A two-minute robustness check I did not run.

**(g) The Methods statistics sentence.** *"We performed statistical tests with one-way analysis of
variance (ANOVA)…"* — one-way, no post-hoc named, no multiplicity correction. I asserted the absence
of an interaction test; C quoted the sentence that makes the absence structural.

### 4.3 🔴 Strongest disagreement — and I win this one

**C concludes: *"The Pathograph is not present in this repository."* It is present. C's sweep was
confined to C's own worktree.**

| | C's measurement | Mine |
|---|---|---|
| Working-tree content sweep | 584 files, **1 hit**, in C's own untracked artifact | shared checkout: `pathograph_inventory.md`, `pathograph_export.jsonl`, `pathograph.py`, `test_pathograph.py`, plus uncommitted edits to `analysis/README.md` and `DATA_SOURCES.md` |
| Ref sweep | 57 refs, 0 hits | 50 refs, 0 hits — **and C's denominator is the better one** (57 = 44 heads + 6 remotes + 5 tags + 1 codex + 1 stash; mine omitted tags and the stash) |

**This is a disagreement caused by different evidence, not different interpretation.** C's numbers
are all correct *for the tree C searched*. The Pathograph lives untracked on the shared checkout's
disk, and `.claude/worktrees/lettore-c/` is not that disk. C's ref sweep and mine agree exactly, and
both are right — the object is on no ref.

**Two consequences follow, and they are not small.**

1. **C's §2 conclusion that §4 is unexecutable, and therefore C's decision to execute §12 only, rest
   on a search that could not have found the workset.** Twelve edges were adjudicable. C adjudicated
   none of them, for a correct reason applied to an incomplete measurement.
2. **C's second negative inherits the same boundary.** C reports *"no governed relation vocabulary
   exists either"*, having searched for `relation_type`, `edge_type`, `RELATION_VOCAB` across
   `*.md`, `*.py`, `*.json`. **The vocabulary exists** — `RELATION_VOCABULARY` in
   `framework/scripts/pathograph.py`, surfaced in the export header as
   `DIRECT · INDIRECT_UNKNOWN_INTERMEDIATES · ASSOCIATED · CONTROVERSIAL_OPEN`. Both C's search terms
   and C's file globs were sound; the file is not in C's tree.

🔴 **The general lesson is the one my own §1 states and C's case proves: a worktree-scoped sweep
cannot establish a repository-scoped negative when the object under test is untracked.** C did
everything right — denominator, positive control (36 of 57 refs for a control string), braces on the
zsh loop — and still reached a false conclusion, because **the surface was chosen before the object's
tracking state was known.** A negative needs its surface justified, not merely declared.

**C is not alone in this and neither am I.** A found the Pathograph because A looked at the shared
checkout. My §11 retraction (§2 above) is the same failure in a different coat: I chose a
transformation and reported its output as a property of the object.

### 4.4 A second, smaller correction to C — and one to my draft of this review

C reports Scientist-B's first pass as absent from all 57 refs. **True at the instant C measured**
(C's sweep predates my 15:24 commit), and stale by the time C published. Same class as A's gate
verdict; no fault in either.

> 🔴 **THE PARAGRAPH ABOVE IS WRONG, AND IT IS WRONG IN MY FAVOUR AND IN C'S. Corrected
> 2026-08-25, original left standing per §9.**
>
> **The timing claim is false.** My pilot was committed at **15:24:34**; C committed at
> **15:37:28** — thirteen minutes *later*. C's sweep did **not** predate my commit. The artifact
> was durable and reachable when C measured.
>
> **The operative cause is scope, not staleness.** C's stated method, verbatim: *"Swept
> `learning/` across all 57 refs."* My artifacts live at `reviews/scientist-b/`. C's sweep found
> the one file of mine under `learning/` — `SLR-scientist-b-0001.md`, which C correctly identified
> as a Session Learning Review and not a pilot — and could not see the eleven under `reviews/`.
> The path prefix was the denominator, and it excluded the actor it was measuring.
>
> 🔴 **What this says about me is worse than what it says about C.** I published a causal
> explanation of a peer's error — *"C's sweep predates my commit"* — **and never measured the two
> timestamps.** It was a story that fitted, offered as a finding, in a review whose whole subject is
> other people's measurement discipline. It is the same class as my retracted 2-of-9: a causal story
> that was never a measurement. And it exonerated C on a ground that does not hold, so the review
> was wrong about the peer as well as about itself.
>
> **The corrected reading:** C's negative about my pilot was a scope error of exactly the kind C's
> own §2 Pathograph conclusion was — the instrument's reach defined the population — and it is C's
> *second* instance in one artifact, not a timing accident. Held for the rebuttal round rather than
> pressed now; C has not read this and cannot answer it yet.
>
> ⚠️ **A's gate verdict was lumped with C's in the sentence above and does NOT move.** A's was a
> genuine race — C's commit landed at 15:37:28, A published at 15:43:51, six minutes and
> twenty-three seconds later, against a surface that had genuinely changed. Only the C half of
> *"no fault in either"* is withdrawn.

C also reports `learning/scientist-b/SLR-scientist-b-0001.md` on `refs/heads/lettore-b`, correctly
identified as a Session Learning Review and not a pilot. **My first check appeared to contradict
this and my first check was truncated by `head`.** Re-run properly: the file exists, 1 of 12
`learning/` paths on that ref, positive control 10 for `SLR-plan`. **C is right, I was briefly wrong,
and I nearly published a false correction against a peer** — recorded because the near-miss is the
finding.

### 4.5 Unsupported inferential steps in C

**None in the science.** C's Q2 is *more* conservative than mine and correctly so:

> *"The experiment cannot distinguish specific from non-specific rescue, because the test that would
> separate them was not performed, and every marginal significance it does report is identical."*

C is right that my formulation — *"lithium raises the threshold irrespective of Wwox genotype"* —
slightly overstates the panels. They show suppression is *significant* in controls, not that its
*magnitude* equals the null's; baselines differ (controls ~stage 0.5–1.5, nulls ~2–3.5), so a real
interaction could exist undetected. **C's wording is weaker and much harder to overturn. I adopt
it.**

The unsupported steps in C are both in §2 and both are the worktree-scope issue, not inference.

### 4.6 Missing negative evidence in C

C's §1 anchoring declaration is exemplary — it names the contamination, refuses to minimise it, and
instructs the reader to weight confirmations below novel findings. I have one addition C could not
have: **C names the deepdive manifest as the contamination source. It is not the only one.**
`disease-models/wwox/analysis/locator_contract_live_test.md`, tracked since 2026-08-04, contains the
Figure 7d, Figure 7b and "elevated is the wrong word" adjudications in prose, and CLAIM 016's own
`Evidence boundary` carries the conclusion in the canonical registry. **The contamination surface is
wider than the manifest, and it includes a canonical file a Scientist is required to read.**

---

## 5 · Convergence map

| Proposition | A | B | C | Status |
|---|---|---|---|---|
| Lithium works in all three genotypes | ✅ | ✅ | ✅ | **converged, three independent derivations** |
| No WWOX-specific rescue demonstrated | ✅ | ✅ | ✅ | converged |
| GSK-3β not established as lithium's target | ✅ | ✅ | ✅ | converged |
| Total GSK-3β flat; Ser9 falls | ✅ | ✅ | ✅ | converged |
| Panel c carries no statistics | ✅ | ✅ | ✅ | converged |
| Heterozygote not intermediate | ✅ | ✅ | ✅ | converged |
| CLAIM 016 cites the wrong panel | ✅ | ✅ | ✅ | converged — **and it is canonical** |
| "Elevated" misdescribes the measurement | ✅ | ✅ | ✅ | converged; **B's word "disproven" retracted** |
| pS9 readout mismatch with CLAIM 035 | ✅ | ✅ | ✅ | converged, independently, three ways |
| S9A mutant makes the mismatch a designed result | ✅ | ✗ | ✗ | **A alone** |
| Metabolic/AKT route explains the Ser9 fall | ~ | ✗ | ✅ | **C alone**; A names the confound and stops |
| ETS-vs-LiCl contrast confounded by exposure | ✗ | ✗ | ✅ | **C alone** |
| Results text states no result for panel c | ✅ | ✗ | ✗ | **A alone** |
| Figure title asserts "leads to" | ✅ | ✗ | ✗ | **A alone** |
| `****` undefined in the legend | ✅ | ✅ | ✅ | converged |
| Edge type for `016 ↔ 035` | `ASSOCIATED` | ~~`INDIRECT`~~ → `ASSOCIATED` | assigns none | **resolved in A's favour** |
| The Pathograph workset exists | ✅ | ✅ | ✗ | **resolved against C** — worktree scope |
| A governed relation vocabulary exists | ✅ | ✅ | ✗ | **resolved against C** — same cause |
| Phase II gate open | ✗ | ✅ | ✗ | **a race; each correct at its instant** |
| Wang 2012 locators sound | 9/9 | ~~2/9~~ → 9/9 | — | **resolved in A's favour; B retracted** |

**Nine converged propositions, four single-actor findings, four resolved disagreements, one race.**

---

## 6 · What remains unresolved, and is preserved as such

1. **Whether the Ser9 fall in `Wwox−/−` brain is WWOX-proximal or systemic.** C's metabolic route
   and A's S9A result both point away from the WWOX-proximal reading; neither refutes it. Both
   explanations predict the same observation. **Decisive test (C's, adopted):** brain pGSK3β(Ser9) in
   `Wwox`-null mice against pair-fed or glucose-clamped littermates, or in a brain-restricted
   conditional null that is not systemically ill.
2. **Whether the ethosuximide genotype restriction survives exposure matching.** C's confound is real
   and untested. Until it is, "ETS is specific, LiCl is not" is a comparison across two designs, and
   the canonical evidence boundary leans on it.
3. **Whether `ASSOCIATED` is the right token or the vocabulary is the wrong instrument.** A and I now
   agree on the token. Neither of us thinks four causal values can express what the registry's own
   paper records already write in seventeen free-text qualifiers. **The agreement is a local optimum
   inside a vocabulary all three of us report as insufficient.**
4. **Whether the twelve adjudicable edges A triaged and C did not see should now be adjudicated by
   one actor or by three.** I adjudicated eleven; A adjudicated one to greater depth than I reached
   on any. **That difference — breadth versus depth — is the routing question, and §15 puts it with
   Orchestrator.**

---

## 7 · What Phase II changed, stated plainly

**Changed my position:** the edge type for `016 ↔ 035` (`INDIRECT_UNKNOWN_INTERMEDIATES` →
`ASSOCIATED`); the word *"disproven"* → *"unsupported and misdescribed"*; my Q1/Q2 formulation →
C's weaker and stronger one; and **one finding retracted outright**.

**Did not change:** every figure reading; the panel-attribution defect; the propagation count; the
directionality verdict; the causal-vocabulary mismatch across 18 of 20 edges; and the conclusion
that this experiment demonstrates neither a WWOX-specific rescue nor GSK-3β as lithium's target.

**Added, from peers, that I could not have reached alone:** A's S9A mutant, A's Results-states-no-
result, A's figure-title finding, A's operator-decision provenance, A's manifest-axis triage, A's
abstract-only PAPER 041; C's metabolic route, C's exposure confound, C's dosage dissociation, C's
reporting-asymmetry formulation, C's ratio robustness check.

**No peer artifact was edited. No canonical file was touched. §16 observed in full.**
