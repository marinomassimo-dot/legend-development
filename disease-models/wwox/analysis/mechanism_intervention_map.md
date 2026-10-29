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
> | **R-01** — the sole entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` | **`SPLIT`.** Retained for survival/SWD/gliosis at HD in the P0–P5 window — ⚠️ **`motor` removed 2026-09-27**: the WT-versus-treated comparison is drawn in all eight panels of Figure 4 and three are significant in the exceed direction, so MOTOR is `PARTIAL / NOT_NORMALISED`, not rescued (`CC-20260826-AAV9-ENDPOINT-SPLIT-01`, MOTOR correction); **downgraded to `PROMISING_BUT_GAP`** for development, cognition, myelin-in-the-dose-study, the (under-transduced) cerebellum, and post-neonatal use |
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
| **M1** | **Neuronal WWOX protein deficit** — neuron-restricted loss is sufficient to reproduce the phenotype; restoration rescues multiple domains (given at P0 to P5 in the null mouse: early-window prevention, not recovery of a manifested deficit; CHAIN A boundary 5) | CLAIM 002 · CLAIM 003 · CLAIM 004 · CLAIM 011 · CLAIM 032 | ✅ loss → disease; restoration → rescue | WWOX protein level *in neurons* |
| **M2** | **Network-state pathology** — spontaneous neocortical bursting, altered oscillatory organization, ↑phase–amplitude coupling; bursting **needs NMDAR activity** (the gap-junction half withdrawn 2026-09-27; NMDAR function not shown raised) | CLAIM 021 · CLAIM 002 | ✅ hyperexcitable | NMDAR activity (not shown raised); the connexin node is withdrawn pending occlusion |
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
  genetic DEE, imported from TSC — would push the **same direction as the only directional datum**, which is a **non-locatored transcriptomic signal at n = 2/4** and is **not a measurement of mTORC1 signalling**. The only other
  WWOX record naming mTOR is `CORPUS-STUB-043` in the paper registry (an LPS lung-injury study),
  status `not_processed`: **nobody has read it, so it cannot carry a direction** and is not cited
  here as evidence for or against. See §5, N-01. **This is a negative whose weight rests on one weak
  datum.**
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
5. **Prevention, not recovery (added 2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P7).** Every in-vivo genetic rescue read in this corpus (two mouse studies; a bounded search for inducible neural Wwox models found none) treats the Wwox-null mouse at P0 to P5
   (main cohorts P0-P1, timing arms P1-P5) in animals never measured before treatment, and measures at P10 or later against an untreated comparator that is already abnormal: the
   result is PREVENTED or EARLY-WINDOW for survival, growth, glucose, SWD/ECoG (recording from about P14, a floor of observation, not an onset), in part (partial, not normalised) for motor score and, at the high dose only, for gliosis, and RECOVERED
   for none. No treated-after-onset mouse arm exists, and the authors say later intervention was not explored. The timing arms are small and not uniformly successful (S8: a P3 arm,
   n = 3, about 67 percent from about day 24; a P5 arm, n = 7, 75 percent from about day 35 to day 300; no P4 survival curve; treated arms compared with wild type). The only genetic
   add-back after a documented phenotype read in this corpus is organoid (neuron-directed AAV9-WWOX at week 10 on a hyperexcitability seen at week 7, read at week 16, radial-glia abnormalities of the knockout lines not
   corrected), and the mouse cannot be carried to a later intervention (DL-MECH-011; `drug_repurposing/rescue_window_it6_20261029.md`, independently verified).

### CHAIN B — the network node (M2)

```
neuron-specific WWOX loss
  → ↑excitatory drive, ↓spontaneous inhibition, depolarization, ↑firing, ↑sag,
    post-inhibitory rebound in L2/3 pyramidal neurons   [CLAIM 021 — measured]
  → spontaneous bursting, altered oscillatory organization, ↑phase-amplitude coupling
  → bursting DEPENDS ON NMDAR activity [CLAIM 021 — NMDAR half only; the gap-junction half of this
    dependence was WITHDRAWN as not attributable 2026-09-27 (`BATCH_20260927_004`,
    `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`) — see the withdrawn node below]
  → NODE: NMDAR ACTIVITY IS REQUIRED for the bursting (d-APV 50 uM eliminated the bursting inside the WWOX system; a competitive antagonist, no test on that arm); a RAISED NMDAR function is NOT shown (three readings, unranked; see the 2026-10-29 update below)
  → NODE WITHDRAWN PENDING OCCLUSION: connexin gap junctions — the carbenoxolone effect is real and not attributable (no washout reversal; the authors write that CBX *«may not be specific to gap junctions»*, that it *«could block NMDA receptors … which could partially account for our observations»* — a cited possibility with NO concentration attached — and that it *«blocks pannexin channels»*). Not «uninvolved»: untested. (2026-09-27, `BATCH_20260927_004`, `CC-20260826-GAPJUNCTION-ATTRIBUTION-01`.)
  → INTERVENTION: memantine (approved) · MK-801/APV (tools) · carbenoxolone (tool — ⚠️ sits under the
    WITHDRAWN node: CBX's 87% suppression is real but NOT attributable to gap junctions, so this entry
    is a tool for an untested node, not an intervention with a mechanism; 2026-09-27,
    `BATCH_20260927_004`)
  → EXPECTED EFFECT: ↓ burst frequency/amplitude, ↓ phase-amplitude coupling
```

🔴 **An unresolved locator question that changes the tier.** The registry records that bursting
*depends on* NMDAR and gap-junction activity, but does **not** record whether that dependence was
established **pharmacologically** (blockers applied to the WWOX-deficient system — which would make
the acute anti-bursting effect a T1 datum for the tool compounds) or by another route. The
distinction decides whether Chain B is a **T1 chain with a translation gap** or a **T2 chain with an
untested conjunction**. It was scored **T2** here, deliberately conservatively; the re-read that resolves it exists (`FTR-20260810-34634460-02`) and the dependence IS pharmacological, so the chain is **T1 for the tool compound d-APV only** — memantine has still never been given to a WWOX system, and `R-02` is untouched. ⚠️ And the window bounds any chronic proposal only as the authors bound it: the P13–P17 age group *«may mimic a late-stage disorder»* and they *«cannot rule out»* an earlier-stage pannexin route — a stated possibility, twice hedged, **not** a statement that the window IS late-stage (2026-09-27, `BATCH_20260927_004`, `CC-20260826-NMDAR-CONJUNCTION-01`, corrected by the blind audit). What remains is
a single re-read of PMID 34634460 with verbatim locators. **This is the highest-value, lowest-cost
open item in the file.**

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P9 and P11; EXPLORATORY; the T1-for-d-APV-only scoring above is unchanged).** d-APV shows that the bursting NEEDS NMDAR activity, not that NMDAR function is raised: three readings fit it and are not ranked (NMDAR gain; permissive necessity in a network whose pyramidal neurons rest about 5.6 mV more depolarised and whose spontaneous inhibitory current amplitude is about half; an AMPAR-led drive), and no NMDAR-specific measurement exists in any Wwox system. The discriminating measurement is the isolated NMDAR current under voltage control (card `F04_nmdar_intervention_class`, step E1), not a drug arm: an AMPAR antagonist is expected to stop an NMDAR-dependent burst whichever reading is true, and a pore blocker is state-dependent (incubation solution 1.3 mM Mg2+, recording bath not stated). Extracellular magnesium as the physiological gate is a hypothesis (`HYP-20261029-01`, card `P11_magnesium_nmdar_gate`), not a node. The baseline burst rate is printed twice, 2.7-fold apart (CLAIM 021 wave note).

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
  → PDK1 inhibits PDH -> pyruvate blocked at the TCA entry   [INFERRED: PDK1 is a transcript; PDH
                                                         phosphorylation, activity and flux are not measured in any WWOX system]
  → human WWOX-KO cerebral organoids: OXPHOS/ATP-synthesis inhibited, glycolysis enriched
                                                        [RNA-seq, GSE156243 — transcriptome, NOT flux]
  → ACTIONABLE NODE: TCA entry, DOWNSTREAM of PDH
  → INTERVENTION: ketogenic diet (ketone bodies enter as acetyl-CoA below the block)
  → EXPECTED EFFECT: restore oxidative flux without reactivating PDH
```

⚠️ **Three brakes, all canonical, all pointing the same way:**
- **The transcriptome is not the flux.** `n=2` WT vs `n=4` KO; EV tables select on raw `P<0.01`. No
  Seahorse, no fluxomics, in any WWOX system.
- **Human metabolism is reported normal where it was checked; "four times" is a count NOT reconciled with N-06 (2026-10-24: one complete screen plus one MRS case in the opposite direction).** Lactate, ammonia, acylcarnitines,
  uric acid, homocysteine, plasma amino acids, urinary organic acids, transferrin isoforms — normal;
  a complete metabolic and mitochondrial screen including muscle biopsy — normal; MRS — normal. The
  single outlier (cerebral lactate *"extremely low"*, the opposite of the Warburg prediction) carries
  a confounding second variant in HSPG2 ([[discovery_ledger_current#DL-BIO-009 — Il metabolismo umano nel deficit di WWOX è, per quanto misurato, **normale**. Il modello murino non si trasferisce.|DL-BIO-009]],
  [[discovery_ledger_current#⚠️ DL-BIO-008 — Contraddizione sul lattato: alto nel siero del topo, **"extremely low" nell'MRS cerebrale umana**|DL-BIO-008]]). **Do not look for confirmation in blood: it has been
  looked for and, in the cases reported, it is normal (count: see N-06).**
- **The real-world continuation signal runs against the rationale.** Ketogenic diet was tried in 3
  WWOX-DEE patients and continued in 1; cannabidiol was continued in 4/4 who started it. In a severe
  WOREE case the ketogenic diet is listed among the *ineffective* interventions alongside eleven
  drugs and three ACTH cycles ([[discovery_ledger_current#DL-MOL-007 — Fallimento sistematico degli ASM sintomatici in WOREE severo → priorità alle leve disease-modifying|DL-MOL-007]]).

🔵 **Update 2026-10-29 (IT5 P7 systems comparison and P9 card I01; COMPUTATIONAL_RESULT at transcript level, exploratory; not flux, activity or rescue).** The middle link "PDK1 up" has no transcript support in either human neural system held: PDK1 is lower **in sign only** in the knockout organoid (-0.39) and in the shRNA-silenced progenitor library (-0.67; one library per arm), both inside their single-gene null (p about 0.30 and 0.49), and HIF1A mRNA is flat in both; the finding is the absence of support, not a demonstrated decrease. The PDK transcript is higher in Wwox-null mouse fibroblasts and in a human knockout fibroblast line, so its sign depends on cell type; the "PDK1 up" prediction is not to be carried into a neural argument. LDHA and a HIF-type glycolysis subset are higher in both neural systems; the broader glycolysis panel is not distinguishable from chance in the progenitor library. A PDH restraint is documented after chemoconvulsant status epilepticus in two non-WWOX models (seizure, injury, neuron loss and drug exposure are not separable in either; the rat datum is protein and phospho-protein level at one week, not activity; the mouse source is abstract level), so a restraint found in a seizing WWOX-DEE brain would not by itself be WWOX-dependent: a competing explanation that applies to every lever on the PDH axis, this diet included.

⇒ The KD rationale is **not falsified** — it rests on the PDK1→PDH block and depressed OXPHOS, not on
lactate — but the easiest endpoint for verifying it has been lost, and the expectation of benefit
must be calibrated **down**. Seahorse OCR/ECAR on donor-derived cells is the cheapest general
bioenergetic screen, **not a PDH-specific measure and not the only possible falsifier**: PDH-specific
readouts (PDH activity in a phosphorylation-preserving lysate, phospho-PDHA1, 13C-glucose or ketone tracing,
pyruvate/lactate ratio, NADH/NAD+) are the discriminating ones. A normal Seahorse in non-neural donor cells
would weaken the rationale; it would not by itself refute a neural block, and a normal result is non-significance,
not equivalence (HYP-20260709-01, correction 2026-10-27). Current reading of the hypothesis: `therapeutic_hypotheses_ledger_current.md` HYP-20260709-01, line `CURRENT READING` (score 12/15, evidence 1/3).

### CHAIN F — allele-level protein rescue (M7), and CHAIN G — allele-level sequence correction (M8)

These two chains are **deliberately not combined**. Lever assignment is per allele.

**Chain F (SDR missense worked example, Q230P):**
```
normal transcript + protein NOT DETECTED in patient fibroblasts     [measured]
  → cause UNRESOLVED: impaired translation OR insolubility OR premature degradation
                                                        [the source does not discriminate]
  → severity tracks residual FUNCTION, not abundance    [CLAIM 030 — allelic series:
                                                         P47T protein present (not quantified) + PPPY binding abolished-or-near-abolished in vitro -> MILD; [corretto 2026-09-28 da «P47T normal protein + abolished PPxY -> MILD;» in `BATCH_20260928_007`, census decision-A1 `L2` sito 3 (`CC-20260928-A1-RESIDUE-01` §4)]
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

Source-link reconciliation (2026-10-25): the `SOURCE_IDS` rows of R-01, R-03 and R-07 carry the
identifiers resolved by Scientist C in
[`module_linkage_and_replicate_scientist-c_20261024.md`](../research/module_linkage_and_replicate_scientist-c_20261024.md)
§§1–2. They identify the existing evidence; they do not establish an independent laboratory,
measure the chloride premise or supply a drug-intervention result.

---

### R-01 — AAV9-hSynI-WWOX (gene addition)

| Field | Value |
|---|---|
| **INTERVENTION** | AAV9, human Synapsin-I promoter, WWOX cDNA; ICV. ⚠️ **Corrected 2026-09-27 — the therapeutic configuration is WPRE-FREE.** The 2021 vector map (Appendix Fig S1A, read at 300 dpi) shows all three constructs WPRE-free, and the 2021 paper never mentions WPRE; the 2026 dose study removed WPRE deliberately (*“we removed WPRE as a proactive risk-mitigation step”*, receipted locator) and states the price: *“this reduction in expression necessitates the use of higher vector doses”*. A WPRE-bearing arm exists in the 2026 paper as a comparator, not as the lever |
| **TARGET** | the WWOX locus product itself — neuronal WWOX protein |
| **SOURCE_IDS** | PMID 34747138, PMID 42422765 (WWOX primary measurements; one laboratory); PMID 42128308 remains the class-level safety review, NOT WWOX EVIDENCE for ganglion toxicity |
| **MECHANISM** | supplies full-length WWOX to neurons, bypassing every allele (gene addition) |
| **EVIDENCE_LEVEL** | **T1** (Wwox-null mouse, WWOX-KO and WOREE-derived organoids) + **T6** for human efficacy |
| **WWOX_DIRECT_EVIDENCE** | Yes — multi-domain rescue: survival, growth, glycaemia, behaviour, ataxia, myelination, gliosis, SWD/ECoG; durable to P300; organoid firing normalized (P=0.77 vs parental) — ⚠️ updated 2026-10-29 (IT6 P7): in the mouse this is early-window prevention (P0 to P5, animals never measured before treatment), not recovery of a manifested deficit; the only post-onset add-back is organoid (week 10 on a phenotype seen at week 7, radial glia not corrected) |
| **NEAR_DISEASE_EVIDENCE** | AAV9 CNS gene addition is clinically established in SMA; not transferable as dose or window |
| **HUMAN_USE_STATUS** | first-in-human compassionate n-of-1 reported at **news level only**, not peer-reviewed |
| **CLINICAL_MATURITY** | industrial partner and regulatory route exist; **no open trial**; efficacy in humans **not demonstrated** |
| **BBB_RELEVANCE** | bypassed — direct CNS administration (ICV) |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ⚠️ **decisive and limiting.** **P0–P5 is the interval that was TESTED in mouse, not a demonstrated boundary** — daily arms from P0 to P5 with at least three littermates per time point, and *«Therapeutic rescue beyond this early postnatal window was not explored»* (⚠️ the paper's own abstract says *«(P1–P5)»* where its Results say *«between P0 and P5»*; the lower bound is not stated consistently, and the dossier's Figure S8 audit reads fewer arms than the body declares — a text-versus-panel discrepancy, recorded and unresolved). Neuronal rescue does **not** repair the prenatal progenitor/radial-glia defect — **that limb is measured, and it is the one this row rests on.** 🔴 **The age slope is retired as unsourced (2026-09-28):** the authors attribute the untested exterior to *«model-specific biological constraints and technical limitations, rather than a definitive boundary for therapeutic responsiveness»* and allow that humans may permit later intervention. `NOT_MEASURED ≠ SMALLER` |
| **REVERSIBILITY_REQUIREMENT** | ❌ **not met — AAV persists.** REVERS score 0, the only 0 in the portfolio |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | 🔴 **TRANSFERRED (T4/T5), relabelled 2026-09-27** — dose-limiting DRG/peripheral-ganglion toxicity at high systemic dose is a **class-level statement from a review** (PMID 42128308 §11) and **no DRG assessment exists in either WWOX paper**; the WWOX-measured PNS fact is biodistribution, not toxicity (sciatic-nerve blot, unquantified, variable across seven high-dose animals); supraphysiological and regionally uneven long-term expression in survivors; PNS/spinal-cord biodistribution; tumour non-finding qualified three times (*gross*, *limited number*, *8–11 months*) in a **tumour suppressor** whose periphery remains null; the organoid work shows loss of the apoptotic checkpoint — **neither too little nor too much WWOX** |
| **EXPECTED_DIRECTION_OF_EFFECT** | restore protein toward physiological, **not** above it |
| **MAIN_TRANSLATIONAL_RISK** | the **window**. Also: a **threshold**, not a gradient — at the printed LD (1.23 × 10¹¹ vg) survival is not rescued while the printed HD (2.63 × 10¹¹ vg) plateaus, so the threshold lies **between** the two and "a lower, safer dose" is refused by the data. ⚠️ **Corrected 2026-09-27:** the earlier wording (“below 2.63 × 10¹¹”) read the upper bracket as the threshold, and the primary never states the dose unit — bare `vg`, no dose in the Methods, bilateral ICV at 2.0 µL/hemisphere — so the **absolute** endpoints are uncertain by a factor of 2 (`LD ∈ [1.23, 2.46]`, `HD ∈ [2.63, 5.26] × 10¹¹ vg`) while the **ratio** `HD/LD = 2.1382` is invariant. Specify any intermediate arm as a fraction of the primary’s HD, never in absolute vg (`CC-20260922-CLAIM011-DOSE-ENDPOINTS-01`) |
| **DECISIVE_PRECLINICAL_TEST** | **delayed, post-onset dosing in a hypomorphic (non-null) model**, with SWD/ECoG and myelin readouts; plus an **intermediate-dose arm between 1.23 and 2.63 × 10¹¹ vg** to localize the threshold |

**Class:** `SPLIT` — written into the record itself on 2026-09-27 (`BATCH_20260927_004`, `CC-20260826-AAV9-ENDPOINT-SPLIT-01` Part 2, op 4), because one class label over nine endpoints was the defect. **`READY_FOR_WWOX_PRECLINICAL_CONSIDERATION`** for **survival · spike-wave discharges · gliosis**, at **high dose**, in the **P0–P5** window. **`PROMISING_BUT_GAP`** for **cognition · developmental trajectory · myelination-in-the-dose-study · cerebellum · post-neonatal administration** — none of these is measured, quantified in a treated arm, or reached by the vector at a level any efficacy endpoint tested. ⚠️ **Motor/locomotor behaviour is in neither list:** the source's running text asserts no locomotor difference (*«showed no significant differences between groups (Figures 4B, 4D–4G)»*) and in its own voice asserts one exceedance outside that set (*«Treated KO mice exhibited significantly higher motor coordination and learning compared with WT mice (Figure 4K).»*), while the panel-level count that would adjudicate the conflict is a **declared attestation over absent bytes**. `NOT_IMPAIRED_AND_NOT_NORMALISED`, and the conflict is recorded rather than resolved. It remains the only entry in the ready class for the three endpoints named.

**Curated card (added 2026-10-27):** the qualified endpoint rows are in `research/drug_repurposing/cards/C01_aav9_wwox.card.json` (spike-wave discharges) and `research/drug_repurposing/cards/C04_aav9_endpoint_families.card.json` (survival, weight, glucose, motor score, gliosis, myelination, each with its comparator and limit); `repurposing_join.py` reads it for this record.

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

**Curated card (added 2026-10-27):** the NMDA-receptor dependence measured with the tool antagonist d-APV (memantine itself never given to a WWOX system), the human GRIN precedent and the adverse wild-type rat datum are in `research/drug_repurposing/cards/F01_glutamate_receptor_node.card.json`; `repurposing_join.py` reads it for this record.

**Consequence note (2026-10-27, `CC-20261027-SCIENTIST-C-W2-THERAPEUTIC-01`, EXPLORATORY, no status change):** the GRIN2A convergence corroborates the node, not the sign of intervention (memantine benefit tracks gain-of-function GRIN variants in another disease, 14 of 19 with 4 transient versus 3 of 15; retrospective, unblinded); the GRIN2A variant class in the cohort abstract is not stated (abstract only, `NO_RECEIPT`). Derived hypothesis: `HYP-20261027-01`.

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P9; EXPLORATORY; the Class and the T2 scoring are unchanged).** The DECISIVE_PRECLINICAL_TEST above is superseded as a DISCRIMINATOR by card `F04_nmdar_intervention_class` (F01 stays as the record of the registration of 2026-10-27): a drug effect on bursting does not say which reading of the d-APV result is true (an AMPAR antagonist is expected to stop an NMDAR-dependent burst too), memantine is a state-dependent pore blocker whose effect here may be a GluN2D interneuron effect or an Mg2+ artefact, and the first measurement is the isolated NMDAR current under voltage control; a GluN2B-selective negative allosteric modulator is a candidate first drug arm and memantine a candidate translation probe afterwards (a proposal, not a ranking). No NMDAR drug is carried forward on the d-APV result alone.

---

### R-03 — Wnt / tankyrase inhibition

| Field | Value |
|---|---|
| **INTERVENTION** | tankyrase inhibitor (e.g. XAV939 as tool); no paediatric-profiled candidate identified |
| **TARGET** | Wnt/β-catenin |
| **SOURCE_IDS** | PMID 34268881 (WWOX organoid endpoint); CLAIM 028 is context-dependence evidence, not the source of the β-catenin measurement |
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

**Curated card (added 2026-10-27):** the qualified disease-side row and the abstention are in `research/drug_repurposing/cards/D02_wnt_tankyrase.card.json`; `repurposing_join.py` reads it for this record.

---

### R-04 — Lithium (GSK3β)

| Field | Value |
|---|---|
| **INTERVENTION** | lithium carbonate |
| **TARGET** | GSK3β (among many) |
| **MECHANISM** | claimed: inhibits a kinase de-repressed by WWOX loss |
| **EVIDENCE_LEVEL** | 🔴 **T5, not T2.** The WWOX experiment **failed its specificity test**: lithium suppressed PTZ seizures in **all three genotypes, wild type included**. What was shown is an anticonvulsant working in an animal that has seizures |
| **WWOX_DIRECT_EVIDENCE** | GSK3β **Ser9 phosphorylation reduced** in Wwox-null cortex/hippocampus/cerebellum, read by the authors as activation (one western, one site, `STATISTICAL_STATUS: NOT_TESTED`; `WWOX AND GSK3` returns 5 PubMed records in total). **No cited source reports elevated abundance**, so the premise *abundance reports activity* has no datum under it — ⚠️ and the narrower correction the 2026-09-27 blind audit forced: total GSK3β **is** blotted and densitometered in Wang 2012's Figure 1, so what is missing is its **stated invariance**, not the measurement (`BATCH_20260927_004`, `CC-20260826-GSK3B-S9-AXIS-01` `D8`/`D13`) — and the load-bearing premise *abundance reports activity* is tagged `PREMISE: DEFAULT_FROM_TEXTBOOK`, because in this very system abundance and activity are **dissociable** (S9-independent inhibition) |
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
| **SOURCE_IDS** | CLAIM 016, CLAIM 035, PAPER 019, PAPER 056 |

**Class:** `DEPRIORITIZE` — not for toxicity, but because **the evidence that made it the strongest
signal does not say what it was read as saying**, and its direction is wrong on a second axis.

**Curated card (added 2026-10-27):** the qualified rows, including the three-genotype specificity failure, are in `research/drug_repurposing/cards/G01_lithium_gsk3.card.json` (also linked from N-02); `repurposing_join.py` reads it for this record.

---

### R-05 — Ketogenic diet

| Field | Value |
|---|---|
| **INTERVENTION** | ketogenic diet |
| **TARGET** | TCA entry, downstream of the PDK1→PDH block |
| **MECHANISM** | ketone bodies enter as acetyl-CoA **below** the block, without needing PDH reactivation |
| **EVIDENCE_LEVEL** | **T3/T4** empirically (standard of care in DEE; GLUT1-deficiency is treated with it) + **T2** for the WWOX-specific rationale |
| **WWOX_DIRECT_EVIDENCE** | PDK1/GLUT1/HK2/PKM2 measured up in Wwox-KO; OXPHOS↓/glycolysis↑ in human WWOX-KO cerebral organoids (transcriptome). Clinically: improved seizure control reported for 3 patients of a 5-patient WOREE series (CLAIM 042: uncontrolled; the number of patients exposed to the diet is not stated, so 3/5 is not a response rate; responders carry splice-region or deletion alleles, none missense) |
| **NEAR_DISEASE_EVIDENCE** | strong across genetic DEE generally |
| **HUMAN_USE_STATUS** | established paediatric intervention |
| **CLINICAL_MATURITY** | highest in the file — an existing protocol with existing monitoring |
| **BBB_RELEVANCE** | ✅ ketone bodies are actively transported |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | ✅ established, with known monitoring (acidosis, lithiasis, growth, dyslipidaemia) |
| **REVERSIBILITY_REQUIREMENT** | ✅ fully — stoppable immediately |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | 🟢 the lowest-risk entry: no new molecule, no BBB problem, risk managed by an existing protocol |
| **EXPECTED_DIRECTION_OF_EFFECT** | restore oxidative flux; **NOT** a demonstrated developmental modification |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 the rationale rests on models; **human WWOX metabolism is reported normal in the cases screened (the count "four independent sources" is not reconciled with N-06)**, and the real-world continuation signal is poor (1/3 continued; listed among ineffective interventions in a severe case) |
| **DECISIVE_PRECLINICAL_TEST** | **Seahorse OCR/ECAR on donor-derived fibroblasts/LCL vs control** — a general bioenergetic screen, NOT PDH-specific and not the only possible falsifier (correction 2026-10-27: add PDH activity in a phosphorylation-preserving lysate, phospho-PDHA1, 13C-glucose/ketone tracing, pyruvate/lactate ratio, NADH/NAD+). Second test: Seahorse on the existing WWOX-KO organoids (human neural, but a different maturity than the donor cells), narrowing the transcriptome→flux gap |
| **SOURCE_IDS** | CLAIM 042, CLAIM 020, DL-MECH-020 |

**Class:** `PROMISING_BUT_MECHANISTIC_GAP` — the gap being **transcriptome vs flux**, which one
experiment closes.

**Curated card (added 2026-10-27):** the clinical seizure-control rows are in `research/drug_repurposing/cards_early/EB-KD-01.card.json` and the lactate and PDH rows of the metabolic rationale in `research/drug_repurposing/cards/E04_ketogenic_lactate_axis.card.json`; `repurposing_join.py` reads it for this record.

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
| **SOURCE_IDS** | CLAIM 006, DL-REPO-002 |

**Class:** `TRANSFER_HYPOTHESIS`.

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P10; EXPLORATORY).** The direction of the glial change is NOT resolved across the Wwox models: the rat lde/lde cortex shows LOWER GFAP-positive and Iba1-positive cell density from PND 5, the null mouse and the P47T knock-in an excess, and the human knockout organoid no reactive programme at week 15; every glial read in the mouse is after the first seizures, and no glial compartment can be assigned as cause. The lead stays an abstention (card `J01_glial_reactivity_modulation`; `DL-REPO-002` update); the discriminating experiment is a within-species time course of glial density before and after the first spike.

---

### R-07 — Bumetanide (NKCC1 / chloride gradient)

| Field | Value |
|---|---|
| **INTERVENTION** | bumetanide |
| **TARGET** | NKCC1 |
| **SOURCE_IDS** | DL-MECH-035 (WWOX organoid marker pattern; no measured chloride premise or bumetanide intervention) |
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

**Curated card (added 2026-10-27):** the abstention and the experiment that would end it are in `research/drug_repurposing/cards/F03_bumetanide_chloride_gradient.card.json`; `repurposing_join.py` reads it for this record.

**Consequence note (2026-10-27, `CC-20261027-SCIENTIST-C-W2-THERAPEUTIC-01`, verified against ChEMBL_37):** ChEMBL curates bumetanide's mechanism as NKCC2 only (SLC12A1); NKCC1 is an activity-table fact (three rows, none a curated mechanism). The experiment specification is in card `F03`. No status change.

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
| **SOURCE_IDS** | DL-MOL-011 |

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
| **SOURCE_IDS** | CLAIM 019, DL-MECH-036, DL-MECH-037, DL-BIO-001 |

**Class:** `PROMISING_BUT_MECHANISTIC_GAP` — the gap is causal, not pharmacological: the branch has
not been discriminated.

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P5 and P6; EXPLORATORY; NOT WWOX EVIDENCE for every external item).** A proposed order of work, not a ranking: the wild-type function ruler first (see the discovery-ledger update of 2026-10-29 on abundance and function), then fate, then levers. In the best-resolved cytosolic-enzyme precedent (cystathionine beta-synthase) route blockade returned protein of unequal worth (sufficient for one allele, partial for three, null for one, wild type rising alongside, exposure toxic), and in ASPA C152W it accumulated insoluble pellet protein with no measurable activity (yeast and U2OS; earlier reports also found no residual activity); no experiment gave a route blocker to a WWOX missense system beyond the P252A route arms, and no precedent separates stabilisation from a transcript effect. The class stays a probe (card A02 revised; A05 an abstention). Details: the hypotheses-ledger update of 2026-10-29 on the missense allele.

### R-10 — ISRIB-class eIF2B activators and other ISR attenuators (class-level; added 2026-10-26 from the Lucas-Clarke follow-up)

| Field | Value |
|---|---|
| **INTERVENTION** | class-level: eIF2B activators (ISRIB and clinical-stage successors), PERK-arm inhibitors, repurposed compounds that reverse eIF2 alpha-P translational repression; the card is `research/drug_repurposing/cards/E01_isr_modulators.card.json` |
| **TARGET** | the eIF2B complex (EIF2B1-5, HGNC:3257-3261) or the PERK arm (EIF2AK3, HGNC:3255); node: integrated stress response, ATF4 output |
| **MECHANISM** | if a WWOX-dependent, harmful ISR elevation exists in WWOX-deficient neural cells, attenuating it protects function; the elevation is shown only in a Drosophila amyloid model (Atf4 signal, n 6) and only with amyloid |
| **EVIDENCE_LEVEL** | **T6** for WWOX (fly, amyloid-conditional, correlational); the human knockout organoid transcriptome points the other way, while a second human transcript system (shRNA-silenced progenitors, one library per arm, knockdown not demonstrated in that library) points the same way as the fly: the sign is UNRESOLVED between systems of very different design (exploratory; updated 2026-10-29) |
| **WWOX_DIRECT_EVIDENCE** | none in any WWOX-deficient human system; ATF4/ISR target transcripts LOWER than chance in the knockout organoid deposit (four against two libraries) and HIGHER in the shRNA-silenced progenitor and neuron libraries (n=1 per arm, possibly native control, cell state differs between arms); neither system measures ATF4 protein or eIF2 alpha phosphorylation, so no human transcript signal is the sign of a WWOX-dependent ISR change (exploratory; updated 2026-10-29) |
| **NEAR_DISEASE_EVIDENCE** | eIF2B activator: target engaged without benefit in adult ALS; memory and tau improved in a mouse amyloid model; guanabenz in children with vanishing white matter, a non-randomised benefit with frequent adverse events (abstract-level) |
| **HUMAN_USE_STATUS** | family-dependent: clinical-stage (eIF2B activators), research tools (ISRIB, PERK inhibitors), licensed for other uses (trazodone, guanabenz) |
| **CLINICAL_MATURITY** | 🔴 not design-ready for WWOX: no signed human readout |
| **BBB_RELEVANCE** | brain-penetrant members exist (phase 1b CSF distribution reported for one eIF2B activator); not assessed for WWOX |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | paediatric experience exists only for guanabenz in vanishing white matter; chronic ISR attenuation in a developing brain is an open safety question |
| **REVERSIBILITY_REQUIREMENT** | pharmacological, reversible in principle |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | PERK inhibition: signs of pancreatic toxicity in a mouse model; a research eIF2B activator stopped for cardiovascular effects in higher species; guanabenz: hallucinations in over half of 33 children and serious adverse events in three quarters (abstract-level); trazodone label: paediatric safety not established |
| **EXPECTED_DIRECTION_OF_EFFECT** | lower ISR output; whether lower is better in WWOX-DEE is the unresolved question |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 the readout the lever needs does not exist in a human WWOX system, and the ISR may be adaptive |
| **DECISIVE_PRECLINICAL_TEST** | **eIF2 alpha phosphorylation** and **ATF4 protein** (with ATF4-target transcripts) in WWOX-deficient versus isogenic human neural cells at matched maturity, with and without a defined proteotoxic challenge; only if elevated, an eIF2B activator against vehicle on that readout and one functional endpoint |
| **SOURCE_IDS** | PAPER 567 (the single reading behind the fly rows; related records are listed in the card, not here, so that the join does not inherit unrelated families of papers) |

**Class:** `READOUT_FIRST` — Track A, route BENEFICIO_PRECOCE; the first experiment is the readout, not a drug.
Fly content is NOT WWOX-DEE evidence. Not medical advice.

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P3 and P4; COMPUTATIONAL_RESULT at transcript level).** A third system does not break the tie: in mouse P17 brain with an unambiguous Wwox deletion (four contrasts, 2 to 4 animals per arm) the ISR target set is inside its matched null in every contrast, with no resolvable sign at about 0.3; Atf4 mRNA alone is lower in all four (an mRNA observation, not an ISR call). A census of public deposits found no deposited proteome, phospho-proteome, translation, eIF2 alpha phosphorylation, ATF4 protein or flux record for a genetically WWOX-deficient neural system (not found by that search is not shown absent; non-neural records exist, given as examples in the discovery-ledger update of 2026-10-29 on the integrated stress response), so the DECISIVE_PRECLINICAL_TEST above stays the next step.

---

### R-11 — Stiripentol (LDH-lowering rationale; added 2026-10-26 from the Lucas-Clarke follow-up)

| Field | Value |
|---|---|
| **INTERVENTION** | stiripentol as the approved paediatric epilepsy member of an LDH-lowering lever; LDHA tool compounds and an LDHA-directed oligonucleotide (approved for primary hyperoxaluria, liver-directed) are context; the card is `research/drug_repurposing/cards/E02_ldh_inhibition.card.json` |
| **TARGET** | LDHA (HGNC:6535, P00338) and LDHB (HGNC:6541, P07195); node: lactate production |
| **MECHANISM** | if lactate or LDH activity is raised and harmful in WWOX-deficient neural cells, lowering LDH lowers lactate and improves function; in the fly, Ldh RNAi added to amyloid plus Wwox reduction improved climbing once |
| **EVIDENCE_LEVEL** | **T6** for WWOX (fly, amyloid-conditional, missing controls); human LDHA transcript up in the knockout organoid (confounded with maturity) and in the shRNA-silenced progenitor library (n=1 per arm; there the progenitor markers fall, so a single less-advanced-tissue explanation does not cover both systems); lactate and ECAR unmeasured in human neural cells (updated 2026-10-29) |
| **WWOX_DIRECT_EVIDENCE** | none at the activity or lactate level in a human WWOX system |
| **NEAR_DISEASE_EVIDENCE** | stiripentol is approved for Dravet syndrome seizures with clobazam; its LDH inhibition is unresolved, with single-concentration measures only: about forty percent at one high-micromolar concentration (second-hand, from a 2015 report whose full text is not held and is UNREAD here), about a tenth (racemate) to a third (enantiomers) at the same concentration and a bound for the potency in a 2024 paper (partial full-text reading, PAPER 568), single-digit percent at a four-fold higher concentration in a database document (Bai 2019); the 2015 report attributes seizure suppression in epilepsy models to LDH inhibition (abstract-level) while a 2024 review argues, on exposure, that other mechanisms dominate its antiseizure action; stiripentol also inhibits mitochondrial complex I directly (2026) [corrected 2026-10-27 by `BATCH_20261019_022` from «its LDH inhibition is weak in the retrieved measurements (…); no source attributes its antiseizure action to LDH»; `CC-20261026-SCIENTIST-B-SADA-LDH-01`] |
| **HUMAN_USE_STATUS** | approved in the US for seizures associated with Dravet syndrome in patients taking clobazam, from six months of age (openFDA label 2026-04-27) |
| **CLINICAL_MATURITY** | marketed for another indication; 🔴 no WWOX rationale beyond a fly precedent |
| **BBB_RELEVANCE** | acts on seizures in the brain; brain LDH engagement is unmeasured |
| **PEDIATRIC_OR_DEVELOPMENTAL_RELEVANCE** | paediatric label for the approved use; WWOX-DEE not assessed |
| **REVERSIBILITY_REQUIREMENT** | pharmacological, reversible in principle |
| **KNOWN_MAJOR_SAFETY_CONSTRAINTS** | labelled use depends on co-therapy with another antiseizure drug; interactions are not assessed here; most-reported spontaneous-report terms include seizure, drug ineffective, decreased appetite, somnolence (counts, not rates); the source paper cites Ldh knockdown as detrimental in other fly amyloid models |
| **EXPECTED_DIRECTION_OF_EFFECT** | lower lactate production; unmeasured |
| **MAIN_TRANSLATIONAL_RISK** | 🔴 benefit would not be attributable to LDH (other pharmacology), and lactate in WWOX deficiency is reported normal or extremely low in humans (human readouts are listed in the card) |
| **DECISIVE_PRECLINICAL_TEST** | an assay-level potency and mode determination of stiripentol on human LDHA and LDHB (with a selective LDHA positive control, detergent and substrate-level arms), then **lactate** (enantiomer- or isotope-resolved) in the double-RNAi fly genotype with an Ldh-alone arm; **LDH activity** and the lactate-to-pyruvate relationship in WWOX-deficient versus isogenic human neural cells at matched maturity; then stiripentol against a selective LDHA tool at matched exposure |
| **SOURCE_IDS** | PAPER 567 (the single reading behind the fly rows; related records are listed in the card, not here, so that the join does not inherit unrelated families of papers) |

**Class:** `READOUT_FIRST` — Track A, route BENEFICIO_PRECOCE. Fly content is NOT WWOX-DEE evidence. Not medical advice.

🔵 **Update 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P4; COMPUTATIONAL_RESULT).** The LDHA and glycolysis rise is seen in two human neural transcript systems only and is not extended to mouse P17 brain with Wwox deletion (10-gene lactate set -0.09 and -0.19, 19-gene panel -0.07 and -0.09 in the cell-targeted hippocampal contrasts; nothing outside the null there); the statement stays set-dependent and two-system (see the discovery-ledger update of 2026-10-29 on LDH lowering).

---

## 5. Negative translation — candidates that should be deprioritized, and why

*A well-reasoned exclusion is worth as much as a promotion.* Each carries its **failure mode**, and
each carries what would **revive** it — nothing dies silently.

### N-01 — mTOR inhibitors (rapamycin / everolimus) → **`INSUFFICIENT` — mai misurato a livello proteico in alcun sistema WWOX**
**Source ids:** PAPER 039, DL-MECH-034.
**Failure mode:** *`INSUFFICIENT` — mai misurato a livello proteico in alcun sistema WWOX.* The reflex move in genetic DEE, imported from TSC.
The only WWOX-specific measurement touching this axis shows **mTOR/EIF4EBP1 DOWN and autophagy DOWN**
in WWOX-KO cerebral organoids. An mTOR inhibitor would push the **same direction as the only directional datum** — a **non-locatored transcriptomic signal at n = 2/4**, **not a measurement of mTORC1 signalling**.
⚠️ **Honest weight of the negative:** this rests on one transcriptomic dataset (`n=2` WT vs `n=4` KO,
EV selection at raw `P<0.01`), so it is a **weak measurement pointing the wrong way**, not a
demonstration of harm. The correct verdict is therefore *no positive rationale exists, and the only
directional datum is unfavourable*.
**`REVIVAL_TRIGGER`:** a protein-level mTORC1 readout (pS6, p4E-BP1) in a WWOX-deficient neuronal
system; or any WWOX model showing mTORC1 **hyper**activation.

**Curated card (added 2026-10-27):** the abstention (mTOR activity in a WWOX system is unmeasured) is in `research/drug_repurposing/cards_early/EB-MTOR-AX-01.card.json`; `repurposing_join.py` reads it for this record.

### N-02 — Lithium as a WWOX-specific disease modifier → **the evidence does not say what it was read as saying**
**Source ids:** CLAIM 016, PAPER 019.
**Failure mode:** *evidence transfer that was never genotype-controlled*, compounded by *wrong
direction on a second axis*. Lithium suppressed PTZ seizures in **all three genotypes including wild
type**; and lithium activates Wnt, which is already hyperactivated. It remains an anticonvulsant; it
is not a WWOX-mechanism drug.
**`REVIVAL_TRIGGER`:** a PTZ arm with an explicit tested `−/−` vs `+/+` contrast, or a different
GSK3β inhibitor under the same design.

**Curated card (added 2026-10-27):** the qualified rows are in `research/drug_repurposing/cards/G01_lithium_gsk3.card.json` (the same candidate as R-04); `repurposing_join.py` reads it for this record.

### N-03 — Sodium-channel blockers (carbamazepine, phenytoin, oxcarbazepine) → **target not causally downstream of WWOX**
**Source ids:** DL-REPO-001.
**Failure mode:** *the target is not causally downstream of WWOX.* Precision therapy in
burst-suppression DEE is gene-dependent: Na-blockers serve the Nav channelopathies (KCNQ2-GoF,
SCN2A). The WWOX node is NMDAR/gap-junction. The value here is **differential** — it excludes a whole
class and redirects attention to R-02.
**`REVIVAL_TRIGGER`:** documented Na-blocker response in WWOX-BS cases, or a Nav dependence measured
in a WWOX model.

### N-04 — Broad GABAergic push (chronic high-dose benzodiazepines; vigabatrin as a mechanism play) → **premise unmeasured; a documented MRI-abnormality liability whose WWOX excess is not shown**
**Source ids:** CLAIM 001, CLAIM 031, DL-MECH-035.
**Failure mode:** *corrects a marker, not the mechanism* — plus an unmeasured premise. VABAM is
documented in two WWOX-DEE children (case-selected, no denominator of exposed WWOX children; the label's 22 against 4 percent concerns non-WWOX infants, so enrichment in WWOX is not supported); and the depolarizing-GABA rationale **failed as a clinical predictor**
(vigabatrin resolved spasms in a WWOX-null child). Both directions of the conflict are live: efficacy
on spasms (n=2) against MRI toxicity (n=2). **Neither closes the question.** The canonical position
is unchanged: caution / avoid unless alternatives are exhausted, with the risk explicitly documented.
**`REVIVAL_TRIGGER`:** `E_GABA` measurement in a WWOX system; or a WWOX cohort with structured VABAM
surveillance imaging.

### N-05 — Boosting WWOX expression alone (CRISPRa, anti-miR-153, small-molecule activators) → **downstream bottleneck, and an allele-asymmetric amplifier**
**Source ids:** DL-MOL-004, CLAIM 019, DL-MECH-069.
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

**Curated card (added 2026-10-27):** the abstention is in `research/drug_repurposing/cards/C03_crispra_boost.card.json`; `repurposing_join.py` reads it for this record.

### N-06 — Lactate, and metabolic blood biomarkers generally, as WWOX readouts → **a biomarker that is not measuring the mechanism**
**Source ids:** DL-BIO-008.
**Failure mode:** *corrects/reports a biomarker, not the mechanism* — inverted: here the biomarker
does not even report. **Counted from the record rather than asserted:** `DL-BIO-008` names **three**
sources, of which **two are human and one is a complete human metabolic screen** — a WWOX
null/null patient of whom the paper itself writes *"Normal results were found in metabolic screening
including liver and renal function tests, complete blood count, blood gas analyses, ammonia, serum
lactate, plasma urea, electrolytes, urine and serum amino and organic acids, and very long chain
fatty acids"* (`PAPER 043`; the phrase *"entirely normal"* is the ledger's compression, not the
paper's words, and carried quotation marks in this record until 2026-10-24). The second human source
is the **single MRS case** (`PAPER 044`), which reports cerebral lactate
*"extremely low"* — the **opposite** of what the Warburg model predicts — in a patient with a
confounding HSPG2 variant. The third source is a **mouse** (`PAPER 024`): `Wwox`-KO serum lactate significantly
raised, which is the direction the model predicts and the reason the record exists as an unresolved
contradiction. Serum lactate is Tier 3, distal, and must not enter the Tier 1/2 biomarker file.
⚠️ **The conclusion is unchanged and its support is smaller than this record claimed.** *Count revised 2026-10-27 by independent verification (`research/locator_audits/2026-10-27_hypcurrent_independent_verification.md`): the count of ONE screen above is also an undercount. `DL-BIO-009` names a second primary human source, Shaukat 2018 (`PAPER 045`, two children, lactate, ammonia, acylcarnitines, amino and organic acids all normal), which `DL-BIO-008` omits; the best statement is **two primary sources (3 patients) with normal blood and urine screens, one secondary normal MRS, and one opposite-direction MRS case**, none of them a mitochondrial or muscle study.* Two normal screens plus one opposite-direction human MRS case is enough to say the biomarker **does not
report reliably**; it is not four concordant human sources, and the human direction of WWOX-deficient
metabolism remains **unmeasured** (`DL-BIO-008`, operative consequence 3).
*Count corrected 2026-10-24 by `scientist-b`, re-derived from `DL-BIO-008` as it now stands. The
earlier wording — "four independent human sources show normal metabolism" — was an **unsourced
count**: the record names one such screen and the other three sources are identified nowhere
(measured independently by `scientist-c`,
`research/module_linkage_and_replicate_scientist-c_20261024.md` §1); the duplicate at row C10 of
`analysis/therapeutic_translation_second_pass.md` was corrected the same day. The attribution of the
three sources was adjudicated by blind audit on 2026-10-24
(`research/page_adjudications/locator_audit_map_repairs_20261024.md`): the complete human screen is
`PAPER 043`, and `PAPER 044` holds the MRS and **no metabolic screen at all**. Paper-faithful
wording substituted for the ledger's compression on the same date and from `PAPER 043`'s artefact.*
**`REVIVAL_TRIGGER`:** Seahorse/fluxomics showing a real bioenergetic shift in donor-derived cells.

### N-07 — Digoxin (HIF1α inhibition) → **right target validation, wrong clinical object**
**Source ids:** PAPER 091, CLAIM 025.
**Failure mode:** *toxicity incompatible* + *wrong endpoint*. The only approved drug that corrects a
Wwox-dependent phenotype **in vivo** — which makes it strong **target validation** for HIF1α/PDK1. But
its endpoint in the mouse was **glycaemia**; the endpoint that matters here is **neuronal
bioenergetics**. Not the same clinical target. Cardiac glycoside, extremely narrow therapeutic index,
dose-dependent cardiac **and neurological** toxicity. The reported dose (100 mg/kg i.p.) is very
likely a typographic error for µg/kg and remains unverified against the original PDF.
**Use correctly:** as target validation. The ketogenic diet **dominates** it — same axis,
incomparably better safety.

### N-08 — Dichloroacetate (PDK inhibition) → **a peripheral-nerve signal that was asymptomatic throughout the one long-term cohort, symptomatic in a separate trial; and never measured in a WWOX system**
**Source ids:** PAPER 557, PAPER 562 (both 🔴 **NOT WWOX EVIDENCE**, class-level), DL-MECH-020 (the
WWOX-side Warburg/HIF1α rationale — the only WWOX anchor this row has).
**Failure mode:** *two-hop inference* + *a safety margin that has never been measured in this
disease*. **The population first, because this record got it wrong twice.** The long open-label
safety study is **not a paediatric series**: 8 patients (4 males) with proven deficiency of the PDC
E1α subunit or of respiratory-chain complexes, followed for 9.7 to 16.5 years, and *"Patients (**1
adult**) ranged in age from 3.5 to 40.2 years at the start of DCA administration and are currently
aged 16.9 to 49.9 years"*. The authors' own scope is *"generally very well tolerated in patients
with mitochondrial diseases, **at least from young childhood through early adulthood**"*.
**What the source says.** In that cohort the nerve finding is **electrophysiological, not
clinical**: *"Nerve conduction either did
not change or decreased modestly and led to reduction or temporary discontinuation of DCA in 3
patients, although symptomatic worsening of peripheral neuropathy did not occur"*; in the body,
those three had the drug paused or halved *"because of periodic **asymptomatic** worsening of lower
extremity nerve conduction velocity"*, and the change was *"not associated in any patient with
changes in blood lactate or with any abnormalities in blood chemistries"*. The **symptomatic** cases
come from a different study: the same authors contrast their result with *"a RCT conducted in older
adolescents and adults with mitochondrial encephalomyopathy, lactic acidosis and stroke-like
episodes (MELAS) that ended prematurely because of symptomatic and electrical evidence of
exacerbation or new onset of peripheral neuropathy"*. They also state the design's limit
themselves: it *"cannot distinguish unequivocally between the relative impact of DCA exposure vs.
underlying disease on the frequency or severity of peripheral neuropathy"*, because neuropathy is
common in mitochondrial disease before any DCA.
⚠️ **And the age explanation cannot carry the symptom split — this record previously implied it
could.** The authors do state that *"DCA metabolism in humans is inversely proportional to age"* and
that GSTZ1 haplotype influences clearance, so **exposure** is age- and genotype-dependent; that
survives. But **symptom status does not follow age inside this cohort**: the nerve effect
*"persisted longest (up to 39 months before restarting DCA) in patient 8, who, to our knowledge, is
the oldest subject to be chronically treated with the drug"* — and it was still **asymptomatic**,
like the other two. So the paediatric/adult contrast between the two studies is **not explained by
this paper**, which instead postulates a combination of *"technical variability in electrical
measurements, the waxing and waning of the underlying disease, chronic DCA exposure and advancing
age"*. What the pharmacokinetic sentence supports is a statement about **exposure**, not about who
becomes symptomatic.
⇒ **Still parked, and for a reason that survives the narrowing.** The honest statement is *a drug
whose nerve signal in the one long-term cohort was asymptomatic and reversible in 3 of 8 across an
age range from early childhood to adulthood, but required nerve-conduction monitoring, with exposure
rising as age rises and varying with GSTZ1 genotype, and with no proof of mechanism in this disease*
— not *dose-dependent neurotoxicity in a child*. Parked pending `legend-safety-triage`, and
downstream of the falsification of R-05 anyway.
⚠️ **Not a denial, and two things are explicitly not measured.** (1) **No paper measures
dichloroacetate in any WWOX system**, of any species — the row's intervention arm is non-WWOX
throughout, so the *benefit* side of the ratio is unmeasured too, and nothing here says the compound
is safe in this genotype (measured independently by `scientist-c`,
`research/module_linkage_and_replicate_scientist-c_20261024.md` §1: attaching `PAPER 557` and
`PAPER 562` closes a **linkage** gap and leaves the **evidence** gap exactly as wide). (2) The word
**"dominated"** — kept in the body, dropped from the headline — is a portfolio judgement on the
shared PDK axis: that R-05 reaches the same metabolic bypass with a profile that needs no nerve
monitoring. It is **not a head-to-head comparison and is untested**: no paper compares them, none was
found, and the one seizure-model paper read for this row argues the opposite sign for a dichloroacetate
**combination** in an acquired-injury rat (`PAPER 562`: dichloroacetate **with pyruvate** reduced
oxidative-stress and glial-activation readouts after pilocarpine seizure, **and significantly reduced
degenerating neurons**; groups of five and eight, one week, one sensorimotor test. The paper's seizure
groups **did include** a dichloroacetate-alone and a pyruvate-alone arm, and it reports that
*"administration of only DCA or pyruvate"* was ineffective on neuronal (NeuN) survival — so the
single-agent negative is **measured in that paper**, not only cited from earlier work, and it is what makes
the effect a property of the **combination**. 🔴 NOT WWOX EVIDENCE; adult male rats, an acquired injury, not
a developmental model; the paper also records a high-dose neurotoxicity ceiling from other work.
*Corrected 2026-10-25 after a blind audit of the 2026-10-24 rewrite found the earlier wording ("citing
prior work, not measuring it") contradicted by the paper's own arms and the neuronal-loss result missing
from the readout list.*)
No dose, administration or suitability is stated or implied here; **not medical advice**.
**Curated card (added 2026-10-26):** the qualified assertions and the target-level pharmacology for the PDK strand are in `research/drug_repurposing/cards/E03_pdk_inhibition_dca.card.json`; `repurposing_join.py` reads it for this record.
**Update 2026-10-29 (card I01, `research/drug_repurposing/cards/I01_pdk_inhibition_dca_premise_seizure_glycaemia.card.json`, IT5 P9; the verdict above is unchanged; NOT WWOX EVIDENCE for every external item; abstract level for most sources).** The strand now has a stated closing condition: close it at the premise if no PDH restraint is shown in a WWOX-deficient neural system, and drop the "PDK1 up" prediction from any priority argument (no transcript support at PDK1 in either human neural system; see CHAIN E). The only primary seizure-endpoint test found of a PDK inhibitor in a PDH-restrained epilepsy model (adult mouse, chronic stage after status epilepticus) showed no anticonvulsant effect and a slight pro-convulsant signal; a randomized paediatric trial in congenital lactic acidosis lowered lactate without benefit on global assessment, growth or intercurrent illness. The safety frame widens from peripheral nerve to nerve plus glycaemia: blood glucose is lowered in three of four datasets with a stated sign (diabetic adults, endotoxaemic minipigs, cirrhotic and healthy adults, where the fall is modest in both groups) and raised back only in a septic mouse (fasting confound), while the Wwox-null mouse dies hypoglycaemic and its hypoglycaemia is rescued by a neuronal promoter; the sign in a hypoglycaemic young animal is unmeasured and the glycaemia concern is not asserted as a contraindication. Next measure: PDHA1 phosphorylation and PDH activity, then a glucose-tracer experiment, in WWOX-deficient against matched control human neural cells, read as a genotype-by-inhibitor interaction (a PDH-deficient line as positive control, a second inhibitor of different chemistry as orthogonal control). Card: `research/drug_repurposing/cards/I01_pdk_inhibition_dca_premise_seizure_glycaemia.card.json`; status `controversial`; no favourable compound is offered. Not medical advice; no dose.
*Narrowed 2026-10-24 by `scientist-b`, re-derived first-hand from the paediatric long-term safety
full text (Abdelmalak 2013, DOI `10.1016/j.ymgme.2013.03.019`, staged receipt
`FTR-20261023-23611579-01`, whose `source_locator` names the artefact) and from that paper's own
citation of the MELAS trial, which was not opened.
The earlier wording — "dose-dependent peripheral neurotoxicity (neuropathy) in a child with
encephalopathy" — had **no source in any registry record** when that was measured on 2026-10-23
(`research/module_batch_selection_scientist-b_20261023.md` §1, §4.1); the registry ids above were
created for this row on 2026-10-24. Sources are named by registry id, DOI and receipt id and **not
by PMID**, because these readings are `partial_fulltext_read` and **staged, not yet recorded**, so a
PMID citation in this layer would open an unread premise against a ratchet at zero headroom.*

### N-09 — pTyr33-WWOX peptide as functional restoration → **the direction is inverted**
**Source ids:** DL-MOL-008, CLAIM 023.
**Failure mode:** *acts in the wrong direction.* Phospho-Tyr33 WOX1 is **pro-apoptotic**; the peptide
**blocks** neuronal death, i.e. it acts as a competitive **inhibitor** of a WWOX-dependent function,
not as its substitute. In a WWOX-**deficient** system, inhibiting WWOX function restores nothing. A
commentary had over-interpreted its own primary source.
**What survives:** possible interest as a **generic neuroprotectant** — a different hypothesis that
does not inherit this rationale. The refutation rests on the abstract (full text paywalled); if the
full text says otherwise it re-opens.

### N-10 — Splice-switching ASO for a canonical acceptor allele → **"not eligible" by the field's own criteria, which say it flatly; what is missing is the measurement that would place this allele in that class**
**Source ids:** DL-MOL-011.
**Failure mode:** *derived from a mechanism that does not do what the design needs.* SSOs **mask**
elements; they do not **create** splice sites. Masking the +8 cryptic site would shift splicing
toward *another* aberrant product, not the wild type. In-frame skipping is **not available here** —
exon 9 is the last exon and carries the stop codon and the final ~62 aa of the SDR; the rat *lde*
model shows that losing the C-terminus destabilizes the protein. The *Milasen* precedent is
**regulatory**, not proof of amenability: it targeted a **gained** cryptic acceptor deep in an
intron, in one patient, and its authors state that only a minority of patients carry mutations
amenable to the strategy and that the drug is not transferable.
**The counterexample search has now been run once, and it supports the direction in a weaker word
than this record used.** The N=1 Collaborative expert-consensus guidelines put a variant of this
class out of scope by **two separate routes, only one of which is experiment-free**:
> *"Variants within 5 bp of the exon-intron/intron-exon boundary are considered 'not eligible' for
> splice correction"* — a **positional** rule, which a canonical acceptor (−2) satisfies on sequence
> alone, and the same document's figure note: *"Anything within 5 bp is considered not eligible for
> targeting with an ASO"*;
> *"if canonical splicing is destroyed … the variant is **most likely not eligible** for a splice
> correction ASO treatment. Canonical splicing is considered destroyed if no wildtype
> transcript/splicing at the canonical splice sites can be identified in the functional analysis.
> If some wildtype transcript is still produced or protein function is detected, canonical splice
> sites are considered as weakened. **Variants that fully abolish canonical splicing are not
> amenable to a splice correction ASO and are classified as "not eligible" for this approach.**"*
and the eligibility table makes both criteria hard, not hedged: *"Not eligible — Canonical splice
site and branchpoints are destroyed OR … OR **Variant within 5 bp of the canonical splice site**"*.
🟠 **Correction of this record's own first repair, 2026-10-24 (blind locator audit,
`research/page_adjudications/locator_audit_map_repairs_20261024.md`, verdict UNDERSHOOT):** the
earlier rewrite claimed the guideline's *"strongest word on the functional route is 'most likely
not eligible', not 'cannot'"*. That was produced by **stopping the quotation one sentence early**.
*"Most likely not eligible"* is the lead-in; two sentences later the same paragraph states the flat
form — *not amenable*, classified *not eligible* — and the table reproduces it as a criterion. The
guideline is therefore **as strong as this record originally was about the class**; the overstatement
was never about the guideline's force.
⚠️ **Scope, stated so this is not read as more than it is — and this is the part that does need
narrowing.** (1) The guideline is **expert consensus, not an experiment**; it says of itself that
there is *"no gold-standard evidence for many considerations"*. (2) The flat verdict applies to
variants that *"fully abolish canonical splicing"*, and **whether the reference acceptor allele is
in that class has never been measured**: *"destroyed"* is defined as a functional transcript result,
and that result does not exist for this allele. The positional 5-bp criterion, by contrast, is met
on sequence alone and needs no measurement — so the class verdict stands on position while the
functional route stays unevidenced. Across the whole
published WWOX literature exactly **three** *cis* splice-allele transcript measurements
exist, **none** of them on this allele (`PREMISE: NOBODY_LOOKED`;
[`splice_allele_rna_evidence_20260922.md`](splice_allele_rna_evidence_20260922.md), which also
records that the "+8 cryptic ⇒ frameshift" arithmetic rests on an unstated coordinate convention
whose two readings give **opposite** frame outcomes). (3) The guideline itself warns against taking
a published absence of wild-type transcript at face value: *"some manuscripts claim there is no
wildtype splicing left whereas faint wildtype bands can be identified in a gel, which might be
sufficient to consider this a suitable case."*
⇒ Status `stress-tested`, **not** `refuted`: the guideline's verdict on the class is flat, and what
is unmeasured is this allele's membership of it by the functional criterion. **Reopening, stated
exactly:** the guideline's *not eligible* column is **OR-joined** — canonical splice site destroyed, **or**
a variant within 5 bp of the canonical splice site, among others. A canonical acceptor allele is at
position −2, so it stays *not eligible* **on position alone, whatever a transcript test shows**. A
measurement on the reference acceptor allele that shows **residual wild-type splicing** would move it
from the guideline's *destroyed* to its *weakened* class on the **functional** criterion only, and so
removes one of the routes to *not eligible*, not the other; it does not by itself make an SSO a live
question. Three qualifications the guideline attaches and the earlier wording dropped: the 5-bp rule is
framed as a **proxy** (variants there "most likely" destroy canonical splicing); the authors state the
guidelines **will be adjusted** as evidence accrues; and a footnote gives **two exceptions** to the
quoted sentence. Whether this allele falls under an exception is not established here. The
transcript measurement is the experiment `TX-001` was designed around, and it remains undone.
*Corrected 2026-10-25 after a blind audit of the 2026-10-24 rewrite found the earlier "unlikely
eligible, not not eligible" reopening true of the functional criterion only.*
*Narrowed 2026-10-24 by `scientist-b`, re-derived first-hand from the consensus guidelines
(Cheerie 2025, DOI `10.1016/j.ajhg.2025.02.017`; the quoted rules are in Data S1, text layer digest
`60abe3f4f1a846e068bc6384d2b2bef8c06b5e60a714c628c9489ac410f8affd`, re-verified today), from the
milasen report (DOI `10.1056/NEJMoa1813279`) and from the ASO-amenability taxonomy (DOI
`10.1038/s41586-023-06277-0`), staged receipts `FTR-20261023-40139194-01`,
`FTR-20261023-31597037-01`, `FTR-20261023-37438524-01`; the "never measured" half re-verified in
`analysis/splice_allele_rna_evidence_20260922.md`. Sources are named by DOI and receipt id because
these readings are `partial_fulltext_read` and **staged, not yet recorded**.*

**Curated card (added 2026-10-27):** the abstention (no aberrant-to-normal transcript ratio exists) is in `research/drug_repurposing/cards/C02_splice_aso.card.json`; `repurposing_join.py` reads it for this record.

### N-11 — 4-PBA / TUDCA on the ER-chaperone rationale → **wrong compartment**
**Source ids:** DIS-004, DL-MECH-036, DL-MECH-037.
**Failure mode:** *derived from a textbook default.* "Misfolded protein → ERAD → chemical chaperone"
is true **only for ER/secretory proteins**. WWOX is cytosolic; the route is lysosomal. The rationale
is dead, **the molecule is not**: 4-PBA is also an HDAC inhibitor and could act as an HSP co-inducer —
**a different mechanism**, to be re-evaluated on that basis only if the lysosomal arm is confirmed.

**Update 2026-10-29 (IT5 P8 and P5, card A01; the headline and the withdrawn ER rationale above are NOT edited; NOT WWOX EVIDENCE).** The compartment objection is restated, not established: a soluble cytosolic protein (Munc18-1, `PAPER 431`, re-read on this question, receipt `FTR-20261028-30266908-02`, partial) was raised by the phenylbutyrate arm and by two HDAC-free osmolytes, while a class-I HDAC inhibitor did not reproduce the mutant gain; that contrast is document-dependent (butyrate is the stronger class-I inhibitor in one ChEMBL document and the weaker in another), so it is weakened, not withdrawn, and an HDAC6 contribution is open. No enzyme and no WWOX system was ever given the class. Potency: the chaperone mechanism has no numeric value in any source (qualitative "Active" records exist for phenylbutyric acid only); HDAC potency is document-dependent and sits one to three orders of magnitude below the 0.5 to 10 mM applied in the cell experiments, so an abundance gain cannot be called chaperoning without an HDAC-free comparator. Association is not modulation is not rescue: no abundance gain may be read as rescue until a wild-type function ruler exists. The Q230P fate experiment must carry three lever classes (physical chaperone and osmolyte arms, a class-I HDAC inhibitor without HDAC6 activity, a pan-HDAC or HDAC6-selective inhibitor) and transgene mRNA under treatment. The class is not promoted and not retired; card A01 stays `controversial`.

**Curated card (added 2026-10-27):** the class card is `research/drug_repurposing/cards/A01_pba_class.card.json`; it is a RECUPERO_PROFONDO class card whose assertions carry NO evidence-scope labels, and this record's verdict (wrong compartment) is not that card's route; `repurposing_join.py` reads it for this record.

### N-12 — HSP70 co-inducers (e.g. arimoclomol) for an SDR missense → **a hypothesis of harm, and it is still only a hypothesis**
**Source ids:** DL-MECH-047, CLAIM 019, D-03.
**Failure mode:** *wrong direction, hidden inside a plausible one* — **as a prediction, not as a
measurement.** "It is a chaperone, therefore it helps folding" is false **as a default**: the sign
depends on which chaperone and which route. The record used to state the consequence flatly; the
three layers behind it are of three different kinds, and separating them is the whole correction.
- **`DATO`, in a WWOX allele, in vitro.** For **WWOX-P252A** the protein is restored by lysosomal
  inhibitors (chloroquine, NH₄Cl) and **not** by MG-132, 3-MA has no effect, HSC70 co-precipitates
  **only** the mutant, and LAMP1 co-localisation is present ⇒ HSC70-associated **lysosomal**
  turnover. Limits as the source states them: overexpression in thyroid-cancer lines and HEK293T,
  not neurons and not patient cells; **CMA is not distinguished** from other HSC70/endolysosomal
  routes without LAMP2A dependence or degron epistasis; **Q230P was not tested**; and the human
  P252A/P282A homozygotes have **no neurological disease**, so the mechanism may transfer while the
  severity does not (`DL-MECH-047`).
- **`IPOTESI`, and this is the record's headline.** That **amplifying** HSP70 would therefore
  *accelerate* the degradation of a destabilized SDR missense. **No HSP70 co-inducer has ever been
  applied to any WWOX allele, in any system.** Arimoclomol appears in these records only in a
  full-text-queue entry and in `D-03`, which itself says *"could accelerate"* — a conditional that
  this record had hardened into a statement.
- **One non-WWOX comparator points the other way, and it was never in the record.** The measured
  sentence names its population and this record must not widen it: *"Arimoclomol dose-dependently
  increased the amount of GCase **in primary GD fibroblasts** across all tested genotypes, including
  neuronopathic and non-neuronopathic associated mutations"*, including the EndoH-resistant pool —
  i.e. it **raised** a misfolded lysosomal client. The neuronal system is a **separate** result in
  the same paper, and is cited as its own sentence: *"While equivalent increases where seen in the
  neuronal-like MASC cell system during shorter timelines (i.e. up to 9 days) it was not possible to
  maintain the neuronal like MASCs in their differentiated state for a longer time"* (differentiated
  skin-derived multipotent adult stem cells, n = 2–4 per cell line). 🟠 **Quotation scope repaired
  2026-10-24:** the previous wording elided exactly the words *"in primary GD fibroblasts"* and then
  widened the sentence to both populations (blind locator audit,
  `research/page_adjudications/locator_audit_map_repairs_20261024.md`, verdict OVERSHOOT by
  ellipsis). Limits: an **ER-synthesised, secretory-route**
  client, which is exactly the compartment N-11 rules out for WWOX; **this source tested only an ER-synthesised client** (for the phenylbutyrate-class lot a soluble client exists, see the N-11 update of 2026-10-29);
  the authors could not resolve which HSP70 family member acts and could not demonstrate reduced
  substrate storage; the compound belongs to the funder. **NOT WWOX EVIDENCE.**
⇒ **Proposed and withdrawn on the same day, and it stays withdrawn — on an untested direction, not
on a measured harm.** Symmetrically, nothing above licenses proposing it either: the comparator is
in the wrong compartment to carry the sign across.
**`REVIVAL_TRIGGER`:** any measurement of a destabilized WWOX SDR missense (Q230P or P252A) under
HSP70 amplification, **in either direction**; or a LAMP2A-dependence / degron-epistasis result that
establishes the route as CMA, which would make the acceleration prediction testable instead of
assumed.
*Hypothesis and finding separated 2026-10-24 by `scientist-b`: the `DATO` layer re-derived today
from `DL-MECH-047` as it now stands (including its 2026-10-03 rectification that only P252A falls
in the SDR), the comparator read first-hand (Fog 2018, DOI `10.1016/j.ebiom.2018.11.037`, staged
receipt `FTR-20261023-30497978-01`; `partial_fulltext_read`, **staged, not yet recorded**). The
earlier wording — "HSC70 does not rescue — it **delivers to the lysosome**" as a flat statement
under the headline "may accelerate the damage" — carried no tag distinguishing the P252A measurement
from the Q230P prediction (`research/module_batch_selection_scientist-b_20261023.md` §3, §4.2).*

**Curated card (added 2026-10-27):** the abstention is in `research/drug_repurposing/cards/A05_hsp70_axis.card.json`; `repurposing_join.py` reads it for this record.

### N-13 — Pro-myelinating agents (clemastine, benztropine, T3, quetiapine) → **wrong cell compartment, and a closing window**
**Source ids:** CLAIM 003, DL-MECH-031.
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

**Curated card (added 2026-10-27):** the compartment content (oligodendrocyte versus astrocyte) is in `research/drug_repurposing/cards/F02_myelination_activity_sign.card.json`; its separate activity-manipulation question is not this record's; `repurposing_join.py` reads it for this record.

### N-14 — Antioxidants (NAC, CoQ10, creatine) on the "WWOX loss → ROS" rationale → **the relationship is not monotonic**
**Source ids:** CLAIM 009, CLAIM 034, PAPER 054, PAPER 071.
**Failure mode:** *the direction of the axis is context-dependent and was assumed.* Two independent
primary systems run **counter-directionally**: in diabetic mouse photoreceptors WWOX is
**up**-regulated and its siRNA knockdown **reduces** superoxide; in the fly, Wwox loss **lowers** and
overexpression **raises** thresholded CM-H2DCFDA fluorescence, with Wwox×Idh and Wwox×Sod genetic
interactions. WWOX↔ROS is **not monotonic and its sign is context-dependent** — which is precisely
the premise the antioxidant logic assumes. The canonical claim was held at `in observation` and not
raised to `conflicting evidence`, because the systems are not comparable — but the note is mandatory
wherever the claim is cited in support of NAC/CoQ10/creatine/KD logic.

### N-15 — Counting seizure control as developmental protection → **the most consequential negative in the whole portfolio**
**Source ids:** CLAIM 031, DL-MECH-039.
**Failure mode:** *corrects a biomarker (seizures) but not the mechanism (development)*. **Quoted
with the qualifications the source attaches, both of which this record had dropped.** The authors
offer the observation as support for their own reading, not as a measured regularity: *"We believe
that, in these children, the underlying cause itself (mutations in WWOX) caused both the severe
cognitive impairment and the epileptic encephalopathy. **In support of this hypothesis** is the fact
that the cognitive and psychomotor impairment preceded the onset of epileptic encephalopathy and did
not improve with achievement of better control of epileptic activity **in some of these cases**"* —
and the outcome sentence carries its own restriction: *"The developmental outcome was unfavourable
with profound impairment despite improvement of epileptic activity **(e.g. in the first child)**"*.
In that first child vigabatrin **resolved** the spasms and at two years the child was profoundly
delayed. Converging, and it is **one patient counted once**: in another cohort the only
**non**-drug-resistant patient died at 8 years — the same single patient that `CLAIM 033` reserve (4)
reports from the same source, so the two records are not two supports.
⚠️ **What the qualifier costs, stated rather than absorbed.** *"In some of these cases"* is of
**ambiguous scope in the source and this record does not resolve it**: it may attach to the
non-improvement, or to the achievement of better seizure control (blind locator audit,
`BATCH_20261003_003`, carried in `CLAIM 031`). And the **order of onset is not shown for both
children**: in child 2 seizures began at five weeks while failure to reach milestones is recorded at
four months. So "impairment precedes the epileptic encephalopathy, in every case, and never
improves" is **not** what was observed; what was observed is that in at least one of two children
profound developmental impairment persisted through resolved spasms, with the authors reading the
sequence as support for a shared cause.
⇒ This is a **DEE, not an EE**. Seizure control remains fully indicated — quality of life, status
epilepticus (a documented cause of death), SUDEP, sleep, manageability — but **must not be scored as
disease modification**. Limits: N=2, observational, uncontrolled, and the load-bearing sentence is
**qualified in the source**, as above. 🔵 **The conclusion survives the narrowing, and the headline
is why it is worth saying so:** scoring seizure control as developmental protection would need the
*opposite* observation — a WWOX child whose developmental trajectory **improved** when seizures came
under control — and the qualifier does not supply one; it only limits how many of these two children
the non-improvement covers. **`REVIVAL_TRIGGER`:** such a case, reported with a developmental
measure before and after seizure control, in any WWOX series. Whether one already exists in the
literature was **not** measured here.
*Qualifier restored 2026-10-24 by `scientist-b`, re-derived first-hand from the source text layer
(Shaukat 2018, [[paper_registry_current#PAPER 045]]; derived text digest
`ae3103d907aceef77695534708bca43e6b476fca12b401ca0f8c0785842ade78`, re-verified today) and
reconciled with `CLAIM 031`, which has carried *"in some of these cases"*, the scope ambiguity and
the order-of-onset gap since 2026-10-03 (`CC-20261003W4-A-SHAUKAT-01`) while this record carried
none of the three; the parenthesis *"(e.g. in the first child)"* was dropped from the quotation and
is restored here. Drift measured in
`research/module_batch_selection_scientist-b_20261023.md` §3, §4.2.*
**Corollary, and it is the reason this file exists:** if the developmental outcome does not respond to
symptom control, **only causal levers can change it** — which is why R-01 and the allele-level chains
carry the weight, and why every downstream candidate in §4 is honestly labelled as symptomatic or
slowing.

### N-16 — Pannexin-1 blockade (brilliant blue FCF and congeners) on the CLAIM 021 network node → **the only WWOX measurement points the wrong way, and it was never tested**
**Failure mode:** *a negative stated as an absence of effect, when what exists is an untested point estimate in the adverse direction.* In the only WWOX system in which a selective pannexin-1 blocker has ever been applied (`Wwox` S-KO neocortical slice, P13–P17), normalized burst frequency rose to **≈ 2.55 during treatment and ≈ 2.6 at washout against a baseline of 1.0**, carrying **no significance marker and no reported test** — while the paper's Results and Discussion describe the arm as *"had minimal effect on the network excitability in the `Wwox` S-KO model"*. Panel attestation, `deepdive_manifests/PMID34634460.json` entry 3, receipt `FTR-20260810-34634460-02`.
⇒ **DEPRIORITIZE.** ⚠️ Scope, stated so the negative is not read as stronger than it is: this means *"the only WWOX measurement points the wrong way and was not tested"*, **not** *"pannexins are uninvolved in WWOX network pathology"*. Two facts from the same paper cut against over-reading it: the authors explicitly keep a pannexin-1 blocker open *"at earlier developmental stages"*, and in the same treatment arm **the range of maximal phase-amplitude coupling shifted from delta-gamma to delta-HFO in 10 of 25 bursts**, which the authors read as a subset of bursts being pannexin-influenced — so the arm is not even a clean no-effect arm in its authors' own reading (verified first-hand in the body, 2026-09-27).
**Revival:** a **powered, significance-tested** pannexin-blocker arm in a WWOX system reporting a **reduction** in burst frequency, at an **earlier** developmental stage than P13–P17.
*Recorded 2026-09-27 outside a `BATCH_COMMIT` (analysis layer, no canonical target) by `CC-20260826-PANNEXIN-N16-01`; its `CLAIM 021` limb is NOT applied and stays with the two MAJOR-classified pharmacology candidates.*

### N-17 — Tau-lowering, imported from tauopathy into CHAIN C → 🔴 **the arrow points the other way: Tau is the EFFECTOR of the benefit, not the toxin**
**Failure mode:** *importing a disease's dominant modality because the pathway diagram looks like that disease, without checking which way the arrow points.* CHAIN C reads like a tauopathy — WWOX loss → GSK3β de-repressed → pTau S396/S404 up (`CLAIM 035`, `DL-MECH-019`) — and tauopathy's dominant modality is **tau-lowering**. In the only system where the question was asked, tau-lowering **removes the benefit of both interventions this chain is built on**. Primary, PMID 22193544, verified first-hand in the body on 2026-09-27 (`files/fulltext/PMID22193544_Wang2012_PMC.xml`, sha256 `eb6f568d…`, `deepdive_manifests/PMID22193544.json` entry 6):
> *"Neither WWOX overexpression nor GSK3β knockdown promoted neurite outgrowth in the Tau knockdown condition, indicating that Tau is the effector of both WWOX and GSK3β."*
and, in the same experiment: *"the neurite outgrowth stimulated by RA was abolished when Tau was knocked down."*
⇒ **A tau-lowering agent would remove the effector both of the gene-therapy arm (R-01) and of the downstream kinase arm (R-04 / the Axin-site node).**
⚠️ **Scope, stated so this is not over-read.** This is a statement about a **direction** in *this* pathway in *this* system (SH-SY5Y, RA-differentiated, RNAi knockdown), and it names **no molecule**. It does **not** say tau-lowering is unsafe in general, it is **not** a clinical statement, and **nothing here is medical advice**. `BLOCCO 1` untouched.
🔵 **Why it is recorded at all:** the pathway was already on record; **the arrow's direction was not**, and the direction is the part an outside reader importing the obvious modality would get wrong. `D-29`: *when the pathway looks like a known disease, check which way the arrow points before importing that disease's modality.*
**Revival / reopening:** a WWOX-deficient neuronal system in which reducing total Tau **improves** a developmental readout — which would mean the effector relation measured here does not hold in that system.
*Recorded 2026-09-27 outside a `BATCH_COMMIT` (analysis layer, no canonical target) by `CC-20260922-TAU-DIRECTION-01` §1. It is a **directional constraint**, not a scored candidate, and it is deliberately **not** added to the §6 prioritization table: no intervention class enters or leaves a class on it.*

---

## 6. Prioritization

**Deliberately very small.** A long shortlist would contradict the evidence.

| Class | Entries |
|---|---|
| **READY_FOR_WWOX_PRECLINICAL_CONSIDERATION** | **R-01** AAV9-hSynI-WWOX |
| **PROMISING_BUT_MECHANISTIC_GAP** | **R-02** memantine/NMDAR · **R-05** ketogenic diet · **R-09** proteostasis programme (SDR missense class) |
| **TRANSFER_HYPOTHESIS** | **R-03** Wnt/tankyrase · **R-06** anti-neuroinflammatory (class) · **R-08** base/prime editing |
| **DEPRIORITIZE** | **R-04** lithium · N-01 mTOR inhibitors · N-03 Na-blockers · N-07 digoxin · N-08 DCA · N-09 pTyr33 peptide · N-10 splice-switching ASO · N-11 4-PBA/TUDCA (ER rationale) · N-12 HSP70 co-inducers · N-13 pro-myelinating agents · N-14 antioxidants on the ROS rationale · **N-16 pannexin-1 blockade** |
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
2. **NMDAR dependence of the bursting phenotype (M2).** The only downstream node whose
   dependence on NMDAR **activity** was shown **inside** a WWOX model (d-APV; a raised NMDAR function is not shown; the gap-junction half was withdrawn on 2026-09-27).
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
2. **mTOR inhibition has never been measured at the protein level in any WWOX system** (N-01) — demoted from this list by `BATCH_20260927_001` (`CC-20260826-MTOR-DIRECTION-01`), no direction asserted. The class stays out at every tier and stays in `DEPRIORITIZE`; what changes is the reason.
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
| **GABA / E-I balance** | The **functional** inhibitory deficit is real and independently measured (reduced spontaneous inhibition, L2/3, neuron-specific loss). The **directional paradox** is unresolved — GABAergic markers ↑ in organoids, ↓ in the mouse. `E_GABA`, chloride, NKCC1/KCC2 and the GABA response are **unmeasured in every WWOX system** | **T6.** Bumetanide unrankable; broad GABAergic push carries a documented MRI-abnormality liability (two case-selected WWOX reports, no denominator) and a falsified clinical prediction |
| **mTOR** | 🔴 **Does not qualify for admission.** The only WWOX-specific datum shows mTOR/EIF4EBP1 **down** and autophagy **down** | **Deprioritized on direction**, with the weakness of the single dataset stated |
| **Circuit-targeted** | ✅ **This is where the programme is real** — but the node is **NMDAR activity** (required for the bursting, not shown raised; the gap-junction half withdrawn), not GABA. It is the one downstream dependence on a receptor activity shown inside a WWOX model | `PROMISING_BUT_MECHANISTIC_GAP` (R-02) |

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
| **E-3** | **Seahorse OCR/ECAR** on donor-derived cells (and on the existing WWOX-KO organoids) | The cheapest general screen for R-05, not PDH-specific and not the only falsifier (see R-05); narrows, does not close, the transcriptome→flux gap that weakens all of M6 | low |
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
| **Seahorse OCR/ECAR** | the transcriptome→flux gap across all of M6 | a general screen for R-05, not the single falsifier (PDH-specific readouts are listed in R-05) |
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
