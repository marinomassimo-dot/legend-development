# Session self-evaluation — `SLR-scientist-b-0005`

**Actor:** `scientist-b` · **Task:** `AQEILAN-FT-B-001`, wave 5 · **Date:** 2026-09-09
**Scope:** two PMIDs in lot order, each taken M0→M5 and committed before the next —
**27551470** then **25238781**. Both `first_read`; both closed.
**Written BEFORE any closing report**, per the protocol's order of operations.

---

## Part 1 — executable verdicts (run first, not answered)

| Check | Verdict |
|---|---|
| `fulltext_receipts.py verify` | **OK** — 148 chained, tail anchored |
| `deepdive_manifest.py --pmid 27551470 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps, 22 locators / 5 artifacts |
| `deepdive_manifest.py --pmid 25238781 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps, 15 locators / 2 artifacts |
| `session_self_eval.py --disease wwox` | **PASS** — no `[DECLARED GAP]` on either wave-5 PMID |
| `legend_lint.py .` | **PASS** (one pre-existing INFO on CLAIM 010, not mine) |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 |
| `genre_discriminator.py --self-test` | **24/24** |

**One LINT block was raised against my own work and cleared, and it is the most useful line in
this table.** After the 25238781 receipt landed, LINT returned `BLOCK_BATCH_COMMIT:
ORPHAN_COMPLETE_READ` — the paper was completely read and appeared in no structured record. It
was correct: I had written a manifest, a dossier and a commit candidate, and **none of those is a
landing surface**. `FT-089` fixed it. *Bad answer avoided:* treating the block as a formality. A
complete read that no human will stumble across is a read this repository cannot use.

---

## Part 2 — judgement

### Reading (Q1–Q3)

**Q1 — section by section, figures as images, tables?** Yes, on both, and both are small enough
that the claim is cheap to audit. 27551470: 5 sections read sequentially, the single figure opened
as the deposit's own graphic *and* adjudicated on a 400 dpi page render at 300 %, 17 references
enumerated by element, `tables`/`supplementary`/`abstract` `not_present` **by element count**.
25238781: 7,211-character body read sequentially, 11 references enumerated, `figures: not_present`
verified on **two independent surfaces** (0 `<figure>` in HTML; `pdfimages` lists no image on
either PDF page). Nothing was downgraded to `captions_only` because on one paper the pixels were
opened and on the other there are no pixels.

**Q2 — read against the grain of the disease label?** Yes, and on 25238781 that is the entire
yield. The paper is cancer genomics with no WWOX-DEE content, and reading it *for what its
taxonomy does to this repository's question* produced the wave's best finding: the field assigns
human genetic disorders to **rare** fragile sites and cancer to **common** ones, WWOX spans a
common one, and twelve disease terms return **zero** across the body.

**Q3 — what would a keyword search not have returned?** Four things, none keyword-shaped.
(a) The Figure 1 caption of 27551470 declares **Δ** for deletions that are *"positively
selected"* — the driver property — and the panel draws its only Δ over the element it labels
**Passenger**; visible only by opening the image. (b) The same paper's Q-value calibration
**undercuts** its own inference: TP53 is quoted 244 orders of magnitude below WWOX, so the metric
ranks recurrent focal deletion, which the *passive* hypothesis predicts equally well. (c) The
2015 piece's evolutionary argument is supported by a fact that contradicts it. (d) The 25238781
PDF text layer substitutes **seven ﬁ ligatures** — found by a parity check between two surfaces,
invisible to any control-character screen.

### Group and field (Q4–Q7)

**Q4/Q5** — Aqeilan laboratory, `Aqeilan RI[au]` = **137**, `AND WWOX` = **65** (re-measured
2026-09-09, unchanged since 2026-08-10). **Primary for the gene, not for the disease** — and this
wave is the first where that distinction had to be *re-derived rather than reused*, because
neither document reports a measurement. What transfers from an experimental lab to an editorial
is authority over **selection and restatement**, not over observation, and both manifests say so
in `group_assessment.weighting`.

**Q6 — did group standing predict a specific error?** Not standing — **genre** did, and that is
the wave's transferable lesson. Both papers are short opinion pieces by a primary laboratory, and
in both the defect is at the *citation layer*, not in any experiment: an inference transmitted
without its source's interpretive status, a headline dropped, a counter-direction omitted, a
citation pointing where this repository's record does not.

**Q7 — intersection size?** `WWOX AND haploinsufficien*` = **3 records in all of PubMed** — the
entire published field behind an inference 27551470 treats as settled. And
`"Cell Death Discov"[jour] AND (fragile[ti] OR FRA16D[ti])`, **all years** = **1**: the piece is
framed as one side of a controversy and **no counterpoint was ever published there.**

### Epistemic discipline (Q8–Q10)

**Q8/Q9 — shows versus claims.** The whole product. The fidelity test was run mechanically:
all 17 references of 27551470 resolved to PMIDs from the deposit's own elements and joined
against the ledger — **3 complete, 1 partial, 13 absent** — and **all four checkable restatements
changed something**. 🔴 **The denominator is stated in the manifest, the dossier and the receipt:
4 of 17.** *Bad answer avoided:* reporting "the restatements were checked" without saying that
76 % of them could not be.

**Q10 — did I distinguish a defect from an author error?** Yes, twice, and once it reversed a
verdict. The 25238781 "missing sentence" in the PDF was **my comparison's fault**, not the
publisher's: `finally` versus `ﬁnally`. And on 27551470 the `pdfimages` extraction is *larger*
than the published JPEG (1447×1521 against 697×565) and is **not the figure** — a Separation
layer carrying none of the arrows, triangle or X. Taking the bigger image would have been the
natural move and would have hidden every symbol the finding turns on.

### Persistence and horizontal reach (Q11–Q15)

**Q11 — ledger or staging?** Ledger, both, through the validated writer, with `verify` after each.
One writer rejection (`analysis_at` later than `event_at`) was correct and was fixed by using the
real clock, not by loosening the record.

**Q12 — multi-hop?** Yes, and on 25238781 it is the deliverable: **all nine chapters** of the CMLS
71(23) special issue resolved to PMIDs with page ranges, plus all 11 references. Corpus
cross-query: **zero of nine held at any depth.** Seven queue records opened (`FT-089`…`FT-095`).

**Q13 — corpus cross-query?** Yes, and one returned a **reproduction, not a coincidence**: the
twelve-term disease screen returns zero on 25238781 exactly as it did on PMID 24510053 — two
documents, two authors, same result, and now a taxonomic explanation for both.

**Q14 — which existing claim?** `CLAIM 029` (`in observation`). **Not narrowed, not corroborated,
left exactly as open as it was** — because the observation is about a *citation*, and an
editorial's reference list is not evidence for or against a claim. What it yields is a reading
order. **`legend-locator-audit` threshold checked mechanically on both papers and NOT met**; the
check is written into both manifests' `skills_considered` so the non-trigger is auditable.

**Q15 — reading debt into the queue?** Yes — `FT-089` through `FT-095`, led by **`FT-090`
(PMID 25416187, Tabarki)**, the single citation carrying 27551470's only statement about the
reference genotype.

### Capability (Q16–Q19)

**Q16/Q17 — what grew, what broke?** `framework/scripts/genre_discriminator.py`, self-test
**24/24** (see below). Nothing broke. Two generated surfaces **drifted and I did not fix them** —
see Q19.

**Q18 — did a check catch me?** **Three times, and every one improved the output.**
(1) LINT's `ORPHAN_COMPLETE_READ`, above. (2) The manifest validator rejected a 26-character
snippet and an `abstract_snippet` pointing at an article with no abstract — both mine, both right.
(3) 🔴 **The control run on my own new tool.** The first version flagged every ordinary primary
paper as `UNDER_DESCRIBED`, because `research-article` over `Journal Article` is the corpus's most
common case and I had not listed it as uninformative. **The fixtures all passed; only running it
against papers whose genre was never in doubt exposed it.** That is the same shape as this
repository's standing lesson — a plausible predicate that answers a different question — and it
is now a regression.

**Q19 — ranking versus judgement?** One place, and I declined. `coverage_report.md` and
`reading_state.md` are generated files and are now **stale** with respect to both wave-5 reads.
Regenerating them would have been a two-second command and is **exactly what my own wave-4 finding
made policy against**: the generators read the working tree, a peer's untracked manifest
(`PMID26499798.json`) is sitting in it, and regenerating would bake unlanded peer work into a
shared surface under my name. **Reported, not fixed.**

### Substance and provenance (Q20–Q25)

**Q20 — main message and hidden gold.** *27551470:* an editorial that argues the active/driver
case, whose leading statistic cannot discriminate the two hypotheses, whose only reported negative
is absorbed by reframing, and whose figure caption contradicts its own panel on the passenger/
driver assignment. *25238781:* a two-page editor's introduction whose value is entirely
structural — a nine-item queue, a dated statement of what the field was not studying, and the
taxonomic reason its literature is silent about the phenotype this repository models.
**Hidden gold:** the cross-document comparison, which exists **only because both were read in one
wave** — the same senior author reports a question as *concluded* in 2014 and as *debatable* in
2015, citing the same chapter for it.

**Q21 — source parity?** Applied and it changed the weighting twice. Neither paper is primary
evidence; both were read at full depth anyway (rule 1), and both produced findings a triage would
have discarded them before reaching. Conversely, neither was allowed to carry biology: every
summary in 25238781 is recorded as a **pointer**, never as evidence.

**Q22 — team classification?** `experimental_lab`, primary for the gene, not for the disease — and
in both manifests I recorded *why that classification does not transfer to these documents*, since
neither reports what the laboratory can produce.

**Q23 — skills used and declined.** Used: `legend-study-intake-triage` (M0 per paper),
`legend-session-self-eval` (this document). Declined with reasons that would survive review, in
both manifests: `find-fulltext` (the cascade was run by hand and is recorded — the *absence* of an
XML surface on 25238781 is a declared result, not a silence), `legend-locator-audit` (threshold
checked, not met), `legend-discovery`, `legend-proband-priority-matrix`, `legend-hypothesis-forge`,
`legend-safety-triage`. 🔴 **`legend-discovery` was declined on the evidence and the reason is the
wave's principle:** mining a citation layer produces leads attributed to a document that belong to
its sources.

**Q24 — where did output land?** Six durable surfaces: two manifests, two dossiers, two commit
candidates, the receipt ledger, the full-text queue, and one new script — plus this evaluation.

**Q25 — can the next run answer mechanically?** Yes. Both receipts name a local fingerprinted
artifact whose digest matches; on 27551470 **both** figure surfaces are md5-identical to the values
the article's own XML declares for them, which is provenance the deposit itself vouches for.

### Friction and transferable delta (Q26–Q27)

**Q26 — friction.** Four items, all small and all correct: a 503 loop on a non-open-access
`fullTextXML` endpoint (resolved into a *recorded absence* rather than a retry); a PMC CDN 404 on
the PDF (resolved by the Europe PMC render route, then **verified against the md5 the deposit
declares** rather than trusted); two validator rejections; one LINT block; two queue-entry format
warnings whose messages said exactly what to change.

**Q27 — transferable capability delta.** Disease-agnostic and gene-agnostic — see below.

---

## The micro-upgrade — `framework/scripts/genre_discriminator.py`

**Earned in one wave, not imagined.** Publication-type metadata was wrong on **both** wave-5
papers, in **opposite directions**:

| PMID | What it is | PubMed | PMC | Direction |
|---|---|---|---|---|
| 27551470 | editorial, 17 refs | `Journal Article` | `editorial` | **under**-describes |
| 25238781 | 2-page editor's introduction | `review-article, Review, Journal Article` | `review-article` | **over**-describes |

A triage that routes on `pubtype` mis-weights both, and **neither failure produces an error to
notice**. The tool compares the declared label against cheap discriminators the deposit already
carries — page span, reference count, figure count, abstract presence, section count, and the
received/accepted date pair — and reports **disagreement**.

**What it refuses to claim** is written into the module: it does **not** determine genre. Nothing
can; genre is an editorial fact. A verdict is a reason for a human to look.

🔴 **The design rule is my own wave-4 finding, applied to my own new code: a screen whose failure
mode is a silent pass is worse than no screen.** So a discriminator that could not be measured
returns `INSUFFICIENT_DATA` **naming what is missing** — never `AGREES`. PMID 27551470 forced it:
its deposit carries `fpage 15040` and an **empty** `lpage`, so its page span is unobtainable, and
the tool must say so while still catching the disagreement it *can* see.

**Verified rather than asserted, on three axes:**

1. **Both real cases caught**, in the correct opposite directions, from their own fingerprinted deposits.
2. **Silent on four genuine primary papers** — 20530675, 21115974, 18674750, 15070730 — after the
   control run exposed a false positive that all the fixtures had passed.
3. **The HTML reference count is verified against ground truth this repository established
   independently**: the broadened pattern reproduces **48** (18674750), **42** (21115974) and
   **11** (25238781) exactly, each a number another reading arrived at on another day without it.
   The rule is recorded in the code: a count is adopted only when it reproduces one of those.

**Self-test 24/24**, including the false-positive regression and all three PMC reference-markup
vintages.

---

## What I would do differently

**Read the two papers in this order again — but say earlier that they are a pair.** The
cross-document finding of §4 of the 25238781 dossier only became visible at the second paper, and
I nearly wrote the first dossier as if it stood alone. The dispatch grouped them as "the
fragile-site review layer" and that grouping turned out to be the substance, not the convenience
it looked like. **A lot whose members cite each other should be read as a set and said to be one
at M0**, not discovered to be one at M5.
