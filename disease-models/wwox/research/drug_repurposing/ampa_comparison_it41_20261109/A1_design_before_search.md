# A1 — the AMPA comparison, fixed before any source was opened (2026-11-09)

Non-canonical research material. Not medical advice; no dose, schedule or route. Reference genotype class only. This file was committed before the producer was dispatched; it states what the comparison must achieve so that a source can be judged against it, not the reverse. Task record `ledger/tasks/orchestrator/ORCH-IT41-20261109.json`. Built on `ampa_nmda_discrim_20261108/` (BH1, BE0, BE1, BE4, matrix rows M07, M08, M14, M15, alternatives AB01, AB04, AB14) and `nmda_composition_discrim_20261109/`.

## The question

Which pharmacological comparison would test whether the spontaneous bursts of the neuron-specific Wwox-deleted neocortical slice depend on AMPA-receptor transmission, while keeping the competing explanations that are already identified (NMDAR-regenerative with a GluN2B or GluN2A part; general loss of excitatory drive; state or recording-condition dependence; kainate-receptor contribution)?

## Required action (DATO about the tool class is not assumed; IPOTESI about the design)

* Reduce fast AMPA/kainate-receptor-mediated transmission in the slice by a **measured** fraction (fast evoked EPSC or fEPSP slope; mEPSC at -70 mV), not a nominal concentration, before the burst is judged.
* Keep the NMDAR-mediated current **unchanged by the tool itself**, measured at the working concentration in the same preparation (a tool that also lowers NMDAR current cannot answer an AMPA question).
* Read burst incidence, frequency, duration and burst-onset current at the verified block, then add d-APV only if bursts persist (order rule BE4).
* Compare with d-APV on the same x-axes (percent of evoked charge, of peak current or fEPSP slope, of recruited cells removed), with a receptor-agnostic release-reducing control (M08).

## Preparation and stage that make a source relevant

Acute neocortical slices, layer II/III pyramidal cells, mouse P13-P17, 35 C, 3.5 mM K+ and 1.3 mM Mg2+ in the incubation medium (34634460); recording Mg2+ not stated. A source on cultured neurons, recombinant receptors, adult tissue or another region is **transfer** and is labelled so. A primary mechanism or selectivity paper is relevant for what the drug does at the receptor; only a slice paper bears on onset, washout and verification in tissue.

## What the block control must demonstrate

1. The fast AMPA/kainate component is reduced to a pre-specified fraction (a design value of about 90 percent has no source and stays a design value; the achieved block is reported as a variable) and has reached steady state (time course measured, not assumed).
2. NMDAR EPSC (isolated at a depolarised potential or in a separate set of cells) is not reduced at that concentration.
3. Intrinsic properties (resting potential, input resistance, spike width) are not changed by the tool; a tool that moves them imitates a general cut of drive.
4. The block is stated as surmountable (competitive) or not (noncompetitive), because glutamate rises inside a burst and a surmountable block weakens exactly when the burst is strongest. d-APV is competitive; a matched-effect comparison between two surmountable tools shares that weakness, between a surmountable and a non-surmountable tool it does not.
5. Kainate-receptor involvement is either separated by the tool's measured AMPA-over-kainate window at the working concentration, or stated as not separated.

## What a result would NOT separate (kept from the earlier packages)

* **Burst abolished after a verified AMPA block** does not distinguish an AMPAR-led drive from an NMDAR-regenerative burst whose depolarising support (relief of Mg2+ block) came from AMPAR current: AMPA block can remove the functional context that makes NMDAR dependence possible. It does not separate presynaptic from postsynaptic loss, does not separate AMPA from kainate receptors unless the tool's window is measured, and is predicted by general loss of drive as well.
* **Bursts persisting under a verified, near-complete block** is the informative outcome for the AMPA-led reading (it removes it for this preparation); it still does not show NMDAR dependence, and persistence at a partial block says nothing.
* A drug response of the burst does not show that the target is altered in Wwox.
* Recording Mg2+ and K+ are not fixed by any of this (M01, M14).

## Decisions that a better source would change

1. Which tool is the "verified-block" tool: a competitive one (NBQX) or a noncompetitive one (a 2,3-benzodiazepine, or perampanel already read in culture); and whether a pair of AMPA tools is a pair of independent mechanisms or one site seen twice (the lesson of the ifenprodil-site NAMs in `nmda_composition_discrim_20261109/`).
2. Whether the matched-effect comparison with d-APV (M08) is read between like tools (both surmountable) or unlike tools, and so how a coincident or separated pair of curves is read.
3. Whether the working concentration and time to steady block can be pre-specified from a tissue source or must be measured (BE1).
4. Whether the AMPA-over-kainate window of the chosen tool is wide enough to name the arm "AMPA" rather than "AMPA/kainate".
5. Whether any tool in the module should leave the arm (for example a tool whose catalogue record is not the compound named) or whether a small alternative with a different profile is justified (rule A3 below).

## Rule for an alternative (A3)

An alternative is searched for only if the options already known (NBQX, 2,3-benzodiazepines, perampanel) carry a limit that defeats one of the five demonstrations above, and the search is by the **missing property** (for example: noncompetitive, AMPA-over-kainate window quantified in the same paper, reversible within minutes in tissue, no action on NMDAR or GABA-A at the working concentration, a slice precedent), not by the disease name. "More potent" or "newer" is not a reason. A new molecule is not required; if one appears, the reasoning that produced it and a check of LEGEND for it are recorded.

## Measurements that stay with the Wwox preparation

Fast-EPSC block fraction and time to steady state; NMDAR EPSC at the working concentration; intrinsic properties under the tool; the d-APV abolition threshold; the matched-effect curves on two metrics; recording Mg2+ and K+. No literature stands in for these.
