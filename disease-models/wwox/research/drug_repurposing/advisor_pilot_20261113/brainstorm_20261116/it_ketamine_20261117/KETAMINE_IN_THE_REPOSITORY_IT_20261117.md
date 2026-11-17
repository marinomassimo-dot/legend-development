# Ketamine in the repository (IT, 2026-11-17; held files only; non-canonical; mechanism level; reference genotype class only; no dose, no recommendation; nothing here is medical advice)

Written for: the 13:46Z meeting (ADV, SCI, HE, operator's reading). Prompt for hypotheses, not evidence. No testimony and no identifier of any person appear in this file. Papers are named by author and year; locators are repository paths. Tier and origin follow the arm table v8 (`ideas_arm_table_v8_20261117.tsv`), the row-level tier table and the tier-3 annex in this folder's parent.

**Answer first.** (Tier note: of the eight pore-blocker cells only C007, C010, C011 and C054 have a naming row in the tier table, and only C010 reaches tier 2, through RNA expression readings, not a drug effect; the other three are simulation, tier 3, parked.) Ketamine was never applied in any WWOX system and no held file reports a ketamine effect in a WWOX model or person. Every held claim about it is a class claim (NMDAR pore blockers) carried from simulation, a competitive antagonist (d-APV) or other diseases. The one WWOX fact that touches ketamine is the reverse direction: the in vivo hyperexcitability recordings in the null mouse were made under ketamine/medetomidine anaesthesia, and the genotype contrast was still present.

## 1. What is held
| Item | Where | What it says about ketamine |
|---|---|---|
| F04 NMDAR intervention class card | `drug_repurposing/cards/F04_nmdar_intervention_class.card.json` | assessment REQUIRES_QUALIFICATION, direction UNRESOLVED; ketamine sits in class B (use-dependent pore blockers, with memantine); the only NMDAR agent applied in a WWOX system is the competitive antagonist d-APV (neuron-specific knockout slice); paediatric suitability, CNS exposure, interactions, time to benefit: UNKNOWN |
| CC-20260826-NMDAR-CONJUNCTION-01 | `research/commit_candidates/` | four recorded risks: P13-P17 slice stage; acute slice is not chronic in vivo; chronic block in a developing brain removes a signal needed for activity-dependent maturation; the in vivo recordings were made under ketamine |
| BLOCK-1 and catalogue | `brainstorm_20261116/it_block1_triage_20261116/README.md`; `generation_it46_20261111/ladder_it46.tsv` | ketamine (approved_any_source, prescription), esketamine; computational triage **not run** (ADMET-AI and medchem absent); the engine ladder lists both as EXCLUDED, "opposite or unsupported action; kept" |
| Comparator rows | `comparators_it39_20261109/output/comparators.tsv` | ketamine and memantine indistinguishable on steady-state current, EPSC decay and extrasynaptic inhibition at equimolar concentration in culture (abstract level); more neuroprotective under oxygen-glucose deprivation (abstract) |
| Dossiers | I1, I3 (SCI), I7 (IT), I9 (ADV), I20 (SCI) | I1 and I3 list pore blockers as the "sustainer" lever (readiness: ketamine yellow, esketamine red); I7 carries the narrow-margin titration; I9 names the BDNF-TrkB label only; I20: not testable in slices as designed |
| Arm table row "NMDAR pore blocker" | v8 | C007 (I1, duration -), C008 (I5), C009 (I9), C010 (I3), C011 (I4), C012 (I10), C044 (I7, abolition at titration), C054 (I1, duration - and interval +) |

## 2. BLOCK-1 status and every held safety signal (harms beside any benefit)
| Signal | Origin and level |
|---|---|
| BLOCK-1 computational triage not run for any NMDAR pore blocker | IT block-1 README; flags from general knowledge are unconfirmed |
| Dissociative effects and abuse potential: labelled concerns, "flagged for the design, never recommended" | IT block-1 README (label level) |
| Readiness sheets: ketamine yellow, memantine yellow, esketamine **red** (red = boxed warning or fatal-or-serious wording; "none is never safe") | SCI dossiers I1, I3 |
| Chronic NMDAR block in the maturation window is the aggravation counterpart of any pore-blocker idea | I9 D6 and CC-NMDAR-CONJUNCTION risk 3 (INFERRED, no WWOX datum) |
| Adults, ketamine with an AMPAR antagonist for postanoxic super-refractory status: reversible cholestatic liver injury 77 against 27 percent | F04 packet DR-P9-013 (abstract; not WWOX; adult) |
| A GluN2B negative modulator in adult depression: dizziness, transient amnesia, somnolence, mild dissociative events (ketamine as reference arm only at some sites) | `glun2b_comparators_sci42_20261110/output/decisive.tsv` D05 (class-adjacent, not ketamine's own table) |
| One published single-case report in a different gene (GRIN1 gain of function): the mechanism-matched pore blocker memantine was stopped because seizures rose; ketamine was followed by a seizure-free interval, baseline not established | `deepdive_manifests/` Lewis 2023 entries (not WWOX; one case) |
| Paediatric label for ketamine: not searched; memantine's paediatric use not established on its label | F04 translation block ("label unknown is not NO_MATCH_FOUND") |

## 3. Held claims, direct and indirect, with tier and origin
| Claim | Direct / indirect | Origin | Tier and status |
|---|---|---|---|
| Competitive NMDAR block (d-APV) abolishes burst activity in the neuron-specific knockout slice; wild type does not burst, so no genotype-by-drug contrast | direct (class A, not a pore blocker) | WWOX observation (F04) | transfer within the NMDAR class to a pore blocker; no arm-table cell carries this as a pore-blocker datum (C010's tier-2 rows are bulk and single-nucleus RNA tables, not a drug effect) |
| Burst duration falls before incidence when the NMDAR weight falls by a fifth (duration 0.76 to 0.30 s, bursts -46 percent, incidence still 0.99) | direct (duration) | simulation (I1, R17c: NMDAR-active agent, duration -54 percent and interval +55 percent; PILOT_ARM_EXPECTATIONS) | tier 3; C007, C011, C054 PARKED: needs the paired slice drug test |
| Abolition at a titration beyond the critical fraction; pore blockers act on the current directly with a narrow margin; fractional block in culture: memantine at 1 micromolar 27.1 percent synaptic, 50.4 percent extrasynaptic; MK-801 about 94 and 96 percent | direct (threshold) | IT dossier I7 (model) plus rat culture pharmacology (transfer) | C044 has no naming row in the tier table: assumption-level; tool pharmacology tier 1-2 |
| Block depends on extracellular Mg2+ (about twenty-fold weaker at GluN2A and GluN2B, about three-fold at GluN2C and GluN2D) and on intracellular Ca2+ for memantine, not ketamine; the slice held 1.3 mM Mg2+ | direct (receptor state) | external pharmacology, abstract and partial full text (F04) | NOT WWOX evidence; qualifies any slice result |
| Genotype contrast of in vivo hyperexcitability stands under ketamine/medetomidine; absolute rates are not those of an awake brain | background, not a drug test | WWOX observation (Repudi 2021, manifest entry 13) | no ketamine-free arm: says nothing on ketamine's effect |
| Neuroprotection under oxygen-glucose deprivation | indirect | culture, abstract level | transfer, other disease |
| BDNF-TrkB and activity-dependent maturation routes "attributed to NMDAR-pore agents such as ketamine" | indirect (plasticity) | I9 D6, label only | assumption; no WWOX datum; sign unknown (the same window carries the aggravation counterpart) |
| Seizure-free interval after ketamine in a GRIN1 gain-of-function single case; partial response in a single ATP1A2-related infant case, with the timing relative to memantine not separable | indirect (clinical analogue) | other-disease case reports (manifest; baseline arm table L03) | tier none for WWOX; one case each |

## 4. What is NOT held
* Any ketamine administration, acute or chronic, in a WWOX model, tissue or person; any ketamine datum for the allele classes; the reference-genotype response is entirely unmeasured.
* Any held statement about a transient benefit lasting weeks after one exposure, or about ketamine metabolites, anti-inflammatory action, sleep or immune effects, or the effect of other sedatives, antibiotics, rest or resolution of an intercurrent illness (no file addresses these; none is assessed here).
* A ketamine-free versus ketamine arm in the in vivo recordings; per-cell data from the slice papers.
* BLOCK-1 computation, CNS exposure, interactions, dose-exposure, paediatric label.

## 5. What the meeting can do with it (IPOTESI, none is a held claim)
Three readings the held files let one state and separate, each with a measurement: (a) acute pore block of the burst-sustaining NMDAR current (test: the paired slice drug test that parks C007, C011, C054; outcome favours it if duration falls before incidence); (b) a plasticity-mediated effect that outlasts exposure (test: none held; the maturation-window readout of I9, sign unknown; it is also where harm is predicted); (c) non-drug factors (no held file; the meeting should say so, not infer). Each stays IPOTESI; none changes a card, rank or cell.

Limits: held files only, one bounded pass (about 60 minutes); abstract-level sources are marked; the readiness colours are SCI's and from labels; I did not re-open the case-report full texts.
