# Audit A (abstract-level; full-text routes returned HTTP 500 / JS shell, so no full text was read)

| # | Verdict | Locator | Source says more/less |
|---|---|---|---|
| 1 | UNDERSHOOT (relation only partly stated; mechanism and voltage dependence NOT_IN_SOURCE) | PMID 21593326: "regulating both membrane potential and input resistance"; PMID 24756635: "influencing the membrane resistance and resting membrane potential" | Both abstracts say Ih sets input/membrane resistance in cortical/hippocampal pyramidal neurons. Neither states direction (larger Ih -> lower Rin), the resting-conductance mechanism, or voltage range. PMID 21795624 gives direction empirically (reduced Ih with higher Rin, reversed by ZD7288). Voltage dependence not checked: Ih is only active near and below rest, so the relation holds at voltages where HCN is open, not generally. This is my background knowledge, not from a source. |
| 2 | SUPPORTED | "L5 pyramidal neurons in lesioned animals had hyperpolarized resting membrane potentials, increased input resistances and reduced voltage sag" | Rat freeze-lesion cortical dysplasia, whole-cell recording in layer 5 pyramidal neurons (slices). Differences became nonsignificant after ZD7288. EPSP summation and intrinsic excitability increased near the lesion. Voltage-dye imaging also done. "Opposite phenotype" holds for Rin, sag and excitability (opposite of Wwox KO: larger sag, depolarised), but RMP is hyperpolarised here. |
| 3 | SUPPORTED, with a scope caveat | "Phenytoin, lamotrigine, and retigabine significantly increased ECoG spike frequency" | In vivo, Hcn1 M294L heterozygous knock-in mouse, ECoG spike frequency (not single-cell spiking). Retigabine seizures in 4/9 mice (full text). Levetiracetam, diazepam, valproate and ethosuximide significantly reduced spiking; carbamazepine showed a trend to increase. So "spiking" means epileptiform ECoG spikes. |
| 4 | OVERSHOOT if stated as general gating, SUPPORTED for mode-shifting | "Mode-shifting in HCN1 channels was insensitive to cholesterol manipulation, while HCN2 and HCN4 were strongly affected" | Human isoforms in CHO cells, patch clamp. Manipulation: depletion by MβCD or mevastatin, enrichment by MβCD/cholesterol. Readouts: gating kinetics (isoform-specific), mode-shifting, plasma-membrane trafficking. HCN1 was not unaffected overall: the abstract says trafficking was affected differentially between isoforms. |
| 5 | SUPPORTED in all parts | "depolarized and demonstrated increased action potential frequency, sag current, and post-inhibitory rebound"; "NMDAR and gap junction dependent" | Layer II/III pyramidal neurons, neuron-specific Wwox deletion vs het/WT. EPSC amplitude up; IPSC frequency AND amplitude down. Bursts were in neocortex (propagating L II/III to L V). Abstract does not give magnitudes or n. "Neocortical" is the slice region; the abstract does not name a pharmacology. |

Plain sample
- (a) PMID 24756635: SUPPORTED, with a nuance. Shah 2014 J Physiol review "Cortical HCN channels: function, trafficking and plasticity"; TRIP8b trafficking is one part, the topic is broader.
- (b) PMID 21593326: topic is NOT HCN regulation in general. It is Lewis et al. 2011 J Neurosci: TRIP8b knockout impairs hippocampal Ih localization and function and gives antidepressant-like behaviour in mice.

Omissions that matter
- Item 1 has no source that states the conductance mechanism or the voltage range. Treat as supported only at the "Ih regulates input resistance" level; direction comes from item 2.
- In item 2, resting potential is hyperpolarised in dysplasia; do not call the whole phenotype the mirror of the Wwox KO.
- In item 3, readout is ECoG spike frequency in vivo, not cellular firing; the retigabine rise is not tied to a cellular mechanism in the abstract.

Depth reached: abstracts via PubMed tools for all six PMIDs; full text only for PMID 36300716 (Europe PMC) for item 3 details. Shah 2014 and Albertson full text were not reachable (HTTP 500 / PMC blocked).
Setting: claude-sonnet-5-5, low reasoning effort, read-only except this file, no e-mail sent, no agents started.
