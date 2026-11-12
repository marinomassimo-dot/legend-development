# Levers: what the data make useful (SCI47 package A, producer P)

Non-canonical research material. Not medical advice. No dose, schedule, route, ranking or recommendation; no prediction of developmental benefit. Reference genotype class only. Table: `levers.tsv` (6 rows). Labels: measured / authors' interpretation / inferred / reused (reader finding at stated depth) / transferred (other system, named).

## Reading budget
New sources read: 1 (PMID 34634460, Breton 2021: full text, legends, Methods, Table 1, Supplement text and figures; Figures 4, 6 and Supplementary Figures S2, S4 opened as images). Everything about other papers is reused from the IT46 readers' notes (Yuan 2019 E_GABA, vigabatrin/tiagabine database rows, ganaxolone, benzodiazepine and NKCC1 abstracts, P8 RNA tables) at their stated depth, not re-read. Budget 8; used 1.

## Which lever each explanation makes useful (protocol-level; no single cause is chosen)
| If the recordings show | Explanation | Lever that becomes interpretable | Lever that does not |
|---|---|---|---|
| mIPSC amplitude down, agonist response normal | E2 (supply per event) | L1 GABA availability | L2 starts from normal receptors |
| mIPSC amplitude down, agonist response down | E3 (receptor response) | L2, if physiological-chloride deficit is confirmed | L1 raises a signal onto fewer receptors |
| mIPSC frequency down, amplitude normal | E1 (fewer or less active inputs) | none at the synapse; interneuron-side question | L1 and L2 act on a smaller input set |
| E_GABA at or above threshold in KO, not in control | E4 | chloride-gated sign for L1/L2; transport only as a measurement first | boosting GABA is conditional and may aggravate |
| deficit only in bursting slices or only with age | E5 | levers on the burst itself (L4, L5) | L1/L2 treat a consequence |
| deficit scales with Cm or Rs | E6 | none (recording artefact) | all |
Nothing in PMID 34634460 chooses a row (matrix O01-O06).

## Kept, with the reason
* **L1 GABA availability (conditional).** Kept because a presynaptic or content-per-event reading (E2) is compatible with a halved sIPSC amplitude and a small frequency fall. It is gated by three measurements that do not exist: mIPSC, agonist response, E_GABA. The acute arm uses a reversible agent; the irreversible transaminase inactivator cannot be titrated in an acute slice (reused, IT46 reader). Not neuron-only (astrocytic uptake, transferred P7 RNA).
* **L2 Postsynaptic GABA-A modulation (conditional).** Kept for E3 only. It amplifies existing GABA signalling (reused). Its rationale beyond general anticonvulsant action exists only if the receptor deficit is confirmed in physiological chloride (P6). Benzodiazepines in the repository's WWOX cases are co-therapy with two single-child benefit reports and no instrument (reused).
* **L4 NMDAR-dependent excitation (comparator and lever).** Kept because it is the only pharmacological arm with a direct measured effect on the burst endpoint in Wwox slices (d-APV 50 uM abolished bursts; 5 slices, 3 animals). It does not discriminate inhibitory explanations (O12) and is generic, so its role is the functional comparator, with a submaximal arm.
* **L5 K+/Ih conductance (conditional; the lever outside GABA).** Kept because Table 1 gives measured passive correlates (input resistance 102.88 to 143.03 Mohm, rest -79.25 to -73.62 mV, sag and rebound larger) in the cells of the IPSC recordings, so the blocker-sensitive difference current can be read in the same cells. Ih blockade is not proposed: the authors cite a report where it worsened seizure-like events.

## Dropped
* **L3 chloride transport as an arm.** The only datum is the one the source cannot supply (the pipette fixed E_Cl). Kept as the measurement E_GABA, not as an arm. KCC2 neuron-enriched and NKCC1 not neuron-enriched in the held RNA (transferred, P7).
* **L6 gap junction/pannexin.** Carbenoxolone is non-specific and not reversible; brilliant blue FCF had no effect; the repository withdrew the gap-junction half of the claim.

## Already-used antiseizure drugs
If a GABA-transaminase inactivator or a benzodiazepine-site drug is the compound under test, the rationale adds nothing over general anticonvulsant action until (i) the deficit is confirmed in physiological chloride with identified events and (ii) the matrix row that points to supply (E2) or receptor (E3) is shown. A lower burst incidence under such a drug would be read against a matched non-GABAergic arm and a non-Wwox hyperexcitable preparation.

## Counter-evidence kept in view
GABA-raising agents can aggravate absence-type seizures; depolarising GABA at P11 aggravated events in one animal model; the neonatal NKCC1 add-on trials were negative or inconclusive; heterozygous slices burst in 4/23 while inhibitory data are pooled; an Ih blocker worsened events in one preparation; the 18% frequency fall has no animal-level test.
