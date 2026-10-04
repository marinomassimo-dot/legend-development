# MIRROR ex-post review — BATCH_20261004_001

`REVIEW_ID` MIRROR-20261004-BATCH20261004001 · `OBJECT` `BATCH_20261004_001` (intake wave 7,
`WM_v7.13` → **`WM_v7.14`**, 15 candidates, one of them merged) landed on `main` at **`2de75c1`**,
pre-batch base `520c726`; measured on `main` at `761b369`, which contains it · `LEVEL` ex-post
review on the author's request (report *Recommended next actions* item 3) · `REVIEWER` ACTOR_ID
`mirror` · `AUTHOR` ACTOR_ID `scientist` (Scientist K, batch integrator) · `ADJUDICATOR` the
author, as a new task.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect
> found given the available evidence bundle", never "true". READ-ONLY toward every registry: this
> review writes one file and four candidate files and edits no canonical record. **Not medical
> advice.**

**Method.** Artefacts in the root `files/` tree were read read-only and **only through scripts**
that print hit counts, byte offsets, single addressed table cells and bounded context windows.
Registry records were addressed by heading span, printing field names, truncated values, byte
lengths and sha256. A safety classifier halted one turn immediately after a wide keyword dump from
the Lange 2026 artefact; it was **not reworded or repeated**, and every later artefact read used
narrow windows (`kw.py … 120 3`-scale) instead.

---

## STEELMAN (first)

- **The batch caught, first-hand, the one defect class no gate in this repository can see, inside
  the only baseline-touching edit it made.** A blind auditor returned `CONTRADICTED` on the central
  sentence of `CC-20261004W7-A-ASTROCYTE-01`; the integrator re-verified it in the artefact and
  withdrew a universal quantifier from a `consolidated baseline` claim. Every statement the landed
  `CLAIM 005` note makes about PMID 42558002 reproduces in the artefact: the four WWOX rows read
  `Unclear` · *«Unclear, as age of seizure onset not reported»* · `Unclear` · **`N/A`**, *«No
  astrocyte changes reported»*, and the direction is carried by the **neuron**-conditional
  knockout's GFAP correlation with the astrocyte-knockout negative as the concessive clause, word
  for word as the note quotes it.
- **The arithmetic repair is right in both directions.** 0.004638 / 0.002756 = **1.683** at **2×**
  the dose → **15.9 % lower** per vector genome («about 16 % BELOW»); the within-day-5 IV step
  0.003111 / 0.001862 = **1.671** («1.67×»); the ICV comparison 0.396319 ± 0.295485 against
  0.293985, **n = 10 each** — every one of those six numbers is a Rioux appendix table cell,
  verified cell-wise.
- **The `DL-METH-117` merge states each carried quantity with the surface it came from.** *«1 ×
  10¹⁰ vg … per pup»* and *«For a P2 pup (~2.0 g body weight), this corresponds to approximately
  5.0 × 10¹² vg/kg»* are verbatim; 10 / 0.04 = 250 is the source's **own** *«250× scale up»*;
  8.0 × 10¹¹ × 250 = 2.0 × 10¹⁴ matches the printed macaque total; the 1–2 kg (GLP, SNBL) and
  2–4 kg (non-GLP) weight ranges and the 3.05 × 10¹⁴ vg/animal NOAEL and the 5.0 × 10¹⁴ / 1.0 ×
  10¹⁵ human starting doses are all printed where the record says.
- **Depth labels are the receipts', not the records'.** All twelve integrator-authored papers carry
  the depth their receipt states, and every `partial_fulltext_read` record carries the literal
  **partial full text** that `coverage_report.PARTIAL_MARKERS` needs.
- **The `LIT-0151` / `CORPUS-STUB-132` repair is two-sided and vocabulary-safe.** `LIT-0494`
  declares *supersedes*, `PAPER 201` declares *promotes*, and — checked in the checker —
  `classify_depth` reads `superseded` into `FILTERED_STATES` and the stub into `catalogued`, so
  neither retired twin can be counted as a second reading.
- **Prohibitions stayed attached.** Per-line sha256 inside `CLAIM 005` / `032` / `033` / `045`:
  **0 lost**, 2 new, every surviving digest byte-identical.

---

## Verdicts by area

| # | Area (the author's own focus list) | Verdict |
|---|---|---|
| A1 | `CLAIM 005` note vs the artefact; direction and attribution | **CONFIRMED** — four rows, three `Unclear` + Repudi `N/A`, neuron-cKO GFAP attribution, both quotes verbatim, section names right (narrative review, no Results) · 🔴 **F1** the withdrawn quantifier survives in `PAPER 202` |
| A2 | 12 integrator-authored records (`PAPER 205`–`216`, `LIT-0497`–`0508`) vs JATS front matter | **CONFIRMED 11/12** on DOI, PMCID, journal, volume, issue, pages/elocation and author order · 🔸 **F3** `PAPER 214` / `LIT-0506` · NOTE **F7** |
| A3 | Depth labels vs `fulltext_receipts.py status --pmid` | **CONFIRMED 12/12**; 7 complete / 5 partial as the receipts read; every partial record says `partial full text` |
| A4 | `DL-METH-117` merge: each quantity with its source, ratios recomputed | **CONFIRMED** — see STEELMAN; the repaired IV cerebral statement recomputes exactly |
| A5 | Four in-place Grubor corrections, § 7.2 verbatim; `FT-193` identity line | **CONFIRMED** on the identity line (`queue_entry_identity` → `resolved`, the PMID leads) and on 5 of 6 quotes · 🔸 **F5** the `DIS-031` quote · NOTE **F6** |
| A6 | `intron 8` label; the Zhao-splice statement on the acceptor allele | **CONFIRMED** on the acceptor disclaimer — `CLAIM 033` *«It says NOTHING about what the reference genotype's acceptor allele does»*, `DL-BIO-002` *«Non dice nulla sull'allele accettore del genotipo di riferimento»* · 🔸 **F4** `PAPER 210` |
| A7 | Patient-overlap labels; no patient counted twice | **CONFIRMED** — `PAPER 143` *«count at most three and possibly two p.Arg264* homozygotes»*, `PREMISE: INFERENZA`; `PAPER 171` *«count it once as unlinked»* for the `c.606-1G>A` homozygote, Tabarki named as neither matchable nor excludable, and the Tunisian heterozygous deletion explicitly barred from bearing on it; `PAPER 205`'s two Turkish cases verified cell-wise (Table 2 rows 29 F infantile GES, 51 M neonatal GES) and entered as new |
| A8 | Prohibition spans, per-line sha256 before/after | **CONFIRMED** — `005` 0→0, `032` 7→8, `033` 1→2, `045` 3→3; **0 removed** anywhere |
| A9 | `LIT-0151` retirement / `CORPUS-STUB-132` promotion two-sidedness | **CONFIRMED** — both pointers present, both statuses in their surfaces' own vocabularies, neither double-counted by `coverage_report` |
| A10 | Overstatement vocabulary in added lines | **CONFIRMED 25/26** — 26 hits (13 `first`, 4 `establish*`, 4 `demonstrat*`, 2 `primo`, `novel`, `shows that`, `confirms`), every one negated, quoted, bibliographic or qualified · 🔸 **F2** the one that is not |
| A11 | Gates at the landed state | **CONFIRMED** — `public_release_gate.py` exit **0**; `fulltext_receipts verify` **OK, 409 chained**, tail anchored; `growth_anchors check` **PASS** (claims 45 · papers 206 · corpus 366 · literature 489 · registry_only 4 · unread_premises 0); LINT exit **0**, **0 BLOCK**, 13 `WARN_BUT_PROCEED`, **none naming any wave-7 record**. The backlog counter now reads **16** — the wave-8 candidates, not this batch's debt, and the batch's own proposal on the five-candidate residue is thereby measured right |

---

## F1 — the quantifier the batch withdrew is still in `PAPER 202` (🔴 the batch's own correction did not propagate, `CC-20261004-MIRROR-21`)

`CLAIM 005` now says three rows and names the fourth as `N/A`. `PAPER 202`, the record for that
very article, still says **`Short title:` … all four WWOX rows marked Unclear on cell autonomy**
and **`Role:` … 🔴 Every one of its four WWOX rows is marked **Unclear** …**. The claim and its own
source record contradict each other, and the sentence a blind auditor falsified is the one a reader
of the paper record gets. A sweep for the phrasing finds it in exactly these two fields and nowhere
else (`LIT-0495` is clean).

```bash
python3 <scratchpad>/intron.py   # the same sweep, re-run for the quantifier phrasings
```

**Fix:** `CC-20261004-MIRROR-21` — two `replace-within` ops on `paper_registry_current.md`.

## F2 — an unmeasured *«first»* in the same `Role` field (🔸 MINOR, same candidate)

*«The first third-party, non-WWOX group to tabulate the WWOX astrocyte evidence»* is the one
occurrence of the overstatement vocabulary in this batch's added lines that is neither negated,
attributed, quoted nor measured. No search for an earlier such table is recorded anywhere in the
batch. It sits in the sentence F1 rewrites, so one op carries both.

## F3 — the journal's Academic Editor is listed as an author (🔸 MINOR, `CC-20261004-MIRROR-22`)

`PAPER 214` and `LIT-0506` give *«Gao H, Xu T, Lebleu B»* for PMID 42511902. The JATS front matter
has two authors (`contrib-group content-type="author"`: Gao Haitong, Xu) and puts Bernard Lebleu in
`contrib-group content-type="editor"`, role **Academic Editor**. This is the one identifier error
in twelve records whose whole point was to measure identity from the front matter rather than from
a candidate's prose — and the MDPI editor group is exactly the trap that pattern exists to avoid
(three other MDPI/PLOS records in the same set — `PAPER 207`, `213`, `215` — got it right, each
excluding its own academic editor).

```bash
python3 <scratchpad>/contrib.py files/fulltext/PMID42511902_Gao2026_PMC.xml
```

## F4 — `intron-8` is asserted in `PAPER 210` where the claim labels it `INFERENZA` (🔸 MINOR, `CC-20261004-MIRROR-23`)

The batch's narrowing №1 established that PMID 42248868 numbers no intron; `CLAIM 033` and
`DL-BIO-002` carry the `INFERENZA` label and quote nothing for it. `PAPER 210`'s `Genotype/model`
says *«(intron-8 donor +5)»* flat. Measured: this batch added exactly **one** new hyphenated
`intron-8` to the paper registry, and it is this one. The label did not reach every place the
derivation is used — which is the answer to the author's own question.

## F5 — one § 7.2 quote is not byte-exact, and the census cannot see it (🔸 MINOR, `CC-20261004-MIRROR-24`)

Five of the six superseded-wording quotes occur **once** in the pre-batch file. `DIS-031`'s occurs
**zero** times: the superseded text read `**read Grubor 2025**` with a terminal period, the quote
drops the asterisks and the period. The substance is identical; the discipline is not. The method
finding is the larger one: the batch's census asked whether the quoted wording occurs once *in the
file after the correction*. That cannot detect a quote that was never in the file before it. The
test that answers § 7.2 runs against the pre-batch revision.

```bash
python3 <scratchpad>/verbquote.py   # pre=0/post=1 for DIS-031; pre=1/post=1 for the other five
```

## F6 — a § 7.2 quote put a second PMID into `FT-193`'s identity line (NOTE, no candidate)

`queue_entry_identity(FT-193)` now returns **two** PMIDs — 41404412 and 42422766 — because the
quoted superseded wording ends *«… read off the reference list of PMID 42422766»*. The state is
`resolved` and the right PMID leads, so nothing is blocked, and the pre-batch entry already carried
42422766 unquoted, so the batch did not introduce the second identifier. It is worth writing down
as a class: a verbatim quote containing an identifier joins the queue's identity grammar, where the
quote's author did not intend it to. Backticking the PMID inside the quote would not help; the
reader scans the line.

## F7 — two citations lack the article number the front matter prints (NOTE, no candidate)

`PAPER 210` / `LIT-0502` cite *«NPJ Genom Med 2026;11»*; the front matter has `elocation-id` **52**.
Incomplete rather than wrong, and the DOI and PMCID resolve the paper.

## F8 — the `CLAIM 005` note carries no premise tag (NOTE, no candidate)

The 3 256-byte append mixes quoted table cells (`DATO`) with a reading of the primary — *«the
evidence behind that direction is narrower than the direction»* — and carries no `PREMISE` line,
while the sibling appends to `CLAIM 032` and `CLAIM 033` both do. The record has **no** prohibition
line at all, before or after, so this is the record's pre-existing style rather than a regression,
and the claim's own `Type:` field is `DATO`. Named for the author's judgement, not filed.

## F9 — `PAPER 201` still says *«Provisional number»* (NOTE, recurrence)

The pattern the previous Mirror review recorded as F6 on `BATCH_20261003_003`/`_004` is here again,
in a record whose number was settled by measurement. Still harmless, still tells the next reader
that a settled number is provisional, still cheapest to drop in the integrator's own op.

---

## Where I could be wrong / `WHAT_WOULD_CHANGE_MY_MIND`

- **F1** would fall if `PAPER 202`'s fields were meant to record *what the candidate said* rather
  than what the source says. Nothing in either field marks it as quoted or superseded, and the
  `Role` field's 🔴 sentence reads as the record's own finding.
- **F3** would fall if this deployment's convention were to list the handling editor. No other
  record in the batch does, and three in the same set exclude theirs.
- **F5** would fall if § 7.2 allowed normalising emphasis inside the quote. I did not find that
  permission; if it exists, the candidate becomes a no-op and the method note still stands.
- **A2** checked identity fields (DOI, PMCID, journal, volume, issue, pages, author order, year)
  against the front matter for all twelve. It did **not** re-read the twelve `Role` fields against
  the bodies; a wrong statement inside a `Role` would not show here, and the batch's own blind
  audit covered propositions rather than bibliography.
- **A4** verified every quantity the merged arm **names**. A scalar the merge omitted — Thomsen
  prints per-kg equivalents (3.1 × 10¹³ and 6.0 × 10¹³ vg/kg at 2–4 kg) that the arm does not
  mention — would be invisible to this check. It supports the arm's own point rather than
  contradicting it, which is why no finding is filed.
- **A10** counted vocabulary, not rhetoric. A record can overstate without any of those words.
- **A7** rests on what the sources print. If a primary ever links the Nagarajan child to Piard
  patient 14, the «at most three, possibly two» statement becomes a count and not a range.

---

## Candidates written by this review

| Candidate | Finding | Ops | File(s) |
|---|---|---:|---|
| `CC-20261004-MIRROR-21` | F1 + F2 | 2 | `registries/paper_registry_current.md` |
| `CC-20261004-MIRROR-22` | F3 | 2 | `registries/paper_registry_current.md` · `registries/literature_tracking_log_current.md` |
| `CC-20261004-MIRROR-23` | F4 | 1 | `registries/paper_registry_current.md` |
| `CC-20261004-MIRROR-24` | F5 | 1 | `research/dismissal_ledger_current.md` |

Each `old` was measured **unique inside its record and in the whole file** immediately before the
candidate was written, and each candidate says the propagating batch must re-measure it.

---

## DEFAULTS_TAKEN (§21c)

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| A safety classifier halted the turn after a wide keyword dump from an artefact | Switched to narrow windows (±120–250 chars, 3–8 hits) and reported the halt in the method note; the dump was **not** reworded or re-run | Every later figure in this review carries a command and a bounded output | A reworded retry, which the brief forbids |
| `files/` is outside the worktree | Read it in place, read-only, through the window and front-matter scripts | No byte written under `files/` | A hardlink copy, which this review did not make |
| The worktree was cut from an older `main` | Reset the task branch to `main` `761b369` before measuring, so the gates ran on the state the batch actually left | `2de75c1` is an ancestor of the measured tree | Measuring a tree the batch never produced |
| The backlog counter reads 16, not the batch's 5 | Attributed the eleven extra to the wave-8 candidates landed after `2de75c1` and did not count them against this batch | They are named in wave-8 files the batch never touched | A finding against a batch that did not cause it |
| Findings need registry edits Mirror may not make | Wrote four candidates with exact ops and measured `old` | §21e: a finding is a new task for the author | A Mirror registry edit, which the role contract forbids |
| Four findings are wording, pattern or incompleteness | Filed as NOTE-level with the correction named, no candidate | A candidate for a one-word judgement call pre-empts the author | Four more candidates the author did not need |
| `PAPER 202`'s two other self-attributed defects (the `No seizures` cell; the organoid-provenance sentence) | Verified the first at the artefact, left the second unchecked and said so | Both are the record's own criticisms of its source, not claims about WWOX biology | A verdict on a sentence I did not measure |

**Review path:** `disease-models/wwox/research/session_evaluations/mirror_review_batch_20261004_001.md`

**Not medical advice.**
