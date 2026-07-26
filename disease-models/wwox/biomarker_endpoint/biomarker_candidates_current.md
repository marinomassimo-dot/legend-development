# BIOMARKER CANDIDATES — WWOX functional-state

> **Operational file of the research line `RL-BIOM-001 — WWOX functional-state biomarkers`.**
> Version: v3.3.1
> Status: STRUCTURE READY — no candidate populated yet (population via BATCH_COMMIT).

---

## 0. SCOPE (HARD RULE)

This file contains **exclusively** candidate biomarkers that measure, or proximally reflect, **the functional state of WWOX**.

> **Hard admission rule.** A candidate biomarker enters this file **only if** it satisfies both conditions:
> 1. **Mechanistic linkage** — it derives from a pathway where WWOX has a demonstrated or strongly inferred causal role (not merely correlational).
> 2. **Functional readout** — it reflects the functional state of WWOX (absent / partially active / restored), not just the presence of disease.

### What does NOT belong here

- EEG / qEEG patterns
- Neuroimaging (MRI, spectroscopy, DTI)
- Sleep, startle, motility, digital biomarkers
- DEE clinical severity endpoints
- Generic non-specific neurodamage markers

→ These live in `clinical_monitoring_endpoints_current.md` as **distal endpoints of monitoring and therapeutic response**, not as WWOX biomarkers.

### Anti-overclaim rule

> **No candidate biomarker in this file may be described as a "validated WWOX biomarker" until direct validation evidence exists (documented sensitivity/specificity in a WWOX-DEE population).**

A candidate is always a **prudent inference** until it has formal validation evidence.

---

## 1. STRATEGIC RATIONALE

Searching for WWOX biomarkers is not a descriptive appendix. It is strategically comparable to therapeutic research, because:

- without robust biomarkers it is **not possible to reliably measure** the effect, duration and biological reversibility of a therapy (gene therapy, drugs, repurposing, cofactors, diet);
- to distinguish **apparent clinical improvement** from **real biological modification**;
- to build **objective endpoints for trial readiness**;
- to make the success or failure of a therapy readable.

> Reference formula (from `LEGEND CORE`):
> *"In WWOX, identifying candidate functional biomarkers is strategically comparable to therapeutic research, because without robust biomarkers it is not possible to reliably measure the effect, duration and biological reversibility of a therapy."*

---

## 2. DUAL OUTPUT MODEL

This research line produces two distinct outputs, not to be confused:

### 2.1 Operational output
A **shortlist of 2–4 Tier 1 candidates** mature enough to be proposed for external validation (e.g. a collaborating lab, a gene-therapy consortium).

### 2.2 Knowledge output
A **reasoned map** of why certain candidates are more plausible than others, useful even if none is ever validated. It retains inferential value even in the case of operational failure.

> Both outputs are legitimate. They must be kept **distinct**: a shortlist is not a validation.

---

## 3. TIER STRUCTURE

Candidates are organized into three tiers by **distance from the WWOX locus**.

### TIER 1 — Direct WWOX readout
Direct measurement of WWOX or its immediate products.

Categorical examples (NOT already-validated candidates):
- WWOX protein expression (Western blot, ELISA, mass spec) in accessible tissue
- WWOX transcript (mRNA quantification) — useful post gene therapy
- WWOX splice variants (if relevant for a specific variant, e.g. Q230P / c.1057-2A>G worked examples)
- WWOX enzymatic activity (oxidoreductase) — if reliably measurable
- Documented direct substrates (accumulated or depleted metabolic intermediates of WWOX-linked pathways)

**Expected status**: gold candidate for measuring the biological effect of gene therapy.

### TIER 2 — Proximal pathway readout
Measurement of pathway markers with a strong causal linkage to WWOX.

Categorical examples (NOT already-validated candidates):
- Redox/mitochondrial markers of the WWOX-Aldh3a2-MAO pathway (if the link holds)
- Specific sphingolipids / ceramides (if WWOX–lipid metabolism is confirmed)
- Cellular oxidative-stress markers in relevant tissue
- Documented direct protein partners (WWOX interactomics)
- Galactose-related pathway metabolites (if linkage confirmed)

**Expected status**: a reasonable proxy, but greater inferential distance from the locus.

### TIER 3 — DOES NOT BELONG IN THIS FILE
Distal endpoints (EEG, neuroimaging, sleep, motility, digital biomarkers) → see `clinical_monitoring_endpoints_current.md`.

---

## 4. TISSUE ACCESSIBILITY MAP

Critical constraint: WWOX is expressed predominantly in the CNS (and reproductive tissues), but the CNS is **not accessible in vivo**. Proxy tissues are required.

| Tissue source | Accessibility | Repeatability | Proxy validity (CNS readout) | Notes |
|---|---|---|---|---|
| Blood (PBMCs) | High | High | **WEAK (score 1)** — WWOX 0.71 TPM in whole blood = lowest of the 54 GTEx v8 tissues (~10% of brain); near the detection floor | Demoted from primary proxy: expression too low for reliable direct quantification of the WWOX product. Downstream biomarkers (metabolites/pathway) in plasma remain valid |
| EBV lymphocytes (LCL) | Medium (line expandable in culture) | Medium | **MODERATE (score 2)** — WWOX 3.17 TPM (46% of brain, GTEx v8) | Best cellular proxy for direct WWOX readout (e.g. Q230P protein stability, c.1057-2A>G splice RT-PCR); not longitudinal on fresh blood |
| Plasma / Serum | High | High | Variable per analyte | Good for metabolites, sphingolipids, redox markers |
| Fibroblasts (skin biopsy) | Medium (one-off procedure) | Low (no easy longitudinal) | **MODERATE (score 2)** — WWOX 2.24 TPM (33% of brain, GTEx v8); measurable in culture | Excellent for baseline, poor for monitoring; access via skin biopsy |
| Saliva | High | High | To assess | Verify whether it carries a WWOX-related signal |
| Urine | High | High | Limited for direct WWOX | Useful for excreted metabolites |
| CSF | Low (invasive lumbar) | Very low | High (closest to CNS) | Only for critical timepoints (e.g. pre/post gene therapy) |
| Hair / Nails | High | Low | Very low | Probably not useful; exclude explicitly after verification |

### Proxy validity score (0–3)

- `0` — the tissue does not reflect WWOX state in the CNS
- `1` — indirect reflection, high volatility
- `2` — partial but usable reflection
- `3` — strong and clinically actionable reflection

> No tissue in WWOX-DEE today has a validated `proxy validity = 3`. All values are inferential.

> **Cellular proxy-scoring source:** GTEx v8 (bulk RNA-seq, adult post-mortem tissue). Ranking: whole blood 0.71 TPM (WEAK, floor) < fibroblasts 2.24 (MODERATE) < LCL 3.17 (MODERATE) < brain 6.82 (target, not accessible in vivo). Caveat: median TPM ≠ protein detectability; does not capture pediatric expression or cell type (neurons vs glia). Proxy verdict = INFERENCE, not formal validation (which requires sensitivity/specificity in a WWOX-DEE population). Does not invalidate downstream (plasma metabolite/pathway) biomarkers.

---

## 5. SCORECARD — Candidate biomarker evaluation rubric

Every candidate biomarker, when populated, must be evaluated on these **13 dimensions**.

Score: `0` (absent/inadequate) — `1` (weak) — `2` (medium) — `3` (strong).

### 5.1 Mechanistic dimensions

| Dimension | Description |
|---|---|
| **WWOX-specificity** | Does the marker change *only* as a function of WWOX, or is it influenced by many pathways? |
| **Functional sensitivity** | Does it distinguish absent / partially active / restored, or only binary? |
| **WWOX-linked biological plausibility** | Strength of the mechanistic evidence for the WWOX link |
| **Distance from the primary mechanism** | 0 = direct readout; 3 = very distal (penalized in Tier 1, accepted in Tier 2) |

### 5.2 Measurement dimensions

| Dimension | Description |
|---|---|
| **Measurability** | Do standardized, accessible measurement methods exist? |
| **Stability** | Intra-individual variability at equal biological state |
| **Low volatility** | Resistance to acute confounders (infections, stress, diet) |
| **Repeatability over time** | Can it be measured longitudinally with good reproducibility? |

### 5.3 Clinical dimensions

| Dimension | Description |
|---|---|
| **Clinical accessibility** | Tissue/instrumentation obtainable in a standard clinical setting |
| **Reduced invasiveness** | Procedure tolerable in a pediatric DEE population |
| **Confounding risk** | How many non-WWOX factors can shift the value? |

### 5.4 Strategic dimensions

| Dimension | Description |
|---|---|
| **Utility for longitudinal monitoring** | Suitable for pre/post-therapy follow-up? |
| **Utility as a trial-readiness endpoint** | Could it serve as a primary or secondary trial endpoint? |

### Scoring summary

Total max: 13 × 3 = 39.

Suggested thresholds (provisional, to revise after the first candidates are populated):

- `≥ 30` — Strong candidate, consider for the operational shortlist
- `20–29` — Moderate candidate, keep in observation
- `10–19` — Weak candidate, knowledge output only
- `< 10` — Drop from the file

---

## 6. EVIDENCE STATUS VOCABULARY

Allowed epistemic states for each candidate. Updated at every BATCH_COMMIT that touches the candidate.

| Status | Meaning |
|---|---|
| `DATO` | Measurement of the marker in a WWOX-DEE population already documented in a paper (even if not yet as a validated biomarker) |
| `INFERENZA` | Marker derived from a documented WWOX-dysregulated pathway, but never measured in WWOX-DEE patients |
| `CANDIDATE` | Operational hypothesis based on mechanistic linkage; not yet measured in WWOX |
| `NOT VALIDATED` | Default status until formal validation (documented sensitivity/specificity) — applicable to *all* current candidates |

### Transition rule

> The `NOT VALIDATED` status applies to all candidates until direct formal-validation evidence exists. Promotion to "validated" requires a specific paper with sensitivity/specificity data in a WWOX-DEE population.

No candidate may be promoted to "validated" without an explicit BATCH_COMMIT documenting the validation source.

---

## 7. CANDIDATE TEMPLATE

Standard template for each candidate when populated.

```markdown
## BC-NNN — [Biomarker name]

### Identification
- ID: BC-NNN
- Tier: 1 | 2
- Created via: BATCH_COMMIT_ID
- Last updated: YYYY-MM-DD
- Evidence status: DATO | INFERENZA | CANDIDATE — NOT VALIDATED

### Description
[What it is, what is measured, how it is measured]

### Mechanistic linkage to WWOX
[Specific pathway, reference papers via wikilink:
  [[paper_registry_current#PAPER NNN]],
  [[claim_registry_current#CLAIM NNN]]]

### Tissue source
- Primary: [tissue]
- Proxy validity score (CNS): 0–3
- Alternative tissues: [...]

### Scorecard (0–3 per dimension)
| Dimension | Score | Notes |
|---|---|---|
| WWOX-specificity | | |
| Functional sensitivity | | |
| WWOX-linked biological plausibility | | |
| Distance from the primary mechanism | | |
| Measurability | | |
| Stability | | |
| Low volatility | | |
| Repeatability over time | | |
| Clinical accessibility | | |
| Reduced invasiveness | | |
| Confounding risk | | |
| Longitudinal-monitoring utility | | |
| Trial-readiness endpoint utility | | |
| **TOTAL** | **/39** | |

### Intended use
- [ ] Pre/post gene therapy monitoring
- [ ] Pharmacological response monitoring
- [ ] Repurposing / cofactor / diet response
- [ ] Trial endpoint candidate
- [ ] Knowledge output only

### Limitations
[What it does NOT measure, main confounders, inferential distance]

### Wikilinks
- Pathway: [[meta_metabolism_current#...]]
- Base claim: [[claim_registry_current#CLAIM NNN]]
- Supporting paper: [[paper_registry_current#PAPER NNN]]
- Research line: [[research_lines_current#RL-BIOM-001]]

### Change log
| Date | Change | Batch ID |
|---|---|---|
```

---

## 8. POPULATED CANDIDATES

> **Currently empty.** No candidate populated in this version of the file.
> Population happens via BATCH_COMMIT, not in this architectural patch.

The next biomarker-related BATCH_COMMITs must:
1. propose new candidates via COMMIT_CANDIDATE
2. fill in the complete template
3. assign a scorecard
4. declare evidence status
5. update sections 9 and 10 of this file

---

## 9. SHORTLIST (operational output)

> **Currently empty.** To be populated when at least 2–4 Tier 1 candidates reach score ≥ 30 and are ready for an external-validation proposal.

Expected format:
```
1. BC-NNN — [Name] — Score: NN/39 — Tissue: [...]
2. ...
```

---

## 10. KNOWLEDGE MAP (knowledge output)

> **Currently empty.** To be built progressively as the reasoned map of candidates, independently of reaching the shortlist.

Expected structure:
- pathway-organized view of candidates
- discussion of Tier 1 vs Tier 2
- gap analysis (what is needed to validate)

---

## 11. CHANGE LOG (this file)

| Date | Event | Batch ID |
|---|---|---|
| — | File created at v3.3.1 — structure only, no candidates populated | Patch 2 |

---

## 12. WIKILINKS

- Research line: [[research_lines_current#RL-BIOM-001 — WWOX functional-state biomarkers]]
- Sister file: [[clinical_monitoring_endpoints_current]]
- Framework: [[LEGEND_CORE]]
- State manifest: [[state_manifest_current]]

---

**End of `biomarker_candidates_current.md`**

> Central discipline: no candidate is a validated WWOX biomarker. All are prudent inferences. Promotion requires direct formal-validation evidence, never inference.
