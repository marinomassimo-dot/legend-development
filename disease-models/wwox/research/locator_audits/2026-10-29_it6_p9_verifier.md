# Independent verification of iteration 6, package P9 (NMDA-receptor intervention classes)

Verifier: independent of the producer. Date: 2026-10-29. Object: branch `task/it6-p9`, directory
`disease-models/wwox/research/drug_repurposing/nmdar_pharmacology_it6_p9_20261029/` (README, comparison table, tool-compound pull,
arithmetic script, F04 packet and card, proposed edits) and the P8 pull. Judged from the sources and by recomputation: the Breton 2021
XML, supplement document and Figure 3 image on disk; ChEMBL REST (re-queried); PubChem PUG REST; ClinicalTrials.gov API v2; openFDA
label JSON; Europe PMC abstracts and open XML. Nothing was registered, no contact address was sent, nothing was paid for.
Marks: SUPPORTED / OVERSTATED / NOT SUPPORTED / UNVERIFIABLE. Not medical advice.

## 1. Verdict

The package is largely accurate at the level of numbers and locators: 32 of 40 checked statements are SUPPORTED. The weaknesses are in
the decision logic, not the data. Three findings should be repaired before the card is relied on:
(a) the ordering "permissive necessity better supported than NMDAR gain" leans on an AMPAR-weighted current comparison that the
README itself says carries no NMDAR information (D1); (b) the F* decision variable is stated with predictions that are not derived
and whose threshold is undefined (D2); (c) the "30- to 100-fold per 20 mV" figure used to demote memantine is physically implausible
for a single-site pore block and rests on one closed paper that was not opened (D3). One factual overgeneralisation about trial
exclusion criteria sits in the README and in the card (D4). The card F04 stays within hypothesis.

## 2. Checks (location, quote, mark)

### 2.1 Breton 2021, PMID 34634460 (local XML, supplement, Figure 3 image)

| # | Statement under test | Source location and quote | Mark |
|---|---|---|---|
| 1 | Age P13-17; bursting in 36/42 knockout, 4/23 heterozygote, 0/11 wild-type slices; hippocampal slices do not burst | Results 2.1: "13 to 17 day old ... 0 of n = 11 ... 4 of n = 23 ... 36 of n = 42 ... hippocampal slices exhibited spontaneous activity indistinguishable from controls" | SUPPORTED |
| 2 | Slices 400-500 um; incubation ACSF with 1.3 mM Mg2+, 3.5 mM K+, 1.5 mM Ca2+, 35 C | Methods 5.2: "sectioned coronally 400-500 um thick"; "ACSF ... 3.5 KCl, 1.3 MgSO4, 1.5 CaCl2 ... kept at 35o for 30 min ... experimentation at 35o". The recording perfusate is not stated separately, as the README says | SUPPORTED (the "not stated" caveat is correct) |
| 3 | d-APV 50 uM; n = 51 bursts, 5 slices, 3 animals | Fig 3 legend: "n = 51 bursts, 5 slices, 3 animals d-APV"; Results: "d-APV (50 uM) eliminated the spontaneous bursting events" | SUPPORTED |
| 4 | sEPSC 23.3 vs 24.7 pA; sIPSC 57.3 vs 27.5 pA with reduced frequency | Results 2.5: "S-CTL 23.3 +/- 12.0 pA; S-KO 24.7 +/- 13.6 pA"; "sIPSCs were reduced in both amplitude and frequency ... 57.3 +/- 31.0 pA; 27.5 +/- 19.4 pA; 10.3 vs 8.4 Hz". The control group is wild type and heterozygote combined ("S-CTL"), and the sEPSC amplitude is described by the source as "significantly more large-amplitude sEPSCs" | SUPPORTED, with the control-group definition missing from the README table |
| 5 | Resting potential -79.25 vs -73.62 mV (heterozygote -75.51); 13, 15, 40 cells | Table 1 row "Resting membrane potential" and "N's 13/5, 15/6, 40/15" | SUPPORTED |
| 6 | Baseline rate 2.29/min (main text) vs 0.84/min (Table S1), "for the same 119 bursts" | Main text: "median inter-burst interval was 26.2 s (2.29 [1.1-4.2] bursts/minute)". Supplement Table S1 (read from the document's table cells): "Frequency (bursts/min) .84 [.57-.1.53]; min 0.36, max 3.89", "N's 119/18/9". The two figures and the 2.7-fold gap are correct (60/26.2 = 2.29). The main text gives no n for the 2.29; "same 119 bursts" is inferred from the identical median duration 0.66 [0.53-1.06] in both places | SUPPORTED for the figures; the "same 119 bursts" is an inference stated as fact (see D7) |
| 7 | Fig 3D carries no significance marker on the d-APV arm | Rendered Figure 3: the bracket and asterisks span baseline-to-CBX in panels d1 and d2; the d-APV bar is absent; the d-APV washout bar is about 1.8 with a large error bar. The legend p values (0.008, 0.0036, 0.0274) are the CBX values in Table S1 text ("decreased the frequency by 87% (p = 0.008) and their duration by 18% (p = 0.0274)") | SUPPORTED |
| 8 | Fig S3C: d-APV effect significant at only the three highest of six strengths | Fig S3 legend: "p values relative to baseline for d-APV treatment ... 0.4798, 0.6458, 0.1692, 0.0229, 0.0103, 0.0006; washout ... 0.9425, 0.2524, 0.1975, 0.0492, 0.0372, 0.0499. unpaired t-test n = 6 slices, 3 animals" | SUPPORTED |
| 9 | mEPSC decay 5.18 vs 4.84 ms; donors under pentobarbital | Results 2.4 ("p = 0.2982"); Methods 5.2 | SUPPORTED |

### 2.2 Arithmetic

| # | Statement | Recomputation | Mark |
|---|---|---|---|
| 10 | Unblocked NMDAR fraction rises 1.41-fold from -79.25 to -73.62 mV at 1.3 mM Mg2+ | B(V) = 1/(1 + ([Mg]/3.57) exp(-0.062 V)): 1.98 % and 2.78 %, ratio 1.41 (script re-derived by hand). The constants 3.57 mM and 0.062 per mV are the standard Jahr-Stevens 1990 values; the paper was not retrievable here, so they stay unchecked at the source, as the README says | SUPPORTED (arithmetic); constants UNVERIFIABLE here |
| 11 | d-APV occupancy at 50 uM from ChEMBL Ki | Re-queried: Ki 280/460/1640 nM (CHEMBL1143579), 390/2800/5900/21000 nM (CHEMBL4024770), all rat oocytes. Occupancy 99.4, 99.1, 96.8, 99.2, 94.7, 89.4, 70.4 % | SUPPORTED |
| 12 | Memantine/ketamine potency falls 30-107-fold per 20 mV "in one document" | The values exist: memantine 840 and 780 nM at -60 mV, 28070 and 25630 nM at -40 mV; ketamine 500/510 and 53320/15220 nM, all in ChEMBL document CHEMBL6083260 (Konecny et al. 2024, Eur J Med Chem, "Dizocilpine derivatives ...", PMID 39442339), human clones in HEK293. Ratios 33, 33, 107, 30 reproduce. The paper itself was not opened by the producer and could not be opened here | Values SUPPORTED as ChEMBL rows; the physical reading is OVERSTATED (D3) |
| 13 | Mg2+ lowers memantine inhibition of GluN2A/2B about 20-fold and of GluN2C/2D about 3-fold | Kotermanski and Johnson 2009 abstract: "1 mM Mg2+o decreased memantine inhibition of NR1/2A and NR1/2B receptors nearly 20-fold ... NR1/2C and NR1/2D ... approximately 3-fold". Body not retrievable | SUPPORTED at abstract level; UNVERIFIABLE for the body, as the README states |

### 2.3 Tool-compound resolution and ChEMBL data quality (ChEMBL_37, re-queried)

| # | Statement | Finding | Mark |
|---|---|---|---|
| 14 | Resolution by InChIKey: Ro 25-6981 = CHEMBL305195; TCN-201 = CHEMBL2333945; NAB-14 = CHEMBL4583491; d-APV = CHEMBL84612 | Each key returned exactly that id. PubChem names: (1R,2S)-4-[3-(4-benzylpiperidin-1-yl)-1-hydroxy-2-methylpropyl]phenol (the Ro 25-6981 free base); TCN-201 (N-[[4-(benzamidocarbamoyl)phenyl]methyl]-3-chloro-4-fluorobenzenesulfonamide); NAB-14 (indol-7-ylcarbamoyl phenyl diethylcarbamate); (2R)-2-amino-5-phosphonopentanoic acid. The (2R) form matches the D-(-)-APV used by Breton | SUPPORTED |
| 15 | NVP-AAM077 matched on the connectivity block only; stereochemistry unverified | CHEMBL273636 carries the (S)-1-(4-bromophenyl)ethyl centre but an unspecified alpha carbon; the PubChem record used for the key is the racemic PEAQX (CID 73409722). The caveat is correct and in fact stronger than stated: the identity of the active diastereomer is not settled by the ChEMBL record | SUPPORTED |
| 16 | NVP-AAM077 about 110-fold (human IC50) vs about 12-fold (rat Ki) | Human: 270 nM (2A) vs 29600 nM (2B) = 110-fold (CHEMBL1135273). Rat: Ki 5.4 vs 67 nM = 12.4-fold (CHEMBL1143579). The same rat document gives Ki 11.6 nM at GluN2C, so the rat compound is not 2A-selective over 2C, which the table's "GluN2A-preferring" label does not convey | SUPPORTED (minor omission) |
| 17 | Eliprodil: 8 rows, 8 documents, one value | On the GluN2B single-protein target CHEMBL1904 exactly 8 rows, 8 documents, all Ki 13 nM. Across all targets the same 13 nM recurs on 14 rows and 14 documents, so the problem is wider than stated | SUPPORTED (understated) |
| 18 | Memantine GluN2A 0.95 nM outlier vs 911 nM | 0.95 nM (CHEMBL2396530, "unknown origin", oocytes) vs 911 nM (CHEMBL1146243, oocytes). Both rows present | SUPPORTED |
| 19 | Esketamine 11.4 nM is an LDH excitotoxicity assay | Assay CHEMBL3636231: "inhibition of glycine and glutamate induced excitotoxicity incubated for 12 hrs by LDH assay", mouse L(tk-) cells. The comparison range "300 to 960" is the rat-labelled rows; guinea-pig and pig rows give 108, 383, 419 | SUPPORTED (range slightly narrowed) |
| 20 | TCN-201 GluN2A assays attached to the GRIN1/GRIN2B target | CHEMBL1907603 holds 446 nM whose assay text reads "human GluN1/GluN2A ... oocytes" (CHEMBL4308997) and 100 nM whose assay text reads "GluN1/GluN2B ... FLIPR" (CHEMBL2343341). The first is a clear mapping artefact; the second is a conflicting annotation that the README calls a review citation, which was not checked | SUPPORTED for 446; UNVERIFIABLE for the "review citation" explanation of 100 |
| 21 | Radiprodil: 9 ChEMBL rows, 4 documents, human-labelled rows without assay organism | 9 rows over CHEMBL1137121, CHEMBL1799931, CHEMBL4052799, CHEMBL4316607; IC50 4-70 nM human-labelled, 3.16 nM mouse, 31.6 nM rat | SUPPORTED |

### 2.4 Human exposure and labels

| # | Statement | Finding | Mark |
|---|---|---|---|
| 22 | Radiprodil: 460 adults (332 neuropathic pain), 3 infants, PN12 | Auvin 2020 XML: "clinical experience ... in 460 adult individuals, including healthy volunteers ... and 332 patients with neuropathic pain"; "Three infants"; "maximum at PN12". Spasm-free after relapse: all three eventually spasm-free on other treatment | SUPPORTED. The 460 includes healthy volunteers; the README line "adults 460 (332 neuropathic pain ...)" does not say so |
| 23 | NCT05818943 phase 1b, 24; NCT07224581 phase 3 recruiting | NCT05818943: registry phase "PHASE1", 24 estimated, ages 6 months-12 years, GRIN gain-of-function, active not recruiting. NCT07224581: official title "Open-Label Phase 1b and a Randomized, Double-Blind, Placebo-Controlled Phase 3", recruiting, 100 estimated, 1 month-18 years. NCT06392009 (TSC/FCD, phase 1/2) and NCT02829827 (infantile spasms, phase 2, terminated, 3 enrolled; "UCB has made the decision to stop the study") confirmed | SUPPORTED |
| 24 | "the registered GRIN studies exclude memantine and perampanel as co-medication" (README section 6; the card's `paediatrics_and_interactions`) | NCT05818943 and NCT06392009: "contraindicated concomitant drugs such as agonists or antagonists of the glutamate receptor, including ... felbamate, memantine, and perampanel". NCT07224581 full eligibility text has no such exclusion (exclusions: clinically relevant condition, more than 4 ASMs, body weight under 5 kg) | OVERSTATED (D4) |
| 25 | Selfotel stroke: day-30 deaths 54/280 vs 37/286 (P 0.05), 90-day 22 vs 17 % not significant | PMID 10657404 abstract: "day 30: 54 of 280 versus 37 of 286; P=0.05"; "62 deaths (22%) ... 49 (17%) ... P=0.15" | SUPPORTED |
| 26 | Selfotel head injury stopped for deaths and futility | PMID 10541229 abstract: stopped for "concern about possible increased deaths and serious brain-related adverse events" and futility; "more complete data analysis revealed no statistically significant difference in mortality". The README omits the later non-significant mortality result, and section 1 item 4 summarises both trials as "stopped ... with a mortality signal" | OVERSTATED (minor, D6) |
| 27 | Memantine label: paediatric effectiveness not established; autism studies failed in 578 children | openFDA label (effective 2026-09-01), 8.4: "Safety and effectiveness in pediatric patients have not been established. Memantine failed to demonstrate efficacy in two 12-week controlled clinical studies of 578 pediatric patients aged 6 to 12 years" | SUPPORTED |
| 28 | Perampanel label: from 4 years, boxed psychiatric warning | openFDA: "partial-onset seizures ... 4 years of age and older"; boxed "SERIOUS PSYCHIATRIC AND BEHAVIORAL REACTIONS". A newer perampanel label (effective 2026-06-02) exists beside the 2025-12-19 one cited; wording identical on these points | SUPPORTED |

### 2.5 Karnstedt, Phillips, counter-evidence

| # | Statement | Finding | Mark |
|---|---|---|---|
| 29 | GRIN series: improvement 14/19 gain-of-function vs 3/15 otherwise; individuals 32-34 same GRIN2D variant, opposite outcomes; seizure worsening in three, EEG worsening in three | Karnstedt 2026 XML: "14/19 GoF vs. 3/15 LoF, p = .0049"; "Individuals #32, #33, and #34 carried the same variant in GRIN2D ... #33 and #34 with seizure frequency reduction approximately at 50% and #32 with worsening"; "In three individuals (#10, #25, and #32), seizure frequency worsened"; "Three cases had worsening of EEG findings". The same text attributes the 32 vs 33 difference partly to age at start (6 y 6 m vs 2 y 6 m), which the README omits. Seizure-frequency reduction was not significant (7/18 vs 2/10, p = .417) | SUPPORTED as quoted; OVERSTATED where used as precedent for a seizure effect (D5) |
| 30 | Memantine inhibition rises with intracellular Ca2+; GluN2D mainly in interneurons so memantine at 10 uM causes pyramidal disinhibition | Phillips 2026 XML Discussion: "in cortical brain slices, where the GluN2D subunit is expressed predominantly in inhibitory interneurons (86, 87), 10 uM memantine causes pyramidal cell disinhibition (88)". Both statements are secondary citations inside Phillips; Phillips recorded in zero Mg2+ in tsA201 cells and itself concludes that disinhibition "still may be observed" at physiological Mg2+ | SUPPORTED as a secondary statement (the README marks it UNVERIFIED) |
| 31 | Ikonomidou 1999: NMDA blockade for hours in late fetal or neonatal life causes widespread apoptosis in the rat | PMID 9872743 abstract, verbatim; agents not named in the abstract, as the README says | SUPPORTED (abstract only) |
| 32 | Adult memantine cohort 211, median age 63, 7 vs 5 with increased frequency; SUPER-CAT 84 vs 49 %, liver injury 77 vs 27 % | PMIDs 41288262 and 42837646 abstracts match exactly | SUPPORTED |
| 33 | Radiprodil effective at more than 80 % of tested gain-of-function GRIN variants | Banke 2026 abstract: ">80% of human disease-associated GRIN1 and GRIN2B missense variants tested in vitro (22/27 ...)" | SUPPORTED |
| 34 | Card F04 states no efficacy, no dose | All 431 string fields searched for efficacy, dose, recommendation and treatment wording. Hits are label quotations, source endpoint names, negations ("No dose, route, schedule or individual recommendation appears") and the explicit limit "Technical comparison is not efficacy, safety or experimental validation". The "for" evidence line that quotes radiprodil activity at GRIN variants and memantine benefit in the GRIN series is attributed and scoped to gain-of-function disease | SUPPORTED, except the exclusion sentence in D4 |

## 3. Decision logic

**3.1 "Permissive necessity better supported than NMDAR gain" (README section 1 item 1). OVERSTATED.**
The README says the source's synaptic data "favour the second reading more than the first" because excitatory amplitude differs by
about 6 percent and inhibitory amplitude by about 52 percent. Section 2 of the same README states that an mEPSC recorded at -70 mV in
1.3 mM Mg2+ "is AMPAR-weighted: it says nothing about NMDAR". A 6 percent AMPAR-weighted difference therefore cannot count against
NMDAR gain. The inhibitory deficit is real and is what the source itself concludes ("primarily through an impairment in the amplitude
of the inhibitory currents"), and it favours a disinhibition component, but it does not exclude NMDAR gain, and H1 and H2 are not
exclusive. What the data support is narrower: no NMDAR-specific measurement exists, the one indirect indicator (mEPSC decay, 5.18 vs
4.84 ms, p = 0.30) shows no change, and the d-APV result alone cannot separate the readings. The README's closing sentence of item 1
("an inference from a single preparation, not a finding") is the correct strength; the "favours" sentence before it is not.
The source also reports a significantly raised mEPSC amplitude in the knockout (Results 2.4), which fits an AMPAR-led reading (H3)
and is described by the README only as "a sliver".

**3.2 The F* experiment and its decision meanings (README section 7). Design sound for E0, E1, E3, E5, E6; OVERSTATED for the F* meanings.**
E1 (isolated NMDAR current, NMDA:AMPA ratio, subunit fractions, resting potential, all genotypes, animal as unit) is the correct direct
discriminator and is well controlled. E3 (matched-trigger wild-type control) correctly prevents a generic dependence from being read as
a Wwox finding. The problems are in E2:
- The table assigns "F* small" to H1 and "F* near complete" to H2. No derivation is given. A threshold network burst can stop at partial
  block under a normal receptor (loss of recruitment), and a raised receptor can still need most of its current blocked. F* is a
  property of network gain, not of which reading is true, so the prediction column of section 3 is asserted, not shown.
- "Small" and "near complete" have no numbers. The README says thresholds are to be fixed before running; that is acceptable only if the
  fixing precedes unblinding and the criterion is written beside the table.
- A GluN2B NAM blocks only the GluN2B-containing fraction, so its ceiling is set by subunit composition. If bursts persist at the NAM
  plateau, F* is undefined; the design then depends on d-APV alone, whose block is surmountable by the high glutamate transient in a
  burst, so the occupancy computed at agonist well below EC50 (the "upper bound") overstates the block during a burst.
- The step from F* "near complete" to "no tolerable window for NMDAR block" mixes a slice measurement with a developmental-toxicity
  argument; the second part rests on an abstract (Ikonomidou) that names no agents.
Recommendation: state F* as an exploratory read-out, add the written threshold, and let E1 carry the H1/H2/H3 decision.

**3.3 "Memantine becomes a translation probe, not the first discriminator" (README section 1 item 2). Reasoned, SUPPORTED with one caveat.**
The argument rests on two supportable points: Mg2+ shifts memantine potency roughly 20-fold at GluN2A/2B but 3-fold at GluN2C/2D
(Kotermanski abstract), and Phillips 2026 shows added Ca2+-dependence on GluN2A. These make a memantine result in 1.3 mM Mg2+ hard to
assign to a subunit, and the README is right that a null can be a concentration artefact and an effect can be a GluN2D-interneuron
(disinhibition) effect. The caveat is D3: the quantitative "30- to 100-fold per 20 mV" statement attached to this argument is not
needed for it and is the weakest part. Also, F01 is correctly left unchanged and F04 is written as a dated successor.

**3.4 Perampanel and complete competitive block as non-discriminators. SUPPORTED** as reasoning (AMPAR block removes the depolarisation
that relieves Mg2+ block; complete block is the experiment already done). The section 3 prediction that an AMPAR antagonist reduces
bursts under every reading is an inference and is labelled as such.

**3.5 Card F04 stays within hypothesis. SUPPORTED** (check 34): no efficacy claim, no dose, no individual recommendation; expected
contribution "UNKNOWN"; burst control separated from developmental recovery.

## 4. Defect list

| ID | Severity | Defect | Where | Repair |
|---|---|---|---|---|
| D1 | Medium | The ordering H2 over H1 is argued from a 6 percent AMPAR-weighted amplitude difference that the README elsewhere says carries no NMDAR information; the source's own significant mEPSC amplitude increase is reduced to "a sliver" | README section 1 item 1; section 2 "Synaptic currents" row | Replace "favour the second reading more than the first" with "do not separate the readings; the inhibitory deficit supports a disinhibition component, the mEPSC increase an AMPAR component"; keep E1 as the discriminator |
| D2 | Medium | F* predictions per reading are not derived, thresholds are undefined, a NAM ceiling makes F* undefined if bursts persist, and competitive block is agonist-surmountable during a burst | README section 3 table (H1 and H2 columns), section 7 E2; card text derived from it | State F* as exploratory, write numeric criteria before the run, add the NAM-ceiling case and the surmountability caveat |
| D3 | Medium | "Potency changes about 30- to 100-fold with a 20 mV change of holding potential" is used as fact. For a monovalent single-site pore block with electrical distance of at most 1, a 20 mV change should shift potency by at most about 2-fold; 33- and 107-fold imply an implausible apparent valence-distance product near 4-5. The values come from one 2024 medicinal-chemistry paper (closed, not opened by the producer or by me); the same README is sceptical of a 960-fold outlier from another single document but accepts this one | README section 1 item 2, section 4 memantine row, `arithmetic_p9.py` item (2) | Mark UNVERIFIED and possibly a protocol or transcription effect; do not cite as a property of the drug; the argument needs only the direction and the Mg2+ result |
| D4 | Medium | "The registered GRIN studies exclude memantine and perampanel as co-medication" is true of NCT05818943 and of the TSC/FCD study, not of NCT07224581, whose posted eligibility text has no such exclusion | README section 6 (GluN2B NAM row); card `p4_card/paediatrics_and_interactions` | Name the two studies, or write "two of the three registered studies" |
| D5 | Low-Medium | The 14/19 vs 3/15 figure is "improvement in any domain" (mainly behaviour); seizure reduction was not significant (7/18 vs 2/10, p = .417). It is used as precedent for gain-of-function selectivity of a seizure-relevant effect. The 32 vs 33 contrast omits the source's own age-at-onset explanation | README section 3 (H1 precedent), section 6; card "for" line 2 | Add the endpoint and the p value and the age caveat |
| D6 | Low | Head-injury trials: the later analysis found no significant mortality difference; "stopped ... with a mortality signal" (section 1 item 4) is correct for stroke day-30 only | README section 1 item 4, section 6 | Reword; keep the stroke figures |
| D7 | Low | "The same 119 bursts" for the main-text rate is an inference (the main text gives no n); the needs observation O7 states it as a fact, and states the experiment "recorded at 35 degrees C" in 1.3 mM Mg2+ although the recording perfusate is unstated (the limits field carries the caveat but the statement does not) | needs observation O7 in `proposed_edits.patch`; README section 2 | Soften the statement; a plausible reconciliation (rate from the median interval vs median of per-slice rates) deserves a sentence |
| D8 | Low | Rat PN12 (largest radiprodil seizure protection) is placed "at the start of the slice window" of mouse P13-17 without a species age mapping | README section 1 item 2 | State the species difference |
| D9 | Low | Reporting details: the sEPSC/sIPSC control group is wild type plus heterozygote; the 460 adults include healthy volunteers; NVP-AAM077 is also potent at rat GluN2C; eliprodil's duplicate-value pattern spans 14 rows, not 8; one TCN-201 row (100 nM) is explained as a review citation without being checked | README sections 2, 4, 5 | Minor wording edits |
| D10 | Info | Producer's harness defect note (`repurposing_coverage.py` line 267 evaluating `rows[fid]` before `row(fid)`) not re-tested here; not part of the scientific audit | README section 8 | None |

No unsupported number was found among the headline figures: every quoted value in Breton, ChEMBL, ClinicalTrials.gov, openFDA,
Karnstedt, Auvin, the selfotel abstracts and the arithmetic reproduced.

## 5. Limits of this verification

Opened in full or in the relevant passages: Breton 2021 (XML, supplement document, Figure 3 image), Karnstedt 2026, Auvin 2020,
Phillips 2026 (passages). Abstract level only: Kotermanski and Johnson 2009, Ikonomidou 1999, selfotel 1999-2000, Banke 2026, PMIDs
41288262 and 42837646. Not opened: Konecny 2024 (source of the voltage-pair values), the 2013 and 2007 documents behind the 0.95 nM and
911 nM rows, the Jahr-Stevens paper. Not tested: the release battery, the scratch trial of the proposed patch, the claim that the
secondary-source GluN2D interneuron localisation holds in mouse cortex at P13-17. The Figure 3 image was read by eye; no values were
extracted from it.
