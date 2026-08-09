# 🔴 A deterministic extractor can return characters the author never wrote

**Found 2026-08-09, while reading PMID 33914858 (Repudi 2021, *Brain*) — the source of
`CLAIM 003`, `consolidated baseline`.**

## The fact

`framework`-prescribed extraction (PyMuPDF `get_text()`) returns, from the Methods of that
paper:

> `Results were considered significant when P 5 0.05, otherwise they`

The page **prints** `P < 0.05`. Rendered at 600 dpi from the same PDF, same page, same line:
the glyph is unambiguously `<`.

Across the whole document: **0 occurrences of `<`, `>`, `≤`, `≥`**, against 14 of `P 5 0.0…`.
Other casualties in the same paper:

| Extracted text | What the page prints |
|---|---|
| `P 5 0.05` | `P < 0.05` |
| `fold change 41.5` | `fold change > 1.5` |
| `delta (55 Hz)` | `delta (<5 Hz)` — a frequency band |
| `P-value 50.01` | `P-value < 0.01` |

## Why the obvious check does not catch it

`fitz`, `pdfplumber` and `pypdf` were run independently on the same file. **All three agree**
on `P 5 0.0` and all three report zero comparison characters.

**Cross-checking with a second extractor does not detect this.** They share whatever the PDF's
text layer offers, so their consensus is consensus about that layer, not about the author's
characters.

> 🔴 **Correction, 2026-08-09, same day.** This section first asserted the mechanism as fact —
> "a broken `ToUnicode` CMap maps `<` and `>` to the code points of `5` and `4`". **That was an
> inference stated as a datum, and it is false.** Inspecting the font objects of this PDF:
> **15 of 16 fonts declare no `ToUnicode` at all.** There is no wrong lookup table; there is no
> table, and the extractors are falling back on the internal encoding of subsetted fonts.
>
> A second hypothesis — "low `ToUnicode` coverage predicts unreliable extraction" — was then
> tested and also failed, in both directions: PMID 42397075 has 7/18 fonts with `ToUnicode`
> and extracts **cleanly** (19 correct comparison characters), while PMID 17803050 has 5/6 and
> extracts **corrupt** (`\x1d`). Coverage does not discriminate.
>
> **The mechanism is therefore not established.** The only `DATO` is: *the rendered page and
> the extracted text disagree*, demonstrated at 600 dpi on page 5 of PMID 33914858.
>
> This matters for design, not just for the record: **a guard cannot be built on the cause,
> because the cause is unknown.** It has to be built on the observable discrepancy — which is
> why the detector below is symptomatic, why the general tripwire has to be a surface that
> does *not* read the text layer, and why the rendered page adjudicates.

## Why this is the worst failure class this system can produce

`CLAUDE.md` rule 5c forbids ML converters as a verification surface because they *reconstruct*:
"a quote checked against that output can pass while matching the reconstruction and not the
paper — the gate would report `verified` on a sentence nobody wrote."

That is exactly what happens here, **through the prescribed method**. A locator captured as
`"significant when P 5 0.05"` and verified by `deepdive_manifest` against the declared
`article_text` **matches byte-for-byte and is stamped `verified`**. The artifact is
fingerprinted, the extraction is deterministic and reproducible, every gate is green — and the
sentence does not exist.

The unstated premise was **`PREMISE: DEFAULT_FROM_TEXTBOOK`: "deterministic extraction yields
the author's characters."** Determinism guarantees *reproducibility*, not *fidelity*. A
reproducibly wrong character is still wrong, and it is worse than a random one because it
survives every repetition of the check.

This also lands precisely on the discipline of negatives. This repository has already corrected
`CLAIM 005` over the difference between "no significance marker" and "not significant". A text
layer in which `<` silently becomes `5` destroys the ability to tell `P < 0.05` from anything
else — in the exact papers where thresholds decide whether a finding is a finding.

## Extent, measured

51 local PDFs scanned.

- **1 SUSPECT with the strong signature**: `PMID33914858` (20 hits, 0 comparison characters).
- **A second, different variant, on a canonical source**: `PMID17803050` (Suzuki 2007,
  `PAPER 059`, the primary source of `CLAIM 038` and `CLAIM 039`) renders the glyph as
  `\x1d` — the GROUP SEPARATOR control character: `"were significantly (P \x1d 0.023) lower"`.
  Less dangerous because a control character is visibly broken rather than plausibly numeric,
  but still not the author's character, and still a string that would verify against its own
  extracted text.
- `PMID19936220` (`PAPER 057`) contains no P-thresholds at all, so its zero-comparison count is
  benign.
- 13 further PDFs carry zero comparison characters and are **unverified either way**.

## Consequences to act on

1. **No locator may be taken from `staging/fulltext_text_20260809/PMID33914858.fitz.txt`** as it
   stands. The reading of PMID 33914858 is suspended, not merely incomplete.
2. **PMID 42397075 is clean** — 16 correct `≤`, all three extractors agreeing on the right
   character — so yesterday's twelve locators are unaffected.
3. **The 2026-08-06 readings of `17803050` need an audit** of any locator quoting a threshold.
   The claims themselves (038, 039) may well stand on prose that carries no comparison glyph;
   what needs checking is the quoted strings, not the conclusions.

## The guard this needs

A check that fails closed at extraction time, before a `.txt` may be declared `article_text`:

- a document containing statistical language but **zero** `<`, `>`, `≤`, `≥` is `SUSPECT`;
- any `P\s*[45]\s*0?\.\d+` or control characters in the C0 range outside tab/newline are
  `SUSPECT`;
- a `SUSPECT` text surface may not back a `complete_fulltext_read` until either the affected
  quotes are adjudicated against a **rendered page image**, or the text is repaired and the
  repair declared.

Rendering the page region is the only adjudicating surface, because the drawn glyph is the
author's and the character code behind it may not be. That makes this the textual analogue of
the existing figure rule — a caption is not its figure, and now: **a text layer is not its
page.**

## Reproduction

```bash
# scratchpad scripts used, in order
python3 cmp.py        # three extractors, two PDFs — they agree, and are wrong on one
python3 render.py files/fulltext/PMID33914858_Aqeilan2021.pdf \
        "significant when P 5 0.05" glyph_test.png   # 600 dpi; the page says "P < 0.05"
python3 scan_cmap.py  # corpus-wide signature scan, 51 PDFs
```
