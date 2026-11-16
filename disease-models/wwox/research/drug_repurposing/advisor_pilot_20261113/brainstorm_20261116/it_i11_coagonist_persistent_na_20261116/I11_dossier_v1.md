# I11 Co-agonist occupancy (H-C1) and persistent sodium current (H-C2): dossier v1 (IT; non-canonical; hypotheses; not medical advice)

Written for: the team and a laboratory. Reference genotype class only; mechanism level; no dose or recommendation. Status ADVANCE, depth chain (H-C1) and chain (H-C2). Source of both seeds: arm B of this morning (`it_arm_b_20261116/hypotheses_arm_b.md`), repository-aware reading; both were reported as having no held test.

**Answer first.** Both ideas explain "NMDAR-dependent bursts without a lost conductance or a raised receptor number" and both reduce to one paired measurement in slices already planned (WO-10, WO-17): the fractional change of the isolated NMDAR EPSC under raised and lowered co-agonist (H-C1), and the TTX-sensitive ramp current per pF between -65 and -45 mV with a persistent-preferring block (H-C2). Together they predict one surprising thing: **the same burst can be removed from two different directions, by lowering effective NMDAR drive (co-agonist scavenging) or by removing the regenerative sodium step, and the two blocks should be non-additive near threshold but additive far from it.**

## D1 Chain (two branches, one trigger-sustainer pair)
H-C1: 1 Wwox neuron loss gives bursts needing NMDAR activity (KNOWN, d-APV, INV-05). 2 The NMDAR needs glycine/D-serine at GluN1 (KNOWN, general). 3 The slice co-agonist supply and site occupancy are not measured in the thread (HELD-DATA: absent; the F04 card says "unmeasured in the slice"). 4 Wwox loss changes co-agonist supply (astrocytic D-serine, Dao, Slc7a10, Slc6a9) or occupancy (ASSUMED). 5 Same glutamate transient then gives larger isolated NMDAR current without receptor change (INFERRED).
H-C2: 1 Knockout pyramidal cells: rest 5.6 mV more depolarised, higher input resistance (KNOWN, Table 1 of the neuron paper, as read in the thread). 2 A persistent TTX-sensitive current is activated near -60 to -45 mV (KNOWN, general). 3 Its size per cell may be unchanged (ASSUMED) but the rest moves it into the active window (INFERRED). 4 It regenerates the NMDAR-triggered event into a burst (ASSUMED).

## D2 Why non-obvious
Every conductance in the thread's ladder (Ba2+, XE-991, ZD7288, K2P, KATP) is a lost hyperpolarising current. These two keep every channel unchanged in number and ask whether an unchanged element is pushed into its active window (H-C2) or whether the agonist rather than the receptor changed (H-C1).

## D3 Consequences across scales; surprising prediction
* Cell: H-C1 predicts a smaller increment under saturating co-agonist and a larger loss under scavenging in knockout; H-C2 predicts a larger TTX-sensitive ramp current fraction at the knockout rest.
* Slice: burst incidence under scavenging and under a persistent-preferring block; the two blocks combined.
* Animal/patient: H-C2 predicts sensitivity to sodium-channel agents with persistent-current preference and, together with I1/I2, that sodium-channel blockers that are non-selective can AGGRAVATE a rebound phenotype by blocking inhibitory-neuron firing while sparing the regenerative step in pyramidal cells (INFERRED; general pharmacology to be re-verified). This gives a mechanistic reading of mixed reports of sodium-channel agents in WWOX.
* **Surprising prediction.** A co-agonist scavenger and a persistent-sodium block remove bursts at fractional reductions of their targets that are SMALLER than d-APV needs, because each acts on the amplifier of an event already near threshold; and the ratio (burst removal per unit of target removal) is larger in knockout than in wild type. A burst fall steeper than the current fall in knockout only is the signature; a matched fall means a generic reduction.

## D4 Minimal model
Deterministic two-variable threshold sketch, no code shipped here (SCI's I1 model owns the dynamics; this dossier gives parameter roles): burst iff g_NMDA x (1 + a x g_NaP(V_rest)) > theta; H-C1 acts on g_NMDA (through occupancy), H-C2 on g_NaP and V_rest. Both lower the margin (theta - drive); an NMDAR blocker and a NaP blocker are two cuts into one inequality. Handed to HE's simulation harness as a request; not evidence.

## D5 Experiments
(a) No new data: a lookup of Srr, Dao, Slc6a9, Slc7a10 and the sodium-channel alpha subunits in the held class-mean RNA tables is possible but not done in this v1 (whether each symbol has a row is unchecked): RNA is not function, and a held-table difference would not reject either idea. Result of (a): none can reject; design the slice experiment.
(b) One slice experiment on the WO-10/WO-17 cells: H-C1 (co-agonist raised to saturation, then scavenged, isolated NMDAR EPSC, cell unit nested in animal); H-C2 (TTX-sensitive ramp current per pF; burst incidence under a persistent-preferring block against a matched reduction of evoked firing). Outcomes as in D3; each both-ways.
(c) Clinical-observational: for sodium-channel agents, the per-child table of I2 (exposures, semiology at exposure, worsening); a design for a clinician-researcher: record semiology and EEG pattern before starting a sodium-channel agent and the occurrence of new myoclonic or absence-like events within weeks (counts only).

## D6 Intervention logic (labels, no dose)
H-C1: glycine-site agents (labels 7-chlorokynurenic acid tool; D-cycloserine partial-agonist), the direction open. H-C2: persistent-current-preferring sodium-channel blockers (label as a class from the arm B text; none ranked). Outside the antiseizure set: co-agonist metabolism enzymes (D-amino-acid oxidase, serine racemase) as tool classes. Aggravation counterpart: raising co-agonist; non-selective sodium block in the rebound phenotype. BLOCK-1: not run (tools absent); flags from general knowledge: the glycine-site tool is not brain-penetrant by repute, the partial agonist is psychotomimetic at higher exposure (unconfirmed).

## D7 Combination
With I7: a co-agonist change moves effective r without moving the GluN2B share; the I7 table's NAM plateau is unaffected by H-C1, the pore-block curve shifts. With I1: H-C2 is a candidate for the regenerative sustainer; I1's gamma shape of the duration (about two to three stages) could include a NaP step. With I2: an aggravation cluster for sodium-channel agents in the rebound semiology would favour H-C2 as the circuit-level reading. Contradiction to settle: INV-05 treats the NAM-sensitive fraction as decisive while H-C1 says the same fraction can hide an occupancy change; only the paired measurement separates them.

## D8 Stronger / killed
Stronger: a measured co-agonist sensitivity difference or TTX ramp difference. Killed by a test: H-C1, equal increment and loss in both genotypes (arm B's own rejecting test); H-C2, a persistent-preferring block that removes knockout bursts only at a concentration lowering evoked firing and the EPSC to the same degree as a generic suppression. Not killed by absence of a held table.

## D9 Cheapest next step, no literature
Add both measurements as dated optional arms to the INV-05 experiment sheet (a line, no ranking change); SCI to say whether WO-10/WO-17 cells can carry them; HE to simulate the two-cut inequality in the I1 harness. Owner IT writes the Update.
