# Working Model Current

## WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model

**Version:** WM_v7.6_2026-09-28
**Date baseline:** 2026-03-28
**Last update:** 2026-09-28 — `BATCH_20260928_007` (**MINOR** — MANUAL, under the operator's standing instruction *«procedi sempre»*, ACTOR_ID `orchestrator`): the commit-candidate backlog, residue by residue. Every residue was re-derived against `main` `7352d52`, and every op was verified by the batch actor against the source bytes after a different reader produced it; four new receipts, two blind locator audits. 🔴 **`CLAIM 011` corrects an order-of-magnitude error:** the WPRE dose-equivalence it carried as *≈44×* is **>4.4×** (S3F pairs `6E10` against `2.63E11` vg; a qualitative lower bound from images), and its S3E per-region multipliers (3.0 / 3.0 / 5.5 / 16.7) are now **printed numerals on a fingerprinted supplement**, no longer a declared attestation. 🔴 **`CLAIM 025`**: the per-subtype directions are checked against Supplementary Tables S4–S8 — the non-invariance holds at table level, but Table S7's HR column contradicts its own «more favourable» labels for HER2-enriched and Luminal B, so no inference may rest on a single subtype's sign; the `PREMISE_TAG` is narrowed to *invariant* direction. **`CLAIM 026`** gains an evidence boundary refusing to read the ER protein-processing enrichment as trafficking support (as corrected by a blind audit: tiers named by threshold, the contaminant-frequency ground limited to the four members it holds for, one unsourced sentence dropped). **`CLAIM 016`** stops asserting that total GSK3β abundance is unchanged in the Wang system (`NOT_ASSERTED`). Paper registry: `PAPER 118` discharges its S4–S8 debt; `PAPER 025`'s note is re-sourced on the restored PDF and records two source-internal conflicts; `CORPUS P337` (Gourley 2005) is completed on a new complete-reading receipt. No claim `Status`, `Type`, `Transferability`, clinical relevance or BLOCCO 1 field moved; no record added or removed; the live sections of this file carry no sentence the batch corrects.

> **Public edition — de-identified.** This is the **canonical, complete** disease-level working model: the fourth Layer-2 "current" file, the one the LINT engine requires alongside the claim / paper / literature registries. It carries the full claim mirror, the full version changelog and the full mechanistic architecture.
> [`../disease_model.md`](../disease_model.md) is the **narrative reader-facing view** of the same model — shorter, prose-first, meant to be read top-to-bottom. Where the two differ in completeness, **this file is canonical**.
> All individual-linking material has been removed: no identified individual, no personal clinical presentation, no treatment schedule, no doses, no case-specific surveillance plan, no family-relationship data. Specific variants appear only as decoupled public worked examples drawn from the published literature, never assembled into one person's genotype. **Not medical advice.**

---

## Disease identity

- **Condition:** WWOX loss-of-function developmental and epileptic encephalopathy — WOREE spectrum (severe, biallelic null-dominant) through SCAR12 (milder, hypomorphic) as one genotype–phenotype continuum.
- **Functional axis:** loss of function is **not necessarily complete**. Residual function is possible and is the variable that tracks severity.
- **Genotype classes (Gao 2025 framework):** N/N (null/null) · N/M (null/missense) · M/M (missense/missense). N/N carries the highest risk of seizures, hypertonia and respiratory complications; N/M and M/M sit below it — which never authorizes reduced clinical vigilance.

---

## Genotype interpretation rules (method)

These rules are **allele-wise**. Each worked example below is carried independently: the public edition never assembles them into one person's genotype.

- **WWOX variants are not interchangeable**; extrapolation from full-KO models requires explicit caution.
- **A compound-heterozygous class is not null/null** — a milder organoid phenotype is expected than in full KO.
- **Separate synthesis · solubility · turnover · route · function.** A variant can be *made but unstable*, *stable but inert*, or degraded by different routes; each implies a different therapeutic lever. Abundance alone never establishes function.
- **Genotype classes** (Gao 2025): N/N · N/M · M/M. The class is a *syntactic* label derived from the DNA lesion type, never from a measured protein effect — it is a **noisy proxy for residual function** (see CLAIM 033).

### Worked example A — a destabilizing SDR missense

p.Gln230Pro (Q230P) ≠ P47T: do not auto-transfer P47T data across variants. In homozygous fibroblasts of this exact variant the transcript is normal and protein is not detected. The cause remains **unresolved** — impaired translation, insolubility, or premature degradation. The HSC70/lysosome read-across from P252A is a **bridge hypothesis**, not a demonstrated mechanism.

An SDR stabilizer is `conditional / not design-ready` (`BATCH_20260714_001`).

### Worked example B — a canonical splice-acceptor variant

A canonical acceptor-site variant is expected to behave as a null-predicted allele — but that expectation is a prediction until an RNA readout measures it, and it may remain a VUS in ClinVar until functional evidence (ACMG PS3) exists.

🔴 **Withdrawn by `BATCH_20260927_004`, and binding on this example:** the NMD premise that closed the splice axis in the therapeutic-hypotheses ledger — unsourced, untagged, and contradicted by the architecture (exon 9 is terminal) — is replaced there by a labelled conditional, with the ledger's proteotoxic flag applying to **both** alleles rather than one (a statement about that ledger entry; the worked examples in this file remain carried independently). `PAPER 044`'s quoted *«the deletion led to nonsense-mediated decay»* is the abstract's and a figure legend's inference from junction qPCR; the **body** says *«suggesting that the two longer transcripts were not expressed or were degraded»*, and no translation block was used on any freely reachable surface.

---

## Mechanistic architecture

### Network hyperexcitability
WWOX-related encephalopathy should not be modelled only as a "seizure disorder" or as a downstream consequence of developmental damage. Current evidence supports a **primary disturbance of neocortical network stability**, including spontaneous bursting, altered oscillatory organization, increased phase–amplitude coupling, reduced spontaneous inhibition, increased excitatory drive, depolarization, increased firing and rebound-prone physiology. This elevates network-state pathology to core-pathway status. *(CLAIM 021 / PAPER 031, Breton 2021.)*

**Unchanged in `BATCH_20260927_004`, and binding here:** no drug is recommended, no dose is transferred, and no molecule enters or leaves a class. The carbenoxolone withdrawal does **not** promote memantine; d-APV is a tool compound and has never been given to a human.

### Prenatal developmental architecture
In severe null genotypes, disease onset may begin prenatally, with detectable fetal brain abnormalities. Severe WWOX disease should therefore not be interpreted as purely postnatal epileptic deterioration: a developmental architecture failure may already be active in utero, especially in null-severe presentations. For an N/M genotype class this informs the structural reading without directly implying the same prenatal burden. *(CLAIM 022 / paper 216.)*

### WWOX as routing / scaffold protein
WWOX should be modelled not only as a tumour suppressor or metabolic regulator, but also as a **routing/scaffold protein** able to change partner localization and thereby redirect biological output. Relocalization of p73 is the anchoring example: the same protein produces different output depending on where WWOX routes it. *(CLAIM 023 / [[paper_registry_current#PAPER 081]], PMID 15070730.)*

🔴 **Narrowed in `BATCH_20260909_001`, and the mirror moved with the claim.** This line previously read *"**phosphorylation-sensitive** routing/scaffold protein"* and named *"**Tyr33-dependent** relocalization"* as the anchoring example. **The primary tests no such relation.** Tyr33 phosphorylation regulates the **binding** — that leg is the best-supported content in the paper and is untouched — but **no experiment in it manipulates phosphorylation and measures localisation**: 20 body sentences mention Src and **zero** of them also mention localisation, cytoplasm, nucleus, redistribution or sequestration. The routing leg itself survives and is **overexpression-dependent by the authors' own words**. What is removed is a causal coupling the model inherited from a claim *title*, never from an experiment. Nothing is reversed and the architecture is unchanged: WWOX remains a routing/scaffold regulator, at `INFERENZA` strength.

### Domain cooperativity
WW-domain biology depends on **WW1–WW2 tandem cooperativity**. Functional interpretation of variants should consider tandem stability, partner-recognition geometry and residual interaction architecture — not isolated single-domain logic. WW2 acts through two separable mechanisms: it pre-orders and stabilizes the otherwise unstable WW1, **and** it can engage a second PPxY motif directly when motif sequence, spacing, linker length and orientation create a compatible topology. The corollary is a measurement rule: **the presence of two PPxY motifs in a partner does not establish that WW2 is occupied** — in the primary source the largest direct WW2 contribution comes from engineered short-linker tandem peptides, while the native ErbB4 PY1PY2 gains affinity yet stays predominantly WW1-bound. Partner topology is therefore part of WWOX's functional state. *(CLAIM 024 / PAPER 055, Rotem-Bamberger 2022; historical pointer: paper 204.)*

### SDR-domain function is measurable — and one region of it must not be touched
The SDR domain is not only a folding and stability problem. It carries a **demonstrated, residue-resolved function**: WWOX binds GSK3β through a 20-residue Axin/FRAT/GSKIP-like docking motif at **388–407**, with **L404 strictly required**, and blocks GSK3β-mediated phosphorylation of Tau at S396/S404 — restoring Tau-driven microtubule assembly and neurite outgrowth, with the interaction detectable between endogenous proteins in mouse brain. Two consequences for the model. **(1) A design constraint, now `DATO`-backed rather than citation-backed:** the canonical ERLIQ 402–406 degron contains a residue required for a demonstrated function, so any ligand that stabilizes WWOX by clamping that region risks rescuing abundance while abolishing function — the "stable but inert" trap, with an experimentally identified victim function. **(2) A measurement warning:** the inhibition is **S9-independent** (phospho-S9 unchanged while kinase output changes) [corrected 2026-09-28 from «GSK3β abundance and phospho-S9 unchanged» by `CC-20260928-MIRROR005-REPAIRS-01` `WM-A9`: the source states invariance for phospho-GSK3βS9 only], so GSK3β de-repression caused by WWOX loss would be **invisible to the standard phospho-S9 western**. *(CLAIM 035 / PAPER 056, Wang 2012.)* **Qualification of the parenthesis above (`BATCH_20260927_004`):** Wang 2012's Figure 1 legend blots and densitometers total GSK3β; what is absent is the **stated invariance**, not the measurement — `NOT_ASSERTED`, not `MEASURE_ABSENT`.

### Metabolic branch refinement
The metabolic branch extends beyond a simple HIF1A/Warburg framing. The WWOX/HIF1A axis appears to act as a broader **state indicator** linked to glycolysis, inflammatory tone, Wnt-related signalling and possibly state-transition biology. Separately, one HEK293T WWOX interactome co-purifies with trafficking proteins and is annotation-enriched for catabolic pathways; Acetyl-CoA convergence follows pathway-map topology. **Functional trafficking–metabolism coupling has not been measured**. An independent non-neural paper supports the VOPP1 interaction limb, not the coupling hypothesis. *(CLAIM 025 / paper 191; CLAIM 026 / PAPER 032 and PAPER 103.)*

> **Integrity exclusion (source-integrity discipline, worked example).** The HGF/Met–TAZ–WWOX bone-metastasis line does **not** count as independent corroboration: the primary (PMID 28151481) was retracted in 2022 for manipulation/reuse of western-blot controls, and the review (PMID 28045433) reuses its data and dependencies. The WWOX/HIF1α axis stands only on the independent sources already registered. **No baseline claim depended on the invalidated line.**

### Research-facing, not yet core
The HYAL-2 / HA / SMAD4 / WWOX branch is retained as a high-value research branch relevant to ECM/membrane-to-nucleus signalling and injury-response biology, but is **not** promoted to a central operational pathway. *(CLAIM 027 / paper 214.)*

### Cross-pathway interpretive principle
WWOX biological output is strongly **partner- and context-dependent**. Expression level alone is insufficient to infer uniform functional benefit: **"more WWOX = better" is not a safe default** across biological contexts. *(CLAIM 028 / papers 207, 218, 206, 214.)*
WWOX may also contribute directly to **ATM-linked DNA-damage-response competence** and genome-stability maintenance. This is not a core clinical pathway, but it opens a plausible structural-vulnerability branch connecting WWOX loss with replicative/genomic stress handling in proliferative developmental compartments. *(CLAIM 029 / PAPER 027, Abu-Odeh 2014; PAPER 110/115 add murine B-cell observations with no direct CNS transfer.)*

---

# BLOCK 1 — decision-ready one-pager (disease level)

> Disease-level management-reasoning principles synthesized from the public literature, to **support — never replace —** a treating clinical team. Nothing here is medical advice, and nothing here describes an individual.

## 0) DATA vs INFERENCE

### DATA (WWOX literature)
- **VABAM** (vigabatrin-associated brain abnormalities on MRI) documented in WWOX-DEE (Choi 2026) — a real safety signal; **conflicting** with You 2024 (seizure reduction, no documented VABAM) and with Shaukat 2018 (*"the spasms resolved"*).
- Network hyperexcitability + AAV-WWOX rescue in human organoids (Steinberg 2024).
- Non-cell-autonomous hypomyelination on neuronal WWOX deletion (Repudi 2021).
- N/N genotype associated with higher risk of seizures, hypertonia and respiratory complications vs N/M and M/M (Gao 2025, n = 50).
- AAV9-hSynI-hWWOX: durable rescue in the Wwox-null murine model, including ECoG/SWD reduction (Obeid 2026). 🔴 **Not a graded continuum — a threshold.** Figure 3B: the low-dose arm (1.23 × 10¹¹ vg) does **not** rescue survival, it moves death from ~20 to ~90 days and then the curve reaches zero, while the high dose (2.63 × 10¹¹ vg) plateaus at ~80% to 300 days; at P20 the low dose had not corrected hypoglycaemia and the high dose had. See [[claim_registry_current#CLAIM 011]], flagged for review.
- Ketogenic diet associated with seizure improvement in 3/5 WOREE patients (Chong 2023).

### INFERENCE
- Ca²⁺ / network dysregulation as a **primary driver** of hyperexcitability — plausible, supported.
- Hypomyelination as a possible **amplifier** — requires imaging confirmation.
- Neuroinflammation as a **low-noise modifier**, partly downstream of network dysfunction (neuron-specific rescue reduces gliosis — Obeid 2026).
- **Q230P functional endpoint:** normal transcript with protein not detected; synthesis/translation versus premature degradation is unresolved, and residual function cannot be inferred from abundance alone.
- Q230P is **not** automatically equivalent to P47T.
- An N/M genotype class implies a lower risk profile than N/N for seizure burden, hypertonia and respiratory complications (inference from Gao 2025).
- Part of the WWOX-DEE phenotype plausibly grafts onto a **prenatal substrate** of abnormal cortical migration/assembly, with defective layering, incomplete cortical maturation and possible downstream myelin/glial failure — which strengthens the interpretive weight of EEG relative to early MRI.
- **GABA remains an axis in tension:** GABAergic vulnerability is probable but not reducible to a simple linear deficit — and as of 2026-09-27 the two accounts of it are **competing, not complementary**: inhibitory **amplitude hypofunction** (measured, in a WWOX system) versus **depolarizing GABA** (`IPOTESI`, no WWOX datum). Only the first has a measurement.

## 1) ACTIVE pathways

### ACTIVE 1 — Ca²⁺ / network dysregulation
- Network stabilization is the operative target.
- **One variable at a time**; protect the readability of any active titration or trial window before introducing a new variable.
- Expected output: reduced epileptiform density; improved EEG/clinical readability.

### ACTIVE 2 — GABAergic vulnerability (SAFETY)
- **Vigabatrin:** strong caution / avoid unless alternatives are exhausted — conflicting evidence between efficacy on spasms and VABAM risk. Position unchanged.
- **Phenobarbital:** caution.
- **Benzodiazepines:** appropriate as rescue; chronic high-dose only if essential.
- The GABA-depolarizing rationale **does not predict** clinical response — mechanism is not outcome. 🔴 **And as of 2026-09-27 (`BATCH_20260927_004`) it is also UNMEASURED**, not merely non-predictive: `IPOTESI` with `PREMISE: DEFAULT_FROM_TEXTBOOK`, with no WWOX datum under it and the corpus's one functional inhibitory measurement pointing at **amplitude hypofunction** instead. ⚠️ **The three positions above are byte-identical and do not move** — they rest on the human safety signal against the human efficacy reports, not on the mechanism. Removing an unmeasured justification from a caution makes the caution less fragile, not weaker. **Not medical advice.**

## 2) SURVEILLANCE pathways

- **Myelination / white matter** — MRI + DTI as a structured baseline; myelination adjuncts only if imaging is suggestive, one variable at a time, after the current protocol is stable.
- **Respiratory / dysphagia** — structurally associated with WWOX-DEE (more severe in N/N, present across genotypes); monitor aspiration risk, dysphagia and respiratory distress during intercurrent infections. **EEG remains more sensitive than early MRI** for network-severity assessment (Sapuppo 2026, *Curr Issues Mol Biol*, peer-reviewed).
- **Ophthalmology** — visual impairment reported in 4/5 WOREE patients even with non-uniformly abnormal imaging (Chong 2023); structured ophthalmological evaluation indicated.

## 3) RED FLAGS — when NOT to change anything

- Infection, fever, dehydration.
- Vomiting/diarrhoea, reduced intake, unstable ketones.
- An active antiseizure-medication change or titration phase.
- Multiple new supplements introduced simultaneously.
- Drastic sleep worsening without a clear cause.

## 4) Note on missense alleles and gene therapy

- Q230P ≠ P47T; avoid automatic cerebellar extrapolations.
- **Gene therapy is the only multi-pathway causal strategy** demonstrated in preclinical models.
- Obeid 2026 (Wwox-null murine model): AAV9-hSynI-hWWOX — neuron-specific targeting, dose calibration, early postnatal window → durable rescue on survival, growth, glucose, behaviour, myelination, gliosis, SWD/ECoG. 🔴 **"Dose calibration" here means clearing a threshold, not sliding along a curve:** below 2.63 × 10¹¹ vg survival is not rescued at all. An inference of the form *"a lower, safer dose would still help"* reads the dose-response as continuous and Figure 3B refuses it for survival in this model.
- Pathway P7 therefore matures from **proof-of-concept to design-principle stage**: neuron targeting, expression control, dose calibration and the early window are the operative variables.
- In humans, efficacy, safety and the optimal window remain under investigation.
- **Partial rescue is expected to be beneficial** in genotype classes retaining a missense allele (Gao 2025 genotype–phenotype suggests partial restoration may suffice).

### Trial-readiness actions (generic)
- Complete genetics.
- Serial EEG.
- MRI + DTI baseline.
- Ordered clinical history.
- Document the genotype class (e.g. N/M = missense + null-predicted splice) against anticipated trial eligibility criteria.

---

# BLOCK 2 — claim registry mirror (baseline)

> Full canonical status lives in [`claim_registry_current.md`](claim_registry_current.md). This mirror is the working model's own copy and must stay synchronized with it (a LINT consistency rule).

| ID | Title | Type | Pathway | Transferability | Status | Source |
|----|-------|------|---------|----------------|--------|--------|
| 001 | Vigabatrin → VABAM in WWOX-DEE | DATO | P2 Safety | T1 | **conflicting evidence** | Choi 2026 / You 2024 / Chong 2023 / Shaukat 2018 |
| 002 | WWOX-LoF → hyperexcitability + AAV rescue in organoids — ⚠️ **the immature/depolarizing-GABA half is `IPOTESI`, not a measured signature** (2026-09-27); the corpus's one functional inhibitory measurement points at **amplitude hypofunction** instead, and the two are competing accounts | DATO + INFERENZA + **IPOTESI** (the GABA-polarity half) | P1+P7 | T2 | consolidated baseline | Steinberg 2024 (preprint record superseded by PAPER 094; Source repointing DEFERRED, bytes not obtainable free) |
| 003 | Neuronal WWOX deletion → non-cell-autonomous hypomyelination | DATO | P4 | T2 | consolidated baseline | Repudi 2021 *Brain* |
| 004 | AAV9-WWOX neuron-targeted multi-domain rescue in vivo — ⚠️ **il confronto contro il WT o non è tracciato, o è significativo contro il rescue**; il g-ratio normalizza, gli assoni non mielinizzati no | DATO | P7 | T2 | consolidated baseline | Repudi 2021 *EMBO* (full text 2026-08-10) |
| 005 | Reduced interneuron **markers** (PV whole-hippocampus + DG/CA1; NPY **DG only**) + regional glial reactivity in **one** systemic Wwox-KO — no medication implication; its imported-premise boundary no longer says seizures are rat-only (corrected 2026-09-27, `BATCH_20260927_002`), and its prohibition on asserting **epileptogenesis as a measured process** stands unchanged | DATO | P2+P6 | T2 | consolidated baseline | Hussain 2019 (PMID 30290271, full text); boundary also cites PAPER 057 / 058 / 059 and PAPER 042 |
| 006 | P47T model shows progressive hippocampal astrogliosis; microglial progression shown for morphology only | DATO+INF | P6 | T3 ⚠️ genotype caution | consolidated baseline | Hussain 2023 |
| 007 | P47T abolishes or near-abolishes WWOX recovery by two PPPY peptides in vitro; WW1/WBP-1/SIMPLE biochemistry is an independent non-neural antecedent | DATO | P3 | T3 ⚠️ genotype caution | consolidated baseline | Hussain 2023 (PAPER 007); Ludes-Meyers 2004 (PAPER 104, antecedent only) |
| 008 | WOREE/SCAR12 form a genotype–phenotype spectrum | DATO | Clinical spectrum | T1 contextual | consolidated baseline | Aldaz 2020 / Banne 2021 |
| 009 | WWOX deficiency plausibly alters mitochondrial quality control, redox, energy efficiency — ⚠️ counter-directional evidence recorded (CLAIM 034) | INFERENZA | P5 | T2 conceptual | in observation | Baryła 2022 / PAPER 054 (counter-direction) |
| 010 | Mitophagy more relevant than senolytics for the WWOX mitochondrial problem | IPOTESI | P5 | T4 | background only | Mechanistic synthesis |
| 011 | AAV9-hSynI-hWWOX: rescue durevole nel modello Wwox-null (survival, ECoG/SWD, myelination, gliosis) — 🔴 **`dose-dependent` descrive un continuo dove la Figura 3B mostra una SOGLIA** fra 1.23 e 2.63 × 10¹¹ vg | DATO (preclinical) | P7 | T2 | **flagged for review** | Obeid 2026 |
| 012 | Severe early-fatal WWOX case (exon 6–7 del + exon 8 frameshift): MRI initially normal, death at 3 months | DATO descriptive | Clinical spectrum | T1 phenotypic | consolidated baseline (full text) | Sapuppo 2026 (*Curr Issues Mol Biol*, peer-reviewed) |
| 013 | N/N genotype in WWOX-DEE associated with higher risk of seizures, hypertonia, respiratory complications vs N/M and M/M | DATO (parental survey) | Clinical spectrum / P2 / respiratory | T1 | in observation | Gao 2025 |
| 014 | WWOX loss perturbs prenatal cortical development, migration and cortical maturation across species | DATO | P3 | T2 | consolidated baseline | Iacomino 2020 / Kumada 2019 / Kośla 2019 |
| 015 | Part of WWOX-DEE likely arises on a structurally misassembled prenatal cortical substrate | INFERENZA strongly supported | P3+P1+P4 | T2 conceptual | consolidated baseline | Iacomino 2020 / Cheng 2020 / Kumada 2019 / Repudi 2021 |
| 016 | GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency — now framed as **de-repression** (loss of a physical brake); the abundance datum is **withdrawn** — Fig. 7c is single-lane densitometry, `NOT_TESTED` in both directions (`BATCH_20260927_003`; mirror corrected 2026-09-28, `CC-20260928-MIRROR003-REPAIRS-01` M4) | DATO+INF | emerging node | T2 mech / T4 clinical | in observation | Cheng 2020 / PAPER 056 (Wang 2012) |
| 017 | WWOX-related human disease spans a spectrum from severe WOREE/WWOX-DEE to milder SCAR12-like phenotypes | DATO | human spectrum / genotype-phenotype | T1 | consolidated baseline | Abdel-Salam 2014 / Piard 2018 / Oliver 2023 / Teplyshova 2024 / Banne 2021 ([[paper_registry_current#PAPER 040]]) |
| 018 | Exon-6 splice disruption is a confirmed pathogenic mechanism in human WWOX disease | DATO | genotype logic | T1 | consolidated baseline | Piard 2019 *EJPN* |
| 019 | Q230P occurs in severe human disease in a compound-heterozygous context; allele-specific interpretation required | DATO+INF | genotype logic | T1 | consolidated baseline | Piard 2019 / Chong 2023 / Gao 2025 / Johannsen 2018 |
| 020 | Selected WWOX-related trajectories may include survival into adulthood with severe disability and late motor regression | DATO | natural history / clinical spectrum | T1 phenotypic | consolidated baseline | Teplyshova & Sharkov 2024 |
| 021 | WWOX loss destabilizes neocortical network physiology via combined synaptic and intrinsic mechanisms — 🔴 **the gap-junction half of the burst dependence is WITHDRAWN as not attributable** (2026-09-27): NMDAR blockade alone abolishes the burst; carbenoxolone's effect does not reverse on washout and the authors name NMDA-receptor block among its possible actions. Not «uninvolved» — untested. ⚠️ The spontaneous-current analysis uses a **pooled wild-type + heterozygote control**, and the heterozygote differs from wild type on four intrinsic properties | DATO | P1 / network-state | T2 | consolidated baseline | PAPER 031 (Breton 2021) |
| 022 | Severe WWOX-null phenotypes can begin prenatally with detectable fetal brain abnormalities | DATO | prenatal architecture / severe spectrum | T1 phenotypic | consolidated baseline | paper 216 |
| 023 | WWOX controls partner function via subcellular rerouting; Tyr33 phosphorylation regulates the **binding**, its effect on rerouting untested (narrowed `BATCH_20260909_001`) | DATO | signalling / routing / scaffold | T2 mechanistic | consolidated baseline | [[paper_registry_current#PAPER 081]] (PMID 15070730) |
| 024 | WWOX WW-domain function depends on WW1–WW2 tandem cooperativity — ⚠️ **bounded 2026-09-27: for at least one partner (ATM) the isolated WW1 domain is sufficient in a HEK293 lysate pull-down, so tandem cooperativity is NOT required for every interaction** (isolated-domain sufficiency, no error bar or replicate count anywhere in the supplement) | DATO | domain architecture / variant interpretation | T2 indirect | consolidated baseline | PAPER 055 (Rotem-Bamberger 2022); hist. paper 204 |
| 025 | WWOX/HIF1A ratio as a systems-level state marker linking glycolysis, inflammation and Wnt-adjacent signalling | DATO+INF | P5 / state transition | T2 conceptual | in observation | paper 191 |
| 026 | WWOX co-associates with trafficking proteins; metabolic pathway annotation on the same prey list, with coupling untested | DATO+IPOTESI | P5 / trafficking | T3 | in observation | PAPER 032 (prey and annotation); PAPER 103 (VOPP1 limb) |
| 027 | WWOX as an ECM/membrane-to-nucleus signalling node via HYAL-2/SMAD4 | INFERENZA | ECM / injury response | T3 indirect | in observation | paper 214 |
| 028 | WWOX output is partner- and context-dependent; expression level ≠ uniform benefit | INFERENZA | cross-pathway interpretive principle | T2 indirect | flagged for review | papers 207, 218, 206, 214 |
| 029 | ATM-linked DDR remains in observation; whole-body-null B-cell repair junctions shift without greater local mutation frequency, and MYC-driven knockout tumours show context-limited instability | DATO+INF prudent | genome stability / ATM / DDR | T2 conceptual for ATM; T3 for murine B-cell observations | in observation | PAPER 027 (Abu-Odeh 2014, *PNAS*); PAPER 110; PAPER 115. PAPER 030 is the duplicate. |
| 030 | In WWOX, severity tracks **residual function**, not protein abundance | INFERENZA | genotype logic / P7 threshold | T2 | in observation | BATCH_20260710_A synthesis |
| 031 | It is a **DEE, not an EE**: seizure control does not save development | INFERENZA | clinical spectrum / strategy | T1 conceptual | in observation | BATCH_20260710_A synthesis |
| 032 | Una copia di WWOX conserva alcuni endpoint osservati, ma non definisce una soglia terapeutica del SNC; tumori spontanei negli eterozigoti e ipomorfo omozigote vitale ma compromesso delimitano l’inferenza (`PREMISE: NOBODY_LOOKED`) | DATO + INFERENZA | P7 / threshold | T1/T2 observations; T3 CNS transfer | in observation | PAPER 078, 098, 107; PAPER 053 is a review conduit |
| 033 | Biallelic null WWOX carries higher mortality than genotypes with at least one missense, but genotype class is only a noisy proxy for residual function | DATO+IPOTESI | genotype–phenotype / prognosis | T1 nominal / T3 effective | in observation | Oliver 2023 / Johannsen 2018 / Banne 2021 |
| 034 | In a post-mitotic excitable neuron under metabolic stress, WWOX up-regulation is pro-oxidant: the sign of WWOX↔ROS is context-dependent, not monotonic | DATO (photoreceptor) + ESPANSIONE (any transfer) | P5 redox / P1 Ca²⁺ | T3 ⚠️ genotype caution | in observation | PAPER 054 (Saadane 2021) |
| 035 | WWOX is a direct, residue-mapped inhibitor of GSK3β via an Axin-like SDR motif; S9-independent, Tau-dependent output — ⚠️ **two intervals, separated 2026-09-27: `WWOX388−407` is what the source says is *required for the interaction* (Fig. 3c), while the conserved FXXXLI/VXRLE docking motif is contained in the DISTINCT `WWOX388−412` (Fig. 2a)**; `L404` strictly necessary; the microtubule limb is **cell-free** and its restoration **partial** | DATO (5 orthogonal assays) + INFERENZA (transfer) | P1 neurodevelopment / SDR function | T2 mechanistic | in observation | PAPER 056 (Wang 2012) |
| 036 | A systemic Wwox-null mouse at P18 is metabolically decompensated, so any brain phenotype in that window carries a quantified systemic confounder | DATO (measures) + INFERENZA (scope as confounder) | P5 metabolism / kidney — cross-cutting | T3 methodological | in observation | PAPER 057 (Ludes-Meyers 2009) |
| 037 | Seizure-related phenotypes in WWOX rodent models are documented in the rat `lde/lde` (audiogenic + EEG), in the **Wwox-null mouse** (behavioural since 2014, electrographic since 2026) and in the **`P47T` knock-in** (video-EEG, adult); the **audiogenic** phenotype is documented in the constitutive `Wwox`-null **mouse** too (behavioural, unscored, no EEG, one laboratory, wild-type comparator 0/8; handling also provoked seizures, so acoustic specificity is not established); only the **kindling-like** progression remains rat-only | DATO | P2 excitability | **per axis (2026-09-27):** T2 biallelic-loss vulnerability · T2 electrographic epileptiform activity in the mouse null (**on the running text; the Fig 7E pairwise assignment is a declared panel attestation, so the SWD *reduction* is assertable and treated-vs-WT *equivalence* is not**) · T2 behavioural seizures incl. audiogenic in constitutive nulls · T3 kindling-like progression (rat only) · T3 any transfer to a human genotype | in observation | PAPER 058 + PAPER 059 (rat) + PAPER 042 / PMID 24369382 (constitutive mouse null, audiogenic + spontaneous, behavioural) + PMID 32000863 (mouse null, behavioural + provoked) + PMID 42422765 (mouse null, ECoG) + PMID 36828035 (`P47T`, video-EEG) |
| 038 | Elevated BUN recurs across Wwox rodent models — and creatinine is elevated in the rat, the only model in which it was measured (creatinine recurrence **`UNDETERMINED`**: no creatinine measurement exists on any of the three surfaces this repository holds for PMID 19936220; narrowed 2026-09-28, `CC-20260922-CLAIM038-UNIT-CLASS-02` Δ3) — with two competing explanations, renal insufficiency or seizure-driven hypercatabolism, neither ever tested | DATO (measures) + IPOTESI (both explanations) | P5 metabolism / kidney | T3 open question | in observation | PAPER 059 (Suzuki 2007) + PAPER 057 (Ludes-Meyers 2009) |
| 039 | Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95% versus 0%; **endpoint: light-microscopy histology at ~28 d, no quantitative motor test** — 🔴 neither evidence stream establishes nor excludes a cerebellar contribution | DATO | P1 neurodevelopment / motor function | T3 | in observation | PAPER 059 (Suzuki 2007) |
| 040 | Neuronal restoration of WWOX suppresses spike-wave discharges in the `Wwox`-null mouse to a level statistically indistinguishable from wild type (`****` WT-vs-KO, `****` KO-vs-HD, **`ns` WT-vs-HD**) — 🔴 `n=5`/group, single channel, no post-surgical recovery interval, P14–P21 only; the interictal-spike endpoint of the same figure sits at the Mann–Whitney floor and is **not tested**; SWD is an absence-type signature, not a convulsive seizure | DATO | P1 neurodevelopment / P7 network excitability | T2 | in observation | PAPER 011 (PMID 42422765), Fig. 7E |
| 041 | P47T mouse: fewer calbindin-positive Purkinje profiles than WT at 80 and 250 days; basket-cell genotype tests nonsignificant at both ages, with no within-mutant progression test | DATO + bounded INFERENZA | P1 cerebellar structure | T3, P47T only | in observation | PAPER 007 (PMID 36828035), Fig. 5d/e |

**Cross-cutting strategic implication.** CLAIM 031 motivates causal intervention; CLAIM 032 makes partial restoration a testable possibility for specified endpoints. The WWOX level, mosaic fraction and timing needed for neurological rescue have not been measured.

---

# BLOCK 3 — flowchart logic summary

1. Is the baseline stable? → if **no**: introduce no variables.
2. Minimum dataset available (EEG, MRI, genetics)? → if **no**: prioritize acquiring it.
3. MRI/DTI: significant hypomyelination? → if **yes**: discuss a myelination adjunct (one variable).
4. Strong GABAergics considered? → apply strong caution; conflicting evidence on vigabatrin (VABAM risk vs occasional seizure reduction); position unchanged — avoid unless alternatives are exhausted.
5. Focus: **network stabilization**.
6. Follow-up on **n-of-1 endpoints** (startle / sleep / EEG), not on seizure count alone.
7. Gene-therapy readiness: maintain trial-ready documentation at all times.

**Principles**
- Do not force decisions.
- Order the timing.
- Separate safety from drivers and from structural surveillance.
- Prevent multi-variable changes during titration or trial phases.

## Monitoring endpoints (n-of-1 method)

- **Startle:** 0–3 score + daily count + main triggers.
- **Sleep:** awakenings per night + wake/sleep differentiation.
- **Feeding / posture:** events during transitions.
- **EEG:** epileptiform-anomaly density + background organization — prioritized over seizure count alone (EEG is more sensitive than early MRI for network severity).

---

## Gene therapy context

- An AAV9-WWOX clinical programme is anticipated (2025–2027).
- The therapeutic window is generally considered still open in early childhood; plasticity at age ~3 is plausible, not guaranteed.
- **Steinberg 2024 organoids:** AAV9-WWOX normalizes Ca²⁺ transients and hyperexcitability; MYC overexpression identified as a key mechanism.
- **Obeid 2026 (Wwox-null murine model):** AAV9-hSynI-hWWOX — durable rescue on survival, glucose, behaviour, myelination, gliosis, SWD/ECoG; neuron-specific targeting; early postnatal ICV delivery. P7 design principles are now defined preclinically. 🔴 With the threshold qualification above: the low-dose arm does not survive.
- **Repudi 2021 *EMBO* (Wwox-null murine model), read in full 2026-08-10:** the companion proof of concept, and its limit is where the comparator sits. The rescue is **not shown to reach wild-type** in the panels where it looks strongest — those brackets are drawn WT-vs-KO and KO-vs-rescued, never WT-vs-rescued — and the one WT-vs-rescued comparison that IS drawn, unmyelinated axons per field, is significant **against** the rescue. The g-ratio does normalise. Transduction reaches 60–70% of neurons; oligodendrocytes are never transduced, which is what makes the myelin recovery non-cell-autonomous. Treatment is at **P0** because the model does not survive otherwise, and post-natal dosing is declared future work.
- **Design principles (Obeid 2026 review):** human synapsin promoter (neuron-specific); WPRE removed (avoid overexpression); controlled dose; critical early postnatal window (P0–P5 in mouse).
- **Safety caveat:** DRG / peripheral-organ dose-limiting toxicity at high systemic AAV dose → favours targeted, controlled delivery (a paediatric regulatory concern).
- **`TX-007` (`BATCH_20260927_004`):** `SAFETY 1` — a measured efficacy floor with **no measured ceiling**, on a tumour suppressor whose induction is pro-apoptotic, delivered by a vector with `REVERS 0`, in a dose-ranging study containing **no tumour surveillance** — an absence measured on the text, not on the missing supplement.
- **Epigenetic option (future / ESPANSIONE):** dCas9/CRISPRa upregulation of endogenous WWOX for **hypomorphic** states — potentially relevant where a residual-function missense allele is present; not actionable now.
- **First-in-human (background / observation):** a WWOX gene therapy reported as administered to an infant with WWOX epilepsy (ICV route). The strongest external signal on the gene-therapy axis; peer-reviewed clinical data awaited. **NOT a datum.**

---

## Changelog

Moved verbatim — with the per-batch `Last update` notes and the MAJOR-batch sections — to [`working_model_history.md`](working_model_history.md) by `BATCH_20260928_004` (structural). This file states the current model; the history states how it got here, and where the two differ this file is the current value.
