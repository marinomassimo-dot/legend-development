# Blind audit, INV-18 (membrane physiology, HCN and alternatives) — verifier vf-18

Task record ORCH-IT38OS-20261108. Order kept: parts A and B were decided, and this file written in full, before `README.md`, `phase1_note.md` or `chains.tsv` were opened (a short post-read section at the end records what happened after). Files read before the verdicts: `verify/items.md`, `extraction.tsv`, `reconcile.tsv`, `evidence.tsv`, the complete original report `/home/desktop/legend-development/files/openscientist_retest_20261108/original_reports/INV-18_membrane.txt` (155 lines), plus the sibling files cited by `reconcile.tsv`. No gate, lint, test or delegation was run. PMIDs claimed under vf-18 before reading: 34634460, 34018186, 24953239, 20573906, 37982354. No page summariser (WebFetch) was used anywhere; every source below was reached as text through the PubMed/PMC tools or plain NCBI E-utilities and Europe PMC REST calls.

## Depth statement (what I actually read)

| PMID | Route | Depth |
|---|---|---|
| 34634460 (Breton 2021, Neurobiol Dis) | PubMed-tool PMC text (Results, Discussion, Methods 5.1-6.7) plus the held XML `files/fulltext/PMID34634460_Breton2021_PMC.xml` for Table 1 and the Fig 6 legend | full text; Table 1 and Fig 6 legend as text; figures not viewed; Table 1 recomputed by me |
| 34018186 (Iacone 2021, Epilepsia) | PubMed-tool PMC text of PMC9543052 | full text including figure legends; figures not viewed |
| 24953239 (Cain 2015, Pflugers Arch) | PubMed-tool PMC text of PMC4435665 | full text including Discussion; figures not viewed |
| 20573906 (Brandt 2010, J Neurosci) | PubMed record; PMC fetch returned an empty stub | abstract only (as the producer) |
| 37982354 (Mishra 2023 review) | NCBI efetch XML of PMC7616572 (tags stripped) | passages located by pattern (reversal potential, sag, rebound, interactions section), not a line-by-line read of the review |
| 31063701, 25760945, 28912545, 25071191, 39793889, 24871327, 41818135, 39548079, 29867437, 24403084, 32000863, 36271927, 25491415, 40953803, 36099307, 17074978, 17605039, 23055973 | PubMed records (efetch/metadata) | abstract only; 37732182 esummary only (identity) |
| 33547341, 22989944 | not re-read; I relied on the prior package rows and say so where it matters | none by me |

## A. Decisive propositions

Verdict table.

| ID | Verdict | One-line reason |
|---|---|---|
| D01 | PARTLY | ivabradine/sag DATO and the circularity of the H3 sag test hold; "sag is not an HCN-exclusive signal in the sources read" says more than the sources say (they call sag characteristic or the hallmark of HCN and never state exclusivity either way) |
| D02 | SUPPORTED (one class/wording correction) | Rin, genotypes, cell type, layer, age and the p-value hedge all verified; the framing "wrong as stated" and the class `superseded_or_contradicted` overstate, because the report's concern (sag not normalised for Rin) stands in substance |
| D03 | SUPPORTED | the -20 to -30 mV figure is in 37982354 only among the sources read; report's value is uncited |
| D04 | SUPPORTED | authors' own reading verified; one counter-instance the item does not use (see D04) |
| D05 | SUPPORTED | model, layer, age, slice counts verified |
| D06 | SUPPORTED (strengthen) | the source locates the strongest effect in neocortex, so "thalamocortical, not neocortical" is partly reversed, not only narrower |
| D07 | SUPPORTED (abstract only) | |
| D08 | SUPPORTED (abstract only) | one descriptor ("heterologous") is not in the 28912545 abstract |
| D09 | SUPPORTED (abstract only) | |
| D10 | SUPPORTED as scoped (abstract only) | "lithium acts in wild type too" is background knowledge, not in a source I read |
| D11 | SUPPORTED | chain verified link by link at abstract level; absence claim re-run by me (see D11) |
| D12 | SUPPORTED (abstract only) | |
| D13 | SUPPORTED | |
| D14 | SUPPORTED | |

Counts: 13 SUPPORTED (of which D02, D06, D08, D10 carry a correction or caveat below), 1 PARTLY (D01), 0 NOT SUPPORTED, 0 UNVERIFIABLE. Sub-parts I could not check myself: 33547341 (TTX-activity-deprivation reading, D04) and 22989944 (ZD7288 sodium current, D06).

### D01 — PARTLY

Report lines checked: L10 ("sag is the specific biophysical fingerprint of Ih"), L32 ("sag is HCN-specific"), L61 and L149 (H3 test), L94, L102.

What the sources say, quoted or located:
- DATO, 40953803 abstract (PubMed record): "The main underlying hallmark of this conductance was the presence of sag". The same abstract continues "the presence of sag - activation of HCN channels", so the review ties sag to HCN activation. It never says "only HCN" or "specific".
- DATO, 37982354 (Mishra), section "Dynamic viewpoint: sag, rebound, and temporal summation": "sag and rebound are characteristic features for the expression of HCN channels", with the explanation that sag arises from HCN deactivation/activation kinetics set against the membrane time constant. Section "Interactions viewpoint": "interactions with other ion channels that co-express with HCN channels can also modulate the ability of neurons to manifest sag or rebound". The review's other relevant sentence is the converse of the report's claim: absence of sag "should not be construed as evidence for the absence of HCN channels". Neither sentence says that a non-HCN conductance can generate sag by itself.
- DATO, 34018186 (read): the authors call the ivabradine-blocked sag an "HCN channel-dependent" membrane property in Wistar cortical layer 5/6 pyramidal neurons; text says ivabradine "blocked the characteristic depolarizing sag", the Fig 5 legend says "decreased the depolarizing sag ... significant for the largest injected currents" (text 3 µmol/L, legend 30 µmol/L).
- DATO, 24953239 (read): the "Ih-mediated depolarizing sag" wording is used; ZD7288 is the Ih tool there.
- DATO, 34634460 Discussion 3.5 (read): the authors cite a neocortical study in which ZD7288 "eliminated sag voltage" and also "increased input resistance"; that source was not retrieved by anyone here.

So: no source read establishes exclusivity, and none refutes it. The producer's INFERENZA "sag is not an HCN-exclusive signal in the sources read" is therefore an over-reading in its first clause. What the sources do support is (i) sag/rebound amplitude depends on the interaction of HCN kinetics with the membrane time constant and on co-expressed channels, (ii) "HCN-specific" in the report is a premise, not a finding of any cited paper. Background knowledge that is not in a source I read (IPOTESI, unverified by me): deactivation of an M-type/Kv7 current can contribute a sag-like relaxation in some neurons; I mention it only so the producer does not assume this is settled in either direction.

The H3 test (report L61/L149; table L102) is circular as the item says: the report's own table (L102) gives "No" for sag after Kv7 opener plus T-type blocker under H1/H2 and also "No (sag is HCN-specific)" under H3, so that row cannot discriminate, and the stated rejection of H3 "if the combination fails to abolish the sag" is met by construction. DATO for ivabradine/sag: SUPPORTED.

Required wording fix (items.md D01 first clause and any copy in decisive.tsv/README): replace "sag is not an HCN-exclusive signal in the sources read" by "no source read establishes that sag is HCN-exclusive; 40953803 calls it the hallmark and 37982354 calls it characteristic and modulated by co-expressed channels; exclusivity is the report's premise".

### D02 — SUPPORTED (Table 1 and Methods read; one wording/class correction)

Primary source read: 34634460, Table 1 (held XML), Methods 5.1, 6.6, 6.7, Fig 6 legend.

- Genotypes: S-WT, S-HT, S-KO, Synapsin-Cre neuron-specific Wwox deletion (Methods 5.1). Cell type: putative pyramidal neurons ("PY") of the superficial neocortex, layer II/III (Fig 6 title "layers II/III"; Methods 6.6 "layer II/III neurons"). Age: "P13 to P17" (Methods 5.1). Preparation: acute coronal slices 400-500 µm, 35 °C (Methods 5.2-5.3).
- Table 1, pyramidal: input resistance 102.88 ± 11.74 (WT), 143.26 ± 15.49* (HT), 143.03 ± 8.88* (KO) MOhm; ratio 1.39 in both mutants (about 40 percent higher, checked). N cells/animals 13/5, 15/6, 40/15. Methods 6.6: "Input resistance was measured by the slope of the computed I-V plot" (current range not given). RMP -79.25, -75.51*, -73.62*; sag at -200 pA 1.18, 2.04*, 2.57*; rebound 0.96, 1.24, 1.86*; tau 18.55, 18.79, 21.25 ms. Asterisks are versus S-WT only; HT versus KO is never tested. Table 1 does not state whether "±" is SD or SEM; the Fig 6B legend says "average ± SEM for all animals tested". Methods 6.7 names an unpaired t-test and a Bonferroni correction "for tests of multiple comparisons" without saying where it was applied.
- Arithmetic: -200 pA x 102.88 / 143.26 / 143.03 MOhm = 20.6 / 28.7 / 28.6 mV (item's "about 20.6 v 28.7" is right). Sag fraction on deflection plus sag: 5.4 / 6.6 / 8.2 percent. Proportional scaling of the WT sag to the larger deflection gives 1.64 mV, i.e. 53 percent (HT) and 33 percent (KO) of the sag rise reproduced by the larger step alone (INFERENZA; assumes sag proportional to deflection, which is itself only roughly true because a more negative excursion also recruits more Ih). Source-based point (not only the prior package): the review the producer read, 37982354, section "The resting viewpoint: conductance-current balance and input resistance", states that open HCN channels depolarise RMP and also reduce Rin (a higher conductance at rest). Wwox pyramidal neurons show RMP depolarised and Rin raised by about 40 percent, which is the pattern of fewer open conductances, not of more open HCN, unless another conductance fell as well (INFERENZA; this bears on the report's "one rise in a conductance" economy at L10/L18 and the report does not address it). The unchanged tau with higher Rin implies lower capacitance (about 180, 131, 149 pF; crude group means), another point against reading Rin as a pure HCN effect (INFERENZA).
- Statistics, my own recomputation (python, scratchpad `tt.py`; not a gate): assuming "±" is SEM, n = cells, two-sided Welch t-test versus WT:
  - Rin: HT 0.048, KO 0.011 (Student 0.053 and 0.022).
  - RMP: HT 0.18 (printed: asterisk), KO 0.028.
  - Sag: HT 0.10 (legend prints 0.04761), KO 0.006 (legend prints 0.00322; Student pooled gives 0.07).
  - Rebound: HT 0.65 (legend prints 0.24947), KO 0.066 (legend prints 0.00393; Student 0.26).
  - With n = animals the same ones fail (sag HT 0.13, rebound KO 0.077, RMP HT 0.20).
  This matches the earlier package's `ephys_claims.tsv` E09 numbers (independent reproduction). The producer's three contrasts (sag in HT, rebound in KO, RMP in HT) are therefore correct under the stated assumptions. The wording in items.md ("not reproducible under assumed Welch/SEM; this is not a contradiction of the paper") and in reconcile.tsv row E01,E02 meets the operator rule: it says not reproducible under assumptions and nothing stronger. Two precision points: (a) there is no printed p for RMP in HT, only a Table asterisk, so say "printed p values and asterisks"; (b) the two sag p values in the Fig 6B legend (0.04761; 0.00322) are not labelled by comparison; assigning them to HT and KO is the producer's reading of their order. Neither point weakens the hedge. I assert no contradiction of the paper: the analysis unit, the test (Welch or Student) and the meaning of "±" are not declared.
- The classification problem: report L141 reads "no input-resistance control (apparent sag depends on R_in)". Rin is measured and shown, so a reading "no Rin measurement" is wrong; but the parenthesis shows the report means that the sag comparison was not controlled or normalised for Rin, and that is true in the paper (the same -200 pA step was applied to cells with 40 percent higher Rin; sag is reported as absolute mV). The item's own INFERENZA says exactly this. Calling the report's premise "wrong as stated" and filing it as `superseded_or_contradicted` (reconcile.tsv row E46) therefore overstates; `verified_or_corrected` with the text "Rin is measured and 40 percent higher in both mutants, which the report missed; the report's concern that sag was not normalised for Rin stands" is the accurate description. The previous package's BRIEF section 2 ("Input resistance is measured: do not treat it as absent") agrees with the narrower reading.

### D03 — SUPPORTED

37982354, section "HCN proteins: structure and its relationship to their unique channel physiology" (efetch XML): "setting their reversal potential ... to be unique at around -20 to -30 mV", with permeability Na:K about 1:4. DATO. Among the sources I read (34634460, 34018186, 24953239, 37982354 and the abstracts) this is the only Ih reversal value; the report's L10/L18 "near -30 mV" is uncited. Caution for the producer: 34634460 Results 2.2 contains a different "-31 ± 9.5 mV", which is the reversal potential of the burst currents measured in voltage clamp, not Ih; the two must not be conflated. In 24953239 the Ih V1/2 of activation is -86 mV in thalamic neurons (Results), so "partly open at the Wwox resting potential of -74 to -79 mV" is plausible but unmeasured in Wwox cells, as the item says. A general Ih reversal range in the textbook literature is background knowledge I did not retrieve.

### D04 — SUPPORTED

24953239 read in full text. Verified: Ih density increased in P15-P20 and adult GAERS VB neurons; HCN1 and HCN3 protein higher; ZD7288 normalised the burst threshold; Discussion: "any apparent compensation is unlikely to be directly related to the development of SWDs"; Summary: the suppressed bursting "does not occur as an adaptive response to SWDs"; "may act to increase the frequency of slow membrane oscillations". The authors write that suppressed bursting "would be expected to reduce absence seizures" yet 100 percent of adults seize, and they hypothesise (not show) that VB bursting suppression "underlies why they do not burst-fire during SWDs". No seizure measurement exists in the paper. So "restraining of seizures" (report L12/L29/L41) is the report's reading, not a finding. The report's quote of the abstract is verbatim.

One fact the item does not use and the producer should add: in GAERS VB neurons the increased Ih came with a lower input resistance, an unchanged resting potential and an unchanged Ih-mediated sag ("sag ... not significantly different"), and ZD7288 hyperpolarised the cells and also lowered Rin, which the authors call "unexpected". That is the best-documented increase of Ih in the report's own evidence set and it did not reproduce the report's triad (depolarised RMP, larger sag, with Rin up in Wwox). It also supports the producer's point in reconcile row E03 that open HCN should lower Rin. Class and species: rat, thalamic relay population, genetic absence model.
"Multiple models" (report L144): only GAERS (read) and CaV3.3 knockout (25071191 abstract: "Contrary to expectations, there was an increased susceptibility to drug-induced SWDs", thalamic reticular neurons), both thalamic; the 33547341 element is TTX-deprived hippocampal cultures (prior package rows E29/E31/E37; not re-read by me). Anchor note: L50 in the item's anchor list is the H2 lipid counter-paragraph and does not concern GAERS.

### D05 — SUPPORTED

34634460 Results 2.1: bursting "0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice"; LFP recorded from slices, whole-cell recordings are separate and the paper does not say the patched cells came from bursting slices. Hippocampal slices showed no bursts. The report's "neuronal cultures — the same preparation class as the Wwox model" (L20) is wrong: acute slices (Methods 5.2). "Wwox-KO" omits that deletion is neuron-specific (Synapsin-Cre). Also the HT group departs from WT in Rin, RMP and sag in Table 1, so "WT/het controls" (report L18) merges a group that shows part of the phenotype; the abstract itself pools them as controls.

### D06 — SUPPORTED, strengthen

34018186, full text. Verified: oral ivabradine (visible reduction at 20 and 30, not 10 mg/kg; AUC significant at 30 mg/kg only, 62 percent less time in seizure, 20 mg/kg p = .07) reduced absence seizures in GAERS only with intravenous elacridar; without elacridar no effect; brain ivabradine 9.5 versus 373 ng/g with and without elacridar (Results 3.1). Elacridar is a P-glycoprotein inhibitor and was inert alone (ELA + vehicle 1.2 ± 0.16 of control). Cortical initiation network (CIN, somatosensory cortex) injection of ivabradine (6 nmol) cut seizure time by 96 percent; VB thalamus injection by 40 percent (Results 3.2). In slices: Wistar cortical layer 5/6 pyramidal neurons (rats 25-35 days old) lost the depolarizing sag with ivabradine and hyperpolarised; GAERS VB thalamocortical neurons likewise (Fig 5 legend: sag decrease "significant for the largest injected currents").
Consequences: (1) The report's "thalamocortical ... not neocortical" efficacy contrast (L26, L139) is contradicted at the site-of-injection level: the largest effect came from injection into a neocortical region. The report's underlying point (a different disease mechanism) may stand, but the sentence as written does not follow from the paper. (2) The cortical sag/RMP data are from normal Wistar rats, not GAERS and not mouse layer II/III. (3) Ivabradine is a compound-level result in a rat absence model; the authors call it a nonselective HCN-isoform inhibitor; no Wwox slice or animal has seen any HCN blocker. (4) Dose discrepancy in the source (3 µmol/L in text, 30 µmol/L in legend) is reported neutrally; no dose preference is drawn. 22989944 not re-read by me.

### D07 — SUPPORTED (abstract only)

31063701 abstract: Kv7.2/7.3 in HEK293 with EC50 9.8 ± 0.4 nM, about 100-fold more potent than retigabine; "also activates the native M-current in rat hippocampal or cortical neurons, causing marked hyperpolarization"; maximal electroshock inhibition after i.p. or intragastric dosing. The abstract names no species for the electroshock model (evidence.tsv V15 says "mouse and rat"). It is a preclinical compound; the report's "validated anti-epileptic strategies" (L32) holds for retigabine as a class but not for SCR2682, which has a single characterisation paper. The INFERENZA (Kv7 opening moves RMP whatever the cause; no Kv7 datum in a WWOX preparation) is correct and consistent with the module. Anchor note: L35 in the item's anchors is the GSK3 paragraph, not Kv7.

### D08 — SUPPORTED (abstract only)

25760945 abstract: Cdk5 regulates native T-type currents in N1E-115 neuroblastoma cells and recombinant Cav3.1 in HEK-293; the rebound phrase is a background sentence. 28912545: GAERS Cacna1h missense variant, calnexin-dependent trafficking of Cav3.2 (the abstract does not name the expression system, so "heterologous" in the item is not abstract-verifiable). 25071191 abstract: TRN neurons from CaV3.3 knockout have rhythmic burst discharges "completely abolished", "tonic firing was significantly increased", and drug-induced SWD susceptibility is increased; the title says rebound burst firing in the reticular thalamus "is not essential" for pharmacological absence seizures; note the abstract also reports enhanced inhibitory drive in TC neurons and increased tonic firing, so "rebound is protective" is not what it shows. None of the three tests T-type current in cortex. TTA-P2 has no source in the report (L61, L149): confirmed. The module's T-type README (line 11) says Z944, ML218 and TTA-P2 share a scaffold: confirmed.

### D09 — SUPPORTED (abstract only; PMC stub)

20573906 abstract: adult female rats, pilocarpine status epilepticus, prolonged bumetanide after SE; "Bumetanide did not exert any significant effects on development of spontaneous seizures"; PK: "extremely rapid elimination and low brain penetration of this drug in rats"; combined bumetanide plus phenobarbital "counteracted several of the behavioral consequences of SE"; the authors conclude the data "do not indicate that bumetanide can prevent epilepsy after SE" and call for lipophilic prodrugs. It does not test the NKCC1/KCC2 gradient in immature or Wwox tissue, nor neuronal RMP. The report cites this paper at L59 for both "failure" and "poor brain penetration", so `extraction.tsv` row E25 note "Poor-penetration statement uncited" is wrong (see corrections). The item's reading, that the chloride arm remains unexamined (absence of evidence, and a pharmacokinetically limited null), is right. The behavioural effect of the combination is a point the report omits when it says bumetanide "failed"; worth one clause.

### D10 — SUPPORTED as scoped (abstract only)

32000863 abstract: "significantly increased activation of GSK3β occurs in Wwox-/- mouse cerebral cortex, hippocampus and cerebellum"; "Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced seizure in Wwox-/- mice" (report quote verbatim). 39793889 abstract: the axin-binding domain of GSK3β for Nav1.6 complex formation in HEK293 and a CA1 AAV construct that reduced maximal firing; nothing about HCN, Kv7, Cav3, sag, RMP or rebound. The absence claim holds within the perimeter of the sources read. CHIR99021 isoform non-selectivity: `gsk3_inv09_20261107/output/evidence.tsv` E16 confirms it; tideglusib has no source in the report. "Lithium acts in wild type too" is general knowledge, not in an abstract I read; label it background.

### D11 — SUPPORTED

Chain verified at abstract level: 24871327 ("Wwox(-/-), but not Wwox(hep-/-) ... marked reductions in serum HDL cholesterol"; also a sex-specific female hep-/- triglyceride effect); 39548079 (Nat Commun 2024, rat DRG nociceptors; "Disruption of OMDs potentiated action potential firing ... facilitated the opening of native" HCN channels; cholesterol supplementation inhibits HCN; OMD size "depends on specific cell types"); the direction matters: low membrane cholesterol raises HCN opening, but nothing shows neuronal membrane cholesterol is lower in Wwox neurons, and serum HDL is a different compartment. PIP2: 17074978 (oocytes, patches, sinoatrial cells), 17605039 (oocytes with PLC-coupled receptors), 23055973 (review). Absence claim "no brain or neuronal membrane cholesterol or PIP2 in Wwox-deficient neurons": re-run by me on 2026-11-08 by two routes. PubMed: `WWOX AND (HCN OR hyperpolarization-activated OR Ih OR HCN1)` gave 2 hits, both Turkish epilepsy-genetics cohorts (41510857, 41153369; gene-list mentions); `WWOX AND (filamin OR TRIP8b OR PEX5L)` 0; `WWOX AND (Kv7 ... bumetanide OR NKCC1 OR KCC2)` 0. Europe PMC REST (full-text fuzzy): 65, 30 and 21 hits; I screened the first 10 titles of each (cohorts, reviews, unrelated) and found no WWOX-HCN, WWOX-filamin or WWOX-lipid-domain paper. Perimeter: titles of the first 10 hits per Europe PMC query, all hits of the PubMed queries; not an exhaustive read of the 116 Europe PMC records.

### D12 — SUPPORTED (abstract only)

29867437 abstract: pyramidal Ih "significantly increases from juvenile to adolescence"; PV+ interneuron Ih "decreases from juvenile to adolescence". Mouse prefrontal cortex, Ih amplitude measured; no drug effect measured. The abstract does not give ages in days, so I cannot say whether P13-17 precedes the "juvenile" window; the report's extrapolation to "a global HCN blocker acts oppositely" (L29) is not in the paper. The held Wwox interneurons are 5 and 6 cells, not PV-identified (pv_inv15 README line 12, confirmed).

### D13 — SUPPORTED

24403084 abstract: FLNa-dependent dynamin internalisation of HCN1 in HEK293; a truncated dominant-negative FLNa raises native HCN1 in hippocampal neurons; decoy peptides "augment endogenous Ih" and enhance "the rebound-response ('voltage-sag')". The abstract names no species; the prior package rows E23-E28 say rat neurons. The no-link absence claim re-run above (filamin/TRIP8b/PEX5L, 0 PubMed hits). Nested-explanations point (lipid, scaffold, homeostatic routes are not independent): agreed (INFERENZA).

### D14 — SUPPORTED

36271927 (J Mol Med, review, "systematically ... presenting the current state of knowledge"), 25491415 (Exp Biol Med, review), 40953803 (Prog Biophys Mol Biol, review), 23055973 (Front Pharmacol, review), 41818135 (J Gen Physiol, authors Handlin, Gieré, Dumaire, Salih, Moutal, Dai: same laboratory as 39548079), 37732182 (bioRxiv preprint with the same title and authors as 39548079): all verified in PubMed records. The report's "corroborated by" (L23) counts reviews and one same-origin reuse as confirmations. One nuance for the producer: the 40953803 abstract equates sag with HCN activation, which is stronger than "hallmark", see D01.

### Point (7): depth statements and the 14 abstract-level views

The 14 views without receipts are exactly rows V14-V27 of `evidence.tsv` (25071191, 31063701, 25760945, 28912545, 29867437, 40953803, 24871327, 41818135, 17074978, 17605039, 23055973, 39793889, 36271927, 25491415). I verified all 14 locator quotes verbatim against the PubMed records (V15 with the species caveat above). The depth label `abstract_only` is honest for each; none of them is described as a read in `evidence.tsv`. The reading claims ledger (`/home/desktop/legend-development/.git/legend-reading-claims/`) shows os-18 claims only for the five receipted PMIDs (claim times 21:06 on 2026-11-08, the same minutes as the receipts); no os-18 claim exists for the 14, and 25071191 is claimed by os-03/vf-03 in a sibling package with the same abstract-only depth. This causes no content error, but the 14 were read without the protocol's claim step, and the conclusions that rest on them (D07, D08, D10-D12, D14) are abstract-level conditional leads. The five receipted views: 37982354 (partial, pattern search; my own check of its two quoted passages found both verbatim), 34018186 and 24953239 (the producer's "partial_fulltext" is conservative; I read both completely as text), 36099307 (abstract verified; the model-only status is correctly stated), 20573906 (abstract only, honest).

## B. Coverage audit (12 points chosen from the whole report)

Result: 12 of 12 PRESENT, 0 PRESENT_NARROWED, 0 MISSING. No extension scan was therefore triggered; I nevertheless compared every remaining report line with `extraction.tsv` and found no further miss.

| # | Report point (line) | Extraction row | Verdict |
|---|---|---|---|
| 1 | dendritic Ih block can raise excitability through temporal summation, uncited (L26, L41) | E10 | PRESENT |
| 2 | SCR2682 named in passing next to retigabine (L32, L123) | E23 | PRESENT |
| 3 | TTA-P2 as the T-type blocker in the H3 probe, no source (L61, L149) | E35 | PRESENT |
| 4 | CHIR99021 and tideglusib named without citation (L35, L153) | E32 | PRESENT |
| 5 | brain cholesterol locally synthesised; myelination competes for lipid flux and is WWOX-impaired, uncited (L50) | E18 | PRESENT |
| 6 | OMD size cell-type-specific (37732182) and immature NKCC1>KCC2 as a table constraint (L98) | E19, E59 | PRESENT |
| 7 | discriminating table row 3, "Partial/No" for the HCN account when the Kv7 + T-type combination normalises RMP/rebound (L103) | E58 | PRESENT |
| 8 | replication in WWOX-deleted human cortical organoids or iPSC neurons; "qualitative electrophysiology" (L141) | E47, E46 | PRESENT |
| 9 | intracellular ZD7288 (or ivabradine) as the H1 probe (L45) | E33, E38 | PRESENT |
| 10 | reverse inference "elevated HCN protein with unchanged V1/2 ... favors H1" (L150) | E39 (note) | PRESENT |
| 11 | diagram arrow "of Nav / (?)HCN / Kv7" (L72) | E57 | PRESENT |
| 12 | elacridar and P-glycoprotein inhibition named in passing (L26, L122) | E34 | PRESENT |

Every caveat paragraph also maps: L141 single study/no Ih I-V/no isoform/no Rin (E46), L142 cross-system (E49), L143 direct link inferential (E48), L144 directionality (E50), L145 cell-type and window (E11, E12), L146 tractability (E37): 6 of 6 present. Counter-arguments (L137-L139 "Refuted" list, E51) and side remarks ("View full report" interface text, E55; "partly an artifact", E56) present. Extraction notes that add value: E41 (circular H3 rejection logic), E50 ("multiple models"), E07 (culture-class wording). Accuracy defect found in the extraction: E25 note says the poor-penetration statement is uncited, but L59 cites 20573906 for it.

## C. Reconciliation sample (8 rows)

Class counts: `reconcile.tsv` has exactly 2 rows with `legend_class` = new_to_legend (E15; E24,E25,E59), 1 superseded_or_contradicted (E46), so I used the minimum available and, for the third new_to_legend slot, a row whose `legend_novelty` is new_to_legend (E10, class verified_or_corrected). Prior-brief checks use `hcn_20261107/BRIEF.md` (the INV-18 predecessor; `git grep -l INV-18` also lists the it36 decisive-rechecks and it34/it35 packages, which do not carry a brief for this question).

| Row | Class | Pointer check | Result |
|---|---|---|---|
| E15 | new_to_legend | `hcn_20261107` cites no PIP2 source; its `queries.tsv` Q02/Q09 search WWOX with PIP2 and find no bridge | OK. The row could say that the PIP2 bridge was searched, not only that no source is cited; PIP2 abstracts verified (D11) |
| E24,E25,E59 | new_to_legend | `hcn_20261107/BRIEF.md`, README and hypotheses.tsv: 0 mentions of chloride, NKCC1, KCC2 or bumetanide; abstract content as stated | OK; `prior_brief_fate` "omitted (no chloride arm)" confirmed. Add the phenobarbital-combination behavioural effect to the note |
| E10 | (class verified_or_corrected, novelty new_to_legend) | no earlier consumer (BRIEF section 5 only warns on opposite trajectories); 36099307 abstract says Ih facilitates proximal and hinders distal drive in a layer V model | OK, but understated: the producer's own source 37982354 states that HCN channels suppress temporal summation (Fig 2 title and text), which is the direct basis for the report's "enhancing temporal summation"; the row says "supported only by a computational model" |
| E01,E02 | already_present_and_used | `needs/needs.json` NEED-INTRINSIC-EXCITABILITY O1-O4 exist (O1 gives the same Table 1 values, age P13-P17, Synapsin-Cre); `hcn_20261107/output/physiology.tsv` and `pv_inv15_20261107/output/currents.tsv` exist | OK. The p-value hedge wording in this row is correct (see A, D02). Side note: need O1 says RMP and sag "grade with gene dose"; HT versus KO is never tested in the paper, as physiology.tsv itself states, so "grade" is descriptive only |
| E33,E38 | already_present_and_used | `hcn_20261107/output/probes.tsv` P01 (ZD7288, 22989944 sodium-current datum), `experiment.tsv` X4-X5, `investigations_it20.tsv` INV-18 "at least two chemotypes" exist | OK; prior fate "modified" matches BRIEF section 5 (ZD7288 off-target; intracellular application does not test network block) |
| E09 | present_not_used | receipts FTR-20261021-24953239-01 (partial) and FTR-20261022-24953239-02 (complete read) exist in `registries/fulltext_read_receipts.jsonl`; `hcn_20261107` does not cite 24953239 | OK; authors' reading verified (D04). Add the counter-instance (Rin down, RMP and sag unchanged) |
| E22,E41,E35,E58 | present_not_used | `ttype_20261107/output/README.md` line 11 holds "Z944, ML218 and TTA-P2 share a scaffo[ld]"; Kv7 lead and `hcn_20261107` hypotheses.tsv HY2 exist; BRIEF section 5 says keep Kv7 and T-type arms separate and add a combination only for a new question | OK |
| E46 | superseded_or_contradicted | BRIEF section 2 "Input resistance is measured: do not treat it as absent"; physiology.tsv Y01 Rin values; Methods 6.6 I-V slope | pointers correct; class overstated (see D02) |

`prior_brief_fate` checked against the BRIEF for 8 rows (E46, E24 group, E10, E01 group, E33 group, E09, E22 group, E34): all match the BRIEF text. One location slip: for row E06,E08,E50,E51,E53 (not in my 8) the phrase "harmful, compensatory or mixed" is in BRIEF's Goal, not section 3. Row E26,E27 says 25071191 is mentioned "only in" `research/repurposing_10h_scientist-b_20261021.md`; `git grep` also lists `deepdive_manifests/PMID35243344.json` and the scientist-b ledger task record, which I did not open; low-impact.

## D. Evidence sample

`evidence.tsv` has no row for 34634460 (Table 1, Methods 5.1, 6.6, Fig 6 legend), the source behind D02 and D05, or for 24403084, 33547341 and 32000863. Those propositions are therefore not traceable to a locator quote inside this package's evidence file (they may sit in `decisive.tsv`, which I did not use). Rows checked against the source texts or PubMed records:

| Row | Backs | Verbatim? | Carries the proposition? |
|---|---|---|---|
| V01 | D03 | yes (elision marked); the TSV holds the literal sequence `−` instead of the minus sign | yes; section is "HCN proteins: structure and ... unique channel physiology" (field says "section number not recorded") |
| V02 | D01 | yes ("... absence of HCN channels") | no for "not exclusive": it is the converse (absence of sag does not exclude HCN); the source continues "(or other resonating conductances)", which refers to resonance |
| V03 | D01 | yes | partly: it shows modulation of sag/rebound by co-expressed channels, not generation by non-HCN channels |
| V04 | D01, D06 | yes, but the unit is garbled (`µmol·L –1`; source "µmol·L" with a lost superscript); Fig 5 legend says 30 µmol/L, flagged in the row | yes |
| V05, V06, V07 | D06 | yes (V05 abstract; V06 abstract; V07 Results 3.3) | yes |
| V08, V09, V10 | D04 | yes (Discussion, abstract, Discussion) | yes; V10 correctly labelled "counter" and as the authors' own speculation |
| V11 | D04 | yes (abstract, spacing "I h" is an extraction artefact) | context only, as labelled |
| V12, V13 | D09 | yes (abstract) | yes |
| V14 | D04, D08 | yes | yes |
| V15 | D07 | yes | quote yes; species field "mouse and rat seizure model" is not in the abstract |
| V16, V17 | D08 | yes | context only; V17 field "heterologous expression" not in the abstract |
| V18 | D12 | yes | yes |
| V19 | D01, D14 | yes | hallmark yes; the same abstract's "presence of sag - activation of HCN channels" is the stronger link and is not recorded |
| V20 | D11 | yes | yes (serum, not brain) |
| V21, V22, V23, V24 | D11 | yes | yes; V23 is a PLC/receptor oocyte paper, role "context" correct |
| V25 | D10 | yes | yes |
| V26, V27 | D11, D14 | yes | yes (reviews) |

No quote exceeds 25 words. No fabricated quote found.

## Corrections the producer must make

1. `verify/items.md` D01 statement, first clause, and any copy in `decisive.tsv`/`README.md`: replace "sag is not an HCN-exclusive signal in the sources read" with "no source read establishes that sag is HCN-exclusive; 40953803 calls it the hallmark of the conductance and 37982354 calls it characteristic and modulated by co-expressed channels; exclusivity is the report's premise".
2. `reconcile.tsv` row `E46`: change `legend_class` from superseded_or_contradicted to verified_or_corrected, and `note` to: "Rin is measured (102.88 / 143.26 / 143.03 MOhm) and about 40 percent higher in both mutants, which the report missed; sag was not normalised to deflection or compared at matched potential, so the report's Rin concern stands in substance". Same softening in item D02 ("wrong as stated").
3. `verify/items.md` D02 and `reconcile.tsv` rows E01,E02/E46: write "printed p values and asterisks" and add that the two sag p values in the Fig 6B legend are not labelled by comparison; keep "not reproducible under assumed Welch/SEM" and "not a contradiction of the paper".
4. `extraction.tsv` row `E25`, note column: delete "Poor-penetration statement uncited"; L59 cites 20573906 for it.
5. `verify/items.md` D06: add that the CIN is somatosensory cortex and ivabradine injection there reduced seizure time by 96 percent versus 40 percent in VB, so the report's "thalamocortical, not neocortical" contrast is contradicted at the injection site; cortical slices are normal Wistar rats aged 25-35 days; text 3 µmol/L versus legend 30 µmol/L.
6. `reconcile.tsv` row `E09`, note: add that in GAERS VB the increased Ih came with lower Rin, unchanged RMP and unchanged sag, and that ZD7288 lowered Rin ("unexpected" in the authors' words).
7. `reconcile.tsv` row `E10`, note: the same review (37982354) states that HCN suppresses temporal summation; "supported only by a computational model" understates the available support, which remains an INFERENZA for Wwox.
8. `evidence.tsv` rows `V01`, `V04`: replace the literal `−`, `·` escape sequences by the characters; V04 unit should read "3 µmol·L(-1)" or the plain sentence without the unit fragment. Row `V15` species: "maximal electroshock model; species not stated in abstract". Row `V17` system: "expression system not stated in abstract". Row `V19`: add the sentence "the presence of sag - activation of HCN channels" to the note.
9. `evidence.tsv`: add rows for 34634460 (Table 1 Rin/sag/RMP/rebound with N; Methods 5.1 "aged P13 to P17"; Methods 6.6 Rin from the I-V slope; Fig 6B legend "average ± SEM for all animals tested"; Results 2.1 slice counts) so D02 and D05 are traceable inside the package.
10. `verify/items.md` anchors: D04 lists L50 (H2 lipid counter-paragraph, not GAERS) and D07 lists L35 (GSK3 paragraph, not Kv7); drop them.
11. `verify/items.md` D10: mark "lithium acts in wild type too" as background knowledge.
12. Record in the README that no os-18 reading claim exists for the 14 abstract-level PMIDs.

## Open uncertainties

- Table 1's "±" is undeclared; every statement about reproducibility of p values is conditional on SEM, cell-level n and a Welch or Student unpaired t-test. Student's version fails more contrasts (sag in KO, 0.07; Rin in HT, 0.053) than Welch's, so the list of "not reproducible" contrasts depends on the test assumed; the three named by the producer are the ones that fail under every variant I tried (cells or animals, Welch or Student).
- The Fig 6 panels were not viewed (legend text only). Whether the bar charts plot cells or animals is unknown ("for all animals tested").
- 20573906 and 11 other sources are abstract-level for me too; 33547341 and 22989944 were not re-read.
- The statement that other conductances can produce sag-like relaxations rests on my background knowledge, not on a retrieved source; I did not test it.
- The Europe PMC absence search was screened by titles of the first 10 hits per query only.

## Post-read note (README.md, phase1_note.md, chains.tsv and, for wording only, decisive.tsv/queries.tsv/receipts INDEX opened after everything above was written)

No verdict in parts A or B changed. The three narrative files agree with the items on every point I had checked independently. Differences and additions:

1. `README.md` "Answer first" bullet 1 and section d bullet 1 say the report's premise "no input-resistance control" is "wrong" and "contradicted by Table 1". This is the over-statement flagged under D02: Rin is measured, but no matched-deflection or normalised sag comparison exists in the paper, which is the substance of the report's parenthesis. Reword as in correction 2. The README's own section d continuation ("Missing instead: matched-potential comparison, Ih in voltage clamp, isoform quantification") already says it correctly.
2. `README.md` section i says the 14 abstract-level sources were read without receipts and then "Reading claims were made after opening the texts (late); stated in queries.tsv Q10". Q10 records claims for the five receipted PMIDs only. The claim ledger holds no os-18 claim for any of the 14, so the sentence should say "no claim was made for the 14". I weigh this as a process gap with no content consequence (the 14 carry `abstract_only` throughout and every quote verified).
3. `README.md` section a/b counts (class and fate totals) recomputed from `reconcile.tsv`: already_present_and_used 23, verified_or_corrected 16, present_not_used 12, new_to_legend 4 items (2 rows), unverified 3, superseded_or_contradicted 1 = 59; fate kept 11, modified 20, narrowed 17, omitted 11 = 59. All correct.
4. `README.md` section g: "ivabradine ... new_to_legend at source level" is consistent with my `git grep` (no consumer of 34018186 outside this package).
5. `chains.tsv` C06, `context` column: "Rat/mouse absence model" for the ivabradine chain; 34018186 is rat only (GAERS and Wistar). Replace by "rat absence model (GAERS); cortical slices from normal Wistar rats".
6. `chains.tsv` C01 favourable reason "sag is HCN-specific" is the report's premise; add "(report premise; not established by a cited source)" to avoid a reader taking it as a finding.
7. `phase1_note.md` states the report has 154 lines; my reader count is 155 lines (the Bottom Line text is line 155). Anchors to L155 in `extraction.tsv` show the last line was read; the count is a counting convention only.
8. `decisive.tsv` D01/D02 carry the same wording as `items.md`; corrections 1-3 apply there as well.
