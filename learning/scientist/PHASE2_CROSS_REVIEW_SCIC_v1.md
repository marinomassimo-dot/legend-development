---
record: PHASE II — CROSS-REVIEW by Scientist C of Scientist A and Scientist B
id: PHASE2_CROSS_REVIEW_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Mutates nothing. No peer artifact edited, moved or rewritten (§8).
authority: roles/scientist.md is PROPOSED; governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
  records ACTIVATION_NOT_CONFIRMED (provenance adopted from Scientist A, verified on main).
---

# Phase II — reviewing A and B, conceding the central point, and one disagreement that survives

> **Nothing here is medical advice.**

---

## 1 · What I read, named by object

| Artifact | sha256 |
|---|---|
| A · `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` | `b443526a…c42d99f2` |
| A · `TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` | `636df2d0…6a9350ed60` |
| B · `PHASE2_CROSS_REVIEW_SCIB_v1.md` | read at `lettore-b` tip `c9a8e9e` |
| Primary re-opened | Cheng 2020 `792b5b29…f00f5` · Fig7 `ced68a66…62542` · **Wang 2012 JATS, newly opened this phase** |

**Every peer claim I accept below, I re-derived from the primary artifact myself.** Where I could
not, I say so. Quoting a peer is not evidence and I have tried not to let agreement substitute for
a check.

---

## 2 · 🔴 The concession, stated before anything I might be right about

**Scientist B refuted my most consequential Phase I conclusion, and B is correct.**

I wrote: *"The Pathograph is not present in this repository."* **It was present**, untracked, on the
shared checkout's disk. I have now verified it directly: `pathograph.py` is real, the inventory
reports **39 claim nodes, 30 directed links, 20 undirected edges, 0 carrying a declared relation
type** — which is the workset §4 described, within one of the figure the dispatch told me to
re-measure rather than inherit.

And the second negative fell with it. I reported *"no governed relation vocabulary exists"*. It
exists: `RELATION_VOCABULARY` in `pathograph.py` — `DIRECT · INDIRECT_UNKNOWN_INTERMEDIATES ·
ASSOCIATED · CONTROVERSIAL_OPEN`. **My own search term `relation_type` matches that file 12 times.**
The terms were right, the globs were right, the file was not in my tree.

**The Orchestrator instructed me to measure this rather than concede it, and measuring changed the
shape of the concession in both directions.** Three tests, all run in my own worktree.

**TEST 1 — was a repository-scoped negative derivable from the surfaces I had? Yes, and it was
*true* of those surfaces.** I content-grepped `pathograph`, case-insensitively, across the **full
tracked content** of the pre-`d422829` tree (`30cb4f3`): **0 files.** Positive control on the same
grep (`legend_lint`): **55 files.**

⇒ **No tracked surface anywhere in this repository named the object.** Not a script, not a protocol,
not `DATA_SOURCES.md`, not the analysis README — the three wiring lines that reference it were
themselves uncommitted and travelled in `d422829`. So this was not a missed pointer. **There was no
pointer.**

That forces me to withdraw a piece of self-criticism I had written here and had believed:

> ~~I ran a positive control on the ref sweep and none on the working-tree sweep; had I run one, the
> conclusion would have collapsed in one command.~~

**It would not have.** A positive control on my working-tree sweep would have confirmed that my
working-tree sweep works — and it *did* work, correctly, on my working tree, which does not contain
the object. No control, no denominator and no diligence *within* my surfaces could have found a file
that is in no ref, in no tracked content, and on another working directory's disk. **Only a change of
scope would have.** I was over-correcting, and over-correcting is the same error with the sign
inverted, so I am marking it rather than leaving the flattering version standing.

**What survives, and it is enough.** My sentence was *"the Pathograph is not present in this
repository"*. It is true of the tracked repository and false of the shared checkout's working
directory, and **I did not distinguish those two things while having access to both** — I had read
`<REPO_ROOT>/files/` earlier in the same session. The correct sentence was
available: *the object is absent from this repository's history and from my worktree, and I have not
established its state on disk outside my worktree.* I asserted the strong form. That is the error,
and it cost twelve adjudicable edges.

It is still the third time this session I let something other than an enumeration define a
population — `registries/*.md` for the GSK grep, `^learning/` for the peer sweep, the worktree for
the object sweep. **One error in three costumes is a habit, and I record it as one.**

**TEST 2 — is the workset figure a measurement or an estimate? A measurement, and I reproduced it.**
The object is now on a ref, so I extracted `pathograph.py` with its two dependencies into a
scratchpad and ran it against my own tree:

```
nodes 39 · claim->claim 41 -> 30 distinct directed · declared edges 20
edges with a declared type 0 of 20 · propositions scanned 1080
```

Identical to the committed inventory. **The 20 is tool-derived and independently reproducible.** The
*twelve* is a different kind of number: it is **A's triage** over that measured population
(12 `PRIMARY_AVAILABLE` / 1 `ARTIFACT_ONLY_NO_MANIFEST` / 4 `SHARED_PAPER_NO_LOCAL_ARTIFACT` /
3 `NO_SHARED_PAPER`), not emitted by the tool. It is internally coherent — 12+1+4 = **17 with a
shared paper**, +3 without = 20, which independently reproduces the packet's expected 17/3 split.
So: a reproducible judgement over a measured population, neither an estimate nor a tool output.

🔴 **A numeric trap worth naming before it bites someone:** the tool independently reports
`isolated nodes 20 · review material present 12`. Those are **isolated nodes**, an unrelated
population that happens to share both figures with A's edge triage. Two different "12 of 20" in one
inventory is exactly the coincidence that produces a confident conflation later.

**TEST 3 — was B's edge set on a ref when B adjudicated? No.** `pathograph.py` enters history at
`d422829`, `2026-08-25T17:02:49+02:00`. B's edge adjudication is `8612baa`,
`2026-08-25T15:46:25+02:00` — **76 minutes earlier.** B's own account is correct: it read the object
from the shared checkout's disk.

⇒ **The defect is symmetric, and B's exposure is the mirror of mine.** I failed to see an untracked
object and drew a false negative. B adjudicated eleven edges *against* an untracked object, so
**B's Phase I artifact was not reproducible from B's own commit**: a reader checking out `lettore-b`
at `8612baa` receives the adjudication and not the thing adjudicated. Neither is misconduct and I am
not scoring a point — it is one structural fact, that untracked state is per-working-directory and
invisible to every reproducibility mechanism this system has, hitting two actors from opposite
sides. `d422829` closes it for the object; it does not close it for the class.

---

## 3 · 🔴 The finding that changes what my Phase I independence was worth

The Orchestrator reports, and B independently found, that
`disease-models/wwox/analysis/locator_contract_live_test.md` carries the paper's adjudicated
conclusions in prose. **I verified it myself rather than accept it:** tracked at *my own HEAD* since
`2026-08-04T20:32:01+02:00` (`3cfd451`), sitting in my worktree the entire session. Lines 374–400
contain, verbatim: Figure 7d has three panels and lithium suppresses in all three; Figure 7b marks
ethosuximide n.s. in `+/+` and `+/−` and significant only in `−/−`; *"'Elevated' is the wrong word …
GSK3β is **dis-inhibited, not more abundant**"*; the `PREMISE: DEFAULT_FROM_TEXTBOOK` tag on
*"lithium is a GSK3β inhibitor"*; and the alternative-mechanism argument from the paper's own
Discussion.

**So my D-2 was not a discovery.** It was found on 2026-08-04, written down with a proposed remedy
(*"→ commit candidate: correct to activation"*), and never applied. I presented it as novel because
I searched `registries/*.md` and the file is in `analysis/`.

I then measured, against all 581 tracked files, which of my other claims pre-existed. Reporting both
directions, because over-correcting is the same error with the sign flipped:

**Pre-existing, not mine:** lithium in all three genotypes · the ethosuximide inversion · "elevated"
is wrong / total flat / dis-inhibited · lithium's non-selectivity with the Discussion alternatives ·
the revival trigger (selective inhibitor or *Gsk3b* epistasis, rescue in null not controls).

**Absent from the tracked tree, verified with the offending file excluded from its own search:**
the `****` is undefined in the legend · panel 7c carries no dispersion, no n, no test, no P ·
*"efficacy is better than ethosuximide"* as an untested between-panel comparison · the ETS/LiCl
exposure mismatch as an **inference** (the Methods quote pre-exists; the consequence does not) ·
the interaction-test / NOT-TESTABLE distinction · the CLAIM 036 metabolic route onto Fig 7c · the
`Fig. 7b` pointer recorded **as a defect** · CLAIM 016↔036 unlinked · the pSer9/total ratio.

**A distinction I had blurred and B's convergence map exposes:** novelty against the *tree* and
novelty against *peers* are different questions. The `****` finding and "panel c has no statistics"
are absent from the tree but were reached independently by all three of us. They are convergences,
not solo findings, and I had implied otherwise.

**The honest conclusion is the Orchestrator's and it is not softenable:** no Scientist reading this
paper through this repository could have been independent of the repository's conclusion about it.
Independence was not spent by peer contact. It was never available. Below, wherever I agree with a
prior conclusion, I say whether I re-derived it from the panel or recognised it from the tree.

---

## A · CONFIRMED BY MY OWN PRIMARY-EVIDENCE CHECK

**A1 · Lithium suppresses PTZ seizures in all three genotypes.** Fig 7d re-read at 4×, per panel:
`+/+` PTZ N=12 vs LiCl N=8, `****`; `+/−` 12 vs 12, `****`; `−/−` 6 vs 7, `****`. A and B concur.
*Provenance: re-derived from the panel — and it was also available in the tree, so my agreement is
not independent of it.*

**A2 · Ethosuximide is genotype-restricted.** Fig 7b at 4×: `n.s.` in `+/+` (N=20/16) and `+/−`
(N=18/12), `***` in `−/−` (N=6/6). Control arms carry the **larger** samples, so the negative is not
a power artefact. *Re-derived; also in the tree.*

**A3 · Total GSK-3β is flat, Ser9 falls, heterozygote not intermediate.** All nine lanes 2.2–2.6 on
the total row; pSer9 2.7·3.1·1.3 / 3.6·3.5·2.0 / 3.9·3.8·2.5. *Re-derived at 3×; also in the tree.*

**A4 · Panel 7c carries no statistics of any kind.** No error bars, no per-lane n, no significance
marker, no P-value; caption offers only *"representative results of four independent experiments"*.
Legend defines `n.s.` and `*** P < 0.001` — and **`****` occurs 0 times in 71,916 characters of
cleaned XML**, existing only inside the image. Converged with A and B; **absent from the tree**.

**A5 · The molecular and pharmacological arms are never joined.** Complete enumeration of
`lithium`/`LiCl` across the XML, plus the 24-page supplement (17,570 extracted chars, zero hits for
`ithium`/`LiCl`/`GSK`/`thosuximide`). No panel and no sentence reports any molecular measurement in
a lithium-treated animal. **Absent from the tree.**

**A6 · A's zero-count on the shared evidential paper — verified from Wang 2012 primary, by me.**
Over the full JATS surface (50,838 cleaned chars, tags→empty): `seizure` **0**, `epilep` **0**,
`convuls` **0**, `lithium` **0**, `LiCl` **0**, `PTZ` **0**, `ethosux` **0**. Positive control
`GSK3` = **193**. ⇒ The "shared evidential paper" on edge `016↔035` is shared **bibliographically
and not evidentially**. A is exactly right and this is the measured fact that decides the edge.

---

## B · ACCEPTED BECAUSE PEER SUPPLIED NEW PRIMARY EVIDENCE / LOCATOR

**B1 · A's S9A mutant — accepted, and I verified it at the source rather than from A.**
Wang 2012, Results, Fig 5a/b, body-exact:

> *"Transfection with GFP–GSK3β WT and S9A notably decreased SH-SY5Y cell differentiation, whereas
> KD and R96A did not affect SH-SY5Y cell differentiation compared with the GFP control"*

A GSK-3β that **cannot be switched off at Ser9 behaves like wild type**, while kinase-dead and the
substrate-binding mutant do not. Kinase activity is required; the Ser9 switch is dispensable. This
is a **designed** result with internal controls, not an inference from an unchanged blot. I did not
open Wang 2012 in Phase I at all. A did, and it is the single most decisive locator in the pilot.

**B2 · The Pathograph and the relation vocabulary exist (B).** Conceded in full at §2.

**B3 · A's operator-decision provenance.** `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` records
`ACTIVATION_NOT_CONFIRMED`. I reached the same authority conclusion from `roles/scientist.md`
frontmatter alone. Same verdict, **better source**; I adopt A's provenance over my inference.

**B4 · B's correction of my staleness.** My "A has none, B has one SLR" and my 0/57 were true at
15:37 and stale on publication. Accepted; already reported upstream with the timeline.

**B5 · B's widening of my contamination declaration.** I named the deepdive manifest as the
contamination source. B is right that it is not the only one, and that one of them is a tracked file
in my own tree. §3 above.

---

## C · DISAGREE — WITH PRIMARY-EVIDENCE REASON

**C1 · 🔴 The edge type `CLAIM 016 ↔ CLAIM 035`. A typed it `ASSOCIATED`; B revised to `ASSOCIATED`
and recorded the disagreement as resolved. I decline to join, and not on taste.**

*First, what is decidable.* The inventory publishes exactly one worked criterion:
`DIRECT — the same experiment measures both endpoints`. Against that criterion the edge is
decidable and decided: **NOT `DIRECT`.** Wang measures no seizure endpoint (A6, verified by me);
Cheng runs no WWOX–GSK-3β binding assay. No experiment measures both.

*Second, what is not decidable.* `INDIRECT_UNKNOWN_INTERMEDIATES`, `ASSOCIATED` and
`CONTROVERSIAL_OPEN` **carry no definition anywhere in the governed surface.** I searched the
inventory, the module and its docstring: they appear once, as a list of accepted values at
inventory line 131, with a single warning that an `ASSOCIATIVE` connective does not make an edge
`ASSOCIATED`. There is no statement of what any of the three *means*.

⇒ `VOCABULARY_INSUFFICIENCY_OBSERVED` — and of a specific kind that is not the kind already
recorded. The declared instances concern a token that cannot *express* a needed proposition. This
one is different: **three of the four values have no published semantics, so "does this token fit"
is not a checkable question.** Two Scientists converged on `ASSOCIATED` with no definition to
converge against. I am not claiming they are wrong; I am claiming the agreement is not yet a
scientific agreement, and recording it as *resolved* overstates what happened. B half-sees this at
its §6.3 — *"a local optimum inside a vocabulary all three of us report as insufficient"* — and I
am making the sharper claim: it is not merely a poor instrument, it is an **undefined** one.

*Third — and this is the substantive disagreement, not the procedural one.* The association A and B
rely on is that both endpoints concern GSK-3β in WWOX-deficient systems. **My Phase I metabolic
confound, composed with A's S9A result, undermines that premise.**

- Wang shows WWOX inhibits GSK-3β **S9-independently** (obs. 6) and that Ser9 is **dispensable**
  to GSK-3β's neuronal output (obs. 7, S9A).
- Therefore, on Wang's own mechanism, a Ser9 change is **not the expected consequence** of losing
  WWOX. Cheng's Fig 7c measures precisely the channel Wang shows WWOX does not use.
- And there is a positive alternative that predicts the observed direction: at P20, in a systemic
  null the paper says *"succumb[s] to death by 4 weeks"*, with **no systemic covariate reported at
  all** (`blood glucose` 0 · `bicarbonate` 0 · `BUN` 0 · `serum` 0 · `body weight` 0 across the XML),
  and with CLAIM 036 documenting hypoglycaemia, acidosis and uraemia at P18 — Ser9 phosphorylation
  is the canonical AKT output and falls under exactly those conditions.

⇒ **If the Cheng pSer9 signal is not reporting WWOX-proximal GSK-3β biology, then the two endpoints
do not share a biological referent — they share a molecule name.** An edge typed on shared molecule
name rather than shared biology is the precise failure the causal layer exists to prevent, and
`pathograph.py`'s own docstring says so: *"two demonstrated facts are not a demonstrated relation
between them."*

**My position:** `NOT_DIRECT`, decided against the only published criterion; **no further token
assigned**; `VOCABULARY_INSUFFICIENCY_OBSERVED` recorded with the exact proposition —

> *"The one bridging measurement offered between CLAIM 035's mechanism and CLAIM 016's phenotype is
> Ser9 phosphorylation, which the mechanism paper shows by designed mutant to be dispensable, and
> for which an untested systemic confound predicts the observed direction."*

I invent no token. Per §16 I annotate nothing in the registry.

**C2 · The ETS-versus-LiCl specificity contrast is confounded and all three of us lean on it.**
B credits this to me and accepts it; I record it here as a standing disagreement with the
**canonical** evidence boundary, which is not a peer and cannot concede. Methods: ethosuximide is a
**single** 150 mg/kg dose at −45 min; LiCl is *"pretreated three times within 1 h"* at 60 mg/kg —
**180 mg/kg cumulative across three administrations**. The two arms differ in dose, schedule and
number of administrations, sit in different panels with different control arms and different N, and
no test compares them. The Discussion's *"its efficacy is better than the commonly used
anticonvulsant drug ethosuximide"* is an eyeball comparison across panels presented as a result.

---

## D · REVISE MY EARLIER POSITION

**D1 · "The Pathograph is not present in this repository" → withdrawn.** §2. The correct statement
was always available to me and I did not make it: *the object is absent from this repository's
history and I have not established its state on disk outside my worktree.*

**D2 · "No governed relation vocabulary exists" → withdrawn.** §2.

**D3 · "Phase II cannot open" → withdrawn as stale**, and the deeper point conceded to B: a phase
gate defined over mutable peer state, with no barrier and no agreed clock, returns a different
verdict to each actor and each is correct at its instant. B's §1.1 is right and it is a finding
about the protocol.

**D4 · My D-2 reclassified from discovery to propagation-failure-with-known-remedy.** §3. The defect
is real and still uncorrected in canonical state; what is false is that I found it. Its value is now
sharper, not smaller: **a defect was identified, a remedy was drafted, and it did not travel** — and
`BATCH_20260810_005` later diagnosed that exact class by name while leaving this instance in place.

**D5 · My D-4 framing revised, because A's S9A result resolves what I called a tension.** I framed
it as *"the model asserts the assay gives a false negative and holds a positive result from that
assay — preserve the tension."* With obs. 7 the better reading is: **the Cheng pSer9 result should
not be read as WWOX-proximal evidence at all.** That is not a tension to preserve — it is a
misattribution to correct. My framing was too even-handed and I withdraw it.

**D6 · The reporting-asymmetry finding demoted from discovery to sharpening.** Both underlying facts
are in the tree; the asymmetry framing is mine, and B judges it *"materially stronger and more
precise"*. A framing contribution, not a new observation, and I had not drawn the line.

**D7 · Novelty claims re-scoped.** §3. Several findings I marked *"not in the manifest"* were true of
the manifest and false of the repository, and two were converged rather than solo.

---

## E · UNRESOLVED

**E1 · Whether the Ser9 fall in `Wwox−/−` brain is WWOX-proximal or systemic.** My metabolic route
and A's S9A result both point away from the WWOX-proximal reading; **neither refutes it**, and both
explanations predict the same observation. Preserved as unresolved, not collapsed.

**E2 · Genotype specificity — three verdicts, deliberately not collapsed.**
*Demonstrated*: no. *Contradicted*: no — the panels show suppression is **significant** in controls,
not that its **magnitude** equals the null's, and baselines differ sharply (controls ~stage 0.5–1.5,
nulls ~2–3.5). *Not testable from this experiment*: **yes** — Methods declare one-way ANOVA with no
post-hoc and no multiplicity correction, each genotype analysed in its own panel, so the difference
of differences is computed nowhere. **The third verdict is the correct one and it is not the same as
the second.** B adopted this weaker wording from me; I hold it against A's stronger phrasing too.

**E3 · Whether the ethosuximide restriction survives exposure matching.** C2. Untested.

**E4 · Whether three of the four relation tokens can be applied at all before they are defined.**
C1. I record this as unresolved rather than answer it, because defining them is not Scientist work.

**E4b · The independence leak is in git's own primitives, and it penalises promptness.** Verified
here rather than accepted. The §3 existence check — *does the peer's artifact exist yet* — is
idiomatically `git log --oneline -1 <ref>`, and on my branch that emits:

```
c55c25c The panel was read before the claim that cites it, and the citation points at the wrong panel
```

— my finding, in full, to anyone merely testing whether I had committed. Two primitives answer the
same question blind: `git log --format='%H %cI' -1 <ref>` and `git ls-tree -r --name-only <ref>`.

**The exposure is not incidental to this repository's style: 21 of 44 head refs (48%) open their
subject with a declarative finding.** So the cheapest existence check leaks conclusions roughly half
the time by construction.

🔴 **And it penalises exactly the discipline the system demands.** A's artifacts were unreadable at
the moment B checked because they were still *untracked*; mine were readable because I had committed
promptly and durably, which is what the contract asks for. **Committing on time is what exposed my
conclusion.** I record this as a protocol defect and not as a reason to change how I write commit
subjects — the subjects are good, and a system whose independence depends on uninformative commit
messages has put the safeguard in the wrong place. The fix is that an existence check must use a
blind primitive.

**E5 · Breadth versus depth on the twelve adjudicable edges.** B adjudicated eleven, A one at
greater depth, I zero. §15 puts this with Orchestrator and I do not pre-empt it. I note only that I
am now unblocked and the work is available.

**E6 · A missing edge, not an untyped one — `CLAIM 016 ↔ CLAIM 036`.** They are mutually unlinked in
both directions (positive control: `CLAIM 035` appears 2× in CLAIM 016's block, so the grep fires).
CLAIM 036 declares itself *"un vincolo di disegno trasversale"* naming P1, P2 and P6, and CLAIM 016
carries a brain measurement in a systemic constitutive null in the immediately adjacent window.
**The pathograph assembles edges from declared wikilinks, so an edge nobody wrote is invisible to
the layer by construction** — this one would not appear in the inventory's 20 no matter how the
evidence stood. A cross-cutting constraint that must be hand-linked to each claim it constrains will
keep missing claims, and the graph cannot show what was never declared.

---

## F · NEW FALSIFIER / DISCRIMINATING EXPERIMENT

**F1 · The decisive test for E1, sharpened by composition.** In Phase I I proposed pair-fed or
glucose-clamped nulls, or the brain-restricted conditional allele CLAIM 036 notes was built and
never used in this direction. A's S9A result lets me add the discriminator that pair-feeding alone
does not give:

> **Measure brain pGSK3β(Ser9) in a non-*Wwox* model of comparable systemic illness at P20** —
> any genotype rendered hypoglycaemic, acidotic and cachectic to a matched degree.
>
> - If Ser9 falls there too, the Cheng observation is a readout of terminal illness and carries no
>   WWOX-specific content. **CLAIM 016's core datum loses its mechanistic reading.**
> - If Ser9 holds, the systemic route is excluded and the WWOX-proximal reading survives — while
>   still having to explain why the channel Wang shows is dispensable is the one that moved.

This is a **positive control for the confound**, which pair-feeding is not: pair-feeding removes the
confound, this reproduces it. Removing a confound and failing to see an effect is weak; reproducing
a confound and seeing the effect is decisive.

**F2 · For genotype specificity (E2).** A PTZ + lithium arm with an **explicitly tested**
genotype × treatment interaction; a structurally unrelated GSK-3β inhibitor at matched exposure; and
a post-treatment pSer9 western demonstrating target engagement — the measurement absent from the
entire paper (A5).

**F3 · For the exposure confound (E3).** Ethosuximide and LiCl at matched cumulative dose and
matched schedule, in one experiment, with a shared control arm.

**F4 · For the edge (C1).** The experiment that would make `016↔035` typable rather than arguable:
**a WWOX–GSK-3β binding-deficient allele — L404A, which Wang shows abolishes binding — knocked into
the mouse, then PTZ challenge.** If the L404A knock-in is seizure-susceptible while total WWOX is
intact, the GSK-3β arm carries the phenotype and the edge earns a causal type. If it is not, the
seizure phenotype runs through something else in WWOX and the edge is bibliographic. **This uses the
mechanism paper's own decisive reagent against the phenotype paper's own endpoint — the one
experiment neither paper could have run alone**, and neither peer proposed it.

---

## 7 · What Phase II changed for me

**Changed:** two Phase I conclusions withdrawn outright (Pathograph, vocabulary); the gate verdict
withdrawn as stale; D-2 reclassified from discovery to propagation failure; D-4's framing replaced
by a misattribution reading on A's evidence; several novelty claims re-scoped; the
reporting-asymmetry demoted to a sharpening.

**Did not change:** every figure reading; the statistical void on panel 7c; the unjoined arms; the
exposure confound; the metabolic alternative; the interaction-test verdict; the pointer defect; and
the conclusion that this experiment demonstrates neither a WWOX-specific rescue nor GSK-3β as
lithium's target.

**Added from peers that I could not have reached alone:** A's S9A mutant (B1) — which changed my
own position, not merely supplemented it; A's zero-count on the shared paper; A's operator-decision
provenance; B's demonstration that my central negative was worktree-scoped; B's widening of my
contamination surface.

**One disagreement survives and I am not conceding it** (C1). B's convergence map records
`016↔035` as *resolved in A's favour*. I do not join that resolution: the token is undefined, and
the biological premise the association rests on is undermined by the composition of A's own S9A
result with my metabolic route. **A surviving disagreement is a valid result.**

No peer artifact was edited. No canonical file was touched. No relation type was written to any
registry. §16 observed in full.
