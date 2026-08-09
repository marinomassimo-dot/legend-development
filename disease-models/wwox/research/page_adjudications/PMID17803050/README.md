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
| `entries[25]` | `BUN … 12.6 q 4.3 / 40.3 q 3.7c` | **`12.6 ± 4.3 / 40.3 ± 3.7ᶜ`** | `p04_table2_…png` |
| `entries[26]` | `GLU … 169.0 q 26.7 / 145.4 q 26.5` | **`169.0 ± 26.7 / 145.4 ± 26.5`** | `p04_table2_…png` |
| `entries[27]` | `Brain 1426.4 q 45.6 / 1338.3 q 107.2c` | **`1426.4 ± 45.6 / 1338.3 ± 107.2ᶜ`** | `p04_table1_…png` |

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

| file | sha256 |
|---|---|
| `p03_electrolytes_and_BUN_significance.png` | `cdaf28ae2e6eb78e95d467085e6dc1a21859f33f0dacf7c0b3b890e7852a2a74` |
| `p04_table2_BUN_CRE_GLU.png` | `c6df6dd90b50d51ef4f2327ca81ddfe9bf79b217dcd79c2fbc6b4ab3be520ca4` |
| `p04_table1_organ_weights.png` | `b017ee91caa839d98f4d0de790cdd42b1c64127e7a58a03d6d0ddefeec436eb6` |

Source PDF: `files/fulltext/PMID17803050_Suzuki2007.pdf`,
`32c12dbdec988fc2071ac9a493c5be49d16757e89b334a5a80b6f0400e904b69`.

## What remains before the gate lifts

The 24 clean locators still need re-anchoring, and the manifest still declares the refused
`.html` surface. That edit is a canonical write and waits for `BATCH_COMMIT`, which is exactly
what `batch_commit_gate: BLOCK_BATCH_COMMIT` is holding.
