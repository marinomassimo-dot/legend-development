# WWOX Therapeutic Translation — Mechanism → Intervention Map

**A causally explicit map from WWOX mechanisms to candidate interventions.** Each entry carries a
verifiable chain: *mechanism → actionable node → intervention → expected mechanistic effect →
evidence → transfer distance → CNS/developmental plausibility → safety constraints → repurposing
maturity → decisive missing evidence.*

> **Status:** non-canonical analysis artefact, same class as
> [`variant_triage_rescuability.md`](variant_triage_rescuability.md) (mechanism → lever) and
> [`therapy_levers.md`](therapy_levers.md) (literature-anchored levers).
> **READ-ONLY toward the four scientific current files.** Nothing here modifies a claim, a paper
> record, the working model or the tracking log; anything promotable goes through
> INGEST → DEEP_DIVE → COMMIT.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is
> described. Specific alleles appear only as **decoupled worked examples** — a destabilizing SDR
> missense (p.Gln230Pro) on one side, a canonical splice-acceptor variant (c.1057-2A>G) on the
> other — carried independently, never combined into one person's genotype. Lever assignment is an
> **allele-level operation**.
>
> **Nothing here is medical advice.** No clinical indication is formulated anywhere in this file.
> Scientific evidence and therapeutic proposal are kept typographically and structurally separate:
> every candidate states what is *measured* before what is *proposed*.

> 🔴 **STRESS-TESTED — four conclusions in this file have moved.**
> [`therapeutic_translation_second_pass.md`](therapeutic_translation_second_pass.md) re-derives the
> conclusions that most affect prioritization. Read it before acting on any of the following:
>
> | This file says | The second pass finds |
> |---|---|
> | **N-01** — mTOR inhibition *"acts in the wrong direction"*; ranked #2 in `TOP_NEGATIVE_FINDINGS` | **`INSUFFICIENT`.** The datum has **no verbatim locator anywhere in this repository**, `EIF4EBP1`↓ inverts when read as biology, and the same list's autophagy direction contradicts it under the coupling needed to read either. The class stays out — the reason changes from *"wrong direction"* to *"never measured"* |
> | **§2.2** — `CORPUS-STUB-043` is *"the only other WWOX record naming mTOR"* | **False.** `CORPUS-STUB-177` (PMID 31966718) has been in the same registry throughout; and three registry stubs name WWOX↔autophagy in **two opposite directions** |
> | **CHAIN B** — scored **T2**; `E-1` is *"the highest-value, lowest-cost open item in the file"* | **`E-1` was already discharged.** Receipt `FTR-20260810-34634460-02` records that **d-APV abolishes the burst** in the WWOX-deficient slice ⇒ **T1 for the tool compound**. The gap-junction half **downgrades** (carbenoxolone blocks NMDAR and does not wash out), and the pannexin blocker went the **wrong way** — new **N-16** |
> | **CHAIN C / R-04** — lithium panel cited as **Fig. 7b**; *"GSK3β abundance elevated"* | **Fig. 7d** (7b is ethosuximide), and **neither cited source reports elevated abundance** — total GSK3β is flat; pSer9 falls. `CLAIM 016` and `CLAIM 035` **exclude each other** on the S9 axis |
> | **R-01** — the sole entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` | **`SPLIT`.** Retained for survival/SWD/motor/gliosis at HD in the P0–P5 window; **downgraded to `PROMISING_BUT_GAP`** for development, cognition, myelin-in-the-dose-study, the (under-transduced) cerebellum, and post-neonatal use |
>
> Ten canonical or tracker records are reported as affected. **None was edited by either file.**

---

## 0. What this file is, and what it refuses to be

**It is:** a causal map. Each intervention is admitted only if a reader can walk backwards from the
molecule to a WWOX measurement and see, at every step, whose data it is, in what system, and where
the chain stops being measured and starts being inferred.

**It is not:** a drug list. A ranked list of compounds with plausible mechanisms is precisely the
artefact this repository exists to refuse. Four of the entries below are **negative** — interventions
that survive a plausibility read and die on a directional, compartmental or developmental check —
and they are held to the same evidentiary standard as the promoted ones.

**Three hard rules inherited from the canonical layer, applied throughout:**

1. **`MARKER_TO_FUNCTION_GATE`** — marker abundance, lineage/survival, transmitter concentration and
   circuit function are four separate questions. A lever justified at one layer is not justified at
   the others ([[meta_gaba_paradox_current]]).
2. **Direction before candidate** — no intervention enters without its axis's *sign* resolved in the
   relevant compartment. The Wnt reversal ([[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]]) and the redox
   counter-direction ([[claim_registry_current#CLAIM 034]]) are the worked reasons.
3. **`MECHANISM_TRANSFER_FIREWALL`** — a comparator model is not a read-across bench. P47T is not a
   bench for a buried SDR missense; G372R is a natural-variant comparator, not a validated negative
   control ([`proteostasis_rationale.md`](proteostasis_rationale.md) §2, step 4).

---

## 1. Evidence ladder (T1–T6) — the levels never merge

| Tier | Definition | What may be said |
|---|---|---|
| **T1** | **Direct WWOX intervention evidence** — the intervention was applied to a WWOX-deficient system and the WWOX-dependent phenotype changed | "this intervention corrects this phenotype in this WWOX model" |
| **T2** | **WWOX mechanistic evidence + intervention in the same pathway**, but the two were never joined in one WWOX experiment | "the node is WWOX-dependent; the drug hits the node; nobody has run the conjunction" |
| **T3** | **Closely related genetic DEE evidence** — another monogenic DEE with a mechanistically comparable lesion | "the class responds; WWOX membership in the class is an assumption" |
| **T4** | **Broader neurological disease evidence** — MS, AD, PD, epilepsy in general | "the drug does something in a nervous system; the disease link is analogical" |
| **T5** | **Generic target pharmacology** — the compound engages the target in any system | "target engagement only" |
| **T6** | **Mechanistic hypothesis only** — no intervention datum anywhere on this axis | "a reason to run an experiment, nothing else" |

> **Tier is assigned to the *conjunction*, not to the drug.** Lithium is a T5/T4 compound with a
> T2 mechanistic rationale and a **failed** T1 specificity test — and it is scored on the failure,
> not on the rationale (§4, R-04).

**A rung that is easy to skip and must not be:** an intervention datum obtained in a WWOX model with
**no genotype-specific comparison** is not T1. It is evidence that the drug works in an animal that
has the phenotype — which is T5 dressed as T1. This distinction alone demotes the single strongest
repurposing signal in the prior literature synthesis (§4, R-04; §5, N-02).

---

## 2. Mechanism selection — what qualifies, and what was refused

**Admission gate.** An axis is admitted to therapeutic exploration only if (a) WWOX-dependence is
measured, not cited; (b) the *direction* of the perturbation is resolved in a compartment relevant
to CNS development; (c) a node exists that a molecule or modality can actually engage. Biological
interest is not admission.

### 2.1 Admitted

| # | Mechanism | Canonical support | Direction resolved? | Actionable node |
|---|---|---|---|---|
| **M1** | **Neuronal WWOX protein deficit** — neuron-restricted loss is sufficient to reproduce the phenotype; restoration rescues multiple domains | CLAIM 002 · CLAIM 003 · CLAIM 004 · CLAIM 011 · CLAIM 032 | ✅ loss → disease; restoration → rescue | WWOX protein level *in neurons* |
| **M2** | **Network-state pathology** — spontaneous neocortical bursting, altered oscillatory organization, ↑phase–amplitude coupling; bursting **depends on NMDAR and gap-junction activity** | CLAIM 021 · CLAIM 002 | ✅ hyperexcitable | NMDAR; connexin gap junctions |
| **M3** | **GABAergic / PV-interneuron dysfunction** — ↓PV⁺ markers (−44% whole hippocampus) and **functionally reduced spontaneous inhibition** in L2/3 pyramidal neurons, against ↑GABAergic markers in organoids | CLAIM 005 · CLAIM 021 · [[meta_gaba_paradox_current]] | ⚠️ **NOT resolved** — see §2.3 | chloride gradient (NKCC1/KCC2) — *unmeasured* |
| **M4** | **GSK3β de-repression** — WWOX is a **direct physical inhibitor** of GSK3β via an Axin-like docking motif at 388–407, L404 strictly required, S9-independent | CLAIM 016 · CLAIM 035 | ✅ loss → de-repression | GSK3β docking site (not the ATP pocket) |
| **M5** | **Wnt/β-catenin hyperactivation** — WWOX sequesters DVL2 cytoplasmically; loss de-represses. In WWOX-KO cerebral organoids: nuclear β-catenin ~1.7×, WNT ligands / LEF1 / AXIN2 ↑, partially recovered by W-AAV | [[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]] · [[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]] · TX-004 | ✅ **hyper**-activation (a reversal of the first reading) | tankyrase / Wnt–β-catenin |
| **M6** | **HIF1α → PDK1 → PDH block** — WWOX binds HIF1α **via WW1**; loss de-represses HIF1α in normoxia; PDK1, GLUT1, HK2, PKM2 measured up; OXPHOS↓/glycolysis↑ signature reproduced in **human** cerebral organoids | [[discovery_ledger_current#DL-MECH-020 — WWOX-loss induce un fenotipo Warburg-like via HIF1α: razionale meccanicistico WWOX-specifico per la dieta chetogenica|DL-MECH-020]] · [[discovery_ledger_current#DL-BIO-007 — Lattato sierico, glicemia e insulina come biomarcatori metabolici in vivo del deficit di WWOX|DL-BIO-007]] · [[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]] · CLAIM 009 | ✅ in model systems · ❌ **not in patients** (§5, N-06) | pyruvate entry into the TCA cycle |
| **M7** | **Allele-level protein failure (SDR missense class)** — normal transcript, protein not detected; severity tracks residual **function**, not abundance | CLAIM 019 · CLAIM 030 · HYP-08 | ⚠️ bottleneck unidentified (synthesis vs solubility vs turnover) | WWOX folding / turnover / function |
| **M8** | **Splice-allele failure (canonical acceptor class)** — acceptor abolished (SpliceAI 0.96; MaxEntScan 7.28 → −0.67), cryptic acceptor gain at +8 | CLAIM 018 · [`variant_triage_rescuability.md`](variant_triage_rescuability.md) | ✅ null-like allele | the DNA base itself |
| **M9** | **Myelination failure** — neuronal deletion → hypomyelination with OPCs present; **oligodendrocytes never transduced** by the rescuing vector, yet myelin improves | CLAIM 003 · CLAIM 004 | ✅ largely **secondary to the neuron** | the neuron, not the oligodendrocyte |
| **M10** | **Neuroinflammation / glia** — ↑IBA1/GFAP area fraction; gliosis **reduced by neuron-restricted rescue** | CLAIM 005 · CLAIM 006 · [[discovery_ledger_current#DL-MECH-012 — WWOX è un *freno* del segnale infiammatorio: la sua perdita de-reprime microgliosi/astrogliosi e cascata citochinica (asse Aldaz, multi-tessuto)|DL-MECH-012]] | ✅ de-repressed, but **downstream** | IL-1β/NLRP3, NF-κB, microglia |

### 2.2 Refused admission (biologically interesting, therapeutically not a target)

- **mTOR / circuit signalling.** Explicitly named in the assignment, and it does **not** qualify. The
  only WWOX-specific measurement that touches mTOR is the WWOX-KO cerebral-organoid transcriptome,
  where **mTOR/EIF4EBP1 is DOWN and autophagy is DOWN**
  ([[discovery_ledger_current#🎯 DL-MECH-034 — Il fenotipo Warburg è confermato **in tessuto neurale umano**: chiude il gap che indeboliva l'ipotesi chetogenica|DL-MECH-034]]). An mTOR inhibitor — the reflex repurposing move in
  genetic DEE, imported from TSC — would push the **same direction as the lesion**. The only other
  WWOX record naming mTOR is `CORPUS-STUB-043` in the paper registry (an LPS lung-injury study),
  status `not_processed`: **nobody has read it, so it cannot carry a direction** and is not cited
  here as evidence for or against. See §5, N-01. **This is the single most consequential negative
  in the file.**
- **Senolytics.** CLAIM 010 is `background only` / `IPOTESI`, with no WWOX model and no CNS anchor.
- **DNA-damage-response / ATM.** CLAIM 029 is `in observation` and structurally important, but the
  therapeutic direction is inverted for a developing brain: WWOX loss causes progenitor
  proliferation **with** loss of the apoptotic checkpoint ([[discovery_ledger_current#DL-MOL-010 — Il banco per testare HYP-08 esiste già. Manca un solo reagente, e il genotipo di riferimento lo possiede.|DL-MOL-010]]) —
  restoring checkpoint competence pharmacologically in a proliferative developmental compartment has
  no safe formulation.
- **ECM / HYAL-2 / SMAD4.** CLAIM 027, explicitly *not promoted to a central pathway*.
- **Calpain.** Rejected as an established WWOX turnover route (DIS-008): no proteolysis was ever
  measured, and the direction is inverted for a substrate.

### 2.3 The axis that is admitted but whose *direction is not resolved* — and why it matters most

**M3 (GABA/PV) is admitted as a mechanism and refused as a target**, and the two must not be
collapsed. What is measured: reduced PV⁺ and (DG-only) NPY⁺ marker counts in **one** systemic
constitutive KO at two weeks; reduced GAD65/67 protein; and — independently, at the functional
level — **reduced spontaneous inhibition** in L2/3 pyramidal neurons under neuron-specific loss
(CLAIM 021). What is **not** measured, in any WWOX model, by anyone: `E_GABA`, intracellular
chloride, NKCC1/KCC2, the GABA response itself, or GABA pharmacology
([[research_candidates_current#RC-001 — NKCC1/KCC2 / chloride-gradient biology in WWOX models|RC-001]]; [[meta_gaba_paradox_current]] Open Question 2).

"Depolarizing GABA" is therefore `IPOTESI` — the authors' reading of a marker pattern against the
developmental literature — and **not** `DATO` of any WWOX study
([[discovery_ledger_current#DL-MECH-035 — GABA depolarizzante negli organoidi WWOX-KO: perché gli antiepilettici standard sottoperformano|DL-MECH-035]]). Two further constraints bind:

- **The systemic-null confounder.** That animal at P14–P18 is metabolically decompensated —
  hypoglycaemic, acidotic, uraemic, hypocalcaemic, leukopenic, anaemic (CLAIM 036). Hypoglycaemia and
  acidosis independently alter interneuron marker expression and glial reactivity. **The design
  cannot separate** cell-autonomous neuronal loss from secondary metabolic injury. The conditional
  allele that would separate them has existed since 2009 and has not been used in this direction.
- **The mechanism does not predict the outcome.** The depolarizing-GABA rationale predicts that
  GABAergic drugs underperform. In a published WWOX-null child, **vigabatrin resolved the spasms**
  (CLAIM 001, CLAIM 031). The mechanism survives as a mechanism; as a clinical predictor it was
  falsified, and the failure is recorded as `FM-018`.

⇒ A chloride-gradient intervention (bumetanide) sits at **T6** for WWOX: its load-bearing premise
has never been measured in a WWOX system. See §4, R-07 and §5, N-04.

---

## 3. The map — mechanism to intervention, chain by chain

Each chain is written so that the link where measurement stops is visible.

### CHAIN A — restore neuronal WWOX (M1)

```
WWOX biallelic LoF
  → neuronal WWOX protein absent/insufficient          [CLAIM 019, CLAIM 030 — measured]
  → neuron-restricted loss reproduces the whole phenotype, myelin included
                                                        [CLAIM 003 — Synapsin-Cre; Olig2-Cre and
                                                         GFAP-Cre produce no evident anomaly]
  → ACTIONABLE NODE: neuronal WWOX protein level
  → INTERVENTION: AAV9-hSynI-WWOX (gene addition, genotype-agnostic)
  → EXPECTED EFFECT: survival, growth, glycaemia, behaviour, ataxia, myelination, gliosis,
    SWD/ECoG                                            [CLAIM 004, CLAIM 011 — measured in the
                                                         Wwox-null mouse]
  → THRESHOLD: haploinsufficiency is not deleterious; the lethal/viable threshold sits BELOW 50%
                                                        [CLAIM 032 — mouse, rat, and every
                                                         published human family]
```

**Where the chain stops being measured — four boundaries, all canonical:**

1. **Dose is a threshold, not a continuum.** Low dose 1.23 × 10¹¹ vg does **not** rescue survival —
   it moves death from ~20 to ~90 days and the curve then reaches zero; high dose 2.63 × 10¹¹ vg
   plateaus at ~80% to day 300. At P20 the low dose had not corrected hypoglycaemia. Any inference
   of the form *"a lower, safer dose would still help"* is **refused by Figure 3B** for survival in
   this model (CLAIM 011, `flagged for review`).
2. **Rescue ≠ normalization.** Where the rescue is compared against wild type, the comparison is
   either untracked or significant **against** the rescue: g-ratio normalizes; unmyelinated axons
   per field do not (~26 in WT vs ~52 in treated, `**`). Myelinated axons, CC1⁺ and PDGFRα⁺ run
   WT-vs-KO and KO-vs-rescued, leaving the residual gap untested (CLAIM 004).
3. **The window.** The efficacious window is P0–P5 in mouse (≈ human perinatal), and the stated
   reason is model survival; post-natal dosing is explicitly future work. Neuronal gene therapy
   rescues excitability and function but does **not** repair the progenitor/radial-glia defect,
   which is largely prenatal (TX-007 window caveat, CLAIM 014, CLAIM 015).
4. **The threshold is known for survival and morphology — not for cognition or epilepsy.** Nobody has
   measured how much WWOX neurodevelopment requires, and haploinsufficiency is tolerated *from
   birth*, whereas a rescue arrives after part of the developmental damage (CLAIM 032, CLAIM 031).

### CHAIN B — the network node (M2)

```
neuron-specific WWOX loss
  → ↑excitatory drive, ↓spontaneous inhibition, depolarization, ↑firing, ↑sag,
    post-inhibitory rebound in L2/3 pyramidal neurons   [CLAIM 021 — measured]
  → spontaneous bursting, altered oscillatory organization, ↑phase-amplitude coupling
  → bursting DEPENDS ON NMDAR activity and gap junctions [CLAIM 021 — dependence stated]
  → ACTIONABLE NODE: NMDAR · connexin gap junctions
  → INTERVENTION: memantine (approved) · MK-801/APV (tools) · carbenoxolone (tool)
  → EXPECTED EFFECT: ↓ burst frequency/amplitude, ↓ phase-amplitude coupling
```

🔴 **An unresolved locator question that changes the tier.** The registry records that bursting
*depends on* NMDAR and gap-junction activity, but does **not** record whether that dependence was
established **pharmacologically** (blockers applied to the WWOX-deficient system — which would make
the acute anti-bursting effect a T1 datum for the tool compounds) or by another route. The
distinction decides whether Chain B is a **T1 chain with a translation gap** or a **T2 chain with an
untested conjunction**. It is scored **T2** here, deliberately conservatively, and the resolution is
a single re-read of PMID 34634460 with verbatim locators. **This is the highest-value, lowest-cost
open item in the file.**

**Human-genetics corroboration of the node:** GRIN2A — an NMDAR subunit — sits among the genes
producing the same burst-suppression phenotype ([[discovery_ledger_current#DL-MECH-002 — GRIN2A nel cohort BS: corroborazione human-genetics del nodo NMDAR|DL-MECH-002]]).
**Differential:** the same cohort logic assigns sodium-channel blockers to the Nav channelopathies
(KCNQ2-GoF, SCN2A) and **not** to WWOX, whose node is different
([[discovery_ledger_current#DL-REPO-001 — Na-channel blockers: leva per le channelopatie BS, NON per WWOX (differenziale terapeutico)|DL-REPO-001]]) — see §5, N-03.

### CHAIN C — the GSK3β docking site (M4)

```
WWOX loss
  → loss of a PHYSICAL brake on GSK3β (not merely a level change): Axin-like docking motif
    388-407, L404 strictly required, S9-INDEPENDENT     [CLAIM 035 — residue-resolved]
  → GSK3β output rises while GSK3β abundance and phospho-S9 stay unchanged
  → MEASUREMENT WARNING: de-repression is INVISIBLE to the standard phospho-S9 western
  → ACTIONABLE NODE: the Axin/FRAT/GSKIP docking site — NOT the ATP pocket
  → INTERVENTION: (a) lithium — see the specificity failure below; (b) an Axin-site ligand
  → EXPECTED EFFECT: restore Tau S396/S404 phosphorylation control, microtubule assembly,
    neurite outgrowth
```

🔴 **The specificity failure that governs this chain.** Lithium suppressed PTZ-induced seizures in
**all three genotypes, wild type included** (Fig. 7b). For ethosuximide the same paper explicitly
declares `n.s.` in `+/+` and `+/−` and significance in `−/−`; for lithium it declares no converse.
⇒ **The experiment does not establish a WWOX-specific pharmacological rescue.** It shows an
anticonvulsant working in a model that has seizures (CLAIM 016, evidence boundary). A published
review transmitted the genotype-specific reading that the primary's panel does not support.

🔴 **And the safety argument is separately rejected.** A WWOX-mimetic peptide (WWOXtide³⁸⁸⁻⁴⁰⁷) was
argued to be *safer than lithium because WWOX inhibits GSK3β substrate-selectively*. **False:** the
same paper's Supplementary Figure C shows WWOX inhibiting GSK3β-dependent phosphorylation of
**GS-1** — a glycogen-synthase peptide unrelated to Tau — to ~18% of control (L404A ~87%). The
interaction is a **generic docking-site block**, not substrate selectivity (DIS-009). The
mechanistic rationale for TX-005 strengthens; **its SAFETY score does not**.

🟢 **What re-opened, on a different axis, hours later.** GSK-3 is three enzymes; **Axin associates
more readily with β1 than with β2**, and the source concludes that *"GSK-3 inhibitors that target the
Axin-binding site in GSK-3 will preserve the beneficial effects of GSK-3β2 on axon growth"*. WWOX
binds **precisely that site**. Tau is a **disfavoured** substrate for β2, and the discriminant is the
C-terminal tail: an **ATP-competitive inhibitor cannot separate the isoforms; an Axin-site ligand
can** ([[discovery_ledger_current#DL-MECH-067 — 🔑 WWOX lega **il sito di Axin**, ed è quindi la classe di inibitore che la letteratura raccomanda per **risparmiare** l'isoforma neuronale|DL-MECH-067]], [[discovery_ledger_current#DL-MECH-068 — 🔑 **tau è un substrato SFAVORITO per β2**, e il discrimine è la coda C-terminale: un inibitore ATP-competitivo **non può** separare le isoforme, un ligando del sito di Axin sì|DL-MECH-068]]). This is
**isoform** selectivity, not substrate selectivity — a different claim from the rejected one, and it
is the most interesting open therapeutic hypothesis on this axis (§7, NEW_HYPOTHESES H-1).

### CHAIN D — the Wnt axis, with its sign corrected (M5)

```
WWOX sequesters DVL2 in the cytoplasm                   [multi-source, oncological context]
  → WWOX loss DE-REPRESSES Wnt/β-catenin
  → in WWOX-KO cerebral organoids: nuclear β-catenin ~1.7x; WNT1/2B/3/3A/5A/8B, LEF1, AXIN2 up;
    partially recovered by W-AAV                        [DL-MECH-034 — human neural tissue]
  → ACTIONABLE NODE: tankyrase / Wnt-beta-catenin
  → INTERVENTION: Wnt inhibitor (e.g. tankyrase inhibitor). NOT lithium.
  → EXPECTED EFFECT: normalize cortical layering / MYC tone
```

⚠️ **The reversal is the finding.** Lithium was the first-named candidate on this axis and is
**mechanistically contra-indicated here**: lithium stabilizes β-catenin and therefore *activates*
Wnt, worsening a hyperactivation ([[discovery_ledger_current#DL-MOL-003 — Asse Wnt: direzione RISOLTA (WWOX-loss → IPER-attivazione) → leva = INIBIZIONE Wnt; ⚠️ litio CONTRO-indicato dal meccanismo|DL-MOL-003]]). Lithium is thus
directionally conflicted **across two admitted axes at once** — a plausible GSK3β rationale on M4, a
harmful direction on M5. **A single compound cannot be scored on its best axis.**

⚠️ **Allele-level consequence.** WWOX's anti-Wnt function is **WW-scaffold** (DVL2 sequestration),
not enzymatic ([[discovery_ledger_current#DL-MECH-008 — La funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica → potenzialmente *risparmiata* dalla variante SDR del genotipo di riferimento|DL-MECH-008]]) — so an SDR-domain missense may leave this
axis **partially preserved**, while a null allele does not. The same logic applies to M6: WWOX binds
HIF1α **via WW1**, not the SDR ([[discovery_ledger_current#DL-MECH-028 — WWOX lega HIF1α via **WW1**, non via SDR: l'asse metabolico potrebbe essere parzialmente preservato in Q230P|DL-MECH-028]]). **Downstream levers are
not uniformly genotype-agnostic**; only gene addition is.

### CHAIN E — the metabolic bypass (M6)

```
WWOX loss
  → HIF1alpha de-repressed in normoxia                  [measured, MEF + cancer]
  → PDK1 up (with GLUT1, HK2, PKM2)                     [qRT-PCR, Wwox-KO — the key enzyme is
                                                         MEASURED, not inferred]
  → PDK1 inhibits PDH -> pyruvate blocked at the TCA entry
  → human WWOX-KO cerebral organoids: OXPHOS/ATP-synthesis inhibited, glycolysis enriched
                                                        [RNA-seq, GSE156243 — transcriptome, NOT flux]
  → ACTIONABLE NODE: TCA entry, DOWNSTREAM of PDH
  → INTERVENTION: ketogenic diet (ketone bodies enter as acetyl-CoA below the block)
  → EXPECTED EFFECT: restore oxidative flux without reactivating PDH
```

⚠️ **Three brakes, all canonical, all pointing the same way:**
- **The transcriptome is not the flux.** `n=2` WT vs `n=4` KO; EV tables select on raw `P<0.01`. No
  Seahorse, no fluxomics, in any WWOX system.
- **Human metabolism is normal, and it was checked four times.** Lactate, ammonia, acylcarnitines,
  uric acid, homocysteine, plasma amino acids, urinary organic acids, transferrin isoforms — normal;
  a complete metabolic and mitochondrial screen including muscle biopsy — normal; MRS — normal. The
  single outlier (cerebral lactate *"extremely low"*, the opposite of the Warburg prediction) carries
  a confounding second variant in HSPG2 ([[discovery_ledger_current#DL-BIO-009 — Il metabolismo umano nel deficit di WWOX è, per quanto misurato, **normale**. Il modello murino non si trasferisce.|DL-BIO-009]],
  [[discovery_ledger_current#⚠️ DL-BIO-008 — Contraddizione sul lattato: alto nel siero del topo, **"extremely low" nell'MRS cerebrale umana**|DL-BIO-008]]). **Do not look for confirmation in blood: it has been
  looked for four times and it is normal.**
- **The real-world continuation signal runs against the rationale.** Ketogenic diet was tried in 3
  WWOX-DEE patients and continued in 1; cannabidiol was continued in 4/4 who started it. In a severe
  WOREE case the ketogenic diet is listed among the *ineffective* interventions alongside eleven
  drugs and three ACTH cycles ([[discovery_ledger_current#DL-MOL-007 — Fallimento sistematico degli ASM sintomatici in WOREE severo → priorità alle leve disease-modifying|DL-MOL-007]]).

⇒ The KD rationale is **not falsified** — it rests on the PDK1→PDH block and depressed OXPHOS, not on
lactate — but the easiest endpoint for verifying it has been lost, and the expectation of benefit
must be calibrated **down**. The only test that can still falsify it is **Seahorse OCR/ECAR on
donor-derived cells**; if that is normal, the hypothesis falls (HYP-20260709-01).

### CHAIN F — allele-level protein rescue (M7), and CHAIN G — allele-level sequence correction (M8)

These two chains are **deliberately not combined**. Lever assignment is per allele.

**Chain F (SDR missense worked example, Q230P):**
```
normal transcript + protein NOT DETECTED in patient fibroblasts     [measured]
  → cause UNRESOLVED: impaired translation OR insolubility OR premature degradation
                                                        [the source does not discriminate]
  → severity tracks residual FUNCTION, not abundance    [CLAIM 030 — allelic series:
                                                         P47T normal protein + abolished PPxY -> MILD;
                                                         G372R barely detectable -> MILD;
                                                         Q230P absent -> SEVERE]
  → ACTIONABLE NODE: folding / turnover / function - which one is UNKNOWN
  → INTERVENTION: conditional, none design-ready
```
🔴 **Three of the four steps of the original chaperone rationale were retracted**: the ΔΔG
"recoverability band" has no demonstrated predictive value for WWOX (nothing to calibrate it
against); the "misfolding-dominant" tally inherits its meaning from that band and measures nothing;
and P47T is not a read-across bench. **Step 1 stands**: Q230 is buried core (relSASA 0.000, α-helix,
27 Cα neighbours within 10 Å) and **not itself a catalytic residue** — which licenses a question, not
an answer ([`proteostasis_rationale.md`](proteostasis_rationale.md) §2).

🔴 **A design constraint that is now `DATO`-backed:** the canonical **ERLIQ 402–406** degron contains
**L404**, strictly required for the demonstrated GSK3β inhibition. Any ligand stabilizing WWOX by
clamping that region risks **rescuing abundance while abolishing function** — the "stable but inert"
trap, with an experimentally identified victim function (working model, *SDR-domain function is
measurable*). In WWOX, **stability and function are in structural tension: stability is bought with
occlusion** ([[discovery_ledger_current#DL-MECH-049 — In WWOX **stabilità e funzione sono in TENSIONE STRUTTURALE**: la stabilità si compra con l'occlusione. Vincolo di progetto per qualunque stabilizzatore di Q230P.|DL-MECH-049]]).

**Chain G (canonical splice-acceptor worked example, c.1057-2A>G):**
```
acceptor abolished (SpliceAI acceptor-loss 0.96; MaxEntScan 7.28 -> -0.67), cryptic gain +8 (0.64)
  → ACTIONABLE NODE: the DNA base itself
  → SSO/ASO: REFUTED MECHANISTICALLY - splice-switching oligos MASK elements; they do not
    CREATE splice sites, and there is nothing to unmask that returns the wild-type transcript
  → in-frame skipping: IMPOSSIBLE - exon 9 is the LAST exon; it carries the stop codon and the
    final ~62 aa of the SDR
  → U1/ExSpeU1: NOT APPLICABLE - they correct DONORS (5'); an acceptor is read by U2AF/U2 snRNP
  → ADAR RNA editing: WRONG DIRECTION - ADAR does A->I; this needs G->A
  → base editing (CBE, C->T on the antisense strand) restores the A and REBUILDS the AG:
    MECHANISTICALLY VALID
  → prime editing: VALID, more flexible
  → trans-splicing (SMaRT/RTM): theoretically applicable, low historical efficiency, no mature
    CNS application
```
✅ **And CLAIM 032 gives this arm an argument it did not have:** because haploinsufficiency is
tolerated, **not every cell must be corrected**. The modest in-vivo efficiency of base editing —
fatal for a disease requiring 100% — **may here be enough**.

⚠️ **Honesty about the strength of this verdict:** it rests on mechanistic reasoning and standard SSO
biology. **No systematic counterexample search was performed.** Status is `stress-tested`, **not**
`refuted`; formal demotion of TX-001 requires an external reviewer or a dedicated bibliographic
search ([[discovery_ledger_current#DL-MOL-013 — VERDETTO sulla tesi ASO: **regge**, con una via RNA che non avevo considerato|DL-MOL-013]]). **No sequence has been designed. This is not
clinical design.**

**The enabling measurement both chains need before any intervention choice:** a published, validated
RT-qPCR quantifies **exon 8→exon 9 junction** transcripts against **core (exons 4–6)** transcripts
(ratio ~67%, intra-line r=0.68) — the very junction an acceptor-class allele destroys. It supplies
both a **state biomarker** for the allele and an **efficacy endpoint** for any correction
([[discovery_ledger_current#DL-BIO-003 — Assay qPCR region-specifico esone 8–9 vs core (esoni 4–6): misura diretta dell'effetto dell'allele di sito accettore|DL-BIO-003]], HYP-20260709-06). Requires junction-spanning primers plus
an NMD block (cycloheximide/SMG1i) to unmask the degraded transcript.

---

## 4. Repurposing records

Fifteen fields per candidate, as specified. `HUMAN_USE_STATUS` and `CLINICAL_MATURITY` describe the
compound **in its approved indication**, never in WWOX.

---

### R-01 — AAV9-hSynI-WWOX (gene addition)

| Field | Value |
|---|---|
| **INTERVENTION** | AAV9, human Synapsin-I promoter, WWOX cDNA, WPRE element; ICV |
| **TARGET** | the WWOX locus product itself — neuronal WWOX protein |
| **MECHANISM** | supplies full-length WWOX to neurons, bypassing every allele (gene addition) |
| **EVIDENCE_LEVEL** | **T1** (Wwox-null mouse, WWOX-KO and WOREE-derived organoids) + **T6** for human efficacy |
| **WWOX_DIRECT_EVIDENCE** | Yes — multi-domain rescue: survival, growth, glycaemia, behaviour, ataxia, myelination, gliosis, SWD/ECoG; durable to P300; organoid firing normalized (P=0.77 vs parental) |
| **NEAR_DISEASE_EVIDENCE** | AAV9 CNS gene addition is clinically established in SMA; not transferable as dose or window |
| **HUMAN_USE_STATUS** | first-in-human compassionate n-of-1 reported at **news level only**, not peer-reviewed |
| **CLINICAL_MATURITY** | industrial partner and regulatory route exist; **no open trial**; efficacy in humans **not demonstrated** |
| **BBB_RELEVANCE** | bypassed — direct CNS administration (ICV) |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⚠️ **decisive and limiting.** Efficacious window P0–P5 in mouse. Neuronal rescue does **not** repair the prenatal progenitor/radial-glia defect. The older the recipient, the smaller the reversible fraction |
| **REVERSIBILITY_REQUIREMENT** | ❌ **not met — AAV persists.** REVERS score 0, the only 0 in the portfolio |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | dose-limiting DRG/peripheral-ganglion toxicity at high systemic dose; supraphysiological and regionally uneven long-term expression in survivors; PNS/spinal-cord biodistribution; tumour non-finding qualified three times (*gross*, *limited number*, *8–11 months*) in a **tumour suppressor** whose periphery remains null; the organoid work shows loss of the apoptotic checkpoint — **neither too little nor too much WWOX** |
| **EXPECTED_DIRECTION_OF_EFFECT** | restore protein toward physiological, **not** above it |
| **MAIN_TRANSLATIONAL_RISK** | the **window**. Also: a **threshold**, not a gradient — below 2.63 × 10¹¹ vg survival is not rescued at all, so "a lower, safer dose" is refused by the data |
| **DECISIVE_PRECLINICAL_TEST** | **delayed, post-onset dosing in a hypomorphic (non-null) model**, with SWD/ECoG and myelin readouts; plus an **intermediate-dose arm between 1.23 and 2.63 × 10¹¹ vg** to localize the threshold |

**Class:** `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` — and it is the only entry in it.

---

### R-02 — Memantine (NMDAR antagonism)

| Field | Value |
|---|---|
| **INTERVENTION** | memantine (approved); MK-801 / APV as tools |
| **TARGET** | NMDA receptor |
| **MECHANISM** | WWOX-loss bursting depends on NMDAR activity; blocking the dependence should reduce bursting |
| **EVIDENCE_LEVEL** | **T2** (see the locator question in Chain B — could be T1 for the tool compounds) |
| **WWOX_DIRECT_EVIDENCE** | the **dependence** is WWOX-model-derived (CLAIM 021). Memantine itself has never been given to a WWOX system |
| **NEAR_DISEASE_EVIDENCE** | **T3** — GRIN2A, an NMDAR subunit, causes the same burst-suppression phenotype |
| **HUMAN_USE_STATUS** | approved (Alzheimer's disease); paediatric off-label use documented |
| **CLINICAL_MATURITY** | high as a compound; zero in WWOX |
| **BBB_RELEVANCE** | ✅ crosses; CNS drug by design |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⚠️ **ambivalent.** Chronic NMDAR blockade in a developing brain carries neurodevelopmental risk; NMDAR signalling is required for activity-dependent maturation — the same processes WWOX loss already impairs |
| **REVERSIBILITY_REQUIREMENT** | ✅ met — stoppable, short half-life relative to the intervention |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | modest efficacy and narrow window in paediatric DEE; developmental NMDAR-blockade concerns |
| **EXPECTED_DIRECTION_OF_EFFECT** | ↓ burst frequency/amplitude, ↓ phase-amplitude coupling |
| **MAIN_TRANSLATIONAL_RISK** | suppressing a network *state* is not correcting a *developmental* lesion; CLAIM 031 says symptomatic control does not buy development |
| **DECISIVE_PRECLINICAL_TEST** | MEA on WWOX-null neurons/organoids: does memantine (or MK-801) reduce spontaneous burst frequency/amplitude and PAC, dose-dependently, **with the parental/rescue line as the internal comparator**? |

**Class:** `PROMISING_BUT_MECHANISTIC_GAP` — the gap is that nobody has run the conjunction, and the
platform to run it has existed for years.

---

### R-03 — Wnt / tankyrase inhibition

| Field | Value |
|---|---|
| **INTERVENTION** | tankyrase inhibitor (e.g. XAV939 as tool); no paediatric-profiled candidate identified |
| **TARGET** | Wnt/β-catenin |
| **MECHANISM** | WWOX loss de-represses Wnt via loss of DVL2 sequestration; inhibition restores tone |
| **EVIDENCE_LEVEL** | **T2** — direction measured in WWOX systems (organoids, human neural tissue); the intervention arm is oncological |
| **WWOX_DIRECT_EVIDENCE** | nuclear β-catenin ~1.7×, WNT/LEF1/AXIN2 up in WWOX-KO cerebral organoids; **partially recovered by W-AAV** (which is itself the strongest evidence that the axis is WWOX-downstream) |
| **NEAR_DISEASE_EVIDENCE** | none in genetic DEE |
| **HUMAN_USE_STATUS** | no approved Wnt/tankyrase inhibitor in paediatric neurology |
| **CLINICAL_MATURITY** | low — oncology development stage |
| **BBB_RELEVANCE** | ❌ not established for the tool compounds |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⚠️ **poor.** Wnt has timing-dependent roles in cortical development; the hyperactivation is documented mainly in cancer contexts, and the developing-neuron sign was confirmed only recently and partially |
| **REVERSIBILITY_REQUIREMENT** | ✅ pharmacologically reversible |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | 🔴 intestinal-crypt turnover and bone toxicity — the classic systemic Wnt-inhibition liabilities, poorly compatible with a growing child |
| **EXPECTED_DIRECTION_OF_EFFECT** | ↓ nuclear β-catenin toward parental levels; normalized cortical layering |
| **MAIN_TRANSLATIONAL_RISK** | **narrow therapeutic window**, and "less Wnt/MYC = better" is not a safe default in a context-dependent WWOX output (CLAIM 028) |
| **DECISIVE_PRECLINICAL_TEST** | in WOREE organoids, **first measure nuclear β-catenin state**, then XAV939 **vs** CHIR99021 on cortical-layering rescue — the two-armed design is what fixes the sign in the right context |

**Class:** `TRANSFER_HYPOTHESIS` — direction resolved, modality not viable for this population today.

---

### R-04 — Lithium (GSK3β)

| Field | Value |
|---|---|
| **INTERVENTION** | lithium carbonate |
| **TARGET** | GSK3β (among many) |
| **MECHANISM** | claimed: inhibits a kinase de-repressed by WWOX loss |
| **EVIDENCE_LEVEL** | 🔴 **T5, not T2.** The WWOX experiment **failed its specificity test**: lithium suppressed PTZ seizures in **all three genotypes, wild type included**. What was shown is an anticonvulsant working in an animal that has seizures |
| **WWOX_DIRECT_EVIDENCE** | GSK3β **abundance** elevated in Wwox-null cortex/hippocampus/cerebellum (2 sources; `WWOX AND GSK3` returns 5 PubMed records in total) — and the load-bearing premise *abundance reports activity* is tagged `PREMISE: DEFAULT_FROM_TEXTBOOK`, because in this very system abundance and activity are **dissociable** (S9-independent inhibition) |
| **NEAR_DISEASE_EVIDENCE** | lithium in paediatric neuropsychiatry; nothing in genetic DEE |
| **HUMAN_USE_STATUS** | approved, used in paediatrics with tight monitoring |
| **CLINICAL_MATURITY** | high as a compound; **the WWOX rationale is what fails, not the drug** |
| **BBB_RELEVANCE** | ✅ crosses |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | usable, with narrow therapeutic index |
| **REVERSIBILITY_REQUIREMENT** | ✅ met |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | low therapeutic index; thyroid and renal monitoring; would interfere with the readability of any concurrent titration (PROTO-FIT 1) |
| **EXPECTED_DIRECTION_OF_EFFECT** | 🔴 **conflicted across two admitted axes**: plausibly beneficial on M4 (GSK3β), **harmful on M5** — lithium stabilizes β-catenin and therefore *activates* a pathway already hyperactivated |
| **MAIN_TRANSLATIONAL_RISK** | adopting a WWOX-specific rationale that the primary panel does not support |
| **DECISIVE_PRECLINICAL_TEST** | a PTZ + lithium arm with an **explicit, tested** `−/−` vs `+/+` comparison — or a different GSK3β inhibitor under the same design. Until then, no genotype-specific claim is available |

**Class:** `DEPRIORITIZE` — not for toxicity, but because **the evidence that made it the strongest
signal does not say what it was read as saying**, and its direction is wrong on a second axis.

---

### R-05 — Ketogenic diet

| Field | Value |
|---|---|
| **INTERVENTION** | ketogenic diet |
| **TARGET** | TCA entry, downstream of the PDK1→PDH block |
| **MECHANISM** | ketone bodies enter as acetyl-CoA **below** the block, without needing PDH reactivation |
| **EVIDENCE_LEVEL** | **T3/T4** empirically (standard of care in DEE; GLUT1-deficiency is treated with it) + **T2** for the WWOX-specific rationale |
| **WWOX_DIRECT_EVIDENCE** | PDK1/GLUT1/HK2/PKM2 measured up in Wwox-KO; OXPHOS↓/glycolysis↑ in human WWOX-KO cerebral organoids (transcriptome). Clinically: seizure improvement in 3/5 WOREE patients in one report |
| **NEAR_DISEASE_EVIDENCE** | strong across genetic DEE generally |
| **HUMAN_USE_STATUS** | established paediatric intervention |
| **CLINICAL_MATURITY** | highest in the file — an existing protocol with existing monitoring |
| **BBB_RELEVANCE** | ✅ ketone bodies are actively transported |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ✅ established, with known monitoring (acidosis, lithiasis, growth, dyslipidaemia) |
| **REVERSIBILITY_REQUIREMENT** | ✅ fully — stoppable immediately |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | 🟢 the lowest-risk entry: no new molecule, no BBB problem, risk managed by an existing protocol |
| **EXPECTED_DIRECTION_OF_EFFECT** | restore oxidative flux; **NOT** a demonstrated developmental modification |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 the rationale rests on models; **human WWOX metabolism is normal across four independent sources**, and the real-world continuation signal is poor (1/3 continued; listed among ineffective interventions in a severe case) |
| **DECISIVE_PRECLINICAL_TEST** | **Seahorse OCR/ECAR on donor-derived fibroblasts/LCL vs control** — the only remaining falsifier since lactate became ambiguous. Zero-cost second test: Seahorse on the existing WWOX-KO organoids, closing the transcriptome→flux gap |

**Class:** `PROMISING_BUT_MECHANISTIC_GAP` — the gap being **transcriptome vs flux**, which one
experiment closes.

---

### R-06 — Anti-neuroinflammatory (class-level; no compound named in the public record)

| Field | Value |
|---|---|
| **INTERVENTION** | class: IL-1β/NLRP3, MAPK/NF-κB or microglia-targeting agent |
| **TARGET** | de-repressed neuroinflammatory signalling |
| **MECHANISM** | WWOX is a brake on inflammatory signalling; its loss de-represses microgliosis/astrogliosis |
| **EVIDENCE_LEVEL** | **T2** for direction; **T6** for any specific compound |
| **WWOX_DIRECT_EVIDENCE** | ↑IBA1/GFAP **area fraction** (not glial cell number) in CA1/CA3/whole hippocampus; only `Il6`, **not** `Tnf-a`, significant at `n=4/group`; progressive astro-microgliosis in the P47T model |
| **NEAR_DISEASE_EVIDENCE** | **T4** — many anti-neuroinflammatories have failed in neurodegenerative disease |
| **HUMAN_USE_STATUS** | class-dependent |
| **CLINICAL_MATURITY** | undetermined — no compound is identifiable in the public record |
| **BBB_RELEVANCE** | ⚠️ class-dependent, unverified |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | unverified |
| **REVERSIBILITY_REQUIREMENT** | ✅ generally met |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | class-dependent; paediatric immunosuppression concerns |
| **EXPECTED_DIRECTION_OF_EFFECT** | ↓GFAP/Iba1, slowed progression — **symptomatic/slowing, not curative** |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 **the target is downstream of the target.** Neuron-restricted WWOX rescue *by itself* reduces gliosis — so part of this axis is a **consequence** of neuronal dysfunction, not an independent driver. Treating it treats an effect |
| **DECISIVE_PRECLINICAL_TEST** | in the **existing, characterized Wwox^P47T mouse** (survives >1 year, vs ~1 month for the null): does the agent reduce astro-microgliosis, slow Purkinje loss, and improve motor coordination? |

**Class:** `TRANSFER_HYPOTHESIS`.

---

### R-07 — Bumetanide (NKCC1 / chloride gradient)

| Field | Value |
|---|---|
| **INTERVENTION** | bumetanide |
| **TARGET** | NKCC1 |
| **MECHANISM** | *if* GABA is still depolarizing, lowering intracellular chloride shifts GABA toward functional inhibition |
| **EVIDENCE_LEVEL** | 🔴 **T6 — mechanistic hypothesis only.** Its load-bearing premise has **never been measured in any WWOX system**: no `E_GABA`, no intracellular chloride, no NKCC1/KCC2, no GABA response, no GABA pharmacology |
| **WWOX_DIRECT_EVIDENCE** | **none.** "Depolarizing GABA" is the authors' `IPOTESI` read off a marker pattern (GAD67↑, VGLUT1 unchanged, GABRB2/GABRB3↓) against the developmental literature |
| **NEAR_DISEASE_EVIDENCE** | **T3/T4** — neonatal seizures and other DEEs, with a mixed-to-negative trial record |
| **HUMAN_USE_STATUS** | approved diuretic; neonatal neurology use investigational |
| **CLINICAL_MATURITY** | investigational for this indication |
| **BBB_RELEVANCE** | 🔴 **poor CNS penetration** — a known, unsolved limitation of this repurposing route |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⚠️ ototoxicity and diuresis in neonates; and **the window may already be closed** — the depolarizing state, if real, is an early-developmental property |
| **REVERSIBILITY_REQUIREMENT** | ✅ met |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | ototoxicity, electrolyte disturbance, volume depletion |
| **EXPECTED_DIRECTION_OF_EFFECT** | unknown — **the sign of the effect depends on an unmeasured quantity** |
| **MAIN_TRANSLATIONAL_RISK** | intervening on a chloride gradient whose direction in WWOX has never been observed |
| **DECISIVE_PRECLINICAL_TEST** | **gramicidin perforated-patch `E_GABA`** in WWOX-KO vs parental neurons/organoids, with NKCC1/KCC2 quantification and the GABA response itself. **This single experiment converts the entire M3 axis from T6 to T2 — or closes it** |

**Class:** `INSUFFICIENT_EVIDENCE` — and it is the cleanest example in the file of a candidate that
cannot be ranked at all until one measurement exists.

---

### R-08 — Base / prime editing of a canonical splice-acceptor allele

| Field | Value |
|---|---|
| **INTERVENTION** | cytosine base editor (C→T on the antisense strand) or prime editor |
| **TARGET** | the pathogenic base — restoring the invariant AG acceptor |
| **MECHANISM** | rebuilds the acceptor destroyed by the variant; the only route that returns the wild-type transcript |
| **EVIDENCE_LEVEL** | **T6** for WWOX; **T5/T4** for the modality in other genetic disease |
| **WWOX_DIRECT_EVIDENCE** | none. The **mechanistic exclusion** of every alternative RNA route is the contribution ([[discovery_ledger_current#DL-MOL-013 — VERDETTO sulla tesi ASO: **regge**, con una via RNA che non avevo considerato|DL-MOL-013]]) |
| **NEAR_DISEASE_EVIDENCE** | base/prime editing is advancing in other monogenic diseases; CNS delivery is the shared bottleneck |
| **HUMAN_USE_STATUS** | investigational |
| **CLINICAL_MATURITY** | low; **CNS delivery immature**; prime-editor cargo exceeds single-AAV capacity |
| **BBB_RELEVANCE** | requires direct CNS delivery (split-AAV or equivalent) |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | window-limited like all restoration levers |
| **REVERSIBILITY_REQUIREMENT** | ❌ **not met — permanent genomic change** |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | bystander editing of nearby cytosines (CBE); off-target editing; germline and oncogenic considerations in a **tumour-suppressor** locus |
| **EXPECTED_DIRECTION_OF_EFFECT** | restore correct exon-9 inclusion — measurable as a rise in the exon8–9/core transcript ratio |
| **MAIN_TRANSLATIONAL_RISK** | delivery, and irreversibility in a gene whose over- and under-dosage are both harmful |
| **DECISIVE_PRECLINICAL_TEST** | **first**, characterize the real transcript: junction-spanning RT-PCR ± NMD block, amplicon sequencing, long-read if multiple isoforms appear. **No editing-vs-anything choice may precede this.** Then: PAM availability and bystander-cytosine survey at the locus |

**Class:** `TRANSFER_HYPOTHESIS` — mechanistically possible, which is exactly what the ASO route is
**not**.

---

### R-09 — Proteostasis modulation for an SDR missense allele

| Field | Value |
|---|---|
| **INTERVENTION** | conditional; **no molecule is design-ready**. Three families: site-specific pharmacological chaperone · kinetic stabilizer · indirect proteostasis regulator |
| **TARGET** | WWOX protein stability — *and its function* |
| **MECHANISM** | if the protein is made but cleared, recover it rather than replace it |
| **EVIDENCE_LEVEL** | **T6** for WWOX. Paradigm precedents (migalastat/Fabry, tafamidis/TTR, Trikafta/CFTR, sapropterin/PKU, ambroxol/Gaucher) are **T5 analogies about other proteins** |
| **WWOX_DIRECT_EVIDENCE** | the **endpoint** is measured (normal transcript, protein not detected); the **mechanism** is not (translation vs solubility vs turnover undiscriminated) |
| **NEAR_DISEASE_EVIDENCE** | strong for the *class* of chaperone rescue; **no WWOX variant has ever been shown to be chaperone-responsive**, so there is nothing to calibrate against |
| **HUMAN_USE_STATUS** | family-dependent |
| **CLINICAL_MATURITY** | 🔴 **not design-ready.** WWOX is an oxidoreductase with undefined physiological substrate — migalastat's route requires an active-site ligand that does not exist here |
| **BBB_RELEVANCE** | family-dependent, unresolved |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⭐ this is the **only lever in the portfolio not racing a closing developmental window**: a protein degraded today can be stabilized tomorrow |
| **REVERSIBILITY_REQUIREMENT** | ✅ fully reversible — REVERS 3 |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | proteasome inhibitors are unacceptable as chronic paediatric therapy. 🔴 **4-PBA/TUDCA were withdrawn on their stated rationale — wrong compartment** (those are ER/secretory chemical chaperones; WWOX is cytosolic and the route is lysosomal). 🔴 **An HSP70 co-inducer such as arimoclomol could *accelerate* destruction** — HSC70 does not rescue, it delivers to the lysosome |
| **EXPECTED_DIRECTION_OF_EFFECT** | **soluble, correctly localized, functional** WWOX. Abundance alone is not success |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 **"stable but inert"** — and here it has an identified victim function: the ERLIQ 402–406 degron contains L404, required for the demonstrated GSK3β inhibition. Stability in WWOX **is bought with occlusion** |
| **DECISIVE_PRECLINICAL_TEST** | the ordered sequence, each step informative alone: (1) WB + qRT-PCR on variant-carrying cells vs control; (2) **nascent synthesis + pulse-chase** with soluble/insoluble fractionation, to separate production from disappearance; (3) orthogonal turnover probes (proteasomal and lysosomal arms with viability) — HSC70/LAMP1 are associative, **LAMP2A-dependence is what CMA requires**; (4) only then a mini-screen; (5) promote a hit only if **≥2 orthogonal readouts beyond abundance** recover, including **subcellular localization** and partner binding |

**Class:** `PROMISING_BUT_MECHANISTIC_GAP` — the gap is causal, not pharmacological: the branch has
not been discriminated.

---

## 5. Negative translation — candidates that should be deprioritized, and why

*A well-reasoned exclusion is worth as much as a promotion.* Each carries its **failure mode**, and
each carries what would **revive** it — nothing dies silently.

### N-01 — mTOR inhibitors (rapamycin / everolimus) → **wrong biological direction**
**Failure mode:** *acts in the wrong direction.* The reflex move in genetic DEE, imported from TSC.
The only WWOX-specific measurement touching this axis shows **mTOR/EIF4EBP1 DOWN and autophagy DOWN**
in WWOX-KO cerebral organoids. An mTOR inhibitor pushes the **same way as the lesion**.
⚠️ **Honest weight of the negative:** this rests on one transcriptomic dataset (`n=2` WT vs `n=4` KO,
EV selection at raw `P<0.01`), so it is a **weak measurement pointing the wrong way**, not a
demonstration of harm. The correct verdict is therefore *no positive rationale exists, and the only
directional datum is unfavourable*.
**`REVIVAL_TRIGGER`:** a protein-level mTORC1 readout (pS6, p4E-BP1) in a WWOX-deficient neuronal
system; or any WWOX model showing mTORC1 **hyper**activation.

### N-02 — Lithium as a WWOX-specific disease modifier → **the evidence does not say what it was read as saying**
**Failure mode:** *evidence transfer that was never genotype-controlled*, compounded by *wrong
direction on a second axis*. Lithium suppressed PTZ seizures in **all three genotypes including wild
type**; and lithium activates Wnt, which is already hyperactivated. It remains an anticonvulsant; it
is not a WWOX-mechanism drug.
**`REVIVAL_TRIGGER`:** a PTZ arm with an explicit tested `−/−` vs `+/+` contrast, or a different
GSK3β inhibitor under the same design.

### N-03 — Sodium-channel blockers (carbamazepine, phenytoin, oxcarbazepine) → **target not causally downstream of WWOX**
**Failure mode:** *the target is not causally downstream of WWOX.* Precision therapy in
burst-suppression DEE is gene-dependent: Na-blockers serve the Nav channelopathies (KCNQ2-GoF,
SCN2A). The WWOX node is NMDAR/gap-junction. The value here is **differential** — it excludes a whole
class and redirects attention to R-02.
**`REVIVAL_TRIGGER`:** documented Na-blocker response in WWOX-BS cases, or a Nav dependence measured
in a WWOX model.

### N-04 — Broad GABAergic push (chronic high-dose benzodiazepines; vigabatrin as a mechanism play) → **premise unmeasured, and a real safety signal**
**Failure mode:** *corrects a marker, not the mechanism* — plus an unmeasured premise. VABAM is
documented in WWOX-DEE; and the depolarizing-GABA rationale **failed as a clinical predictor**
(vigabatrin resolved spasms in a WWOX-null child). Both directions of the conflict are live: efficacy
on spasms (n=2) against MRI toxicity (n=2). **Neither closes the question.** The canonical position
is unchanged: caution / avoid unless alternatives are exhausted, with the risk explicitly documented.
**`REVIVAL_TRIGGER`:** `E_GABA` measurement in a WWOX system; or a WWOX cohort with structured VABAM
surveillance imaging.

### N-05 — Boosting WWOX expression alone (CRISPRa, anti-miR-153, small-molecule activators) → **downstream bottleneck, and an allele-asymmetric amplifier**
**Failure mode:** *the target is not the bottleneck.* Normal transcript with protein not detected
means the bottleneck is downstream of transcription — a rejection resting on a **direct measurement
of the exact variant**, which is why it holds where others fell.
**And an asymmetry that is easy to miss:** a non-allele-specific boost on a compound background pushes
*more* aberrant transcript toward NMD on the splice allele while **preferentially amplifying the
missense allele** — whose folding fate is unknown. More synthesis of a destabilized protein in a
neuron may be neutral **or harmful**; WWOX is pro-apoptotic in some contexts, and the organoid work
shows both proliferation with DNA damage and loss of the apoptotic checkpoint. **Neither too little
nor too much WWOX.**
**`REVIVAL_TRIGGER`:** evidence that a compound-heterozygous transcript behaves differently from the
published homozygote; or discrimination of the missense allele's folding fate.

### N-06 — Lactate, and metabolic blood biomarkers generally, as WWOX readouts → **a biomarker that is not measuring the mechanism**
**Failure mode:** *corrects/reports a biomarker, not the mechanism* — inverted: here the biomarker
does not even report. Four independent human sources show normal metabolism; the single MRS outlier
reports cerebral lactate *"extremely low"*, the **opposite** of what the Warburg model predicts, in a
patient with a confounding HSPG2 variant. Serum lactate is Tier 3, distal, and must not enter the
Tier 1/2 biomarker file.
**`REVIVAL_TRIGGER`:** Seahorse/fluxomics showing a real bioenergetic shift in donor-derived cells.

### N-07 — Digoxin (HIF1α inhibition) → **right target validation, wrong clinical object**
**Failure mode:** *toxicity incompatible* + *wrong endpoint*. The only approved drug that corrects a
Wwox-dependent phenotype **in vivo** — which makes it strong **target validation** for HIF1α/PDK1. But
its endpoint in the mouse was **glycaemia**; the endpoint that matters here is **neuronal
bioenergetics**. Not the same clinical target. Cardiac glycoside, extremely narrow therapeutic index,
dose-dependent cardiac **and neurological** toxicity. The reported dose (100 mg/kg i.p.) is very
likely a typographic error for µg/kg and remains unverified against the original PDF.
**Use correctly:** as target validation. The ketogenic diet **dominates** it — same axis,
incomparably better safety.

### N-08 — Dichloroacetate (PDK inhibition) → **dominated, and neurotoxic**
**Failure mode:** *toxicity incompatible* + *two-hop inference*. Dose-dependent peripheral
neurotoxicity (neuropathy) in a child with encephalopathy is an unfavourable ratio without proof of
mechanism. R-05 achieves the same metabolic bypass with an incomparably better profile. Parked
pending `legend-safety-triage`, and downstream of the falsification of R-05 anyway.

### N-09 — pTyr33-WWOX peptide as functional restoration → **the direction is inverted**
**Failure mode:** *acts in the wrong direction.* Phospho-Tyr33 WOX1 is **pro-apoptotic**; the peptide
**blocks** neuronal death, i.e. it acts as a competitive **inhibitor** of a WWOX-dependent function,
not as its substitute. In a WWOX-**deficient** system, inhibiting WWOX function restores nothing. A
commentary had over-interpreted its own primary source.
**What survives:** possible interest as a **generic neuroprotectant** — a different hypothesis that
does not inherit this rationale. The refutation rests on the abstract (full text paywalled); if the
full text says otherwise it re-opens.

### N-10 — Splice-switching ASO for a canonical acceptor allele → **the modality cannot do the job**
**Failure mode:** *derived from a mechanism that cannot work.* SSOs **mask** elements; they do not
**create** splice sites. Masking the +8 cryptic site would shift splicing toward *another* aberrant
product, not the wild type. In-frame skipping is impossible — exon 9 is the last exon and carries the
stop codon and the final ~62 aa of the SDR; the rat *lde* model shows that losing the C-terminus
destabilizes the protein. The *Milasen* precedent is **regulatory**, not proof of amenability.
Status `stress-tested`, **not** `refuted`: no systematic counterexample search was run.

### N-11 — 4-PBA / TUDCA on the ER-chaperone rationale → **wrong compartment**
**Failure mode:** *derived from a textbook default.* "Misfolded protein → ERAD → chemical chaperone"
is true **only for ER/secretory proteins**. WWOX is cytosolic; the route is lysosomal. The rationale
is dead, **the molecule is not**: 4-PBA is also an HDAC inhibitor and could act as an HSP co-inducer —
**a different mechanism**, to be re-evaluated on that basis only if the lysosomal arm is confirmed.

### N-12 — HSP70 co-inducers (e.g. arimoclomol) for an SDR missense → **may accelerate the damage**
**Failure mode:** *wrong direction, hidden inside a plausible one.* "It is a chaperone, therefore it
helps folding" is false: **the sign depends on which chaperone and which route.** HSC70 does not
rescue — it **delivers to the lysosome**. Proposed and withdrawn on the same day.

### N-13 — Pro-myelinating agents (clemastine, benztropine, T3, quetiapine) → **wrong cell compartment, and a closing window**
**Failure mode:** *the target is not causally downstream of WWOX in the cell being targeted* +
*developmental window*. Deleting Wwox in oligodendrocytes (Olig2-Cre) or astrocytes (GFAP-Cre)
produces no evident anomaly; deleting it in **neurons** reproduces the whole phenotype, myelin
included. Even if OPCs were all present, pushing them alone would yield little — **they are not
receiving the axonal signal**. And the myelin window closes early (PND5–21 in rat; myelination lost by
9 weeks in a severe human null).
⚠️ **Not `refuted`:** the oligodendrocyte-directed AAV arm is technically confounded (poor
oligodendroglial tropism by neonatal ICV), the neuron-only rescue is **incomplete** with the residual
gap attributed by the authors — as their `IPOTESI` — to an oligodendrocyte-autonomous WWOX function,
and a cell-autonomous oligodendroglial role under remyelination stress is in observation from a
review-sourced primary still queued. **Partial benefit is not excluded.**

### N-14 — Antioxidants (NAC, CoQ10, creatine) on the "WWOX loss → ROS" rationale → **the relationship is not monotonic**
**Failure mode:** *the direction of the axis is context-dependent and was assumed.* Two independent
primary systems run **counter-directionally**: in diabetic mouse photoreceptors WWOX is
**up**-regulated and its siRNA knockdown **reduces** superoxide; in the fly, Wwox loss **lowers** and
overexpression **raises** thresholded CM-H2DCFDA fluorescence, with Wwox×Idh and Wwox×Sod genetic
interactions. WWOX↔ROS is **not monotonic and its sign is context-dependent** — which is precisely
the premise the antioxidant logic assumes. The canonical claim was held at `in observation` and not
raised to `conflicting evidence`, because the systems are not comparable — but the note is mandatory
wherever the claim is cited in support of NAC/CoQ10/creatine/KD logic.

### N-15 — Counting seizure control as developmental protection → **the most consequential negative in the whole portfolio**
**Failure mode:** *corrects a biomarker (seizures) but not the mechanism (development)*. In published
WWOX children, cognitive and psychomotor impairment **precedes** the onset of epileptic encephalopathy
and **does not improve** when epileptic activity is controlled: *"the developmental outcome was
unfavourable with profound impairment **despite improvement of epileptic activity**"*. In one case
vigabatrin **resolved** the spasms and at two years the child was profoundly delayed. Converging: in
another cohort the only **non**-drug-resistant patient died at 8 years.
⇒ This is a **DEE, not an EE**. Seizure control remains fully indicated — quality of life, status
epilepticus (a documented cause of death), SUDEP, sleep, manageability — but **must not be scored as
disease modification**. Limits: N=2, observational, uncontrolled.
**Corollary, and it is the reason this file exists:** if the developmental outcome does not respond to
symptom control, **only causal levers can change it** — which is why R-01 and the allele-level chains
carry the weight, and why every downstream candidate in §4 is honestly labelled as symptomatic or
slowing.

---

## 6. Prioritization

**Deliberately very small.** A long shortlist would contradict the evidence.

| Class | Entries |
|---|---|
| **READY_FOR_WWOX_PRECLINICAL_CONSIDERATION** | **R-01** AAV9-hSynI-WWOX |
| **PROMISING_BUT_MECHANISTIC_GAP** | **R-02** memantine/NMDAR · **R-05** ketogenic diet · **R-09** proteostasis programme (SDR missense class) |
| **TRANSFER_HYPOTHESIS** | **R-03** Wnt/tankyrase · **R-06** anti-neuroinflammatory (class) · **R-08** base/prime editing |
| **DEPRIORITIZE** | **R-04** lithium · N-01 mTOR inhibitors · N-03 Na-blockers · N-07 digoxin · N-08 DCA · N-09 pTyr33 peptide · N-10 splice-switching ASO · N-11 4-PBA/TUDCA (ER rationale) · N-12 HSP70 co-inducers · N-13 pro-myelinating agents · N-14 antioxidants on the ROS rationale |
| **INSUFFICIENT_EVIDENCE** | **R-07** bumetanide · Zfra peptide (monitor, do not promote) · anti-miR-153 (pleiotropic; conserved because it *proves the principle*, not because it is the molecule) · WWOX-mimetic peptides (the safety argument is rejected; the objective is not) |

> **Note on ranking method.** Priority is a holistic reading, not a sum. R-01 leads on mechanism and
> is simultaneously the only entry with `REVERSIBILITY = 0` and a hard window. R-09 ranks below it on
> evidence and above everything on one dimension nothing else has: **it is the only lever not racing a
> closing developmental window.** Those are different kinds of value and are not commensurable.

---

## 7. Closing blocks

### TOP_MECHANISTIC_LEVERS

1. **Neuronal WWOX protein level (M1).** The only node where loss is *sufficient*, restoration is
   *demonstrated*, and the required efficiency is *quantified* — haploinsufficiency is not
   deleterious, so the threshold sits below 50%, and partial correction may suffice.
2. **NMDAR / gap-junction dependence of the bursting phenotype (M2).** The only downstream node whose
   causal dependence was established **inside** a WWOX model.
3. **The GSK3β docking site 388–407/L404 (M4).** Residue-resolved, S9-independent — and it doubles as
   a **design constraint** on every stabilizer, because the degron and the function overlap.
4. **The allele-level protein/sequence lesion (M7/M8).** The only levers that address the cause at the
   level at which the disease is written.

### TOP_REPURPOSING_CANDIDATES

| Rank | Candidate | Class | Why it is here, in one line |
|---|---|---|---|
| 1 | **Ketogenic diet** | PROMISING_BUT_MECHANISTIC_GAP | already paediatric standard-of-care, fully reversible, and the only repurposing candidate with a WWOX-specific mechanistic rationale whose key enzyme (PDK1) is **measured** rather than inferred |
| 2 | **Memantine** | PROMISING_BUT_MECHANISTIC_GAP | targets the one downstream dependence demonstrated inside a WWOX model, is CNS-penetrant and reversible; the conjunction has simply never been run |
| 3 | *(no third)* | — | 🔴 **Deliberate.** The next candidates are the ones §5 removes. Filling this row would be the exact failure this file is built to avoid |

### TOP_NEGATIVE_FINDINGS

1. **Seizure control must not be counted as developmental protection** (N-15). Cognitive impairment
   precedes the epileptic encephalopathy and does not improve when seizures are controlled. This
   re-scores the entire "buy time" logic and is why causal levers carry the portfolio.
2. **mTOR inhibition points the wrong way** (N-01). The reflex DEE repurposing move, and the only
   WWOX-specific directional datum is unfavourable — with the weakness of that datum stated.
3. **Lithium's WWOX-specific rationale does not survive its own figure** (N-02). Seizure suppression
   in **all three genotypes including wild type** makes it an anticonvulsant, not a mechanism drug —
   and it activates Wnt, which is already hyperactivated.
4. **A splice-switching ASO cannot restore an abolished acceptor** (N-10). The modality masks; it does
   not create. This retires the arm that a mechanism-naive reading would rank first.
5. **HSC70 delivers to the lysosome — a chaperone inducer may accelerate destruction** (N-12), and
   **4-PBA/TUDCA were the wrong compartment entirely** (N-11). Two candidate molecules died on
   textbook defaults that nobody had written down as premises.
6. **WWOX↔ROS is not monotonic** (N-14). Two independent primary systems run counter-directionally,
   which undercuts the antioxidant rationale at its premise rather than its dose.

### PV_GABA_MTOR_PROGRAM_STATUS

**Explicitly evaluated, as instructed — and explicitly not privileged, because another axis has better
evidence.** The three components do not have the same status and must not be reported as one
programme:

| Component | Status | Verdict |
|---|---|---|
| **PV / interneuron** | Marker-level `DATO` in **one** systemic constitutive KO at two weeks (PV⁺ −44% whole hippocampus; NPY⁺ DG only), with a **measured systemic confounder** (that animal is hypoglycaemic, acidotic, uraemic at P18) and `MARKER_TO_FUNCTION_GATE` unmet — no pan-GABA lineage count, no birthdating, no fate mapping, no apoptosis assay | **Mechanism: admitted. Target: not yet.** No PV-directed intervention is scorable |
| **GABA / E-I balance** | The **functional** inhibitory deficit is real and independently measured (reduced spontaneous inhibition, L2/3, neuron-specific loss). The **directional paradox** is unresolved — GABAergic markers ↑ in organoids, ↓ in the mouse. `E_GABA`, chloride, NKCC1/KCC2 and the GABA response are **unmeasured in every WWOX system** | **T6.** Bumetanide unrankable; broad GABAergic push carries a real safety signal and a falsified clinical prediction |
| **mTOR** | 🔴 **Does not qualify for admission.** The only WWOX-specific datum shows mTOR/EIF4EBP1 **down** and autophagy **down** | **Deprioritized on direction**, with the weakness of the single dataset stated |
| **Circuit-targeted** | ✅ **This is where the programme is real** — but the actionable node is **NMDAR/gap-junction**, not GABA. It is the one downstream dependence established inside a WWOX model | `PROMISING_BUT_MECHANISTIC_GAP` (R-02) |

**Overall programme verdict:** *the PV/GABA/mTOR programme, as usually formulated, does not hold.* The
circuit arm survives and relocates to a different receptor; the GABA arm is blocked on a single
missing measurement; the mTOR arm is directionally contra-indicated. **The axis with better evidence
is M1 (neuronal WWOX restoration), and it is ranked above all of them** — which is precisely what the
instruction to not privilege this programme required.

### DECISIVE_PRECLINICAL_EXPERIMENTS

Ordered by *information gained per unit cost*, not by ambition.

| # | Experiment | Decides | Cost |
|---|---|---|---|
| **E-1** | **Re-read PMID 34634460 with verbatim locators**: was the NMDAR/gap-junction dependence established pharmacologically? | Whether Chain B is T1 or T2 — i.e. whether R-02 is a translation gap or an untested conjunction | ~zero (one reading) |
| **E-2** | **Gramicidin perforated-patch `E_GABA`** in WWOX-KO vs parental neurons/organoids + NKCC1/KCC2 + GABA response | Converts the whole M3 axis from T6 to T2, **or closes it**. Also decides bumetanide, and retro-validates or retires the depolarizing-GABA reading of a decade of interpretation | low — the platform exists |
| **E-3** | **Seahorse OCR/ECAR** on donor-derived cells (and on the existing WWOX-KO organoids) | The only remaining falsifier of R-05; closes the transcriptome→flux gap that weakens all of M6 | low |
| **E-4** | **Junction-spanning RT-PCR ± NMD block + amplicon (and long-read) sequencing** on splice-allele-carrying cells | The mandatory gate before **any** correction-modality choice; and supplies the efficacy endpoint (exon8–9/core ratio) | low |
| **E-5** | **Nascent synthesis + pulse-chase with soluble/insoluble fractionation** on SDR-missense cells | Discriminates translation vs solubility vs turnover — the branch on which the entire R-09 programme depends | medium |
| **E-6** | **Intermediate-dose AAV arm between 1.23 and 2.63 × 10¹¹ vg** | Localizes the survival **threshold** — the most informative experiment the gene-therapy paper implies and did not run | medium |
| **E-7** | **Delayed, post-onset dosing in a hypomorphic (non-null) model** | The critical translational gap for anyone past the neonatal window | high |
| **E-8** | **Functional comparison Q230P vs G372R vs P47T vs null in one system**, measuring **function, not abundance** | Whether a stabilized SDR-missense protein is functional — the assumption everything in R-09 rests on. **G372R is the natural control**: if it responded to a chaperone identically, the structural model would be false and the rescue non-specific | medium — one missing line |
| **E-9** | **MEA ± memantine/MK-801 on WWOX-null neurons/organoids**, with parental and rescue lines as internal comparators | Runs the conjunction R-02 has been missing | low |
| **E-10** | **Nuclear β-catenin state first, then XAV939 vs CHIR99021** on organoid cortical layering | Fixes the Wnt sign in a developing-neuron context rather than a cancer one | medium |

### EVIDENCE_GAPS

1. **No `E_GABA`, chloride, NKCC1 or KCC2 measurement exists in any WWOX system.** An entire
   therapeutic axis rests on an unmeasured premise.
2. **No metabolic flux measurement exists in any WWOX system.** Every metabolic conclusion is
   transcriptomic or abundance-based; the transcriptome is not the flux.
3. **No conditional/cell-type-specific separation of the systemic-null confounder.** The allele that
   would separate cell-autonomous neuronal loss from secondary metabolic injury has existed since
   2009 and has not been used in this direction.
4. **No functional readout on a stabilized SDR-missense protein.** Abundance has been measured;
   function has not — and the allelic series proves abundance does not predict severity.
5. **No post-neonatal, post-onset gene-therapy efficacy datum.** The single most important
   translational unknown for anyone not treated perinatally.
6. **The residual gene-therapy gap is untested against wild type** for myelinated axons, CC1⁺ and
   PDGFRα⁺ — the parentheses run WT-vs-KO and KO-vs-rescued, leaving the visible remaining difference
   unmeasured.
7. **The GSK3β abundance→activity premise is `PREMISE: DEFAULT_FROM_TEXTBOOK`** in a system where the
   two are demonstrably dissociable — and de-repression is invisible to the standard phospho-S9
   western, so most published assays of it would return a false negative.
8. **Field density is a structural limit, not a gap in our reading:** `WWOX AND GSK3` returns 5 PubMed
   records in total; `WWOX AND (Olig2 OR NG2 OR PDGFRA OR oligodendrocyte precursor)` returns 0;
   `WWOX AND "growth hormone"` returns 0. Several axes cannot be consolidated because the literature
   to consolidate them does not exist.

### NEW_HYPOTHESES

- **H-1 — Isoform-selective GSK3β inhibition via the Axin docking site.** Axin associates more readily
  with **β1** than with **β2**; tau is a **disfavoured** substrate for β2; the discriminant is the
  C-terminal tail. Therefore an **ATP-competitive inhibitor cannot separate the isoforms, but an
  Axin-site ligand could** — and **WWOX binds precisely that site**. This is *isoform* selectivity, a
  claim distinct from the *substrate* selectivity that was rejected. `PREMISE: INFERENZA` — that
  Axin-site binding confers β1 preference has **never been measured on WWOX**. **Decisive test:**
  WWOX and WWOXtide³⁸⁸⁻⁴⁰⁷ against β1 vs β2 in parallel.
- **H-2 — Downstream levers are not uniformly genotype-agnostic.** WWOX binds HIF1α via **WW1** and
  sequesters DVL2 via the **WW scaffold** — neither via the SDR. An SDR-domain missense may therefore
  leave the **metabolic and Wnt axes partially preserved** while a null allele does not. If true, the
  metabolic and Wnt levers are **worth less in a missense-carrying class than in a biallelic null
  class** — the inverse of the usual assumption, and it would re-rank R-03 and R-05 by genotype class.
  **Decisive test:** HIF1α target-gene panel and nuclear β-catenin in SDR-missense vs null cells.
- **H-3 — Partial correction may be sufficient, and this changes which modality is viable.** Because
  haploinsufficiency is tolerated, the modest in-vivo efficiency of base editing — disqualifying for a
  disease requiring near-total correction — **may be adequate here.** The threshold argument turns a
  modality's central weakness into a tolerable one. **Caveat:** the threshold is established for
  **survival and morphology**, never for cognition or epilepsy.
- **H-4 — The exon 8→9 junction assay is a dual-use instrument.** The same published RT-qPCR is
  simultaneously a **state biomarker** for an acceptor-class allele and the **efficacy endpoint** for
  any correction of it. Without a molecular endpoint no correction is testable; this supplies one that
  already exists and is validated in another context.
- **H-5 — NMD efficiency may itself be WWOX-dependent** ([[discovery_ledger_current#DL-MECH-069 — 🔑 L'efficienza dell'NMD potrebbe essere **WWOX-dipendente**, e questo tocca sia l'allele di sito accettore sia l'esperimento disegnato per caratterizzarlo|DL-MECH-069]]),
  which would touch **both** the acceptor allele's fate **and** the design of the very experiment
  meant to characterize it. If it holds, the NMD-block control in E-4 is not a control but a variable.

### BENCHMARK_CANDIDATES_DISCOVERED

**Model systems and assays that can benchmark a WWOX intervention** (all exist; none needs building):

| Benchmark | What it benchmarks | Note |
|---|---|---|
| **G372R patient iPSC (SDR missense, mild phenotype)** | the **natural negative control** for any SDR-missense rescue: if it responds to a chaperone identically to a severe missense, the structural model is false and the rescue non-specific | a comparator, **not** a validated negative control — the firewall applies |
| **Wwox^P47T knock-in mouse** | a **hypomorphic-allele bench** surviving >1 year (vs ~1 month for the null) — long enough to test a slowing agent | not a read-across bench for a buried SDR missense (different domain, different lesion) |
| **Rat `lde/lde`** | the animal proxy of the **acceptor-class allele** (exon-9 lesion), with a 95%-penetrant electrographically documented seizure phenotype and ataxic gait | the seizure phenotype in this literature is a **rat** phenotype and is explicitly absent in Wwox-null mice — never transfer it to a mouse |
| **WOREE patient-iPSC forebrain/cerebral organoids + hESC WWOX-KO + stable W-AAV rescue + lenti-WWOX** | an n-of-1-capable screening bench with electrophysiology (LFP + cell-attached), DNA-damage foci, astrogenesis and RNA-seq readouts | W-AAV rescue there is supraphysiological, ubiquitous and only **partial** — a benchmark with a known ceiling |
| **GEO GSE156243** | a public re-analysable transcriptome of WWOX-KO cerebral organoids | `n=2` WT vs `n=4` KO; EV selection at raw `P<0.01`; five gene symbols corrupted by spreadsheet auto-dating are annotated |
| **Exon 8→9 vs core RT-qPCR** | acceptor-allele state and correction efficacy | published, validated at n=381/89 LCL; needs junction-spanning primers plus an NMD block |
| **GS-1 peptide phosphorylation assay** | GSK3β docking-site occupancy — the assay that **refuted** the substrate-selectivity argument | reusable to test H-1 |
| **Gramicidin perforated patch** | `E_GABA` — the missing measurement of the entire M3 axis | standard technique, never applied to a WWOX model |
| **Seahorse OCR/ECAR** | the transcriptome→flux gap across all of M6 | the single falsifier of R-05 |
| **MEA burst frequency/amplitude + phase-amplitude coupling; LFP 0.25–1 Hz band power; GAD67/VGLUT1 ratio** | reusable network endpoints, already quantified in WWOX systems | usable as pre-specified endpoints rather than post-hoc |

**Comparator therapeutic programmes** (paradigms, **not** transferable evidence): migalastat/Fabry
(variant-specific amenability assay) · tafamidis/TTR (kinetic stabilization) · Trikafta/CFTR-F508del
(combination correction) · sapropterin/PKU · ambroxol/Gaucher (repurposing onto a lysosomal route) ·
*Milasen* (an n-of-1 **regulatory** precedent, never proof of amenability) · GLUT1-deficiency/KD (an
encephalopathy of glucose entry treated by the same bypass) · clemastine/MS (a remyelination trial
with a VEP-latency endpoint and a **modest** effect).

---

## 8. Layer discipline — what this file did not do

- It **did not** modify any canonical file. No claim status changed, no working-model version bumped,
  no paper record touched.
- It **did not** promote any hypothesis. R-01…R-09 are candidates in a non-canonical map; TX-001…TX-007
  in [`../therapeutics/therapeutic_strategies_current.md`](../therapeutics/therapeutic_strategies_current.md)
  remain the operational tracker, and HYP-* in
  [`../research/therapeutic_hypotheses_ledger_current.md`](../research/therapeutic_hypotheses_ledger_current.md)
  remain the hypothesis portfolio. Where this map disagrees with either, **this map is the newer
  reading and the weaker artefact** — reconciliation goes through the pipeline, not through this file.
- It **did not** formulate a clinical indication, a dose, a schedule or a sequence of care.
- It **did not** design a sequence, a molecule or a construct.
- Every molecule named is **material for discussion with a treating clinical team**, and nothing here
  substitutes for one. **Not medical advice.**
