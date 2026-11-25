# ADV-278 spec: does valproate change WWOX protein in human neural cells? A one-page discriminating experiment (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; no clinical dose or treatment recommendation; nothing here is medical advice. Held material only (no new paper search, no external service, no contact, no spend). Consumers: DL-REPO-003 (IT), RP-008, the portfolio. Design for the operator and any laboratory the operator chooses; nothing is to be run, bought or contacted from this file. Sources named inline; numbers recomputed by `adv278_n.py` (output `adv278_n_output.tsv`). One premise of the brief is corrected in section 6.

**The question.** ADV-275: WWOX **mRNA** is up after valproate in four human neural deposits from four institutions (WWOX ratios 1.28 to 1.91; mean of log2 0.615 = 1.53-fold, SD of log2 0.22 across deposits, none down). ADV-277: WWOX **protein** has no counterpart: in the one valproate organoid proteome where the exposure acted (H1-0 protein 1.8 to 2.6-fold) WWOX has no protein group among 5,104. The DL-REPO-003 annotation "decreases expression" is therefore untested at protein level, and a protein that is lost in the disease cannot be assumed to follow its transcript.

## 1. Readout (what can see WWOX protein) and the floor

| Role | Assay | Why this, from held records |
|---|---|---|
| Primary | **Targeted MS (PRM/SRM), heavy-labelled standard peptides, two tryptic peptides, one N-terminal and one C-terminal to residue 230**, same lysate as the sentinel | `sdr_missense_readout_assessment_20260920` and census S3/T8: antibody-independent, absolute copy number, lower bound stated; the shotgun DIA run did not see WWOX at all (ADV-277), so shotgun depth is not enough. Two peptides because one peptide can lie (a modified or missed-cleavage peptide). Peptide sequences are **not held**; the laboratory chooses them from recombinant WWOX digests. |
| Secondary | Immunoblot, **HPA050992** (aa 32 to 110, N-terminal; WB 1:1000 attested in rat, Tochigi 2019) plus **fragment-competition control** (preadsorb with the GST fusions `ww 1-110` and `ADH 110-414`, census S2); a WWOX-null human lysate as negative lane if the laboratory holds or makes one (none is held here) | Census: 0 of 17 antibodies are wholly C-terminal to 230; no antibody has a stated sensitivity floor (0 of 12 rows, lysis census); DETECTION-FLOOR record: "not detected" is an assay result, never "absent". The blot cannot be the primary readout because its floor is unknown. |
| Sentinel (same lysate) | **H1-0 protein by PRM** (acted 1.8 to 2.6-fold in the organoid deposit); acetylated histone H3 or H4 on the blot as second sentinel | ADV-277: the RNA sentinel (H1F0, CDKN1A) failed where the exposure plainly acted, so the sentinel must be protein, in the same lysate. |
| Normalisation | Median of at least 20 unchanged reference peptides plus total protein; RNA by at least three reference genes verified unchanged | HDAC inhibitors shift global expression (ADV-275 limit); one housekeeping gene is not a normaliser. |

**The floor and where the number comes from.** No held record gives WWOX absolute abundance in human neural cells. What is held: (a) the organoid DIA run quantified H1-0 at about 4 to 7 x 10^5 (arbitrary intensity) and not WWOX, so WWOX there lies below that run's floor (coverage); (b) two mouse brain tables quantify Wwox at about 9 x 10^3 (prefrontal, TMT/DIA units) against H1-0 at a control mean of 1.7 x 10^5 in the same table (about 5 percent), and 8.3 to 8.9 x 10^3 against H1-0 2.5 to 3.2 x 10^4 in striatum (about 30 percent): different tissue, species, platform and units, so **not an absolute number and not transferable**. The requirement is therefore stated as a gate, not as a figure: **step 0 (two vehicle lysates, dilution series of the heavy standard, at least 5 points) must give the endogenous level in fmol per ug and the lower limit of quantification (LLOQ); the endogenous peptide in vehicle must sit at 3 times LLOQ or more**, so that a fall to two thirds (the margin of section 4) is still above LLOQ. Blot: LLOQ in ng from a >=5-point dilution of a WWOX-positive lysate or recombinant protein on the same membrane (lysis census rule). If step 0 fails, stop: outcome 4.

## 2. Design (units, arms, exposure)

* **Preparation:** human forebrain organoids or NGN2 neurons as in the held deposits (organoids from day 21, 1 mM valproate; sampled day 35 and day 50, MSV000097991; NGN2 neurons with VPA from day 1, GSE129241). **Unit = independent differentiation batch within a line** (a pool of at least 3 organoids is one unit's arm); paired vehicle and drug arms started from the same batch. **Lines as units are not enough:** three lines (the held proteome) give a smallest detectable fold of 2.6 at the held spread (section 3).
* **Arms (concurrent, same plate layout, same medium change days):** vehicle; valproate at two targets, **about 0.1 mM free** (the top of the paediatric binding model in `free_serum.tsv`: total 100 ug/mL = about 15 ug/mL free) and **1 mM** (the level that acted in the held organoid deposit; ADV-275 deposits span 0.4 to 1 mM); **entinostat** (class I benzamide: moved 3 of 5 WWOX probe sets in Rempel 2015, sheet "entinostat" 1.25 to 1.51) and **vorinostat** (hydroxamate, no probe set moved, largest 1.24; ADV-269 sheets by name) as the **class-heterogeneity control** (ADV-273: 3 of 6 HDAC inhibitors moved WWOX). Concentrations of the two controls: titrated in step 0 to H1-0 PRM >= 1.5-fold; held anchor only vorinostat 1 to 2.5 uM in neurons (ADV-275). No dose is recommended for any person.
* **Exposure is measured, not nominal (RP-047 rule):** LC-MS/MS of valproate (total, and free by ultrafiltrate of the medium, since the medium may carry albumin: assumption, to be confirmed on the lot used) in fresh and spent medium at every medium change and at harvest, and in the lysate if the method allows. **An arm counts as exposed only if** the measured harvest-time concentration is within 30 percent of its target (a design choice, adjustable) **and** H1-0 PRM >= 1.5-fold in that unit. Others are reported, not pooled.
* **Time:** primary = **14 days of exposure (day 21 to day 35)**, where the sentinel is held to act; secondary = 72 h (the transcript deposits, GSE187006, GSE241903), with RNA and protein from the **same** lysate, because a protein with a long half-life can lag a transcript (half-life of WWOX not held).
* **Disease context:** wild-type reference cells only. A WWOX-deficient or hypomorphic line would be the second experiment (RP-047 factorial), never mixed into this one.

## 3. n from the held spread

| Held anchor (per held file) | Spread of log2 |
|---|---|
| H1-0 protein per-line ratio, D50 (1.82, 2.14, 2.59) / D35 (1.97, 2.52, 3.54), `adv277_values.txt` (file ratios are arithmetic-mean ratios; blind recompute on geometric means: D50 SD 0.30, D35 0.26 on two lines or 0.43 with the one-control KOLF2 line) | SD 0.26 to 0.30 / 0.26 to 0.43 |
| Within-arm H1-0 pools, D50, per line (BIONi, HMGU1, KOLF2) | SD 0.22, 0.09, 0.61 (KOLF2 is the noisy line) |
| Mouse Wwox intensity, within arm (prefrontal, striatum) | SD 0.25, 0.05 |
| WWOX mRNA ratio, 5 up-called human deposits (my selection) / all 8 eligible rows with >= 3 per arm (blind reader's rule, incl. not-distinguished rows) | SD 0.22 (mean 1.53-fold) / 0.26 (mean 1.43-fold) |

Planning value **s = 0.43** (largest held between-line spread; every other held spread, including the 0.26 transcript SD, is lower; WWOX is far scarcer than H1-0, so its real spread is likely larger: unquantified). Paired one-sample t on log2 ratios, alpha 0.05 two-sided, 80 percent power, Monte Carlo (`adv278_n_output.tsv`):

| Units n | smallest detectable rise / fall at s = 0.25 | at s = 0.43 | at s = 0.60 | power at the expected 1.5-fold, s = 0.43 |
|---|---|---|---|---|
| 3 (lines) | 1.76 / 0.57 | 2.64 / 0.38 | 3.91 / 0.26 | 0.28 |
| 4 | 1.44 / 0.69 | 1.87 / 0.53 | 2.42 / 0.41 | 0.47 |
| 6 | 1.28 / 0.78 | 1.54 / 0.65 | 1.83 / 0.55 | 0.76 |
| **8** | 1.23 / 0.82 | **1.41 / 0.71** | 1.62 / 0.62 | **0.91** |

**Specified n: 8 independent batches in at least 3 lines (for example 3 lines x 3 batches, one line with 2), per arm, paired.** Six is marginal (the expected 1.5-fold sits at its limit); three lines alone cannot resolve less than a 2.6-fold change and would return "none" for a real rise. Spread is a held-data proxy for H1-0, not WWOX: **step 0 replaces it** with the WWOX spread from the vehicle pairs, and n is recomputed before the drug arms are run.

## 4. PREREG (to be fixed by the laboratory before the run)

Primary contrast: valproate (exposed arm of section 2) against concurrent vehicle, geometric-mean ratio of the two-peptide WWOX quantity, 14 days, paired by batch, n = 8, 95 percent CI. **Expected: 1.3-fold up (range 0.9 to 1.8)**: the mRNA rise (1.43 to 1.53-fold depending on whether not-distinguished rows are counted; up-called range 1.28 to 1.91) attenuated at protein level (my prior, not sourced); probability that WWOX is quantifiable in vehicle 0.7 (the organoid DIA miss is a depth statement, not an absence); given quantifiable, up 0.5, none 0.35, down 0.15 (my priors).

| Outcome | Rule (all of: step 0 passed, sentinel passed in the units counted, >= 6 units quantified per arm, both peptides agree in direction) | DL-REPO-003 | RP-008 and portfolio |
|---|---|---|---|
| **UP** | ratio >= 1.2 and lower 95% CI > 1 | The mRNA rise has a protein counterpart in a human neural system under measured exposure: positive control exists; the "decreases expression" annotation is contradicted in this system at both levels; class heterogeneity gets a protein answer if entinostat and vorinostat differ. | Closes the protein-gap question; opens the WWOX-deficient factorial (RP-047) with this arm as its positive control. |
| **DOWN** | ratio <= 0.83 and upper 95% CI < 1 | The curated direction is supported at protein level against the transcript: a concern, in a disease of WWOX loss, that needs the same assay in a hypomorph and a dose-response before anything is said; the transcript rise stays a transcript fact. | Raises a safety-direction row to the portfolio's front; no clinical statement. |
| **NONE** | 95% CI wholly inside 0.67 to 1.5 | Transcript rise does not reach protein under 14-day exposure: the "positive control" is a transcript control only; annotation not supported. | Parks valproate-WWOX; frees the strand. |
| **NOT DETECTABLE** | endogenous peptide below 3 x LLOQ in vehicle in at least half the units, or sentinel failed, or fewer than 6 units | Coverage statement only: "not detectable with the assay at stated LLOQ"; no direction. | A reading question (which targeted WWOX quantification exists: none in the 2026-09-21 census, query dated) and an assay-development item; do not re-run valproate. |

A fifth, non-outcome state is reported as such: all conditions met but the CI straddles a margin (neither UP, DOWN nor NONE): **unresolved at n = 8**; report the CI, do not call it "none".
**Rejecting observation** (of "valproate raises WWOX protein >= 1.2-fold"): sentinel passed, >= 6 units quantified, upper 95% CI < 1.2.

## 5. What makes the experiment uninformative (so it is not run)

1. Step 0: the endogenous WWOX peptide is under 3 x LLOQ in vehicle (the held shotgun run already failed to see it): stop; assay development first.
2. H1-0 PRM < 1.5-fold in the valproate arm, or measured exposure outside 30 percent of target (RNA sentinels alone do not count: they failed where the exposure acted).
3. One line, one batch, or lines as the only units (smallest detectable change 2.6-fold): returns "none" for a real rise.
4. A single antibody or a single peptide as the readout; an antibody without the fragment-competition or WWOX-null control; the C-terminal side of residue 230 read on a datasheet nobody opened (census S5).
5. Drug arms and vehicle not concurrent, or normalisation to one housekeeping gene or protein.
6. Valproate added only for hours when the protein half-life is unknown (the 72 h arm is secondary for that reason).

## 6. The brief's premises against the held records

Checked and **not contradicted**: the class split (VPA, entinostat, TSA move at least one WWOX probe set; panobinostat, belinostat, vorinostat none) matches the Rempel sheets as corrected after my own slip (read by sheet name: VPA 600 uM 1.19, 1.43, 1.09, 1.33, 1.68, three of five probe sets up; entinostat 1.25 to 1.51, three up; TSA one up and one down); the 5,104 protein groups and the absent WWOX group match `adv277_values.txt` and the ADV-277 result. Two cautions the brief does not carry: (1) the day-35 H1-0 geometric mean in the organoid deposit includes a line (KOLF2) with one quantified control, so the D35 spread of 0.43 is the weakest of the held spreads; (2) the same organoid study prints WWOX **mRNA** 2.06-fold up at day 50 (ADV-277 section 5, Supplementary Table 2, adjusted p 1.2e-13), so WWOX is transcribed in that material while its protein was not seen: step 0 is the first thing to learn, not a formality.

Closure: increment about 60 minutes; blind arithmetic check of section 3 (one `legend-delegate`, sonnet, effort high, stated) in `BLIND_CHECK_N_ARITHMETIC_ADV278_SCI_20261125.md`; whether a successor window is wanted: see the note to ADV.
