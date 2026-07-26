# META INDEX — Knowledge Layer
**Version:** v1.3
**Baseline:** Bootstrap v1.0
**Last update:** 2026-07-25 — `BATCH_20260725_001`: public traceability repair 213→207 for CLAIM 028 and public-edition registry note corrected. No scientific synthesis changed. Prev: lint sync aligned the index to Commit 181–220 and Phase 1 triage 221–400.

> ✅ STATUS: index aligned; all 5 active metas propagated to Commit 181–220. Metas 6/7/8 still to be created.

> **Public edition.** Disease-level syntheses from public literature. Paper/claim numbers reference the public canonical registries shipped in `disease-models/wwox/registries/`.

## Purpose
This file is the central index of the Meta-Analysis Layer.

It serves to:
- track all active meta-analyses
- see the state of each axis
- orient research and updates
- avoid duplication
- identify gaps and priorities

LEGEND must read it at the start of every STANDARD or FULL session.

---

# Active meta-analyses

## 1. Network / Myelin / Glia
- File: meta_network_myelin_glia_current.md
- Status: consolidating
- Pathway: P1, P4, P6
- Synthesis: WWOX loss → network instability + impaired oligodendrocyte maturation → hypomyelination → conduction deficit
- Key corpus papers: 87, 97, 163, 48, 3, 4, 7, 13, 210
- Priority: high
- Notes: central axis of the model; neuronal hub confirmed by neuronal-specific rescue (Repudi 2021 EMBO, Obeid 2026)

---

## 2. Metabolism / HIF1A / AMPK
- File: meta_metabolism_current.md
- Status: emerging → consolidating
- Pathway: P5
- Synthesis: WWOX loss → glycolytic shift + redox stress → neuronal vulnerability
- Key corpus papers: 2, 39, 64, 78, 144, 125, 23
- Priority: medium-high
- Notes: growing axis; WWOX/HIF1A/AMPK confirmed in muscle and liver models; CNS applicability still indirect

---

## 3. Prenatal Structure / Migration / GSK3β
- File: meta_prenatal_structure_current.md
- Status: consolidating / major structural axis
- Pathway: P3, P4, GSK3β
- Synthesis: WWOX loss → cytoskeleton/migration defects → cortical misassembly → hypomyelination → seizure vulnerability
- Key corpus papers: 97, 93, 163, 87, 106
- Priority: very high
- Notes: one of the major model shifts; GSK3β tracked as an emerging node (paper 93: lithium abolishes PTZ-induced seizures in Wwox-/-)

---

## 4. Human Spectrum / Natural History
- File: meta_human_spectrum_current.md
- Status: consolidating
- Pathway: cross-cutting
- Synthesis: WWOX disease = a genotype-dependent spectrum with non-monolithic trajectories
- Key corpus papers: 30, 36, 59, 114, 118, 151, 166, 175, 180, 96, 60, 90
- Priority: high
- Notes: includes long survival (paper 180); KD signal (paper 118); exon 6/Q230P logic (paper 151); missense vs null survival (paper 30)

---

## 5. GABA / GABA Paradox / Strategy Space
- File: meta_gaba_paradox_current.md
- Status: emerging high-value / high-uncertainty
- Pathway: P2 (core), P1, P3
- Synthesis: non-linear GABAergic dysfunction, likely developmental and function-dependent → network instability
- Key corpus papers: 85, 87, 53, 3, 210, 207
- Priority: maximum
- Notes: the most complex and strategic axis; data in tension between models (mouse KO → ↓ GABAergic interneurons; organoid KO → ↑ GABAergic markers); requires continuous integration

---

# Meta-analyses in development

## 6. Neuroinflammation / Glia Progression
- File: to be created → meta_neuroinflammation_current.md
- Status: emerging
- Pathway: P6
- Priority: medium
- Notes: strong in partial LoF (P47T, papers 53 and 110); a possible progression pathway; gliosis as downstream of neuronal dysfunction (Obeid 2026)

---

## 7. Gene Therapy / Rescue
- File: to be created → meta_gene_therapy_current.md
- Status: emerging
- Pathway: P7
- Priority: medium
- Notes: relevant for the future; design principles defined (Repudi 2021 EMBO, Obeid 2026); not for immediate decisions

---

## 8. Cerebellar Axis
- File: to be created → meta_cerebellar_axis_current.md
- Status: emerging → consolidating
- Pathway: P3/P4
- Priority: medium-high
- Notes: Purkinje loss, vermis defects, ataxia, degeneration (papers 53, 93); to be better separated from the general cluster

---

# Overall system state

## Most solid axes
- Network + myelin (meta 1)
- Prenatal structure (meta 3)
- Human spectrum (meta 4)

## High strategic-priority axes
- GABA paradox (meta 5) — maximum priority
- Metabolism (meta 2)

## Emerging axes
- GSK3β (included in meta 3)
- Neuroinflammation (meta 6 — to be created)
- Cerebellar axis (meta 8 — to be created)

## Axes in tension
- GABA (non-linear interpretation — meta 5)
- primary vs secondary role of glia
- centrality of metabolism in the human WWOX CNS

---

# Identified gaps

- lack of direct data on functional GABA (not just markers)
- absence of WWOX-specific data on NKCC1/KCC2
- need to better connect: metabolism ↔ network; GABA ↔ prenatal structure
- few complete longitudinal human datasets
- missing full texts on key corpus papers (93, 97, 151 prioritized)
- metas 6, 7, 8 still to be formally created

---

# Full-text priorities

## High priority
- paper 93 (GSK3β, myelin, PNS, cortical malformations)
- paper 97 (migration, cortical layering, cytoskeleton)
- paper 151 (splice vs compound phenotype, Q230P context)

## Medium
- paper 163 (rat model, cortex, hypomyelination — partially integrated)
- paper 20 (WWOX crossroads CNS + metabolic)

## Already covered or sufficiently integrated
- paper 30 (Oliver 2023 — full text PMC available)
- paper 36 (Gao 2025 — full text available)
- paper 48 (Repudi 2021 EMBO — integrated)
- paper 87 (Repudi 2021 Brain — integrated)
- paper 118 (Chong 2023 — partial)
- paper 180 (Teplyshova 2024 — full text PMC)

---

# Commit 181–220 propagation status
*(reflects CLAIM 021–029 and papers 181–220)*

## Claims generated by batch 181–220 and their target meta
- CLAIM 021 (paper 210) — neocortical network hyperexcitability → **meta 1 (network/myelin/glia)**
- CLAIM 022 (paper 216) — prenatal null-severe onset → **meta 3 (prenatal structure)** — ✅ propagated
- CLAIM 023 (paper 206) — WWOX–p73 routing/scaffold → cross-cutting architectural principle
- CLAIM 024 (paper 204) — WW1–WW2 tandem cooperativity → genotype-interpretation framework
- CLAIM 025 (paper 191) — WWOX/HIF1A ratio state marker → **meta 2 (metabolism)** — ✅ propagated
- CLAIM 026 (paper 182) — trafficking–metabolism coupling node → **meta 2 (metabolism)** — ✅ propagated
- CLAIM 027 (paper 214) — HYAL-2/SMAD4 ECM signaling → research-facing (meta 6 candidate)
- CLAIM 028 — context-dependence principle → cross-cutting — traceability pointer resolved 213→207 by `BATCH_20260725_001`
- CLAIM 029 (paper 138) — ATM/DDR competence → research-candidate (RC-012)

## Metas updated by commit 181–220
- ✅ meta_metabolism_current.md → v1.1
- ✅ meta_human_spectrum_current.md → v1.1
- ✅ meta_prenatal_structure_current.md → v1.1

## Metas propagated by the lint (gap closed)
- ✅ meta_network_myelin_glia_current.md → v1.1. CLAIM 021 (network-state pathology core) integrated.
- ✅ meta_gaba_paradox_current.md → v1.1. CLAIM 021 (functional inhibitory deficit) + CLAIM 028 (marker ≠ function) integrated.

## Traceability repair (resolved 2026-07-25)
- `BATCH_20260725_001`, manually authorized after a cross-file audit, normalized CLAIM 028 to **papers 207, 218, 206, 214**. CORPUS P207 and the tracking log both map 207 to CLAIM 028; no P213 record exists. This repairs provenance only and does not change the claim's scientific interpretation or status.

---

# Operating rules

## Updating a meta
A meta-analysis is updated when:
- new papers modify the interpretation
- convergences emerge
- relevant tensions emerge

## Creating a new meta
Create a new meta when:
- ≥3 coherent papers
- a new axis emerges
- there is an impact on the global model

---

# Next actions

## Priority 1
Use meta_gaba_paradox_current as a lens for the next papers

## Priority 2
Full-text extraction: papers 93, 97, 151

## Priority 3
Formalize the Research Layer: research_lines_current, research_candidates_current, full_text_queue_current

## Priority 4
Create metas 6 (neuroinflammation), 7 (gene therapy), 8 (cerebellar axis)

## Priority 5
Next batch: papers 181–270 with Meta-Layer-guided triage

---

# Final note

This file represents the current state of LEGEND's cumulative knowledge after Commit 181–220 (CLAIM 021–029) and Phase 1 triage 221–400.

It must be:
- updated after every STANDARD or FULL session that touches the Meta Layer
- read at the start of every RUN
- used to guide priorities and interpretation
