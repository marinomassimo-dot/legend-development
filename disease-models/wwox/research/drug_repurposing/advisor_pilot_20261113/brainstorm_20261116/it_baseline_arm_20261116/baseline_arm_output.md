# Baseline arm output (memory-free), 2026-11-16

Worked only from the bundle folder (TASK.md, RULE_v1.md, 15 thread files). Mechanism matching only; no dose, no recommendation to use any agent. Reference genotype class only.

Reading choices that the rule left open (stated so that they can be re-scored):
- R1. Score counts only lines with sign = match (sum over distinct (axis, origin) of tier x directness). A "literal" score that also counts sign = unknown lines (their tier x directness) is shown beside it, because the rule text does not say whether an unknown line enters the sum. The two readings change the top class at seizure / P13-P15 (section B).
- R2. Tier is the thread's evidence tier; directness is the class-to-thread link. Where the agent measured is not in the class (d-APV is neither a pore blocker nor a GluN2B NAM), the class link is carried by directness, not by lowering tier.
- R3. The one WWOX burst dataset spans P13-P17; it is placed in P13-P15 (nearest defined window), not duplicated into "later".
- R4. Unit set has no "slice": slice-level counts are written as `cells` with a note.
- R5. Endpoint `seizure` here means the burst proxy in slices, or an animal seizure/PTZ readout where the line says so. Endpoint `development`: the bundle holds no measurement for any class (all unknown).
- R6. Sign `unknown` carries tier = the thread's evidence and directness = the link actually stated in the bundle (0 when the bundle says nothing about the class).

## A. Matrix (TSV)

```tsv
line	class	endpoint	age_window	thread	sign	tier	directness	axis	origin	has_genotype_contrast	has_drug_by_genotype	unit	locator	note
L01	NMDAR pore blockers	seizure	P13-P15	T1	match	2	3	AX-NMDAR	O-WWOXSLICE-dAPV	phenotype yes (bursts 36/42 KO vs 0/11 WT); drug arm KO only	no	cells (slice counts)	T1_nmda_inv05.md ## Answer item 1; T2_chloride_gradient.md ## Counter-evidence and limits bullet 2	d-APV removed bursts at P13-P17 in neuron-KO slices (prior complete read, not reopened). d-APV is a competitive antagonist, not a pore blocker; fixes NMDAR-activity dependence only, not the subunit. If the phenotype contrast is allowed to qualify, tier would be 3 (score 9).
L02	NMDAR pore blockers	seizure	later/unspecified	T1	match	1	3	AX-NMDAR	O-EMNETT-20720132	no	no	cells	T1_nmda_inv05.md ## Answer item 5	Rat autaptic hippocampal neurons DIV13, room temp: memantine blocked 27.1% of synaptic NMDAR EPSC (concentration omitted here). Non-WWOX tool pharmacology.
L03	NMDAR pore blockers	seizure	later/unspecified	T1	unknown	1	1	AX-NMDAR-clinical	O-39970743-case	no	no	children	T1_nmda_inv05.md ## Answer item 4	One infant, ATP1A2-related DEE, ketamine then memantine; concomitant ketamine and timing cannot be separated. Not WWOX.
L04	GluN2B NAMs	seizure	P13-P15	T1	match	2	2	AX-NMDAR	O-WWOXSLICE-dAPV	as L01	no	cells (slice counts)	T1_nmda_inv05.md ## Answer item 1, ## Corrections (probe classes)	Same origin as L01, different class. d-APV gives no subunit; directness 2 (same pathway), not 3.
L05	GluN2B NAMs	seizure	P6-P8	T11	match	1	3	AX-GluN2Bshare	O-MIERAU2004	no (wild type only)	no	cells	T11_wo11.md ## Answer first	Ifenprodil-sensitive share of L4-evoked NMDA EPSC 53% (43-61), controls n 9, treated n 5; wild-type mouse barrel cortex L2/3, room temp, 2 mM Mg. Target-level only: no WWOX recording or burst exists at P6-P8.
L06	GluN2B NAMs	seizure	P13-P15	T11	unknown	1	3	AX-GluN2Bshare	O-MIERAU2004	no	no	cells	T11_wo11.md ## Answer first; T11_wo11_second_reader.md ## Answer first	Same share 14% (interval 0-34), n 15 vs 10: interval includes zero, so no match is claimed. Evoked synaptic current, wild type, between-cell design, not the isolated current in burst slices (WO-10 open). Second-reader file is the same origin (counted once).
L07	GluN2B NAMs	seizure	later/unspecified	T1	match	1	2	AX-NMDAR	O-38529699-radiprodil	no	no	animals	T1_nmda_inv05.md ## Answer item 3	Radiprodil reduced audiogenic seizure onset and severity in mice with a GluN2A gain-of-function change; abstract only; acute dosing, reflex seizures; other genotype. Shows circuit lever, not that GluN2B carries the WWOX lesion.
L08	AMPA antagonists	seizure	P13-P15	T1	unknown	0	1	AX-AMPA	none	no	no	cells	T1_nmda_inv05.md ## Conditional hypothesis, ## First discriminating experiment; T1_T11_target_first_nmdar.md section 6	No AMPA-antagonist measurement in any WWOX system; AMPA-evoked responses appear only as a spared control; AMPAR agents declared outside that package's question.
L09	GABA-A PAM (excl. benzodiazepines)	seizure	P13-P15	T2	match	3	2	AX-GABA	O-WWOXSLICE-sIPSC	yes (controls 14 cells/7 animals vs KO 9 cells/5 animals)	no	cells	T2_chloride_gradient.md ## Decision this changes bullets 1-3 and ## Counter-evidence and limits	Reduced sIPSC in KO at P13-P17. Datum recorded with 140 mM KCl pipette, no glutamate-receptor block named, 4xSD threshold: cannot test the chloride gradient; amplitude loss itself "not yet beyond the recording conditions". File states a burst reduction by a GABA-A positive modulator is compatible with every explanation and discriminates none. Match = same axis only.
L10	Benzodiazepines	seizure	P13-P15	T2	unknown	3	1	AX-GABA	O-WWOXSLICE-sIPSC	as L09	no	cells	T2_chloride_gradient.md as L09	Bundle never names benzodiazepines; membership in GABA-A modulators rests only on the wording of the rule's column header. No aggravation statement either.
L11	GABA-AT/GAT	seizure	P13-P15	T2	unknown	3	1	AX-GABA	O-WWOXSLICE-sIPSC	as L09	no	cells	T2_chloride_gradient.md as L09	Bundle holds no statement on GABA-AT or GAT; link is by the word GABA only. T6 (GABA-AT clinical series) is not in the bundle: unknown.
L12	Kv7 openers	seizure	P13-P15	T7	unknown	3	1	AX-Kcond	O-WWOXSLICE-Table1	yes (Rin 102.9 vs 143.0 MOhm; rest depolarised 5.6 mV)	no	cells	T7_potassium.md ## Direct answer bullet 1; ## Counter-evidence and limits	Resting phenotype is a K+-conductance question; Kv7 is expected small at that rest, the published F-I slope does not support a Kv7 deficit (weakly), no K+ current measured in any WWOX neuron. Retigabine named only as conditional mechanism comparator (KH2). Not a match, not neutral.
L13	Kv7 openers	seizure	later/unspecified	T7	aggravation	1	0	AX-Kv7-HCN1	O-IT35-abstract	no	no	animals	T7_potassium.md ## Counter-evidence and limits last bullet	Retigabine increased ECoG spiking in an HCN1 gain-of-function mouse (abstract level). Other genotype, directness 0: reported in the aggravation column as off-genotype, not as a WWOX finding.
L14	T-type calcium	seizure	later/unspecified	T5	unknown	1	3	AX-Cav3	7 origins: Santi2002, PerezReyes2008, Furukawa2009, Tanaka2010, Hara2020, Masumiya2001, Shin2008	no	no	cells (heterologous or native non-WWOX)	T5_cav3_pair.md ## Answer first, ## Limits; T5_cav3_gaps.md ## Answer first	Cav3 pharmacology of efonidipine and flunarizine, different assays/species, never matched; no WWOX phenotype is linked to Cav3 anywhere in the bundle, so no match is claimed. Verdict in both files: qualified proposal, not matched, not demoted.
L15	(unassigned; see note)	seizure	later/unspecified	T3	unknown	0	0	AX-PTZ	O-32000863-fig7b	PTZ stage nulls 1.87 vs wild type 0.25 (genotype of "nulls" not named in the file)	not established (the open question)	animals	T3_nx1_ptz_sizing.md ## Answer first (table), item 4	Ethosuximide arm in a PTZ model: PTZ-generic, tier 0 by the rule. The bundle does not state which class ethosuximide belongs to, so no class column receives this line; if it were put in T-type it adds 0 either way.
L16	ALL classes	seizure	all	T4	unknown	0	0	AX-lithium	-	-	-	-	T4_T8_gsk3_inv09.md ## Answer first, ## Delta	Directness 0 for every class by rule; no class column for GSK3 tools. Lithium row non-attributable to GSK3.
L17	sodium-channel; SV2A; valproate-type; steroid/ACTH; cannabidiol/fenfluramine-type	seizure and development	all	none	unknown	0	0	-	-	-	-	-	no thread	No thread, measurement or statement in the bundle. Sodium: only a mention of a sodium-channel-blocking class as a mechanism-different comparator in a design step (T7_potassium.md ## Roles of the interventions); no measurement.
L18	sodium-channel (T12 aggravation)	seizure	all	T12	unknown	0	0	-	-	-	-	-	no statement	No statement on aggravation by sodium-channel agents in the bundle: unknown, not "none".
L19	ketogenic diet	seizure and development	all	T10	unknown	0	0	AX-metab	-	-	-	-	T10_metabolic_inv07.md ## Answer, ## Conditional hypothesis	T10 says PDK, LDH and substrate-bypass levers stay open and that no WWOX neural system has a PDH, lactate/pyruvate or flux measurement. The bundle never connects a diet to substrate bypass.
L20	carbonic-anhydrase/multi-target	seizure and development	all	T7 (pH)	unknown	0	0	AX-pH	-	-	-	-	T7_ph_k2p.md ## Answer first item 4	pH difference between genotypes is unmeasured; the bundle names no agent that sets pH.
L21	ALL classes	development	P6-P8, P13-P15, later/unspecified	T1/T2/T11	unknown	0	0	-	-	-	-	-	T1_nmda_inv05.md ## Priority open question ("Viability and maturation require separate, longer exposures; no window is deduced")	No development or maturation endpoint is measured for any class in a WWOX system.
L22	threads with no class column	-	-	T8, T9, T4	-	-	-	-	-	-	-	-	T8_eif2b_result.md; T9_ctgf.md; T4_T8_gsk3_inv09.md	ISR/eIF2B (probe and GSK3 tools, no catalogued eIF2B target), myelin/OPC (CTGF verdict: inconsistent or composition-explained) and lithium/GSK3 map to no class column. No cell.
L23	ALL classes	-	-	T6	unknown	-	-	-	-	-	-	-	not in bundle	GABA-AT clinical series: unknown.
```

Aggravation count (column kept apart, never netted): sodium-channel unknown; benzodiazepines unknown; Kv7 openers 1 off-genotype (HCN1 gain-of-function mouse, abstract level, L13), 0 in a WWOX system; every other class unknown.

## B. Class ranking per endpoint and age window

Score_match = sum over distinct (axis, origin) of tier x directness, match lines only (R1). Score_literal = same, but also counting the unknown-sign lines that carry a tier and directness. Aggravation shown apart.

Endpoint seizure (burst proxy)

| Window | Rank by score_match | score_match | score_literal | Aggravation |
|---|---|---|---|---|
| P6-P8 | 1. GluN2B NAMs (sole scored class; target-level, wild type, no WWOX burst at this age) | 3 | 3 | unknown |
| P6-P8 | every other class | unknown | - | unknown |
| P13-P15 | 1= GABA-A PAM excl. benzodiazepines (L09) | 6 | 6 | unknown |
| P13-P15 | 1= NMDAR pore blockers (L01) | 6 | 6 | unknown |
| P13-P15 | 3. GluN2B NAMs (L04; L06 unscored) | 4 | 7 | unknown |
| P13-P15 | Kv7 openers (L12, sign unknown) | 0 | 3 | 1 off-genotype |
| P13-P15 | benzodiazepines (L10); GABA-AT/GAT (L11) | 0 each (sign unknown) | 3 each | unknown |
| P13-P15 | AMPA antagonists (L08) | 0 (sign unknown) | 0 | unknown |
| P13-P15 | T-type calcium; sodium-channel; SV2A; valproate-type; steroid/ACTH; cannabidiol/fenfluramine; carbonic-anhydrase/multi-target; ketogenic diet; GABA-AT clinical series | unknown (no thread tied to a WWOX phenotype at this age) | T-type: no P13-P15 line | unknown |
| later/unspecified | 1. NMDAR pore blockers (L02; L03 unscored) | 3 | 4 | unknown |
| later/unspecified | 2. GluN2B NAMs (L07) | 2 | 2 | unknown |
| later/unspecified | T-type calcium: thread present (L14), no WWOX phenotype link, so not scorable by sign | unknown | 21 (7 origins x 1 x 3) | unknown |
| later/unspecified | all other classes | unknown | - | unknown |

Endpoint development: empty ranking for every class and window (unknown, not neutral).

Notes on the ranking:
- At P13-P15 the top is a tie between GABA-A PAM and pore blockers under score_match; under score_literal GluN2B NAMs lead (7 against 6) because the L06 line (14%, interval 0-34) enters. The first place therefore depends on one sign decision (R1).
- The pore-blocker top rests on d-APV, an agent outside both split classes. The GABA-A PAM top rests on the sIPSC datum that T2 itself says cannot test the chloride gradient.
- T-type calcium has the largest literal score at later/unspecified (21) from seven heterologous or non-WWOX origins and no WWOX link; this is volume of tool pharmacology, shown for transparency and not used as a rank.
- Agent-level ranking inside the top class: not done. No thread discriminates two agents of a top class in a WWOX system (the memantine versus MK-801 contrast in T1_nmda_inv05.md item 5 and ## Corrections is non-WWOX, synaptic versus extrasynaptic only).

## C. Three weakest cells and the single measurement that would change the top class

1. GluN2B NAMs x seizure x P13-P15 (L04 and L06). The only number (14%, interval 0-34, evoked EPSC in wild-type barrel cortex, room temperature, between-cell, one concentration) comes from outside the burst preparation; the line's sign hinges on whether the interval excludes zero. Measurement: the NAM-sensitive fraction of the isolated NMDAR current in bursting KO slices at P13-P17 (WO-10). If its interval excludes zero the line becomes a match and GluN2B NAMs score 7 (top, score_match); if it is about zero they stay at 4.
2. GABA-A PAM x seizure x P13-P15 (L09). Tier 3 rests on a recording that cannot test the chloride gradient (pipette-set chloride, unblocked excitatory events, amplitude-dependent detection threshold). Measurement: re-record sIPSC with glutamate-receptor block, fixed absolute threshold and per-animal summary (M03 in T2). If the amplitude loss does not hold, tier 3 drops and pore blockers lead alone at 6. This is the single measurement that breaks the current tie toward the NMDAR side; WO-10 above is the one that moves GluN2B NAMs to the top.
3. NMDAR pore blockers x seizure x P13-P15 (L01). The measured agent is d-APV, no WWOX measurement of a pore blocker exists, and there is no drug-by-genotype arm (wild-type slices do not burst). Measurement: burst incidence against matched measured fractional NMDAR-current reduction for a d-APV titration and a pore-blocker titration in KO slices (X2/X5 in T1_nmda_inv05.md). A curve coinciding with d-APV would confirm the line; a failure would remove it.

## D. Outside knowledge and bundle gaps

Used in a cell: none. Class membership of the only agent measured in a WWOX system (d-APV) is placed by the bundle's own wording (a competitive reference); benzodiazepines are treated as unknown rather than as GABA-A modulators because only the rule's column header implies it.

Tempted to use, not used (each left unknown or at 0):
- Which class ethosuximide belongs to, and what it does (T3 line L15 left unassigned; it adds 0 under tier 0 anyway).
- That a ketogenic diet bypasses pyruvate dehydrogenase via ketone bodies (T10, L19).
- That carbonic-anhydrase inhibitors change tissue pH (T7 pH thread, L20).
- That GABA-AT or GAT inhibition raises GABA (T2, L11; directness held at 1 by the word GABA only), and any drug names for T6.
- That benzodiazepines are synaptic GABA-A modulators and what they do in a depolarising-chloride setting (aggravation left unknown).
- Whether sodium-channel agents aggravate seizures in any genetic epilepsy (T12 left unknown).
- General clinical use of valproate-type agents, SV2A ligands, steroids/ACTH, cannabidiol and fenfluramine in developmental epilepsies, and any clinical series in WWOX-related disease.
- The usual developmental timing of the GluN2B-to-GluN2A shift (the bundle calls its own mouse timing unverified and carried).
- Textbook mechanisms of retigabine-class and perampanel-class agents beyond what the files state.

What the bundle lacked and I needed:
- Any drug-by-genotype measurement of any class in a WWOX system (the only drug result is d-APV in KO slices).
- Any WWOX recording or burst at P6-P8; any development, viability or maturation endpoint.
- The isolated NMDAR current and its NAM-sensitive fraction in bursting KO slices (WO-10).
- An agent-to-class table (ethosuximide, benzodiazepine, d-APV) and the INV-03 rationale linking Cav3 to a WWOX phenotype.
- Threads T6 and T12, and any thread for sodium-channel, SV2A, valproate-type, steroid/ACTH, cannabidiol/fenfluramine, carbonic-anhydrase/multi-target classes.
- The gene of the "nulls" in the T3 PTZ figure (not named in the file).
- A statement of whether an unknown-sign line enters the score (R1), of which window holds P13-P17, and of a slice unit (R3, R4).
