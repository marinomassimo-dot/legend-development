# META — Network / Myelin / Glia
**Version:** v1.1
**Status:** consolidating → network-state pathology promoted to core
**Last update:** 2026-06-09 — Commit 181–220 propagation: CLAIM 021 integrated (paper 210, neocortical network-state pathology).

---

## Scope
The relationship between WWOX-dependent neuronal dysfunction, network hyperexcitability, myelination and glia in the WWOX LoF context.

---

## Evidence Base

### Core papers (corpus 1–180)
- Paper 87 (PMID 33914858) — Repudi 2021 Brain: neuronal Wwox deletion → epilepsy + myelin defects
- Paper 48 (PMID 34747138) — Repudi 2021 EMBO: neonatal AAV9-SynI-WWOX → rescue Wwox-null
- Paper 97 (PMID 32581702) — Iacomino 2020: loss of Wwox → impaired neuronal migration + cortical layering
- Paper 163 (PMID 31340538) — rat lde/lde: cerebral cortex hypomyelination
- Paper 93 (PMID 32000863) — Cheng 2020: Wwox-/- → neurodevelopmental + degenerative neuropathies + GSK3β
- Paper 3 (PMID 34831305) — Steinberg/Aqeilan 2021 review: models overview
- Paper 4 (PMID 33255508) — Aldaz/Hussain 2020: WWOX LoF in neurodevelopmental/neurodegenerative disorders
- Paper 13 (PMID 33916893) — Banne 2021: comprehensive overview WWOX germline mutations

### Supporting
- Repudi 2021 Brain (LIT-004 / PAPER 004) — neuronal deletion → non-cell-autonomous hypomyelination
- Repudi 2021 EMBO (LIT-005 / PAPER 005) — AAV9-WWOX rescue multi-domain
- Obeid 2026 bioRxiv (LIT-0011 / PAPER 011) — AAV9-hSynI-hWWOX: dose-dependent durable rescue
- Steinberg 2024 organoids (LIT-001 / PAPER 001) — hyperexcitability + Ca²⁺ dynamics + MYC

### Deep-dive 181–220 (Commit 181–220)
- Paper 210 → CLAIM 021: neuron-specific Wwox loss destabilizes neocortical network physiology via combined synaptic + intrinsic mechanisms

---

## Core Findings (DATO)

- WWOX is preferentially expressed in neurons; neuron-specific deletion is sufficient to replicate the null phenotype (Brain 2021)
- WWOX neuronal loss → hyperexcitability and seizures (network-level)
- WWOX neuronal loss → reduced oligodendrocyte maturation → non-cell-autonomous hypomyelination
- Reduced myelinated axons → conduction deficit
- Peripheral involvement too (Schwann cell apoptosis in Wwox-/-, paper 93)
- Gliosis (astro-microgliosis) reduced after neuron-specific rescue → part of P6 is downstream of neuronal dysfunction, not a primary autonomous glial process (Obeid 2026)
- AAV9-hSynI-hWWOX: rescue dose-dependent e durevole su survival, ECoG/SWD, myelination, gliosis (Obeid 2026)
- In human WWOX-KO organoids: Ca²⁺ dysregulation + hyperexcitability + MYC upregulation (Steinberg 2024)

**Network-state pathology as a primary level (CLAIM 021 / paper 210)**
- Wwox neuron-specific loss → spontaneous neocortical bursting, altered oscillatory organization, increased phase-amplitude coupling
- Layer 2/3 pyramidal neurons: increased excitatory drive, **reduced spontaneous inhibition**, depolarization, increased firing, increased sag and post-inhibitory rebound
- Bursting depends on NMDAR activity and gap junctions
- Reading: network dysfunction is (at least partly) **primary**, not just secondary seizures or downstream developmental damage → network-state pathology rises to core-pathway status (overlap with the GABA axis: see meta_gaba_paradox, functional inhibitory deficit)

---

## Integrated Model (INFERENZA)

```
WWOX neuronal loss
→ network instability (Ca²⁺ dysregulation, hyperexcitability)
→ impaired oligodendrocyte maturation (non-cell-autonomous)
→ hypomyelination
→ conduction deficit
→ amplification of network instability

+ gliosis as a downstream response (not a universal primary driver)
+ peripheral involvement in severe models
```

---

## Pathway Mapping

- P1 — Ca²⁺ / network dysregulation (core)
- P4 — myelination / white matter (central)
- P6 — glia / neuroinflammation (downstream, non primario)
- P7 — gene therapy readiness (rescue design principles)

---

## Claim Impact

### Strengthened
- CLAIM 002: WWOX-LoF → hyperexcitability + AAV rescue (Steinberg 2024 organoids)
- CLAIM 003: neuronal WWOX deletion → non-cell-autonomous hypomyelination (Repudi 2021 Brain)
- CLAIM 004: AAV9-WWOX neuron-targeted rescue multi-domain (Repudi 2021 EMBO)
- CLAIM 011: AAV9-hSynI-hWWOX dose-dependent durable rescue (Obeid 2026)

### Integrated (Commit 181–220)
- CLAIM 021: WWOX loss destabilizes neocortical network physiology via combined synaptic + intrinsic mechanisms (paper 210 = Breton et al. 2021) — elevates network-state pathology to core-pathway; supports reading a disorganized EEG as primary network-state dysfunction, not only secondary epileptiform activity.

### Integrated (Obeid 2026 review)
- **Dual myelin mechanism**: beyond the neuronal non-cell-autonomous one (CLAIM 003, Repudi 2021), Abudiab 2025 (cuprizone / SOX10) shows a **cell-autonomous oligodendroglial** role of WWOX in OL differentiation and remyelination, emerging under stress/remyelination. The two mechanisms integrate, not exclude. Primary queued (FT-007). [in observation — review-sourced]

### Rescaled
- P6 as a universal primary driver → now read as amplifier/downstream in severe-LoF scenarios

---

## Research Lines

### RL-001 — Neuronal hub → hyperexcitability + myelination failure
- Status: central / consolidating
- The most solid line in the system

### RL-009 — Developmental glial maturation / myelin assembly failure
- Status: emerging
- Glia as a secondary but real actor in progression

---

## Case-level relevance

### What it changes
- Supports an integrated network + myelin reading as a single system
- Strengthens the MRI + DTI baseline rationale
- Supports gene therapy as the single multi-pathway causal intervention
- Strengthens the trial-readiness rationale

### What it does NOT change
- A compound-heterozygous genotype (N/M) ≠ the full KO of mouse models
- Does not authorize direct transfer of rescue data from null/null models to a compound-heterozygous case
- Partial residual function expected in a compound-heterozygous case → a rescue effect is plausible even with partial restoration

---

## Open Questions

- Precise causal direction between network dysfunction and myelin failure: sequential or parallel?
- Primary vs secondary role of glia in N/M (partial LoF) contexts
- What threshold of WWOX restoration is sufficient for myelin rescue?
- Optimal intervention timing to maximize myelin rescue

---

## Next Actions

- Integrate with meta_prenatal_structure (migration + myelin overlap)
- Deep-dive paper 93 full text for GSK3β data and peripheral conduction
- Monitor gene-therapy literature for design-principle updates
