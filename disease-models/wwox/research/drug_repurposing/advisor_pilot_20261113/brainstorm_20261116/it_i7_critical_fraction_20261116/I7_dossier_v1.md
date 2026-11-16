# I7 Critical NMDAR fraction and the age window: dossier v1 (IT; non-canonical; hypothesis, not finding; not medical advice)

Written for: the team (SCI, HE, ADV) and, later, a laboratory. Reference genotype class only. Mechanism level only: no dose, no recommendation; labels are classes. Status: ADVANCE, depth: model. Labels: KNOWN (source) / HELD-DATA / ASSUMED / INFERRED.

**Answer first.** The held facts already contain a sharp, checkable prediction that nobody drew: d-APV removes the bursts (KNOWN, INV-05 item 1), but the GluN2B-sensitive share of the NMDAR current is only 14% at P13-P15 in intact wild-type barrel cortex against 53% at P6-P8 (KNOWN, Mierau 2004, wild type, evoked L4-to-L2/3 EPSC, room temperature, 2 mM Mg). If bursts need a critical fraction f_c of the NMDAR current, a GluN2B negative allosteric modulator can abolish them in the P13-P17 window only when f_c is above 0.86 or when the knockout share is larger than the wild-type value. The experiment is therefore not "does a NAM work" but "what is the knockout share at the age of the bursts, and what is f_c": two numbers, one cell type, one titration.

## D1 Chain
1. Wwox loss in cortical neurons gives bursts at P13-P17 in slices (KNOWN, neuron-knockout paper; held thread).
2. Bursts need NMDAR activity: d-APV removes them (KNOWN, INV-05 item 1, prior complete read).
3. d-APV is a total block; it does not say how much current must remain (INFERRED, INV-05 note: "fixes dependence only").
4. A burst needs the NMDAR current to stay above a fraction f_c of its untreated value (ASSUMED; the null model of a regenerative event).
5. The ifenprodil-sensitive share of the NMDAR EPSC is 53% at P6-P8, 14% at P13-P15 intact, 49% when deprived (KNOWN, wild type only; Mierau 2004 as held in the T11 file). Knockout share: not held.
6. A drug removing fraction r of the current abolishes bursts iff r > 1 - f_c; a NAM's r is bounded by e x share, a pore blocker's r is set by titration (INFERRED from 4 and 5).

## D2 Why non-obvious
The standard reading asks "is GluN2B the carrier of the lesion" and ranks NAMs by that. This reading drops subunit identity as the question and asks for a margin: how much of the current the burst can lose. It makes the age of the experiment part of the hypothesis, so a pooled "NAM works or not" across ages averages two regimes.

## D3 Consequences, with a surprising one
* Cell: knockout isolated NMDAR EPSC at P13-P17 with an ifenprodil-type arm: share s_KO (measured in the same neurons as the burst readout).
* Slice: burst incidence and duration against matched fractional current reduction for a titrated pore blocker and a NAM (two unrelated NAMs): the curves cross at f_c if the model holds; a NAM curve that stops at a plateau (max r = e x s) with bursts still present is the signature.
* Animal / patient: a GluN2B-directed class should act EARLY (spasm window, high share) and fade, while a total reduction acts at any age but with a narrow margin to physiology (INFERRED).
* **Surprising prediction.** In the P13-P17 window a saturating NAM leaves bursts essentially intact (plateau at about 14% current removal) even though d-APV abolishes them, unless the knockout share is raised. Few would expect "a NMDAR-dependent phenomenon that a GluN2B NAM cannot touch". If instead the NAM abolishes bursts at P13-P17, then s_KO is much larger than 0.14 (a knockout composition change, an independent finding) or f_c is above 0.86.

## D4 Model
`critical_fraction_model.py` (deterministic, no random numbers; `--help` prints usage): table of f_c against share per age window and the needed s_KO. A hypothesis generator; it contains no data from the knockout.

## D5 Experiments
(a) No new data: held tables contain wild-type shares only (Mierau values in the T11 file); no knockout ifenprodil value exists in the held tables (checked: IT47 baseline arm pre-test); so (a) gives the model table and nothing more. Honest limit: "cannot be rejected on held data" -> design the slice experiment.
(b) One slice experiment (can ride on WO-10/X1 and X2 of INV-05): knockout and control, P6-P8 and P13-P17 groups (the early group needs the burst readout at an age where bursts may not occur: if no bursts at P6-P8 the early arm gives the share only). Per neuron: ifenprodil-sensitive fraction of the isolated NMDAR EPSC; per slice: burst incidence against matched current reduction by d-APV titration versus NAM titration. Outcomes: NAM plateau below abolition at P13-P17 with d-APV abolishing = model supported, f_c above the plateau; NAM abolishes with s_KO about 0.14 = f_c above 0.86 (bursts need nearly all the current); NAM abolishes with s_KO much larger = composition change.
(c) Clinical-observational: age at starting any NMDAR-active agent and its stated response in the held case series (see I2 table: probably zero children with such agents; then the design is a prospective registry of spasm-window versus later-window response, counts only).

## D6 Intervention logic (labels; no dose)
Link 4-6: GluN2B NAMs (labels: radiprodil, ifenprodil-type tools) act early; pore blockers (label: memantine, ketamine-type) act on r directly with a narrow margin; glycine-site agents (see I11/H-C1) shift the effective current without changing receptor number; agents outside the antiseizure set: none new here. Aggravation counterpart: an NMDAR potentiator or a co-agonist raiser would be expected to raise bursts (INFERRED). BLOCK-1: tools only and not run (ADMET-AI, medchem, RDKit absent in this deployment; flags from general knowledge unconfirmed).

## D7 Combination
With I2: the early spasm window is the high-share window; I2's per-child table asks whether spasm-semiology response is different. With I1 (SCI): f_c is the NMDAR-sustainer's parameter (the duration stage): a NAM should shorten duration at P6-P8 and not at P13-P17. With I11: a co-agonist change moves r without moving the share (the NAM plateau is unaffected, the pore-block curve shifts). Contradiction to settle: INV-05 radiprodil result in a GluN2A gain-of-function model shows a GluN2B lever can work where the lesion is elsewhere (KNOWN abstract), which is compatible with a high-share window.

## D8 Stronger / killed
Stronger: knockout share measured; a burst-incidence curve against matched reduction. Killed by a test: a NAM at saturating level abolishes bursts at P13-P17 while the knockout share is about 0.14 and the pore-block curve shows f_c below 0.86 (internally inconsistent with the model: then the burst has a GluN2B-specific component beyond current share, and the model is rejected, not the hypothesis of NMDAR dependence).

## D9 Cheapest next step with no literature
Run the model table (done), fix the two numbers to be measured (s_KO, f_c) into the INV-05 experiment sheet as a dated Update; owner IT writes the Update now; SCI reads whether the existing WO-10 design already contains the ifenprodil arm at P13-P17.
