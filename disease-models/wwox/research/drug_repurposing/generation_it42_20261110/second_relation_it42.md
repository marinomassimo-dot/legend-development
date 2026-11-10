# IT42 P5 — the second relation, chosen and framed before any compound is looked at

Non-canonical working note. Not medical advice. Written 2026-11-10, before the search; a later change is a dated addendum, not an edit.

## Choice

**S7: raising available GABA by blocking GABA reuptake (GAT-1, SLC6A1) or GABA breakdown (GABA transaminase, ABAT), as opposed to potentiating the GABA-A receptor (S5, already censused in IT41).** Reason: it discriminates a WWOX-model explanation that S5 cannot. The model holds a halved inhibitory current amplitude and reduced inhibitory frequency in the neuron-specific knockout slice (alternative AB06, reduced inhibition). A lever that raises GABA availability helps only if the deficit is on the **supply side** (less GABA released or made); it does nothing for a **postsynaptic or chloride-gradient** deficit, which S5 and S6 address. So the result separates two explanations of the same observation.

## Frame

| Item | Statement |
|---|---|
| Hypothesised function of the perturbation | Increase synaptic and extrasynaptic GABA tone without changing glutamate-receptor currents. IPOTESI. |
| Direction, as known or conditional | **Conditional.** In cells with a depolarising GABA response (immature neurons, high intracellular chloride) more GABA can excite; in P13–P17 mouse cortex the response is mostly hyperpolarising but the chloride state of the Wwox preparation is unmeasured. A mixed literature on vigabatrin in the module's own records says the direction cannot be assumed. |
| Cellular and maturational context | Neuron-specific knockout slices P13–P17, layer II/III; human organoid and immature neurons are the other context and differ in chloride gradient. |
| Compensatory alternative | A homeostatic change in tonic inhibition or in GAT-1 expression could mask or reverse the effect; a raised GABA tone could also shift the Mg2+ block through hyperpolarisation, changing NMDA-receptor dependence without a receptor change. |
| Endpoint that separates benefit, general suppression and worsening | Burst incidence **and** a matched-effect control that lowers bursts by a non-GABAergic route to the same measured fraction (general suppression); an evoked-IPSC amplitude and E/I ratio (supply versus response); the chloride reversal potential (direction). Worsening = bursts rise or the delayed evoked response rises. |
| What is verifiable in silico | Which molecules the catalogue holds for SLC6A1 and ABAT with action, species and assay text; which rows are substrates or unrelated; which records carry a label conflict; the evidence level per gene from Harness's identity route. |
| What needs a measurement | Chloride state, evoked IPSC, a supply-versus-response test in the Wwox slice. |

## What the output may be

A compound, a comparator, a circumscribed generative question, or an abstention — whichever the data support. No composite is chosen in advance, and no special code is written for this relation: it enters `relations_it41.tsv` as rows and runs through `action_search.py` and the same qualification columns as S1.
