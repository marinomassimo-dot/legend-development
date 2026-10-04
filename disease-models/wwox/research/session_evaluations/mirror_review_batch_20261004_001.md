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
