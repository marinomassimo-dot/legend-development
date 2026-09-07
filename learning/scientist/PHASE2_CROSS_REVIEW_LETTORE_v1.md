---
record: PHASE II — CROSS-REVIEW by Scientist A of Scientist B and Scientist C
id: PHASE2_CROSS_REVIEW_LETTORE_v1
actor: worktree `lettore` (mapped scientist-a) — NOT ACTIVATED; operator-directed analytical pilot
authority: roles/scientist.md is PROPOSED; DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE returns
  ACTIVATION_NOT_CONFIRMED. Nothing here assumes contract authority.
date: 2026-08-25
status: NON-CANONICAL. No canonical file written. No peer artifact edited, moved or rewritten.
headings: pilot-local (A–F), NOT governed verdict vocabulary
---

# Phase II — reviewing B and C, correcting two of my own findings

> **Nothing here is medical advice.**

Every position below is bound to the primary artifact and a locator. **Quoting a peer is not
evidence**, and where I record agreement I say whether I re-derived it or recognised it.

## 0.1 · Artifacts read, named by object

| Artifact | sha256 |
|---|---|
| B · `PILOT_PMID32000863_..._SCIB_v1.md` | read at `lettore-b` tip `fb31c2a`+ (`git show`) |
| B · `PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md` | same ref |
| B · `PHASE2_CROSS_REVIEW_SCIB_v1.md` | same ref |
| C · `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md` | `lettore-c` `c55c25c`, blob `4be1f97`, 41 547 B |
| C · `PHASE2_CROSS_REVIEW_SCIC_v1.md` | `lettore-c`, read **after** this document was drafted and **before** it was published — it changed D-2 and E-4 rather than being noted as unread |

**Primary, now resident in my own worktree and verified before use** — the Orchestrator placed
them and instructed me not to trust the placement:

| Artifact | Expected | Measured in `.claude/worktrees/lettore/files/` | |
|---|---|---|---|
| `PMID32000863_Cheng2020_PMC.xml` | `792b5b29…f00f5` | `792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5` | ✅ |
| `…_assets/40478_2020_883_Fig7_HTML.png` | `ced68a66…62542` | `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542` | ✅ |
| `…_Cheng2020_supplementary.pdf` | — | `0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f` | ✅ matches my Phase I declaration |

`git check-ignore -v` → `.gitignore:7:files/`. `git status --porcelain` lists no `files/` path.
The evidence is present and unreachable by any branch, which is the correct state.

**No mismatch, so the Plan-reported second PMC snapshot (`7d235c00`, 158 798 B) is not implicated
in anything I read.** Two snapshots of one article remains an open finding and is not mine.

---

## 0.2 · 🔴 Contamination — restated per proposition, because my first disclosure was too generous to me

In Phase I I disclosed that `CLAIM 016`'s `Evidence boundary` gave me the three-genotype pattern
before the panel did. **That was incomplete.** B found the wider surface and I verified it on
`main`: `disease-models/wwox/analysis/locator_contract_live_test.md`, tracked since 2026-08-04
(`8a49d75`), lines 375–395, carries in prose — *"Figure 7d has three panels … lithium suppresses
seizures in all three"*; the ethosuximide inversion; *"'Elevated' is the wrong word … total GSK3β
is flat (2.2–2.6 …); GSK3β is dis-inhibited, not more abundant"*; the `PREMISE: DEFAULT_FROM_TEXTBOOK`
tag on *"lithium is a GSK3β inhibitor"*; the Wnt/myelin alternatives; and the `REVIVAL_TRIGGER`
naming a selective inhibitor showing rescue *"in the null and not in controls"*.

**So the repository already held most of what my Phase I presents as adjudication.** No Scientist
reading this paper through this repository could have been independent of it. I state that flatly
rather than around it.

What I bounded, to keep the concession honest rather than theatrical. Counted over that file's 454
lines: `representative` **0** · `four independent` **0** · `ANOVA` **0** · `interaction` **0** ·
`error bar` **0** · `S9A` **0** · `Tau` **0** · `22193544` **0** · `statistic` 2 (neither about
Fig. 7c) · `Wang` 1 (a wikilink line) · `heterozyg` 3 (all about *developmental* measures — S1f,
S6b, S7, Fig. 2b — none about Fig. 7c).

| Proposition | Re-derived from the panel/text | Recognised from the tree |
|---|---|---|
| Lithium significant in all three genotypes | ✅ **this session, at native resolution** (Phase I: overview only) | ✅ also in the tree since 2026-08-04 |
| Total GSK3β flat; Ser9 falls | ✅ 6× | ✅ in the tree |
| Ethosuximide inversion | ✅ | ✅ in the tree |
| "Elevated" misdescribes | ✅ | ✅ in the tree |
| Panel c carries **no statistics**; n=4 declared, one representative shown | ✅ | ❌ **absent from the tree** |
| Heterozygote not intermediate *on Fig. 7c* | ✅ | ❌ absent (the tree has het≈WT for developmental measures only) |
| Wang S9A mutant behaves as wild type | ✅ | ❌ absent |
| Wang contains zero seizure/lithium content | ✅ | ❌ absent |
| Results text states no result for Fig. 7c | ✅ | ❌ absent |
| Fig. 7 title asserts *"leads to"* | ✅ | ❌ absent |
| Supplementary carries nothing on this arm | ✅ | ❌ absent |

**On the Orchestrator's leak mechanism.** `git log --oneline` answers existence and discloses the
subject line; this repository writes findings into subject lines. B checked me by filename and C
by subject line, and the asymmetry was luck — my artifacts were still untracked when B looked.
I add the measurement that makes it concrete: **my own four subject lines carry conclusions**
(*"The bridging measurement is on the axis the mechanism paper says WWOX does not use"*). Anyone
running the §3 existence check against my branch reads my central finding without opening a file.
The quarantine was unobservable, not disobeyed.

---

## 0.3 · 🔴 My Phase I routing fact was false. Owning it precisely, because the precise version has a different fix

I reported the Phase II gate CLOSED on Scientist C. **C had committed its first pass at 15:37:28;
my handoff asserting the contrary is 15:43:51, six minutes and twenty-three seconds later.** The
gate was open and I reported it shut. I then **repeated the claim in my 0B/0C reply, after all four
of my commits, without re-measuring.** That repetition is the error; the original measurement was
merely stale.

Two distinct failures, and conflating them would hide the fix for one of them:

1. **A decayed population figure, republished.** My `git log main..lettore-c` was path-blind and
   returned empty *when it ran*. Nothing was wrong with the instrument. The fault is that a
   count about mutable peer state was carried forward and published as current. **Fix: re-measure
   at publication, not at discovery.** My own memory of this class did not save me from it.
2. **A directory-scoped sweep.** My *untracked* check for C read `…/lettore-c/learning/scientist/`.
   Had C written elsewhere I would have missed it, exactly as C — sweeping `^learning/` — missed
   B in `reviews/scientist-b/`. **Fix: enumerate the population, never let a convention define it.**

I accept the Orchestrator's finding. I do not accept the merged version of it: my commit check was
never directory-scoped, and recording it that way would put the wrong repair in the practice record.

---

# A · CONFIRMED BY MY OWN PRIMARY-EVIDENCE CHECK

Each re-derived by me from the fingerprinted artifacts in my own tree, not accepted from a peer.

**A-1 · Lithium's suppression carries `****` in all three genotypes; no saline arm; N as reported.**
Fig. 7d re-read at native resolution — the check I explicitly declined in Phase I, having seen only
a half-scale overview. `+/+` 12 vs 8 · `+/−` 12 vs 12 · `−/−` 6 vs 7, each sub-panel bracketed
`****`. **Confirms B, C and my own pilot.** Legend defines only `n.s.` and `***P < 0.001`; `****`
occurs **0 times** in the XML — it exists only as ink.

**A-2 · Fig. 7c carries no statistical support of any kind.** No error bars, no SD/SEM, no marker,
no test, no P value, no per-lane n. Legend, BODY-EXACT: *"The representative results of four
independent experiments are shown."* **Converges with B and C, independently derived by all three.**

**A-3 · Total GSK3β is flat; Ser9 falls.** 6×: pGSK3β 2.7·3.1·**1.3** | 3.6·3.5·**2.0** |
3.9·3.8·**2.5**; total 2.2·2.4·2.4 | 2.3·2.4·2.6 | 2.2·2.4·2.6. C's values are identical to mine to
the last digit. **GSK3β is dis-inhibited, not more abundant** — with the caveat I insisted on in
Phase I and B has now adopted: the abundance direction *is* upward by 9–18%, so *"elevated"* is
**unsupported and misdescribed, not disproven.** B retracted *"disproven"*; C reached the same
formulation independently. Three-way convergence including on the strength of the word.

**A-4 · The heterozygote is not intermediate.** pS9/total: 1.05× · 0.93× · 0.89× of wild type.
C computed the same three rows and got the same numbers.

**A-5 · Cheng reports no systemic covariate whatever.** Re-run by me over my own cleaned XML:
`blood glucose` 0 · `bicarbonate` 0 · `BUN` 0 · `creatinine` 0 · `hypoglyc` 0 · `acidosis` 0 ·
`serum` 0 · `body weight` 0; `glucose` 2, both irrelevant. **Denominator differs slightly from C's**
— my cleaned surface is 70 057 chars, C's 71 916 — because we flatten whitespace differently. *The
counts agree; the denominators do not, and that difference is worth more than the agreement:* two
derivations of one artifact producing the same zeros is the control neither of us could run alone.

**A-6 · `CLAIM 036` values.** Verified verbatim on `main`: glucose 143.5 vs 250.6 mg/dL
(`p=0.000131`), total bicarbonate 14.50±3.5 vs 21.67 mEq/L (`p=0.006227`), BUN 37.25 vs 17.67 mg/dL
(`p=0.01086`), blood chemistry `n=3/3/4`, model `Wwox^ΔCre/ΔCre` EIIA-Cre at **P18**. C quoted them
exactly.

**A-7 · The pointer defect.** `CLAIM 016` cites `Fig. 7b` for a `Fig. 7d` result. Converged by all
three. **C's formulation is better than mine** — *"the pointer routes a verifier to the refutation
of the claim it anchors"* — and C adds a disjunction I did not see: read charitably, so that
`Fig. 7b` governs only the ethosuximide clause, **the lithium assertion is then left with no figure
locator at all, in the one sentence that constitutes its evidence boundary. Defective either way.**
I adopt C's formulation.

---

# B · ACCEPTED BECAUSE PEER SUPPLIED NEW PRIMARY EVIDENCE / LOCATOR

**B-1 · 🔴 C's exposure confound. Verified verbatim; accepted; and I sharpen it.**
Methods, BODY-EXACT against `792b5b29…f00f5` in my own tree:

> *"Ethosuximide (i.p., 150 mg/kg) … was injected into mice 45 min before PTZ-induced clonic
> seizures. LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection."*

ETS: **one** administration, 150 mg/kg. LiCl: **three**, 180 mg/kg cumulative. Different dose,
schedule and number of administrations. C is right that the specificity contrast between the arms
is confounded by exposure. **I quoted that sentence in my own Phase I dosing table and did not draw
the consequence.**

*What I add:* the confound has a **direction**, which makes it worse than a symmetric caveat.
Higher cumulative exposure makes lithium *more* likely to clear significance in precisely the
low-ceiling control arms where ETS did not. So exposure is not merely a reason to distrust the
contrast — it is a **competing explanation for the exact pattern observed.**

*What it does not touch, stated to keep the concession the right size:* my load-bearing finding —
lithium's suppression is significant in `Wwox+/+` — is **within-panel, within-drug**, and does not
use ethosuximide at all. C's confound demolishes the rhetorical comparison in my pilot §7 (*"this
paper assigns that signature to the wrong drug"*), which I withdraw as an argument. It leaves the
wild-type result standing.

**B-2 · 🔴 C's WWOX-dosage / pSer9 dissociation. Verified at 4×; accepted; and it does more work
than C claimed.** Panel c's Wwox row, nine lanes: `+/+` strong, `+/−` **visibly weaker** in
cerebellum and hippocampus (subtler in cortex), `−/−` **absent**. The row carries **no densitometry**,
so this is a qualitative band read and I scope it as one. Gene dosage is plainly visible in WWOX
protein and **entirely absent in pSer9** — half the WWOX yields full or greater Ser9 phosphorylation.

*What I add:* this is not only a constraint on stoichiometry. **It discriminates between the two
live explanations of the Ser9 fall.** A WWOX-proximal mechanism predicts a dosage-graded pSer9;
there is none. C's metabolic route predicts that `+/−` — healthy, per `CLAIM 032`'s
haploinsufficiency-is-not-deleterious — should be indistinguishable from `+/+`, and that only the
systemically ill `−/−` should move. **That is exactly the observed pattern.** The heterozygote lane
fits the metabolic reading better than the mechanistic one, and neither C nor I said so.

**B-3 · 🔴 C's metabolic/AKT route. Accepted at C's strength, not above it.** Ser9 is the canonical
output of insulin/IGF-1 → PI3K → AKT; Fig. 7c is at P20 in a systemic constitutive null; `CLAIM 036`
documents hypoglycaemia, acidosis and uraemia at P18 (A-6). A hypoglycaemic, catabolic animal has
reduced AKT and therefore reduced Ser9 phosphorylation — **the direction and the readout Fig. 7c
reports.** C holds it as *"an untested confound of high prior plausibility, not a demonstrated one"*,
declaring the strain and timepoint differences. I adopt that wording unchanged.

**B is right that I stopped.** My Phase I named `CLAIM 036` as *"a standing confound"* and went no
further. Naming a confound is not proposing a mechanism, and C proposed one that predicts the
observation without any WWOX–GSK3β interaction.

**B-4 · B's §3.3 — three canonical surfaces disagree, and the corroboration is circular. Verified,
accepted, and it is worse than B stated.** All four independently checked on `main`:

| Surface | PMIDs 24369382 · 24456803 · 30361190 · 27495153 |
|---|---|
| `paper_registry_current.md` | `Evidence depth: full text reviewed`; three add `coverage_status: complete_fulltext_read` |
| `reading_state.md` (lines 60, 61, 73, 81) | **`partial_fulltext_read`**, all four, every section `unknown_legacy` |
| `fulltext_read_receipts.jsonl` | `record_kind: legacy_reconstruction` |
| `files/fulltext/` · `deepdive_manifests/` | 0 artifacts, 0 manifests |

My Phase I reported the registry and the filesystem and **missed the middle two rows.** B is right.

*The third leg, quoted so it cannot be softened.* `FTR-20260726-24456803-01`:

```
evidence_depth     : "partial_fulltext_read"
record_kind        : "legacy_reconstruction"
source_fingerprint : null
source_locator     : "disease-models/wwox/registries/paper_registry_current.md#PAPER 043"
evidence_basis[0]  : "PAPER 043 declares Evidence depth: full text reviewed
                      (coverage_status: complete_fulltext_read)"
```

**The receipt's `source_locator` points at the registry, not at the paper.** So the circle closes on
itself: the registry asserts a complete read, the receipt cites the registry as its evidence, and
the receipt's own `evidence_depth` field then contradicts the registry. *Two things I add:*
`source_fingerprint` is **null**, so these four receipts could never satisfy the fail-closed artifact
gate — they are grandfathered, which **explains** the missing artifacts rather than compounding the
mystery. And the receipt is not merely weak corroboration: **it disagrees with the surface it cites.**

Consequence for my own Phase I: my triage class `SHARED_PAPER_NO_LOCAL_ARTIFACT` for four edges is
right about reachability and **understates the finding** — the surfaces never agreed on what was
read. B's extension stands, extended.

**B-5 · B's retraction of its 2/9 locator finding.** B withdrew it after re-deriving with tags
stripped to empty. I note only what B itself drew out and it is the better lesson: B's negative
control passed, and a negative control cannot test whether the surface compared against is the right
surface. B's diagnosis of its own mechanism is correct. *Per the Orchestrator, this needs no
defending and I spend no further pass on it.*

---

# C · DISAGREE — WITH PRIMARY-EVIDENCE REASON

**C-1 · Against C: *"The Pathograph is not present in this repository."* It is present, and I
disagree from evidence, not from authority.** In the shared checkout:
`legend-operating-convention-v1:disease-models/wwox/analysis/pathograph_inventory.md`,
`…/data/pathograph_export.jsonl`, and `pathograph.py` with `test_pathograph.py` under
`framework/scripts/` on that same branch. **And it is now on a ref**
— `d422829`, branch `legend-operating-convention-v1`, which I verified by `git ls-tree`; it was on
none of 57 refs when C measured.

> 🔴 **Paths qualified by ref, 2026-08-26.** This entry was right that the object exists and
> still wrote the paths bare, as if resolvable from any checkout. They are not: all four live on
> `legend-operating-convention-v1` alone, and on neither `main` nor `lettore`. **Being correct
> about existence is not the same as being correct about location** — which is precisely the
> distinction this entry was arguing for, applied one level short of its own citations.

**But C's method was sound and mine was lucky.** C's ref sweep and mine agree exactly — the object
was on **no ref** — and C's denominator (57 = heads + remotes + tags + codex + stash) is better than
the one B used. C ran a positive control and braced its zsh loop. The single fault is scope: a
worktree-scoped content sweep cannot establish a repository-scoped negative for an **untracked**
object, and the tracking state was not knowable before the sweep. I found the Pathograph because I
searched the shared checkout — a choice I made for the artifact reason, not because I foresaw this.

**Consequence I must state even though it favours my own count:** C's decision that §4 was
unexecutable rests on that sweep, so C's zero edges is a correct decision on an incomplete
measurement. **This does not make my one edge a better disposition** — see C-3.

**C-2 · Against C: the governed relation vocabulary exists.** `RELATION_VOCABULARY` at
`pathograph.py:119–123` (under `framework/scripts/` on `legend-operating-convention-v1`),
surfaced in the inventory at line 131. C searched sound
terms and sound globs; the file was not in C's tree. Same cause as C-1, not a second error.

**C-3 · Against the Orchestrator's provisional reading of the edge-count spread — and against my own
interest.** My dispatch has **no cap** on edge adjudications (§17 below). So my count of one is not
explained by paperwork: **I chose depth over breadth under an uncapped instruction, and said so at
the time** (*"left undone for want of session, not for want of evidence"*). The dispatch divergence
C surfaced is real and material for C; **it does not exculpate me**, and a reconciliation that scored
my restraint as judgement would be scoring a choice I already declared as an unfinished task.

**C-4 · Against B's convergence-map line *"resolved in A's favour"* for the edge type.** I decline
the win, and then some: I have **withdrawn my own token**. See D-2 / D-2b — C is right on both the
criterion and the substance, and the entry should be struck rather than reworded.

**C-5 · Against my own E-4 as I first wrote it.** I framed the vocabulary question as *"unresolvable
as posed."* That is too comfortable. C shows one half **is** resolvable: `DIRECT` has a published
criterion and the edge fails it, so `NOT_DIRECT` is a decided result, not an abstention. Only the
remaining three tokens are undecidable. **A partly-decidable question reported as undecidable hides
the part that was answerable**, and I corrected E-4 accordingly.

---

# D · REVISE MY EARLIER POSITION

**D-1 · 🔴 I withdraw the word "REFUTED". This is a substantive scientific revision.**

Phase I pilot §7 typed proposition (i) — *lithium rescues a WWOX-specific epileptic mechanism* —
as **"❌ REFUTED by the paper's own panel"**, and my addendum's answer to Q2 read *"lithium reduces
chemoconvulsant-provoked seizure severity … in a manner that is **not** genotype-specific"*. Both
are too strong, and re-reading Fig. 7d at native resolution — which in Phase I I had not done —
shows why.

**Measured from the panel, at 3×, in my own tree:**

| Genotype | PTZ peak (Racine) | PTZ+LiCl peak | Peak Δ | Where the separation lives |
|---|---|---|---|---|
| `+/+` | ~1.35 at t≈1 min | ~0.4 | **~0.3–1.0** | almost entirely in the first ~5 min; from t≈5 the two traces interleave, blue at or above red at several points |
| `−/−` | ~3.5 at t≈5–7 min | ~1.5 at t≈7–9 | **~2.0** | sustained across the whole window |

**The magnitudes differ by roughly an order of magnitude, and the wild-type effect is small and
transient.** B and C both caught my overstatement independently; C's formulation is the one that
survives — *"the experiment cannot distinguish specific from non-specific rescue, because the test
that would separate them was not performed"* — and I adopt it.

*What I add, from the wild-type panel:* `****` is attached to a difference that is visually absent
over ~55 of 60 minutes. Each animal contributes ~60 repeated scores analysed as independent
observations by one-way ANOVA, which is exactly the design that manufactures significance from a
small transient difference. **The wild-type `****` is not evidence of a comparable effect; it is
evidence that the analysis cannot distinguish a large sustained effect from a small transient one.**

**The three verdicts, kept distinct as the dispatch requires:**

| Question | Verdict |
|---|---|
| Is genotype specificity **DEMONSTRATED**? | **No.** No interaction test exists; one-way ANOVA within genotype cannot address it. |
| Is genotype specificity **CONTRADICTED**? | **No — and my Phase I leaned this way.** The wild-type result refutes only the strongest form, *"lithium acts only where WWOX is missing"*. It does **not** refute the graded form, *"lithium acts more where WWOX is missing"*, which the magnitudes are visibly consistent with. |
| Is it **NOT TESTABLE** from this design? | **Yes.** One-way ANOVA, no interaction term, no post-hoc named, repeated measures as independent, unequal N, no saline arm in 7d, and a floor in the control arms. |

**What does not change:** the paper demonstrates **no WWOX-specific rescue**, and it never measured
GSK3β in a treated animal. The conclusion is unmoved; the *reason* is now *"the discriminating test
was not run"* rather than *"the panel refutes it"*. **That is a weaker claim and a much harder one
to overturn.**

**D-2 · 🔴 I withdraw my confidence in `ASSOCIATED` as a criterion-backed choice. C is right and
B and I converged on a word.**

Measured: `RELATION_VOCABULARY` at `pathograph.py:119–123` is a bare 4-tuple; validation at
`:401–404` is membership-only. Across the inventory and the assembler, **`DIRECT` has one gloss**
(*"the same experiment measures both endpoints"*), **`ASSOCIATED` has one *negative* constraint**
(*"An `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`"*) **and no positive criterion**,
and **`INDIRECT_UNKNOWN_INTERMEDIATES` and `CONTROVERSIAL_OPEN` have no definitional text anywhere.**

My Phase I rejected `INDIRECT_UNKNOWN_INTERMEDIATES` because *"it asserts a causal path with
unspecified intermediates."* **That reading is mine. The token says nothing.** B changed position to
match it. So the agreement B scored as *"resolved in A's favour"* is agreement between two
reconstructions of an undefined label, and **C is right to refuse to join it.**

**D-2b · 🔴 And C goes further than the criterion problem. On the substance, C is right, and I
withdraw `ASSOCIATED` altogether.**

C's Phase II C1 landed after I drafted D-2 and I read it before publishing. Its third argument is
not procedural:

> *"If the Cheng pSer9 signal is not reporting WWOX-proximal GSK-3β biology, then the two endpoints
> do not share a biological referent — they share a molecule name."*

The association B and I relied on was *"both endpoints concern GSK3β in WWOX-deficient systems."*
**That premise is exactly what my own S9A finding and C's metabolic route jointly attack.** If
Fig. 7c's Ser9 fall is an AKT readout in a hypoglycaemic, acidotic, uraemic animal (B-3, A-6), then
Cheng's molecular endpoint is not WWOX–GSK3β biology at all, and what remains linking the two
claims is the *name* `GSK3β`. `pathograph.py`'s own docstring names this failure: *"two demonstrated
facts are not a demonstrated relation between them."* **C turned my finding into an argument against
my own conclusion, which is the best possible use of it.**

**Revised position — I adopt C's: `NOT_DIRECT`, decided against the only published criterion; no
further token assigned.** Wang measures no seizure endpoint (E-2), Cheng runs no binding assay, so
no experiment measures both and `DIRECT` is excluded on the one criterion that exists. Beyond that
exclusion I assign nothing.

**One thing I do not concede, recorded so the residue is visible.** *"They share a molecule name"* is
very slightly too strong. They also share a **prediction**: Wang's mechanism entails that WWOX-null
neurons should carry de-repressed GSK3β, and Cheng's animals are WWOX-null and seize. That link is
real and it is *entailed, not measured* — which makes the honest object a **hypothesis**, not a
typed relation. **The vocabulary has no hypothesis tier**, so the only faithful action available is
to assign no token, and that is what I do.

**What survives unchanged, and it is the part that matters scientifically:** `035 → 016` is
directional; the WWOX ⊣ GSK3β half is strongly evidenced; the seizure half is carried only by a
non-specific, untargeted drug; and the bridging Ser9 readout is on the axis Wang shows WWOX does not
use. `VOCABULARY_INSUFFICIENCY_OBSERVED`, below.

**D-3 · I withdraw the ethosuximide contrast as an argument** (B-1), retaining the wild-type
lithium result, which does not depend on it.

**D-4 · I correct my Phase I §3.3(b)** to the four-surface version in B-4.

---

# E · UNRESOLVED

**E-1 · Is the Ser9 fall WWOX-proximal or systemic?** Three findings now point away from the
WWOX-proximal reading and **none refutes it**: my S9A result (the axis is dispensable by design),
C's metabolic route (the observation is fully predicted without any WWOX–GSK3β interaction), and the
dosage dissociation (B-2). Both explanations predict the same panel. **Preserved as unresolved.**

**E-2 · Is the bridge from Wang 2012 to Cheng 2020 empirical or inferential? — INFERENTIAL, and this
is my answer to the question the Orchestrator posed.** The bridge is a **citation**: Cheng's
reference list carries `WangHY… Cell Death Differ 2012 19 1049`, and Cheng's Results open with
*"WWOX has been shown to interact with and inhibit GSK3β … in human neuroblastoma SH-SY5Y cells
[65]"*. No experiment in Cheng tests the Wang mechanism — no pull-down, no L404-dependent
manipulation, no substrate-specific kinase readout in vivo. And Wang measures nothing on Cheng's
side: `seizure` **0**, `epilep` **0**, `convuls` **0**, `lithium` **0**, `LiCl` **0** across 49 334
non-abstract characters and the abstract. **The two papers share a citation, not a measurement.**
C verified this count at the source rather than from me, which is the confirmation that counts.

**E-3 · Does the ethosuximide genotype restriction survive exposure matching?** Untested (B-1).
Until it is, *"ETS is specific, LiCl is not"* is a between-panel comparison across two designs — and
the canonical `Evidence boundary` leans on it.

**E-4 · Is the vocabulary the wrong instrument? — *partly decided*, and I over-declared this.**
**Decided:** the edge is `NOT_DIRECT`, against the one published criterion (D-2b). **Undecidable:**
whether it is `ASSOCIATED`, `INDIRECT_UNKNOWN_INTERMEDIATES` or `CONTROVERSIAL_OPEN`, because none
of the three has published semantics. All three of us report the vocabulary as insufficient; C drew
the consequence that agreement inside it is not scientific agreement, and that the undecidable part
must not swallow the decidable one.

**E-5 · Breadth versus depth.** B adjudicated eleven edges, I adjudicated one more deeply, C zero.
Which is the right shape for a graph contribution is a routing question (§15), **now known to be
partly a dispatch-text question** (C-3, §17).

---

# F · NEW FALSIFIER / DISCRIMINATING EXPERIMENT

**F-1 · For E-1, the decisive test — C's, adopted unchanged.** Brain pGSK3β(Ser9) in `Wwox`-null
mice versus **pair-fed or glucose-clamped** littermates, or in a **brain-restricted conditional**
null that is not systemically ill — the `Wwox^flox` allele `CLAIM 036` records as built and never
used in this direction. *If the pSer9 drop survives metabolic normalisation, the mechanistic reading
stands; if it does not, `CLAIM 016`'s core datum is a readout of terminal illness.*

**F-2 · A cheaper discriminator I can add, from my S9A finding.** The metabolic route acts
**through Ser9**; the Wang mechanism is **S9-independent**. So they are separable without any
metabolic intervention: **measure GSK3β activity by a substrate readout that does not use Ser9** —
phospho-Tau S396/S404, the exact substrate pair Wang used — in `Wwox−/−` brain. If GSK3β output is
raised while Ser9 is *held constant*, the Wang mechanism is operating in vivo. If output tracks Ser9
alone, the metabolic route explains the panel. **This uses only tissue the original study already
collected.**

**F-3 · For the pharmacology.** A PTZ + lithium arm with an **explicit, tested genotype × treatment
interaction**; a structurally unrelated GSK3β inhibitor at **matched cumulative exposure and matched
schedule** (B-1); a post-treatment pSer9 or substrate western demonstrating target engagement; and a
saline arm in the lithium panel. Against **spontaneous** seizures on video-EEG — the endpoint this
paper documents from P12 and never used.

**F-4 · For E-3.** Ethosuximide at matched cumulative exposure and matched administration count
against LiCl, in all three genotypes, in **one** experiment with one control structure.

---

# VOCABULARY_INSUFFICIENCY_OBSERVED

Recorded as instructed; **no token invented, no vocabulary proposed.**

| # | Exact proposition | Why no governed token expresses it |
|---|---|---|
| V-1 | *"WWOX physically inhibits GSK3β by docking-motif binding, S9-independently; GSK3β de-repression is hypothesised to contribute to seizure susceptibility; the only measurement bridging them is on the axis the mechanism paper shows is not the operative channel."* | One edge, two halves at different evidential strength, plus a **mechanism-channel qualifier** that belongs to neither endpoint and is what adjudicates the edge. Four causal tokens carry none of it. |
| V-2 | *"GSK3β hyperactivation **may** contribute to seizure susceptibility in WWOX deficiency."* | `CLAIM 016`'s own title. **The hedge has no representation.** `may contribute` and `contributes` collapse to the same token. |
| V-3 | *"The observation is equally well predicted by systemic metabolic decompensation, with no WWOX–GSK3β interaction required."* | A **competing explanation** is not a relation between two claims and has nowhere to live. `CONTROVERSIAL_OPEN` would misdescribe it: nothing is contested — one explanation is untested. |
| V-4 | *"Lithium suppresses PTZ seizures in all three genotypes; genotype specificity is neither demonstrated nor contradicted but untestable in this design."* | *Untestable-by-design* is a property of the **evidence**, not of the relation, and no token or field carries it. |
| V-5 | 🔴 *Any* typed edge | **Three of four tokens have no published definition** (D-2). Membership validation without criteria means two Scientists can agree on a token while disagreeing on what it asserts — and B and I did. |

---

# COVERAGE OF THE MANDATED TOPICS

| Topic | Where |
|---|---|
| Lithium across genotypes | A-1, D-1 |
| Genotype specificity — demonstrated / contradicted / NOT TESTABLE | **D-1**, three distinct verdicts, not collapsed |
| GSK-3β target attribution | D-1 *("what does not change")*, E-2, F-3 |
| Fig. 7c statistics | A-2 |
| Ser9 | A-3, B-3, E-1, F-2 |
| Abundance vs dis-inhibition | A-3 |
| Heterozygote | A-4, B-2 |
| Wang 2012 / S9A; empirical or inferential bridge | **E-2 — inferential**; F-2 |
| `CLAIM 036` metabolic confounder | A-6, B-3, E-1, F-1 |
| Ethosuximide | B-1, D-3, E-3, F-4 |
| DisMech causal promotion | below |
| Graph representation | D-2, V-1…V-5 |
| `CLAIM 016` / `035` / `036` consistency | below |
| Transport and pointer defects | A-7, §0.1, below |

**DisMech causal promotion.** Unchanged from my pilot and no peer disputed it: the node's evidence
snippet is **verbatim the abstract sentence and absent from the body** (present-in-abstract True,
present-in-body False). DisMech preserves the provoked-vs-spontaneous and non-selectivity
limitations and **omits the wild-type response** — the only one of the three that bears on whether
the result is about WWOX at all. Phase II adds two omissions: it cannot carry *untestable-by-design*
(V-4), and its `direction: ABOLISHED` on *"Induced-seizure onset after GSK-3beta inhibition"* now
reads against a measured wild-type Δ of ~0.3–1.0 stages confined to five minutes (D-1).

**`CLAIM 016` / `035` / `036` consistency — three defects, none repaired.**
① `CLAIM 016`'s `Summary` (*"GSK3β is elevated"*) and `Type` (`DATO (abbondanza, murino)`) contradict
its own later `Meccanismo aggiunto` block; a graph materialiser reads the superseded field.
② `CLAIM 016` and `CLAIM 035` are reciprocally wikilinked while `CLAIM 035` contains the argument
that `CLAIM 016`'s only in-vivo measurement is on the wrong axis — held with no comment. C records
the same as its D-4.
③ **`CLAIM 016` and `CLAIM 036` do not reference each other**, though `CLAIM 036` is a declared
cross-cutting design constraint on exactly the window and model `CLAIM 016`'s datum comes from.
C records this as D-3; I confirm it and add that ③ is the one with a *mechanism* attached (B-3), so
it is the most consequential of the three.

**Transport.** The Phase I hazard is resolved for this paper: the four artifacts are now in my tree
at matching digests (§0.1), gitignored, on no branch. The general condition is unchanged — evidence
does not travel with a branch, and a verdict whose inputs are not reachable by its reader is a
memory of a verification.

---

## OBSERVATION_SCOPE

- Four peer artifacts read in full. **No peer artifact edited, moved or rewritten.**
- Primary re-read in **my own worktree** at verified digests: Fig. 7d whole panel + `+/+` and `−/−`
  sub-panels at 3×; panel c Wwox row at 4×; Methods dosing paragraph; text surface re-derived by me.
- **Eight crop recipes published and all re-executed byte-identically.** Crops written outside the
  repository — derivation published, reproduction not shipped. Source `ced68a66…62542`, PIL 11.3.0,
  `crop(box)` → `resize(w*s, h*s, LANCZOS)`:
  `c_full` (820,0,1946,500) 2× `257f7216…` · `c_lanelabels` (1440,105,1880,155) 6× `d6e2775a…` ·
  `c_pgsk_nums` (1440,225,1880,270) 6× `9a0b8246…` · `c_tot_nums` (1440,320,1880,365) 6× `45a233d9…` ·
  `d_whole` (820,470,1946,1627) 1× `288c0193…` · `c_wwox_row` (1130,370,1900,470) 4× `30feac56…` ·
  `d_KO_zoom` (1130,1250,1600,1560) 3× `153f572a…` · `d_WT_zoom` (1130,560,1600,880) 3× `a33010e3…`
- The Wwox-row read is **qualitative** — that row carries no densitometry.
- Fig. 7d magnitudes are read **off the plotted axis**, not from tabulated values; the paper reports
  none. They are order-of-magnitude, not measurements.
- Nineteen of twenty edges remain unadjudicated by me. Twelve are adjudicable today.
- No canonical file written. No `BATCH_COMMIT`. `roles/scientist.md` untouched.

---

*Non-canonical. Nothing here is medical advice.*
