# Levetiracetam, endogenous zinc and attainable exposure
context_policy: QUESTION_DRIVEN

The opening comparison found more Slc30a3 transcript in two pooled WWOX neuronal classes and a hippocampal culture response at 30 µM levetiracetam with 15 µM added zinc. The questions here are whether endogenous zinc has that receptor-level effect and whether the drug reaches that extracellular concentration. The published 30 µM observation is a reference point for complete reversal under one challenge. A lower exposure may still have activity.

## Circuit comparison

| Preparation and readout | What changes | What the comparison can distinguish |
|---|---|---|
| Ruiz et al., guinea pig, 3–4 weeks. Same CA3 pyramidal neuron, dentate versus stratum radiatum input. Results p. 1093, Figs. 2–3, Discussion p. 1094. | Chelation increased the dentate-evoked inhibitory current by 26.5 ± 6.3% with TPEN (n=9) and 31.9 ± 6.9% with extracellular Ca-EDTA (n=8). Neither increased the radiatum response. Added zinc depressed both pathways. | Input-specific access to extracellular zinc is plausible. Tonic inhibition fits these data. A transient at the receptor during a physiological train was unmeasured. Anatomical observations in this paper used rat tissue. [Original study](https://doi.org/10.1152/jn.00755.2003) |
| Molnár and Nadler, rat after pilocarpine status epilepticus, recurrent mossy fibers and direct GABA photorelease on proximal granule-cell dendrites. Selected publisher-indexed Results passages and abstract, limited coverage. | Applied zinc depressed the muscimol response by about 23% under modified bath chemistry. The authors report no detectable zinc-attributable depression of the direct GABA response with the tested trains. | Local agonist sensitivity can coexist with inadequate spillover in the tested region. A spatially restricted event could escape this measurement. Age and detection limits were not verified in the accessible passages. [Original study](https://doi.org/10.1152/jn.2001.85.5.1932) |
| Grauert et al., rat, postnatal days 20–40. Granule-cell evoked currents and interneuron calcium currents. Results accompanying Figs. 1E, 2 and 6. | Chelation increased the stratum lucidum-evoked inhibitory current by 31.6 ± 5.2% (n=20). The change on a nickel background was a 1.6 ± 2.5% reduction (n=11). Other T-type antagonists also occluded facilitation. Chelation increased low-voltage activated calcium current in interneurons. | An evoked current can increase through presynaptic interneuron excitability. Blocker selectivity and baseline depression constrain the inference. The authors identified a ZnT3-null comparison as missing. [Original study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3903352/) |

The same recording sign can therefore arise from at least two cellular sites. None of the three experiments paired levetiracetam with endogenous zinc in WWOX. None quantified the free zinc waveform at the implicated inhibitory receptor. Nominal added zinc and a chelator concentration cannot be used to calculate it.

## Human compartment comparison

The nominal culture reference of 30 µM is 5.1063 µg/mL for levetiracetam (170.21 g/mol). Zampella et al. used HPLC on serial ventricular CSF in acute severe adult brain injury. Table 2 contains six participants with baseline, one-hour and six-hour samples. Five of six exceeded 30 µM at one hour (median 56.11 µM) and six at six hours (median 53.76 µM). Subtracting each person's baseline preserved these counts. There was no seizure-outcome assessment. This compares concentrations across preparations and does not establish a therapeutic threshold. Reproduce the aggregate with `python3 csf.py zampella.xml` using the linked JATS source. [Primary study](https://doi.org/10.7759/cureus.5784) · [JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6825487/fullTextXML) · [Computed timepoints](csf.tsv)

Rambeck et al. measured CSF and estimated extracellular drug in temporal neocortex during epilepsy surgery. Tables 1, 2 and 3B identify three levetiracetam cases aged 32, 39 and 44. Their CSF ultrafiltrate concentrations all exceeded 30 µM. Compare with the person-specific cortical estimates below. Convert each source value in µg/mL to µM by multiplying by 1000/170.21. Catheters are nested within each person.

| Source case | CSF ultrafiltrate, µg/mL | Cortical extracellular estimates, µg/mL, in catheter order | Sites at or above 30 µM |
|---|---:|---|---:|
| 6 | 24.47 | 5.25, 5.57 | 2/2 |
| 15 | 24.82 | 10.45, 8.73 | 2/2 |
| 17 | 10.92 | 0.14, 1.61, 2.43, 1.17 | 0/4 |

The largest estimate in case 17 was 14.28 µM despite a CSF value of 64.16 µM. Case 6 lay close to the comparison point. Values depend on recovery estimated in vitro with a temperature correction. Some recoveries were imputed, and the first probe in case 17 was at the detection limit. Even omitting that probe, the direction of the case 17 comparison persists. These surgical measurements support attainable local concentrations in some adults and show why a CSF value alone cannot identify cortical exposure in an individual child. [Primary study, Tables 1–3B and Fig. 2](https://pubmed.ncbi.nlm.nih.gov/16650134/)

## Decision and next comparison

Lower the priority of a **general postsynaptic zinc-rescue mechanism**. Retain the localized CA3 hypothesis and the independent possibility of presynaptic seizure suppression. In a circuit with measured free zinc, the discriminating observation is selective recovery of the direct GABA response at locally attainable levetiracetam exposure, with preservation of native-chloride inhibition and physiological firing. Compare tonic and stimulus-locked zinc separately. A change confined to evoked transmission is insufficient, including when a T-type channel blocker abolishes it. All existing patient exposure comparisons here are adult. There is no drug-by-genotype functional rescue or evidence of improved WWOX development in this comparison.

Keep levetiracetam active for a bounded final check of pediatric efficacy and clinical attribution. Extract seizure type, age, duration and denominator from the blinded infant adjunctive trial and compare them with timed WWOX drug changes already audited in the laboratory. Determine whether any stable-background, EEG-linked exposure changes the symptomatic decision. If it does not, park for an unselected trial and retain the defined circuit reopening criterion.
