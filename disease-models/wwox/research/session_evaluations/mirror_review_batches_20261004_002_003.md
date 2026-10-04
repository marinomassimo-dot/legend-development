# MIRROR ex-post review — BATCH_20261004_002 and BATCH_20261004_003

`REVIEW_ID` MIRROR-20261004-BATCH20261004002-003 · `OBJECT` **two consecutive batches**:
`BATCH_20261004_002` (intake wave 8, `WM_v7.14` → **`WM_v7.15`**, 11 candidates, landed `bdc61a0`;
report `2026-10-04_BATCH_20261004_002.md`) and `BATCH_20261004_003` (intake wave 9 + the four
Mirror repairs, `WM_v7.15` → **`WM_v7.16`**, 17 candidates, landed `ce4aa9c`; report
`…_003.md`) · measured on `main` at **`ce4aa9c`**, which contains both · `LEVEL` ex-post review on
the author's request (`_003` *Recommended next actions* item 1) plus the `D6` classification
reserved to Mirror · `REVIEWER` ACTOR_ID `mirror` · `AUTHORS` ACTOR_ID `scientist` (Scientist L and
Scientist M) · `ADJUDICATOR` the authors, as new tasks.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect
> found given the available evidence bundle", never "true". READ-ONLY toward every registry: this
> review writes one file and five candidate files and edits no canonical record. **Not medical
> advice.**

**Method.** Registry records were addressed by heading span and printed field by field, never by
grepping the two large registries as text. Artefacts in the root `files/` tree were read read-only
through scripts that strip JATS tags and print bounded keyword windows, single addressed table
cells and front-matter contrib groups. Every ratio below was recomputed from the two numbers its
record names; the two F-tests were recomputed from the printed F and degrees of freedom with a
local incomplete-beta implementation (no `scipy` on this deployment). A safety classifier halted
one turn — a plain `Read` of the first 220 lines of the `_002` report. It was **not reworded or
retried**; the rest of both reports was read through a line-slice script, and every later read used
the same route.

---

## STEELMAN (first)

- **Where I could re-measure a number independently, the two batches were right to the last digit,
  including numbers no gate in this repository can see.** `De 2025` Table 4, recomputed from the
  supplementary cells rather than read: **559** distinct WWOX probe locations for the drug-response
  phenotype (exact), best LRR p **1.68e-4** at chr16:78,383,363 — *inside* the deletion interval the
  record names — against a Bonferroni threshold of 0.05/559 = **8.94e-5**, best genotype-based p
  **4.92e-3**, and **14,283 unique rows of 16,980** — the record's own figure, which I reproduced
  only on the fourth projection I tried. A reading that survives being re-derived by a hostile
  script is a different object from one that survives being re-read.
- **Grubor 2025 is carried at the strength the artefact prints, both ways.** *«2/3 vs 1/3, 3/3 vs
  1/3, 3/3 vs 1/3»* and *«10 of 26»* / *«1 out of 29»* / *«11 of 36 DRGs; 3 of 3 subjects»* /
  *«one finding of mild severity of 36 DRGs»* are the paper's own sentences; 38.5/3.4/30.6/2.8 %
  recompute; and the rejected proposition that immunosuppression **bounds** DRG risk is **not
  revived**, with the reasons (n = 3, 43 days, sponsor, residual lesions) stated in `DIS-031`.
- **Thomsen Table S3 verified cell-wise.** `8.00E+11 → 2.00E+13 vg/mL → 2.00E+14` is the printed
  row; 8.00 × 10¹¹ / 0.04 mL = 2.00 × 10¹³ and × 10 mL = 2.00 × 10¹⁴; the 250-fold factor is
  10/0.04. The debt retires as **not printed** — a different verdict from *answered*, said so in
  all four touched records.
- **Petrozziello: the statistics are exact and the record says which readings are hands.**
  `F(1,28) = 6.181 → p = 0.019149` and `F(1,28) = 0.3129 → p = 0.580353` recompute to the printed
  0.0192 and 0.5804; the 0.71 / 0.64 / 0.32 viability ratios are labelled hand readings of a panel,
  and the preprint status travels with every one of them.
- **The valproate debt was left open, which is the harder thing to do.** `WWOX` occurs **zero**
  times in the running text of all four primaries — I counted on the artefacts: 0/0/0/0 — the
  platform is one H9/ESNATS lineage, the four share measurements, and the fifth primary is
  paywalled. The curated *«Decreases expression»* row is therefore contradicted and **not
  replaced** by a counter-direction claim.
- **Depth discipline is airtight across 27 new records.** `fulltext_receipts.py status` returns
  `partial_fulltext_read` for **18 of 18** wave-8 PMIDs; every one of the 30 new `LIT` records
  carries the literal **partial full text** that `coverage_report.PARTIAL_MARKERS` needs; and
  *«read in full»*, *«panel level»*, *«full text reviewed»* and `complete_fulltext_read` occur
  **zero** times in `PAPER 217`–`243`.
- **Identity was measured from the front matter, nine times out of nine in wave 9** — including
  three editor contribs correctly excluded, the Bey-not-Hordeaux correction (Hordeaux is author 7
  of 22, verified) and eLife's reviewing-editor group left out of `PAPER 243`.
- **Prohibitions stayed attached.** Per-line sha256 across `CLAIM 011/032/045/046/047` between
  `761b369` and `ce4aa9c`: **0 removed**, 4 added, 2 edited in place (both the declared narrowings).
- **Patient counting held.** `PAPER 117` Patient 11 *«counted once — `DATO`, because the later
  authors state the identity themselves»*; `PAPER 220` *«Count once (INFERENZA)»* with identity to
  `PAPER 013` case 50 neither confirmed nor excluded; the two deep-intronic sources counted once
  each at class level with the zygosity difference **recorded, not reconciled**.
- **The one red suite is not theirs.** `test_batch_queue.py` fails here exactly as the `_003`
  addendum says, on `READ_NOT_REGISTERED=['21476439']`, a wave-10 receipt.

---

## Verdicts by area (the authors' own focus lists)

| # | Area | Verdict |
|---|---|---|
| B1 | `CLAIM 046` / `CLAIM 047`: classification, premises, negatives, `BLOCK 2` mirror rows, reciprocal `PAPER` links | **CONFIRMED** — both `in observation`, `Type` and `PREMISE_TAG` present (incl. a declared `DEFAULT_FROM_TEXTBOOK` on reporter-predicts-therapeutic), rows 046/047 present in `BLOCK 2`, `PAPER 223/225/226/227/228` all declare their claim · 🔸 **F6** one ratio in `047` |
| B2 | 18 records `PAPER 217`–`234` / `LIT-0509`–`0526` vs JATS front matter | **CONFIRMED 17/18** on PMID, PMCID, DOI, journal, volume, issue, pages/elocation, author order · 🔸 **F1** `PAPER 228` / `LIT-0520` |
| B3 | Depth labels vs `fulltext_receipts.py status --pmid`; `partial full text`; no overstated depth | **CONFIRMED 18/18 + 30/30**; zero depth overstatements in either registry |
| B4 | `DL-REPO-003` as an unread debt with a falsifier, and its wave-9 amendment | **CONFIRMED** — the debt is stated, not settled; the UP direction, the shared measurements and the paywalled fifth primary are all in the record · 🔸 **F4** the supplement bytes are absent |
| B5 | The measured-vs-predicted table and `CLAIM 033` riserva (1) — is anything about PMID 36926521 overstated? | **CONFIRMED — nothing overstated.** The record says *one* blot, one control, no quantification, *«it measures the genotype»*, exon-5 skipping with *«no skipped fraction, no frame statement, no NMD test»*, the source's own *«PCR»* (never «RT-PCR»), and `PREMISE: DATO (one blot and one PCR, both qualitative)` · 🔸 **F2** one clause of the privacy repair |
| B6 | Residue dispositions | **CONFIRMED** — `GRAPH-HYGIENE` `NOT INTEGRATED` appended **append-only** with its reason; four `DEFERRED` with 2026-10-06/08 triggers; `growth_anchors` now names **9** (the 4 residue + 5 wave-10) and no longer counts the closed stub |
| C1 | 17 propagated candidates: ≥12 carried quantitative statements re-measured against artefacts, ratios recomputed | **CONFIRMED 15/15 checked** (Grubor ×3, Thomsen S3, Petrozziello ×3, valproate ×2, De ×4, Henry ×2, Tang, Dong ×2, Lima, Khadija arithmetic) — see STEELMAN; two figure-only values (gnomAD 7355/21694 = 0.3390; the 1.10× γ-H2AX) I could recompute but not re-read, and both are labelled panel readings |
| C2 | Repaired records `PAPER 156/208/209/162/216/202/214/210`, `DIS-031`, `DIS-028`, `FT-193`, `FT-194` | **CONFIRMED** — all four Mirror repairs applied, two of them generalised; `PAPER 156` now names 110 carriers **and** the 204 cohort and scopes *«No CNVs»* to 104 genes · 🔸 **F3** `PAPER 210`'s second field · 🔸 **F5** `CLAIM 011`'s missing marker |
| C3 | The *«WWOX n = 2…»* style counts | **CONFIRMED** — Dong prints `WWOX (n = 4)` and `PAPER 156` resolves it into **three distinct heterozygous missense alleles in 1 + 2 + 1 participants**, with the `ClinVar Benign` column read as a condition list and the 7.5 × 10⁻³ / 0.001 ratio (7.5×) correct after the earlier `MIRROR-12` fix |
| D | `c.107+119C>G`: qualitative-only, read fraction/frame/NMD/protein/tissue unmeasured, preprint = one unillustrated sentence, never promoted, zygosity differs | **CONFIRMED at all four sites** — `PAPER 241`, `RL-C-20261004w9c1`, `FT-194`, `LIT-0537`; the allele string occurs **5 times in the landed state and nowhere without its caveat**; `CLAIM 032`/`CLAIM 033` do not carry it; the working model's one mention says *«measured qualitatively only»*. **No transfer**: the binding transfer-limit paragraph names acceptor, canonical ±1/±2 and missense classes explicitly |
| E | Patient-overlap labels (`INFERENZA`) and no patient counted twice | **CONFIRMED** — see STEELMAN |
| F | Per-line sha256 prohibition spans for `CLAIM 011/032/045/046/047` | **CONFIRMED** — 0 removed; `032` byte-identical (8→8); `046`/`047` 0→2 each; the two edited lines are the declared narrowings · 🔸 **F5** one of them lacks its § 7.2 marker |
| G | `public_release_gate.py` over the whole tree; parent-of-origin wording in the new records | **PASS, 0 BLOCK**, 12 `[REVIEW]`, of which 3 are wave-8/9 candidates and manifests. The four current registries carry **one** parental-side phrase in total · 🔸 **F2** · NOTE **F7** |
| H | Overstatement vocabulary in added lines | **CONFIRMED** — every *«first»* / *«only»* is scoped to *«the model holds»* or *«the read literature»* (an in-repo, falsifiable statement), and `PAPER 202`'s unmeasured *«first»* is gone: it now reads *«no priority is claimed: no search for an earlier such table was run»* |
| I | Gates at the landed state | **CONFIRMED** — LINT exit **0**, **0 BLOCK**, 13 `WARN_BUT_PROCEED`, none naming a wave-8/9 record; `fulltext_receipts verify` **OK, 429 chained**, tail anchored; `growth_anchors check` **PASS** (claims 47 · papers 233 · corpus 367 · literature 519 · registry_only 4 · unread_premises 0); release gate exit **0** |

---

## F1 — a journal's Academic Editor is the fifth author of `PAPER 228` / `LIT-0520` (🔸 MINOR, `CC-20261004-MIRROR-31`)

The JATS front matter of PMID 41744777 has **four** authors and puts **Chen Shih-Heng (David)** in
`contrib-group content-type="editor"`, `role` **Academic Editor**. Both records list him fifth.
This is precisely the class `CC-20261004-MIRROR-22` repaired in `PAPER 214` one batch earlier.
`BATCH_20261004_003` generalised the rule — correctly, over **its own** records, excluding three
editor contribs including this same editor in `PAPER 242` — and never swept the landed wave-8 set.
A repair that becomes a rule should be run backwards once over the records written the day before.

```bash
python3 <scratchpad>/editorsweep.py disease-models/wwox/registries/paper_registry_current.md '^PAPER 2[1-4][0-9]\b'
```

Two hits, one of them a false positive worth naming: `PAPER 214` reports `IN_AUTHORS` because its
**corrected** field quotes the superseded wording verbatim. That is the same "a quote joins the
record's grammar" class this reviewer recorded as F6 last time, now biting an automated check
rather than a reader.

## F2 — one clause of the privacy repair still names a parental side, eleven words before the clause that says it does not (🔸 MINOR, `CC-20261004-MIRROR-32`)

`CLAIM 033`'s riserva (1) opens one clause by naming **which** parent transmitted an allele, and
closes the same sentence by stating that the source names the relationship and *«this record does
not»*, because such a side does not belong in a statement about the reference genotype. **The
sentence is not reproduced here, and the candidate names only the string it replaces** — the exact
trap `BATCH_20261004_002` recorded, and the gate blocked this review's first draft on it twice,
which is the third independent instance of the same pull. `public_release_gate.py` does
not see it, because its rule needs **both** sides paired; it flags the three *other* surfaces of
the same reading as `[REVIEW]`. `BATCH_20261004_002` wrote the lesson — *describe the class, do not
paste the instance* — and this is the one place in the four current registries where such a side
survives (measured: a case-insensitive sweep for either transmitting-parent term returns **1** hit
across all four files, and it is this clause). The phase statement loses nothing: *parental
segregation* establishes phase in trans.

## F3 — `PAPER 210`'s second field still asserts the derivation the first one now labels (🔸 MINOR, `CC-20261004-MIRROR-33`)

`CC-20261004-MIRROR-23` was applied exactly as written, to `Genotype/model`. Two lines below,
`clinical relevance` still reads *«a measured WWOX splice outcome in the same intron as the
reference genotype's splice allele»* — true only under the exon-map derivation that the field above
now marks `INFERENZA`, and it is the sentence that makes the record look adjacent to the reference
genotype. One-field repairs are now the recurring shape of this defect: `PAPER 202` (F1 last
review), `PAPER 210` twice, `PAPER 228`. **A candidate that repairs a field should name the record,
not the field.**

## F4 — the one quantitative range whose source bytes are absent is also one of the three that landed unaudited (🔸 MINOR, `CC-20261004-MIRROR-34`)

`DL-REPO-003` states *«ratios 1.33 to 2.13, adjusted p 0.007 to 0.042»* from supplementary probe
tables. `evidence_presence.py` reports **1/5 present** for PMID 23179753 and **1/4** for PMID
27188386: only the main JATS articles are on this disk, and a digest search recovered none of the
`MOESM` tables. The reading is not thereby wrong — the manifests fingerprint the absent files, and
everything I *could* check in that candidate (WWOX = 0 occurrences ×4, platform, doses) reproduces
— but the record should say that its numbers are, here and now, declared rather than re-attestable.
`BATCH_20261004_003` named this candidate as one of three that landed without a blind audit and
wrote the right upgrade (`--search` as step 0); the surface debt belongs in the record too.

## F5 — a statement about this corpus's reading state was replaced with no superseded wording (🔸 MINOR, `CC-20261004-MIRROR-35` op 2.1)

`CLAIM 011`'s `PREMISE_TAG` lost *«the source reports no 65Q-versus-27Q comparison and Figure 4B is
unread …»* with no marker. The replacement is **more** accurate, which is why this is a discipline
finding and not a content one: *«Figure 4B is unread»* is a record of a completed act, § 7.2's own
object, and item 2 of that section requires the old words to travel in the line. The sibling edit
to `CLAIM 045` in the same batch carries its marker; so does `PAPER 214`. Measured: of 12 in-place
line replacements in the paper registry and 2 in the claim registry, **2** carry one.

## F6 — `CLAIM 047` prints a ratio without its two inputs, in a sentence where every other ratio has them (🔸 MINOR, `CC-20261004-MIRROR-35` op 2.2)

The batch's own arithmetic screen classified the ~127-fold liver reduction as *reported, not
derived* (its two values are figure-only), and `PAPER 228` says so; `CLAIM 047` does not. The claim
is the surface a reader meets.

## F7 — three of the gate's `[REVIEW]` privacy lines sit in wave-8/9 authored surfaces (NOTE, no candidate)

`CC-20261004W8-A-PATIENT-OVERLAP-01`, `-A-REGISTRY-01` and `CC-20261004W9-C-DEEPINTRONIC-01` each
pair both transmitting sides for one individual in a published cohort. The gate returns
`[REVIEW]`, not `[BLOCK]`, by design — those variants belong to other published genotypes — and the
landed registries are clean. It is written down because candidates are shipped surfaces too, the
decision *«read it before publishing»* is the operator's, and this is the second batch whose
candidate bodies carry the instance while its records carry the class.

## F8 — the paragraph-number defect the `_002` report measured was not routed anywhere (NOTE, no candidate)

Two blind auditors independently found anchors whose **paragraph** number is off by one or two while
the section is always right, and the report named the upstream counter. Nothing in either batch
opens a harness task for it, and `_003` does not mention it. A measured tool defect with no owner
is a finding that expires.

---

## The `D6` decision — a Mirror act, taken here

**`MIRROR-RULING-20261004-D6`.** `CC-20260826-GSK3B-S9-AXIS-01` has been deferred for eight batches
on one point: its residue `D6` is marked **`MAJOR?` → Mirror, fail-closed**, and §21d moves no
authority H.1 assigns to Mirror, so no Scientist session could clear it. `BATCH_20261004_002` read
this correctly and routed it. I take the decision.

**What `D6` asks for.** A **reciprocal boundary** in `CLAIM 016` **and** `CLAIM 035` naming the
mutual exclusion on the S9 axis and both horns — (a) the pS9 fall is driven by something other than
loss of the WWOX docking-site brake, so `CLAIM 016`'s only *in vivo* de-repression evidence is not
evidence that the `CLAIM 035` mechanism operates *in vivo*; or (b) it is WWOX-dependent, so
`CLAIM 035`'s S9-independence needs a boundary it does not have — with neither claim citable as
corroboration of the other on that axis until one horn closes.

**Measured before deciding.** `CLAIM 016` `Status`: **`in observation`**. `CLAIM 035` `Status`:
**`in observation`**. Neither is a `consolidated baseline`. `D3`, `D4` and `D11` have already
landed (`CLAIM 016`'s `Type` reads *«DATO densitometrico NOT_TESTED … significatività non
riportata»*; `CLAIM 035`'s Summary already separates *«388–407 richiesti»* from *«388–412
contiene»*). The **reciprocal boundary itself is absent from both records**: `CLAIM 016` carries the
pS9-premise critique and `CLAIM 035` carries the false-negative prediction, the two wikilink each
other, and **neither names the exclusion**. So `D6` is still owed, and the registry currently holds
two mutually exclusive readings that cross-reference each other without a bound.

**Ruling: `D6` is `MINOR`.** Reasons:

1. **It creates no claim, reverses none, and touches no `consolidated baseline`** — the three
   triggers both of these batches used, and both targets are live `in observation`, measured above.
2. **A boundary that only removes a permitted inference cannot reverse a baseline.** `D6` adds a
   restriction on use and two open horns; it is the same act as `CLAIM 033`'s riserva (1) and
   `CLAIM 011`'s `PREMISE_TAG`, both propagated `MINOR` in these batches, and it makes the registry
   say *less*, not more.
3. **Fail-closed has no object here.** Body §12 resolves *persistent doubt* to MAJOR. The doubt the
   candidate records is about **which horn is true**, not about the change class; the class question
   was answerable by measurement and has been answered. Deferring a bound for eight batches is the
   costly outcome, because the unbounded state — not the bound — is what a reader is exposed to.

**Two conditions, binding on the propagating batch** (without them the act is not the one I
classified, and it comes back for review):

- **Reciprocity in one batch.** Both records, same batch, or neither. A one-sided landing leaves the
  unedited record still offering corroboration — the F1/F3 defect shape of this review and the last.
- **Neither horn may be stated as resolved, and no claim's `Status` or `Summary` assertion may
  change.** If the propagating batch finds itself withdrawing `CLAIM 035`'s S9-independence or
  `CLAIM 016`'s *in vivo* de-repression, **that** op is MAJOR and is a different candidate.

**What I did not decide.** `D2` (the manifest's historical scope record) is specified by
`prompt_batch_commit.md` § 7.2 item 2 and needs no ruling. `D3`/`D4`, marked `MINOR?`, are already
landed. The **substance** of the exclusion — which horn holds — is not a Mirror call and no
evidence here settles it: both sides rest on single-lane densitometry with
`STATISTICAL_STATUS: NOT_TESTED` on one side and a locator-shifted S9 panel on the other.

---

## Where I could be wrong / `WHAT_WOULD_CHANGE_MY_MIND`

- **F1** would fall if this deployment's convention were to list the handling editor. Four other
  records in the same two batches exclude theirs, and `CC-20261004-MIRROR-22` settled the rule.
- **F2** would fall if a parental side attributed to a *published cohort case* were outside the
  privacy design even inside a reference-genotype claim. The record's own next clause says
  otherwise, which is why I filed it rather than noting it.
- **F5** would fall if § 7.2's *«historical record of a completed act»* did not cover a premise
  line's statement about what has been read. I read the section; it names the changelog and the
  scope record explicitly and the class generally, and the batch applied the marker to the sibling
  edit of the same shape.
- **The `D6` ruling** would change if either claim's `Status` were `consolidated baseline` at the
  moment of propagation. The propagating batch must re-read both (`registry_records.py get`), as it
  does for every target; if either has been promoted since `ce4aa9c`, the classification is void and
  returns to Mirror.
- **C1 verified every quantity the records *name*.** Two are panel readings I recomputed but could
  not re-read (the gnomAD 7355/21694 screenshot, the 1.10× γ-H2AX bar), and the Khadija ratios
  (10/54, 16/54, 4/107, 13.17 Mb) recompute but their source is a `.docx` I did not open. A number
  the records omit is invisible to this check.
- **The valproate reading** rests on supplements absent from this disk (F4). All-absent means
  *not re-measurable here*, never *unsupported* — the lesson that a negative finding must itself be
  verified cuts both ways.
- **B5** read the riserva as written. It did **not** re-derive the exon-5 structural call from the
  artefact's own supplementary row; a wrong genotype interpretation inside the source would not show
  in this check, and the batch's own blind audit covered the propositions rather than the variant
  calling.
- **H** counted vocabulary, not rhetoric. A record can overstate with none of those words.

---

## Candidates written by this review

| Candidate | Finding | Ops | File(s) |
|---|---|---:|---|
| `CC-20261004-MIRROR-31` | F1 | 2 | `registries/paper_registry_current.md` · `registries/literature_tracking_log_current.md` |
| `CC-20261004-MIRROR-32` | F2 | 1 | `registries/claim_registry_current.md` |
| `CC-20261004-MIRROR-33` | F3 | 1 | `registries/paper_registry_current.md` |
| `CC-20261004-MIRROR-34` | F4 | 1 | `research/discovery_ledger_current.md` |
| `CC-20261004-MIRROR-35` | F5 + F6 | 2 | `registries/claim_registry_current.md` |

Each `old` was measured **unique inside its record and in the whole file** immediately before the
candidate was written, and each candidate says the propagating batch must re-measure it. `D6` gets
no candidate: the ops are already written in `CC-20260826-GSK3B-S9-AXIS-01`, and authoring that
boundary's text is Scientist work, not Mirror's.

---

## DEFAULTS_TAKEN (§21c)

| Condition | Default taken | Why it is safe | What would have been different |
|---|---|---|---|
| A safety classifier halted a plain `Read` of the `_002` report | Switched to a line-slice script and read the rest, and both reports, that way; recorded the halt | No content was reworded or retried; every figure here carries its command | A reworded retry, which the brief forbids |
| `files/` is outside the worktree | Read the root tree in place, read-only, through tag-stripping window scripts | No byte written under `files/` | A hardlink copy, which this review did not make |
| The worktree was cut from an older `main` | Reset the task branch to `main` `ce4aa9c`, which contains both batches, before measuring | `bdc61a0` is an ancestor of the measured tree | Measuring a tree neither batch produced |
| Two batches, one review file, as the brief directs | Verdicts keyed `B*` (wave 8) and `C*` (wave 9) so each author can read only their own rows | Nothing is attributed across batches; F3/F5 name the batch that caused them | Two files and a duplicated method note |
| `test_batch_queue.py` is red here | Attributed to wave 10's unregistered PMID 21476439 and **not** counted against either batch, after reproducing the identical single-PMID failure | The `_003` addendum measured it on an export of `main` and I reproduced it on `main` itself | A finding against batches that did not cause it |
| The backlog counter reads 9, not the 4 residue items | Attributed the five extra to wave 10, landed after both batches | They are named in wave-10 files neither batch touched | A finding about another actor's queue |
| No `scipy` on this deployment, and two F-tests had to be recomputed | Implemented the regularized incomplete beta locally and printed both p-values | Both reproduce the source's printed values to four digits, which is the test | Accepting two printed p-values unchecked |
| `public_release_gate.py` blocked **this review's own first draft** five times, on F2's quotation and on an F7 heading | Rewrote both to describe the class, trimmed the same quotation out of `CC-20261004-MIRROR-32`'s prose (it survives **once**, as the op's `old`), and re-ran: **exit 0, 0 BLOCK**, and no `[REVIEW]` line names any file this review wrote | The finding is unchanged and the repair it proposes is unchanged; only this file's wording was | A review shipping the exact string whose removal it asks for — the third instance of the pull `BATCH_20261004_002` named |
| Findings need registry edits Mirror may not make | Wrote five candidates with exact ops and measured `old` | §21e: a finding is a new task for the author | A Mirror registry edit, which the role contract forbids |
| Two findings are wording or routing judgements (F7, F8) | Filed as NOTE with the correction named, no candidate | A candidate for a judgement call pre-empts the author | Two candidates nobody asked for |
| `D6` was reserved to Mirror and the author asked for the ruling or a statement of what evidence I lack | **Decided it** (`MINOR`, with two binding conditions) after measuring both claims' live `Status` and the absence of the boundary | The classification question was answerable by measurement; the substance of the exclusion is not mine and is explicitly left open | A ninth deferral of a bound that no actor but Mirror could unblock |

**Review path:**
`disease-models/wwox/research/session_evaluations/mirror_review_batches_20261004_002_003.md`

**Not medical advice.**
