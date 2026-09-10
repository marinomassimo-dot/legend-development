# Actor retrospective — 2026-09-09 Aqeilan free-full-text sweep

**Analyst:** `analyst-retro` · **Date:** 2026-09-09 · **Subjects:** `scientist-a`, `scientist-b`,
`scientist-c`, `orchestrator` · **Scope:** the 23-PMID sweep of task contracts `AQEILAN-FT-A-001`,
`AQEILAN-FT-B-001`, `AQEILAN-FT-C-001`, eleven waves across one calendar day.

**Purpose.** This document exists to make the Scientists better. It is not a narrative of the
sweep — [`2026-09-09.md`](2026-09-09.md) already is one, and its § 7 records what the three lots
returned. What follows is the error record: what went wrong, what nearly went wrong, **which
control actually caught it**, and what a later session can measure to know whether the fix worked.

**It is written from artefacts, not from memory or from anyone's report.** Every incident below
names the file it is drawn from. Where the record and a prior summary disagree, the record wins,
and § 0.3 lists the three places where that happened.

**Analyst scope.** Read-only toward every actor's manifests, dossiers, receipts and task contracts;
no scientific current file, no `BATCH_COMMIT`, no receipt-schema change, no push. The proposals in
§ 9 are proposals.

---

## 0 · Method, and what this census can and cannot see

### 0.1 · Sources

| Source | What it supplied |
|---|---|
| `research/session_evaluations/2026-09-09_*.md` (9 files) | the actors' own failure enumerations and attributions — the richest source by a wide margin |
| `learning/scientist-b/SLR-scientist-b-0002.md` | `scientist-b`'s wave-1 diagnosis, which lives outside `session_evaluations/` and is the only record of the sweep's most instructive near-error |
| `research/deepdive_manifests/*.json`, `research/fulltext_dossiers/*.md`, `research/commit_candidates/*.md` | the primary evidence for each incident; audit notes; declared gaps |
| `ledger/tasks/scientist-{a,b,c}/AQEILAN-FT-*-001.json` | wave results, interruptions, self-imposed targets, `not_mine` declarations |
| `git log` 2026-09-08→2026-09-10, message bodies | unusually informative in this repository; the source for four incidents recorded nowhere else |
| [`2026-09-08.md`](2026-09-08.md), [`2026-09-08_scientist_brief.md`](2026-09-08_scientist_brief.md), [`2026-09-09.md`](2026-09-09.md) | the dispatch, the standing brief the actors were graded against, the resume record |
| `framework/protocols/session_self_evaluation.md` | the standard the diagnoses are written against |

### 0.2 · The counting rule, stated so the ratio in § 5 is reproducible

An **incident** is one defect or near-error that an actor enumerated in its own diagnosis, or that
an artefact records against an actor. Repeated instances of one rejection class inside one wave
(e.g. "the validator rejected my locator design four times") count as **one** incident, with the
instance count carried in the text. A **catcher** is classified as:

- **machine** — a validator, writer, linter, screen, test suite, HTTP status or shell error;
- **blind auditor** — `legend-locator-audit`, run blind on (proposition, quote, anchor) triples;
- **peer/coordinator** — another actor or the orchestrator;
- **self** — the actor's own re-reading, cross-measurement, control run, or refusal to believe a
  result it had not earned.

### 0.3 · 🔴 The census's own blind spot, stated first because it bounds everything after it

**This census is built from the actors' own enumerations, so an error nobody caught appears in no
list.** The ratio in § 5 measures *how errors that were caught were caught* — it does not and
cannot measure the undetected rate. Three independent facts show the floor is not zero:

- `scientist-a` wave 3 committed a cross-panel bridge that was wrong on a fact in a sentence it had
  itself quoted two hours earlier; the audit caught it, and the audit was run only because a
  `consolidated baseline` claim was in scope. On the majority of this sweep's readings **the R4
  threshold was checked and not met**, so no blind auditor ever looked.
- `scientist-b` wave 2's `F3` (a manifest naming four queue IDs belonging to other papers) passed
  `STRICT` and would have stayed passed: *"Nothing in `deepdive_manifest.py` checks that a
  `multihop.queued[].queue` identifier exists or names the same PMID, so a manifest can point at
  another paper's debt and every gate stays green."*
- `scientist-c` wave 3's inverted screen call: *"Nothing in the repository would have caught this."*

**Corrections made to the working summary while building this census** — each verified against the
artefact, none taken on trust:

1. The near-error described as a figure read "at 667px that was right at 400 dpi" is real and is
   `scientist-b`'s, wave 1, PMID 29724996 Figure 6A — **not** a figure-audit incident of the kind
   § 1 collects, and **caught by the actor's own judgement, not by a machine**. § 2.1.
2. `erratum_scope_check.py` is `scientist-b`'s file (`ce7f89a`), the crash was surfaced by
   `scientist-c`, and it **was repaired the same day by the orchestrator** in `0e33f0f` — the record
   is not an open defect but a closed one, and the closure carries the more useful lesson (§ 4.2).
3. The record documents **three session terminations, all three attributed to rate limits**
   (`scientist-a` wave 2, `scientist-b` wave 3, `scientist-c` wave 2), plus a **fourth** rate-limit
   event that killed two blind auditors without killing the session. **No artefact in this
   repository describes a process exit**, and this analyst did not manufacture one. § 6.4.

---

## 1 · `scientist-a` — `AQEILAN-FT-A-001`

**Lot:** 8 PMIDs · **Closed:** 5 at `complete_fulltext_read` · **Held:** `33914858` (acquisition,
19-tier lawful cascade exhausted), `25331887` and `34268881` (schema — coverage of cited-but-
undistributed material). **Waves:** 4, of which wave 2 was killed by a rate limit and produced no
self-evaluation.

### 1.1 · Errors and near-errors

| # | Incident | Caught by | Artefact |
|---|---|---|---|
| A1 | Strict validator returned **22 BLOCKs** on arrival — the checkout held no evidence bytes | machine | wave-1 eval |
| A2 | Receipt writer rejected `analysis_at` later than `event_at` (clock error, recurs in wave 3) | machine | wave-1, wave-3 evals |
| A3 | A locator snippet below the 30-character minimum | machine | wave-1 eval |
| A4 | 🔴 **`DUPLICATE_QUEUE_ID` on its own `FT-044` heading — already committed.** Would have made every existing reference to `FT-044` ambiguous | machine (`legend_lint.py`) | wave-1 eval |
| A5 | 🔴 **Wording overshoot in a draft locator:** wrote that the WT-vs-rescue comparison was *"untested"* for TBR1 and SATB2, when the legend's all-pairwise Tukey test means **tested and not significant** | blind auditor | `PMID34268881.json` entries[14], anchor records the correction |
| A6 | `pdftotext -layout` **spliced two columns across the gutter** | self, before quoting | wave-3 eval |
| A7 | Manifest validator rejected the first locator design **four times** (needle collisions from one snippet reused across three locators; a relation not in the enum; a panel pointing at another panel; two needles under 30 chars) | machine | wave-3 eval |
| A8 | `regenerate_adjudications.py` rejected **all 9** adjudication digests (rendered from the unrounded rect, stored the rounded one) and flagged 2 non-unique needles | machine | wave-3 eval |
| A9 | 🔴 **The wave's most attractive finding, built, written into a manifest and committed:** a Fig 6 → Fig 5 cross-panel bridge that **fails on cell line** (NIH 3T3 vs SAOS-2) — a fact in a sentence the actor had itself captured as a locator two hours earlier | blind auditor (7 of 13 triples corrected) | wave-3 eval |
| A10 | An undeclared assumption forced into the open: **Fig 5 has no caption**, so *which panel is the reduced dose* is an assumption, not a datum | blind auditor | wave-3 eval |
| A11 | 🔴 **Background knowledge standing in for a source:** identified Figure 2A's markers as known phosphorylation sites; the article names **one** phosphosite and residues 12, 14 and 33 appear nowhere in its prose. `DEFAULT_FROM_TEXTBOOK` used without declaring it, forbidden by `scientist_reading_modes.md` § 3.3 | **both** blind auditors, independently | wave-4 eval |
| A12 | 🔴 **Two field-density counts written from expectation, and a false sentence built on one:** Zfra as 2 (it is **13**), Alzheimer as 36 (it is **32**) | **self**, re-measuring before shipping | wave-4 eval; commit `a387bf1` |
| A13 | 🔴 **A PMID taken from an external search while the identifier sat inside the artefact:** gave ref 1 as `29581896` where the deposit's own `ext-link` markup carries `29310447` — a different paper entirely | **both** blind auditors, independently | `PMID31428585.json` audit_note; commit `ef02e94` |

### 1.2 · The pattern the actor named itself, and why it is the durable finding

Wave 3 diagnosed the failure as *appeal-driven under-scrutiny*: **"the finding I most want to be
true is the one to re-derive from the source before writing it."** Wave 4 then met that target —
the Figure 2B genotype work was checked first and hardest and *"survived two independent
recomputations from the pixels, tick position by tick position"* — **and every error of wave 4 came
from somewhere else.** The actor's own conclusion:

> **"These are one failure, not three: an assumption asserted with the confidence of a measurement,
> in a place too small to look at twice."**

That is a better generalisation than the wave-3 one, because it covers A11, A12, A13, and also A5
(a legend convention assumed rather than read) and A9 (a cell line assumed rather than re-checked).
**The target that follows is the actor's own and should be adopted verbatim as a standing rule:**
*before a locator carries an identifier, a count or a residue identity, the value must come from the
artefact or from a command run in this session — never from recall, and never from the first hit of
a search.*

### 1.3 · The two things this actor got structurally right

- **Ordering under session mortality.** A rate limit killed two auditors mid-run in wave 4. The
  actor landed the *reading* first — manifest, receipt, dossier — and wrote **no commit candidate**
  until verdicts existed, *"on the reasoning that a landed reading with no commit candidate touches
  no claim."* Nothing had to be reconstructed on resume. Wave 2 had lost an audit to a session
  boundary and shipped ten locators marked `[UNAUDITED]` with the candidate HELD; wave 4 lost a
  harder failure and lost nothing. **This is a procedural repair with a measurable before/after and
  it should be policy.**
- **Correcting a persisted wrong value lawfully.** A13's bad PMID sat in an append-only ledger and
  was fixed by a linked `receipt_correction` (`FTR-20260909-31428585-02`), never by editing the
  JSONL.

### 1.4 · The audit's best output was not an error

Both auditors independently found a **second** unsupported forward clinical claim in PMID 31428585
that none of the actor's locators covered — *"Furthermore, blocking the downregulation of WWOX in
the middle aged individuals would likely to prevent the development of AD"* — weaker than the one
the reading was built on, because it carries **no attribution at all** where the first at least
names a personal communication. The reading's headline changed shape from one unsupported clinical
claim to two.

> **"A reading is not only judged by whether its propositions are true, but by whether the document
> contains something worse that it walked past."**

**This is the strongest argument in the whole record for keeping blind audits expensive and for
running them on omission as well as on error.** Two auditors, working from triples alone, found
something no gate in this repository can look for.

---

## 2 · `scientist-b` — `AQEILAN-FT-B-001`

**Lot:** 8 PMIDs · **Closed:** 7 at `complete_fulltext_read`, 1 at `partial_fulltext_read` by
declared downgrade (`20146584`, two NIHMS figure images behind a reCAPTCHA) · **Waves:** 6, of which
wave 3 was terminated by a rate limit after the reading and before any manifest existed.

### 2.1 · 🔴 The sweep's most instructive near-error, and it was caught by nobody but the reader

`learning/scientist-b/SLR-scientist-b-0002.md`, wave 1, PMID 29724996 Figure 6A:

> **"I was about to file a false correction against a correct locator.** Reading Fig 6A at the
> 667 px PMC rendering I made the counts ~14 vs ~1 of ~15 and began drafting a correction to
> `entries[21]`, which asserts 11/12 vs 4/18. At 400 dpi the bars resolve as stacked **by genotype
> within each outcome category** and the existing locator is **exactly right**. What caught it was
> the rule that a figure is inspected at original resolution — applied *before* contradicting an
> existing locator, not after. **Grade for my own first pass here: `failed`.** The near-miss is the
> most important thing in this batch, because the wrong edit would have been confident,
> well-argued, and would have passed every gate this repository owns."

The receipt `FTR-20260909-29724996-01` carries the mechanism: the PMC assets are 667–800 px wide,
the bar charts are **vector art in the publisher PDF**, so rasterising the page at 400 dpi resolves
them arbitrarily crisply. At 400 dpi: tumour-free = control 14 + cKO 1; liver-tumours = control 4 +
cKO 11 — i.e. control **4/18**, cKO **11/12**, exactly what the existing locator said.

**Why this is the most instructive incident in the sweep.** Every property that makes an error
survivable was absent. It would have been an *edit to an existing correct canonical locator*, made
by the actor best placed to make it, argued from pixels, and it touched no `consolidated baseline`
claim — so `legend-locator-audit` **did not trigger** and no blind auditor was ever in the loop.
The only thing between it and the ledger was a procedural rule the reader chose to apply in the
right order. **A repository whose deepest control is "the reader remembered the rule" has a control
gap at exactly the point where an actor is most confident.**

### 2.2 · Errors and near-errors

| # | Incident | Caught by | Artefact |
|---|---|---|---|
| B1 | The Fig 6A false correction, above | **self** (procedural rule, applied in the right order) | `SLR-scientist-b-0002.md`; receipt `FTR-20260909-29724996-01` |
| B2 | Validator refused the first supplement text surface (`U+000C` at offset 1500); re-derived with `pdftotext -raw -nopgbrk`, **not stripped** | machine | wave-1 eval |
| B3 | Receipt writer rejected `analysis_at` twice | machine | wave-1 eval |
| B4 | **A commit message lost a clause to shell backtick expansion.** Not amended — history rewrite is reserved. Remaining messages avoided backticks | self | wave-1 eval |
| B5 | 🔴 **A structural fact asserted from indirect evidence:** concluded and wrote that *"the supplementary figures are not in this PDF — only legends"* from per-page text lengths. `pdfimages -list` then showed **16 image XObjects on pages 4–7** — sliced into strips by Word→PDF. *"Distance from a false negative: one command."* | **self**, one step later | wave-2 eval (F1) |
| B6 | Five coupled locators carried the panel-relation marker on the **text** side — the opposite of the rule the actor had read in full **that same session** | machine (`deepdive_manifest.py`) | wave-2 eval (F2) |
| B7 | 🔴 **A manifest passed `STRICT` while naming four queue IDs belonging to other papers** (`FT-072`–`FT-075`, all live entries about unrelated papers; `FT-071` is this paper's own). No gate covers this | **self**, by an independent grep of the queue *after* `STRICT` had passed | wave-2 eval (F3) |
| B8 | Strict validator refused an entry carrying `qualifies` without a `qualifies_needle` | machine | wave-4 eval |
| B9 | 🔴 **`multihop.performed` flipped `false`→`true` while wave 4 performed no new multi-hop work.** *"The validator checks that the key exists, never that its value is earned"* | **self**, in the self-evaluation, before any closing report | wave-4 eval (Q12) |
| B10 | A stale "55 entries" sentence sitting two fields below the corrected `73` | self | wave-4 eval |
| B11 | LINT `BLOCK_BATCH_COMMIT: ORPHAN_COMPLETE_READ` — a completely-read paper appearing in no structured record. *"I had written a manifest, a dossier and a commit candidate, and none of those is a landing surface"* | machine | wave-5 eval |
| B12 | Validator rejected a 26-character snippet and an `abstract_snippet` on an article with no abstract | machine | wave-5 eval |
| B13 | 🔴 **The actor's own new tool flagged every ordinary primary paper as `UNDER_DESCRIBED`.** *"The fixtures all passed; only running it against papers whose genre was never in doubt exposed it"* | **self**, by a control run | wave-5 eval |
| B14 | A "missing sentence" in a PDF attributed to the publisher was **the actor's own comparison's fault**: `finally` versus `ﬁnally` | self, by a two-surface parity check | wave-5 eval |
| B15 | The `pdfimages` extraction of a figure is *larger* than the published JPEG (1447×1521 vs 697×565) and **is not the figure** — a Separation layer carrying none of the arrows, triangle or X. *"Taking the bigger image would have been the natural move and would have hidden every symbol the finding turns on"* | self | wave-5 eval |
| B16 | 🔴 **Nearly accepted a `REFUSED` verdict without asking what it was refusing for.** The refusal fired on 8 harmless front-matter separators and on suspicion-by-absence, while `PRINTABLE_SUBSTITUTIONS` matched the actual genotype corruption **with nothing** | **coordinator's mid-task instruction** | wave-6 eval; commit `1e12c82` |
| B17 | Nearly recorded `figures: read` on `20146584` by genre analogy with the sibling paper read hours earlier | self, refused; took the `partial` downgrade | wave-6 eval; `PMID20146584.json` `unretrievable_debt` |

### 2.3 · The pattern

This actor's failures are **not** reading failures; every one of B5–B17 is a failure of a
*declaration about the reading* — a coverage claim, a flag, a queue ID, a relation side, a screen's
verdict. Its own wave-2 formulation is the sharpest in the record:

> **"Reading a rule is not the same as having applied it, and this is the second consecutive wave in
> which a check, not the reader, enforced a rule the reader had just read."**

And its wave-6 generalisation is the one worth propagating repository-wide:

> **"'The gate said no' is not a finding; 'the gate said no because X' is."**

This actor also produced the sweep's clearest evidence that **the unit of work is the lot, not the
paper**: a growth-phenotype contradiction inside PMID 25245215 that could not be adjudicated (the
corpus cross-query returned 0 hits over 9 terms and 2 artifacts) was **closed four hours later by
the next paper in the same wave**, PMID 20146584 — *"not because I went looking, but because the
debt was specific enough that the answer was recognisable when it appeared in an unrelated sentence
about mouse pups."*

---

## 3 · `scientist-c` — `AQEILAN-FT-C-001`

**Lot:** 7 PMIDs · **Closed:** 7 of 7, plus one paper outside the lot read and receipted because
reading a full text obliges a receipt (`28373548`, the expression of concern on `16223882`) ·
**Waves:** 4, of which wave 2 was terminated by a rate limit and produced no self-evaluation (its
obligation was discharged in wave 3).

### 3.1 · 🔴 The screen that returned CLEAN without screening anything

Wave 3, and the actor's own account is the best statement of the failure class this repository
keeps rediscovering:

> "I called `_refuse_suspect_surface(text, path_string)` — **arguments inverted**. It returned
> normally. `path` is not touched before the loop, so the loop screened the *filename*, which holds
> no control characters, and I read the silent return as CLEAN. The surface I was actually asking
> about — the PMID 16223882 PDF text layer — carries **191 C0 controls and zero comparators**, and
> the correct call refuses it.
>
> **Nothing in the repository would have caught this.** I caught it only because I had separately
> counted the raw characters, saw `<`, `±`, `×`, `β`, `μ` all at zero in a paper that prints
> `P < 0.05` and `β-actin`, and refused to believe a screen that called that clean. Had I trusted
> the green, I would have declared a SUSPECT surface as `article_text` and anchored twelve text
> locators to characters no author wrote — the exact false positive rule 5c calls the worst class
> this system can produce, **and it would have worn the badge of having been checked.**"

Two properties make this the most severe near-error of the sweep:

1. **It retro-invalidated an already-reported result.** *"It also means my earlier 'supplement text:
   CLEAN' result for 41562193 was meaningless when I reported it."* That paper survived only because
   the authoritative screen also runs inside `deepdive_manifest.py` at write time — i.e. **by
   defence in depth, not by the check the actor ran**.
2. **The lesson the actor drew is the right one and is not "be careful":** *"my check asserted
   nothing and I reported it as though it had."*

The micro-upgrade shipped in response is proportionate and mutation-tested: an argument-shape guard
plus `test_suspect_surface_call_shape.py` (9/9), where disabling the `PathLike` check turns exactly
the two inversion cases red and leaves the other seven green.

### 3.2 · Errors and near-errors

| # | Incident | Caught by | Artefact |
|---|---|---|---|
| C1 | Europe PMC `fullTextXML` **404** on both wave-1 papers; PMC `/bin/` 404; PMC article page returned a reCAPTCHA | machine (HTTP status), recorded as **surface facts** (`FT-077`), not routed around | wave-1 eval |
| C2 | Receipt append rejected: `analysis_at` later than `event_at` (recurs in wave 3) | machine | wave-1, wave-3 evals |
| C3 | 🔴 Receipt append rejected: **`conflicting identifiers for the same study`** — the writer refused the actor's **correct** DOI because a prior receipt had persisted a **wrong** one. The actor refused to write the falsehood to satisfy the check | machine (and the actor's refusal) | wave-1 eval; § 6.3 of [`2026-09-09.md`](2026-09-09.md) |
| C4 | Commit wrapper failure from the actor's **own** unescaped inner double quotes | machine (the shell); `git status` confirmed nothing staged | wave-1 eval |
| C5 | `research_type` rejected against its enum; `source_fulltext_indexed_evidence` field name wrong | machine | wave-1 eval |
| C6 | Character-fidelity mismatch: a candidate snippet used `µ` (U+00B5) where the artifact holds `μ` (U+03BC) | **self**, by pre-verifying every snippet against the validator's own extractor before writing the manifest | wave-1 eval |
| C7 | 🔴 `pdftotext -layout` on a **two-column** article interleaved the columns and **injected the page number `588` into the middle of the sentence carrying the headline claim** | **self**, by comparison against the rendered page — *"a human act that does not scale, which is exactly why it became this session's micro-upgrade"* | wave-1 eval |
| C8 | Multi-hop debts recorded in the manifest and dossier only — **prose, not the queue** | self, and **fixed inside the evaluation** rather than promised (`FT-075`/`FT-076`) | wave-1 eval |
| C9 | Group publication counts **137/64 carried forward from a 2026-08-11 measurement**, not re-derived, in a field-density-sensitive slot | self, graded `partial`; **debt closed in wave 3** (today's measurement: 137/65) | wave-1 and wave-3 evals |
| C10 | The inverted screen call, § 3.1 | **self**, by disbelieving a green result | wave-3 eval |
| C11 | `_xml_surfaces` returned nothing — the regex was `<body>` and the deposit writes `<body id="…">` | self, by the assertion failing rather than by a wrong answer | wave-3 eval |
| C12 | Figure 2 colour segmentation attributed 13 px of the **plot frame** to a signature in every column; Figure S1 legend-box border `(213,213,213)` mistaken for a swatch `(184,184,184)` | **self**, by arithmetic disagreement with printed panel totals | wave-3 eval |
| C13 | Figure S1 baseline set at the x-axis **labels** (y=1992) instead of the axis (y=1574) | **self** — every bar came out at ~25 mutations, contradicting the visual read | wave-3 eval |
| C14 | Receipt refused: `first_read cannot name prior_receipt` **and** `prior_receipt is null and this study already has 1 receipt(s)` | machine | wave-3 eval |
| C15 | Manifest refused twice: `gene_direct_refs_in_source: must be a list`; two snippets under 30 characters | machine | wave-3 eval |
| C16 | Adjudication crops: **5 of 12** digests regenerated differently (rendered from the unrounded rect, stored the rounded one); **8** needles refused as non-unique | machine (`regenerate_adjudications.py`) | wave-3 eval |
| C17 | 🔴 **The task contract's own acquisition hint was false** (`pmcid: null`, `free_sites: []`), and both the 2026-09-08 pre-flight and Europe PMC agreed with it. NCBI `idconv` returns `PMC11159152` | **the repository's own memory** — the corpus seed and surface census — not by any tool | wave-4 eval; `PMID18460020.json`; commit `3fcb5c0` |
| C18 | Receipt append refused: `unknown fields: ['references']` (it is the optional tenth **coverage** key, not a top-level field) | machine | wave-4 eval |
| C19 | Manifest BLOCK: `landing` must name records, not a URL; `source_fulltext_indexed` undeclared — *"and it forced the honest `false`, which is the more useful record"* | machine | wave-4 eval |
| C20 | 🔴 **The actor's own wave-1 tool produced 25 false positives on its second production paper** — `TABLE_ROW_RE` excludes table rows by wide inter-column gaps, and PyMuPDF emits **one cell per line**, so there were no gaps to find | **self**, on the tool's second production run | wave-4 eval; commit `492a532` |
| C21 | Two lines of the actor's own reasoning **tested and REFUSED**: an apparent Fig 3c-vs-3d contradiction (a confounded measurement) and an expected β-actin confound in Fig 5c (densitometry says the opposite; the paper's central in vitro claim **survives** at 2.69× after normalisation) | **self**, by measuring — *"and one of those measurements told me I was wrong"* | wave-4 eval; commit `3fcb5c0` |
| C22 | 🔴 **Regenerated shared derived surfaces mid-wave and saw the regeneration bake in two peers' uncommitted manifests** — then **reverted** rather than land three actors' in-flight state under its own name | **self** | commit `a8a6a1d` (orchestrator, recording it) |

### 3.3 · The pattern

This actor's error profile is the inverse of `scientist-b`'s: its failures are **measurement**
failures (C11–C13, C20), and its catches are overwhelmingly **cross-measurement** — one instrument
disagreeing with another, or arithmetic refusing to reconcile. That is a genuinely different and
more transferable habit than care, and the actor said so:

> "The target was met. **It was met by writing the limit into the locator rather than by being more
> careful, which is the only version that survives a bad session.**"

Three places in wave 3 where it declined to assert a panel property it could not measure — the
Fig 1B duplication verdict (declined at 421×196), the Fig 3B lane-9 caspase band (stated as a
gradation and an ordering, not as a cleavage), Figure 5C (recorded as qualitative) — are the direct
remedy for wave 2's error-bar failure, and they are the right shape.

**Its own harshest grade is the one to keep:** *"the process still shipped a tool that produced 25
false positives on its second production paper, and that is graded here, separately and worse."*
The fix (C20) was chosen **by measuring both classes on two real papers** — genuine furniture spans
53.7–111.5 % of a document, table cells 2.7–7.6 %, so the threshold sits in an empty band an order
of magnitude wide — and one candidate fix was **reverted** because it silenced the suite's oldest
genuine regression. *"Breaking a genuine existing regression to remove a false positive is the wrong
trade"*, and the rejected design is recorded in the docstring so it is not re-proposed.

---

## 4 · `orchestrator`

The orchestrator's defects are of a different kind — they are **shipped infrastructure**, so each
one is multiplied by three actors.

### 4.1 · The commit wrapper, shipped defective

The `flock`-guarded, path-scoped wrapper of the standing brief § 4 *"lived in the halted session's
scratchpad and did not survive it"* ([`2026-09-09.md`](2026-09-09.md) § 3). It was re-created and
smoke-tested against a clean path — and still shipped with a **`-m`-after-`--` defect**, found by
`scientist-a` on first use and *"fixed by the coordinator before I first used it"* (wave-1 eval,
item 5).

**Assessment.** The smoke test verified the property the author was worried about (it declines to
commit rather than producing an empty commit) and not the property that was broken (argument
ordering with a message containing spaces). This is the same shape as `scientist-b`'s
`genre_discriminator` — *"the fixtures all passed"* — and as the erratum tool's 12/12 self-test
that never called the function it was testing. **Three instances in one day of: a test that passes
while testing something adjacent to the thing that fails.** § 9.6 proposes the measurable response.

### 4.2 · `erratum_scope_check.py` — the tool whose crash input is the remedy it recommends

`scientist-b` shipped it in wave 1 with a `--self-test` of 12 cases, all 12 passing, *"every one of
which was a live false positive before it was a test"*. It surfaced a real, newly visible debt:
58 manifests mention an erratum, 52 negated, 2 `CLEAR`, **4 `SCOPE_UNDECLARED`**.

`scientist-c` then landed a manifest that honestly declared `corrected_items: []` and the tool
crashed:

```
File "framework/scripts/erratum_scope_check.py", line 197, in check_manifest
    "locators": len(entries),
UnboundLocalError: cannot access local variable 'entries' where it is not associated with a value
```

The declared-empty branch returns `len(entries)` **one line before `entries` is assigned**.

- **Why it survived review:** the branch had never executed — *"no manifest in the corpus declared
  an empty scope until today."*
- **Why the self-test was blind to it:** *"it exercises `parse_panel` and `intersects` and **never
  calls `check_manifest`**."*
- **Blast radius, measured:** corpus-wide runs crash; `--pmid`-targeted runs work; **the self-test
  still reports 12/12 green.**
- 🔴 **The property that makes this worth a section:** *"The remedy the tool documents for PMID
  38182577 — declare the empty scope — is currently the input that breaks the tool."* A tool that
  punishes compliance with its own recommendation will train actors not to comply.

**Handled correctly on all three sides.** `scientist-c` reported and did **not** fix it (a peer's
file; cross-actor fixes are the orchestrator's), and wrote the one-line repair *and the regression
that would have caught it* into `CC-20260909-38355659-01` § 4. The orchestrator applied exactly
that in `0e33f0f`, kept the second half as the durable part — *"two branch cases that call
`check_manifest` itself, because a self-test that never calls the function cannot report on it"* —
mutation-tested it, and re-ran the corpus: **60 manifests with an erratum, 3 CLEAR, 53 negated,
4 `SCOPE_UNDECLARED`.** Self-test 12/12 → **14/14**.

### 4.3 · 🔴 The misattribution of authorship

`ledger/tasks/scientist-b/AQEILAN-FT-B-001.json`, field `wave3_not_mine`:

> "`framework/scripts/tool_preflight.py`, `framework/scripts/test_tool_preflight.py` and the
> uncommitted diffs to `CLAUDE.md` and `.claude/skills/legend-start/SKILL.md` are **`scientist-a`'s
> work, not mine. The coordinator initially misattributed them to me and withdrew that in full.**
> I did not revert or alter any of them — I only ran the tool and its tests read-only while deciding
> whether to land them; both diffs are intact at +9 insertions."

**What actually prevented the damage.** Not the withdrawal — by the time the misattribution was
withdrawn, `scientist-b` was already *"deciding whether to land them"*, i.e. holding a peer's
uncommitted work under an instruction that it was its own. What prevented a revert or an
unattributed landing was **`scientist-b`'s own discipline of treating unfamiliar in-flight state as
read-only until proven otherwise**, and its habit of writing a `not_mine` inventory into its task
contract. That is a control the repository does not own; it belongs to one actor's practice.

**Severity.** In a shared checkout with three concurrent writers and a path-scoped commit wrapper,
an authorship claim from the coordinator is the strongest signal an actor has about what it may
touch. There is no machine check anywhere in this repository that answers *"whose uncommitted file
is this?"* — and `git` cannot answer it either, because the work is uncommitted by construction.

### 4.4 · Cross-actor repairs the orchestrator took, correctly

| Repair | Commit | Note |
|---|---|---|
| Executable bit restored on new scripts after `test_release_surface.py` went red | `36d1415`, then **again** in `a8a6a1d` on four more scripts | *"the second time this release-surface red appeared — the authors were mid-wave both times and correctly declined to touch a peer's files"* |
| Four publication-gate blocks reported by `scientist-b` | `fc95d91` | Three spaced-`PMID nnn` wikilinks (one de-linked to plain text because its dossier does not exist yet), and **a literal e-mail address in the standing brief's own attribution block** — the brief printed a `Co-Authored-By` trailer verbatim and tripped the release gate. `BLOCK_PUBLICATION` 4 → PASS 0 |
| The `erratum_scope_check.py` `UnboundLocalError` | `0e33f0f` | § 4.2 |
| Derived surfaces regenerated **at wave close on a clean tree** | `a8a6a1d`, `f422420` | The policy `scientist-b` established and the other two honoured: the generators read the **working tree**, not the index |

**This division worked and should be kept:** a scientist reports a cross-actor red, it does not fix
it. It was applied consistently by all three actors and produced zero cross-actor file collisions in
eleven waves.

### 4.5 · Where the orchestrator's own dispatch was wrong

- **A false acquisition hint carried into a task contract as fact.** `AQEILAN-FT-C-001` declared
  `pmcid: null` and `free_sites: []` for PMID 18460020; both were wrong (C17). The brief instructs
  actors *"do not re-derive them"*, so the hint was authoritative by design. It was caught only
  because the actor checked the repository's own corpus seed against it.
- **A stale attribution line in the standing brief** — known and corrected at dispatch
  ([`2026-09-09.md`](2026-09-09.md) § 3), but the literal address remained in the committed brief
  until the release gate caught it half a day later.

---

## 5 · The attribution census — machine-caught versus self-caught

**This is the metric worth tracking**, and `scientist-a`'s wave-1 line is the reason:

> **"Every one of the six was caught by a machine or another agent. Not one was caught by my own
> re-reading, which is the single most useful line in this diagnosis and the argument for keeping
> all of these gates expensive."**

### 5.1 · Aggregate, by the counting rule of § 0.2

| Actor | Incidents | machine | blind auditor | peer / coordinator | **self** | self-caught |
|---|---:|---:|---:|---:|---:|---:|
| `scientist-a` | 13 | 6 | 5 | 1 | **1** | **8 %** |
| `scientist-b` | 17 | 6 | 0 | 1 | **10** | **59 %** |
| `scientist-c` | 22 | 11 | 0 | 0 | **11** | **50 %** |
| `orchestrator` | 5 | 1 | 0 | 3 | **1** | 20 % |
| **Sweep** | **57** | **24** | **5** | **5** | **23** | **40 %** |

**Read this table with three cautions, all of which matter more than the numbers.**

1. **The denominator is self-reported** (§ 0.3). It counts caught errors only.
2. **The classes are not comparable in severity.** Most machine catches are schema rejections —
   a snippet under 30 characters, a timestamp ordering, a field name — which are cheap, instant, and
   would never have reached a claim. Weighting every incident equally flatters no one and mostly
   measures how strict the validators are.
3. **`scientist-a`'s 8 % is not a worse actor; it is a different exposure.** It is the only actor
   that crossed the R4 threshold, so it is the only actor a blind auditor ever examined — 5 of its
   13 incidents were found by auditors who found nothing on the other two actors **because they were
   never run there**. Remove the audits and its self-caught share is 1 of 8. That is still the
   lowest in the sweep, and the actor said so itself before anyone else could.

### 5.2 · The sub-census that actually matters: the six near-errors that were one step from landing

| Near-error | Actor | Caught by |
|---|---|---|
| False correction to a **correct existing locator** from a 667 px rendering (§ 2.1) | `scientist-b` | **self** — a procedural rule applied in the right order |
| A safety-critical screen called with **inverted arguments**, returning CLEAN on an unscreened filename (§ 3.1) | `scientist-c` | **self** — disbelieving a green result |
| A committed cross-panel bridge **wrong on cell line** (A9) | `scientist-a` | blind auditor |
| A PMID taken from a search **while the identifier sat inside the open artefact** (A13) | `scientist-a` | both blind auditors |
| A `REFUSED` verdict nearly accepted **without asking what it refused for** (B16) | `scientist-b` | coordinator |
| Peers' untracked work nearly **baked into shared derived surfaces** (C22) | `scientist-c` | **self**, then reverted |

**self 3 · blind auditor 2 · peer 1 · machine 0.**

🔴 **On the incidents that would actually have damaged the record, the machines caught nothing.**
That inverts the aggregate and it is the single most important measurement in this document. The
validators, writers and linters are excellent at refusing malformed *declarations* and blind to
wrong *content* — which is precisely their design, and precisely why the two controls that did work
(a reader's rule applied before contradicting a locator, and two blind auditors reading triples with
no knowledge of the conclusions) are the ones to invest in.

### 5.3 · The self-evaluation is itself a control, and it has a measurable yield

`scientist-b`'s `multihop.performed` flip (B9) and its stale reference count (B10) were caught **by
the act of writing the diagnosis**, before any closing report — *"which is the entire argument for
running it first."* `scientist-c` fixed its prose-not-queue debt (C8) **inside** its own evaluation
rather than promising it. `scientist-a`'s wave-3 evaluation produced the target that wave 4 then met.

**Yield: 4 defects caught and 1 target set, across 9 evaluations.** Against that: **every wave that
produced no self-evaluation was a wave that had been terminated** (§ 6.4). The protocol's ordering
rule — *takeaways written first describe a session that went well* — was honoured by all three
actors on every wave that survived to write one.

---

## 6 · Problems classified

Kept separate because they have different owners and different fixes.

### 6.1 · Scientific

| # | Problem | Where |
|---|---|---|
| S1 | A genotype–phenotype rule stated at **allele level** while the source's own Figure 2B records 3 of 6 named variants in **compound-heterozygous** genotypes | `PMID26499798.md` § 3; corroborates the wave-2 narrowing on `CLAIM 030` |
| S2 | An inference transmitted **stripped of its declared interpretive status** (haploinsufficiency) | `PMID27551470.md` § 3, ref 9 → PMID 17360458 |
| S3 | A caveat **alive in prose and dead in a table** — chapter 8's Table 1 lists TP53 as a partner with no caveat while its prose carries the qualification, *"and a partner table is exactly the surface a downstream consumer mines"* | commit `d1387d2`; `PMID25245215.md` |
| S4 | **`propose` → `conclude`**: an editor's introduction reporting its own author's chapter at a stronger epistemic grade than the chapter states | `PMID25238781.md` § 4; `PMID25245215.md` |
| S5 | A **negative absorbed rather than conceded** — a null on CFS alteration vs gene-product expression, glossed inside a section headed *"support its role as a tumor suppressor"* | `PMID27551470.md` § 2.3 |
| S6 | A leading statistic that **cannot discriminate the hypothesis it is offered to settle** (TP53 quoted 244 orders of magnitude below WWOX on the same metric) | `PMID27551470.md` § 2.2 |
| S7 | **Reagent and antibody descent from a paper under a standing expression of concern**, invisible to any per-PMID retraction check | `PMID18460020.md` § 7; `CC-20260909-18460020-01` |
| S8 | Three **consolidated baseline** claims whose primary sources this repository cannot open or has never opened: `CLAIM 003` (`33914858`, parked), `CLAIM 030` (`29808465`, abstract only), and the P47R/survival limb (`25411445`, no depth) | [`2026-09-09.md`](2026-09-09.md) § 6.1, § 7.3 |

### 6.2 · Procedural

| # | Problem | Where |
|---|---|---|
| P1 | **A rule read in full the same session, then not applied** — twice consecutively, by the same actor, on different rules | B6, wave-2 eval (F2) |
| P2 | **An assumption asserted with the confidence of a measurement**, three instances in one wave | A11, A12, A13 |
| P3 | **A green result accepted without asking what it screened** (C10) or **why it refused** (B16) | § 3.1, § 2.2 |
| P4 | A **coverage claim** or **effort flag** improved without the work behind it (B9), or nearly (B17) | wave-4, wave-6 evals |
| P5 | **`DEFAULTS_TAKEN` and `STOP_LOG` are mandated by the brief § 1 and § 5 and persist almost nowhere.** A repository-wide grep finds `DEFAULTS_TAKEN` in exactly **two** files: the brief that mandates it, and one commit candidate. The rest lived in final messages to the orchestrator, which are transcripts | brief § 1; `CC-20260909-38355659-01` § 4 |
| P6 | The **misattribution of authorship** (§ 4.3), for which no machine control exists | `AQEILAN-FT-B-001.json` `wave3_not_mine` |
| P7 | **A lot whose members cite each other was discovered to be a set at M5, not declared one at M0** — *"the dispatch grouped them as 'the fragile-site review layer' and that grouping turned out to be the substance, not the convenience it looked like"* | wave-5 eval, closing section |

### 6.3 · Schema — all four referred to the operator, none improvised

| # | Problem | Where |
|---|---|---|
| H1 | **No lawful route to correct a wrong `study_id`.** `receipt_correction` must preserve study identity — the field that is wrong; `receipt_invalidation` addresses evidence belonging to a *different* study. Net effect: **the ledger refuses a correct DOI because an incorrect one was persisted first.** Proposed and deliberately unimplemented: a `record_kind: identity_correction` that changes `study_id` only and freezes every reading field | C3; [`2026-09-09.md`](2026-09-09.md) § 6.2 |
| H2 | **First contact with the text after a `legacy_reconstruction` is unrepresentable under `first_read`** — the writer refuses `first_read` with a `prior_receipt` and refuses a null `prior_receipt` when the study already has an event, while the dispatch and the protocol both say a prior `legacy_reconstruction` means `first_read` | C14; wave-3 eval |
| H3 | **The panel-relation vocabulary is unavailable in exactly the papers whose surface is worst.** Adjudicated text locators must declare `surface: figure`, and `TEXT_SURFACES = {body, table, supplement}`, so no adjudicated locator can be the target of `text_contradicted_by_panel` or `panel_qualifies_text`. Three genuine coupled relations on PMID 16223882 could not be declared | wave-3 eval |
| H4 | **`ARTIFACT_KINDS` has no binary supplement kind and `_artifact_text` has no `.pptx` branch**, so a `.pptx` is declarable only as `supplement_text`, which its own text verification then refuses. Consequence: the single most consequential sentence of the PMID 38499540 reading — the authors' deposited note that the *t*-tests were computed over microscopy **fields**, not per **mouse**, in a speaker-notes pane — is carried in the dossier only and **not** as a machine-verified locator. It is not mislabelled as a figure | wave-4 eval Q26; `PMID38499540.json` |
| H5 | **Where undistributed-but-cited material belongs in a coverage map is unsettled.** Under the contract's own wording `FTR-20260814-34268881-03` **qualifies as complete** while its author declared it partial. Both readings are defensible, which is the problem | [`2026-09-09.md`](2026-09-09.md) § 6.2 |
| H6 | **A per-PMID retraction check cannot see the integrity status of the papers a paper depends on.** `CC-20260909-18460020-01` proposes a `Reagent provenance:` registry field; if the schema has no such field, the finding is that it needs one | S7 |

### 6.4 · Infrastructure

| # | Problem | Measured effect |
|---|---|---|
| I1 | **Three session terminations, all three rate limits.** `scientist-a` wave 2 — the auditor completed but its report never reached the session, which shipped ten locators marked `[UNAUDITED]` with the candidate HELD, released only when the orchestrator relayed the report verbatim. `scientist-b` wave 3 — terminated after a complete reading and before any manifest existed: `ANALYSIS_DONE_RECEIPT_NOT_PERSISTED`, paid off a wave later without re-reading. `scientist-c` wave 2 — terminated between a receipt append and its declared discovery-ledger append, leaving LINT at `BLOCK_BATCH_COMMIT: OUTPUT_STUDY_MISMATCH`; on resume the intended append was written rather than the receipt walked back. A **fourth** rate-limit event killed two blind auditors mid-run in `scientist-a` wave 4 without killing the session. **No artefact describes a process exit.** | 3 of 11 waves produced no self-evaluation, and all 3 are these |
| I2 | **PyMuPDF / `fitz` is absent from this deployment**, so rule 5e's own remedy — anchoring locators to rendered pages when a text layer is SUSPECT — is unrunnable through that route repo-wide. `capability_scout_log.md` records the deliberate SKIP: *"`fitz` is already absent in this environment and a red suite proves it."* Rule 5e was nonetheless executed for the first time in this deployment (`scientist-a`, PMID 24510053; `scientist-c`, PMID 16223882 at 12/12 verified adjudications) through `regenerate_adjudications.py`'s canonical call | The remedy exists but its most-cited implementation route does not; every 5e reading in this sweep had to go through the regenerator |
| I3 | **PMC began serving a Google reCAPTCHA during the sweep** where it had not that morning, triggered by a browser-like User-Agent. `pmc_pow_fetch.py` parses the older proof-of-work interstitial and **raises** on the challenge page. Workaround found by measurement: send **no** User-Agent. Later the challenge extended to asset paths regardless of UA | Cost PMID 20146584 its two figure images and its `complete` depth; affects every actor |
| I4 | **`files/` is gitignored by design**, so 428 of 464 fingerprinted artifacts are absent from this checkout. `test_surface_census` and a 55-manifest `--verify-artifacts` sweep are red for that reason alone | Two release suites permanently red; every actor had to distinguish this from a real defect, and each did so empirically by stashing its own change and re-running |
| I5 | **Five OA indexes unanimously reported PMID 24510053 closed and all five were wrong**, because they key on a DOI whose journal has since changed publisher | Produced `oa_status_dissent.py`; returned a **true negative** on its next use and was credited as one |
| I6 | **`test_batch_queue` is red because readings have outrun the paper registry** (80 complete reads against a 67 ratchet at wave close, 69 vs 67 mid-sweep). The ratchet is working as written; **only a `BATCH_COMMIT` closes it, and that is the operator's** | Not an actor's defect; correctly named in commit messages rather than left as an anonymous red |

---

## 7 · Qualifying "compression toward confidence"

Three actors reached this conclusion independently and [`2026-09-09.md`](2026-09-09.md) § 7.1
records it. **A conclusion three agents reach independently is exactly the kind that needs its
denominator printed on it**, so this section does two things: it lists the specific source-to-source
comparisons that support it, and it separates two claims that are easy to conflate and that rest on
completely different evidence.

### 7.1 · The two claims, separated

> **Claim D (dependency between publications).** The documents in this literature are not
> independent of one another: they share reagents, share authorship, and in several cases a
> secondary source is a restatement of its own author's primary.
>
> **This is a property of the literature.** It is established by artefacts external to this sweep
> and would be true whoever read them.

> **Claim V (independence of the actors' verifications).** Three actors, working separately, reached
> the same characterisation of that literature.
>
> **This is a property of this sweep**, and it is weaker than it looks. § 7.4.

**Conflating them produces a false syllogism** — "three independent readers found dependence,
therefore the dependence finding is independently confirmed" — in which the *subject* of
independence silently changes between premise and conclusion. Claim D is well evidenced. Claim V is
partially evidenced and its limits are enumerable.

### 7.2 · Claim D — the checkable comparisons, with both sides quoted

Every row below is verifiable by opening the two named surfaces. The denominator is in § 7.3.

**(a) `propose` → `conclude`, between a chapter and its own editor's introduction.**
Source: PMID 25245215 (chapter 8 of CMLS 71(23), the field's dedicated WWOX chapter).
Restatement: PMID 25238781 (the editor's introduction to the same issue).

> **The introduction says:** *"Authors conclude that these observations indicate that WWOX is
> functionally required for cell homeostasis and that its deletion has important consequences
> contributing to the neoplastic process."*
>
> **The chapter says `we propose`**, and its Concluding remarks hedge three more times: *"it can be
> argued"*, *"might have"*, *"it can be speculated"*.

`scientist-b`'s commit `d7325a1`: *"It delivers the content at a weaker epistemic grade than the
promise assigned it, and **the upgrade was made by the same person single-authoring the summary of
his own chapter**."*

**(b) A caveat alive in one document's prose and dead in another's table.**
PMID 20146584 (2010) records an **explicit failure to replicate**: these authors could not
recapitulate WWOX–p53 binding. PMID 25245215's **Table 1 lists TP53 as a partner with no caveat**,
while its own prose carries the qualification. Commit `d1387d2`: *"a partner table is exactly the
surface a downstream consumer mines."*

**(c) A haploinsufficiency inference transmitted stripped of its declared interpretive status.**
Source: PMID 17360458 (Aqeilan 2007, PNAS). Restatement: PMID 27551470 (2016 editorial), ref 9.

> **The datum transmits correctly:** *"Wwox heterozygous mice develop higher incidence of
> spontaneous tumors"* — 10/58 heterozygotes versus 2/60 wild type.
>
> **What does not transmit:** the source's own haploinsufficiency conclusion is **interpretive** —
> its tumours retain Wwox immunoreactivity, and *"protein positivity does not demonstrate an intact
> second allele or unchanged dosage."*
>
> **`scientist-b`'s verdict:** *"The editorial transmits the inference without its declared
> interpretive status."*

Field size, measured the same day: **`WWOX AND haploinsufficien*` returns 3 records in all of
PubMed** — *"the entire published field behind an inference this editorial treats as settled."*

**(d) Faithful, and half.** Ref 12 → PMID 23370280 (Salah 2013). Cytoplasmic retention of ΔNp63α and
suppressed transactivation transmit correctly. **Dropped:** the source's headline that WWOX competes
with ITCH and thereby *increases* ΔNp63α abundance while lowering its activity — the demonstration
that greater protein abundance can coexist with lower function. Under a heading *"WWOX promotes
apoptosis"*, only the suppressive half survives. *"Incomplete rather than false, and incomplete in
the direction that serves the argument."*

**(e) Disposal by omission, checked against the very review cited.** Ref 7 → PMID 24510053. The
editorial attributes the *"frequent loss in cancer"* framing to that review. The review, as read
here, reports: *"Some studies document **increased** WWOX in breast, gastric and prostate
carcinomas, which the authors read as complex regulation."* The countervailing observation is not
carried — **and the entire selective-pressure argument requires loss to be the rule.**

**(f) A citation that points where this repository's record does not.** Ref 8 → PMID 25331887, for
the ITCH step. This repository's **blind locator audit** of that paper's supplement struck the
clause *"ITCH-dependent"* from `CLAIM 029`'s own text, finding it *"has no blot, lane, label or
legend mention anywhere in this supplement."* `scientist-b` states the narrow, defensible form and
refuses the wide one: *"This is not a claim that the editorial is wrong… the citation offered for
the ITCH step points where this repository's own record does not."*

**(g) A directional conflict between two secondary sources by overlapping authorship.** PMID
20146584 (2010) says WWOX is **reduced** after UV; PMID 25245215 (2014) says **increased**, on
*unpublished data*, in the direction its DDR model requires. Commit `d1387d2` records it *"as a
conflict between secondary sources, not as biology."*

**(h) The same observation used on both sides of the argument, never reconciled.** In PMID 27551470,
hemizygosity is the premise of the **passenger** hypothesis in the Introduction — *"This assumption
led to the hypothesis that alterations in CFSs are secondary events"* — and three paragraphs later
it is evidence for the **driver** view: *"most of the deletions within WWOX are hemizygous rather
than homozygous, suggesting haploinsufficiency."*

**(i) A leading statistic that cannot discriminate.** Same document: WWOX at Q = 1.31E⁻²⁶⁶ against
**TP53 at 5.04E⁻²²** — *"some 244 orders of magnitude weaker… It does not rank importance. It ranks
recurrent focal deletion, which is precisely what a common fragile site is expected to produce
whether or not the gene inside it is a driver."*

**(j) A cited fact that runs against the claim it is offered to support.** Same document: *"cancer
usually occurs after the reproductive phase and therefore loss of CFS would not have an inherited
selective pressure. **In support of this assumption**, germline mutations or loss of function of
WWOX are associated with neuronal disorders."* A germline loss-of-function phenotype is what
inherited selective pressure looks like, and it acts **before** reproduction. *"This needs no
external data — the inversion is visible in the article's own two consecutive sentences."*

**(k) `scientist-a`'s independent instance, in a different literature.** PMID 26499798 states its
genotype–phenotype rule at **allele level** while **its own Figure 2B, read at 8× and reproduced
independently by both blind auditors, records three of the six named variants in compound-
heterozygous genotypes.**

**(l) `scientist-c`'s independent instance, at the reagent layer rather than the citation layer.**
Four papers that read as four independent bricks share an adenovirus and both antibodies, all
traced to PMID 16223882 — a paper carrying an expression of concern *"whose scope is precisely the
loading-control panel that would license quantitative comparison."*

### 7.3 · 🔴 The denominator, printed on the conclusion

**Every checkable restatement in this sweep changed something. There were five.**

| Document | Restatements | Checkable against a source this repository holds | Changed something |
|---|---:|---:|---:|
| PMID 27551470 (editorial, 17 refs) | 17 | **4** (3 complete + 1 partial in the ledger; **13 absent**) | 4 / 4 |
| PMID 25238781 (editor's introduction, 9 chapters + 11 refs) | 20 | **0** — *"zero of nine held at any depth"* | — |
| PMID 25245215 (chapter 8, the promise test) | 1 | **1** | 1 / 1 |
| **Total** | **38** | **5** | **5 / 5** |

**So the fidelity finding is 5 for 5 on a denominator of 5, drawn from three documents with
overlapping authorship, of which 33 of 38 restatements could not be checked at all.**

That is a striking rate and a small sample, and `scientist-b` said so in its own manifest, dossier
and receipt rather than letting the ratio travel bare: *"Bad answer avoided: reporting 'the
restatements were checked' without saying that 76 % of them could not be."*

**The defensible statement**, and the one this retrospective endorses:

> **This literature's checkable restatements changed something in every case examined (5/5), and the
> change was in the direction of greater confidence and less qualification in every case. The
> unchecked majority (33/38) is unchecked, not confirmed.** The transferable operating rule is
> unaffected by the sample size, because it is a rule about routing and not about a rate:
> **resolve to primary sources or inherit the compression.**

Two further measurements support the routing rule independently of the 5/5:

- The reagent dependency (l) is not a restatement rate at all; it is a **structural** dependency
  established from the deposits themselves.
- The absences carry their denominators: `WWOX AND haploinsufficien*` = **3** records in all of
  PubMed; `"Cell Death Discov"[jour] AND (fragile[ti] OR FRA16D[ti])` all years = **1**, so *"the
  piece is framed as one side of a controversy and no counterpoint was ever published there"*;
  ten of twelve phenotype terms literally zero across 31,756 characters of the field's dedicated
  WWOX chapter.

### 7.4 · Claim V — how independent were the actors' verifications, exactly

**Independent, in these respects, and they are real:**

- **Disjoint lots.** One owner per PMID; no PMID appears in two lots; no `PARALLEL_READ_GROUP` was
  declared because none was needed ([`2026-09-08.md`](2026-09-08.md) § 3).
- **Disjoint literatures.** `scientist-a` read CNS primaries and two reviews; `scientist-b` read a
  fragile-site review layer and a DDR primary; `scientist-c` read bone and pancreatic oncology and a
  2005 PNAS reagent source. The three instances (j)/(k)/(l) are drawn from different documents in
  different subfields at the citation layer, the figure layer and the reagent layer respectively.
- **Independent acquisition and independent locators.** Each actor fingerprinted its own artifacts
  and captured its own verbatim locators; nothing was inherited across actors.
- **Independent instruments.** `scientist-a` found its instance by reading a figure against a
  review's prose; `scientist-b` by resolving reference lists to PMIDs and joining them against the
  ledger; `scientist-c` by tracing reagent provenance to a deposit under an expression of concern.
- **Timing.** The three closed within hours of each other and did not coordinate.

**Not independent, in these respects, and they bound the claim:**

- **One standing brief.** All three were dispatched with the same
  [`2026-09-08_scientist_brief.md`](2026-09-08_scientist_brief.md), whose § 0 requires reading
  `gold_is_in_the_details.md` rules 1–8 and 5b–5e and `epistemic_discipline.md`, and whose M5
  instructs *"what it does not support (the negative is the product, not the residue)"*. **Three
  readers trained on one instruction to hunt for exactly this class of defect are not three
  independent detectors of it.**
- **One shared checkout on `main`.** Each actor could — and did — read peers' committed dossiers and
  manifests. `scientist-c`'s reagent finding cites `scientist-a`'s `evidence_presence.py` as the
  same defect found from the other direction; `scientist-b`'s wave-5 cross-document finding cites a
  locator persisted in its own wave-5 manifest; `scientist-a`'s wave-3 finding uses the dismissal
  ledger. Cross-reading was correct practice and it is also correlation.
- **One corpus.** All three joined restatements against the **same** receipt ledger, so all three
  inherited the same 13-absent / 4-present availability pattern.
- **One lot family.** 20 of the 23 PMIDs are Aqeilan-lab or Aqeilan-adjacent by construction — the
  sweep was defined as *"the Aqeilan free-full-text sweep"*. `scientist-c` had to correct that
  framing on its own last paper: *"the lot is the 'Aqeilan sweep' and Aqeilan is **fourth of six**;
  the primary group is Yokozaki/Semba (Kobe)."* **A finding about a literature's internal dependency
  is partly a finding about how the lot was drawn.**
- **`scientist-b` contributes 3 of the 5 checkable restatements and both zero-denominator
  documents.** Rows (a)–(j) are one actor's work. The genuinely independent corroboration is
  (k) `scientist-a` and (l) `scientist-c` — **two instances, in different layers, not two
  replications of the same measurement.**

### 7.5 · The verdict this retrospective is prepared to defend

> **Claim D holds and is well evidenced**, from three layers (citation, figure, reagent) and by
> artefacts anyone can re-open. **Its rate is not established**: 5/5 on n=5, 33 unchecked.
>
> **Claim V holds in the narrow sense that matters operationally** — three actors with disjoint
> lots, disjoint literatures and independent instruments converged — **and does not hold in the
> strong sense** that would let the convergence be counted as three-fold confirmation, because the
> actors shared a brief that told them what to look for, a corpus that told them what was
> checkable, and a lot family drawn around one laboratory.
>
> **The operating conclusion is unaffected either way, which is the best argument for it:**
> a repository reading this literature must resolve to primary sources or inherit the compression.
> That follows from Claim D alone.

---

## 8 · The therapeutic negative, stated precisely

The operator's requirement is to keep **"no support in this lot"** strictly apart from **"evidence
of ineffectiveness."** The record mostly does this well; two wordings need tightening and one needs
a correction.

### 8.1 · What the lot actually contains

| Reading | Design | What it is not |
|---|---|---|
| PMID 16223882 (`scientist-c`) | Ad-WWOX restoration in three WWOX-negative lung cancer lines; xenografts **from pre-treated cells** | *"the in vivo result is demonstrated on pre-treated cells and never inside a Wwox-expressing tumour"* |
| PMID 18460020 (`scientist-c`) | Ad-WWOX in pancreatic carcinoma; **engraftment prevention with a dying inoculum**; the Ad-WWOX histology arm **occupies zero pixels** because no treated tumours formed to section | not tumour treatment |
| PMID 21731849 (`scientist-c`) | a same-lab **review**; contribution is synthesis only | no measurement of its own |
| PMID 34268881 (`scientist-a`) | AAVS1/lentiviral WWOX **rescue in isogenic cortical organoids**, ubiquitous promoter, **supraphysiological** expression, **partial** rescue, applied after organoid formation | *"il rescue prova che alcuni fenotipi sono modificabili… ma non autorizza inferenze cliniche su vettore, dose, distribuzione o sicurezza"* — the authors themselves call it proof of concept and ask for *"fine-tuning of expression levels"* |

🔴 **A correction to the summary framing.** A flat statement that *"the lot contains no
rescue-of-established-disease design"* is not accurate as written and should be scoped. It is exactly
true of **`scientist-c`'s three oncology readings**, which is how [`2026-09-09.md`](2026-09-09.md)
§ 7.2 states it. Across the whole sweep there **is** a rescue design — PMID 34268881 — and it is a
developmental, supraphysiological, partial, marker-selective rescue in an organoid model, not a
rescue of established disease and not a dose, window, targeting or safety statement. Stating the
absence too broadly is the mirror image of the error this section exists to prevent, and it would be
caught by anyone who opened the lot.

### 8.2 · The three reasons the oncology readings do not corroborate each other

From `PMID18460020.md` § 7, and correctly recorded as a **deliberate non-link** rather than absorbed
as a corroboration:

1. **Not independent.** *"This paper's virus and both antibodies come from that paper. Agreement
   between a source and its own reagent-consumer is not corroboration."*
2. **Integrity.** The parent paper is under a standing expression of concern, and the repository's
   own instruction is no canonical promotion until it resolves.
3. **Design.** Engraftment prevention with a dying inoculum is not tumour treatment.

And from `PMID16223882.md` § 6, `CLAIM 002` and `CLAIM 004` — both `consolidated baseline` claims
about WWOX restoration producing rescue — are **deliberately not touched**: *"'Restoring WWOX
rescues' is precisely the sentence that would travel between these contexts unexamined, and this
reading supplies no support for it outside oncology."*

### 8.3 · The precise wording, and the wordings to avoid

> ✅ **Defensible.** *No reading in this lot supplies evidence for WWOX restoration as a therapy for
> the reference genotype. The oncology restoration readings are prevention-of-engraftment and
> pre-treatment designs and are not independent of one another; the one rescue design in the sweep is
> a supraphysiological, partial, marker-selective developmental rescue in an organoid model whose own
> authors present it as proof of concept and ask for expression fine-tuning. **This is an absence of
> support, not a demonstration of inefficacy**, and it constrains what may be claimed, not what may
> be true.*

> ❌ **To avoid.** *"The lot shows WWOX restoration does not work"* · *"these papers fail to
> demonstrate efficacy"* (an efficacy design absent cannot fail) · *"restoration is ineffective in
> established disease"* (nothing here tested established disease) · *"the overshoot shows the rescue
> is harmful"* — explicitly refused by the source reading: *"It does **not** show the rescue is
> harmful. Overshoot of a marker is not a toxicity finding, and no endpoint here measures harm"* ·
> *"the lot contains no rescue design"* (§ 8.1).

### 8.4 · The one carried caution, and its declared limits

PMID 16223882 supports, as `IPOTESI` only: **overexpressing Wwox in cells that lack it kills them.**
In an oncology frame that is the therapeutic effect; in a WWOX-DEE frame it is a **dose-and-cell-type
question**. The reading fences it immediately and correctly: *"explicitly not a safety finding about
any WWOX gene therapy: the cells here are tumour lines with a p53 status the paper itself flags as
relevant, the vector is adenoviral, the dose is moi 100, and none of that transfers to a neuron."*

It composes with PMID 34268881's `IPOTESI` — that *"the dose-response for WWOX restoration may be
non-monotonic rather than saturating"*, tagged `PREMISE: DEFAULT_FROM_TEXTBOOK` on the unstated
assumption that more restored WWOX is monotonically better, with a `REVIVAL_TRIGGER` of *a titrated
rescue series with a wild-type comparator drawn at every dose and at least one patterning endpoint.*
**Two independent readings, in unrelated systems, both pointing at dose rather than at presence.**
That is a research target, and it is not a claim.

---

## 9 · Proposed improvements, each with an observable criterion

Ordered by expected yield per unit of work. Every criterion is measurable by a later session from
committed artefacts alone. **Baselines are measured today**, so drift is detectable.

### 9.1 · Make the near-error class the audits catch into a class the audits are *run* for

**The finding.** On the six near-errors that were one step from landing, machines caught **zero**
(§ 5.2). Blind auditors caught two — and were run at all only on `scientist-a`, because R4 triggers
on `consolidated baseline` claims. `scientist-b`'s Fig 6A false correction (§ 2.1) touched no such
claim, so no auditor ever saw it, and the actor said what would have happened: *"the wrong edit
would have been confident, well-argued, and would have passed every gate this repository owns."*

**Proposal.** Add one trigger to the R4 floor: **a reading that contradicts, corrects or replaces an
existing persisted verbatim locator must be audited blind, whatever claim status is involved.** The
audit need cover only the contradicted triples, so the cost is bounded by how often it happens —
which the baseline below measures.

**Observable criterion.**
- *Baseline, today:* in this sweep, **3** readings contradicted a pre-existing locator
  (`scientist-b` PMID 18674750 `entries[21]` — landed and correct; `scientist-b` PMID 29724996
  Fig 6A — withdrawn; `scientist-a` PMID 34268881 `entries[14]` — corrected by audit). **1 of 3 was
  audited.**
- *Target, next sweep:* **3 of 3**, i.e. every manifest whose locator carries a "this corrects what I
  wrote on `<date>`" clause also carries an `audit_note` naming the auditor count and the verdicts.
- *Machine-checkable form:* a script greps manifests for locator text asserting a correction to a
  prior locator and asserts the presence of a sibling `audit_note`. Reports a ratio, not a block.

### 9.2 · Every screen must say what it screened

**The finding.** Two of the sweep's most severe near-errors are the same defect at different
altitudes: a screen returning **CLEAN on an unscreened surface** (§ 3.1), and a screen returning
**REFUSED for the wrong reason** (B16). `scientist-b` had already shipped a whole tool about it in
wave 5 — *"a screen whose failure mode is a silent pass is worse than no screen"* — and then nearly
committed the second form in wave 6. `scientist-c`'s partial fix (an argument-shape guard) closes
the inversion case only.

**Proposal.** A uniform verdict contract for every screen in `framework/scripts/`: a verdict is a
record, not a boolean, and it carries **the digest and byte length of what was screened** and, on a
refusal, **which signature fired**. A verdict over a zero-length or non-artifact input is an error,
never a pass. `INSUFFICIENT_DATA` naming what is missing — already the design rule of
`genre_discriminator.py` — becomes the repository-wide convention rather than one tool's practice.

**Observable criterion.**
- *Baseline, today:* `text_surface_intrusion_check.py`, `_refuse_suspect_surface`,
  `erratum_scope_check.py`, `oa_status_dissent.py`, `manifest_flag_drift.py`,
  `locator_identifier_provenance.py`, `genre_discriminator.py` — **1 of 7** (`genre_discriminator`)
  refuses to return an uninformative pass; **0 of 7** report the digest of what they screened.
- *Target:* 7 of 7 report `screened: {digest, bytes}`; 7 of 7 return `INSUFFICIENT_DATA` naming the
  missing input rather than a green verdict.
- *Mutation test that proves it:* handing each screen a path where it expects content, or an empty
  string, turns exactly the new cases red and leaves every other case green — the shape
  `test_suspect_surface_call_shape.py` already demonstrates for one tool.

### 9.3 · A self-test that never calls its own entry point is not a self-test

**The finding.** Three instances in one day (§ 4.1): the commit wrapper smoke-tested a different
property from the one that broke; `erratum_scope_check.py` reported **12/12 green while crashing
corpus-wide**, because its self-test *"exercises `parse_panel` and `intersects` and never calls
`check_manifest`"*; `genre_discriminator.py`'s fixtures all passed while it flagged every ordinary
primary paper, exposed only by a control run against papers whose genre was never in doubt.

**Proposal.** A meta-test that enumerates every script in `framework/scripts/` carrying a
`--self-test` or a `test_*.py`, and asserts that the suite invokes the module's **top-level entry
point** at least once, with at least one case drawn from a **real corpus artefact** rather than a
fixture. The orchestrator's repair in `0e33f0f` already added exactly this for one tool and is the
model.

**Observable criterion.**
- *Baseline, today:* `erratum_scope_check.py` shipped at 12/12 with 0 cases calling `check_manifest`;
  after repair, 14/14 with 2. The equivalent coverage for the other tools shipped this sweep is
  **unmeasured** — measuring it is the first deliverable.
- *Target:* the meta-test reports, per script, `entry_point_called: true|false` and
  `real_artifact_case: true|false`; **0 scripts** at `false/false`; the count is reported in every
  capability-scout entry that ships a tool.
- *Second-order criterion, the one that matters:* **zero tools ship in a sweep whose corpus-wide run
  crashes while their self-test is green.** Baseline this sweep: **1**.

### 9.4 · Identifiers, counts and residue identities must come from the artefact

**The finding.** `scientist-a`'s wave-4 pattern (A11, A12, A13): *"an assumption asserted with the
confidence of a measurement, in a place too small to look at twice."* Two of the three were caught
only because two blind auditors looked. The actor shipped `locator_identifier_provenance.py` in
response, which asks whether an identifier asserted in a proposition occurs in any artefact the
manifest declares — *"never whether it is correct, which nothing local can know"* — and which caught
**two defects in itself** before landing, one of which was that it *would have missed the error it
exists for*.

**Proposal.** Wire it into `deepdive_manifest.py` as a **WARN with a required declaration**, not a
block: an identifier or count asserted in a proposition must either occur in a declared artefact, or
carry an explicit `external_provenance` field naming the command or index that produced it and the
date. The declaration is the point; a value that must be declared external is a value someone can
challenge.

**Observable criterion.**
- *Baseline, today, from the tool's own first measurement:* **80 manifests, 26 measurable, 37
  in-artefact, 4 declared external, 15 undeclared external, 16 source-identity unverified** — offered
  by its author as a review queue, explicitly *"not as 16 errors"*.
- *Target, next sweep:* **undeclared external = 0** on every manifest minted after the change, with
  the pre-existing 15 worked down as their papers are next touched, not retro-edited.
- *Independent confirmation:* blind auditors report **zero** factual-identifier errors of the
  `29581896` class. Baseline this sweep: **1**, found by both auditors independently.

### 9.5 · Close the two gaps that were registered twice and built zero times

Both are small, both were deliberately deferred for defensible reasons — *"one upgrade with real
regression evidence is worth more than two rushed ones"* — and both are now overdue.

**(a) The queue-ID cross-check (B7).** Nothing checks that a `multihop.queued[].queue` identifier
exists or names the same PMID, so a manifest can point at another paper's debt and stay green.
Registered wave 2, not built; the actor's reason — *"a second validator change written at the end of
a long wave is exactly the kind of change that gets its tests written to match whatever it does"* —
is sound and no longer applies at the start of a sweep.

- *Observable criterion:* a corpus sweep of all 80 manifests reports the current count of queue IDs
  that do not resolve, or resolve to an entry naming a different PMID. **That number is the
  baseline** — it is unmeasured today, and measuring it is the deliverable. Target after the fix:
  0 new occurrences; a regression fixture asserts refusal.

**(b) Wire `text_surface_intrusion_check.py` into the validator for PDF-derived surfaces.** Named as
the obvious next step in `scientist-c`'s wave-1 residual risk, **repeated unchanged in wave 3 and
again in wave 4** — *"unchanged after a second production run that proved it earns its place."* It
remains a command run by hand, which means the defect it catches (a verbatim quote taken across a
page-furniture intrusion, e.g. the page number `588` injected into the headline sentence) is caught
only when someone remembers to run it.

- *Observable criterion:* `deepdive_manifest.py` invokes it on every artifact of kind
  `article_text` derived from a PDF; a locator whose snippet spans a detected intrusion **BLOCKs**.
  *False-positive baseline after the wave-4 dispersion fix:* **14** on PMID 18460020 (from 28),
  **0** table false positives (from 25), **13** unchanged on ~~PMID 20530675~~ **PMID 21731849**.
  Target: the wiring adds **no** new false positives against those two numbers, proven by
  re-running both papers before and after.

  > 🔴 **Corrected 2026-09-10 — the paper was misattributed, and this document's own rule is that
  > the record wins.** The wave-4 evaluation reads *"28 → 14 on this paper, table false positives
  > 25 → 0, and **the wave-1 paper unchanged at 13**"*; wave 4's paper is PMID 18460020 and the
  > wave-1 paper is PMID 21731849, named as such in the same evaluation's account of the reverted
  > absolute-line-floor fix. PMID 20530675 contributed a different datum entirely — the supplement
  > that went **12 → 1** in wave 1. Measured independently by two sessions on 2026-09-10 while
  > implementing § 9.5(b), each reporting 13 on 21731849 and 0 on the 20530675 supplement, and the
  > false-positive budget was held against the corrected attribution.
  >
  > **The propagation is the lesson, not the digit.** This line is a specification; the dispatch
  > that commissioned the work quoted it verbatim, so a number wrong in the record became a target
  > wrong in the task, and only a measurement caught it. It is § 9.4's own pattern — *an assumption
  > asserted with the confidence of a measurement, in a place too small to look at twice* — committed
  > by the document that names it.

### 9.6 · Make the attribution census a standing, parseable metric

**The finding.** This retrospective had to reconstruct § 5 by hand from nine prose diagnoses using
inconsistent vocabularies, and the reconstruction is contestable at the margins. Yet the underlying
number is the most decision-relevant thing in the record — it is what tells the operator whether to
invest in gates, in auditors, or in reader practice.

**Proposal.** `session_self_evaluation.md` gains one required block at the end of every diagnosis, in
a fixed parseable form:

```
ATTRIBUTION_CENSUS
incidents: <n>
machine: <n>   blind_auditor: <n>   peer: <n>   self: <n>
severity_high: <n>   of which self: <n>
undetected_known: <n>   # defects found later, attributed to this wave
```

The last two lines are the ones that carry information the aggregate hides (§ 5.2, § 0.3).

**Observable criterion.**
- A script parses the block from every `session_evaluations/*.md` in a date range and emits the
  ratios without a human reading prose. **Baseline: 0 of 9 diagnoses carry a parseable census; this
  document is the manual substitute and should not need to exist twice.**
- *The number to watch:* `severity_high self / severity_high total`. **This sweep: 3/6.** A rising
  ratio means reader practice is improving; a falling one means the gates are carrying more of the
  load than the readers are, which is the condition `scientist-a` named in wave 1.

### 9.7 · Persist `DEFAULTS_TAKEN` and `STOP_LOG` where a later session can find them

**The finding.** The brief mandates both, *"both, even when empty"*, and a repository-wide grep finds
`DEFAULTS_TAKEN` in **two** files — the brief itself and one commit candidate (§ 6.2, P5). Every
other default taken during ten unattended hours lived in a final message to the orchestrator, which
is a transcript. § 21c's safe-default mechanism is what allowed the sweep to run unattended at all,
and its evidence is almost entirely gone.

**Proposal.** `DEFAULTS_TAKEN` and `STOP_LOG` become required keys of the **task contract JSON**, per
wave, alongside `WAVE_n_RESULT` — the surface that already survives a session death and that every
actor already writes.

- *Observable criterion:* every `WAVE_n_RESULT` in every task contract carries both keys.
  **Baseline: 0 of 11 waves.** Target: 11 of 11 in the next sweep, and a later session can answer
  *"what did an actor decide without the operator, and why was it safe?"* from committed state
  alone. Secondary: the count of defaults taken per wave becomes a measurable, and an actor
  reporting zero defaults across a ten-hour unattended wave becomes visible as the anomaly it
  probably is.

### 9.8 · Declare a lot's internal dependencies at M0, not at M5

**The finding.** `scientist-b`'s own closing sentence for wave 5: *"A lot whose members cite each
other should be read as a set and said to be one at M0, not discovered to be one at M5."* The
cross-document finding of § 7.2(a) exists **only** because both papers were read in one wave, and the
actor *"nearly wrote the first dossier as if it stood alone."* The same shape recurred as the wave-6
debt closure and as `scientist-c`'s reagent-provenance finding.

**Proposal.** The dispatch resolves each lot's members against each other before assignment —
citation edges between assigned PMIDs, shared first/last authors, shared reagents where a prior
reading records them — and states the edges in the task contract. It is one query over data the
dispatch already has.

- *Observable criterion:* each task contract carries an `internal_edges` block. **Baseline: 0 of 3
  contracts carry one, and at least 4 real edges existed** — 25238781→25245215 (chapter of the same
  issue), 27551470→25245215 (ref 10), 18460020→16223882 (reagents), 20530675→16223882 (reagents).
  Target: the count of cross-document findings *discovered at M5* falls, and the count *predicted at
  M0 and then confirmed or refuted* rises. Both are countable from the dossiers.

---

## 10 · Not this analyst's to fix, restated so it is not lost

- **The four schema decisions of § 6.3** — `identity_correction`, the `first_read` /
  `legacy_reconstruction` gap, the panel-relation vocabulary on adjudicated locators, and
  `ARTIFACT_KINDS` for binary supplements — are reserved to the operator. All four were **referred,
  not improvised**, by the actors who hit them, which is the correct outcome and worth saying.
- **`BATCH_COMMIT`** is the only thing that clears `test_batch_queue`, and it is the operator's.
- **PMID 33914858** needs a human browser (§ 6.1 of [`2026-09-09.md`](2026-09-09.md)), and its text
  layer must be **re-tested rather than assumed clean** — this article is the repository's own worked
  example of a defective one.
- **The three unread primaries named by more than one actor** — `29808465`, `25411445`, `15126504` —
  are the highest-value reading debt this sweep produced, and § 7.3 is the reason: a repository whose
  load-bearing genotype facts sit in restatements it cannot check is carrying the compression it just
  measured.

---

*Disease-level, derived from public literature. Nothing here is medical advice. This is the public
edition and contains no individual-level record: where a private edition would reason about one
person, this reasons about the reference genotype, a WWOX-DEE genotype class.*
