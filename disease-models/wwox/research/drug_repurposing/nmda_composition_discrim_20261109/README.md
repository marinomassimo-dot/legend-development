# INV-05 narrow comparison — how much NMDAR current can a GluN2B NAM remove, and what that does to the NAM-versus-d-APV design (2026-11-09)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. One package, one producer, one independent blind verifier, one recheck of the corrections. Task record `ledger/tasks/orchestrator/ORCH-IT40INV05-20261109.json`. Built on `ampa_nmda_discrim_20261108/` (BH2, matrix rows M04–M06, experiment BE2); nothing there is changed here.

## Decision this changes (labels: DATO / INFERENZA / IPOTESI)

* **The pair is d-APV plus ONE ifenprodil-site GluN2B NAM, compared only up to the NAM's measured ceiling.** DATO (recombinant): the ifenprodil-site NAMs share one ceiling on GluN1/GluN2A/GluN2B triheteromers: ifenprodil 32 percent, CP-101,606 29 percent, radiprodil 45 percent (rat), against 88, 89 and 82 percent on GluN2B diheteromers; 300 nM Zn2+ lifts the triheteromer ceiling to 50 and 58 percent. INFERENZA: the "two unrelated NAMs" of the module are unrelated in chemotype, not in site or in ceiling, so a second NAM controls off-target chemistry only; it does not separate a diheteromer pool from an insensitive triheteromer pool. One named NAM is enough for the design; the second is optional.
* **If d-APV needs more than the NAM's removable share to abolish the bursts, the NAM arm cannot reach the threshold.** That bounds the comparison, it does not fail it: curves can be compared over the range both drugs reach. A plateau at the ceiling with the burst intact is unresolved (GluN2A pool, insensitive triheteromers or total-gain threshold above the ceiling), not support for total gain; this corrects the draft wording the audit caught.
* **A left shift of the NAM curve is not by itself a composition result** on an evoked-EPSC axis (synaptic against extrasynaptic or burst-pool differences); d-APV is surmountable, so its axis is the less trustworthy one. The percent removed must be measured at the burst, not at the evoked EPSC (new measurement M-N8).
* **The three-shares solution (NAM plus TCN-201) is fragile** (TCN-201 91 percent on GluN2A diheteromers, 72 percent on triheteromers, none on GluN2B; potency set by glycine, 3 µM in the source; the system is near-collinear: by INFERENZA arithmetic on the recombinant maxima its determinant is about 0.12 and its condition number about 32, so an error of 0.05 in a removed fraction moves a share by about 0.1 to 0.3; the maxima are low-glycine values and tonic Zn2+ moves the NAM coefficient from 0.32 to 0.50). The GluN2A arm can be dropped if the question is total gain against the NAM-sensitive part.
* **Conditional hypothesis generation is not blocked** (the IT39 wording "three measurements before any compound" concerned reading a specific experiment): IT40 can state conditional hypotheses of the form "if the burst-abolishing threshold x lies below the NAM's measured removable share, a left-shifted curve would favour GluN2B weight", with the measurement that closes each condition. None of these shows benefit.
* Nothing changes a rank, a card verdict or a work order. No new molecule was named (checked: none emerged from the reasoning).

## Status of the deliverables (nothing applied to a consumer)

| Layer | State |
|---|---|
| Sources newly read, with receipts | 5 staged in `research/receipt_staging/it40inv05/`, all pass `staged_receipt_check.py --check-doi`, none recorded: 24607230 Hansen 2014 (partial full text; Results, Discussion, Tables 1–2, Figs 2–3 viewed), 26185009 Mierau 2016 (partial; Methods, Results, Tables 1–2, Fig 4), 30946007 Koster 2019 (partial; NMDAR-EPSC Results, Fig 3), 7901753 Williams 1993 and 11182088 Philpot 2001 (abstract only) |
| Reused, no new receipt | 9400004 Fischer 1997 (abstract only, earlier receipt); 40994429 radiprodil Table 1 re-read for the species split (covered by the staged `-61` receipt of the IT39 B package) |
| Not reached | full texts of Fischer 1997, Williams 1993, Philpot 2001 (publisher bot check, not retried, no open copy); Hansen supplement (no object in the open-data bucket); bodies of 39406518 and 21789901 (listed as candidates); Stroebel and Tovar triheteromer-share papers (outside the brief) |
| Verifier (first pass) | 12 propositions: 10 supported, 2 partly (D10 species mix, D12 perimeter), 0 not supported; 22 evidence rows, 2 defective in content; 11 corrections, all applied; recheck: one number (radiprodil 91 vs 45, comparison.tsv) and four stale wordings were still open and were fixed by the Orchestrator; the closing pass (`verify/audit.md`, "Closing pass") confirmed the number and the wordings and added the corrections below |
| Delivered tables | `output/decisive.tsv` (12), `output/comparison.tsv` (5 hypotheses), `output/new_measurements.tsv` (12), `output/evidence.tsv` (24), `output/figure_notes.tsv`, `output/queries.tsv` (15) |
| Proposals | `consumer_delta.md`: 9 rows; applied: 0 |

## The compact comparison (full cells: `output/comparison.tsv`)

| Hypothesis | Action and probe | Strengthened by | Weakened by | Unresolved when | Public sources suffice? |
|---|---|---|---|---|---|
| H_total_gain | d-APV titrated against the percent of isolated NMDAR EPSC removed (reference curve; competitive, surmountable, mechanism carried) | sharp d-APV threshold x measured first (a NAM curve coincident with d-APV only over a range shorter than x is unresolved, not support) | burst persists at near-complete removal | NAM stops below x (fits several hypotheses) | no (M-N1, M-N7, M-N8) |
| H_GluN2B | one ifenprodil-site NAM at saturating exposure, matched percent removed | curve left of d-APV over the range it reaches, EPSC fraction measured | curve coincident with d-APV | plateau below abolition (needs the TCN-201 arm) | partly: recombinant ceilings read; native fraction in this preparation not |
| H_GluN2A | TCN-201 at two measured co-agonist levels with glycine alone | effect at low, not at surmounting, co-agonist | no effect or equal effect at both levels | partial fall (diheteromer or triheteromer) | no (M-N4) |
| H_general_drive | AMPA antagonist and d-APV at matched charge on two metrics | coincident curves | NAM or d-APV acts at smaller charge removed | metrics order differently | no; antagonist identity unresolved (M-N5) |
| H_state | graded bath Mg2+, K+ (not a drug) | NAM-d-APV relation unchanged across levels | NAM effect only at low Mg2+ or high K+ | unequal shifts | no (M-N6) |

## What public sources resolve, and what needs a new experiment

Resolved from public sources (recombinant, oocytes, rat cDNA; partial full text): selectivity and incomplete inhibition of ifenprodil and CP-101,606, the Zn2+ dependence of the triheteromer ceiling, the radiprodil species split, TCN-201 maxima. One native bound from another preparation (mouse visual cortex layer II/III, P15, room temperature; Table 2 of 26185009: NMDAR/AMPAR ratio 1.18 to 0.83 under 3 µM ifenprodil, about 30 percent, roughly plus or minus 10 percentage points, different cell groups, late-time ratio affected by decay shortening 116 to 76 ms); at P30 and P45 the fall was smaller and not significant. A second native datum (26185009 and 30946007, P42, decay only) gives no amplitude.

**Not resolvable from literature, to be measured in the Wwox slice** (`output/new_measurements.tsv`): the isolated NMDAR EPSC and the d-APV percent-removed series with the burst-abolishing threshold x (M-N1, M-N7); the NAM-removable fraction with and without a Zn2+ chelator at plateau, at slice temperature and pH, with equilibration time and a vehicle arm (M-N2, M-N10, M-N11); the NMDAR component of the burst itself (M-N8); slice glycine or D-serine for both the NAM and TCN-201 arms (M-N4, M-N9); a verified AMPA-antagonist block and its primary selectivity paper (M-N5); recording Mg2+, K+, Zn2+, temperature and pH as measured values with a second Mg2+/K+ level (M-N6); a d-APV shift against raised glutamate (M-N12). No other literature stands in for these.

## Counter-evidence and limits

* The native bound (about 30 percent) is one other preparation, one region, one age, room temperature, 3 µM ifenprodil pre-incubated for 40 minutes or more; it is not the ceiling for the Wwox cells and is not used as one.
* The Ro 25-6981 numbers (9 nM against 52 µM) remain an abstract; its maximum inhibition and assay conditions are unknown. Williams and Fischer abstracts use "activity dependent" in ways that may differ in definition; not called a disagreement without the full texts.
* A drug response in the burst slice would not show that the target is altered in Wwox.
* Absence (D12): no isolated-EPSC NAM fraction for non-visual mouse layer II/III at P13–P17 found by a title/abstract screen of the first 12–15 hits per query, with the verifier's re-runs (114, 113, 95, 4 and 0 hits); Methods of plasticity papers were not searched. Two candidates are listed, not read: 39406518 (mouse somatosensory L2/3, P13–P21, GluN2B-dependent t-LTD) and 21789901 (rat visual cortex L2/3, 12–15 days, Ro 25-6981 and ifenprodil block LTD).

## Novelty

* `new_to_legend`: the composition-dependent, Zn2+-dependent NAM ceiling as a design constraint, and the shared ceiling of three ifenprodil-site compounds (the module held the 45 percent triheteromer figure for radiprodil only and "incomplete, agonist-level dependent" as a note). Literature novelty: not assessed.
* `already_in_legend`: matched-current design (X2 of `nmda_inv05_20261107`), d-APV as reference, TCN-201 co-agonist dependence, the carbenoxolone and AMPA questions (not reopened).
* No new molecule.

## Queries run

15 rows in `output/queries.tsv` (PubMed tool, Europe PMC REST, publisher pages recorded as unreachable and not retried), including the verifier's re-run strings and hit counts.
