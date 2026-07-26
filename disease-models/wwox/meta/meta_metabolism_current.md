# META — Metabolism / HIF1A / AMPK
**Version:** v1.1
**Status:** emerging → consolidating (expanded)
**Last update:** 2026-04-17 — Commit 181–220: metabolic branch expanded beyond Warburg-only; WWOX/HIF1A ratio as systems-level state marker; trafficking–metabolism coupling node added

---

## Scope
The metabolic role of WWOX, glycolytic shift, HIF1A/AMPK regulation, energetic vulnerability in the WWOX LoF context. Focus on CNS relevance and mechanistically useful pathways.

---

## Evidence Base

### Core papers (corpus 1–180)
- Paper 2 (PMID 36271927) — Baryła 2022 review: WWOX e metabolic regulation (comprehensive)
- Paper 39 (PMID 30755385) — Abu-Remaileh 2019 Mol Metab: WWOX somatic ablation in skeletal muscle → glucose intolerance + AMPK impairment + HIF1α accumulation
- Paper 64 (PMID 35328751) — Baryła 2022 IJMS: WWOX/HIF1A axis downregulation → altered glucose metabolism
- Paper 78 (PMID 27308416) — Abu-Remaileh 2014 commentary: WWOX loss activates aerobic glycolysis
- Paper 144 (PMID 25012504) — Abu-Remaileh 2014 CDD: WWOX regulates glucose metabolism via HIF1α modulation
- Paper 125 (PMID 26390919) — Choo 2015: WWOX moderates mitochondrial respiratory complex (Drosophila)
- Paper 23 (PMID 25595186) — Richards 2015: WWOX role in metabolism and cancer
- Paper 20 (PMID 24932569) — Aldaz 2014: WWOX at crossroads of cancer, metabolic syndrome, CNS

### Supporting
- Baryła 2022 (LIT-002 / PAPER 002) — metabolic/redox framework
- Baryła 2025 (LIT-0019) — WWOX/HIF1A ratio in cancers; WWOX sequesters HIF1A in the cytoplasm
- Chong 2023 (LIT-0017 / PAPER 017) — mildly elevated lactate in a null/null case → small human clinical signal

---

## Core Findings (DATO)

- WWOX sequesters HIF1α in the cytoplasm via the WW domain; WWOX loss → free HIF1α → upregulation of glycolytic genes
- WWOX loss → shift toward aerobic glycolysis (Warburg-like effect) in cell and animal models
- WWOX physically interacts with AMPK; WWOX loss → impaired AMPK activation
- In WWOX-specific muscle mouse models: reduced slow-twitch fiber, reduced mitochondrial content, reduced glucose oxidation
- In cell models: WWOX loss → increased glucose uptake + reduced mitochondrial respiration
- WWOX-specific human metabolic signal: mildly elevated lactate in a null/null WOREE patient (Chong 2023) — a very small but human datum
- In Drosophila: WWOX modulates the mitochondrial respiratory complex; WWOX alteration → reduced response to mitochondrial metabolic stress

---

## Integrated Model (INFERENZA)

```
WWOX loss
→ free HIF1α in the nucleus
→ upregulation of glycolytic genes (GLUT1, PDK1, LDH)
→ shift from OXPHOS to glycolysis
→ increased ROS / redox stress
→ reduced mitochondrial energy efficiency
→ neuronal vulnerability (energy-dependent CNS)

+ impaired AMPK → altered metabolic stress response
+ possible lactate accumulation in severe scenarios
```

---

## Pathway Mapping

- P5 — metabolism / mitochondria / redox / mitophagy (core)
- P1 — network dysregulation (indirect output: energetically vulnerable neurons)
- P4 — myelination (overlap: high-energy-demand oligodendrocytes)

---

## Claim Impact

### Strengthened
- CLAIM 009: WWOX deficiency plausibly alters mitochondrial quality control, redox and energy efficiency (in observation → supporto crescente)

### Critical limit
- CLAIM 009 remains INFERENCE: the direct link between the WWOX/HIF1A axis and human pediatric CNS neurons is not yet directly demonstrated
- The strong models are muscle, liver, Drosophila — not direct pediatric CNS WWOX-LoF
- The human signal (Chong 2023 lactate) is very small (1 patient, null/null)

---

## Research Lines

### RL-003 — WWOX as bioenergetic governor (AMPK–HIF1A–mitochondria)
- Status: high-priority consolidating
- Supported by papers 39, 64, 144, 2

### RL-005 — Metabolic vulnerability in CNS WWOX-LoF
- Status: emerging
- To develop: CNS-specific models, not only peripheral

---

## Case-level relevance

### What it supports
- Conceptual rationale for KD (reduces glycolytic substrate, favors OXPHOS)
- Conceptual rationale for CoQ10, creatine (mitochondrial support)
- Possible lactate monitoring as an indirect biomarker
- HIF1A/Warburg framework as a plausible amplification mechanism

### What it does NOT imply
- Does not authorize an immediate strategy change
- Not directly demonstrated in the human pediatric WWOX-LoF CNS
- The human signal is too small for an operational claim

### Genotype note
- A compound-heterozygous case (N/M) is expected to retain partial residual function
- The degree of metabolic shift may be smaller than in null/null models
- Caution in automatically transferring muscle/liver data to the CNS

---

## Open Questions

- How relevant is the metabolic axis in the WWOX-LoF CNS relative to network dysfunction?
- Is there a measurable metabolic biomarker (lactate, pyruvate, acylcarnitine)?
- Is metabolism a driver or an amplifier in the pediatric CNS context?
- Connection between glycolytic shift and myelin vulnerability?

---

---

## Meta update — Commit 181–220: WWOX metabolism is broader than Warburg-only logic

The metabolism branch should no longer be summarized as a narrow WWOX–HIF1A–glycolysis axis. The literature now supports a broader interpretation in which:

- the **WWOX/HIF1A ratio** functions as a systems-level indicator of maladaptive state rather than a simple two-gene relationship (paper 191; CLAIM 025);
- low WWOX / high HIF1A states are associated not only with glycolytic activation but also with inflammatory and Wnt-related components;
- WWOX-related metabolic dysregulation may involve a **trafficking–metabolism interface**, supported by interactome data linking WWOX to ER/Golgi/endosomal/lysosomal systems and catabolic pathways converging on **Acetyl-CoA** (paper 182; CLAIM 026).

### Practical interpretation
This branch should be read as:
- glycolytic tilt
- altered glucose transport logic
- metabolic-state dysregulation
- inflammatory-metabolic coupling
- possible compartmental/endomembrane contribution to metabolic failure

### Evidence weight
- Human non-tumoral support (WWOX/HIF1A ratio): strong
- Translational systems-level support (interactome/pathway): strong

### Nuance — HIF1α-independent axis (Obeid 2026 review / Lucas-Clarke 2025) [in observation]
A Drosophila model shows a WWOX metabolic effect that is **HIF1α-INDEPENDENT** (lactate↑/Ldh↑ via **ATF4/UPR**; neuroprotection via **methionine suppression, not lactate**). This tempers the HIF1A-centric reading: the metabolic branch is broader than a WWOX–HIF1A axis. Not a direct contradiction (different system) → a tension to reconcile. Primary queued FT-009; CLAIM 025 annotated accordingly.
- Direct CNS transferability: not yet proven

### Status update
- **RL-003** (WWOX as bioenergetic governor) remains high-priority consolidating
- **CLAIM 009** continues as INFERENZA in observation — no promotion yet
- **CLAIM 025** and **CLAIM 026** added as mechanistic enrichments; do not override CLAIM 009 limits

**Version update:** v1.1 — 2026-04-17
