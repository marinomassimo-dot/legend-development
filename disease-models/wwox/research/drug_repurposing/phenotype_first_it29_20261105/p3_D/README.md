# IT29 P3-D: what other developmental epilepsy models say about compounds and action classes on network discharge (case 2, letter D)

Scientist D, event-id suffix -06, 2026-11-05. Non-canonical research material, not medical advice; no dose, schedule or clinical preference is given. Public edition, WWOX-DEE reference genotype class. Zero spend; no e-mail or registration sent anywhere; only Europe PMC REST and PMC open full text were used.
Endpoint (case 2): network-level discharge in a developmental epilepsy setting (burst or event frequency in larva, slice, MEA; behavioural or electrographic seizures in pups and mice). Favourable = less discharge without sedation or toxicity explaining it.
Files: `evidence_it29_D.tsv` (26 rows), `receipts/` (12 drafts, `FTR-20261105-<PMID>-06`, none recorded). No source was already in the receipt ledger (grep of `ledger/` for each PMID: no receipt; two PMIDs only appear in task notes as "owed").

## 0. Decision (10 lines)

1. **Phenotypic screens in other developmental epilepsies do not corroborate ethosuximide.** In scn1lab larvae it made discharge more frequent in 4 of 7 fish (D02); in stxbp1b larvae it was null (D12). The only T-type-class compound that passed both behaviour and electrographic tests was dimethadione (D05), and the authors note that ethosuximide and flunarizine were not similarly effective, so T-type attribution is not supported. The Cheng 2020 pup result stays a single-laboratory observation (cite `compare_it28_p9_20261105`).
2. **Vigabatrin is lesion-dependent, not a class constant**: adverse in scn1lab larvae (6 of 7 fish more active, D03), favourable in the Tsc1 GFAP knockout mouse (seizures near zero, D25). The repository should not carry a GABA-axis sign without naming the lesion.
3. **Clobazam / benzodiazepine-site potentiation is corroborated in one LoF model and contradicted in another.** Diazepam lowered discharge in scn1lab larvae (D01) and clobazam raised the hyperthermia threshold in Scn1a A1783V/WT mice (D15), but diazepam was null in stxbp1b larvae (D12) and clobazam plus valproate did not raise the threshold under subchronic exposure (D16). The IT14 P3 clobazam/NDMC hypothesis keeps its status; the lesion that responds is interneuron-driven (Scn1a), and the Wwox neuron-deleted cortex has a measured sIPSC deficit (IT14 P3), which is not shown to be sodium-channel based.
4. **Kv7 opener: lesion-dependent.** Favourable in KCNQ2-variant iPSC networks (evoked spikes, D22; the lesion itself) and in Scn8a gain-of-function slices (abstract only, D23); null for hyperthermia threshold in Scn1a loss (retigabine, D17). A Kv7 opener helps where excitation is raised or the M-current is the lesion; it was not shown to help where inhibition is lost.
5. **Sodium-channel blockers are pro-convulsant in Scn1a loss** (carbamazepine: fish D04, mouse D18; lamotrigine sub-chronic: lower threshold and 2 of 6 deaths, D18; mepivacaine: hyperexcitable, D08), while an isoform-selective Nav1.6 inhibitor prevents induced seizures in an Scn8a gain-of-function mouse (D24). Loss-of-function and gain-of-function lesions have opposite sign for this class; this is the transfer condition most likely to matter. Whether Wwox loss lowers Nav1.1-dependent interneuron output is unmeasured, so sodium-channel blockers remain an unquantified hazard class, not a candidate.
6. **NMDAR antagonists**: no DEE-model corroboration. Huperzine A failed in scn1lab although it worked in WT PTZ fish (D07); tiletamine was listed as ineffective. The provoked-seizure signal in normal animals did not transfer to a genetic LoF network.
7. **Class that replicates across lesions: serotonergic agents** (clemizole, trazodone, fenfluramine/norfenfluramine; D09, D10, D13) in two LoF zebrafish models, same laboratory. Not reproduced in the mouse hyperthermia screen (fenfluramine and lorcaserin null, D17). Target attribution (5-HT2B) rests on binding correlation; two 2B-binding analogues were inactive.
8. **Chloride homeostasis (KCC2 activation) reduced pup spasm-like events in Cdkl5-null mice** (D20) but did not reduce time in epileptic activity in adults (D21): a threshold-like gain, not a burden gain; WT-plus-drug control is missing.
9. **Lithium, organoid-level drug tests, Syngap1 and Stxbp1 mouse pharmacology: silent in what was reached** (CDKL5 organoids show hyperexcitability but no drug, D26).
10. **Almost no row has target-specific attribution**: 25 of 26 rows are `compound_only`; the screens pre-register effect, not mechanism.

Rows per direction: favourable 12, adverse 5, null 5, context_dependent 3, undetermined 1.

## 1. Evidence by theme

### 1a. Zebrafish LoF screens (scn1lab, stxbp1b)
Baraban 2013 (partial full text, results on pharmacology): in agar-immobilised scn1lab larvae valproate, diazepam, potassium bromide and stiripentol reduced event frequency; burst durations did not change; ethosuximide, carbamazepine and vigabatrin made activity more frequent in some fish. This is a statement about frequency of discharge events; the duration of each burst, a variable that matters for the WWOX d-APV-sensitive burst phenotype, was not moved by any compound.
Dinday and Baraban 2015 (partial full text): of 1012 repurposed compounds 20 reduced behaviour, 4 passed two independent locomotion trials, and only dimethadione also suppressed electrographic discharge; three others were false positives with ongoing discharge. 154 compounds were toxic and 55 hyperexcitable, so a naive locomotion screen without a lethality and pro-convulsant filter would keep about one in five library compounds as a hazard or confound (D08). Fenfluramine suppressed discharge but 1 mM was toxic; the window is narrow (D09).
Griffin 2019 (partial full text): 28 clemizole analogues; three with 5-HT2B preference and benzimidazole core suppressed discharge; two other 2B-binding analogues did not; known 2B agonists methylergonovine, 6-APB and norfenfluramine suppressed behaviour. The authors state that the conclusion is limited to pharmacological tools and needs molecular strategies. m-CPP and CP-809,101 gave biphasic responses (D11).
Stxbp1b (2022; PMID 35451230, partial full text): phenytoin, valproate, ethosuximide, levetiracetam, diazepam all null on ictal-like events; clemizole and trazodone 80 and 83 percent lower (D12, D13). 4-phenylbutyrate was null on discharge and on the movement deficit of stxbp1a, which is a hypoactivity phenotype and a different endpoint (D14).

### 1b. Mouse LoF and GoF models
Scn1a A1783V/WT hyperthermia (ETSP, 2021; platform paper, 2025): the model is refractory to a battery of ASMs; clobazam and tiagabine raised the threshold, carbamazepine and sub-chronic lamotrigine lowered it, retigabine, cannabidiol, fenfluramine, lorcaserin, stiripentol, valproate, clonazepam, phenobarbital null (D15 to D19). Under subchronic exposure with plasma levels in the human range, clobazam plus valproate was not different from control; adding stiripentol raised the threshold and lowered spontaneous seizures against the two-drug background (D16). No sedation was recorded in the 2025 study.
Scn8a gain of function: NBI-921352 prevented induced seizures in N1768D/+ mice, and also in wild-type mice and rats, so there is no mutation selectivity in the effect (D24). Brain 2025 abstract: M-current opening and persistent sodium current block both suppressed Ca2+ spikes or spreading depolarisation ex vivo and an M-current inhibitor increased spikes only in mutant slices (D23, abstract only).
Cdkl5 knockout: KCC2 activation lowered early spasm-like behaviour and baseline EEG power, but time in epileptic activity after kainate was not lower (D20, D21).
Tsc1 GFAP knockout: vigabatrin lowered seizure frequency near zero from before onset, with modest survival gain and no obvious behavioural effect, but mTOR signalling also fell in culture, so GABA-T inhibition is not the only mechanism (D25).

### 1c. Human cells
KCNQ2 variant iPSC networks (partial full text, supplement figure not opened): burst duration is longer in all three lines compared with isogenic controls; retigabine reduced evoked spikes in G256W/+ and the effect reversed on washout (D22). The spontaneous burst-duration phenotype was not tested with a drug.
CDKL5 organoids: hyperexcitability by patch-clamp, no drug (D26, abstract only).

## 2. Repository compounds against DEE-model screens

| Repository compound or class | Corroborate | Contradict | Silent |
|---|---|---|---|
| clobazam / NDMC (benzodiazepine-site) | scn1lab diazepam (D01), Scn1a mouse clobazam (D15) | stxbp1b diazepam null (D12); clobazam plus valproate null subchronic (D16) | N-desmethylclobazam alone; any Wwox-relevant lesion |
| ethosuximide | none | scn1lab adverse (D02), stxbp1b null (D12) | provoked pup model (that is Cheng 2020 only) |
| T-type blockers | dimethadione (D05) | flunarizine, ETX not effective (D06) | isoform-specific Cav3 compounds |
| lithium | none | none | all |
| vigabatrin | Tsc1 knockout (D25) | scn1lab adverse (D03) | stxbp1, Cdkl5, Kcnq2 |
| NMDAR antagonists | none | huperzine A, tiletamine in scn1lab (D07) | MEA/organoid |
| Kv7 openers | KCNQ2 iPSC (D22), Scn8a slices (D23, abstract) | Scn1a mouse threshold (D17) | scn1lab, stxbp1b |

## 3. Readout specifics and confounds
* Frequency versus duration: scn1lab compounds moved event frequency, not burst duration (D01). Kv7 and KCC2 results are evoked-spike count or latency (D21, D22), not spontaneous bursting.
* Behaviour versus discharge: locomotion hits were false positives in 3 of 4 (Dinday); only discharge-confirmed compounds are counted favourable in the zebrafish rows, except D10 and D11 which are behaviour-led with partial EEG.
* Sedation and toxicity: only the 2025 platform and the Tsc1 study state absence of sedation; lamotrigine produced deaths (D18); fenfluramine lethal at the highest zebrafish concentration (D09). No row is shown to be sedation-free except where noted.
* Provoked versus spontaneous: huperzine A worked in provoked WT PTZ and failed in spontaneous LoF discharge (D07).
* LoF versus GoF: sodium-channel blockers flip sign (D04, D18 versus D24); Kv7 opening is useful in GoF and Kcnq2-LoF models but null in Scn1a-LoF.
* Species and assay: fenfluramine and lorcaserin helped in fish, not in the mouse hyperthermia threshold. A fish bath concentration is not a mammalian exposure.

## 4. What is not established
* No compound-to-target attribution with a target-specific control exists for any favourable row except the lesion-matched KCNQ2 rows (and those still lack a channel-blocker reversal).
* Whether Wwox neuron-deleted networks behave like an interneuron-LoF lesion (sodium-channel blockers harmful, benzodiazepine helpful) or like an excitatory-gain lesion is not decided by these sources.
* No row tests a compound on a WWOX-DEE preparation.
* No stage-matched dose-response with toxicity bounds exists for the compounds the repository carries.

## 5. Not reached
* Syngap1, Stxbp1 mouse and Scn2a pharmacology on network endpoints: searched, no open pharmacology paper found within the time-box (a 2026 SYNGAP1 humanised-model paper is listed but was not opened).
* Dravet iPSC/organoid drug tests: records returned were closed or had no drug arm.
* Lithium and NMDAR antagonists in DEE networks: no source found.
* Scn8a Brain 2025 (full text closed): drug names and exposures unknown; SCN8A N1466 CHO-cell paper (PMID 35902765) is cell-level currents and was not scored.
* KCNQ2 iPSC supplement figure 7 not opened.
Would reopen: the supplements above; a Scn1a or Stxbp1 MEA study with a benzodiazepine arm.
