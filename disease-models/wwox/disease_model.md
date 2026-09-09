# WWOX-DEE — Disease Model & Decision Framework

> **Public, de-identified disease-level model.** Derived from the LEGEND working model with the individual clinical record removed (clinical presentation, treatment regimen, and case-specific surveillance are not included). What remains is the disease-level mechanistic synthesis, the genotype-interpretation rules, the literature-anchored data, and the decision-logic framework — all from public literature. **Not medical advice.** Specific variants appear only as decoupled public worked examples — a destabilizing SDR missense on one side, a canonical splice-acceptor variant on the other — never assembled into one person's genotype.

**Model version lineage:** v3.0 (2026-07-14) — a MAJOR baseline reversal (see the repair changelog at the end) illustrating the epistemic discipline in action.

---

## Genotype interpretation rules (method)

- p.Gln230Pro (Q230P) ≠ P47T — do not auto-transfer P47T data across variants.
- Compound heterozygous ≠ null/null — a milder organoid phenotype is expected than in full KO.
- WWOX variants are **not interchangeable**; extrapolation from full-KO models requires explicit caution.
- Q230P (SDR domain): in homozygous fibroblasts of the exact variant, transcript is normal and protein is not detected. The cause remains unresolved — impaired translation, insolubility, or premature degradation. The HSC70/lysosome read-across from P252A is a **bridge hypothesis**, not a demonstrated mechanism for Q230P.
- Genotype class (Gao 2025 framework): an N/M combination (missense + null-predicted splice) sits outside the highest-risk N/N subgroup — but this never authorizes reduced clinical vigilance.

---

## Mechanistic architecture (disease-level)

**Network hyperexcitability.** WWOX-related encephalopathy should not be modeled only as a "seizure disorder" or as a downstream consequence of developmental damage. Evidence supports a **primary disturbance of neocortical network stability**: spontaneous bursting, altered oscillatory organization, increased phase-amplitude coupling, reduced spontaneous inhibition, increased excitatory drive, depolarization, increased firing, rebound-prone physiology. This elevates network-state pathology to core-pathway status. *(CLAIM 021 / Breton 2021.)*

**Prenatal developmental architecture.** In severe null genotypes, onset may begin prenatally, with detectable fetal brain abnormalities. Severe WWOX disease should not be read as purely postnatal epileptic deterioration; a developmental architecture failure may already be active in utero, especially in null-severe presentations. *(CLAIM 022 / paper 216.)*

**WWOX as routing/scaffold protein.** Beyond tumor suppressor / metabolic regulator, WWOX is a routing/scaffold protein that can change partner localization and redirect biological output. Relocalization of p73 is the anchor example: the same protein produces different output depending on where WWOX routes it. *(CLAIM 023 / PAPER 081, PMID 15070730.)* — **Narrowed in `BATCH_20260909_001`:** the word *phosphorylation-sensitive* and the phrase *Tyr33-dependent* are removed, because the primary source tests no relation between phosphorylation and localisation (20 body sentences mention Src; zero also mention localisation). Tyr33 phosphorylation regulates the **binding**, which is unaffected.

**Domain cooperativity.** WW-domain biology depends on WW1–WW2 tandem cooperativity; variant interpretation should consider tandem stability, partner-recognition geometry, and residual interaction architecture — not isolated single-domain logic. *(CLAIM 024 / paper 204.)*

**Metabolic branch.** Beyond a simple HIF1A/Warburg framing, the WWOX/HIF1A axis appears to be a broader state indicator linked to glycolysis, inflammatory tone, Wnt-related signaling, and possibly state-transition biology; interactome data suggest a trafficking–metabolism interface (ER/Golgi/endosomal/lysosomal) with Acetyl-CoA-centered catabolic convergence. *(CLAIM 025 / paper 191; CLAIM 026 / Hussain 2018.)*

> **Integrity exclusion (a worked example of source-integrity discipline):** the HGF/Met–TAZ–WWOX bone-metastasis line does **not** count as independent corroboration — the primary (PMID 28151481) was retracted in 2022 for western-blot control manipulation/reuse, and a review (PMID 28045433) reuses its data/dependencies. The WWOX/HIF1α axis stands only on the independent sources. No baseline claim depended on the invalidated line.

**Research-facing (not yet core).** HYAL-2 / HA / SMAD4 / WWOX — a high-value ECM/membrane-to-nucleus and injury-response branch, retained but not promoted. *(CLAIM 027 / paper 214.)*

**Cross-pathway interpretive principle.** WWOX output is strongly partner- and context-dependent. Expression level alone is insufficient to infer uniform functional benefit — **"more WWOX = better" is not a safe default** across contexts. *(CLAIM 028 / papers 213, 218, 206, 214.)* WWOX may also contribute to ATM-linked DNA-damage-response competence and genome-stability maintenance — a plausible structural-vulnerability branch. *(CLAIM 029 / Abu-Odeh 2014.)*

---

## Literature-anchored data (DATO — WWOX literature)

- VABAM documented in WWOX-DEE with vigabatrin (Choi 2026) — a real safety signal; conflicting with You 2024 (seizure reduction, no documented VABAM).
- Network hyperexcitability + AAV-WWOX rescue in organoids (Steinberg 2024).
- Non-cell-autonomous hypomyelination in neuronal WWOX deletion (Repudi 2021).
- N/N genotype → higher risk of seizures, hypertonia, respiratory complications vs N/M and M/M (Gao 2025, n=50).
- AAV9-hSynI-hWWOX: dose-dependent durable rescue in a Wwox-null murine model, including ECoG/SWD reduction (Obeid 2026).
- Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023).

### Inferences (INFERENZA)
- Ca²⁺ / network dysregulation as a primary driver of hyperexcitability — plausible, supported.
- Hypomyelination as a possible amplifier — needs imaging confirmation.
- Neuroinflammation as a low-noise modifier, partly downstream of network dysfunction (neuron-specific rescue reduces gliosis).
- Q230P functional endpoint: normal transcript, protein not detected; synthesis/translation vs premature degradation unresolved; residual function cannot be inferred from abundance alone.
- Part of the WWOX-DEE phenotype plausibly grafts onto a prenatal cortical-assembly substrate (defective layering, incomplete maturation, downstream myelin/glial failure), strengthening the interpretive weight of EEG over early MRI.
- GABA remains an axis in tension: GABAergic vulnerability is probable but not reducible to a simple linear deficit.

---

## Decision-logic framework (disease-level; not medical advice)

*These are disease-level management-reasoning principles synthesized from the literature for WWOX-DEE, to support — never replace — a treating clinical team.*

**Active pathways.**
- *Ca²⁺ / network dysregulation* — network stabilization is the operative target; change one variable at a time, protecting readability of any active titration/trial window.
- *GABAergic vulnerability (SAFETY)* — vigabatrin: strong caution / avoid unless alternatives are exhausted (conflicting evidence: efficacy on spasms vs VABAM risk); phenobarbital: caution; benzodiazepines: appropriate as rescue, chronic high-dose only if essential.

**Surveillance.**
- *Myelination / white matter* — MRI + DTI as a structured baseline; myelination adjuncts only if imaging is suggestive, one variable at a time.
- *Respiratory / dysphagia* — structurally associated with WWOX-DEE (more severe in N/N, present across genotypes); monitor aspiration/dysphagia/respiratory distress during intercurrent infections. EEG remains more sensitive than early MRI for network severity (Sapuppo 2026).
- *Ophthalmology* — visual impairment reported in 4/5 WOREE patients even with non-uniform imaging (Chong 2023); structured evaluation indicated.

**Red flags — when NOT to change anything.** Infection/fever/dehydration; vomiting/diarrhea/reduced intake/unstable ketones; active AED change or titration; multiple new supplements at once; drastic sleep worsening without clear cause.

**Flowchart logic.** (1) Baseline stable? if no → introduce no variables. (2) Minimum dataset (EEG, MRI, genetics)? if no → prioritize. (3) MRI/DTI hypomyelination? if yes → discuss a myelination adjunct (one variable). (4) Strong GABAergics? apply strong caution (VABAM). (5) Focus: network stabilization. (6) Follow-up: N-of-1 endpoints (startle/sleep/EEG). (7) Maintain gene-therapy trial-ready documentation at all times.
**Principles:** don't force decisions; order timing; separate safety from drivers and structural surveillance; prevent multi-variable changes during titration/trial phases.

**Monitoring endpoints (N-of-1 method).** Startle (0–3 score + daily count + triggers); sleep (awakenings/night + wake/sleep differentiation); feeding/posture (events during transitions); EEG (epileptiform density + background organization — prioritized over seizure count alone).

---

## Gene therapy context (public / preclinical)

- A clinical AAV9-WWOX programme is anticipated (2025–2027).
- Steinberg 2024 organoids: AAV9-WWOX normalizes Ca²⁺ transients and hyperexcitability; MYC overexpression identified as a key mechanism.
- Obeid 2026 (Wwox-null murine): AAV9-hSynI-hWWOX — dose-dependent durable rescue (survival, glucose, behavior, myelination, gliosis, SWD/ECoG); neuron-specific targeting; early postnatal ICV delivery.
- **Design principles:** human synapsin promoter (neuron-specific); WPRE removed (avoid overexpression); dose controlled; critical early postnatal window (P0–P5 in mouse).
- **Safety caveat:** DRG / peripheral-organ dose-limiting toxicity at high systemic AAV dose → favors targeted/controlled delivery (a pediatric regulatory concern).
- **Epigenetic option (future / extension):** dCas9/CRISPRa upregulation of endogenous WWOX for **hypomorphic** states — potentially relevant to residual-function missense alleles; not actionable now.
- **First-in-human (background/observation):** a WWOX gene therapy reported given to an infant with WWOX epilepsy (ICV) — the strongest external signal for the GT axis; awaiting peer-reviewed clinical data. NOT a datum.
- Partial restoration may be sufficient (genotype–phenotype suggests haploinsufficiency is tolerated) — which **lowers the therapeutic threshold**.

---

## Claim registry summary (baseline mirror)

Full canonical status lives in [`registries/claim_registry_current.md`](registries/claim_registry_current.md). Key disease-level claims (ID · title · type · status):

- 001 Vigabatrin → VABAM in WWOX-DEE · DATO · **conflicting evidence**
- 002 WWOX-LoF → hyperexcitability + AAV rescue in organoids · DATO+INF · consolidated
- 003 Neuronal WWOX deletion → non-cell-autonomous hypomyelination · DATO · consolidated
- 004 AAV9-WWOX neuron-targeted multi-domain in-vivo rescue · DATO · consolidated
- 011 AAV9-hSynI-hWWOX dose-dependent durable rescue · DATO(preclinical) · consolidated
- 014/015 Prenatal cortical development perturbation / misassembled substrate · DATO/INF · consolidated
- 019 Q230P in severe compound-het disease; allele-specific interpretation required · DATO+INF · consolidated
- 028 WWOX output partner/context-dependent; expression ≠ uniform benefit · INFERENZA · flagged for review
- 030 Severity tracks residual **function**, not protein abundance · in observation
- 031 It is a **DEE, not an EE**: seizure control does not save development · in observation
- 032 Haploinsufficiency is tolerated: the therapeutic threshold is well below full restoration · in observation

---

## Repair changelog (the epistemic discipline in action)

**WM v2.1 → v3.0 (2026-07-14) — MAJOR baseline reversal.** Withdrew the equation `normal mRNA + absent protein = post-translational degradation`. Johannsen 2018 explicitly states two alternatives: impaired translation **or** premature degradation. Consequences: CLAIM 019 keeps the human datum on the exact variant but downgrades the cause to unresolved; CMA, `LRSVQ`, and the helix-lid model remain hypotheses transferred from P252A/AlphaFold, **not** a demonstrated Q230P mechanism; C299R withdrawn as a validated catalytic/off-lid control; the first experimental gate separates synthesis, insolubility, and turnover, with abundance and function measured together; an SDR stabilizer is `conditional / not design-ready`.

*(This reversal — retracting a plausible, already-consolidated conclusion the moment the evidence no longer uniquely supported it — is a worked example of the [false-negative/premise discipline](../../framework/instruction/epistemic_discipline.md).)*
