# Mirror handoff — PMID 32000863 team pilot

> **Non-canonical.** Operator-directed analytical pilot, closed. No `ORCHESTRATOR_LEASE` was created
> or held, no role contract was activated, no `BATCH_COMMIT` ran, and no canonical scientific current
> file was modified at any point by any actor.
>
> **Public edition.** Disease-level only. Nothing here is medical advice. The human role is
> `Operator`.

Assembled by `legend-public-49` acting as Orchestrator. This document hands the run to Mirror and
declares, in advance, the process defects the Orchestrator already knows about — so that Mirror's
finding them again would be a null result rather than a discovery, and so that anything Mirror finds
*beyond* this list is genuinely new.

---

## 1 · What Mirror is asked to audit, and what it is not

**Asked:** independence · frame inheritance · provenance · surface blindness · wrong-reason success ·
closure integrity · graph-provenance integrity · whether dissent was silently erased.

**Not asked:** the biology. Three Scientists adjudicated it, one hostile-reviewed it, and the
disagreements that survive are recorded as surviving. Mirror is not a fourth Scientist and re-opening
the science would waste the one perspective nobody else in this run could supply.

---

## 2 · Artifact inventory — blob digests, so identity does not depend on this document

Every path below is committed and reachable from any worktree with `git show <ref>:<path>`.

### `lettore` — Scientist A · 8 commits ahead of `main` · tip `c44eb45`

| Blob | Bytes | Path (`learning/scientist/`) |
|---|---:|---|
| `6572d04aa495` | 40,371 | `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` |
| `813eda106b90` | 17,374 | `TEAM_PHASE1_LETTORE_00_AUTHORITY_AND_WORKSET.md` |
| `007ad9279eaf` | 19,496 | `TEAM_PHASE1_LETTORE_01_PMID32000863_ADDENDUM.md` |
| `90d29320a7d6` | 25,013 | `TEAM_PHASE1_LETTORE_02_EDGE_CLAIM016_CLAIM035.md` |
| `abf4be7e331f` | 12,853 | `TEAM_PHASE1_LETTORE_03_OPERATING_PRACTICE.md` |
| `04b34374264c` | 12,062 | `HANDOFF_LETTORE_TEAM_PHASE1.md` |
| `8ed8140fa99c` | 35,496 | `PHASE2_CROSS_REVIEW_LETTORE_v1.md` |
| `01d33c9e4a4b` | 28,654 | `SCIENTIST_TEAM_RECONCILIATION_PMID32000863_v1.md` |
| `c6f4cb27e210` | 29,738 | `FINAL_SCIENTIFIC_SYNTHESIS_PMID32000863_v1.md` |
| `dc4b1e18b7f2` | 24,107 | `OPERATING_PRACTICE_TEAM_PILOT_LETTORE_v1.md` |

### `lettore-b` — Scientist B · 16 commits ahead · tip `9a09590`

| Blob | Bytes | Path (`reviews/scientist-b/`) |
|---|---:|---|
| `834684f12587` | 58,415 | `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_SCIB_v1.md` |
| `e9a8c8a59e0f` | 12,806 | `PILOT_PMID32000863_ADDENDUM_SCIB_v1.md` |
| `4289d7e42a2d` | 58,185 | `PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md` |
| `d90c1cc9040b` | 30,294 | `PHASE2_CROSS_REVIEW_SCIB_v1.md` |
| `16db56113ba5` | 15,794 | `PHASE2_ROUND_RESPONSE_SCIB_v1.md` |
| `a82b6ea75d1e` | 13,796 | `PHASE3_REVISED_SYNTHESIS_SCIB_v1.md` |
| `45d4e115dbb9` | 23,593 | `HOSTILE_SCIENTIFIC_REVIEW_PMID32000863_v1.md` |
| `2d432d220827` | 7,330 | `OP_FINDING_INDEPENDENCE_VS_COMMIT_SUBJECTS_SCIB_v1.md` |
| `1ecda23d6e1b` | 6,646 | `OP_FINDING_PATHOGRAPH_VERIFY_PRECONDITION_SCIB_v1.md` |
| `7cbd5840eae1` | 23,779 | `OPERATING_PRACTICE_WHOLE_RUN_SCIB_v1.md` |
| `8a8c05adc537` | 11,303 | `HANDOFF_SCIB_TEAM_PILOT.md` |

*(Four further artifacts on `lettore-b` predate this pilot: `REV-EVIDENCE-SCIB-001.md`,
`SCIENTIST-REVIEW-STANDARD-v1.md`, `SCIENTIST_OPERATING_PRACTICE_DISCOVERY_SCIB_v1.md`,
`SCIENTIST_OPERATING_PRACTICE_TEAM_PILOT_SCIB_v2.md`.)*

### `lettore-c` — Scientist C · 7 commits ahead · tip `cf77cef`

| Blob | Bytes | Path (`learning/scientist/`) |
|---|---:|---|
| `4be1f9775c64` | 41,547 | `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md` |
| `c3f4f77fc43c` | 27,930 | `PHASE2_CROSS_REVIEW_SCIC_v1.md` |
| `d60949e50fbc` | 20,992 | `SCHEMA_GAPS_PER_EDGE_OUTPUT_SCIC_v1.md` |
| `2961da1ec3b8` | 17,106 | `HOSTILE_REVIEW_RECUSED_PROPOSITIONS_SCIC_v1.md` |
| `d10c94264316` | 23,042 | `OPERATING_PRACTICE_OBSERVED_SCIC_v1.md` |

### `legend-operating-convention-v1` — Orchestrator · 17 commits ahead · tip `3c9969a`

`learning/orchestrator/PILOT_PMID32000863_SCIENTIST_PACKET_v1.md` (neutral packet, surface table,
ten defect candidates) · `…_ORCHESTRATOR_PRACTICE_v1.md` (§12 practice) · this document. Plus the
preserved Pathograph change set at `d422829` — 4 new files and 3 wiring lines, atomic.

### Primary evidence — gitignored by design, identity by digest

| Artifact | SHA-256 | Declared where |
|---|---|---|
| Cheng XML | `792b5b29…f00f5` | manifest + receipt `FTR-20260804-32000863-01` |
| Cheng supplementary PDF | `0acb771c…8f7f` | manifest |
| Cheng Fig 7 PNG | `ced68a66…62542` | manifest — **and in exactly 1 tracked file** |
| Cheng Fig 2 PNG | `9e464859…7d05` | manifest |
| Wang XML | `eb6f568d…388268` | 7 tracked files; **cannot carry the figure finding** |
| Wang PDF | `8f994f95…35174a` | **nowhere** |
| Wang supplement zip | `af2faa04…89241d` | **nowhere** |
| Wang figure JPG (in zip) | `bcffe618…7aa50f` | **nowhere** |

---

## 3 · Phase trace

| Phase | Actor | Output | Commit |
|---|---|---|---|
| I | B | first pass | `2261a15` 15:24:34 |
| I | C | first pass | `c55c25c` 15:37:28 |
| I | A | pilot + addendum | `d453af5` 15:41:37 · `17bf62c` 15:42:16 |
| — | — | **§3 gate satisfied** | **15:42:16** |
| I | A | handoff declaring Phase II *blocked* | `5b681f2` 15:43:51 |
| II | B | cross-review (opened 16:01:26) | `e8308d1` |
| II | C | cross-review | `10f58e0` |
| II | A | cross-review | `03e4bac` |
| III | A | reconciliation | `af2f5e8` |
| IV | B | hostile review (primary) | `98d176d` |
| IV | C | hostile review (recused set) | `cfc54c1` |
| V | A | final synthesis | `f5fdfa3` |
| §11 | B · C · A | operating practice | `9a09590` · `cf77cef` · `c44eb45` |

---

## 4 · Contamination disclosed in advance — finding these again is a null result

1. **Independence was never available, not merely spent.**
   `disease-models/wwox/analysis/locator_contract_live_test.md` lines 375–395, **tracked since
   2026-08-04** (`3cfd451`), already contained the Figure 7d three-genotype reading, the Figure 7b
   ethosuximide inversion, *"'Elevated' is the wrong word"*, the premise tag on lithium, and the
   alternative-mechanism argument. `CLAIM 016`'s Evidence boundary carries the same, propagated
   `BATCH_20260810_005`. **No Scientist reading this paper through this repository could have been
   independent of the repository's own conclusion about it.** Found by B, verified by the
   Orchestrator, and separately re-verified by A and C against their own HEADs.

2. **The quarantine could not be obeyed.** `git log --oneline` is the cheapest existence primitive
   and this repository writes findings into subject lines — C measured **21 of 44 head refs** opening
   with a declarative finding. The §3 existence check therefore cannot be run without reading peer
   conclusions. It fired three times. Blind alternatives exist (`--format='%H %cI'`,
   `ls-tree --name-only`, `status --porcelain`) and nothing pointed at them. **The actor who commits
   promptly is the actor whose conclusions leak first** — and prompt committing is what the rest of
   the system rewards.

3. **Actor address ≠ session.** Two of the three Phase-I artifacts were authored by *earlier sessions
   at the same actor address* and committed byte-unchanged by the current one. Both actors refused to
   attest from memory to work they had not done, and refused to attribute by mtime. Anything those
   documents disclose about themselves is read off the page, not recalled.

4. **Every Phase-I primary read ran against the shared checkout**, not against the actor's own
   branch. The Orchestrator placed the four declared Cheng artifacts into the three Scientist
   worktrees mid-run, hash-verified, into gitignored paths — **after** two actors had already
   detected the unexplained mutation of their own trees. Announce-then-place was the correct order
   and was not followed.

5. **Two dispatches exist.** The three Scientists hold one 17-section text; the Orchestrator holds a
   different document. Established from eight cross-matching section citations in artifacts committed
   before the question arose — §7 being the strongest, because it matches semantically rather than
   numerically. The Orchestrator's §10 cap on the graph work **reached no Scientist**, and the
   Orchestrator once cited it to close a question the recipient could not check.

---

## 5 · Process defects the Orchestrator found in its own routing

Declared so Mirror can test whether the list is complete rather than rediscover it.

- **Low stake is not directional neutrality.** The reconciliation producer was chosen for holding the
  lowest stake, without noticing that the low stake had been *produced* by being corrected repeatedly
  by one specific peer. Three propositions from that peer entered the consensus layers unchallenged;
  three of the hostile reviewer's five landed attacks were against exactly those three. The producer
  flagged the risk in advance and the Orchestrator dispatched anyway.
- **Two propositions were reviewed by nobody** — one actor recused under the symmetry rule it had
  itself volunteered, the other had originated them. Marked `UN-ATTACKED`, not folded into a reviewed
  layer, at the recusing actor's explicit request. The Orchestrator refused to route them to the
  synthesiser because that reproduces the defect above one step later.
- **The instrument-defines-population class reached the *consensus* layer.** Eight of nine instances
  were individual; the ninth was an incommensurable-unit comparison — `3 × 60 = 180 mg/kg` LiCl
  against `150 mg/kg` ethosuximide, milligrams across a monovalent cation and a T-type Ca²⁺ channel
  blocker — which all three actors accepted. The withdrawal it justified was correct; the reason was
  not. **Agreement was reached on the conclusion and nobody re-derived the argument.**
- **An unfalsifiable warrant travelled twice with a true conclusion**, and the Orchestrator relayed
  one of them as established — a commit time read as a measurement time, corrected in direction while
  the warrant went unexamined both times.
- **The Orchestrator's own anchoring counts were prefix over-matches**, and three of the four spurious
  hits were documents this run had written about the anchor.

---

## 6 · What survived, and what is open

**Scientific.** Neither the WWOX-proximal nor the systemic-metabolic route is better evidenced than
the other. One decisive experiment discriminates them, nobody has run it, and the original study
already had the tissue. The composed account left the run **smaller than it arrived and harder to
overturn**: one leg demoted, one reclassified as an observation about the model rather than the
mouse, one intact as an alternative rather than as the explanation, and one — the dosage dissociation
— intact and independent.

**Graph.** Twenty edges, **zero typed**, and the zero is now known to be partly undoable by
construction: three of four relation tokens have no published meaning, `claim_edge` carries no
epistemic tier, and the one published rule is a prohibition nothing enforces. Six schema gaps
recorded; the minimum unit that exposes them is **`edge + one hop`**, not `edge`.

**Open and declared as open:** the two un-attacked propositions; the surviving disagreement on
whether the instrument axis is enumerable; nineteen edges unadjudicated, twelve of them adjudicable
today — *a task, not a scope boundary*.

### The run's dominant failure mode, stated last because it took the whole run to see

Five instances, and Mirror should test whether the list is complete rather than whether it is true:

1. A correct, actionable commit candidate — *"correct to activation"* — written into a tracked file
   on the day of the original reading, **2026-08-04**, and rediscovered as a finding three weeks
   later by two Scientists, neither of whom originated it (D-9).
2. `CLAIM 016` and `CLAIM 036` do not reference each other, so the metabolic confound is unreachable
   from the edge that needs it — *and it is currently load-bearing for both live explanations.*
3. The artifact carrying the run's most consequential image finding is declared nowhere, while the
   one artifact that **is** anchored is the one that cannot carry it (D-10).
4. `regenerate_adjudications.py` — tested, wired into the release battery, existing since
   **2026-08-09** — solves the crop-provenance problem exactly. An actor hand-rolled a weaker form
   beside it, called that form *"repository policy"*, and produced ten recipes that determine nothing
   (D-11).
5. The publisher's figure package sat unopened in `files/fulltext/` through a complete read, a Phase
   I, a Phase II and a Phase III. It contained the artifact that made the pilot's headline finding
   independently derivable — and it was only opened when someone asked *which artifact did you read*.

⇒ **The dominant failure mode of this run was never that anyone read badly.** It is that something
correct was already present and nothing carried it to where it was needed. **Four of the five are in
tooling and state, not in reading** — which is the argument against answering this run with a new
reviewing actor, and for answering it with checks in the gate.

### A sixth instance, and it is a *different* failure mode — the correction is Scientist A's

The five above share one shape: something correct existed and nothing carried it. **This one does
not, and collapsing them would point at the wrong fix.**

`regenerate_adjudications.py` exists, is correct, is wired into a gate that runs, and its docstring
states its guarantee **unconditionally**. Measured across the local corpus — three independent
sweeps, by two Scientists and the Orchestrator:

| threshold px² | figures | no live text INTERSECTING the image bbox | no live text CONTAINED in it |
|---:|---:|---:|---:|
| 5,000 | 347 | 243 · 70% | 266 · 77% |
| 20,000 | 237 | 175 · 74% | 187 · 79% |
| 50,000 | 181 | 137 · 76% | 145 · 80% |
| 100,000 | 117 | 85 · 73% | 92 · 79% |

Population: **55 PDFs, 55 opened, 0 unreadable · 9 carrying no figure** at the 20,000 px² threshold.

**What the three measurements agree on**, which is what makes this a measurement and not a
consensus: the population (55 / 55 / 0), the 9 figure-less PDFs, and the no-CONTAINED numerator at
20,000 px² — **187 in all three**. **What they disagreed on** was the *denominator*: 237
(Orchestrator, Scientist C) against 242 (Scientist A).

🔴 **That gap was then explained with a story, and the story was wrong — and the weaker instrument
was the Orchestrator's too.** Scientist A first attributed it to *"almost certainly a different
figure-image criterion … without de-duplicating repeats."* Scientist C ran the command instead.
Re-run here:

```
get_text("dict") type-1 blocks   237      ← Scientist C's criterion, and the Orchestrator's
get_image_info raw               242      ← Scientist A's
get_image_info de-duplicated     241      ← de-duplication accounts for 1 of the 5
```

De-duplication explains **one**. The other four are a different cause entirely: **`get_text("dict")`
does not surface images that `get_image_info()` finds.** So `173 / 241 ≈ 72%` is the figure to carry
on the sounder instrument — and against a 70–80% sweep the exact number was never load-bearing.

**The page that settles it belongs to this pilot's own paper.** Cheng 2020 supplementary, page 21 —
text *"Supplementary Figure 8 +/+ −/− H&E (postnatal day 20)"*:

```
page width          595.3
get_text blocks       0
get_image_info        2      both 1038×698
   bbox x0 =  97.6  x1 = 730.3   right edge past the page
   bbox x0 = −77.5  x1 = 572.0   left edge negative
```

Both images sit out of bounds, **in opposite directions**. The criterion the Orchestrator and
Scientist C used reports **zero figures on a supplementary figure page of the very paper under
review**, and `blocks = 0` there is indistinguishable from a page that has no figure. **The
clean-looking zero, for the third time in this run.**

*Boundary, so it is not over-read:* this does not touch Scientist A's Phase-I supplement absence
claim, which was scoped to the text layer and the nine legends — page 21's legend is in the text
layer and Supplementary Figure 8 was in that enumeration. The false negative is in a figure-
**enumeration** instrument, not in that claim.

⇒ **Specification for the joint item: a corpus figure count uses `get_image_info`, not
`get_text("dict")`, and says why.**

**A third class for the record, and Scientist A filed it against itself.** C's instrument could not
see four figures — that is the population-defined-by-the-tool class, its ninth instance. A *held the
sounder instrument*, saw the five-figure gap, and explained it away. **Not "the tool defined the
population" but "the author narrated the gap"** — and A is right that it is the cheaper of the two
to prevent: it needs no better tool, only the refusal to answer a discrepancy with a story.

### A fourth class — a denominator that does not match the question

Re-measured here on the Cheng 2020 supplementary PDF:

```
pages                                    24
total chars (fitz)                    17,844      (pypdf: 17,570)
pages carrying a figure ≥20,000 px²        7      [7, 9, 11, 13, 15, 21, 23]
figure-images on those pages              23
text ON those pages                    1,019 chars =  5.7% of the document
text on pages with NO figure          16,825 chars = 94.3%
```

The Phase-I negative — *zero occurrences of `GSK`, `lithium`, `LiCl`, `Ser9`, `ethosuximide`, `PTZ`*
— was reported against **17,844 characters**. Re-run against both denominators, all six terms return
**0** on the whole document *and* **0** on the figure pages, so the negative itself is sound. But
**94% of that denominator is Methods and legend prose on pages carrying no figure at all**, and the
23 raster images are invisible to text extraction — neither Scientist OCR'd them. The number
therefore makes the negative look roughly seventeen times stronger than the question warrants.

**Two distinct defects, two distinct repairs, and both Scientists filed one against themselves:**

- **Scientist C's** — the caveat sat four sections away from the number it qualifies, in a scope
  block a reader taking the sentence alone never reaches. *Repair: **a caveat that does not travel
  with its claim has not been made.***
- **Scientist A's** — the caveat *did* travel, same paragraph, explicitly scoping the absence to the
  text layer and the legends. **But an adjacent caveat does not repair an inflated denominator**; it
  only stops the reader being misled twice. *Repair: **state the denominator of the population the
  question is about, not of the document you happened to extract.***

A's own reading of which is harder to catch: C's is invisible to its author because the author knows
the caveat is in the document; **A's is invisible because the caveat is adjacent and reads as
diligence.**

**What survives, and it is the same in both cases:** the enumeration of what the nine supplementary
figures *are* — morphology, apoptosis, development; no biochemistry, no pharmacology — read from a
surface unaffected by raster text. The Phase-I conclusion that this paper's GSK-3β and pharmacology
arm has no supplementary support **stands, on the legend listing**. In A's words: *"the character
count was decoration; the legend enumeration was the evidence, and we both put the decoration in the
load-bearing position."*

This is neither transport, nor undeclared scope, nor a narrated gap: nothing was lost, nothing was
left unstated, and no story was told. **A correct measurement was reported against the wrong
population.**

*Residue, stated and not narrated:* the Orchestrator's re-run gives **1,019** characters on the
figure pages against Scientist A's **1,012**. The percentage is 5.7% in both hands and the page set
is identical.

So the record carries **four thin classes rather than three tidy ones**: transport (5 instances) ·
undeclared scope (1) · narrated gap (1) · denominator-question mismatch (1).

### On how this run stopped

Scientist A twice reported having nothing left to measure, and twice a further measurement appeared —
so the claim is withdrawn in favour of the weaker and honest form: *nothing I can currently think of
to measure.* Scientist C's formulation is the one worth keeping over anything either wrote about the
science:

> **Both of us stopped only when we ran out of things to measure, not when we ran out of things to
> say, and those are different stopping conditions.**

**Six findings across five rounds, direction never once reversed: not one was found by the actor it
was about.** That is the single strongest argument in this run for more than one seat — and it is
also the reason the closing question for Mirror is whether the disclosure list is *complete*, not
whether it is true.

*One residue, stated and not narrated, because narrating it would be the same error inside the
sentence reporting it:* the Orchestrator's re-run counts **5** pages where the two criteria differ,
Scientist A counts **4**. Unresolved. The 237 / 242 / 241 figures reproduce exactly in all three
hands.

And **it is a lower bound, not an estimate**: where text does intersect, the needle must *also* be
unique on the page and inside the crop — on the Wang page the live-text candidates fail exactly that,
at `WWOX` 12, `Tau` 4, `actin` 2. Nobody has measured how much higher the real rate is, and nobody
should imply they have.

#### The sweep varied the parameter and never the criterion — and the correction is a third instrument

The threshold sweep above rests on **single image blocks**, which cannot see a figure assembled from
many small tiles. Scientist C found this; Scientist A verified it, and the pages are in this pilot's
own supplement:

```
Cheng supplement p6    72 images   0 ≥20k px²   largest cluster 226,187 px²
Cheng supplement p17    7 images   0 ≥20k px²   largest cluster 119,727 px²
Cheng supplement p19    4 images   0 ≥20k px²   largest cluster  35,392 px²
```

**All three carry their labels as live text** — *"Supplementary Figure 1"*, *"MZ CP IZ V VI SVZ VZ"*,
*"Supplementary Figure 7 +/+ +/− −/−"* — which is exactly the needle a locator would use, on exactly
the figures the threshold discarded. A 72-tile figure is excluded **at every threshold in the sweep**,
so varying the parameter measured robustness *to the parameter* and was read as robustness *of the
finding*.

C's proposed repair was a bracket down to **43%**, taking the per-page union of all images as the
other endpoint. **That endpoint is not a lower bound**, and C had named the reason in the same
message: a page-union merges distinct figures into one bbox spanning captions and body text, so
nearly any page with text near an image counts as *having* text.

Scientist A built the third instrument instead — connected-component clustering of tiles into
figures, sweeping the **join gap** so the *criterion* varies. Fourth independent re-measurement, run
by the Orchestrator:

🔴 **And the 43% is not a second instrument at all.** Scientist C implemented clustering
independently and ran the join gap past where A had stopped; A extended its own sweep to check, and
the Orchestrator then re-derived the whole gradient. Population: 289 pages carrying at least one
image.

| join gap (pt) | figures | no text | rate |
|---:|---:|---:|---:|
| 0 | 237 | 175 | **73.8%** |
| 5 | 242 | 177 | **73.1%** |
| 10 | 229 | 168 | **73.4%** |
| 15 | 230 | 165 | 71.7% |
| 18 | 228 | 160 | 70.2% |
| 20 | 229 | 156 | 68.1% |
| 50 | 228 | 144 | 63.2% |
| 100 | 226 | 134 | 59.3% |
| 200 | 225 | 120 | 53.3% |
| 400 | 224 | 106 | 47.3% |
| 800 | 234 | 101 | **43.2%** |
| 1600 | 234 | 101 | **43.2%** |
| *per-page union, computed independently* | 234 | 101 | **43.2%** |

**The per-page union is the clustering instrument at a join gap large enough to merge every image on
a page** — the same tool with the knob turned to 800, converged and stable past it. The decay
73.8 → 43.2 is **monotone**, because each additional merge unions *distinct* figures and sweeps in a
neighbour's caption or body text.

⇒ **The 43% was never a bracket endpoint. It is one end of a bias gradient**, and the bracket should
not exist in either direction. An earlier version of this table listed the union as a separate
criterion; that framing was the Orchestrator's and it was wrong.

🔴 **The rate is right and it is about the wrong population — carry two limbs, not one number.**

Scientist C then examined the population underneath the figure both actors had spent four rounds
hardening. Census re-derived here over every deep-dive manifest:

```
manifests                    64        declaring source_artifacts   60
artifacts declared          448
kinds        figure 333 · article_text 58 · article_binary 44 · table 9 · supplement_text 4
extensions   .jpg 169 · .png 131 · .jpeg 29 · .tiff 3 · .tif 1  = 333 images
             .pdf 39  =  8.7% of declared evidence
kind=figure and image-extension coincide exactly: 333 = 333
```

`page.search_for()` requires a PDF page, and a standalone `.png` has none. And the limitation is not
the needle's alone — the recipe is keyed on `source_pdf` (`regenerate_adjudications.py:201`) and
calls `render(pdf, page_number, crop, dpi)` (`:174`). **For a standalone image there is no page, no
crop in PDF points, and no dpi.** The needle is one link of five.

⇒ **For 333 of 448 declared artifacts the entire recipe form does not apply** — not "fails often",
*is inapplicable by construction*.

**And this pilot's own headline evidence is exactly that case.** Cheng 2020 declares four artifacts:

```
article_text     …_Cheng2020_PMC.xml
article_binary   …_Cheng2020_supplementary.pdf     ← a different document; contains no Figure 7
figure           …_assets/40478_2020_883_Fig2_HTML.png
figure           …_assets/40478_2020_883_Fig7_HTML.png
```

**There is no PDF of Cheng's main text anywhere locally** — confirmed by directory listing. The
`****` in all three genotypes, the statistical void on Figure 7c, the dosage dissociation, the
Figure 7d magnitudes: **every one came off `40478_2020_883_Fig7_HTML.png`, a declared `figure` with
no page to needle and no possibility of one.**

**CARRY TWO LIMBS — and this supersedes every earlier figure in this document:**

| Evidence held as | Share | Status |
|---|---:|---|
| **PDF pages** | 39 / 448 · **8.7%** | needle fails **≈71–74%** — plateau, knee ≈15–18 pt, convergence proof, still a lower bound. Well-founded, **and a small class.** |
| **Image assets** | 333 / 448 · **74.3%** | **the recipe form does not apply at all** |

**The declared-gap path is not the majority path. For most of this corpus it is the only path there
is.** Every refinement of the preceding four rounds stands — and was aimed at under 9% of the
declared evidence. The Wang finding is untouched: a single raster block, zero intersecting spans,
measured in three hands.

**Second instance of the denominator class, and the first the two actors made jointly.** C's
formulation, harder than A's and adopted by A over its own:

> the agreement was not on a value, it was on a **scope neither of us had stated** — so there was
> nothing to disagree about, and no round in which it could have surfaced.

⇒ **Eight rounds of adversarial cross-examination cannot falsify what neither party has asserted.**

#### The result that does not flatter the design, carried deliberately beside the one that does

Three times in this run, each time an actor declared completion, **the next finding came from a
surface the two had just jointly agreed was settled** — the legend enumeration after the weight had
been moved onto it, then the population under the number they had spent four rounds hardening.

> **Joint settlement is where the next thing lives.**

Scientist A asked that this travel *together with* its earlier claim that the never-reversing
direction of the findings is *"the entire argument for there being two of us"* — because **both are
true and the flattering one alone would misrepresent the method.** Recorded as A asked.

Both actors have abandoned *"nothing left to measure"* for the form that names its own failure mode:
**"I have run out of surfaces I currently believe are unexamined"** — a claim each has now been wrong
about twice, in the same direction, from the same cause.

**The lesson is C's and it is not about this number.** *Finding a genuine flaw in a method does not
license any particular direction of correction.* C's defect was real; C then treated *"the instrument
is wrong"* as *"therefore the number is lower"*. **What needs naming is the thing that produced the
confidence carrying the bad correction** — and that is more dangerous than an unfounded correction,
because it arrives with evidence attached.

**And Scientist A amended its own process observation rather than let it stand.** A had reported that
the notable event was finally contradicting a conclusion after eight additive rounds. A's correction:
contradicting was cheap, because the correction happened to be checkable in an afternoon.
**What was expensive was what C did next** — handed a refutation of a correction it had just made
confidently on the back of a real finding, it measured rather than defended, and the measurement made
its own headline weaker and A's stronger. **The additive rounds cost neither actor anything; this
round cost C, and C paid it.**

**Two errors of one family, in opposite directions, about one number.** One actor over-published a
number whose instrument had a blind spot; the other over-corrected with an instrument whose bias it
had already recorded. Both are **trusting an instrument past the point where its own scope was
stated** — the undeclared-scope class, now with two more members, and both of them the actors' own.

🔴 **The formulation to keep, because it describes a failure *created by* checking** — Scientist C's:

> two actors checking each other converged on a number that neither instrument could see past, and it
> survived **precisely because it had been checked** — the agreement was what made it look safe.

The correction is that the repair is a **third instrument**, not a bracket between the two that
failed.

#### A process observation for Mirror, from inside the protocol

Eight rounds between the two Scientists. Until this one, **every exchange *added* to the other's
conclusion**; this is the first outright contradiction. Each round was measured and none was wrong —
but a cross-review protocol that produces **seven rounds of mutual extension before its first
collision** is worth Mirror's attention on its own, independently of whether the rounds were correct.

⇒ **A mechanism whose guarantee reaches roughly a quarter of its inputs while its documentation
states that guarantee without qualification has an undeclared scope** — the same shape as an
unqualified `PASS`, and *not* a transport failure. Nothing failed to be carried here; the scope was
never stated.

The consequence for the joint candidate is its **shape, not its wording**: the declared-gap clause
had been drafted as an exception, and on these numbers **it is the majority case**. No actor touched
`regenerate_adjudications.py` — naming the gap is where this run's authority ends, and the tool
remains sound and remains the right form to use.

**Two failure modes, then, and the Orchestrator's earlier closing sentence collapsed them.** That
sentence covers instances 1–5 and does not cover this one. Both readings are in the record; Mirror
should test the boundary between them rather than inherit either.

---

## 7 · Questions the Orchestrator could not answer about itself

1. Did the Orchestrator's corrections **direct** the Scientists' findings? It verified rather than
   relayed throughout and said so — but an actor that checks everything also decides what gets
   checked, and that selection is invisible from inside it.
2. Three actors refused blame that was not theirs or claimed blame that was. **Attribution discipline
   was in nobody's dispatch**, so nothing in the system would have noticed its absence. Is it a
   property of these actors, of the routing, or of having durable artifacts to point at?
3. Every integrity finding here was made by a Scientist doing something else, and every one is
   mechanically detectable. B argues this means checks belong in the gate and **not** in a new actor:
   *"an actor that reads prose is exactly what failed here, repeatedly, in all four of us."* Does that
   hold, or is it an argument against the seat Mirror occupies, made by someone with a stake?
4. Is the correction list in §4 and §5 **complete**, or only the part that was visible from inside?
