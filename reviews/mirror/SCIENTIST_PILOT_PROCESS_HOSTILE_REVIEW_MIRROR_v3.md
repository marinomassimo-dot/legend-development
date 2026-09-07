---
artifact: MIRROR hostile review (Annex C.2) — Scientist cross-review pilot, as a PROCESS and EVIDENCE SYSTEM
review_id: SCIENTIST_PILOT_PROCESS_HOSTILE_REVIEW_MIRROR_v3
object: the closed PMID 32000863 three-Scientist cross-review pilot — Phase I…V plus the
  post-closure round; 29 Scientist artifacts, the Orchestrator packet and Mirror handoff, the
  needle/crop and manifest gates, and the interaction record itself
level: R4 (METHOD — Mirror; C.1 floor for a methodology-changing inferential process;
  C.4 object class SYSTEM → Mirror)
reviewer: mirror
author: three Scientist seats + Orchestrator (addressed by seat, never by session)
adjudicator: none granted or implied here
date: 2026-08-25
verdict: REFINED — see § 1
relation_to_prior: COMPLEMENTS `PATHOGRAPH_PIPELINE_HOSTILE_REVIEW_MIRROR_v2` (Pathograph layer,
  DisMech boundary, provenance chain). It does not supersede it. v2 was pinned at 13:32Z; the run
  produced 24 further commits after v2 closed, and this review binds to the actual tips.
governance_loaded: 3.1.1
personal_data: none introduced. The human role is `Operator` throughout. § 4.5 reports a
  pre-existing exposure on `main`; it names no person and quotes no identifier.
scope_note: every number below was produced by executing a command in this session. Where I report
  another actor's figure I re-derived it and say by how much we differ. Where I could not
  re-derive it, I say so. Nothing was mutated: § 0.4.
---

# The taxonomy is nearly right and the package is not complete — and three of the four gaps are in what the gates never look at

---

## 0 · OBSERVATION_SCOPE

Every negative below is scoped to this table. **Local NOT_FOUND is not repo-wide NOT_EXIST.**
I inherited no scope declaration from the producers; each row was re-measured here.

### 0.1 Refs and trees

| Fact | Value |
|---|---|
| Derivation instant | `2026-08-25T19:16:40Z` |
| My worktree / HEAD | `.claude/worktrees/mirror`, branch `mirror` @ `c7e8d6e` — **0 behind `main`**, 84 ahead |
| `main` | `788c357` |
| Scientist A | `.claude/worktrees/lettore`, branch `lettore` @ `605fc5d` — **201 behind `main`**, 16 ahead |
| Scientist B | `.claude/worktrees/lettore-b`, branch `lettore-b` @ `9a09590` — 0 behind, 16 ahead |
| Scientist C | `.claude/worktrees/lettore-c`, branch `lettore-c` @ `5b1d6c2` — 0 behind, 14 ahead |
| Orchestrator (packet) | shared checkout `/Users/…/legend-public`, `legend-operating-convention-v1` @ `a58af46` — 0 behind, 26 ahead |
| Plan | `.claude/worktrees/evidence-index`, `plan-orchsurf-r4-transcription` @ `e4aa80c` — 2 behind |
| Ref population swept | all 44 `refs/heads` + 5 `refs/remotes`, enumerated with `git for-each-ref` |
| Sweep positive control | `LEGEND` present in 215 tracked files on `main`; `Phase II` present on all four pilot refs |

### 0.2 Artifacts inspected — the denominator of this review

| Seat | Path prefix | Docs read or scanned |
|---|---|---:|
| A | `learning/scientist/`, `framework/protocols/` | 12 |
| B | `reviews/scientist-b/`, `learning/scientist-b/` | 12 |
| C | `learning/scientist/` | 5 |
| Orchestrator | `learning/orchestrator/` | 3 (packet · practice · Mirror handoff) |
| **Total scanned for object archaeology** | | **29 docs · 746,625 bytes** |
| Privacy sweep population | same four prefixes | **48 `.md` files** |

Tools executed: `legend_lint.py` · `fulltext_receipts.py verify` · `growth_anchors.py check` ·
`regenerate_adjudications.py verify` (all 3 recipes, and per-PMID) · `deepdive_manifest.py
--verify-artifacts` (all 64 PMIDs) · `independent_privacy_scan.py` · `public_release_gate.py
--mode release` · `test_regenerate_adjudications.py` · plus three scripts I wrote for this review
(artifact census, locator partition, figure/no-text gradient).

### 0.3 What I could NOT reach — declared, not inferred

- **The dispatch text the three Scientists actually received.** The Orchestrator reports two
  divergent dispatches (§4.5 of its handoff). Neither is a durable artifact I can open. Every
  statement here about what an actor was *asked* to do is read off the actor's own record.
- **The figure/no-text sweep on a per-seat surface.** `files/` is gitignored and per-worktree, so
  the sweep can only run where the PDFs are. See M3-4 — this is a finding, not merely a limit.
- **The densitometry re-reads.** I adjudicated no panel and no biological proposition.

### 0.4 This review mutated nothing

`git status --porcelain` in my worktree is unchanged from session start (the same 10 untracked
Mirror records, now 11 with this file). The shared checkout, `lettore-b` and `lettore-c` were
clean before and after. `lettore` carried one uncommitted manifest edit before and after
(§ 6.4). All mutation testing ran on copies under the session scratchpad, through the tools'
own `--workspace` flag; the four canonical current files were never opened for writing.

---

## 1 · VERDICT

### STEELMAN (C.2 — mandatory, before the objections)

Six things in this package are better than the state of the art it replaced, and I could not
break any of them.

1. **The producers asked the right question.** The handoff opens by declaring its own defects
   *"so that Mirror's finding them again would be a null result."* That inverts the usual
   incentive and it worked: five of my confirmed findings are outside the disclosure list
   precisely because the list cleared the cheap ground.
2. **The four-class split is defensible and I keep it.** Transport · undeclared scope ·
   narrated gap · denominator-question mismatch. I attacked the boundaries (§ 2) and each
   survives, because each implies a *different* repair layer. The producers' own resistance to
   collapsing them into one closing sentence was correct.
3. **The convergence on the figure-coverage gradient is real and reproduces in a fourth hand.**
   My independent implementation gives 289 image-bearing pages, 55/55/0 PDFs, 9 figure-less, and
   a monotone decay to a plateau at join gap 800 that equals the page-union — the load-bearing
   shape, reproduced without reading their code (§ 3.3).
4. **No canonical state was touched by any seat, and I proved it the hard way.** Zero current-file
   modifications relative to each branch's *own* base, with a positive control showing the command
   is capable of returning non-zero (§ 4.4). LINT `PASS`, receipts `OK — 128 chained, tail
   anchored`, growth anchors `PASS`.
5. **The self-attribution discipline is the strongest cultural artifact here.** Actors refused
   blame that was not theirs, filed defects against their own headline findings, and one
   abandoned a correction it had made confidently on the back of a real finding. That is rare and
   it is not decorative — it is what made the record auditable from outside.
6. **The producers' recommendation against a new reviewer actor is correct**, and my evidence for
   it is independent of theirs (§ 8).

### KEY OBJECTION

**The package is true on the surfaces it inspected and it is not complete — and the incompleteness
has one shape: every seat measured a tree, and no seat measured which tree.**

Scientist A ran the entire pilot from a base **11 days and 217 files behind** the base B and C
used. Its own proposed output contract publishes five populations — 49 manifests, 813 locators,
53 paper records — that are 23–32 % stale against `main`, in a document whose § 0 states *"a count
whose population was defined by the counting tool is not a measurement."* The three-hands
agreement the package offers as its proof of measurement-over-consensus (55 PDFs / 55 opened /
0 unreadable) is agreement over **one gitignored directory** that only the shared checkout holds.
None of this is on the disclosure list, and it is the confound under every "A found what B
missed" sentence in the record.

### VERDICT: `REFINED`

`REFINED_FORMULATION` — the proposition as submitted:

> *The pilot exposed a set of distinct failure classes complete enough to support surgical repair.*

as it survives review:

> **The pilot's four failure classes are distinct, correctly named, and each maps to a different
> repair layer — that half is CONFIRMED. The set is not complete. Four further confirmed instances
> sit outside the disclosure list, all of the same two classes the pilot already named, which is
> itself the finding: the classes generalise further than the producers applied them. Surgical
> repair is available now, without reopening exploratory science, provided five bounded closures
> land first — one of which (§ 4.5) is a standing privacy-gate blind spot on `main` that the pilot
> neither caused nor detected and that no producer is authorised to close.**

`REVIEWER_CONFIDENCE` — **high** on every mechanical finding: all executed, all with a stated
denominator, and the four gate findings carry a mutation battery with positive *and* negative
controls (§ 4.1–4.3). **Medium** on the interaction classification of § 6, which rests on reading
prose the actors wrote about themselves. **Low-to-none** on anything biological: I adjudicated
nothing.

`RESIDUAL_UNCERTAINTY` — I cannot see the dispatch texts, so the "review prompts biased actors
toward additive extension" hypothesis (§ 6.3, explanation 3) is **untestable from my surface** and
is recorded as such rather than dismissed. My own figure/no-text counts run 4–8 lower than the
producers' at every join gap; I did not resolve the criterion difference, and I did not need to,
because the shape and the plateau reproduce.

`WHAT_WOULD_CHANGE_MY_MIND` — three things, and each is a single command:

1. A ref stamped in `scientist_evidence_standard.md` § 0 alongside its five populations, and the
   three stale counts re-derived there. That removes M3-2 and most of M3-1's consequence.
2. `regenerate_adjudications.py verify` wired into `run_release_regressions.py`, plus one test
   that opens a real recipe. That removes M3-8.
3. A `PRIVATE_NAME` rule that fires on the lowercase path form, demonstrated by the fixture pair
   in § 4.5. That removes M3-10.

With those three landed, this review moves to `CONFIRMED` on everything except § 6, which needs
the dispatch texts and not another measurement.

---

## 2 · THE FAILURE TAXONOMY, ATTACKED

The dispatch asks me not to accept the producers' A–E labels. I tested each boundary against the
question *"do these two require different repairs?"* — because a taxonomy that does not change the
repair is narrative, not engineering.

| Producers' class | Distinct? | Repair layer it implies | Mirror's verdict |
|---|:--:|---|---|
| **A · Transport** — correct evidence existed, did not reach the surface that needed it | ✅ | plumbing: carry the reference, not the restatement | **KEEP.** 5 disclosed instances + 2 I confirmed new (M3-5, M3-6). The repair is a field, not a reviewer. |
| **B · Undeclared scope** — a guarantee stated unconditionally, reaching a bounded subset | ✅ | tool/docstring + gate: the verdict must print its own population | **KEEP, and it generalises further than they applied it.** M3-8, M3-9, M3-10 are three new members, all in gates the pilot never examined. |
| **C · Narrated gap** — a discrepancy answered with a causal story instead of a measurement | ✅ | skill/mode: a refusal, needs no tool | **KEEP.** Cheapest to prevent, and A was right that this is the distinguishing property. |
| **D · Wrong denominator** — a correct measurement reported against the wrong population | ✅ | contract: state the population the *question* is about | **KEEP, and it recurs inside its own repair** — see below. |
| **E · Shared blind spot / consensus without coverage** | ⚠️ | **not a fifth class** | **MERGE into B.** See below. |

### 2.1 E is not a fifth class — it is B observed from the outside

The producers' own formulation gives the reason: *"eight rounds of adversarial cross-examination
cannot falsify what neither party has asserted."* That is a statement about an **unstated scope**
— class B — plus the observation that peer review cannot repair B. The failure mode is B; the
*consequence* is that adding reviewers does not touch it. Splitting them invites the wrong fix
(more seats) for the right diagnosis (declare the scope).

**Repair test, which is what decides it:** B's repair is "the guarantee prints its population." E
has no repair of its own — E is what happens when B's repair is absent and you add reviewers
anyway. Merged.

### 2.2 D recurs inside the correction that names it — CONFIRMED, mechanically

This is the sharpest structural finding about the taxonomy, and it is not a criticism of the
insight: it is evidence that the class is deeper than one instance.

The producers correct a denominator error (17,844 characters → the figure-page population), then
correct a second one (PDF pages → declared artifacts), landing on **39 / 448 = 8.7 %** and
**333 / 448 = 74.3 %**. I reproduce both figures *exactly* at `main` (§ 3.1). But **448 declared
artifacts is not the population of the mechanism under discussion either.**

Three different populations, all defensible, all giving different answers:

| Population | Count | Whose question it answers |
|---|---:|---|
| PDFs among manifest-declared artifacts | **39 / 448 = 8.7 %** | the producers' — "what share of declared evidence *could* the crop recipe reach?" |
| Local PDFs on disk (rule 5e's own population) | **55**, of which rule 5e says *"33 … will eventually need adjudicating"* | `gold_is_in_the_details.md` § 5e's — and its stated 51 has decayed to 55 |
| **Recipes the gate actually holds** | **3 papers · 27 crops · 47 locators** | the one that decides whether a green gate means anything |
| **All verbatim locators corpus-wide** | **1,002**, of which **47 (4.7 %)** are crop-verified | the one a consumer of the evidence needs |

⇒ **MIRROR FINDING M3-3.** The class is correctly named and was applied one layer short. This is
not a defect in the producers' reasoning; it is the reason D deserves a contract line rather than
a lesson.

### 2.3 One class is missing, and it is the one this pilot is made of

Neither the disclosure list nor the four classes name: **a measurement whose validity depends on
which ref it was taken at, published without the ref.** It is adjacent to D and it is not D — D is
*which population*, this is *which snapshot of that population*. It produced M3-1, M3-2 and M3-3,
and it is the only class here that is invisible to every actor inside the run, because a tree
looks the same from inside whatever its age.

Provisional name for this dispatch only: **STALE-REF MEASUREMENT**. I do not propose canonical
vocabulary; § 12 routes it.

### 2.4 One producer instance is misassigned

**PRODUCER CLAIM:** the `regenerate_adjudications.py` finding is class B (undeclared scope) —
*"a mechanism whose guarantee reaches roughly a quarter of its inputs while its documentation
states that guarantee without qualification."*

**MIRROR FINDING:** the docstring is the *smaller* half. The tool's guarantee is not
under-declared so much as **never exercised**: no gate invokes `verify`, and the test that IS
wired runs entirely on fabricated pages (§ 4.1). That is a different repair — one line in
`run_release_regressions.py`, not a docstring edit — so the assignment matters.

---

## 3 · TOOL COVERAGE, RE-DERIVED FROM ZERO

I inherited none of 448 · 333 · 39 · 8.7 % · 74.3 % · ≈71–74 % · 43.2 %.

### 3.1 The artifact census — reproduces exactly at `main`, and not at every seat

`census.py`, walking `deepdive_manifests/*.json` at a named ref:

| Ref | manifests | declaring `source_artifacts` | artifacts declared | `kind=figure` | `.pdf` | pdf % | img % |
|---|---:|---:|---:|---:|---:|---:|---:|
| `main` = `788c357` | 64 | 60 | **448** | **333** | **39** | **8.71** | **74.33** |
| `lettore-b`, `lettore-c` | 64 | 60 | 448 | 333 | 39 | 8.71 | 74.33 |
| **`lettore` (Scientist A)** | **49** | **45** | **335** | **255** | **29** | **8.66** | **76.12** |

Every producer figure **CONFIRMED at `main`**, to the unit. `kind=figure` and image-extension
coincide exactly, 333 = 333, as claimed.

Two facts the package does not carry:

- **448 declarations = 447 distinct paths.** `PMID25331887_AbuOdeh2014_PMC.html` is declared by
  both `PMID25331887.json` and `PMID27308504.json`. The proportions move by <0.3 % and the
  conclusion does not; the denominator is nonetheless 447 objects, not 448.
- **The ratio survives the tree difference; the counts do not.** 8.66 % vs 8.71 %, 76.1 % vs
  74.3 %. Recorded because it is the good news inside M3-3: the pilot's *conclusion* is robust to
  the ref, and only its arithmetic is not.

### 3.2 The population the crop recipe actually reaches

`regenerate_adjudications.py` iterates `page_adjudications/*/adjudications.json` and keys on
`source_pdf` (`:201`) → `render(pdf, page, crop, dpi)` (`:174`). **The producers' construction
argument is CONFIRMED**: a standalone `.png` has no page, no crop in points and no dpi.

Measured reach:

```
page_adjudications/ : 3 directories — PMID 16061658, 17803050, 21212533
crop artifacts      : 27
needles             : 9
locators resolved   : 47   (10 + 29 + 8 per PMID)
```

`verify` in the **shared checkout** (the only tree holding the 55 PDFs):
`OK: 27 adjudication artifact(s) regenerate to their declared digest, and 47 locator(s) resolve to
a span inside the crop that shows them` — exit 0.

`verify` in **my own worktree**: `FAILED — 3 problem(s) across 0 artifact(s)`, all three
*"source PDF absent"*. **The tool fails closed and is right to.** But the consequence is that
this gate's verdict is a property of which directory you are standing in, and nothing records
that.

### 3.3 The figure/no-text gradient — independently re-implemented

I wrote my own clustering sweep (connected components of `get_image_info()` bboxes joined at gap
*g*, clusters ≥ 20,000 pt², "no text" = no type-0 text block intersecting), over all 55 PDFs.

| | producers | mirror |
|---|---:|---:|
| PDFs / opened / unreadable | 55 / 55 / 0 | **55 / 55 / 0** ✅ |
| PDFs carrying no figure | 9 | **9** ✅ |
| pages carrying ≥ 1 image | 289 | **289** ✅ |

| join gap | their figures | mine | their no-text | mine | their rate | **my rate** |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 237 | 238 | 175 | 170 | 73.8 % | **71.4 %** |
| 5 | 242 | 243 | 177 | 170 | 73.1 % | **70.0 %** |
| 10 | 229 | **229** | 168 | 160 | 73.4 % | **69.9 %** |
| 15 | 230 | **230** | 165 | 157 | 71.7 % | **68.3 %** |
| 18 | 228 | **228** | 160 | 154 | 70.2 % | **67.5 %** |
| 20 | 229 | **229** | 156 | 150 | 68.1 % | **65.5 %** |
| 200 | 225 | **225** | 120 | 116 | 53.3 % | **51.6 %** |
| 400 | 224 | **224** | 106 | 104 | 47.3 % | **46.4 %** |
| 800 | 234 | **234** | 101 | 100 | 43.2 % | **42.7 %** |
| 1600 | 234 | **234** | 101 | 100 | 43.2 % | **42.7 %** |

**CONFIRMED:** the figure counts reproduce to within 0–1 across the gradient, exact at 7 of 10
sampled gaps. The decay is monotone, saturates at gap 800, and the saturated value equals the
page-union — so *"the 43 % is the same instrument with the knob turned to 800"* is
**independently confirmed, in a hand that did not read their code.**

**REFINED:** my no-text numerator runs 4–8 lower at every gap, so my rates sit 1–3 points below
theirs. I did not resolve the criterion difference (their text primitive is not stated). The
published plateau *"≈71–74 %"* is at the top of the reproducible band; my hand gives **67.5–71.4 %**
over the same 0–18 pt window. **The direction is against the producers' own interest** — their
figure makes the coverage problem look slightly worse than mine does — which is worth recording
precisely because the flattering error is the one to watch for.

**Fourth-hand caveat, and it is the whole of M3-4:** my run used the same 55 PDFs in the same
gitignored directory as theirs. Four hands over one dataset is one measurement with four
implementations. It tests the *code*; it cannot test the *corpus*.

### 3.4 The cluster-area table reproduces only at an undeclared join gap

The handoff's tile evidence — the page trio that establishes the criterion defect:

| page | their largest cluster | mine at gap 0 | mine at gap 5 |
|---|---:|---:|---:|
| Cheng suppl. p6 | 226,187 | **226,187** ✅ | 226,187 |
| Cheng suppl. p17 | 119,727 | 18,644 ❌ | **119,727** ✅ |
| Cheng suppl. p19 | 35,392 | 10,304 ❌ | **35,392** ✅ |

⇒ **MIRROR FINDING M3-11.** All three reproduce **exactly at join gap = 5 pt**, and the table
declares no join gap. A reader re-deriving at the obvious default gets two of three wrong and
concludes the measurement does not reproduce. The numbers are right; the scope is undeclared —
class B, inside the evidence used to establish class B.

**CONFIRMED without qualification**, because it is the load-bearing half: Cheng supplementary
**page 21** reproduces to the decimal —

```
page width 595.3       get_text("dict") type-1 blocks: 0       get_image_info: 2
   1038 × 698   bbox x0 =  97.6  x1 = 730.3     ← right edge past the page
   1038 × 698   bbox x0 = −77.5  x1 = 572.0     ← left edge negative
page text: "Supplementary Figure 8 +/+  -/- H&E (postnatal day 20)"
```

Two images out of bounds in opposite directions, on a figure page of the paper under review, and
`blocks = 0` is indistinguishable from a page with no figure. **The instrument-defines-population
finding is CONFIRMED at its strongest point.**

### 3.5 The number the package does not carry, and it is the one a consumer needs

`deepdive_manifest.py:74` — `TEXT_SURFACES = {"body", "table", "supplement"}`. `figure` and
`abstract` are excluded from quote verification **by construction**. Partitioning all 1,002
locators across the 64 manifests:

| Bucket | locators | share |
|---|---:|---:|
| **Text-verified** by the manifest gate (schema v2, artifact declared, surface ∈ TEXT_SURFACES) | **631** | **63.0 %** |
| **`figure` surface — outside every text check** | **338** | **33.7 %** |
| Legacy schema, no artifact binding | 33 | 3.3 % |
| — of the 338, on a paper with a crop recipe | 58 | 5.8 % |
| — of the 338, with **no mechanical check of any kind available today** | **280** | **27.9 %** |

**Corpus-wide, 47 of 1,002 locators (4.7 %) are verified by the crop recipe; 631 (63.0 %) are
verified by exact text match; 338 (33.7 %) are verified by neither.**

⇒ **MIRROR FINDING M3-9.** The pilot's framing — *"for 333 of 448 declared artifacts the recipe
form does not apply"* — is true and cuts on the wrong axis for a consumer. It (a) **understates
what is covered**, because image *identity* is gated by SHA-256 and the manifest gate fails closed
on a corrupted figure digest (§ 4.2), and (b) **misses the sharper number**, which is about
locators, not artifacts, and is 33.7 % rather than 74.3 %.

On the pilot's own paper: **5 of 25 locators are `figure` surface**. Entries `[22]`, `[23]`,
`[24]` — Fig. 7d three-genotype, Fig. 7c densitometry, Fig. 2 — sit on
`40478_2020_883_Fig7_HTML.png` and `…Fig2_HTML.png`, present in all four seats at digest
`ced68a66…` matching the manifest. **The producers are right that the decisive evidence is on a
raster with no page.**

**One over-generalisation, corrected:** entries `[18]` and `[21]` are also `figure` surface and
point at `PMID32000863_Cheng2020_supplementary.pdf` — **a PDF, with pages, recipe-eligible
today**. So *"every one came off the PNG"* holds for the three main-figure locators and not for
all five. Two of the paper's five figure locators are reachable by the existing mechanism and no
recipe was written for them. `M3-13`, non-blocking, and it makes the repair cheaper rather than
harder.

**And no PDF of Cheng's main text exists anywhere under the repository root — CONFIRMED**
by name sweep across every worktree. The supplement and the XML are present; the main text is not.

### 3.6 The evidence population is larger than the declared population

| | count |
|---|---:|
| Files on disk under `files/fulltext/` (shared checkout) | **649** |
| Distinct artifact paths declared by any manifest | 447 |
| Declared **and** on disk | 427 |
| Declared but absent — **all 20 are rule-5e crops, correctly delegated** | 20 |
| **On disk, declared by no manifest** | **328** |
| — of which image files | **192** |

The 20 absences are not a defect: rule 5e publishes the recipe and never the image, the gate says
so in its own verdict string, and `PMID17803050`'s 7 crops *are* on disk because someone ran
`write`. **My first count would have been a false finding and the delegation clause is what
prevented it** — recorded because it is the one place a Mirror wrong-reason error was caught by the
tool's own scope declaration, which is the behaviour § 12 asks other tools to copy.

The 328 are the general form of the pilot's instance 5 (*"the publisher's figure package sat
unopened"*). It is not one zip. **The declared-artifact population is 69 % of the evidence
actually on disk**, and nothing enumerates the difference.

---

## 4 · WRONG-REASON TESTING — a mutation battery with both controls

The dispatch asks whether each green result could have passed for the wrong reason. I answered by
mutation rather than by argument. All mutations ran on scratch copies through the tools' own
`--workspace` flag; the repository was never modified.

### 4.1 The adjudication regeneration gate — **green for the wrong reason, CONFIRMED**

| Question | Measured |
|---|---|
| Is `regenerate_adjudications.py` wired into a gate? | **Its *test* is** — `run_release_regressions.py` line 42 |
| Does that test open a real recipe or a real PDF? | **No.** 12 tests, all on a `FakePage` standing in for `fitz.Page`. `Ran 12 tests … OK` in 0.040 s |
| Does any gate invoke `verify`? | **No.** The string `regenerate_adjudications.py verify` occurs in the module docstring, two READMEs and four prose records — **and in zero executable gates** |
| Real recipes in the gate population | **0** |

⇒ **MIRROR FINDING M3-8.** The producers' *"tested, wired into the release battery"* is **true of
the needle predicate and false of the recipes**. The battery would stay green if all three
`adjudications.json` files were deleted, if their digests drifted, or if the three PDFs vanished.
The predicate is genuinely well tested — that part is not in dispute and belongs in § 11.

This is the same shape as the producers' class B, one layer up: **a gate whose green covers a
population of zero real objects, reported as coverage of the mechanism.**

### 4.2 The locator-resolution gate — the mutation battery

Harness: `deepdive_manifest.py --workspace <scratch> --artifact-workspace <shared> --pmid 32000863
--verify-artifacts`. Control 0 (unmutated copy) → `PASS`, and restored → `PASS`.

| # | Mutation | Verdict | Reads |
|---|---|---|---|
| 1 | Fabricated snippet on a **`body`** locator | **FAIL** ✅ | `entries[0].snippet: not verified in the declared body artifact` |
| 2 | Corrupted `sha256` of a **`figure`** artifact | **FAIL** ✅ | `source_artifacts[3].sha256: fingerprint mismatch` |
| 3 | Fabricated snippet on **`entries[22]`** — the Fig. 7d three-genotype locator, the pilot's headline finding | **PASS** ❌ | silent |
| 4 | Fabricated **anchor** on the same locator — *"Figure 99z, image inspected at 1×1 pixels — a panel that does not exist"* | **PASS** ❌ | silent |

**Three conclusions, and the third is the one that matters most.**

- **Positive controls fire.** The gate is real: text quotes and artifact digests are both defended.
- **Image identity is covered.** Mutation 2 refutes any reading of the pilot in which figure
  evidence is wholly ungated.
- 🔴 **Mutation 4 is a new finding.** A *wrong figure pointer on a figure locator passes the
  manifest gate silently.* v2 established the Fig. 7b/7d defect as a **propagation** failure into
  `claim_registry_current.md:300`. Mutation 4 shows **the origin surface has no check either** —
  the same defect written directly into a manifest would be accepted. So the class is not confined
  to the propagation step, and a repair aimed only at propagation leaves the door open upstream.

**Scope declaration, in the gate's favour:** the verdict string says *"exact **text** locators
verified where declared"*. The word `text` is doing real scope work and the tool is not lying.
What it never prints is **how many locators it skipped** — 338 of 1,002 corpus-wide, 5 of 25 on
this paper. A `PASS` that named its own population would have made M3-9 visible on day one.

### 4.3 Agreement between independent actors — **wrong reason, CONFIRMED**

The package's own justification: *"What the three measurements agree on … is what makes this a
measurement and not a consensus: the population (55 / 55 / 0), the 9 figure-less PDFs, and the
no-CONTAINED numerator at 20,000 px² — 187 in all three."*

Measured, per worktree, `files/fulltext/*.pdf`:

| Tree | PDFs | all files |
|---|---:|---:|
| **shared checkout** | **55** | 174 |
| `lettore` (A) | 9 | 37 |
| `lettore-b` (B) | 3 | 16 |
| `lettore-c` (C) | 1 | 3 |
| `evidence-index` (Plan) | 4 | 13 |
| `mirror`, `orchestrator` | *no such directory* | — |

`files/` is line 7 of `.gitignore`. **No Scientist seat could run a 55-PDF sweep in its own
worktree.** All three sweeps — and mine — necessarily ran against the one shared directory.

⇒ **MIRROR FINDING M3-4.** Agreement on 55 / 55 / 0 and on the 9 figure-less PDFs is **entailed by
the shared surface** and carries no independent information whatever. It is not corroboration; it
is four reads of one `ls`. The informative event was the **disagreement** — 237 vs 242 — which
they resolved correctly by running the command.

This is exactly the producers' own class E/B — *"the agreement was what made it look safe"* — and
they applied it to the *instrument* while missing that it also applies to the *data*. **The
sentence "what makes this a measurement and not a consensus" is, for the population half,
precisely backwards.**

### 4.4 LINT · receipts · growth anchors · clean worktree · unchanged current files

All run by me, in my own tree at `c7e8d6e`:

```
legend_lint.py .            VERDICT: PASS   (1 [INFO], CLAIM 010 background-only wikilink)
fulltext_receipts.py verify OK: 128 chained receipt(s), tail anchored
growth_anchors.py check     PASS — claims 39 · papers 70 · corpus 356 · literature 390
```

**Current-file immutability — and the check that would have got it wrong.** Comparing each seat's
current files against `main` reports **four differences on `lettore`**, which reads as a mutation.
It is not. Comparing against each branch's **own merge-base**:

| Branch | base | current files modified |
|---|---|---:|
| `lettore` | `9b0cf47` | **0** |
| `lettore-b` | `788c357` | **0** |
| `lettore-c` | `788c357` | **0** |
| `legend-operating-convention-v1` | `788c357` | **0** |

Positive control: `git diff --name-only 419b680~1 419b680` on `claim_registry_current.md`
returns **1**, so the command is capable of reporting non-zero.

⇒ **CONFIRMED: no seat mutated canonical state.** And a **latent wrong-reason hazard, recorded**:
an auditor running the naive against-`main` form would falsely accuse Scientist A. The correct
form is against the branch's own base — which only matters because of M3-1.

**Outside the review directories, exactly two files were written**, both by A, both into
`framework/protocols/`: `scientist_evidence_standard.md` (392 lines) and
`scientist_operating_practice_v1.md` (705 lines). Both open with **"Non-canonical, PROPOSED"** and
**"Non-canonical, DESCRIPTIVE"** respectively, both name their author and branch, and neither is on
`main`. **Authority correctly declared.** The residue is one line: `framework/protocols/` is the
normative directory per the router, so the *path* asserts a status the *frontmatter* denies.
Non-blocking.

### 4.5 🔴 The privacy gate — a green over a population the rule cannot see

This is the finding with the largest consequence and the smallest repair, and it is **not the
pilot's doing.**

Seven committed pilot artifacts, across all four seats, carry the Operator's given name inside an
absolute filesystem path — ten occurrences:

| Seat | files | occurrences |
|---|---:|---:|
| A | 2 | 3 |
| B | 3 | 5 |
| C | 1 | 1 |
| Orchestrator | 1 | 1 |

Every occurrence is of the form `` `/Users/<name>/Desktop/legend-public/...` `` in a
worktree-identification table. **This is exactly the disciplined scope declaration this review
asks every actor to write** — which is why it is a gate problem and not an actor problem.

**Does the gate see it? Mutation battery, two fixtures, one scan:**

```
upper.md :  "Nobody but <Name> can close these."                    → BLOCK  PRIVATE_NAME  ✅
lower.md :  "| Worktree | `/Users/<name>/Desktop/legend-public/…` |" → no finding          ❌
FINDINGS 1 · BLOCKING 1
```

**The `PRIVATE_NAME` rule fires on the capitalised form and is blind to the lowercase path form.**

**Denominator, and it is the part that matters — this predates the pilot:**

| Ref | tracked files carrying the path form | occurrences |
|---|---:|---:|
| **`main`** | **16** | **26** |
| `lettore-b` | 19 | 31 |
| `plan-orchsurf-r4-transcription` | 19 | 30 |
| `lettore-c` | 17 | 27 |
| `legend-operating-convention-v1` | 16 | 26 |
| `orchestrator` | 13 | 24 |
| `lettore` | 4 | 9 |

`main`'s 16 files include four surfaces the public edition **ships**:
`discovery_ledger_current.md`, `full_text_queue_current.md`, `fulltext_read_receipts.jsonl`,
`framework/state/sync_epochs.jsonl` — plus `launch/KERNEL_SPEC.md` (4 occurrences).

```
public_release_gate.py --root . --mode release --skip-clean-clone
VERDICT: PASS      BLOCKS: 0
```

⇒ **MIRROR FINDING M3-10.** The publication gate returns **PASS with zero blocks** on a tree
carrying 26 occurrences of the Operator's given name in shipped files. This is a **standing
blind spot on `main`**, not a pilot regression: the pilot neither introduced the class nor
detected it, and its artifacts extend it by roughly 5 occurrences on `lettore-b`, 4 on Plan and 1
on `lettore-c`. The Orchestrator's own commit `5debf86` (*"seven identifiers leave with them"*)
shows the seat already handles this class **when it can see it** — which is the argument that the
repair belongs in the rule, not in a reviewer.

**Requires Human Gate.** It is a privacy property of a public repository; no producer seat is
authorised to decide it, and I am not either.

---

## 5 · TRANSPORT VERSUS READING — the chain, reconstructed

The dispatch requires each confirmed propagated defect to be traced to the exact transition where
degradation occurred, because the repair layers differ. Two new ones, both inside the pilot's own
record rather than in canonical state.

### 5.1 M3-5 · The convergence map still reports an outcome all three actors abandoned

```
SOURCE EVIDENCE      Wang 2012 measures no seizure endpoint; Cheng 2020 runs no binding assay
  → interpretation   B(I): INDIRECT_UNKNOWN_INTERMEDIATES → B(II): ASSOCIATED, on A's gloss
  → SUMMARY ARTIFACT PHASE2_CROSS_REVIEW_SCIB_v1.md:431
                     | Edge type `016 ↔ 035` | `ASSOCIATED` | … | **resolved in A's favour** |
  → later positions  A (D-2): withdraws ASSOCIATED, adopts C's NOT_DIRECT
                     C (C1): NOT_DIRECT, no further token
                     B (round response §3): **NOT_DIRECT. No further token assigned.**
  → amendment        ✗  NONE. `convergence map` occurs 0 times in all four later B artifacts.
  → graph            ✓  `pathograph_export.jsonl` still carries relation_type: UNTYPED
```

**The transition is at the summary artifact, and the failure is that nothing revisits it.** All
three actors reached `NOT_DIRECT`; the one table a downstream consumer would read first still says
`ASSOCIATED` — the token B then established is *forbidden* by the only published rule about it
(`pathograph.py:153–156`, repeated at `:1117`).

**Blast radius: bounded, and I checked rather than assumed.** The graph carries `UNTYPED` with
`relation_type_basis: NO_DECLARED_RELATION_ANNOTATION`. No canonical or generated surface inherited
the stale value. This is a prose-layer defect with a live wrong answer on it.

**CLASS: transport, not reading.** Every reading was correct at the time. Repair layer:
`HANDOFF/PLUMBING` — a superseded summary needs a supersession stamp, not a better reviewer.

### 5.2 M3-6 · A refuted falsifier design stands in the pilot's closing scientific artifact

```
18:05:57  lettore-b 44d96e5  "I rejected the milligram argument and left it standing in the
                              two falsifiers built on it"
          → B §5b: "You cannot match cumulative dose across a T-type Ca²⁺ channel blocker and a
            monovalent cation … As written, F-5 is not performable."
            Repair supplied in the same paragraph: match on ED₅₀, free-brain concentration or
            target engagement. "Milligram parity is not a control; it is the appearance of one."

18:21:55  lettore   f5fdfa3  FINAL_SCIENTIFIC_SYNTHESIS_PMID32000863_v1.md
          → F-4: "a structurally unrelated GSK-3β inhibitor at matched cumulative exposure and
            schedule"
          → F-5: "ETS and LiCl at matched cumulative dose and schedule, in one experiment,
            one control arm."
```

**16 minutes, and the correction is not in the closing artifact.** The document contains zero
occurrences of `equi-effective`, `ED₅₀` or `not performable` in the repair sense.

**Stated as a property of the blob, not of anyone's knowledge.** Commit time is not observation
time; A may have drafted F-4/F-5 before 18:05. That is precisely why this is transport and not
reasoning: the artifact as it stands carries a design a peer refuted, and no mechanism forces a
re-read before the closing document lands.

**Boundary, so it is not over-read.** The *observation* O-11/A-9 — *"ethosuximide one dose of
150 mg/kg; LiCl three doses of 60 mg/kg = 180 mg/kg cumulative"* — is factually correct and B never
disputed it. What is refuted is **milligram-matching as the repair**, and only F-4/F-5 carry that.

**CLASS: transport.** Repair layer: `HANDOFF/PLUMBING` — the closing synthesis needs a
merge-base against every peer artifact committed since its draft opened.

### 5.3 The producers' five transport instances — CONFIRMED as transport, not reading

I re-tested the boundary the dispatch warns about (do not call a reading failure transport merely
because an earlier artifact exists). All five hold: in each case the correct object is *present and
locatable* at an earlier ref, and the defect is that nothing carried it. Instance 4 — the
hand-rolled crop form beside a working `regenerate_adjudications.py` — is the strongest, and § 4.1
now adds that the tool it duplicated is itself unexercised by any gate, which makes the
"rediscovery" more forgivable and the repair more urgent.

---

## 6 · THE INTERACTION, MEASURED

### 6.1 The timeline — 65 commits, four seats, 4 h 02 m

| Phase | Window | Commits |
|---|---|---:|
| I — first passes | 15:24 → 15:43 | 8 |
| II — cross-review + round response | 16:01 → 17:49 | 12 |
| III — reconciliation | 17:51 | 1 |
| IV — hostile reviews (B primary, C recused set) | 18:00 → 18:12 | 4 |
| V — final synthesis | 18:21 | 1 |
| §11 — operating practice, **declared close** | 18:29 → 18:32 | 4 |
| **post-closure — the figure-population round** | **18:34 → 19:26** | **24** |

### 6.2 🔴 The package's headline process claim is REFUTED by its own artifacts

**PRODUCER CLAIM:** *"Eight rounds between the two Scientists. Until this one, every exchange
added to the other's conclusion; this is the first outright contradiction … a cross-review protocol
that produces seven rounds of mutual extension before its first collision is worth Mirror's
attention."*

**MEASURED, from the Phase II documents themselves** — every one of which carries a section headed
`C · DISAGREE — WITH PRIMARY-EVIDENCE REASON`:

| Seat | confirmed by own check | accepted from peer | **disagree** | revised own position | unresolved | falsifiers |
|---|---:|---:|---:|---:|---:|---:|
| A | 7 | 5 | **5** | 4 | 5 | 4 |
| C | 6 | 5 | **2** | 7 | 6 | 4 |
| B | §3.1–3.6 on A, §4.1–4.6 on C, including **§3.4 "Strongest disagreement — and A wins it"** and **§4.3 "Strongest disagreement — and I win this one"** | | **2 named** | 4 positions moved, 3 against B | 4 | — |

**Contradiction was present from Phase II and was structurally required by the form.** The
post-closure round was not the first collision; it was the first collision **about a shared
instrument rather than about a proposition** — which is a different and more interesting claim,
and the one worth carrying.

⇒ **MIRROR FINDING M3-7a.** The "seven additive rounds" framing is an artifact of counting
*rounds* rather than *items*. It should not survive into any design argument, because it supports
"the protocol suppresses contradiction" when the record shows the opposite.

### 6.3 The eight competing explanations, adjudicated

| # | Explanation | Verdict | Evidence |
|---|---|---|---|
| 1 | Genuine independence created epistemic value | **PARTLY SUPPORTED** | B lists 11 items *"I could not have reached alone"*; C lists 5; A lists 3. But independence was never available — the repository already held the conclusion (disclosed, and I confirm `locator_contract_live_test.md` is tracked since 2026-08-04) |
| 2 | **Actors differed in tools or surfaces rather than reasoning** | **STRONGLY SUPPORTED — and undisclosed** | 217 files differ between A's base and B/C's; 49 vs 64 manifests; 813 vs 1,002 locators; `files/` holds 9 / 3 / 1 PDFs per seat. **M3-1.** |
| 3 | Review prompts biased actors toward additive extension | **UNTESTABLE FROM MY SURFACE** | the two dispatch texts are not durable artifacts. Recorded as open, not dismissed |
| 4 | Shared frame inheritance delayed contradiction | **SUPPORTED, and it is the disclosed one** | contamination item 1; and B's own account of changing position *"on a gloss, and I did not check whether the gloss had a source"* |
| 5 | Task structure rewarded finding additional material | **WEAKLY SUPPORTED** | the six-section form (A/B/C/D/E/F) allocates one section to disagreement and five to other acts; but all three used the disagree section |
| 6 | Tool limitations created artificial complementarity | **SUPPORTED** | C's *"the Pathograph is not present"* was a worktree-scope artifact, withdrawn; the general case (217 files) was never drawn |
| 7 | **A third deterministic method resolved the hardest disagreement** | **STRONGLY SUPPORTED** | 237 vs 242 was settled by running `get_image_info` against `get_text("dict")`, not by argument; the 43 % bracket was dissolved by a third instrument (clustering), not by a third opinion. **I reproduce both.** |
| 8 | Longer review increased discovery because more surfaces were eventually inspected | **SUPPORTED** | 24 of 65 commits — and the four largest findings — came **after** the declared close |

**⇒ The two strongest explanations are 2 and 7, and neither is "more reviewers."** What produced
the epistemic gain was (a) seats standing on different surfaces, which is an *accident* here and
should become a *declaration*, and (b) a deterministic instrument settling what argument could not.

### 6.4 Three arithmetic and staleness defects inside the record

- **M3-7 · The convergence map under-counts its own table.** Mechanical tally of the status
  column: **10 converged · 5 single-actor · 4 resolved · 1 race = 20 rows.** The summary sentence
  reads *"Nine converged propositions, four single-actor findings, four resolved disagreements,
  one race"* = **18**. Under-counts converged by 1 and single-actor by 1.
- **M3-12 · The Mirror handoff is stale against the run it describes.** It declares `lettore` tip
  `c44eb45`, `lettore-c` tip `cf77cef`, Orchestrator tip `3c9969a`. Actual tips: `605fc5d`,
  `5b1d6c2`, `a58af46` — **8, 7 and 9 further commits**, carrying the entire figure-population
  round. Only `lettore-b`'s `9a09590` is current. A consumer resolving the declared blob digests
  gets a mid-run snapshot.
- **A's tree carried an 11-day-old uncommitted edit through the whole pilot.** `PMID42422765.json`
  receipt pointer `…-04` → `…-05`, mtime 2026-08-14 18:14, still uncommitted. **Not a pilot act** —
  it predates the run — and the structural validator passes it. It corroborates M3-1
  independently of the git evidence: no gate has looked at that tree since 2026-08-14.

### 6.5 Two propositions were reviewed by nobody — CONFIRMED and correctly declared

R-3 and R-4: B originated them, C recused under a symmetry rule it volunteered, A was the
synthesiser. Marked `UN-ATTACKED` in A's § J-5 and in C's § 6, **not folded into a reviewed
layer**. C states it against itself: *"a real hole and it is the price of the symmetry rule."*

**This is the package at its best and I add nothing to it.** The hole is named, scoped, and left
open rather than papered over.

---

## 7 · THE STOPPING CONDITION

### 7.1 The system already has a stopping rule and the pilot did not cite it

`governance/annex_c_review_protocol.md` § C.3, status **FROZEN**, normative:

> *"max 2 round → adjudication; cap una review attiva per Scientist"*

**The pilot ran eight rounds.** Sweeping all four pilot refs for any citation of Annex C, C.3 or a
round cap returns **zero pilot artifacts** (the hits on `lettore-b` / `lettore-c` /
`legend-operating-convention-v1` are pre-existing files — `actor_identity_proposal.md`,
`SLR-plan-0008.md`, `AUTHOR-RESPONSE-*` — none written in this run). Positive control: `Phase II`
resolves on all four refs.

⇒ **MIRROR FINDING M3-14.** The producers report *"we have no valid stopping rule"* and ask whether
one should be built. **The governance has one, it is frozen, and the pilot exceeded it fourfold
without registering a deviation rationale.** This inverts the design question: the gap is not a
missing rule, it is that **no actor's fingerprint set surfaced the rule they were bound by.**

I take no position on whether a 2-round cap is right for a three-seat scientific cross-review —
that is Plan's and the Operator's. I record only that the pilot's stopping problem was diagnosed
as an absence when it is a **non-observation of an existing constraint**, and those have opposite
repairs.

### 7.2 How the run actually stopped — classified

| Candidate | Supported? |
|---|---|
| Exhaustion of known tests | ✗ — 24 post-closure commits after the declared close |
| **Exhaustion of known surfaces** | ✓ — and this is the producers' own honest formulation |
| Saturation of findings | ✗ — the last four commits each carry a distinct new finding |
| Reviewer fatigue | not measurable from my surface |
| **Iteration budget exhaustion** | **most consistent with the trace** — the final three commits land on three different branches at 19:23, 19:26 and 19:26, within 3 minutes. That is a coordinated stop, not a convergence |
| True closure | ✗ — refuted by the producers themselves |

**The producers' replacement of *"nothing left to measure"* with *"I have run out of surfaces I
currently believe are unexamined"* is correct and should be kept verbatim.** Their own
observation — *"joint settlement is where the next thing lives"* — is the most useful stopping
heuristic in the package, and it is an anti-stopping rule: it says a declared settlement is a
signal to look once more, which is the opposite of a threshold.

**I decline to propose a numerical stopping threshold.** The evidence supports none, and § 7.1
shows the last thing this system needs is a second uncited one.

---

## 8 · THE "NO NEW REVIEWER ACTOR" QUESTION

**PRODUCER RECOMMENDATION:** do not answer this pilot with a new reviewing actor. B's argument:
*"an actor that reads prose is exactly what failed here, repeatedly, in all four of us."*

**MIRROR FINDING: the recommendation is correct, and I reach it on independent evidence.**

The dispatch sets the bar: a new actor is justified only if a recurring unmet function requires
distinct independence, authority, memory, tooling or longitudinal responsibility that no existing
seat can supply. Testing my own 14 findings against that bar:

| Finding | Would a new *reviewing actor* have found it? | What would have |
|---|---|---|
| M3-1 · divergent trees | possibly, by reading | `git merge-base` printed in every observation-scope block |
| M3-2 · stale denominators | possibly | a ref field beside the population table |
| M3-3 · census population | possibly | same |
| M3-4 · agreement over one directory | **unlikely — it required standing outside all four seats** | Mirror, which exists |
| M3-5 · stale convergence map | yes, by reading | a supersession stamp |
| M3-6 · refuted falsifier | yes, by reading | a merge-base check before a closing artifact |
| M3-7 · miscounted table | **no — it needed a tally, not a reader** | `awk` |
| M3-8 · unexercised gate | **no** | one line in `run_release_regressions.py` |
| M3-9 · locator partition | **no** | the gate printing its own population |
| M3-10 · privacy blind spot | **no** | a case-insensitive rule + a fixture |
| M3-11 · undeclared join gap | **no** | the parameter in the table caption |
| M3-14 · uncited round cap | **no** | the governance fingerprint surfacing Annex C |

**Eight of fourteen are invisible to any prose reader and closed by a command.** Four more are
readable but need *durable-artifact diffing*, which is Mirror's existing analysis surface. **Zero
require a seat that does not exist.**

**And the seat that found all fourteen is Mirror.** The pilot's question *"is B's argument against
the seat Mirror occupies, made by someone with a stake?"* answers itself in the negative: B's
argument is that **prose-reading actors are the wrong instrument for mechanical defects** — which
is Mirror's own § "Analysis surface" doctrine (*"Mirror's primary analysis runs on the consolidated
event ledger … not by reading fifty chats"*). B is arguing *for* the way Mirror is specified, not
against Mirror.

**DO NOT CREATE A NEW ACTOR.** The unmet function is not a seat; it is that **six existing gates
do not print the population they cover.**

---

## 9 · OPERATIONAL ARCHAEOLOGY — which objects real Scientist work already emits

29 documents, 746,625 bytes, pattern census. This is not a schema proposal; it is a frequency
table of what is *already there*, which is what the dispatch asks for.

| Object | docs / 29 | A | B | C | total | On the dispatch's § 12 list? |
|---|---:|---:|---:|---:|---:|:--:|
| claim / proposition id | **27** | 335 | 278 | 91 | 704 | ✓ |
| hypothesis / candidate relation | **27** | 118 | 80 | 35 | 233 | ✓ |
| evidence locator | **25** | 136 | 64 | 27 | 227 | ✓ |
| contradiction / disagreement | **22** | 48 | 37 | 24 | 109 | ✓ |
| causal limit / boundary | **18** | 16 | 29 | 8 | 53 | ✓ |
| **epistemic tier / premise tag** | **16** | 43 | 13 | 10 | 66 | ✗ |
| **observation scope / denominator** | **16** | 23 | 13 | 9 | 45 | ✗ |
| **retraction / position revision** | **15** | 26 | 41 | 14 | 81 | ✗ |
| unresolved question | 14 | 9 | 11 | 5 | 25 | ✓ |
| reproduction command | 13 | 10 | 20 | 5 | 35 | ✗ |
| graph contribution | 12 | 63 | 4 | 11 | 78 | ✓ |
| falsifier / decisive test | 10 | 7 | 11 | 4 | 22 | ✓ |

**Three objects appear in more than half the corpus and are absent from the proposed list:**

1. **Position revision with attribution.** 15/29 documents, 81 occurrences. Every one names *who*
   caused the change. This is the pilot's single most characteristic act and it has no slot. M3-5
   and M3-6 are both failures to *carry* one.
2. **Observation scope / denominator.** 16/29. Its absence as a first-class field is the direct
   cause of M3-1, M3-2, M3-3 and M3-11.
3. **Epistemic tier on the relation, not only on the node.** 16/29 documents tag propositions
   `DATO` / `INFERENZA` / `PREMISE_TAG`; the graph's `claim_edge` carries no tier — measured by A
   and confirmed in v2 § E.

**Two objects on the list are thinner in practice than expected:** `falsifier` (10/29) and
`graph contribution` (12/29, and 63 of 78 from a single seat). Neither is absent; both are
concentrated rather than universal, which is a reason to make them optional rather than required.

**This is archaeology, not architecture.** I propose no schema and design no graph.

---

## 10 · FAILURE MAP

`FACT` = measured here · `INF` = inference from measured facts · `PR` = producer recommendation ·
`MF` = Mirror finding. Repair layers are the dispatch's local analytical categories.

| ID | Observed failure | Exact example | Measured scope | Existing canonical rule | Distinct class? | Repair layer | Evidence | Remaining uncertainty | Plan? | Human Gate? |
|---|---|---|---|---|---|---|---|---|:--:|:--:|
| **M3-1** `FACT` `MF` | Three seats read materially different trees; undisclosed | `lettore` base `9b0cf47` (08-14) vs `788c357` (08-22) | 217 files · 49 vs 64 manifests · 813 vs 1002 locators · 53 vs 70 PAPER | none | **new — STALE-REF MEASUREMENT** | SCIENTIST CONTRACT | **CONFIRMED**, git | none on the fact; the per-finding confound is unquantified | ✅ | — |
| **M3-2** `FACT` `MF` | Proposed output contract publishes 3 stale populations, names no ref | `scientist_evidence_standard.md` § 0 | 49/813/53 vs 64/1002/70 | its own § 0 rule | instance of M3-1 | SCIENTIST CONTRACT | **CONFIRMED** | none | ✅ | — |
| **M3-3** `FACT` `MF` | 448-artifact denominator is one of three defensible populations; the gate's is 3 recipes | § 2.2 table | 448 vs 55 vs 3/27/47 vs 1002 | none | instance of D | SCIENTIST CONTRACT | **CONFIRMED**, re-derived at 5 refs | which population the *contract* should name | ✅ | — |
| **M3-4** `FACT` `MF` | 3-hand agreement on the PDF population is agreement over one gitignored directory | 55 / 9 / 3 / 1 per seat | all 6 trees | none | instance of B/E | HANDOFF/PLUMBING | **CONFIRMED**, `ls` + `.gitignore:7` | none | ✅ | — |
| **M3-5** `FACT` `MF` | Convergence map still reports an abandoned outcome | `PHASE2_CROSS_REVIEW_SCIB_v1.md:431` | 4 later B artifacts, 0 amendments; graph `UNTYPED` | C.2 (`AUTHOR_RESPONSE` mandatory) | instance of A | HANDOFF/PLUMBING | **CONFIRMED** | none | ✅ | — |
| **M3-6** `FACT` `MF` | Refuted falsifier design stands in the closing artifact | final synthesis F-4 / F-5 vs `44d96e5` | 16 min apart; 0 repair strings | none | instance of A | HANDOFF/PLUMBING | **CONFIRMED** (blob property) | whether A had read `44d96e5` — deliberately not inferred | ✅ | — |
| **M3-7** `FACT` `MF` | Summary sentence under-counts its own table | 9/4/4/1 = 18 vs tallied 10/5/4/1 = 20 | 20 rows | none | minor | TEST ONLY | **CONFIRMED**, `awk` | none | — | — |
| **M3-7a** `FACT` `MF` | "Seven additive rounds before the first collision" is refuted by the Phase II documents | A: 5 disagree · C: 2 · B: 2 named | 3 Phase II docs | none | **corrects a producer claim** | NO CHANGE (record only) | **CONFIRMED** | none | ✅ | — |
| **M3-8** `FACT` `MF` | The crop gate's release test covers **0** real recipes; no gate invokes `verify` | `test_regenerate_adjudications.py`, 12 tests on `FakePage` | 3 recipes · 27 crops · 47 locators, all outside the battery | rule 5e | instance of B | **TOOL/SCRIPT** | **CONFIRMED**, executed | none | ✅ | — |
| **M3-9** `FACT` `MF` | 338/1002 locators (33.7 %) outside every text check; fabricated figure snippet **and** anchor both PASS | mutations 3 & 4, `entries[22]` | corpus-wide, 64 manifests | `TEXT_SURFACES` at `:74` | instance of B | **TOOL/SCRIPT** | **CONFIRMED**, mutation battery with both controls | how many of the 338 are load-bearing | ✅ | — |
| **M3-10** `FACT` `MF` | Privacy gate blind to the lowercase path form; release gate PASS on 26 occurrences in shipped files | fixture pair; `--mode release` → PASS, BLOCKS 0 | `main`: 16 files / 26 occurrences | public-edition de-identification | instance of B | **TOOL/SCRIPT** + **GOVERNANCE** | **CONFIRMED**, mutation-controlled | whether any occurrence is intended | ✅ | ✅ **YES** |
| **M3-11** `FACT` `MF` | Cluster-area table reproduces only at an undeclared join gap = 5 pt | p6 ✅ / p17 ❌ / p19 ❌ at gap 0 | 3 pages | none | instance of B | TEST ONLY | **CONFIRMED** | none | — | — |
| **M3-12** `FACT` `MF` | The Mirror handoff is stale against the run it describes | tips `c44eb45`/`cf77cef`/`3c9969a` vs `605fc5d`/`5b1d6c2`/`a58af46` | 8 + 7 + 9 commits | none | instance of A | HANDOFF/PLUMBING | **CONFIRMED** | none | ✅ | — |
| **M3-13** `FACT` `MF` | "Every decisive locator came off a PNG" over-generalises | `entries[18]`, `[21]` → supplementary **PDF** | 5 figure locators on PMID 32000863 | none | narrows a producer claim | NO CHANGE (record only) | **CONFIRMED** | none | — | — |
| **M3-14** `FACT` `MF` | 8 rounds against a frozen `max 2 round` cap, cited nowhere | Annex C.3 | 0 citations across 4 pilot refs, positive control passed | **Annex C.3, FROZEN** | **not a missing rule — a non-observed one** | **ORCHESTRATOR CONTRACT** | **CONFIRMED** | whether the cap suits a 3-seat scientific review | ✅ | ✅ **YES** |
| **M3-15** `FACT` | Plan's 12 records + 3 commit candidates still untracked | `evidence-index`, 14 dirty entries | 1 tree | v2 repair #1 | carried from v2 | HANDOFF/PLUMBING | **CONFIRMED** | none | ✅ | — |

**Producer claims I tested and did not break:** the four-class taxonomy (§ 2) · the 448/333/39
census at `main` (§ 3.1) · the construction argument for standalone images (§ 3.2) · the gradient
and its plateau (§ 3.3) · page 21's out-of-bounds bboxes (§ 3.4) · no canonical mutation (§ 4.4) ·
the five transport instances (§ 5.3) · the two `UN-ATTACKED` propositions (§ 6.5) · the
"no new actor" recommendation (§ 8).

---

## 11 · DO NOT REPAIR — no evidence for change

**Mandatory section.** These survived hostile review or are adequate as they stand. Changing them
would be architecture tourism.

1. **The four-class taxonomy.** Keep all four. Merge only E into B (§ 2.1). Do not add classes
   beyond the one § 2.3 names, and do not add that one without Plan's adjudication.
2. **`regenerate_adjudications.py` itself.** The needle discipline — unique on its page, a fragment
   of the snippet it names, `crop_contains_span` re-checked after rounding — is correct, well
   tested at the predicate level, and its 12 tests pass under mutation for what they cover. **The
   defect is that nothing points it at real recipes.** Do not rewrite the tool.
3. **Rule 5e and the recipe-not-image policy.** The 20 "missing" artifacts are correct behaviour,
   the verdict string declares the delegation, and that declaration caught a would-be Mirror false
   finding (§ 3.6). This is the model the other gates should copy.
4. **The manifest gate's text verification.** 631 locators matched character-for-character across
   64 manifests, all PASS, and both positive controls fire. This is a large, real, working gate.
   Its scope statement (*"exact **text** locators"*) is accurate. Add the population count; change
   nothing else.
5. **Fail-closed behaviour when the PDF is absent.** `verify` failing in my worktree is correct.
   Do not add a skip-if-missing path.
6. **The `UN-ATTACKED` marking of R-3 and R-4.** Correctly refused, correctly named, correctly not
   folded into a reviewed layer. Do not route them to the synthesiser.
7. **Actor boundaries.** Scientist / Orchestrator / Plan / Mirror as they stand. **No new actor**
   (§ 8). No expansion of Mirror's perimeter. Mirror still holds no command and produces no
   primary evidence.
8. **The self-attribution and self-defect-filing practice.** Both Scientists filed defects against
   their own headline findings; one abandoned a correction made on the back of a real finding.
   This is the highest-value behaviour in the record and it is unlegislated. **Do not turn it into
   a rule** — a mandated confession section becomes a form to fill in. Record it as an
   `ACTIVE_LESSON` candidate and leave the incentive alone.
9. **A's two `framework/protocols/` documents.** Correctly self-declared non-canonical, correctly
   attributed, not on `main`. One line about path-versus-status is owed; the documents are not.
10. **The commit candidates `POINTER-01`, `DRIFT-01`, `GRAPH-MATERIALIZATION-01`.** Endorsed in
    v2 § 12 and unchanged. Do not re-review them here.
11. **The stopping *formulation*.** *"I have run out of surfaces I currently believe are
    unexamined"* and *"joint settlement is where the next thing lives"* are better than any
    threshold. Keep verbatim; add no number (§ 7.2).
12. **The graph's `UNTYPED` edge.** It is right, it is right for the right reason, and M3-5 did
    not reach it. Do not type it.

---

## 12 · MINIMUM NEXT ACTIONS

Ordered by `KEEP → TEST → TOOL PATCH → SCOPED CONTRACT PATCH`. **None is written here.** Five of
the seven are one line.

| # | Action | Layer | Closes | Size | Absorbed by an open object? |
|---|---|---|---|---|---|
| **1** | Add a lowercase/path-form case to the `PRIVATE_NAME` rule in `independent_privacy_scan.py`, with the two-fixture control of § 4.5 as its test | TOOL/SCRIPT + **HUMAN GATE** | M3-10 | 1 pattern + 2 fixtures | **`harden-release-scan-scoping`** already exists and is the natural home |
| **2** | Add `regenerate_adjudications.py verify` to `run_release_regressions.py`, and one test that opens a real recipe | TOOL/SCRIPT | M3-8 | 1 line + 1 test | v2 repair #2's sibling — same commit |
| **3** | Make every gate verdict print the population it covered: `deepdive_manifest` (`n text-verified / n skipped`), `regenerate_adjudications` (`n recipes`), the privacy scan (`n files scanned`) | TOOL/SCRIPT | M3-9, M3-8, part of M3-3 | 3 f-strings | new, minimal |
| **4** | Add a `measured_at_ref` field beside every population table a Scientist publishes; back-fill `scientist_evidence_standard.md` § 0 | SCIENTIST CONTRACT | M3-1, M3-2, M3-3, M3-11 | 1 field | **fold into the existing `scientist_evidence_standard.md`** — do not originate a parallel object |
| **5** | Before a closing/summary artifact lands, diff it against every peer artifact committed since its draft opened; stamp a superseded summary rather than leaving it | HANDOFF/PLUMBING | M3-5, M3-6, M3-12 | a merge-base check | **`PATHOGRAPH-TRANSPORT-CONSOLIDATION-001`** already owns the transport class |
| **6** | Surface Annex C.3's round cap in the Scientist and Orchestrator fingerprint sets; register a deviation rationale or an amendment | ORCHESTRATOR CONTRACT + **HUMAN GATE** | M3-14 | fingerprint composition | `governance/plan_defined_parameters.md` § P2.2 |
| **7** | Commit Plan's 12 records and 3 commit candidates | HANDOFF/PLUMBING | M3-15 | a `git add` | carried from v2 repair #1 |

**Not proposed, deliberately:** no new actor · no new control plane · no graph schema · no
numerical stopping threshold · no new governance annex · no rewrite of
`regenerate_adjudications.py` · no re-opening of the science.

**Sequencing note, and it is the one an ordinary review would get wrong.** Action **3 before
action 4**. If the contract requires a `measured_at_ref` while the gates still print unqualified
`PASS`, actors will declare the ref of a measurement whose *population* is still undeclared — and
the next M3-3 will arrive wearing a ref stamp and look verified.

---

## 13 · FINAL QUESTION

> *Is the Scientist package merely TRUE on the surfaces it inspected, or is it COMPLETE ENOUGH —
> with explicitly bounded residual uncertainty — to permit surgical repair without reopening
> exploratory science?*

**TRUE on its surfaces. NOT complete. AND surgical repair is available without reopening the
science** — those three are compatible and the package earns the third.

- **True:** every producer figure I could re-derive, reproduced. The census exact at `main`. The
  gradient's shape, plateau and convergence exact in an independent implementation. Page 21 exact
  to the decimal. No canonical mutation, verified with a positive control.
- **Not complete:** four confirmed instances outside the disclosure list (M3-5, M3-6, M3-8,
  M3-10), plus a structural independence fact the run could not see from inside (M3-1) and a
  frozen governance constraint nobody cited (M3-14). Answering the Orchestrator's closing
  question 4 directly: **the § 4 / § 5 correction list is the part that was visible from inside**,
  and the part that was not is the part about *which tree*.
- **Surgical anyway:** every one of the fourteen is closed by a command, a field or a line, and
  **none requires re-reading a paper, re-adjudicating a proposition, or reopening exploratory
  science.** The scientific residue the pilot declared open — the two `UN-ATTACKED` propositions,
  the WWOX-proximal-versus-systemic disagreement, the nineteen unadjudicated edges — is
  untouched by this review and remains exactly as the producers left it.

**The one thing that must not be surgical is § 4.5.** It is a privacy property of a public
repository, it predates this pilot, and the gate says `PASS`. It goes to the Operator.

**And the boundary, since the dispatch asks me to review it rather than the conclusions:** this
package is the first in the record whose authors made their own failure list the *primary* output
and the science the secondary one. That inversion is what let a fourth seat find fourteen things
in an afternoon. It is also why the fourteen are small. **Both of those are the same fact.**

---

## 14 · HANDOFF v2.1

```
HANDOFF · MIRROR → PLAN (cc ORCHESTRATOR)
REVIEW_ID          SCIENTIST_PILOT_PROCESS_HOSTILE_REVIEW_MIRROR_v3
OBJECT             the closed PMID 32000863 three-Scientist cross-review pilot, as a PROCESS and
                   EVIDENCE SYSTEM — 29 Scientist artifacts, the Orchestrator packet and Mirror
                   handoff, six gates, and the interaction record
LEVEL              R4 (METHOD — Mirror) · C.4 object class SYSTEM
VERDICT            REFINED
RELATION           COMPLEMENTS PATHOGRAPH_PIPELINE_HOSTILE_REVIEW_MIRROR_v2 — does not supersede it
OBSERVATION_SCOPE  2026-08-25T19:16:40Z · mirror c7e8d6e (0 behind main) · main 788c357 ·
                   lettore 605fc5d (201 behind) · lettore-b 9a09590 · lettore-c 5b1d6c2 ·
                   orchestrator-packet a58af46 · plan e4aa80c · 44 heads + 5 remotes swept,
                   positive control passed · 29 docs / 746,625 B archaeology · 48 .md privacy sweep

1 · WHAT MIRROR CONFIRMED
  Producer figures reproduced: 448/333/39 · 8.71% · 74.33% (exact at main) · 55/55/0 PDFs ·
  9 figure-less · 289 image pages · monotone decay to a 42.7% plateau equal to the page union ·
  Cheng suppl. p21 out-of-bounds bboxes to the decimal · zero canonical mutation (positive control) ·
  LINT PASS · receipts OK 128 chained · growth anchors PASS.
  Producer taxonomy: four classes are distinct and each implies a different repair layer.
  Producer recommendation against a new reviewer actor: CORRECT, on independent evidence.

2 · WHAT MIRROR REJECTED OR NARROWED
  M3-7a  "seven additive rounds before the first collision" — REFUTED by the Phase II documents
         themselves (A: 5 disagree items · C: 2 · B: 2 named). Must not enter a design argument.
  M3-3   448 is one of three defensible populations; the gate's own is 3 recipes / 47 locators.
  M3-4   the 55/55/0 three-hand agreement is entailed by one gitignored directory, not corroborated.
  M3-9   "the recipe form does not apply to 333/448" understates coverage (image identity IS gated)
         and misses the sharper number: 338/1002 locators (33.7%) outside every text check.
  M3-13  "every decisive locator came off a PNG" — 2 of 5 point at the supplementary PDF.
  E is not a fifth failure class; it is B observed from outside. Merge it.

3 · WHAT REMAINS UNRESOLVED
  The two dispatch texts are not durable artifacts, so "prompts biased actors toward extension"
  is UNTESTABLE from Mirror's surface. My no-text numerator runs 4–8 below the producers' at every
  join gap; criterion difference unresolved, shape and plateau unaffected. How many of the 338
  unchecked figure locators are load-bearing is unmeasured. Whether Annex C.3's 2-round cap suits
  a three-seat scientific cross-review is not Mirror's to decide.

4 · SCIENTIFIC vs OPERATIONAL
  SCIENTIFIC: none. Mirror adjudicated no biological proposition, typed no edge, touched no
  hypothesis, and propagated none of the eleven reported canonical defects. The declared scientific
  residue is untouched.
  OPERATIONAL: all 15 findings.

5 · WHICH OPEN OBJECT CAN ABSORB EACH FINDING
  M3-10                    → branch `harden-release-scan-scoping` (exists) + HUMAN GATE
  M3-8                     → the same commit as v2 repair #2 (the two typing invariants)
  M3-9, M3-3(part)         → new, 3 f-strings, no new object
  M3-1, M3-2, M3-3, M3-11  → fold into `scientist_evidence_standard.md` — DO NOT originate a parallel object
  M3-5, M3-6, M3-12        → `PATHOGRAPH-TRANSPORT-CONSOLIDATION-001` already owns the transport class
  M3-14                    → `governance/plan_defined_parameters.md` § P2.2 fingerprint composition
  M3-15                    → v2 repair #1, unfinished for the Plan seat only
  M3-7, M3-7a, M3-13       → record only; no object needed

6 · REQUIRES HUMAN GATE
  M3-10  the release gate returns PASS on a tree carrying 26 occurrences of the Operator's given
         name across 16 tracked files on `main`, five of them in shipped public-edition surfaces.
         Pre-existing, not caused by the pilot, and not a producer's to decide.
  M3-14  eight rounds against a FROZEN `max 2 round → adjudication`. Either a registered deviation
         or an amendment; both are above every actor here.

7 · WHAT SHOULD NOT BE CHANGED
  No new actor. No new control plane. No graph schema. No numerical stopping threshold. No new
  governance annex. No rewrite of regenerate_adjudications.py. Rule 5e, the manifest text gate,
  fail-closed behaviour, the UN-ATTACKED marking, the actor boundaries, the graph's UNTYPED edge,
  and the unlegislated self-defect-filing practice all stand as they are — see § 11, twelve items.

SEQUENCING  Action 3 (gates print their population) BEFORE action 4 (contract requires a ref).
            Reversed, the next wrong denominator arrives wearing a ref stamp and looks verified.

MIRROR ASSERTS NO SCIENTIFIC VERDICT. No biological relation was adjudicated. No forced consensus.
No new reviewer actor created or proposed. No governance object created. No canonical file read for
writing. No personal identifier introduced into this artifact. Nothing was mutated by this review;
all mutation testing ran on scratch copies through the tools' own --workspace flag.
```
