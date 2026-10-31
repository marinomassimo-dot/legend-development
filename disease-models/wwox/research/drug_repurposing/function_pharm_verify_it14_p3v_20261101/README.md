# Independent verification of function_pharm_it14_p3_20261101 (IT14)

Verifier: a separate agent (not the producer), 2026-11-01. Recorded here by the Orchestrator from the verifier's hand-back; the verifier wrote no file. **What the verifier knew:** the producer's claims from the brief (not its tables); it extracted the Breton 2021 and clobazam sources first and read the producer's README only afterwards, so it is independent, not blind. Agreement between agents is not biological evidence; this checks reading and arithmetic.

## Decisions

| Item | Verdict |
|---|---|
| 1. Decisive premise (Breton 2021, PMID 34634460, Table 1, bursts, sIPSC) | **CONFIRMED WITH CORRECTIONS.** Table 1 values, burst counts (WT 0/11, HT 4/23, KO 36/42) and the Fisher tests reproduce (KO vs HT p = 7.4e-8; HT vs WT p = 0.28). Over-reads in the producer's wording: 'the only KO-specific deficit is inhibitory' (mEPSC and sEPSC amplitude differ between HT and KO; rebound is KO-only); 'depolarisation graded and shared' (input resistance and AP amplitude are fully shared; HT-vs-KO never tested; real KO-HT resting-potential gap 1.9 mV; cells treated as independent although from 5, 6 and 15 animals); 'HT near wild type for inhibition' is an untested pooling convention (HT differs from WT in mEPSC amplitude and frequency and has bursts in 4/23 slices). The Fig 4 legend n are internally inconsistent. |
| 2. Pharmacological identity and action | **NOT CONFIRMED on the main point.** The 'selectivity GAP' for clobazam and N-desmethylclobazam is false: three open primary papers give subtype data and disagree (Ralvenius 2016: N-desmethylclobazam efficacy ratio alpha2/alpha1 1.77; Hammer 2015, human oocytes: non-selective; Jensen 2014: modest alpha2 affinity preference). The negative holds only for the catalogues. Other identity items confirmed (ChEMBL ids; vigabatrin racemate; ezogabine and tiagabine at secondary level); CHEMBL2093872 is a target id; NNC-711 not found in ChEMBL by name; ezogabine Kv7 EC50 spread is up to about 9-fold across isoforms. |
| 3. Logic of E0 to E2 | **CONFIRMED WITH CORRECTIONS.** E1 (gabazine in WT/HT) shows sufficiency of disinhibition in a normal circuit, not that it is the KO step; bath K+ is not Vm-matching; E2 is satisfied by repair and by counterbalance; benzodiazepine-site potentiation may not restore IPSC charge; no AMPAR arm; the intrinsic Ih/input-resistance step is not represented; R4 and R5 are not separable. The power statement assumes independent slices: at one value per animal (n = 6) power is 0.61 for 0.80 against 0.17 and 0.28 for 0.60 against 0.17. |

## What the module may and may not say (verifier's wording)

May: both compounds are benzodiazepine-site positive modulators of alpha1, 2, 3 and 5 beta gamma2 receptors, EC50 about 0.1 to 1 uM; subtype selectivity is disputed across three primary papers that differ in species, system and readout; clobazam is an approved benzodiazepine-site drug and N-desmethylclobazam its main active metabolite (label facts); no GABAergic drug has been tested in any WWOX preparation; as an ex vivo probe it is a hypothesis of compensation of a measured inhibitory loss, conditional on E0 locating the deficit as receptor-limited.

May not: that subtype potency is unquantified or a 'selectivity gap' exists; that N-desmethylclobazam is alpha2-selective as an established fact; that inhibitory loss is the only KO-specific deficit or that HT inhibition is near wild type; that compensation of any kind, clinical benefit or a dose is established.

## Not checked by the verifier

The ChEMBL activity rows, the GtoPdb extract, the ChEMBL tiagabine document, the Fig 4 image and the Breton supplement; the ezogabine and vigabatrin enantiomer statements rest on secondary sources; D-AP5 identity is prior knowledge, not verified at a source; no figure was digitised.
