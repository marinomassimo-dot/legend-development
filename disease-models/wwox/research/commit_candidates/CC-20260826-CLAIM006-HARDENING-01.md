# COMMIT CANDIDATE — `CLAIM 006` / `PAPER 007` final hardening: the over-claim is one figure caption, and it propagated to the wrong brain region

**Candidate ID:** CC-20260826-CLAIM006-HARDENING-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** independent re-derivation of [`CC-20260826-CLAIM006-01`](CC-20260826-CLAIM006-01.md) at
figure-pixel level, plus three propagation surfaces it does not carry.
**Does not supersede it** — it confirms its panel read and corrects two things in its proposed
replacement.
**Change class:** 🔴 **MAJOR** (inherits) · **Locator audit trigger:** ✅ **REQUIRED**
**Canonical targets:** `CLAIM 006` · `working_model_current.md:154` · `analysis/therapy_levers.md`
§B2 · **plus** `discovery_ledger_current.md` `DL-MECH-012` ·
`literature_tracking_log_current.md:2298` · `research_lines_current.md` `RL-NEUROINF-001`
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

---

## 0. Independent re-read — the panel evidence, verified from pixels, not from the prior candidate

Every value below was read at native resolution from the NIHMS figure rasters, without consulting
`CC-20260826-CLAIM006-01`'s table while reading. **Its panel read is confirmed in full.**

| Artefact | sha256 | px |
|---|---|---|
| `PMID36828035_Hussain2023_assets/nihms-1957654-f0003.jpg` | `d2bc329fd35845a4c04bb73b7c8204de3229d6ab98f06181eb7dd087a8cd6f67` | 1531 × 2100 |
| `…/nihms-1957654-f0004.jpg` | `f9787d65761c0819213ac1e94e0b36a42a230c29ea1d6fd6f7eee7868310eaa5` | 1430 × 2100 |
| `…/nihms-1957654-f0005.jpg` | `4ade833d8d552aac551f87431e4aaa6c2cc435633826b38c42e09585be770050` | 1542 × 2100 |

⚠️ These live under `files/`, which is **gitignored and per-working-directory**. Resolve against
the checkout that holds `files/fulltext`; the sha256 is the durable identifier.

### The design settles it: the paper draws a within-genotype 80 d → 250 d bracket wherever it tested an age effect

| Axis | Panel | Region | 80 d (WT · mut) | 250 d (WT · mut) | vs-WT | **age bracket** | Verdict |
|---|---|---|---|---|---|---|---|
| Microglial **number** | 3b | HPC CA1+CA3+DG | ≈22 · ≈34 | ≈22.5 · ≈33.5 | `*` both | ❌ **none** | 🔴 **NOT PROGRESSIVE** |
| Microglial **area %** | 3c | HPC | ≈14.5 · ≈21 | ≈11 · ≈20.5 | `*` both | ❌ **none** | 🔴 **NOT PROGRESSIVE** — mutant flat; the gap widens because **WT falls** |
| Microglial **branches** | 3e | HPC | ≈98 · ≈60 | ≈93 · ≈40 | `*` both | ✅ **`*` mut→mut** | ✅ **PROGRESSIVE** |
| Microglial **junctions** | 3f | HPC | ≈51 · ≈30 | ≈47 · ≈20 | `*` both | ✅ **`*` mut→mut** | ✅ **PROGRESSIVE** |
| Microglial **branch length** | 3g | HPC | ≈485 · ≈315 µm | ≈430 · ≈215 µm | `*` both | ✅ **`*` mut→mut** | ✅ **PROGRESSIVE** |
| Astrocyte **number** | 4b | HPC | ≈26 · ≈39 | ≈27.5 · ≈56 | `*` both | ✅ **`*` mut→mut** | ✅ **PROGRESSIVE** |
| Astrocyte **area %** | 4c | HPC | ≈11 · ≈24 | ≈13 · ≈39.5 | `*` both | ✅ **`*` mut→mut** | ✅ **PROGRESSIVE** |
| **Oligodendrocyte** loss (Olig2⁺) | 4e | 🔴 **corpus callosum** | ≈205 · ≈122 | ≈235 · ≈117 | `*` both | ❌ **none** | **established by 80 d, FLAT** |
| **Purkinje** loss (calbindin⁺) | 5d | cerebellum, vermis | ≈82 · ≈25 *(median)* | ≈100 · ≈42 *(median)* | `*` both | ❌ **none** | **established by 80 d, FLAT** |
| **Basket cells** (Hcn1⁺) | 5e | cerebellum, vermis | ≈80 · ≈78 | ≈95 · ≈112 | 🔴 **`ns` both** | ❌ none | 🔴 **SPARED at both ages** |

**Score: of nine pathology axes, five progress — three of them the same microglial cell's
morphology, two the astrocyte. Four do not, and one lineage is spared entirely.**

---

## 1. The four questions, answered exactly

### WHAT THE AUTHORS CLAIM — and the claim is narrower inside the paper than on its cover

| Surface | Verbatim | Progression asserted for |
|---|---|---|
| **Title** | *"…induces epilepsy, **progressive neuroinflammation**, and cerebellar degeneration…"* | undifferentiated "neuroinflammation" |
| **Abstract** | *"…signs of **progressive neuroinflammation** with elevated **astro-microgliosis that increased with age**."* | 🔴 **both lineages, explicitly by abundance** |
| **Fig. 3 caption title** | *"Wwox^P47T/P47T hippocampi exhibit **progressive microgliosis**."* | microglia |
| **Fig. 4 caption title** | *"Wwox^P47T/P47T hippocampi exhibit **progressive astrogliosis** and **reduced** oligodendrocyte numbers."* | astrocytes **only** — *"reduced"*, not *"progressively reduced"* |
| **Fig. 5 caption title** | *"Wwox partial LoF leads to cerebellar atrophy and Purkinje cell degeneration."* | 🔴 **none** |
| **Fig. 9 caption title** | *"…further evidence of severe dysfunction in Wwox P47T **cerebella**."* | none |

🔴 **The authors are more careful than their abstract at every point where they had to name a
lineage.** Fig 4's caption withholds "progressive" from the oligodendrocyte clause in the same
sentence where it grants it to astrocytes. Fig 5 withholds it entirely. **The over-claim is
localised to exactly two surfaces — the title and the abstract — plus one figure caption title
(Fig 3) whose panels split.**

### WHAT THEIR FIGURES SUPPORT

- ✅ **Astrogliosis progresses**, on both number and area, with within-genotype brackets. Fully
  supported.
- ◐ **Microgliosis progresses in morphology only.** Fig 3's caption title is defensible **if
  "microgliosis" is read as activation state**; it is false if read as abundance — and the
  abstract reads it as abundance (*"astro-microgliosis that increased with age"*).
- ❌ **Oligodendrocyte loss, Purkinje loss: established by 80 d, flat.** No age effect tested,
  none drawn.
- ❌ **Basket cells: `ns` at both ages.** A cerebellar interneuron population is spared beside a
  Purkinje population reduced to a quarter — this is the paper's own specificity control and it is
  currently invisible to LEGEND.

### WHAT LEGEND CURRENTLY CLAIMS

- `CLAIM 006` **Title** *(literal, line 119)*: `P47T model shows progressive neuroinflammation`
- `CLAIM 006` **Summary** *(literal, line 126)*: `P47T murine model shows progressive microgliosis and astrogliosis.`
- Status `consolidated baseline`, `Type: DATO + INFERENZA prudente`.

⇒ LEGEND transcribed the **abstract's** reading — *both lineages, by abundance* — which is the one
reading the figures contradict. It did not invent anything.

### WHAT MINIMUM REPAIR IS JUSTIFIED

The prior candidate's repair, **with two corrections**:

**Title** — BEFORE: `P47T model shows progressive neuroinflammation`
AFTER: `P47T model shows progressive astrogliosis; microgliosis is early and progresses only in morphology`

**Summary** — BEFORE: `P47T murine model shows progressive microgliosis and astrogliosis.`
AFTER *(literal)*:
> In the `Wwox^P47T/P47T` **hippocampus**, **astrogliosis progresses** between 80 and 250 days —
> Gfap⁺ number ≈39 → ≈56 and Gfap⁺ area fraction ≈24 % → ≈40 %, each carrying a within-genotype
> significance bracket. **Microgliosis is established by 80 days and does not progress in
> abundance**: Iba1⁺ number ≈34 at both ages, area fraction ≈21 % → ≈20.5 %, neither carrying a
> within-genotype bracket, and the widening area gap is driven by a **decline in the wild type**
> (≈14.5 % → ≈11 %). What does progress is **microglial morphology** — branches, junctions and
> total branch length all fall with within-genotype significance. **Separately, in the corpus
> callosum**, Olig2⁺ oligodendrocyte number is reduced by 80 days and flat thereafter; **and in the
> cerebellum**, calbindin⁺ Purkinje loss is likewise established by 80 days and flat, while Hcn1⁺
> basket cells are `ns` at both ages. All counts are `n = 3` mice per group.

#### 🔴 Correction 1 — the prior candidate places a corpus-callosum measurement inside a hippocampus-scoped sentence

`CC-20260826-CLAIM006-01` §2 proposes a Summary opening *"In the `Wwox^P47T/P47T` hippocampus…"*
and closing *"Olig2⁺ oligodendrocyte loss is established by 80 days and flat."* **Fig 4's caption
places that count in the corpus callosum**, not the hippocampus:

> *"(e) Bar graph showing quantitative measurement of Olig2 positive oligodendrocytes counted in
> three independent 500 μm² regions spanning the entire imaged **corpus callosum**."*

Adopting the repair as drafted would fix a time-course error and introduce a **region** error into
a `consolidated baseline` Summary. Corrected above.

#### 🔴 Correction 2 — Figs 3–4 report means; Fig 5 reports medians. The prior candidate's `≈` values mix them

Figs 3 and 4 are bar graphs, *"data is represented as mean ± SEM"*. Fig 5d/5e are **box-and-whisker
plots**, *"horizontal line at median"*. The prior candidate lists Purkinje as *"WT ≈95"* at 80 d;
the **median** is ≈82 (box ≈68–122, whiskers ≈48–158). The Purkinje "improvement" ≈25 → ≈42 that
§1.1 of that candidate flags as possible survivor selection is a **median** shift — and the 80-day
mutant box's lower whisker reaches **0**. Any statement about that shift must name the statistic.

---

## 2. 🔴 Three method boundaries that no surface currently records

None of these is in `CLAIM 006`, in `PAPER 007`, or in either candidate.

| Boundary | Verbatim from the captions | Why it binds |
|---|---|---|
| **Pseudoreplication** | Fig 3b/c and 4b/c: *"Each data point represents quantitation from a **single subfield** of **n = 3 mice/group**"*; Fig 4e: *"a single independent region from n = 3 mice/group"*; Fig 5d/e: *"1000 μm² sections … pairs (**n = 3**)"* | Every `*` in this figure set is an **unpaired Student's t-test over subfields/sections**, not over animals. Nine points per bar come from three mice. The inferential unit is the animal; the test uses the subfield |
| **The asterisk means three different things** | Fig 3: *"`*p-value < 0.005`"* · Fig 4: *"`*p-value < 0.01`"* · Fig 5: *"`*p-value < 0.05`"* | A reader comparing `*` across Fig 3 and Fig 5 is comparing a 0.005 threshold with a 0.05 one. **Any cross-figure strength comparison is invalid without the per-figure threshold** |
| **The cerebellar inflammation measurement has no declared age** | Fig 9d/e: *"mean IL1β (d) and TNFα (e) mRNA … in Wwox^WT/WT and Wwox^P47T/P47T **CB** (n = 6 mice/group)"* — **no age group stated** | This is the **only** cerebellar inflammation measurement in the paper. It is a single unstated timepoint and therefore **cannot support any progression claim in the cerebellum** |

⚠️ **These do not withdraw any measured elevation.** Both glial lineages are significantly elevated
versus WT at both ages under the paper's own thresholds. They bound how much weight a `consolidated
baseline` may place on the effect sizes.

---

## 3. Propagation into action-oriented surfaces — the complement, measured

The prior candidate searched for the **phrase**. This sweep searched for the **concept**, over
every surface that licenses an action, enumerated in advance rather than discovered by grep:

```bash
for f in disease-models/wwox/analysis/therapy_levers.md \
         disease-models/wwox/therapeutics/therapeutic_strategies_current.md \
         disease-models/wwox/biomarker_endpoint/biomarker_candidates_current.md \
         disease-models/wwox/biomarker_endpoint/clinical_monitoring_endpoints_current.md \
         disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md \
         disease-models/wwox/research/research_candidates_current.md \
         disease-models/wwox/research/research_lines_current.md \
         disease-models/wwox/research/discovery_ledger_current.md \
         disease-models/wwox/meta/meta_network_myelin_glia_current.md \
         disease-models/wwox/registries/working_model_current.md \
         disease-models/wwox/disease_model.md disease-models/wwox/mission.md ; do
  /usr/bin/grep -nEi "microglio|iba1|astroglio|gfap|neuroinflamm|neuroinfiamm|astro-microglio" "$f"
done
```

**Denominator: 12 action-oriented surfaces enumerated, 12 searched.** Six carry glial wording;
**three carry the over-claim and are not in the prior candidate's table.**

| Surface | Wording | Prior candidate | Action |
|---|---|---|---|
| `therapy_levers.md:22` §B2 | *"Partial-LoF WWOX models show **progressive astro-microgliosis worsening with age** (PMID 36828035, P47T)"* | ✅ listed | 🔴 **repair** — see §4 |
| 🔴 `discovery_ledger_current.md:208` `DL-MECH-012` | *"cervelletto: **astro-microgliosi progressiva** + perdita Purkinje (Wwox^P47T)"* | ❌ **absent** | 🔴 **repair — two defects**, §4 |
| 🔴 `discovery_ledger_current.md:2298` | model/phenotype comparison table row: *"epilessia ad esordio adulto, neurodegenerazione cerebellare, atassia, **neuroinfiammazione progressiva** \| Hussain et al. 2023"* | ❌ **absent** | ⚠️ **repair** — this is a phenotype description, not a title quote |
| ⚠️ `research_lines_current.md:91` `RL-NEUROINF-001` | line title *"Neuroinflammation / glia **progression**"* | ❌ absent | ⚠️ **annotate** — the axis name encodes the undifferentiated claim |
| `working_model_current.md:154` | mirror: *"006 \| P47T model → progressive neuroinflammation"* | ✅ listed | ✅ repair with the Title |
| `discovery_ledger_current.md:125` `DL-REPO-002` | proposed experiment: *"il farmaco-X riduce **astro-microgliosi (GFAP/Iba1)**"* | ✅ listed as annotate | ⚠️ **annotate**, and see §4 |
| `meta_network_myelin_glia_current.md:43` | *"Gliosis (astro-microgliosis) reduced after neuron-specific rescue"* — **Obeid 2026, `Wwox`-null** | ✅ correctly excluded | ❌ **no change** — different paper, different model, no time-course claim |
| `therapeutic_hypotheses_ledger_current.md:39/44/59` | `HYP-…-02` cites `DL-MECH-012` for direction | ✅ listed as no-change | ⚠️ **inherits** whatever `DL-MECH-012` is corrected to |
| `therapeutic_strategies_current.md` · `biomarker_candidates_current.md` · `clinical_monitoring_endpoints_current.md` · `research_candidates_current.md` · `mission.md` · `disease_model.md:51` | no P47T time-course claim; `disease_model.md:51` describes neuroinflammation as a *downstream modifier*, no progression | — | ❌ **no change** |

---

## 4. The three new repairs, with review fields

### Δ-A · `discovery_ledger_current.md:208` — `DL-MECH-012` · 🔴 **two defects, one of them anatomical**

- **CURRENT_TEXT** *(literal fragment)*:
  > **L'indizio**: in tutti i tessuti la **perdita di WWOX aumenta l'infiammazione** — cervelletto: astro-microgliosi progressiva + perdita Purkinje (Wwox^P47T); sepsi: peggiore gliosi/apoptosi cerebrale dopo LPS; …
- **PROPOSED_REPLACEMENT** *(literal fragment)*:
  > **L'indizio**: in tutti i tessuti la **perdita di WWOX aumenta l'infiammazione** — `Wwox^P47T`: **ippocampo** — astrogliosi progressiva (numero e area, 80→250 d) e microgliosi già stabilita a 80 d che progredisce **solo in morfologia**; **cervelletto** — perdita di Purkinje stabilita a 80 d e piatta, con IL1β/TNFα mRNA elevati a un singolo timepoint non dichiarato; sepsi: peggiore gliosi/apoptosi cerebrale dopo LPS; …
- **EVIDENCE_CLASS:** `DATO` on the elevations; the words *"progressiva"* and *"cervelletto"* were
  `INFERENZA` carried as `DATO`
- **LOCATOR:** Fig 3b/3c/3e–g, Fig 4b/4c/4e, Fig 5d/5e, Fig 9d/9e captions and panels
- **DO_NOT_INFER:** that cerebellar inflammation was shown to progress — **it was measured once, at
  an age the caption does not state**; that hippocampal astrogliosis transfers to the cerebellum;
  that the multi-tissue direction claim (WWOX loss → inflammation ↑) is weakened. **It is not** —
  direction is unaffected by either correction.
- **WHY_MINIMUM:** one region word and one time-course word. The three-tissue convergence, the
  scaffold mechanism and the `maturing` status are untouched.
- **AFFECTED_DOWNSTREAM:** 🔴 `DL-REPO-002` — whose entire ABC map reads
  *"B = de-repressione dell'infiammazione (microgliosi/astrogliosi) documentata da Aldaz"* and whose
  proposed experiment is *"nei topi Wwox^P47T … misurare se il farmaco-X riduce astro-microgliosi
  (GFAP/Iba1), rallenta la perdita di Purkinje"*. Also `HYP-20260705-02`, `HYP-…-03`,
  `DL-MECH-014`, `DL-MECH-015`, and the pending neuroinflammation meta whose priority this entry
  raises.
- **BASELINE_EFFECT:** **NARROWED** on time course; 🔴 **REVERSED** on region

### Δ-B · `therapy_levers.md:22` §B2 · 🔴 the only surface where the over-claim licenses an action

- **CURRENT_TEXT** *(literal)*:
  > - **B2. Neuroinflammation control.** Partial-LoF WWOX models show progressive astro-microgliosis worsening with age (PMID **36828035**, P47T). Relevant to hypomorphic alleles. No WWOX-specific drug identified yet.
- **PROPOSED_REPLACEMENT** *(literal)*:
  > - **B2. Neuroinflammation control.** In the partial-LoF `P47T` mouse, **hippocampal astrogliosis worsens with age** (Gfap⁺ number and area, 80 → 250 d, within-genotype significance); **microgliosis does not worsen in abundance** — Iba1⁺ number and area are flat between the same ages — though microglial **morphology** does (branches, junctions, branch length). ⚠️ **An anti-microglial agent aimed at abundance therefore has no age-dependent signal to act on in this model**, and a trial powered on Iba1⁺ counts would be powered on a flat endpoint. Astrocytic endpoints carry the age signal. All from PMID **36828035**, `n = 3` mice per group, subfield-level statistics. No WWOX-specific drug identified yet.
- **EVIDENCE_CLASS:** `DATO` (panel-level) replacing `INFERENZA`
- **LOCATOR:** as Δ-A
- **DO_NOT_INFER:** that microglia are unaffected — they are significantly elevated versus WT at
  both ages; that morphological progression is a validated drug endpoint; that any of this
  transfers to the reference genotype — `CLAIM 006`'s `T3 with genotype caution` is unchanged and
  P47T's WW1 mechanism differs from an SDR allele.
- **WHY_MINIMUM:** the lever is kept. Only the endpoint it points a drug at is corrected.
- **AFFECTED_DOWNSTREAM:** `DL-REPO-002`, `TX` portfolio §B, `RL-NEUROINF-001`
- **BASELINE_EFFECT:** **NARROWED**

### Δ-C · `discovery_ledger_current.md:2298` · MINOR

- **CURRENT_TEXT** *(literal cell)*: `epilessia ad esordio adulto, neurodegenerazione cerebellare, atassia, neuroinfiammazione progressiva`
- **PROPOSED_REPLACEMENT** *(literal cell)*: `epilessia ad esordio adulto, neurodegenerazione cerebellare, atassia, astrogliosi ippocampale progressiva (microgliosi non progressiva in abbondanza)`
- **EVIDENCE_CLASS / LOCATOR / DO_NOT_INFER:** as Δ-B
- **WHY_MINIMUM:** four words in one table cell of a model-comparison table.
- ⚠️ **Not to be confused with a title quote.** `literature_tracking_log_current.md:2502` reads
  *"**Note:** Title: WWOX P47T partial loss-of-function mutation induces epilepsy, progressive
  neuroinflammation, and cerebellar degeneration in mice"* — that line **stays unchanged**, because
  quoting a title accurately is not an over-claim. 🔴 **A first draft of this candidate attributed
  line 2298 to the tracking log rather than to the discovery ledger**, which would have sent the
  repair at the one line that must not be touched. The attribution is recorded corrected rather
  than silently fixed.
- **BASELINE_EFFECT:** **NARROWED**

---

## 5. Special-invariant audit

| Check | Verdict |
|---|---|
| Does any repair turn `NOT_REPORTED` into `ABSENT`? | ✅ **no** |
| Does any repair turn `NO_DETECTION` into `NO_PHENOTYPE`? | ✅ **no.** Basket cells are `ns` — recorded as **`ns` on a tested comparison**, which is a *result*, not a non-detection. The distinction is stated in the AFTER Summary |
| Is a flat measurement reported as absence? | ✅ **no.** Iba1⁺ abundance is **elevated and flat**, and the AFTER text says both |
| Is any elevation withdrawn? | ✅ **no.** Both lineages remain significantly elevated versus WT at both ages |
| Is the paper accused of error? | ✅ **no.** Fig 4's own caption withholds "progressive" from oligodendrocytes; Fig 5's withholds it entirely. The over-claim is the abstract's, and it is quotable as the abstract's |

---

## 6. What this candidate refuses to do

- **Does not supersede** `CC-20260826-CLAIM006-01`; it confirms its panel read and corrects two
  points in its proposed replacement.
- **Does not downgrade `CLAIM 006`'s status.** The content is measured and not in dispute.
- **Does not resolve the Purkinje ≈25 → ≈42 median shift.** Survivor selection and cohort variance
  remain undecided by these panels, and it must not be reported as recovery.
- **Does not extend the correction to `meta_network_myelin_glia_current.md:43`** — that line is
  about Obeid 2026 in the `Wwox`-null and makes no time-course claim.
- **Does not claim `DL-MECH-012`'s multi-tissue direction is wrong.** Only its region and its time
  course.

---

## 7. Review required

🔴 **Operator authorization** — MAJOR, and Δ-B moves a therapeutic-lever rationale.
🔴 **Locator audit REQUIRED.** The finding rests on the presence and absence of within-genotype
brackets in ten panels. It has now been read twice, independently, with agreement — that is
corroboration, not verification: **both reads used the same rasters and the same reader class.**


---

## BATCH DISPOSITION — `BATCH_20260926_ALDAZ` (2026-09-26, ACTOR_ID `plan`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260926_ALDAZ`.

Propagated, with the audited wording in place of the drafted one: `CLAIM 006` title, summary and the method boundaries of §2 (pseudoreplication at n = 3 mice, two time points, no multiplicity correction, no declared blinding); the working-model mirror; Δ-B (`therapy_levers.md` lever B2 [ref corrected 2026-09-28 from "§B2" · CC-20260928-SECTION-REFS-01]); Δ-B was propagated **minus** its "no age-dependent signal to act on" / "flat endpoint" clauses, which inherit the refused null — §B2 states only that the abundance comparison was not tested; Δ-A and Δ-C as **append-only notes** on `DL-MECH-012`, `DL-BIO-085` and its downstream `DL-REPO-002` (the ledger is append-only, so the entries are annotated, not rewritten); `RL-NEUROINF-001`. **Still owed:** the corpus-callosum Olig2⁺ and cerebellar Purkinje/basket-cell content its proposed summary adds. It was not in the audited text, and it belongs with the new cerebellar claim `CC-20260913-36828035-01` §4 asks for, not inside a hippocampal glia claim. The candidate stays queued for that.

---

## WAVE-2 READINESS (2026-09-27)

**context_policy declared:** `QUESTION_DRIVEN`. One question, put back to a source already read to
completion: where exactly does the paper place the Olig2⁺ count, on what sampling unit, and what
does it report for myelin in that same region. Records reached by `registry_records.py get --id`;
source read at `files/fulltext/PMID36828035_Hussain2023_PMC.xml` and the Figure 4 raster.

**Actor:** `scientist`, wave-2 package `provenance`.

### 1 · What was still owed, and what of it is already spent

`BATCH_20260926_ALDAZ` propagated the audited `CLAIM 006` wording, the §2 method boundaries, the
working-model mirror, Δ-B (minus its refused null clauses), Δ-A and Δ-C as append-only ledger notes,
and `RL-NEUROINF-001`. Its disposition leaves two things owed: the **corpus-callosum Olig2⁺**
content and the **cerebellar Purkinje/basket** content.

🔵 **The cerebellar half is spent.** `CLAIM 041` (landed `BATCH_20260926_ALDAZ_R7`, receipt
`FTR-20260913-36828035-03`) carries the Purkinje/basket contrast — fewer calbindin⁺ profiles at
both ages, basket counts with no significant genotype difference — and carries it **better than this
candidate drafted it**: its evidence boundary states that the panels do not compare 80 with 250 days
within the mutant, so *"progression or nonprogression is untested"*, where this candidate's Summary
said *"established by 80 days and flat"*. Verified in the live record. **That half is SUPERSEDED by
`CLAIM 041`.**

🔴 **The corpus-callosum half is real and still unwritten.** `Olig2` appears in no claim but
`CLAIM 003`. The candidate's own Correction 1 is why it cannot simply be appended to `CLAIM 006`:
the measurement is in the **corpus callosum**, and `CLAIM 006` is scoped to the hippocampus.

### 2 · What I did

**Verified the region and the sampling unit at source** rather than carrying the candidate's
quotation, and added the caption as a persisted locator (`deepdive_manifests/PMID36828035.json`
entry 58): *"Bar graph showing quantitative measurement of Olig2 positive oligodendrocytes counted
in three independent 500 μm2 regions spanning the entire imaged corpus callosum."* — with the
caption's own unit and test, `n = 3` mice per group, unpaired Student's t-test at `p < 0.01`. The
panel attestation already persisted as entry 23 (WT ~205 vs mutant ~122 at 80 days; ~235 vs ~117 at
250 days; **no within-genotype bracket**, and the relative gap widens because **wild type rises**).

**Read the paper's own myelin result in the same region**, because without it an oligodendrocyte
deficit reads as a myelin deficit: *"no significant differences in Mbp staining were detected when
comparing"* wild type and homozygote in the parietal cortex above the corpus callosum
(Results 2.6, Supplementary Figs. 6a–d; manifest entry 36, itself narrowed by a 2026-09-26 blind
audit from an earlier over-reading).

**Read Figure 4 at the pixels** to confirm the panel and its brackets before proposing any wording.

### Verdict — **READY_MINOR**

The proposal below is a **registry boundary on `PAPER 007`**, not a new claim and not an edit to
`CLAIM 006`. It records a measured deficit with the three things that bound it — region, sampling
unit, and the untested age comparison — plus the paper's own Mbp null. **No claim is created**: a
white-matter/oligodendrocyte claim would need a decision this section does not take, and the
candidate itself says the content *"belongs with the new cerebellar claim … not inside a hippocampal
glia claim"*. Writing it on the paper record puts the datum where a reader of that paper meets it,
and leaves the claim decision open rather than pre-empted.

### Operation list for `batch_commit.py propagate`

**File:** `disease-models/wwox/registries/paper_registry_current.md` — **full rewrite** (the paper
registry is propagated by full rewrite). One line changes inside `PAPER 007`.

**OP 1 · record `PAPER 007` · replace one line**

*old (verbatim, from the current file):*

```
**Secondary pathway:** P3 — interaction logic
```

*new:*

```
**White-matter boundary — the Olig2⁺ deficit is a CORPUS-CALLOSUM measurement and it is not a myelin result (`CC-20260826-CLAIM006-HARDENING-01` residue, 2026-09-27).** Figure 4e counts Olig2⁺ oligodendrocytes *"in three independent 500 μm2 regions spanning the entire imaged corpus callosum"*, `n = 3` mice per group, unpaired t-test at `p < 0.01`: mutant ≈122 vs wild type ≈205 at 80 days and ≈117 vs ≈235 at 250 days, each with an asterisk. 🔴 **No within-genotype 80-vs-250-day bracket is drawn, so progression is UNTESTED**, and the widening relative gap is driven by the **wild type rising**, not by the mutant falling — 80 days is the earliest age sampled, not a demonstrated onset. ⚠️ **The same paper reports no myelin difference in the region above it**: *"no significant differences in Mbp staining were detected when comparing"* the two genotypes in parietal cortex above the corpus callosum (Results 2.6, Supplementary Figs. 6a–d), which does not establish equivalent myelination elsewhere or by other measures but does forbid reading the cell-count deficit as a demonstrated hypomyelination. **Scope:** this is white matter, **not** the hippocampal compartment of [[claim_registry_current#CLAIM 006]], and it is not carried by any claim today; `Olig2` appears in no claim but [[claim_registry_current#CLAIM 003]], whose residual oligodendroglial limb is a different model and a different question. Locators: `deepdive_manifests/PMID36828035.json` entries 23 (panel), 36 (Mbp), 58 (caption, added 2026-09-27).
**Secondary pathway:** P3 — interaction logic
```

**Change class:** MINOR (one registry boundary line; no claim, no status, no working-model change).
**Review floor:** the candidate's own `MAJOR` / R4 applies to the `CLAIM 006` narrowing, which
**already landed audited**; this residue narrows nothing and creates nothing, so it carries no new
audit trigger. **Applied outside batch:** `deepdive_manifests/PMID36828035.json` (entry 58).

**On propagation:** the corpus-callosum half is discharged and the cerebellar half is
**SUPERSEDED by `CLAIM 041`** — at that point this candidate may be closed.

**Pending, and named so it is not lost:** whether the white-matter datum should become a claim of
its own is **undecided**, deliberately. It needs a record decision (new claim vs `PAPER 007`
boundary as above), and one measurement would settle what it means — the myelin endpoints
`CC-20260826-CLAIM003-01` §4 specifies, applied to white matter in this model.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

`OP 1` applied to `PAPER 007` in the paper-registry full rewrite: the corpus-callosum Olig2⁺ boundary, with the region, the three 500 μm² sampling regions, `n = 3` per group, the **untested** 80-vs-250-day comparison, the widening gap driven by the wild type rising, and the paper's own *"no significant differences in Mbp staining"* result above it. Both quotations were re-verified verbatim against `files/fulltext/PMID36828035_Hussain2023_PMC.xml` in the root checkout before the op was applied. No claim is created and `CLAIM 006` is untouched; the cerebellar half stays **SUPERSEDED by `CLAIM 041`**. Whether the white-matter datum becomes a claim of its own is still open and is not pre-empted.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.
