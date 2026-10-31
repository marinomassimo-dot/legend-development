# PRE_REGISTRATION, IT14 P3 (function-first pharmacology). Fixed before any compound search.

Scientist, task `ORCH-ROADMAP-IT14-20261101`, branch `task/it14-p3` (from `task/it14`), 2026-10-31 (Europe/Rome). Public edition, WWOX-DEE genotype class. Not medical advice.
Written after reading: IT13 P3a and P3b READMEs, candidacies, datasets_q4; the P3a verification; IT6 P9 README; needs (4 entries); cards F01 F03 F04 H01 P11 (p4_fields); units U17 U21 U23 (units.tsv); the phenotype-first table; and the primary text of Breton 2021 (PMID 34634460, PMC XML in `files/fulltext`: Results 2.1 to 2.6, Table 1, Fig 3 to 6 legends). No compound has been searched in this session.

## 1. WWOX observations available (source: Breton 2021 Table 1 and Results, read in full text)

| Observation (S = Synapsin-Cre neuron deletion, P13-P17, layer II/III) | WT | HT | KO |
|---|---|---|---|
| Slices with spontaneous bursts | 0 of 11 | 4 of 23 | 36 of 42 |
| Pyramidal resting potential, mV (Table 1) | -79.25 +/- 1.99 | -75.51 +/- 1.81 * | -73.62 +/- 1.36 * |
| Input resistance, MOhm | 102.9 | 143.3 * | 143.0 * |
| Sag at -200 pA / post-inhibitory rebound | 1.18 / 0.96 | 2.04 * / 1.24 | 2.57 * / 1.86 * |
| sIPSC amplitude, pA (pooled WT+HT vs KO) | 57.3 (control) | (pooled) | 27.5 |
| F-I slope | 0.184 | 0.162 | 0.204 (no difference) |

Consequence I noticed only now, and which P3a did not use: the intrinsic changes (depolarisation, higher input resistance, larger sag) are already present in the heterozygote, which almost never bursts. They are graded with gene dose and shared; the burst incidence is not. So a depolarised resting potential alone cannot be the KO-specific step. What differs between KO and HT in the source is the statistical contrast on inhibition (KS sHT v sKO and sWT v sKO both significant; sWT v sHT not reported in the text: to be read from Fig 4H) and the mEPSC amplitude. Also: the sIPSC recordings used a KCl internal solution (Methods), so amplitude carries no information on the chloride gradient; sag in mV at a fixed current step scales with input resistance, so "Ih elevated" is not separated from the input-resistance change.

## 2. Scoring of candidate functional questions (0 to 3 per criterion; fixed before the ladder)

Criteria: R = WWOX relevance (a measured WWOX observation, in a WWOX-deficient system, motivates it); M = available functional measure (a number exists, with model identity and unit stated); D = ability to discriminate rival explanations of the same bursting; P = interrogable pharmacology (target-selective agents with public primary data exist); V = feasibility of verification (a verifier can check the decisive premise from public sources in days). Score = sum (max 15). Ties go to the question that also supplies the measurements for the others.

| Question | R | M | D | P | V | Sum | Reason in one line |
|---|---|---|---|---|---|---|---|
| Q-inh: synaptic (GABA-A phasic) inhibition onto layer II/III pyramidal cells | 3 | 3 | 3 | 2 | 2 | 13 | only deficit that is KO-specific by incidence; sIPSC numeric; titratable in WT and HT; PAM pharmacology subunit/state dependent (P=2) |
| Q-NMDAR: NMDAR contribution and its Mg2+ gate | 3 | 2 | 2 | 3 | 2 | 12 | d-APV abolishes bursts but cannot separate gain from permissive necessity; no NMDAR current measured; already designed (IT6 P9, F04, P11) |
| Q-intrinsic: resting potential / input resistance (generic K+ conductance) | 2 | 3 | 1 | 3 | 2 | 11 | numeric, but graded and shared with the non-bursting heterozygote |
| Q-HCN: Ih (sag, rebound) | 2 | 2 | 1 | 2 | 2 | 9 | sag confounded by input resistance; HCN blocker pharmacology not subtype-clean; authors cite worsening with ZD7288 |
| Q-PVfire: PV interneuron firing / Kv3 (interneuron AP amplitude 60.8 to 45.0 mV; Pvalb mRNA lower) | 2 | 2 | 2 | 2 | 1 | 9 | upstream of Q-inh; n = 5 to 6 interneurons; Kv3 modulators have thin public pharmacology |
| Q-Kv7 specifically | 1 | 1 | 1 | 3 | 2 | 8 | no Kv7 datum; Kcnq2 mRNA inside the control-line band; an opener hyperpolarises any neuron |
| Q-gapjunction/pannexin (carbenoxolone -87 percent of burst frequency) | 2 | 2 | 1 | 0 | 1 | 6 | carbenoxolone is non-selective; no selective agent with public pharmacology to ladder |
| Q-T-type/GIRK | 1 | 1 | 1 | 2 | 1 | 6 | one behavioural PTZ result; Cacna1g/h/Kcnj6 mRNA flat |
| Q-chloride gradient (NKCC1/KCC2) | 1 | 0 | 1 | 2 | 1 | 5 | no E_GABA measurable (KCl internal); transcript ratio not raised |

Rival "secondary state" (hypomyelination, illness, glycaemia, seizure history) has no pharmacological ladder; it is a control arm, not a question.

## 3. The question and contrast fixed

**Question.** In the Wwox neuron-deleted neocortex, is the loss of fast GABA-A synaptic inhibition onto layer II/III pyramidal cells the step that converts the graded intrinsic phenotype (shared by heterozygote and KO) into d-APV-sensitive bursting, and, if so, which pharmacological way of restoring inhibitory charge (post-synaptic receptor potentiation, reuptake/transaminase-mediated GABA elevation, or upstream interneuron firing) acts on that step without suppressing the network generally?

**Rivals (same pathological activity).** R1 NMDAR gain; R2 intrinsic depolarisation (graded; HT shares it); R3 disinhibition (this question); R4 secondary state; R5 gap-junction/pannexin-coupled propagation (only as a propagation, not initiation, factor).

**Contrast (what separates them), in the Breton preparation, animals as units, Cre-negative and heterozygote slices kept separate:**
1. Same-cell triad in KO, HT, WT: isolated NMDAR current (amplitude, decay, GluN2B sensitivity), sIPSC amplitude and charge with a physiological internal chloride, resting potential and input resistance.
2. Sufficiency in WT and HT slices: reduce IPSC charge to the KO-measured fraction with a titrated GABA-A antagonist, and separately depolarise by the measured 5.6 mV (bath K+), and separately lower Mg2+ only to the point that matches the KO-measured NMDAR current if raised; ask which single manipulation yields d-APV-sensitive bursts.
3. Necessity/correction in KO slices: restore IPSC charge to the control value with each of three mechanisms (post-synaptic PAM, GAT1 inhibition or GABA-T inactivation, PV-firing enhancer if a selective one exists), and, as non-discriminating symptom controls, an antiseizure agent of unrelated mechanism and TTX.
4. Controls for suppression: the same agents on WT slices evoked responses and on non-burst firing (F-I curve), cell viability, and wash-out; a firing-reduction readout is accepted only with these.

## 4. Predictions, fixed now

- P-i: the ladder will not produce one molecule that is "the" GABA restorer; "GABA-A PAM" is not an identity: effect depends on alpha/gamma/delta subunits, synaptic vs extrasynaptic pool and state (benzodiazepine site needs gamma2; neurosteroids act at delta). So at most probe-level hypotheses per mechanism.
- P-ii: vigabatrin (the clinical reference with partial-benefit reports in WWOX-DEE) raises ambient GABA; its action maps to tonic, not to the amplitude of phasic IPSCs, so it is an alternative mechanism on the same function and not a test of the sIPSC deficit.
- P-iii: no therapeutic candidacy will survive; the useful output is the experiment and its correction of P3a (the Kv7 proposal rested on a depolarisation shared with the HT; it loses priority).
- P-iv (abstention condition): if Fig 4H shows sIPSC reduced in HT to the KO level, the KO-specificity argument fails and the question reverts to Q-NMDAR (12 points) as the leading function.
- Weaker-claim guard: ChEMBL/IUPHAR values are recorded as the source states them, assay and species per row; no value is carried to another molecule.

## 5. Out of scope

Individual regimens; supplement/OTC priority; any statement of benefit for a person.
