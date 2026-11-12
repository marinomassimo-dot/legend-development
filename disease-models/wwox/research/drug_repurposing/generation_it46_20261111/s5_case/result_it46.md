# IT46 P9: result of the second new case S5 (positive modulation of the GABA-A receptor), against the pre-registration

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Nothing here nominates a compound for use. Frame, rule, arms, predictions and failure outcomes: `prereg_it46.md` (committed before any count). Blind reader: `verify/VERDICTS.md` (sonnet, high; about 79 tool calls, 229k tokens, about 7 minutes). **Status: provisional on one arm.** The ChEMBL activity read for C2 could not be made (the public API returned HTTP 500 and timeouts when tried); C2 below is the mechanism and interaction tables only. The activity read is a stated open step and, when made, only adds to the C2 row.

## Two errors in my own pre-registered frame, found after it was committed
1. **"Not measured as a deficit of synaptic current in the Wwox slices at P13-17" is wrong.** The reader (full text of PMID 34634460, text only) found spontaneous IPSCs measured in the recorded layer II/III pyramidal cells: amplitude 57.3 to 27.5 pA (a 52% fall), frequency 10.3 to 8.4 Hz (an 18% fall, SDs as large as the means), in the neuron-specific Synapsin-Cre knockout at P13-17. What is not measured: the cause; evoked IPSCs (none in the paper); the GABA reversal potential (the pipette held 140 mM chloride); the pharmacological identity of the events (no GABA-A antagonist named in the delivered text); interneuron number or type. The frame's observation row is corrected here, not edited in the committed pre-registration.
2. **"GABRA2, GABRA3, GABRA5 and GABRB2 are not in any held table" is wrong.** The P8 extraction included them (checked against `chloride_gaba_expression.py`). `cell_context` returns data for all seven symbols. The prediction "the context part adds a statement for three of seven symbols" is therefore **exceeded** (seven of seven), which is a different kind of miss than the one I predicted.

## Counts (same inputs for every arm)
| Measure | C1 | C2 (tables only; activity read pending) | C3 qualification (ladder) | C4 |
|---|---|---|---|---|
| Molecules | 71 (ChEMBL curated mechanism rows) | 115 rows from mechanism and interaction tables | 131 ladder rows = 106 families (100 engine candidates, 24 excluded and kept, 7 verdict unknown) | no new molecule |
| Roles | | | 75 candidate, 54 unqualified entity, 2 physiological intervention | |
| Next verification | none | none | measure in the context 72; qualify role and status 22; none unless the exclusion premise changes 24; read what the verdict lacks 7; qualify identity 6 | |
| Cell-class context | none | none | 7 of 7 symbols have a row: GABRA5 and GABRG2 neuron-enriched in both species; GABRA1 and GABRB3 shared in the mouse table (neuron-enriched in the one human neuron sample); GABRA2 shared in the mouse, enriched elsewhere in the human sample; GABRA3 shared | |
| Hypotheses | 0 | 0 | 0 | 1 conditional comparison with six alternatives |
The 24 excluded rows are modulators with the opposite action (negative modulators), kept visible with their reason, not dropped.

## What the reader found (depth stated in the file)
* **R2:** a benzodiazepine-site modulator amplifies existing GABA signalling (diazepam moves the GABA EC50 from 41.0 to 21.7 micromolar in oocytes; the same abstract reports direct gating at ultrahigh receptor levels). Where GABA is depolarising or excitatory the effect is **hedged in animals** (diazepam aggravated events at P11 but not P14 in one study, anticonvulsant in others); the two clinical NKCC1-block trials were add-ons to phenobarbital, not benzodiazepines, one negative, one a small pilot.
* **R3:** tonic delta-subunit receptors are enhanced by neurosteroids; synaptic currents fall while tonic current rises in status epilepticus; ganaxolone against placebo in one developmental encephalopathy (CDKL5) reduced motor seizures (30.7% against 6.9%); no head-to-head tonic-against-synaptic comparison in any developmental and epileptic encephalopathy. PARTLY.
* **R4:** OPCs express functional GABA-A receptors in mouse cortex, and a benzodiazepine-site modulator acted on evoked NG2-cell currents (abstract level), so a **slice-bath modulator is not neuron-only** around postnatal week 2; newly formed oligodendrocytes are not sourced. The held RNA agrees in direction for Gabra1 and Gabrb3 (OPC 3.60 and 21.79 FPKM against neurons 5.49 and 24.53; two pools, different ages).
* **R5:** the one randomised trial of the class is in Lennox-Gastaut (placebo −12.1% against −68.3% drop seizures), not stratified by cause; 14% lost the initial response by year 3 in the extension; "irrespective of cause" and "no developmental gain" are **not sourced** as findings. Benzodiazepines in WWOX children are **not summarised in INV-10**; the upstream A1 table has nine rows mentioning them, which I classified in `benzodiazepine_mentions_a1.tsv`: seven patient groups, two single-child reports of response (nitrazepam after relapse; clobazam added to valproate after vigabatrin failed), three groups with no effect or refractoriness (including clonazepam and clobazam listed as ineffective), two with co-therapy and no stated outcome. No instrument, no cohort.

## What the combination (C4) says, and what it changes
INFERENZA, conditional: the spontaneous IPSC deficit is larger in **amplitude** (52%) than in **frequency** (18%); a deficit of interneuron number or firing would be expected to lower frequency more, so the amplitude change points at the receptor response or the GABA content per event (caveats: pipette with 140 mM chloride, event-detection bias, SDs as large as the means, no evoked IPSC). That puts the receptor-level lever (S5, modulate the receptor) and the supply-level lever (S7, raise GABA per synapse) on the same sample, and adds a discriminating result written after the reader's finding (not part of the pre-registered frame): **D5** a modulator against a reuptake blocker, each at the dose that restores the same fraction of sIPSC amplitude in the knockout, in the same cells, with the wild-type response as the reference.
The next experiment therefore changes from "a modulator arm in the slice" (C1-C3) to: (1) repeat the sIPSC measurement with a physiological chloride pipette and a GABA-A antagonist to confirm identity, and add evoked IPSC and E_GABA (IT46-Q01) in the same cells; (2) only then modulator and reuptake arms against a non-specific arm at matched cellular effect (the three-arm design of IT46-Q04); (3) genotype-by-drug interaction for Wwox specificity; and the effect of a bath modulator is not neuron-only.

## Pre-registered failure outcomes, checked
| Failure outcome | Result |
|---|---|
| The C4 next experiment equals the C1-C3 one | No (above). |
| C4 states a premise the reader finds unsupported | The frame's observation row was wrong (corrected above) and "irrespective of cause" for benzodiazepine efficacy is unsourced; the tonic-against-synaptic comparison is PARTLY. Counted as a miss of the frame, not of the premise carried to the proposal. |
| C4 has fewer defensible hypotheses than C3 | No. |
| C4 recovers nothing C1-C2 missed and adds no premise | No: it adds the amplitude-versus-frequency inference, D5 and the corrected observation; it recovers no molecule. |
| Activity read adds nothing and no row has a distinct next step | **Not evaluable** (activity read pending); the ladder rows do have distinct next steps (five kinds). |

## Against the predicted difference
1 held (the next experiment differs). 2 **exceeded** (context for 7 of 7, not 3). 3 held (131 rows, five kinds of next step). 4 held (no compound nominated). The prediction that the tables left four symbols unknown was an error of mine.

## Limits
One further case, chosen by a mechanical rule, scored by the session that built the method; independent reader for premises only; counts are mine. Reader depth is abstract for every source except PMID 34634460 (text only, no figure legends or supplement). The activity read is open. The benzodiazepine classification of the A1 rows is from table cells, not from the primary papers. Translations of any dashboard text from this case are the assistant's.
