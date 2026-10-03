# MIRROR ex-post review — BATCH_20261003_003 and BATCH_20261003_004

`REVIEW_ID` MIRROR-20261004-BATCH20261003003004 · `OBJECT` `BATCH_20261003_003` (WM_v7.10 →
**WM_v7.11**, 16 candidates; wave-4 plus three Mirror repairs) landed on `main` at **`c0d4cc5`**
(+ `2f03353`), pre-batch base `f110c76`; and `BATCH_20261003_004` (WM_v7.11 → **WM_v7.12**, 17
candidates; wave-5 plus the wave-3 group-C residue, two merges) landed at **`e6df539`**,
pre-batch base `59022b2` · `LEVEL` ex-post review on the authors' request (both reports'
*Recommended next actions* item 1) · `REVIEWER` ACTOR_ID `mirror` · `AUTHORS` ACTOR_ID
`scientist` (Scientist H for `_003`, Scientist I for `_004`) · `ADJUDICATOR` each author, as a
new task.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect
> found given the available evidence bundle", never "true". READ-ONLY toward every registry: this
> review writes one file and three candidate files and edits no canonical record. **Not medical
> advice.**

**Method.** Artefacts in the root `files/` tree were read read-only and **only through scripts**
that print digests, hit counts, byte offsets, single addressed table cells and bounded context
windows — never a record body as prose. Registry records were addressed by heading span, printing
field names, truncated values, byte lengths and sha256. One early full read of a batch report was
halted by a safety classifier; it was not reworded or repeated, and every later read ran through
the slice/offset scripts named in `DEFAULTS_TAKEN`.

---

## STEELMAN (first)

- **`CLAIM 045` is the most carefully bounded new claim this repository has written.** Its own
  `Title` carries the limit ("and no endpoint beyond that is measured"); the `Bound` line states
  that **no** heterozygote-vs-control statistical test exists on any measure; the human arm is
  entered as a **negative** with a `DO_NOT_CITE`; `PREMISE_TAG` splits `DATO` (proportions) from
  `INFERENZA` (reading them as graded); `REVIVAL_TRIGGER` names the one experiment that would
  tighten it; `Impact on Working Model` is `none`. The `BLOCK 2` row (`working_model_current.md`
  line 201) reproduces class, type, pathway, transferability, status and both papers, and the
  reciprocal `Claim links` exist on **both** sources (`PAPER 004` line 112, `PAPER 156` line
  8712) — the `BATCH_20261003_001` F2 defect class is closed, not merely noted.
- **Cell-wise, the human negative is exactly right.** In
  `files/supplements/PMID35460704/mmc1.pdf` the three WWOX rows read `p.Gly30Arg` 5.61E-06 (1
  participant), `p.Arg120Trp` 7.50E-03 ClinVar **Benign** (2 participants), `p.Leu307Val`
  5.28E-05 (1) — four occurrences, three distinct alleles, as the record states; the significant
  burden genes in the body are `ABCA1`, `LDLR`, `HK3`, `CFTR`, as the record states; the cohort is
  204 participants, as the record states.
- **The `CLAIM 003` boundary note is the hardest case in either batch and it is handled
  correctly.** A `consolidated baseline` claim is touched on the strength of a **preprint**, and
  the appended text says so three times over: not peer reviewed, DOI and version printed, *«un
  preprint non alza mai lo stato di una claim»*, **same laboratory** as `PAPER 004` therefore not
  an independent observer, result **narrower** than the headline, and a two-part promotion
  condition (peer review **and** independent replication, or an oligodendrocyte-specific rescue).
  The figures reproduce verbatim in the artefact: *«O-CTR: 117.6 ± 12.5 vs. O-KO: 125.1 ± 9 per
  FOV; P = 0.22»*, with *«a subtle reduction in myelin thickness»*.
- **The two merges are real merges, not two records with one proposition.** `DIS-033` enumerates
  **eleven** PMIDs across the two disjoint candidate source sets (6 + 5), every one of the eleven
  artefacts is present, and `WWOX` occurs **0** times in all eleven — so *«all earned nulls for
  the gene»* is measured, not asserted. `RL-GT-002` lists **eight** sources against its own
  *«all eight sources»*.
- **`RL-GT-002` carries its limits where a reader cannot miss them.** The CRIM stratification
  reproduces verbatim in PMID 41314141 (*«predicted null mutations (no residual endogenous MFSD8
  protein), would be considered CRIM negative and placed on enteral prednisone, sirolimus, and
  tacrolimus»*, against two drugs for CRIM positive); the three limits the brief asks after are
  all present in `Transfer limits (binding)` — missense with stable protein is excluded by name
  (P47T, Q230P, G372R, A141T, P252A), the durability observation is marked as resting on a
  **secreted** enzyme whose antibody mechanism does not carry to an intracellular protein, and
  *«No controlled comparison of triple versus single-agent prophylaxis exists in any of these
  programmes: the pattern is correlational»*.
- **The harness fix is minimal, explained and self-reporting.** `generate_semantic_graph.py` now
  sends the research-line field table through the same `rewrite_registry_links` call the paper and
  claim notes use; all three note kinds that render a field table are covered, the comment records
  why the omission could not fire before `RL-GT-002`, and the generator still fails closed on
  `unresolved_generated_wikilinks`, so the next omission of this class cannot land silently.
  `test_generate_semantic_graph.py`: 16 tests **OK**.

---

## Verdicts by area

| # | Area | Verdict |
|---|---|---|
| A1 | `_003` `CLAIM 045`: class, premises, negatives, `BLOCK 2` row, reciprocal `PAPER` links | **CONFIRMED** · 🔸 **F3** `Wikilinks` omits `PAPER 156` |
| A2 | `_003` `CLAIM 003` boundary note and the eight amendments | **CONFIRMED** (AM1/AM3/AM5/AM7 re-verified at the artefacts) · 🔴 **F2** AM6 arithmetic |
| A3 | `_003` twelve group-C records authored from prose | **CONFIRMED** on a sample (`PAPER 161`: *«all males and females … died abruptly by P8»*, myocardial degeneration, metadata matching the artefact) |
| A4 | `_003` preprint records keyed by DOI (`PAPER 157` / `158`, `LIT`) | **CONFIRMED** — `fulltext_receipts.py status --doi 10.1101/2025.11.22.689900` resolves; both say in-record that a preprint founds no claim; `Status` is a bare vocabulary value with the qualifier on its own `Registry role` line |
| A5 | `_003` `PAPER 142` identity-then-completion | **CONFIRMED, out of scope** — the record is **byte-identical** (21 lines, 3 688 B, sha `084cb4b57244`) at `f110c76`, `59fba0b`, `d13e51d` and `e6df539`; its completion landed in `BATCH_20261003_002` (`9fea70f`), not here |
| A6 | `_004` `DIS-033` merge — do the eleven cited sources support the merged statement? | **CONFIRMED** — eleven PMIDs enumerated, eleven artefacts present, `WWOX`=0 in all eleven, each attributed statement checked at its own source (41712282 ICM/IT order-of-magnitude; 39358605 4×10¹³ vs 2–5×10¹²; 40988338 *«only ∼70% of WT levels»*) |
| A7 | `_004` `RL-GT-002` merge — is "predicted-null recipient" an INFERENCE, are the limits carried? | **CONFIRMED on the limits** · 🔸 **F4** the CRIM-negative reading of the reference genotype is stated in the indicative, its `INFERENZA` label living only in the separate `Tag` field |
| A8 | `_004` eighteen integrator amendments | **CONFIRMED** on the eight re-verified (4, 5, 6, 7, 8, 14, 17 and the `DIS-034` split) · 🔴 **F1** amendment 7's per-agent durations |
| A9 | `_004` eighteen new `PAPER` + twenty-two `LIT` records from prose and receipts | **CONFIRMED** 37/37 new registry records carry a depth label their receipt supports |
| A10 | `_004` harness fix to `generate_semantic_graph.py` | **CONFIRMED** — see STEELMAN |
| A11 | ≥ 12 carried quantitative statements vs artefacts (cell-wise for tables) | **CONFIRMED 15/16**, one defect (**F1**). Checked: 41712282 (15.7±3.1 vs 1.2±0.74 ×10³ vg/genome), 39358605 (×2 doses), 40988338 (~70 %), 41712149 (11/81 ≈14 %, 20/74 ≈27 %, three-quarters >50 mg/dL *«irrespective of attribution»*), 41966056 (16 of 17; 48 weeks; **F1**), 40809677 (four-fold = deliberate brain-volume normalisation; humoral quote), 35460704 (204; n=4; three alleles cell-wise), 31618474 (*«6.8 Mb deletion that included … SCN1A and SCN2A»*, no chromosome named), 40349107 (1,719 pg/mL reached, contrast ≤679), 35328751 (PDH *p* < 0.001 in the OE arm), PPR1124524 (117.6/125.1, *P* = 0.22) |
| A12 | Depth labels vs `fulltext_receipts.py status --pmid` | **CONFIRMED 37/37** — every `partial_fulltext_read` record also carries the literal **partial full text**; no record claims complete depth without a `complete_fulltext_read` receipt; the two records containing "read in full" (`PAPER 170`, `182`) scope it to named sections and state the complement |
| A13 | Overstatement vocabulary in added registry lines | **CONFIRMED** — of 48 `first`, 7 `demonstrat*`, 5 `establish*`, 2 `novel`, 2 `shows that`, every occurrence is negated (*«not demonstrated»*, *«NOT ESTABLISHED»*, *«establishes no ceiling»*), attributed (*«presents as novel»*), bibliographic (a full title) or carries a measurement |
| A14 | Per-line sha256 prohibition spans of `CLAIM 011` / `032` / `045` | **CONFIRMED** — `011` 3/3 digests byte-identical `f110c76`→`e6df539`; `032` 5 → 7, **0 lost**; `045` new, 3 prohibition lines; `CLAIM 003`'s single boundary digest changed and the pre-batch line is a **byte-exact prefix** of the post-batch line (+1 323 B), so the `BATCH_20260928_005` op-`B2` class is excluded by measurement |
| A15 | Gates at `e6df539` | **CONFIRMED** — `public_release_gate.py` exit 0, **BLOCKS: 0**; `growth_anchors check` **PASS** (claims 45 · papers 172 · corpus 366 · literature 456 · registry_only 4 · unread_premises 0); `fulltext_receipts verify` **OK, 375 chained**, tail anchored; LINT **BLOCK_BATCH_COMMIT ×3**, all three the `ORPHAN_COMPLETE_READ` of PMIDs 36291747 / 40507943 / 42135313 that `_004`'s report names as the merge's and not its own, plus 13 `WARN_BUT_PROCEED`, none naming `CLAIM 045` or any `_003` / `_004` record |
| A16 | Patient-overlap statements and double counting | **CONFIRMED** — Tarta-Arsene 2017 = Piard P8 carries `PREMISE: INFERENZA` with the explicit *«the new-patient count is at most 19»*; the Ehaideb sibship = Al Baradie family 2 carries `PREMISE: INFERENZA` *«not author-confirmed: count the sibship once»*; Burgess ↔ `PAPER 018` patient 6 is author-stated (*«briefly reported»* + citation) and correctly entered as `DATO` with *«One patient, counted here»*; `PAPER 171` states that its own 70-patient literature denominator double-counts both and ends *«do not use its percentages as a WOREE denominator»* · 🔸 **F5** the L239R case/cohort overlap (pre-existing debt of `BATCH_20261003_002`) |
