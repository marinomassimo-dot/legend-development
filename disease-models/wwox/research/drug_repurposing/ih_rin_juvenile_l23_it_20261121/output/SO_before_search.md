# SO_before_search - Ih-blocker effect on resting Rin, juvenile rodent L2/3 pyramidal (IT, 2026-11-21)

Written before the first retrieval call of this package (the earlier IT48-Q01 package read one thesis; nothing else has been searched for this question). Producer: model sonnet, effort high (as stated at dispatch). Reference genotype class only; no dose, no recommendation, no agent nominated.

## Question
In wild-type rodent neocortical layer 2/3 pyramidal neurons at about P13-P17 (acute slices), by how much does an HCN/Ih blocker (ZD7288, cilobradine, zatebradine, ivabradine) or genetic HCN loss change resting input resistance (or input conductance, or holding current near rest)? Report as share of input conductance, 1 - Rin_before/Rin_after, labelled DERIVED when computed from group means.

## FOUND (a qualifying source) - all must hold
1. Rodent neocortex, layer 2/3 pyramidal cells (layer 2 alone or "superficial layers" = near-miss, recorded but not counted).
2. Age window overlapping P13-P17 stated for the cells used (a group label alone, e.g. "p14" inside p8-p45, is recorded as a weaker age statement and flagged).
3. An HCN blocker or HCN1/HCN2 knockout compared before/after or against wild type, with numbers from which a Rin, conductance or holding-current change near rest is read.
4. Read in full text (Methods and the Results lines). Recorded per source: blocker, concentration, TTX, pipette solution (K-gluconate or K-methylsulfate), temperature, small-step ratio or fit.
Value only in a figure or Extended Data = "figure-only, unread" unless figure geometry is measured (method stated).

## Prediction fixed before retrieval
Thesis lead (Fucke 2008): ZD7288 50 uM, p14, Rin 157 to 213 MOhm, derived share 0.26 (n 6 cells). My prior expectation for independent sources: shares in the range 0.10 to 0.40 (wide), most likely 0.15 to 0.30, because published L2/3 and L5 cortical pyramidal data give a few-mV sag and a 10-30% Rin rise with blockers; the prior is a prediction to be tested, not evidence.

## Decision rule (from the brief)
- Thesis value outlier / not reproducible: two independent qualifying sources (different laboratories) with share <= 0.10 or >= 0.40.
- Supported: the shares of independent qualifying sources lie within 0.15 to 0.35.
- Fewer than two independent qualifying sources by two routes: the thesis stays one provisional lead; answer "no second source found", stated as two-route, never as proof.
- Mixed (one inside, one outside, or shares between the bands, e.g. 0.10-0.15 or 0.35-0.40): reported as mixed, no verdict.
- Independence: different laboratory (senior author/institution); same-laboratory papers count once.

## Stop rule
Stop when two independent qualifying sources are read, or after the Methods and Results of at most 40 candidate full texts, whichever comes first. No widening into a pool.

## Routes (all keyless, no e-mail, no personal detail to any service, no browser-header spoofing; a challenge page is a stop for that route, recorded)
- R1 PubMed (E-utilities esearch through the PubMed tool) strings such as: (HCN OR "h-current" OR Ih OR ZD7288) AND "input resistance" AND ("layer 2/3" OR "layer II/III") AND (juvenile OR postnatal OR development); read the hit count first, narrow if more than a few hundred.
- R2 Europe PMC REST search with the same grouped strings, and full text via Europe PMC fullTextXML or PMC where open; bioRxiv open copies.
- R3 citation graph: OpenAlex (public, no key; year-sliced if cursor paging fails) and Europe PMC citations for the seeds below.
- Full text from PMC / Europe PMC / bioRxiv open copies only; paywalled items go to a supply list, not counted as read.

## Seeds named before use (the first-pass Ih developmental / L2/3 Ih papers found by R1/R2 will be added in a dated addendum to this file BEFORE their citation lists are pulled)
- Kalmbach et al. 2018, Neuron, "h-channels contribute to divergent intrinsic membrane properties of supragranular pyramidal neurons in human versus mouse cerebral cortex" (mouse L2/3, ZD7288; age likely adult - to be checked, near-miss if so).
- Nolan et al. 2003, Cell, HCN1 knockout (neocortical L5/hippocampal; layer likely not L2/3 - checked as a source of citing papers).
- Fucke 2008 heiDOK thesis (in hand; OpenAlex W2567363407, cited-by count 0 at the earlier package).
No seed is assumed qualifying; each is read or rejected on its text.

## Addendum 1 (written 2026-11-21 after the first-pass Europe PMC strings, BEFORE any citation list was pulled)
First pass (Europe PMC TITLE_ABS strings; PubMed tool strings with "layer 2/3" returned 0 hits twice and are recorded in SEARCH_RECORD.md) surfaced these Ih / L2/3 / development papers. They are added as citation-graph seeds and, where open, as candidates for reading:
- Kalmbach 2018 Neuron (PMID 30392798) - already named above.
- "Cell-Type Specific Development of the Hyperpolarization-Activated Current, Ih, in Prefrontal Cortical Neurons" (Front Synaptic Neurosci 2018, PMID 29867437).
- "Resonance properties of different neuronal populations in the immature mouse neocortex" (Eur J Neurosci 2012, PMID 22748148).
- "HCN channels reveal conserved and divergent physiology in supragranular pyramidal neurons in primate species" (Commun Biol 2026, PMID 41559478; preprint PPR1072121).
- "Input-specific gating of NMDA amplification via HCN channels in mouse L2/3 pyramidal neurons" (preprint PPR730965).
- "Layer- and subregion-specific differences in the neurophysiological properties of rat medial prefrontal cortex" (PMID 28978762).
- "Interlaminar differences of intrinsic properties of pyramidal neurons in the auditory cortex of mice" (PMID 18775844).
- "Selective and brain-penetrant HCN1 inhibitors..." (Cell Chem Biol 2024, PMID 38042151).
Each is judged on its text against the FOUND rules; being a seed or a first-pass hit implies nothing about qualification.
