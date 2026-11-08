# Package B: separating AMPA, NMDAR composition, general excitatory drive and carbenoxolone effects (producer an-b, 2026-11-08; revised after the independent audit)

Not medical advice; no dose, schedule or route; reference genotype class only. Nothing outside this folder was edited. Receipts (suffix 61, and corrections with suffix 62) are staged in `receipts/`, validated, not recorded. The independent audit is `../verify/audit.md`; its corrections are applied in this folder.

## Answer first (10 labelled lines)

1. DATO: in the Synapsin-Cre Wwox knockout neocortical slices (P13-P17) bursts need NMDAR activity (d-APV 50 uM, 51 bursts, 5 slices, 3 animals, reversible), but the paper contains no AMPA/kainate antagonist, no GluN2 subunit drug, no gap-junction drug other than carbenoxolone, and states only the incubation ACSF (1.3 mM Mg2+, 3.5 mM K+); the recording Mg2+ is not stated.
2. DATO and INFERENZA: d-APV abolishes the spontaneous bursts. For the evoked delayed response the figure shows about 0.4 of baseline with a washout overshoot to about 1.3, but the amplitude metric has a floor (wild type reads about 0.115 mV at the same latency), so against the floor about 20 percent of the delayed component remains; that residual is not evidence of incomplete block or threshold behaviour.
3. INFERENZA: the knockout mEPSC shift to larger events at -70 mV with a decay of about 5 ms is the kinetic signature of an AMPA-type quantum; pooled-event KS p values are inflated and are not confirmation. AMPA dependence of the burst is untested (BH1), and AMPA block abolishing bursts would not separate AMPA-dependent drive from NMDAR-regenerative drive (loss of Mg2+ relief); only persistence under a verified block is informative.
4. INFERENZA: d-APV abolition cannot separate AMPA-dependent drive, GluN2B- or GluN2A-containing NMDAR drive, general loss of drive, or a depolarisation plus Mg2+-relief state. `prediction_matrix.tsv` shows which arm separates which pair. The matched-effect arm (M08) is necessary but not sufficient: a matched percent depends on the metric, so it needs two metrics and a receptor-agnostic release-reducing control.
5. DATO: the carbenoxolone burst fall is not assignable to gap junctions. In the mouse hippocampal culture paper 100 uM reduced the AMPA EPSC to 63 percent and the NMDA EPSC to 69 percent (presynaptic), the IPSC to about 50 percent (fully reversible), broadened spikes and lowered input resistance; the EPSC reduction recovered incompletely. Direct NMDAR channel block is neither shown nor excluded (the AMPA-only glutamate test ran with NMDAR blocked). Madry's rat CA1 result is low-powered (P12, carbenoxolone alone: 22 percent lower, n = 6 against 14, P = 0.46; P20 only with La3+) and reads a reversed-uptake ischaemic glutamate current, so it neither contradicts the culture result nor excludes an NMDAR block. BH3 is close to a withdrawal of the gap-junction attribution.
6. DATO: the paper's text, legends, Table S1 and figures disagree on baseline frequency (2.29 against 0.84 per minute for the same 119 bursts; 2.29 is exactly 60/26.2 s and the Fig 1D inter-burst histogram looks more compatible with 0.84), carbenoxolone n (36/4 against 13/6), brilliant blue FCF n (73/6 against 25/6), carbenoxolone amplitude, S1 burst counts, S3 latency n and Fig 4 S-CTL cell count. Drug groups are compared with one pooled baseline by unpaired tests, so no printed drug percent change is a within-slice effect. Only direction and non-recovery (carbenoxolone), "no reduction" (brilliant blue FCF), d-APV abolition and genotype incidence (36/42, 4/23, 0/11) are used.
7. INFERENZA: radiprodil is GluN2B-selective in oocytes (the selectivity sentence cites an unread supplementary figure) with incomplete inhibition of triheteromers (45 percent maximum) and very slow washout; its activity dependence was not tested and its slice Mg2+ is stated two ways in its source. TCN-201 is GluN2A-selective only in recombinant receptors, potency set by glycine, maximum inhibition 73-81 percent in its own table. Perampanel is a noncompetitive AMPA/kainate antagonist with slow kinetics in culture; its earlier text-versus-figure potency conflict is withdrawn as a probable axis-label misread (tick-based reading about 0.45 and 1 uM agrees with Table 1). A tool arm must verify block by the evoked response and fix order and washout.
8. DATO: NBQX and GYKI 52466 have no primary mechanism source in this reading (not read or not open access; the literature exists); an AMPA arm that uses them is "use-only, mechanism not read", and the decision rests on the measurement, not the tool.
9. IPOTESI: three comparisons are carried and each is PARTLY supported by the audit (BH1 AMPA dependence; BH2 NMDAR composition at matched current; BH3 carbenoxolone attribution, near withdrawal of the gap-junction half). None is a drug recommendation; none changes a rank.
10. NEW MEASUREMENTS (experimental needs; other literature is no substitute): recording Mg2+ and K+ as measured bath values with temperature and blockers present; a within-slice paired design; whether the burst survives a verified AMPA block; a receptor-agnostic release-reducing control on at least two metrics; the isolated NMDAR EPSC and matched-current curves with the NAM-sensitive fraction; the slice co-agonist level before TCN-201; carbenoxolone's effect on EPSCs, spike width and coupling in these slices; Panx1 engagement for brilliant blue FCF; a floor control for the delayed-response metric; a GABA-A arm with an evoked IPSC (alternative AB06; potentiator abolition alone is also predicted by H4); AMPAR/NMDAR ratio and AMPA EPSC kinetics in the knockout cells; slice equilibration time for each drug at 35 C and the temperature mismatch with the source preparations (room temperature in culture, oocytes and Hansen; 30-33 C in the radiprodil and Madry slices; 35 C in the WWOX preparation); TTX/action-potential dependence of the burst; heterozygote drug sensitivity (4 of 23 bursting slices).

## Which hypotheses survive and what each rests on

* BH1 (PARTLY): survives as a measurement question; rests on the absence of any AMPA/kainate test in the paper and on the kill condition "bursts survive a verified block". Perampanel potency caveat withdrawn; the H2 prediction under M07 corrected; kainate not separated.
* BH2 (PARTLY): survives as a design question; rests on the absence of any isolated NMDAR current, subunit, co-agonist or Mg2+ datum for the preparation. The delayed-response residual no longer supports it; M05 cannot split diheteromer from triheteromer share.
* BH3 (PARTLY, near withdrawal of the gap-junction attribution): what survives is the direction-only reading of the carbenoxolone result, the culture off-target evidence, the missing Panx1 engagement and connexin-selective test, and the measurement plan; no datum in the sources read separates the gap-junction half from the off-target explanations.

## What changed relative to the IT38 qualified state

* IT38 (inv05_nmda D08, D13, D15; inv10_seizures D05, D06) held: bursts d-APV dependent; carbenoxolone caveat; AMPA not tested; matched-current d-APV as the first comparison. Unchanged and confirmed from the full text.
* New: the evoked delayed-response residual is mostly a metric floor and is not abolition either way (D13 said "suppressed"); further text/legend/table disagreements and the pooled-baseline design of the source; the kinetic argument and its limits for an AMPA-type mEPSC; primary readings of carbenoxolone's off-target actions in culture and the low-power slice null; brilliant blue FCF selectivity in oocytes with no slice engagement check; radiprodil's triheteromer ceiling, slow washout and Mg2+ ambiguity (D15 stays unverified for activity dependence); TCN-201's glycine dependence and incomplete maximum inhibition; perampanel's mechanism and kinetics.
* Not changed: no ranking, no direction state, no target; felbamate and perampanel remain a class transfer.

## Phase 3 corrections (audit) and points of disagreement

Applied: items 1 to 10 of the coordinator's list (perampanel axis reading re-viewed and the conflict withdrawn as a probable misread; metric floor; Madry weight and P20 wording; IPSC and EPSC recovery; genetic-ablation wording; matrix M07, M08, M10 and new arms M16 to M18; further disagreements, including a re-look at the inter-burst histogram; probe details; query perimeter; replacement receipts -62 for 34634460 and 19535488; docx image numbering). My own re-view of the perampanel Fig 1D agrees with the audit by geometry (numerals about 0.8 times as far apart as ticks; six points at half-decade steps; Methods maximum 30 uM) but at my enlargement I could not read pixel positions to the audit's precision, so the reading stays INFERENZA. For the WWOX Fig 1D I could not tally 101 intervals to a median; I report what the histogram looks like and keep both baselines out of every comparison.

## Evidence (full list in `evidence.tsv`; observations in `observations.tsv`)

Primary WWOX source 34634460 (all sections except the reference list; Figs 1-6 and all four supplementary images viewed; Table S1 read). Tool papers: 19535488 (carbenoxolone, mouse hippocampal culture), 20940167 (pannexin blockers, rat CA1 slices), 23589583 (brilliant blue FCF, oocytes), 22553026 (TCN-201, recombinant), 40994429 (radiprodil, oocytes, mouse CA1 slices, mice), 25229608 (perampanel, culture), 15297615 (mefloquine, abstract only).

## Counter-evidence and transfer limits

* Heterozygotes burst (4 of 23 slices) and show intrinsic changes; HT mEPSC amplitude differs from wild type (KS): the dependence is not confined to the null and HT is not a clean intermediate comparator.
* Carbenoxolone: culture (mouse, P0-P1 origin, 6-15 DIV, room temperature) against slices (rat CA1, P12 and P20, 33 C; reversed-uptake ischaemic current); neither is the burst preparation.
* Radiprodil in vivo support is a GluN2B gain-of-function line; slice data are mouse CA1 at P17-P22; the bath concentration used (3 uM) was about 100 times the oocyte IC50.
* Perampanel and TCN-201 numbers are culture or recombinant; none is a P13-P17 neocortical datum.
* A drug response is not proof of a defect in its target; an increased mEPSC is not assumed harmful.

## Not reached

Chepkova's carbenoxolone and NMDAR paper (no open full text; abstract not read); the Cx36 mefloquine full text (reCAPTCHA page, not retried); first-hand primary papers for NBQX, GYKI 52466, felbamate, ifenprodil and Ro 25-6981 (not read; not an absence from PubMed); a kainate-selective tool and its mechanism paper; the subunit-pharmacology limitation paper (PMC record outside the bucket, not opened); figures of 19535488, 22553026 and 40994429 (captions only; the bucket has none for the latter two); Supplementary Fig 1B and the supplement of 40994429; the WWOX reference list; any slice measurement of Mg2+, isolated NMDAR EPSC, co-agonist level, Panx1 engagement, coupling, GABA-A manipulation or kainate separation.

## Queries

`queries.tsv` QB01 to QB24 (claims and ledger lookups, bucket and PMC routes, PubMed searches returning identifiers only, conversions, local text searches, the three WWOX perimeter strings QB20-QB22, and the re-view of figures QB24).

## Cap accounting

Eight sources newly read or re-read: the WWOX paper (re-read with a new question; prior receipt FTR-20261019-34634460-01) and seven others (six at partial full text, one at abstract). Phases 2 and 3 added no source (the two optional AMPA-mechanism reads were unreachable: no open full text for four candidates, QB18). Cap of 8 not exceeded; no overrun. Receipts: eight suffix-61 receipts and two suffix-62 correction receipts, all validated.

## Recording the receipts

The two `-62` correction receipts name the staged `-61` receipts of the same studies as prior: record each `-61` before its `-62` (or record the `-62` alone), never in parallel.

## Files

`observations.tsv`, `alternatives.tsv`, `probes.tsv`, `figure_notes.tsv`, `evidence.tsv`, `queries.tsv`, `prediction_matrix.tsv`, `hypotheses.tsv`, `experiments.tsv`, `held_not_used.tsv`, `engine_consumption.md`, `consumer_delta.md`, `receipts/`.
