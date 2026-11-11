# SCI45 S0/S1 — pH, K2P conductances and the instruments that separate the explanations, written before any search (2026-11-11)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; nothing promoted. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI / ESPANSIONE. Task record `ledger/tasks/orchestrator/ORCH-SCI45-20261111.json`. A later change to this file is a dated addendum, not an edit.

## S0 — what is already held, what is not, and the perimeter

**State found (2026-11-11).** `main` = 3f8f17fb (SCI44 landed: A d088b964, B+C+coda 34f93af0). IT44 (task/it44, session legend-development-4e) has applied SCI44 package A by folder (8edf3852) and awaits B and C; its S11 result (K+ opener relation for KH1) is read in `generation_it44_20261110/relation_s11_result_it44.md` of that branch (read-only). No IT45 branch or task record existed at the start; HE45 has a worktree. No overlap: IT44 touches no pH, TASK-1/3 or pH-led reading.

**Held, and not reread here (cited by pointer):**

| Held | Where | Used as |
|---|---|---|
| Wwox Table 1 and the 2.7 nS / 28 percent scale; degeneracy with size plus shunt | SCI43 `README.md`, `output/decisive.tsv` | the effect size a pH mechanism would have to carry |
| Wwox Methods: internal 135 K-gluconate, 1 MgCl2, 10 NaCl, 2 Na2ATP, 0.3 NaGTP, **10 mM NaHEPES pH 7.2-7.3**, 0.5 EGTA; ACSF given = incubation ACSF (**25 mM NaHCO3**, 10 glucose, 3.5 KCl, 1.3 MgSO4, 1.5 CaCl2), 35 C; no separate recording ACSF; **bath pH value not stated** | `membrane_hypotheses_20261108/verify/audit.md` A1.15 | conditions of the preparation (not unknown) |
| K+ shares by channel family from other preparations; Kv7 not at rest; K2P blockers raise dendritic Rm in adult L2/3 (40595546, pooled) | SCI43 / SCI44-C | prior shares, none in a Wwox cell |
| Juvenile neocortex KATP: share 11-17 percent, ATP-free upper bound; lactate closes KATP; 2 mM pipette ATP weakens PH4 for the published values | SCI44-C, A (PH4) | the metabolic-to-K link already open; not repeated |
| RNA by cell class (mouse P7, human): Kcnk9 (TASK-3) neuron-specific (17 FPKM), Kcnk2 (TREK-1) neuronal and glial, Kcnk1 neuron > astrocyte; **Kcnk3 (TASK-1) was not in the 15 predictions** | `kchan_expression_sci44_20261111/` | cell attribution of the channels (RNA, not current) |
| K2P tool searches in juvenile layer 2/3 (A1899, spadin, ML365, PK-THPP, ML133, fluoxetine): no somatic recording found at title/abstract level, 18 strings | `potassium_shares_sci44_20261110/output/decisive.tsv` C08 | these strings are **not** repeated; new strings are pH-led and TASK-led |
| IT44 S11: K2P openers in the catalogue act on the Ba2+-weak subfamily (TREK-1/2, TRAAK); Ba2+ concentration response for TASK-1, TASK-3 and THIK-1 not reached | IT44 `relation_s11_result_it44.md` | reason to read TASK Ba2+/pH response |
| NP10679 pH profile only as an abstract-level figure (21 nM at pH 6.9, 130 nM at 7.6); the tissue pH measurement proposed in SCI42 M01/A4 | `glun2b_comparators_sci42_20261110/S3_design.md` | the shared condition record |

**Missing (the reading targets):** (i) primary pH sensitivity of TASK-1, TASK-3, TREK-1 with conditions (nothing sourced is held; the coda's chain was background knowledge); (ii) native juvenile cortical pH evidence; (iii) tool identity and measured selectivity for the few tools that could separate the channels; (iv) what sources state about pH in bicarbonate-buffered slices and about lactate and pH in tissue.

**Perimeter, narrowed from the brief (decision in the record):** the three channels are kept (TASK-1 added to the coda's TASK-3/TREK-1 because TASK-1/3 heteromers and the TASK-1 pK are the usual source of mis-transfer); a general K2P review is not opened; THIK/TWIK/TRESK appear only as selectivity counter-targets of a tool. The "lactate up -> pH down" step is read as its own question (R4), not inherited. Sent to IT44/IT45 with this file.

## S1 — the DREAM chain, stepped, with the state of each step

Proposal under test (coda, IPOTESI): raised lactate -> lower tissue pH -> closure of pH-sensitive two-pore-domain channels -> higher Rin, depolarised rest with an E_K reversal -> network gain -> a pharmacological response that depends on the state.

| # | Step | Where it stands | Label | Specific caution |
|---|---|---|---|---|
| 1 | Metabolic state of the affected cell | Glycolytic signature in non-neural WWOX systems and an organoid; no PDH, lactate or pyruvate measure in a neural WWOX preparation (SCI44, INV-07) | observed elsewhere / not in the preparation | the organoid is age-confounded; no cell class resolved |
| 2 | Lactate and pyruvate in the slice | not measured in the Wwox slice; lactate up in a fibroblast pool and in a fly model under Abeta42 | not observed in the preparation; documented in other systems | extracellular lactate in a perfused slice is set mostly by bath glucose and diffusion, not by the genotype alone |
| 3 | pHo and pHi | not measured; **"lactate up -> pH down" is not inherited**: lactate is exported with H+ by MCTs, but a 25 mM HCO3-/5% CO2 bath, tissue buffering and a 400 um slice's diffusion limit decide whether a change of interstitial pH follows; the sign inside the cell can differ; activity itself moves pH (alkaline then acid transients) | hypothesised; to be read (R4) | pHo and pHi are two variables acting on different channels |
| 4 | Slice and recording conditions | known in part: 25 mM HCO3-, 35 C, 10 mM glucose, 3.5 K+, whole-cell with **10 mM HEPES (pHi clamped near 7.2-7.3 by dialysis)**, 2 Na2ATP, 0.5 EGTA; bath pH value, O2/CO2 fractions and slice depth not stated | partly documented in the Methods | whole-cell dialysis fixes pHi for channels that sense pHi but leaves pHo free; perforated patch leaves both |
| 5 | Channel activity | background knowledge only: TASK-1 and TASK-3 are inhibited by extracellular acidification, with different pK; TREK-1 behaves differently and is regulated from the inside; native versus recombinant, homomer versus TASK-1/3 heteromer unknown here | inferred / hypothesised until read | the intracellular and extracellular directions can have opposite signs on the K2P ensemble |
| 6 | Resistance, potential, network | the Wwox pair (Rin +39 percent, rest +5.6 mV) is observed; whether any of it comes from a pH-sensitive conductance is open; K2P blockers raise Rm in adult L2/3 dendrites (pooled) | observed (pair) / inferred (route) | the 28 percent loss may exceed the whole Ba2+-sensitive share measured in a wild-type adult cortex (23 percent): a size check is part of the answer |
| 7 | Effect of a compound | no tool tested in the Wwox preparation; for K2P, only adult pooled and recombinant data | not observed | a tool that moves a conductance shows that it contributes, not that it is altered |

## Competing explanations, written before any name

For each, a result that would strengthen it and one that would weaken it. (E1 is the proposal; the rest are what it must beat.)

| Id | Explanation | Strengthened by | Weakened by |
|---|---|---|---|
| E1 | **Modulation of a conductance by pH**: a pH-sensitive K2P conductance is partly closed in the knockout slice because interstitial or cellular pH differs | a measured pHo (or pHi) difference between genotypes in the recording condition; a channel whose pK and Hill lie inside the pH range the slice can reach; a Rin/rest difference that shrinks when pH is set equal in both genotypes; a K2P-sensitive difference current per pF that differs by genotype | genotype-equal pH where recorded; channel pK far outside the reachable range; difference current per pF equal across genotypes; native evidence that the juvenile somatic resting current is not K2P |
| E2 | **Consequence of network activity**: bursting slices or cells (4/23 vs 36/42) acidify and alkalinise their own interstitium or raise [K+]o, and the Rin/rest pair follows | pH or [K+]o transients that track bursts; the pair changes under synaptic blockade (the same cell, before and after) | the pair unchanged by blockade; non-bursting cells already differ |
| E3 | **Metabolic change without relevant acidification**: lactate/pyruvate change acts through KATP, MCT-coupled conductances, redox or ATP, or not at all, while pH stays at the bath value | no pH difference with a measured lactate difference; effect of KATP tools in ATP-undisturbed cells (SCI44-PH4) | pH moves with lactate across a range that closes K2P; a TASK-selective tool reproduces the pair |
| E4 | **Differences of maturation or compartment**: the genotype shifts the developmental trajectory (the K2P fall P7-P28) or the compartment (soma vs dendrite) | the difference is absent at matched capacitance/age markers; channel RNA and current time courses diverge by genotype | the difference persists at matched capacitance and age; somatic difference current present |
| E5 | **Conditions of the preparation**: slice depth, perfusion, O2/CO2 mix, bath pH, temperature, K+ differ by genotype/day | a bath pH or flow difference documented per day; the difference follows the day, not the genotype | the same difference with measured identical conditions |
| E6 | **Drug actions on other targets**: a "TASK tool" or "TREK tool" acts on Kv, Na+, Kir, HCN, NMDAR or via pH itself (acid also opens KATP, inhibits NMDAR, acts on ASIC), so a response is not proof of the K2P target | the tool's effect persists in a knockout or in the presence of the channel's other blockers; the effect has the same size on a matched non-K2P suppression | the effect is lost where the channel is absent/inactivated; two scaffolds with different off-target profiles agree |

## What a reading could change, fixed before searching

| Result of the reading | Moves |
|---|---|
| TASK-1 and TASK-3 pK/Hill place a measurable fraction of current inside pH 6.9-7.4 and a native cortical neuron shows the same | E1 up; the tissue pH measurement of M01 becomes the premise of the K2P arm (not only of the GluN2B tool); a K2P-selective tool earns a probe role |
| The channels' response lies outside the range a bicarbonate-buffered slice can reach, or the native evidence is not neocortical | E1 down; conditional transfer kept, named as such; the pH measurement stays a GluN2B/M01 question |
| TREK-1 responds to pHi (activation by acid) and to pHo with another sign | the sign of an acidification on the K2P ensemble is not single-valued; whole-cell (pHi clamped) vs perforated patch becomes a design variable |
| Sources show that interstitial pH in perfused slices hardly follows lactate | "lactate up -> pH down" is demoted for this preparation; E3 rises |
| The commonly used tools have measured selectivity too small to separate TASK-1 from TASK-3 or TREK-1 | the tools stay probes of a family; a genetic or expression-led arm is the discriminator |

## Predictions fixed before searching (priors; recorded so they can fail)

From background knowledge, unverified; to be scored after the reading.
* **P1.** Recombinant TASK-1 has the higher pK (about 7.2-7.4) and TASK-3 the lower (about 6.5-6.8): the two differ by more than 0.4 pH unit.
* **P2.** TASK-1/3 are sensitive to pHo; the cited pH sensors are extracellular histidines; the pHi sensitivity is smaller.
* **P3.** TREK-1 is activated by intracellular acidification and is not simply closed by extracellular acid; the extracellular response is weaker or of another direction.
* **P4.** No source reports a somatic pH response of TASK or TREK current in juvenile (P10-P25) neocortical layer II/III pyramidal neurons; native evidence comes from other regions (cerebellar granule, hypothalamic, brainstem, hippocampal) or from ages other than juvenile.
* **P5.** No tool among ML365, A1899, PK-THPP, spadin, fluoxetine separates TASK-1 from TASK-3 and TREK-1 with a measured fold of 100 or more in the same assay; the more selective ones separate TASK-1 from TASK-3 by a smaller fold.
* **P6.** In bicarbonate-buffered slices the pHo changes reported with activity or lactate are of the order of 0.1 pH unit or less, not 0.3-0.5.
* **P7.** A source that states a lactate-to-pH relation does so for in vivo or ischaemia/high-load conditions, not for a perfused juvenile cortical slice at physiological glucose.

## The size check, an analysis for after the reading

The Wwox pair needs a net loss of about 28 percent of the resting conductance. If a pH-sensitive K2P population carries a share s of the wild-type resting conductance and the pH change closes a fraction f of it, then the loss is s*f; f needed = 0.28/s. With s <= 0.23 (the Ba2+-sensitive share measured elsewhere), f would exceed 1 for the whole share; juvenile neurons may carry more. The reading supplies pK and Hill, so the required delta-pH at each s becomes a table (software, no new source). Fixed now: this is a **constraint** (what must be true), not an estimate of what is true.

## What no further literature search can resolve (stated now)

Whether interstitial or intracellular pH differs between genotypes in the recorded slice; whether lactate is raised in the Wwox slice; the K2P share of the somatic resting conductance of a layer II/III P13-P17 neuron in this preparation; whether the Rin/rest difference is carried by a K2P channel at all. These need the measurement set of S4 (pH electrode or ratiometric dye in the recording condition, difference currents per pF, perforated patch).

## Plan

One central package (K2P x pH, R1-R4 and tool identity), one producer (sonnet/medium) then one blind verifier (sonnet/high), sequential. Delivery to IT45 before the queue. Queue by S8 order, one item at a time.
