# WOREE_RESCUE_REFERENCE — bound from the evidence this repository holds

> **Non-canonical research record.** Scaffold built by Harness Engineering (`plan`) on 2026-10-20
> under `PLAN-REPURPOSING-INTEGRATION-20261020`; **filled by `scientist-c` on 2026-10-21** under
> `REPURP-P3-RESCUEREF-C-20261021`. It touches none of the four scientific current files and no
> `BATCH_COMMIT` accompanies it. Nothing here is medical advice; no dose, route or schedule for
> any person; class level only; paediatric suitability is not presumed anywhere below.
>
> `context_policy: QUESTION_DRIVEN` — declared, not `SOURCE_FIRST`. The dispatch stated LEGEND's
> current position (CLAIM 011 flagged over *dose-dependent* against a threshold) and the task was
> a re-read of named panels against a named question. What was admitted before the source was
> re-opened is listed in the task record's `TASK_ACK`.

## 0 · What changed on 2026-10-21

Harness Engineering's §0 measured that the paper the roadmap wanted transcribed from an abstract
is already a complete read here: PMID **42422765** = DOI 10.1016/j.omta.2026.201791 =
PMCID PMC13343157, `PAPER 011` / `CLAIM 011`, twelve receipts, one `complete_fulltext_read`
(`FTR-20260814-42422765-06`), a schema-v2 manifest now carrying **40** locator entries, a 55 KB
locator dossier and both supplements on disk. That measurement stands and is not re-derived here.

This fill does three things:

1. binds every cell it can from those locators and from a **native-resolution re-inspection** of
   the panels the five families rest on — the 726 px PMC CDN rasters the earlier reads used are
   replaced, for the panels below, by the 300 dpi rasters embedded in the publisher PDF and by
   400 dpi page renders of the two surfaces that are partly vector;
2. leaves `NOT_YET_BOUND` where the evidence does not reach, and says in the cell what would
   bind it;
3. records the adjudication of the `CLAIM 011` dose flag, in §3, as the task required.

**Surfaces re-opened as images, with digests.** All live in the shared checkout's `files/`.

| Surface | Path | sha256 | What it is |
|---|---|---|---|
| Publisher PDF | `files/supplement/PMID42422765_r2/PMC13343157.1.pdf` | `8850ea32d27a638b4ab8a38bfc9281ac9bac269a70e8c27302dd1001f92cbee4` | 17 pp., Elsevier; figures embedded at 300 dpi |
| Supplement | `files/supplement/PMID42422765/mmc1.pdf` | `dd4919a80af937037309eddd2939db4f11af230e00849bf4b362832bcb5572e9` | S1–S8 |
| JATS XML | `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` | `7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2` | body + captions; exponents squashed (see §3.2) |
| Figure 1 raster | `files/figures/PMID42422765_r2/native_renders_20261021/fig1_PMC13343157_p03_embedded_1993x1968.png` | `36089c2f67646ef3543002fd94507f1d2d5556283b3173edf31aae7cff6b3dd2` | `pdfimages -png -f 3 -l 3`, 1993×1968 |
| Figure 3 raster | `…/fig3_PMC13343157_p06_embedded_1744x1699.png` | `9152439cab8c2d56ee8312fd0b955d6aeb6411cdb10471786b4534ca6c753d3b` | `pdfimages -png -f 6 -l 6`, 1744×1699 |
| Figure 6 raster | `…/fig6_PMC13343157_p10_embedded_1744x1617.png` | `2fb1c5e3a10c595c6c2023977103d959364464dee3cd7b684da6111e6744a83e` | `pdfimages -png -f 10 -l 10`, 1744×1617 |
| Figure 7 page | `…/fig7_PMC13343157_p11_pagerender_400dpi.png` | `409c46a23bb56f71fa2030d37c55473d4641bb60ba7f8c3598aec055f24894f8` | `pdftoppm -r 400 -f 11 -l 11`, 3350×4350 |
| Figure S7 page | `…/figS7_mmc1_p09_pagerender_400dpi.png` | `8bddedc97603c7cd573cdd17a1e9ddefc3abe997877876623feb5cbf407a05cf` | `pdftoppm -r 400 -f 9 -l 9`, 3402×4394 |

Extractors: poppler-utils 24.02.0 (`pdfimages`, `pdftoppm`). Figure-to-file pairing was taken
from `figure_legend_pairs.py` over the JATS XML and cross-checked by aspect ratio against the
PDF's embedded images, because file numbers are not figure numbers: `ga1`↔graphical abstract,
`gr1`↔Figure 1 … `gr7`↔Figure 7, eight figures, zero flagged rows. Figure 7 is the one figure
whose plots are **vector** in the PDF — its embedded raster is only the ECoG traces — which is
why it is read from a page render rather than an extracted image.

## 1 · What the scaffold demands per row — unchanged

Every endpoint family takes **one row per measure**, and a row is complete only when all eight
columns are bound: `figure_or_table` · `model` · `control` · `age` · `intervention` ·
`direction` · `duration` · `limits`. The binding rules of the original scaffold stand verbatim:
the panel identifier plus the locator or receipt that attests it, never the roadmap's prose;
the comparator actually run, never "improved"; the measurement age, never the intervention
window reused as one; the dose **with its unit convention as printed**; a direction never
inferred from another endpoint in the same paper; the duration of the *effect*, not the survival
of the cohort; and limits that are this measure's, not the abstract's.

Two rules the roadmap states and this card keeps, and one this fill adds:

- do not call an improvement equivalent to the control without examining the measure **and the
  power of the comparison**; a partial benefit on one useful endpoint is admissible;
- **no numeric weights.** The five families are revisable qualitative references. No candidate is
  required to cover all five; concordance with them is **not** evidence of efficacy for any
  candidate; and nothing below ranks one family above another;
- 🔴 **added here:** where the primary's own direction word is *dose-dependent*, the cell says
  **whether a low-dose arm exists for that measure at all**. Three of the five families contain
  measures with no low-dose arm, and a direction cell that omits that is not a bound cell.

Status vocabulary, unchanged and not expanded: `BOUND` (new; a sourced value with its panel) ·
`TRANSCRIBED_FROM_ROADMAP` (a sentence carried from the external deliverable, unverified here) ·
`NOT_YET_BOUND` (owed; the absence is a debt, not a negative result) · `UNKNOWN` (looked for and
not determinable from the artefacts held).

**Shared model, control and intervention vocabulary** — written once so the per-measure rows do
not restate it and cannot drift:

| Token | Bound value |
|---|---|
| `KO` | *Wwox*-null full knockout, FVB background; the allele is the **Aqeilan-laboratory targeted deletion** (Methods cite ref. 69 = Aqeilan 2007, *Targeted deletion of Wwox reveals a tumor suppressor function*) — manifest entries 34, 35 |
| `WT+RI` / `KO+RI` | wild-type, or knockout, injected with the **reference item**; the untreated comparator arm |
| `W` | AAV9-hSynI-hWWOX, **WPRE-free** in the dose study; the promoter-comparison constructs of Figure 1 are a **different architecture** — EF1α, CMV and MBP all carry WPRE (manifest entry 16) |
| `LD` | 1.23 × 10¹¹ vg **as printed**; convention undeclared by the primary (§3.2) |
| `HD` | 2.63 × 10¹¹ vg **as printed**; same ambiguity; `HD/LD = 2.1382` is invariant under every permitted reading |
| route | bilateral ICV, stereotaxic, 2.0 µL/hemisphere, one injection per hemisphere (manifest entry 32) |
| window | main cohorts injected at **P0–P1** (Figure 4A); the timing experiment's arms are **P1, P2, P3, P5** (S8A/B); the Methods section is headed *P0–P5* and the Discussion writes *"at any time point between P0 and P5"* |

---

## 2 · The five endpoint families

### 2.1 Excitability / EEG

| # | figure_or_table | model | control | age | intervention | direction | duration | limits |
|---|---|---|---|---|---|---|---|---|
| **E1** | **Figure 7E**, read at 400 dpi from the vector page render (`fig7_…_400dpi.png`); caption and running text from the JATS XML | `KO` pups | **WT littermates** and `KO+RI`; caption states *n* = 5 pups per group; at 400 dpi the panel resolves 5 markers per group | ICV at **P0**; ECoG implanted at **P14**; recording from ~P14 | `W` at **HD only** — 🔴 **there is no LD arm in this panel** | **decrease.** Spike-wave discharges/hour: WT ≈ 0.03 (points ≈ 0.00/0.00/0.02/0.04/0.06), KO ≈ 0.635 (≈ 0.32/0.62/0.70/0.74/0.80), KO+HD ≈ 0.13 (≈ 0.00/0.09/0.11/0.18/0.26). Brackets printed: `****` WT–KO, `****` KO–HD, **`ns` WT–HD** | **7 consecutive days** of continuous recording, ~P14 to ~P21. No later ECoG timepoint exists in the paper | 🔴 **Dose-dependence is NOT TESTED here** — one dose, so this measure cannot support a *dose-dependent* direction and must not be cited for one. The authors qualify it themselves: *"Although based on a limited cohort"*. Single-channel epidural montage, recording electrode above the right dorsal cortex only. **SWDs are an absence-type electrographic correlate**, not a surrogate for the tonic, clonic, tonic-clonic, myoclonic and spasm types that compose the WOREE spectrum — read with `CLAIM 031` and `CLAIM 040`. Events were screened by a blinded investigator; the Methods declare blinding only *"when feasible"* elsewhere (manifest entry 21) |
| **E2** | **Figure 7B and 7C**, same 400 dpi surface | `KO` pups | **WT littermates**; caption states *n* = 5 per group | ~P14–P21 | 🔴 **none — 7B and 7C contain no treated arm** | **increase, with a text-versus-panel conflict.** 7B: KO spike rate above WT on each of 7 days. 7C average spikes/day: WT ≈ 2.2, KO ≈ 9.3 — and the panel **prints `0.2000` above the WT–KO bracket**, while the running text says *"Averaged spike counts further confirmed a significant elevation in spike activity in KO animals (Figure 7C)"* | 7 days | 🔴 **The panel contradicts the text** (persisted manifest entries 3/4/5, re-confirmed here at 400 dpi — not a new finding and not a correction of one). At 400 dpi 7C resolves **2 distinct WT markers and 3 distinct KO markers** against a caption stating *n* = 5 per group: markers may overlap at identical values and the panel cannot discriminate, so the panel is not evidence against the caption — but it is not evidence for *n* = 5 either. This is a **disease-phenotype measure, not a rescue measure**, and it belongs to the family only as its baseline |

**Family verdict.** The excitability family is bound at **HD only**. The useful early datum is E1:
SWD incidence falls from a KO level to a level statistically indistinguishable from wild type,
in the only CNS-electrophysiological endpoint the study runs. That is a legitimate single useful
endpoint. It is **not** evidence of a dose-response, and it is **not** evidence about convulsive
seizure types. What would bind an LD cell: an LD ECoG arm — the paper does not have one, and no
re-read of this corpus can produce it.

### 2.2 Myelination

| # | figure_or_table | model | control | age | intervention | direction | duration | limits |
|---|---|---|---|---|---|---|---|---|
| **M1** | **Figure 6E**, read at 300 dpi (`fig6_…_1744x1617.png`) | `KO` | `WT` | **P18** | 🔴 **none — WT versus KO only** | **decrease in the disease state.** MBP intensity, KO relative to WT, printed as percentages above each pair: **CC 48 %, cortex 30 %, striatum 50 %, anterior commissure 70 %** | single timepoint | This is the **only MBP quantification anywhere in the paper**, and it contains **no treated arm**. It establishes the deficit, not the rescue |
| **M2** | **Figure 6C and 6D**, same surface | `KO` | `WT` | P18 | none | **decrease.** Brain weight WT ≈ 465 mg vs KO ≈ 247 mg (`****`); corpus-callosum thickness WT ≈ 322 vs KO ≈ 230 (`**`) | single timepoint | Structural correlates of the same deficit; again **no treated arm** |
| **M3** | **Figure 6F** (300 dpi) and **Figure S7I** (400 dpi page render) | `KO` | `WT+RI` | 🔴 **UNKNOWN for 6F** — neither the caption nor the Results paragraph states an age for panel F; **S7I is ~P90** per its caption | `W` at `LD` **and** `HD` — both arms present | 🔴 **QUALITATIVE ONLY.** Both panels are representative micrographs with no axis, no bar and no significance marker. The authors' reading is *"HD treatment achieved near-complete rescue across affected regions, whereas LD treatment produced only partial recovery relative to HD (Figures 6F; S7I)"* — recorded as the **authors' interpretation of an unquantified image**, not as a measured direction | S7I attests ~P90; 6F attests no timepoint | 🔴 **The dose-dependence of myelination is never quantified** (manifest entry 6; re-confirmed here at 300 and 400 dpi). 🔴 **6F additionally has no untreated-KO column** — its three columns are WT, LD, HD — so within that panel the treated arms have no disease baseline; the baseline is in 6A/6B at a different age and magnification. What would bind a direction cell: MBP densitometry of the LD and HD arms against both WT and KO at a stated age. Nothing in the artefacts held supplies it |

**The oligodendrocyte boundary — stated here because this is the family where it is read wrongly.**
Figure 1 panels G, H, I and M, read at 300 dpi (`fig1_…_1993x1968.png`): the **MBP-promoter**
construct `AAV9-MBP-hWWOX-WPRE` (4 × 10¹⁰ vg, *n* = 5) produced **no benefit on any endpoint it
was measured on** — survival identical to `KO+RI` (both arms at 0 % by ~day 16–17, panel G), body
weight tracking `KO+RI` (panel H), and P14 glucose ≈ 52 mg/dL against `KO+RI` ≈ 58 and WT ≈ 137,
with the bracket printed **`ns`** between `KO+RI` and MBP+W and `****` between WT and `KO+RI`
(panel I). 🔴 **This does not show that oligodendrocytes are useless as a pharmacological target,
and the card must not be cited as if it did.** Panel M shows WWOX immunoreactivity in cortex as
**essentially blank in the MBP column** while the synapsin column is strong and cellular
(manifest entry 17): the construct produced **essentially no detectable protein**, so the
oligodendrocyte question is **unanswered by this experiment rather than answered negatively**.
The configuration differs too — the promoter-comparison vectors all carry WPRE and were given at
4 × 10¹⁰ vg, which is **not** the 4 × 10¹⁰ of Figures 2 and 3 (manifest entry 16) — and panel M
images **cortex**, where oligodendrocyte density is lower than in white matter, with no
corpus-callosum column shown. The authors' own Discussion sentence, *"expression in
oligodendrocytes alone is insufficient to confer benefit"*, is their interpretation of this
experiment and is recorded as such. `REVIVAL_TRIGGER`: an oligodendrocyte-directed construct that
demonstrates measurable WWOX protein in white matter and is then tested — or any re-test of the
MBP arm with an expression readout that is not blank.

### 2.3 Neuroinflammation / gliosis

| # | figure_or_table | model | control | age | intervention | direction | duration | limits |
|---|---|---|---|---|---|---|---|---|
| **G1** | **Figure S7A–S7B**, 400 dpi page render (`figS7_…_400dpi.png`) | `KO` | `WT` (labelled WT-RI / KO-RI) | **P20**, stated in the caption | none | **increase in the disease state.** % Iba1 area: WT ≈ 4.5, KO ≈ 7.6; bracket `*` | single timepoint | Disease baseline only |
| **G2** | **Figure S7C–S7D**, same surface | `KO` | `WT` | **P20** | none | **increase in the disease state.** % GFAP area: WT ≈ 3.7, KO ≈ 23.7; bracket `***` | single timepoint | Disease baseline only |
| **G3** | **Figure S7E–S7F**, same surface | `KO` treated | **`WT-RI` only** | 🔴 **UNKNOWN** — the S7 caption gives P20 for A–D and states no age for E–H | `W` at `LD` **and** `HD` | **no significant difference in either direction.** % Iba1 area: WT ≈ 9.3, **LD ≈ 16.2**, HD ≈ 10.8; both printed brackets are **`ns`** (WT–LD and WT–HD) | single timepoint | 🔴 **No untreated-KO arm in this panel**, so the text's *"significantly reduced … microglial density"* has no baseline to be reduced from here. 🔴 And the WT value itself moves between panels — ≈ 4.5 in S7B, ≈ 9.3 in S7F, on a different axis range — so the two panels **cannot be read across**. The LD point is numerically the highest of the three and is not significant |
| **G4** | **Figure S7G–S7H**, same surface | `KO` treated | **`WT-RI` only** | 🔴 **UNKNOWN**, as G3 | `W` at `LD` **and** `HD` | **binary, not graded.** % GFAP area: WT ≈ 1.75, **LD ≈ 3.05 (`**` against WT)**, **HD ≈ 1.9 (`ns` against WT)**. The low dose is significantly worse than wild type; the high dose is not distinguishable from it | single timepoint | Same two limits as G3 — no KO arm, and the WT value moves from ≈ 3.7 (S7D) to ≈ 1.75 (S7H) between panels. This is the family's clearest **LD-fails / HD-passes** result, and it is a comparison **against wild type**, never against the disease state |
| **G5** | **Figure S8I**, 200 dpi render (manifest entry 9; not re-opened in this fill) | `KO` treated | **`WT` and untreated `KO` together** — the only gliosis panel that has both | not stated on the panel; S8 is the **timing** experiment | `W` at **HD**, injected at **P5** | **decrease.** GFAP-positive cells: WT ≈ 5, KO ≈ 44, KO+W(P5) ≈ 5; brackets `***` (WT–KO) and `ns` (WT–treated) | single timepoint | 🔴 **This is a different experiment.** S8 varies the *timing* of a single high dose, not the dose. It supplies the untreated baseline S7 lacks, and it does **not** supply a low-dose arm. Merging it with S7 to produce a dose-response is the error this row exists to prevent |

**Family verdict.** Gliosis is the family where the primary's *dose-responsive* wording is least
supported by its own panels: the two quantified treated-arm panels (S7F, S7H) contain **no
untreated-KO comparator**, their wild-type reference values differ roughly two-fold from the
wild-type values in the disease-baseline panels of the same figure, and the only significant
treated-arm result is **LD worse than WT**, not LD intermediate between KO and HD. A glial
improvement observed after a **neuronal** rescue also does not identify a direct glial target —
that inference, which the roadmap carried, is `INFERENZA` at best and is not bound by any panel
here. What would bind a direction cell: S7-style quantification with a `KO+RI` arm in the same
panel at a stated age.

### 2.4 Growth / metabolism

| # | figure_or_table | model | control | age | intervention | direction | duration | limits |
|---|---|---|---|---|---|---|---|---|
| **W1** | **Figure 3C**, 300 dpi (`fig3_…_1744x1699.png`) | `KO` | `WT+RI` and `KO+RI` | P0 → **P30**, sampled every 5 days | `W` at `LD` **and** `HD` | 🔴 **increase, and NOT dose-graded.** Weight at P30: WT ≈ 17.5 g, **LD ≈ 15.3 g, HD ≈ 15.6 g** — the two treated arms are superimposed. `KO+RI` ends at P15 at ≈ 4.7 g | to P30 | 🔴 **No significance markers are printed on panel C at all** — no asterisk, no `ns`, on any pair. Both treated arms remain slightly below WT at P30 and the panel does not test whether that gap is significant |
| **W2** | **Figure 3D**, same surface | `KO` | `WT+RI`, `KO+RI` | P0 → **P180** | `W` at `LD` **and** `HD` | **increase, sustained at HD.** WT ≈ 26.9 g and HD ≈ 26.0 g at P180, error bars overlapping throughout. 🔴 **The LD curve ends at ~day 60 at ≈ 21 g** — near the WT value at that age — because the LD animals die, not because the weight fell | HD followed to **180 days**; LD to ~60 days; `KO+RI` to ~15 days | 🔴 **Duration of the LD arm is survival-limited, and the panel must not be read as LD growth failing.** On body weight the low dose is **not** the failure the survival curve shows it to be. No significance markers on panel D either |
| **W3** | **Figure 3E** | `KO` | `WT+RI` **and** `KO+RI` | **P10** | `W` at `LD` **and** `HD` | **partial and not significant against the disease state.** Glucose mg/dL: WT ≈ 130, `KO+RI` ≈ 95 (`*` against WT), LD ≈ 105, HD ≈ 113 — **both treated arms `ns` against WT and `ns` against `KO+RI`** | single timepoint | 🔴 The only glucose panel that still **has** an untreated-KO arm, and in it neither dose is significantly different from untreated. The running text's *"from P10 both doses partially corrected hypoglycemia"* is qualified by this panel (manifest entries 36/37, `panel_qualifies_text`) |
| **W4** | **Figure 3F** | `KO` | `WT+RI` only | **P20** | `W` at `LD` **and** `HD` | 🟢 **graded — this is the family's genuine dose-response.** WT ≈ 145, **LD ≈ 128 (`*` against WT)**, **HD ≈ 147 (`ns` against WT, `**` against LD)** | single timepoint | 🔴 **No `KO+RI` arm: those animals are dead by P20**, so the comparison is treated-against-wild-type only. This is the one glycaemic measure on which LD and HD separate |
| **W5** | **Figure 3G** | `KO` | `WT+RI` only | **P30** | `W` at `LD` **and** `HD` | **no difference.** All three groups ≈ 160–170 mg/dL; all printed brackets `ns` | single timepoint | No `KO+RI` arm, same reason. By P30 the dose separation of W4 has closed |
| **W6** | **Figure 3H** | `KO` | `WT+RI` only | **P180** | `W` at **HD only** | **no difference.** WT ≈ 197, HD ≈ 188; bracket `ns` | single timepoint at 180 days | HD only; no LD arm survives to P180 |

**Family verdict.** Growth and glycaemia are bound and are the family that most repays reading in
full, because **the dose behaves differently in each of its measures**: body weight is *not*
graded (LD = HD, W1), P10 glucose is *not* corrected by either dose against the disease state
(W3), P20 glucose *is* graded (W4), and by P30 the difference is gone (W5). A systemic readout
after a brain-directed intervention still needs its own mechanism statement, and this study
supplies none: no mechanism linking neuronal WWOX restoration to glycaemia is measured anywhere
in it. That gap is an `IPOTESI` to be tested, not a limitation to be waived.

### 2.5 Survival / function

| # | figure_or_table | model | control | age | intervention | direction | duration | limits |
|---|---|---|---|---|---|---|---|---|
| **S1** | **Figure 3B**, 300 dpi (`fig3_…_1744x1699.png`), re-inspected at native resolution and measured against the printed axes — **the adjudication panel of §3** | `KO` | **`WT+RI` (*n* = 20) and `KO+RI` (*n* = 10)**, both plotted | ICV at P0–P1; followed to **300 days** | `W` at `LD` (*n* = 20) **and** `HD` (*n* = 30) | 🔴 **increase at both doses, but only HD is durable, and the two are qualitatively different.** Measured off the axes: `KO+RI` first death ~day 9, **0 % by ~day 15**; **`LD` holds 100 % to ~day 18, declines, and reaches 0 % at ~day 78–81**; **`HD` holds 100 % to ~day 24 and plateaus at 76–77 % from ~day 80 through day 300**; `WT+RI` is at 100 % to ~day 45, ≈ 89–90 % to ~day 122, and **≈ 71–72 % from ~day 126 through day 300**. Caption statistics: HD vs WT **p = 0.78**, HD vs LD p < 0.0001, LD vs `KO+RI` p < 0.0001 | HD: effect held to **300 days**, the end of the plot. LD: ~80 days, at which point the arm is extinct | 🔴 **Read the duration of the effect, not the survival of the cohort.** LD's benefit is a **postponement of death**, not a durable rescue; HD's plateau sits **at or marginally above the wild-type control's own survival** (76–77 % vs 71–72 %), which is what `p = 0.78` says and which also means *"comparable to WT"* here includes a wild-type arm that itself lost ~29 % of its animals over 300 days. Two doses cannot locate a threshold (§3.1). The absolute dose is uncertain by exactly a factor of two (§3.2) |
| **S2** | **Figure S8A–S8D**, 200 dpi render (manifest entry 10; not re-opened in this fill) | `KO` | `KO+RI` (*n* = 6), dead by ~day 15 | injection at **P1 (*n* = 6), P2 (*n* = 6), P3 (*n* = 3), P5 (*n* = 7)**; weight and glucose at **P14** | `W` at **HD only**, timing varied | **increase.** S8B: the **P1 and P5** arms plateau near **75 % to 300 days**. S8C/S8D: `***` and `**` for WT vs KO, and a **single `ns` spanning all five treated timepoints against WT** | to 300 days for P1 and P5 | 🔴 **The 300-day plot shows only P1 and P5**; P2, P3 and P4 appear solely in the 40-day panel, and **P3 is an *n* = 3 arm that lost animals** (down to ~67 % at ~day 24). 🔴 **The tested window is P1–P5** on the panels, while the Methods heading and the Discussion both write *P0–P5* and the main cohorts were injected at P0–P1. 🔴 **`NOT_MEASURED` is not `SMALLER`:** the authors state *"Therapeutic rescue beyond this early postnatal window was not explored, as* Wwox*-null mice rapidly deteriorate with progressive neurological dysfunction and early lethality, precluding effective intervention at later stages."* That is a statement about what was not done and why — it is **not** a measurement that later treatment helps less. Nothing in this corpus bounds efficacy after P5 in either direction |
| **S3** | **Figure 4B–4K**, 104 ppi (manifest entries 0/1/2; not re-opened in this fill — see §3.3) | `KO` | **`WT` only (*n* = 9) against `KO+HD` (*n* = 10)** | behaviour at **3 months**; injection at P0–P1 | `W` at **HD only** | **mixed, and partly counter-directional.** The text states *"Locomotor activity parameters … showed no significant differences between groups (Figures 4B, 4D–4G)"*, while the same figure prints an asterisk on 4D (velocity) and 4E (distance), and panel **4K reports treated animals with significantly higher rotarod latency than WT** | single session at 3 months | 🔴 **There is no untreated-disease arm, by construction:** *"Behavioral testing could not be performed in untreated* Wwox*-null mice due to severe morbidity and early lethality, and LD-treated mice did not survive to P90; therefore, analyses were limited to WT and HD-treated groups."* 🔴 **No cognitive endpoint is measured anywhere in the study.** The 4D/4E text-versus-panel conflict is a persisted, declared contradiction whose figure bytes the blind audit returned `UNVERIFIABLE_SURFACE`; it is **not adjudicated here** (§3.3). No multiplicity correction is declared by either side |
| **S4** | **Figure S4A–S4E**, 300 dpi render (manifest entry 27; not re-opened in this fill) | `KO` | `WT` and `KO` | not stated on the panel | `W` at `LD` **and** `HD` | 🟢 **graded.** Composite motor score: WT ≈ 0, KO ≈ 3.6, **LD ≈ 1.8**, **HD ≈ 0.3**; **WT–HD `ns`**, **LD–HD `***`**. The low dose is genuinely intermediate | single assessment | Fertility (S4C–S4D) rests on roughly **three plotted observations per group** and has **no untreated-KO comparator**. The motor measure is the clearest graded dose-response in the whole study and it is in a supplement, not in the main figures |

**Family verdict.** Survival is bound with the sharpest result in the paper and the sharpest
limit: HD produces survival indistinguishable from the wild-type control to 300 days, LD does
not produce survival at all past ~80 days, and the function measures that could tell the two
apart either do not exist at LD (S3, behaviour) or are the one place where LD is genuinely
intermediate (S4, motor). **A single useful endpoint is a legitimate early benefit** and this
family supplies two of them; neither is a dose-response.

---

## 3 · The divergences the original scaffold asked the filler to resolve

### 3.1 🔴 ADJUDICATION of the `CLAIM 011` review flag — **NARROW**

The flag, raised 2026-08-10 (`CC-20260810-CLAIM011-REVIEW`), says that *"dose-dependent"*
describes a continuum where the panel shows a **threshold**. Figure 3B was re-inspected **as an
image at native resolution** before any of this was written: the 300 dpi raster embedded in the
publisher PDF (`fig3_…_1744x1699.png`, sha256 `9152439c…53d3b`), 2.4 × the linear detail of the
726 px PMC CDN file `gr3.jpg` the flag was written from, with the curve values read off the
printed axes (x ticks at 0/100/200/300 days; y ticks at 0/50/100 %).

**Verdict: NARROW.** Neither KEEP nor REVERSE survives the measurement, for a reason neither the
claim nor the flag states: *dose-dependent* is **true of some endpoints of this study and false
of others**, and the title binds it to exactly the three where it is weakest.

**What the evidence supports, endpoint by endpoint:**

| Endpoint | LD | HD | Is it dose-graded? |
|---|---|---|---|
| Survival (3B) | 0 % by ~day 78–81 | 76–77 % plateau to day 300 | 🔴 **no — step** |
| Body weight P30 (3C) | 15.3 g | 15.6 g | 🔴 **no — equal** |
| Body weight to P180 (3D) | tracks WT to ~day 60, arm then extinct | tracks WT to day 180 | level equal; **duration** differs |
| Glucose P10 (3E) | ns vs WT **and ns vs KO** | ns vs WT and ns vs KO | no |
| Glucose P20 (3F) | `*` vs WT | `ns` vs WT, `**` vs LD | 🟢 **yes** |
| Glucose P30 (3G) | ns | ns | no — difference closed |
| Vector genomes + mRNA, P30 (5A–5H) | — | — | 🔴 **no — 7 of 8 regional comparisons `ns`** (manifest entry 12) |
| WWOX protein P30 (5I–5L) | lower | higher | 🟢 yes (authors: *"a marked dose-dependent increase in WWOX protein"*) |
| Myelination (6F, S7I) | "partial" | "near-complete" | 🔴 **never quantified** |
| Microglia % Iba1 (S7F) | 16.2, `ns` vs WT | 10.8, `ns` vs WT | no — and no KO arm |
| Astrocytes % GFAP (S7H) | 3.05, `**` vs WT | 1.9, `ns` vs WT | 🔴 **binary** — and no KO arm |
| Motor score (S4A) | 1.8 | 0.3; LD–HD `***` | 🟢 **yes** |
| ECoG / SWD (7E) | **no arm** | 0.13/h, `ns` vs WT | 🔴 **not testable** |
| Behaviour at 3 months (Fig 4) | **no arm** — did not survive to P90 | — | 🔴 **not testable** |

**The narrowing, stated so it can be audited:**

1. **KEEP** *dose-dependent* where the data are graded and say which: **WWOX protein expression**
   (5I–5L), **glycaemia at P20** (3F) and the **composite motor score** (S4A). On these the
   authors' word is accurate and the low dose is genuinely intermediate.
2. **NARROW** it for **survival**, which is the endpoint the claim's own title binds it to.
   *Durable* rescue is a property of the **high dose alone** in this study: the LD curve reaches
   zero. LD does significantly extend life against `KO+RI` (p < 0.0001) — so "LD does nothing"
   would be a **reversal in the wrong direction and is refused here** — but a benefit that ends
   in an extinct arm at ~80 days is a postponement, not a durable rescue, and the two recommend
   different trials exactly as the flag says.
3. **NARROW** it for **body weight**, where the flag is silent and the panel is explicit:
   **LD = HD at P30** (15.3 vs 15.6 g, with no significance marker printed on the panel at all).
   A reader who carries "more dose, more benefit" is wrong about weight in the opposite
   direction from the one the flag warns about.
4. **NARROW the three domains the title names.** `ECoG/SWD` has **no low-dose arm** and therefore
   cannot be part of a dose-dependent claim at all; **myelination** is unquantified in every
   treated arm; **gliosis** is binary (LD worse than WT, HD not) and its treated-arm panels carry
   **no untreated-KO comparator**. The title's *"dose-dependent durable rescue … on multiple
   domains including ECoG/SWD, myelination and gliosis"* names, as the content of its
   dose-dependence, the three domains where dose-dependence is least supported.
5. 🔴 **NARROW the flag's own inference.** *"The panel places a threshold between 1.23 and
   2.63 × 10¹¹ vg"* claims more than two dose points can carry: with two arms a step and a steep
   continuum are indistinguishable, and what the panel **refuses** is linear interpolation of
   durable benefit, not the existence of intermediate behaviour. The step reading is
   **strengthened, not established,** by assembling four dose levels across two figures — Figure
   2B's `AAV9-hSynI-hWWOX` arms at 4 × 10¹⁰ (*n* = 3) and 8 × 10¹⁰ (*n* = 5), same promoter, same
   WPRE-free architecture, **no survivors in either** (manifest entry 14), against 1.23 × 10¹¹
   (extinct at ~80 days) and 2.63 × 10¹¹ (76–77 % at 300 days) — so durable survival reads
   0 / 0 / 0 / ~76 % across four doses. 🔴 **The arms are different cohorts in different
   experiments**, and manifest entry 14 already records that the running text claims 8 × 10¹⁰
   rescued lethality where the panel reading does not; that discrepancy is carried unresolved,
   with the presumption left in favour of the text.
6. 🔴 **Two numbers in the flag's prose are corrected by measurement.** The flag writes that LD
   *"shifts death from ~20 to ~90 days"* and that HD *"plateaus at ~80 % to 300 days"*. Measured
   off the axes: `KO+RI` reaches 0 % at **~day 15**, LD at **~day 78–81**, and the HD plateau is
   **76–77 %**. 🔴 **Neither value sits behind a persisted verbatim locator** — the manifest's 40
   entries contain no Figure 3B entry at all, which is why §4 adds one — so this corrects claim
   **prose**, not a locator, and the fourth mandatory audit trigger does not fire on it. The
   measurement also adds the fact the flag's "~80 %" obscures: **the wild-type control arm itself
   ends at 71–72 %**, below the high-dose arm.

**What does not change.** The claim's `Type`, `Transferability: T2`, its genotype caution, its
`PREMISE_TAG` on the dose ceiling, its `REVIVAL_TRIGGER` (an intermediate-dose arm, defined as a
fraction of the primary's HD rather than in absolute vg) and its configuration boundary are all
untouched by this adjudication and are re-affirmed by it.

**Audit status.** `CLAIM 011`'s `Status` is `flagged for review`, **not** `consolidated
baseline`, and this reading contradicts, corrects or replaces **no persisted verbatim locator**
— it confirms two (entries 3/5, Figure 7C at 400 dpi) and qualifies none. **The mandatory
triggers of `legend-locator-audit` therefore do not fire by the letter.** A **voluntary blind
audit is recommended anyway** over the new Figure 3B triples and the five new panel
attestations below, because the claim's clinical relevance is HIGH and it feeds `CLAIM 031` and
`CLAIM 040`. 🔴 **Producer is not verifier: this adjudication is not certified by its own
author, and nothing here is propagated.** No registry file is touched; the proposal travels as
`CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01` and the Orchestrator routes both the
audit and the commit.

### 3.2 Dose unit convention — unchanged, and restated because every `intervention` cell depends on it

The primary **never declares its unit convention**: bare `vg` on every surface, `hemisphere`
adjacent to no dose, and **no dose anywhere in the Methods** — the only vector quantity there is
*"Viral titers were determined by RT-qPCR using bGH primers."* (manifest entry 33). Injection is
bilateral ICV, *"delivering 2.0 μL/hemisphere"*, one per hemisphere (entry 32). The absolute dose
per animal is therefore uncertain by **exactly a factor of two** — LD ∈ [1.23, 2.46] × 10¹¹ vg,
HD ∈ [2.63, 5.26] × 10¹¹ vg — while **`HD/LD = 2.1382` is invariant** under every permitted
reading. 🟢 **Nothing in §3.1 depends on the ambiguity.** 🔴 And no dose may be quoted from an
extracted surface: the PMC text route **deletes** the exponent (`1.23 × 10vg`) and the JATS route
**squashes** it (`10<sup>11</sup>` → `1011`). The values above were read from the **rendered
panel and page**, not from a text layer.

### 3.3 Which endpoints the complete read resolved — and the one it did not

`CLAIM 011` recorded that the three remaining domains are resolved by the complete read *"and not
all in the same direction"*. Measured here: **ECoG/SWD is resolved at HD only (E1); myelination
is resolved as unquantified in every treated arm (M3); gliosis is resolved as binary against
wild type with no disease comparator (G3/G4).** The directions the original scaffold pre-filled
from the roadmap — "improvement of excitability", "improvement of myelination", "improvement of
gliosis" — are **not promoted**: the first is kept with its single-dose bound, the second is
demoted to an author interpretation of an unquantified image, and the third is replaced by the
binary result the panels actually print.

🔴 **One conflict is deliberately left open and is not adjudicated by this task.** The Figure 4
text-versus-panel contradiction (4D/4E asterisks against the text's *"no significant
differences"*) and the declared panel attestation *"3 of the 8 Figure 4 panels differ from WT in
the direction of excess"* turned `UNVERIFIABLE_SURFACE` in the blind audit for want of bytes.
Figure 4's bytes **are** now reachable — `gr4.jpg` is on disk and the publisher PDF carries the
panel at 300 dpi on page 7 — but adjudicating it is a different question from this task's, it
would touch a different part of the claim, and settling it inside a dose adjudication would
bury it. It is reported as the next measurement worth making (§5).

## 4 · What this fill owes forward

- **The manifest gains six locator entries** (one body, five figure attestations): Figure 3B
  measured off its axes; Figure 3C/3D growth; Figure 6E/6F with the missing-KO-column fact;
  Figure 1G/1H/1I/1M for the oligodendrocyte boundary; Figure S7 at 400 dpi with the
  cross-panel wild-type discrepancy; Figure 7E at 400 dpi with the absent LD arm. Each names the
  digest of the surface it was read from. They are additions; **no existing entry is edited**.
- **The receipt is staged, never recorded** —
  `research/receipt_staging/scientist-c/FTR-20261021-42422765-01.json`,
  `reread_reason: new_question_outside_prior_coverage`, `prior_receipt: FTR-20261019-42422765-01`.
  The Orchestrator records it in event-ID order.
- **Nothing reaches the four scientific current files**, `disease_model.md`, the roadmap, the
  scout log, the clinical census or `repurposing_bridge.py`. This card and the commit candidate
  are the whole output surface.

## 5 · What this reference is not — unchanged, and now bound

- **It is not Q230P evidence.** The model is a *Wwox*-null full knockout on FVB carrying the
  Aqeilan 2007 targeted-deletion allele. It is neither the Q230P missense allele nor a compound
  heterozygote. The design principles — neuron targeting, expression control, dose, early window
  — transfer to trial-readiness logic; **the expected level of rescue in the reference genotype
  does not follow from this study** in either direction, and partial residual function is a
  reason to expect a *different* result, not a larger one.
- **It is not a reusable RNA-seq rescue signature.** There is no rescue-versus-knockout
  transcriptomic contrast in this study to invert, to feed to a perturbation model or to pass to
  LINCS/iLINCS. GSE156243 is a knockout-versus-wild-type organoid contrast and is **not** this
  study's rescue arm; the two must not be merged.
- **It is not an endpoint weighting.** Five revisable qualitative references, no numeric weight,
  no coverage requirement, and concordance with them is not evidence of efficacy for any
  candidate.
- **It is not a safety assessment.** The study reports **no overexpression-toxicity endpoint and
  no tumour surveillance at all**, and the long-term expression it does report is regionally
  uneven, supraphysiological in survivors and survivor-selected (`PREMISE: NOBODY_LOOKED` on the
  upper bound, `CLAIM 011`). The construct is neuron-specific but **not CNS-confined**: WWOX
  protein reaches the sciatic nerve of high-dose animals while the liver stays at background
  (manifest entries 18/19).
- **It is not medical advice, and it names no dose, route, schedule or paediatric suitability for
  any person.**

---

**The one measurement that would most change this card.** An **intermediate-dose arm** —
defined as a fraction of the primary's HD (between 1 × and 2.14 × the LD), never in absolute vg,
because the unit convention is undeclared and the absolute number is not reproducible by another
laboratory — **carried to 300 days with survival, weight, glycaemia, ECoG and quantified MBP
measured in the same animals**. It would settle in one experiment whether durable survival is a
step or a steep continuum, whether the ECoG benefit is dose-dependent at all, and whether
myelination rescue is graded; and it would do so with the only endpoint set in which the four
families can be compared within one cohort instead of across panels with incompatible
comparators.
