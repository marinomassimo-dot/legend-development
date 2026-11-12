# IT46 P9: second new case, fixed before execution (S5 positive modulation of the GABA-A receptor, need NEED-INHIBITORY-HYPOFUNCTION)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Written and committed **before** any count, activity read or reading for this case. Same method as S7 (`../p3_case_prereg_it46.md`); the S7 result was not changed to suit this case.

## Selection (mechanical, applied once)
Rule fixed here: the lowest-numbered relation of S1-S8 that (a) was not a case of IT43, IT44, IT45 or IT46 (those used S9, S10, S11, S12, S13, S2, S3, S7 and the pH-K2P package), and (b) has at least one target gene in a held cell-class expression table, so that the context part of the method can be tested with data. Applied: S1 (GRIN2B) and S4 (GJD2, PANX1) have no gene in a held table; **S5 (GABRA1, GABRA2, GABRA3, GABRA5, GABRB2, GABRB3, GABRG2) has GABRA1, GABRB3 and GABRG2 in the tables extended in P8** → S5. Its sibling S6 (chloride gradient) is the condition under S7 and is not chosen. Disclosure: S5 is close to S7 in family (both act on GABAergic transmission, both conditional on the chloride gradient); the rule, not the closeness, chose it; S5 and S6 were searched in IT41 (P11 family) by the mechanism path only, with no activity read and no qualification.

## Need, inputs, snapshot
Need: NEED-INHIBITORY-HYPOFUNCTION (reduced spontaneous inhibition and PV/GABAergic marker deficit); sign condition: NEED-GABA-CHLORIDE-GRADIENT. Input digests (first 16 hex of SHA-256): `entity_roles_it44.tsv` 08ccbb565b517160; `ladder_it46.tsv` 7e5c821d1e27f1b2; `cell_context_it46.tsv` fc1622cc722de85a; `relations_it41.tsv` 1575988691964ff2. Unlike S7, S5 has **no activity read**: one is made for C2 with `activity_search.py` (public ChEMBL REST, dose-response types, zero spend) and its tables kept in `s5_case/` (a stated addition).

## Arms (same inputs for every arm)
C1 ChEMBL curated mechanism rows by the seven symbols (distinct parent molecules; target record granularity noted, since GABA-A is a pentamer and a record may name a family). C2 + interaction table + the dose-response activity rows. C3 + the ladder rows of S5, the roles, and the context rows. C4 the contextualised combination from the frame below.

## C4 frame (written now, before names)
| Item | Statement |
|---|---|
| Observation | Reduced spontaneous inhibition and a PV/GABAergic marker deficit are carried in the model as one of several explanations of the slice burst phenotype (alternative AB06); not measured as a deficit of synaptic current in the Wwox slices at P13-17. |
| Relation | A positive allosteric modulator of the GABA-A receptor amplifies the existing GABA signal; it adds nothing where there is little GABA and aggravates excitation where GABA is depolarising beyond threshold. |
| Alternatives | (a) bursts are glutamate-driven and inhibition is irrelevant; (b) the inhibition deficit is of interneuron number or output, not of the receptor, so a receptor modulator amplifies a smaller signal; (c) tonic extrasynaptic receptors (delta-containing) matter more than synaptic ones; (d) any effect is generic antiseizure action (benzodiazepine-like drugs act in many epilepsies) and says nothing about WWOX; (e) the sign depends on the chloride gradient (S6, IT46-Q01). |
| Discriminating results | D1 spontaneous and evoked IPSC amplitude and frequency by genotype (is the inhibition deficit real?). D2 a modulator at matched measured cellular effect against an unrelated arm (generic or GABA-specific). D3 the modulator effect read against the measured GABA reversal potential (sign). D4 effect of a tonic-selective against a synaptic-selective modulator (only if such tools are identified; otherwise the question stays open). |
| Where inert or opposite | little GABA (low interneuron output); depolarising beyond threshold; glutamate-driven bursts; sedation-like network suppression with no selectivity. |
| What the held tables can say | GABRG2 is neuron-enriched in the mouse and human tables; GABRA1 and GABRB3 are shared with the P17 oligodendrocyte-precursor class in the mouse table (neuron-enriched in the one human neuron sample): a slice-bath modulator is not neuron-only. GABRA2, GABRA3, GABRA5, GABRB2 are not in any held table (unknown). |

## Predicted difference of the method (written before the counts)
1. The C4 next experiment differs from the C1-C3 one (a modulator arm in the slice): it begins with D1 (is the deficit of synaptic inhibition real?) and D3 (the sign), the same recording programme as IT46-Q01/Q04.
2. The context part adds a statement for 3 of 7 symbols (the slice-bath arm is not neuron-only) and leaves four symbols unknown.
3. The ladder shows many known approved compounds with a role and a next step, and the qualification separates a subunit-resolved record from a family record (a record granularity, not selectivity).
4. The method does not nominate a compound and does not claim that more inhibition helps.

## Outcomes counted as failure
The C4 next experiment equals the C1-C3 one; C4 states a premise the reader finds unsupported; C4 has fewer defensible hypotheses than C3; C4 recovers no molecule or comparison C1-C2 missed **and** adds no premise; the activity read finds nothing beyond the mechanism rows **and** the ladder gives no row a distinct next step (then the added value for this case is nil and is reported).

## Verification perimeter
One blind reader (sonnet, high; no recursion) gets the C4 premises with named sources (reduced inhibition in the Wwox model; the PAM amplification and sign conditionality; the extrasynaptic/delta tonic question; benzodiazepine efficacy as generic antiseizure action; oligodendrocyte-lineage GABA-A expression) and the C1-C3 tables, not my conclusions; returns SUPPORTED / UNSUPPORTED / NOT_REACHED per premise. Excluded: the S6 search itself.
