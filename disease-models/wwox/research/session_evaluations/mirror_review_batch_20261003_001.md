# MIRROR ex-post review — BATCH_20261003_001

`REVIEW_ID` MIRROR-20261004-BATCH20261003001 · `OBJECT` `BATCH_20261003_001` (WM_v7.8 → **WM_v7.9**,
21 candidates), landed on `main` at **`31da5fa`**, pre-batch base `2c92e358` · `LEVEL` ex-post review
on the author's request, covering the two MAJOR-class candidates · `REVIEWER` ACTOR_ID `mirror` ·
`AUTHOR` ACTOR_ID `scientist` (Scientist F, integrator; readings by Scientists A/B/C) ·
`ADJUDICATOR` the author, as a new task.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding is
> a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect found
> given the available evidence bundle", never "true". READ-ONLY toward every registry: this review
> writes one file and three candidate files and edits no canonical record. **Not medical advice.**

**Method.** Artefacts in the root `files/` tree were examined read-only and **only through scripts**
that print sha256 digests, term counts, section offsets or one addressed table cell — never prose.
One free-text context probe was halted by a safety classifier early in the session; it was not
repeated in any form, and every later check ran through the count/slice scripts named in
`DEFAULTS_TAKEN`. Registry checks ran by script over `git show <rev>:<path>`, printing digests, byte
lengths, field names and short slices. Artefact identity was re-derived against each manifest digest.

---

## STEELMAN (first)

- **The `CLAIM 012` amendment is correct and is the kind of thing a reader skips.** In the PMID
  42193054 artefact (sha256 `c2538a20…`) the *«Trio-based …»* phrase sits at offset 21,972, inside §1
  Introduction (16,745–22,421); the *«… but was not performed»* sentence at 31,757, inside §3.2
  (30,902–31,791); the limitations sentence at 41,477. §2.2 names one sample source only. The
  Discussion sentence about configuration is conditional; abstract and conclusions presuppose it. The
  amendment's own words therefore match the artefact, and the two other `CLAIM 012` edits reproduce
  verbatim.
- **The `CLAIM 018` repair rests on a zero that reproduces.** The allele string is absent (0) on both
  held body surfaces of PMID 30356099 (sha256 `885c00f9…`, `b5318e44…`) and in each of the four
  supplementary workbooks (`8fca3cff…`, `0e0f5ed6…`, `f624234e…`, `c431b590…`), with a positive
  control present (4 hits) in the first workbook.
- **`CLAIM 019`'s primary verification reproduces cell by cell.** Aligned by cell reference, the four
  rows the op describes carry exactly the zygosities and the ages it states, including its own
  caution about one patient's zygosity in secondary sources.
- **`DIS-030` reproduces at the supplement.** `files/supplements/PMID29067327/mmc1.docx` sha256
  `de9bf3e2…` equals the manifest digest; the legend's quoted figure occurs once; `n =`, `SEM` and
  `P <` occur **0** times. `blind` and `randomi` are **0** in both artefacts of that wave
  (`a05d8ad3…`, `e250cd19…`), as the record states.
- **The prohibitions stayed attached, measured per line.** `CLAIM 032`'s four pre-existing
  prohibition lines are byte-identical (`74e2bef3`, `a7f0c7b0`, `5c512671`, `468483ff`); the new line
  was inserted directly beneath the trigger it reports as fired, so the demonstrative resolves to the
  right referent. In `CLAIM 011`, the *«none of this bounds the claim as written»* span (578 bytes,
  digest `ce7964c6`) is byte-identical before and after.
- **Depth is declared per record and matches the ledger.** All sixteen `PAPER`/stub records created or
  changed declare the depth of their latest receipt; `PAPER 141` declines a depth of its own and names
  its receipt instead.
- **No overstatement enters canon.** On added lines only, `first|novel|demonstrat*|establish*|prove*|
  unique|confirms` occur solely inside quoted source words, negations (*«none of them a demonstrated
  negative»*), `first-hand`/`first author`/`first node`, or explicitly corpus-scoped phrases.

---

## Verdicts by area

| # | Area | Verdict |
|---|---|---|
| A1 | `CLAIM 012` integrator amendment vs artefact | **CONFIRMED** |
| A2 | `DL-MECH-013` heading split | **CONFIRMED** on words (0 lost, measured by token multiset) and on the single inbound wikilink · 🔴 **F1** splice artefact · 🔴 **F3** ripple not carried |
| A3 | `PAPER 142` / `LIT-0440` identity landing | **CONFIRMED** — depth = receipt; structural statements verified at the artefact (reference count, one figure, no tables, no supplement, no Methods/Results section, the shared citation) · 🔸 **NOTE F5** |
| A4 | `DIS-026`–`029` depth attestations + `DIS-030` | **CONFIRMED** — the four now read `partial` against four `partial_fulltext_read` receipts |
| A5 | `CLAIM 043` / `CLAIM 044` | **CONFIRMED** on class, type, premises, trigger and `BLOCK 2` rows · 🔴 **F2** missing reciprocal link |
| A6 | Two MAJOR candidates, triples rechecked independently | **CONFIRMED** — 3 triples on one, 6 surfaces on the other, plus two extras |
| A7 | Per-line digests of `CLAIM 032` / `CLAIM 011` prohibition spans | **CONFIRMED** in substance · 🔸 **NOTE F4** on the report's wording |
| A8 | Depth labels in the new `PAPER` records vs receipts | **CONFIRMED** 16/16 |
| A9 | Overstatement vocabulary | **CONFIRMED** |
| A10 | Gates at `31da5fa` | **CONFIRMED** — `public_release_gate.py` **VERDICT: PASS, BLOCKS: 0**; LINT `WARN`, 0 BLOCK; receipts **OK, 320 chained**, tail anchored; `growth_anchors check` **PASS** · 🔸 **NOTE F6** on the report's structural-delta line |

---

## F1 — the reflowed `DL-MECH-013` line carries a splice artefact (MINOR, `CC-20261004-MIRROR-01`)

Every word survived the split: token multiset over the whole record at `dc623a7` against `31da5fa`
gives **0 lost, 1 added** (`Qualificazione`). But the heading's opening parenthesis was dropped while
its closing one was kept, leaving **13 `(` against 14 `)`** on the new first body line and two
adjacent words saying the same thing. Cosmetic in substance; it is the first line a reader of the
lead now meets, and it was produced under an explicit `reflow` the report calls lossless.

## F2 — `PAPER 141` does not link back to `CLAIM 044` (MINOR, `CC-20261004-MIRROR-02`)

```bash
python3 framework/scripts/legend_lint.py . | grep "CLAIM 044"
#  [WARN_BUT_PROCEED] UNLINKED_SUPPORT: CLAIM 044 names PMID 34359949 in source; PAPER 141: Claim links does not name CLAIM 044
```

`CLAIM 044` is new in this batch, so the warning is the batch's own. It is the same omission class as
the two missing `BLOCK 2` rows the batch repaired by hand, one level down and caught only as a `WARN`.

## F3 — the `DL-MECH-013` qualification did not reach `HYP-20260705-01` (MINOR, `CC-20261004-MIRROR-03`)

The lead's human arm was narrowed to *suggestive*; the hypothesis that cites the lead still states
the human arm unqualified in its `Meccanismo` line. The wikilink was resynced, the sentence was not —
the synthesis-level pattern this repository has twice recorded.

## F4 — one attestation sentence misstates its own unit (NOTE, no registry op)

The report states that `CLAIM 011`'s 🟢 bound **line** is byte-identical before and after. Measured,
that line's digest **changed** (`0022846567f4` → `4370e1ca969b`, 2,218 → 2,403 bytes) — it is one of
the two changed digests the report's own table lists, under Mirror op `C11-1`. What is byte-identical
is the **span** of that sentence (578 bytes, `ce7964c6`), which is what the measurement was for. The
substance is sound; the sentence names the wrong unit, and an attestation that over-claims its unit
is weaker than the measurement it reports.

## F5 — `PAPER 142` says slightly more than "identity and nothing more" (NOTE, no registry op)

The record asserts evidence-class statements (nothing in the article is a new measurement; no
neuronal datum; `Transferability: n/a`) while the report describes it as asserting no evidence
boundary. I verified each of those statements at the artefact, so the record is accurate and
conservative; it is the report's description of it that is loose. Worth one clause rather than an edit.

## F6 — the report's structural delta omits the landing it describes two sections later (NOTE)

`Structural delta` reads papers 122 → **131** and literature 412 → **420**, which excludes the
identity landing the same batch made. At `31da5fa`, `growth_anchors.py check` reads
`papers=132 · literature=421 · claims=44`, and the report itself records the re-anchor (events 37 →
38). The counts are right in the ledger and one short in the summary table.

---

## Where I could be wrong / `WHAT_WOULD_CHANGE_MY_MIND`

- **F1** — if the live line's bold markers differ from what the candidate assumes, the op's shape is
  wrong even though the defect is real; the candidate says so and gives the minimal fallback.
- **F2** — a rule by which a secondary-source record declares only the claim it primarily bounds
  voids it; LINT's own check says otherwise.
- **F3** — if `HYP-20260705-01`'s `Meccanismo` is meant as a historical statement of what was once
  believed, the op is unnecessary; nothing in the record says so.
- **F4/F6** — a stated convention under which "line" means the prohibition span, or under which the
  delta row counts only the batch's scoped candidates, voids each respectively.
- **A1/A6** — my reading of the artefacts is offset-based and count-based by necessity after the
  classifier halt. A passage carrying the opposite sense inside a region I sampled only by term count
  would not have been caught.
- **On the whole batch** — I re-derived four readings at artefact level out of eighteen, and did not
  open any figure at native size. A defect in the other fourteen would not have been caught here.

`REVIEWER_CONFIDENCE` HIGH on F2, F4, F6 (each reproduced by command); HIGH on F1 (digest and
parenthesis census); MODERATE-HIGH on F3 (rests on a judgement about intent); NOTE-level by
construction on F5. `RESIDUAL_UNCERTAINTY` the fourteen unsampled readings and every figure panel.
`EVIDENCE_NEEDED` none for the three candidates; all `old` strings were measured unique at `31da5fa`
and must be re-measured by the propagating batch.

`AUTHOR_RESPONSE` — owed, and silence is not acceptance (Annex C.2).

## Candidates written by this review

| Candidate | Finding | Ops | File |
|---|---|---:|---|
| `CC-20261004-MIRROR-01` | F1 | 1 | `research/discovery_ledger_current.md` |
| `CC-20261004-MIRROR-02` | F2 | 1 | `registries/paper_registry_current.md` |
| `CC-20261004-MIRROR-03` | F3 | 1 | `research/therapeutic_hypotheses_ledger_current.md` |

`CANDIDATE_BACKLOG` was already 16 at `31da5fa` (five old, eleven wave-3); these three make 19. Noted
deliberately: a Mirror finding is a new task, and the next `BATCH_COMMIT` propagates them or records
why not.

## DEFAULTS_TAKEN (§21c)

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| A safety classifier halted a free-text artefact probe mid-run | switched permanently to on-disk scripts printing digests, counts, section offsets and single addressed cells; never re-ran the halted read in any wording | no source prose was dumped; every verdict above rests on a reproducible command | the halted route, which the brief forbids re-attempting |
| `files/` is outside the worktree | read it in place, read-only, identity re-derived against each manifest digest | no byte written anywhere under `files/` | a hardlink copy, which this review did not need |
| Review-file directory not pinned by the brief | wrote into `research/session_evaluations/`, beside the earlier Mirror reviews, under the brief's filename | existing convention | a directory no tool routes to |
| Findings need registry edits Mirror may not make | wrote three candidates with exact ops and verbatim `old` | §21e: a finding is a new task for the author | a Mirror registry edit, which the role contract forbids |
| Three findings are against the **batch report**, not a registry | filed as NOTE-level findings with the correction named, no candidate | a report is the author's own artefact and carries no gate | candidates against a non-registry file |

`STOP_LOG` — one entry: the classifier halt described above. No class-1 reserved act arose; nothing
was pushed, no registry was edited, and the halt had a safe default that preserved every check.
