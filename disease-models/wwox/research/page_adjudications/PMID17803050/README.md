# Page adjudication — PMID 17803050 (Suzuki 2007, *Comparative Medicine*)

The text surface of this paper is `SUSPECT` and refused by
[`deepdive_manifest.py`](../../../../../framework/scripts/deepdive_manifest.py): its PDF text
layer carries 34 C0 controls plus roughly 145 printable substitutions. It cannot back a
locator. **The rendered page adjudicates**, because the drawn glyph is the author's and only
the character code behind it is in doubt.

This is road 3 of three: re-anchor the affected locators to the page rather than re-derive the
whole surface. Road 1 (another copy of the PDF) is expected to fail — the corruption is a
property of the font subsetting of this typesetting, so any copy of the same setting carries
it identically. Road 2 (rebuilding the whole surface from the rendering) is worth it only when
someone reopens the paper in full; as the primary source of `CLAIM 038` and `CLAIM 039`, that
will happen.

## Scope, measured rather than assumed

The 29 text locators of this reading were placed against the printed pages: **29 placed, 0
unplaced, across 5 pages**. Only **5** have corruption *inside* the quoted span. The other
**24** are clean within their own quote and need re-anchoring only — their characters were
never in doubt, they are collateral damage from the surface being refused whole.

| page | locators | corrupted inside the quote |
|---:|---:|---:|
| 2 | 6 | 0 |
| 3 | 2 | **2** |
| 4 | 3 | **3** |
| 5 | 3 | 0 |
| 8 | 15 | 0 |

## The five, adjudicated at 500–600 dpi

The text is vector, so no resolution ceiling applies — unlike the figures, where the ceiling
rule holds and above it you are enlarging rather than looking.

| locator | text layer says | the page prints | artifact |
|---|---|---|---|
| `entries[0]` | `significantly (P \x1d 0.05) higher` | **`significantly (P < 0.05) higher`** | `p03_…png` |
| `entries[1]` | `(Ca2\x0c, Na\x0c, K\x0c, and Cl–)` | **`(Ca²⁺, Na⁺, K⁺, and Cl⁻)`** | `p03_…png` |
| `entries[25]` | `BUN … 12.6 q 4.3 / 40.3 q 3.7c / 10.1 q 2.7 / 35.6 q 12.8d` | **`12.6 ± 4.3 / 40.3 ± 3.7ᶜ ‖ 10.1 ± 2.7 / 35.6 ± 12.8ᵈ`** | `p04_table2_…png` |
| `entries[26]` | `GLU … 169.0 q 26.7 / 145.4 q 26.5 / 155.0 q 30.1 / 157.4 q 38.9` | **`169.0 ± 26.7 / 145.4 ± 26.5 ‖ 155.0 ± 30.1 / 157.4 ± 38.9`** | `p04_table2_…png` |
| `entries[27]` | `Brain 1426.4 q 45.6 / 1338.3 q 107.2c / 2254.2 q 274.7 / 4542.0 q 1375.3e` | **`1426.4 ± 45.6 / 1338.3 ± 107.2ᶜ` (absolute) ‖ `2254.2 ± 274.7 / 4542.0 ± 1375.3ᵉ` (relative)** | `p04_table1_…png` |

`‖` separates the two column groups: *Female rats* from *Male rats* in Table 2, and
*Absolute (mg)* from *Relative* in Table 1. Both are visible in the images.

Mappings confirmed on the page: `U+001D` → `<`, `U+000C` → superscript `⁺`, `–` → superscript
`⁻`, `q` → `±`. These match the substitution map independently established across the corpus.

**Two locators cost one render.** `entries[0]` and `entries[1]` are adjacent sentences in the
same column, so a single 500 dpi crop adjudicates both. Renders are per page region, not per
locator — which is why the cost of this road is five renders and not twenty-nine.

## 🔴 The adjudication CONFIRMS the science

Not one of the five changes a value, a direction or a significance verdict. BUN is still
roughly 3.2× higher, glucose is still unchanged, brain weight still shows the sparing
arithmetic, and the significance is still `P < 0.05`. **The defect was in the evidence chain,
never in the facts.** `CLAIM 038` and `CLAIM 039` stand exactly as written; what was missing
was the repository's ability to prove them, and these three images restore it for the five
quotes where the proof had been lost.

## A method note worth keeping

The first render of `entries[0]` used the needle `significantly (P` and landed on a
**different sentence** on page 2 — "average body weights were significantly (P < 0.05) lower".
Both sentences are real, both carry the same corruption, and the wrong one would have
adjudicated the right character for the wrong locator. This is the `find()` first-occurrence
hazard documented in `_quote_matches`, met in practice within minutes of writing it down.
**Adjudicate on a needle unique to the locator**, not on the fragment that happens to contain
the corrupted character.

## Artifacts

| file | crop (page 4, PDF points) | sha256 |
|---|---|---|
| `p03_electrolytes_and_BUN_significance.png` | p3 `(300, 630, 580, 690)` @600 | `cdaf28ae2e6eb78e95d467085e6dc1a21859f33f0dacf7c0b3b890e7852a2a74` |
| `p04_table2_BUN_CRE_GLU.png` | `(40, 480, 570, 562)` @500 | `9b2268e2d64658b113b3a45e09e93d308ec0d2639004d138012eba46f62fe90b` |
| `p04_table1_organ_weights.png` | `(40, 62, 570, 250)` @400 | `98ebfb5061b258104c56687279b10f0c4b9220a143b3ccba3f50f5a4a2ba031e` |

### 🔴 Correction, same day — the first two table crops did not contain their own span

The originals were `Rect(40, 505, 320, 560)` and a matching narrow band. The BUN row extends
to **x ≈ 524**: `12.6` sits at x=191 and `35.6` at x=510. Four values that are *inside* the
quoted spans of `entries[25]` and `entries[26]` — the whole male-rat half of both rows — fell
outside the image. **A locator anchored to that artifact would have been verified against
pixels that were not there.**

Adjudicated separately, the missing values are all `±` and no number or direction changes, so
the finding below stands. But the artifact promised more than the proof it carried, which is
the same defect class as everything else this week, committed while documenting that defect
class. Found by an independent reviewer, not by me.

Both crops now include the full row width **and the column headers**, so each image explains
itself: Table 2 shows `Female rats` / `Male rats` over `Normal` / `Mutant`, and Table 1 shows
`Absolute (mg)` / `Relative` over the same pair — which is what makes `entries[27]`'s
absolute-versus-relative proposition readable from the image alone rather than only from the
locator's anchor text.

**The general rule this earns:** *an adjudication artifact must contain the entire span it
adjudicates.* Unlike most of what this repository checks by argument, this one needs no
reader — the crop rectangle against the span rectangle, both already in hand.

**Implemented** as `deepdive_manifest.crop_contains_span`. All three artifacts above pass:

| locator | crop | verdict |
|---|---|---|
| `entries[0]`, `entries[1]` | p3 `(300, 630, 580, 690)` | ✅ contained |
| `entries[25]`, `entries[26]` | p4 `(40, 480, 570, 562)` | ✅ contained |
| `entries[27]` | p4 `(40, 62, 570, 250)` | ✅ contained |

🔴 **A design constraint the check surfaced immediately, and it is the same lesson twice in one
day.** Containment is only meaningful against *the right span*. The first verification run
reported `p03` as OUTSIDE — because `search_for("significantly (P")` returns hits in **both
columns**, and the left-column occurrence lies outside the crop. The crop was correct; the
needle was ambiguous. Two of the five needles here still return more than one hit.

So when the 24 are re-anchored, the check cannot take a bare quote fragment: **each image
locator must carry a needle unique on its page**, or the span it resolves to is a guess. That
is the `find()` first-occurrence hazard for a third time — in `_quote_matches`, then in the
first render of `entries[0]`, now in the containment check itself. Three different mechanisms,
one root: *a quote fragment does not identify a location.*

Source PDF: `files/fulltext/PMID17803050_Suzuki2007.pdf`,
`32c12dbdec988fc2071ac9a493c5be49d16757e89b334a5a80b6f0400e904b69`.

## What remains before the gate lifts

The 24 clean locators still need re-anchoring, and the manifest still declares the refused
`.html` surface. That edit is a canonical write and waits for `BATCH_COMMIT`, which is exactly
what `batch_commit_gate: BLOCK_BATCH_COMMIT` is holding.
