# CC-20261003w4-C-TOXBIOMARKER-01 — a vector-toxicity surveillance panel with measured operating characteristics, and why it is Tier 3 for WWOX

- `context_policy: SOURCE_FIRST`
- Sources: PMID 36700120 (`FTR-20261003-36700120-01`), PMID 41404412
  (`FTR-20261003-41404412-01`), PMID 35331006 (`FTR-20261003-35331006-01`). All manifests validate
  (`--verify-artifacts --require-current-schema`, `VERDICT: PASS`). **None mentions WWOX.**
- Change class: **MINOR**. One research-line record and one research-candidate record, both research
  layer. No claim and no biomarker record is created, because under `LEGEND_CORE` §13 none of these
  analytes is a WWOX biomarker at all.
- **Nothing here is medical advice.**

## The §13 ruling first, because it determines where this goes

`LEGEND_CORE` §13 requires that a **disease** biomarker measure the functional state of the target
gene: Tier 1 a direct gene readout, Tier 2 a proximal pathway readout, **Tier 3 not a gene biomarker
→ separate file**.

Neurofilament light chain, neurofilament heavy chain, CSF CXCL10 and CSF MIP1α measure **neuro-axonal
injury and innate immune activation of any cause**. None of them reports WWOX abundance, transcript,
splicing or function. All four are therefore **Tier 3 with respect to WWOX** and may not be recorded
as WWOX biomarkers in any registry. They are admissible only as **biomarkers of vector toxicity** in
a safety-surveillance record — a different object, and this candidate keeps it in the research layer
and out of the biomarker line `RL-BIOM-001`.

§13 also forbids calling any candidate "validated" without direct sensitivity and specificity
evidence **in the disease population**. There is none: PMID 36700120 states that "To date, NfL
measurements have not been incorporated into clinical trials for AAV therapies." The panel below is
therefore **nonclinical-grade**, and that word is load-bearing.

## What is measured, and this corrects a premise of the assignment

The assignment supposed that PMID 36700120 offers a correlation with severity but "not a per-animal
detection threshold". **It offers exactly that.**

| Measurement | Value |
|---|---|
| Denominator | 260 cynomolgus macaques, nine studies (four GLP, five non-GLP); 193 dosed with AAV9, of which 8 received empty capsid or a promoter-less construct, leaving 185 with a full vector; 67 vehicle controls |
| Histopathology rigour | **18–21 DRG per animal** (5–6 cervical, thoracic and lumbar each; 2–3 sacral), five-point severity scale, ACVP board-certified pathologist with contemporaneous peer review and consensus grading; composite per-animal endpoint: 132 unremarkable, 67 minimal, 41 slight, 20 moderate |
| Lesion incidence | **78 %** at 2–12 weeks (max per-animal severity moderate), **42 %** up to 52 weeks (max minimal) |
| Clinical signs | 1 animal (the Results give the denominator as 193, the Discussion as 185) |
| Blood–CSF agreement | Pearson R² = 0.80 over 399 paired samples (serum 0.80, plasma 0.82) |
| Baselines | Pre-dose means 12.2 pg/mL serum, 12.2 pg/mL plasma, 192 pg/mL CSF — CSF ≈16× blood |
| Correlation with severity | Kendall τ 0.50–0.55 for all four NfL measures |
| **ROC AUC** | **0.85 blood / 0.81 CSF** for unremarkable vs any finding; **0.95 / 0.94** excluding minimal grade |
| **Per-animal cut-offs** (fold change from pre-dose; blood / CSF sensitivity and specificity) | 1.5× → 0.73/0.71 and 0.83/0.68 · 2× → 0.68/0.82 and 0.76/0.72 · 3× → 0.59/0.92 and 0.68/0.84 · 5× → 0.43/0.96 and 0.60/0.91 · 10× → 0.32/0.99 and 0.49/0.95 |
| Incremental value | Blood NfL added to a confounder model (dose, route, sex, treatment group) improved fit at p = 8 × 10⁻¹¹; adding CSF on top of blood improved fit at p = 0.0003 but moved AUC only 0.83 → 0.85 — i.e. **blood alone is sufficient**, and the invasive sample is not needed |
| Mechanistic constraint | Empty capsid and promoter-less constructs produced **neither** lesion nor NfL rise |
| Earlier-rising candidates | PMID 41404412: CSF CXCL10 significantly raised at **day 5** and MIP1α at day 9, both **before** the first lesion at day 15, both correlating with serum NF-H; CSF CXCL10 (max 9 400 pg/mL) ≈9× serum, indicating local CNS synthesis |

## The five caveats that must travel with the panel

1. **The procedure moves the marker.** Post-dose **vehicle-control** NfL rises above pre-dose in both
   matrices with wider ranges (serum mean 12.2 → 24.3 pg/mL; CSF 192 → 433.7 pg/mL). The authors
   attribute this to intrathecal dosing, CSF collection, femoral blood draws, co-housing and
   handling, and cite a report that CSF neurofilament can stay elevated for up to three weeks after
   a lumbar puncture. PMID 41992613 reproduces the effect independently: its CSF NfL peaked at day 15
   **in every group including vehicle**.
2. **A rise can occur without a lesion, and the authors say so**, because the lesion is heterogeneous
   and not all ganglia are examined.
3. **It is not disease-specific**, which the authors name as the obstacle to using it in a patient
   who already has a neurodegenerative disorder — precisely the WWOX-DEE case.
4. **Only fold-change cut-offs exist**, never a concentration. This presupposes a pre-dose sample and
   a stable individual baseline, so the panel is unusable without baseline sampling designed in
   before dosing.
5. **Non-independence.** PMID 36700120 and PMID 35331006 are the same sponsor with four shared
   authors, and the pooled data were "extracted from the Novartis study data warehouse"; three study
   descriptors match the other paper's studies. The assay's performance claim is one sponsor's
   internal validation, not a cross-sponsor replication.

## What this adds to the wave-3 specification

`CC-20261003W3-C-RESTORATION-SPEC-01` records PMID 40349107 using serum NfL as a toxicity biomarker
with a threshold of "1,719 pg/mL or greater" in affected animals against "≤679 pg/mL" with a
de-targeting element. PMID 36700120 supplies what that bare threshold lacks — a denominator, a ROC
curve and sensitivity/specificity — **and simultaneously constrains how the wave-3 threshold can be
used**, because the validated discriminator is a **fold change from an individual's own pre-dose
value**, not an absolute concentration. A single absolute cut-off carried forward from one study is
therefore weaker than it looks, and the correct form of the wave-3 row is a fold-change rule plus a
mandatory baseline draw.

## Ops (provisional; anchors and next-free ids re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RL-C-20261003w4c — Vector-toxicity surveillance for a CNS AAV: a nonclinical-grade panel (blood NfL, with CSF CXCL10 and MIP1α as earlier-rising candidates), Tier 3 under LEGEND_CORE §13` |
| anchor | after the current final record `RL-GT-001`; the file's last line is `**Version update:** v1.3 — 2026-07-25 (integrity repair: restored the previously referenced RL-BIOM-001 record)`. If `RL-C-20261003w4a` and `RL-C-20261003w4b` are applied first, append after them |
| body | The measurement table and the five caveats above, verbatim in substance. 🔴 Opening sentence must state the §13 ruling: these analytes measure vector toxicity, not WWOX function, are **Tier 3** with respect to WWOX, and may not be recorded as WWOX biomarkers; the record exists in the research layer as a **safety-surveillance** object. Status `open`, tag `DATO` for the measured operating characteristics and `INFERENZA` for their applicability to a WWOX programme. Cross-reference `RL-BIOM-001` **explicitly as the line this record does NOT belong to**, `RL-GT-001`, and `CC-20261003W3-C-RESTORATION-SPEC-01` (whose off-target-organ row carries the bare 1 719 pg/mL threshold this record qualifies). |
| next action | Where the repository carries an absolute serum-NfL threshold, carry the fold-change rule and the mandatory pre-dose baseline alongside it; and record that blood sampling alone is sufficient, since adding CSF moved ROC AUC only 0.83 → 0.85. |

### 2 · `disease-models/wwox/research/research_candidates_current.md`

| field | value |
|---|---|
| op | `append` (new record) |
| record | `RC-C-20261003w4 — Before any WWOX vector study, design the toxicity-surveillance baseline rather than the threshold` |
| anchor | the file's last line is `---`, following the `## Pre-existing RCs` heading block; append a new record after it |
| body | The concrete acquisition: a pre-dose blood draw per animal, longitudinal sampling at the time points where the signal actually lives (day 8 onward, maximum between days 15 and 28/29, with resolution by 52 weeks), and **both** a vehicle arm and an empty-capsid or promoter-less arm — because PMID 36700120 shows the vehicle arm moves the marker and shows that capsid alone moves neither marker nor histology, so without both arms a rise cannot be attributed. Carry the four limits of the panel: nonclinical only; fold-change not concentration; not disease-specific, which is a specific problem in a developmental encephalopathy where background neurofilament may already be raised; and one sponsor's internal validation. Also carry CSF CXCL10 and MIP1α as the earlier-rising candidates from PMID 41404412 with their limit — they are reported in three studies from one sponsor, with no independent replication and no operating characteristics at all. |

## What would change the model if true, and what would falsify this

**Would change it:** a cross-sponsor validation of the NfL operating characteristics, or any clinical
dataset relating blood NfL to a histopathological or electrophysiological DRG endpoint in humans —
which would move the panel from nonclinical-grade toward clinical use. Also: operating
characteristics for CSF CXCL10, which currently has none and whose only support is one sponsor's
three studies.

**Would falsify statements here:** evidence that NfL does report WWOX functional state in some
proximal way, which would move it from Tier 3 to Tier 2 — note that `WWOX AND neurofilament` returns
**1** PubMed record (esearch 2026-10-03), so this is an empty field rather than a settled one; or
study identifiers showing PMID 36700120's nine studies are independent of PMID 35331006's, which
would make the validation a cross-study rather than a within-programme result.

### LOCATOR TRIPLES FOR BLIND AUDIT

(A per-animal detection threshold with sensitivity and specificity does exist for this biomarker. | A cutoff of 1.5-fold in NfL from pre-dose values leads to the greatest sensitivity | Results, correlation between NfL changes and DRG histopathology, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The lesion requires transgene expression: capsid alone produced neither pathology nor a biomarker rise. | No DRG microscopic findings were observed in cynomolgus macaques administered empty AAV9 capsid | Results, DRG microscopic evaluation, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(A biomarker rise can occur without any microscopic correlate, by the authors' own caveat. | may not have been associated with microscopic changes | Discussion, assay performance paragraph, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The biomarker has not been taken into clinical AAV trials, so it is not clinically validated. | To date, NfL measurements have not been incorporated into clinical trials for AAV therapies. | Discussion, clinical translation paragraph, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(A raised value is not specific to any disease, which is the stated obstacle to using it in a patient who already has a neurodegenerative disorder. | Greater concentrations of NfL can occur with neuronal injury and are not disease specific | Discussion, soluble biomarker paragraph, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The lesion shows no clear dose relationship, so the biomarker is not a proxy for dose. | Relatively little or no discernible dose response was reported in the DRG microscopic findings | Results, early DRG microscopic findings, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(The validation dataset is one sponsor's own warehouse, not a cross-sponsor replication. | extracted from the Novartis study data warehouse | Materials and methods, data extraction and analyses, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(One pooled study used animals of the same unusual origin as the companion paper's mechanistic study, which is one of three matching descriptors. | a small group of Mauritius-origin macaques from a European-based supplier were included in one non-GLP study | Materials and methods, animal test system, `files/fulltext/PMID36700120_Johnson2022_PMC.xml`)

(Chemokine signal in the CSF preceded the lesion, which is what makes it a candidate earlier marker. | prior to detectable neuronal cell body degeneration/necrosis observed on day 15 by both histopathology and electron microscopy | Results, type I interferon signalling and immune cell recruitment, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(The authors of the earlier-marker study also state that their effector mechanism is a postulate, which bounds how far the marker's interpretation can go. | it is reasonable to postulate that the infiltrating T cells in the DRG are targeting transduced neurons | Discussion, immune-mediated elimination, `files/fulltext/PMID41404412_Grubor2025_PMC.xml`)

(In the other primate programme the biomarker tracked the lesion but the regimens did not change it, so a marker is not a mitigation. | microscopic DRG findings were not mitigated with coadministration of anti-inflammatory or immunosuppressive regimens | Conclusions, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)

(That programme's own authors caution against translating their biomarker findings to patients. | The translational relevance of DRG pathology in humans is currently unknown | Discussion, clinical relevance paragraph, `files/fulltext/PMID35331006_Tukov2022_PMC.xml`)


## BATCH DISPOSITION — `BATCH_20261003_003` (2026-10-03, ACTOR_ID `scientist`, Scientist H), append-only

**Verdict:** PROPAGATED

**PROPAGATED, authored from the prose specification.** `RL-C-20261003w4c` opens with the §13 ruling, as the candidate required: NfL, NF-H, CSF CXCL10 and MIP1α are **Tier 3 with respect to WWOX**, admissible only as vector-toxicity surveillance, and the record states explicitly that it does **not** belong to the biomarker line `RL-BIOM-001`. It carries the operating-characteristics table (ROC AUC, the five fold-change cut-offs with sensitivity and specificity, the denominators, the baselines) and all five caveats, including that the procedure itself moves the marker and that only fold changes — never a concentration — are validated. `RC-C-20261003w4` appended to `research_candidates_current.md` with the baseline-first acquisition and the two mandatory control arms. Nothing was recorded in any biomarker or endpoint file.
