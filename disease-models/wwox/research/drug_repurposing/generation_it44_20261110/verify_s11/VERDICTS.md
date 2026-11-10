# IT44 S11 independent reader: VERDICTS

Reader: sonnet, high effort, one delegate, no sub-delegation. Date 2026-11-10. Zero spend. No e-mail or contact
detail was sent, searched for or stored. Not medical advice.
Method: PubMed search and metadata (abstracts), PMC full text through a summarising fetch tool, and the public
ChEMBL REST activity endpoint. I did not read `s11/`, `pointers_it44.tsv`, `summary_it44.tsv`,
`entity_roles_it44.tsv`, `relation_s11_frame_it44.md` or any search_rows/molecules/verdict file.
Tool-call count: about 71 (approximate; counted from the transcript, before this Write).
Caveat on quotes: PMC pages were read through a summarising fetch tool; quoted PMC text is as that tool returned it
(not a verbatim re-read of the PDF). Old EMBO J pages returned the abstract only. Where a number lives only in a
full text I did not reach, the cell says NOT_REACHED.
Legend: SUPPORTED = a source I reached says it; CORRECTED = the premise in the brief or a common assumption is wrong
or incomplete; NOT_REACHED = unknown, not negative.

## Q1. Ba2+ block of K2P channels (extracellular, 50-200 uM window)

| Channel | Verdict | Reported block, system, PMID, quoted words |
|---|---|---|
| TREK-1 (KCNK2) | CORRECTED (not "insensitive", but weak: sub-mM IC50) | Ma 2011, Xenopus oocytes, TEVC, PMID 21965685: "a half block (IC50) at 0.56 +/- 0.03 mm with an apparent Hill coefficient of 1.48"; "72.90 +/- 4.63% inhibition" at 1 mM; no value at 100 uM was reported. Same paper: "it has long been believed that the TREK-1 channel is Ba2+ insensitive or resistant". Zhou 2009, CHO cells, PMID 19571146: "800 um extracellular Ba2+ had no effect on whole-cell currents of TREK-1". My own arithmetic from the Hill fit (inference, not a reported value): about 7% block at 100 uM. Net: at 50-200 uM TREK-1 is at most weakly blocked; reports disagree above 0.5 mM (no effect at 0.8 mM in CHO vs IC50 0.56 mM in oocytes). Ma/Lewis 2020, PMID 32317978 (abstract): mouse TREK-1 and TREK-2 "could be blocked by Ba" (concentration not in abstract). |
| TREK-2 (KCNK10) | SUPPORTED (weak) | Bang 2000, rat TREK-2 in COS-7, PMID 10747911: "TREK-2 was partially blocked (36%) by 2 mm Ba(2+)". No 50-200 uM value reached. |
| TRAAK (KCNK4) | SUPPORTED (weak, no number) | Fink 1998, Xenopus oocytes and COS cells, PMID 9628867 (abstract): "These currents are only partially inhibited by Ba2+ at high concentrations". No concentration or percent reached. |
| TASK-1 (KCNK3) | NOT_REACHED | Original TASK-1 paper (PMID 9312005) abstract has no Ba2+ statement; no Ba2+ value found in anything I read. |
| TASK-3 (KCNK9) | NOT_REACHED | Czirjak and Enyedi 2002, PMID 11875121 (abstract): no Ba2+ value. TASK-3 cloning paper not located by search. |
| TWIK-1 (KCNK1) | SUPPORTED, but the two sources disagree 10-fold | Lesage 1996, human TWIK-1, PMID 8605869 (abstract): "TWIK-1 channel activity is blocked by Ba2+(IC50=100 microM)". Mouse TWIK-1 in oocytes, PMID 9013852: "currents are blocked by Ba2+ and quinine" (no number). Zhou 2009, rat TWIK-1 K274E in CHO, PMID 19571146: "800 um extracellular Ba2+ inhibited only 50% ... IC50 value of 960 um"; the authors call the difference with 100 uM a possible species difference or small-oocyte-current error. So TWIK-1 is the only K2P I reached with an IC50 inside the window, and only in one report. |
| THIK-1 (KCNK13) | NOT_REACHED for the cloned channel | Rajan 2000, PMID 11060316 (abstract): current "enhanced by arachidonic acid and inhibited by halothane"; no Ba2+ value. Native Purkinje background current "shares several properties with ... THIK-1" and was inhibited "by barium (Ba2+; 300 microM, 50%)" (Bushell 2002, PMID 11834618): this is a native current assigned to THIK-1 by similarity, not THIK-1 data. |

Related native-tissue statements (context, not channel assignments): hippocampal astrocyte passive conductance
"essentially insensitive to extracellular Ba2+" (1.2 mM Ba2+ inhibited 17 +/- 6%, PMID 19571146); the same paper says
"Mammalian K2P channels ... are much less sensitive to extracellular Ba2+ than inward rectifier K+ channels" and gives
Kir4.1 IC50 = 3.5 uM. H441 airway cells carry a "Ba2+-resistant, acid-sensitive K+ conductance" (PMID 17277046).
Cadaveira-Mosquera 2011 (PMID 21273422, mouse sympathetic neurons): riluzole-activated current "inhibited by barium"
(concentration not in abstract). Kubanek 2016 (PMID 27112990) used BaCl2 "to block K2P channels" (concentration not in
abstract). Kir2.1 itself shows "voltage- and concentration-dependent blockade by external barium" (PMID 30835490,
abstract; no IC50).

## Q2. Small-molecule activators of Kir2.1 / Kir2.2 / Kir2.3

| Compound | Verdict | Source and what it was measured on |
|---|---|---|
| Zacopride | SUPPORTED for Kir2.1 only; CORRECTED for Kir2.2/2.3 | Zhai 2017, PMID 28542320: "In Kir2.x transfected Chinese hamster ovary (CHO) cells, zacopride activated the Kir2.1 homomeric channel but not the Kir2.2 or Kir2.3 channels"; also "a selective and moderate agonist of the IK1/Kir2.1 channels", patch clamp in rat ventricular myocytes, 1 umol/L; the antiarrhythmic effect "were reversed by 1 umol/L BaCl2". Cardiac preparations and CHO cells; no neuron data reached. Further cardiac use: PMID 31507422, PMID 28623610 ("I-specific agonist zacopride"). EC50 not reached (abstracts). |
| Flecainide | SUPPORTED as an enhancer of Kir2.1 only; not a selective opener | Caballero 2010, PMID 20713726: "Flecainide increases outward I(Kir2.1) ... by decreasing their affinity for intracellular polyamines"; "does not increase I(Kir2.2) and I(Kir2.3)" because those lack Cys311. A sodium-channel antiarrhythmic ("exhibits ventricular proarrhythmic effects"), so a mechanism-of-action probe, not a Kir2 opener. |
| Chloroethylclonidine | CORRECTED: an inhibitor, not an activator | Muessel 2013, microglia, PMID 23893870: "The inhibition of Kir2.1 with chloroethylclonidine"; Sanson 2019, PMID 30835490: "multichannel inhibitors chloroethylclonidine, chlorpromazine ...". |
| Any Kir2.2 or Kir2.3 opener | NOT_REACHED | Searches run: "Kir2.1 activator", "Kir2.1 activator small molecule opener", "activator of inward rectifier Kir2 channel Kir2.3 Kir2.2 opener ...", "zacopride Kir2.1 IK1 agonist", "chloroethylclonidine Kir2.1 activation", "flecainide increases Kir2.1 current", a Kir2 pharmacology review query. Sanson 2019 closes with "the currently limited K2.1 pharmacology". I found no Kir2.2/Kir2.3 opener; absence rests on PubMed abstract search plus the ChEMBL target view (59 activity rows on the Kir2.1 target, all inhibitors, plus one row of -16% "Activation" at 30 uM, i.e. an inhibition), so treat as "not reached", not "none exists". |

## Q3. Riluzole on K2P and its other neuronal actions

| Item | Verdict | Evidence |
|---|---|---|
| Riluzole activates TREK-1 and TRAAK | SUPPORTED, but biphasic for TREK-1 | Duprat 2000, COS cells, PMID 10779373 (abstract): "riluzole is an activator of TREK-1 and TRAAK ... Whereas riluzole activation of TRAAK is sustained, activation of TREK-1 is transient and is followed by an inhibition. The inhibitory process is attributable to an increase of the intracellular cAMP concentration by riluzole that produces a protein kinase A-dependent inhibition of TREK-1." EC50 and percent: NOT_REACHED (full text paywalled; fetch returned 403). Fink 1998 (PMID 9628867, abstract): "TRAAK channels are stimulated by the neuroprotective drug riluzole". Lamas review (PMID 30964046, Table 3 as summarised): TREK-1 and TRAAK activated "at 100 uM" in heterologous channels; TREK-2 at 300 uM native (Cadaveira-Mosquera 2011, PMID 21273422). ChEMBL (via a review, see Q5): TREK-1 EC50 139.4 uM; fold change 2.0 at 100 uM (COS7) and 1.4 at 10 uM (CHO). |
| Opposite sign in some native neurons | SUPPORTED | Rat DRG leak currents: "riluzole, norfluoxetine and prostaglandin F2alpha inhibited the leak K+ currents" (PMID 29980241). Purkinje background current: riluzole "(500 microM) ... reversibly inhibited" by 36% (Bushell 2002, PMID 11834618). |
| Sodium channels | SUPPORTED, at roughly 20-100x lower concentration than the K2P effect | Rat cortical synaptosomes, veratridine-induced Na+ entry blocked by "riluzole, lifarizine IC50 approximately 1-5 microM" (Deffois 1996, PMID 8981487). Hippocampal slice, veratridine-induced failure: riluzole IC50 "1.95" microM (Ashton 1997, PMID 9037412). Riluzole blocking the persistent Na+ current lowers firing gain in CA3 pyramidal cells (Tamir 2025, PMID 40681116, abstract; concentration NOT_REACHED). |
| Glutamate release | SUPPORTED, concentration NOT_REACHED | Rat cortical synaptosomes: riluzole inhibits 4-AP-evoked glutamate release "concentration-dependent", via reduced Ca2+ influx, P/Q-type channels (Wang 2004, PMID 15051158). Riluzole 84 +/- 5% inhibition of glutamate release vs 52 +/- 12% for GABA, read as Na+ channel antagonism (PMID 12604696). |
| Other | SUPPORTED (no numbers) | Lamas review: riluzole "exerts effects on a good number of ion channels, like sodium, potassium, calcium channels", also GABA-A, glycine, glutamate receptors (PMID 30964046). |

## Q4. BL-1249 selectivity; flufenamic acid on TREK

| Item | Verdict | Evidence |
|---|---|---|
| BL-1249 EC50, TREK subfamily | SUPPORTED | Pope 2018, Xenopus oocytes TEVC, PMID 30089357 (full text as summarised): TREK-1 5.5 +/- 1.2 uM, TREK-2 8.0 +/- 0.8 uM, TRAAK 48 +/- 10 uM. Abstract: "activates all TREK subfamily members but has no effect on other K2P subfamilies"; "activating K2.1(TREK-1) and K10.1(TREK-2) ~10-fold more potently than K4.1(TRAAK)". |
| BL-1249 non-activated K2P | SUPPORTED | Full text: no activation of TWIK-1, TASK-1, TASK-2, TASK-3, THIK-1, TRESK "tested up to the solubility limit (~80 uM)". The phrase "has no effect on other K+ subfamilies" is in the abstract; Kv, Kir and hERG results were NOT_REACHED (the summary of the full text said they are not mentioned). The paper also says "Although not selective for K2P channels, a number of fenamates ... activate members of the mechanosensitive TREK K2P subfamily" and "Fenamates are weak K2P modulators". |
| BL-1249 tetrazole analogue work | SUPPORTED | PMID 31072652: "BL-1249, a fenamate class non-steroidal anti-inflammatory and a known activator of the K2P potassium channels TREK-1 (K2P2.1) and TREK-2 (K2P10.1)"; poor physicochemical and DMPK properties. |
| Flufenamic acid activates TREK | SUPPORTED only through ChEMBL curation of a review; primary NOT_REACHED | ChEMBL rows (Q5): TREK-1, EC50 100 uM (COS7, whole cell, +50 mV); 3.5-fold and 250% increase at 100 uM (HEK293). A title-style search returned PMID 16075240 (fenamates and diltiazem, lipid-sensitive mechano-gated 2P-domain K+ channels) as the likely primary, but its abstract call was rate-limited and I did not read it, so I make no claim from it. Flufenamic acid on TASK-3/THIK-1: no data reached. In ChEMBL it has a TRESK row: EC50 "> 100 uM" and 474 uM (PMID 27641472 per the ChEMBL document record, abstract not read). |

## Q5. ChEMBL activity rows (REST, read 2026-11-10)

Brief premise CORRECTED. CHEMBL1914276 is not a K2P target. `target/CHEMBL1914276` returns pref_name "Inward
rectifier potassium channel 2", organism Homo sapiens, accession P63252 (Kir2.1, KCNJ2). Query
`activity?molecule_chembl_id=CHEMBL744&target_chembl_id=CHEMBL1914276` returned total_count 0; the same with
CHEMBL23588 returned total_count 0. Full per-molecule pulls (CHEMBL744: 879 rows; CHEMBL23588: 372 rows) contain no row on
CHEMBL1914276. Molecule ids confirmed: CHEMBL744 = RILUZOLE, CHEMBL23588 = FLUFENAMIC ACID. So on the named target
the record establishes neither activation nor inhibition; there is no record. The Kir2.1 target holds 59 rows, none for these two
molecules.

The rows that do exist are on CHEMBL2321615, "Potassium channel subfamily K member 2" (TREK-1), Homo sapiens.
All have assay_type B, assay_organism null (target_organism Homo sapiens), and come from document CHEMBL3817738, which is
a review (Vivier et al., J Med Chem 2016, "Perspectives on the Two-Pore Domain Potassium Channel TREK-1", PMID
26588045), i.e. curated secondary data.

| Molecule | activity_id | standard_type, value, units | assay description |
|---|---|---|---|
| CHEMBL744 riluzole | 16619938 | FC = 2.0 (no unit) | "Activation of TREK1 (unknown origin) expressed in COS7 cells assessed as increase in whole cell currents at 100 uM at +50 mV relative to control" |
| CHEMBL744 | 16619968 | FC = 1.4 | "Activation of human TREK1 expressed in CHO cells assessed as increase in channel currents at 10 uM relative to control" |
| CHEMBL744 | 16619970 | EC50 = 139400 nM (139.4 uM) | "Activation of TREK1 (unknown origin) expressed in COS7 cells assessed as increase in whole cell currents at +50 mV relative to control" |
| CHEMBL23588 flufenamic acid | 16619969 | EC50 = 100000 nM (100 uM), pchembl 4.00 | same COS7 EC50 assay (CHEMBL3819803) |
| CHEMBL23588 | 16619974 | FC = 3.5 | "Activation of TREK1 (unknown origin) expressed in HEK293 cells assessed as increase in current density at 100 uM relative to control" |
| CHEMBL23588 | 16619977 | Activity = 250 % | "Activation of TREK1 ... HEK293 ... increase in current currents at 100 uM relative to control" |

Verdict on direction: these rows establish activation of TREK-1 (K2P2.1), not Kir2.1, and the potencies are weak
(EC50 100-139 uM, 100 uM test concentrations). Because the source is a review and organism is "unknown origin",
treat them as pointers to primary papers, not as stand-alone measurements. Flufenamic acid also has rows on TRESK
(CHEMBL2331042, document CHEMBL3860067). Riluzole also has 4 rows on hERG (CHEMBL240), irrelevant here.

## Q6. Other K2P or Kir activator described in cortical pyramidal neurons

| Item | Verdict | Evidence |
|---|---|---|
| A K2P or Kir2 activator with input-resistance or resting-potential effect in cortical pyramidal neurons (slice or culture) | NOT_REACHED | None found in my searches (riluzole + cortical pyramidal + input resistance; ML335/ML402 + neurons; Kir2 activator queries). Absence rests on PubMed abstract search only. |
| ML335 and ML402 (TREK-1/TREK-2 activators) | SUPPORTED as compounds; no neuron data reached | Lolicato 2017, PMID 28693035 (abstract): structures of TREK-1 with "two selective K2.1 (TREK-1) and K10.1 (TREK-2) activators - an N-aryl-sulfonamide, ML335, and a thiophene-carboxamide, ML402"; measured in oocytes/HEK293. |
| Retigabine (Kv7/M-current enhancer, not K2P/Kir) | Adjacent, hippocampal | Tamir 2025, adult rat CA3 pyramidal cells, PMID 40681116: blocking IM with XE991 "increased input resistance"; "Enhancing IM by retigabine produced opposite effects". Reports an opposite effect to XE991 but does not state input resistance for retigabine itself; a Ba2+-insensitive route to lower input resistance, in hippocampus not cortex. |
| Native riluzole-activated TREK-like current | Peripheral neurons only | Mouse superior cervical ganglion neurons (PMID 21273422). Zhou 2009 notes TASK-1 colocalises with NeuN in hippocampal pyramidal neurons (PMID 19571146) - expression, not an activator. |

## What an investigator proposing "add a Ba2+-sensitive resting K+ conductance with an opener" most needs to know

1. The assumption "Ba2+-sensitive implies Kir2 or K2P" hides a split. At 50-200 uM Ba2+ the evidence I reached
   points to Kir-type channels: TREK-1 IC50 0.56 mM (oocytes; no effect at 0.8 mM in CHO), TREK-2 36% at 2 mM, TRAAK only
   "partially inhibited ... at high concentrations", versus Kir4.1 IC50 3.5 uM. The only K2P with a reported sub-200 uM
   IC50 is TWIK-1 (100 uM in one oocyte paper; 960 uM in another). TASK-1, TASK-3 and THIK-1 Ba2+ data were NOT_REACHED, so
   they cannot be excluded or included. A resting conductance lost at <=200 uM Ba2+ is therefore more likely Kir (or
   TWIK-1) than TREK/TRAAK.
2. Therefore the K2P openers do not match that hypothesis. Riluzole, BL-1249 and flufenamic acid act on the TREK
   subfamily (and riluzole on TRAAK), the very channels least sensitive to Ba2+. Restoring input-resistance with them
   would restore a largely Ba2+-insensitive current, and the Ba2+ test would not confirm the mechanism.
3. The only Kir2 opener reached (zacopride) is Kir2.1-selective ("but not the Kir2.2 or Kir2.3"), characterised in
   heart and CHO cells, with no neuron data. Flecainide raises Kir2.1 outward current only through Cys311 and is a Na+
   channel drug; chloroethylclonidine is an inhibitor. No Kir2.2/Kir2.3 opener was reached. Which Kir2 subunit carries
   resting current in juvenile cortical pyramidal neurons would have to be established first.
4. The ChEMBL pointer is wrong for this question: CHEMBL1914276 is Kir2.1, and riluzole and flufenamic acid have zero
   activity rows on it. The rows that exist are on TREK-1 (CHEMBL2321615), curated from a 2016 review, EC50 100-139 uM.
   Anything built on "riluzole/flufenamic acid vs CHEMBL1914276" has no data behind it.
5. Riluzole is a poor mechanism-specific tool: its K2P activation needs about 100 uM (TREK-1 transient, then
   cAMP/PKA-mediated inhibition), while Na+ channel block (IC50 ~1-5 uM) and reduced glutamate release occur at 20-100x lower concentrations,
   and it inhibited leak currents in rat DRG and Purkinje neurons. Any effect of riluzole on input resistance would not be
   attributable to K2P without a TREK/TRAAK-specific control.
6. BL-1249 is the cleaner K2P probe (TREK-1 5.5 uM, TREK-2 8.0 uM, TRAAK 48 uM; no effect on TWIK-1, TASK-1/2/3, THIK-1,
   TRESK up to ~80 uM), and ML335/ML402 are structurally distinct TREK activators; both still target the Ba2+-weak subfamily and
   have no cortical pyramidal neuron data reached.
7. Flufenamic acid's TREK activation rests on ChEMBL's review curation (EC50 100 uM); the primary paper (candidate PMID
   16075240) was not read. Fenamates are described as "weak K2P modulators" and "not selective for K2P channels".
8. Gaps to close before relying on any of this: TASK-1, TASK-3 and THIK-1 Ba2+ concentration-response; full text of
   Duprat 2000 for riluzole EC50 and percent; primary flufenamic acid/TREK paper; any Kir2.x or K2P activator tested in
   cortical pyramidal neurons; Kv/Kir/hERG selectivity of BL-1249.
