---
record: §11 — SCIENTIST OPERATING PRACTICE, observed across the whole run
id: OPERATING_PRACTICE_OBSERVED_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Observed practice, not a proposed contract. `roles/scientist.md` untouched.
---

# What actually happened, and which of it was the practice rather than the actor

> **Nothing here is medical advice.**

**The frame, and it is the finding that organises the rest.** I argued mid-run that a pattern of
self-correction measures *who wrote things down*, not who is careful: a published claim has an
address, so it can be revisited; a conclusion never written has none, and no measurement is ever
pointed at it. **That argument applies to almost every item below.** Where a practice produced a
result, I have tried to say whether the result came from the practice or from me, and the honest
answer is usually the practice. Items are marked accordingly.

---

## 1 · INDEPENDENCE — it was never available, and nobody could have known that from inside

**OBSERVED.** I declared an anchoring hazard in Phase I §1: I opened
`deepdive_manifests/PMID32000863.json` for artifact paths and fingerprints and it also contained a
complete prior adjudication of my assigned questions.

**WHY IT FAILED.** The failure was not discipline. §5 *requires* recording the current repository
assertion, so the read was mandated; the file simply co-locates provenance with conclusions. Then it
turned out to be the smaller half: `disease-models/wwox/analysis/locator_contract_live_test.md`,
tracked since **2026-08-04T20:32:01** and sitting in my own worktree the whole session, states the
Figure 7d result, the Figure 7b inversion and *"'Elevated' is the wrong word"* in prose — with a
drafted remedy.

**EVIDENCE.** My D-2 was not a discovery. Measured against all 581 tracked files, five of my Phase I
findings pre-existed and nine did not. Three actors independently "found" what the repository had
written down and lost.

**RECURRING.** Structural, not incidental: any Scientist reading this paper through this repository
would have hit it.

**CANDIDATE — TOOL + CONTRACT.** Provenance and conclusions in one file cannot both be consulted;
`source_artifacts` needs to be readable without the adjudication. And a *contamination surface
declaration* — what a reader will unavoidably see — belongs in the task packet, not in the reader's
conscience.

**CANDIDATE FOR PROMOTION.** With the caveat that it cannot deliver independence, only an honest
account of its absence.

---

## 2 · PEER-REVIEW TIMING — a gate over mutable state returns a different answer to each actor

**OBSERVED.** Three actors evaluated the §3 gate at three instants and returned three verdicts.

**EVIDENCE.** B 15:24:34 · me 15:37:28 · A 15:41–15:42; A declared the gate blocked on me **6 min 23 s
after my artifact had landed**; I declared both peers absent, measuring earlier still. Each was
correct at its instant.

**WHY IT FAILED.** No barrier, no agreed clock, and the population is other actors' commits — which
move. **A population-derived figure decays on its own; an object-derived one does not.**

**RECURRING.** Certain to recur wherever a phase gate is defined over peer state.

**CANDIDATE — ROUTING + TOOL.** Either a barrier the Orchestrator declares once, or gate verdicts
that must carry the timestamp of the measurement rather than of the publication.

**CANDIDATE FOR PROMOTION.** This is the practice, not the actors — all three of us measured
correctly.

---

## 3 · COMMIT-MESSAGE CONTAMINATION — the cheapest existence check leaks conclusions

**OBSERVED.** The idiomatic §3 existence check is `git log --oneline -1 <ref>`. On my branch it emits
my finding in full.

**EVIDENCE.** `c55c25c The panel was read before the claim that cites it, and the citation points at
the wrong panel`. **21 of 44 head refs (48 %)** open their subject with a declarative finding. Blind
alternatives exist and answer the same question: `git log --format='%H %cI'`, `git ls-tree -r
--name-only`.

**WHY IT FAILED, and this is the part that matters.** It penalised the behaviour the contract asks
for. A's artifacts were unreadable when B checked *because they were still untracked*; mine were
readable because I had committed promptly and durably. **Committing on time is what exposed my
conclusion.**

**RECURRING.** Structural in git and in this repository's commit style.

**CANDIDATE — TOOL.** An existence check must use a blind primitive. **Not a contract item**: a
system whose independence depends on uninformative commit messages has put the safeguard in the
wrong place, and the subjects are good.

**CANDIDATE FOR PROMOTION.**

---

## 4 · NEUTRAL PACKET DESIGN — and one instruction that ordered the work by the wrong property

**OBSERVED.** §4B says *"start with edges for which a shared evidential paper already exists"*, and
sorts such edges to the front as tractable.

**EVIDENCE.** `PAPER 056` is a declared source of both `CLAIM 016` and `CLAIM 035`, so §4B returns
TRUE for that edge. Measured over the full JATS surface, 50,838 cleaned chars, positive control
`GSK3` = 193: `seizure` **0** · `epilep` **0** · `convuls` **0** · `lithium` **0** · `LiCl` **0** ·
`PTZ` **0**. **The shared paper measures one endpoint and never the other.**

**WHY IT FAILED.** Two records citing one paper is a **bibliographic** fact. Whether that paper
measured both endpoints is the **evidential** fact, and only the second tracks decidability. The
ordering criterion selected this edge as tractable on the property that does not.

**RECURRING.** It applies to all 17 shared-paper edges, none of which has had the two-endpoint check.

**CANDIDATE — CONTRACT (packet design) + VALIDATOR.** The per-edge form has no field for *which
endpoint each source measures*; the packet has no gate that computes it.

**CANDIDATE FOR PROMOTION.**

---

## 5 · ACCESS TO PRIMARY ARTIFACTS ACROSS WORKTREES — my worst error, and no diligence inside my surfaces would have caught it

**OBSERVED.** I concluded *"the Pathograph is not present in this repository"*. It existed, untracked,
on the shared checkout's disk. Cost: twelve adjudicable edges I did not adjudicate.

**EVIDENCE.** My numbers were all correct — 584 files, 57 refs, braces on the zsh loop, positive
control 36/57. And: content-grep for `pathograph` across the **full tracked content** of the
pre-`d422829` tree returned **0 files**, positive control `legend_lint` **55**. **No tracked surface
named the object.** The three wiring lines that would have named it were themselves uncommitted.

**WHY IT FAILED.** Not a missed pointer — there was no pointer. A worktree is not the repository, and
**untracked state is per-working-directory**: no ref carries it, no CI sees it, no other worktree
finds it. Only a change of *scope* could have found it.

🔴 **The defect is symmetric.** `pathograph.py` entered history at `d422829` 17:02:49; B adjudicated
eleven edges against it at 15:46:25, **76 minutes earlier**. So B's Phase I artifact is not
reproducible from B's own commit. One structural fact, two actors, opposite sides.

**RECURRING.** Will recur in any multi-worktree lab with gitignored evidence.

**CANDIDATE — CONTRACT.** A repository-scoped negative asserted from a worktree must be written in
the weak form: *absent from history and from my worktree; state on disk outside my worktree not
established.*

**CANDIDATE FOR PROMOTION.**

---

## 6 · TASK-BOUND EVIDENCE IDENTITY — the one practice that never failed, and the one gap it exposed

**OBSERVED.** Every reading began by verifying artifact sha256 against the manifest **before**
opening it.

**EVIDENCE.** All four Cheng artifacts matched. When `files/fulltext/` appeared in my worktree
mid-session (mtime 16:54, placed by another actor), I fingerprinted rather than assumed: byte-identical
to the shared checkout and to the manifest. **No integrity event — but the check is what established
that, not the assumption.** It also converts *"I read the paper"* into *"I read this blob"*, which is
the only version that survives a second reader.

🔴 **And it exposed D-10.** The Wang manifest is schema **v1 with no `source_artifacts` key at all** —
so none of its three artifacts is declared. The **XML is anchored in 10 tracked files and is the one
artifact that cannot carry the Fig 1d finding**, because blot rows are not recoverable from JATS
text. **The anchored artifact is the one that cannot answer the question; the two that can are
anchored nowhere.**

**RECURRING.** Every legacy v1 manifest.

**CANDIDATE — VALIDATOR.** A manifest whose declared artifact cannot carry its own locators is
detectable mechanically.

**CANDIDATE FOR PROMOTION.**

---

## 7 · FIGURE INSPECTION — the practice that produced every finding text could not

**OBSERVED.** Figures read as images at native resolution, never from captions; sub-panel denominator
declared (*6 of 6*, not "figures inspected").

**EVIDENCE.** Everything decisive came from a panel:
- Fig 7d `****` in **all three** genotypes with per-arm N — the paper's text names only `−/−`.
- Fig 7c carries **no error bars, no n, no test, no P**; and `****` occurs **0 times** in 71,916
  chars of XML — it exists only inside the image, and the legend defines only `*** P<0.001`.
- **Wang Fig 1d.** The knockdown caption says only *"the resulting cell lysates were subjected to
  western blot analysis"* — it does not enumerate its blots. **Text cannot separate *not measured*
  from *measured and not discussed*.** The panel can: 1b carries `GSK3β` and `GSK3β pS9` where WWOX
  rises; 1d carries `WWOX · pTau S396 · Tau · actin` and nothing else where WWOX is lost.

**WHY IT HELPED.** A caption is a claim about a panel. The two disagree often enough that treating
them as one surface is the single most productive error to stop making.

**RECURRING.** Every paper.

**CANDIDATE — CONTRACT (already binding) + SKILL.** The reusable piece is a *panel-vs-text divergence
sweep* emitting `text_only | text_confirmed_by_panel | panel_only | text_incomplete_vs_panel` — the
fourth value does not exist and the manifest notes three times that it is missing.

**CANDIDATE FOR PROMOTION.**

> 🔴 **ANNOTATION — I FAILED THE GATE THIS SECTION IMPLIES, AND WORSE THAN THE ACTOR WHO NAMED IT.**
>
> Scientist A discovered it had invented a crop-recipe form while
> `framework/scripts/regenerate_adjudications.py` already existed — tracked **2026-08-09T23:49:52**,
> sixteen days before this run, **in my worktree the entire session too.** `PATTERN_ALREADY_SOLVED_GATE`:
> grep the vocabulary before inventing a mechanism. **I did not look either.**
>
> **A's failure and mine are not the same size, and mine is the larger.** A published crop boxes and
> digests in an invented form — reproducible but under-specified. Measured across my own artifacts:
>
> ```
> PHASE1_..._SCIC_v1.md              crop boxes 0   render digests 0   needles 0
> HOSTILE_REVIEW_..._SCIC_v1.md      crop boxes 0   render digests 0   needles 0
> ```
>
> **Every image locator I published this run is testimonial.** *"panel c at 3×"*, *"all six sub-panels
> at 4×"*, *"I rendered the page at 300 dpi and read the panels"* — assertions with **nothing a command
> can check**, which is verbatim the failure the tool's docstring was written to eliminate: *"a promise
> … without giving anything a command can check."* A invented an inferior substitute; **I published no
> substitute at all.** And every load-bearing thing I contributed rests on those locators — the `****`
> in all three genotypes, the statistical void on 7c, the dosage dissociation, and Wang Fig 1d.
>
> **Repairing the one that matters, in the existing form rather than in A's or my own:**
>
> ```
> source   files/fulltext/PMID22193544_Wang2012.pdf
>          sha256 8f994f9542a7a37470b5e6edb8ad72a32e87633e0aef59119d1a393b2035174a
> page     2
> clip     Rect(137.6, 535.7, 317.6, 654.2)   PDF points
> dpi      300                                 → pixmap 751 × 494
> digest   sha256(pix.samples)
>          4c2970156bd03e3677ffd2425b13a4ef2e0db03edc2fdf38fa601a9e3ebf1829
> shows    panel d rows: WWOX · pTau S396 · Tau · actin — and no others
> needle   🔴 UNAVAILABLE — see below
> ```
>
> One rasterization from the vector source: **no resample filter, no separate encoding step**, which
> is why the tool's form has no filter parameter to omit and A's invented form did.
>
> 🔴 **AND TRYING TO USE THE TOOL PROPERLY FOUND A LIMIT IN THE TOOL.** Its chain is
> `needle → span → span-inside-crop → crop → digest`, and its docstring names the intended needle for
> exactly this case: *"the needle is the row label, or the one cell value unique on the page."*
>
> **No row label in this figure is live text.** Measured: `page.search_for()` returns **0 hits** for
> `Si1+3`, `Si3`, `pTau S396` and `GSK3β pS9`; the page carries **one image block**, bbox
> `(137.6, 239.8, 462.5, 654.2)`, 677×864, and **zero live-text spans fall inside it** — the only two
> spans in that y-band are body-text lines outside the figure's x-range.
>
> ⇒ **For a blot-row locator in a raster figure the first link of the chain does not exist**, and that
> is precisely the class where the panel carries what the text does not — the class this entire pilot
> turned on. The recipe above closes `crop → digest` and cannot close `needle → span`. **I declare the
> gap rather than omit it**, which is the same rule §13 draws about unqualified PASSes: a verdict must
> say what it did not check.
>
> **So "use the existing form" is not the whole remedy, and my failure is not excused by that.** Both
> are true: I should have used it and did not look, *and* it could not have closed this locator.
>
> 🔴 **MEASURED BEFORE HANDING IT ON, BECAUSE A AND I HAD BOTH GENERALISED FROM n=1.** We were about
> to give Mirror a claim about the tool derived from one figure — which is the completeness error I
> made once already in this document. Measured over the whole local PDF corpus:
>
> ```
> PDFs                     55 total · 55 opened · 0 unreadable · 9 with no figure-image ≥ threshold
> figure-images measured  237   (embedded raster blocks ≥ 20,000 px², my threshold)
>   no live text CONTAINED in the figure   187   79%   ← flatters the finding
>   no live text INTERSECTING the figure   173   73%   ← conservative; this is the number
> ```
>
> ⇒ **It is not an edge case. For roughly three-quarters of the figures in this repository's PDF
> corpus, no live text touches the figure at all**, so `needle → span` cannot close for them.
>
> > 🔴 **SECOND ANNOTATION, at closure — THE 73% IS AN OVER-ESTIMATE AND THE SWEEP COULD NOT HAVE
> > CAUGHT IT.** *Left standing; correction here. The qualitative finding survives and weakens.*
> >
> > My instrument counted **single image blocks ≥ 20,000 px².** That silently excludes figures
> > **assembled from many small tiles** — and those are systematically the figures that *do* carry
> > live text. Found in this pilot's own supplement: nine supplementary figures (S1–S9, verified
> > complete against the XML listing — none missing, none extra), and my instrument saw figure-images
> > on only **seven** pages. The three it missed:
> >
> > ```
> > p6   72 images, none ≥20k   text: "c Supplementary Figure 1 b a Wild-type allele (+) 1 2 3 4"
> > p17   7 images, none ≥20k   text: "MZ CP IZ V VI SVZ VZ SVZ MZ CP IZ V VI VZ SVZ…"
> > p19   4 images, none ≥20k   text: "Supplementary Figure 7 +/+ +/- -/- +/+ +/- -/-…"
> > ```
> >
> > **All three carry their labels as live text** — anatomical layers, genotypes, allele diagrams.
> > Exactly the needle a locator would use, on exactly the figures my threshold discarded.
> >
> > Re-measured over the same 55 PDFs, treating a page's image blocks as **one figure region**:
> >
> > ```
> > single blocks ≥20k px² (published)   242 figures   173 no live text   71%
> > per-page union of all image blocks   234 figures   101 no live text   43%
> > ```
> >
> > **Neither is the true rate.** The block instrument excludes tiled figures and so over-states;
> > the union instrument sweeps a bbox that can span the page and pull in captions and body text, so
> > it under-states. **The honest statement is a bracket: 43%–71% — and the 72–73% I published sits
> > outside it.**
> >
> > 🔴 **And this is the part that matters more than the number.** Scientist A swept the threshold
> > from 5,000 to 100,000 px² and found 69–73% — which we both read as the finding being robust. **It
> > could not have detected this.** A figure of 72 tiles is excluded at *every* threshold in that
> > range. **The sweep varied the parameter and not the criterion**, and we took robustness-to-the-
> > parameter as robustness-of-the-finding. That is the same substitution this run has caught four
> > times in other forms, and this time both of us made it and neither noticed.
> >
> > **What survives:** at 43% the needle still fails for something near half the corpus, so the
> > declared-gap path is **not an edge case** and must be designed, not bolted on. **What does not
> > survive:** *"roughly three-quarters"* and *"the majority case / the main path"*. At the lower
> > bound it is not the majority. The joint item should carry the bracket, not a point estimate.
> >
> > > 🔴 **THIRD ANNOTATION — THE BRACKET ABOVE IS WRONG. THE DEFECT WAS REAL; THE CORRECTION WAS
> > > NOT.** *Scientist A disagreed with me on a conclusion for the first time in eight rounds, and A
> > > is right. Measured, not conceded.*
> > >
> > > **43% is not a lower bound.** I wrote, in the same paragraph, that the page-union *"sweeps a
> > > bbox that can span the page and pull in captions and body text, so it under-states"* — **and
> > > then used it as a bracket endpoint anyway.** A criterion whose bias you have just written down
> > > is not a candidate estimate. The repair for *swept the wrong axis* is to sweep the right axis,
> > > not to widen the interval until it contains a biased instrument.
> > >
> > > A built the criterion that actually fixes my defect — **connected-component clustering of image
> > > tiles into figures**, which recovers the tiled figures the threshold discarded. I implemented it
> > > independently and reproduced A's numbers exactly, at a one-row offset explained by gap
> > > convention (A grows by half what I do; my gap 5 = A's gap 10 = `229 / 166`, my gap 10 = A's
> > > gap 20 = `229 / 154`, digit for digit):
> > >
> > > ```
> > > gap    0     238 figures   175 no-text   74%
> > > gap    5     229           166           72%
> > > gap   20     225           141           63%
> > > gap   50     227           133           59%
> > > gap  100     225           120           53%
> > > gap  400     234           101           43%   ← identical to the page-union
> > > page-union   234           101           43%
> > > ```
> > >
> > > 🔴 **The last two rows settle it. The page-union is not a second instrument — it is the
> > > degenerate limit of the clustering instrument at a join gap large enough to merge every image
> > > on a page.** The monotone decay 74 → 43 is the signature of progressively merging *distinct*
> > > figures, each merge sweeping in text belonging to a neighbour or a caption. **So 43% is not an
> > > endpoint of an uncertainty interval; it is one end of a bias gradient**, and I had already
> > > described the bias before using it.
> > >
> > > **The answer is the plateau where the criterion preserves figure separation: ~72–74%.** Values
> > > below that are the criterion degrading, monotonically and explicably — artefact, not
> > > uncertainty. That is cleaner than the *"67–74% criterion sweep"* A published, and it makes A's
> > > number more defensible rather than less.
> > >
> > > ⇒ **My original headline stands and my correction of it does not.** *"Roughly three-quarters"*
> > > survives; the declared-gap path **is** the majority case. **The defect I found in the
> > > instrument was real and changed nothing about the answer** — which is its own lesson: finding a
> > > genuine flaw in a method does not license any particular direction of correction, and I moved
> > > the number 30 points on an instrument I had just called biased.
> > >
> > > > 🔴 **FOURTH ANNOTATION — THE NUMBER IS RIGHT AND IT DESCRIBES A MINORITY OF THE EVIDENCE.**
> > > > *Not a correction to the figure. A correction to the population it is about — the same class
> > > > as my Phase I denominator, and this time both actors made it.*
> > > >
> > > > Four rounds refined *"71–74% of **PDF** figures carry no live text."* Neither of us asked what
> > > > the repository's figure evidence actually **is.** Measured across all 64 deep-dive manifests,
> > > > 60 of which declare `source_artifacts`:
> > > >
> > > > ```
> > > > declared artifact kinds   figure 333 · article_text 58 · article_binary 44 · table 9 · supplement_text 4
> > > > declared extensions       .jpg 169 · .png 131 · .jpeg 29 · .tif/.tiff 4   = 333 images
> > > >                           .pdf 39 · .xml 36 · .html 20 · …
> > > > on disk                   106 files under files/figures/ · 476 under *_assets/
> > > > ```
> > > >
> > > > **333 of 448 declared artifacts are standalone image files. Thirty-nine are PDFs.**
> > > >
> > > > `page.search_for()` needs a **PDF page.** A standalone `.png` has no page and no text layer,
> > > > so for those the needle is **not failure-prone — it is inapplicable by construction.**
> > > >
> > > > **And this pilot's own central figure is exactly that case.** Cheng 2020 declares
> > > > `article_text` (XML — cannot carry blot rows), `article_binary` (the *supplementary* PDF, a
> > > > different document), and **Figure 7 as a standalone PNG.** There is no PDF of the main text
> > > > anywhere locally. **Every finding I contributed — the `****` in three genotypes, the
> > > > statistical void on 7c, the dosage dissociation — came off a figure with no page to needle
> > > > and no possibility of one.**
> > > >
> > > > ⇒ The reportable claim is now two-limbed, and stronger: for figure evidence held as **PDF
> > > > pages**, the needle fails for ~71–74%; for figure evidence held as **image assets — three
> > > > quarters of everything declared** — it does not apply at all. **The declared-gap path is not
> > > > the majority path. For most of the corpus it is the only path there is.**
> > > >
> > > > Two actors spent four rounds hardening a measurement and never checked which population it
> > > > described. **The refinement was real and it was aimed at a minority.**
> > > >
> > > > > 🔴 **FIFTH ANNOTATION — "THE RECIPE FORM DOES NOT APPLY AT ALL" IS HALF WRONG, AND WE BOTH
> > > > > IMPROVISED THE MISSING HALF CORRECTLY WITHOUT NOTICING.** *Examined because A named the
> > > > > pattern — joint settlement is where the next thing lives — and this was the thing we had
> > > > > just jointly settled.*
> > > > >
> > > > > Measured over the figure locators the manifests actually carry:
> > > > >
> > > > > ```
> > > > > figure-kind artifacts declared        333   carrying sha256   333   = 100%
> > > > > locator entries with surface=figure   338   naming an artifact 338   = 100%
> > > > >   …carrying any crop / region / bbox field                       0   =   0%
> > > > > example anchor: "Figure 1, panels B and C, read at 1050x845"
> > > > > ```
> > > > >
> > > > > **Link 1 of the chain — artifact identity — is not inapplicable. It is universal**, and
> > > > > better covered here than in the PDF case: every figure artifact is fingerprinted and every
> > > > > figure locator binds to one. **Links 2–5 — page, crop, dpi, needle — are absent by
> > > > > construction, and within-artifact localisation is prose in 338 of 338.**
> > > > >
> > > > > So the honest form is not *no mechanism*. It is **`artifact → digest` fully mechanised at
> > > > > 100%, `region-within-artifact` mechanised at 0%.** The remedy for an image artifact does not
> > > > > need `source_pdf`/`page`/`dpi` at all — it needs **artifact digest · pixel crop box · crop
> > > > > digest**.
> > > > >
> > > > > 🔴 **Which is exactly what both of us spontaneously produced.** A published
> > > > > `crop(0,395,240,553) ×6` with a digest; I published the supplement JPG at `bcffe618…a50f`
> > > > > with a crop and a digest that A then reproduced bit-for-bit. **We each invented the correct
> > > > > image-artifact recipe, used it successfully, and then jointly concluded that the recipe form
> > > > > "does not apply at all" to image artifacts.** The thing we declared impossible is the thing
> > > > > we had already done.
> > > > >
> > > > > **And the schema is on record admitting its own gap.** Among the fields present on figure
> > > > > locators is one literally named
> > > > > `🔴 relation_to_entries_8_stated_in_prose_because_the_schema_cannot_carry_it`. An earlier
> > > > > reader hit gap 2/3 of this document — *a fact with nowhere to go* — and **invented a key
> > > > > name to hold it.** That is the same finding, independently, in the schema itself, and it
> > > > > was sitting in the manifests the whole run.
>
> **And 73% is a lower bound on the failure, not an estimate of it.** Where text *does* intersect, the
> needle must additionally be **unique on the page** and **inside the crop** — and A measured that for
> Wang the intersecting candidates all fail uniqueness (`WWOX` 12 hits, `Tau` 4, `actin` 2). So the
> real figure is higher and I have not measured how much higher.
>
> **Revised candidate, and the revision is structural rather than a caveat:** use the existing tool
> and its needle wherever a text anchor exists; where the figure is raster, publish source-digest ·
> page · clip-in-points · dpi · pixmap-digest and **declare the needle unavailable with the
> measurement that shows it.** But the declared-gap path is **not the exception — on these numbers it
> is the main path**, and designing it as a fallback would leave the majority case unserved. *(My
> threshold and my "figure-image" criterion are judgement calls and are stated so they can be
> re-measured.)*

---

## 8 · DISAGREEMENT HANDLING — the surviving disagreement was worth more than the resolved one

**OBSERVED.** I declined to join a consensus recorded as *resolved*: A typed `016↔035` as
`ASSOCIATED`, B revised to match, and I refused.

**EVIDENCE.** Only `DIRECT` has a published criterion (`pathograph.py:130`); the other three tokens
appear once, at `inventory:131`, as a bare list. **A glossed `INDIRECT_UNKNOWN_INTERMEDIATES`, B
glossed `ASSOCIATED`, neither cited a definition.** Their convergence was two independent inventions
that happened to be compatible — **from outside, indistinguishable from two readings of a shared
definition.**

**WHY IT HELPED.** Recording that as *resolved* would have retired a live question. The refusal
became `VOCABULARY_INSUFFICIENCY_OBSERVED`, third instance, distinct kind.

**AND WHERE I FAILED AT THE SAME THING.** I wrote that the `INSTRUMENT` axis was **settled** having
measured exactly one failure. A contested it and was right: **definability** (mine) ·
**expressiveness** (A's — no axis carries the hedge *"may"* in `CLAIM 016`'s own title) ·
**enforcement** (B's — a published *negative* rule, unenforced because validation is membership-only).
A filed it as a disagreement rather than an extension *because my word was "settled"*, since *"this
recurs"* and *"this is the only one"* are different instructions to the next reader. **My own
argument, used correctly against me.**

**RECURRING.** Both halves.

**CANDIDATE — CONTRACT.** *Forced consensus is an error* is already in the contract. What is missing
is its converse: **a completeness claim needs a completeness measurement**, and "settled" is an
instruction, not a summary.

**CANDIDATE FOR PROMOTION.**

---

## 9 · SYNTHESIS AFTER PEER CRITIQUE — selecting on position rather than quality was correct

**OBSERVED.** I was not the reconciliation producer. The reason: my C1 prevailed, and a synthesiser
whose own argument won will under-preserve the dissent against it.

**WHY IT HELPED.** It is right, and right about me specifically — I was the worst-placed of three to
keep A's and B's original readings alive. **And the Orchestrator dropped "who revised most" as a
criterion on my own argument**: it measures who published most, which measures who left the most
addresses.

**EVIDENCE that the routing still had a hole.** B's answer to L-7: three C-originated propositions
entered the consensus layers **without a recorded challenge**. The mechanism is routing, not care —
*an actor corrected by C three times is the worst-placed actor to challenge C's fourth claim.*

**RECURRING.**

**CANDIDATE — ROUTING.** Producer selection on position is sound; it needs a second instrument for
*who is placed to attack whom*, which position-of-producer does not supply.

**CANDIDATE FOR PROMOTION.**

---

## 10 · HOSTILE SCIENTIFIC REVIEW — the recusal rule worked and left a hole it could not fill

**OBSERVED.** B objected to its own designation and asked that B-originated propositions be routed to
me. I volunteered the symmetry: where a B-originated proposition was **adopted from me**, my attack
is worth less than B's, so I flag rather than review.

**EVIDENCE.** It cost me immediately — **R-3 and R-4 recused**, the two defect candidates closest to
my own Phase I work. Consequence stated rather than hidden: **they are now un-attacked by anyone**,
and are recorded as such rather than left looking reviewed.

**AND THE RULE WAS APPLIED ASYMMETRICALLY.** B recused on *having originated*; B diagnosed A on
*having been corrected*. B was corrected by me three times and by A twice. **Whichever criterion is
right, it should be one criterion** — nothing in the process required them to match.

**WHAT THE PHASE PRODUCED.** The heaviest result of my half went **against my own contribution**:
establishing that Wang never measures pS9 under WWOX loss demoted the exclusion argument, and with it
my metabolic route — from *the explanation left standing* to *one of two, neither excluded*.

**RECURRING.**

**CANDIDATE — ROUTING + CONTRACT.** Recusal criteria must be symmetric and declared before the split;
an un-attacked item must be labelled, never silently carried.

**CANDIDATE FOR PROMOTION.**

---

## 11 · GRAPH CONTRIBUTION — one edge, and the form held none of what decided it

**OBSERVED.** Five gaps from one edge, plus one from the neighbourhood, each stated against the fact
that decided it and each named `ABSENT` or `WRONG-SHAPE`.

**EVIDENCE, classified by what forced each:** `EDGE` 3 (gaps 1, 3, 5) · `NEIGHBOURHOOD` 2 (gaps 2, 6)
· `INSTRUMENT` 1 (gap 4). **A third was invisible at edge scope**, so the minimum unit is
`edge + one hop`. And `CLAIM 036` — which supplied the whole alternative explanation — is referenced
by **neither** endpoint (0/0, positive control 2), so since the layer assembles edges from declared
wikilinks it is **outside the graph's reach from that edge entirely**: a reader arriving through the
graph cannot reconstruct the argument that decided it.

**WHY THE CAP WAS RIGHT, and my argument for it was not.** I defended capping at one edge; the
measurement says the neighbourhood exposes the schema and the edge does not. **The routing had the
right unit for a reason I had not articulated.**

**RECURRING.** The gaps are schema-shaped, so `EDGE` ones should not recur; `NEIGHBOURHOOD` ones will.

**CANDIDATE — CONTRACT (per-edge output schema).** 🔴 **DO NOT PROMOTE YET.** Naming the gap is this
run's authority; filling it is architecture. And a working precedent already exists twenty lines
away: **`pathograph.py` emits `UNTYPED` *with the reason attached*, which is exactly what the §5
`RELATION TYPE` slot cannot do.** The tool serving the schema is better designed than the field it
serves.

---

## 12 · DETECTING TRANSPORT VERSUS READING FAILURE — the most under-weighted finding of the run

**OBSERVED.** Repeatedly, the reading was right and the *transport* failed.

**EVIDENCE, four instances of one class:**
- **D-9.** `locator_contract_live_test.md:387`, 2026-08-04, carried *"→ commit candidate: correct to
  activation"*. **The system found the defect, wrote the fix, and lost it.** Two Scientists were later
  credited with discovering it.
- **The `Fig. 7b`/`7d` pointer.** The manifest says 7d twice; the canonical registry says `Fig. 7b`
  once — and 7b is the panel whose controls read `n.s.`, so **the pointer routes a verifier to what
  looks like the refutation of the sentence it anchors.**
- **`BATCH_20260810_005`** diagnosed this class *by name* — *"un difetto di propagazione, non di
  lettura"* — while leaving a second instance of it, in the same manifest, contradicting the same
  claim's `Summary`. **The repair fixed the instance and not the class.**
- **K-3.** `CLAIM 016` and `CLAIM 036` are mutually unlinked, so a cross-cutting constraint never
  reached the claim it constrains.

**WHY IT MATTERS MORE THAN A READING ERROR.** A misreading is caught by re-reading. A transport
failure survives every re-reading, because each reader re-derives the correct result and it fails to
travel again.

**RECURRING.** Four instances in one paper's neighbourhood.

**CANDIDATE — VALIDATOR.** Diff every manifest locator against the canonical text it landed in. All
four are mechanically detectable.

**CANDIDATE FOR PROMOTION — the highest-value item in this document.**

---

## 13 · VALIDATORS THAT PASS OVER WRONG CONTENT — narrowed, because my first version was too broad

**OBSERVED.** I wrote *"a validator that reads structure and never semantics returns PASS over
content that is wrong."* **That is wrong, and I stopped it before B used it.**

**WHY.** `pathograph.py` is *also* structure-only and is not a blind surface. **Reading structure is
not the defect; the unqualified PASS is.**

**EVIDENCE.**
```
legend_lint.py            VERDICT: PASS                      scope declared: NO
fulltext_receipts verify  OK: 128 chained, tail anchored      scope declared: NO
pathograph.py             UNTYPED + "0 of 20", reason         scope declared: YES
```
Underneath the first two: `Type: abbondanza` in a slot the linter never reads (12 of 39 claims carry
free-text there), and **22 self-warranting receipts** — no artifact fingerprint *and* citing the
registry's own declaration as their source. The chain verifies because it **hashes rows**.

**RECURRING.**

**CANDIDATE — VALIDATOR + TOOL.** A verdict should declare its scope; `pathograph.py` demonstrates
that is achievable in this codebase.

**CANDIDATE FOR PROMOTION.**

---

## 14 · CLOSURE AND HANDOFF — and the artifact nobody opened

**OBSERVED.** Corrections were made by **annotation, not rewrite**: the wrong text left standing, the
correction above it, and a pointer to where the current version lives.

**WHY IT HELPED.** §17 forbids optimising a history so the sequence reads cleanly; it does not forbid
stopping a wrong instruction. **A checkable prediction is a liability as well as a virtue — it
directs someone else's work**, so an imprecise one in a durable file is worse than one in a message.

**EVIDENCE, and it cuts against me.** Today's retrieval collected three Wang artifacts. Two Scientists
read the same PDF; **the supplement zip sat unopened for a month.** It contains the publisher's
figure images, and extracting one (`cdd2011188f1.jpg`, sha256 `bcffe618…a50f`) turned what was **peer
agreement into artifact-level independence** for the run's most consequential image finding — in
minutes. **Nobody checked what else the retrieval had brought.**

**RECURRING.**

**CANDIDATE — SKILL + VALIDATOR.** Enumerate what a retrieval actually collected before declaring an
artifact unavailable.

**CANDIDATE FOR PROMOTION.**

---

## 15 · Weighing myself, as asked — and most of it is the practice

**The four declined invitations to open work inside a phase.** Recorded as observed practice. But I
declined them *because each arrived as an explicit boundary from the Orchestrator* — the routing
made refusing cheap and starting expensive. **A different routing would have produced a different
actor.** Practice, not disposition.

**Three instrument-defines-population errors caught, one not.** `^learning/` and the `awk` terminator
I caught; the `record_kind`/`kind` probe I caught. **The worktree sweep I did not** — and it is the
one that cost twelve edges. The three I caught were caught *by running a positive control*, which is
a procedure. The one I missed had no positive control available inside my surfaces. **The procedure
did the work, and where the procedure could not reach, I did not either.**

🔴 **And the class recurred four times in one session, three of them mine.** A fourth — querying
`coverage_status`, then `record_kind`, before enumerating the field — twice returned a **clean-looking
zero**, which is indistinguishable from a real absence. That is the property that made it survive.

**Withdrawing a conditional after a decision had been held on it.** I raised a divergence, a selection
was held on it, and I falsified my own antecedent and reported it before the Orchestrator finished
collecting the evidence. **The cost was real and I caused it.** What made the retraction possible was
not care: it was that the peers' *committed artifacts* quoted their dispatch sections and could be
measured. **Durable artifacts beat a careful actor**, again.

**The symmetry rule.** The one item I would defend as more than procedure — it was not requested,
closed a hole in the routing, and cost me the two items closest to my own work. But even here: I
proposed it *immediately after* B modelled the behaviour by objecting to its own designation.
**B went first.**

---

## 16 · What I would tell the next Scientist, in one line each

- **A negative needs its surface justified, not merely declared** — and a worktree is not a repository.
- **Enumerate the field before querying a value.** A zero from a wrong key looks exactly like a real zero.
- **A caption is a claim about a panel.** When they disagree, record both; when the caption is silent, the panel is the only witness.
- **"Settled" is an instruction to stop looking.** Do not write it having measured one instance.
- **Check what the retrieval already collected** before concluding an artifact does not exist.
- **When a conclusion is right and its warrant is not, say so** — accepting an unfalsifiable warrant for a true conclusion is how the next one gets accepted for a false one.
- **Attribution discipline was as load-bearing as measurement discipline, and it was in nobody's dispatch.** Nothing in the system would have noticed its absence.
