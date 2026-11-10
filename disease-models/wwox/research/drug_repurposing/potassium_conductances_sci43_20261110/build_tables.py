"""SCI43 S3/S4: writes the readable tables of the generation step (hypotheses, tool roles, identity, experiment ladder, outcome matrix).
Text lives here so that a reviewer reads one file; the TSVs are the data the generator reads. Labels: DATO / INFERENZA / IPOTESI / ESPANSIONE.
Prop ids D01-D16 and share ids S01-S21 refer to output/decisive.tsv and output/shares.tsv (producer og-k); IR = output/implied_reversal_points.tsv."""
import csv
from pathlib import Path
OUT = Path(__file__).resolve().parent / "output"
def w(name, hdr, rows):
    for r in rows: assert len(r) == len(hdr), (name, r[0], len(r), len(hdr))
    with open(OUT / name, "w", newline="") as f:
        t = csv.writer(f, delimiter="\t", lineterminator="\n"); t.writerow(hdr); t.writerows(rows)

H = ["hyp_id", "level", "observation", "relation_qualified", "proposed_action_class", "favourable_context", "opposite_context", "expected_functional_result", "refuting_measure", "premise", "function_that_could_improve", "usefulness_without_wwox_repair", "label", "support_ids"]
HYP = [
 ["KH1", "neuron (circuit only by inference)",
  "WT to KO: Rin 102.9 to 143.0 MOhm (+39 percent), rest -79.3 to -73.6 mV, tau 18.6 to 21.3 ms; HT equals KO on Rin and is intermediate on rest; bursts in 36/42 KO, 4/23 HT, 0/11 WT slices (34634460 Table 1; hcn physiology Y01-Y03).",
  "A Ba2+-sensitive resting K+ conductance (Kir2-type and/or a K2P-type leak; not separable with Ba2+) carries about 23 percent of the resting conductance of a WT L2/3 neuron (D01, S01) and Ba2+ block raises Rin about 30 percent with a small depolarisation and a lower rheobase (S01); the Wwox pair implies a lost conductance of about 28 percent whose implied reversal (-93.7 KO, -88.8 HT, recorded scale) lies in the K+ range and apart from the maturation values (-72 to -79) (IR); a known Ba2+-sensitive current gain (Fmr1 KO) gives the mirror pattern (Rin -28 percent, rest -3.7 mV, implied -91.6 against a measured Ba2+ reversal -89.6) (D13, S02-S04, IR).",
  "Add or restore a resting K+ conductance of about 2.7 nS (reversal near E_K) to the KO neuron: experimentally by dynamic clamp; pharmacologically only an activator class acting on a Ba2+-sensitive resting channel (no neocortical K2P tool located, D09; no Kir2 activator in the catalogue).",
  "A Ba2+-sensitive current (Kir2-type) per pF smaller in KO and HT than in WT, with reversal near the corrected E_K, measured with synaptic transmission blocked and the junction potential measured; capacitance and access resistance reported; dynamic-clamp re-addition restores Rin and rest.",
  "Ba2+-sensitive current per pF equal across genotypes; or the contrast shrinks under blockade or matched access resistance; or capacitance is lower and tau scales so that the pair follows from cell size; or the implied reversal after the measured junction correction is outside K+ range.",
  "Rin, rest, rheobase and gain move toward WT; bursts may fall only if intrinsic gain is limiting. HT carries the full Rin change and rarely bursts, so intrinsic change alone is not sufficient for bursts (DATO from Table 1; HT versus KO untested in the paper).",
  "Difference-current ladder (K-EXP step 2), then dynamic clamp (step 5).",
  "The Ba2+-sensitive share is the same in this preparation (P13-P17, layer II/III, somatosensory, 35 C) as in the adult auditory-cortex source; Ba2+ at 60 uM is neuron-autonomous (glial Kir4.1 not excluded: UNSOURCED_BACKGROUND, to be sourced or dropped).",
  "Intrinsic excitability (input-output gain, rheobase, resting state). Not stated: seizure, development.",
  "Yes: a hyperpolarising conductance can be useful as compensation whether or not WWOX is restored; the premise (a deficit of that conductance) is not needed for the compensation to act, but is needed to call it a repair.",
  "INFERENZA (arithmetic on printed means) + IPOTESI", "D01,D02,D13,D16,S01-S04,IR"],
 ["KH2", "neuron to circuit (spiking range)",
  "Rest is below the activation range of Kv7 (rest -79 to -74 recorded, about 8-16 mV more negative after junction correction, D14-D15); no AHP, adaptation or Kv7 current is reported for Wwox neurons; the F-I slope is reported not to differ once shifted to rheobase (supplement unread).",
  "Kv7 current starts near -70 mV (D03); XE991 has no effect at -70 mV on a recombinant channel and half-inhibits near -51 mV, so a null XE991 effect at rest says nothing about the share (D05); KCNQ2 loss raised Rin 25 percent with rest near -67 mV (D04) but with a higher AP count and smaller mAHP, and Ank2-cKO L2/3 neurons (Kv7 protein reduced) showed higher current-spike slope with retigabine rescuing mAHP and spike count (S12-S13, functional only).",
  "A Kv7 opener as a spike-frequency and AHP stabiliser acting in the subthreshold-to-spiking range, not on resting Rin or rest; read as a mechanism comparator for the K+ lever and as a possible compensation.",
  "An XE991-sensitive current at about -55 to -45 mV smaller in KO/HT, mAHP smaller, adaptation weaker, gain steeper.",
  "XE991-sensitive current equal; mAHP equal; F-I slope equal at matched rheobase (as the paper reports); or an opener raises spiking in a Wwox slice (the HCN1 gain-of-function mouse precedent: retigabine increased ECoG spiking, abstract-level, IT35).",
  "Fewer spikes per burst-initiating depolarisation and a longer AHP; no change of Rin or rest. Burst effect unknown.",
  "XE991-sensitive current at -55 mV and mAHP by genotype (step 3).",
  "A Kv7 deficit exists in the spiking range of Wwox neurons (unmeasured); the published unchanged F-I slope argues against it.",
  "Spike-frequency adaptation and AHP, not resting state.",
  "Yes, as compensation, without any claim of a Kv7 lesion (a response does not show a lesion).",
  "IPOTESI, weakened by an observation already in the record", "D03,D04,D05,D06,S09,S12,S13"],
 ["KH3", "neuron",
  "Sag at -200 pA 1.18, 2.04, 2.57 mV and rebound larger only in KO; Rin higher.",
  "Ih carries about 6 percent of the resting conductance in WT L2/3 and its block lowers sag from 1.8 to 1.0 mV and hyperpolarises 4.7 mV (D07); it carries most of the conductance at -80 mV in deep layers (D08, data not shown, not L2/3). A larger Rin drives a cell further for the same step, so the absolute sag can rise without more HCN (IT36/IT40).",
  "HCN block is a tool arm for sag and rebound and for the hyperpolarising effect on rest; it cannot carry the 28 percent resting conductance by itself (about 6 percent in the source).",
  "Excess sag persists at matched potential and deflection and a ZD7288-sensitive current per pF is larger in KO.",
  "Excess sag vanishes at matched conditions or the ZD7288-sensitive current per pF is equal.",
  "Sag and rebound reflect recruitment by a more resistive cell, not a difference in HCN.",
  "Matched-deflection sag and the ZD7288-sensitive current in the same cells (step 4).",
  "Existing INV-18 main arm; here only its share of the conductance is added.",
  "Sag/rebound only.",
  "Not a compensation claim.",
  "DATO (share from another preparation) + INFERENZA", "D07,D08,S05,S16"],
 ["KH4", "circuit / network consequence",
  "Intrinsic changes are as large in HT as in KO (Rin 143.26 vs 143.03) while bursts are 4/23 versus 36/42; the recordings were probably made with synapses intact (inference from the Methods drug list).",
  "If the K+ conductance change were produced by network activity (extracellular K+ or activity-dependent regulation), the HT, which rarely bursts, should not show the full Rin change; it does (DATO from Table 1; HT v KO untested). Ba2+ at 60 uM was applied with synapses intact and spontaneous EPSPs present in the preprint (S01).",
  "No neuron-targeted drug: a network consequence is addressed upstream (INV-05 axis) or by glial K+ buffering (no activator in the catalogue).",
  "The contrast shrinks under synaptic blockade, or in non-bursting KO slices.",
  "The contrast is unchanged under blockade and in non-bursting KO and HT slices (supports an intrinsic origin).",
  "If consequence: K+ levers act downstream of the cause and cannot be a repair.",
  "Step 1: the same cells recorded with and without blockers, bursting and non-bursting slices.",
  "Wwox slices are recorded with synapses intact in the source paper (inferred, not stated).",
  "Circuit state.",
  "Not directly.",
  "INFERENZA (HT versus KO argument)", "S01"],
 ["KH5", "development / recording",
  "P13-P17 sits in a steep transition: Rin falls about 47 percent per interval from P7 to P28, rest hyperpolarises 8.3 then 3.1 mV, tau falls with Rin so capacitance is about constant (prelimbic L3, 188 to 180 pF) (D10, S19); Kv7 current density about doubles P11-14 to P20-24 (D11).",
  "A maturation delay would raise Rin and depolarise rest like the Wwox pair, but the implied reversal of the developmental conductance gain is -72 to -79 mV, not -89 to -94 (IR), and tau rises with Rin at constant capacitance, whereas Wwox tau is flat (18.6, 18.8, 21.3 ms): a delay at constant capacitance predicts tau up about 39 percent. Cell size alone (C down) predicts Rin up and tau flat but not a depolarised rest unless a fixed seal shunt is added (IT40).",
  "No pharmacological lever; the measurement of capacitance, tau, ages and weights decides whether any K arm is needed.",
  "Capacitance lower in mutants and tau flat; ages, weights and layer matched; the K+ difference current per pF equal.",
  "Capacitance equal with higher Rin (conductance lost); the implied reversal stays K-like after the measured junction correction.",
  "None (an explanation, not an arm).",
  "Capacitance and tau in the same cells (step 0).",
  "Developmental data are from prelimbic cortex at 31 C: a transfer in region and temperature.",
  "n.a.",
  "n.a.",
  "INFERENZA", "D10,D11,S19,S20,IR"],
]
w("hypotheses.tsv", H, HYP)

T = ["tool", "family_relation", "identity_state_catalogue", "role", "role_reason", "potency_unit_assay_source", "engagement_in_cortical_neurons", "alternative_actions_documented", "limit"]
TOOLS = [
 ["Ba2+ (BaCl2; inorganic)", "Kir2-type and, at higher concentration, K2P-type leak", "inorganic ion; ChEMBL has barium salts, no neuronal-channel mechanism record", "sonda (difference current and Rin share)", "the only measured share of the order of 28 percent (about 23 percent, S01) is a Ba2+ share; the share is a bound for the Kir/K2P-type family, not a Kir2 identification (S15)", "potency not found in the sources read (T04)", "yes in L2/3 and deep-layer neurons (D01, D02; 16177047 Fig 4-5)", "blocks a K+-selective linear leak at 200 uM in deep neurons (16177047); glial Kir4.1 and other Ba2+-sensitive channels: UNSOURCED_BACKGROUND", "not a drug; no exposure statement; concentration chosen from the source, not by this package"],
 ["XE991", "Kv7 (KCNQ2/3)", "DGIdb-only record; no ChEMBL-selected record; ChEMBL human IC50 row on KCNQ2 exists (identity run)", "sonda (spiking-range current)", "state-dependent: no effect at -70 mV on Kv7.2, half-inhibition near -51 mV (D05), so it must be applied at a depolarised holding potential to read a share", "IC50 0.6-0.7 uM recombinant and about 1 uM native, COPIED by the source, primaries not opened (tools.tsv)", "yes (current block in dissociated L2/3 neurons, 21697446; firing effect in slices)", "blocks other channels at high micromolar doses (21697446, citations unopened)", "selectivity NOT_ASSESSED"],
 ["Linopirdine", "Kv7", "ChEMBL-selected record CHEMBL319111 plus DGIdb-only record", "sonda (second chemotype for the Kv7 arm)", "second blocker chemotype so that one off-target action is not read as Kv7", "IC50 about 2-10 uM recombinant, 3-36 uM native, COPIED (tools.tsv)", "yes (holding-current shift 7.5 pA at -70 mV with 3 uM, 11 cells, dissociated cells)", "as XE991 (21697446 Discussion)", "selectivity NOT_ASSESSED"],
 ["Retigabine (ezogabine)", "Kv7 opener", "CHEMBL41355 chembl_selected (synonym match), curated mechanism on KCNQ2-5 (a family record: 5 genes)", "comparatore di meccanismo (spiking range), conditioned on KH2 premise", "functional rescue of mAHP and spike count in Ank2-cKO L2/3 neurons (S13) and an opener-induced -24 mV half-activation shift measured on recombinant Kv7.2 (28483800); no Rin or rest change in the text (D06)", "no EC50 in the sources read; shift measured at 10 uM on Kv7.2 (recombinant)", "functional only; no neuronal Kv7 current measured", "not stated in the sources read; the HCN1 gain-of-function mouse counter-precedent (abstract-level, IT35)", "no exposure, no clinical statement; catalogue max phase is a record, not a status"],
 ["Azetukalner (XEN1101)", "Kv7 opener", "CHEMBL5095264 chembl_selected plus DGIdb-only record; zero catalogue target rows although ChEMBL has a human EC50 on KCNQ2 and DGIdb interactions on KCNQ2/3", "identità o farmacologia ancora irrisolta (for this package); a reading gap, not a candidate", "the symbol lookup of IT40/IT41 (7 molecules, 2 openers) does not reach it; it appears only by name", "ChEMBL human EC50 row on KCNQ2 exists, not read here", "none read", "none read", "catalogue blind spot is itself a finding for the generator (catalogue_by_family.tsv); selectivity NOT_ASSESSED"],
 ["Flindokalner (BMS-204352)", "Kv7 activator (catalogue); other channel actions not read here", "CHEMBL266510 chembl_selected plus DGIdb-only record; two-gene and single-protein records", "identità o farmacologia ancora irrisolta", "not part of the sources read", "not read", "none read", "not read", "selectivity NOT_ASSESSED"],
 ["ZD7288", "Ih (HCN)", "DGIdb-only record; no ChEMBL measured read (NOT_READ in the identity run)", "sonda (Ih arm; second chemotype needed)", "block of sag and hyperpolarisation in L2/3 and deep neurons (S05, S16)", "potency not found in the sources read; 50 uM called nominally saturating in 16177047", "yes (sag reduced 1.8 to 1.0 mV in L2/3; abolished in deep layers)", "off-target actions not located in the sources read; the INV-18 row already records sodium- and T-type actions at abstract level", "selectivity NOT_ASSESSED"],
 ["Ivabradine", "Ih (HCN) clinically used blocker", "CHEMBL471737 and CHEMBL2145077 chembl_selected plus DGIdb-only; ChEMBL mechanism row is HCN4 only (record granularity, not isoform selectivity)", "comparatore (Ih arm second chemotype), carried from INV-18", "not read here", "not read here", "none read here (earlier INV-18 notes: abstract-level in rat cortex)", "not read here", "no brain-exposure statement carried"],
 ["Volatile anaesthetics (desflurane, enflurane, halothane, isoflurane, sevoflurane)", "K2P TREK/TASK openers per the catalogue only", "five ChEMBL rows, OPENER on KCNK2/3/9/10, single-protein records", "esclusione circoscritta as a lever; read at most as a general-suppression control class", "catalogue rows on K2P are these five molecules and doxapram (blocker); none is shown to act on neocortical K2P channels in the sources read; a general anaesthetic acts on more than K2P (UNSOURCED_BACKGROUND)", "not read", "none read", "not read", "no lever proposed"],
 ["K2P tools named in the literature (TREK activators, TASK blockers) and Kir2 tools (a Kir2 blocker)", "K2P, Kir2", "not in the catalogue by name, or DGIdb-only (ML297 is a GIRK name and is not used)", "informazione insufficiente", "no source with a K2P tool applied to neocortical pyramidal neurons was found (D09, perimeter in queries.tsv); no Kir2 activator in the catalogue", "not read", "none read", "not read", "the lever for KH1 has no read tool; the experiment (dynamic clamp) does not need one"],
]
w("tools_roles.tsv", T, TOOLS)

I = ["name", "identity_state", "chembl_selected_ids", "dgidb_only_records", "curated_mechanism_on_expected_genes", "measured_activity_rows", "selectivity", "note"]
IDR = [
 ["XE991", "NAME_EXACT", "none", "CAT:DGIDB:6067b4b58fc4", "none", "ChEMBL human IC50 row on KCNQ2 (CHEMBL342375), not read", "NOT_ASSESSED", "no ChEMBL-selected record"],
 ["linopirdine", "NAME_EXACT", "CAT:CHEMBL319111", "CAT:DGIDB:62f941a3c095", "none", "none returned", "NOT_ASSESSED", ""],
 ["retigabine", "SYNONYM_EXACT (to ezogabine)", "CAT:CHEMBL41355", "CAT:DGIDB:0986d2506c1a; CAT:DGIDB:45c82cc94b86 (a derivative record)", "KCNQ2 CURATED_MECHANISM", "other-species EC50 rows", "NOT_ASSESSED", "a derivative DGIdb record shares the label: not merged"],
 ["azetukalner", "NAME_EXACT", "CAT:CHEMBL5095264", "CAT:DGIDB:79c7cbc464e5", "none (zero catalogue target rows)", "ChEMBL human EC50 on KCNQ2, not read", "NOT_ASSESSED", "invisible to the symbol lookup; reached by name only"],
 ["flindokalner", "NAME_EXACT", "CAT:CHEMBL266510", "CAT:DGIDB:ea4a5dfb1784", "KCNQ2-5 CURATED_MECHANISM (activator)", "human EC50 row, not read", "NOT_ASSESSED", "BMS-204352 resolves to this record"],
 ["ZD7288", "NAME_EXACT", "none", "CAT:DGIDB:5dad25f2b336", "none", "NOT_READ", "NOT_ASSESSED", ""],
 ["ivabradine", "NAME_EXACT", "CAT:CHEMBL471737; CAT:CHEMBL2145077", "CAT:DGIDB:fcc164e2d2b6; CAT:DGIDB:69500b506e04", "HCN4 only (record granularity)", "other-species EC50 on HCN1 (CHEMBL471737)", "NOT_ASSESSED", ""],
 ["ML213", "NAME_EXACT", "none", "CAT:DGIDB:2908937e0365", "none", "human and rat EC50 rows on KCNQ2 (CHEMBL1703636), not read", "NOT_ASSESSED", "not carried as a tool: no neuronal source read"],
 ["ML297", "NAME_EXACT", "none", "CAT:DGIDB:4e99738bec0c", "none", "none on the expected genes", "NOT_ASSESSED", "a GIRK name; not used"],
]
w("identity_tools.tsv", I, IDR)

L = ["step", "arm", "what_is_measured", "controls_from_the_first_slice", "controls_that_can_follow", "replicate_unit", "decides", "state"]
LAD = [
 ["0", "conditions", "capacitance, tau, access resistance and bridge balance by genotype; the measured junction potential of the actual solutions; age, weight, layer, area, temperature; recording with and without synaptic blockers", "littermate WT, HT, KO in the same slice batches; identity by morphology or marker", "blind genotype scoring", "animal", "E3 (size or maturation) and E4 (recording) against E2; whether the borrowed -13 mV is the right size", "start set"],
 ["1", "blockade and slice state", "Rin, rest, sag, rebound with synaptic transmission intact versus blocked, in bursting and non-bursting KO and HT slices", "same cells before and after blockers; vehicle time control", "extracellular K+ read in bursting slices", "animal", "E5 (network consequence) against intrinsic", "start set"],
 ["2", "Ba2+-sensitive difference current", "current-clamp Rin share and voltage-clamp difference current of a low-micromolar Ba2+ (the producer's source used 60 uM) over about -130 to -60 mV, with TTX and synaptic blockers, zero-crossing against E_K computed for the measured junction potential, per pF", "WT and HT in the same batches; vehicle; a second Ba2+ concentration to see the leak component (the 200 uM source shows more)", "a Kir2 blocker named in the literature (not read here)", "animal", "KH1: is the Ba2+-sensitive current smaller per pF, and does the Rin and rest pair follow the implied reversal", "start set"],
 ["3", "Kv7 difference current at a depolarised holding potential", "XE991-sensitive current at about -55 to -45 mV (not at rest: D05), mAHP and adaptation in current clamp, a second blocker chemotype (linopirdine)", "WT and HT; vehicle; XE991 in WT as the genotype-independent baseline", "retigabine at matched effect size (see step 6)", "animal", "KH2: a spiking-range Kv7 deficit; F-I slope at matched rheobase", "start set"],
 ["4", "Ih difference current", "ZD7288-sensitive current per pF and matched-deflection sag with a second chemotype", "WT and HT; vehicle", "ivabradine as a second chemotype only after engagement is shown", "animal", "KH3: the share of sag and rebound that is Ih", "start set (existing INV-18 arm)"],
 ["5", "sufficiency by dynamic clamp", "add a leak of about 2.7 nS with reversal at E_K (corrected) to KO and HT neurons, and subtract it in WT, then re-read Rin, rest, sag, rebound, rheobase and gain", "a sham conductance of zero; a leak of the same size at a reversal of 0 mV (a seal-like shunt) to separate a K+ reversal from a generic shunt", "a graded size series", "animal", "KH1 sufficiency versus KH5: if re-adding the conductance restores Rin and rest but tau stays flat, a smaller cell remains; if it also restores sag and rebound, recruitment explains them", "conditional on step 2 giving a smaller Ba2+ current or a K-like implied reversal"],
 ["6", "opener at matched effect", "a Kv7 opener only if step 3 shows a spiking-range deficit; matched input-output reduction control (the AMPA/kainate pair of IT41 on the evoked-charge axis; a sodium-channel-blocking antiseizure class as a mechanism-different comparator at a matched fall of evoked firing)", "vehicle; the effect on WT cells at the same concentration", "wash-out", "animal", "mechanism effect versus general suppression versus a worse function (AHP, sag, resting state)", "conditional"],
]
w("experiment_ladder.tsv", L, LAD)

M = ["outcome_id", "possible_outcome", "explanation_favoured", "explanation_weakened", "pharmacological_hypothesis_that_rises", "falls_or_stays_open", "next_priority_change"]
MAT = [
 ["O1", "Ba2+-sensitive current per pF smaller in KO and HT; reversal near corrected E_K; dynamic clamp restores Rin and rest", "E2 (a resting K+ conductance)", "E3, E4", "KH1 (add or restore a resting K+ conductance as compensation)", "KH3 stays for sag only; the Ih blocker as first arm falls behind the ladder", "step 5 and a search for a resting-K+ activator with a neocortical source"],
 ["O2", "Ba2+-sensitive current per pF equal; capacitance lower in KO and HT", "E3 (cell size) with or without a fixed shunt", "E2", "none (no K arm)", "KH1 falls", "stop the K branch; keep step 0 as a condition record"],
 ["O3", "Ba2+-sensitive current equal; XE991-sensitive current at -55 mV smaller; mAHP smaller", "E2 within Kv7 in the spiking range", "KH1", "KH2 (Kv7 opener as spiking-range comparator)", "an opener still shows a response, not a lesion; the unchanged F-I slope must be reconciled", "step 6 at matched effect"],
 ["O4", "All difference currents equal per pF under blockade and matched Ra", "E4/E5 (state or selection) or a non-K, non-Ih conductance", "E1, E2, E3", "none", "KH1, KH2, KH3 fall", "return to INV-05 order"],
 ["O5", "The Rin and rest contrast shrinks under synaptic blockade or in non-bursting slices", "E5 (network consequence)", "intrinsic K+ lesion", "none at the neuron", "KH1 and KH2 are downstream; the HT argument is questioned", "upstream (INV-05) first"],
 ["O6", "Excess sag persists at matched deflection and a ZD7288-sensitive current per pF is larger; Rin pair follows the K+ ladder", "E1 for sag with E2 for Rin and rest (both)", "single-cause readings", "KH3 for sag, KH1 for Rin and rest (complementary levers)", "an opener changes none of sag", "Ih tool arm kept beside, not before, the ladder"],
 ["O7", "Re-adding the leak restores Rin and rest but tau stays flat and sag and rebound remain", "E2 for Rin and rest plus smaller capacitance (E3) and an Ih contribution for sag", "pure K+ loss at constant capacitance", "KH1 partial; KH3 open", "none removed", "report the split; no pharmacological claim beyond the compensation"],
]
w("outcome_matrix.tsv", M, MAT)
print("written")
