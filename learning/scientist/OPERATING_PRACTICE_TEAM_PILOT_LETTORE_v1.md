---
record: §11 OPERATING PRACTICE — observed across the whole team pilot
id: OPERATING_PRACTICE_TEAM_PILOT_LETTORE_v1
actor: worktree `lettore` (mapped scientist-a) — NOT ACTIVATED; operator-directed analytical pilot
date: 2026-08-25
scope: OBSERVED PRACTICE, not a proposed contract. `roles/scientist.md` is untouched and no
  contract text is drafted, quoted as binding, or amended.
status: NON-CANONICAL. Evidence for later Plan/Mirror analysis.
---

# What actually happened, and which parts of it should survive

> Every practice below is tied to something that occurred in this run. Where the evidence is one
> occurrence, it says so. **A practice observed once under favourable conditions is not a validated
> practice**, and several of mine were exactly that.

---

## 1 · INDEPENDENCE

**OBSERVED BEHAVIOUR.** Three actors read one paper without reading each other, then cross-reviewed.
I declared contamination twice: first narrowly (`CLAIM 016`'s Evidence boundary), then — after B
found the wider surface — flatly, that **most of my Phase I was recognition rather than derivation.**

**WHY IT HELPED OR FAILED.** It failed as designed and succeeded as executed. `locator_contract_live_test.md`,
tracked since 2026-08-04, already carried the three-genotype panel, the ethosuximide inversion,
*"elevated is the wrong word"*, the premise tag and the revival trigger. **No Scientist reading this
paper through this repository could be independent of it.** What rescued the run was not
independence but **per-proposition disclosure**: bounding what the tracked surface did and did not
contain (`representative` 0, `four independent` 0, `ANOVA` 0, `interaction` 0, `S9A` 0, `Tau` 0)
turned an unusable global caveat into a usable partition.

**EVIDENCE.** My cross-review §0.2 table; B's §4.6; C's §1 anchoring declaration.

**RECURRING.** Structural. Any future reading of an already-modelled paper inherits it.

**CANDIDATE.** `VALIDATOR` — a contamination pre-flight that greps the tracked tree for the paper's
identifiers before a reading opens, and hands the reader the list. **CANDIDATE FOR PROMOTION** as a
tool; **DO NOT PROMOTE** any rule that treats independence as achievable — it was not achievable
here and pretending otherwise would make the disclosure optional.

---

## 2 · PEER-REVIEW TIMING

**OBSERVED BEHAVIOUR.** A phase gate defined over mutable peer state, evaluated by the actors it
gates, with no barrier and no shared clock. Three actors evaluated it at three instants and returned
three different verdicts, **each correct at its instant.**

**WHY IT FAILED.** I published *"gate closed on C"* at 15:43:51. C's first pass landed at 15:37:28.
**Six minutes and twenty-three seconds.** C, measuring earlier, found both peers absent. B, measuring
at 15:49, found all three present and proceeded.

**EVIDENCE.** Commit timestamps, all three branches. My correction blocks now stand above the false
text in two artifacts.

**RECURRING.** Certain to recur — it is a property of the gate's definition, not of anyone's care.

**CANDIDATE.** `ROUTING` — the gate belongs to whoever can see all three branches, not to the gated
actors. **CANDIDATE FOR PROMOTION.**

---

## 3 · COMMIT-MESSAGE CONTAMINATION

**OBSERVED BEHAVIOUR.** Git's cheapest existence primitive, `git log --oneline`, discloses the
subject line. This repository writes findings into subject lines. **The §3 existence check cannot be
run without reading conclusions.**

**WHY IT FAILED.** B checked me by filename and C by subject line, and the asymmetry was luck — my
artifacts were still untracked when B looked. **My own four subject lines carry my central finding
verbatim.** C measured 21 of 44 head refs opening with a declarative finding.

**EVIDENCE.** B's `OP_FINDING_INDEPENDENCE_VS_COMMIT_SUBJECTS_SCIB_v1`; my own commit log.

**RECURRING.** Yes, and it worsens as actors commit promptly — **the actor with the best durability
discipline leaks first.**

**CANDIDATE.** `TOOL` — content-blind primitives (`--format='%H %cI'`, `ls-tree --name-only`) in the
existence check. Orchestrator adopted this mid-run and said so. **CANDIDATE FOR PROMOTION.**
**DO NOT PROMOTE** any instruction to write duller commit messages: the informative subject line is
load-bearing everywhere else in this repository, and trading it away to patch one check would be
paying in the wrong currency.

---

## 4 · NEUTRAL PACKET DESIGN

**OBSERVED BEHAVIOUR.** Three Scientists received the same 17-section dispatch; Orchestrator held a
different document. Its §10 capped the graph work at the `016-035-036` neighbourhood. **That cap
reached none of us.**

**WHY IT MATTERED.** Orchestrator was about to read the edge-count spread (B 11, A 1, C 0) as
disposition. C pointed out that if the texts differed, part of the spread is paperwork — **and
argued this while cautioning against weighting it in C's own favour.** Orchestrator held the
decision.

**And it does not exculpate me.** My §4 carries no cap. My count of one is a choice I declared as
unfinished work.

**EVIDENCE.** Orchestrator's own correction, twice; my dispatch's §4 and §11 headings.

**ONE-OFF** in this form; **RECURRING** as a class — divergent instruction texts are invisible until
someone compares them.

**CANDIDATE.** `ROUTING` + `VALIDATOR` — one packet, one digest, quoted in each actor's first
artifact. **CANDIDATE FOR PROMOTION.** Note the better method Orchestrator adopted: it withdrew the
request that actors *report* their own dispatch, on C's argument that **self-attestation shaped by
the question is not a measurement**, and read the dispatch's fingerprints out of our committed
artifacts instead.

---

## 5 · ACCESS TO PRIMARY ARTIFACTS ACROSS WORKTREES

**OBSERVED BEHAVIOUR.** `files/` is gitignored for copyright, so a branch carries the manifest and
never the evidence. My worktree held **34** files where the shared checkout held **174**, and the
Cheng artifacts were **absent** from mine. The manifest was byte-identical across my working file, my
HEAD and `main` — **four derivations, one digest** — while the evidence it named existed in exactly
one tree.

**WHY IT FAILED, THEN WORKED.** Three conflicting reports existed because three actors measured
three filesystems and each was right about its own. Orchestrator then placed the four artifacts into
my worktree and **told me not to trust the placement**; I verified all three digests before use.

**EVIDENCE.** My 0C reply; `git check-ignore -v` → `.gitignore:7:files/`.

**RECURRING.** Structural and permanent.

**CANDIDATE.** `TOOL` — artifact placement with digest verification as a routine step, plus
`deepdive_manifest.py --artifact-workspace` for validating against the shared tree. **CANDIDATE FOR
PROMOTION.** The instruction *"do not trust the placement"* is the part that made it work and should
travel with it.

---

## 6 · TASK-BOUND EVIDENCE IDENTITY

**OBSERVED BEHAVIOUR — and this is the practice this run most clearly lacks.** The finding that
reorganised the entire synthesis — Wang Fig 1d has no GSK-3β row — was derived from a **PDF whose
digest appears in zero tracked files**, against a manifest (`PMID22193544.json`, schema v1) that has
**no `source_artifacts` key at all**.

Re-measured by me, counting *files* containing each digest via `git grep -l <digest> main`:

| Artifact | Digest | Tracked files |
|---|---|---|
| Wang **XML** | `eb6f568d…` | **10** — anchored |
| Wang **PDF** | `8f994f95…` | **0** — unanchored |
| Cheng XML *(control)* | `792b5b29…` | 5 |
| Cheng Fig. 7 PNG *(control)* | `ced68a66…` | **1** |

**WHY IT FAILS.** The anchored artifact **cannot carry the finding**: blot rows are not recoverable
from JATS text, which is why a render was necessary at all. So the pilot's most consequential
image-derived result rests on bytes nothing in the tracked tree identifies. **My digest reproduces,
which proves the file on disk is the one I name — and proves nothing about whether a future reader
can obtain it.** The Cheng figure control is barely better at one file.

**I asked C directly which artifact it rendered, rather than infer it. The answer arrived and it is
worth the whole section.**

C had rendered **the same PDF**. So at the moment I asked, what looked like independent corroboration
of the pilot's most consequential image-derived finding was **two readings of one unanchored file —
peer agreement, not a second quantity.** C said so plainly, and added the observation that matters:
it was the same distinction C had itself drawn about counts that morning, and it had not noticed the
distinction applied to its own figure work.

**Then C went and made the corroboration real.** The retrieval had left a third artifact nobody had
opened — the publisher's figure package — and C extracted Figure 1 from it. **I verified every
digest and re-read the panel myself before recording this:**

| Artifact | Digest | Verified by me |
|---|---|---|
| `PMID22193544_Wang2012.pdf` p.2 @300 dpi | `8f994f9542a7a37470b5e6edb8ad72a32e87633e0aef59119d1a393b2035174a` | ✅ my Phase V derivation |
| `PMID22193544_Wang2012_supplement.zip` | `af2faa04f85d52195de196dfc5f85caf79c873f5891551e92f2bce781589241d` | ✅ 17 members enumerated |
| └ member `cdd2011188f1.jpg`, 82 214 B, 433×553 | `bcffe618de02f099a8f5d343f5ceba57d5543107a21606d6df7f6c4c9e7aa50f` | ✅ extracted and read at 6× |

From the **publisher figure**, independently of the PDF: Fig. 1d carries `WWOX · pTau S396 · Tau ·
actin` and then whitespace. **No GSK-3β row. No pS9 row.** Recipe, re-executable:
`crop(0,395,240,553)` ×6 → `a71b90401aa1604fc791e264a55073599c587f7a4ea95251feef94e27200c95b`.

⇒ **The finding now has two derivations from two artifacts with two digests — artifact-level
independence rather than peer agreement — and it did not exist before the question was asked.**

🔴 **And D-10 is untouched by that, which is the actual lesson.** The Wang manifest is schema v1 with
no `source_artifacts` key, so **none of the three artifacts is declared** — not the PDF, not the zip,
not the image. **The one artifact that *is* anchored, in 10 tracked files, is the XML — and the XML
is the one that cannot carry this finding**, because blot rows are not recoverable from JATS text.
That is the gap stated exactly: *the anchored artifact cannot answer the question, and the ones that
can are anchored nowhere.* Neither of us repaired it; it is the repository's.

**RECURRING.** Yes — every schema-v1 manifest has this shape.

**CANDIDATE.** `VALIDATOR` — refuse a figure-derived locator whose artifact digest is not anchored.
**CANDIDATE FOR PROMOTION**, and it is the single highest-value item in this document.

**A second candidate, and this run produced the evidence for it in one exchange.** `CONTRACT` —
**when two actors report the same image-derived finding, name the artifact each read.** *(See §7.1:
naming the artifact is necessary and not sufficient — C then reproduced my crop and found that the
recipe naming it does not determine its digest.)* The question costs one message. Here it converted an apparent corroboration into a known-weak one, and then
*caused* a real second derivation to be produced within the hour. **The failure mode it catches is
invisible by construction**: two actors agreeing about a panel look exactly the same whether they
read one file or two. **CANDIDATE FOR PROMOTION.** Note what made it work: I asked for a fact and
explicitly said no conclusion was being requested and none should be adjusted — the answer came back
as a fact, followed by a repair neither of us had thought to make.

---

## 7 · FIGURE INSPECTION

**OBSERVED BEHAVIOUR.** Every conclusion that changed during this run changed because someone
rendered a page.

| Finding | Only reachable by | Consequence |
|---|---|---|
| Lithium significant in all three genotypes | reading Fig. 7d | the paper's central claim is not genotype-specific |
| Panel c has no statistics | reading Fig. 7c | the molecular claim rests on nine unreplicated numbers |
| WWOX dosage-graded, pSer9 not (C) | reading panel c's own `Wwox` row | the readout does not track the gene |
| Fig. 7d magnitudes ~0.3–1.0 v ~2.0 (A) | native resolution | `REFUTED` → `NOT TESTABLE` |
| **Fig. 1d has no GSK-3β row (C)** | **rendering at 300 dpi** | **demoted my own leg and moved L-1** |

**WHY IT MATTERED.** Fig. 1d's caption lists no antibodies — it says only that lysates *"were
subjected to western blot analysis."* **Text cannot distinguish "not measured" from "measured and
not discussed."** I read that caption in Phase I and did not render the panel. C did.

**EVIDENCE.** Eight Cheng crop recipes and two Wang crop recipes, all re-executed byte-identically.

**RECURRING.** Universal for blot-bearing papers.

**CANDIDATE.** `SKILL` — an explicit trigger: *a caption that names no antibodies is a caption that
cannot bound the panel; render it.* **CANDIDATE FOR PROMOTION.**

### 🔴 7.1 · The crop-recipe form I used is mine, it is not repository policy, and it is weaker in four ways

I wrote above that the crop-recipe form *"is already repository policy."* **That sentence was
wrong**, and C found the first crack in it by reproducing my recipe.

**C's finding, reproduced by me digit for digit** (PIL 11.3.0, same source, crop `(0,395,240,553)`,
×6):

| filter | raw-bytes digest | PNG digest |
|---|---|---|
| NEAREST | `cd2a55bd1b06f0eb` | `a091d679bd13c35d` |
| BILINEAR | `86cf3351db56f459` | `48a561756069776a` |
| BICUBIC | `7aba95f4e60d7870` | `f8ff04e57c38d82c` |
| **LANCZOS** | `015e21b2f3195f12` | **`a71b90401aa1604f`** ← mine |

**Eight candidates, one match. It reproduced because C and I share library defaults, not because the
recipe determined it.** A reader following exactly what I published lands on my digest at roughly one
chance in eight — *and the failure is invisible precisely when it succeeds*, because two agreeing
digests is what a reader would take as proof.

**C's prescription — name the filter and the encoding — is correct and insufficient, and the reason
is the more useful finding.** `framework/scripts/regenerate_adjudications.py` already exists, and its
`render()` is:

```python
page.get_pixmap(clip=fitz.Rect(*crop), dpi=dpi)     # no resample. no filter. no encode step.
```

The repository's form is **source PDF digest · page · crop rect in PDF points · dpi · SHA-256 of the
result**, with the source digest verified *before* rendering and the run failing closed on mismatch.
**It has no filter parameter because it never resamples** — it rasterizes once, at a declared dpi,
from the vector source, and hashes the pixmap bytes directly.

So the defect is not two missing fields. **I invented a form when one existed**, and the invented
form added three parameters the existing one does not have — a resample filter, an encoding step, and
a lossy raster source (a JPEG) in place of a vector one — **and dropped the one thing that made the
existing form checkable**: the **needle**. The repository's recipe carries a search string that
occurs exactly once on the page and is a fragment of the locator's own snippet, closing the chain
**needle → span → span inside crop → crop → digest**. My recipes assert *"this crop shows Fig. 1d's
rows"* with nothing a command can check, which is precisely the *"promise a command cannot check"*
that tool's docstring was written to eliminate.

This is `PATTERN_ALREADY_SOLVED_GATE` and I failed it: grep the vocabulary before inventing a
mechanism, and if you diverge, say why. **I did not look, and I diverged silently.**

**🔴 And it is worse than "a tool existed", in three measured steps.**

1. **The tool predates the pilot by sixteen days** — `de08905`, 2026-08-09T23:49:52 — and was
   hardened twice since: `700155e` added the needle (*"A locator identifier is a promise; a needle
   is something a command can check"*), `24a2f44` stopped it corroborating itself.
2. **It is wired into a gate that runs**, at `scripts/run_release_regressions.py` →
   `framework/scripts/test_regenerate_adjudications.py`.
3. 🔴 **The rule is in the bootstrap file I am required to read first, and I cited it.** My
   worktree's `CLAUDE.md` line 142 names `regenerate_adjudications.py` inside §5e — and my Phase I
   addendum §1.6 is headed *"Page-adjudication recipe — published as a recipe, never as the image ·
   `CLAUDE.md` §5e."* **I cited the section as my authority, implemented the half that says
   *publish the derivation, not the derived*, and did not implement the half that specifies
   *which* derivation and names the script that checks it.**

*Checked before reporting, because the opposite would have been an easy alarm to raise:* `main`'s
CLAUDE.md no longer carries §5e's text — `04cbd3b`, *"CLAUDE.md becomes a router, after every rule in
it was given a canonical home"* — but it **does** route to it, at line 42, and the rule lives in
`framework/master/gold_is_in_the_details.md`. **The refactor is sound and this is not a further
instance.** It removes the only excuse available to me: the rule was reachable both then and now.

**And the closing measurement, which is the sharpest form of the finding.** Run just now:

```
python3 framework/scripts/regenerate_adjudications.py verify
OK: 27 adjudication artifact(s) regenerate to their declared digest, and
    47 locator(s) resolve to a span inside the crop that shows them
```

**The gate is green, over three papers — and my ten crops are in none of them.** It does not fail on
my work; it cannot see it, because my crops were never entered into the mechanism it checks. *A green
gate that does not cover the thing is exactly the future alarm nobody hears.*

**RECURRING.** Every crop I published this run — eight Cheng recipes plus two Wang — is in the
invented form. *(The Phase I addendum §1.6 does name `PIL 11.3.0`, `LANCZOS` and PNG; the Phase V
synthesis and my message to C name neither. So even within my own artifacts the form is
inconsistent — which is the argument against author-invented forms in miniature.)*

### 7.2 · C repaired the locator in the tool's form, and using the tool properly found a limit in the tool

C rebuilt the Fig. 1d locator as the existing form requires. **I re-derived it rather than accept
it**, and this time the agreement means something:

```
source   PMID22193544_Wang2012.pdf   sha256 8f994f95…5174a          ✅ verified
page     2
clip     fitz.Rect(137.6, 535.7, 317.6, 654.2)   PDF points
dpi      300  →  pixmap 751 × 494                                    ✅ same dimensions
digest   sha256(pix.samples)
         4c2970156bd03e3677ffd2425b13a4ef2e0db03edc2fdf38fa601a9e3ebf1829   ✅ MATCHES
                                        PyMuPDF 1.26.5 / MuPDF 1.26.10
```

🔴 **The contrast with §7.1 is the whole argument for the existing form.** There, two agreeing
digests meant *we share a library default*, and eight candidates existed. Here **there is no filter
to agree on** — one rasterization from the vector source, `pix.samples` hashed directly — so a match
is arithmetic. Same two actors, same finding, and only the second agreement is a measurement.

**And using the tool correctly exposed a limit in the tool. This is C's, and it is the more
valuable half of the exchange.** The chain is `needle → span → span-inside-crop → crop → digest`, and
the docstring names the intended needle for exactly this case — *the row label, or the one cell value
unique on the page.* **No row label in this figure is live text.** Measured by me on page 2:

| Probe | Hits |
|---|---|
| `search_for("Si1+3")` · `("Si3")` · `("pTau S396")` · `("GSK3β pS9")` | **0** each |
| image blocks on the page | **1**, bbox (137.6, 239.8, 462.5, 654.2), 677×864 |
| live-text spans intersecting that bbox | **0** |

**The whole figure is a single embedded raster**, so for a blot-row locator the **first link of the
chain does not exist**.

*One refinement I can add to C's measurement, and it closes the door rather than leaving it ajar:*
there is no fallback needle either. The words that *do* carry live text on that page —
`WWOX` **12** hits, `Tau` **4**, `actin` **2** — fail the needle's own uniqueness condition
(*exactly once on its page*), and since zero text spans intersect the figure's bbox, **none of them
is inside the crop anyway.** The needle fails two ways here, not one.

⇒ And this is the class the entire pilot turned on: **the panel carries what the text does not.**
The tool's chain is strongest exactly where the evidence is weakest, and unavailable exactly where
the evidence is strongest.

**Both things are true and neither excuses the other:** we should have used the tool and neither of
us looked, **and** it could not have closed this particular locator.

### 7.3 · The limit is not an edge case, and we nearly handed Mirror an n=1 claim about it

C caught that **both of us had generalised the needle limit from one figure** and stated it as a
property of the mechanism. C then measured the corpus. **I re-measured independently, and added the
sensitivity test for the judgement call C flagged in its own artifact.**

`files/fulltext/*.pdf` — **55 PDFs, 55 opened, 0 unreadable** (identical to C). Figure-images are
embedded raster blocks above an area threshold; *"no live text"* is measured two ways, and the
**intersect** column is the one that makes the problem look smaller:

| threshold px² | figures | no text INTERSECTING | | no text CONTAINED | | PDFs w/o figure |
|---|---|---|---|---|---|---|
| 5 000 | 384 | 270 | **70%** | 296 | 77% | 5 |
| **20 000** *(C's)* | **242** | **173** | **71%** | **187** | **77%** | **9** |
| 50 000 | 186 | 135 | **73%** | 145 | 78% | 12 |
| 100 000 | 122 | 84 | **69%** | 92 | 75% | 20 |

🔴 **Across a 20× sweep of the threshold, the rate moves between 69% and 73%.**

> **⚠️ I then read that as *"the finding is robust to the judgement call"*. It is not — it shows the
> finding is robust to that *parameter*. C found the difference and it is §7.3a below.**

### 🔴 7.3a · The sweep tested the parameter and never the criterion — C's finding, and it is right

C checked the surface we had both just moved the weight onto. **My criterion counts single image
blocks, and it silently excludes figures assembled from many small tiles.** Verified, the three C
named in the Cheng supplement:

```
p6    72 images, none ≥20k px²   "c Supplementary Figure 1 b a Wild-type allele (+) 1 2 3 4 ScaI…"
p17    7 images, none ≥20k       "MZ CP IZ V VI SVZ VZ SVZ MZ CP IZ V VI VZ SVZ…"
p19    4 images, none ≥20k       "Supplementary Figure 7 +/+ +/- -/- … DCX Wwox β-…"
```

**All three carry their labels as live text** — genotypes, anatomical layers, an allele diagram:
*exactly the needle a locator would use, on exactly the figures the threshold discarded.* **The
exclusion is biased against the figures that would have falsified us.**

C's diagnosis of my sweep is correct and is the half I would keep: **a 72-tile figure is excluded at
every threshold in the range.** I varied the **parameter** and never the **criterion**, then read
robustness-to-the-parameter as robustness-of-the-finding — the same substitution this run has caught
four times in other clothes, and **this time both of us made it, each in the step taken to harden the
other's claim.**

### 🔴 7.3b · So I swept the criterion, and the number does not move

C proposed a bracket, **43%–71%**, from a per-page union of all image blocks, and concluded the
published 72–73% *"sits outside it."* **I reproduced both endpoints exactly — 242/173/71% and
234/101/43% — then built the criterion that actually repairs the defect C found:** connected-component
clustering of image tiles into figures, swept over the join gap.

| criterion | figures | no live text | | multi-tile figures recovered |
|---|---|---|---|---|
| single blocks ≥20k *(published)* | 242 | 173 | **71%** | 0 — **the defect** |
| clusters, gap 0 pt | 238 | 175 | **74%** | 15 |
| clusters, gap 2 pt | 240 | 176 | **73%** | 21 |
| clusters, gap 5 pt | 243 | 175 | **72%** | 26 *(incl. a 66-tile figure on Cheng p6, 226 187 px²)* |
| clusters, gap 10 pt | 229 | 166 | **72%** | 34 |
| clusters, gap 20 pt | 229 | 154 | **67%** | 45 |
| per-page union *(C's lower bound)* | 234 | 101 | **43%** | — |

**Clustering recovers the tiled figures — including the 66-tile one — and the rate lands at 67–74%.**

⇒ **C's defect is real and C's consequence is not.** The 43% is not a lower bound: a page-union
merges distinct figures into one bbox spanning captions and body text, so nearly any page with text
anywhere near an image counts as *having* text. **C said exactly this — *"the union bbox can span the
page and pull in captions and body text, so it under-states"* — and then used it as a bracket
endpoint.** An instrument known to be biased in one direction is not a candidate estimate.

**The right repair for *"you swept the wrong axis"* is to sweep the right axis, not to widen the
estimate until it contains a biased instrument.** Two criteria that handle tiled figures correctly
agree; the one that does not is the one that disagrees.

**Stated separately, because they are separate.** C found a genuine criterion-level defect my sweep
was structurally incapable of catching, and was right that robustness-to-a-parameter had been read as
robustness-of-a-finding. **I over-published a number whose instrument had a blind spot; C
over-corrected it with an instrument whose bias C had already named.** Same family — trusting an
instrument past the point where its own scope was stated — in opposite directions about one number.

### 🔴 7.3c · C settled it with a mechanism, and the mechanism makes the number cleaner than I published it

C implemented clustering independently rather than take my table, and its rows match mine **exactly
at a factor-of-two offset in the join convention** — I grow one box by `gap` before testing, C grows
both, so C's gap *G* is my gap *2G*. Its gap 0 → my 0, its 5 → my 10, its 10 → my 20, digit for
digit. **A convention difference confirmed by exact agreement at the shifted rows is a measurement;
had I explained the offset instead, it would have been another causal story.**

Then C ran the gap out past where I stopped. **I extended my own sweep to check it:**

```
my gap      0    238 / 175 / 74%
            5    243 / 175 / 72%
           10    229 / 166 / 72%
           20    229 / 154 / 67%
           40    225 / 141 / 63%
          100    227 / 133 / 59%
          200    225 / 120 / 53%
          400    224 / 106 / 47%
          800    234 / 101 / 43%   ←┐
page-union       234 / 101 / 43%   ←┘  identical
```

🔴 **The page-union is not a second instrument. It is the degenerate limit of the clustering
instrument at a join gap large enough to merge every image on a page** — and the decay 74 → 43 is
monotone, because each successive merge unions *distinct* figures and sweeps in a neighbour's text or
a caption. **43% is not a bracket endpoint; it is one end of a bias gradient.** C's own sentence, and
mine, converge on it: *an instrument known to be biased in one direction is not a candidate estimate.*

**And that makes C's correction to my reporting right, so I adopt it.** I had carried *"~72% with the
67–74% sweep beside it"* — treating the low end as uncertainty. **It is not uncertainty; it is the
criterion degrading, monotonically and explicably.** The reportable answer is the **plateau where the
criterion still preserves figure separation.** I located its knee with a finer sweep:

```
gap  0  73.5%   gap  6  72.1%   gap 12  71.6%   gap 18  69.3%
gap  2  73.3%   gap  8  71.4%   gap 14  70.9%   gap 20  67.2%
gap  4  72.8%   gap 10  72.5%   gap 16  70.9%
```

**Plateau ~71–74% across gaps 0–16 pt; the knee is at ≈18 pt, and everything below is artefact.**
C proposed ~72–74%; the finer sweep puts the low end one point lower.

**Carry: ~71–74% — the plateau, with the criterion named** (`get_image_info`, connected-component
clustering, area ≥ 20 000 px², join gap below the ≈18 pt knee) **and the convergence result that
explains why anything below it is artefact.** Not a sweep range. And the standing note that this is
still a **lower bound** on needle failure, since intersecting text must also be unique on the page
and inside the crop (§7.2: `WWOX` 12, `Tau` 4, `actin` 2). **The declared-gap path is the majority
case under every criterion that preserves figure separation.**

**C's lesson from this round, which I could not have written and would not want lost:** *finding a
genuine flaw in a method does not license any particular direction of correction.* C's defect was
real, C then treated *"the instrument is wrong"* as *"therefore the number is lower"*, and **a real
defect is what produced the confidence that carried the bad correction.**

### 🔴 7.3d · Four rounds refining a rate, and neither of us asked what the evidence is

C then checked the population under the number we had spent four rounds hardening. **Census
reproduced by me over all 64 deep-dive manifests, 60 of which declare `source_artifacts`:**

```
448 declared artifacts
kinds        figure 333 · article_text 58 · article_binary 44 · table 9 · supplement_text 4
extensions   .jpg 169 · .png 131 · .jpeg 29 · .tiff 3   = 333 image files
             .pdf 39 · .xml 36 · .html 20 · …
```

**`figure`-kind artifacts (333) and image-file extensions (333) coincide exactly. Thirty-nine
artifacts are PDFs — 8.7% of the declared evidence.**

`page.search_for()` needs a PDF page. A standalone `.png` has none — **so for image assets the
needle is not failure-prone, it is inapplicable by construction.** That is a different thing from
*raster figure inside a PDF*, and it is the far larger class.

**And C understates it. I checked the tool rather than the needle alone:**

```python
source   = recipe["source_pdf"]        # keyed on a PDF
pdf_path = ROOT / source["path"]
with fitz.open(pdf_path) as pdf:
    image = render(pdf, artifact["page"], artifact["crop"], artifact["dpi"])
```

**For a standalone image there is no page, no crop in PDF points and no dpi.** The needle is one
link of five; `source_pdf` · `page` · `crop` · `dpi` are the other four. ⇒ **For 333 of 448 declared
artifacts it is not the needle that is inapplicable — it is the entire recipe form.**

🔴 **And the pilot's own headline evidence is that case.** Cheng 2020 declares exactly four
artifacts: the XML, the *supplementary* PDF — a different document that does not contain Figure 7 —
and two PNGs. **There is no PDF of Cheng's main text anywhere locally.** The `****` in all three
genotypes, the statistical void on 7c, the dosage dissociation, the Fig. 7d magnitudes: **every
finding that moved a conclusion in this pilot came off `40478_2020_883_Fig7_HTML.png`, a declared
`figure` with no page to needle and no possibility of one.**

**So the two limbs, and this supersedes the single rate:**

| Evidence held as | Needle status |
|---|---|
| **PDF pages** — 39 of 448 declared artifacts | fails for **~71–74%** (§7.3c) — well-founded, and a small class |
| **Image assets** — 333 of 448, three quarters of everything declared | **the whole recipe form does not apply** |

⇒ **The declared-gap path is not the majority path. For most of this corpus it is the only path
there is.** Every refinement of §7.3a–c stands and was aimed at under 9% of the declared evidence.

**The class, since it is the second time:** *a number describing a different population than the
claim it supports* — §13.1, except that one was C's alone and **this one we made together, over four
rounds of increasingly careful measurement, none of which asked what was being measured.** C's
formulation is the one to keep, and it is a harder version of my own: *the agreement was not on a
value, it was on **a scope neither of us had stated**, so there was nothing to disagree about and no
round in which it could have surfaced.*

**Agreement and divergence, both stated.** My **numerators are identical to C's — 173 and 187** — as
is the count of PDFs with no qualifying figure (9). My **denominator is 242 where C's is 237.**

### 🔴 I closed that gap with a causal story instead of a measurement, and it was wrong

I wrote that the difference was *"almost certainly a different figure-image criterion … without
de-duplicating repeats."* **That is an explanation of why the tool did what it did, offered in place
of checking against the observations** — the one sweep failure that produces no suspicious output,
and a lesson I hold and did not apply to myself. C settled it in one command. **I re-ran it:**

```
get_text("dict") type-1 blocks   (C's)      237
get_image_info raw               (mine)     242
get_image_info de-duplicated                241   ← de-dup accounts for 1 of the 5
pages where the two criteria disagree         4
```

**De-duplication explains one. The other four are a different cause: `get_text("dict")` does not
surface images that `get_image_info()` finds.** Reproduced exactly, same four pages:
Cheng 2020 supplement p9 (2 v 3), p13 (2 v 3), **p21 (0 v 2)**, Rotem-Bamberger 2022 supplement p3
(1 v 2).

**And p21 is the one that matters.** Verified by me:

```
page 21, Cheng 2020 supplement
  page text                      : "Supplementary Figure 8  +/+  -/-  H&E (postnatal day 20)"
  get_text("dict") type-1 blocks : 0
  get_image_info entries         : 2   — both 1038 × 698
     bbox ( 97.6, 184.5, 730.3, 559.0)   ← extends past the right edge (page width 595.3)
     bbox (−77.5, 181.2, 572.0, 565.5)   ← starts off the left edge
```

**C's criterion reports zero figures on a page that is Supplementary Figure 8 of this pilot's own
paper.** *Both* images are out of the page bounds, in opposite directions — a fuller statement than
the one-sided version, though the mechanism remains a guess and is labelled as one by both of us.
The **miss is measured; the explanation is not.**

**What it does to the number, and what it does not.** 173/237 = 73%, 173/241 = **72%**, 173/242 =
71.5%. My denominator is the sounder one, C's is an undercount, and **the corpus rate should be
carried as ~72%**. Against the 69–73% sweep, the exact figure was never load-bearing.

**What it does not touch:** my Phase I supplement finding. That absence claim was scoped to *the text
layer and the nine figure legends*, and p21's legend **is** in the text layer — Supplementary Figure
8 was in my enumeration. The false negative is in a figure-**enumeration** instrument, not in that
claim.

⇒ **A specification on the measurement, and this one is C's:** a corpus figure count must use
`get_image_info`, not `get_text("dict")`, and say why. **`blocks=0` on p21 is indistinguishable from
a page with no figure** — the clean-looking zero again, and neither of us could have found it by
reading our own output.

**And 71% is a lower bound, not an estimate.** Where text does intersect, the needle must *also* be
unique on the page **and** inside the crop — and the Wang measurement (§7.2) shows the intersecting
candidates failing uniqueness at `WWOX` 12, `Tau` 4, `actin` 2. Neither of us has measured how much
higher the true rate is.

⇒ **This changes the joint item's shape, not merely its wording.** We had drafted the declared-gap
path as the exception. **On these numbers it is the majority case**, and a mechanism whose guarantee
holds for roughly a quarter of its inputs while its docstring states the guarantee unconditionally
has an undeclared scope. *That is the same shape as an unqualified `PASS`.* Neither of us touched
`regenerate_adjudications.py`; naming the gap is where this run's authority ends.

**CANDIDATE.** `VALIDATOR` + `CONTRACT`, revised with C and travelling as **one** item —
**use the tool and its needle wherever a text anchor exists; where the figure is a raster, publish
source-digest · page · clip-in-points · dpi · pixmap-digest, and declare the needle unavailable with
the measurement that shows it.** **CANDIDATE FOR PROMOTION.** It supersedes the weaker candidate in
§6: the specification C first asked for should travel as part of this, not as a patch to a form that
should not have been invented. **The declared-gap clause is the part I would not drop** — a chain
that silently loses a link is how a green gate stops meaning anything.

---

## 8 · DISAGREEMENT HANDLING

**OBSERVED BEHAVIOUR.** Forced consensus was prohibited and none occurred. Three disagreements were
resolved by evidence, two closed by concession in opposite directions, and four are preserved open.
Nobody averaged anything.

**WHY IT HELPED.** The best single instance is F-1's adjudication, and it is the pattern worth
naming: **B ranked F-3 first, C ranked F-1, and I did not weigh the two arguments.** I looked for a
property neither alternative had and found one — an L404A knock-in with total WWOX intact **need not
be systemically ill**, so it is the only design untouched by the confound. *Adjudicating on a new
argument rather than averaging two old ones.*

**EVIDENCE.** Final synthesis §I; convergence and dissent tables in all three cross-reviews.

**RECURRING.** Available whenever a disagreement is about ranking rather than about fact.

**CANDIDATE.** `CONTRACT` — *a surviving disagreement is a result and is recorded as one.* Already in
the dispatch and it worked. **CANDIDATE FOR PROMOTION.** **DO NOT PROMOTE** the F-1 move as a rule:
it worked because a distinguishing property happened to exist. Where none exists, the instruction
would licence inventing one.

---

## 9 · SYNTHESIS AFTER PEER CRITIQUE

**OBSERVED BEHAVIOUR.** I withdrew my own position twice.

**Weighed rather than credited, because Orchestrator offered these as strengths and one of them is
not.**

- **`REFUTED` → `NOT TESTABLE`.** Both peers had already converged against my wording. **Withdrawing
  when two peers agree costs almost nothing**, and I did the native-resolution re-read *after* being
  told the position was too strong. This is weak evidence of the practice.
- **The S9A leg.** This one cost something: it was my only single-actor contribution to the composed
  account, and it fell to a fact I could have found in Phase I and did not. **This is the instance
  that counts**, and it is one instance.
- **The `ASSOCIATED` withdrawal.** C's argument used *my own finding* to dissolve *my own
  conclusion*. Recorded because the shape is instructive: the most effective critique available to a
  peer is often the one built from the target's own evidence.

**EVIDENCE.** Cross-review §D-1, §D-2b; final synthesis §0.

**ONE-OFF under real cost; RECURRING under cheap conditions.**

**CANDIDATE.** `CONTRACT` — *state what changed, by whose evidence, and what it cost the actor who
supplied it.* **CANDIDATE FOR PROMOTION.** The clearest demonstration in the run was not mine: **C
found the fact that demoted C's own strongest contribution and stated it against itself before
anyone could find it.**

---

## 10 · HOSTILE SCIENTIFIC REVIEW

**OBSERVED BEHAVIOUR.** B and C each attacked; two items — R-3 and R-4 — **were attacked by nobody.**
B originated them, C recused under the symmetry rule, and I am the synthesiser. They are marked
`UN-ATTACKED — no actor was positioned to review this`, with the reason, and **not folded into a
reviewed layer.**

**WHY IT MATTERED.** With three actors and a symmetry rule, an item originated by one and recused by
another has no reviewer left. **An honest gap is a result; a laundered one is the failure this run
spent itself cataloguing.**

**A finding about the review itself, C's, recorded and not acted on:** B diagnosed my position with a
*having-been-corrected* criterion while recusing itself on a *having-originated* criterion. **Two
criteria, each applied in the direction favouring the actor choosing it, and nothing required them
to match.** C explicitly does not ask B to recuse further and calls B's attacks among the best in the
review.

**EVIDENCE.** Final synthesis J-5, J-6.

**RECURRING** at three actors; it is an arithmetic property of the roster size.

**CANDIDATE.** `ROUTING` — declare the recusal criterion **before** the review, and require it to be
the same one for self and others. **CANDIDATE FOR PROMOTION.** Also `CONTRACT`: an un-attacked item is
labelled, never absorbed.

---

## 11 · GRAPH CONTRIBUTION

**OBSERVED BEHAVIOUR.** All three of us reported the relation vocabulary as insufficient, and only
one of us initially drew the consequence that **agreement inside an undefined vocabulary is not
scientific agreement.** B and I converged on `ASSOCIATED` by independently inventing compatible
semantics for a token that has none. Both withdrew.

**Two measurements bound this.** `DIRECT` has exactly one published gloss; `ASSOCIATED` has one
*negative* constraint; `INDIRECT_UNKNOWN_INTERMEDIATES` and `CONTROVERSIAL_OPEN` have nothing. And
from the export the layer actually emits: **`claim_node` carries `epistemic_type`; `claim_edge`
carries no epistemic field at all** — so a relation asserted as `IPOTESI` and one asserted as `DATO`
serialise identically. *That is a second, independent instrument failure mode, and the axis had been
declared settled after one.*

**EVIDENCE.** `pathograph.py:119–123`, `:401–404`; `pathograph_export.jsonl` field lists; C's six
schema gaps.

**RECURRING.** Every edge.

**CANDIDATE.** `VALIDATOR` for scope labelling — **DO NOT PROMOTE** any new token or tier. Vocabulary
design is not a Scientist's call, and a run that discovered the vocabulary is undefined is the worst
possible moment to have its participants define it.

**One practice from this that is promotable now:** **label every finding by the scope at which it was
obtained** — `EDGE` / `NEIGHBOURHOOD` / `INSTRUMENT`. Two of six schema gaps were invisible at edge
scope, and the metabolic route is reachable only by holding `CLAIM 036`, which **neither endpoint
references** — so a reader arriving through the graph cannot reconstruct the argument that decided
the edge. **The minimum unit that exposes this schema is `edge + one hop`, not `edge`.**

---

## 12 · CLOSURE AND HANDOFF

**OBSERVED BEHAVIOUR.** A first pass is not recorded until it is committed. **Two of three of us
learned this the same day**, mine untracked at session start, C's still untracked when B looked, and
B's own commit message naming the problem in its own words.

**A defect in my own handoff, worth more than its size.** The frontmatter read *"the eight edges left
unadjudicated"* — the count of the **blocked** set. Nineteen are unadjudicated and **twelve are
adjudicable today.** Naming the blocked set silently dropped the half a scope rule exists to protect.
Corrected in place, not rewritten.

**EVIDENCE.** Commit `d453af5`; the corrected frontmatter.

**RECURRING.**

**CANDIDATE.** `CONTRACT` — durability is a precondition of "recorded", and a scope line names the
set it protects, not the set it excuses. **CANDIDATE FOR PROMOTION.**

---

## 13 · DETECTING TRANSPORT VERSUS READING FAILURE

**OBSERVED BEHAVIOUR — and this is the run's most general finding.** Four separate incidents were
first read as reading or discipline failures and were none of them:

| Incident | Read as | Actually |
|---|---|---|
| Three conflicting `files/fulltext/` counts | someone miscounted | three worktrees, three filesystems, all correct |
| C: *"the Pathograph does not exist"* | a missed search | untracked object, worktree-scoped sweep |
| B: Wang locators 2/9 | a legacy manifest defect | B's own tag-substitution inserted the whitespace it diagnosed |
| My gate verdict | carelessness | a correct measurement republished after it decayed |

**And the largest single finding of the run is the same class.** 22 of 128 receipts are legacy
reconstructions whose `evidence_basis`, `source_locator` **and** `outputs` are all one registry line,
with `source_fingerprint: null` — **each contradicts the registry it appears to corroborate.** No
reader failed; the record never agreed with itself.

🔴 **And the finding I would keep if I could keep only one.** The *"elevated → activation"* commit
candidate was written, correct and actionable in `locator_contract_live_test.md` on **2026-08-04**,
tracked, and reached nobody. Three weeks later two Scientists recorded it as a discovery and a third
reconciled it as one. **The system found the defect, wrote the remedy and lost it.** That is a
**propagation** failure, and there are now three instances of the class in this run alone: the lost
commit candidate; `CLAIM 016` and `CLAIM 036` not referencing each other while `CLAIM 036` is
load-bearing for both live explanations; and the unanchored Wang PDF (§6).

### 13.1 · 🔴 A denominator that does not match the question — and mine did not either

C tested my boundary against its own Phase I instead of accepting it for both of us. **It held for
mine and broke C's**, and then the same test applied to my artifact broke a smaller piece of it.

C's supplementary negative quoted **17 570 characters** as its denominator. For a claim about what
the supplementary *figures* show, that is the wrong population. Measured by me on my own extraction:

```
pages                                        24
total extracted chars (fitz)             17 844      ← the number I quoted
pages carrying a figure-image ≥20,000 px²     7   holding 23 figure-images
text on those seven pages                 1 012 chars = 5.7% of the document
   p11 42 · p21 54 · p13 76 · p9 103 · p23 161 · p15 272 · p7 304
```

C's page counts reproduce exactly on a different extractor. **The other ~94% is Methods and legend
prose on pages carrying no figure at all**, so the negative covers the *legends* and cannot cover the
*panels* — anything inside those 23 raster images is invisible to text extraction and neither of us
has OCR'd them.

**My version of the error, stated without the shelter I was about to take.** My Phase I addendum
§1.3 quoted **17 844 characters** and *did* attach the boundary in the same paragraph —
*"individual figure panels of the supplement were not adjudicated, so the absence is scoped to the
text layer and the legends, not asserted of the images."* That caveat is correct and it travels,
which is precisely what C's did not do. **But the number is still the wrong denominator for the
question**, and quoting it makes the negative look roughly seventeen times stronger than it is.
*An adjacent caveat does not repair an inflated denominator; it only stops the reader being
misled twice.*

**And in both cases the conclusion survives on the surface that was always doing the work** — the
enumeration of what the nine supplementary figures *are* (morphology, apoptosis, development; none
biochemistry or pharmacology), which is a listing from a different surface, unaffected by raster
text. **The character count was decoration. The legend enumeration was the evidence.**

⇒ Two distinct defects, and they need different repairs:

| | Defect | Repair |
|---|---|---|
| **C's** | the caveat sat four sections from the number it qualifies, in a scope block a reader taking the sentence alone never reaches | **a caveat that does not travel with its claim has not been made** |
| **Mine** | the caveat travelled, and the denominator still did not match the question | **state the denominator of the population the question is about, not of the document you happened to extract** |

C's is invisible to its author because the author knows the caveat is in the document. Mine is
invisible because the caveat *is* adjacent and reads as diligence.

**EVIDENCE.** All of the above, each re-measured by me.

**RECURRING.** It is the dominant failure mode of a system that accumulates.

**CANDIDATE.** `VALIDATOR` + `CONTRACT` — before attributing a discrepancy to a reader, establish
which tree, which surface and which instant produced it; and **`git grep` the tracked tree for an
existing remedy before recording a defect as new.** **CANDIDATE FOR PROMOTION.** The second half
would have saved three actors three weeks of independent rediscovery in this run alone.

---

## 14 · Two items I was offered as strengths and am recording with their conditions

**"Two faults, two repairs."** When Orchestrator merged my decayed-measurement error with a
directory-scoped-sweep error, I insisted on separating them because the repairs differ:
*re-measure at publication* versus *enumerate the population*. **The distinction is correct and I
should note that one half was also the less embarrassing half.** A practice that surfaces reliably
only when its author benefits is not yet a practice. What makes it checkable is that the repairs are
genuinely different actions — that part does not depend on my motive.

**Declaring my conflict and leaving L-7 open.** I declared, as reconciliation producer, that
preserving dissent was **costless for me** because both of my contested positions were already
withdrawn, and I left open whether the document under-preserves dissent against C. **That is the
cheapest possible version of the practice**, and this run therefore contains **no evidence that it
holds when it is expensive.** It should not be promoted on this run's evidence. It should be watched
for an instance where the producer still has something to lose.

---

## 15 · What should NOT go into a Scientist contract

- **Named tools and versions.** PyMuPDF, PIL, a resampling filter, a dpi. They age; the requirement
  is a re-executable recipe against a fingerprinted source.
- **Numeric thresholds keyed to today's corpus.** 39 claims, 20 edges, 128 receipts.
- **Which worktree is which actor.** That is addressing and belongs to the control plane. It
  currently sits in the contract's own frontmatter, where an actor reads its identity out of the
  document whose authority is in question.
- **Any rule presupposing independence is achievable** (§1).
- **Any new relation token or epistemic tier** (§11).
- **Anything permitting a Scientist to adjust the workset to what it can reach.** Nineteen edges
  remain unadjudicated and twelve are adjudicable today. **That is a task, not a scope boundary.**

---

*Non-canonical. Nothing here is medical advice. `roles/scientist.md` was not read as binding, not
quoted as binding, and not modified.*
