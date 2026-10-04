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

`CLAIM 033`'s riserva (1) reads *«… maternal inheritance establishes phase in trans …»* and then,
in the same sentence, *«the source names the relationship; this record does not, because a parental
side does not belong in a statement about the reference genotype»*. `public_release_gate.py` does
not see it, because its rule needs **both** sides paired; it flags the three *other* surfaces of
the same reading as `[REVIEW]`. `BATCH_20261004_002` wrote the lesson — *describe the class, do not
paste the instance* — and this is the one place in the four current registries where a parental
side survives (measured: **1** occurrence of `maternal|paternal` in all four). The phase statement
loses nothing: *parental segregation* establishes phase in trans.

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

## F7 — the gate's three `[REVIEW]` parent-of-origin lines all sit in wave-8/9 authored surfaces (NOTE, no candidate)

`CC-20261004W8-A-PATIENT-OVERLAP-01`, `-A-REGISTRY-01` and `CC-20261004W9-C-DEEPINTRONIC-01` each
pair a maternal and a paternal side for an individual in a published cohort. The gate returns
`[REVIEW]`, not `[BLOCK]`, by design — the variants are not the reference genotype's — and the
landed registries are clean. It is written down because candidates are shipped surfaces too, the
decision *«read it before publishing»* is the operator's, and this is the second batch whose
candidate bodies carry the instance while its records carry the class.

## F8 — the paragraph-number defect the `_002` report measured was not routed anywhere (NOTE, no candidate)

Two blind auditors independently found anchors whose **paragraph** number is off by one or two while
the section is always right, and the report named the upstream counter. Nothing in either batch
opens a harness task for it, and `_003` does not mention it. A measured tool defect with no owner
is a finding that expires.

---
