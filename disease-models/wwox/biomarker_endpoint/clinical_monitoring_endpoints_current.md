# CLINICAL MONITORING ENDPOINTS — Distal response markers

> **Operational file for the clinical, neurophysiological, neuroimaging, motor, behavioral and digital endpoints used to monitor response to therapeutic interventions in WWOX-DEE.**
> Version: v3.3.1
> Status: STRUCTURE READY — no endpoint populated yet (population via BATCH_COMMIT).
> Sister file: [[biomarker_candidates_current]]

---

## 0. SCOPE (HARD RULE)

This file contains **distal endpoints of monitoring and therapeutic response** in WWOX-DEE.

> **Hard disambiguation rule.**
> The endpoints here **are not WWOX biomarkers**.
> They are **clinical / functional / neurophysiological indicators of response** to therapeutic interventions.
> For WWOX biomarkers (Tier 1 and Tier 2) → see `biomarker_candidates_current.md`.

### What belongs here

- Specific or non-specific EEG / qEEG patterns
- Structural and functional neuroimaging (MRI, DTI, spectroscopy, volumetry)
- Motor endpoints (gross/fine motor, posture, tone)
- Sleep endpoints (architecture, duration, fragmentation, video-PSG)
- Behavioral / cognitive / social endpoints (standardized scales)
- Epileptological endpoints (seizure frequency, duration, severity, drug load)
- Digital biomarkers (wearables, motion tracking, vocalization, video)
- Startle response and other reflexes
- Nutritional / growth endpoints (BMI, head circumference) where relevant

### What does NOT belong here

- Biochemical / molecular markers → see `biomarker_candidates_current.md`
- Direct measurements of WWOX (protein, mRNA, activity) → see `biomarker_candidates_current.md`
- Generic clinical observations without a measurement protocol

### Non-confusion rule

> **A distal clinical endpoint can change even without a WWOX-linked biological modification.**
> Examples: EEG improvement after AED readjustment, motor improvement after physiotherapy, sleep improvement after an environmental intervention.
> This file documents **useful** endpoints, not **causally WWOX-specific** ones.
> To infer a WWOX-linked biological effect, distal endpoints must be **read in combination with proximal biomarkers** (Tier 1/2).

---

## 1. STRATEGIC RATIONALE

Even with validated proximal WWOX biomarkers, distal clinical endpoints remain necessary for three operational reasons:

1. **Measuring real clinical benefit.** A gene therapy that restores WWOX expression (Tier 1) but produces no measurable clinical improvement has no therapeutic value.
2. **Fine temporal granularity.** Some endpoints (EEG, sleep, digital) are repeatable daily or weekly — far more than biochemical biomarkers.
3. **Accessibility.** An EEG or a wearable is obtainable in a standard clinical setting, whereas some Tier 1 biomarkers require biopsies or specialized labs.

> Reference formula:
> *"WWOX biomarkers (Tier 1/2) measure whether the therapy is acting; distal clinical endpoints (Tier 3) measure whether the patient is doing better. Both are needed, and they must not be confused."*

---

## 2. DOMAIN STRUCTURE

Endpoints are organized by **functional domain**, not by proximity hierarchy.
Each domain has different operational properties (frequency, accessibility, subjectivity, sensitivity to change).

### 2.1 Neurophysiological

- Routine EEG (background, epileptiform anomalies, organization)
- qEEG (quantitative analysis, power spectrum, coherence)
- Long-term video-EEG monitoring
- ERP / EP (evoked potentials, where applicable)

### 2.2 Neuroimaging

- Structural MRI (volumetry, malformations, myelination)
- DTI (tract integrity)
- Spectroscopy (MRS) — in-vivo CNS metabolites
- Functional MRI (limited in severe pediatric DEE)

### 2.3 Epileptological

- Seizure frequency (by type)
- Seizure duration
- Severity (scales: e.g. Hague Seizure Severity Scale)
- Drug load / number of AEDs
- Status epilepticus episodes
- Response to rescue medications

### 2.4 Motor

- Standardized motor scales (GMFM, AIMS, others)
- Tone (Ashworth, MAS)
- Posture, head control, support
- Fine motor (where assessable)

### 2.5 Sleep

- Sleep architecture (PSG)
- Total duration, latency, efficiency
- Fragmentation, awakenings
- Circadian pattern
- Nocturnal events (seizures, abnormal movements)

### 2.6 Behavioral / cognitive / social

- Developmental scales (e.g. Bayley, Vineland)
- DEE-specific scales (if available)
- Engagement, attention, eye contact
- Vocalization / non-verbal communication
- Quality of Life (QoL) — caregiver and (where possible) patient

### 2.7 Digital biomarkers

- Wearables: HR, HRV, continuous motor activity
- Video motion tracking
- Audio-based: vocalizations, crying, respiratory patterns
- Smartphone / tablet — engagement with stimuli
- Continuous sleep tracking

### 2.8 Nutritional / growth

- Weight, height, BMI
- Head circumference (relevant in pediatric DEE)
- Dysphagia, feeding modality
- Peripheral nutritional markers (if relevant)

---

## 3. SCORECARD — Endpoint evaluation rubric

Every endpoint, when populated, is evaluated on **8 dimensions** (simplified relative to the biomarker file — there is no WWOX-specificity because it is irrelevant by design).

Score: `0` (absent/inadequate) — `1` (weak) — `2` (medium) — `3` (strong).

### 3.1 Measurement dimensions

| Dimension | Description |
|---|---|
| **Standardized measurability** | Is there a standard protocol, a validated scale, available instrumentation? |
| **Repeatability over time** | Reproducible longitudinally with low inter-rater drift? |
| **Temporal granularity** | Obtainable frequency (daily / weekly / monthly / quarterly) |
| **Clinical accessibility** | Obtainable in a standard clinical setting (no specialized lab)? |

### 3.2 Sensitivity dimensions

| Dimension | Description |
|---|---|
| **Sensitivity to change** | Does the endpoint capture real changes over time? |
| **Baseline available** | Is there a pre-intervention baseline measurement? |
| **MCID defined** | Is there a Minimal Clinically Important Difference for this population (or a proxy)? |

### 3.3 Strategic dimensions

| Dimension | Description |
|---|---|
| **Clinical actionability** | Does a measured change lead to a concrete clinical decision? |

### Scoring summary

Total max: 8 × 3 = 24.

Suggested thresholds (provisional):

- `≥ 18` — Strong endpoint, include in the monitoring plan
- `12–17` — Moderate, evaluate case by case
- `6–11` — Weak, optional
- `< 6` — Drop from the file

---

## 4. RESPONDER DEFINITION (CRITICAL)

For every endpoint used to assess therapeutic response, what constitutes response vs non-response must be defined **a priori**.

### Minimum components of a responder definition

1. **Direction**: should the marker increase or decrease?
2. **Magnitude (MCID)**: how much must it change to be clinically relevant?
3. **Persistence**: for how long must the change be maintained?
4. **Baseline reference**: relative to what is it measured (single timepoint / mean of N measurements)?
5. **Confounders to exclude**: AED adjustment, intercurrent infections, growth, etc.

> **Anti-overclaim rule.**
> A responder definition established post-hoc after seeing the data **is not valid** as evidence of efficacy.
> Responder definitions must be fixed before the observation period.

---

## 5. EVIDENCE STATUS VOCABULARY

Epistemic states for each endpoint.

| Status | Meaning |
|---|---|
| `VALIDATED_GENERIC` | Endpoint validated in a generic DEE population (not WWOX-specific) |
| `VALIDATED_WWOX` | Endpoint validated specifically in a WWOX-DEE population (rare) |
| `EXPLORATORY` | Used in the literature but without formal validation in DEE |
| `NOT VALIDATED` | Default status for new endpoints or emerging digital biomarkers |

> Most endpoints in WWOX-DEE today are `VALIDATED_GENERIC` or `EXPLORATORY`. Few are `VALIDATED_WWOX`.

---

## 6. ENDPOINT TEMPLATE

Standard template for each endpoint when populated.

```markdown
## CME-NNN — [Endpoint name]

### Identification
- ID: CME-NNN
- Domain: Neurophysiological | Neuroimaging | Epileptological | Motor | Sleep | Behavioral | Digital | Nutritional
- Created via: BATCH_COMMIT_ID
- Last updated: YYYY-MM-DD
- Evidence status: VALIDATED_GENERIC | VALIDATED_WWOX | EXPLORATORY | NOT VALIDATED

### Description
[What it measures, how it is measured, scale/instrument used]

### Time resolution
- Minimum interval: [e.g. 24h, 1 week, 1 month, 3 months]
- Practical interval: [...]
- Baseline available: YES | NO | PARTIAL

### Scorecard (0–3 per dimension)
| Dimension | Score | Notes |
|---|---|---|
| Standardized measurability | | |
| Repeatability over time | | |
| Temporal granularity | | |
| Clinical accessibility | | |
| Sensitivity to change | | |
| Baseline available | | |
| MCID defined | | |
| Clinical actionability | | |
| **TOTAL** | **/24** | |

### Responder definition
- Direction: ↑ | ↓ | bidirectional
- Magnitude (MCID): [value or "not established"]
- Persistence required: [e.g. 4 consecutive weeks]
- Baseline reference: [single / mean of N timepoints]
- Confounders to exclude: [...]

### Intended use
- [ ] Pre/post gene therapy monitoring
- [ ] Pharmacological response monitoring
- [ ] Repurposing / cofactor / diet response
- [ ] Trial endpoint candidate
- [ ] Routine clinical follow-up

### Limitations
[What this endpoint does NOT say, main confounders, value outside the context]

### Linked biomarkers (Tier 1/2) — combined reading
[Which biomarkers from biomarker_candidates_current should be read together with this endpoint to infer a WWOX-linked biological effect]

### Wikilinks
- Sister file: [[biomarker_candidates_current]]
- Paper support: [[paper_registry_current#PAPER NNN]]

### Change log
| Date | Change | Batch ID |
|---|---|---|
```

---

## 7. POPULATED ENDPOINTS

> **Currently empty.** No endpoint populated in this version of the file.
> Population happens via BATCH_COMMIT.

The next clinical-endpoint BATCH_COMMITs must:
1. propose new endpoints via COMMIT_CANDIDATE
2. fill in the complete template
3. assign a scorecard
4. declare evidence status
5. fix the responder definition **before** the observation period
6. declare the proximal biomarkers to read in combination

---

## 8. MONITORING PLAN (operational view)

> **Currently empty.** To be built when a sufficient set of endpoints is populated.

Expected format (future):

```
Pre/post gene therapy monitoring plan:
- Daily: [endpoint X, Y]
- Weekly: [endpoint Z]
- Monthly: [endpoint W]
- Quarterly: [endpoint V]
+ paired biomarkers (Tier 1/2): [...]
```

---

## 9. COMBINED READING WITH BIOMARKERS

> **Currently empty.** To be populated when Tier 3 endpoints and Tier 1/2 biomarkers are both mature.

Logic: for each clinical endpoint, indicate which proximal biomarkers should be read together to distinguish:

- **apparent clinical improvement without WWOX biological modification** (placebo, physiotherapy, AED readjustment)
- **clinical improvement with WWOX biological modification** (real effect of the gene-therapy / molecular intervention)
- **WWOX biological modification without clinical improvement** (therapy acting but clinical benefit not yet visible)
- **no change** (ineffective therapy)

This is the fundamental 2×2 matrix for reading therapeutic response non-naively.

---

## 10. CHANGE LOG (this file)

| Date | Event | Batch ID |
|---|---|---|
| — | File created at v3.3.1 — structure only, no endpoints populated | Patch 3 |

---

## 11. WIKILINKS

- Sister file: [[biomarker_candidates_current]]
- Research line: [[research_lines_current#RL-BIOM-001 — WWOX functional-state biomarkers]]
- Framework: [[LEGEND_CORE]]
- State manifest: [[state_manifest_current]]

---

**End of `clinical_monitoring_endpoints_current.md`**

> Central discipline: these endpoints are distal. They measure clinical response, not the functional state of WWOX.
> To infer a WWOX-linked biological effect, they must be **read in combination** with proximal biomarkers (Tier 1/2).
