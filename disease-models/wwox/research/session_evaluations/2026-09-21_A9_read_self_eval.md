# Session self-evaluation — the A9 read (2026-09-21)

**Scope.** One full-text read: `PMID 35984507`, main article and supplementary, from
operator-supplied PDFs. Landed as `BATCH_20260921_002`. This file is the self-evaluation the
protocol requires **before** takeaways, and its rule is that *the upgrade is the answer, not the
promise of one* — so each item below either names a shipped change or says plainly that nothing
shipped and why.

---

## 1 · 🔴 The thing that went right, and it is the thing this session kept getting wrong

**The operator handed me a reading and asked what I thought. I checked it before agreeing with it.**

That is the exact discipline this session failed at three times earlier today — a delegate's census
was taken at face value and produced three false statements about this repository, one of which was
**pushed** before it was corrected. Here the operator's reading was **right on every point they
made**, and agreeing without checking would have been indistinguishable from the failure. The
difference is not the outcome; it is that the verification exists and is fingerprinted.

**And the check paid, twice.** It found two things the operator's reading did not contain:

- the **total-WWOX antibody listed in the methods with no total-WWOX result reported**, which turns
  *"the causal attribution is untested"* into *"the pharmacodynamic readout itself is ambiguous"*;
- the **~64 % belongs to the late-intervention arm**, not to the paper as a whole.

## 2 · 🔴 The near-miss, recorded because it is the most instructive thing here

The first term-search I wrote over the extracted PDF returned **`S8G` = 1**.

`S8G` is the inactive Zfra control peptide. A single hit would have meant the specificity control
existed — the opposite of the finding — and it would have gone into the reading, the receipt, the
registry and my answer to the operator. What it actually was: the byte run `s\x128G` inside an
**embedded font program**, matched because my tolerant matcher allowed arbitrary non-word bytes
between characters so that line-wrapped words would still match.

**Three things about this are worth keeping.**

1. **It was caught only because the count was run twice with two different matchers and disagreed.**
   Nothing about the number `1` looks wrong. There is no lexical fingerprint, exactly as with the
   interrogative-to-declarative re-voicing named earlier today.
2. **The first fix did not work and looked like it did.** Replacing non-text bytes with a *space*
   turns `s\x128G` into `s 8G` — and a tolerance built to bridge line wrapping bridges a space
   happily. The hit survived. The real fix is a sentinel the tolerance cannot cross.
3. **A tolerance wide enough to bridge typesetting is wide enough to bridge binary.** That is the
   general lesson and it is now a comment in the tool, not a memory.

**UPGRADE SHIPPED:** `framework/scripts/pdf_text_extract.py` + `test_pdf_text_extract.py` (20
tests). Both the false positive and the failed first fix are regression arms — the failed fix is
asserted *as failing*, so the next person cannot re-introduce it believing it works.

## 3 · The upgrade that made the negatives admissible at all

A text extractor's dangerous output is **zero**, and *"the paper does not contain this"* and *"the
tool did not read this paper"* are indistinguishable from the zero alone. This repository has
already paid for that once (the MCP extractor silently deletes italicised tokens, so italic-class
zero counts were instrument readings).

**UPGRADE SHIPPED:** `pdf_text_extract.py search` **refuses to print any query count** until named
positive controls come back non-zero, and exits non-zero. It is not advice; the negative cannot be
obtained without the control.

**It earned itself immediately, on my own bad input.** I passed `beta-actin` as a control; the
paper spells it `β-actin`, the glyph did not survive extraction, the control read `DEAD`, and the
run refused. The control was wrong, not the tool — which is exactly what the gate is for.

**And it caught a second class of defect I had not anticipated.** The supplementary is a
Word-generated PDF that emits a BCP-47 language tag before every text run, so it extracts as
`WWOXen-US-en-USmitochondria`. Single words match through that; **phrases do not**. Every
phrase-level negative in that file would have been a false negative. Stripped, and the
supplementary's negatives were then re-run with **phrase-level** controls live
(`mitochondrial membrane potential` 3, `caspase 3 activity` 1) before any zero was accepted.

## 4 · What I did NOT do, stated rather than skipped

- **The figure panels were not inspected.** Legends, axis mentions and body text only. `D-14` is
  untouched and both receipts declare `figures: captions_only`. Every negative in the read is a
  **text** negative and is labelled as one. A paper whose central claim rests on blot densitometry
  has a readable layer I did not read.
- **No claim was generated, and that is a decision, not an omission.** The model organism is
  wild-type WWOX in hyperglycaemia; the reference genotype's problem is too little functional WWOX.
  `T3`. The `clinical relevance` on `LIT-0093` was **lowered** `HIGH` → `MODERATE` — a triage value
  set on a title, corrected by the reading.
- **No new gate, workflow, authority layer, registry or mandatory audit.** One tool, routed once,
  with tests. `extraction_damage_report.py` and `legend-locator-audit` remain optional, per the
  operator's instruction of this morning.

## 5 · The honest limit of what was resolved

**`A9` is closed, but it is closed as an ambiguity, not as a result.** The paper does not say
whether total WWOX moves; it *could* have, and did not. So the repository now records *"this cannot
be determined from this paper"* where it previously recorded *"an independent lab confirms WWOX
inhibition is protective"*. That is a better state and a smaller one.

**`REVIVAL_TRIGGER`:** a single measurement — total WWOX protein alongside pTyr33-WWOX under
Zfra1-31 — decides it. That is recorded on `PAPER 097`, on `HYP-20260705-05` and in the read.

## 6 · One process note about the acquisition itself

**`A9` was not unblocked by a better route. It was unblocked by a person sending a file.** Eight
automated tiers, two independent measurements of the PMC stub, and a `HUMAN_ACTION` file were the
correct response to a real blockage — and what solved it was outside the system. What the system
can now do that it could not this morning is **read a PDF once it arrives**, which was previously a
silent dead end: an operator-supplied full text would have stayed unreadable in a deployment with
no PDF toolchain. That gap is closed; the acquisition gap is not, and is not closable from here.

*Nothing in this document is medical advice.*
