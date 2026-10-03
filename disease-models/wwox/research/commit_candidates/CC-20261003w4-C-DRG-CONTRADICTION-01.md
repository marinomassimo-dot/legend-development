# CC-20261003w4-C-DRG-CONTRADICTION-01 — is AAV dorsal-root-ganglion toxicity immune-preventable or dose-intrinsic? Characterised, not decided

- `context_policy: SOURCE_FIRST`
- Sources: PMID 41404412 (`FTR-20261003-41404412-01`), PMID 35331006 (`FTR-20261003-35331006-01`),
  PMID 36700120 (`FTR-20261003-36700120-01`). All three manifests validate
  (`--verify-artifacts --require-current-schema`, `VERDICT: PASS`). **None of the three mentions
  WWOX.**
- Change class: **MINOR**. Nothing is narrowed or reversed: it adds one research-line record holding
  an open question and one dismissal-ledger negative stating that the question is not yet decidable
  from these sources. Both are research layer.
- **Nothing here is medical advice.**

## The finding, in one sentence

Two regulatory-grade primate datasets disagree about whether AAV-mediated DRG toxicity can be
prevented by immunosuppression — one reduced it across three different cargos, the other could not
reduce it even under complete B-cell depletion — and the disagreement **cannot be resolved from
either source**, because the regimens differ in drug class, the negative rests on two to three
animals per cell, and the procedures differ in contrast agent and in ganglion sampling density.

## Why this must be carried as an open question rather than settled

The two outcomes imply **opposite risk-mitigation plans** for any neuron-targeted AAV, which is why
leaving it open is the informative act:

- If the immune mechanism holds, the dominant class toxicity of a CNS AAV has a clinically feasible
  prophylaxis, and the plan is a defined peri-dosing immunosuppression protocol with a duration
  (the source predicts at least six months) and its own paediatric risk assessment.
- If the transduction/expression mechanism holds, immunosuppression buys nothing, and the only
  levers are dose, promoter strength and tissue de-targeting.

A third possibility is that both are true of different components — the earliest events of the one
source are explicitly **uncorrelated with transgene level**, while its later events correlate with
it, which the authors themselves read as two distinct mechanisms.

## The axis-by-axis characterisation

| Axis | PMID 41404412 (Grubor 2025, Biogen) | PMID 35331006 (Tukov 2022, Novartis) |
|---|---|---|
| **Species / age** | Cynomolgus macaque, 2–4 y and 2–3 y | Cynomolgus macaque, 13–19 mo (Asian origin) and 25–34 mo (Mauritius origin) |
| **Vector / cargo** | AAVhu68-ss-coSMN1; AAV9-hGBA1; **AAV9-mir-SOD1, a non-protein cargo** | scAAV9 onasemnogene abeparvovec (CMV enhancer / chicken-β-actin, human *SMN*), one cargo |
| **Dose** | 3.68 × 10¹³ / 3.5 × 10¹³ / 3.0 × 10¹³ / 4.0 × 10¹³ GC per animal, one dose per study | 1.2 / 3.0 / 6.0 × 10¹³ vg per animal as a series; the mitigation arm fixed at 3.0 × 10¹³ |
| **Route** | ICM (three studies), IT lumbar (one); **no contrast agent** | IT lumbar, **0.20 mL Omnipaque 180 iohexol immediately before the vector**; plus an intravenous arm at 1.1 × 10¹⁴ vg/kg |
| **Regimen** | Dexamethasone 0.5 mpk SID + **tacrolimus 1 mpk SID (calcineurin inhibitor)** ± MMF 50 mpk BID; from day −2 and day −3, but **day 2** in the first study | Prednisolone 1 mg/kg/day from day −1; or rituximab 20 mg/kg q2w from day −14 + everolimus 0.5 mg/kg/day to day 14. **No calcineurin inhibitor, no T-cell-directed agent** |
| **Readout** | Graded histopathology; electron microscopy; DRG RNA-seq with WGCNA; immune-cell ISH and IHC; CSF and serum cytokines; ELISpot; **serum NF-H (heavy chain)** | Graded histopathology; antisense/sense ISH; **nerve conduction velocity**; serum/plasma and CSF **NfL (light chain)**; lymphocyte immunophenotyping; clinical-trial and pharmacovigilance review |
| **Earliest time point** | **Day 5**, before the lesion exists | **2 weeks**, after it exists |
| **DRG sampling density** | ≈9–12 ganglia per animal (26, 29, 36 across three animals per study) | Not stated in the main text; per-level tables are supplement-only |
| **n per comparison** | 3 per group | 3 per sex interim, **2 per sex terminal** |
| **Sponsor** | Biogen (all but two authors; the other two at the contract facility) | Novartis (all authors); the studies answer an **FDA partial clinical hold** on the sponsor's own product |
| **Result** | Pathology reduced across three cargos; transgene expression unchanged (p = 0.45, 0.997, 0.33) | Pathology unchanged by either regimen, including under 100 % B-cell depletion |

### What the disagreement is NOT

- **Not timing.** PMID 35331006's regimens began on day −1 and day −14, *earlier* than PMID 41404412's
  weakest arm, which began on day 2.
- **Not species.** Both are cynomolgus macaque.
- **Not a flat contradiction about immunity.** PMID 35331006 scopes its own negative to "primary
  **adaptive** immune responses" and states that innate activation "was not excluded".

### The three live explanations, with the evidence for each

1. **Drug class.** PMID 41404412's own reading: tacrolimus is the active element and PMID 35331006
   never tested that class. Most parsimonious — and offered by the party whose regimen worked.
2. **Power.** PMID 35331006's mitigation comparison has n = 2–3 per sex per cell with no power
   statement, and in its published female cervical-DRG table the prednisolone arm at day 92 shows
   neuronal degeneration in **2 of 2** animals against **1 of 2** unsuppressed — a direction two
   animals cannot establish either way.
3. **Procedure and sampling.** Iohexol contrast in one and not the other; ≈9–12 versus an unstated
   number of ganglia per animal; different capsid, promoter and cargo.

### The constraint both poles must respect

PMID 36700120 shows that **empty capsid and promoter-less constructs cause neither the lesion nor an
NfL rise**. Whatever the effector arm, the lesion requires transgene expression — which is also
PMID 35331006's stated mechanism and is not contradicted by PMID 41404412, whose late (day 15–29)
transcriptional changes do correlate with transgene level.

### Non-independence, which changes how the poles are weighed

PMID 35331006 and PMID 36700120 are **not** two sources. Same sponsor; four shared authors (Tukov,
Meseck, Penraat, Chand); PMID 36700120's data "extracted from the Novartis study data warehouse";
and three of its study descriptors match the other paper's studies specifically — a Mauritius-origin
non-GLP cohort, two studies using Omnipaque 180 contrast, and an intravenous arm at ≈1.0 × 10¹⁴
vg/kg. Neither paper cross-lists study identifiers, so overlap cannot be **proved** from these
artefacts. The appearance of two-against-one is therefore one sponsor's dataset against another's.

## Transfer limit to WWOX-DEE, stated explicitly

None of the three sources mentions WWOX (`grep` returns 0 on each artefact), and
`WWOX AND dorsal root ganglion` returns **2** PubMed records (esearch 2026-10-03). AAV DRG toxicity
is reported as a **class effect of the vector**, not of any transgene, so the *existence* of the risk
transfers to any AAV CNS programme including a WWOX one. What does **not** transfer: the regimens
(NHP immunosuppression schedules are not an infant protocol and none was tested in one), the
magnitudes (cargo-, capsid-, dose- and route-specific), and the mechanism (the one source that
measured it states the immune mechanism **does not hold in mouse**, so no rodent WWOX study can test
this question).

## Ops (provisional; anchors and next-free ids re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RL-C-20261003w4a — Is AAV dorsal-root-ganglion toxicity immune-preventable or dose-intrinsic? An open question with two primate datasets on opposite sides` |
| anchor | after the current final record `RL-GT-001`; the file's last line is `**Version update:** v1.3 — 2026-07-25 (integrity repair: restored the previously referenced RL-BIOM-001 record)` |
| body | The axis table above; the three live explanations with their evidence; the constraint from PMID 36700120 that the lesion requires transgene expression; the non-independence of PMID 35331006 and PMID 36700120 with its three matching descriptors; and the transfer limit paragraph. Status `open`, tag `INFERENZA`. Cross-reference `RL-GT-001` (gene therapy design principles) and `CC-20261003W3-C-RESTORATION-SPEC-01`, whose off-target-organ row already carries DRG toxicity as an AAV class effect. |
| next action | Watch for a head-to-head primate study giving dexamethasone + tacrolimus against prednisolone alone with vector, dose, route, contrast protocol and ganglion sampling density held constant, and powered. Nothing in the repository can decide this question without it. |

### 2 · `disease-models/wwox/research/dismissal_ledger_current.md`

| field | value |
|---|---|
| op | `append` (new record, provisional id `DIS-031`; `DIS` max measured at **30** by `registry_records.py catalog` after merging `main` at 31da5fa) |
| record | `DIS-031 — «AAV dorsal-root-ganglion toxicity is immune-mediated and can be prevented prophylactically» → ❌ NOT ESTABLISHED on the sources read (and its negation is not established either)` |
| anchor | after `DIS-030`; the file's last line is the `REVIVAL_TRIGGER` bullet of `DIS-030` |
| body | **PREMISE: DATO** (2026-10-03, intake wave 4, Scientist C, `context_policy: SOURCE_FIRST`). The positive rests on a multi-target pharmacological block with n = 3 per group in which no antigen-specific T cells were detected and the effector mechanism is labelled a postulate by its own authors. The negative rests on two regimens that exclude the drug class the positive identifies as active, with n = 2–3 per sex per cell and no power statement, in a study whose own authors scope their conclusion to adaptive immunity and state that innate activation was not excluded. **Both directions are therefore unsupported as general claims**, and this entry exists so that the next session does not adopt either pole from an abstract. The entry explicitly does **not** reject either result as reported: each is a valid measurement of its own protocol. |
| `REVIVAL_TRIGGER` | A primate study comparing a calcineurin-inhibitor-containing regimen against a steroid-only regimen with vector, dose, route, contrast protocol and ganglion sampling density held constant and with a stated power analysis; **or** publication of study identifiers showing whether PMID 36700120's nine pooled studies include PMID 35331006's studies, which would decide whether the negative pole has independent support. |

## What would change the model if true, and what would falsify this

**Would change it:** the head-to-head study above. It is the single largest unknown in specifying a
CNS AAV's risk profile in advance, and it is answerable with existing reagents.

**Would falsify the characterisation here:**
- a power analysis showing PMID 35331006's mitigation arms were adequately powered — the published
  per-cell n of 2–3 is the whole basis for discounting its negative, and removing that basis would
  make the disagreement biological rather than methodological;
- study identifiers showing PMID 36700120's studies do **not** include PMID 35331006's, which would
  restore the two as independent sources and strengthen the "not preventable" pole.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Immune cell recruitment and ultrastructural change were detected before any lesion could be seen. | prior to detectable neuronal cell body degeneration/necrosis observed on day 15 by both histopathology and electron microscopy | Results, type I interferon signalling and immune cell recruitment, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(In the first of the three mitigation studies the drugs began the day after the vector, so that arm was not prophylactic. | Immunosuppression (IMS) dosing started on day 2 | Materials and methods, AAVhu68-hSMN1 immunosuppression study #1, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The source names the result it contradicts and attributes the difference to the drugs used rather than to biology. | without apparent reductions in AAV-mediated DRG toxicity | Discussion, comparison with other regimens, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The stated reason for the difference is the addition of a T-cell inhibitor to a steroid. | we reason that the inhibition of T cells via the addition of Tacrolimus to an anti-inflammatory glucocorticoid steroid is responsible for observed effect | Discussion, comparison with other regimens, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The authors decline to call their regimen optimal. | While we cannot conclude the “optimal” regimen, our data support that dexamethasone and tacrolimus are sufficient to reduce AAV-mediated DRG toxicity | Discussion, comparison with other regimens, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The effector mechanism is a postulate and not a measurement, because no antigen-specific T cells were found. | it is reasonable to postulate that the infiltrating T cells in the DRG are targeting transduced neurons | Discussion, immune-mediated elimination, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The required duration of suppression is a prediction that no arm in the study tested. | we predict that the immunosuppression regimen would need to be maintained for at least 6 months | Discussion, immune-mediated elimination, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The authors state that the immune mechanism does not hold in the mouse, which bounds every rodent test of this question. | immune infiltration into the DRG in mice is considered a secondary response to neuronal degeneration | Discussion, species comparison, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The other primate programme found no mitigation from the regimens it tested. | microscopic DRG findings were not mitigated with coadministration of anti-inflammatory or immunosuppressive regimens | Conclusions, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(That negative is scoped by its own authors to adaptive immunity. | suggesting that primary adaptive immune responses may not be a critical mediator | Discussion, immunosuppression paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The same authors leave innate immune activation explicitly unexcluded. | activation of the innate immune response in transduced cells was not excluded | Discussion, pathogenesis paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The comparison between regimens is reported qualitatively, with no statistic attached. | In general, these findings were reported as similar in incidence and severity in animals administered | Results, thirteen-week intrathecal mechanistic study, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The lesion did not scale with dose across the range tested, so dose alone cannot bound it. | did not demonstrate a dose response | Discussion, comparison with other AAV gene therapies, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(Human relevance of the finding is declared unknown by the authors. | The translational relevance of DRG pathology in humans is currently unknown | Discussion, clinical relevance paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(The lesion requires transgene expression: capsid alone produced neither pathology nor biomarker rise. | No DRG microscopic findings were observed in cynomolgus macaques administered empty AAV9 capsid | Results, DRG microscopic evaluation, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The pooled dataset comes from one sponsor's own warehouse. | extracted from the Novartis study data warehouse | Materials and methods, data extraction and analyses, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(One of the pooled studies used animals of the same unusual origin as the companion paper's mechanistic study. | a small group of Mauritius-origin macaques from a European-based supplier were included in one non-GLP study | Materials and methods, animal test system, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The lesion shows no clear dose relationship in the pooled dataset either, over the largest available denominator. | Relatively little or no discernible dose response was reported in the DRG microscopic findings | Results, early DRG microscopic findings, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED, authored from the prose specification.** `RL-C-20261003w4a` appended to `research_lines_current.md` (the axis table, the three live explanations with their evidence, the constraint that the lesion requires transgene expression, the non-independence of the two Novartis papers with its three matching descriptors, and the transfer-limit paragraph) and **`DIS-031`** appended to `dismissal_ledger_current.md` with its `PREMISE: DATO` tag and its `REVIVAL_TRIGGER`, stating that **both** directions are unsupported as general claims. `DIS` was re-measured at 30, so the declared `DIS-031` was free. The research-lines anchor was first written as an `id` and the editor refused it (`ANCHOR_MISSING`, exit 3, nothing written) because `RL-*` records sit at the file's section level; re-keyed to the exact heading text and applied.
