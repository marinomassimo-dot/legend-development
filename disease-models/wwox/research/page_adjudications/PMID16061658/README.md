# Page adjudication — PMID 16061658 (Aqeilan 2005, *Cancer Research*)

> ## 🔴 The images are not in this repository — the recipe is
>
> A crop of a printed page reproduces the author's characters. That is exactly what makes it
> evidence, and exactly why it cannot be redistributed. This article carries
> `©2005 American Association for Cancer Research`, and there is **no open deposit anywhere**:
> Europe PMC returns `pmcid null · inPMC N · isOpenAccess N`, Unpaywall returns `is_oa false ·
> oa_status closed · has_repository_copy false`. The crops cover two full text columns, a
> complete figure and a complete figure legend.
>
> So what ships is [`adjudications.json`](adjudications.json). From your own copy of the article:
>
> ```bash
> python3 framework/scripts/regenerate_adjudications.py write  --pmid 16061658
> python3 framework/scripts/regenerate_adjudications.py verify --pmid 16061658
> ```
>
> Current verdict: **9 artifacts regenerate to their declared digest, 10 locators resolve to a
> span inside the crop that shows them.**

## Why this article had to be adjudicated

Its text layer is `SUSPECT` and stays `SUSPECT`. Two C0 controls, and — decisively — **zero**
occurrences of `< > ≤ ≥ ± × − µ α β Δ` across 44,465 extracted characters, in a paper that says
*significan* six times and states plasmid amounts throughout. Suspicion by absence.

Then the damage, identified character by character:

| the layer says | the page prints | count |
|---|---|---:|
| `using 63\x01 objective lens` | `63×` | 1 |
| `(6.0 Ag)` · `(1.0 Ag)` · `(7.0 Ag)` | **`µg`** | 16 |
| `p73h` · `h-dystroglycan` | **`p73β`** · `β-dystroglycan` | 7 |

**Twenty-five corruptions, twenty-three printable — 92%.** A control-character scan finds two of
twenty-five and reports the surface clean.

🔴 **And the font layer says why, which is more useful than the count.** Nineteen fonts, all
embedded subsets, **all declaring `WinAnsiEncoding` and not one carrying a `ToUnicode` map**. The
PDF is not damaged: it is well formed and declares the wrong thing. That is why comparing
extractors detects nothing — `fitz`, `pdfplumber` and `pypdf` all obey the same false
declaration. The check costs one second and needs no extraction.

## The defect is visible *inside* the adjudicated set

`p06_figure5_legend_doses.png` is the demonstration, not an illustration of one. Those are the
plasmid amounts **of the competition experiment itself**. Quoted from the text layer, the legend
would have published four doses nobody used.

## Scope — bounded, and the bound is the point

This is a **bounded adjudication under a bounded authorisation**, not a complete read. All nine
pages were read as rendered images — that is how the perimeter was chosen, since an earlier
perimeter derived from a keyword scan *on the refused surface* was withdrawn. But only the
panels the competition frame rests on were inspected at adjudication resolution:
**5 of 17 panels**. Figures 2, 3 and 4 were seen at page scale and are **not** adjudicated; the
K274, localisation and transactivation experiments they carry remain reading debt on this
article, and the receipt records the depth as `partial_fulltext_read` for that reason.

## What the nine crops carry

| artifact | page | what it is for |
|---|---:|---|
| `p02_rationale_common_targets.png` | 2 | the hypothesis: WWOX and YAP share tandem WW domains and **common protein targets** |
| `p03_ww1_primarily_responsible.png` | 3 | the **WW1 anchor** — Y33R abolishes ErbB-4 binding |
| `p07_competition_experiment.png` | 7 | 🔴 **the DATO** — the whole Results section: titration, Y33R rescue, and the hedged conclusion |
| `p06_figure5_legend_doses.png` | 6 | the doses and the lane→antibody map, and the `µg`/`Ag` demonstration |
| `p06_figure5_panels.png` | 6 | Figure 5A/5B, the blots themselves |
| `p08_generalised_frame.png` | 8 | 🔴 the generalisation the downstream literature cites — to a **class**, `PPxY-containing target proteins` |
| `p08_affinity_asymmetry.png` | 8 | why WWOX is *prevalent*: it engages **both** PPxY motifs, YAP only one |
| `p07_figure6_legend.png` | 7 | the model's own statement of scope: *ErbB-4 and other target proteins* |
| `p07_figure6_model.png` | 7 | 🔴 the diagram, adjudicated **for an absence** |

## dpi discipline, measured before rendering rather than after

Per image, before any content was rendered:

- **page 6** carries the Figure 5 blots as raster at **149.1–149.9 effective ppi** → the panel
  crop is rendered at **150 and no higher**. Above that you are enlarging, not looking.
- **page 7 carries zero images.** Figure 6 is entirely **vector**, so 400 dpi there is
  resolution, not upsampling — and that was *measured*, not assumed from the fact that it looks
  like a diagram.
- text crops are vector and unconstrained.

## 🔴 The one absence this set is allowed to assert, and how

`ITCH` appears nowhere in this article. That statement has been made before in this corpus **and
was correctly withdrawn**, because it came from a term count on the refused text layer — and a
zero drawn from a surface that mangles sixteen printable characters is not an absence, it is
`NOT_FOUND_IN_TRIAGE`.

This one is different in route, which is the only thing that makes it reportable: it is read off
**Figure 6 at 400 dpi vector resolution**, on the diagram where the authors state which partners
they claim. They draw WWOX bound to an octagon reading *Other PPxY-containing partners*, to
`AP2γ`, and to `P73`. There is no ITCH.

**Consequence, stated as scope and not as a result:** this article anchors WWOX/YAP competition
at ErbB-4 and the PPxY-class generalisation. It is **not** the primary evidence for any
WWOX–ITCH claim. That evidence is `PMID 23370280`'s own co-immunoprecipitation with a Y33R
rescue control, and it belongs to that paper.

## Two things the executable recipe caught that prose would not have

**A crop that did not contain its own span, by 1.2 points.** `p03` was first cut at
`y1 = 697`; the span of `primarily responsible for the interaction` ends at `y = 698.2`.
`crop_contains_span` refused it. A published recipe that renders a crop *almost* containing its
locator is worse than no recipe, because it carries the badge of having been checked.

**Four needles that were not unique — because they wrapped.** `search_for` returns one rectangle
per line segment, so a phrase crossing a line break matches twice and is rejected. Every needle
here was therefore chosen off the layout to sit on a single printed line.

🔴 **And a needle discipline specific to this article.** A needle is matched against the **text
layer**, which is the thing under suspicion here; a snippet is what the **page** prints. So every
needle is drawn from a span that is pure ASCII in both surfaces, and none spans a `µ`, a `β` or
an en dash. A needle containing `µ` would simply fail to resolve — but a needle taken from the
corrupted rendering would resolve *successfully*, to a string the author never wrote.

## A schema limit found here, passed to Plan

`entries[11]` (the Figure 6 diagram) **qualifies** `entries[8]` (the generalisation sentence): the
diagram bounds the scope of the sentence. Written as a `qualifies` pointer, the validator refused
it — correctly on its own terms, because `qualifies` must point at a *text* surface and **rule 5e
makes every locator on an adjudicated article a page crop with `surface: "figure"`**. The
text/panel distinction the relation depends on collapses exactly where page adjudication applies.

It is recorded in prose in the manifest instead. Worth noting that `PMID 17803050`, the only
other fully adjudicated article here, carries **32 entries, all `surface: "figure"`, and not one
cross-entry relation** — the same collapse, unremarked.

Source PDF: `files/fulltext/PMID16061658_Aqeilan2005.pdf`,
`075fdbbcd1e17c3ba1654e78e56ed7345b3e5242ffcf0944f4f6569cf90103eb`.
