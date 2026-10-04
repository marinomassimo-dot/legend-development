# MIRROR ex-post review — BATCH_20261004_004 and BATCH_20261004_005

`REVIEW_ID` MIRROR-20261004-BATCH20261004004-005 · `OBJECT` **two consecutive batches**:
`BATCH_20261004_004` (intake wave 10, the PMID 21476439 enzymology reading, the Steinberg 2026
re-read, the `GSK3B-S9` `D6` landing, Mirror repairs 31–35 and the privacy repairs,
`WM_v7.16` → **`WM_v7.17`**, landed `21fc25a2`; report `2026-10-04_BATCH_20261004_004.md`) and
`BATCH_20261004_005` (intake wave 11 + `CC-20260826-CLAIM003-01` re-authored and consumed,
`WM_v7.17` → **`WM_v7.18`**, landed `a1536ad9`; report `…_005.md`) · measured on `main` at
**`a2d69a08`**, which contains both · `LEVEL` ex-post review on the operator's request, including
the two binding conditions of `MIRROR-RULING-20261004-D6`, which this reviewer issued ·
`REVIEWER` ACTOR_ID `mirror` · `AUTHORS` ACTOR_ID `scientist` (Scientist N and Scientist O) ·
`ADJUDICATOR` the authors, as new tasks.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect
> found given the available evidence bundle", never "true". READ-ONLY toward every registry: this
> review writes one file and two candidate files and edits no canonical record. **Not medical
> advice.**

**Method.** Registry records were addressed by heading span and printed field by field, never by
grepping the two large registries as text. Artefacts in the root `files/` tree were read in place,
read-only, through tag-stripping keyword-window scripts, addressed table cells and rendered pages.
Every ratio and every panel value below was re-derived from the two numbers or the pixel geometry
its record names; Table II of PMID 21476439 was re-read on a 160-dpi render of the rotated journal
page 80, and Figure 2F of PMID 42397075 on the 600-dpi panel asset, with the axis ticks measured
(152.75 px per log2 unit) before any bar was called.

---

## STEELMAN (first)

- **The 14-Km arithmetic is exact, and it is the kind of statement no gate here can check.** From
  Table II and Table I, re-read cell by cell on the rendered page: **13 of 14** apparent Km values
  lie below the lowest substrate concentration that substrate was given, and the **single**
  exception is **testosterone with NADP⁺** (14.551 ·10⁻⁵ M against a lowest [S] of 7.5 ·10⁻⁵ M).
  I re-derived all 14 comparisons independently; the tightest non-exception is
  5α-DHP-allo/NADP⁺ at 4.702 against 5.0, which the record's claim survives. The printed
  Mann-Whitney p values (0.0000–0.0091) are all below the floor of an exact two-sided test at the
  paper's own *«at least two or three»* (0.333 at n=2+2, 0.100 at n=3+3), and the record labels
  that as a DERIVATION rather than an error of the source.
- **`PAPER 244` carries the source's own word.** *«The WWOX cDNA fragment restricted by BamHI and
  EcoRI…»* is the paper's sentence; **`full-length` appears nowhere as an assertion** — the record
  carries it only as the derivation it withdraws. The motif attribution is withdrawn in both
  surfaces: the `GANSGIG` (131–137) / `YNRSK` (293–297) sentence does carry **no citation of its
  own** in the artefact, and `PAPER 244` and `LIT-0306` both say so. `TX-003` was not touched by
  either batch (no therapeutic file in either diff).
- **The `D6` landing satisfies both conditions I made binding.** `CLAIM 016` and `CLAIM 035` each
  gained **exactly one line**, in the **same batch**; per-line sha256 over both records shows
  **0 lines removed, 1 added** on each side; `Status`, `Type`, `Summary` and `Source` are
  byte-identical on both; both horns are stated open and **neither is resolved**; and no
  mutual-corroboration wording survives anywhere in either record — what survives is the
  prohibition on citing one as corroboration of the other.
- **Figure 2F recomputes to the digit.** With x(0) at px 1244 and 152.75 px/unit, the WWOX-KO `Neu`
  bar is **−2.40** (366 px) and the `RGs` bar **+1.00** (153 px): the correction from −2.6 to −2.4
  and the +1.0 radial-glia figure are both right, and the old value was wrong.
- **The privacy repairs are complete and measurable without reproducing a single string.** Across
  every file the two batches touched, added lines contain **zero** occurrences of either
  transmitting-side term of the gate's own vocabulary (the one `parent-of-origin` occurrence per
  batch is a policy sentence in the report); batch 004 *removed* such wording from the claim
  registry, the literature log, the paper
  registry, one candidate and one manifest. `public_release_gate.py`: **PASS, 0 BLOCK**, and no
  `[REVIEW]` line names any record either batch authored.
- **Depth discipline is exact across 11 new records.** `fulltext_receipts.py status --pmid` returns
  `complete_fulltext_read` for 40083435, 40884527 and 21476439 and `partial_fulltext_read` for the
  other eight; **every** partial record carries the literal **partial full text**, and the one
  unread landing (`CORPUS-STUB-185` / `LIT-0544`, PMID 33726816) says *«no reading was performed
  and no receipt is owed»* instead of borrowing a depth it does not have.
- **Identity was measured, not copied.** `PAPER 245` (Cancer Gene Ther 30(8):1144, 14 authors),
  `PAPER 246` (Front Pediatr 13:1471965), `CORPUS-STUB-183` (Epilepsia Open 10(5):1605) and
  `CORPUS-STUB-184` (IJMS 26(17):8521) all match their JATS front matter field for field, and
  `CORPUS-STUB-184`'s title is truncated by the privacy rule with the omission declared.
- **The counting discipline holds arithmetically.** Four sources × (2+1+1+1) children gives the
  landed range **2–5 children in 1–4 families**, and the lower bound is the sibling pair; Beretti
  prints `WWOX (n = 2)` of **56** enrolled and of **35** solved (56 − 21 unsolved = 35), and
  neither is turned into a case; `WWOX` occurs **exactly three times** in Panchenko (Introduction,
  Discussion, one reference title), as `CORPUS-STUB-184` states.
- **`CLAIM 003`'s re-authored statement is right where it matters.** On the artefacts:
  *«we examined MBP staining in O-KO and control littermates at P17 and found no major changes
  (Supplementary Fig. 8)»*; the legend reads *«Conditional ablation of Wwox in **OPCs** does not
  impair myelination in O-KO at P17»* — the batch's own correction of *oligodendrocyte-specific*
  is right; the clasping test is Supplementary Fig 2D at **P18**; the O-KO survival arm is
  *«O-Control, n = 11 and O-KO, n = 10, P-value 1.0»*; and **cuprizone** and **lysolecithin** occur
  **zero** times in the article and **zero** times in the complete supplement, which is exactly the
  measured absence the record claims.
- **Taouis is carried at the strength of a co-IP.** WW1-WW2 *«did not interact»*, WW2-SDR *«did»*,
  the authors *«suggest»* the N-terminal part of the SDR domain, Y33R retains binding, and a
  hostile search for an affinity constant or a stoichiometry returns **0 hits**. And the record's
  own independence caveat checks out: **Aqeilan RI is author 11 of PMID 22634283**.
- **The isodisomy rule is class-level.** *«Homozygosity is not proof of two carrier parents»* names
  no side, no individual and no family; it speaks of consanguinity and of segregation in one
  parent, which is the genotype-reading rule, not a transmission record.

---

## Verdicts by area

| # | Area | Verdict |
|---|---|---|
| A1 | `D6` on `CLAIM 016` **and** `CLAIM 035`: one batch, both horns open, no `Status`/`Summary` change, no mutual-corroboration wording left | **CONFIRMED** — per-line sha256: 0 removed / 1 added on each record; both still `in observation`; both conditions of `MIRROR-RULING-20261004-D6` satisfied |
| A2 | PMID 21476439 records (`PAPER 244`, `LIT-0306`, `CORPUS P306`, `FT-130`, `FT-147`): *cDNA fragment* vs *full-length*; motif attribution; `TX-003` | **CONFIRMED** — the source's own *fragment* wording carried; *full-length* appears only as the withdrawn derivation; motif attribution withdrawn in both records; `TX-003` untouched · 🔸 **F2** `LIT-0306`'s triage fields |
| A3 | The 14-Km arithmetic and the Mann-Whitney floor, recomputed from Table II on the rendered rotated page 80 | **CONFIRMED** — 13/14 below the lowest [S], exception testosterone/NADP⁺; all 14 p values unattainable at n = 2–3 |
| A4 | PMID 42397075 records: cell fraction −2.6 → **−2.4**, `RG` **+1.0**, the earned glial null, artefact-digest instability, `CLAIM 002/003/005` boundary-text-only | **CONFIRMED** — both panel values recomputed from axis geometry; the three claim records gained appended boundary text and nothing else · NOTE **F3** |
| A5 | Privacy repairs: no parent-of-origin pairing in the records, manifests and candidates either batch touched | **CONFIRMED by script, no string reproduced** — zero occurrences of either transmitting-side term of the gate's vocabulary in added lines of either batch; removals where the repairs said |
| B1 | `CLAIM 003` re-authored statement vs the Repudi artefacts on rendered pages (PDF + supplement File009) | **CONFIRMED on substance** — quantitative-vs-qualitative split, MBP P17, clasping P18, survival n/P, zero challenge experiments · 🔴 **F1** the page number |
| B2 | The isodisomy rule in the working model: any parental-side wording? | **CONFIRMED — none.** Class-level throughout |
| B3 | `PAPER 245/246`, `CORPUS-STUB-181`–`189`, `LIT-0539`–`0548`: identity vs JATS front matter; depth labels vs `fulltext_receipts.py status --pmid` | **CONFIRMED 11/11 on depth** (3 complete, 8 partial, every partial carrying *partial full text*) **and on the four identities I re-measured from front matter** |
| B4 | `H322R`, the `L239R` range, Beretti 2 of 56, Taouis mapping, Aqeilan on PMID 22634283 | **CONFIRMED** — ClinVar `VCV000241108` is *Uncertain significance*, 3 submitters, no conflicts; *one family* is labelled INFERENZA; 2–5 in 1–4 recomputes; 2/56 and 2/35 are the artefact's; no Kd or stoichiometry exists; Aqeilan is author 11 |
| C | ≥12 carried quantitative statements re-measured against artefacts | **CONFIRMED 15/16**, the exception being **F1**; see STEELMAN for the list · NOTE **F4** |
| D | Per-line sha256 prohibition spans for `CLAIM 002/003/005/011/016/019/032/033/035/045/046/047` | **CONFIRMED** — 12/12 records: 6 untouched, 5 pure insertions, and **one** replacement, which is `CLAIM 033`'s `CC-20261004-MIRROR-32` privacy repair. **Zero** prohibition lines removed |
| E | `public_release_gate.py` over the whole tree | **PASS, BLOCKS: 0**, 29 `[REVIEW]`, none in a record either batch authored |
| F | Overstatement vocabulary in added lines | **CONFIRMED** — every *first* / *only* / *unique* is scoped to *«the read corpus»*, *«this paper»* or *«identified in the corpus read here as of…»*, each an in-repo falsifiable statement |
| G | Gates at the measured state | **CONFIRMED** — LINT exit **0**; `fulltext_receipts verify` **OK, 458 chained, tail anchored**; `growth_anchors check` **PASS** (claims 47 · papers 236 · corpus 376 · literature 529 · registry_only 4 · unread_premises 0), with a backlog decision due on 14 candidates of wave 12 |

---

## F1 — the one in-batch "correction of fact" that corrected a right value into a wrong one (🔴 MINOR, `CC-20261004-MIRROR-41`)

`CLAIM 003`'s new boundary states that the MBP sentence *sits on journal page 3072*, and marks
3071 as the batch's own superseded draft. **Measured on the artefact: it is on page 3071.** The
sentence is on PDF page 11, whose printed folio is `| 3071`; PDF page 12, folio `3072`, contains
zero occurrences of it. This repository's own `deepdive_manifests/PMID33914858.json` anchors that
Results section to *«journal page 3071 (PDF page 11)»* in two separate locators, so the landed
text now contradicts both the source and the manifest it was read from.

```bash
pdftotext -f 11 -l 11 files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf - | grep -c "MBP staining in O-KO"   # 1, page header "| 3071"
pdftotext -f 12 -l 12 files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf - | grep -c "MBP staining in O-KO"   # 0, page header "3072"
```

Severity is MINOR — it is a locator, the quoted sentence and the endpoint attribution are right,
and no measurement moves — but it sits inside a `consolidated baseline` claim and it was landed as
a *correction*, which is the shape most likely to be trusted later. The `_005` report and
`CC-20260826-CLAIM003-01` carry the same figure; those are history and this review proposes no
edit to them.

## F2 — `LIT-0306` says READ IN FULL in one field and *no deep-dive yet* in five others (🔸 MINOR, `CC-20261004-MIRROR-42`)

`BATCH_20261004_004` updated four fields of `LIT-0306` and left the triage-era fields behind. The
record now reads `Current status: READ IN FULL 2026-10-04 … registered as PAPER 244` beside
`Status: screened`, `Filter decision: deep-dive — full text required`,
`Flags: FASE 1 batch entry / no deep-dive yet`, `Over-inference risk: standard triage — not
evaluated`, `Working Model impact: none yet` and `Date last touched: 2026-04-18`. The convention
is not in doubt: of `LIT-0533`–`LIT-0548`, **15 of 16** read records carry `Status: processed`, and
the sixteenth (`LIT-0544`) is `screened` **because it was not read** and says so in a `Status
note`. `PAPER 244` meanwhile carries `Status: processed` and `Over-inference risk: HIGH`, so the
two surfaces of one reading disagree. A reader filtering the log by `Status` or by `Flags` — which
is what those fields are for — does not find the corpus's only enzymology primary.

```bash
python3 <scratchpad>/mir_field.py disease-models/wwox/registries/literature_tracking_log_current.md '^## LIT-05(3[3-9]|4[0-8])$' Status
```

## F3 — two record separators where one belongs (NOTE, no candidate)

`paper_registry_current.md` carries `---`, a blank line and `---` between `PAPER 244` and
`PAPER 245`: batch 004 ended the file with a separator after `PAPER 244`, and batch 005 opened its
first appended record with another. Cosmetic — LINT is green and `registry_records.py` segments
both records correctly — and filed as a NOTE because a surgical edit to a separator is a worse
risk than the blemish. Worth folding into the next edit that touches either record.

## F4 — one hand-read panel value is 16 % further from zero than the record says (NOTE, no candidate)

`PAPER 094` describes SCAR12's radial-glia deviation as *about −0.25*. Measured on the same axis
calibration that confirmed −2.40 and +1.00, the bar runs 1200→1244 px, i.e. **−0.29**. The word
*about* covers it, the sign and the ordering the record argues from are unaffected, and WOREE's
*+0.05 to +0.08* measures +0.08–0.09. Noted so the next reader of that panel knows the geometry
has been taken, not so the sentence changes.

---

## Where I could be wrong / `WHAT_WOULD_CHANGE_MY_MIND`

- **F1** would fall if this repository anchored by PDF page or by the page a figure is printed on
  rather than by the folio of the page carrying the sentence. It does not: the manifest's own
  anchor for that section says *«journal page 3071 (PDF page 11)»*, and the landed text names a
  *journal page*.
- **F2** would fall if `Status` in the literature log meant *triage state at discovery* rather than
  *current state*. Fifteen sibling records written by the same two batches say otherwise, and the
  one exception documents itself.
- **The `D6` verification is byte-level, not semantic.** I measured that no `Status`, `Summary` or
  measurement changed and that both horns are open; whether the boundary's *reasoning* is the best
  available reading of two single-lane densitometries is not a Mirror call and is not settled here.
- **A5 is a measurement over added lines**, not over the whole corpus: a parental pairing that
  survived in a line neither batch touched would not appear in it. The gate's whole-tree run (E)
  covers that, and it is green with 0 BLOCK.
- **C re-measured what the records name.** Figure values I could recompute I did; a number a record
  omits is invisible to this check, and the Fig 2F calibration rests on five printed tick centres,
  not on the authors' data.
- **F counted vocabulary, not rhetoric.** A record can overstate using none of those words.

---

## Candidates written by this review

| Candidate | Finding | Ops | File |
|---|---|---:|---|
| `CC-20261004-MIRROR-41` | F1 | 1 | `registries/claim_registry_current.md` |
| `CC-20261004-MIRROR-42` | F2 | 6 | `registries/literature_tracking_log_current.md` |

Each `old` was measured **unique inside its record** immediately before the candidate was written,
and each candidate says the propagating batch must re-measure it.

---

## DEFAULTS_TAKEN (§21c)

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| `files/` is outside the worktree | Read the root tree in place, read-only, through window scripts and renders | No byte written under `files/` | A copy this review did not need |
| The worktree was cut from an older `main` | Fast-forwarded the task branch to `main` `a2d69a08`, which contains both batches, before measuring | Both landings are ancestors of the measured tree | Measuring a tree neither batch produced |
| Two batches, one review file, as the brief directs | Verdicts keyed `A*` (batch 004) and `B*` (batch 005), shared checks `C`–`G` | Nothing is attributed across batches | Two files and a duplicated method note |
| A safety classifier stopped one turn mid-call (a shell-quoted grep pattern) | Rewrote the **call**, never the content, and moved every later read to small addressed scripts | No wording was reworded or retried; every figure here carries its command | A reworded retry, which the brief forbids |
| `growth_anchors check` reports a 14-candidate backlog | Attributed to intake wave 12, which landed after both batches, and **not** counted against either | Every named candidate is a `…W12-…` file neither batch wrote | A finding about another actor's queue |
| Two findings are cosmetic or a hand-reading tolerance (F3, F4) | Filed as NOTE with the measurement named, no candidate | A candidate for a judgement call pre-empts the author | Two candidates nobody asked for |
| Findings need registry edits Mirror may not make | Wrote two candidates with exact ops and `old` measured unique in its record | §21e: a finding is a new task for the author | A Mirror registry edit, which the role contract forbids |

**Review path:**
`disease-models/wwox/research/session_evaluations/mirror_review_batches_20261004_004_005.md`

**Not medical advice.**
