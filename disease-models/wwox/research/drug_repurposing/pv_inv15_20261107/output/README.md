# INV-15 delta: PV interneurons, inhibitory function, perineuronal nets

Producer `pv-p`, 2026-11-08. Non-canonical, not medical advice. Reference genotype class only. Tables: `evidence.tsv`, `alternatives.tsv`, `currents.tsv`, `experiment.tsv`, `queries.tsv`; receipts in `receipts/INDEX.tsv`.

## Answer first

Neither "PV loss shown" nor "no PV data" is right. PV-marker data exist in the global knockout hippocampus; none exist for PV cells in the neuron-targeted model, whose inhibitory currents come from unidentified cells. The hyaluronan-net lead has no WWOX bridge in anything read. The cheapest decisive step is one per-animal, same-section comparison, not a drug.

## DATO (acquired, with row ids in `evidence.tsv`)

- Global knockout, hippocampus, 2 weeks, PMID 30290271: PV-positive cells 44 percent lower overall (n = 7 and 7), some areas with none; NPY-positive lower in dentate gyrus only (30 percent); combined GAD65/67 protein lower (n = 5 and 5) (P01 to P06). Optical-fractionator counts estimate marker-positive cells; no death, lineage or pan-GABAergic count exists (P04, P05).
- Neuron-targeted model (Synapsin-Cre), cortex layer II/III, 13 to 17 days, PMID 34634460: sIPSC amplitude 57.3 to 27.5 pA, frequency lower (C05). mIPSC was not recorded (C04); IPSCs used a 140 mM KCl internal (C06) and no antagonist is named for isolation (C07). Interneurons: 5 cells from 4 animals against 6 from 5, not PV-identified (C13); firing unchanged, spike amplitude lower (C14).
- Declared counts do not add up: sIPSC controls 14 cells from 7 animals against components of 4 + 4 animals; sEPSC controls 18 cells from 10 animals against components of 31 cells from 13 animals (C08 to C10). p values near 1e-100 from 9 against 14 cells imply events as units (C11, C12).
- The paper's "postsynaptic" wording concerns glutamatergic mEPSCs (C03). For inhibition its own discussion leaves pre- or postsynaptic change and fewer interneurons open (C15).
- PMID 27845895: the death readout needs an overexpressed complex (H01, H02); the authors tie neuronal protection to less HYAL2/WWOX/SMAD4 signalling (H04). The review PMID 42812881 contains no WWOX item (R07).
- Pilot and NB-4 corrections stand: one pool per arm, Pvalb 70 and 37 UMI, undecidable (B01, B02); 36 percent is an adult whole-brain reporter value carried to no allele, age, region or PV cell (B03, B04); the poster has no result (B06).

## INFERENZA

- A marker count cannot say whether cells are gone, silent for PV, or not yet PV-positive; PV and the nets mature in the same window (R01).
- The amplitude change cannot be given to the postsynaptic side: fewer or weaker presynaptic cells, release, input composition, recording conditions and contamination by excitatory events all fit (`alternatives.tsv`, A1 to A8).
- No chloride gradient follows from these recordings. The three systems (global hippocampus counts, conditional cortex currents, pooled transcripts) are not replicates of one endpoint.

## IPOTESI (with the test that discriminates)

- Priority experiment (`experiment.tsv`, X1 to X6): Synapsin-Cre Wwox floxed animals against Cre-positive littermates (heterozygotes separate), P14 and P17, cortex L2/3 and hippocampus, on the same sections: PV protein and Pvalb mRNA, Gad1 and a second lineage marker as denominator, NeuN, Wwox, tdTomato (the reporter allele is in the conditional models of the NB-4 source). Unit: animal. Decision: lower lineage density means fewer cells; unchanged density with lower PV means expression or maturation; both unchanged sends the question to identified-cell physiology. It changes whether a function-first probe or a counts-first line continues.
- Pharmacological levers stay hypotheses with separate conditions (X8): a Kv3 modulator needs a Kv3-sensitive deficit in identified fast-spiking cells; a GABA-A modulator needs a postsynaptic deficit and a known chloride gradient; an excitatory-input modulator is not selective potentiation of interneurons. A non-cell-autonomous defect can still be probed. Syn1-Cre uniformity is not assumed; a PV-Cre design depends on the Pvalb program and is not first.
- Net arm (X7, X9): only conditional on X4 and only where controls show nets. A WWOX-net link is refuted if net per PV cell does not differ at a measurable age, if WFA differences are explained by PV number, if matrix genes and proteins do not differ, or if the HYAL2 axis changes signalling but not the net.

## NON RISOLTO

- Missing bridge: no primary linking WWOX to hyaluronan synthesis, link protein or nets (PubMed Q3, Q4: 0 hits; Europe PMC Q7: titles only, none). The one lead is Has3 loss giving seizures through extracellular space volume (R05, A01, A02), abstract-level only and independent of PV and nets; it is a different mechanism, not support.
- Whether PV cells are recombined, lost, or merely PV-low in the neuron-targeted model; the Pvalb transcript in the neurosphere supplement was not re-checked.

## Delta for consumers

- INV-15 (`../../ranking_it8_p9_20261029/investigations_it20.tsv`): replace "PV loss" wording by marker-positive count, global knockout, hippocampus, 2 weeks; add the three-system separation and the experiment. Rank untouched.
- `../../nb4_delta_20261107/CONSUMER_NOTE.md` stays authoritative on the reporter value; this delta adds that its recombination read-out is the X4 tdTomato-in-PV item.
- Any consumer text that calls the inhibitory deficit of PMID 34634460 postsynaptic, or implies that PV cells were recorded, is withdrawn.

## Sources and depth

New: PMID 42812881 partial full text (sections in the receipt); PMID 24790187 abstract only (PMC tool empty, Europe PMC 500, E-utilities stub). Reopened: 30290271 and 34634460 (held XML, decisive passages; figure images not viewed); 27845895 not reopened, quoted from its receipt text. Stage 2 not used. Europe PMC search returned 503 twice (Q6, Q8), not retried; no access challenge met.

## Added after the independent audit (`../verify/audit_p.md`: 44 rows, 42 supported, 2 undershoot, 1 unverifiable clause)

H01 and H04 limits corrected (27845895 has a rat brain-injury experiment, Fig 10, with the Hyal-2/WWOX complex accumulating in nuclei of apoptotic neurons: more evidence against a protective-activation lead; the same group's 2016 review says over-accumulation in the nucleus causes neuronal death, abstract only). P01: the CA3 significance statement concerns a panel nobody viewed (Cloudflare 403). The inconsistent declared counts in 34634460 are confirmed (4+4=8 animals against 7; 31 cells and 13 animals against 18 and 10), and the event-as-unit conclusion is arithmetic, not inference: a two-sample KS test cannot reach p below 2/C(n+m,n) with one value per cell (2.4e-6 for 14 v 9; 1.1e-5 for 10 v 10; 1.7e-4 for 7 v 9), yet the reported p values are far below. Further audit points: Gad1 is a weak denominator; more than half of control Pvalb UMI sit in doublet-flagged nuclei; interneuron AP half-width is not wider; heterozygotes differ from wild type in several measures but are pooled as controls; mEPSC frequency falls under TTX while the heading says "postsynaptic, not presynaptic"; the paper gives no criterion for recognising interneurons and its Discussion says interneuron AP properties are unchanged against its own Table 1; experiment X3 wording (layer II/III neocortex only), X2 (tdTomato stated only for the 2021 paper's animals; record the breeding direction), X6 (a branch for lineage density and PV fraction both lower), X8 (a GABA-A positive modulator cannot separate a postsynaptic deficit from a nonspecific action). Absence claim H4: PubMed 0 hits stands; Europe PMC REST answered HTTP 200 every time in the audit (no 503) and WWOX AND perineuronal gives 4 hits, none a data link (a figure-caption co-mention in a 2025 hyaluronan review; two conference abstract books unopened). The NB-4 delta statement on recombination is confirmed. Not checked by anyone: figures of the PV papers, the supplement tables of the neurosphere paper (empty folder), the pilot's result tables. The corrections were rechecked by comparison with the audit text, not by a second blind pass.
