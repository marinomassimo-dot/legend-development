# CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01 — the dose flag on `CLAIM 011`, adjudicated against the panel at native resolution

- **Actor:** `scientist-c` · **Task:** `REPURP-P3-RESCUEREF-C-20261021`
- **Target records:** `claim_registry_current#CLAIM 011` (Title, and the flag block raised
  2026-08-10 by `CC-20260810-CLAIM011-REVIEW`). No other record is touched.
- **target_wm_version:** `WM_v7.27`
- **Change class:** **MINOR.** No claim is created, none is reversed, no record whose `Status` is
  `consolidated baseline` is touched, and `CLAIM 011`'s `Type`, `Status`, `Transferability`,
  `Source`, `Genotype/model relevance`, `PREMISE_TAG` and `REVIVAL_TRIGGER` are all left exactly
  as they stand. What moves is the **scope of one word** in the Title and in the flag, plus two
  numeric corrections to flag prose.
- **Source:** PMID 42422765 (DOI 10.1016/j.omta.2026.201791, PMCID PMC13343157), `PAPER 011`.
  Prior depth `complete_fulltext_read` (`FTR-20260814-42422765-06`). This candidate rests on a
  **targeted re-inspection of named panels at native resolution**, receipt **staged**
  `FTR-20261021-42422765-01`, manifest `deepdive_manifests/PMID42422765.json` (schema v2),
  six new locator entries, **no existing entry edited**.
- **Blind locator audit:** 🔴 **NOT RUN — and not mandatory.** `CLAIM 011`'s `Status` is
  `flagged for review`, not `consolidated baseline`; the change class is MINOR, not MAJOR; this
  reading closes no research direction; and it **contradicts, corrects or replaces no persisted
  verbatim locator** — it *confirms* two (manifest entries 3 and 5) at 400 dpi. None of the four
  mandatory triggers fires. 🟢 **A voluntary audit is nevertheless recommended** over the six new
  triples before this lands, because the claim's `clinical relevance` is HIGH and it feeds
  `CLAIM 031` and `CLAIM 040`. **Producer is not verifier: the author of this adjudication does
  not certify it.** The Orchestrator routes the audit.
- **Not medical advice. No dose, route, schedule or paediatric suitability for any person;
  class level only.**

## 1 · The flag, and what was re-opened

`CLAIM 011` has carried since 2026-08-10 the flag *«"dose-dependent" describes a continuum where
the panel shows a threshold»*, with Figure 3B cited as read from `gr3.jpg`
(sha256 `c63f930c…4997d`, 726 × 708 px, the PMC CDN raster).

Before any of this was drafted, **Figure 3B was re-inspected as an image at native resolution**:
the 300 dpi raster embedded in the publisher PDF, extracted with `pdfimages` from
`files/supplement/PMID42422765_r2/PMC13343157.1.pdf`
(sha256 `8850ea32d27a638b4ab8a38bfc9281ac9bac269a70e8c27302dd1001f92cbee4`) and persisted as
`files/figures/PMID42422765_r2/native_renders_20261021/fig3_PMC13343157_p06_embedded_1744x1699.png`
(sha256 `9152439cab8c2d56ee8312fd0b955d6aeb6411cdb10471786b4534ca6c753d3b`) — 1744 × 1699 px,
2.4 × the linear detail of the CDN file. Curve values were read against the printed axes
(x ticks 0 / 100 / 200 / 300 days; y ticks 0 / 50 / 100 %), not estimated by eye.

Figures 1, 6, 7 and S7 were re-opened on the same principle; Figure 7 and S7 as **400 dpi page
renders**, because Figure 7's plots are vector in the PDF and its embedded raster is only the
ECoG traces.

## 2 · Verdict — **NARROW**

Neither `KEEP` nor `REVERSE` survives the measurement, because *dose-dependent* is **true of some
endpoints of this study and false of others**, and the Title binds it to the three where it is
weakest.

| Endpoint | LD (1.23 × 10¹¹ vg as printed) | HD (2.63 × 10¹¹ vg as printed) | Graded? |
|---|---|---|---|
| Survival, Fig 3B | **0 % at ~day 78–81** | **76–77 % plateau to day 300** | 🔴 step |
| Body weight P30, Fig 3C | 15.3 g | 15.6 g | 🔴 equal |
| Body weight to P180, Fig 3D | tracks WT to ~day 60, arm then extinct | tracks WT to day 180 | level equal, duration differs |
| Glucose P10, Fig 3E | ns vs WT **and ns vs KO+RI** | ns vs WT and ns vs KO+RI | no |
| Glucose P20, Fig 3F | `*` vs WT | `ns` vs WT, `**` vs LD | 🟢 yes |
| Glucose P30, Fig 3G | ns | ns | no |
| Vector genomes + mRNA P30, Fig 5A–5H | — | — | 🔴 7 of 8 regional comparisons `ns` |
| WWOX protein P30, Fig 5I–5L | lower | higher | 🟢 yes |
| Myelination, Fig 6F / S7I | "partial" | "near-complete" | 🔴 never quantified |
| % Iba1, S7F | 16.2, `ns` vs WT | 10.8, `ns` vs WT | no, and no KO arm |
| % GFAP, S7H | 3.05, `**` vs WT | 1.9, `ns` vs WT | 🔴 binary, and no KO arm |
| Motor score, S4A | 1.8 | 0.3; LD–HD `***` | 🟢 yes |
| ECoG / SWD, Fig 7E | **no arm** | 0.13/h, `ns` vs WT | 🔴 not testable |
| Behaviour at 3 months, Fig 4 | **no arm** (did not survive to P90) | — | 🔴 not testable |

**The five components of the narrowing:**

1. **KEEP** the word where the data are graded and name those endpoints: WWOX protein expression,
   P20 glycaemia, composite motor score.
2. **NARROW** it for **survival**. *Durable* rescue is a high-dose-only property: the LD curve
   reaches **zero**. 🔴 **"LD does nothing" is refused**: the caption prints LD vs `KO+RI`
   p < 0.0001 and the measured curve shows death postponed from ~day 15 to ~day 78–81. A
   postponement that ends in an extinct arm is not a durable rescue, and the two beliefs
   recommend different trials, which is the flag's point and is upheld.
3. **NARROW** it for **body weight**, where the flag is silent: **LD = HD at P30** (15.3 vs
   15.6 g), with **no significance marker printed on panel 3C or 3D at all**.
4. **NARROW the Title's three named domains.** `ECoG/SWD` has **no low-dose arm**, so it cannot
   support a dose-dependent claim at all; **myelination** is unquantified in every treated arm
   (Fig 6E, the only MBP quantification, contains no treated arm; 6F and S7I are representative
   images, and 6F has no untreated-KO column either); **gliosis** is binary and its treated-arm
   panels (S7F/S7H) carry **no untreated-KO comparator**, with wild-type values that differ
   roughly two-fold from the wild-type values in the disease-baseline panels of the same figure.
5. 🔴 **NARROW the flag's own inference.** *"The panel places a threshold between 1.23 and
   2.63 × 10¹¹ vg"* claims more than two dose points can carry: with two arms a step and a steep
   continuum are indistinguishable. What the panel **refuses** is linear interpolation of durable
   benefit. The step reading is **strengthened, not established**, by four dose levels across two
   figures — Fig 2B's hSynI, WPRE-free arms at 4 × 10¹⁰ (*n* = 3) and 8 × 10¹⁰ (*n* = 5) with no
   survivors (manifest entry 14), then 1.23 × 10¹¹ extinct at ~80 days and 2.63 × 10¹¹ at 76–77 %
   to 300 days — but those are **different cohorts in different experiments**, and entry 14
   already carries an unresolved discrepancy between the running text and the panel for 8 × 10¹⁰,
   with the presumption left in favour of the text.

## 3 · Two numeric corrections to flag prose — not to a locator

| Flag prose | Measured on the 300 dpi panel against its printed axes |
|---|---|
| LD *"shifts death from ~20 to ~90 days"* | `KO+RI` reaches 0 % at **~day 15** (first death ~day 9); LD reaches 0 % at **~day 78–81** |
| HD *"plateaus at ~80 % to 300 days"* | HD plateaus at **76–77 %** from ~day 80 through day 300 |
| *(absent from the flag)* | 🔴 **`WT+RI` itself ends at 71–72 %** — 100 % to ~day 45, ≈ 89–90 % to ~day 122, then 71–72 % to day 300. The high-dose arm therefore sits **at or marginally above its own wild-type control**, which is what the caption's `p = 0.78` says and what *"comparable to WT"* conceals |

🔴 **Neither corrected value sits behind a persisted verbatim locator.** The manifest's forty
entries contain **no Figure 3B entry at all** — which is the real defect this candidate repairs,
and the reason the fourth mandatory audit trigger does not fire: there is no locator here to
contradict, only claim prose whose panel reading was never bound. §4 binds it.

## 4 · Proposed edits — verbatim

**4a · Title.** Replace

> *AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multipli
> inclusi ECoG/SWD, mielinizzazione e gliosi*

with

> *AAV9-hSynI-hWWOX in Wwox-null murine model: durable survival rescue at the high dose only,
> with dose-grading demonstrated on expression, P20 glycaemia and motor score and NOT on
> survival, body weight, ECoG/SWD, myelination or gliosis*

**4b · One block appended to the flag, replacing nothing above it.**

> ✅ **Flag ADJUDICATED 2026-10-21 (`CC-20261021-SCIENTIST-C-CLAIM011-DOSE-ADJUDICATION-01`,
> `FTR-20261021-42422765-01`) — verdict NARROW, with Figure 3B re-inspected as an image at native
> resolution (300 dpi raster embedded in the publisher PDF, sha256 `9152439c…53d3b`, 1744 × 1699,
> against the 726 px CDN file the flag was written from) and the curves read off the printed
> axes.** *«Dose-dependent» is true of this study's expression, P20 glycaemia and motor measures
> and false of its survival, weight, ECoG, myelination and gliosis measures,* and the Title bound
> it to the three where it is weakest. **Survival is a step, not a gradient:** LD reaches **0 % at
> ~day 78–81** and HD plateaus at **76–77 % through day 300**, against a `WT+RI` control that
> itself ends at **71–72 %** — so *«comparable to WT»* includes a wild-type arm that lost ~29 % of
> its animals. 🔴 **But LD is not nothing:** the caption prints LD vs `KO+RI` p < 0.0001 and death
> is postponed from ~day 15 to ~day 78–81; a postponement ending in an extinct arm is not a
> durable rescue, and that distinction, not «more dose more benefit», is what recommends different
> trials. 🔴 **And LD is not uniformly worse: on body weight LD = HD** (15.3 vs 15.6 g at P30,
> Fig 3C, with **no significance marker printed on panel C or D at all**). 🔴 **The three domains
> the old Title named cannot carry the word:** Figure 7E has **no low-dose arm** (HD only, *n* = 5
> per group, SWD/hour KO ≈ 0.635 → HD ≈ 0.13, `****`, `ns` against WT ≈ 0.03, 7 days of recording
> from ~P14); myelination is **never quantified in any treated arm** (Fig 6E, the only MBP
> quantification, is WT vs KO; 6F and S7I are representative images and 6F lacks an untreated-KO
> column); gliosis is **binary with no disease comparator** (S7H % GFAP: WT ≈ 1.75, LD ≈ 3.05
> `**`, HD ≈ 1.9 `ns`; S7F % Iba1 all `ns`; **neither panel contains a `KO+RI` arm**, and the
> wild-type value moves ≈ 2× between S7D and S7H). ⚠️ **The flag's own inference is narrowed too:**
> two dose points cannot *locate* a threshold — a step and a steep continuum are indistinguishable
> — so what the panel refuses is **linear interpolation of durable benefit**, not the existence of
> intermediate behaviour. The step reading is **strengthened, not established**, by four dose
> levels across two figures (Fig 2B's 4 × 10¹⁰ and 8 × 10¹⁰ hSynI/WPRE-free arms, no survivors;
> then 1.23 × 10¹¹ and 2.63 × 10¹¹) — **different cohorts in different experiments**, with the
> text-versus-panel discrepancy at 8 × 10¹⁰ still unresolved in favour of the text. 🟢 **Nothing in
> this adjudication depends on the unit ambiguity**, and the `PREMISE_TAG` on the dose ceiling,
> the configuration boundary and the `REVIVAL_TRIGGER` are unchanged and re-affirmed: an
> **intermediate-dose arm, defined as a fraction of the primary's HD**, remains the single most
> informative experiment this paper implies, and it should carry survival, weight, glycaemia,
> ECoG **and quantified MBP in the same animals** to 300 days.

**4c · Nothing else.** `Status` stays `flagged for review` until the Orchestrator decides
whether the adjudication retires it; this candidate does not propose retiring it, because the
rewrite of the `Summary` that the new Title implies is a separate act and `CC-20260826-AAV9-
ENDPOINT-SPLIT-01` already tracks it.

## 5 · What this candidate does NOT do

- It does **not** adjudicate the Figure 4 text-versus-panel conflict (4D/4E asterisks against
  *"no significant differences"*, plus the declared *«3 of 8 panels differ from WT in the
  direction of excess»* attestation that the blind audit returned `UNVERIFIABLE_SURFACE`). The
  bytes are now reachable — `gr4.jpg` on disk, and the panel at 300 dpi on page 7 of the
  publisher PDF — but it is a different question about a different part of the claim, and
  settling it inside a dose adjudication would bury it. **Reported as the next measurement.**
- It does **not** promote any direction into the `Summary`, touch `CLAIM 031`, `CLAIM 040` or any
  `consolidated baseline` record, or alter the genotype caution. The model remains a *Wwox*-null
  full knockout on FVB carrying the Aqeilan 2007 targeted-deletion allele; **the expected level
  of rescue in the reference genotype does not follow from this study** in either direction.
- It does **not** treat `NOT_MEASURED` as `SMALLER`. The tested timing arms are **P1, P2, P3, P5**
  (S8A/B), the Methods heading and the Discussion write *P0–P5*, the main cohorts were injected
  at P0–P1, and the authors state *«Therapeutic rescue beyond this early postnatal window was not
  explored»*. Nothing in this corpus bounds efficacy after P5 in either direction.
- It does **not** soften the oligodendrocyte limit or invent one. The MBP-promoter construct
  produced **no benefit on any measured endpoint** (Fig 1G/1H/1I) **and essentially no detectable
  WWOX protein** (Fig 1M), at a different dose and a different cassette (WPRE-bearing, 4 × 10¹⁰
  vg) — so the oligodendrocyte question is **unanswered by that experiment, not answered
  negatively**. `REVIVAL_TRIGGER`: an oligodendrocyte-directed construct with demonstrated WWOX
  protein in white matter, then tested.
- It asserts **no reusable RNA-seq rescue signature**: there is no rescue-versus-knockout
  transcriptomic contrast in this study, and GSE156243 is a knockout-versus-wild-type organoid
  contrast that must not be merged with it.
