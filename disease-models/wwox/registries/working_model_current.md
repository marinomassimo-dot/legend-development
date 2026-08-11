# Working Model Current

## WWOX loss-of-function (WOREE / WWOX-DEE) — disease-level working model

**Version:** WM_v4.2_2026-08-10
**Date baseline:** 2026-03-28
**Last update:** 2026-08-10 — `BATCH_20260810_005` (**MINOR**): **il mirror delle claim non si era mosso con le claim.** `CLAIM 004` e `CLAIM 011` erano state portate a `flagged for review` il 2026-08-10 nel registro, e questa tabella continuava a mostrarle entrambe `consolidated baseline`: un lettore del solo modello di lavoro avrebbe visto due baseline sane dove il registro segnalava due difetti. Corretto in entrambe le direzioni — `CLAIM 004` **torna** `consolidated baseline` perché il suo flag è **risolto** dalla lettura integrale di PMID 34747138 (il comparatore mancante è ora scritto dentro la claim: dove il rescue è confrontato col WT, o il confronto non è tracciato, o è significativo **contro** il rescue; il g-ratio normalizza, gli assoni non mielinizzati no), e `CLAIM 011` **resta** `flagged for review` con la soglia di Figura 3B scritta anche qui, nelle tre righe narrative che ripetevano *«dose-dependent»* e portavano il lessico del continuo dentro il modello. `PAPER 063` (Steinberg 2021, atlante dei modelli) promosso da `CORPUS-STUB-003`, `LIT-0030` completata; `CORPUS-STUB-048` risolto come duplicato di `PAPER 005`, `LIT-0072` completata; entrambi i placeholder conservati append-only. Correzione di registro: `PAPER 005` indicava `CORPUS-STUB-042` come proprio duplicato e **non lo è** (è PMID 35107375, filovirus VP40). `CLAIM 016` riceve il confine che il locator del suo primario portava dal giorno della lettura e che non era mai arrivato in canonico: **il litio ha soppresso le crisi da PTZ in tutti e tre i genotipi, wild-type incluso**, quindi l'esperimento non stabilisce un rescue farmacologico WWOX-specifico. `CLAIM 003` riceve il confine di *«non-cell-autonoma»*: è una componente, non l'intero fenomeno. Nessuna inversione di baseline, nessun cambiamento di BLOCCO 1, nessuna raccomandazione terapeutica. Prev: 2026-08-06 — `BATCH_20260806_002` (**MINOR**): the imported-premise chain under `CLAIM 005` traced to its end, every link read in full. **Early death is first-hand** in PMID 19936220; 🔴 **epileptogenesis is not measured there at all**, and its terminal source PMID 19500159 states in three places — and in a Table 2 whose `Epilepsy` row is empty for both mouse models — that **Wwox-null mice show no epilepsy**. Two citation hops had converted an explicit negative about a rat into a positive assertion about a mouse. Four claims added `in observation`: **036** (a systemic Wwox-null mouse at P18 is metabolically decompensated, so brain phenotypes in that window carry a quantified confounder), **037** (the seizure phenotype is a rat `lde/lde` phenotype, EEG-documented, explicitly absent in mice), **038** (elevated BUN/creatinine recur across models with two competing and untested explanations — renal insufficiency or seizure-driven hypercatabolism), **039** (ataxia at 95% versus 0%, non-cerebellar, the most penetrant phenotype of the `lde` model and one the downstream literature dropped entirely). `PAPER 057/058/059` and `LIT-0405` created. **`PAPER 021` metadata corrected**: the author is **Tochigi**, not Kumada, and its title named an invented *lissencephaly* that appears nowhere in the paper — `CLAIM 014/015` now state that it contributes early postnatal maturation (PND5–21), not prenatal migration or layering. No baseline reversal, no BLOCK 1 change, no therapeutic recommendation. Prev: 2026-08-06 — `BATCH_20260806_001` (**MAJOR**): CLAIM 005 narrowed to what PMID 30290271 measures — marker-positive counts, glial area fractions, GAD65/67 protein in **one** systemic KO — and its medication caution (*"Supports caution with strong GABAergic burden"*) **deleted**. The paper tests no drug, no GABA concentration and no inhibitory function; the caution was never its result. The experimental datum is not demoted and the claim stays `consolidated baseline` / `DATO`: the MAJOR bump is required by removing safety language from a baseline claim, which is a policy change even when it removes rather than adds. PAPER 006 / LIT-006 identifiers normalized (PMID 30290271 / PMC7104842 / DOI 10.1016/j.nbd.2018.09.026); `CORPUS-STUB-085` resolved as its duplicate, preserved append-only. Prev: 2026-07-26 — `BATCH_20260726_001` (MINOR): three papers read in full and integrated (PAPER 054, 055, 056), two new claims `in observation` (CLAIM 034 — the sign of WWOX↔ROS is context-dependent; CLAIM 035 — WWOX is a residue-mapped direct inhibitor of GSK3β), CLAIM 016 enriched with the mechanism and a `PREMISE_TAG`, CLAIM 024 given its identified primary source, CLAIM 009 given a mandatory counter-directional note. No baseline reversal, no BLOCK 1 change. Prev: 2026-07-25 — `BATCH_20260725_001` (MINOR): restored CLAIM 033 to the complete BLOCK 2 mirror and normalized the CLAIM 028 source pointer from the nonexistent paper 213 to the tracked CORPUS P207. No scientific claim, status or clinical logic changed. Prev: 2026-07-14 — `BATCH_20260714_001`: canonical repair of CLAIM 019. Johannsen 2018 demonstrates normal mRNA + Q230P protein not detected, but does **not** discriminate impaired translation from premature degradation. Degradation withdrawn as a datum and the experimental branches reopened. MAJOR bump v2.1 → v3.0.

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

### Worked example B — a canonical splice-acceptor variant

A canonical acceptor-site variant is expected to behave as a null-predicted allele — but that expectation is a prediction until an RNA readout measures it, and it may remain a VUS in ClinVar until functional evidence (ACMG PS3) exists.

---

## Mechanistic architecture

### Network hyperexcitability
WWOX-related encephalopathy should not be modelled only as a "seizure disorder" or as a downstream consequence of developmental damage. Current evidence supports a **primary disturbance of neocortical network stability**, including spontaneous bursting, altered oscillatory organization, increased phase–amplitude coupling, reduced spontaneous inhibition, increased excitatory drive, depolarization, increased firing and rebound-prone physiology. This elevates network-state pathology to core-pathway status. *(CLAIM 021 / PAPER 031, Breton 2021.)*

### Prenatal developmental architecture
In severe null genotypes, disease onset may begin prenatally, with detectable fetal brain abnormalities. Severe WWOX disease should therefore not be interpreted as purely postnatal epileptic deterioration: a developmental architecture failure may already be active in utero, especially in null-severe presentations. For an N/M genotype class this informs the structural reading without directly implying the same prenatal burden. *(CLAIM 022 / paper 216.)*

### WWOX as routing / scaffold protein
WWOX should be modelled not only as a tumour suppressor or metabolic regulator, but also as a **phosphorylation-sensitive routing/scaffold protein** able to change partner localization and thereby redirect biological output. Tyr33-dependent relocalization of p73 is the anchoring example: the same protein produces different output depending on where WWOX routes it. *(CLAIM 023 / paper 206.)*

### Domain cooperativity
WW-domain biology depends on **WW1–WW2 tandem cooperativity**. Functional interpretation of variants should consider tandem stability, partner-recognition geometry and residual interaction architecture — not isolated single-domain logic. WW2 acts through two separable mechanisms: it pre-orders and stabilizes the otherwise unstable WW1, **and** it can engage a second PPxY motif directly when motif sequence, spacing, linker length and orientation create a compatible topology. The corollary is a measurement rule: **the presence of two PPxY motifs in a partner does not establish that WW2 is occupied** — in the primary source the largest direct WW2 contribution comes from engineered short-linker tandem peptides, while the native ErbB4 PY1PY2 gains affinity yet stays predominantly WW1-bound. Partner topology is therefore part of WWOX's functional state. *(CLAIM 024 / PAPER 055, Rotem-Bamberger 2022; historical pointer: paper 204.)*

### SDR-domain function is measurable — and one region of it must not be touched
The SDR domain is not only a folding and stability problem. It carries a **demonstrated, residue-resolved function**: WWOX binds GSK3β through a 20-residue Axin/FRAT/GSKIP-like docking motif at **388–407**, with **L404 strictly required**, and blocks GSK3β-mediated phosphorylation of Tau at S396/S404 — restoring Tau-driven microtubule assembly and neurite outgrowth, with the interaction detectable between endogenous proteins in mouse brain. Two consequences for the model. **(1) A design constraint, now `DATO`-backed rather than citation-backed:** the canonical ERLIQ 402–406 degron contains a residue required for a demonstrated function, so any ligand that stabilizes WWOX by clamping that region risks rescuing abundance while abolishing function — the "stable but inert" trap, with an experimentally identified victim function. **(2) A measurement warning:** the inhibition is **S9-independent** (GSK3β abundance and phospho-S9 unchanged while kinase output changes), so GSK3β de-repression caused by WWOX loss would be **invisible to the standard phospho-S9 western**. *(CLAIM 035 / PAPER 056, Wang 2012.)*

### Metabolic branch refinement
The metabolic branch extends beyond a simple HIF1A/Warburg framing. The WWOX/HIF1A axis appears to act as a broader **state indicator** linked to glycolysis, inflammatory tone, Wnt-related signalling and possibly state-transition biology. In parallel, WWOX interactome data suggest a **trafficking–metabolism interface** involving endomembrane systems (ER / Golgi / endosomal / lysosomal) and Acetyl-CoA-centred catabolic convergence. *(CLAIM 025 / paper 191; CLAIM 026 / PAPER 032, Hussain 2018.)*

> **Integrity exclusion (source-integrity discipline, worked example).** The HGF/Met–TAZ–WWOX bone-metastasis line does **not** count as independent corroboration: the primary (PMID 28151481) was retracted in 2022 for manipulation/reuse of western-blot controls, and the review (PMID 28045433) reuses its data and dependencies. The WWOX/HIF1α axis stands only on the independent sources already registered. **No baseline claim depended on the invalidated line.**

### Research-facing, not yet core
The HYAL-2 / HA / SMAD4 / WWOX branch is retained as a high-value research branch relevant to ECM/membrane-to-nucleus signalling and injury-response biology, but is **not** promoted to a central operational pathway. *(CLAIM 027 / paper 214.)*

### Cross-pathway interpretive principle
WWOX biological output is strongly **partner- and context-dependent**. Expression level alone is insufficient to infer uniform functional benefit: **"more WWOX = better" is not a safe default** across biological contexts. *(CLAIM 028 / papers 207, 218, 206, 214.)*
WWOX may also contribute directly to **ATM-linked DNA-damage-response competence** and genome-stability maintenance. This is not a core clinical pathway, but it opens a plausible structural-vulnerability branch connecting WWOX loss with replicative/genomic stress handling in proliferative developmental compartments. *(CLAIM 029 / PAPER 030, Abu-Odeh 2014.)*

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
- **GABA remains an axis in tension:** GABAergic vulnerability is probable but not reducible to a simple linear deficit.

## 1) ACTIVE pathways

### ACTIVE 1 — Ca²⁺ / network dysregulation
- Network stabilization is the operative target.
- **One variable at a time**; protect the readability of any active titration or trial window before introducing a new variable.
- Expected output: reduced epileptiform density; improved EEG/clinical readability.

### ACTIVE 2 — GABAergic vulnerability (SAFETY)
- **Vigabatrin:** strong caution / avoid unless alternatives are exhausted — conflicting evidence between efficacy on spasms and VABAM risk. Position unchanged.
- **Phenobarbital:** caution.
- **Benzodiazepines:** appropriate as rescue; chronic high-dose only if essential.
- The GABA-depolarizing rationale **does not predict** clinical response — mechanism is not outcome.

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
| 002 | WWOX-LoF → hyperexcitability + AAV rescue in organoids | DATO+INF | P1+P7 | T2 | consolidated baseline | Steinberg 2024 |
| 003 | Neuronal WWOX deletion → non-cell-autonomous hypomyelination | DATO | P4 | T2 | consolidated baseline | Repudi 2021 *Brain* |
| 004 | AAV9-WWOX neuron-targeted multi-domain rescue in vivo — ⚠️ **il confronto contro il WT o non è tracciato, o è significativo contro il rescue**; il g-ratio normalizza, gli assoni non mielinizzati no | DATO | P7 | T2 | consolidated baseline | Repudi 2021 *EMBO* (full text 2026-08-10) |
| 005 | Reduced interneuron **markers** (PV whole-hippocampus + DG/CA1; NPY **DG only**) + regional glial reactivity in **one** systemic Wwox-KO — no medication implication | DATO | P2+P6 | T2 | consolidated baseline | Hussain 2019 (PMID 30290271, full text) |
| 006 | P47T model → progressive neuroinflammation | DATO+INF | P6 | T3 ⚠️ genotype caution | consolidated baseline | Hussain 2023 |
| 007 | P47T abolishes PPxY binding to WW-domain partners | DATO | P3 | T3 ⚠️ genotype caution | consolidated baseline | Hussain 2023 |
| 008 | WOREE/SCAR12 form a genotype–phenotype spectrum | DATO | Clinical spectrum | T1 contextual | consolidated baseline | Aldaz 2020 / Banne 2021 |
| 009 | WWOX deficiency plausibly alters mitochondrial quality control, redox, energy efficiency — ⚠️ counter-directional evidence recorded (CLAIM 034) | INFERENZA | P5 | T2 conceptual | in observation | Baryła 2022 / PAPER 054 (counter-direction) |
| 010 | Mitophagy more relevant than senolytics for the WWOX mitochondrial problem | IPOTESI | P5 | T4 | background only | Mechanistic synthesis |
| 011 | AAV9-hSynI-hWWOX: rescue durevole nel modello Wwox-null (survival, ECoG/SWD, myelination, gliosis) — 🔴 **`dose-dependent` descrive un continuo dove la Figura 3B mostra una SOGLIA** fra 1.23 e 2.63 × 10¹¹ vg | DATO (preclinical) | P7 | T2 | **flagged for review** | Obeid 2026 |
| 012 | Severe early-fatal WWOX case (exon 6–7 del + exon 8 frameshift): MRI initially normal, death at 3 months | DATO descriptive | Clinical spectrum | T1 phenotypic | consolidated baseline (full text) | Sapuppo 2026 (*Curr Issues Mol Biol*, peer-reviewed) |
| 013 | N/N genotype in WWOX-DEE associated with higher risk of seizures, hypertonia, respiratory complications vs N/M and M/M | DATO (parental survey) | Clinical spectrum / P2 / respiratory | T1 | in observation | Gao 2025 |
| 014 | WWOX loss perturbs prenatal cortical development, migration and cortical maturation across species | DATO | P3 | T2 | consolidated baseline | Iacomino 2020 / Kumada 2019 / Kośla 2019 |
| 015 | Part of WWOX-DEE likely arises on a structurally misassembled prenatal cortical substrate | INFERENZA strongly supported | P3+P1+P4 | T2 conceptual | consolidated baseline | Iacomino 2020 / Cheng 2020 / Kumada 2019 / Repudi 2021 |
| 016 | GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency — now framed as **de-repression** (loss of a physical brake), not merely elevated abundance | DATO+INF | emerging node | T2 mech / T4 clinical | in observation | Cheng 2020 / PAPER 056 (Wang 2012) |
| 017 | Ketogenic diet has small but real human support in WWOX-related epileptic encephalopathy | DATO | P1+P5 | T1 contextual | consolidated baseline | Chong 2023 |
| 018 | Exon-6 splice disruption is a confirmed pathogenic mechanism in human WWOX disease | DATO | genotype logic | T1 | consolidated baseline | Piard 2019 *EJPN* |
| 019 | Q230P occurs in severe human disease in a compound-heterozygous context; allele-specific interpretation required | DATO+INF | genotype logic | T1 | consolidated baseline | Piard 2019 / Chong 2023 / Gao 2025 / Johannsen 2018 |
| 020 | Selected WWOX-related trajectories may include survival into adulthood with severe disability and late motor regression | DATO | natural history / clinical spectrum | T1 phenotypic | consolidated baseline | Teplyshova & Sharkov 2024 |
| 021 | WWOX loss destabilizes neocortical network physiology via combined synaptic and intrinsic mechanisms | DATO | P1 / network-state | T2 | consolidated baseline | PAPER 031 (Breton 2021) |
| 022 | Severe WWOX-null phenotypes can begin prenatally with detectable fetal brain abnormalities | DATO | prenatal architecture / severe spectrum | T1 phenotypic | consolidated baseline | paper 216 |
| 023 | WWOX controls partner function via phosphorylation-dependent subcellular rerouting | DATO | signalling / routing / scaffold | T2 mechanistic | consolidated baseline | paper 206 |
| 024 | WWOX WW-domain function depends on WW1–WW2 tandem cooperativity | DATO | domain architecture / variant interpretation | T2 indirect | consolidated baseline | PAPER 055 (Rotem-Bamberger 2022); hist. paper 204 |
| 025 | WWOX/HIF1A ratio as a systems-level state marker linking glycolysis, inflammation and Wnt-adjacent signalling | DATO+INF | P5 / state transition | T2 conceptual | in observation | paper 191 |
| 026 | WWOX as a trafficking–metabolism coupling node (endomembrane → Acetyl-CoA convergence) | DATO+INF | P5 / trafficking | T2 conceptual | in observation | PAPER 032 (Hussain 2018) |
| 027 | WWOX as an ECM/membrane-to-nucleus signalling node via HYAL-2/SMAD4 | INFERENZA | ECM / injury response | T3 indirect | in observation | paper 214 |
| 028 | WWOX output is partner- and context-dependent; expression level ≠ uniform benefit | INFERENZA | cross-pathway interpretive principle | T2 indirect | flagged for review | papers 207, 218, 206, 214 |
| 029 | WWOX contributes to ATM-linked DDR competence and genome-stability maintenance | DATO+INF prudent | genome stability / ATM / DDR | T2 conceptual | in observation | PAPER 030 (Abu-Odeh 2014, *PNAS*) |
| 030 | In WWOX, severity tracks **residual function**, not protein abundance | INFERENZA | genotype logic / P7 threshold | T2 | in observation | BATCH_20260710_A synthesis |
| 031 | It is a **DEE, not an EE**: seizure control does not save development | INFERENZA | clinical spectrum / strategy | T1 conceptual | in observation | BATCH_20260710_A synthesis |
| 032 | **Haploinsufficiency is not deleterious**: the therapeutic threshold sits well below full restoration | INFERENZA | P7 / threshold | T2 | in observation | BATCH_20260710_A synthesis |
| 033 | Biallelic null WWOX carries higher mortality than genotypes with at least one missense, but genotype class is only a noisy proxy for residual function | DATO+IPOTESI | genotype–phenotype / prognosis | T1 nominal / T3 effective | in observation | Oliver 2023 / Johannsen 2018 / Banne 2021 |
| 034 | In a post-mitotic excitable neuron under metabolic stress, WWOX up-regulation is pro-oxidant: the sign of WWOX↔ROS is context-dependent, not monotonic | DATO (photoreceptor) + ESPANSIONE (any transfer) | P5 redox / P1 Ca²⁺ | T3 ⚠️ genotype caution | in observation | PAPER 054 (Saadane 2021) |
| 035 | WWOX is a direct, residue-mapped inhibitor of GSK3β via an Axin-like SDR motif (388–407 / L404); S9-independent, Tau-dependent output | DATO (5 orthogonal assays) + INFERENZA (transfer) | P1 neurodevelopment / SDR function | T2 mechanistic | in observation | PAPER 056 (Wang 2012) |
| 036 | A systemic Wwox-null mouse at P18 is metabolically decompensated, so any brain phenotype in that window carries a quantified systemic confounder | DATO (measures) + INFERENZA (scope as confounder) | P5 metabolism / kidney — cross-cutting | T3 methodological | in observation | PAPER 057 (Ludes-Meyers 2009) |
| 037 | The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, EEG-documented, and is explicitly absent in Wwox-null mice | DATO | P2 excitability / epileptogenesis | T2 vulnerability / T3 phenotype transfer | in observation | PAPER 058 (Suzuki 2009) + PAPER 059 (Suzuki 2007) |
| 038 | Elevated BUN and creatinine recur across Wwox rodent models with two competing explanations — renal insufficiency or seizure-driven hypercatabolism — neither ever tested | DATO (measures) + IPOTESI (both explanations) | P5 metabolism / kidney | T3 open question | in observation | PAPER 059 (Suzuki 2007) + PAPER 057 (Ludes-Meyers 2009) |
| 039 | Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95% versus 0% — and it is not cerebellar | DATO | P1 neurodevelopment / motor function | T3 | in observation | PAPER 059 (Suzuki 2007) |

**Cross-cutting strategic implication.** CLAIM 031 + CLAIM 032 together state that (a) **only causal levers** can change the developmental outcome and (b) those levers **need not restore 100 %** of function. The portfolio narrows and the threshold drops.

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
- **Epigenetic option (future / ESPANSIONE):** dCas9/CRISPRa upregulation of endogenous WWOX for **hypomorphic** states — potentially relevant where a residual-function missense allele is present; not actionable now.
- **First-in-human (background / observation):** a WWOX gene therapy reported as administered to an infant with WWOX epilepsy (ICV route). The strongest external signal on the gene-therapy axis; peer-reviewed clinical data awaited. **NOT a datum.**

---

## Changelog

| Date | Version | Change | Driver | Confidence |
|------|---------|--------|--------|-----------|
| 2026-03-28 | v1.0 | Baseline established | Session consolidation | High |
| 2026-03-28 | v1.1 | BLOCK 2 mirror: CLAIM 011, 012 added | Obeid 2026 / Sapuppo 2026 — Scholar pre-scan | Moderate |
| 2026-03-29 | v1.2 | BLOCK 2: CLAIM 001 → conflicting evidence; CLAIM 011/012 integrated (full text closed); CLAIM 013 added; genotype-class framework added; gene-therapy context updated with Obeid 2026 full data; surveillance expanded (respiratory, ophthalmic, EEG priority); Q230P SDR mechanism added to genotype rules; BLOCK 1 inference set expanded; BLOCK 3 vigabatrin note updated | Weekly report consolidation | High for BLOCK 2; BLOCK 1 operationally unchanged |
| 2026-04-10 | v1.3 | Bootstrap: BLOCK 2 mirror expanded with CLAIM 014–020; prenatal-structural and GABA-tension interpretation added | Bootstrap consolidation | High |
| 2026-04-12 | v1.4 | Structural propagation: CLAIM 014 refined, CLAIM 015 promoted to consolidated baseline, CLAIM 016 reframed as amplifier-node logic | Structural / developmental / myelin core | High |
| 2026-04-17 | v1.6 | Mechanistic Architecture section added (network-state pathology, prenatal architecture, routing/scaffold, domain cooperativity, metabolic branch, HYAL-2 research branch, cross-pathway caution); BLOCK 2 expanded with CLAIM 021–028 | Papers 181–220 deep dive | High for BLOCK 2 |
| 2026-04-17 | v1.7 | CLAIM 028 refined with paper 218 quantitative p73-binding support; ATM/DDR axis added as CLAIM 029 | Papers 218 / 138 propagation | Medium-high |
| 2026-06-09 | v1.7.1 | Supplementary commit (lint): CLAIM 020 restored to the BLOCK 2 mirror — present in the claim registry, missing from the mirror. No content change | Consistency lint | High (mechanical alignment) |
| 2026-06-14 | v1.7.2 | Status normalization: 9 non-standard claim statuses brought to the standard vocabulary in both registry and mirror (011/012/021/022/023/024 → consolidated baseline; 025/026 → in observation; 028 → flagged for review; 013 → in observation) | Consistency lint (claim-status vocabulary) | High (vocabulary alignment) |
| 2026-06-18 | v1.8 | Obeid 2026 review integrated (PAPER 029): corroborates CLAIM 002/011/013/016/019/020/028; CLAIM 025 nuanced (HIF1α-independent tension); paper 210 identified as Breton 2021; gene-therapy context gains design principles + DRG safety + dCas9-hypomorphic option + first-in-human (background); 5 new primaries queued + first-in-human watch | Obeid 2026 deep dive | High for BLOCK 2 |
| 2026-06-28 | v1.8 | Metadata reconciliation (no bump): Sapuppo preprint → peer-reviewed (*Curr Issues Mol Biol*); PAPER 010 stub → full-text-reviewed, `background_only` reconfirmed | Paper-update commit candidates | High (metadata alignment) |
| 2026-06-28 | v1.8 | Wikilink retrofit (no bump): corpus-paper 138 promoted to PAPER 030 (Abu-Odeh 2014, *PNAS*) to anchor CLAIM 029; resolves 1 of 9 missing-wikilink warnings | Wikilink retrofit | High (structural anchor) |
| 2026-07-05 | v1.8 | Source normalization only (no bump): CLAIM 021 anchored to PAPER 031 (Breton 2021 full text); CLAIM 026 anchored to PAPER 032 (Hussain 2018 full text) | Source-normalization candidates | Medium-high (audit trail strengthened) |
| 2026-07-10 | v2.0 | **URGENT category 5** (retraction/invalidation): primary PMID 28151481 marked retracted/invalidated in tracking; the dependent review PMID 28045433 downgraded to `background only / dependency-contaminated`; the line excluded from corroboration of the HIF1α/WWOX branch. No claim or clinical block depended on the source | Retraction handling | High for editorial integrity; no new clinical datum |
| 2026-07-10 | **WM_v2.1** | **BATCH_20260710_A (MINOR) — WM_v2.0 → WM_v2.1_2026-07-10.** New papers: 039 (Steinberg 2021 organoids), 041 (Johannsen 2018, Q230P), 042 (Mallaret 2014, P47T/G372R), 045 (Shaukat 2018, West/DEE); PAPER 011 identifier normalized. New claims `in observation`: **030** severity tracks residual function, not abundance; **031** it is a DEE, not an EE; **032** haploinsufficiency is not deleterious. CLAIM 019 updated (Johannsen promotes to DATO only the endpoint `normal transcript + protein not detected`); CLAIM 001 corroborated on both sides, `conflicting evidence` confirmed. BLOCK 1 unchanged | Batch deep dive | High |
| 2026-07-14 | **v3.0** | **BATCH_20260714_001 (MAJOR — baseline reversal).** See the repair section below | Canonical repair of CLAIM 019 | High |
| 2026-07-25 | **v3.1** | **BATCH_20260725_001 (MINOR — canonical synchronization).** CLAIM 033 restored to the BLOCK 2 mirror; CLAIM 028 source pointer corrected 213→207 across canonical and meta surfaces; no scientific or clinical-policy change | Public audit + manual operator trigger | High (cross-file evidence) |
| 2026-07-26 | **v3.2** | **BATCH_20260726_001 (MINOR — 3 commit candidates propagated).** New papers, all read in full with persisted receipts: **054** (Saadane 2021, photoreceptor Ca²⁺/calpain/WWOX), **055** (Rotem-Bamberger 2022, WW2 tandem cooperativity — the identified primary source behind CLAIM 024), **056** (Wang 2012, WWOX ⊣ GSK3β via L404). New claims `in observation`: **034** the sign of WWOX↔ROS is context-dependent; **035** WWOX is a residue-mapped direct inhibitor of GSK3β. **016** enriched: reframed from "GSK3β elevated" to "GSK3β de-repressed", with a `PREMISE_TAG` on the abundance-reports-activity assumption. **024** given its identified source, placeholder CORPUS P204 preserved unmerged. **009** carries a mandatory counter-directional note and stays `in observation` (the studies are not comparable, so no escalation to `conflicting evidence`). Mechanistic architecture: "Domain cooperativity" sharpened; new section on measurable SDR function and the 388–407/L404 no-touch zone. **No baseline reversal, no BLOCK 1 change, no therapeutic recommendation** | Batch deep dive (3 candidates) + manual operator trigger | High for BLOCK 2; BLOCK 1 unchanged |
| 2026-08-06 | **v4.0** | **BATCH_20260806_001 (MAJOR — safety-language removal from a baseline claim).** PMID 30290271 read in full (receipt `FTR-20260806-30290271-01`; 21 verbatim locators, 7 of them anchored to figure panels). **CLAIM 005** narrowed to what the source measures and its clinical meaning *"Supports caution with strong GABAergic burden"* **deleted**: the study tests no drug, no GABA concentration, no inhibitory current and no E/I ratio, so the caution was never its result — it was a marker→function→medication chain nobody had written down as an inference. The datum is not demoted (`consolidated baseline` / `DATO` retained); what is removed is a policy sentence that had no source. Evidence boundary recorded on the claim: PV is lower in DG, CA1 **and the whole hippocampus (−44%)**, NPY **only in DG**, CA1/CA3 show no obvious difference and the whole-hippocampus NPY panel carries **no significance marker** — a visual panel reading, not a reported test. Only `Il6`, not `Tnf-a`, is significant. Early death and epileptogenesis in this model are **imported premises** (PMID 19936220, Mallaret 2014), not re-measured here → `FT-043`. **PAPER 006** / **LIT-006** identifiers normalized; `CORPUS-STUB-085` resolved as duplicate, preserved append-only. Publication-integrity audit of the 7 held records run first: no canonical claim rests on any of them. **No new therapeutic recommendation; BLOCK 1 unchanged** | Full-text deep dive + operator authorization | High for BLOCK 2 and for source-level safety discipline |
| 2026-08-06 | **v4.1** | **BATCH_20260806_002 (MINOR — 4 commit candidates propagated).** The imported-premise chain under CLAIM 005 traced end to end, every link read in full with persisted receipts: **PAPER 057** (Ludes-Meyers 2009, PMID 19936220, `FTR-20260806-19936220-01`), **PAPER 058** (Suzuki 2009, PMID 19500159, `FTR-20260806-19500159-01`), **PAPER 059** (Suzuki 2007, PMID 17803050, `FTR-20260806-17803050-01`). 🔴 **The premise was not merely unsupported — its terminus contradicts it.** PMID 19936220 measures no epileptogenesis in any form (no EEG, seizure, behaviour or brain histology; its only brain measurement is organ weight), and PMID 19500159 states in three places, plus a Table 2 whose `Epilepsy` row is **empty for both mouse models**, that Wwox-null **mice show no epilepsy**. Early death, co-cited in the same sentence, **is** first-hand — which is why the sentence read as verified. Four claims added `in observation`: **036** systemic metabolic decompensation of the P18 mouse null as a quantified confounder for any brain phenotype in that window, with `PREMISE: DEFAULT_FROM_TEXTBOOK` on brain ablation never being shown; **037** the seizure phenotype as a rat `lde/lde` phenotype, EEG-documented, with the allele corrected to *structurally a C-terminal frameshift, functionally a protein-level null*; **038** the recurring BUN/creatinine signature with **two competing untested explanations**, renal insufficiency versus seizure-driven hypercatabolism, the second of which competes directly with the renal-tubular-acidosis hypothesis PMID 19936220 proposed for the mouse and never considered; **039** ataxia at 95% versus 0%, non-cerebellar, the most penetrant phenotype of the model and one the downstream literature dropped entirely. 🔴 **PAPER 021 metadata corrected:** the author is **Tochigi**, not Kumada, and the record carried an **invented title naming *lissencephaly*** — a word absent from the paper — which had been steering it toward a migration/layering reading the study does not make; CLAIM 014/015 now state it contributes early postnatal maturation (PND5–21), not prenatal assembly. Method note recorded on LIT-0405: this paper's abstract was supplied first and refused as a reading; had it been accepted, *"decreased plasma GH"* would have entered the model as a datum, and its own body reports the difference as **not significant**. **No baseline reversal, no BLOCK 1 change, no therapeutic recommendation** | Three full-text deep dives + one metadata correction, operator authorised | High for BLOCK 2 and for citation-provenance discipline |

---

## BATCH_20260714_001 — WM_v2.1 → **WM_v3.0_2026-07-14** (MAJOR)

**Baseline reversal.** The equation `normal mRNA + absent protein = post-translational degradation` is **withdrawn**. Johannsen 2018 explicitly states two alternatives: impaired translation **or** premature degradation.

**Consequences:**
- CLAIM 019 retains the human datum on the exact variant, but downgrades the *cause* to unresolved;
- CMA, the `LRSVQ` motif and the helix-lid model remain hypotheses transferred from P252A/AlphaFold, **not** a Q230P mechanism;
- C299R is withdrawn as a validated catalytic / off-lid control;
- the first experimental gate must separate **synthesis, insolubility and turnover**; abundance and function must be measured together;
- an SDR stabilizer is `conditional / not design-ready`.

**Unchanged:** the human Q230P phenotype, the genotype classification, the BLOCK 1 clinical logic, and the primary Johannsen / Zhang data. **No clinical indication derives from this repair.**

> This reversal — retracting a plausible, already-consolidated conclusion the moment the evidence no longer uniquely supported it — is the worked example behind the premise/false-negative discipline in [`../../../framework/instruction/epistemic_discipline.md`](../../../framework/instruction/epistemic_discipline.md).
