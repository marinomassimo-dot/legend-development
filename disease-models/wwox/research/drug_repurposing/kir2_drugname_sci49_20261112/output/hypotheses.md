# Hypotheses (generation only; SCI49 package B)

Non-canonical research material. Not medical advice; no dose, schedule, route or recommendation; no compound ranked. Reference genotype class only. Generation is kept apart from checking: a blind verifier will test these, and nothing here is softened to survive review. Novelty classes: (a) new combination for LEGEND (relation between facts already in the repository), (b) novelty against the literature (not checked unless stated), (c) prediction not yet validated. Three hypotheses; one is conditional.

## H1 — a Kir2-family share of the Ba2+-sensitive resting conductance can be attributed with ML133 and a pH control
* Observation (DATO): a Ba2+-sensitive share of resting conductance is about 23 percent in wild-type adult-ish mouse L2/3 neurons (SCI43/SCI44, one 60 uM dose, not an isoform); the Wwox resting conductance is lower by about 28 percent (carried, SCI43); no Kir2 tool was identified before this package (SCI43). ML133 blocks Kir2.1-2.3/2.6 at 1.9-4.0 uM (pH 7.4), spares Kir1.1, 4.1, 7.1 (21615117).
* Mechanistic explanation (IPOTESI): a Kir2-type conductance carries part of the Ba2+ difference and its reduction contributes to the higher Rin; the rest is K2P, other Kir (Kir4.1/5.1 or KATP) or an indirect glial effect.
* Pharmacological lever: block of Kir2 (a discriminator, not a proposal of benefit).
* Compound or probe: ML133 (probe at family level, role in roles.tsv); verified in a primary paper, not in cortical pyramidal neurons.
* Prediction: in wild-type juvenile L2/3 neurons, ML133 at pH 7.4 removes a part (not all) of the Ba2+ difference current and raises Rin; at pH 6.5 the same concentration has no effect; the Ba2+ share is unchanged by pH.
* Discriminating experiment: Rin and difference-current measurements with Ba2+ alone, ML133 alone at pH 7.4 and at pH 6.5, then Ba2+ on top, in the same neurons (OQ1).
* Expectation under H1: ML133 effect pH-dependent and smaller than the Ba2+ effect, additive-to-occluded with Ba2+. Under the strongest alternative (a K2P/other-Kir Ba2+ share): ML133 effect small or absent at pH 7.4, or equal at both pH values (off-target), and Ba2+ still removes a large share.
* Would reject it: no ML133 effect at pH 7.4 beyond vehicle with a Ba2+ effect present; or an ML133 effect independent of pH.
* Decision it changes: whether the first INV-18 arm needs a Kir2-directed step (ladder 2b) or only a K2P/high-Ba2+ step; whether KH1 stays "no tool".
* Premise unresolved: none for the test itself (a blocker); the direction of benefit remains unresolved and is not used.
* Transfer limits: recombinant HEK293 potency; ML133 neuron evidence is an abstract on dentate granule cells (40789514); hERG about 5 uM at pH 8.5 in a deposit and Kir6.2 7.7 uM mean a window of a few fold; species mouse; age P13-P17 not measured in any retrieved source; disease Wwox not tested.
* Counter-evidence kept visible: little discrimination among Kir2 isoforms; high protein binding and clearance; pH affects the drug's access (inside-out IC50 is nearly pH-independent); pH acts on other channels.
* Novelty: (a) yes (SCI43 KH1 plus SCI44 share plus this probe); (b) not checked; (c) yes, unvalidated.

## H2 — a Kir2.1-restricted activator changes the outward-current region near rest, not the inward conductance (conditional)
* Observation (DATO): flecainide raises IKir2.1 by 22 percent at -120 mV and 53.9 percent at -50 mV in CHO cells, via Cys311 and lower polyamine affinity; not Kir2.2/2.3 (20713726). Zacopride raises the outward component under hypoxia (28542320).
* Mechanistic explanation (IPOTESI): if the Wwox rest is depolarised by a Ba2+-sensitive deficit, an agent that relieves polyamine block raises the outward current near rest more than the inward one.
* Lever and compound: Kir2.1 activation; flecainide named only as a mechanism comparator (conditional); zacopride not interpretable.
* Prediction: a Cys311-dependent shift of the Ba2+-sensitive current toward positive potentials with little change of Rin at hyperpolarised potentials.
* Experiment: I-V of the Ba2+ difference current before and after the agent in WT neurons; compare Rin at -90 and at -60 mV.
* Under H2: gain mostly above EK. Under the alternative (Nav block or other actions dominate): spike threshold and firing change without a change of the difference current.
* Would reject it: no change of the Ba2+ difference current, or a change that is Kir2.1-independent (no effect of ML133 occlusion).
* Decision it changes: whether any activator can be used to test KH1 as a mechanism; premise unresolved: direction of benefit (not assumed); so this stays conditional.
* Transfer limits: CHO homomeric Kir2.1 only; heteromers in neurons unknown; flecainide also acts on other channels (recollection, not read); neuron data absent.
* Counter-evidence: flecainide is a documented proarrhythmic in some cardiac contexts (not read here); Kir2.1 only.
* Novelty: (a) yes, weak; (b) not checked; (c) yes.

## H3 — part of the slice Ba2+ effect on neuronal resting properties is indirect (Kir4.1 and extracellular K+)
* Observation (DATO): VU0134992 is above 30-fold selective for Kir4.1 over Kir2.1/2.2/1.1 in Tl+ flux (abstract, 29895592); ML133 is weak on Kir4.1 (76 uM). Bath Ba2+ acts on all of them.
* Explanation (IPOTESI): bath Ba2+ blocks astrocytic Kir4.1, slows K+ buffering and depolarises neurons indirectly, so a bath-Ba2+ share is not a purely neuronal conductance.
* Lever and probe: Kir4.1 block with VU0134992 (probe for Kir4.1; abstract-level reading) as a discriminator.
* Prediction: a Kir4.1 probe changes neuronal Vm or Rin modestly and reduces the later Ba2+ effect; ML133 does not occlude that part.
* Experiment: Ba2+ bath versus Ba2+ in the pipette (intracellular) versus Kir4.1 probe, same neurons (OQ5).
* Under H3: part of the Ba2+ depolarisation is lost with a Kir4.1 probe. Under the alternative: Kir4.1 probe has no effect on the neuron.
* Would reject it: no change of neuronal Vm or Rin with the Kir4.1 probe.
* Decision it changes: whether the 23 percent figure can be read as neuronal.
* Premise unresolved: none; transfer limits: recombinant Tl+ flux; no slice data; abstract only.
* Novelty: (a) yes; (b) not checked; (c) yes.

## Adjacent literature (stated with transfer limits)
Kir2.1 loss or gain in Andersen-Tawil or short QT contexts (cardiac, CHO and cardiomyocyte data above) informs the pharmacology of the channel only, not Wwox cortex; Kir4.1 astrocytic pharmacology (VU0134992 paper) informs H3 only; mTOR-pathway mouse models report Ba2+-sensitive currents in L2/3 mPFC pyramidal neurons at P26-P51 and cite Kir2.1 overexpression as a genetic arm (38411613, copied).
