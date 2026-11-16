# FATE TABLE — round 1, 24 judged items, held-data pre-tests (SCI, 2026-11-16)

Assigned by SCI (Scientist session) at the request of ADV; arm taken from the IT key on main. Mechanism matching only; no dose, schedule, route or recommendation. Reference genotype class only. Machine-readable twin: `FATE_TABLE.tsv`, `FATE_COUNTS.tsv`.

**Categories.** R = rejecting observation met (the observation the author named as falsifying is present in held data). C = counter-signal (held data point away from the hypothesis but do not meet its own stated rejection). N = consistent / not rejected (a test could have rejected it and did not). P = partially supported (one half is supported, the other is not testable or fails). U = untestable by held data (no held table can discriminate).

**Labels.** *independent* = the data used were not what shaped the hypothesis. *consistency only* = the data (or the scan that produced them) were known to the author, so passing is not a test.

## Counts per arm

| arm | n | R | C | N | P | U |
|---|---|---|---|---|---|---|
| ADV | 5 | 2 | 0 | 0 | 1 | 2 |
| HE | 4 | 0 | 0 | 3 | 1 | 0 |
| IT | 5 | 0 | 0 | 2 | 1 | 2 |
| SCI | 5 | 0 | 2 | 0 | 1 | 2 |
| baseline | 5 | 1 | 1 | 0 | 2 | 1 |
| all | 24 | 3 | 3 | 5 | 6 | 7 |

Independence of the pre-tests: baseline 5 of 5 independent; HE 4 of 4; ADV 4 of 5 (J03 consistency only); IT 4 of 5 (J12 consistency only); SCI 3 of 5 (J06 and J17 consistency only, and all five pre-tests of SCI's own items were run by SCI).

## Items

| id | arm | item | fate | basis | label |
|---|---|---|---|---|---|
| J01 | SCI | HSCI-2 | U | no held GABA-A drug arm in any Wwox slice; T-type transcripts disagree between laboratories (Cacna1g down in neuron-deletion hippocampus N, up in P47T PFC); not rejected | independent |
| J02 | HE | H-HE-4 | P | compartment premise: Gabrg2 neuronal (5-fold at P17), NR3C1 only 2-fold astrocyte-like; the endpoint half needs A1 children that do not exist | independent |
| J03 | ADV | H-ADV-3 | P | rejecting observation NOT met: Mbp still -36% within mature-oligodendrocyte nuclei after composition; counter-signal: myelin-gene loss is smaller in neocortex (bursts) than hippocampus; PV axons unreachable | consistency only |
| J04 | baseline | H-B3 | R | organoid: GRIN2A (+1.11 v projected -1.66) and KCC2 (+0.73 v -0.14) move opposite to the calibration projection; NKCC1 flat; composite rests on SNAP25 and five lines | independent |
| J05 | SCI | HSCI-3 | U | no burst-against-current-removed series is held; WO-11's 14% (0-34) is a wild-type evoked fraction at one concentration | independent |
| J06 | SCI | HSCI-4 | P | Fos, Arc, Npas4, Egr1 lower in neuron-like nuclei (Fos 3.05 to 1.40 CPM; Arc 9.40 to 4.68) and in bulk neuron-deletion tables, absent in the independent P47T line; shaped by the scan that serves as its test | consistency only |
| J07 | HE | H-HE-2 | N | GAT-3 16-fold (P7 classes) and 7-fold (P17 nuclei) astrocytic, GAT-1 3.3- and 5-fold; Abat shared; functional claim untested | independent |
| J08 | baseline | H-B4 | P | astrocyte-like nuclei: Atp1a2 -32%, Aqp4 -49%, Gja1 -43% (K+ buffering signature), Kir4.1 unchanged, glutamate transporters HIGHER (counter-signal for the glutamate half); one pool | independent |
| J09 | ADV | H-ADV-4 | R | mTORC1 signature absent in the organoid (panel median -0.11, p 0.21) and in the neuron-deletion tables (targets mostly down); present only in P47T (hallmark GSEA NES 1.5-2.1, IT12 reimplementation) | independent |
| J10 | ADV | H-ADV-5 | U | no held curve pair: every held WWOX pharmacology is single-level | independent |
| J11 | baseline | H-B1 | P | interval and duration are held; carbenoxolone dissociates (0.84 to 0.03 bursts/min, duration 0.66 to 0.54 s, 13 bursts) but is not T-type specific; the sustainer half has no partial data (d-APV abolished) | independent |
| J12 | IT | HIT-1 | U | development unchanged in 6 of 6 both-endpoint children and imaging abnormal in 6 of 6: no variance | consistency only |
| J13 | IT | HIT-5 | U | development unchanged in 6 of 6: no association can be computed | independent |
| J14 | HE | H-HE-1 | N | P17 neuron-like nuclei ratios to Snap25 are 2.6 to 15 times the P7 ratios, so HE's change-my-mind condition is not met; whole-cell against nuclear RNA, assay-confounded; no within-assay table | independent |
| J15 | ADV | H-ADV-2 | U | no coherent metabolic transcript signature across lines; KATP subunits mildly lower; a genotype-by-substrate interaction is functional | independent |
| J16 | HE | H-HE-3 | N | valproate sign is real in the held LINCS table (4 of 4 neuron-like negative) but not distinctive: 18% of neuron-like signatures are at or below -1.05, lamotrigine as negative, carbamazepine positive; no second held LINCS context | independent |
| J17 | SCI | HSCI-5 | C | recombination artefact explanation of the spared hippocampus rejected (Wwox -85% hippocampus v -68% cortex); Npy up in two laboratories but Npy1r, Npy2r, Npy5r DOWN in both (nuclei -53 to -69%; P47T Npy2r -0.89 FDR 0.047), no regional asymmetry | consistency only |
| J18 | baseline | H-B5 | U | per-slice excised fraction is not held; pool level: Wwox-positive nuclei 32.0% to 4.8% (neuron-like 34.0% to 5.4%), astrocyte-like also fall (28.1% to 3.3%) | independent |
| J19 | SCI | HSCI-1 | C | NKCC1 transcript lower (neuron-like nuclei 59.1 to 38.9 CPM; P47T -0.33 to -0.36), KCC2 unchanged: away from a loading state; transport function not measured | independent |
| J20 | IT | HIT-3 | P | pooled confound visible: add-on rows improved 13 of 13 against tried 12 of 25 (non-overlapping Wilson intervals); the within-class test cannot be run at these n | independent |
| J21 | baseline | H-B2 | C | transcript-level counter-signal to a high GluN2B share: Grin2b down 116 to 33 TPM in the S-deletion hippocampus, P47T Grin2b -0.10 to +0.02 (ns); the function test is WO-10 | independent |
| J22 | IT | HIT-2 | N | two children consistent (spasms resolved on vigabatrin, later focal types improved on levetiracetam); the rejecting case is not found; order confounds | independent |
| J23 | ADV | H-ADV-1 | R | Erbb4 -13 to -16% in interneuron-like nuclei, unchanged detection, unchanged in P47T: rejecting observation met at transcript level; signalling untested | independent |
| J24 | IT | HIT-4 | N | vigabatrin 'resolved' 4 of 9 (0.19-0.73) inside the published cessation range 36 to 54%; rejecting observation not met | independent |

## Limits (read before comparing arms)

- n is 4 to 6 per arm: a one-item difference is a 20-25 point swing; none of these counts is a rate.
- Categories are my assignments from my own pre-tests; no second reader has re-assigned them. The category boundaries C v N and P v U are judgement calls and the basis column is where to dispute them.
- Held data are transcripts (one pool per arm for nuclei, 2-5 animals or lines elsewhere); transcript is not function, so R means the transcript-level rejecting observation was met, not that the mechanism is excluded.
- U is not a failure of the hypothesis: it marks where a new measurement (the experiment brief) is the only test. It is the largest category (7 of 24), the same size as the whole of R plus C (6).
- Own-arm bias: my five items carry two C and no R; I tested them most carefully, so the arm that I wrote is the one most exposed to rejection. Read the SCI row with that in mind.
- This is the held-data fate, not the judge's metric; the two can and do differ (e.g. J11, the baseline survivor, is P here).

## Update 2026-11-16 (round 2): arm B row (IT's H-C1 to H-C5, frozen de2dd121a)

Same categories and labels; pre-tests in `ARMB_HYPOTHESES_PRETEST_SCI.md` (`armb_pretests.py`, `armb_pretest_output/`); rows `R2-C1` to `R2-C5` appended to `FATE_TABLE.tsv`, row "arm B" appended to `FATE_COUNTS.tsv` (the "all" row stays the 24 round-1 items). All five pre-tests are independent of the hypothesis (the delegate opened none of the tables).

| arm | n | R | C | N | P | U |
|---|---|---|---|---|---|---|
| arm B (repository knowledge, no perspective instruction) | 5 | 0 | 0 | 1 | 1 | 3 |

H-C1 U, H-C2 U, H-C3 P, H-C4 U, H-C5 N. Against round 1: the baseline A row was [1,1,0,2,1] and the authors' rows add to [R 2, C 2, N 5, P 4, U 6] over 19 items. Arm B has no rejection and no counter-signal, but three of five are U (60%), against 6 of 19 (32%) for the authors and 1 of 5 for baseline A: the held tables reach arm B's mechanisms less often, which is a statement about the tables, not about the hypotheses. Read with the limits above; n is 5.

Second read wanted for: H-C5 (N or U: a presence condition passed is a weak test; same biology as J23, where the same numbers gave R because ADV named a transcript level), H-C3 (P or C), H-C1 (U or P).
