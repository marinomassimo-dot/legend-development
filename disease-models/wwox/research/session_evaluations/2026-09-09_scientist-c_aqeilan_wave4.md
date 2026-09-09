# Batch self-evaluation — `scientist-c`, `AQEILAN-FT-C-001` **wave 4, and the lot closes**, 2026-09-09

> Written **after** the executable gate returned its verdict and **before** capability scouting
> and the closing report. Takeaways written first describe a session that went well.

## Scope and executable verdict

- **Batch:** wave 4 of a 7-PMID lot — **one paper, the last one**. Mode `PRIMARY_EVIDENCE_READ`.
  Shared root checkout, branch `main`, three scientist actors concurrent.
- **Study:** `PMID 18460020` (Nakayama 2008, *Cancer Sci*) → `FTR-20260909-18460020-01`,
  `complete_fulltext_read`, `reread_reason: first_read`, `prior_receipt: null`.
- **`session_self_eval.py`:** `PASS` — *every complete read has landed and every declared output
  resolves*. receipts **150** · complete_fulltext_events **81** · active_complete_reads **70** ·
  unread_premises **3/3** (ratchet held; **not raised** by this batch).
- **Manifest:** strict `PASS`, **0 gaps**, schema v2, **34 locators** (22 text/table, 12 figure),
  run from the shared checkout with `--verify-artifacts --require-current-schema`.
- **Receipts:** `OK: 150 chained receipt(s), tail anchored`.
- **LINT:** `PASS` (one standing `[INFO]` on CLAIM 010, pre-existing and not mine).
- **Growth anchors:** `PASS` — claims 39 · papers 70 · corpus 356 · literature 390 ·
  registry_only 13 · unread_premises 3. **Not moved by this batch and correctly so:** this reading
  creates no PAPER record itself (it proposes one) and closes no registry-only declaration.
- **Local verdict:** the paper closed at `complete_fulltext_read` with **no waivers on any
  section**; the one waiver taken is `abstract_anchoring_waived`, argued and explicitly scoped so
  it cannot be read as a figure waiver.
- **Declared gaps in the corpus-wide run:** six manifests carry them; **none is mine**.

---

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplement | **15 of 15** main-figure panels read **as pixels** at 200–900 dpi, plus Table 1 read as text *and* re-read on the rendered page, plus one **authentic embedded raster** extracted for densitometry. **No `captions_only` anywhere.** Supplement `unavailable` with a four-route cascade. | `strong` | none |
| Main message vs. actual contribution | The paper's transferable content is **method, not biology**. Its own headline — WWOX loss as an early PanIN event — is the one claim with `WWOX AND PanIN = 1` behind it. | `strong` | none |
| Hidden gold beyond keywords/abstract | **Every quantitative statement in this paper is figure-resident** — the running text carries no P value and no dispersion statement at all. The missing Ad-WWOX histology arm, the MOI-10 decoupling, the undefined asterisk, the `Neural invasion` label and the absent loading control **exist only in the pixels**; a keyword search returns none of them. | `strong` | none |
| Source parity: context, type, recency | Read in full **because** it is oncology and pancreatic (`gold_is_in_the_details` rule 3), and the yield vindicated that: a 2008 Tier-C-shaped paper produced seven transferable method findings. | `strong` | none |
| Team type, field density, observation vs interpretation | 🔴 **Corrected an inherited framing:** the lot is the "Aqeilan sweep" and Aqeilan is **fourth of six**; the primary group is Yokozaki/Semba (Kobe). Weighting split **three ways** and written into the manifest. Counts **re-derived 2026-09-09**, closing the stale-count debt my own wave-1 evaluation raised against me. | `strong` | **wave-1 debt CLOSED** |
| DATO / INFERENZA / IPOTESI / ESPANSIONE | Every carried statement typed. Transfer verdict **`ESPANSIONE` / T3 / LOW**. Two `PREMISE: DEFAULT_FROM_TEXTBOOK` with revival triggers (mRNA-unchanged ⇒ post-transcriptional; polyUb ⇒ proteasome on the Smurf/Smad4 axis). | `strong` | none |
| Existing claims touched | **None.** R4 threshold re-run **mechanically** over all **18** `consolidated baseline` claims by a section-aware parse. 🔴 A bare `grep -c` reported **21**; three occurrences are prose inside a CLAIM 004 audit note. **Grep as a counting method would have made me re-derive a check I had already passed.** | `strong` | none |
| Multi-hop and corpus cross-query | 50 references enumerated, count confirmed independently by Crossref. The load-bearing hop — ref 21 = PMID 16223882 — **was already read in full by me in wave 3**, so the reagent dependency could be *checked* rather than assumed. | `strong` | one debt queued: ref 29, Kuroki 2004 |

---

## Persistence diagnosis

- **Durable IDs:** `DL-METH-112` and `DL-MECH-113` appended to the discovery ledger;
  `CC-20260909-18460020-01`; dossier `PMID18460020.md` (371 lines); manifest with 14 fingerprinted
  artifacts. **Nothing sits in `staging/`.**
- **Receipt binding:** bound to the **PDF** (`a345d0b4…`) as `article_binary` with the extracted
  TXT declared as `article_text`, exactly as the protocol requires for a PDF-only paper.
- **Coverage honesty:** `limitations: not_present` because the article **has no limitations
  section**; `supplementary: unavailable` with the cascade written down, never silently omitted.
- **Can a future run distinguish full text from abstract-only?** Yes, mechanically — and this
  manifest additionally declares `source_fulltext_indexed: **false**` with its evidence, which is
  the *harder* honest answer: a PMCID exists, but **a PMCID is a record, not an indexed body.**

---

## Process and capability diagnosis

- **Skills used / declined:** all nine recorded in `skills_considered` with reasons that would
  survive review, including the two the dispatch named — `oa_status_dissent.py` (used, **returned a
  true negative**, credited as such) and `find-fulltext` (declined, cascade terminated at tier 2).
- **Failures, and what caught each:**
  1. **The task contract's own acquisition hint was false** (`pmcid: null`, `free_sites: []`), and
     the 2026-09-08 pre-flight and Europe PMC agreed with it. Caught by **this repository's own
     memory** — the corpus seed and the surface census — not by any tool.
  2. `pmc_pow_fetch.py` on the article HTML: `ValueError`, not a POW page. → reCAPTCHA; rerouted.
  3. Receipt append refused: `unknown fields: ['references']`. **The writer, not me** — `references`
     is the optional *tenth coverage key*, not a top-level field.
  4. Manifest `BLOCK`: `landing` must name records, not a URL. **The validator, not me.**
  5. Manifest `BLOCK`: `source_fulltext_indexed` undeclared. **The validator, not me** — and it
     forced the honest `false`, which is the more useful record.
  6. My micro-upgrade's first fixtures failed **three** ways; see below.
- 🔴 **Two lines of my own reasoning tested and REFUSED**, and this is the part of the session I
  most want reviewed:
  - I believed Fig 3c contradicted Fig 3d. I measured colony density; the measurement disagreed
    with my eye **and** with the reported counts **in an inconsistent direction** — the signature of
    a confounded measure. The Mock plate is rendered at a different scale and background. **Line
    discarded.**
  - I believed the β-actin in Fig 5c dipped in the Mock lane and inflated the Smad4 result.
    Densitometry on the authentic embedded raster says the **opposite**: Mock and pWWOX are well
    matched, and **the paper's central in vitro claim survives at 2.69× after normalisation.**
  **Both are in the dossier at the same prominence as the findings that held.** A reading that
  reports only its successes is not a reading.
- **The instinct the dispatch told me to keep, used twice:** the `_refuse_suspect_surface` green
  was accepted only after proving the same call **refuses** a corrupted string — and after
  re-confirming that the zero-argument shape still returns a meaningless green.

### Micro-upgrade, and its three failures

`text_surface_intrusion_check.py` — the tool I shipped in wave 1 — **produced 25 false positives on
this paper.** `TABLE_ROW_RE` excludes table rows by their wide inter-column gaps, and PyMuPDF emits
**one cell per line**, so there were no gaps to find and Table 1's values were reported as page
furniture. 25 false positives on a 7-page paper is enough noise to make a reader ignore the three
real ones — which is the failure that matters.

Fixed by a **dispersion** test, chosen by *measuring both classes on two real papers* rather than
guessed: genuine furniture spans 53.7–111.5% of a document, table cells 2.7–7.6%; the threshold sits
in an empty band an order of magnitude wide. Result: **28 → 14 on this paper, table false positives
25 → 0, and the wave-1 paper unchanged at 13.**

🔴 **Three failures during the fix, each recorded because each changed the design:**
1. An **absolute line floor** ("furniture must cross about a page") separated the classes just as
   cleanly — **and silenced the suite's oldest regression**, the real PMID 21731849 header, whose
   fixture is a short extract. **Reverted.** Breaking a genuine existing regression to remove a
   false positive is the wrong trade, and the rejected design is recorded in the docstring so the
   next reader does not re-propose it.
2. My first fixtures were 34 lines — not documents. A ratio is meaningless on an input where one
   table honestly occupies most of the text. Lengthened to realistic size.
3. My "genuine header still caught" fixtures returned **nothing**, and **the tool was right**: I had
   repeated *one* sentence around every header, so those sentences became furniture themselves, and
   a furniture line between two furniture lines is correctly not an intrusion into a sentence.
   **The fixture was wrong, not the tool.**
- **A counterexample decided the shape of the fix and is now locked in a test:** the `|` separator
  of a running header spans 70% of the document with a **median gap of 2**. A gap-based test — the
  obvious alternative — would have thrown away real furniture to remove false furniture.

---

## The three failure modes the protocol warns about — checked against my own answers

- **Answering yes to everything:** the two refused lines above, plus a reverted design and three
  admitted fixture failures. The wave-1 stale-count debt is **closed**, not re-promised.
- **Grading the outcome instead of the process:** the outcome was strong — a missing experimental
  arm, an invalid declared test, an undefined asterisk. The **process** still shipped a tool that
  produced 25 false positives on its second production paper, and *that* is graded here, separately
  and worse.
- **Writing the diagnosis myself and calling it evidence:** four of six failures above were caught
  by **tooling, not by me** — the receipt writer twice, the manifest validator twice. The two I
  caught myself were caught by *disbelieving my own eye and measuring*, and one of those measurements
  told me I was wrong.

---

## Residual risk and next decisive action

1. **Derived-surface drift, reported and deliberately not fixed** (dispatch instruction):
   `reading_state.md` has **no row** for 18460020 and no derived surface names its receipt. The tree
   is clean; the orchestrator regenerates at wave close.
2. 🔴 **A per-PMID retraction check cannot see the integrity status of the papers a paper depends
   on.** 18460020 is clean and draws its virus and both antibodies from a paper under a standing
   expression of concern. `CC-20260909-18460020-01` proposes a `Reagent provenance:` field; **if the
   registry schema has no such field, the finding is that it needs one.**
3. `text_surface_intrusion_check.py` is **still not wired into any gate** — the wave-1 residual risk,
   **unchanged after a second production run that proved it earns its place.** Wiring it into
   `deepdive_manifest.py` for PDF-derived surfaces remains the obvious next step and was again
   deliberately not done in the same change as a behavioural fix.
4. The `identity_correction` contract finding and the `surface: figure` coupled-relation finding
   remain **referred to the operator**, unimplemented and not worked around.
