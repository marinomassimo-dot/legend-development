# Session self-evaluation — `SLR-scientist-b-0006`

**Actor:** `scientist-b` · **Task:** `AQEILAN-FT-B-001`, **wave 6 — the wave that closes the lot**
**Date:** 2026-09-09
**Scope:** the last two PMIDs of eight, each taken M0→M5 and committed before the next —
**25245215** then **20146584**. Both `first_read`.
**Written BEFORE any closing report**, per the protocol's order of operations.

---

## Part 1 — executable verdicts (run first, not answered)

| Check | Verdict |
|---|---|
| `fulltext_receipts.py verify` | **OK** — 154 chained, tail anchored |
| `deepdive_manifest.py --pmid 25245215 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps, **21 locators / 5 artifacts** |
| `deepdive_manifest.py --pmid 20146584 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps, **15 locators / 1 artifact** |
| `session_self_eval.py` | **PASS** — no `[DECLARED GAP]` on either wave-6 PMID |
| `legend_lint.py .` | **PASS** (one pre-existing INFO on CLAIM 010, not mine) |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 |
| `genre_discriminator.py --self-test` | **24/24** |
| `test_deepdive_manifest.py` after the micro-upgrade | **94 tests, OK** (was 92) |
| Regression sweep over all 55 corpus manifests | **55 non-PASS before my change, 55 after, 0 implicating the new pattern** |

**On that last row, because it is the one that could have hidden a self-inflicted wound.** The 55 are
the pre-existing evidence-locality condition — `files/` is gitignored, the artifacts those manifests
fingerprint are not on this disk. I did not assume that. I grepped every one for my new signature
(`0` hits) *and* re-ran the whole sweep against `git stash`-ed code to get the before-count. Both
halves were necessary: the grep proves my pattern is not the cause, the stash proves the count did not
move.

---

## Part 2 — judgement

### Reading (Q1–Q3)

**Q1 — section by section, figures as images, tables?**
**25245215: yes, fully.** 11 pages, 26 sections read sequentially; **both** figures opened as images at
native resolution; Table 1 read row by row (19 partner rows) and joined against the resolved reference
list; 109 references enumerated by element.
**20146584: text yes, figures no — and that is the whole reason its receipt is partial.** 13 sections
read sequentially, 90 references enumerated and all 90 resolved from the deposit's own `<pub-id>`
elements. The two NIHMS figure assets sit behind a reCAPTCHA and **every other route is genuinely
exhausted**; `figures: captions_only` downgrades the receipt and I took the downgrade.

🔴 **Bad answer avoided, and it was available.** Both figures on 20146584 are, by their captions, a
cancer-summary diagram and a signalling schematic — exactly the kind I had just finished inspecting on
the sibling paper, where they turned out to be schematics. It would have been easy to reason "same
genre, same authors, I know what these look like" and record `figures: read`. That reasoning is
precisely D-14. **On the sibling paper, hours earlier, opening the schematic is what revealed a node
absent from both prose and caption (PHD2, with a printed `?`) and a caption naming an entity the panel
does not draw (VHL).** The cost of not seeing Figure 2 here is therefore *measured*, not hypothetical —
which is also why the downgrade is not a formality.

**Q2 — was the structured surface sought before the PDF, and its absence recorded?**
Yes, and this is where the wave's best process moment sits. On 25245215 Europe PMC `fullTextXML`
returned 404 ×3 and `efetch` returned the publisher's refusal comment, so **no XML surface exists** and
that absence is recorded per rule 5d. On 20146584, Europe PMC `fullTextXML` returned **404 again** —
the identical signal.

🔴 **I re-ran `efetch` anyway instead of generalising the sibling's failure, and it returned the
complete 129 KB deposit with no refusal comment.** Two articles, one wave, the same two endpoints,
opposite outcomes. Had I generalised, the lot's final paper would have been read off a PDF, or not at
all. *The lesson to carry: an endpoint's verdict is per-article, and a publisher's XML policy is not a
property of the journal.*

**Q3 — were quotes captured while the document was open, verified against the declared surface?**
Yes. All 36 locators were verified character-for-character against the validator's own extraction
**before** the manifest was written — 21 + 15, with the two abstract-resident candidates identified as
such and demoted to companion metadata rather than used as evidence.

### Discipline (Q4–Q6)

**Q4 — did I demote what the evidence did not earn?** **Three times, and each cost me a better story.**

1. **The term screen on 20146584.** Eleven of twelve terms zero. It was available to bank as a *fourth*
   independent confirmation of the structural absence. It is not one: the article is **February 2010
   and predates the description of WWOX germline disease**. There was no phenotype to omit. Recorded as
   a **chronological control**, and the demotion is written into the locator itself so a later reader
   cannot re-inflate it.
2. **My own wave-5 finding.** Wave 5 recorded the passive/active framing as having *moved* from
   *concluded* to *debatable* across thirteen months. Chapter 8 shows **both framings already coexisted
   in 2014 in the same author's own chapter**. The wave-5 observation stands as stated — it concerned
   the editor's summary of chapter 6 — but the *movement* narrative is weakened, and I wrote that into
   the dossier and the commit candidate rather than leaving the better story standing.
3. **The cooperation question.** Chapter 8's 2014 *"yet to be determined"* looked contradicted by the
   2010 review's citation of an insertional-mutagenesis screen. **It is not:** a retroviral insertion
   screen is not a targeted-deletion cross, so chapter 8's qualifier does real work. I recorded only
   the narrow, true statement.

**Q5 — checked-and-not-found recorded with its denominator?** Yes, and once it was later *closed*.
On 25245215 the internal growth-phenotype contradiction could not be adjudicated: this repository holds
ref [7] at complete depth but its dossier and manifest carry **no growth statement — 0 hits, 9 terms, 2
artifacts**. Recorded as reading debt rather than settled by picking the likelier sentence.
🔴 **Then the second paper of the same wave closed it**, giving the time course both chapter-8 sentences
compress: indistinguishable at birth, smaller by day 3, dead by 4 weeks, with bone growth retardation.
*Neither chapter-8 sentence is accurate alone.* **This is the clearest evidence in six waves that the
unit of work is the lot, not the paper** — and it only worked because the debt was written down in a
form the next reading could find.

**Q6 — did I stay inside my mandate?** Yes. No current file touched, no `BATCH_COMMIT`, no push, no
peer file edited. `scientist-c`'s untracked work on PMID 18460020 and a peer's untracked
`locator_identifier_provenance.py` were observed and left alone. **Derived surfaces were not
regenerated**, per my own wave-4 finding that is now policy, because a peer held untracked work on
disk — drift is reported below, not fixed.

### The weak answer, and what it cost

**Q — did I over-trust a screen because it returned the outcome I expected?**
🔴 **Nearly, and this is the wave's real finding about my own method.** The 25245215 PDF text layer was
`REFUSED` by the validator. Refused is the *right outcome*, and I could have stopped there — the surface
was excluded, the reading proceeded on clean HTML, nothing was harmed.

The coordinator's mid-task instruction is what stopped me: *finish the determination from the
validator's own code, and if the answer is that the validator screens less than rule 5d requires, that
is a finding to report, not a gap to route around.* Doing that showed the refusal fired for **two
incidental reasons** — 8 harmless front-matter `·` separators, and suspicion-by-absence — while
**`PRINTABLE_SUBSTITUTIONS` matched the actual defect with nothing**. The counterfactual, run rather
than argued:

```
as extracted                        REFUSED  (C0 control — a keyword separator)
C0 stripped                         REFUSED  (suspicion by absence)
C0 stripped + statistics reworded   ACCEPTED  ← Wwox?/-, Wwox?/?, Wwox?/mic all intact
```

**A green result for the wrong reason is the failure mode I shipped a whole tool about in wave 5**
(`genre_discriminator`'s design rule: *a screen whose failure mode is a silent pass is worse than no
screen*). I had the rule and still nearly accepted a refusal without asking what it was refusing *for*.
**The generalisation: "the gate said no" is not a finding; "the gate said no because X" is.**

---

## Part 3 — the capability micro-upgrade, and it is what the weak answer earned

**Shipped:** a fifth signature in `PRINTABLE_SUBSTITUTIONS` in `framework/scripts/deepdive_manifest.py`,
catching `?` welded to `/` where the page prints a superscript allele sign.

```
Wwox +/−  →  Wwox?/-      Wwox +/+  →  Wwox?/?      Wwox +/− mice  →  Wwox?/mice
```

- **Why it is needed even though the surface was already refused:** it was refused twice and for neither
  the right reason, and both incidental signatures are removable by ordinary variation in another paper
  from the same producer. The surface that survives them is one in which **wild-type and heterozygote
  are typographically indistinguishable** — the exact distinction rule 5d names as load-bearing.
- **Calibrated before shipping, the way the four existing signatures were:** screened over **all 45
  local text-bearing artifacts** in `files/fulltext/` (25 structured XML/HTML/TXT surfaces, 20 PDFs via
  `pdftotext`). **9 hits, all 9 in `PMID25245215_Aqeilan2014_PMC.pdf`, 0 in the other 44.**
- **Both halves tested**, as the module's own convention requires: one test that the substitution is
  caught and survives a "repair", one that the pattern does **not** fire on ordinary prose — a question
  mark ending a sentence before a slashed pair, a correctly-rendered `Wwox+/-`, and an ordinary
  `positive/negative`. Suite **94 tests, OK**.
- **Verified against the real artifact:** the previously-`ACCEPTED` counterfactual is now `REFUSED`
  **for the genotype reason**, not an incidental one.
- **Zero regression:** 55 corpus manifests non-PASS before and after, none implicating the new pattern,
  proven by grep *and* by re-running against stashed code.

**Why this and not something larger.** Proportionality. The wave measured exactly one gap, in a screen
this repository already relies on, and the fix is four lines of pattern plus two tests plus a
calibration. The `.pptx` / `ARTIFACT_KINDS` schema item stayed **escalated and unbuilt** — neither
wave-6 paper has a supplement of any kind, so nothing forced it, and it remains a schema decision
reserved to the operator.

---

## Part 4 — reported, not fixed

- **Derived-surface drift.** `coverage_report.md` and `reading_state.md` are generated files and are now
  stale with respect to both wave-6 readings. **Not regenerated**, per my wave-4 finding that is now
  policy: the generators read the **working tree**, and `scientist-c` holds untracked work on
  PMID 18460020 on disk, so regenerating would bake unlanded peer work into a shared surface under my
  name. Orchestrator action at wave close on a clean tree.
- **A live change in the acquisition environment, affecting every actor.** `pmc.ncbi.nlm.nih.gov` now
  serves a **Google reCAPTCHA** where it did not this morning. On 25245215 the trigger was **the
  browser-like User-Agent** — a request with *no* UA, and plain `curl`/`Wget` agents, returned the full
  262 KB article. `framework/scripts/pmc_pow_fetch.py` **cannot help**: it parses the older
  proof-of-work interstitial and raises on this challenge page. Later in the wave the challenge extended
  to asset paths regardless of UA, which is what cost 20146584 its figures.
- **`session_self_eval.py` reports `[DECLARED GAP]` on PMID 22193544** — no locator declares a `surface`,
  and `source_fulltext_indexed` is undeclared. Not mine, not touched. Flagged because 22193544 is the
  **D-14** paper and both wave-6 papers cite it.

---

## Part 5 — the one thing I would tell the next reader of this lot

**Write the debt in a form the next reading can find.** The growth-phenotype contradiction was recorded
on 25245215 as an explicit *checked-and-not-found with its denominator*, naming the PMID and the 9 terms
that returned nothing. Four hours later the next paper in the same wave closed it — not because I went
looking, but because the debt was specific enough that the answer was recognisable when it appeared in
an unrelated sentence about mouse pups. **A vague debt ("this needs checking") would have been invisible
at exactly that moment.**
